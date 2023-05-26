import os
import shutil

downloads = "/Users/nam/Downloads/";
photos = "/Users/nam/Pictures/Downloads";
docs = "/Users/nam/Documents/Downloads";
books = "/Users/nam/Documents/Ebooks";

print("Scanning for files in the Downloads folder");
print("");

if len(os.listdir(downloads)) > 2:
    for file in os.scandir(downloads):
        basename = os.path.basename(file);
        extension = os.path.splitext(file);

        if extension[1] == '':
            continue;
        elif extension[1] == '.png' or extension[1] == '.jpg' or extension[1] == '.svg':
            print('Moving photo %s' % basename);
            shutil.move(file, photos);
        elif extension[1] == '.pdf' or extension[1] == '.doc':
            print("Moving document %s" % basename);
            shutil.move(file, docs);
        elif extension[1] == '.mobi' or extension[1] == '.epub':
            print("Moving ebook %s" % basename);
            shutil.move(file, books);
        else:
            continue;

    print("\nCompleted");
else:
    print("No file found");
