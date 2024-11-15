import cv2
import mediapipe as mp
import pyautogui

# Initialize hand tracking
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.5)

# Set up cv2 video capture with your webcam
cap = cv2.VideoCapture(0)  # Use 0 for the default camera, you can change it if you have multiple cameras

# Set up pyautogui screen dimensions
screen_width, screen_height = pyautogui.size()

# Main loop
while True:
    # Capture the frame from the webcam
    ret, frame = cap.read()
    if not ret:
        break

    # Flip the frame horizontally for a later selfie-view display
    frame = cv2.flip(frame, 1)

    # Convert the BGR image to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the image and get hand landmarks
    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        # Get the landmarks of the first detected hand
        hand_landmarks = results.multi_hand_landmarks[0]

        # Extract specific landmarks for hand tracking (e.g., index finger tip)
        index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]

        # Map hand landmarks to screen coordinates
        x, y = int((1 - index_finger_tip.x) * screen_width), int(index_finger_tip.y * screen_height)

        # Move the mouse cursor to the calculated position
        pyautogui.moveTo(x, y)

        # Perform a click action if the index finger is closed (optional)
        if index_finger_tip.y < hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP].y:
            pyautogui.click()

    cv2.imshow("Virtual Mouse", frame)

    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all windows
cap.release()
cv2.destroyAllWindows()