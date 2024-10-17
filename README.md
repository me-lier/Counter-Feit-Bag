# Counter-Feit-Bag

This project is aimed at detecting counterfeit bags using a machine learning model built with Keras and a web interface powered by Streamlit.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Installation

To run this project locally, follow the steps below:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/me-lier/Counter-Feit-Bag.git
    ```
2. **Navigate to the project directory**:
    ```bash
    cd Counter-Feit-Bag
    ```
3. **Install the required dependencies**:
    Run the following command in the terminal:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

To start the web application, run the following command in the terminal:
```bash
streamlit run app.py
```
This will launch the Streamlit app in your default web browser, where you can upload images of bags and get predictions on their authenticity.

## Project Structure

	•	app.py: The main file that runs the Streamlit app.
	•	model/: Directory containing the trained Keras model.
	•	data/: Directory for the dataset Images
	•	requirements.txt: Lists all the dependencies required to run the project.

## Contributing

Feel free to contribute by opening issues or submitting pull requests. For major changes, please open an issue to discuss what you would like to change.

## License

This project is licensed under the Apache License. See the LICENSE file for more details.
