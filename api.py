#!/usr/bin/env python3
import yt_dlp
import asyncio

class APIDownloader:
    def __init__(self, *args, **kwargs):
        """Agar bot is class ko initialize karte waqt koi bhi arguments bhejta hai, 
        toh yeh unhe accept kar lega aur crash nahi hoga."""
        pass

    async def get_download_link(self, url, *args, **kwargs):
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
            loop = asyncio.get_event_loop()
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = await loop.run_in_executor(None, lambda: ydl.extract_info(url, download=False))
                
                if 'url' in info:
                    return info['url']
                elif 'entries' in info:
                    return info['entries'][0]['url']
        except Exception as e:
            print(f"yt-dlp Error: {e}")
            
        return None

# Backward compatibility ke liye (agar bot bina class ke direct call kar raha ho)
async def get_download_link(url, *args, **kwargs):
    downloader = APIDownloader()
    return await downloader.get_download_link(url)
