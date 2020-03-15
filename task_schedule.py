try:
    from chapter_two.bin import task
except ModuleNotFoundError:
    from chapter_two.bin import task

if '__main__' == __name__:
    task.introduction()