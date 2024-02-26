'''
Functions to extract audio from video. 
'''
import asyncio
from ffmpeg import FFmpeg

class Extract():
    async def extract_from_video():
        ffmpeg = (
            FFmpeg()
            .option("y")
            .input("input.mp4")
            .output(
                "output.mp4",
                {"codec:v": "libx264"},
                vf="scale=1280:-1",
                preset="veryslow",
                crf=24,
            )
        )

        await ffmpeg.execute()