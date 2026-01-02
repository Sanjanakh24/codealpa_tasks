# Cloud-Based Bus Pass System

A simple **cloud-deployed web application** built using **Python Flask** and **MySQL (AWS RDS)** that allows users to book bus passes and view all booked passes through a browser interface.

---

## 📌 Project Overview

The Cloud-Based Bus Pass System is designed to demonstrate:
- Flask backend development
- Integration with a cloud-hosted MySQL database (AWS RDS)
- Basic HTML rendering without separate template files
- CRUD operation (Insert & View)
- Cloud-ready deployment configuration

Users can:
- Enter passenger details
- Book a bus pass
- View all booked passes stored in the database

---

## 🛠 Technology Stack

| Layer | Technology |
|------|-----------|
| Backend | Python (Flask) |
| Database | MySQL (AWS RDS) |
| Frontend | HTML (Flask `render_template_string`) |
| Cloud | AWS EC2 / Any cloud VM |

---

## 📂 Project Structure

```
project-folder/
│
├── app.py             # Main Flask application
├── requirements.txt   # Requirements Files
└── README.md          # Project documentation
```

---

## ⚙️ Prerequisites

Before running this project, ensure you have:

- Python 3.8+
- pip (Python package manager)
- MySQL Database (AWS RDS recommended)
- EC2 or any cloud VM (optional for cloud deployment)

---

## 📦 Required Python Packages

Install dependencies using:

```
pip install flask pymysql
```

---

## 🗄️ Database Setup (MySQL / AWS RDS)

### 1️⃣ Create Database

```sql
CREATE DATABASE buspass;
USE buspass;
```

### 2️⃣ Create Table

```sql
CREATE TABLE passes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    route VARCHAR(50),
    price INT
);
```

---

## 🔐 Database Configuration

Update the database connection in `app.py`:

```python
host="<YOUR_RDS_ENDPOINT>"
user="admin"
password="<YOUR_PASSWORD>"
database="buspass"
```

⚠️ **Important:** Never hardcode passwords in production. Use environment variables instead.

---

## ▶️ Running the Application (Local)

```bash
python app.py
```

Access the application in your browser:

```
http://localhost:5000
```

---

## ☁️ Running on Cloud (AWS EC2)

1. Launch an EC2 instance
2. Install Python and dependencies
3. Open port **5000** in EC2 Security Group
4. Run:

```bash
python app.py
```

Access using:

```
http://<EC2_PUBLIC_IP>:5000
```

---

## 🔗 Application Routes

| Route | Method | Description |
|------|-------|------------|
| `/` | GET | Home page with booking form |
| `/book` | POST | Book a new bus pass |
| `/passes` | GET | View all booked passes |

---

## ✅ Features

- Cloud-ready Flask application
- MySQL database integration
- Simple and clean UI
- Insert and retrieve data
- Beginner-friendly project structure

---

## 🚀 Future Enhancements

- User authentication
- Update & delete passes
- Better UI using HTML templates
- Environment variable security
- Docker deployment

---

## 👨‍💻 Author

Developed as part of a **Cloud & Python learning project**.

---

## 📜 License

This project is for **educational purposes only**.

