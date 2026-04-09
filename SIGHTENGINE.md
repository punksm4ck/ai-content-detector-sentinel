# Sightengine API Setup

AI Sentinel uses [Sightengine](https://sightengine.com) for AI-generated content detection.

## Getting API Keys

1. Sign up at [sightengine.com/signup](https://sightengine.com/signup) — free tier includes **500 API calls/month**
2. Go to your dashboard → **API Credentials**
3. Copy your **API User** and **API Secret**
4. In AI Sentinel: right-click tray → **⚙ Configuration** → **🔑 API** tab → paste both values

## Which Model Is Used

AI Sentinel calls the `genai` model:

```
POST https://api.sightengine.com/1.0/check.json
  models=genai
  api_user=YOUR_USER
  api_secret=YOUR_SECRET
  media=<JPEG frame bytes>
```

Response field used: `type.ai_generated` (float 0.0–1.0)

## Rate Limits & Cost

| Plan | Calls/month | Price |
|---|---|---|
| Free | 500 | $0 |
| Pay-as-you-go | Unlimited | ~$0.001/call |

With default settings (4s interval, motion-triggered), typical usage is **200–800 calls/day** depending on screen activity. Monitor your usage at [dashboard.sightengine.com](https://dashboard.sightengine.com).

## Threshold Tuning

The default threshold is **85%** (`0.85`). Lower = more sensitive (more false positives), higher = more strict (may miss borderline cases).

Recommended range: **0.80–0.92**
