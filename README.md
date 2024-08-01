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
- **react-bootstrap**: 
- **@monaco-editor/react**: 
- **@mui/material**: 




- **Socket.IO**: For real-time communication between the mentor and student.

### Backend

- **Django**: For the backend server and handling API requests.
- **Django Channels**: For WebSocket support to enable real-time updates.
- **Django Rest Framework**: For building RESTful APIs.

### Database

- **PostgreSQL**: For storing code blocks and user data.
- **Redis**:

### Deployment

- **Railway**:

## Installation and Setup

### Backend

1. Clone the repository:
    ```bash
    https://github.com/eyalyehiely/learning-backend/
    cd learning/backend
    ```

2. Create a virtual environment and activate it:
    ```bash
    on macOS:
    python3 -m venv venv
    source venv/bin/activate

    on Windows:

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
    on macOS:
    python3 manage.py runserver

   on Windows:
    python3 manage.py runserver
    ```

### API Documentation
---

```
ws/codeblock/${id}/
```
This WebSocket endpoint is used to establish a real-time connection between student to teacher.
- **Path Parameters**:
- ```id ```: The code block id.


---
```
GET /codeblocks/
```
This endpoint fetch all code blocks to the Lobby page.
- **Response**:

- ```id ```: The code block id.
- ```title```: The code block title.
- ```instructions```: The code block instructions.
- ```code```: The code block script.


```
POST /codeblock/${id}/check/
```
This endpoint checks if the user script is correct.

**Request Body**:
- ```code```: The user script.
- ```user_id```: The user unique id.



**Response**:

- ```id ```: The code block id.
- ```title```: The code block title.
- ```instructions```: The code block instructions.
- ```code```: The code block script.

A message indicating if the script is correct.




```
POST /fetchClientUuidToServer/
```
This endpoint send to the server the user unique id.

**Request Body**:
- ```user_id```: The user unique id.



**Response**:

A message indicating if the user_id accepted.



```
POST /codeblock/submission/
```
This endpoint create a new submission if there isnt already one.

**Request Body**:
- ```user_id```: The user unique id.
- ```code_block_id```: The original script id.





**Response**:

A message if submission exist or create a new one.


```
GET,DELETE /codeblock/submission/{id}/?user_id={clientUUID}
```


**GET:**

**Response**:
- Return the current submission or try to create one.


**DELETE:**

**Request**:
- Return the current submission or try to create one. ??????


**Response**:
DELETE the current submission.





```
PUT /codeblock/submission/{id}/?user_id={clientUUID}
```
This endpoint edit the current submission.

**Request Body**:
- ```code```: The user script.
- ```code_block_id```: The original script id.
- ```user_id```: The user unique id.




**Response**:

Saving the new submission or send an error message.





```
POST /log_visitor/
```
This endpoint check how many users are in the same submission and determine a role.

**Request Body**:
- ```user_id```: The user unique id.
- ```url```: The submission url.




**Response**:

Saving the new role & send data:
- ```user_id```: The user unique id.
- ```url```: The submission url.
- ```role```: The current role.




### Frontend

1. Clone the repository:
    ```bash
    https://github.com/eyalyehiely/learning-frontend/
    cd learning/backend
    ```

2. Install the dependencies:
    ```bash
    npm install
    ```

3. Start the development server:
    ```bash
    npm start
    ```



## Submission

1. Deploy the project and supply the URL for the app.
2. Upload your code to GitHub and attach a link to your GitHub repository.

## Contact

If you have any questions regarding the assignment, do not hesitate to contact us over email or phone.

Good luck!

---


