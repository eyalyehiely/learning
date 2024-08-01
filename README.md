# Online Coding Web Application

## Introduction

This project is designed to help students and mentors conduct remote coding sessions. 
by writing and changing the code in real-time. The application consists of two main pages: the Lobby page and the Code Block page.

## Features

### Lobby Page

- The Lobby page displays a list of code blocks, each represented by a name (e.g., “Async case”).
- Users can choose a code block, which will navigate them to the Code Block page.

### Code Block Page

- The first user to open the Code Block page is considered the mentor, and subsequent users are students.
- The mentor sees the code block in read-only mode.
- Students can edit the code block, and changes are displayed in real-time using WebSockets.
- Syntax highlighting is provided using Highlight.js (or an equivalent library).
- Supports JavaScript code only.

### Bonus Feature

- Each code block can have a “solution” field. If the student's code matches the solution, a big smiley face is displayed on the screen.

## General Guidelines

- Code blocks are created manually, with fields `title` and `code` (a string representing JS code).
- Clear comments are added to the code where needed.
- The project involves client, server, and database components and can be implemented using any framework/language.

## Tech Stack

### Frontend

- **React**: For building the user interface.
- **Bootstrap**: 
- **Socket.IO**: For real-time communication between the mentor and student.

### Backend

- **Django**: For the backend server and handling API requests.
- **Django Channels**: For WebSocket support to enable real-time updates.
- **Django Rest Framework**: For building RESTful APIs.

### Database

- **PostgreSQL**: For storing code blocks and user data.

### Deployment

- The project can be deployed using any hosting service such as Railway.app, Netlify, Vercel, etc.

## Installation and Setup

### Backend

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/online-coding-webapp.git
    cd online-coding-webapp/backend
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up the database (make sure PostgreSQL is installed and running):
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. Run the development server:
    ```bash
    python manage.py runserver
    ```

### Frontend

1. Navigate to the frontend directory:
    ```bash
    cd ../frontend
    ```

2. Install the dependencies:
    ```bash
    npm install
    ```

3. Start the development server:
    ```bash
    npm start
    ```

## Deployment

1. Choose a hosting service (e.g., Railway.app, Netlify, Vercel).
2. Deploy the backend and frontend separately, ensuring that the frontend can communicate with the backend API.

## Submission

1. Deploy the project and supply the URL for the app.
2. Upload your code to GitHub and attach a link to your GitHub repository.

## Contact

If you have any questions regarding the assignment, do not hesitate to contact us over email or phone.

Good luck!

---

Moveo's HR team

Gilad Herman | VP HR
Email | gilad@moveo.group
Moveo.group
