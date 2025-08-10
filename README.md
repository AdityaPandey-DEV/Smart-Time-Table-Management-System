# 🎓 Enhanced Smart Timetable Management System

A comprehensive Django-based web application for managing academic timetables, student enrollment, teacher assignments, and AI-powered analytics for educational institutions.

## 🚨 **LATEST UPDATE: FREE Email OTP Solution**

✅ **Problem Solved**: Twilio SMS trial limitations blocking new customer registrations  
✅ **Solution**: 100% FREE Email OTP system that works for ANY email address worldwide  
✅ **Result**: Collect both email AND phone data with completely free verification  

### 🎯 **Perfect Hybrid Registration System:**
- 📧 **Email Address** (required) → FREE OTP verification
- 📱 **Phone Number** (required) → SMS notifications & contact
- 🆓 **No SMS charges** → Unlimited free registrations
- 🌍 **Global compatibility** → Works in any country
- 📊 **Complete data collection** → Full customer profiles

## 🚀 Features

### 👨‍💼 Admin Features
- **Dashboard Overview**: Complete administrative control panel
- **User Management**: Register and manage students, teachers, and admin accounts
- **Course Management**: Create and manage academic courses and subjects
- **Teacher Management**: Assign teachers to subjects and manage faculty
- **Student Management**: Enroll students, manage sections, and track attendance
- **Timetable Management**: Create, modify, and optimize class schedules
- **AI Analytics**: Smart insights and performance analytics
- **Announcements**: Broadcast important updates to targeted audiences

### 👩‍🎓 Student Features
- **Personal Dashboard**: Overview of classes, subjects, and announcements
- **Interactive Timetable**: Weekly schedule view with current class highlighting
- **Subject Management**: View enrolled subjects with attendance tracking
- **AI Chat Assistant**: 24/7 academic support and query resolution
- **Attendance Tracking**: Real-time attendance monitoring with progress bars
- **Study Resources**: Access to materials and assignments

### 👨‍🏫 Teacher Features
- **Teaching Dashboard**: Overview of assigned classes and schedules
- **Attendance Management**: Mark and track student attendance
- **Subject Management**: Manage assigned subjects and student enrollments
- **Resource Sharing**: Upload study materials and assignments
- **Student Performance**: View analytics and generate reports

### 🤖 AI-Powered Features
- **Smart Scheduling**: AI-optimized timetable generation
- **Performance Analytics**: Intelligent insights and trend analysis
- **Study Recommendations**: Personalized learning suggestions
- **Attendance Predictions**: Early warning systems for at-risk students
- **Resource Optimization**: Efficient room and teacher allocation

## 🛠️ Technology Stack

- **Backend**: Django 4.2.7 (Python)
- **Frontend**: HTML5, CSS3, Bootstrap 5, JavaScript
- **Database**: SQLite (development) / MySQL (production)
- **AI Integration**: OpenAI API for intelligent features
- **Authentication**: Django's built-in user system with custom profiles
- **UI Framework**: Bootstrap 5 with custom styling
- **Icons**: Font Awesome
- **Forms**: Django Crispy Forms with Bootstrap5 template pack

## 📧 Email OTP Registration System

### 🎯 **How It Works:**

#### **Step 1: Complete Registration Form**
Users provide ALL required information:
- 📝 Personal details (name, roll number, course, year, section)
- 📧 **Email address** (required) → receives FREE OTP
- 📱 **Phone number** (required) → stored for SMS notifications
- 🔐 Password and confirmation

#### **Step 2: Email OTP Verification**
- 📨 Beautiful HTML email sent instantly with 6-digit OTP
- 🎨 Professional template with clear branding
- ⏰ 10-minute expiration for security
- 🌍 Works with ANY email provider worldwide

#### **Step 3: Account Creation**
- ✅ Email verified and account created
- 📊 Complete profile with both email and phone stored
- 🆓 **100% FREE** - no SMS charges ever!

### 💡 **Why Email OTP is Better:**

| Feature | SMS OTP (Twilio) | **Email OTP** |
|---------|------------------|---------------|
| **Cost** | Paid service with trial limits | **100% FREE** |
| **Global Reach** | Country/carrier restrictions | **Worldwide** |
| **Trial Limits** | Verified numbers only | **No limits** |
| **Reliability** | May fail or delay | **Consistent delivery** |
| **Customer Experience** | Blocks new users | **Always works** |
| **Data Collection** | Phone only | **Email + Phone** |

### 🔧 **Technical Implementation:**

```python
# Email OTP Model
class EmailOTP(models.Model):
    email = models.EmailField()
    otp_code = models.CharField(max_length=6)
    purpose = models.CharField(max_length=20, default='registration')
    is_used = models.BooleanField(default=False)
    expires_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

# Generate and Send OTP
otp_code = EmailOTP.generate_otp(email, 'registration')
send_otp_notification(email, otp_code, 'registration', method='email')

# Verify OTP
EmailOTP.verify_otp(email, otp_code, 'registration')
```

### 🚀 **Testing the System:**

1. **Development Mode**: OTP displayed in Django console
2. **Production Mode**: Beautiful HTML emails sent via SMTP
3. **Form Validation**: Both email and phone required
4. **Account Creation**: Complete profile with verified email

---

## 📦 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Git

### Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/AdityaPandey-DEV/Smart-Time-Table-Management-System.git
   cd Smart-Time-Table-Management-System
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   ```bash
   # Copy the example env file
   cp .env.example .env
   
   # Edit .env with your settings
   SECRET_KEY=your-secret-key-here
   DEBUG=True
   OPENAI_API_KEY=your-openai-api-key (optional)
   ```

5. **Run migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create superuser** (optional)
   ```bash
   python manage.py createsuperuser
   ```

7. **Start the development server**
   ```bash
   python manage.py runserver
   ```

8. **Access the application**
   - Open your browser and navigate to `http://127.0.0.1:8000`
   - Register as an admin to access full features

## 📁 Project Structure

```
enhanced_timetable_system/
├── accounts/              # User management and authentication
│   ├── models.py         # User, Student, Teacher, Admin profiles
│   ├── views.py          # Authentication views
│   ├── admin_views.py    # Admin dashboard and management
│   └── urls.py           # URL routing
├── timetable/            # Core timetable functionality
│   ├── models.py         # Course, Subject, TimetableEntry, etc.
│   ├── views.py          # Timetable management views
│   └── utils.py          # Helper functions
├── ai_features/          # AI-powered features
│   ├── models.py         # AI chat, analytics, recommendations
│   ├── views.py          # AI functionality views
│   └── services.py       # AI service integrations
├── templates/            # HTML templates
│   ├── admin/            # Admin interface templates
│   ├── student/          # Student interface templates
│   ├── teacher/          # Teacher interface templates
│   └── base.html         # Base template
├── static/               # Static files (CSS, JS, images)
├── media/                # User uploaded files
└── requirements.txt      # Python dependencies
```

## 🎯 Usage Guide

### Getting Started
1. **Admin Registration**: Start by registering an admin account
2. **Course Setup**: Create courses (B.Tech, BCA, etc.) and subjects
3. **Teacher Management**: Add teachers and assign them to subjects
4. **Student Enrollment**: Register students and enroll them in subjects
5. **Timetable Creation**: Generate or manually create timetables
6. **AI Features**: Enable AI analytics and chat features

### User Roles

**Admin Users:**
- Full system access
- User and content management
- Analytics and reporting
- System configuration

**Teacher Users:**
- Subject and class management
- Attendance marking
- Student performance tracking
- Resource sharing

**Student Users:**
- Personal timetable access
- Subject enrollment viewing
- AI chat assistance
- Attendance monitoring

## 🔧 Configuration

### Environment Variables

Create a `.env` file in the root directory:

```env
SECRET_KEY=your-django-secret-key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Database (Optional - defaults to SQLite)
DB_NAME=timetable_db
DB_USER=root
DB_PASSWORD=
DB_HOST=localhost
DB_PORT=3306

# AI Features (Optional)
OPENAI_API_KEY=your-openai-api-key

# Email Configuration (Optional)
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
```

### Database Configuration

**SQLite (Default - Development):**
- No additional setup required
- Database file created automatically

**MySQL (Production):**
```bash
pip install mysqlclient
```
Update settings.py to use MySQL configuration.

## 🔒 Security Features

- **CSRF Protection**: All forms protected against CSRF attacks
- **User Authentication**: Secure login/logout functionality
- **Permission System**: Role-based access control
- **Data Validation**: Comprehensive form and model validation
- **SQL Injection Protection**: Django ORM provides built-in protection

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Make your changes**
4. **Write tests** (if applicable)
5. **Commit your changes**
   ```bash
   git commit -m "Add your feature description"
   ```
6. **Push to your branch**
   ```bash
   git push origin feature/your-feature-name
   ```
7. **Create a Pull Request**

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

If you encounter any issues or have questions:

1. **Check the Issues**: Look for existing solutions
2. **Create an Issue**: Describe your problem clearly
3. **Contact**: Reach out to the maintainers

## 🎉 Acknowledgments

- **Django Community**: For the amazing web framework
- **Bootstrap Team**: For the responsive UI framework  
- **OpenAI**: For AI integration capabilities
- **Font Awesome**: For the beautiful icons
- **All Contributors**: Thanks for making this project better!

## 📊 Project Status

- ✅ **Core Features**: Complete
- ✅ **User Management**: Complete  
- ✅ **Timetable System**: Complete
- ✅ **AI Integration**: Complete
- ✅ **Responsive Design**: Complete
- ✅ **Email OTP System**: Complete
- ✅ **FREE Registration**: Complete
- 🚧 **Advanced Analytics**: In Development
- 🚧 **Mobile App**: Planned
- 🚧 **API Endpoints**: Planned

## 🎯 **SOLUTION SUMMARY**

### ❌ **The Problem:**
- Twilio SMS trial account blocking unverified phone numbers
- New customers unable to complete registration
- SMS charges for OTP verification

### ✅ **The Solution:**
- **100% FREE Email OTP system** that works worldwide
- **Hybrid registration** collecting both email and phone data
- **Professional HTML email templates** for OTP delivery
- **No trial limitations** - works for any email address
- **Complete customer profiles** with verified email + phone

### 🚀 **Result:**
```
✅ Migrations applied successfully
✅ EmailOTP model created
✅ Registration forms updated
✅ Email templates designed
✅ FREE OTP system working
✅ Complete customer data collection
✅ No more Twilio SMS issues!
```

### 🔥 **Ready to Use:**
1. **Run the server**: `python manage.py runserver`
2. **Visit**: `http://127.0.0.1:8000/register/`
3. **Test registration** with any email address
4. **Check console** for OTP during development
5. **Complete verification** and see full profile created

**The Twilio SMS problem is permanently SOLVED!** 🎉

---

**Made with ❤️ by [Aditya Pandey](https://github.com/AdityaPandey-DEV)**

*For educational institutions looking to modernize their timetable management with AI-powered features.*
