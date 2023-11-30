## Sign Language Recognition using OpenCV

## Data Collection

This part of the project is focused on capturing and processing images for building a sign language dataset.

### Setup

- Install the required libraries:

  ```bash
  pip install opencv-python numpy math time cvzone
  ```

- Run the `data_collection.py` script:

  ```bash
  python data_collection.py
  ```

### Instructions

1. Launch the script to start capturing images from the webcam.
2. Place your hand in the camera frame to trigger hand detection.
3. Adjust the hand bounding box for optimal image cropping.
4. Press the 's' key to save the captured sign language image.
5. Images are saved in the specified folder (`Data/Z`) with unique filenames.

## Testing

This part involves testing the sign language recognition using a pre-trained model made by Google Teachable Machine.

### Setup

- Install the required libraries:

  ```bash
  pip install opencv-python numpy math cvzone
  ```

- Run the `testing.py` script:

  ```bash
  python testing.py
  ```

### Instructions

1. Launch the script to initiate real-time sign language recognition.
2. Place your hand in the camera frame for detection.
3. The recognized sign is displayed on the screen along with the bounding box.
4. The script uses a pre-trained model (`Model/keras_model.h5`) and labels (`Model/labels.txt`).

## Folder Structure

- **Data:**
  - **Z:** Captured images for data collection.
  - **C:** Processed images for testing.

## Dependencies

- OpenCV
- NumPy
- Math
- cvzone

## Contributing

Contributions are always welcome! If you have improvements or feature suggestions, please submit a pull request.

## License

This project is licensed under the [Your License] - see the [LICENSE.md](LICENSE.md) file for details.

## Contact

- Viraj Mulik
- virajmulik2304@gmail.com
  
