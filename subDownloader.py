from pathlib import Path
import subliminal
from subliminal import download_best_subtitles, Video
from babelfish import Language

# Folder where the script is located
VIDEO_FOLDER = Path(__file__).parent
VIDEO_EXTENSIONS = ['.mp4', '.mkv', '.avi', '.mov', '.wmv']

def download_bulgarian_subs():
    # Scan all video files in the folder
    video_files = []
    for f in VIDEO_FOLDER.iterdir():
        if f.suffix.lower() in VIDEO_EXTENSIONS:
            video_obj = Video.fromname(str(f))
            video_obj._file_path = f
            video_files.append(video_obj)

    if not video_files:
        print("No video files found in this folder.")
        return

    # Download best Bulgarian subtitles for all videos
    subtitles = download_best_subtitles(video_files, {Language('bul')}, providers=['opensubtitles'], only_one=True)

    for video, subs in subtitles.items():
        if subs:
            for sub in subs:
                sub_path = video._file_path.with_suffix('.srt')
                # Write subtitle content manually
                with open(sub_path, 'wb') as f:
                    f.write(sub.content)
                print(f"Downloaded: {sub_path.name}")
        else:
            print(f"No Bulgarian subtitles found for: {video._file_path.name}")

if __name__ == "__main__":
    download_bulgarian_subs()
