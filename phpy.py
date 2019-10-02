#Extend#############################################################
def pip(command,value):
    try:
        import subprocess
        subprocess.run('pip %s %s'%(command,value))
    except:
        raise RuntimeError ("Failed To Load subprocess library")

#Converted##########################################################
def isset(varName):
    keys = globals().keys()
    for key in keys:
        if str(varName) == key:return True
    return False

def is_dir(dir):
    try:
        from os import scandir as sd
    except:
        print("")        
    try:
        sd(str(dir)).__next__()
        return True
    except:
        return False

def file_exists(path):
    try:
        open(str(path))
        return True
    except:
        return False

def date(format):
    try:
        from time import strftime,gmtime
    except:
        print()
    try:
        return strftime(str(format),gmtime())
    except:
        print()
        
def time():
    try:
        from time import time
    except:
        print()
    return time()

def explode(delimiter,string):
    return str(string).split(delimiter)

def strtolower(string):
    return lower(string)

def strtoupper(string):
    return upper(string)

def strval(value):
    return str(value)

def intval(string):
    integer = ''
    for ch in str(string):
        if(ch in ['0','1','2','4','5','6','7','8','9']):
            integer += ch
    return int(integer)

def stripos(string, keyword):
    return str(string).find(keyword)

def die(string):
    raise Warning (string)
    
def count(var):
    return len(var)

def file_get_contents(fileName):
    try:
        return open(fileName,'r').read()
    except:
        raise FileNotFoundError ("File Not Found")
    
def file_put_contents(fileName,Data):
    try:
        open(fileName,'w').write(Data)
    except:
        raise Exception ("Failed To Save File")

def empty(var):
    if type(var) is int and var not in ['',None]:
        return False
    if type(var) is str and var not in ['',None]:
        return False
    if type(var) in [list,tuple,dict] and var not in [{},(),[],'',None]:
        return False
    if var not in [[],[[]],{},(),'',None]:
        return False
    return True

def echo(val):
    print(val)

def print_r(val):
    print(val)

def var_dump(array):
    print(array)

def json_encode(array):
    try:
        import json
    except:
        print()
    try:
        return json.dumps(array)
    except:
        raise ValueError ("Failed To Encode Json")
    
def json_decode(jsonEn):
    try:
        import json
    except:
        print()
    try:
        return json.loads(jsonEn)
    except:
        raise ValueError ("Failed To Decode Json")

def base64encode(string):
    try:
        import base64
    except:
        print()
    return base64.b64encode('base64')

def base64decode(base64):
    try:
        import base64
    except:
        print()
    return base64.b64decode('base64')

def read(file):
    try:
        return open(fileName,'r').read()
    except:
        raise FileNotFoundError ("File Not Found")

def scandir(dir):
    try:
        import os
    except:
        print()
    a = os.scandir(dir)
    list = []
    while(True):
        try:
            b = str(a.__next__()).split("'")[1]
            if (b == ''):break
            list.append(b)
        except:
            break
    return list

def substr(string,start,end=''):
    string = str(string)
    if(end == ''):
        return string[int(start):]
    else:
        return string[int(start):int(end)]

def unlink(path):
    try:
        import os
    except:
        print()
    try:
        os.remove(path)
        return True
    except:
        return False

def urlencode(url):
    try:
        import urllib
    except:
        print()
    return urllib.parse.quote(url)

def urldecode(enurl):
    try:
        import urllib
    except:
        print()
    return urllib.parse.unquote(enurl)


def bin2hex(text):
    return ''.join(hex(ord(c)) for c in text).replace('0x','')

def decbin(num):
    """
    Converts a decimal number(num) to binary
    
    Parameters
    ----------
    num : int or string

    Returns
    -------
    integer denoting value of decimal number in binary format.
    """
    try:
        return bin(int(num))[2:]
    except:
        raise ValueError("Expected a Number as input")

def decoct():
    """
    Converts a decimal number(num) to octal i.e. base 8.
    
    Parameters
    ----------
    num : int or string

    Returns
    -------
    integer denoting value of decimal number in octal format.
    """
    try:
        return oct(int(num))[2:]
    except:
        raise ValueError("Expected a Number as input")

def dechex(num):
    """
    Converts a decimal number(num) to hexadecimal ie base 16
    
    Parameters
    ----------
    num : int or string

    Returns
    -------
    integer denoting value of decimal number in hex format.
    """
    try:
        # returning upper because php does that.
        return hex(int(num))[2:].upper()
    except:
        raise ValueError("Expected a Number as input")


