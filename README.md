# YouTube Music Downloader

A Python-based tool to download music from YouTube Music in MP3 format. The script uses the `yt-dlp` library for downloading and `ffmpeg` for audio extraction.

## Features
- Download YouTube Music tracks as MP3 files.
- High-quality audio extraction (up to 320 kbps).
- Interactive file dialogs for selecting input files and download locations.
- Retry mechanism for failed downloads.
- Support for YouTube Music cookies.

## Prerequisites
Before running the script, make sure you have the following installed:
1. **Python 3.8+**
2. **ffmpeg**
   - Install via package manager:
     - **Linux**: `sudo apt install ffmpeg`
     - **macOS**: `brew install ffmpeg`
     - **Windows**: Download from [ffmpeg.org](https://ffmpeg.org/).

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/Monster-ZeroX/YouTube-Music-Downloader.git
   cd YouTube-Music-Downloader
Install dependencies:
bash
Copy code
pip install -r requirements.txt
Usage
Export Cookies (if required):

Install the Get cookies.txt LOCALLY Chrome extension.
Open YouTube Music in Chrome and log in to your account.
Click on the extension icon and export cookies for music.youtube.com as cookies.txt.
Run the Script:

bash
Copy code
python youtube_music_downloader.py
Follow the graphical prompts to:

Select a text file containing YouTube Music links.
Optionally select the exported cookies.txt file for authenticated downloads.
Choose a download location.
The downloaded MP3 files will be saved in the selected folder.

Input File Format
The input file should be a .txt file with one YouTube Music link per line:

arduino
Copy code
https://music.youtube.com/watch?v=s0WIUpETeok&si=5CVSX_rXD1680iAR
https://music.youtube.com/watch?v=srrGnB2yPbg&si=hBa4mdLPHVvaolNb
Example
Input file: httpsmusicy.txt
Output: MP3 files saved in the selected folder.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Contributions
Contributions are welcome! Feel free to open issues or submit pull requests.

Disclaimer
This script is intended for personal use only. Ensure you comply with YouTube's terms of service.
