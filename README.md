This project delivers Test Automation framework  for Web and API using python,pytest and Selenium WebDriver,Allure and executed test cases in jenkins pipeline.

Testing site for Web  - UI Testing Playground
Testing site for API -Petswagger


*Testing Scenarios*
I have considered common automation pitfalls found in modern web applications, such as dynamic IDs, AJAX requests, Login functionality 
1) In Web testing - Automated Handling Dynamic ID, Login to the Sample App, Handling Ajax data Scenarios
2) In ApI Testing-Automated User creation and User retrieval call by username

Handling Dynamic ID- ID are one of the importan attribute for testing the elements. when id are chanding dynamically, then we have to go with stable locators like text, class name .
Sample APP- Login test is main functionality to test across any web application.
Ajax data-This Test scenarios needs to be tested in modern web applications where elements may appear on the page after loading data with AJAX requests.

2) In ApI Testing-Automated User creation and User retrieval call by username


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
pip install --upgrade urllib3

cd Testcases
pytest -s -v  --alluredir="./allure_report"

To create Report instantly:
allure serve . /allure-report  
