run:
	python3 -m venv .venv
	bash -c "source .venv/bin/activate"
	pip3 install -r requirements.txt
	clear
	streamlit run main.py


run-maps:
	python3 -m venv .venv
	bash -c "source .venv/bin/activate"
	pip3 install -r requirements.txt
	clear
	streamlit run 02_Maps.py