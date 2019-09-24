from time import sleep

from app import celery
from .models import CommercialProposal, MainMetrics


# @celery.task(name='generate_tasks')
def generate_tasks_by_id(cp_id, kw_ids):
    import pdb;pdb.set_trace()
    pass


@celery.task(name='get-just-magic-info')
def get_just_magic_info():
    pass




@celery.task(name='sum-of-two-numbers')
def count_words():
    for i in range(5):
        sleep(1)
        print(i)
