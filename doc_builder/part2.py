# Part 2: Sections 16 through 30 (Simple English Revision Guide)

def get_part2_html():
    return r"""
    <!-- ==================== SECTION 16: TECHNOLOGY STACK ==================== -->
    <div class="page-break"></div>
    <h1 class="section-title"><span class="section-number">16</span> Technology Stack (What We Used &amp; Why)</h1>
    
    <p>Here is a clean summary of every tool and version used in the project:</p>

    <table>
        <thead>
            <tr>
                <th style="width: 20%;">Technology</th>
                <th style="width: 20%;">Exact Version</th>
                <th style="width: 60%;">What It Does in Simple Words</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td><strong>Java</strong></td>
                <td>17 LTS (runs on 17-23)</td>
                <td>The main programming language used to write the backend code.</td>
            </tr>
            <tr>
                <td><strong>Spring Boot</strong></td>
                <td>3.3.3</td>
                <td>The framework that makes creating web apps and REST APIs fast and simple.</td>
            </tr>
            <tr>
                <td><strong>Spring Data JPA</strong></td>
                <td>Bundled with Spring Boot</td>
                <td>Lets us talk to the database easily without writing long SQL queries.</td>
            </tr>
            <tr>
                <td><strong>Hibernate</strong></td>
                <td>6.5.2</td>
                <td>The engine that maps Java objects directly into database table rows.</td>
            </tr>
            <tr>
                <td><strong>MySQL</strong></td>
                <td>8.0</td>
                <td>The permanent database that saves records to the hard drive.</td>
            </tr>
            <tr>
                <td><strong>H2 Database</strong></td>
                <td>2.2.224</td>
                <td>A temporary in-memory database that lets you run the project without installing MySQL.</td>
            </tr>
            <tr>
                <td><strong>HTML5 &amp; CSS3</strong></td>
                <td>Standard Web</td>
                <td>Creates the layout, tables, modal popup boxes, and dark/light themes.</td>
            </tr>
            <tr>
                <td><strong>JavaScript (ES6)</strong></td>
                <td>Vanilla (No React)</td>
                <td>Sends requests to the backend using <code>fetch()</code>, filters the table, and calculates stats.</td>
            </tr>
            <tr>
                <td><strong>Maven</strong></td>
                <td>3.9.9 (via mvnw)</td>
                <td>Downloads all the required Java libraries and builds the project into a <code>.jar</code> file.</td>
            </tr>
            <tr>
                <td><strong>Docker</strong></td>
                <td>Alpine Linux Container</td>
                <td>Packs the entire application into a lightweight container so it runs anywhere.</td>
            </tr>
        </tbody>
    </table>

    <!-- ==================== SECTION 17: WHY JAVA? ==================== -->
    <h1 class="section-title"><span class="section-number">17</span> Why Java?</h1>
    
    <p>Why did we choose Java instead of Python or Node.js?</p>
    <ul>
        <li><strong>Strong Type Checking:</strong> In Java, if a salary is a <code>Double</code> or an ID is a <code>Long</code>, the compiler makes sure you don't accidentally put text in it. This prevents many bugs before the code even runs.</li>
        <li><strong>Industry Standard for Enterprise:</strong> Most banks, colleges, and large companies use Java for their core business software because it is very fast, reliable, and secure.</li>
        <li><strong>Great Ecosystem:</strong> Spring Boot and Hibernate are mature tools that have been tested and improved for over 20 years.</li>
    </ul>

    <!-- ==================== SECTION 18: WHY JAVA 17 / JAVA 23? ==================== -->
    <h1 class="section-title"><span class="section-number">18</span> Why Java 17 LTS? (And what about Java 23?)</h1>
    
    <p><strong>The simple fact:</strong> Our <code>pom.xml</code> file specifies <code>&lt;java.version&gt;17&lt;/java.version&gt;</code>.</p>
    <ul>
        <li><strong>What is LTS?</strong> Java 17 is an <strong>LTS (Long Term Support)</strong> release. That means Oracle and the open-source community support and patch it for many years. It is rock-solid and stable.</li>
        <li><strong>Minimum for Spring Boot 3:</strong> Spring Boot 3 requires Java 17 as the minimum version. You cannot run Spring Boot 3 on old Java 8 or Java 11.</li>
        <li><strong>What if you have Java 23?</strong> Java 23 is a newer version. If you have Java 23 installed on your laptop, the project will still run fine! But keeping Java 17 in <code>pom.xml</code> guarantees that anyone with Java 17 or higher can run the project without errors.</li>
    </ul>

    <!-- ==================== SECTION 19: WHY SPRING BOOT? ==================== -->
    <h1 class="section-title"><span class="section-number">19</span> Why Spring Boot?</h1>
    
    <p>Before Spring Boot, building a Java web app was painful: you had to install a separate Apache Tomcat server, write hundreds of lines of XML configuration files, and manage dozens of jar files by hand.</p>
    <p>Spring Boot fixes this by:</p>
    <ul>
        <li><strong>Built-in Tomcat:</strong> Tomcat is embedded inside the app. You just run <code>java -jar app.jar</code> and the web server starts automatically on port 8080!</li>
        <li><strong>Starter Packages:</strong> Adding one line <code>spring-boot-starter-web</code> automatically gives you everything you need for REST APIs and JSON parsing.</li>
        <li><strong>Automatic Configuration:</strong> Spring Boot looks at your dependencies and automatically configures database connections and templates for you.</li>
    </ul>

    <!-- ==================== SECTION 20: WHY SPRING BOOT 3.3.3? ==================== -->
    <h1 class="section-title"><span class="section-number">20</span> Why Spring Boot 3.3.3?</h1>
    
    <p>Line 8 of <code>pom.xml</code> confirms version <code>3.3.3</code>. We use this version because:</p>
    <ul>
        <li>It uses the new <code>jakarta.persistence</code> namespace (the modern standard for Java persistence).</li>
        <li>It includes the latest security patches and bug fixes.</li>
        <li>It is fully compatible with Hibernate 6.5 and MySQL 8.0.</li>
    </ul>

    <!-- ==================== SECTION 21: WHY SPRING DATA JPA? ==================== -->
    <h1 class="section-title"><span class="section-number">21</span> Why Spring Data JPA?</h1>
    
    <p>Without Spring Data JPA (using old JDBC), writing an "Employee lookup by ID" takes 20 to 30 lines of code: opening connections, writing <code>SELECT * FROM employees WHERE id = ?</code>, reading row columns, and closing connections.</p>
    
    <p>With Spring Data JPA, all you write in <code>EmployeeRepository.java</code> is:</p>
    <pre><code>public interface EmployeeRepository extends JpaRepository&lt;Employee, Long&gt; {
    // That is it! Spring gives you:
    // .findAll(), .findById(), .save(), .deleteById() automatically!
}</code></pre>
    <p>This saves hours of boring repetitive typing and prevents typos in SQL statements.</p>

    <!-- ==================== SECTION 22: WHY HIBERNATE? ==================== -->
    <h1 class="section-title"><span class="section-number">22</span> Why Hibernate? (And how is it different from JPA?)</h1>
    
    <div class="box-note">
        <div class="box-title">Important Viva Question: JPA vs Hibernate</div>
        <strong>JPA (Jakarta Persistence API)</strong> is just a set of <em>rules and interfaces</em> (like an official rulebook).<br>
        <strong>Hibernate</strong> is the actual <em>engine</em> that follows those rules and does the hard work of writing SQL and talking to the database.
    </div>
    
    <p><strong>Why Hibernate is useful:</strong></p>
    <ul>
        <li><strong>Automatic Table Creation:</strong> With <code>hibernate.ddl-auto=update</code>, Hibernate checks your Java <code>Employee</code> class and automatically creates or updates the <code>employees</code> table in MySQL for you!</li>
        <li><strong>Automatic Updates:</strong> When you change an employee's salary in Java, Hibernate notices the change and automatically runs an SQL <code>UPDATE</code> statement.</li>
    </ul>

    <!-- ==================== SECTION 23: WHY MYSQL? ==================== -->
    <h1 class="section-title"><span class="section-number">23</span> Why MySQL?</h1>
    
    <p>MySQL is the world's most popular open-source relational database. For employee records, MySQL is perfect because:</p>
    <ul>
        <li>Employee data is structured into neat rows and columns (ID, Name, Email, Department, Salary).</li>
        <li>It supports transactions (ACID properties), meaning records won't get corrupted if the power goes out.</li>
        <li>It is permanently saved on the hard drive.</li>
    </ul>

    <!-- ==================== SECTION 24: WHY H2 IN-MEMORY DATABASE? ==================== -->
    <h1 class="section-title"><span class="section-number">24</span> Why H2 In-Memory Database?</h1>
    
    <p>H2 is a super-fast database that runs completely inside the computer's RAM memory without needing any installation.</p>
    
    <p><strong>Why is H2 awesome in this project?</strong></p>
    <ul>
        <li><strong>Instant Setup for Friends/Teachers:</strong> If you give this project to a classmate or teacher who doesn't have MySQL installed, they can just run the H2 command and the app works immediately!</li>
        <li><strong>Fast Testing:</strong> Our automated tests use H2. The tests start with a clean empty database, test all features, and erase everything in 3 seconds.</li>
    </ul>

    <!-- ==================== SECTION 25: WHY DUAL DATABASE SUPPORT? ==================== -->
    <h1 class="section-title"><span class="section-number">25</span> Why Dual Database Support? (MySQL + H2)</h1>
    
    <p>Our project supports both databases using <strong>Spring Profiles</strong>:</p>
    <ul>
        <li><strong>Default Profile (MySQL):</strong> Uses <code>application.properties</code> to connect to MySQL on port 3306 for permanent real-world storage.</li>
        <li><strong>H2 Profile:</strong> Uses <code>application-h2.properties</code> to run with zero installation.</li>
    </ul>
    <p>You can switch between them just by adding <code>-Dspring-boot.run.profiles=h2</code> to your command. You don't have to touch a single line of Java code!</p>

    <!-- ==================== SECTION 26: WHY MAVEN &amp; MAVEN WRAPPER? ==================== -->
    <h1 class="section-title"><span class="section-number">26</span> Why Maven &amp; The Maven Wrapper?</h1>
    
    <p>Maven is our build tool. It reads <code>pom.xml</code> and downloads all the Spring Boot, MySQL, and Hibernate libraries automatically from the internet.</p>
    <p><strong>What is <code>mvnw</code> (Maven Wrapper)?</strong></p>
    <ul>
        <li>Normally, to build a Java project, you must install Maven on your laptop and set up environment variables.</li>
        <li>With the Maven Wrapper files (<code>mvnw.cmd</code> on Windows, <code>mvnw</code> on Linux/Mac), you don't need to install Maven at all! The script downloads the correct Maven version automatically.</li>
    </ul>

    <!-- ==================== SECTION 27: WHY VANILLA HTML/CSS/JAVASCRIPT? ==================== -->
    <h1 class="section-title"><span class="section-number">27</span> Why Vanilla HTML, CSS, and JavaScript? (No React)</h1>
    
    <p>Why didn't we use React, Angular, or Vue for the frontend?</p>
    <ul>
        <li><strong>No Extra Tooling:</strong> React requires installing Node.js, npm, running <code>npm install</code> (which downloads 300MB of dependencies), and running a separate server.</li>
        <li><strong>Packed Inside Java JAR:</strong> Plain HTML, CSS, and JS files sit inside <code>src/main/resources/static/</code>. When you build the Java project, the frontend gets packed directly inside the <code>app.jar</code> file! One single file contains both the backend and frontend.</li>
        <li><strong>Super Fast:</strong> The webpage opens instantly without waiting for a heavy JavaScript framework to boot up.</li>
    </ul>

    <!-- ==================== SECTION 28: FRONTEND ARCHITECTURE ==================== -->
    <h1 class="section-title"><span class="section-number">28</span> Frontend Architecture (The 3 Frontend Files)</h1>
    
    <p>Our frontend is made of 3 simple, clean files located in <code>src/main/resources/static/</code>:</p>
    <ul>
        <li><code>index.html</code>: The webpage skeleton. Contains the header, 4 stats cards, the search bar, the employee table, and the popup dialog forms.</li>
        <li><code>styles.css</code>: 730 lines of CSS. Handles the layout, card styling, button hover effects, popup animations, and the Dark/Light themes.</li>
        <li><code>app.js</code>: The JavaScript engine. Uses <code>fetch('/employees')</code> to talk to Spring Boot, updates the table rows, filters records as you type, and calculates the summary statistics.</li>
    </ul>

    <!-- ==================== SECTION 29: UI/UX DESIGN ==================== -->
    <h1 class="section-title"><span class="section-number">29</span> UI/UX Design (User Experience)</h1>
    
    <p>The user interface is designed to be clean, intuitive, and easy to use:</p>
    <ul>
        <li><strong>Instant Feedback:</strong> When you save or delete an employee, a floating "toast notification" pops up in the corner to confirm success.</li>
        <li><strong>Clear Confirmation:</strong> When you click Delete, a confirmation popup appears asking <em>"Are you sure you want to delete [Name]?"</em> so you don't delete someone by accident.</li>
        <li><strong>Responsive:</strong> Looks great on both laptop screens and mobile phones.</li>
    </ul>

    <!-- ==================== SECTION 30: DARK AND LIGHT MODE ==================== -->
    <h1 class="section-title"><span class="section-number">30</span> Dark and Light Mode (How It Works)</h1>
    
    <p>You can toggle between Dark mode and Light mode using the button in the top-right corner. Here is the simple 3-step mechanism:</p>
    <ol>
        <li>When clicked, JavaScript toggles the attribute <code>data-theme="light"</code> or <code>data-theme="dark"</code> on the root <code>&lt;html&gt;</code> tag.</li>
        <li>In <code>styles.css</code>, CSS variables (like <code>--bg-primary</code> and <code>--text-primary</code>) change their color values automatically.</li>
        <li>JavaScript saves your choice in the browser using <code>localStorage.setItem('theme', theme)</code>. When you refresh or visit tomorrow, your theme preference is remembered!</li>
    </ol>
    """
