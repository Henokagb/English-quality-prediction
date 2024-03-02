FROM continuumio/anaconda3:latest

RUN conda update -n base conda && \
    conda install jupyter -y

RUN python -c "import nltk; nltk.download('stopwords'); nltk.download('punkt'); nltk.download('wordnet')"

WORKDIR /

COPY requirements.txt .


RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install -r requirements.txt
RUN python -m spacy download en

COPY . .

EXPOSE 8888

CMD ["jupyter", "notebook", "--ip='*'", "--port=8888", "--no-browser", "--allow-root"]
