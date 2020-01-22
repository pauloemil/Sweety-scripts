from cx_Freeze import setup, Executable

base = None
                            #change my name
executables = [Executable("final.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {
        'packages':packages,
    },
}

setup(
    #change name if wanna 
    name = "finalla",
    options = options,
    version = "0.1",
    description = 'thehe',
    executables = executables
)

# shift + Rclick on folder to powershell
# python setup.py build
