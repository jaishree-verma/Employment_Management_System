package com.management.employee.repository;

import com.management.employee.entity.Employee;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface EmployeeRepository extends JpaRepository<Employee, Long> {

    // Custom finder method to search employees by department (case-insensitive)
    List<Employee> findByDepartmentIgnoreCase(String department);
}
