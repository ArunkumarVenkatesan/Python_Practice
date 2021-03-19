from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, exc
from sqlalchemy.orm import scoped_session, sessionmaker
from flask_marshmallow import Marshmallow
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from models.customers import CustomerModel
from models.loan import LoanModel
from db import db
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///BankDB.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)
BankDB = SQLAlchemy(app)
ma = Marshmallow(app)

@app.before_first_request
def create_tables():
    db.create_all()

class CustomerSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = CustomerModel
class LoanSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = LoanModel
class ViewCustomerSchema(ma.SQLAlchemySchema):
    class Meta:
        model = CustomerModel
    Username=auto_field()
    Address=auto_field()
    PAN=auto_field()
    Account_type=auto_field()

class ViewLoanSchema(ma.SQLAlchemySchema):
    class Meta:
        model = LoanModel		
    Customer_id=auto_field()
    Name=auto_field()
    Loan_id=auto_field()
    Loan_amount=auto_field()
    Loan_type=auto_field()

customer_schema = CustomerSchema()
viewcustomer_schema = ViewCustomerSchema()
viewloan_schema = ViewLoanSchema()
customers_schema = CustomerSchema(many=True)
loan_schema = LoanSchema()
loans_schema = LoanSchema(many=True)

class UpdateAccountDetails(Resource):  
    def put(self, Customer_id):
        cust = CustomerModel.query.get_or_404(Customer_id)
        if 'Name' in request.json:
            cust.Name = request.json['Name']
        if 'Username' in request.json:
            cust.Username = request.json['Username']
        if 'Password' in request.json:
           cust.Password = request.json['Password']
        if 'Address' in request.json:
           cust.Address = request.json['Address']
        if 'State' in request.json:
           cust.State = request.json['State']
        if 'Country' in request.json:
           cust.Country = request.json['Country']
        if 'Email_address' in request.json:
           cust.Email_address = request.json['Email_address']   
        if 'PAN' in request.json:
           cust.PAN = request.json['PAN']
        if 'Contact_no' in request.json:
           cust.Contact_no = request.json['Contact_no']
        if 'DOB' in request.json:
           cust.DOB = request.json['DOB']
        if 'Account_type' in request.json:
           cust.Account_type = request.json['Account_type']         
        BankDB.session.commit()
        return customer_schema.dump(cust)
    
    # def delete(self, customer_id):
    #     cust = CustomerModel.query.filter_by(Customer_id=customer_id).first()
    #     if cust is None:
    #         return {"message": "Customer does not Exist in the Table."}    
    #     BankDB.session.delete(cust)
    #     # CustomerModel.query.filter_by(Customer_id=customer_id).delete()
    #     BankDB.session.commit()
    #     return f'Customer Deleted Successfully'
    @classmethod
    def delete(cls, customer_id: int):
        cust = CustomerModel.query.filter_by(Customer_id=customer_id).first()
        if cust:
            cust.delete_from_db()
            return {"message": 'Customer Deleted Successfully'}, 200

        return {"message": 'Customer Not Found'}, 404

class ViewCustomer(Resource):
    def get(self,customername):
        Cust = CustomerModel.query.filter_by(Username=customername).first_or_404(description='No Customer Exists with this Username {}. Kindly Re-check'.format(customername))
        return viewcustomer_schema.dump(Cust)
        # return customers_schema.dump(cust)

class AddCustomer(Resource):
    def get(self):
        cust = CustomerModel.query.all()
        return customers_schema.dump(cust)
    def post(self):
        result = CustomerModel.query.filter_by(Username=request.json['Username']) #db.execute("SELECT * from Customers WHERE username = :c", {"c": request.json['username']}).fetchone()
        if result:
                # result = db.query(Customer).count()
                new_cust = CustomerModel(
                    Name = request.json['Name'],
                    Username = request.json['Username'],
                    Password = request.json['Password'],
                    Address = request.json['Address'],
                    State = request.json['State'],
                    Country = request.json['Country'],
                    Email_address = request.json['Email_address'],
                    PAN = request.json['PAN'],
                    Contact_no = request.json['Contact_no'],
                    DOB = request.json['DOB'],
                    Account_type = request.json['Account_type']
                )
                BankDB.session.add(new_cust)
                BankDB.session.commit()
                return customer_schema.dump(new_cust), 201
        else:
            return f"User {request.json['Username']} already Exists in the Table."

class ApplyLoan(Resource):
    def get(self):
        loan = LoanModel.query.all()
        return loans_schema.dump(loan)
    def post(self):
        # result = db.execute("SELECT * from Loan WHERE name = :c", {"c": request.json['name']}).fetchone()
        result = LoanModel.query.filter_by(Name=request.json['Name']) #db.execute("SELECT * from Customers WHERE username = :c", {"c": request.json['username']}).fetchone()
        if result:
            # result = db.query(Customer).count()
            new_loan = LoanModel(
                Customer_id = request.json['Customer_id'],
                Name = request.json['Name'],
                Loan_type = request.json['Loan_type'],
                Loan_amount = request.json['Loan_amount'],
                Loan_date = request.json['Loan_date'],
                Rate_of_interest = request.json['Rate_of_interest'],
                Duration = request.json['Duration']
            )
            BankDB.session.add(new_loan)
            BankDB.session.commit()
            return loan_schema.dump(new_loan), 201
        else:
            return f"User {request.json['Name']} already exists in the table."

class ViewLoan(Resource):
    def get(self,loan_id):
       loan = LoanModel.query.filter_by(Loan_id=loan_id).first_or_404(description='No loan Exists with this loan Id {}. Kindly Re-check'.format(loan_id))
       return viewloan_schema.dump(loan)

api.add_resource(AddCustomer,'/addcustomer')
api.add_resource(ViewCustomer,'/viewcustomer/<customername>')
api.add_resource(UpdateAccountDetails,'/updateaccount/<int:customer_id>')    
api.add_resource(ApplyLoan,'/ApplyLoan')
api.add_resource(ViewLoan,'/GetLoanDetail/<int:loan_id>')