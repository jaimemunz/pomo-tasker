
class Task:

    def __init__(self):
        self.task_list = []
        self.current_index = 0

        
    def add_task(self, task, time = 5):
        task_time_pair = (task, time)
        self.task_list.append(task_time_pair)

    def get_tasks(self):
        return self.task_list

    def get_current_task(self):
        print self.task_list[self.current_index][0]

    def get_next_task(self):
        self.current_index += 1
        return self.task_list[self.current_index][0]


task_list = Task()

task_list.add_task("Task One", 20)
task_list.add_task("Task Two", 30)
task_list.add_task("Task Three", 40)
task_list.get_current_task()
