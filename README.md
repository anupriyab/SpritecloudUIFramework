This project delivers Test Automation framework  for Web and API using python,pytest and Selenium WebDriver,Allure.

Testing site for Web  - UI Testing Playground
Testing site for API -Petswagger


*Languages and Frameworks*

This project using the following languages and frameworks:
 Python as the programming language
 PyTest as the UnitTest framework to support the test creation
 Selenium WebDriver as the web browser automation framework using the Python binding
 Assert as the  assertion library
 Allure Report as the testing report strategy
 Log as the logging management strategy


*How to execute the Script*
pip install -r requirements.txt
cd Testcases
pytest -s -v  --alluredir="./allure_report"
