# 🚀 Quick Gmail App Password Setup for adityapandey.dev.in@gmail.com

## ⚡ 5-Minute Setup

### Step 1: Enable 2-Factor Authentication
1. Go to: https://myaccount.google.com/security
2. Click "2-Step Verification" 
3. Follow setup (you'll need your phone)
4. ✅ Complete 2FA setup

### Step 2: Generate App Password
1. Go to: https://myaccount.google.com/apppasswords
2. Select "Mail" app
3. Select "Other (Custom name)"
4. Type: **Enhanced Timetable System**
5. Click "Generate"
6. 📋 **Copy the 16-character password** (like: `abcd efgh ijkl mnop`)

### Step 3: Update .env File
Open your `.env` file and replace:
```
EMAIL_HOST_PASSWORD=your-gmail-app-password-here
```

With your actual App Password (remove spaces):
```
EMAIL_HOST_PASSWORD=abcdefghijklmnop
```

### Step 4: Test Email Setup
```bash
python test_email.py
```

You should see: ✅ Email sent successfully!

## 📧 Test Registration

After setup, try:
1. `python manage.py runserver`
2. Go to: http://127.0.0.1:8000/register/student/
3. Register with any email address
4. **Real OTP email will be sent!** 📨

## 🔥 What You'll Get

✅ **Real emails sent to users**  
✅ **Professional OTP verification**  
✅ **Beautiful HTML email templates**  
✅ **Works for all user types** (Student, Teacher, Admin)  
✅ **Password reset emails**  
✅ **100% FREE** (no SMS charges)

## 🎯 Quick Commands

```bash
# Test email configuration
python test_email.py

# Start development server
python manage.py runserver

# Test student registration
# Go to: http://127.0.0.1:8000/register/student/
```

---

**Need help?** The setup should take less than 5 minutes once you have the App Password!
