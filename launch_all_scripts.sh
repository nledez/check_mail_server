#!/bin/bash
./venv/bin/python main.py
for diag in diag_*.py; do
	echo '********************************************************************************'
	./venv/bin/python ${diag}
	echo '--------------------------------------------------------------------------------'
done
