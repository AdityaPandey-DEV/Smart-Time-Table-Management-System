# 🚀 Render Email Fix Guide

## 🔧 Environment Variables to Update

Go to your Render service: **Smart-Time-Table-Management-System-1**  
Navigate to: **Environment Variables**

### 1. **Fix Gmail App Password (CRITICAL)**
```
Key: EMAIL_HOST_PASSWORD
Current: hagb aiwz qltg fflz
Fix to: hagbaiwzqltgfflz
```
**Remove all spaces from the App Password!**

### 2. **Fix Production Settings**
```
Key: DEBUG  
Current: True
Fix to: False
```
**For production security**

### 3. **Fix Secret Key**
```
Key: SECRET_KEY
Current: your-secret-key-here
Fix to: django-insecure-render-prod-key-2024-change-this-to-something-secure-random
```
**Use a proper secret key**

### 4. **Optional: Remove Unused Services**
These are not needed for email functionality:
- `CELERY_BROKER_URL` 
- `CELERY_RESULT_BACKEND`
- `REDIS_URL`
- `TWILIO_*` variables (unless you want SMS)

## 🎯 **After Making Changes:**

1. **Save environment variables**
2. **Redeploy your service** (Render will auto-redeploy)
3. **Test registration at:** https://smart-time-table-management-system-1.onrender.com
4. **Check your email** for OTP codes

## 📧 **Test Email Functionality**

After fixing the password:

1. Go to: https://smart-time-table-management-system-1.onrender.com/register/student/
2. Fill registration form with any email
3. Click "Send OTP"
4. **Check your email inbox** for OTP
5. Enter OTP to complete registration

## 🔍 **If Still No Email:**

1. **Check spam/junk folder**
2. **Verify App Password is exactly 16 characters without spaces**
3. **Try registering with adityapandey.dev.in@gmail.com** (your Gmail address)
4. **Check Render logs** for email sending errors

## 🎉 **What Should Work After Fix:**

✅ **Real emails sent to user inboxes**  
✅ **Student registration with email OTP**  
✅ **Admin registration with email OTP**  
✅ **Teacher registration with email OTP**  
✅ **Password reset emails**  
✅ **Professional HTML email templates**

---

**The main issue is the spaces in EMAIL_HOST_PASSWORD - fix that first!**
