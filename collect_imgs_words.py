import os
import cv2

# Path to the directory for storing data
DATA_DIR = r'C:\Users\MAAZ ALI BAIG\sign-language-and-speech-recognition-mab\data_words'

# Ensure the base dataset directory exists
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

number_of_classes = 5  # Number of word classes
dataset_size = 100     # Number of images per class

cap = cv2.VideoCapture(0)

# Loop through each class to collect images
for j in range(number_of_classes):
    class_dir = os.path.join(DATA_DIR, str(j))
    if not os.path.exists(class_dir):
        os.makedirs(class_dir)  # Create a subdirectory for the class

    print(f'Collecting data for class {j}')

    # Wait for the user to press 'Q' to start capturing images
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture frame from webcam.")
            break

        cv2.putText(frame, '', (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3,
                    cv2.LINE_AA)
        cv2.imshow('frame', frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):  # Wait for 'Q' to start capturing
            break

    # Capture `dataset_size` images for the current class
    counter = 0
    while counter < dataset_size:
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture frame from webcam.")
            continue

        # Show the frame
        cv2.imshow('frame', frame)

        # Save the frame to the appropriate class directory
        img_path = os.path.join(class_dir, f'{counter}.jpg')
        success = cv2.imwrite(img_path, frame)
        if success:
            counter += 1
        else:
            print(f"Failed to save image: {img_path}")

        # Brief pause to control frame rate
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
print("Data collection completed!")
