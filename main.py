import cv2
import numpy as np

# Create a blank parking lot
width, height = 600, 400
parking_lot = np.zeros((height, width, 3), dtype=np.uint8)

# Draw parking spaces
for i in range(0, width, 100):
    cv2.rectangle(parking_lot, (i, 50), (i + 80, 150), (255, 255, 255), 2)

# Initialize car positions
cars = [(i, 300) for i in range(0, width, 200)]

# Function to update car positions
def move_cars():
    global cars
    new_positions = []
    for x, y in cars:
        y -= 5  # Move cars upwards
        if y < 50:  # Reset car position if it reaches parking spots
            y = 300
        new_positions.append((x, y))
    cars = new_positions

# Simulation loop
while True:
    frame = parking_lot.copy()

    # Draw moving cars
    for x, y in cars:
        cv2.rectangle(frame, (x, y), (x + 50, y + 30), (0, 255, 0), -1)

    cv2.imshow("Parking Lot Simulation", frame)
    move_cars()

    if cv2.waitKey(100) & 0xFF == ord('q'):  # Press 'q' to exit
        break

cv2.destroyAllWindows()
