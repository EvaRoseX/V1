# ═══════════════════════════════════════════════════════════════
# 🌸 YUMI DOWNLOADER - DEPLOYER CONFIGURATION
# ═══════════════════════════════════════════════════════════════
# © 2026 Ghost Marshal | CorruptCrew
# 📂 Source: https://github.com/corruptcrew/YumiDownloader
# ═══════════════════════════════════════════════════════════════

# ───────────────────────────────────────────────────────────────
# 🔑 BOT TOKEN (Required)
# Get from @BotFather on Telegram
# ───────────────────────────────────────────────────────────────
BOT_TOKEN = "8262263812:AAGRegbTDQTBIAnY670-1HgqFnc3BuR8Nqc"

# ───────────────────────────────────────────────────────────────
# 🏷️ DEPLOYER INFO (Your details - shown in "Bot Owner" button)
# This is displayed separately from the original creator
# ───────────────────────────────────────────────────────────────
DEPLOYER_NAME = "Godz"  # Your name or bot instance name
DEPLOYER_USERNAME = "@BYGOD_HELPER"  # Your Telegram username

# ───────────────────────────────────────────────────────────────
# 🔐 DEPLOYER SUDO USERS (Your admin IDs)
# ⚠️ Owner (Ghost Marshal - 8785375616) is already hardcoded in bot.py
# Add YOUR sudo user IDs here (comma-separated)
# Format: [YOUR_ID_1, YOUR_ID_2, ...]
# ───────────────────────────────────────────────────────────────
DEPLOYER_SUDO_USERS = [7562079827]  # Add your IDs: [123456789, 987654321]

# ───────────────────────────────────────────────────────────────
# 📢 DEPLOYER FORCE JOIN CHANNELS (Your channels)
# ⚠️ Owner channel (@corruptcrew) is already hardcoded in bot.py
# Add YOUR channels here for force join
# Bot MUST be admin in these channels to work
# Format: ["@yourchannel1", "@yourchannel2", ...]
# Leave empty [] if you don't want additional force join
# ───────────────────────────────────────────────────────────────
DEPLOYER_CHANNELS = ["@ownergodupdate"]  # Add your channels: ["@yourchannel"]

# ───────────────────────────────────────────────────────────────
# 💬 DEPLOYER SUPPORT & UPDATE LINKS (Your links)
# These are shown alongside owner's links
# ───────────────────────────────────────────────────────────────
SUPPORT_CHANNEL = "https://t.me/ownergodupdate"  # Your support
UPDATE_CHANNEL = "https://t.me/ownergodupdate"  # Your updates

# ───────────────────────────────────────────────────────────────
# 🎨 BOT SETTINGS
# ───────────────────────────────────────────────────────────────
BOT_NAME = "Yumi Downloader"
BOT_VERSION = "v2.0.0"
WELCOME_MESSAGE = """
🌸 **Welcome to Yumi Downloader!** 🌸

I can download videos from multiple platforms.
Send me a link to get started!

⚡ **Features:**
• Fast Downloads
• Multiple Quality Options
• No Watermark
• 24/7 Online

📢 **Join:** @corruptcrew
👤 **Dev:** @GhostMarshal
"""

# ───────────────────────────────────────────────────────────────
# 🌐 API SETTINGS (Optional - Leave default if using public API)
# ───────────────────────────────────────────────────────────────
API_ENDPOINT = "https://api.example.com/download"
API_KEY = "your_api_key_here"
API_TIMEOUT = 120

# ───────────────────────────────────────────────────────────────
# 💾 DATABASE SETTINGS
# ───────────────────────────────────────────────────────────────
DATABASE_NAME = "yumi_users.db"
