#!/bin/bash/python
import sys
# --config file path to config

indent = 0

l = {'testbb' : {'cc': 1, 'bb': 2}, 'test': {'hey' : 0, 'hi' : {'my' : 2, 'name' : 2}}, 'weee' : 'hhooooo', 'wow' : {'thats' : 1, 'really' : 2, 'cool' : 3}}
def get_tag_list():
    def seperation(indent):
        tmp = ''
        for i in range(indent):
            chr = ''
            if i == 0:
                chr = '│'
            if i > 0:
                chr = ' ' 
            if i == indent-1:
                chr = '│'
            tmp += chr
        return tmp
    def get_dict(d, indent):
        if isinstance(d,dict):
            x = 0
            for k,i in d.items():
                tmp = ''
                x += 1
                if x == 1:
                    tmp = '{}┐{} * '
                if x > 1:
                    tmp = '{}├{} * '
                if x == len(d):
                    tmp = '{}┘{} * '

                if isinstance(i,dict):
                    if x == 1:
                        print('{}├┐{} * '.format(seperation(indent),k))
                    if x > 1:
                        print('{}├┐{} *'.format(seperation(indent),k))
                    

                    indent += 1 
                    get_dict(i, indent)
                    indent -= 1 
                    print('{}├┘'.format(seperation(indent)))
                else:
                    print('{}├{}'.format(seperation(indent),k))
    get_dict(l,indent)
get_tag_list()
                    

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
                if len(sel) == 2 and sel[index+1] == '':
                    print(s) 
                continue
            if sel[index] != '':
                if isinstance(di.get(sel[index]), dict):
                    di = di.get(sel[index])
                    sd = ''
                    for key in di.keys():
                        sd += raw_data + '/' + key + '\n'
                    if index + 1 >= len(sel):
                        print(sd) 
                else:
                    print(di.get(sel[index]))
                    break

    else:
        print(type(selection))
        print('Error (2): run_selection : selection is not STRING')
    pass

def nav_tree(section):
    if(section == 'commands'):
        pass
    if(section == 'projects'):
        pass
    if(section == 'common'):
        pass
    if(section == 'all'):
        pass
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
        elif args[arg] == '--tree':
            if arg+1 >= len(args):
                print('Error (3): not enough args')
                break
            nav_tree(arg+1)
            continue

main()
