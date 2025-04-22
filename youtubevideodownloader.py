from pytube import YouTube

# Step 1: Ask for YouTube URL
url = input("Enter the YouTube video URL: ")

# Step 2: Create YouTube object
yt = YouTube(url)

# Step 3: Get the highest resolution stream
video = yt.streams.get_highest_resolution()

# Step 4: Download the video
video.download()

print("Download complete!")
