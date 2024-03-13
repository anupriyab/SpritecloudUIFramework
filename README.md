This project provides a comprehensive Test Automation framework for both web and API testing, leveraging Python, pytest, and Selenium WebDriver. Additionally, it incorporates Allure for reporting purposes and is seamlessly integrated into Jenkins pipelines for efficient execution of test cases. Moreover, the framework implements cross-browser testing to guarantee that UI elements are correctly displayed and function as intended across different platforms.

Testing site for Web  - UI Testing Playground.

Testing site for API -  PetSwagger


***Testing Scenarios***
I have considered common automation pitfalls found in modern web applications, such as Dynamic IDs, AJAX requests, Login functionality, User Creation, User retrieval.

1) In Web testing - Tested Handling Dynamic ID, Login to the Sample App, Handling Ajax data Scenarios

  *Handling Dynamic ID*- IDynamic IDs can cause test failures and hinder automation efforts. By testing the handling of dynamic IDs, we ensure that our tests remain stable and reliable.
  *Sample APP*- Login functionality directly impacts user experience and security. Testing login ensures that users can access the application as intended, minimizing the risk of unauthorized access or security 
    breaches.
  *Ajax Data*-AJAX data handling is critical for ensuring the responsiveness and usability of web applications. Testing AJAX scenarios helps identify and address issues related to data loading and page updates, 
   ensuring a seamless user experience.

2) In API Testing- Tested User creation and User retrieval call by username
    *User Creation* -User creation testing ensures that user registration functionality works as expected, enabling users to sign up for the application without encountering errors.
    *User retrieval* - Testing user retrieval by username ensures that user data can be retrieved efficiently, supporting various application features such as user profile display.


***Languages and Frameworks***

This project using the following languages and frameworks:

 Python as the programming language.
 PyTest as the UnitTest framework to support the test creation.
 Selenium WebDriver as the web browser automation framework using the Python binding.
 Assert as the  assertion librar.y
 Allure Report as the testing report strategy.
 Logging as the logging management strategy.


***How to execute the Script***

  pip install -r requirements.txt
  pip install --upgrade urllib3
  cd Testcases
  pytest -s -v  --alluredir="./allure_report"

***To create Report instantly:***
    allure serve . /allure-report  
