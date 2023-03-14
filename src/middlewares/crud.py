from .crud_system.groups import GroupsController
from .crud_system.schedule import ScheduleController
from .crud_system.teachers import TeacherController
from .crud_system.admin import AdminController

class CrudController(GroupsController, ScheduleController, TeacherController, AdminController):
    def __init__(self) -> None:
        print('Crud Controller initialized!')
        
