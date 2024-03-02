# English Quality Prediction

The goal of this model is to provide a score to an essay based on thousands of graded essays.

## Usage

The main notebook is located in `model_test.ipynb`.

### Running Locally

To run this notebook locally or in a Python environment:

1. Install the required dependencies:
   
   ```bash
   pip install -r requirements.txt

2. Use the command:

   ```bash
   jupyter notebook

Or open jupyter notebook graphically.
If you are in a python environment, don't forget to lauch jupyter notebook inside this environment


###Whith Docker

Build the image

   ```bash
   docker build -t english-grader .

Run the image
   ```bash
   docker run -p 8888:8888 english-grader

Finally, open the file model_test.ipynb and run all the cells
