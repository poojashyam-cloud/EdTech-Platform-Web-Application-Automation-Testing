**Automation Testing of EdTech Platform Web Application**

**Project Overview:**
* This project automates UI testing for GUVI (**_https://www.guvi.in_**), an EdTech platform, using **Selenium, Pytest,POM** and Object-Oriented Programming (OOP) principles. 
* It validates core functionalities like login, navigation, and UI elements across multiple browsers. 

**Tech Stack**
* Python
* Selenium
* PyTest

**Scope:**
* Simulate real user interactions and validate UI behavior
* Ensure cross-browser compatibility (Chrome, Firefox, Edge, Safari)
* Log results, capture screenshots, and generate HTML reports
* Maintain modular, scalable, and reusable test architecture

**Test Suite:**
* Tes_Case  Description
* TC1 Validate URL accessibility
* TC2	Verify page title
* TC3	Check Login button visibility and clickability
* TC4	Check Sign-Up button functionality
* TC5	Validate Sign-Up redirection
* TC6	Login with valid credentials
* TC7	Login with invalid credentials
* TC8	Validate menu items: Courses, LIVE Classes, Practice
* TC9	Check presence of Dobby Assistant
* TC10	Logout functionality

****Project Structure:****
**EdTech_Platform_Web_Application_Automation**
* **-POM(PageObjectModel)**  
* **-Test**
* **-Test_Data**
* **-utils**
* **-reports**
* **-screenshots**

**Requirements**
Things need to be installed in project
* selenium
* pytest
* pytest-html

**Key Features**
**conftest :** Ensures Cross Browser Execution
**Page Object Model (POM):** Encapsulated page interactions for maintainability
**Pytest Hooks:** Logging and screenshot capture for every test case
**Error Handling:** Robust exception management for resilient test execution
**Test suite:** Including both valid (positive) and invalid (negative) test scenarios.
**Locators:** Centralised Repository for Locators of all page class,for easy maintenance and future updation.

**Reporting:**
* Screenshots captured for both passed and failed tests
* Logs stored per test case for debugging
* HTML reports generated

**To Run**
**1. Cross Browser Execution  ->** pytest --browser=browser_name  (eg:browser_name as chrome/edge/safari/firefox)
**2. To generate HTML repot ->** pytest --html=reports.html 
**3. To generate browser specific HTML report ->** pytest ---browser=chrome --html=chrome_report.html




