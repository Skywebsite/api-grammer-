# 🚀 Deploy to Render

## Step-by-Step Deployment Guide

### 1. Create Render Account
- Go to [render.com](https://render.com)
- Sign up or log in

### 2. Create New Web Service
1. Click **"New +"** → **"Web Service"**
2. Connect your GitHub repository: `Skywebsite/api-grammer-`
3. Select the repository

### 3. Configure Service Settings

**Basic Settings:**
- **Name:** `ai-writing-assistant` (or your preferred name)
- **Region:** Choose closest to you
- **Branch:** `main`
- **Root Directory:** Leave empty (or `./` if needed)

**Build & Deploy:**
- **Environment:** `Python 3`
- **Build Command:** `pip install -r requirements.txt`
- **Start Command:** `uvicorn main:app --host 0.0.0.0 --port $PORT`

**Advanced Settings:**
- **Plan:** Free (or paid for better performance)
- **Auto-Deploy:** Yes (deploys on every push)

### 4. Environment Variables (Optional)
You can add environment variables if needed:
- `PYTHON_VERSION=3.9.18` (if not using render.yaml)

### 5. Deploy
- Click **"Create Web Service"**
- Render will automatically:
  1. Clone your repository
  2. Install dependencies
  3. Download the HuggingFace model (this takes time on first deploy)
  4. Start your API

### 6. Access Your API
Once deployed, Render will provide a URL like:
- `https://ai-writing-assistant.onrender.com`

Your API endpoint will be:
- `https://ai-writing-assistant.onrender.com/ai`
- Docs: `https://ai-writing-assistant.onrender.com/docs`

## ⚠️ Important Notes

### First Deployment
- The first deployment will take **15-30 minutes** because:
  - It needs to download the HuggingFace model (~3.13GB)
  - Install all dependencies including PyTorch

### Free Tier Limitations
- Services on free tier **spin down after 15 minutes of inactivity**
- First request after spin-down will be slow (cold start)
- Consider upgrading to paid plan for always-on service

### Memory Requirements
- The model requires significant RAM (~4-6GB)
- Free tier has 512MB RAM limit
- You may need to:
  - Upgrade to a paid plan, OR
  - Use a smaller model, OR
  - Use Render's Docker deployment with more resources

### Alternative: Use Smaller Model
If you encounter memory issues, you can modify `main.py` to use a smaller model:

```python
# Instead of:
model_name = "pszemraj/flan-t5-large-grammar-synthesis"

# Use:
model_name = "pszemraj/flan-t5-base-grammar-synthesis"  # Smaller model
```

## 🔧 Troubleshooting

### Build Fails
- Check build logs in Render dashboard
- Ensure all dependencies are in `requirements.txt`
- Verify Python version compatibility

### Out of Memory
- Upgrade to paid plan with more RAM
- Use a smaller model
- Optimize model loading

### Slow Response Times
- First request is always slow (model loading)
- Free tier has CPU limitations
- Consider upgrading plan

## 📝 Update Requirements for Render (Optional)

If you want to use newer Python versions on Render, you can create a `requirements-render.txt`:

```txt
fastapi==0.103.2
uvicorn[standard]==0.23.2
transformers==4.35.0
sentencepiece==0.1.99
torch==2.1.0
```

Then update `render.yaml` build command to use this file.

## ✅ Success Checklist

- [ ] Repository pushed to GitHub
- [ ] Render account created
- [ ] Web service created and connected
- [ ] Build command set: `pip install -r requirements.txt`
- [ ] Start command set: `uvicorn main:app --host 0.0.0.0 --port $PORT`
- [ ] Service deployed successfully
- [ ] API endpoint accessible
- [ ] Test API with a sample request

## 🎉 You're Done!

Your API is now live on Render! Share the URL with others to use your AI Writing Assistant API.

