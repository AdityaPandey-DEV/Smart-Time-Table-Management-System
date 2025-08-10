# 📧 Email Setup Guide for Enhanced Timetable System

## Why Email OTP Instead of SMS?
- **100% FREE** - No monthly charges like SMS
- **No API limits** - Gmail provides generous limits
- **Better deliverability** - Emails are more reliable
- **User-friendly** - Most users check email regularly

## 🚀 Quick Setup (5 Minutes)

### Step 1: Enable Gmail 2-Factor Authentication
1. Go to [Google Account Security](https://myaccount.google.com/security)
2. Under "Signing in to Google", click "2-Step Verification"
3. Follow the setup process to enable 2FA

### Step 2: Generate App Password
1. In Google Account Security, find "2-Step Verification"
2. Scroll down to "App passwords"
3. Click "App passwords"
4. Select "Mail" and "Other (Custom name)"
5. Enter "Enhanced Timetable System"
6. Copy the 16-character password (e.g., `abcd efgh ijkl mnop`)

### Step 3: Create Environment File
Create a `.env` file in your project root:

```bash
# Email Configuration for Gmail
DEBUG=True
SECRET_KEY=your-secret-key-here

EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=abcd efgh ijkl mnop

# Database
DATABASE_URL=sqlite:///db.sqlite3
```

### Step 4: Test Email Setup
```bash
python test_email.py
```

You should see: `✅ Email sent successfully!`

## 🔧 Alternative Email Providers

### Outlook/Hotmail
```bash
EMAIL_HOST=smtp.live.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@outlook.com
EMAIL_HOST_PASSWORD=your-outlook-password
```

### Yahoo Mail
```bash
EMAIL_HOST=smtp.mail.yahoo.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@yahoo.com
EMAIL_HOST_PASSWORD=your-yahoo-app-password
```

## 🎯 Development vs Production

### Development Mode (DEBUG=True)
- OTP codes are printed in console for testing
- Emails are sent to console backend by default
- Fallback to SMTP if configured

### Production Mode (DEBUG=False)
- Must have proper email configuration
- Real emails sent to users
- No console fallback

## 🚨 Troubleshooting

### "535 Username and Password not accepted"
- ✅ Enable 2-Factor Authentication on Gmail
- ✅ Use App Password, NOT your regular Gmail password
- ✅ Remove spaces from app password in .env file

### "SMTPAuthenticationError"
- ✅ Check EMAIL_HOST_USER matches your Gmail address
- ✅ Regenerate App Password if needed
- ✅ Make sure 2FA is enabled

### "No module named 'decouple'"
```bash
pip install python-decouple
```

### Emails not received
- ✅ Check spam/junk folder
- ✅ Verify email address spelling
- ✅ Test with test_email.py first

## 📱 For Users

### What Users See:
1. Enter email address in registration form
2. Click "Send OTP" button
3. Check email inbox (and spam folder)
4. Enter 6-digit code from email
5. Account verified and created!

### Email Template Features:
- Professional design
- Clear OTP display
- 10-minute expiration notice
- Branded for your institution

## 🎉 Success!

Once configured, your users get:
- ✅ FREE registration with email verification
- ✅ Professional OTP emails
- ✅ Secure account creation process
- ✅ No SMS charges or API limits

---

**Need help?** Check the troubleshooting section or run `python system_health_check.py`
