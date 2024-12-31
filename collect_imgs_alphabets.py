import os
import cv2

# Path to the dataset directory
DATA_DIR = r'C:\Users\MAAZ ALI BAIG\sign-language-and-speech-recognition-mab\data_alphabets'

# Create the dataset directory if it doesn't exist
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

number_of_classes = 26  # Total classes (e.g., A-Z)
dataset_size = 100      # Number of images per class

# Initialize video capture
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    raise IOError("Cannot open webcam. Ensure it's properly connected and accessible.")

for class_id in range(number_of_classes):
    # Create a directory for the current class if it doesn't exist
    class_dir = os.path.join(DATA_DIR, str(class_id))
    if not os.path.exists(class_dir):
        os.makedirs(class_dir)

    print(f'Collecting data for class {class_id}. Get ready!')

    # Wait for user to signal readiness
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to read frame from webcam.")
            continue

        # Display instruction on the screen
        cv2.putText(frame, '', (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
        cv2.imshow('frame', frame)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    # Capture `dataset_size` images for the class
    counter = 0
    while counter < dataset_size:
        ret, frame = cap.read()
        if not ret:
            print("Failed to read frame from webcam.")
            continue

        # Show progress and display frame
        cv2.putText(frame, f'Capturing {counter + 1}/{dataset_size}', (50, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
        cv2.imshow('frame', frame)

        # Save the frame
        img_path = os.path.join(class_dir, f'{counter}.jpg')
        success = cv2.imwrite(img_path, frame)
        if success:
            counter += 1
        else:
            print(f"Failed to save image: {img_path}")

        # Wait briefly to avoid high frame rate
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
print("Data collection completed!")
