#!/bin/bash
watchmedo shell-command --recursive --ignore-directories --patterns="*.less" --wait --command='fab lessc' .
