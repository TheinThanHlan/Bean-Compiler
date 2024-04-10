from . import bean
from . import service


def generate(tokens):
    bean.generate(tokens)
    service.generate(tokens)
