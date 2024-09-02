"V0
set number

syntax on
set backspace=2
set tabstop=2
colorscheme desert
set guifont=Monospace\ 18


function Verilog_module_inst()
	"let l:selection = getreg('')
	"后面两行用于选择起止位置，利用符号'< 和'>来进行表示可视区域的起止位置，双引号则表示里面是字符串
	let l:start_pos = getpos("'<")
	let l:end_pos = getpos("'>")
"这李的start_pos后面跟了一个[1].这是因为getpos函数返回的其实是四个参数，1表选区开始的行，2表列，0表示缓冲区，3表示坐标
"因此下面两句的意思是，选中开始位置到结束位置的所有的行，再按\n为分隔符，将所有的元素拼接成一个字符串（这是因为getline返回的是
"列表，这点与python的内建函数相类似）
	let l:selection = getline(l:start_pos[1], l:end_pos[1])
	let l:selection_str = join(l:selection,"\n")

	"echo " TEST Selected text: " .string(l:selection_str)
"选择该.py文件所在的路径，前面产生的字符串作为参数传入 
	let l:txt_processed = system('python3 /home/edson/PycharmProjects/pythonProject1/ic/module_inst.py',l:selection_str)
	"echo "python data is " . string(txt_processed)

"execute用于动态执行一段Vimscript代码，其中.用于字符串的连接，假设两个行号分别是1和10，则执行以下功能
"将1和逗号和10与d拼接起来 等同于1,10d，其实就是vim命令模式下执行的删除操作
	execute l:start_pos[1] . "," . l:end_pos[1] . "d"

" 调用vim的内置函数append（），作用在插入新的行
" 从开始位置插入行，内容则是 python传回的字符串（已经按照换行符分割了）
	call append(l:start_pos[1]-1,split(l:txt_processed,"\n"))

	

endfunction 

vnoremap <leader>i :<C-u>call Verilog_module_inst()<CR>
