all: 
	python3 main.py

run:
	python3 main.py
	cat outFile

git:
	make clean
	git status
	git add -A
	git commit -m "made changes"
	git push

clean:
	rm -rf __pycache__
	rm -f outFile
