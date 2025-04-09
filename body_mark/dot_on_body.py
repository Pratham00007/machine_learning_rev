import cv2
import mediapipe as mp

# mediapipe is library developed by gooogle for
#  tracking body like hand , palm  it can also draw the line by joining points

mp_pose=mp.solutions.pose
# track the human pose wheer is hand , join full human skeleton
pose=mp_pose.Pose(static_image_mode=True,min_detection_confidence=0.5)
# it is saying i will give you picture not video ,
# if you get 50% probability just mark the location
mp_drawing=mp.solutions.drawing_utils
# to draw we assign this

# loading image
image_path="r1.jpg"
image=cv2.imread(image_path)
image_rgb=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
# bcs mediapipe need rgb image or video to process

# perform pose_estimation
results=pose.process(image_rgb)
# drawing landmarks
if results.pose_landmarks:
    print("Pose Landmark detected!")
    