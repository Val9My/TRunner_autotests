# TRunner_autotests
#### **Python UI autotests for TRunner tool**

- Add webdriver folder path into PATH
- Put in D:\credls.txt :

LOGIN in 1st row, and 

PASSWORD in 2nd row.

- Chrome - is a default browser. 

To run tests on Firefox type:

pytest -s -v --browser_name=firefox test_.py

- To save report in .html file add: --html=report.html

