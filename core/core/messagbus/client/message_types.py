from google._upb._message import Message


def get_pb2_messages(pb2_module):
    module_messages = {}
    for var in pb2_module._globals:
        print(var)
        print(type(var))
        print('----------')
        print(type(pb2_module._globals.get(var)))
        try:
            print(issubclass(pb2_module._globals.get(var), Message))
            module_messages[var] = pb2_module._globals.get(var)
        except TypeError:
            continue
        print('\n\n\n')
    return module_messages
