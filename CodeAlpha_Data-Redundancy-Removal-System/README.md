# CodeAlpha_Data-Redundancy-Removal-System

A web-based application built using **Python Flask** and **SQLite** to eliminate data redundancy by ensuring that only unique records are stored in the database. The system validates user input and prevents duplicate entries, demonstrating efficient data handling and backend validation.

---

## Table of Contents

1. [About](#about)
2. [Features](#features)
3. [Folder Structure](#folder-structure)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Technology Stack](#technology-stack)
7. [Contribution](#contribution)

---

## About

The CodeAlpha Data Redundancy Removal System is designed to prevent duplicate data storage in databases. It checks incoming records before insertion and ensures data consistency using unique constraints and backend validation. This project demonstrates fundamental concepts of database management and backend development.

---

## Features

- Prevents duplicate data entries  
- Backend validation using Flask  
- SQLite database integration  
- Simple and clean web interface  
- Efficient data storage and retrieval  

---

## Folder Structure

```

📦 CodeAlpha_Data-Redundancy-Removal-System
┣ 📂 templates
┃ ┗ HTML templates
┣ 📄 app.py
┣ 📄 data.db
┣ 📄 requirements.txt
┣ 📄 README.md

````

- **templates**: HTML files rendered by Flask  
- **app.py**: Main Flask application  
- **data.db**: SQLite database file  
- **requirements.txt**: Python dependencies  

---

## Installation

1. **Clone the repository**
```bash
   git clone https://github.com/Sanjanakh24/CodeAlpha_Data-Redundancy-Removal-System.git
   cd CodeAlpha_Data-Redundancy-Removal-System
````

2. **Create a virtual environment (optional but recommended)**

   ```bash
   python3 -m venv venv
   source venv/bin/activate        # macOS / Linux
   .\venv\Scripts\activate         # Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

1. **Run the Flask application**

   ```bash
   python app.py
   ```

2. **Open your browser**

   ```
   http://127.0.0.1:5000
   ```

3. **Submit data**
   Enter user details in the form. Duplicate entries will be automatically detected and prevented.

---

## Technology Stack

| Component       | Technology       |
| --------------- | ---------------- |
| Backend         | Python Flask     |
| Database        | SQLite           |
| Frontend        | HTML, CSS        |
| Dependency Mgmt | requirements.txt |

---

## Contribution

Contributions, issues, and feature requests are welcome.
Fork the repository and submit a pull request.

---

```

