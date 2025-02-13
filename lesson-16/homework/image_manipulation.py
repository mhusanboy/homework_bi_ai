from pathlib import Path
import numpy as np 
from PIL import Image

current_dir = Path(__file__).resolve().parent



def save_file(arr, name, mode = 'RGB'):
    img = Image.fromarray(arr, mode=mode)
    img.save(current_dir/f'{name}.jpg')

def flip_image(image_loc):
    name_without_ext = image_loc[:-4]
    with Image.open(current_dir/image_loc) as img:
        img_arr = np.array(img)
        flipped = img_arr[::-1, ::-1, :]
        save_file(flipped, name_without_ext + '_flipped')

def add_random_noise(image_loc):
    name_without_ext = image_loc[:-4]
    with Image.open(current_dir/image_loc) as img:
        img_arr = np.array(img)
        mean = 0
        std = 30
        noised = np.clip(img_arr + np.random.normal(mean, std, img_arr.shape), 0, 255).astype(np.uint8)
        save_file(noised, name_without_ext+'_noised')

def brighten_channels(image_loc, val):
    name_without_ext = image_loc[:-4]
    with Image.open(current_dir/image_loc) as img:
        img_arr = np.array(img)
        brightened = np.clip(img_arr + val, 0, 255).astype(np.uint8)
        save_file(brightened, name_without_ext+'_brightened')

def apply_mask(image_loc):
    name_without_ext = image_loc[:-4]
    with Image.open(current_dir/image_loc) as img:
        img_arr = np.array(img)
        h, w, _ = img_arr.shape 
        h = (h - 100) // 2
        w = (w - 100) // 2
        for i in range(h, h + 100):
            for j in range(w, w + 100):
                img_arr[i,j] = np.array([0, 0, 0])
        save_file(img_arr, name_without_ext + '_masked')


img_file = 'images/birds.jpg'

flip_image(img_file)
add_random_noise(img_file)
brighten_channels(img_file, 0)
apply_mask(img_file)