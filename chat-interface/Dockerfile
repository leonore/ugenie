FROM python:3-onbuild
RUN python -m spacy download en

# expose Flask port number
EXPOSE 5000

# run application
CMD ["python", "main.py"]
