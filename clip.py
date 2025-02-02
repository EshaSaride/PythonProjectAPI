from transformers import CLIPProcessor, CLIPModel

try:
    # Load pre-trained CLIP model
    model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
    processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")
    print("CLIP Model installed and working correctly!")
except Exception as e:
    print(f"Error loading CLIP: {e}")
