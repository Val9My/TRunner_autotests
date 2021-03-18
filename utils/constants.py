
DEFAULT_WAIT_TIME = 10

with open('D:/credls.txt', 'r') as f:
    lines = f.read().splitlines()
LOGIN = str(lines[0])
PASSWORD = str(lines[1])
DB_NAME = str(lines[2])
DB_USER = str(lines[3])
DB_PASSWORD = str(lines[4])
DB_HOST = str(lines[5])
DB_PORT = str(lines[6])
INV_CODE = str(lines[7])
TEMP_USER = str(lines[8])
TEMP_PASSW = str(lines[9])
TEMP_TOKEN = str(lines[10])
TEMP_ROLE = str(lines[11])

SEARCH_FOR_TEST_CASE1 = "inventory"
SEARCH_FOR_TEST_CASE2='short'
