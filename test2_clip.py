# Import required libraries
from transformers import CLIPProcessor, CLIPModel
from PIL import Image
import requests
from io import BytesIO

# Load CLIP model and processor
model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

# ✅ Fix: Use a valid image URL
image_url = "https://i.pinimg.com/736x/0a/c8/71/0ac87183395fa1ef4d40bb04803e2aa3.jpg"

# Download and open the image properly
response = requests.get(image_url)
if response.status_code == 200:  # Check if request was successful
    image = Image.open(BytesIO(response.content))
else:
    raise Exception("Failed to download image.")

# Define test text prompts
text_inputs = ["This is a Golden Retriever", "This is a Husky", "This is a Labrador", "There are both Husky and Golden Retriever in picture"]


# Process the inputs
inputs = processor(text=text_inputs, images=image, return_tensors="pt", padding=True)

# Get CLIP model predictions
outputs = model(**inputs)
logits_per_image = outputs.logits_per_image  # Similarity scores
probs = logits_per_image.softmax(dim=1)  # Convert scores to probabilities

# Print results
for text, prob in zip(text_inputs, probs[0]):
    print(f"Text: '{text}' - Probability: {prob.item():.4f}")