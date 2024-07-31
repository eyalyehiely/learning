# Learning Platform

This project is a learning platform designed to facilitate interactions between teachers and students. The platform allows teachers to create and manage code blocks, which students can then access, edit, and submit. Real-time updates and live collaboration are supported through WebSockets.

## Technologies Used

- **Backend**: Django, Django REST Framework
- **Frontend**: React, Vite
- **Database**: PostgreSQL
- **Cache and Message Broker**: Redis
- **Deployment**: Railway
- **WebSockets**: Django Channels
- **API Documentation**: Swagger
- **Styling**: Tailwind CSS

## Features

- Teachers can create and manage code blocks.
- Students can access code blocks, edit them, and submit their solutions.
- Real-time updates using WebSockets.
- Role-based access control (teacher and student roles).
- Detailed API documentation with Swagger.

## Project Setup

### Prerequisites

- Python 3.9+
- Node.js 14+
- PostgreSQL
- Redis

### Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/learning-platform.git
   cd learning-platform


2. **Backend setup**:

   ```python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. pip install -r requirements.txt