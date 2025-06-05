import gradio as gr
from model.model_loader import run_drs_cam
from PIL import Image
import os

# Ensure output directory exists
os.makedirs('static/outputs', exist_ok=True)

def process_image(image: Image.Image):
    # Save the uploaded image temporarily
    temp_input_path = "temp_input.jpg"
    image.save(temp_input_path)

    # Run your model function
    output_path = run_drs_cam(temp_input_path)

    # Return the output image file path to Gradio
    return output_path

iface = gr.Interface(
    fn=process_image,
    inputs=gr.Image(type="pil"),
    outputs=gr.Image(type="filepath"),
    title="DRS-CAM Visualizer",
    description="Upload an image to get the DRS-CAM heatmap overlay."
)

if __name__ == "__main__":
    iface.launch()
