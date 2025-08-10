#!/usr/bin/env python3
"""
Test script to verify OpenAI API key setup
Run: python test_openai_setup.py
"""

import os
import sys
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def test_openai_setup():
    """Test OpenAI API key setup"""
    print("🔍 Testing OpenAI API Setup...")
    print("-" * 50)
    
    # Check if API key is set
    api_key = os.getenv('OPENAI_API_KEY')
    
    if not api_key:
        print("❌ OPENAI_API_KEY not found in .env file")
        print("📝 Please add your API key to .env file:")
        print("   OPENAI_API_KEY=sk-your-actual-api-key-here")
        return False
    
    if api_key == 'sk-your-openai-api-key-here':
        print("❌ Default placeholder API key detected")
        print("📝 Please replace with your actual OpenAI API key")
        return False
    
    if not api_key.startswith('sk-'):
        print("❌ Invalid API key format (should start with 'sk-')")
        print("📝 Get your API key from: https://platform.openai.com/api-keys")
        return False
    
    print(f"✅ API key format looks correct: {api_key[:15]}...")
    
    # Try to import and test OpenAI
    try:
        import openai
        print("✅ OpenAI package is installed")
    except ImportError:
        print("❌ OpenAI package not installed")
        print("📝 Install it with: pip install openai")
        return False
    
    # Test API connection
    try:
        client = openai.OpenAI(api_key=api_key)
        
        # Make a simple test request
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": "Say 'API test successful!'"}
            ],
            max_tokens=10
        )
        
        result = response.choices[0].message.content
        print(f"✅ API connection successful!")
        print(f"📬 Test response: {result}")
        
        # Show usage info
        print("\n💡 Usage Information:")
        print(f"   - Model used: gpt-3.5-turbo")
        print(f"   - Tokens used: ~{response.usage.total_tokens}")
        print(f"   - Approximate cost: ${response.usage.total_tokens * 0.002 / 1000:.6f}")
        
        return True
        
    except openai.AuthenticationError:
        print("❌ Authentication failed - Invalid API key")
        print("📝 Check your API key at: https://platform.openai.com/api-keys")
        return False
        
    except openai.RateLimitError:
        print("❌ Rate limit exceeded or quota exhausted")
        print("📝 Check your usage at: https://platform.openai.com/usage")
        return False
        
    except Exception as e:
        print(f"❌ API test failed: {str(e)}")
        return False

def test_huggingface_setup():
    """Test Hugging Face setup as alternative"""
    print("\n🤗 Testing Hugging Face Alternative...")
    print("-" * 50)
    
    hf_key = os.getenv('HUGGINGFACE_API_KEY')
    
    if not hf_key:
        print("ℹ️  HUGGINGFACE_API_KEY not set (optional)")
        print("📝 For free alternative, get token from: https://huggingface.co")
        return False
    
    if hf_key.startswith('hf_'):
        print("✅ Hugging Face token format looks correct")
        
        try:
            import requests
            headers = {"Authorization": f"Bearer {hf_key}"}
            response = requests.get("https://huggingface.co/api/whoami", headers=headers)
            
            if response.status_code == 200:
                user_info = response.json()
                print(f"✅ Hugging Face API working for user: {user_info.get('name', 'Unknown')}")
                return True
            else:
                print("❌ Hugging Face token invalid")
                return False
                
        except Exception as e:
            print(f"❌ Hugging Face test failed: {e}")
            return False
    else:
        print("❌ Invalid Hugging Face token format (should start with 'hf_')")
        return False

def show_next_steps():
    """Show what to do next"""
    print("\n🚀 Next Steps:")
    print("-" * 50)
    print("1. Run your Django server: python manage.py runserver")
    print("2. Go to: http://127.0.0.1:8000/")
    print("3. Register as a student or admin")
    print("4. Try the AI chat feature!")
    print("5. Check the AI analytics dashboard")
    print("\n📚 Documentation:")
    print("- OpenAI Guide: See OPENAI_SETUP_GUIDE.md")
    print("- Project Features: Check README.md")

if __name__ == "__main__":
    print("🤖 Enhanced Timetable System - API Setup Test")
    print("=" * 60)
    
    # Test OpenAI first
    openai_success = test_openai_setup()
    
    # Test Hugging Face alternative
    hf_success = test_huggingface_setup()
    
    print("\n📊 Summary:")
    print("-" * 50)
    
    if openai_success:
        print("✅ OpenAI API: Ready to use!")
    elif hf_success:
        print("✅ Hugging Face API: Ready to use!")
    else:
        print("❌ No AI API configured")
        print("📝 Please set up either OpenAI or Hugging Face API")
        print("📖 See OPENAI_SETUP_GUIDE.md for detailed instructions")
        sys.exit(1)
    
    show_next_steps()
    print("\n🎉 Setup complete! Your AI-powered timetable system is ready!")
