# Crate a csv file
import csv

dataList=[['S.No','ParticipantName','Experience'],[1,'karthi','5 years'],
[2,'Suresh','10 Years']]

with open("pythonTestfile.csv","w") as file:
    writer = csv.writer(file,delimiter=',')
    writer.writerows(dataList)