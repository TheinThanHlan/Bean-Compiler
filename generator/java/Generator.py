from . import bean
from . import controller
from . import dao
def generate(tokens):
    bean.generate(tokens)
    controller.generate(tokens)
    dao.generate(tokens)
