from PIL import Image

def create_gif(image_paths, output_gif_path, duration=250):
 images = [Image.open(image_path) for image_path in image_paths]
# Save as GIF
 images[0].save(
 output_gif_path,
 save_all=True,
 append_images=images[1:],
 duration=duration,
 loop=0 # 0 means infinite loop
 )

if __name__ == "__main__":
 # List of image file paths
 image_paths = ["1.jpg", "2.jpg", "3.jpg", "4.jpg"] # Add your file paths
# Output GIF path
 output_gif_path = "output.gif"
# Create GIF
 create_gif(image_paths, output_gif_path)

print(f"GIF created and saved at {output_gif_path}")