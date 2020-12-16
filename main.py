
import os
from dotenv import load_dotenv
from TemperatureReport import report

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

if __name__ == '__main__':
    userid = os.environ.get('USER_ID')
    password = os.environ.get('PASSWORD')
    result = report(userid, password)
    if result[0]:
        print(result[1])
