import os
import shutil

desktop = "/Users/nam/Desktop";

print("Scanning for files and folders on desktop");
print('');

if len(os.listdir(desktop)) != 0:
    for file in os.scandir(desktop):
        print("Removing %s" % os.path.basename(file));

        if os.path.isdir(file):
            shutil.rmtree(file);
        else:
            os.remove(file);

    print("\nCleaned the desktop");
else:
    print("No file found");
