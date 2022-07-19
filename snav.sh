#!/bin/bash
selection="m/"
list=$( python3 main.py --passsel $selection )
selection=$( echo "$list" | fzf )
list=$( python3 main.py --passsel $selection )
selection=$( echo "$list" | fzf )

echo $list
echo $selection


