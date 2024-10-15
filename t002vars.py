"""
urban university – python Junior grade course
implemented by gee3k (c) 2024-2025
"""

def start():
    if __name__ != "__main__":
        print( f"\n=* {__name__} *=")

    # variables
    print( "Variables" )
    tasks_count = 12
    spend_hours = 1.5
    course_name = "Python"
    average_task_time = spend_hours / tasks_count
    print( f"Курс: {course_name}, " +
           f"всего задач: {tasks_count}, " +
           f"затрачено часов: {spend_hours}, " +
           f"среднее время выполнения задачи: {average_task_time} " +
           "часа." )

if __name__ == "__main__":
    start()