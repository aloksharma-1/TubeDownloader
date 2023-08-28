# TubeDownloader - YouTube Video Downloader

TubeDownloader is a Python-based software that allows you to easily download YouTube videos right to your local machine. With TubeDownloader, you can save your favorite videos for offline viewing and convenience.

(https://github.com/aloksharma-1/TubeDownloader/blob/main/icon.ico)

## Features

- Download YouTube videos with ease.
- Choose the video quality that suits your needs.
- Simple and user-friendly interface.
- Supports downloading multiple videos concurrently.

## Getting Started

### Prerequisites

- Python 3.x
- pytube library (install using `pip install pytube`)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/aloksharma-1/TubeDownloader.git

## Navigate to the project directory:

```bash
 cd TubeDownloader
```bash

## Install required dependencies:

pip install pytube
Usage
Run the TubeDownloader software:

python tubedownloader.py 
Enter the YouTube video URL you want to download.

Select the desired video quality.

Click the "Download" button to initiate the download.

The downloaded video will be saved in the specified download directory.

## Converting to Executable (.exe)
You can convert the TubeDownloader Python program into a standalone executable file (.exe) using pyinstaller. 
This allows users to run the program without requiring a Python environment. Follow these steps to create the .exe file:

## Open a command prompt or terminal.

#### Navigate to the TubeDownloader directory:

cd path/to/TubeDownloader
Install pyinstaller if you haven't already:

pip install pyinstaller
Run the following command to create the executable:


pyinstaller --onefile tubedownloader.py

The --onefile flag packages everything into a single executable, while the --noconsole flag suppresses the console window.

The executable will be located in the dist directory. You can distribute this .exe file to users who don't have Python installed.

Please note that the conversion process may take some time, and the resulting executable might be relatively large due to packaging the Python interpreter and necessary libraries.

For more advanced options and customizations, refer to the pyinstaller documentation.

## Contributing
Contributions are welcome! Feel free to open issues and submit pull requests to enhance the functionality of TubeDownloader.

## License
This project is licensed under the MIT License.

## Contact
For any inquiries or feedback, please contact alok2910472@gmail.com.

##  Acknowledgments
# pytube - Python library for downloading YouTube videos.
# Font Awesome - Icons used in the application.
# Gradient Background - Gradient color scheme for the user interface.


Remember to replace placeholders like `[your email address]`, `/path/to/logo.png`, and `/path/to/TubeDownloader` with appropriate values.
