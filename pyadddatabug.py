import os
from appdirs import user_data_dir

def main():
    appdirs_appdata = user_data_dir(appname='app name', appauthor='app author', version='1.0.1')
    print(f'appdirs appdata should be {appdirs_appdata}')
    example_dir = os.path.join(appdirs_appdata, 'example')
    os.makedirs(example_dir)
    # C:\Users\dolia\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\Local\app author\app name\1.0.1\example

if __name__ == '__main__':
    main()

