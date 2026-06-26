# Restaurant POS Billing System

A simple and efficient Restaurant Point of Sale (POS) Billing System built using Python.
This system helps restaurants manage orders, calculate bills, and generate invoices easily.



## Project Description

The Restaurant POS Billing System is designed to automate the billing process in restaurants and cafes.

### It helps:
    
    - Take customer orders
    
    - Calculate item-wise and total billing
    
    - Generate final invoices
    
    - Reduce manual calculation errors
    
    - Speed up the billing process




## Features

    - Menu Display
    
    - Item Selection with Quantity

    - Role Based Access (Admin, Cashier)
    
    - Automatic Bill Calculation
    
    - Tax / Discount Calculation (if applicable)
    
    - Generate Final Bill / Invoice
    
    - Inventory Management
    
    - Simple and User-Friendly Interface

    


## Technologies Used

    - Backend: Python, Django (MTV Architecture) 

    - Frontend: HTML5, CSS3, JavaScript (Bootstrap 5, BI Icons)

    - Database: MySQL / PostgreSQL / SQLite 

    - Reporting: ReportLab (PDF Engine), OpenPyxl (Excel Generation)

    -  Environment: Pip-managed dependencies (Standardized via requirements.txt)



## Installation & Setup



### Step 1: Clone the Repository

    git clone  https://github.com/KAVINPRABHAKAR/Restaurant_POS_Billing_System.git



### Step 2: Navigate to Project Directory

    cd Restaurant_POS_Billing_System



### Step 3: Create Virtual Environment (Optional)

    python -m venv venv



### Step 4: Activate Virtual Environment

    venv\Scripts\activate



### Step 5: Install Required Dependencies


    pip install -r requirements.txt

    If requirements.txt is not available, install Django manually

    pip install django



### Step 6: Apply Database Migrations

    python manage.py makemigrations
    
    python manage.py migrate



### Step 7: Create Superuser (Admin Login)

    python manage.py createsuperuser

    Enter username, email, and password when prompted.



### Step 8: Run the Development Server

    python manage.py runserver



### Step 9: Open in Browser

    Admin Panel

    http://127.0.0.1:8000/admin/



### Now you can:

    - Access Admin Panel

    - Add Categories 
    
    - Add Menu Items 

    - Login as Admin & Cashier

    - Manage Orders & Inventory



### Step 10: Open in Browser
    
    Main Application

    http://127.0.0.1:8000/



### Now you can See:

    - Login Page

    - Dashboard Page

    - Add Orders Page

    - Daily Sales Analytics Page & Most Sold Items

    - Inventory Management Page

    - Sales Report Page

    - Logout Option



### Output Screenshots


### Admin Page


![project_output](Output_Screenshots/admin.png)



### Add Food Categories



![project_output](Output_Screenshots/admin1.png)



![project_output](Output_Screenshots/admin2.png)



![project_output](Output_Screenshots/admin3.png)



![project_output](Output_Screenshots/admin4.png)



![project_output](Output_Screenshots/admin5.png)



![project_output](Output_Screenshots/admin6.png)



![project_output](Output_Screenshots/admin7.png)



![project_output](Output_Screenshots/admin8.png)



![project_output](Output_Screenshots/admin9.png)



![project_output](Output_Screenshots/admin10.png)



### Add Menu Items


![project_output](Output_Screenshots/admin11.png)



![project_output](Output_Screenshots/admin12.png)



![project_output](Output_Screenshots/admin13.png)



![project_output](Output_Screenshots/admin14.png)



![project_output](Output_Screenshots/admin15.png)



![project_output](Output_Screenshots/admin16.png)



![project_output](Output_Screenshots/admin17.png)



![project_output](Output_Screenshots/admin18.png)



![project_output](Output_Screenshots/admin19.png)



![project_output](Output_Screenshots/admin20.png)



![project_output](Output_Screenshots/admin21.png)



![project_output](Output_Screenshots/admin22.png)



![project_output](Output_Screenshots/admin23.png)



![project_output](Output_Screenshots/admin24.png)



![project_output](Output_Screenshots/admin25.png)



![project_output](Output_Screenshots/admin26.png)



![project_output](Output_Screenshots/admin27.png)



![project_output](Output_Screenshots/admin28.png)



![project_output](Output_Screenshots/admin29.png)



### Login Page



![project_output](Output_Screenshots/login.png)



### Orders Page



![project_output](Output_Screenshots/orders.png)





![project_output](Output_Screenshots/orders1.png)





![project_output](Output_Screenshots/orders2.png)





![project_output](Output_Screenshots/orders3.png)





![project_output](Output_Screenshots/orders4.png)





![project_output](Output_Screenshots/orders5.png)






### Dashboard Page



![project_output](Output_Screenshots/dashboard.png)





### Inventory Management


![project_output](Output_Screenshots/inventory.png)





### Order Receipt




![project_output](Output_Screenshots/pdf_bill.png)





### Sales Reports



![project_output](Output_Screenshots/pdf_report.png)




![project_output](Output_Screenshots/sales_report.png)




![project_output](Output_Screenshots/sales_report1.png)




![project_output](Output_Screenshots/sales_report2.png)




![project_output](Output_Screenshots/excel_report.png)
