from database import engine, metadata_obj
from tables import tasks_tabe, users_table, posts_table, comments_table, movie_table, genre_table, genre_movie_table
from crud import (
    create_user,
    check_user,
    create_task, 
    get_tasks, 
    get_one_task, 
    delete_task, 
    update_task, 
    mark_as_complated, 
    mark_as_incomplated,
    get_movie_by_genre
)

metadata_obj.create_all(engine)

# print(get_movie_by_genre('komediya'))
# print(get_movie_by_genre('jangari'))
# create_user('sami', '12345')
# user = check_user('sami', '12345')
# print(user)
# test qiling har bir crud functionni
# create_task('kitob oqish')
# tasks = get_tasks()
# print(tasks)
# update_task(2, name='test', description='test')
# task = get_one_task(2)
# print(task)
# delete_task(2)
# mark_as_complated(5)
# mark_as_incomplated(30)
# try:
#     get_one_task(30)
# except:
#     print('task yoq')
