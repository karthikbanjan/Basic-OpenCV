# Code by Karthik Banjan

import cv2 as cv


# Function to rescale image/frame
def rescale(img, scale):
    return cv.resize(img, None, fx=scale, fy=scale)


# Function to display image with scaling
def display_img(img, scale=1.0):
    img = rescale(img, scale)
    cv.imshow("Image", img)
    cv.waitKey(0)
    cv.destroyAllWindows()


# Function to display video with scaling
def display_video(vid_path, vid_title, scale=1.0):
    cap = cv.VideoCapture(vid_path)

    while True:
        ret, frame = cap.read()
        if not ret:
            cap.release()
            cv.destroyAllWindows()
            return

        frame = rescale(frame, scale)
        cv.imshow(vid_title, frame)

        if cv.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv.destroyAllWindows()


while True:
    print()
    print("1. WebCam Capture")
    print("2. Video File Display and Rescale")
    print("3. Image File Display and Rescale")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        display_video(0, "Webcam")

    elif choice == 2:
        video_path = input("Please provide the video path: ")
        cap = cv.VideoCapture(video_path)
        display_video(video_path, "Original Video")

        print()
        print("Do you wish to rescale the video?")
        print("1. Yes")
        print("2. No")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            cap = cv.VideoCapture(video_path)
            scale = float(input("Enter the scale factor: "))
            display_video(video_path, "Scaled Video", scale)

        elif choice == 2:
            print("Video rescaling not required.")

    elif choice == 3:
        img_path = input("Please provide the image path: ")
        img = cv.imread(img_path)
        display_img(img)

        print()
        print("Do you wish to display the image in different sizes?")
        print("1. Yes")
        print("2. No")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            scale = float(input("Enter the scale factor: "))
            display_img(img, scale)

        elif choice == 2:
            print("Image rescaling not required.")

    elif choice == 4:
        print("Thank you for using this program!")
        break
