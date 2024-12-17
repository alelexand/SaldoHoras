from cx_Freeze import setup, Executable
base = None

executables = [
    Executable("executor.py", base=base)
]

buildOptions = dict(
    packages=[],
    includes=["openpyxl", "pyautogui", "selenium", "sqlite3", "getpass", "pandas", "win32"],
    include_files=["Arquivo", "chromedriver.exe"],
    excludes=[]
)

setup(
    name="AppDeComplementoFolhaDePonto",
    description="Gerar dados do Banco de horas",
    options=dict(build_exe=buildOptions),
    executables=executables
)

'''BY: ALEXANDRE AUTOMAÇÃO'''