// Employee Management System Client JavaScript - Black, Yellow & Light Theme

const API_BASE = '/employees';
let allEmployees = [];
let deleteTargetId = null;

// DOM Elements
const htmlElement = document.documentElement;
const themeToggleBtn = document.getElementById('themeToggleBtn');
const themeLabel = document.getElementById('themeLabel');

const employeeTableBody = document.getElementById('employeeTableBody');
const emptyState = document.getElementById('emptyState');
const searchInput = document.getElementById('searchInput');
const departmentFilter = document.getElementById('departmentFilter');
const refreshBtn = document.getElementById('refreshBtn');

// Stat Elements
const statTotalEmployees = document.getElementById('statTotalEmployees');
const statDepartments = document.getElementById('statDepartments');
const statTotalPayroll = document.getElementById('statTotalPayroll');
const statAvgSalary = document.getElementById('statAvgSalary');

// Modal Elements
const employeeModal = document.getElementById('employeeModal');
const modalTitle = document.getElementById('modalTitle');
const employeeForm = document.getElementById('employeeForm');
const empIdInput = document.getElementById('empId');
const empNameInput = document.getElementById('empName');
const empEmailInput = document.getElementById('empEmail');
const empDepartmentSelect = document.getElementById('empDepartment');
const empSalaryInput = document.getElementById('empSalary');
const openAddModalBtn = document.getElementById('openAddModalBtn');
const closeModalBtn = document.getElementById('closeModalBtn');
const cancelModalBtn = document.getElementById('cancelModalBtn');

// Delete Modal Elements
const deleteModal = document.getElementById('deleteModal');
const deleteEmpName = document.getElementById('deleteEmpName');
const closeDeleteModalBtn = document.getElementById('closeDeleteModalBtn');
const cancelDeleteBtn = document.getElementById('cancelDeleteBtn');
const confirmDeleteBtn = document.getElementById('confirmDeleteBtn');
const toastContainer = document.getElementById('toastContainer');

// Initialize Dashboard & Theme
document.addEventListener('DOMContentLoaded', () => {
    initTheme();
    loadEmployees();
    setupEventListeners();
});

// Theme Toggle Logic
function initTheme() {
    const savedTheme = localStorage.getItem('theme') || 'dark';
    setTheme(savedTheme);
}

function setTheme(theme) {
    htmlElement.setAttribute('data-theme', theme);
    localStorage.setItem('theme', theme);
    if (theme === 'light') {
        themeLabel.textContent = 'Dark Mode';
    } else {
        themeLabel.textContent = 'Light Mode';
    }
}

function toggleTheme() {
    const currentTheme = htmlElement.getAttribute('data-theme');
    const newTheme = currentTheme === 'light' ? 'dark' : 'light';
    setTheme(newTheme);
}

// Event Listeners Setup
function setupEventListeners() {
    // Theme Switcher Trigger
    themeToggleBtn.addEventListener('click', toggleTheme);

    // Refresh Button
    refreshBtn.addEventListener('click', loadEmployees);

    // Filter & Search
    searchInput.addEventListener('input', filterAndRender);
    departmentFilter.addEventListener('change', handleDepartmentFilter);

    // Add Employee Modal Trigger
    openAddModalBtn.addEventListener('click', () => openEmployeeModal());

    // Modal Close Triggers
    closeModalBtn.addEventListener('click', closeEmployeeModal);
    cancelModalBtn.addEventListener('click', closeEmployeeModal);

    // Form Submit
    employeeForm.addEventListener('submit', handleFormSubmit);

    // Delete Modal Triggers
    closeDeleteModalBtn.addEventListener('click', closeDeleteModal);
    cancelDeleteBtn.addEventListener('click', closeDeleteModal);
    confirmDeleteBtn.addEventListener('click', executeDelete);
}

// Fetch All Employees from Backend REST API
async function loadEmployees() {
    try {
        const response = await fetch(API_BASE);
        if (!response.ok) throw new Error('Failed to fetch employees');
        allEmployees = await response.json();
        filterAndRender();
        updateStats(allEmployees);
    } catch (error) {
        console.error('API Error:', error);
        showToast('Could not load employees from backend', 'error');
    }
}

// Handle Department Filter Selection
async function handleDepartmentFilter() {
    const selectedDept = departmentFilter.value;
    if (selectedDept === 'ALL') {
        loadEmployees();
    } else {
        try {
            const response = await fetch(`${API_BASE}/department/${encodeURIComponent(selectedDept)}`);
            if (!response.ok) throw new Error('Failed to filter department');
            const deptEmployees = await response.json();
            renderTable(deptEmployees);
            updateStats(allEmployees);
        } catch (error) {
            console.error('Filter Error:', error);
            showToast('Error filtering by department', 'error');
        }
    }
}

// Client-side Live Search & Render
function filterAndRender() {
    const query = searchInput.value.toLowerCase().trim();
    const filtered = allEmployees.filter(emp => 
        emp.name.toLowerCase().includes(query) ||
        emp.email.toLowerCase().includes(query) ||
        emp.department.toLowerCase().includes(query) ||
        emp.id.toString().includes(query)
    );
    renderTable(filtered);
}

// Render Table Rows
function renderTable(employees) {
    employeeTableBody.innerHTML = '';

    if (employees.length === 0) {
        emptyState.classList.remove('hidden');
        return;
    } else {
        emptyState.classList.add('hidden');
    }

    employees.forEach(emp => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td><strong>#${emp.id}</strong></td>
            <td>
                <div class="emp-info">
                    <span class="emp-name">${escapeHtml(emp.name)}</span>
                    <span class="emp-email">${escapeHtml(emp.email)}</span>
                </div>
            </td>
            <td>
                <span class="badge-dept">${escapeHtml(emp.department)}</span>
            </td>
            <td>
                <span class="salary-text">₹${Number(emp.salary).toLocaleString('en-IN')}</span>
            </td>
            <td class="text-right">
                <button class="action-btn edit" onclick="editEmployee(${emp.id})" title="Edit Employee">
                    <i class="fa-solid fa-pen"></i>
                </button>
                <button class="action-btn delete" onclick="confirmDelete(${emp.id}, '${escapeHtml(emp.name)}')" title="Delete Employee">
                    <i class="fa-solid fa-trash-can"></i>
                </button>
            </td>
        `;
        employeeTableBody.appendChild(row);
    });
}

// Update Dashboard Statistics Cards
function updateStats(employees) {
    const totalCount = employees.length;
    statTotalEmployees.textContent = totalCount;

    const departmentsSet = new Set(employees.map(e => e.department));
    statDepartments.textContent = departmentsSet.size;

    const totalPayroll = employees.reduce((sum, e) => sum + (e.salary || 0), 0);
    statTotalPayroll.textContent = `₹${totalPayroll.toLocaleString('en-IN')}`;

    const avgSalary = totalCount > 0 ? Math.round(totalPayroll / totalCount) : 0;
    statAvgSalary.textContent = `₹${avgSalary.toLocaleString('en-IN')}`;
}

// Open Add / Edit Modal
function openEmployeeModal(emp = null) {
    employeeForm.reset();
    if (emp) {
        modalTitle.innerHTML = '<i class="fa-solid fa-user-pen"></i> Edit Employee Details';
        empIdInput.value = emp.id;
        empNameInput.value = emp.name;
        empEmailInput.value = emp.email;
        empDepartmentSelect.value = emp.department;
        empSalaryInput.value = emp.salary;
    } else {
        modalTitle.innerHTML = '<i class="fa-solid fa-user-plus"></i> Add New Employee';
        empIdInput.value = '';
    }
    employeeModal.classList.remove('hidden');
}

function closeEmployeeModal() {
    employeeModal.classList.add('hidden');
}

// Handle Form Submission (Add or Update)
async function handleFormSubmit(event) {
    event.preventDefault();

    const id = empIdInput.value;
    const payload = {
        name: empNameInput.value.trim(),
        email: empEmailInput.value.trim(),
        department: empDepartmentSelect.value,
        salary: parseFloat(empSalaryInput.value)
    };

    try {
        let response;
        if (id) {
            response = await fetch(`${API_BASE}/${id}`, {
                method: 'PUT',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(payload)
            });
        } else {
            response = await fetch(API_BASE, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(payload)
            });
        }

        if (!response.ok) throw new Error('Operation failed');

        const savedEmployee = await response.json();
        showToast(`Employee "${savedEmployee.name}" saved successfully!`, 'success');
        closeEmployeeModal();
        loadEmployees();
    } catch (error) {
        console.error('Save Error:', error);
        showToast('Failed to save employee. Please check inputs.', 'error');
    }
}

// Trigger Edit Mode
function editEmployee(id) {
    const emp = allEmployees.find(e => e.id === id);
    if (emp) {
        openEmployeeModal(emp);
    }
}

// Trigger Delete Confirmation Modal
function confirmDelete(id, name) {
    deleteTargetId = id;
    deleteEmpName.textContent = name;
    deleteModal.classList.remove('hidden');
}

function closeDeleteModal() {
    deleteModal.classList.add('hidden');
    deleteTargetId = null;
}

// Execute Delete API Request (DELETE /employees/{id})
async function executeDelete() {
    if (!deleteTargetId) return;

    try {
        const response = await fetch(`${API_BASE}/${deleteTargetId}`, {
            method: 'DELETE'
        });

        if (!response.ok) throw new Error('Failed to delete');

        showToast('Employee deleted successfully', 'info');
        closeDeleteModal();
        loadEmployees();
    } catch (error) {
        console.error('Delete Error:', error);
        showToast('Error deleting employee', 'error');
    }
}

// Toast Notifications Helper
function showToast(message, type = 'info') {
    const toast = document.createElement('div');
    toast.className = `toast ${type}`;
    
    let icon = 'fa-info-circle';
    if (type === 'success') icon = 'fa-check-circle';
    if (type === 'error') icon = 'fa-exclamation-circle';

    toast.innerHTML = `<i class="fa-solid ${icon}"></i> <span>${escapeHtml(message)}</span>`;
    toastContainer.appendChild(toast);

    setTimeout(() => {
        toast.style.opacity = '0';
        toast.style.transform = 'translateX(100%)';
        setTimeout(() => toast.remove(), 300);
    }, 3500);
}

// Utility: Escape HTML String
function escapeHtml(str) {
    if (!str) return '';
    return str.toString()
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/"/g, "&quot;")
        .replace(/'/g, "&#039;");
}
