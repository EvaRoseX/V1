#!/usr/bin/env python3
import yt_dlp
import asyncio

async def get_download_link(url):
    """Direct yt-dlp ka use karke download link nikalne ka function"""
    ydl_opts = {
        'format': 'best',
        'quiet': True,
        'no_warnings': True,
        'http_headers': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
        },
        'nocheckcertificate': True,
    }
    
    try:
        # Loop running event mein yt-dlp ko safely run karne ke liye
        loop = asyncio.get_event_loop()
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = await loop.run_in_executor(None, lambda: ydl.extract_info(url, download=False))
            
            # Agar direct video url mil jaye
            if 'url' in info:
                return info['url']
            # Agar playlist ya multiple formats hon
            elif 'entries' in info:
                return info['entries'][0]['url']
    except Exception as e:
        print(f"yt-dlp Error: {e}")
        
    return None
