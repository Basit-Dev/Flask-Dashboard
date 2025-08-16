# Flask-Dashboard
A Flask-based user dashboard with PostgreSQL, HTML, and TailwindCSS. A user registration with full CRUD operations (add, edit, delete). Provides a responsive interface with a clean design, and PostgreSQL integration for managing users efficiently.

---

## What This Project Is

This application lets you:
- **View a directory of users** in a clean, tabular layout  
- **Add new users** with details such as name, email, phone, and department  
- **Edit existing users** to update their information  
- **Delete users** from the system when no longer needed  

I built it to practice creating a full-stack web application with Flask, PostgreSQL, and TailwindCSS. It’s designed to be simple, responsive, and easy to extend, working smoothly across desktop and mobile devices.

---

## User Stories
- **As an administrator**, I want to view a dashboard of all users so that I can manage accounts.  
- **As an administrator**, I want to add new users so that I can grow the user base.  
- **As an administrator**, I want to edit user information so that I can keep records accurate.  
- **As an administrator**, I want to delete users so that I can remove inactive or invalid accounts.

---

## Tech Stack
- Flask (Python)  
- PostgreSQL  
- HTML + TailwindCSS  
- Jinja2 Templates  

## What the Website Looks Like & Functionality Overview

The dashboard has a clean and minimal design with a focus on usability:

- **Navigation Bar**:  
  Positioned at the top with the project name on the left and quick actions (`View Users` and `Add User`) on the right.  
  The bar uses a light grey background with subtle separation from the main content.

- **Page Title**:  
  A bold, blue "User Directory" heading introduces the main section.

- **User Table**:  
  - Displays users in a tabular format with columns for Name, Email, Phone, Department, and Actions.  
  - The table header has a solid blue background with white text for contrast.  
  - Rows with a light background for readability seperated by a light grey line.  
  - Emails are styled as blue links.  
  - Actions include **Edit** (blue) and **Delete** (red) for clear visual cues.

- **Buttons**:  
  The primary "Add User" button uses a solid blue background with white text to stand out as the main call-to-action.

- **Layout**:  
  The overall layout is centered, responsive, and styled with TailwindCSS, giving it a modern web application feel.

### Works on Any Device
- Whether you’re on your phone or laptop, the layout adjusts to fit your screen, mobile devices use a hamburger menu implenented using JavaScript.

---

## How It Works

The User Directory App follows a straightforward flow:

1. **Home Page**  
   Users land on a welcome screen that explains the app and provides a button to view the user list.

2. **User Directory**  
   Displays all registered users in a table with columns for name, email, phone, department, and actions.

3. **Add User**  
   Clicking **Add User** opens a form where new user details can be entered and stored in the PostgreSQL database.

4. **Edit User**  
   Each user row includes an **Edit** action, allowing updates to user information through a form.

5. **Delete User**  
   The **Delete** action removes a user record from the database.

6. **Database Integration**  
   All data is persisted in PostgreSQL. Flask handles routing and logic, while Jinja2 templates and TailwindCSS style the front end.

7. **Responsive UI**  
   The interface is styled to be clean, modern, and responsive, making it usable across devices.

In short, the app provides a lightweight, for managing a list of users with full CRUD functionality.

---