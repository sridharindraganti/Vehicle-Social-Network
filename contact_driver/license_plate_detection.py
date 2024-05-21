import cv2
import numpy as np
import easyocr

def detect_license_plate():
    # Initialize the camera
    cap = cv2.VideoCapture(0)

    # Check if the camera is opened successfully
    if not cap.isOpened():
        print("Error: Could not open camera.")
        return None

    # Get the dimensions of the screen
    screen_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    screen_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Calculate the position of the rectangle box in the middle of the screen
    box_width = 200
    box_height = 100
    box_x = (screen_width - box_width) // 2
    box_y = (screen_height - box_height) // 2

    detected_text = None

    while True:
        # Read a frame from the camera
        ret, frame = cap.read()

        # Check if the frame was read successfully
        if not ret:
            print("Error: Could not read frame.")
            break

        # Create a mask for the license plate box
        mask = np.zeros_like(frame)
        mask[box_y:box_y + box_height, box_x:box_x + box_width] = frame[box_y:box_y + box_height,
                                                                  box_x:box_x + box_width]

        # Apply a blur effect to the mask
        blurred_mask = cv2.GaussianBlur(mask, (15, 15), 0)

        # Combine the original frame and the blurred mask
        output_frame = cv2.addWeighted(frame, 0.7, blurred_mask, 0.3, 0)

        # Draw the predefined rectangular box
        cv2.rectangle(output_frame, (box_x, box_y), (box_x + box_width, box_y + box_height), (255, 0, 0), 2)

        # Display the frame with the rectangular box
        cv2.imshow('License Plate Detection', output_frame)

        # Check for key press events
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        elif key == ord('c'):
            # Use EasyOCR to read text from the captured image
            reader = easyocr.Reader(['en'])
            result = reader.readtext(frame[box_y:box_y + box_height, box_x:box_x + box_width], detail=0)
            detected_text = ' '.join(result)
            print("Detected text:", detected_text)

            # Release the camera and close all windows
            cap.release()
            cv2.destroyAllWindows()

            return detected_text

    # Release the camera and close all windows
    cap.release()
    cv2.destroyAllWindows()

    return detected_text