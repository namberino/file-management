with open("desktopclean.py") as dsk, open("organization.py") as org:
    print("Cleaning the Desktop");
    print("");
    exec(dsk.read());
    print("\n\n\n");
    print("Reorganizing the files in the Downloads folder");
    print("");
    exec(org.read());
