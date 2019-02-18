env_dir := ../venv
pip := $(env_dir)/bin/pip
python := $(env_dir)/bin/python
pyrcc5 := $(env_dir)/bin/pyrcc5
pyuic5 := $(env_dir)/bin/pyuic5

env:
	git init
	python3 -m venv $(env_dir)
	$(pip) install -r requirements.txt --process-dependency-links
	$(pip) install --upgrade pip

ui:
	$(pyrcc5) {{cookiecutter.package_name}}/ui_designer/resources.qrc --import-from {{cookiecutter.package_name}}.ui -o {{cookiecutter.package_name}}/ui_designer/resources_rc.py
	$(pyuic5) {{cookiecutter.package_name}}/ui_designer/mainwindow.ui --import-from {{cookiecutter.package_name}}.ui -o {{cookiecutter.package_name}}/ui_designer/mainwindow_qt.py")

