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

## Figma Files

<p align="center">
  <strong>Colour Pallette</strong><br>
  <img src="documentation/wireframes/figma/colour/colour-pallette.png" alt="Colour Pallette" width="300" />
</p>

<p align="center">
  <strong>Desktop Home</strong><br>
  <img src="documentation/wireframes/figma/mono/desktop-home.png" alt="Desktop Home" width="300" />
</p>

<p align="center">
  <strong>Desktop Users</strong><br>
  <img src="documentation/wireframes/figma/mono/desktop-user.png" alt="Desktop Users" width="300" />
</p>

<p align="center">
  <strong>Desktop Update User</strong><br>
  <img src="documentation/wireframes/figma/mono/desktop-update-user.png" alt="Desktop Update User" width="300" />
</p>

<p align="center">
  <strong>Desktop Add User</strong><br>
  <img src="documentation/wireframes/figma/mono/desktop-add-user.png" alt="Desktop Add User" width="300" />
</p>

<p align="center">
  <strong>Desktop Add User Confirm</strong><br>
  <img src="documentation/wireframes/figma/mono/desktop-add-user-confirm.png" alt="Desktop Add User Confirm" width="300" />
</p>

<p align="center">
  <strong>Desktop Delete User</strong><br>
  <img src="documentation/wireframes/figma/mono/desktop-delete-user.png" alt="Desktop Delete User" width="300" />
</p>

<p align="center">
  <strong>Mobile User</strong><br>
  <img src="documentation/wireframes/figma/mono/mobile-user.png" alt="Mobile User" width="300" />
</p>

<p align="center">
  <strong>Mobile Delete</strong><br>
  <img src="documentation/wireframes/figma/mono/mobile-delete.png" alt="Mobile Delete" width="300" />
</p>

<p align="center">
  <strong>Mobile Add User Confirm</strong><br>
  <img src="documentation/wireframes/figma/mono/mobile-add-user-confim.png" alt="Mobile Add User Confirm" width="300" />
</p>

<p align="center">
  <strong>Desktop Home</strong><br>
  <img src="documentation/wireframes/figma/colour/desktop-home-colour.png" alt="Desktop Home" width="300" />
</p>

<p align="center">
  <strong>Desktop Users</strong><br>
  <img src="documentation/wireframes/figma/colour/desktop-user-colour.png" alt="Desktop Users" width="300" />
</p>

<p align="center">
  <strong>Desktop Update User</strong><br>
  <img src="documentation/wireframes/figma/colour/desktop-update-user-colour.png" alt="Desktop Update User" width="300" />
</p>

<p align="center">
  <strong>Desktop Add User</strong><br>
  <img src="documentation/wireframes/figma/colour/desktop-add-user-colour.png" alt="Desktop Add User" width="300" />
</p>

<p align="center">
  <strong>Desktop Add User Confirm</strong><br>
  <img src="documentation/wireframes/figma/colour/desktop-add-user-confirm-colour.png" alt="Desktop Add User Confirm" width="300" />
</p>

<p align="center">
  <strong>Desktop Delete User</strong><br>
  <img src="documentation/wireframes/figma/colour/desktop-delete-user-colour.png" alt="Desktop Delete User" width="300" />
</p>

<p align="center">
  <strong>Mobile User</strong><br>
  <img src="documentation/wireframes/figma/colour/mobile-user-colour.png" alt="Mobile User" width="300" />
</p>

<p align="center">
  <strong>Mobile Delete</strong><br>
  <img src="documentation/wireframes/figma/colour/mobile-delete-colour.png" alt="Mobile Delete" width="300" />
</p>

<p align="center">
  <strong>Mobile Add User Confirm</strong><br>
  <img src="documentation/wireframes/figma/colour/mobile-add-user-confirm-colour.png" alt="Mobile Add User Confirm" width="300" />
</p>

---

## Credits and Acknowledge
- Flash messages credits to StackOverflow.


## Screenshots of validation

<p align="center">
  <strong>welcome.html</strong><br>
  <img src="documentation/validation/welcome-screen-html-validation.png" alt="Welcome screen validation" width="300" />
</p>

<p align="center">
  <strong>users.html</strong><br>
  <img src="documentation/validation/users-screen-html-validation.png" alt="User screen validation" width="300" />
</p>

<p align="center">
  <strong>update_user.html</strong><br>
  <img src="documentation/validation/update-user-screen-html-validation.png" alt="Update user validation" width="300" />
</p>

<p align="center">
  <strong>delete_user.html</strong><br>
  <img src="documentation/validation/delete-user-screen-html-validation.png" alt="Delete user validation" width="300" />
</p>

<p align="center">
  <strong>confirm_update.html</strong><br>
  <img src="documentation/validation/confirm-update-screen-html-validation.png" alt="Confirm update validation" width="300" />
</p>

<p align="center">
  <strong>add_user.html</strong><br>
  <img src="documentation/validation/add-user-screen-html-validation.png" alt="Add user validation" width="300" />
</p>

<p align="center">
  <strong>CSS</strong><br>
  <img src="documentation/validation/css-validation.png" alt="CSS output validation" width="300" />
</p>

---

# Frontend Manual Testing Guide

## What Are We Testing?
We want to make sure the app looks, works and responds when you click buttons, fill out forms, search for users and CRUD operations display the correct results.

Pages to check:
- **Welcome page** (`/`)
- **User list** (`/users`)
- **Add user** form (`/add`)
- **Update user** form (`/update/<id>`)
- **Confirm update** (`/update/confirm/<id>`)
- **Delete user** confirmation (`/delete/<id>`)

---

## Test Implementation Requirements
- Browser: Chrome, Firefox, Safari, or Edge.
- Will run on (`http://localhost:5000`).
- Some fake data like:  
  - Alice Brown, `alice@example.com`, `07123456789`, Sales  
  - Bob Chen, `bob@example.com`, `07987654321`, Support  

---

## Step 1: Check General Stuff

- Page load without errors.
- Layout neat and not broken.
- buttons and links work when clicked.
- On phone or tablet, it resize nicely without weird scroll bars.

---

## Step 2: Welcome Page (`/`)

- Page loads as intended.
- Buttons take you to the user list page.

---

## Step 3: User List (`/users`)

- If there are no users, a message - "No users found" displays.
- Search by name, email, phone, department - displays correct results.
- When something random is typed - "No users found".
- After searching, “Show all” button displays and when clicked displays all users.
- Update and delete buttons navigate tpo the correct pages.

---

## Step 4: Add User (`/add`)

- Checked if input fileds are blank and click submit - Error displays.
- When invalid email typed - Shows error.
- Once a user user is added - it takes you back to the user list with a success message.
- When an email is the same - a “duplicate email” error displays.

---

## Step 5: Update User (`/update/<id>`)

- Form shows the correct id for the user.
- After changing details and updated - “User updated successfully” displays.
- When changing the email to one that already exists - Error displays. **FAILED**
- After clicking cancel - it takes you back to the user list.

---

## Step 6: Confirm Update (`/update/confirm/<id>`)

- It shows the new details before updating.
- After click confirm - it saves the changes.
- If you click cancel - it takes you back without updating.

---

## Step 7: Delete User (`/delete/<id>`)

- It asks “Are you sure?” before deleting.
- Cancel - User is still in the list.
- Once clicked delete - User is removed from the list.

---

## Step 8: Messages & Alerts

- When things work, green "Success" messages display.
- When there’s an error (like duplicate email), a red "Error" message displays.
- Messages go away automatically, when X clicked or when user refreshes the screen.

---

## Step 9: Mobile View

- Navbar, forms, and tables look as intended.
- You scroll easily without breaking the layout.

---

## Step 10: Quick Test

After making changes, quickly check:
- [x] Add a user - works.
- [x] Search users - works.
- [x] Update user - works.
- [X] Delete user - works.
- [x] Layout on mobile - works.

---