# Tuition Management System

A Django-based system for managing student tuition payments and fees.

## Use Case Diagram

```
+----------------------------------------------------------------------------------------+
|                                Tuition Management System                                 |
+----------------------------------------------------------------------------------------+
                                          
    +---------------+
    |               |                                     +--------------------+
    |               |-----> View Student List             |                    |
    |               |                                     |                    |
    |    Student    |-----> View Payment History          |                    |
    |               |                                     |                    |
    |               |-----> Make Payment                  |                    |
    |               |                                     |    System Admin    |
    +---------------+                                     |                    |
                                                         |                    |
    +---------------+                                    |                    |
    |               |-----> Manage Students ------------>|                    |
    |               |                                    |                    |
    |     Staff     |-----> Process Payments ----------->|                    |
    |               |                                    |                    |
    |               |-----> View Reports                 |                    |
    |               |                                    |                    |
    +---------------+                                    +--------------------+
                                                         |
                                                         |
    +---------------+     +-----------------------+      |
    |  Financial    |---->| Generate Reports      |<-----|
    |   Officer     |     +-----------------------+
    +---------------+     | Manage Fee Structure  |<-----|
                         +-----------------------+
                         | View Financial Stats  |<-----|
                         +-----------------------+

```

## Actors and Their Roles

1. Student
   - View personal information
   - View payment history
   - Make payments
   - Download payment receipts

2. Staff
   - Manage student records
   - Process payments
   - View reports
   - Update student information
   - Generate payment receipts

3. Financial Officer
   - Generate financial reports
   - Manage fee structure
   - Monitor payment statistics
   - Handle payment issues
   - View financial analytics

4. System Admin
   - Manage user accounts
   - Configure system settings
   - Monitor system performance
   - Manage access rights
   - Backup and restore data

## Functional Diagram

```
Tuition Management System
│
├── Student Management
│   ├── Add New Student
│   ├── View Student List
│   ├── View Student Details
│   ├── Update Student Information
│   └── Delete Student
│
├── Payment Management
│   ├── Make New Payment
│   ├── View Payment List
│   ├── View Payment Details
│   ├── Generate Payment Receipt
│   └── View Payment History
│
└── Admin Dashboard
    ├── User Management
    │   ├── Add/Edit Users
    │   └── Manage Permissions
    │
    ├── System Settings
    │   ├── Fee Structure
    │   └── Academic Terms
    │
    └── Reports
        ├── Payment Reports
        ├── Student Reports
        └── Financial Summary 

```

## Technologies
- Django
- Python
- SQLite


## Run
- Dump data: python dumpdata_direct.py 