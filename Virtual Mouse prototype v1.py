import cv2
import mediapipe as mp
import pyautogui

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

# Open the camera
cap = cv2.VideoCapture(0)# Set the camera index (usually 0 for built-in webcam)

while True:
    # Read a frame from the camera
    ret, frame = cap.read()

    # Flip the frame horizontally (optional, depending on your setup)
    frame = cv2.flip(frame, 1)

    # Convert the frame to RGB for Mediapipe
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame with Mediapipe Hands
    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        # Get the landmarks of the first detected hand
        hand_landmarks = results.multi_hand_landmarks[0]

        # Get the coordinates of the tip of the index finger
        index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]

        # Convert normalized coordinates to pixel values
        h, w, _ = frame.shape
        # Invert the x-coordinate value
        x = w - int(index_finger_tip.x * w)
        y = int(index_finger_tip.y * h)

        # Move the mouse to the fingertip position
        pyautogui.moveTo(x, y)

    # Display the frame
    cv2.imshow("Virtual Mouse", frame)

    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close the OpenCV window
cap.release()
cv2.destroyAllWindows()
