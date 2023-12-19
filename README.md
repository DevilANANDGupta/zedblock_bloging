# Personal Blog Platform

This is a simple personal blog platform where you can share your thoughts and stories. Users can read posts, and you, as the admin, can add or delete posts.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the Application](#running-the-application)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Overview

Welcome to your Personal Blog Platform! This platform is designed for sharing personal stories and engaging with readers. As the admin, you have the ability to add new blog posts and delete existing ones. The platform features a responsive design to ensure an optimal viewing experience on various devices.

## Features

- **Read Blog Posts:** Users can read personal stories and thoughts shared on the blog.
- **Engage with Comments:** Readers can engage with the content by leaving comments on blog posts.
- **Admin CRUD Operations:** As the admin, you have the ability to perform CRUD (Create, Read, Update, Delete) operations on blog posts. These actions are protected by an admin password.

## Getting Started

### Prerequisites

Ensure you have the following installed on your machine:

- **Python:** 
- **Flask:** 
- **SQLite**

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/personal-blog-platform.git

2. Navigate to the project directory:

  cd personal-blog-platform
  
3.Create a virtual environment:

  python -m venv venv
4.Activate the virtual environment:

On Linux/macOS:
source venv/bin/activate
On Windows:
.\venv\Scripts\activate
5. Install dependencies
pip install -r requirements.txt


Running the Application
Run the Flask application: cmd/terminal: py run.py
Open your web browser and go to http://127.0.0.1:5000/.





Project/
│
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── models.py
│   └── templates/
│       ├── base.html
│       ├── homepage.html
│       ├── post_detail.html
│       └── admin.html
│
├── static/
│   ├── css/
│   │   └── styles.css
│  
│
├── venv/
├── .gitignore
├── README.md
├── requirements.txt
├── run.py
└── config.py
