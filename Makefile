.PHONY: deploy
deploy: build
	twine upload dist/*

.PHONY: test-deploy
test-deploy: build
	twine upload --repository testpypi dist/*

.PHONY: build
build:
	rm -rf dist build django_jp_birthday.egg-info
	make test
	python setup.py sdist bdist_wheel

.PHONY: delete
delete:
	rm -rf dist build django_jp_birthday.egg-info

.PHONY: test
test:
	python setup.py test
