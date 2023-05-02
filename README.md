# login-screen-lora

A github repo containing the LoRA weights for a fine-tuned model which was trained on Stable Diffusion 1.5.

## Dependencies

- Python
- pip
- a Nvidia graphics card with cuda enabled

## Setup

- Install dependencies with pip by executing the command: ```sh pip install -r requirements.txt```

## Inference

In order to perform inference all you need to do is to run the sample.py file. It doesn't let the user access the prompt directly since the output will suffer unless the prompt is constructed in a certain way.
