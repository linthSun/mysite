@echo off

set targe=''
set url= -i https://pypi.tuna.tsinghua.edu.cn/simple
set act=pip install 
setlocal enabledelayedexpansion
for /f   %%i in (requirements.txt)  do (
set target=%act%%%i%url%
%act%%%i%url%
) 

pause