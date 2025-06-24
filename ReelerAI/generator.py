import os
from text_to_audio import text_to_speech_file
import subprocess
def text_to_audio(folder):
    with open(f"user_uploads/{folder}/prompt.txt", 'r') as f:
        prompt = f.readlines()
    text_to_speech_file(", ".join(prompt), folder)
    
def reeler(folder):
    command = command = f'''ffmpeg -f concat -safe 0-1 user_uploads/{folder}/input.txt -i user_uploads/{folder}/audio.mp3 -vf
    "scale=1080:1920:force_original_aspect_ratio=decrease,pad-1080:1920: (ow-1w)/2:(oh-1h)/2:black" -c:v libx264 -c:a aac -shortest -r 30 -pix_fmt yuv420p static/reels/{folder}.mp4'''
    subprocess.run(command, shell= True, check= True)
    


if __name__ == "__main__":
    with open("done.txt", "r") as f:
        done_folders = (f.readlines())
    folders = os.listdir("user_uploads")
    for folder in folders:
        if f'{folder}\n' not in done_folders and (folder != ".DS_Store"):
            text_to_audio(folder)
            reeler(folder)
            with open("done.txt", "a") as f:
                f.write(f"{folder}\n")