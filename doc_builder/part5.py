# Part 5: Sections 61 through 75 (Simple English Revision Guide)

def get_part5_html():
    return r"""
    <!-- ==================== SECTION 61: USE CASE 1 ==================== -->
    <div class="page-break"></div>
    <h1 class="section-title"><span class="section-number">61</span> End-to-End Walkthrough 1: Adding a New Employee</h1>
    
    <p>Let's follow the entire story of adding an employee from start to finish:</p>

    <div class="box-note">
        <div class="box-title">Scenario: Adding "Ananya Verma" (Engineering, ₹75,000)</div>
        <ol>
            <li><strong>You click "Add Employee":</strong> A popup dialog opens on your screen.</li>
            <li><strong>You type in details:</strong> Name = Ananya Verma, Email = ananya@gmail.com, Dept = Engineering, Salary = 75000.</li>
            <li><strong>You click "Save":</strong> JavaScript reads your inputs, formats them into JSON, and sends an HTTP POST to <code>/employees</code>.</li>
            <li><strong>Controller catches it:</strong> <code>EmployeeController</code> receives the request and turns the JSON into a Java <code>Employee</code> object.</li>
            <li><strong>Service and Repository save it:</strong> <code>EmployeeService</code> calls <code>EmployeeRepository.save()</code>.</li>
            <li><strong>Database saves row:</strong> Hibernate writes an <code>INSERT INTO employees...</code> SQL query. The database gives Ananya a new ID (e.g., ID 3).</li>
            <li><strong>Server replies:</strong> The controller sends back <code>201 Created</code> with the new employee JSON.</li>
            <li><strong>Webpage updates:</strong> The popup box closes, a green toast notification says <em>"Employee saved successfully!"</em>, and Ananya appears in the table. The total payroll and employee count cards increase automatically!</li>
        </ol>
    </div>

    <!-- ==================== SECTION 62: USE CASE 2 ==================== -->
    <h1 class="section-title"><span class="section-number">62</span> End-to-End Walkthrough 2: Filter by Department</h1>
    
    <div class="box-note">
        <div class="box-title">Scenario: Filtering by "IT" Department</div>
        <ol>
            <li><strong>You pick "IT" from dropdown:</strong> In the control bar, you select "IT".</li>
            <li><strong>JavaScript makes a call:</strong> JavaScript executes <code>fetch('/employees/department/IT')</code>.</li>
            <li><strong>Controller delegates:</strong> <code>EmployeeController</code> calls <code>employeeService.getEmployeesByDepartment("IT")</code>.</li>
            <li><strong>Repository derived query:</strong> <code>findByDepartmentIgnoreCase("IT")</code> runs:
                <code>SELECT * FROM employees WHERE UPPER(department) = 'IT';</code></li>
            <li><strong>Results displayed:</strong> Only IT department employees appear in the table.</li>
        </ol>
    </div>

    <!-- ==================== SECTION 63: USE CASE 3 ==================== -->
    <h1 class="section-title"><span class="section-number">63</span> End-to-End Walkthrough 3: Update Employee Details</h1>
    
    <div class="box-note">
        <div class="box-title">Scenario: Changing Salary from 50000 to 65000</div>
        <ol>
            <li><strong>Click Edit:</strong> You click the pen icon next to Rahul (ID 1).</li>
            <li><strong>Popup opens:</strong> The form opens with Rahul's current details pre-filled.</li>
            <li><strong>Change Salary:</strong> You change the salary to 65000 and click Save.</li>
            <li><strong>PUT request sent:</strong> JavaScript sends an HTTP <code>PUT /employees/1</code> with the new details.</li>
            <li><strong>Database updated:</strong> <code>EmployeeService</code> finds employee 1, updates the fields, and saves to database.</li>
            <li><strong>Confirmation:</strong> Server returns <code>200 OK</code>, the table updates, and the stats card updates the average salary.</li>
        </ol>
    </div>

    <!-- ==================== SECTION 64: MASTER DATA FLOW ==================== -->
    <h1 class="section-title"><span class="section-number">64</span> Master System Data Flow Diagram</h1>
    
    <div class="diagram-box">
        <div class="diagram-caption">Complete Master Data Flow</div>
        <p style="font-family: monospace; font-size: 8.5pt;">
            [ USER / Web Browser ]<br>
            &darr; &uarr; (HTTP / JSON via fetch API)<br>
            [ Spring Boot Controller: EmployeeController ]<br>
            &darr; &uarr; (Method calls &amp; returns)<br>
            [ Business Logic Service: EmployeeService ]<br>
            &darr; &uarr; (JpaRepository proxy)<br>
            [ Persistence: EmployeeRepository + Hibernate ]<br>
            &darr; &uarr; (SQL INSERT / SELECT / UPDATE / DELETE)<br>
            [ Database: MySQL 8.0 or In-Memory H2 ]
        </p>
    </div>

    <!-- ==================== SECTION 65: DECISION MATRIX ==================== -->
    <h1 class="section-title"><span class="section-number">65</span> Technology Decision Matrix (Quick Table)</h1>
    
    <table>
        <thead>
            <tr>
                <th style="width: 20%;">What We Chose</th>
                <th style="width: 25%;">Alternative Option</th>
                <th style="width: 55%;">Why We Chose It (Simple Explanation)</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td><strong>Java 17</strong></td>
                <td>Python / Node.js</td>
                <td>Strong typing prevents salary and ID bugs; enterprise standard for backend software.</td>
            </tr>
            <tr>
                <td><strong>Spring Boot</strong></td>
                <td>Jakarta EE / Express</td>
                <td>Tomcat is built-in; starters make REST APIs super fast to build.</td>
            </tr>
            <tr>
                <td><strong>Spring Data JPA</strong></td>
                <td>Plain JDBC</td>
                <td>Eliminates 90% of repetitive SQL boilerplate code.</td>
            </tr>
            <tr>
                <td><strong>Hibernate</strong></td>
                <td>Direct SQL</td>
                <td>Automatically updates database tables and maps Java objects to rows.</td>
            </tr>
            <tr>
                <td><strong>MySQL 8.0</strong></td>
                <td>MongoDB</td>
                <td>Employee records fit perfectly into structured tables with ACID guarantees.</td>
            </tr>
            <tr>
                <td><strong>H2 Database</strong></td>
                <td>Local MySQL only</td>
                <td>Allows anyone to run the project in seconds without installing MySQL.</td>
            </tr>
            <tr>
                <td><strong>Vanilla JS</strong></td>
                <td>React / Angular</td>
                <td>No npm install or Node.js needed; frontend is bundled inside the Java JAR file.</td>
            </tr>
            <tr>
                <td><strong>Docker</strong></td>
                <td>Manual deploy</td>
                <td>Packages the app into a container that runs identically on any machine or cloud server.</td>
            </tr>
        </tbody>
    </table>

    <!-- ==================== SECTION 66: WHY THIS NOT THAT ==================== -->
    <h1 class="section-title"><span class="section-number">66</span> "Why This and Not That" (Common Viva Comparisons)</h1>
    
    <p><strong>1. Spring Data JPA vs Plain JDBC:</strong><br>
    Plain JDBC requires writing 30 lines of code just to read one employee by ID. Spring Data JPA gives you <code>findById()</code> in a single line. It saves time and prevents SQL typos.</p>

    <p><strong>2. Vanilla JavaScript vs React:</strong><br>
    React is great for huge apps like Facebook, but for an employee dashboard it introduces 300MB of dependencies and complex build scripts. Plain HTML/CSS/JS is fast, lightweight, and packs right inside the Spring Boot JAR file.</p>

    <p><strong>3. H2 vs MySQL for Testing:</strong><br>
    Testing against MySQL requires setting up passwords and cleaning up rows afterwards. H2 runs in memory, runs tests in 3 seconds, and deletes everything automatically when tests finish.</p>

    <!-- ==================== SECTION 67: VERSION ANALYSIS ==================== -->
    <h1 class="section-title"><span class="section-number">67</span> Versions Used &amp; Compatibility</h1>
    
    <ul>
        <li><strong>Java 17 LTS:</strong> The stable baseline. Compatible with newer Java 21 and Java 23 runtimes.</li>
        <li><strong>Spring Boot 3.3.3:</strong> The latest stable branch of Spring Boot 3. Requires Java 17+.</li>
        <li><strong>MySQL 8.0:</strong> The modern MySQL release with high performance and strong security.</li>
    </ul>

    <!-- ==================== SECTION 68: REQUIREMENT TRACEABILITY ==================== -->
    <h1 class="section-title"><span class="section-number">68</span> Requirements Traceability Table</h1>
    
    <table>
        <thead>
            <tr>
                <th>Requirement</th>
                <th>Java File</th>
                <th>Automated Test</th>
                <th>Status</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>FR-01 Add Employee</td>
                <td><code>EmployeeController.java</code> (line 27)</td>
                <td><code>testAddEmployee()</code></td>
                <td><span class="badge badge-implemented">VERIFIED</span></td>
            </tr>
            <tr>
                <td>FR-02 View All</td>
                <td><code>EmployeeController.java</code> (line 34)</td>
                <td><code>testGetAllEmployees()</code></td>
                <td><span class="badge badge-implemented">VERIFIED</span></td>
            </tr>
            <tr>
                <td>FR-03 Lookup by ID</td>
                <td><code>EmployeeController.java</code> (line 41)</td>
                <td><code>testGetEmployeeById()</code></td>
                <td><span class="badge badge-implemented">VERIFIED</span></td>
            </tr>
            <tr>
                <td>FR-04 Update</td>
                <td><code>EmployeeController.java</code> (line 49)</td>
                <td><code>testUpdateEmployee()</code></td>
                <td><span class="badge badge-implemented">VERIFIED</span></td>
            </tr>
            <tr>
                <td>FR-05 Delete</td>
                <td><code>EmployeeController.java</code> (line 61)</td>
                <td><code>testDeleteEmployee()</code></td>
                <td><span class="badge badge-implemented">VERIFIED</span></td>
            </tr>
            <tr>
                <td>FR-06 Dept Filter</td>
                <td><code>EmployeeController.java</code> (line 73)</td>
                <td><code>testGetEmployeesByDepartment()</code></td>
                <td><span class="badge badge-implemented">VERIFIED</span></td>
            </tr>
        </tbody>
    </table>

    <!-- ==================== SECTION 69: TEST TRACEABILITY ==================== -->
    <h1 class="section-title"><span class="section-number">69</span> Test Coverage Disclosure</h1>
    
    <p>Our project contains <strong>6 automated integration tests</strong> in <code>EmployeeControllerTest.java</code>. Each test verifies a specific HTTP endpoint and asserts that the HTTP status code (200 or 201) and JSON data match expectations. All 6 tests pass successfully.</p>

    <!-- ==================== SECTION 70: DEPLOYMENT TRACEABILITY ==================== -->
    <h1 class="section-title"><span class="section-number">70</span> Deployment Traceability</h1>
    
    <p>How our code goes from GitHub to the Cloud:</p>
    <p><code>GitHub Repository &rarr; Dockerfile &rarr; Docker Container Image &rarr; Render Cloud &rarr; Live Website</code></p>

    <!-- ==================== SECTION 71: PROJECT MATURITY ==================== -->
    <h1 class="section-title"><span class="section-number">71</span> Project Maturity Review</h1>
    
    <ul>
        <li><strong>What is Ready:</strong> Full CRUD operations, department search, live dashboard stats, dual database support, automated tests, Docker containerization, and live cloud deployment.</li>
        <li><strong>What is Missing for Big Enterprise Use:</strong> User login passwords (authentication), role permissions, pagination, and multi-table relationships.</li>
    </ul>

    <!-- ==================== SECTION 72: INTERVIEW PREPARATION ==================== -->
    <h1 class="section-title"><span class="section-number">72</span> Technical Interview Q&amp;A (Memorize These!)</h1>
    
    <p><strong>Q1: What does <code>@RestController</code> do in Spring Boot?</strong><br>
    <strong>A:</strong> It is a combination of <code>@Controller</code> and <code>@ResponseBody</code>. It tells Spring that this class handles web requests and converts the returned Java objects directly into JSON.</p>

    <p><strong>Q2: What is the difference between <code>@GetMapping</code> and <code>@PostMapping</code>?</strong><br>
    <strong>A:</strong> <code>@GetMapping</code> is used to fetch/read data without changing the server state. <code>@PostMapping</code> is used to send new data in the request body to create a new record in the database.</p>

    <p><strong>Q3: How does Spring Data JPA create queries from method names?</strong><br>
    <strong>A:</strong> It reads method name keywords like <code>findByDepartmentIgnoreCase</code>. It parses <code>findBy</code> (SELECT), <code>Department</code> (the column), and <code>IgnoreCase</code> (UPPER() comparison) and generates the SQL automatically.</p>

    <p><strong>Q4: Why do we use Constructor Injection instead of <code>@Autowired</code> on fields?</strong><br>
    <strong>A:</strong> Constructor injection makes variables <code>final</code> (immutable), guarantees all required dependencies are provided, and makes writing unit tests much easier without needing reflection.</p>

    <!-- ==================== SECTION 73: PROJECT DEFENSE / VIVA QUESTIONS ==================== -->
    <h1 class="section-title"><span class="section-number">73</span> Viva / Project Defense Questions</h1>
    
    <p><strong>Q1: Why did you use two databases (MySQL and H2)?</strong><br>
    <strong>A:</strong> MySQL is for permanent, real-world storage. H2 runs in memory with zero installation, which allows teachers, reviewers, or automated test runners to execute the project instantly without setting up a MySQL server.</p>

    <p><strong>Q2: What happens if I try to delete an employee ID that doesn't exist?</strong><br>
    <strong>A:</strong> <code>EmployeeService</code> checks <code>existsById(id)</code>. If false, it throws a <code>RuntimeException</code>. The controller catches this and returns HTTP status <code>404 Not Found</code> with JSON <code>{"message": "Employee not found with ID: X"}</code>.</p>

    <p><strong>Q3: Why did you not use React for the frontend?</strong><br>
    <strong>A:</strong> Using plain HTML, CSS, and JavaScript allows us to package the frontend right inside the Spring Boot JAR file. The entire app (frontend + backend) runs as a single self-contained JAR file under 50 MB with zero Node.js dependencies.</p>

    <!-- ==================== SECTION 74: FINAL SUMMARY ==================== -->
    <h1 class="section-title"><span class="section-number">74</span> Final Project Summary</h1>
    
    <div class="box-note">
        <p><strong>Problem:</strong> Managing employee records in Excel spreadsheets leads to duplicate IDs, accidental overwrites, and no REST API integration.</p>
        <p><strong>Solution:</strong> We built the Employment Management System—a full-stack web application using Java 17, Spring Boot 3.3.3, Spring Data JPA, MySQL/H2, and a responsive web dashboard.</p>
        <p><strong>Outcome:</strong> Complete CRUD functionality, real-time department filtering, live statistics, automated MockMvc tests, multi-stage Docker builds, and live deployment on Render.</p>
    </div>

    <!-- ==================== SECTION 75: APPENDIX ==================== -->
    <h1 class="section-title"><span class="section-number">75</span> Appendix: Quick Commands &amp; SQL Cheat Sheet</h1>
    
    <p><strong>1. Useful Terminal Commands:</strong></p>
    <pre><code># Run with H2 In-Memory Database (No setup needed):
.\mvnw.cmd spring-boot:run "-Dspring-boot.run.profiles=h2"   (Windows)
./mvnw spring-boot:run -Dspring-boot.run.profiles=h2         (Mac/Linux)

# Run with MySQL:
./mvnw spring-boot:run

# Run all 6 automated tests:
./mvnw test

# Start with Docker Compose (MySQL + App):
docker compose up -d</code></pre>

    <p><strong>2. MySQL Table DDL:</strong></p>
    <pre><code>CREATE TABLE employees (
    id BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255),
    department VARCHAR(255),
    salary DOUBLE
);</code></pre>

    <p><strong>3. Key Terminology:</strong></p>
    <ul>
        <li><strong>CRUD:</strong> Create, Read, Update, Delete.</li>
        <li><strong>REST:</strong> Representational State Transfer (architectural style for web APIs).</li>
        <li><strong>ORM:</strong> Object-Relational Mapping (translating Java objects to database rows).</li>
        <li><strong>MockMvc:</strong> Testing library that simulates HTTP web requests in memory.</li>
        <li><strong>LTS:</strong> Long-Term Support (software version supported for multiple years).</li>
    </ul>
    """
