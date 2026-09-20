# Part 1: Sections 1 through 15 (Simple English Revision Guide)

def get_part1_html():
    return r"""
    <!-- ==================== SECTION 1: COVER PAGE ==================== -->
    <div class="cover-page">
        <div class="cover-header">
            <div class="cover-badge">Student &amp; Interview Revision Guide</div>
            <div class="cover-title">Employment Management System</div>
            <div class="cover-subtitle">Full-Stack Project Documentation &amp; Step-by-Step Technical Notes</div>
        </div>

        <div class="cover-metadata">
            <table class="cover-meta-table">
                <tr>
                    <td class="label">Project Name</td>
                    <td>Employment Management System (EMS)</td>
                </tr>
                <tr>
                    <td class="label">GitHub Repository</td>
                    <td>https://github.com/jaishree-verma/Employment_Management_System</td>
                </tr>
                <tr>
                    <td class="label">Author / Developer</td>
                    <td>Jaishree Verma</td>
                </tr>
                <tr>
                    <td class="label">Core Technologies</td>
                    <td>Java 17, Spring Boot 3.3.3, Spring Data JPA, Hibernate, MySQL, H2, HTML, CSS, JavaScript</td>
                </tr>
                <tr>
                    <td class="label">Documentation Version</td>
                    <td>1.0 (Simple English Revision Edition)</td>
                </tr>
                <tr>
                    <td class="label">Purpose of Document</td>
                    <td>Complete project explanation for quick revision, exams, viva, and technical interviews.</td>
                </tr>
            </table>
        </div>

        <div class="cover-footer">
            Employment Management System | Clean Black &amp; White Revision Edition
        </div>
    </div>

    <!-- ==================== SECTION 2: DOCUMENT CONTROL ==================== -->
    <div class="page-break"></div>
    <h1 class="section-title"><span class="section-number">02</span> Document Control &amp; Quick Facts</h1>
    
    <p>This table gives you all the core facts about the project at a single glance. Everything here was checked directly from the project files:</p>

    <table>
        <thead>
            <tr>
                <th style="width: 30%;">Item</th>
                <th style="width: 70%;">Details Checked from Code</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td><strong>Project Name</strong></td>
                <td>Employment Management System</td>
            </tr>
            <tr>
                <td><strong>Project Type</strong></td>
                <td>Full-Stack Web Application (Spring Boot backend + HTML/CSS/JS frontend)</td>
            </tr>
            <tr>
                <td><strong>Backend Language</strong></td>
                <td>Java 17 (configured in <code>pom.xml</code> line 18)</td>
            </tr>
            <tr>
                <td><strong>Framework</strong></td>
                <td>Spring Boot version 3.3.3</td>
            </tr>
            <tr>
                <td><strong>Database Layer</strong></td>
                <td>Spring Data JPA with Hibernate 6.5</td>
            </tr>
            <tr>
                <td><strong>Databases Used</strong></td>
                <td>MySQL 8.0 (for permanent storage) and H2 Database (temporary in-memory for testing/dev)</td>
            </tr>
            <tr>
                <td><strong>Frontend</strong></td>
                <td>Pure HTML5, CSS3, and JavaScript (No heavy frameworks like React/Angular)</td>
            </tr>
            <tr>
                <td><strong>Testing Tool</strong></td>
                <td>JUnit 5 and MockMvc (automated tests run without starting a browser)</td>
            </tr>
            <tr>
                <td><strong>Deployment</strong></td>
                <td>Docker container on Render Cloud platform</td>
            </tr>
        </tbody>
    </table>

    <div class="box-note">
        <div class="box-title">Important Revision Note: Java 17 vs Java 23</div>
        If someone asks: <em>"Which Java version is used?"</em><br>
        Answer: <strong>Java 17 LTS</strong> is the official configured version in <code>pom.xml</code> and <code>Dockerfile</code>. If your computer has Java 23 installed, the code runs on Java 23 without any problems because Java is backwards compatible.
    </div>

    <!-- ==================== TABLE OF CONTENTS ==================== -->
    <div class="page-break"></div>
    <h1 class="section-title"><span class="section-number">TOC</span> Table of Contents (All 75 Sections)</h1>
    
    <p>Here is the roadmap of all 75 topics covered in this guide:</p>

    <div style="display: flex; gap: 15px; font-size: 8pt;">
        <div style="flex: 1;">
            <p><strong>Part A: Basics &amp; Requirements (01–11)</strong></p>
            <ul style="list-style: none; padding-left: 0;">
                <li>01. Cover Page</li>
                <li>02. Document Control</li>
                <li>03. Executive Summary</li>
                <li>04. Problem Statement</li>
                <li>05. Why Choose This Project?</li>
                <li>06. Project Objectives</li>
                <li>07. Scope of the System</li>
                <li>08. Target Users</li>
                <li>09. Functional Requirements (FR-01 to FR-08)</li>
                <li>10. Non-Functional Requirements</li>
                <li>11. Old System vs New System</li>
            </ul>

            <p><strong>Part B: Architecture &amp; Data Flow (12–15)</strong></p>
            <ul style="list-style: none; padding-left: 0;">
                <li>12. Solution Overview</li>
                <li>13. System Architecture (4 Layers)</li>
                <li>14. Why Layered Architecture?</li>
                <li>15. Complete Request Lifecycle</li>
            </ul>

            <p><strong>Part C: Why These Technologies? (16–27)</strong></p>
            <ul style="list-style: none; padding-left: 0;">
                <li>16. Technology Stack Table</li>
                <li>17. Why Java?</li>
                <li>18. Why Java 17 / 23?</li>
                <li>19. Why Spring Boot?</li>
                <li>20. Why Spring Boot 3.3.3?</li>
                <li>21. Why Spring Data JPA?</li>
                <li>22. Why Hibernate?</li>
                <li>23. Why MySQL?</li>
                <li>24. Why H2 In-Memory DB?</li>
                <li>25. Why Dual Databases?</li>
                <li>26. Why Maven &amp; Wrapper?</li>
                <li>27. Why Vanilla HTML/CSS/JS?</li>
            </ul>

            <p><strong>Part D: Frontend (28–30)</strong></p>
            <ul style="list-style: none; padding-left: 0;">
                <li>28. Frontend Architecture</li>
                <li>29. UI/UX Design</li>
                <li>30. Dark and Light Mode</li>
            </ul>
        </div>

        <div style="flex: 1;">
            <p><strong>Part E: Data &amp; APIs (31–39)</strong></p>
            <ul style="list-style: none; padding-left: 0;">
                <li>31. Employee Data Model</li>
                <li>32. Database Design (Schema)</li>
                <li>33. JPA Annotations</li>
                <li>34. REST API Catalog (6 Endpoints)</li>
                <li>35. API Request / Response Examples</li>
                <li>36. HTTP Status Codes Explained</li>
                <li>37. How Department Filtering Works</li>
                <li>38. How Search Works</li>
                <li>39. How Dashboard Stats Work</li>
            </ul>

            <p><strong>Part F: Testing &amp; Security (40–45)</strong></p>
            <ul style="list-style: none; padding-left: 0;">
                <li>40. Testing Architecture</li>
                <li>41. All 6 Test Cases Explained</li>
                <li>42. Why MockMvc?</li>
                <li>43. Postman Testing Guide</li>
                <li>44. Error Handling</li>
                <li>45. Security: Current vs Production</li>
            </ul>

            <p><strong>Part G: Docker &amp; Deployment (46–52)</strong></p>
            <ul style="list-style: none; padding-left: 0;">
                <li>46. Dockerfile Explained</li>
                <li>47. Why Multi-Stage Docker?</li>
                <li>48. Docker Compose Explained</li>
                <li>49. Cloud Deployment on Render</li>
                <li>50. Why Render?</li>
                <li>51. How to Run Locally</li>
                <li>52. Configuration Files</li>
            </ul>

            <p><strong>Part H: Analysis &amp; Interview Questions (53–75)</strong></p>
            <ul style="list-style: none; padding-left: 0;">
                <li>53. Directory Structure Tree</li>
                <li>54. Code Quality Review</li>
                <li>55. Design Patterns Used</li>
                <li>56. Performance Review</li>
                <li>57. Scalability Plan</li>
                <li>58. Current Limitations</li>
                <li>59. Future Enhancements</li>
                <li>60. Why These Features?</li>
                <li>61–63. Three Complete Use Cases</li>
                <li>64. Master Data Flow Diagram</li>
                <li>65–67. Technology Decision Matrix</li>
                <li>68–70. Traceability Tables</li>
                <li>71. Project Maturity</li>
                <li>72. Technical Interview Q&amp;A</li>
                <li>73. Project Defense / Viva Q&amp;A</li>
                <li>74. Final Technical Summary</li>
                <li>75. Appendix (Commands &amp; SQL)</li>
            </ul>
        </div>
    </div>

    <!-- ==================== SECTION 3: EXECUTIVE SUMMARY ==================== -->
    <div class="page-break"></div>
    <h1 class="section-title"><span class="section-number">03</span> Executive Summary (Simple Overview)</h1>
    
    <p><strong>In Simple Words:</strong> The <strong>Employment Management System (EMS)</strong> is a web application that helps a company manage its employees. Instead of using paper files or Excel sheets, an HR manager can open a web browser, see all employees in a clean table, add a new employee, edit someone's salary or department, search by name, filter by department, or delete someone who left the company.</p>

    <p><strong>How It Is Built:</strong></p>
    <ul>
        <li><strong>Frontend (What you see):</strong> A single webpage built using plain HTML, CSS, and JavaScript. It has a Dark mode and Light mode, a search bar, and 4 cards showing stats (Total employees, number of departments, total payroll, and average salary).</li>
        <li><strong>Backend (The brain):</strong> A Java program using <strong>Spring Boot</strong>. It receives requests from the webpage (like "save this employee") and runs the business logic.</li>
        <li><strong>Database (Where data lives):</strong> Can save data into <strong>MySQL</strong> (for permanent storage) or into <strong>H2</strong> (a temporary memory database for fast testing).</li>
        <li><strong>Testing &amp; Deployment:</strong> It has automated tests (MockMvc) to make sure every button works, and it is packed inside a Docker container so it can run on any computer or cloud server (Render).</li>
    </ul>

    <!-- ==================== SECTION 4: PROBLEM STATEMENT ==================== -->
    <h1 class="section-title"><span class="section-number">04</span> Problem Statement (Why Do We Need This?)</h1>
    
    <p>In many small offices and colleges, employee records are kept in Excel files or on paper. This causes several big problems:</p>

    <ol>
        <li><strong>Mistakes and Typos:</strong> In Excel, someone might type department as "IT", another person types "it", and another types "Information Tech". This makes searching very difficult.</li>
        <li><strong>Accidental Overwrites:</strong> If two people open the same file, one person's changes can overwrite another person's changes.</li>
        <li><strong>Difficult Search:</strong> As the company grows to 500 or 1,000 employees, finding someone or calculating department salary takes too much manual work.</li>
        <li><strong>No REST API:</strong> Other software (like payroll systems or fingerprint attendance machines) cannot easily read data from a spreadsheet.</li>
    </ol>

    <!-- ==================== SECTION 5: WHY DID WE CHOOSE THIS PROJECT? ==================== -->
    <h1 class="section-title"><span class="section-number">05</span> Why Did We Choose This Project?</h1>
    
    <p>We chose to build an Employment Management System because it is the classic real-world software engineering problem. Almost every company in the world needs employee management software (like Workday, BambooHR, or internal HR portals).</p>
    
    <p>Building this project teaches all the core skills of a modern full-stack developer:</p>
    <ul>
        <li>How to design clean database tables with primary keys.</li>
        <li>How to write REST APIs following proper HTTP methods (POST, GET, PUT, DELETE).</li>
        <li>How to connect Java to databases using Spring Data JPA without writing long SQL statements.</li>
        <li>How to write clean JavaScript to talk to the backend using <code>fetch()</code>.</li>
        <li>How to write automated tests so you know your code works before showing it to anyone.</li>
        <li>How to put everything in Docker and deploy it to the cloud.</li>
    </ul>

    <!-- ==================== SECTION 6: PROJECT OBJECTIVES ==================== -->
    <h1 class="section-title"><span class="section-number">06</span> Project Objectives</h1>
    
    <p><strong>Main Goals (Primary Objectives):</strong></p>
    <ul>
        <li>Store employee information (Name, Email, Department, Salary) in a centralized database.</li>
        <li>Provide full CRUD functionality (Create, Read, Update, Delete).</li>
        <li>Allow instant filtering of employees by department (like showing only IT staff).</li>
        <li>Provide a web dashboard with live statistics (Total employees, total salary bill, average salary).</li>
        <li>Expose clean REST API endpoints for other programs to use.</li>
        <li>Include automated tests so the project can be verified anytime.</li>
    </ul>

    <p><strong>Extra Goals (Secondary Objectives):</strong></p>
    <ul>
        <li>Provide both Dark mode and Light mode so the screen is comfortable to look at.</li>
        <li>Save user theme choice in browser memory (localStorage) so it stays when refreshed.</li>
        <li>Support zero-setup local running with H2 database (run with 1 command, no database install needed).</li>
        <li>Dockerize the project so it runs anywhere identically.</li>
    </ul>

    <!-- ==================== SECTION 7: SCOPE ==================== -->
    <h1 class="section-title"><span class="section-number">07</span> Scope of the Project</h1>
    
    <table>
        <thead>
            <tr>
                <th style="width: 25%;">Area</th>
                <th style="width: 55%;">Features</th>
                <th style="width: 20%;">Status</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td><strong>In Scope (Currently Working)</strong></td>
                <td>Add employee, view all employees, view by ID, update employee, delete employee, filter by department, live search bar, dashboard stats, dark/light theme, automated tests, Docker setup, Render deployment.</td>
                <td><span class="badge badge-implemented">IMPLEMENTED</span></td>
            </tr>
            <tr>
                <td><strong>Partially Working</strong></td>
                <td>Form input validation (HTML requires fields, but backend relies on basic exceptions rather than formal annotations).</td>
                <td><span class="badge badge-partial">PARTIAL</span></td>
            </tr>
            <tr>
                <td><strong>Out of Scope (Not in this version)</strong></td>
                <td>User login passwords (authentication), user roles (Admin vs Employee permissions), multiple database tables (like a separate department table).</td>
                <td><span class="badge badge-not-implemented">NOT INCLUDED</span></td>
            </tr>
            <tr>
                <td><strong>Future Scope (Planned Next)</strong></td>
                <td>Login with JWT tokens, attendance tracking, leave requests, PDF salary slip download.</td>
                <td><span class="badge badge-future">FUTURE</span></td>
            </tr>
        </tbody>
    </table>

    <!-- ==================== SECTION 8: TARGET USERS ==================== -->
    <h1 class="section-title"><span class="section-number">08</span> Who Uses This System? (Target Users)</h1>
    
    <div class="row-2">
        <div class="col-2">
            <p><strong>1. HR / Office Manager:</strong></p>
            <p>Uses the web dashboard in the browser to add new hires, update salaries, look up contact emails, filter by department, and see how much total salary the company pays each month.</p>
        </div>
        <div class="col-2">
            <p><strong>2. Developer / External System:</strong></p>
            <p>Uses the REST APIs (using Postman or code) to fetch employee JSON data or connect the employee list to other software like attendance clocks or payroll engines.</p>
        </div>
    </div>
    <p><em>Note: Right now, anyone who opens the URL can use the dashboard because login/passwords are not yet added.</em></p>

    <!-- ==================== SECTION 9: FUNCTIONAL REQUIREMENTS ==================== -->
    <h1 class="section-title"><span class="section-number">09</span> Functional Requirements (What the System Does)</h1>
    
    <p>Here are the 8 exact features implemented in the code:</p>

    <table>
        <thead>
            <tr>
                <th style="width: 12%;">ID</th>
                <th style="width: 28%;">Feature</th>
                <th style="width: 45%;">How It Works in Code</th>
                <th style="width: 15%;">Status</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td><strong>FR-01</strong></td>
                <td>Add Employee</td>
                <td>Send <code>POST /employees</code> with name, email, department, salary. Returns <code>201 Created</code>.</td>
                <td><span class="badge badge-implemented">WORKING</span></td>
            </tr>
            <tr>
                <td><strong>FR-02</strong></td>
                <td>View All Employees</td>
                <td>Send <code>GET /employees</code>. Returns list of all employees in JSON.</td>
                <td><span class="badge badge-implemented">WORKING</span></td>
            </tr>
            <tr>
                <td><strong>FR-03</strong></td>
                <td>View Employee by ID</td>
                <td>Send <code>GET /employees/{id}</code>. Returns that specific employee or 404 error.</td>
                <td><span class="badge badge-implemented">WORKING</span></td>
            </tr>
            <tr>
                <td><strong>FR-04</strong></td>
                <td>Update Employee</td>
                <td>Send <code>PUT /employees/{id}</code> with new details. Saves changes and returns updated employee.</td>
                <td><span class="badge badge-implemented">WORKING</span></td>
            </tr>
            <tr>
                <td><strong>FR-05</strong></td>
                <td>Delete Employee</td>
                <td>Send <code>DELETE /employees/{id}</code>. Removes employee from database.</td>
                <td><span class="badge badge-implemented">WORKING</span></td>
            </tr>
            <tr>
                <td><strong>FR-06</strong></td>
                <td>Filter by Department</td>
                <td>Send <code>GET /employees/department/{dept}</code>. Returns employees belonging to that department.</td>
                <td><span class="badge badge-implemented">WORKING</span></td>
            </tr>
            <tr>
                <td><strong>FR-07</strong></td>
                <td>Live Search Bar</td>
                <td>Type in search box on the dashboard; JavaScript instantly filters the table as you type.</td>
                <td><span class="badge badge-implemented">WORKING</span></td>
            </tr>
            <tr>
                <td><strong>FR-08</strong></td>
                <td>Dashboard Statistics</td>
                <td>JavaScript automatically calculates total count, active departments, total payroll, and average salary.</td>
                <td><span class="badge badge-implemented">WORKING</span></td>
            </tr>
        </tbody>
    </table>

    <!-- ==================== SECTION 10: NON-FUNCTIONAL REQUIREMENTS ==================== -->
    <h1 class="section-title"><span class="section-number">10</span> Non-Functional Requirements (Quality &amp; Speed)</h1>
    
    <ul>
        <li><strong>Speed (Performance):</strong> Database lookups in H2 take less than 5 milliseconds. The webpage loads in under 1 second because there are no heavy libraries.</li>
        <li><strong>Reliability (ACID):</strong> Data is stored in a relational database with transactions. When you save an employee, it is saved completely or not at all (no half-saved records).</li>
        <li><strong>Ease of Running (Portability):</strong> With Docker, anyone can run the app on Windows, Mac, or Linux without installing Java or MySQL manually.</li>
        <li><strong>Easy to Test:</strong> 6 automated tests check all the main features in less than 3 seconds.</li>
    </ul>

    <!-- ==================== SECTION 11: OLD SYSTEM VS PROPOSED SYSTEM ==================== -->
    <h1 class="section-title"><span class="section-number">11</span> Old System (Excel/Paper) vs New System (EMS)</h1>
    
    <table>
        <thead>
            <tr>
                <th style="width: 25%;">Area</th>
                <th style="width: 37%;">Old Way (Spreadsheets)</th>
                <th style="width: 38%;">New Way (Employment Management System)</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td><strong>Data Storage</strong></td>
                <td>Saved in files on one computer. Can be accidentally deleted.</td>
                <td>Stored in a central database (MySQL / H2).</td>
            </tr>
            <tr>
                <td><strong>How Users Open It</strong></td>
                <td>Must email files or share on a USB drive.</td>
                <td>Open website in any browser using a simple link.</td>
            </tr>
            <tr>
                <td><strong>Searching</strong></td>
                <td>Manually scrolling or using Excel Ctrl+F.</td>
                <td>Type in search bar or pick department from dropdown.</td>
            </tr>
            <tr>
                <td><strong>ID Numbers</strong></td>
                <td>Manually typed numbers; duplicates happen easily.</td>
                <td>Database automatically generates unique IDs (1, 2, 3...).</td>
            </tr>
            <tr>
                <td><strong>Connecting other software</strong></td>
                <td>Impossible or requires manual CSV exports.</td>
                <td>Standard REST API endpoints return JSON data.</td>
            </tr>
        </tbody>
    </table>

    <!-- ==================== SECTION 12: SOLUTION OVERVIEW ==================== -->
    <h1 class="section-title"><span class="section-number">12</span> Solution Overview (How the Pieces Connect)</h1>
    
    <p>Here is the simple journey of data in this application:</p>

    <div class="diagram-box">
        <div class="diagram-caption">How a User Request Flows Through the System</div>
        <p style="font-family: monospace; font-size: 9pt; margin: 10px 0;">
            [ USER in Web Browser / Postman ]<br>
            &darr; (Sends HTTP Request like GET or POST)<br>
            [ Controller: EmployeeController.java ] &rarr; Receives request and path<br>
            &darr;<br>
            [ Service: EmployeeService.java ] &rarr; Runs business checks<br>
            &darr;<br>
            [ Repository: EmployeeRepository.java ] &rarr; Spring Data JPA interface<br>
            &darr;<br>
            [ Database: MySQL or H2 ] &rarr; Reads or saves the employee row<br>
            &darr; (Data comes back up the same way)<br>
            [ JSON Response back to User's Screen ]
        </p>
    </div>

    <!-- ==================== SECTION 13: SYSTEM ARCHITECTURE ==================== -->
    <h1 class="section-title"><span class="section-number">13</span> System Architecture (The 4 Layers)</h1>
    
    <p>Our Java backend is organized into <strong>4 clean layers</strong>. Each layer has one specific job:</p>

    <ol>
        <li><strong>Controller Layer (<code>EmployeeController.java</code>):</strong><br>
            The front door. It receives the HTTP requests from the browser (e.g., <code>POST /employees</code>), converts the JSON into Java objects, and returns HTTP responses with status codes like <code>200 OK</code> or <code>201 Created</code>.
        </li>
        <li><strong>Service Layer (<code>EmployeeService.java</code>):</strong><br>
            The brain. It contains the business rules. For example, when updating an employee, it checks if the employee actually exists; if not, it throws an error.
        </li>
        <li><strong>Repository Layer (<code>EmployeeRepository.java</code>):</strong><br>
            The database helper. It extends <code>JpaRepository</code>. We don't even have to write SQL queries—Spring Data JPA writes them for us automatically!
        </li>
        <li><strong>Entity Layer (<code>Employee.java</code>):</strong><br>
            The blueprint. A simple Java class that represents an employee row in the database table with fields: <code>id</code>, <code>name</code>, <code>email</code>, <code>department</code>, and <code>salary</code>.
        </li>
    </ol>

    <!-- ==================== SECTION 14: WHY LAYERED ARCHITECTURE? ==================== -->
    <h1 class="section-title"><span class="section-number">14</span> Why Use a Layered Architecture?</h1>
    
    <p>Beginners often put all their code inside one big file or directly inside the Controller. Why didn't we do that?</p>

    <ul>
        <li><strong>Easy to Understand:</strong> If you have a bug with saving to the database, you look in the Repository. If you have a bug with webpage routing, you look in the Controller.</li>
        <li><strong>Easy to Test:</strong> We can test the Service layer without even starting a web server or database.</li>
        <li><strong>Easy to Change:</strong> If tomorrow we want to switch from MySQL to Oracle or MongoDB, we only change the database layer—the Controller and frontend code don't need any changes!</li>
    </ul>

    <!-- ==================== SECTION 15: COMPLETE REQUEST LIFECYCLE ==================== -->
    <h1 class="section-title"><span class="section-number">15</span> Complete Request Lifecycle (Step-by-Step)</h1>
    
    <p>What happens when you click "Save Employee" on the webpage? Let's trace it step by step:</p>

    <ol>
        <li><strong>Step 1 (Browser):</strong> You click "Save". JavaScript in <code>app.js</code> reads the form values (Name, Email, Dept, Salary) and puts them into a JSON package.</li>
        <li><strong>Step 2 (Network):</strong> JavaScript sends an HTTP <code>POST</code> request to <code>http://localhost:8080/employees</code>.</li>
        <li><strong>Step 3 (Controller):</strong> Spring Boot's <code>EmployeeController</code> catches this request. Jackson library turns the JSON text into a Java <code>Employee</code> object.</li>
        <li><strong>Step 4 (Service):</strong> Controller passes the employee to <code>EmployeeService.saveEmployee()</code>.</li>
        <li><strong>Step 5 (Repository &amp; Hibernate):</strong> Service calls <code>EmployeeRepository.save()</code>. Hibernate generates the SQL statement: <code>INSERT INTO employees (name, email, department, salary) VALUES (?, ?, ?, ?)</code>.</li>
        <li><strong>Step 6 (Database):</strong> MySQL or H2 executes the insert and gives the new employee an <code>id</code> (like ID 1).</li>
        <li><strong>Step 7 (Response):</strong> The controller sends back the saved employee in JSON format with status code <code>201 Created</code>.</li>
        <li><strong>Step 8 (Screen Update):</strong> JavaScript gets the response, shows a green notification ("Employee saved successfully!"), closes the popup window, and adds the new row to the table.</li>
    </ol>
    """
