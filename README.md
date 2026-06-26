# SujeetBoss3 DRM Uploader Bot

A high-speed Telegram DRM video downloader and uploader bot built with Pyrogram and Cython optimizations.

## 🚀 One-Click Deploy to Heroku

Click the button below to instantly deploy this bot to Heroku. All required environment variables will be prompted automatically.

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

> **Note:** Make sure you have uploaded your repo to GitHub before clicking the deploy button, so Heroku can clone it directly.

## ⚙️ Environment Variables Required

- `API_ID`: Your Telegram API ID from my.telegram.org
- `API_HASH`: Your Telegram API Hash from my.telegram.org
- `BOT_TOKEN`: Your Telegram Bot Token from @BotFather
- `AUTH_USERS`: List of Telegram User IDs separated by commas who are authorized to use the bot.
- `CREDIT`: Your Custom Watermark / Channel Name (e.g. "Ram™")

## ⚡ Speed Optimizations Applied
- `workers=100` implemented for extremely fast Pyrogram concurrency.
- `ffmpeg` buildpack is automatically installed via Heroku for fast DRM video processing.
