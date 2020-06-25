import inspect


def generate_head(module):
    code = "import sys \n" + "sys.path.append(\"code\")\n"
    code = code + "from " + module.__name__ + " import *\n\n"
    code = code + "async def execute_steps(**missing_argument):\n"
    return code



def generate_body(recipe, module):
    code = ""
    for child in recipe['children']:
        if child['step'] == 'for':
            code = code + (child['depth']) * '    ' \
                + 'for ' + child['iterator'] \
                + ' in ' + child['iterable']['step'] \
                + '(**' + str(child['iterable']['arguments']) \
                + '):' + '\n'
            code = code + generate_code(child, module)

        elif child['step'] == 'while':
            pass

        elif child['step'] == 'if':
            pass
            
        elif child['step'] == 'attribution':
            code = code + (child['depth']) * '    ' + \
                child['to'] + ' = ' + str(child['from']) + '\n'

        elif inspect.iscoroutinefunction(getattr(module, child['step'])):
            code = code + (child['depth']) * '    ' \
                + 'await ' + child['step'] + '(**'+ str(child['arguments']) +', **missing_argument)' + '\n'
            
        
        else:
            code = code + (child['depth']) * '    ' \
                + child['step'] \
                + '(**' + str(child['arguments']) \
                + ')\n'
    return code



def generate_code(recipe, module):
    code = generate_head(module)
    code = code + generate_body(recipe, module)
    return code