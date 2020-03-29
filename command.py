import funcs

def get_cmds():
    cmdarr = []

    for filename in funcs.get_listdir('/commands'):
        if filename == '__pycache__':
            continue
        if not '.' in filename:
            for filename2 in funcs.get_listdir(f'commands/{filename}'):
                if filename2.endswith('.py'):
                    modname = f'commands.{filename}.{funcs.remove_end(filename2)}' 
                mod = funcs.import_module(modname)

                cmdarr.append([mod.aliases, mod])
        if filename.endswith('.py'):
            modname = f'commands.{funcs.remove_end(filename)}' 
            mod = funcs.import_module(modname)

            cmdarr.append([mod.aliases, mod])

    return cmdarr
