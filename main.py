#!/bin/bash/python
import sys

# --config file path to config

l = {'testbb' : {'cc': 1, 'bb': 2}, 'test': {'hey' : 0, 'hi' : 1}}
def run_fzf(data):
    s = ''
    for i in l:
       s += i + ' ' 
    return s

def run_selection(selection):
    if type(selection) is str:
        raw_data = selection

        sel = selection.split('/')
        di = l

        for index in range(len(sel)):
            if len(sel) == 2 and sel[index] == 'm':
                di = l
                s = ''
                for key in di.keys():
                    s += raw_data + key + '\n'
                if len(sel) == 2 and sel[1] == '':
                    print(s) 
                continue
            if sel[index] != '':
                if isinstance(di.get(sel[index]), dict):
                    di = di.get(sel[index])
                    sd = ''
                    for key in di.keys():
                        sd += raw_data + '/' + key + '\n'
                    print(sd) 
                else:
                    print(di.get(sel[index]))
                    break

    else:
        print(type(selection))
        print('Error (2): run_selection : selection is not STRING')
    pass

def main():
    args = sys.argv

    for arg in range(len(args)):
        if args[arg] == '--getselopts':
            print(run_fzf(''))
            continue
        elif args[arg] == '--passsel':
            if arg+1 >= len(args):
                print('Error (1): not enough args')
                break
            run_selection(args[arg+1])
            continue

main()
