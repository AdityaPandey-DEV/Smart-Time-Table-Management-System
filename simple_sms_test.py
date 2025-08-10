#!/usr/bin/env python3
"""
Simple Twilio SMS Test Script
"""

from twilio.rest import Client
import os

# Your Twilio credentials - Use environment variables for security
account_sid = os.environ.get('TWILIO_ACCOUNT_SID', 'your_account_sid_here')
auth_token = os.environ.get('TWILIO_AUTH_TOKEN', 'your_auth_token_here')
twilio_phone = os.environ.get('TWILIO_PHONE_NUMBER', '+1234567890')

# Test phone number
test_phone = os.environ.get('TEST_PHONE_NUMBER', '+1234567890')

def send_test_sms():
    """Send a test SMS"""
    try:
        print("📱 Initializing Twilio client...")
        client = Client(account_sid, auth_token)
        
        print(f"📤 Sending SMS to {test_phone}...")
        message = client.messages.create(
            body="🎉 Hello from your Django Timetable System! SMS is working perfectly! ✅",
            from_=twilio_phone,
            to=test_phone
        )
        
        print(f"✅ SMS sent successfully!")
        print(f"Message SID: {message.sid}")
        print(f"Status: {message.status}")
        print(f"From: {message.from_}")
        print(f"To: {message.to}")
        
        return True
        
    except Exception as e:
        print(f"❌ SMS failed: {str(e)}")
        return False

if __name__ == '__main__':
    print("🚀 Testing Twilio SMS...")
    print("=" * 40)
    
    success = send_test_sms()
    
    if success:
        print("\n🎉 SMS functionality is working!")
        print("Now your Django app can send SMS messages.")
    else:
        print("\n❌ SMS test failed.")
        print("Check your Twilio credentials and account status.")
        
    print("\n📝 Next: Run your Django server and test OTP functionality!")
