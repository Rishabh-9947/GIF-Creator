from PIL import Image, ImageSequence
import os

def create_gif(image_folder, output_filename, duration=500):
    # Ensure the output filename has the .gif extension
    output_path = f"{output_filename}.gif" if not output_filename.lower().endswith('.gif') else output_filename

    # Get all the image file paths
    images = [os.path.join(image_folder, f) for f in os.listdir(image_folder) if f.endswith(('.png', '.jpg', '.jpeg'))]
    images.sort()  # Sort the images by name (optional)

    # Open images and create the frames list
    frames = [Image.open(image) for image in images]

    # Ensure all frames are the same size
    widths, heights = zip(*(i.size for i in frames))
    max_width, max_height = max(widths), max(heights)
    frames_resized = [frame.resize((max_width, max_height), Image.Resampling.LANCZOS) for frame in frames]

    # Save the frames as a GIF
    frame_one = frames_resized[0]
    frame_one.save(output_path, format='GIF', append_images=frames_resized[1:], save_all=True, duration=duration, loop=0)
    print(f"GIF saved to {output_path}")

# Main function
if __name__ == "__main__":
    image_folder = input("Enter the folder containing images: ")
    output_filename = input("Enter the output GIF file name (with or without .gif extension): ")
    create_gif(image_folder, output_filename)