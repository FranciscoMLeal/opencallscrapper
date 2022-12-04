NAME = opencallscrapper

all: 
	python opencallscrapper.py 

clean:
	rm -f seenresults.txt
	rm -f pastresearch.txt
	touch seenresults.txt
	touch pastresearch.txt