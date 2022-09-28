import subprocess

command = 'cmatrix'
subprocess.Popen(["/bin/bash cmatrix"], stderr=subprocess.STDOUT, stdout=subprocess.PIPE)