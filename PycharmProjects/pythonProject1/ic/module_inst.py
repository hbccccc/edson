import re
import sys



#def verilog_inst(verilog_code:str):
def verilog_inst(verilog_code): #used for python2
    pattern_direction = re.compile(r'(?:input)\b|(?:output)\b')
    pattern_width     = re.compile(r'(?=\[).*\]')
    #pattern_signal_no_end    = re.compile(r'(?<=ut)\s*\w+(?=\s*,)')
    pattern_signal_no_end = re.compile(r'(?<=put|.].|ire|reg|out)\s*\w+(?=\s*,)')
    #pattern_signal_end       = re.compile(r'\b\w*\b[^,]*(?=\))|\b\w*\b\s*$')
    pattern_signal_end = re.compile(r'(\b\w+\b\s*(?=[^,])(?=\)\s*?;))')
    pattern_module_name      = re.compile(r'(?<=module\s)\s*\b\w+\b')
    pattern_parameter_flg = re.compile(r'#')
    pattern_parameter_name   = re.compile(r'(?<=parameter\s)\s*\b\w+\b')
    pattern_parameter_val   = re.compile(r'(?<==)\s*.*\s*(?=[,)])')


    parameter_flg = re.findall(pattern_parameter_flg,verilog_code)
    parameter_value = re.findall(pattern_parameter_val,verilog_code)
    module_name = re.findall(pattern_module_name,verilog_code)
    parameter_list = re.findall(pattern_parameter_name,verilog_code)


    lines = verilog_code.splitlines()
    processed_lines = header_processed(module_name,parameter_list,parameter_value,parameter_flg)
    direct = []
    width = []
    signal_no_end = []
    signal_end = []

    for line in lines:
        direct = re.findall(pattern_direction,line)
        width  = re.findall(pattern_width,line)
        signal_no_end = re.findall(pattern_signal_no_end,line)
        signal_end = re.findall(pattern_signal_end,line)
        if(len(signal_end)):
            a =line_processed(direct,width,signal_end,True)
            processed_lines += a
        elif(len(signal_no_end)):
            a =line_processed(direct,width,signal_no_end,False)
            processed_lines += a
    return processed_lines



#def header_processed(module_name:list,parameters:list,parameter_val:list, parmeter_flg:list):
def header_processed(module_name, parameters, parameter_val, parmeter_flg):
    _module_name = str(module_name.pop()).strip()
    processed_lines = _module_name
    width_max = 15
    i = 0
    if len(parmeter_flg)==1:
        processed_lines += '''
#('''
    for parameter in parameters:
        default_value = str(parameter_val.pop(0))
        processed_lines += ('''
.''' + str(parameter).strip()+(width_max-len(str(parameter).strip()))*' ' +'( )' + '//default value : ' + default_value.strip())
        i+=1
        if len(parameters)==i:
            processed_lines += '''
)
'''
    processed_lines +="  " + 'inst_'+ _module_name + '(' +'''
'''
    return processed_lines



#def line_processed(direction:list,width:list,signal:list,end_flag:bool):
def line_processed(direction, width, signal, end_flag):
    blank_width1 = 20
    blank_width2 = 0
    dir_buffer = ''
    width_buffer =''
    signal_buffer=''
    if len(direction):
        dir_buffer = str(direction.pop()).strip()
    if len(width):
        width_buffer = str(width.pop()).strip()
    if len(signal):
        signal_buffer = str(signal.pop()).strip()
    signal_size = len(signal_buffer)
    blank_width1 = blank_width1-signal_size
    process_line = '.'+ signal_buffer+ blank_width1*' '+'('+blank_width2*' ' +'w_'+signal_buffer +blank_width1*' '+')'
    if not end_flag:
        process_line += f',// {str(dir_buffer).strip()} {str(width_buffer).strip()} \n'

    elif dir_buffer :
        process_line += f' // {str(dir_buffer).strip()} {str(width_buffer).strip()} \n);'

    return process_line



#multi_line_string = """module counter
#  #( 	parameter N = 2,
#   		parameter DOWN = 0)
#
#  ( input 							clk,
#    input 							rstn,
#    input 							en,
#   	output 	reg [N-1:0] out);
#
if __name__ == "__main__":
    input_txt = sys.stdin.read()

    output_txt = verilog_inst(input_txt)
    print(output_txt)


