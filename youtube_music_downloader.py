import yt_dlp
import os
from tkinter import Tk, filedialog
from tqdm import tqdm

# Retry log file
failed_log_file = "failed_downloads.log"

# Function to open a file dialog and select a file
def select_file(prompt_message):
    Tk().withdraw()  # Hide the root window
    file_path = filedialog.askopenfilename(title=prompt_message, filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    return file_path if file_path else None

# Function to open a directory dialog and select a folder
def select_directory(prompt_message):
    Tk().withdraw()  # Hide the root window
    directory_path = filedialog.askdirectory(title=prompt_message)
    return directory_path if directory_path else None

# Function to download YouTube music as MP3
def download_youtube_music(input_file, output_dir, cookies_file=None):
    with open(input_file, "r") as file:
        links = [line.strip() for line in file if line.strip()]

    ydl_opts = {
        "format": "bestaudio/best",
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "320",
        }],
        "outtmpl": os.path.join(output_dir, "%(title)s.%(ext)s"),
        "noplaylist": True,
        "extractor_args": {
            "youtube": {
                "player_skip": ["ios", "mweb"],
            }
        },
        "cookiefile": cookies_file if cookies_file else None,
        "quiet": False,  # Ensure debug logs are shown
        "ignoreerrors": True,  # Skip links that cause errors
    }

    failed_links = []

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        for link in tqdm(links, desc="Downloading videos"):
            try:
                print(f"\nDownloading: {link}")
                ydl.download([link])
            except Exception as e:
                print(f"Failed to download {link}: {e}")
                failed_links.append(link)

    # Log failed links
    if failed_links:
        with open(failed_log_file, "w") as log_file:
            log_file.write("\n".join(failed_links))
        print(f"\nFailed downloads logged to {failed_log_file}.")
    else:
        print("\nAll downloads completed successfully!")

    return failed_links

# Retry failed downloads
def retry_failed_downloads(output_dir, cookies_file=None):
    if not os.path.isfile(failed_log_file):
        print(f"No failed downloads log found. Nothing to retry.")
        return

    with open(failed_log_file, "r") as file:
        links = [line.strip() for line in file if line.strip()]

    if not links:
        print("No failed downloads to retry.")
        return

    print("\nRetrying failed downloads...")
    ydl_opts = {
        "format": "bestaudio/best",
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "320",
        }],
        "outtmpl": os.path.join(output_dir, "%(title)s.%(ext)s"),
        "noplaylist": True,
        "extractor_args": {
            "youtube": {
                "player_skip": ["ios", "mweb"],
            }
        },
        "cookiefile": cookies_file if cookies_file else None,
        "quiet": False,
    }

    failed_links = []

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        for link in tqdm(links, desc="Retrying failed downloads"):
            try:
                print(f"\nRetrying: {link}")
                ydl.download([link])
            except Exception as e:
                print(f"Failed again: {link}: {e}")
                failed_links.append(link)

    # Update failed downloads log
    if failed_links:
        with open(failed_log_file, "w") as log_file:
            log_file.write("\n".join(failed_links))
        print(f"\nFailed downloads updated in {failed_log_file}.")
    else:
        os.remove(failed_log_file)  # Remove log if all retries succeed
        print("\nAll retries completed successfully!")

# Main script execution
if __name__ == "__main__":
    print("Please select the text file containing YouTube Music links.")
    input_file = select_file("Select the text file with YouTube Music links")
    if not input_file:
        print("No file selected. Exiting.")
        exit()

    print("Please select the cookies file (optional).")
    cookies_file = select_file("Select the cookies file (optional)")

    print("Please select the directory where you want to save the downloads.")
    output_dir = select_directory("Select the download location")
    if not output_dir:
        print("No download location selected. Exiting.")
        exit()
    
    # Download videos
    failed_links = download_youtube_music(input_file, output_dir, cookies_file)

    # Retry failed downloads if any
    if failed_links:
        retry_choice = input("\nWould you like to retry failed downloads? (yes/no): ").strip().lower()
        if retry_choice in ["yes", "y"]:
            retry_failed_downloads(output_dir, cookies_file)
