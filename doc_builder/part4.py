# Part 4: Sections 46 through 60 (Simple English Revision Guide)

def get_part4_html():
    return r"""
    <!-- ==================== SECTION 46: DOCKER ==================== -->
    <div class="page-break"></div>
    <h1 class="section-title"><span class="section-number">46</span> Dockerfile Explained (Line by Line)</h1>
    
    <p>A Dockerfile is a recipe that builds a container image for our project. Here is our <code>Dockerfile</code>:</p>

    <pre><code># Stage 1: Build the JAR file
FROM maven:3.9.9-eclipse-temurin-17-alpine AS build
WORKDIR /app
COPY pom.xml .
RUN mvn dependency:go-offline -B
COPY src src
RUN mvn clean package -DskipTests

# Stage 2: Create the small runtime image
FROM eclipse-temurin:17-jre-alpine
WORKDIR /app
COPY --from=build /app/target/employee-management-0.0.1-SNAPSHOT.jar app.jar
EXPOSE 8080
ENTRYPOINT ["java", "-jar", "app.jar", "--spring.profiles.active=h2"]</code></pre>

    <!-- ==================== SECTION 47: WHY MULTI-STAGE DOCKER? ==================== -->
    <h1 class="section-title"><span class="section-number">47</span> Why Use a Multi-Stage Docker Build?</h1>
    
    <div class="diagram-box">
        <div class="diagram-caption">Stage 1 vs Stage 2 in Docker</div>
        <p style="font-family: monospace; font-size: 8.5pt;">
            [ Stage 1: Heavy Build Image (~850 MB) ]<br>
            Has Java Compiler, Maven, Source Code &rarr; Compiles app.jar &rarr; Discarded!<br>
            &darr; Only app.jar is copied over<br>
            [ Stage 2: Clean Lightweight JRE Image (~180 MB) ]<br>
            Has ONLY the lightweight JRE and app.jar &rarr; Deployed to Cloud!
        </p>
    </div>

    <ul>
        <li><strong>Saves 75% Disk Space:</strong> Our final container image is only around 180 MB instead of almost 1 GB!</li>
        <li><strong>More Secure:</strong> The final container does not have compilers, build tools, or source code inside it. Attackers cannot compile anything if they break in.</li>
    </ul>

    <!-- ==================== SECTION 48: DOCKER COMPOSE ==================== -->
    <h1 class="section-title"><span class="section-number">48</span> Docker Compose (Running App + MySQL Together)</h1>
    
    <p><code>docker-compose.yml</code> lets you start both the Spring Boot app and a MySQL database with a single command: <code>docker compose up -d</code>.</p>
    <ul>
        <li><strong>Service 1 (mysqldb):</strong> Runs official MySQL 8.0 on port 3306. Saves database files permanently inside a volume named <code>db_data</code>.</li>
        <li><strong>Service 2 (app):</strong> Builds our Spring Boot app from the Dockerfile, exposes port 8080, and connects to the MySQL container over an internal Docker network.</li>
    </ul>

    <!-- ==================== SECTION 49: CLOUD DEPLOYMENT ON RENDER ==================== -->
    <h1 class="section-title"><span class="section-number">49</span> Cloud Deployment on Render</h1>
    
    <p>Our project is deployed live on the internet using <strong>Render</strong> at:<br>
    <strong>https://employee-management-system-2ne1.onrender.com/</strong></p>
    
    <p><strong>How the deployment works:</strong></p>
    <ol>
        <li>Whenever we push new code to GitHub, Render detects the push.</li>
        <li>Render reads our <code>Dockerfile</code> and builds the Docker container image.</li>
        <li>Render starts the container and maps port 8080 to a public HTTPS web address.</li>
    </ol>

    <!-- ==================== SECTION 50: WHY RENDER? ==================== -->
    <h1 class="section-title"><span class="section-number">50</span> Why Render? (And not AWS or Azure?)</h1>
    
    <ul>
        <li><strong>Simple &amp; Free:</strong> AWS ECS and Kubernetes require complex networking, security groups, and cost money every month. Render gives us free container hosting without credit card charges.</li>
        <li><strong>Automatic HTTPS:</strong> Render automatically gives us an SSL certificate (padlock icon) for free.</li>
        <li><strong>GitHub Integration:</strong> Git push &rarr; automatic deployment!</li>
    </ul>

    <!-- ==================== SECTION 51: HOW TO RUN LOCALLY ==================== -->
    <h1 class="section-title"><span class="section-number">51</span> Step-by-Step Guide: How to Run on Your Laptop</h1>
    
    <div class="box-note">
        <div class="box-title">Option A: The Fastest Way (Zero Installation with H2 Database)</div>
        Open PowerShell / Terminal in the project folder and type:<br>
        <strong>Windows:</strong> <code>.\mvnw.cmd spring-boot:run "-Dspring-boot.run.profiles=h2"</code><br>
        <strong>Mac / Linux:</strong> <code>./mvnw spring-boot:run -Dspring-boot.run.profiles=h2</code><br>
        Open your browser and visit: <strong>http://localhost:8080/</strong><br>
        You can also view the H2 Database Console at: <strong>http://localhost:8080/h2-console</strong>
    </div>

    <div class="box-note">
        <div class="box-title">Option B: Run with MySQL and Docker</div>
        If you have Docker Desktop installed, just run:<br>
        <code>docker compose up -d</code><br>
        Both the MySQL database and the Spring Boot application will start automatically.
    </div>

    <div class="box-note">
        <div class="box-title">Option C: Run Automated Tests</div>
        To run all 6 integration tests, type:<br>
        <code>.\mvnw.cmd test</code> (Windows) or <code>./mvnw test</code> (Mac/Linux)
    </div>

    <!-- ==================== SECTION 52: CONFIGURATION FILES ==================== -->
    <h1 class="section-title"><span class="section-number">52</span> Configuration Files Explained</h1>
    
    <ul>
        <li><code>application.properties</code>: Used when running with MySQL. Contains MySQL URL (<code>localhost:3306/employee_db</code>), username, and password.</li>
        <li><code>application-h2.properties</code>: Used when running with H2. Uses memory database URL (<code>jdbc:h2:mem:employee_db</code>) and enables the web console.</li>
        <li><code>application-test.properties</code>: Used only when running automated tests (<code>jdbc:h2:mem:testdb</code>) so tests don't touch development data.</li>
    </ul>

    <!-- ==================== SECTION 53: DIRECTORY STRUCTURE ==================== -->
    <h1 class="section-title"><span class="section-number">53</span> Project Folder Structure Tree</h1>
    
    <pre><code>Employment_Management_System/
├── src/
│   ├── main/
│   │   ├── java/com/management/employee/
│   │   │   ├── EmployeeManagementApplication.java # Main class with main() method
│   │   │   ├── controller/EmployeeController.java # REST API endpoints (/employees)
│   │   │   ├── entity/Employee.java               # Database table entity blueprint
│   │   │   ├── repository/EmployeeRepository.java # Database CRUD interface
│   │   │   └── service/EmployeeService.java       # Business logic operations
│   │   └── resources/
│   │       ├── application.properties             # MySQL settings
│   │       ├── application-h2.properties          # H2 memory database settings
│   │       └── static/
│   │           ├── index.html                     # Webpage HTML
│   │           ├── styles.css                     # Webpage styles & themes
│   │           └── app.js                         # JavaScript frontend logic
│   └── test/
│       ├── java/com/management/employee/
│       │   └── EmployeeControllerTest.java        # 6 automated MockMvc tests
│       └── resources/
│           └── application-test.properties        # Test database settings
├── Dockerfile                                     # Docker container blueprint
├── docker-compose.yml                             # Multi-container setup (App + MySQL)
├── Employee_Management_API.postman_collection.json# Postman tests file
├── pom.xml                                        # Maven dependencies and versions
└── README.md                                      # Documentation file</code></pre>

    <!-- ==================== SECTION 54: CODE QUALITY REVIEW ==================== -->
    <h1 class="section-title"><span class="section-number">54</span> Code Quality Review (Good Points &amp; Future Fixes)</h1>
    
    <div class="row-2">
        <div class="col-2">
            <p><strong>Good Things in the Code:</strong></p>
            <ul>
                <li>Constructor injection used everywhere (safe and easy to test).</li>
                <li>Clean naming for all variables and functions.</li>
                <li>HTML escaping in JavaScript (<code>escapeHtml()</code>) prevents XSS injection bugs.</li>
                <li>Clean separation: Controller does HTTP, Service does logic, Repository does database.</li>
            </ul>
        </div>
        <div class="col-2">
            <p><strong>Things That Can Be Improved:</strong></p>
            <ul>
                <li>Add a DTO layer (Data Transfer Objects) instead of exposing the database Entity directly.</li>
                <li>Use <code>@ControllerAdvice</code> for global error handling instead of try-catch blocks.</li>
                <li>Add <code>@NotBlank</code> and <code>@Positive</code> annotations for backend input validation.</li>
            </ul>
        </div>
    </div>

    <!-- ==================== SECTION 55: DESIGN PATTERNS ==================== -->
    <h1 class="section-title"><span class="section-number">55</span> Design Patterns Used in the Project</h1>
    
    <ul>
        <li><strong>Layered Pattern:</strong> Splitting the app into Controller &rarr; Service &rarr; Repository &rarr; Database.</li>
        <li><strong>Repository Pattern:</strong> Using <code>EmployeeRepository</code> interface to hide database details from the rest of the application.</li>
        <li><strong>Dependency Injection (DI / IoC):</strong> Spring Boot creates objects (beans) and injects them into constructors automatically.</li>
        <li><strong>Singleton Pattern:</strong> Spring Boot creates only one instance of <code>EmployeeService</code> and <code>EmployeeRepository</code> and shares it across the app.</li>
    </ul>

    <!-- ==================== SECTION 56: PERFORMANCE ==================== -->
    <h1 class="section-title"><span class="section-number">56</span> Performance Review</h1>
    
    <ul>
        <li><strong>Query Speed:</strong> H2 database queries finish in under 5 milliseconds.</li>
        <li><strong>Search Speed:</strong> Searching in the browser table is instant (under 10 milliseconds) because JavaScript searches in memory.</li>
        <li><strong>Transparency:</strong> Note that no formal multi-user stress testing (like 10,000 users at once) was done on this project.</li>
    </ul>

    <!-- ==================== SECTION 57: SCALABILITY PLAN ==================== -->
    <h1 class="section-title"><span class="section-number">57</span> Scalability Plan (What If Employee Count Grows?)</h1>
    
    <ul>
        <li><strong>100 to 1,000 Employees:</strong> The current project works smoothly without any changes.</li>
        <li><strong>10,000 Employees:</strong> Sending 10,000 employees in one JSON list will be too slow. We should add <strong>pagination</strong> (showing 50 employees per page: <code>?page=0&amp;size=50</code>).</li>
        <li><strong>100,000+ Employees:</strong> We should add an index to the <code>department</code> column in MySQL (<code>CREATE INDEX idx_dept ON employees(department)</code>) and use Redis cache for frequently searched data.</li>
    </ul>

    <!-- ==================== SECTION 58: CURRENT LIMITATIONS ==================== -->
    <h1 class="section-title"><span class="section-number">58</span> Current Limitations (Being Completely Honest)</h1>
    
    <ul>
        <li>No login screen or password protection (anyone who visits the site can view/delete).</li>
        <li>No pagination (all records are loaded in one big list).</li>
        <li>Only 1 database table (no separate table for departments or managers).</li>
        <li>Hard delete (when you delete an employee, the row is permanently gone—no recycle bin).</li>
    </ul>

    <!-- ==================== SECTION 59: FUTURE ENHANCEMENTS ==================== -->
    <h1 class="section-title"><span class="section-number">59</span> Future Enhancements (What to Build Next)</h1>
    
    <ul>
        <li><strong>Spring Security + JWT:</strong> Add login screen and assign roles (Admin vs Regular User).</li>
        <li><strong>Attendance &amp; Leave:</strong> Track daily attendance and allow employees to request time off.</li>
        <li><strong>Export to PDF / Excel:</strong> Add a button to download the employee table or salary slips.</li>
        <li><strong>Soft Delete:</strong> Keep deleted records marked as <code>is_deleted = true</code> so history is preserved.</li>
    </ul>

    <!-- ==================== SECTION 60: WHY THESE FEATURES? ==================== -->
    <h1 class="section-title"><span class="section-number">60</span> Why These Features? (Managing Scope)</h1>
    
    <p>Why did we build employee CRUD, department filtering, and statistics instead of building attendance or payroll first?</p>
    <ul>
        <li><strong>First Things First:</strong> You cannot have attendance or payroll without a working employee list first! Employee management is the core foundation.</li>
        <li><strong>Keep It Reliable:</strong> Instead of building 10 half-working features, we built 6 solid features with 100% working automated tests, Docker containerization, and live cloud deployment.</li>
    </ul>
    """
