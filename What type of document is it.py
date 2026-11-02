archive = input("Enter the file name and file type:  ")
if archive.endswith(".mp4") or archive.endswith(".avi") or archive.endswith(".mov"):
    print("The file is a video.")
elif archive.endswith(".mp3") or archive.endswith(".wav") or archive.endswith(".flac"):
    print("The file is a audio file.")
elif archive.endswith(".jpg") or archive.endswith(".png") or archive.endswith(".jpeg"):
    print("The file is an image.")
elif archive.endswith(".pdf") or archive.endswith(".docx") or archive.endswith(".txt"):
    print("The file is a document.")
else:
    print("The file type is not recognized.")