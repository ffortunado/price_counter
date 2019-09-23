from time import sleep

from app import celery


@celery.task
def generate_tasks_by_id()


@celery.task
def count_words():
    for i in range(5):
        sleep(1)
        print(i)
