# English Quality Prediction
Authors: @spero2003 , @YamamotoGenryuusai , @Marcel229225

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
If you are in a python environment, don't forget to launch jupyter notebook inside this environment


### With Docker

1. Build the image

   ```bash
   docker build -t english-grader .

2. Run the image

   ```bash
   docker run -p 8888:8888 english-grader

Open the file model_test.ipynb and run all the cells

When all the cell are run, go to the last cell and set the essay_example variable to the an essay of your choice. Then, run the cell again to get the note.

![Get the prediction](Screenshot.png)
