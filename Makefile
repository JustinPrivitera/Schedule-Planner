all: 
	python3 main.py

run:
	python3 main.py
	cat outFile

git:
	make clean
	git status
	git add -A
	git commit -m "committed with make git"
	git push

view:
	subl main.py
	subl Scheduler.py
	subl node.py
	subl setup.py

clean:
	rm -rf __pycache__
	rm -f outFile
