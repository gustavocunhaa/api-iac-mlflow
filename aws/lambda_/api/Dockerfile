# Define python version build argument
ARG VERSION_PYTHON
           
# Pull python image
FROM public.ecr.aws/lambda/python:${VERSION_PYTHON}
           
# Switch to task root
WORKDIR ${LAMBDA_TASK_ROOT}
           
# Install requirements
COPY requirements.app.txt ${LAMBDA_TASK_ROOT}
RUN pip install -r requirements.app.txt
           
# Prepare function directory
COPY src ${LAMBDA_TASK_ROOT}/src/
COPY aws ${LAMBDA_TASK_ROOT}/aws/
           
# Prepare function execution
WORKDIR ${LAMBDA_TASK_ROOT}
CMD ["aws.lambda_.api.lambda_function.handler"]