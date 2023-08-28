# TubeDownloader

TubeDownloader is a Python-based software that allows you to easily download YouTube videos right to your local machine. With TubeDownloader, you can save your favorite videos for offline viewing and convenience.

## Features

- Download YouTube videos with ease.
- Choose the video quality that suits your needs.
- Simple and user-friendly interface.
- Supports downloading multiple videos concurrently.

## Getting Started

### Prerequisites

- Python 3.x
- pytube library (install using `pip install pytube`)

## Usage

1. **Install required dependencies:**

   ```bash
   pip install pytube
   
1. **Run the TubeDownloader software:**
   ```bash
   python tubedownloader.py

2.**Enter the YouTube video URL you want to download.**

3.**Select the desired video quality.**

4.**Click the "Download" button to initiate the download.**

5. **The downloaded video will be saved in the specified download directory.**

## Converting to Executable (.exe)
You can convert the TubeDownloader Python program into a standalone executable file (.exe) using pyinstaller.
This allows users to run the program without requiring a Python environment. Follow these steps to create the .exe file:

1.*Open a command prompt or terminal.*

2.*Navigate to the TubeDownloader directory:*
  
  **cd path/to/TubeDownloader**
    

3. *Install pyinstaller if you haven't already:*
     ```bash
    pip install pyinstaller
4. *Run the following command to create the executable:*
      ```bash
   pyinstaller --onefile tubedownloader.py
**The --onefile flag packages everything into a single executable.**

**The --noconsole flag suppresses the console window.**

5. *The executable will be located in the dist directory. You can distribute this .exe file to users who don't have Python installed.*

**Note: The conversion process may take some time, and the resulting executable might be relatively large due to packaging the Python interpreter and necessary libraries.**

**For more advanced options and customizations, refer to the pyinstaller documentation.**

## Contributing
Contributions are welcome! Feel free to open issues and submit pull requests to enhance the functionality of TubeDownloader.

## License
This project is licensed under the <ins>MIT License.</ins>

## Contact
For any inquiries or feedback, please contact <ins>alok2910472@gmail.com</ins>.

## Acknowledgments
<ins>pytube</ins> - Python library for downloading YouTube videos.

<ins>Font Awesome</ins> - Icons used in the application.

Gradient Background - Gradient color scheme for the user interface.
