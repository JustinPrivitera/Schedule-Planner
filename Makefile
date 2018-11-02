all: 
	python3 main.py
	cat outFile

clean:
	rm -rf __pycache__
	rm -f outFile
