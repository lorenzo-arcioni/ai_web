#!/bin/bash

content="Algoritmi"

echo "Updating content:" $content

rm -rf ./content/$content
cp -r ../my-obsidian-vault/00_Informatica/$content ./content/$content

echo "Done"

./update_tikz.sh