all: 
	python3 main.py

run:
	python3 main.py
	cat outFile

run2:
	python3 main.py 0 inFile2
	cat outFile	

git:
	make clean
	git status
	git add -A
	git commit -m "added preliminary logic functionality"
	git push

open:
	subl main.py
	subl Scheduler.py
	subl node.py
	subl setup.py
	subl README.md

clean:
	rm -rf __pycache__
	rm -f outFile
