import json
from ibm_watson import VisualRecognitionV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# Replace these with your actual IBM Cloud credentials
api_key = "YOUR_API_KEY"
url = "YOUR_SERVICE_URL"

# Initialize the Watson Visual Recognition service
authenticator = IAMAuthenticator(api_key)
visual_recognition = VisualRecognitionV3(
    version="2018-03-19",
    authenticator=authenticator
)
visual_recognition.set_service_url(url)

# Specify the image file you want to analyze
image_path = 'path_to_your_image.jpg'

# Classify the image
with open(image_path, 'rb') as image_file:
    classes = visual_recognition.classify(
        image_file,
        threshold='0.6',  # Adjust the threshold as needed
        owners=["me"])  # You can specify your own custom classifiers here

# Process the results
if classes is not None and 'images' in classes:
    for image in classes['images']:
        if 'classifiers' in image:
            for classifier in image['classifiers']:
                for cls in classifier['classes']:
                    class_name = cls['class']
                    score = cls['score']
                    print(f"Class: {class_name}, Score: {score}")
else:
    print("No classes found in the image.")

