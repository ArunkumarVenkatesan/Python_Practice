from BankTest import app
import jwt
import json
import pytest_cov

test=app.test_client()
def test_addCustomer():
    response= test.post('/addcustomer', 
                             json={"Name" : "Arunkumar","Username" : "varun",
                                   "Password" : "arun@123","Address" : "Madurai",
                                   "State" : "TamilNadu","Country" : "India",
                                   "Email_address" : "arun@gmail.co,","PAN" : "Ay879T",
                                   "Contact_no" : "1234567","DOB" : "30/12/90",
                                   "Account_type" : "Savings"})

    status = response.status_code
    assert status == 201

def test_applyLoan():
    response= test.post('/ApplyLoan', 
                             json={"Customer_id":"7","Name":"Arun",
                                   "Loan_type":"Car","Loan_amount":"500000",
                                   "Loan_date":"03/15/2020","Rate_of_interest":"13",
                                   "Duration":"7"})

    status = response.status_code
    assert status == 201

def test_getLoanDetails():
    response= test.get('/GetLoanDetail/8')

    status = response.status_code
    assert status == 200

def test_viewCustomer():
    response= test.get('/viewcustomer/varun')

    status = response.status_code
    assert status == 200