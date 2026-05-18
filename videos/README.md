# 🎬 Yumi Downloader - Video Files

This folder contains video files used in the bot. Deployers can replace these videos by simply adding files with the **same exact names**.

## 📝 Video File Names (Fixed)

| File Name | Used When | Description |
|-----------|-----------|-------------|
| `startmenuvid.mp4` | `/start` command | Welcome video shown when users start the bot |
| `channelcheckvid.mp4` | After channel verification | Video shown after user joins required channels |
| `botownervid.mp4` | Clicking "👤 Bot Owner" button | Video shown when user views bot owner info |

## 🔧 How to Replace Videos

1. **Download your new video** (MP4 format recommended)
2. **Rename it** to match the exact filename above
3. **Replace the existing file** in this folder
4. **Restart the bot** - it will automatically use your new video

## 📋 Example

To replace the start menu video:

```bash
# 1. Get your new video
curl -o startmenuvid.mp4 https://example.com/your-video.mp4

# 2. Replace the existing file
mv startmenuvid.mp4 /path/to/yumi-downloader/videos/

# 3. Restart the bot
# The bot will automatically detect and use your new video
```

## 🎯 Requirements

- **Format**: MP4 (recommended) or any format Telegram supports
- **Size**: Under 50MB (Telegram limit)
- **Duration**: Any length (recommended 10-30 seconds)
- **Name**: Must match exactly (case-sensitive)

## 📁 Folder Structure

```
yumi-downloader/
├── bot.py
├── config.py
├── teleprinter.py
└── videos/
    ├── startmenuvid.mp4      # Start command video
    ├── channelcheckvid.mp4   # Channel verification video
    └── botownervid.mp4       # Bot owner info video
```

## 💡 Tips

- Videos are sent as `send_video()` - they'll play inline in Telegram
- If a video file is missing, the bot will log an error but continue working
- You can have different videos for different deployments
- No need to modify bot.py - just replace the files!

---

**© 2026 Ghost Marshal | CorruptCrew**
