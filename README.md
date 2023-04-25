# youtube-downloader

This application allows you to download YouTube videos as mp4 files on your PC. Provide a link to the desired YouTube video, and the path to the location you would like to download the file, and click the download button.

# Using on your machine (Ubuntu)
1. Download this folder (do not rename, as folder name is important for next steps) If you rename ANYTHING, makesure to update all files to newer names and modify following steps accordingly

2. Copy or move the .desktop file to your desktop directory (if you make a copy: changes to .desktop file in the downloaded folder will not change the .desktop file that is being executed when clicking on the icon)

3. Open folder and open .desktop file

4. Update lines 3 & 5 of .desktop file (icon & exec) to the locations of the playbutton.png file (Icon) and the downloader.py file (Exec), by defualt they are set to the locations of these files on my machine

5. Open terminal window and execute the following commands with the location of downloader.py, in repo folder (first command) and location of py.desktop, in Desktop folder (second command):

chmod u+x /home///<downloader.py>

then

gio set /home///<.desktop file> metadata::trusted true

6. If clicking on the icon does not work, right click on the icon and click "allow launching"

# future updates
- make GUI more pretty
- add downloading progress bar