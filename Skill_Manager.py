from Hal.Classes import Response
from Hal.Decorators import reg
from Hal.Skill import Skill

class Skill_Manager(Skill):
    def __init__(self):
        pass

    @reg(name='your_skill_name')
    def your_skill_name(self, required_param, optional_param='default value'):
        '''
        your_skill_name description

        :param string required_param: The required param description
        :param string optional_param: (Optional) The optional param description
        '''
        return Response(True, data='result data')
