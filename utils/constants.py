
DEFAULT_WAIT_TIME = 10

with open('D:/credls.txt', 'r') as f:
    lines = f.read().splitlines()
LOGIN = str(lines[0])
PASSWORD = str(lines[1])

SEARCH_FOR_TEST_CASE = "inventory"
