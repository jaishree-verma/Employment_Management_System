# Employee Management System (Spring Boot + JPA + MySQL + Web UI)

A full-stack Employee Management System built using **Java 23**, **Spring Boot 3.3**, **Spring Data JPA**, **MySQL / H2 Database**, and a **Dark Glassmorphic Web Dashboard**.

---

## Key Features

-  **RESTful API**: Full CRUD capabilities for employee records.
-  **Glassmorphism Web Dashboard**: Responsive single-page interface with live stats, search bar, department filters, and action modals.
-  **Department Search**: Custom JPA query to search employees by department.
-  **Dual Database Profiles**:
  - `default`: MySQL persistence (`employee_db`).
  - `h2`: Instant in-memory database with web console (`/h2-console`).
-  **Postman Collection**: Exported JSON collection (`Employee_Management_API.postman_collection.json`) for endpoint testing.
-  **Automated Test Suite**: 100% passing MockMvc integration tests (`EmployeeControllerTest.java`).

---

##  Tech Stack & Layered Architecture

```
Client Browser / Postman
         ↓
  [Controller]      EmployeeController.java (@RestController, @RequestMapping("/employees"))
         ↓
   [Service]        EmployeeService.java (@Service business logic & error handling)
         ↓
  [Repository]      EmployeeRepository.java (JpaRepository<Employee, Long>)
         ↓
  [Entity / DB]     Employee.java (@Entity) ──> MySQL / H2 Database
```

- **Backend**: Java 23, Spring Boot 3.3, Spring Data JPA, Hibernate, Maven.
- **Frontend**: HTML5, Vanilla CSS3 (Glassmorphism, Google Font `Outfit`), JavaScript (Fetch API).
- **Database**: MySQL / H2 In-Memory.

---

## REST API Specification

| Method | Endpoint | Description | Sample Request Body |
| :--- | :--- | :--- | :--- |
| `POST` | `/employees` | Create a new employee | `{"name": "Rahul", "email": "rahul@gmail.com", "department": "IT", "salary": 50000}` |
| `GET` | `/employees` | Get list of all employees | N/A |
| `GET` | `/employees/{id}` | Get employee by ID | N/A |
| `PUT` | `/employees/{id}` | Update employee details | `{"name": "Rahul Sharma", "email": "rahul.sharma@gmail.com", "department": "IT", "salary": 65000}` |
| `GET` | `/employees/department/{dept}` | Filter employees by department | N/A |
| `DELETE` | `/employees/{id}` | Delete employee by ID | N/A |

---

##  Getting Started

### 1. Clone Repository
```bash
git clone https://github.com/jaishree-verma/atomgoal.git
cd Employment_Management_System
```

### 2. Run Application (Option A: In-Memory H2 Database)
No database setup needed:
```powershell
.\mvnw.cmd spring-boot:run "-Dspring-boot.run.profiles=h2"
```
- **Web UI**: Open `http://localhost:8080/`
- **H2 Console**: Open `http://localhost:8080/h2-console`

### 3. Run Application (Option B: Local MySQL Database)
1. Ensure MySQL is running on port 3306.
2. Update database credentials in `src/main/resources/application.properties`:
   ```properties
   spring.datasource.username=root
   spring.datasource.password=your_mysql_password
   ```
3. Execute:
   ```powershell
   .\mvnw.cmd spring-boot:run
   ```

### 4. Run Automated Tests
```powershell
.\mvnw.cmd test
```

---

##  License
Licensed under the [MIT License](LICENSE).
