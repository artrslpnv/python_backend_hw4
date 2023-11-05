PATH := /Users/artrslpnv/opt/anaconda3/bin
PIP :=  ${PATH}/pip3
PYTHON3 :=  ${PATH}/python3
TESTS :=  ${PATH}/pytest -v ./test_controllers.py
clear:
	rm -rf venv

venv:
	python3 -m venv venv

install_requirements:
	${PIP} install -r requirements.txt

run:
	${PYTHON3} server.py
test:
	${TESTS}
