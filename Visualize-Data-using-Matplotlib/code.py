# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Code starts here
data = pd.read_csv(path)
loan_status = data['Loan_Status'].value_counts()
loan_status.plot(kind="bar")


# --------------
#Code starts here

property_and_loan = data.groupby(['Property_Area', 'Loan_Status']).size().unstack()
plt.xlabel('Property Area')
plt.ylabel('Loan Status')
plt.xticks(rotation=45)


# --------------
#Code starts here

education_and_loan = data.groupby(['Education', 'Loan_Status']).size().unstack()
education_and_loan.plot(kind='bar', stacked=True, figsize=(15,10))
plt.xlabel('Education Status')
plt.ylabel('Loan Status')
plt.xticks(rotation=45)
plt.show()


# --------------
#Code starts here
graduate = data[data['Education'] == 'Graduate']
not_graduate = data[data['Education'] == 'Not Graduate']
graduate.plot(kind='density', label='Graduate')
not_graduate.plot(kind='density', label='Not Graduate')
#Code ends here

#For automatic legend display
plt.legend()


# --------------
#Code starts here
fig ,(ax_1,ax_2,ax_3) = plt.subplots(1,3, figsize=(20,10))
ax_1.plot(data['ApplicantIncome'], data['LoanAmount'])
ax_1.set_title('Applicant Income')
ax_1.scatter(data['ApplicantIncome'], data['LoanAmount'])

ax_2.plot(data['CoapplicantIncome'], data['LoanAmount'])
ax_2.set_title('Coapplicant Income')
ax_2.scatter(data['CoapplicantIncome'], data['LoanAmount'])

data['TotalIncome']=data['ApplicantIncome']+data['CoapplicantIncome']

ax_1.plot(data['TotalIncome'], data['LoanAmount'])
ax_1.set_title('Total Income')
ax_1.scatter(data['TotalIncome'], data['LoanAmount'])


