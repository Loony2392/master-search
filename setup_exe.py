
from cx_Freeze import setup, Executable

setup(
    name="Master Search",
    version="2025.11.19",
    description="Professional file search tool",
    executables=[
        Executable("gui_main.py", target_name="Master_Search"),
        Executable("cli_main.py", target_name="MasterSearch_CLI"),
    ],
)
