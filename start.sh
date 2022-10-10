#!/bin/bash
screen sudo waitress-serve --host 0.0.0.0 --port=105 main:app
