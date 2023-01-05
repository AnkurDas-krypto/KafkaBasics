
import os

API_KEY = os.getenv('API_KEY',None)
ENDPOINT_SCHEMA_URL  = os.getenv('ENDPOINT_SCHEMA_URL',None)
API_SECRET_KEY = os.getenv('API_SECRET_KEY',None)
BOOTSTRAP_SERVER = os.getenv('BOOTSTRAP_SERVER',None)
ENDPOINT_SCHEMA_URL  = os.getenv('ENDPOINT_SCHEMA_URL',None)

SCHEMA_REGISTRY_API_KEY = os.getenv('SCHEMA_REGISTRY_API_KEY',None)
SCHEMA_REGISTRY_API_SECRET = os.getenv('SCHEMA_REGISTRY_API_SECRET',None)
SECURITY_PROTOCOL="SASL_SSL"
SSL_MACHENISM="PLAIN"
# API_KEY = os.getenv('7HUOJ656CYIV46ZK', None)
# ENDPOINT_SCHEMA_URL  = os.getenv('https://psrc-8kz20.us-east-2.aws.confluent.cloud',None)
# API_SECRET_KEY = os.getenv('c2RqxrFoESTLQgPzAs7QHjnEaAws/92WlG8NqdzUYXnBZl9sG9T0c9PICO8JC3Ju',None)
# BOOTSTRAP_SERVER = os.getenv('pkc-41voz.northamerica-northeast1.gcp.confluent.cloud:9092',None)
# SECURITY_PROTOCOL = os.getenv('SECURITY_PROTOCOL',None)
# SSL_MACHENISM = os.getenv('SSL_MACHENISM',None)
# SCHEMA_REGISTRY_API_KEY = os.getenv('4OFTK3XZVG2TGXO5',None)
# SCHEMA_REGISTRY_API_SECRET = os.getenv('HgfmZeReg+fL1pgMSx0CPhFHYrf8j2VNNx0XbET8sTGkjiKp1SSo658yl7i+Zwnd',None)


def sasl_conf():

    sasl_conf = {'sasl.mechanism': SSL_MACHENISM,
                 # Set to SASL_SSL to enable TLS support.
                #  'security.protocol': 'SASL_PLAINTEXT'}
                'bootstrap.servers':BOOTSTRAP_SERVER,
                'security.protocol': SECURITY_PROTOCOL,
                'sasl.username': API_KEY,
                'sasl.password': API_SECRET_KEY
                }
    print(sasl_conf)
    return sasl_conf



def schema_config():
    return {'url':ENDPOINT_SCHEMA_URL,
    
    'basic.auth.user.info':f"{SCHEMA_REGISTRY_API_KEY}:{SCHEMA_REGISTRY_API_SECRET}"

    }

if __name__ == '__main__':
    sasl_conf()

