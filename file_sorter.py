from pathlib import Path

folder = Path("test_folder_exit")

for file in folder.iterdir():
    print(file.suffix)

    x = file.suffix.lower()

    if file.is_dir():
        print(f"{file.name} is a folder")

    elif x in [".png", ".jpg", ".jpeg"]:
        print(f"{file.name} is this a image")

    elif x in [".mp4", ".avi", ".mov", ".mpeg"]:
        print(f"{file.name} is this a video")

    elif x in [".mp3", ".wav", ".flac"]:
            print(f"{file.name} is this a audio")

    elif x in [".txt", ".docx", ".pdf"]:
            print(f"{file.name} is this a document")

    elif x in [".zip", ".rar", ".tar"]:
            print(f"{file.name} is this a compressed file")

    elif x in [".exe", ".msi"]:
            print(f"{file.name} is this a executable file")

    elif x in [".html", ".css", ".js"]:
            print(f"{file.name} is this a web file")

    elif x in [".py", ".java", ".c", ".cpp"]:
            print(f"{file.name} is this a source code file")

    elif x in [".csv", ".xlsx", ".json"]:
            print(f"{file.name} is this a data file")

    else:
            print(f"{file.name} is this a unknown file type")