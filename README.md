# 📘 Learning Log  

🚧 **Project Status: In Progress** 🚧  

Learning Log is a web app built with Django that allows users to track topics of interest and record their learning journey through journal entries.  

---

## 🚀 Features  

### 🏗️ Core Functionality  
- **Topic & Entry Management** – Users can create topics and add journal entries.  
- **Admin Interface** – Manage data through Django's built-in admin panel.  

### 🔐 User Authentication  
- **Secure User Accounts** – Login, logout, and registration via Django’s UserCreationForm.  
- **Access Control** – Certain pages are restricted to logged-in users using `@login_required`.  
- **User-Specific Data** – Each user sees only their own topics and entries.  

### 🎨 User Experience & Design  
- **Responsive UI** – Styled with Bootstrap for a clean, mobile-friendly design.  
- **Consistent Navigation** – Includes a navbar and structured templates for a seamless experience.  

### 🌍 Deployment & Security  
- **Live Deployment** – Hosted on a remote server for online accessibility.  
- **Production-Ready** – `DEBUG = False` with custom error pages for security.  

---

## 🛠️ Installation & Setup (Using Poetry)  

### Prerequisites  
- Python 3.x  
- [Poetry](https://python-poetry.org/docs/#installation)  

### Steps  
1. **Clone the Repository**  
   ```sh
   git clone https://github.com/your-username/learning-log.git
   cd learning-log```

2. **Install dependencies with poetry**

```poetry install```

3. **Run Migrations**

```poetry run python3 manage.py migrate```

4. **Create a Superuser**
```poetry run python3 manage.py createsuperuser```

5. **Start the Development Server**

```poetry run python3 manage.py runserver```
