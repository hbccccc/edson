# -*- coding utf-8 -*-
import  os
import sys
from typing import Dict, Union
import shutil
from warnings import simplefilter


class dir_gen(object):

    def __init__(self,path:str,dir_dict:Dict[str,list],name:str):
        self._path = path
        self._dir = dir_dict
        #self._base_path = base_path
        self._name = name


    def _dir_gen(self):
        current_path = os.path.join(self._path,self._name)
        #result is a string : "path/name"

        os.mkdir(current_path,mode=0o755)
        for key in self._dir.keys():
            if len(self._dir.get(key))==1:
                sub_path = os.path.join(current_path,self._dir.get(key).pop())
                os.mkdir(sub_path,mode=0o755)
            else:
                sub_path = os.path.join(current_path,key)
                os.mkdir(sub_path,mode=0o755)
                for member in self._dir.get(key):
                    sub_sub_path = os.path.join(sub_path,member)
                    os.mkdir(sub_sub_path,mode=0o755)

        shutil.copyfile('/home/edson/source_file/Makefile',os.path.join(current_path,'vcs/Makefile')  )
        shutil.copyfile('/home/edson/source_file/tb_top.sv',os.path.join(current_path,'sim/tb_dir/tb_top.sv')  )

#    def source_file_cp(self):
#        for key in self._source_file.keys():
#            if isinstance(self._source_file.get(key),str):
#                source_file_path = self._source_file.get(key).pop()
#                current_path = os.path.join(self._path,self._name)
#                dst_path = os.path.join(current_path,key)
#                shutil.copyfile(source_file_path,dst_path)
#            elif isinstance(self._source_file.get(key), dict):
#                for sub_key in self._source_file.get(key):
#                  if isinstance(self._source_file.get(key).get(sub_key),str):
#                      source_file_path = self._source_file.get(key).get(sub_key).pop()
#



# file tree:
# farther_dir :
#    --------dc
#    --------fpga
#    --------rtl
#                ---common_module
#                ---glb_define
#    --------sim
#                ---tb_dir
#                        ---tb_top.sv
#                ---class_dir
#                ---sim_def_dir
#    --------vcs
#                ---Makefile

def ic_dir_gen(path:str,name:str):
    dir_dict = {
            "dc"    : ["dc"],
            "fpga"  : ["fpga"],
            "rtl"   : ['common_module','glb_def' ],
            'sim'   : ["class_dir" ,'sim_def_dir', 'tb_dir'],
            "vcs"   : ["vcs"]
    }

    dir_gen_test = dir_gen(path,dir_dict,name)
    dir_gen_test._dir_gen()

if __name__ == "__main__":
    current_path= sys.argv[1]
    dir_name = sys.argv[2]
    ic_dir_gen(current_path,dir_name)