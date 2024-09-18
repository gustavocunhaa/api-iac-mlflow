FROM public.ecr.aws/lambda/python:3.12

# Install the function's dependencies using file requirements.txt
COPY requirements.txt  .
RUN  pip3 install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"

# Copy function code
COPY predict.py ${LAMBDA_TASK_ROOT}
COPY config.yaml ${LAMBDA_TASK_ROOT}
COPY api.py ${LAMBDA_TASK_ROOT}

# Set the CMD to your handler
CMD [ "api.handler" ]