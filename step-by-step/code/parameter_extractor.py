import functions_file as ff
import inspect
import json
import sys
import os


def extract_info(func, ignore_params=['driver']):
    """ Extracts the function information, that is, name,
    mandatory parameters, optional parameters and their arguments.
    Parameters:
            func -- some function object
            ignore_params -- parameters to ignore on return

    Returns:
            The function name and parameters.
    """
    name = func.__code__.co_name
    optional_params = dict()
    mandatory_params = list()
    signature = inspect.signature(func)
    for k, v in signature.parameters.items():
        if v.default is not inspect.Parameter.empty:
            optional_params[k] = v.default
        else:
            if k not in ignore_params:
                mandatory_params.append(k)

    func_info = {
        'name': name,
        'mandatory_params': mandatory_params,
        'optional_params': optional_params
    }
    return func_info

def import_by_path(module_path):
    module_folder_path = os.path.dirname(module_path)
    module_name = os.path.basename(module_path)
    sys.path.append(module_folder_path)
    module = __import__(module_name[:-3])
    return module



def get_module_functions(module_path):
    """ Extracts the module functions.
    Parameters:
            module -- the module to extract the functions
    Returns:
            Module functions.
    """

    module = import_by_path(module_path)

    # module_folder_path = os.path.dirname(module_path)
    # module_name = os.path.basename(module_path)

    # sys.path.append(module_folder_path)

    # module = __import__(module_name[:-3])
    result = []
    for attr in dir(module):
        if type(getattr(module, attr)).__name__ == "function":
            result.append(getattr(module, attr))
    return result


def get_module_functions_info(module_path):
    """ 
    Returns a set with information of all the module functions
    """
    return [extract_info(i) for i in get_module_functions(module_path)]

