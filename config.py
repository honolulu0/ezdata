'''
配置文件
'''
import os
import json
from dotenv import load_dotenv
read_env = os.environ.get('read_env', True)
if read_env not in [False, None, '', '0']:
    dotenv_path = os.environ.get('ENV', 'dev.env')
    # dotenv_path = os.environ.get('ENV', 'prod.env')
    root_path = os.path.abspath(os.path.dirname(__file__)).split('src')[0]
    dotenv_path = os.path.join(root_path, dotenv_path)
    load_dotenv(dotenv_path=dotenv_path)
SYS_CONF = os.environ
# mysql相关配置
DB_HOST = SYS_CONF['DB_HOST']
DB_PORT = int(SYS_CONF['DB_PORT'])
DB_USER = SYS_CONF['DB_USER']
DB_PWD = SYS_CONF['DB_PWD']
DB_NAME = SYS_CONF['DB_NAME']
DB_CHARSET = SYS_CONF['DB_CHARSET']
DB_TYPE = SYS_CONF['DB_TYPE']
POOL_RECYCLE = int(SYS_CONF['POOL_RECYCLE'])  # session最大保持时间
ECHO_SQL = SYS_CONF['ECHO_SQL'] == '1'  # 是否打印sql
# es 相关配置
ES_HOSTS = json.loads(SYS_CONF['ES_HOSTS'])
ES_CONF = {
    'hosts': ES_HOSTS
}
ES_USER = SYS_CONF.get('ES_USER')
ES_PWD = SYS_CONF.get('ES_PWD')
if ES_USER not in [None, '']:
    ES_CONF['http_auth'] = (ES_USER, ES_PWD)
# 日志相关配置
LOG_LEVEL = SYS_CONF.get('LOG_LEVEL', 'INFO')
SYS_LOG_INDEX = SYS_CONF.get('SYS_LOG_INDEX', 'sys_logs')
INTERFACE_LOG_INDEX = SYS_CONF.get('INTERFACE_LOG_INDEX', 'interface_logs')
TASK_LOG_INDEX = SYS_CONF.get('TASK_LOG_INDEX', 'task_logs')
# redis 相关配置
REDIS_HOST = SYS_CONF['REDIS_HOST']
REDIS_PORT = int(SYS_CONF['REDIS_PORT'])
REDIS_PASS = SYS_CONF['REDIS_PWD']
REDIS_DB = int(SYS_CONF['REDIS_DB'])
# celery 配置
CELERY_BACKEND_URL = f'redis://:{REDIS_PASS}@{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}'
CELERY_BROKER_URL = f'redis://:{REDIS_PASS}@{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}'
CELERY_DEFAULT_QUEUE = SYS_CONF['CELERY_DEFAULT_QUEUE']
FLOWER_API_URL = SYS_CONF['FLOWER_API_URL']
SCHEDULER_API_URL = SYS_CONF['SCHEDULER_API_URL']
# 对象存储相关配置
OSS_TYPE = SYS_CONF['OSS_TYPE']
OSS_HOST = SYS_CONF['OSS_HOST']
OSS_PORT = SYS_CONF['OSS_PORT']
OSS_KEY = SYS_CONF['OSS_KEY']
OSS_SECRET = SYS_CONF['OSS_SECRET']
OSS_BUCKET = SYS_CONF['OSS_BUCKET']
# web相关配置
# 是否启用token刷新机制
USE_TOKEN_REFRESH = SYS_CONF['USE_TOKEN_REFRESH'] == '1'
# 用户token过期时间
TOKEN_EXP_TIME = int(SYS_CONF['TOKEN_EXP_TIME'])
# sqlalchemy配置
engine_db_config = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(
        DB_USER, DB_PWD, DB_HOST, DB_PORT, DB_NAME)
SQLALCHEMY_DATABASE_URI = engine_db_config
SQLALCHEMY_POOL_RECYCLE = POOL_RECYCLE
# 服务私钥
SECRET_KEY = SYS_CONF['SECRET_KEY']
# xorbits集群地址 local为本地
XORBITS_CLUSTER = SYS_CONF.get('XORBITS_CLUSTER', 'local')

