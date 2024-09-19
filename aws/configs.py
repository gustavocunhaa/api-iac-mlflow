ACCOUNT = '851725532859'
REGION = 'us-east-1'
PROJECT_NAME = 'irisMlflow'

ENV = 'dev'

# Ref -> https://semver.org/
VERSION_MAJOR = 1 # Incrementar quando houver mudanças que quebrem a compatibilidade com versões anteriores
VERSION_MINOR = 0 # Incrementar quando houver mudanças que não quebrem a compatibilidade com versões anteriores
VERSION_PATCH = 0 # Incrementar quando houver correções de bugs / hotfixes / etc

# Versão do Python
VERSION_PYTHON = '3.12' # Afetará o backend lambda

# Configurações de usuários da API
API_USERS = [
    {"name":"bank"}
]

# Warmup da Lambda da API de acordo com um cron job
LAMBDA_WARMUP = {
    "parameter": "cron(*/2 * * * ? *)"
}

# Memory capacity in MB
LAMBDA_MEMORY = 1024