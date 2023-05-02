import torch
import os
from diffusers import StableDiffusionPipeline

num_inferences = 4

while True:
    style = input("Select an option (vivid or minimalistic): ").lower()
    if style == "vivid":
        break
    elif style == "minimalistic":
        break
    else:
        print("Invalid option selected. Please choose either 'vivid' or 'minimalistic'.")

color = input("Select a color: ")
background = input("Select the contents of the background: ")
prompt = f"{style} with {color} colors and {background} in the background"

pipe = StableDiffusionPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5", torch_dtype=torch.float16)
pipe.unet.load_attn_procs("./login_simple")
pipe = pipe.to("cuda")

os.makedirs("samples", exist_ok=True)

for i in range(num_inferences):
    image = pipe(
        prompt, num_inference_steps=50
    ).images[0]
    image.save(f'samples/{prompt.replace(" ", "_")}_{i+1}.png')
