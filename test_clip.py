# Import required libraries
from transformers import CLIPProcessor, CLIPModel
from PIL import Image
import requests
from io import BytesIO

# Load CLIP model and processor
model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

# ✅ Fix: Use a valid image URL
image_url = "https://cdn.britannica.com/91/82291-050-EB7A276A/Mohandas-K-Gandhi-leader-Mahatma-Indian.jpg"

# Download and open the image properly
response = requests.get(image_url)
if response.status_code == 200:  # Check if request was successful
    image = Image.open(BytesIO(response.content))
else:
    raise Exception("Failed to download image.")

# Define test text prompts
text_inputs = ["Mahatma Gandhi","Nelson Mandela","Dr Ambedkar"]


# Process the inputs
inputs = processor(text=text_inputs, images=image, return_tensors="pt", padding=True)

# Get CLIP model predictions
outputs = model(**inputs)
logits_per_image = outputs.logits_per_image  # Similarity scores
probs = logits_per_image.softmax(dim=1)  # Convert scores to probabilities

# Print results
for text, prob in zip(text_inputs, probs[0]):
    print(f"Text: '{text}' - Probability: {prob.item():.4f}")
