import csv


with open('C:\\Users\\jakub\\OneDrive\\Dokumenty\\pythonexercise\\python-portfolio-project-starter-files\\insurance.csv', 'r') as insurance_data:
    csv_reader = csv.reader(insurance_data)
    list_insurance = list(csv_reader)


list_insurance.pop(0)


age = []
sex = []
bmi = []
children = []
smoker = []
region = []
charges = []

for x in list_insurance:
    age.append(x[0])
    sex.append(x[1])
    bmi.append(x[2])
    children.append(x[3])
    smoker.append(x[4])
    region.append(x[5])
    charges.append(x[6])


def average_age(parameter):
    int_convert = [int(i) for i in parameter]
    avg_age = sum(int_convert) / len(parameter)
    return avg_age

avg_age = average_age(age)
# print(f'Average age of dataset is {str(round(avg_age,2))}')

def smoker_vs_nosmoker(parameter1, parameter2):
    int_convert = [float(x) for x in parameter2]
    zipped = list(zip(parameter1,int_convert))
    smoker_charges = 0
    non_smoker_charges = 0
    count_smoker = 0
    count_nonsmoker = 0
    for x,y in zipped:
        if x == 'no':
            non_smoker_charges += y
            count_nonsmoker += 1
        else:
            smoker_charges += y
            count_smoker += 1
    average_smoker = smoker_charges / count_smoker
    average_nonsmoker = non_smoker_charges / count_nonsmoker
    return average_smoker, average_nonsmoker



def majority(parameter):
    majority = [(i,parameter.count(i)) for i in set(parameter)]
    return majority

for i in list_insurance:
    print(i)