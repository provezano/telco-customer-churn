FROM python:3.8.11-slim 
ENV PYTHONUNBUFFERED=TRUE 
RUN pip --no-cache-dir install numpy scikit-learn flask gunicorn
WORKDIR /app 
COPY ["*.py", "churn-model.bin", "./"] 
EXPOSE 9696 
ENTRYPOINT ["gunicorn", "--bind", "0.0.0.0:9696", "churn_serving:app"]