# 🚀 Deployment Guide - Liver Disease Prediction App

## Free Hosting Platform: Render (Recommended)

### Prerequisites
1. Create a free account at [render.com](https://render.com)
2. Install Git if not already installed
3. Have your project files ready

---

## Step 1: Prepare Your Code for GitHub

1. **Create a GitHub Repository**:
   - Go to [github.com](https://github.com) and sign in
   - Click "New Repository"
   - Name it `liver-disease-prediction`
   - Make it **Public** (free)
   - Click "Create Repository"

2. **Upload Files to GitHub**:
   - Upload all these files to your repository:
     - `app.py`
     - `index.html`
     - `predict.html`
     - `about.html`
     - `requirements.txt`
     - `Procfile`
     - `runtime.txt`
     - `liver_disease_model.pkl`
     - `label_encoder.pkl`
   - Or use Git commands:
     ```bash
     git init
     git add .
     git commit -m "Initial commit"
     git branch -M main
     git remote add origin https://github.com/YOUR_USERNAME/liver-disease-prediction.git
     git push -u origin main
     ```

---

## Step 2: Deploy to Render

1. **Sign in to Render**:
   - Go to [dashboard.render.com](https://dashboard.render.com)
   - Click "New +" and select "Web Service"

2. **Connect GitHub**:
   - Authorize GitHub if prompted
   - Select your `liver-disease-prediction` repository

3. **Configure the Web Service**:
   - **Name**: `liver-predict-ai`
   - **Environment**: `Python`
   - **Build Command**: (leave blank - Render auto-detects)
   - **Start Command**: `python app.py`

4. **Advanced Settings**:
   - Click "Advanced"
   - Add these environment variables:
     - `PYTHON_VERSION`: `3.11.0`

5. **Deploy**:
   - Click "Create Web Service"
   - Wait 2-5 minutes for deployment

---

## Step 3: Get Your Shareable URL

Once deployed, Render will provide a URL like:
```
https://liver-predict-ai.onrender.com
```

**Share this URL with anyone!**

---

## Alternative: Railway.app

1. Go to [railway.app](https://railway.app)
2. Sign up with GitHub
3. Click "New Project" → "Deploy from GitHub repo"
4. Select your repository
5. Railway will auto-detect Python/Flask
6. Get your URL from the deployment

---

## Alternative: PythonAnywhere

1. Go to [pythonanywhere.com](https://pythonanywhere.com)
2. Create free account
3. Go to "Files" → "Upload a file" (upload all files)
4. Go to "Web" → "Add a new web app"
5. Select "Flask" and Python 3.11
6. Configure WSGI file to point to your app
7. Your URL: `yourusername.pythonanywhere.com`

---

## 🔧 Troubleshooting

### Common Issues:
- **Import errors**: Check `requirements.txt` has all dependencies
- **Model loading error**: Ensure `.pkl` files are uploaded
- **Port error**: App uses `PORT` env variable (already configured)

### Test Locally First:
```bash
pip install -r requirements.txt
python app.py
```
Then visit `http://localhost:10000`

---

## 📱 Your Website Features

After deployment, users can:
- Visit the homepage to learn about the service
- Click "Predict" to enter health parameters
- See normal value ranges for each test
- Get instant AI-powered liver disease predictions
- View confidence scores for predictions

---

**🌐 Share your website URL: `https://liver-predict-ai.onrender.com` (after deployment)**

