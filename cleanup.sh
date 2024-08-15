#!/usr/bin/env bash

git checkout --orphan cleanup
git add -A
git commit -am "$1"
git branch -D master
git branch -m master
git push -f origin master
