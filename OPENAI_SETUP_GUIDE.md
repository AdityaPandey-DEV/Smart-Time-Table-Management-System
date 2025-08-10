# 🔑 OpenAI API Setup Guide

## Option 1: OpenAI API (Recommended - $5 Free Credits)

### Step 1: Create Account & Get Free Credits
1. Visit [OpenAI Platform](https://platform.openai.com)
2. Sign up with email/Google/Microsoft account
3. **New users get $5 in free credits** (expires in 3 months)
4. Verify your phone number (required for API access)

### Step 2: Generate API Key
1. Go to [API Keys page](https://platform.openai.com/api-keys)
2. Click "Create new secret key"
3. Name it: `Enhanced-Timetable-System`
4. **Copy the key immediately** (starts with `sk-...`)
5. Store it securely - you can't view it again!

### Step 3: Set Up in Your Project
Create `.env` file in your project root:

```env
# OpenAI Configuration
OPENAI_API_KEY=sk-your-actual-api-key-here

# Other configurations...
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

---

## Option 2: Free Alternatives

### 🆓 **Hugging Face (Completely Free)**

1. **Sign up**: [https://huggingface.co](https://huggingface.co)
2. **Get Token**: Profile → Settings → Access Tokens → New Token
3. **Use in `.env`**:
```env
HUGGINGFACE_API_KEY=hf_your-token-here
```

4. **Update your AI code to use Hugging Face**:
```python
# In your AI features, replace OpenAI calls with:
import requests

def get_ai_response(prompt):
    headers = {"Authorization": f"Bearer {settings.HUGGINGFACE_API_KEY}"}
    payload = {
        "inputs": prompt,
        "parameters": {"max_length": 200}
    }
    response = requests.post(
        "https://api-inference.huggingface.co/models/microsoft/DialoGPT-medium",
        headers=headers,
        json=payload
    )
    return response.json()[0]['generated_text']
```

### 🆓 **Google Colab + Free Models**

Use Google Colab to run free models:
```python
# Install transformers in your project
pip install transformers torch

# Use local models (no API key needed)
from transformers import pipeline

chatbot = pipeline("conversational", model="microsoft/DialoGPT-medium")
response = chatbot("What is my schedule today?")
```

### 🆓 **Ollama (Local AI)**

Run AI models locally on your computer:

1. **Install Ollama**: [https://ollama.ai](https://ollama.ai)
2. **Download a model**: `ollama pull llama2`
3. **Use in your code**:
```python
import requests

def local_ai_response(prompt):
    response = requests.post('http://localhost:11434/api/generate',
        json={
            'model': 'llama2',
            'prompt': prompt,
            'stream': False
        })
    return response.json()['response']
```

---

## 🛠️ **Setting Up Your Environment**

### Step 1: Create .env File
Copy the example and fill in your values:

```bash
# Copy the example
cp .env.example .env

# Edit with your preferred editor
notepad .env  # Windows
```

### Step 2: Update Your .env File
```env
# Django Configuration
SECRET_KEY=django-insecure-your-secret-key-here-change-this-for-production
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# AI Configuration (Choose one)
OPENAI_API_KEY=sk-your-openai-key-here  # If using OpenAI
HUGGINGFACE_API_KEY=hf_your-hf-token-here  # If using Hugging Face

# Email Configuration (for OTP - use Gmail App Password)
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-16-digit-app-password

# Database (SQLite default - no setup needed)
# DB_NAME=db.sqlite3
```

### Step 3: Install Required Packages
```bash
# For OpenAI
pip install openai

# For Hugging Face
pip install transformers torch

# For local models
pip install ollama-python
```

### Step 4: Test Your Setup
```bash
python manage.py shell

# Test OpenAI
>>> import openai
>>> import os
>>> openai.api_key = os.getenv('OPENAI_API_KEY')
>>> print("OpenAI key loaded:", bool(openai.api_key))

# Or test Hugging Face
>>> import os
>>> print("HF token loaded:", bool(os.getenv('HUGGINGFACE_API_KEY')))
```

---

## 💡 **Recommendations**

### For Development & Testing:
- **Start with OpenAI's $5 free credits** - easiest and most reliable
- **Use Hugging Face** if you want completely free
- **Try Ollama** for offline development

### For Production:
- **OpenAI API** - best quality but costs money
- **Self-hosted models** - more cost-effective for high usage
- **Hybrid approach** - free tier for basic features, paid for advanced

---

## 🔒 **Security Best Practices**

1. **Never commit `.env` to git**:
```bash
echo ".env" >> .gitignore
```

2. **Use environment variables in production**
3. **Rotate keys regularly**
4. **Set spending limits** in OpenAI dashboard
5. **Monitor usage** to avoid unexpected charges

---

## 🚨 **Troubleshooting**

### Common Issues:

1. **"Invalid API key"**
   - Check if key starts with `sk-`
   - Ensure no extra spaces
   - Regenerate if needed

2. **"Rate limit exceeded"**
   - You've used up your free credits
   - Wait or add payment method

3. **"Model not found"**
   - Check model name spelling
   - Some models need approval

### Need Help?
- Check [OpenAI Documentation](https://platform.openai.com/docs)
- Visit [Hugging Face Docs](https://huggingface.co/docs)
- Look at your project's AI features in `ai_features/` folder

---

## 📊 **Cost Estimation**

### OpenAI Pricing (after free credits):
- **GPT-3.5-turbo**: $0.002 per 1K tokens (~750 words)
- **Your $5 free credits = ~2.5M tokens** (enough for thousands of queries)

### Free Alternatives Cost:
- **Hugging Face**: Completely free (with rate limits)
- **Ollama**: Free but uses your computer resources
- **Google Colab**: Free with usage limits
