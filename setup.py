import cx_Freeze
executables=[cx_Freeze.Executable(script="STORM5.py",icon="assets2/naruto2.ico")]
cx_Freeze.setup(name="STORM5",
options={"build_exe": {"packages":["pygame"],
"include_files":["assets2"] }},
executables = executables
) 