In this repo you can find the last part of the diffusion model ISY project. It is based on this repo:
 https://github.com/lllyasviel/ControlNet
Please take look into the results folder:
The initial testing_folder contains some images and their variations created using gradio_canny2image.py.
The toy_example folder contains some exemplary results from fine-tuning ControlNet on the toy dataset
provided by the repository (training/fill50k). The poses folder contains some exemplary fine-tuning results on human
pose data (training/poses).

Training can be done following the steps described in docs/train.md. If it is supposed to be performed on a different
dataset from the toyexample fill50k, just set it at the top of tutorial_dataset.py

The training data for the poses was taken from here https://huggingface.co/datasets/sayakpaul/poses-controlnet-dataset/tree/main/data
The download yields the poses.parquet file. The data was converted to a form that matches the original toy_example using
convert_dataset.py. Thereafter, it was used for fine-tuning.

A side note: Since I am working on a Laptop with a 8GB VRAM GPU I had to set save_memory in the config.py to TRUE and
the batch_size to 1. As a result the training process with these settings is very slow. If you are on a machine
with a better GPU, consider setting it back to FALSE and also increase the batch_size in the tutorial_train.py
to whatever your device can handle.