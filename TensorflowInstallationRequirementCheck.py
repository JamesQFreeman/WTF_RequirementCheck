#/usr/bin/python3
'''this a check for the Tensorflow installation'''
import os
''' Input the supporting version of the following requirement below
'''
VC_RUNTIME_VERSION = ['msvcp140.dll']
CUDA_VERSION = ['80']
CUDNN_VERSION = ['5']
PYTHON_VERSION = [(3, 5)]


SYSTEM_PATH_LIST = []
def check_python_version():
    '''This function chech whether the python version in conformity with
    the TensorFlow's requirement
    It return True if version is right and vise versa
    '''
    import sys
    current_python_version = (sys.version_info.major, sys.version_info.minor)
    if any(x == current_python_version for x in PYTHON_VERSION):
        return True
    else:
        _version_error_handler('Python', PYTHON_VERSION, current_python_version)
        return False

def check_windows():
    '''This function check whether we are running the windows
    '''
    if os.name == 'nt':
        return True
    else:
        _missing_error_handler('Windows', ['7', '8', '10'])
        return False

def check_c_runtime():
    '''This function check whether we have the right version of c runtime
    '''
    if any(map(_check_file_existense_in_path, VC_RUNTIME_VERSION)):
        return True
    else:
        _version_error_handler('C Runtime', VC_RUNTIME_VERSION, [])
        return False


def check_gpu():
    '''This function I didnt know how to do with it
    '''
    return True

def check_cuda_version():
    '''This function use the cusparse dll to check whether the cuda is successfully installed
    '''
    check_list = ['cusparse64_'+ x+ '.dll' for x in CUDA_VERSION]
    if any(map(_check_file_existense_in_path, check_list)):
        return True
    else:
        _version_error_handler('CUDA', CUDA_VERSION, [])
        return False


def check_cudnn():
    '''This function use the cudnn dll to check whether the cudnn is successfully installed
    '''
    check_list = ['cudnn64_'+ x+ '.dll' for x in CUDNN_VERSION]
    if any(map(_check_file_existense_in_path, check_list)):
        return True
    else:
        _version_error_handler('CUDNN', CUDNN_VERSION, [])
        return False

def check_scipy():
    '''This function import the scipy to check whether scipy is installed
    '''
    try:
        import scipy
        return True
    except ImportError:
        _missing_error_handler('SciPy', '')
        return False

def check_mkl():
    '''This function is unfinished
    '''
    if _check_file_existense_in_path('\\Lib\\site-packages\\numpy\\core\\mkl_core.dll'):
        return True
    else:
        _missing_error_handler('mkl', [])

def get_system_path():
    '''This function returns a system PATH in list form
    '''
    global SYSTEM_PATH_LIST
    if not SYSTEM_PATH_LIST:
        SYSTEM_PATH_LIST = os.environ['PATH'].split(";")
        return SYSTEM_PATH_LIST
    else:
        return SYSTEM_PATH_LIST

def _version_error_handler(things_lacking, valid_version, current_version):
    ''' A universal handler for sth wrong
    '''
    if not current_version:
        _missing_error_handler(things_lacking, valid_version)
    else:
        print(things_lacking+" version is not compatible for current TensorFlow")
        print("These "+ things_lacking+ " version below are compatible: ")
        print(valid_version)
        print("Your "+ things_lacking+ " version is: ")
        print(current_version)
        print('\n')

def _missing_error_handler(things_lacking, valid_version):
    ''' A universal handler for sth missing
    '''
    print(things_lacking+" is not installed")
    if valid_version:
        print("These "+ things_lacking+ " version below are compatible: ")
        print(valid_version)
    print('\n')

def _check_file_existense_in_path(filename):
    '''This function receives a filename and check its existence in the System Path
    return True and False
    '''
    path_list = get_system_path()
    check_list = [x+'\\'+filename for x in path_list]
    #print(check_list)
    return any(map(os.path.exists, check_list))
'''
def test_function():
    print(_check_file_existense_in_path('cusparse64_80.dll'))
    print(check_windows())
    print(check_python_version())
    '''

if __name__ == '__main__':
    '''The main function of the script, there several steps below:
    1. Check if we are in windows?
    2. Check the C Runtime
    3. Check Cuda
    4. Check CuDnn
    5. Check MKL
    6. Check Python version
    todo: 7. Check GPU CUDA Compute Capability 3.0 or higher.
    8. Check scipy
    '''
    #test_function()
    if all([check_windows(),
            check_c_runtime(),
            check_cuda_version(),
            check_gpu(),
            check_cudnn(),
            check_mkl(),
            check_python_version(),
            check_scipy()
           ]):
        print("Congradulation! You are ready for the TensorFlow installation")

