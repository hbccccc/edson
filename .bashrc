# .bashrc

# Source global definitions
if [ -f /etc/bashrc ]; then
	. /etc/bashrc
fi


#配置VCS的路径
export VCS_HOME=/home/synopsys/vcs/vcs_mx_vO-2018.09-SP2/vcs-mx/O-2018.09-SP2
export VERDI_HOME=/home/synopsys/verdi/verdi_2018_9/verdi/Verdi_O-2018.09-SP2


#VCS
PATH=$PATH:$VCS_HOME/bin
alias vcs="vcs"

#VERDI
PATH=$PATH:$VERDI_HOME/bin
alias verdi="verdi"

#LICENCE
export LM_LICENSE_FILE=27000@localhost.localdomain
alias LICENSE_START="/home/synopsys/linux64/bin/lmgrd  -c /home/synopsys/scl/2018.06/admin/license/Synopsys.dat"



alias pycharm='/home/edson/Downloads/pycharm-community-2024.2.0.1/bin/pycharm'

dir_gen(){
	current_path="$PWD"
	python3 /home/edson/PycharmProjects/pythonProject1/ic/dir_gen.py "$PWD" "$1"
} 



#alias pycharm='./Downloads/pycharm-community-2024.2.0.1/bin/pycharm.sh'
# Uncomment the following line if you don't like systemctl's auto-paging feature:
# export SYSTEMD_PAGER=

# User specific aliases and functions
