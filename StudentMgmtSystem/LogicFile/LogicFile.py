import requests
from LearningPytest.StudentMgmtSystem.DataFile.DataSupplyForMethods import *


def add_student():
    global Id_extracted
    responsePost = requests.post(url=get_configurations()['API']['Base_Url'] + 'api/studentsDetails', json=post_data(),
                                 verify=False)
    print(responsePost.json())
    Id_extracted = responsePost.json()['id']
    # return Id_extracted


def get_student_data():
    #add_student()
    responseGet = requests.get(url=get_configurations()['API']['Base_Url'] + 'api/studentsDetails/' + str(Id_extracted),
                               verify=False)
    print(responseGet.json())

# get_student_data()
