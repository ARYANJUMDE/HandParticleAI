# import cv2
# import mediapipe as mp

# # Webcam
# cap = cv2.VideoCapture(0)

# # Hand detector
# mpHands = mp.solutions.hands
# hands = mpHands.Hands()

# # Drawing utility
# mpDraw = mp.solutions.drawing_utils

# while True:
#     success, img = cap.read()

#     # Convert BGR to RGB
#     imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#     # Process hands
#     results = hands.process(imgRGB)

#     # If hands found
#     if results.multi_hand_landmarks:
#         for handLms in results.multi_hand_landmarks:

#             # Draw landmarks
#             mpDraw.draw_landmarks(
#                 img,
#                 handLms,
#                 mpHands.HAND_CONNECTIONS
#             )

#     # Show image
#     cv2.imshow("Hand Tracking", img)

#     # Quit
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()

#Index Finger Calculation 
# import cv2
# import mediapipe as mp

# # Webcam
# cap = cv2.VideoCapture(0)

# # MediaPipe Hands
# mpHands = mp.solutions.hands
# hands = mpHands.Hands()

# # Drawing Utility
# mpDraw = mp.solutions.drawing_utils

# while True:
#     success, img = cap.read()

#     # Flip image for mirror effect
#     img = cv2.flip(img, 1)

#     # Convert to RGB
#     imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#     # Process image
#     results = hands.process(imgRGB)

#     # Get image size
#     h, w, c = img.shape

#     # If hand detected
#     if results.multi_hand_landmarks:

#         for handLms in results.multi_hand_landmarks:

#             # Draw hand landmarks
#             mpDraw.draw_landmarks(
#                 img,
#                 handLms,
#                 mpHands.HAND_CONNECTIONS
#             )

#             # Get all landmark points
#             for id, lm in enumerate(handLms.landmark):

#                 # Convert landmark to screen coordinates
#                 cx = int(lm.x * w)
#                 cy = int(lm.y * h)

#                 # Detect index fingertip
#                 if id == 8:

#                     # Draw circle on fingertip
#                     cv2.circle(img, (cx, cy), 20, (255, 0, 255), cv2.FILLED)

#                     # Print coordinates
#                     print("Finger Position:", cx, cy)

#     # Show window
#     cv2.imshow("Finger Tracking", img)

#     # Exit with q
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()


# import cv2
# import mediapipe as mp
# import pygame
# import random
# import math

# # Initialize Pygame
# pygame.init()

# # Window size
# WIDTH, HEIGHT = 1280, 720

# # Create window
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Hand Particle System")

# # Webcam
# cap = cv2.VideoCapture(0)

# # MediaPipe Hands
# mpHands = mp.solutions.hands
# hands = mpHands.Hands()

# # Particle list
# particles = []

# # Create particles
# for i in range(200):
#     particles.append([
#     random.randint(0, WIDTH),   # x
#     random.randint(0, HEIGHT),  # y
#     random.uniform(-2, 2),      # velocity x
#     random.uniform(-2, 2)       # velocity y
# ])

# # Main loop
# running = True

# while running:

#     # Exit window
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     # Fill screen black
#     screen.fill((0, 0, 0))

#     # Read webcam
#     success, img = cap.read()

#     # Flip image
#     img = cv2.flip(img, 1)

#     # Convert to RGB
#     imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#     # Process hands
#     results = hands.process(imgRGB)

#     # Default finger position
#     finger_x = WIDTH // 2
#     finger_y = HEIGHT // 2

#     # If hand detected
#     if results.multi_hand_landmarks:

#         for handLms in results.multi_hand_landmarks:

#             # Get index fingertip
#             lm = handLms.landmark[8]

#             # Convert coordinates
#             finger_x = int(lm.x * WIDTH)
#             finger_y = int(lm.y * HEIGHT)
            
#     for particle in particles:
#         px, py, vx, vy = particle
#         # Direction to finger
#         dx = finger_x - px
#         dy = finger_y - py
#         distance = math.sqrt(dx**2 + dy**2)
#         # Attraction force
#         if distance < 200 and distance != 0:
#             force = 200 / distance
#             vx += (dx / distance) * force * 0.05
#             vy += (dy / distance) * force * 0.05
#         # Add friction
#         vx *= 0.95
#         vy *= 0.95
#         # Update position
#         px += vx
#         py += vy
#         # Keep inside screen
#         if px < 0 or px > WIDTH:
#             vx *= -1
#         if py < 0 or py > HEIGHT:
#             vy *= -1
#         # Save values
#         particle[0] = px
#         particle[1] = py
#         particle[2] = vx
#         particle[3] = vy
#         # Draw particle
#         pygame.draw.circle(
#             screen,
#             (0, 255, 255),
#             (int(px), int(py)),
#             3
#         )
#         # Draw finger point
#     pygame.draw.circle(
#         screen,
#         (255, 0, 255),
#         (finger_x, finger_y),
#         15
#     )

#     # Update display
#     pygame.display.update()

# # Quit
# cap.release()
# pygame.quit()
import cv2
import mediapipe as mp
import pygame
import random
import math

# Initialize
pygame.init()

# Screen
WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("AI Particle Universe")

clock = pygame.time.Clock()

# Webcam
cap = cv2.VideoCapture(0)

# MediaPipe
mpHands = mp.solutions.hands
hands = mpHands.Hands(
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

# Particles
particles = []

# Create particles
for i in range(100):

    particles.append([
        random.randint(0, WIDTH),      # x
        random.randint(0, HEIGHT),     # y
        random.uniform(-2, 2),         # vx
        random.uniform(-2, 2),         # vy
        random.randint(2, 5),          # size
        random.randint(100, 255),      # r
        random.randint(100, 255),      # g
        random.randint(100, 255)       # b
    ])

running = True

while running:

    clock.tick(60)

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fade effect
    fade = pygame.Surface((WIDTH, HEIGHT))
    fade.set_alpha(35)
    fade.fill((0, 0, 0))
    screen.blit(fade, (0, 0))

    # Webcam frame
    success, img = cap.read()

    if not success:
        continue

    img = cv2.flip(img, 1)

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    results = hands.process(imgRGB)

    # Default finger position
    finger_x = WIDTH // 2
    finger_y = HEIGHT // 2

    pinch = False

    # Hand detection
    if results.multi_hand_landmarks:

        for handLms in results.multi_hand_landmarks:

            # Index finger
            index_tip = handLms.landmark[8]

            finger_x = int(index_tip.x * WIDTH)
            finger_y = int(index_tip.y * HEIGHT)

            # Thumb finger
            thumb_tip = handLms.landmark[4]

            thumb_x = int(thumb_tip.x * WIDTH)
            thumb_y = int(thumb_tip.y * HEIGHT)

            # Distance between fingers
            pinch_distance = math.sqrt(
                (thumb_x - finger_x) ** 2 +
                (thumb_y - finger_y) ** 2
            )

            # Pinch gesture
            if pinch_distance < 40:
                pinch = True

    # Finger glow
    for radius in range(40, 0, -20):

        glow = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)

        pygame.draw.circle(
            glow,
            (255, 0, 255, 15),
            (finger_x, finger_y),
            radius
        )

        screen.blit(glow, (0, 0))

    # Update particles
    for particle in particles:

        px, py, vx, vy, size, r, g, b = particle

        dx = finger_x - px
        dy = finger_y - py

        distance = math.sqrt(dx**2 + dy**2)

        # Attraction
        if distance < 250 and distance != 0:

            force = 250 / distance

            vx += (dx / distance) * force * 0.08
            vy += (dy / distance) * force * 0.08

        # Explosion effect
        if pinch and distance < 200 and distance != 0:

            explode_force = 20 / distance

            vx -= (dx / distance) * explode_force * 15
            vy -= (dy / distance) * explode_force * 15

        # Floating randomness
        vx += random.uniform(-0.1, 0.1)
        vy += random.uniform(-0.1, 0.1)

        # Friction
        vx *= 0.96
        vy *= 0.96

        # Update position
        px += vx
        py += vy

        # Wall bounce
        if px < 0 or px > WIDTH:
            vx *= -1

        if py < 0 or py > HEIGHT:
            vy *= -1

        # Save
        particle[0] = px
        particle[1] = py
        particle[2] = vx
        particle[3] = vy

        # Color animation
        r = (r + random.randint(-2, 2)) % 255
        g = (g + random.randint(-2, 2)) % 255
        b = (b + random.randint(-2, 2)) % 255

        particle[5] = r
        particle[6] = g
        particle[7] = b

        # Glow
        glow_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)

        pygame.draw.circle(
            glow_surface,
            (r, g, b, 25),
            (int(px), int(py)),
            size * 5
        )

        screen.blit(glow_surface, (0, 0))

        # Main particle
        pygame.draw.circle(
            screen,
            (r, g, b),
            (int(px), int(py)),
            size
        )


    # Finger core
    pygame.draw.circle(
        screen,
        (255, 255, 255),
        (finger_x, finger_y),
        10
    )

    # Explosion visual
    if pinch:

        pygame.draw.circle(
            screen,
            (255, 100, 100),
            (finger_x, finger_y),
            40,
            3
        )

    # Update screen
    pygame.display.update()

# Quit
cap.release()
pygame.quit()