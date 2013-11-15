venv: venv/bin/activate 
venv/bin/activate: requirements.txt
	test -d venv || virtualenv venv
	. venv/bin/activate; pip install -r requirements.txt
	touch venv/bin/activate

debug: venv
	. venv/bin/activate; python run_server.py

clean:
	rm -rf venv
