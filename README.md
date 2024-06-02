# Hand_Recognition_Controller 
The Hand_Recognition_Controller revolutionizes human-computer interaction by streamlining the use of Hand Gestures and Recognition, ushering in a new era of seamless computing experiences. This groundbreaking system minimizes direct physical contact with the computer, enabling users to effortlessly navigate input and output operations through a combination of static and dynamic hand gestures and recognition. Leveraging cutting-edge advancements in Machine Learning and Computer Vision, this project employs sophisticated algorithms to accurately interpret hand gestures and recognition, all without the need for additional hardware. Utilizing state-of-the-art models like Convolutional Neural Networks (CNN) integrated with MediaPipe and implemented via pybind11, it comprises two distinct modules: one tailored for direct hand interactions utilizing MediaPipe Hand detection, and the other compatible with gloves of any uniform color. Currently optimized for the Windows platform, this system promises a seamless and intuitive computing experience. 

Note: Python version 3.8.5 is recommended for optimal performance.

# Features
### Neutral Gesture
### Move Cursor
### Left Click
### Right Click
### Double Click
### Scrolling
### Drag and Drop
### Multiple Item Selection
### Volume Control
### Brightness Control

# Getting Started

  ### Pre-requisites
  
  Python: (3.6 - 3.8.5)<br>
  
  ### Procedure
  ```bash
  git clone https://github.com/nabilafatika/Hand_Recognition_Controller.git
  ```
  For detailed information about cloning visit [here](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository-from-github/cloning-a-repository).
  
  Step 1: 
  ```bash
  pip install Flask
  ```
  
  Step 2:
  ```bash
 pip show flask 
  ```
  
  Step 3:
  ```bash
  pip install -r requirements.txt
  ```
  
  Step 4:
  ```bash 
  pip install pywin32

  ```
  Step 5:
  For running app.py:
  ```bash 
  python app.py
  ```
### Credit :
<p>This project is an adaptation of a GitHub resource ([link](https://github.com/xenon-19/Gesture-Controlled-Virtual-Mouse.git)) that greatly contributed to my understanding of machine learning, particularly in hand recognition. This resource provided essential knowledge, helping me to comprehend and undertake this project.</p>

<p>Hand recognition involves identifying and interpreting hand gestures using computer vision and machine learning techniques. Through the GitHub resource, I learned about feature extraction, pattern recognition, and algorithms like convolutional neural networks (CNNs) that are effective for image recognition tasks.</p>

<p>Driven by curiosity, I adopted a "project-based learning - learning by doing" approach. This hands-on method allowed me to apply theoretical knowledge practically, enhancing my understanding and skills. I experimented with various machine learning techniques, data preprocessing, model training, and evaluation to refine hand recognition systems.</p>

<p>This project not only improved my technical skills but also deepened my appreciation for the practical applications of machine learning in computer vision. It highlights the effectiveness of curiosity-driven exploration and hands-on learning in mastering complex subjects.</p>
<p>Nabila Fatika - 2024</p>
