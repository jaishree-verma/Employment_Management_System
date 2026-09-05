package com.management.employee.service;

import com.management.employee.entity.Employee;
import com.management.employee.repository.EmployeeRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
public class EmployeeService {

    private final EmployeeRepository employeeRepository;

    @Autowired
    public EmployeeService(EmployeeRepository employeeRepository) {
        this.employeeRepository = employeeRepository;
    }

    // Add / Save a new employee
    public Employee saveEmployee(Employee employee) {
        return employeeRepository.save(employee);
    }

    // View all employees
    public List<Employee> getAllEmployees() {
        return employeeRepository.findAll();
    }

    // Find employee by ID
    public Optional<Employee> getEmployeeById(Long id) {
        return employeeRepository.findById(id);
    }

    // Update employee details
    public Employee updateEmployee(Long id, Employee updatedEmployeeDetails) {
        return employeeRepository.findById(id).map(existingEmployee -> {
            existingEmployee.setName(updatedEmployeeDetails.getName());
            existingEmployee.setEmail(updatedEmployeeDetails.getEmail());
            existingEmployee.setDepartment(updatedEmployeeDetails.getDepartment());
            existingEmployee.setSalary(updatedEmployeeDetails.getSalary());
            return employeeRepository.save(existingEmployee);
        }).orElseThrow(() -> new RuntimeException("Employee not found with ID: " + id));
    }

    // Delete an employee by ID
    public void deleteEmployee(Long id) {
        if (!employeeRepository.existsById(id)) {
            throw new RuntimeException("Employee not found with ID: " + id);
        }
        employeeRepository.deleteById(id);
    }

    // Search employees by department
    public List<Employee> getEmployeesByDepartment(String department) {
        return employeeRepository.findByDepartmentIgnoreCase(department);
    }
}
