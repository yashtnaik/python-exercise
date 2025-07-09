import re, os, sys

logfile=input('Enter the log file name in which you would like to look for the error:   ')
err=input('Enter the error string to look for:   ')

cwd=os.getcwd()
logpath=os.path.join(cwd, logfile)

try:
    with open(logpath,'r') as f:
        data_read=f.read()
except Exception as e:
    print(f'Error occured while reading the {logfile}, Error:{e}')
    sys.exit(1)

pattern=re.compile(fr'{err}')
err_regx=pattern.findall(data_read)

print(f'{len(err_regx)} Matches found for the error:{err}')