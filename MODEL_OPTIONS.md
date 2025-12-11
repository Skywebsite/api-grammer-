# Model Options for Different Environments

## Memory Requirements

The AI Writing Assistant can use different models depending on available resources:

### Option 1: Base Model (Recommended for Render Free Tier)
- **Model**: `pszemraj/flan-t5-base-grammar-synthesis`
- **Size**: ~500MB
- **RAM Required**: ~1-2GB
- **Quality**: Good
- **Status**: ✅ Currently configured in `main.py`

### Option 2: Large Model (Better Quality, Needs More RAM)
- **Model**: `pszemraj/flan-t5-large-grammar-synthesis`
- **Size**: ~3.13GB
- **RAM Required**: ~4-6GB
- **Quality**: Excellent
- **Use Case**: Local development or paid Render plan

## How to Switch Models

### For Render Free Tier (Current Setup)
The code is already configured to use the base model which should work with 512MB RAM.

### For Local Development with More RAM
Edit `main.py` and change:
```python
model_name = "pszemraj/flan-t5-large-grammar-synthesis"
```

### For Render Paid Plan
If you upgrade to a paid plan with more RAM (2GB+), you can use the large model:
1. Edit `main.py` to use the large model
2. Commit and push
3. Redeploy

## Troubleshooting

### "Out of memory" Error
- **Solution**: Use the base model (already configured)
- **Alternative**: Upgrade to Render paid plan

### Model Download Issues
- First deployment takes 15-30 minutes to download the model
- Model is cached after first download
- Check Render logs for download progress

## Current Configuration
✅ Using: `pszemraj/flan-t5-base-grammar-synthesis` (base model)
✅ Compatible with: Render free tier (512MB RAM)

