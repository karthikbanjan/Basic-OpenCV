# Code by Karthik Banjan

import cv2 as cv


# Function to rescale image/frame
def rescale(img, scale):
    return cv.resize(img, None, fx=scale, fy=scale)


while True:
    print()
    print("1. WebCam Capture")
    print("2. Video File Display and Rescale")
    print("3. Image File Display and Rescale")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        cap = cv.VideoCapture(0)
        while True:
            ret, frame = cap.read()
            cv.imshow("WebCam", frame)
            if cv.waitKey(1) & 0xFF == ord('q'):
                break
        cap.release()
        cv.destroyAllWindows()

    elif choice == 2:
        video_path = input("Please provide the video path: ")
        cap = cv.VideoCapture(video_path)
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            cv.imshow("Video", frame)
            if cv.waitKey(1) & 0xFF == ord('q'):
                break
        cap.release()
        cv.destroyAllWindows()

        print()
        print("Do you wish to rescale the video?")
        print("1. Yes")
        print("2. No")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            cap = cv.VideoCapture(video_path)
            scale = float(input("Enter the scale: "))
            while True:
                ret, frame = cap.read()
                if not ret:
                    break
                frame = rescale(frame, scale)
                cv.imshow("Video", frame)
                if cv.waitKey(1) & 0xFF == ord('q'):
                    break
            cap.release()
            cv.destroyAllWindows()

        elif choice == 2:
            print("Video rescaling not required")

    elif choice == 3:
        img_path = input("Please provide the image path: ")
        img = cv.imread(img_path)
        cv.imshow("Image", img)
        cv.waitKey(0)
        cv.destroyAllWindows()

        print()
        print("Do you wish to display the image in different sizes?")
        print("1. Yes")
        print("2. No")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            print("Enter the scale factor: ")
            scale = float(input())
            img = rescale(img, scale)
            cv.imshow("Image", img)
            cv.waitKey(0)
            cv.destroyAllWindows()

        elif choice == 2:
            print("Image rescaling not required")

    elif choice == 4:
        break
