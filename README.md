# DeepST

DeepST is a novel telepresence solution that employs deep learning techniques to enhance semantic communication and improve video conferencing capabilities. The project aims to develop a prototype that addresses two critical interdependent tasks: designing the overall software system architecture (SC+JSCC) and developing a deep learning-enabled joint source coding channel (JSCC) pipeline for low-bitrate communication.

## Installation Instructions

### SC
To get the SC code running, please refer to the instructions provided [here](https://github.com/tpulkit/txt2vid).

### JSCC

Run the test.py file, which establishes a communication pipeline that includes both the SC and JSCC channels.

#### Training and Testing Procedures

The deepst-v4.2.ipynb Jupyter Notebook file encompasses all necessary steps for environment setup, data preprocessing, model configuration, training, and testing. You can retrain the model by modifying parameters within this file. Additionally, the JSCC folder includes small samples of the text data utilized in the training process.

For testing the model's accuracy (input and output text), run the DeepST-run-v3.ipynb file.

#### JSCC Neural Network Structure

![JSCC Neural Network Structure](https://github.com/JuicyMango123/DeepST-Portfolio/blob/main/JSCC/Images/Neural-Network.png)

#### JSCC Training Framework

![JSCC Training Framework](https://github.com/JuicyMango123/DeepST-Portfolio/blob/main/JSCC/Images/Training-Framework.png)

## Acknowledgements

The SC code segment is based off Txt2Vid
 - [Txt2Vid](https://github.com/tpulkit/txt2vid)