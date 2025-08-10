#!/usr/bin/env python3
"""
Quick email test script for Enhanced Timetable System
Run this after setting up Gmail App Password to test email functionality
"""
import os
import django
from django.conf import settings

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'enhanced_timetable_system.settings')
django.setup()

from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

def test_email():
    try:
        print("🧪 Testing email configuration...")
        print(f"📧 Email Backend: {settings.EMAIL_BACKEND}")
        print(f"📧 Email Host: {settings.EMAIL_HOST}")
        print(f"📧 Email User: {settings.EMAIL_HOST_USER}")
        
        # Send test email
        subject = "Enhanced Timetable System - Email Test"
        message = "This is a test email to verify SMTP configuration is working correctly!"
        from_email = settings.EMAIL_HOST_USER
        to_email = [settings.EMAIL_HOST_USER]  # Send to yourself
        
        result = send_mail(
            subject=subject,
            message=message,
            from_email=from_email,
            recipient_list=to_email,
            fail_silently=False
        )
        
        if result:
            print("✅ Email sent successfully!")
            print("✅ Gmail SMTP configuration is working!")
            print("✅ OTP emails should now be delivered to your inbox")
        else:
            print("❌ Email sending failed")
            
    except Exception as e:
        print(f"❌ Email test failed: {str(e)}")
        print("\n🔧 Common fixes:")
        print("1. Make sure 2-Factor Authentication is enabled on Gmail")
        print("2. Generate App Password from Google Account Security settings")
        print("3. Update EMAIL_HOST_PASSWORD in .env file")
        print("4. Check if Gmail is blocking 'less secure apps'")

if __name__ == "__main__":
    test_email()
