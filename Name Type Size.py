archive = input("Enter the file name and file type : ")
size = input("Enter the file size in MB: ")
if archive.endswith(".mp4") or archive.endswith(".avi") or archive.endswith(".mov"): 
    if size.endswith("MB") and int(size.replace("MB", "")) < 100:
        print("The file is a video and it is small in size.")
    elif size.endswith("MB") and int(size.replace("MB", "")) > 100 and int(size.replace("MB", "")) < 500:
        print("The file is a video and it is medium in size.")
    elif size.endswith("MB") and int(size.replace("MB", "")) > 500:
        print("The file is a video and it is large in size.")
else:
    print("The file is not a video")