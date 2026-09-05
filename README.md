# Employee Management System

A full-stack, enterprise-ready Employee Management System built with Java 23, Spring Boot 3.3, Spring Data JPA, Hibernate, MySQL/H2 Database, and a vanilla CSS Single-Page Application (SPA) Web Dashboard.

Live Demo: https://employee-management-system-2ne1.onrender.com/  
GitHub Repository: https://github.com/jaishree-verma/Employment_Management_System

---

## Table of Contents
- [Problem Statement](#problem-statement)
- [Solution](#solution)
- [System Architecture & Implementation](#system-architecture--implementation)
- [Key Features](#key-features)
- [API Endpoint Specifications](#api-endpoint-specifications)
- [Frontend Dashboard & UI Design](#frontend-dashboard--ui-design)
- [Testing & Quality Assurance](#testing--quality-assurance)
- [Local Installation & Setup](#local-installation--setup)
- [Deployment](#deployment)
- [Future Enhancements](#future-enhancements)
- [License](#license)

---

## Problem Statement

Managing employee data across departments, tracking payroll allocations, and performing record updates in traditional spreadsheet-based or fragmented systems presents significant challenges:

1. **Data Inconsistency & Redundancy**: Manual tracking leads to duplicate entries, mismatched records, and lack of validation.
2. **Inefficient Searching & Filtering**: Finding records by employee ID or department requires manual scanning or complex spreadsheet queries.
3. **Lack of Standardized Interfaces**: Fragmented tools lack a uniform RESTful API interface for web dashboard integration, reporting tools, or third-party service consuming.
4. **Complex Initial Setup**: Developing backend solutions often requires heavy database setup, hindering quick testing, demonstration, and onboarding.

---

## Solution

The Employee Management System addresses these challenges by offering a centralized, performant backend service and a responsive web client:

1. **Centralized RESTful API**: Built on Spring Boot and Spring Data JPA, exposing standardized HTTP endpoints for complete employee Lifecycle Management (Create, Read, Update, Delete).
2. **Automated Department & ID Queries**: Optimized database queries for real-time filtering by department and instant lookup by ID.
3. **Dual Persistence Configuration**: Configured with dual profile support:
   - **Production / MySQL Profile**: Persistent relational storage using MySQL Server.
   - **Development / H2 Profile**: Zero-config, zero-dependency in-memory database for immediate local execution and testing.
4. **Interactive Single-Page Web Dashboard**: A light and dark mode web interface providing live statistical summaries (Total Headcount, Active Departments, Total Payroll, Average Salary) and real-time record management.

---

## System Architecture & Implementation

### Layered Architecture Pattern

The backend is structured according to the classic 4-tier layered software architecture:

```text
HTTP Request (Client Browser / Postman)
       │
       ▼
[ Controller Layer ]      EmployeeController.java (@RestController)
       │                  - Maps HTTP routes (/employees)
       │                  - Handles request payloads and HTTP status codes
       ▼
[ Service Layer ]         EmployeeService.java (@Service)
       │                  - Business logic validation
       │                  - Exception handling for missing records
       ▼
[ Repository Layer ]      EmployeeRepository.java (JpaRepository<Employee, Long>)
       │                  - Spring Data JPA abstraction
       │                  - Custom query derivation (findByDepartmentIgnoreCase)
       ▼
[ Database Layer ]        Employee.java (@Entity) <---> MySQL / H2 Database
```

### Technology Stack

- **Backend Framework**: Java 23, Spring Boot 3.3.3, Spring Data JPA, Hibernate ORM
- **Web Server**: Embedded Apache Tomcat 10.1
- **Database Engine**: MySQL 8.0 (Persistent) / H2 Database (In-Memory)
- **Build & Dependency Management**: Apache Maven 3.9 & Maven Wrapper (`mvnw`)
- **Frontend Technologies**: HTML5, Vanilla CSS3 (Custom Glassmorphism Design System, CSS Variables), Vanilla JavaScript (Fetch API, DOM Manipulation)
- **Containerization & Deployment**: Docker (Multi-stage build), Render Cloud Platform

---

## Key Features

- **Employee Lifecycle Management**: Add new employees, view full roster, lookup by ID, edit employee details, and delete entries.
- **Department-Based Filtering**: Search employees by department name case-insensitively using JPA derived queries.
- **Live Analytical Dashboard**: Computes aggregate metrics dynamically (headcount, payroll totals, average compensation, department breakdown).
- **Dual Color Themes**: Built-in Black & Cyberpunk Yellow dark mode alongside a clean Light Mode, with theme preferences saved in browser local storage.
- **Real-Time Client-Side Search**: Filter employee records by name, email, department, or ID without full page reloads.

---

## API Endpoint Specifications

Base Path: `/employees`

| HTTP Method | Endpoint Path | Description | Request Body Example | Success Status |
| :--- | :--- | :--- | :--- | :--- |
| `POST` | `/employees` | Add a new employee | `{"name": "Rahul", "email": "rahul@gmail.com", "department": "IT", "salary": 50000}` | `201 Created` |
| `GET` | `/employees` | Retrieve all employees | None | `200 OK` |
| `GET` | `/employees/{id}` | Retrieve employee by ID | None | `200 OK` / `404 Not Found` |
| `PUT` | `/employees/{id}` | Update employee details | `{"name": "Rahul Sharma", "email": "rahul.sharma@gmail.com", "department": "IT", "salary": 65000}` | `200 OK` / `404 Not Found` |
| `DELETE` | `/employees/{id}` | Delete employee by ID | None | `200 OK` / `404 Not Found` |
| `GET` | `/employees/department/{department}` | Search employees by department | None | `200 OK` |

---

## Frontend Dashboard & UI Design

The frontend is served directly by Spring Boot from `src/main/resources/static/`:

1. **index.html**: Semantic HTML5 layout featuring header branding, stat counter cards, search control panel, data table, and modal dialogs.
2. **styles.css**: Custom styling featuring a Black and Yellow dark mode palette (`#090a0d` and `#facc15`), light mode system overrides (`[data-theme="light"]`), responsive CSS grid, and modal transition animations.
3. **app.js**: Asynchronous JavaScript executing REST API calls via the Fetch API, managing DOM states, updating aggregate statistics, and rendering toast notifications.

---

## Testing & Quality Assurance

### Automated Integration Testing

Automated integration tests are implemented in `src/test/java/com/management/employee/EmployeeControllerTest.java` using Spring Boot Test, MockMvc, and an isolated H2 in-memory test database.

Tested scenarios include:
- `testAddEmployee`: Validates `POST /employees` returns `201 Created` with generated primary key.
- `testGetAllEmployees`: Validates `GET /employees` returns full collection.
- `testGetEmployeeById`: Validates single record retrieval by primary key.
- `testUpdateEmployee`: Validates `PUT /employees/{id}` updates attributes.
- `testGetEmployeesByDepartment`: Validates custom query execution for department filtering.
- `testDeleteEmployee`: Validates record deletion and subsequent `404 Not Found` assertion.

### Executing Automated Tests

Run the following command in terminal:
```bash
./mvnw test
```

Expected Output:
```text
[INFO] Running com.management.employee.EmployeeControllerTest
[INFO] Tests run: 6, Failures: 0, Errors: 0, Skipped: 0, Time elapsed: 11.88 s
[INFO] BUILD SUCCESS
```

### Postman Collection Testing

A pre-configured Postman Collection is included at `Employee_Management_API.postman_collection.json`.

To test via Postman:
1. Open Postman.
2. Click **Import** and select `Employee_Management_API.postman_collection.json`.
3. Execute request scenarios against `http://localhost:8080/`.

---

## Local Installation & Setup

### Prerequisites

- Java Development Kit (JDK 17 or Java 23) installed.
- Git CLI.
- (Optional) MySQL Server 8.0 installed if running with MySQL profile.

### Step 1: Clone Repository
```bash
git clone https://github.com/jaishree-verma/Employment_Management_System.git
cd Employment_Management_System
```

### Step 2: Run with In-Memory H2 Database (Recommended for Quick Setup)

No database configuration required. Run:

On Windows PowerShell:
```powershell
.\mvnw.cmd spring-boot:run "-Dspring-boot.run.profiles=h2"
```

On Linux / macOS:
```bash
./mvnw spring-boot:run -Dspring-boot.run.profiles=h2
```

Access Points:
- Web Dashboard: `http://localhost:8080/`
- H2 Console: `http://localhost:8080/h2-console` (JDBC URL: `jdbc:h2:mem:employee_db`, Username: `sa`, Password: *blank*)

### Step 3: Run with MySQL Database

1. Ensure MySQL Server is running on port `3306`.
2. Update database credentials in `src/main/resources/application.properties`:
   ```properties
   spring.datasource.url=jdbc:mysql://localhost:3306/employee_db?createDatabaseIfNotExist=true&useSSL=false&allowPublicKeyRetrieval=true&serverTimezone=UTC
   spring.datasource.username=root
   spring.datasource.password=YOUR_MYSQL_PASSWORD
   ```
3. Execute:
   ```bash
   ./mvnw spring-boot:run
   ```

---

## Deployment

### Dockerized Cloud Deployment

The repository includes a multi-stage `Dockerfile` utilizing an official Maven build stage and lightweight Alpine JRE runtime stage.

#### Local Container Execution using Docker Compose

To start both MySQL database container and Spring Boot application container simultaneously:
```bash
docker compose up -d
```

#### Production Deployment on Render

1. Create a new Web Service on Render.com connected to repository `jaishree-verma/Employment_Management_System`.
2. Select **Docker** environment. Render automatically detects the repository `Dockerfile`.
3. Select the **Free** compute plan and click **Deploy Web Service**.

Live Deployment URL: https://employee-management-system-2ne1.onrender.com/

---

## Future Enhancements

The following features are planned for future iterations:

1. **Security & Authentication**: Implement Spring Security with JWT (JSON Web Tokens) and Role-Based Access Control (RBAC) to distinguish Admin and Employee permissions.
2. **Attendance & Leave Management**: Track daily attendance logs, leave balances, and approval workflows.
3. **Data Export & Reporting**: Enable exporting employee rosters and payroll reports to CSV, Excel, and PDF formats.
4. **Audit Logging & Soft Deletes**: Track modifications (created by, updated by timestamps) and implement soft-delete mechanisms for historical record retention.
5. **Pagination & Sorting**: Implement Spring Data `Pageable` and `Sort` interface support for scaling large employee datasets.

---

## License

This project is open-source software licensed under the [MIT License](LICENSE).
