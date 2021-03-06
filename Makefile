MODULE := kafka_cli
BLUE='\033[0;34m'
NC='\033[0m' # No Color

run:
	@python -m $(MODULE)	

test:
	@pytest

lint:
	@echo "\n${BLUE}Running Pylint against source and test files...${NC}\n"
	@pylint --rcfile=setup.cfg **/*.pys
	@echo "\n${BLUE}Running Flake8 against source and test files...${NC}\n"
	@flake8
	@echo "\n${BLUE}Running Bandit against source files...${NC}\n"
	@bandit -r --ini setup.cfg

clean:
	rm -rf ./kafka_cli/__pycache__/*.pyc
	rm -rf ./kafka_cli/Kafka/__pycache__/
	rm -rf ./tests/__pycache__/
	rm -rf .pytest_cache .coverage .pytest_cache coverage.xml
	rm -rf ./dist
	rm -rf ./build
	rm -rf ./*egg-info

.PHONY: clean test

install:
	@python setup.py install

build:
	@python setup.py sdist bdist_wheel

