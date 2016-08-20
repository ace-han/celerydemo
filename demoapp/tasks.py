
from celery import shared_task
from celery.utils.log import get_task_logger
from demoapp import utils

logger = get_task_logger(__name__)

@shared_task(bind=True)
def add(self, x, y):
    result = utils.add(x, y)
    logger.info('add triggered task name: %s, result: %s', self.name, result)
    return result

@shared_task(bind=True)
def mul(self, x, y):
    result = utils.mul(x, y)
    logger.info('mul triggered task name: %s, result: %s', self.name, result)
    return result

@shared_task(bind=True)
def xsum(self, numbers):
    result = utils.xsum(numbers)
    logger.info('xsum triggered task name: %s, result: %s', self.name, result)
    return result  
    