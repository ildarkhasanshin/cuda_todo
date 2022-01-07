import os
from cudatext import *

fn_config = os.path.join(app_path(APP_DIR_SETTINGS), 'cuda_todo.ini')

todo_vars = 'TODO,NOTE,NOTES,FIX,FIXME,IMPORTANT,CHANGED,HACK,TEST'

class Command:
    def __init__(self):
        global todo_vars
        todo_vars = ini_read(fn_config, 'options', 'todo_vars', str(todo_vars))
        todo_vars = todo_vars.split(',')
    
    def config(self):
        ini_write(fn_config, 'options', 'todo_vars', str(','.join(todo_vars)))
        file_open(fn_config)
        
    def run(self):
        ts = ed.get_text_all()
        ts_ = []
        i = 0
        for line_ in ts.split("\n"):
            for tv_ in todo_vars:
                if (line_.find(tv_) != -1):
                    ts_.append(i)
            i += 1
        for ts__ in ts_:
            ed.bookmark(BOOKMARK_SET, ts__)
    
    def clear(self):
        for bkm in ed.bookmark(BOOKMARK_GET_ALL, 0):
            line_ = ed.get_text_line(bkm['line'])
            for tv_ in todo_vars:
                if (line_.find(tv_) != -1):
                    ed.bookmark(BOOKMARK_CLEAR, bkm['line'])
