import os
from text_to_audio import text_to_speech_file
def text_to_audio(folder):
    with open(f"user_uploads/{folder}/prompt.txt", 'r') as f:
        prompt = f.readlines()
    text_to_speech_file(",".join(prompt), folder)
    
def reeler(folder):
    pass


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