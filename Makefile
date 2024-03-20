install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt &&\
        python -m textblob.download_corpora

test:
	python -m pytest -vv RumbleTest/test_*.py

format:	
	black *.py RumbleLib/*.py

lint:
	pylint --disable=R,C --extension-pkg-whitelist='pydantic' rumble.py --ignore-patterns=test_.*?py *.py  RumbleLib/*.py

container-lint:
	docker run --rm -i hadolint/hadolint < Dockerfile

refactor: format lint

deploy:
	aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 561744971673.dkr.ecr.us-east-1.amazonaws.com
	docker build -t logistics .
	docker tag logistics:latest 561744971673.dkr.ecr.us-east-1.amazonaws.com/logistics:latest
	docker push 561744971673.dkr.ecr.us-east-1.amazonaws.com/logistics:latest
		
		
all: install lint test format
