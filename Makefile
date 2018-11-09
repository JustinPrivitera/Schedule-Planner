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
	git commit -m "committed with make git"
	git push

gitl:
	make clean
	git status
	git add -A
	git commit -m "made changes to logic functionality"
	git push

open:
	subl main.py
	subl Scheduler.py
	subl node.py
	subl setup.py
	subl README.md
	subl logic.py

clean:
	rm -rf __pycache__
	rm -f outFile
