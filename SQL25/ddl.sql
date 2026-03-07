-- Employees
CREATE TABLE employees (
    emp_id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    dept_id INT,
    salary NUMERIC(10, 2),
    manager_id INT,  -- self-referencing FK
    hire_date DATE
);

-- Departments
CREATE TABLE departments (
    dept_id SERIAL PRIMARY KEY,
    dept_name VARCHAR(100),
    location VARCHAR(100)
);

-- Projects
CREATE TABLE projects (
    project_id SERIAL PRIMARY KEY,
    project_name VARCHAR(100),
    budget NUMERIC(12, 2),
    dept_id INT
);

-- Employee-Project mapping (many-to-many)
CREATE TABLE emp_projects (
    emp_id INT,
    project_id INT,
    role VARCHAR(50),
    hours_worked INT,
    PRIMARY KEY (emp_id, project_id)
);

-- Sales
CREATE TABLE sales (
    sale_id SERIAL PRIMARY KEY,
    emp_id INT,
    sale_date DATE,
    amount NUMERIC(10, 2),
    region VARCHAR(50)
);

-- Seed Data
INSERT INTO departments VALUES (1, 'Engineering', 'NYC'), (2, 'Marketing', 'LA'), (3, 'HR', 'Chicago'), (4, 'Finance', 'NYC');

INSERT INTO employees VALUES
(1, 'Alice',   1, 95000, NULL,  '2018-03-01'),
(2, 'Bob',     1, 85000, 1,    '2019-06-15'),
(3, 'Carol',   2, 72000, NULL,  '2020-01-10'),
(4, 'Dave',    2, 68000, 3,    '2021-03-22'),
(5, 'Eve',     3, 61000, NULL,  '2017-09-01'),
(6, 'Frank',   1, 91000, 1,    '2016-11-30'),
(7, 'Grace',   4, 105000,NULL, '2015-07-19'),
(8, 'Hank',    4, 98000, 7,    '2018-02-28'),
(9, 'Ivy',     3, 59000, 5,    '2022-04-05'),
(10,'Jake',    NULL, 55000, NULL,'2023-01-01'); -- no department

INSERT INTO projects VALUES
(1, 'Alpha', 500000, 1),
(2, 'Beta',  300000, 2),
(3, 'Gamma', 150000, 1),
(4, 'Delta', 200000, NULL); -- unassigned dept

INSERT INTO emp_projects VALUES
(1, 1, 'Lead',    120),
(2, 1, 'Member',  80),
(2, 3, 'Lead',    60),
(3, 2, 'Lead',    100),
(4, 2, 'Member',  50),
(6, 1, 'Member',  90),
(6, 3, 'Member',  45),
(7, 4, 'Lead',    70);

INSERT INTO sales VALUES
(1,  2, '2025-01-05', 12000, 'East'),
(2,  2, '2025-01-20', 8000,  'West'),
(3,  3, '2025-02-01', 15000, 'East'),
(4,  4, '2025-02-14', 7000,  'West'),
(5,  2, '2025-03-10', 20000, 'East'),
(6,  3, '2025-03-22', 9000,  'West'),
(7,  6, '2025-04-01', 11000, 'East'),
(8,  6, '2025-04-15', 13000, 'East'),
(9,  2, '2025-05-01', 5000,  'West'),
(10, 3, '2025-05-20', 18000, 'East'),
(11, 8, '2025-06-01', 22000, 'East'),
(12, 8, '2025-06-15', 3000,  'West');