import numpy as np
from PIL import Image

# Load image
image = Image.open("images/birds.jpg")
img_array = np.array(image)

# Flip image horizontally and vertically
flipped_img = np.flipud(np.fliplr(img_array))

# Add random noise
noise = np.random.randint(-50, 50, img_array.shape, dtype=np.int16)
noisy_img = np.clip(img_array + noise, 0, 255).astype(np.uint8)

# Brighten the red channel
bright_img = img_array.copy()
bright_img[:, :, 0] = np.clip(bright_img[:, :, 0] + 40, 0, 255)

# Apply a black mask in the center
h, w, _ = img_array.shape
center_x, center_y = w // 2, h // 2
masked_img = img_array.copy()
masked_img[center_y-50:center_y+50, center_x-50:center_x+50] = [0, 0, 0]

# Save results
Image.fromarray(flipped_img).save("flipped.jpg")
Image.fromarray(noisy_img).save("noisy.jpg")
Image.fromarray(bright_img).save("brightened.jpg")
Image.fromarray(masked_img).save("masked.jpg")

print("Done! Check the saved images.")

