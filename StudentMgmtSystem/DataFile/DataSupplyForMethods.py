import configparser


def get_configurations():
    config = configparser.ConfigParser()
    config.read('C:\\Users\\ag9m\\PycharmProjects\\VENV\\LearningPytest\\StudentMgmtSystem\\ConfigFile\\Properties.ini')
    return config


def post_data():
    data = {
        "first_name": "I",
        "middle_name": "Will",
        "last_name": "Win",
        "date_of_birth": "12/12/2020"
    }
    return data


def post_data_for_chaining():
    data = {
        "first_name": "surely",
        "middle_name": "I_Will",
        "last_name": "Win",
        "date_of_birth": "12/12/2020"
    }
    return data

def post_data_for_techdetails(id):
    data = {
        "id": id,
        "language": [
            "Python",
            "Pytest","SQL"
        ],
        "yearexp": "6",
        "lastused": "1",
        "st_id": id,
    }
    return data

def post_data_for_address(id):
    data = {
        "Permanent_Address": {
            "House_Number": "201",
            "City": "BLr",
            "State": "KA",
            "Country": "IND",
            "PhoneNumber": [
                {
                    "Std_Code": "0194",
                    "Home": "2421224",
                    "Mobile": "2421442"
                },
                {
                    "Std_Code": "0191",
                    "Home": "2421224",
                    "Mobile": "2421442"
                }
            ]
        },
        "Current_Address": {
            "House_Number": "201",
            "City": "BLr",
            "State": "KA",
            "Country": "IND",
            "PhoneNumber": [
                {
                    "Std_Code": "0194",
                    "Home": "2421224",
                    "Mobile": "2421442"
                },
                {
                    "Std_Code": "0191",
                    "Home": "2421224",
                    "Mobile": "2421442"
                }
            ]
        },
        "stId": id
    }
    return data
