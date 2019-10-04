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

def implode(glue,pieces):
    return glue.join(pieces)

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


def str_replace(string, value, new_value, occurences = -1):
    """
    Replaces the value of `value` to `new_value` in `string`. 
    If occurences is defined, will only replace the first n occurences. A negative value replaces all values. 
    """

    return string.replace(value, new_value, occurences)

def trim(string, trim_chars = None):
    """
    Strips all whitespace characters from the beginning and end of the `string`. If `trim_chars` is set, instead of whitespace, will replace only those characters. 
    """
    return string.strip(trim_chars)

def strpos(string, search_val, offset = 0):
    """
    Returns the position of `search_val` in `string`, or False if it doesn't exist. If `offset` is defined, will start looking if `search_val` exists after the `offset`. 
    """
    try:
        return string[offset:].index(search_val) + offset
    except ValueError: 
        return False

def strstr(string, search_val):
    """
    Searches string for `search_val` and if found, returns all characters from there onwards. Returns false if `search_val` is not found. 
    """
    str_index = strpos(string, search_val)
    if not str_index: return False
    return string[str_index:]

def is_string(val):
    return type(val) == str

def is_array(val):
    return type(val) == list

def in_array(l, val):
    return l in val

def array_unique(l):
    """
    Removes all duplicates from `l`. 
    """
    return list(set(l))

def array_search(l, val):
    """
    Returns the index of `val` in `l`. 
    """
    try:
        return l.index(val)
    except ValueError:
        return False

def array_reverse(l):
    """
    Reverses an array. PHP's array_reverse() allows you to preserve the old keys, but that doesn't work in python. 
    """
    return list(reversed(l))

def array_map(func, l):
    return list(map(func, l))

def array_diff(l, *other_arrays):
    """
    Removes all elements from `l` that are present in at least one of the arrays in `other_arrays`. 
    """
    for a in other_arrays: 
        l = [x for x in l if x not in a]
    return l
