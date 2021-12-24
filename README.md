# Photo Library Organizer

I made this for my camera roll on December 23, 2021 as a quick script for my own utility.

It takes a flat directory of files (in my case, my photos) and organizes them in folders by year and month.

For example, a file like `test.jpg` made in June 2019 would now be `2019/06/test.jpg`.

This uses Python 3 with modules `os`, `shutil`, and `datetime`. Since it takes the modified time, it should work in Windows, MacOS and Linux.

This was the most direct way for me to organize my photo library that I had backed up onto OneDrive from my phone over the past five years.