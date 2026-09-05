package com.management.employee;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.management.employee.entity.Employee;
import com.management.employee.repository.EmployeeRepository;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.AutoConfigureMockMvc;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.http.MediaType;
import org.springframework.test.context.ActiveProfiles;
import org.springframework.test.context.TestPropertySource;
import org.springframework.test.web.servlet.MockMvc;

import static org.hamcrest.Matchers.*;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.*;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.*;

@SpringBootTest
@AutoConfigureMockMvc
@ActiveProfiles("test")
@TestPropertySource(locations = "classpath:application-test.properties")
public class EmployeeControllerTest {

    @Autowired
    private MockMvc mockMvc;

    @Autowired
    private EmployeeRepository employeeRepository;

    @Autowired
    private ObjectMapper objectMapper;

    @BeforeEach
    void setUp() {
        employeeRepository.deleteAll();
    }

    @Test
    void testAddEmployee() throws Exception {
        Employee employee = new Employee("Rahul", "rahul@gmail.com", "IT", 50000.0);

        mockMvc.perform(post("/employees")
                .contentType(MediaType.APPLICATION_JSON)
                .content(objectMapper.writeValueAsString(employee)))
                .andExpect(status().isCreated())
                .andExpect(jsonPath("$.id", notNullValue()))
                .andExpect(jsonPath("$.name", is("Rahul")))
                .andExpect(jsonPath("$.email", is("rahul@gmail.com")))
                .andExpect(jsonPath("$.department", is("IT")))
                .andExpect(jsonPath("$.salary", is(50000.0)));
    }

    @Test
    void testGetAllEmployees() throws Exception {
        employeeRepository.save(new Employee("Rahul", "rahul@gmail.com", "IT", 50000.0));
        employeeRepository.save(new Employee("Priya", "priya@gmail.com", "HR", 60000.0));

        mockMvc.perform(get("/employees"))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$", hasSize(2)))
                .andExpect(jsonPath("$[0].name", is("Rahul")))
                .andExpect(jsonPath("$[1].name", is("Priya")));
    }

    @Test
    void testGetEmployeeById() throws Exception {
        Employee saved = employeeRepository.save(new Employee("Rahul", "rahul@gmail.com", "IT", 50000.0));

        mockMvc.perform(get("/employees/" + saved.getId()))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.id", is(saved.getId().intValue())))
                .andExpect(jsonPath("$.name", is("Rahul")));
    }

    @Test
    void testUpdateEmployee() throws Exception {
        Employee saved = employeeRepository.save(new Employee("Rahul", "rahul@gmail.com", "IT", 50000.0));
        Employee updateDetails = new Employee("Rahul Sharma", "rahul.sharma@gmail.com", "IT", 65000.0);

        mockMvc.perform(put("/employees/" + saved.getId())
                .contentType(MediaType.APPLICATION_JSON)
                .content(objectMapper.writeValueAsString(updateDetails)))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.name", is("Rahul Sharma")))
                .andExpect(jsonPath("$.email", is("rahul.sharma@gmail.com")))
                .andExpect(jsonPath("$.salary", is(65000.0)));
    }

    @Test
    void testGetEmployeesByDepartment() throws Exception {
        employeeRepository.save(new Employee("Rahul", "rahul@gmail.com", "IT", 50000.0));
        employeeRepository.save(new Employee("Amit", "amit@gmail.com", "IT", 55000.0));
        employeeRepository.save(new Employee("Priya", "priya@gmail.com", "HR", 60000.0));

        mockMvc.perform(get("/employees/department/IT"))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$", hasSize(2)))
                .andExpect(jsonPath("$[0].department", is("IT")))
                .andExpect(jsonPath("$[1].department", is("IT")));
    }

    @Test
    void testDeleteEmployee() throws Exception {
        Employee saved = employeeRepository.save(new Employee("Rahul", "rahul@gmail.com", "IT", 50000.0));

        mockMvc.perform(delete("/employees/" + saved.getId()))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.message", containsString("deleted successfully")));

        mockMvc.perform(get("/employees/" + saved.getId()))
                .andExpect(status().isNotFound());
    }
}
