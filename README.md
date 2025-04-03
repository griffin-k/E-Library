# **Library Management System with AI Chatbot**

![Library Management System](https://via.placeholder.com/1200x400?text=Library+Management+System)

A sophisticated **Library Management System** built using **Django**. This system provides a complete set of features for managing library operations, including book management, user authentication, and interactive charts. Additionally, it features an **AI-based chatbot** that assists users by answering their queries about books, availability, and more.

---

## **Key Features**

- **AI-Powered Chatbot**: An intelligent chatbot that can answer common library-related questions, including book availability, categories, and more.
- **Admin Dashboard**: Provides real-time analytics with visual representations of library statistics, including total books, members, and departmental breakdowns.
- **Student Dashboard**: Offers students a personalized space to view their borrowed books and interact with the AI chatbot for library assistance.
- **User Authentication**: A secure login and registration system for Admin, Students, and Faculty with role-based access control.
- **Book Management**: Admins can easily manage books, add new entries, and categorize them.
- **Book Search Functionality**: Users can search for books based on various criteria such as title, author, or category.
- **Recent Book Additions**: Displays a list of the most recent books added to the library system.
- **Departmental Statistics**: Visualize student, faculty, and staff distributions across various departments using interactive charts.
- **Responsive UI**: A fully responsive user interface designed using **Tailwind CSS** for optimal performance across devices.

---

## **Screenshots**

### Admin Dashboard
![Admin Dashboard](https://via.placeholder.com/800x400?text=Admin+Dashboard)

The admin dashboard provides an overview of key statistics, including total books, members, and staff. It also includes interactive charts for managing departmental data.

### Student Dashboard
![Student Dashboard](https://via.placeholder.com/800x400?text=Student+Dashboard)

The student dashboard displays personal records, borrowed books, and allows users to interact with the AI chatbot for help.

### Departmental Distribution (Bar Chart)
![Departmental Chart](https://via.placeholder.com/800x400?text=Departmental+Statistics+Chart)

Interactive bar charts visualize the distribution of students, faculty, and staff across different departments, providing easy-to-read insights for admins.

### Recent Book Additions
![Recent Book Additions](https://via.placeholder.com/800x400?text=Recent+Books)

This section showcases the most recent books added to the system, ensuring that users are always informed of the latest updates.

### AI Chatbot Interaction
![AI Chatbot](https://via.placeholder.com/800x400?text=AI+Chatbot+Interaction)

The AI chatbot helps users by answering questions about book availability, categories, and library policies.

---

## **Technologies Used**

- **Django**: A high-level Python web framework for building the backend.
- **Chart.js**: A JavaScript library for creating interactive charts and graphs.
- **Tailwind CSS**: A utility-first CSS framework for rapid UI development.
- **SQLite/PostgreSQL/MySQL**: Database systems for storing user, book, and department data.
- **JavaScript**: Used for client-side scripting, including fetching data and rendering charts.
- **Python**: Used for backend logic and AI chatbot integration.
- **AI Libraries**: (Optional) Integrating libraries such as **DialogFlow**, **Rasa**, or **ChatterBot** for chatbot functionality.

---

## **Installation Guide**

### 1. Clone the Repository

To get started, clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/library-management-system.git
cd library-management-system
pip install -r requirements.txt
python3  manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
```


## **Usage**

Once the server is running, you can access the following features:

### **User Authentication**
- **Admin**: Full access to manage books, members, and view statistics.
- **Student**: Limited access to view personal records and interact with the AI chatbot.
- **Faculty**: Similar to students, with access to library resources.

### **Admin Dashboard**
The admin dashboard gives a detailed view of the library's operational statistics, such as:
- Total number of books.
- Total members (students, faculty, staff).
- Visual charts for student distributions by department.
- Access to book management and addition.

### **Student Dashboard**
The student dashboard provides:
- A list of borrowed books.
- Ability to view personal records.
- Interaction with the AI chatbot for library assistance.

### **AI Chatbot**
The AI chatbot interacts with users to answer questions about:
- Book availability and locations.
- Library rules and policies.
- Latest book additions and categories.

### **Interactive Charts**
- **Departmental Distribution**: Admins can view the breakdown of students, faculty, and staff in each department using bar charts.
- **Book Categories**: A doughnut chart visualizes the distribution of books by category.

---

## **Contributing**
We welcome contributions from the community! To contribute, please follow these steps:
1. **Fork** the repository.
2. **Clone** your fork locally.
3. **Create a new branch** for your feature (`git checkout -b feature-name`).
4. **Commit** your changes (`git commit -m 'Add new feature'`).
5. **Push** to your fork (`git push origin feature-name`).
6. **Create a pull request**.

We appreciate your help in improving the project!

---

## **License**
This project is licensed under the **MIT License**. See the LICENSE file for more details.

---

## **Contact**
**Karimullah**  
[Your Email Address] (karimullah.khan3637@gmail.com)
[Your GitHub Profile](https://github.com/griffin-k)  

