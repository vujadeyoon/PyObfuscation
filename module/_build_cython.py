import os
import numpy as np
from distutils.core import setup
from Cython.Build import cythonize
from vujade import vujade_path as path_
from vujade import vujade_str as str_
from vujade import vujade_utils as utils_
from vujade.vujade_debug import printd, pprintd


if __name__ == '__main__':
    is_move_py = str_.str2bool(_v=utils_.get_env_var(_name_var='IS_MOVE_PY', _default='', _is_raise_existed=True))
    path_dir_py_ori = path_.Path(os.path.join(os.getcwd(), '_code_python3'), _is_absolute=True)
    path_dir_root = path_.Path(utils_.get_env_var(_name_var='PATH_DIR_PROJECT_ROOT', _default='', _is_raise_existed=True), _is_absolute=True)
    list_spath_py_pyx = path_dir_root.rglob(_patterns=('*.py', '*.pyx'))

    for _idx, _spath_py_pyx in enumerate(list_spath_py_pyx):
        path_py_pyx = path_.Path(_spath_py_pyx, _is_absolute=True)
        str_command = "setup(name='{}', ext_modules=cythonize('{}'), include_dirs=[np.get_include()])".format(path_py_pyx.name, path_py_pyx.str)
        exec(str_command)
        path_py_pyx.replace_ext(_new='.c').unlink(_missing_ok=True)

        list_spath_so = path_.Path(os.getcwd()).glob(_patterns=('{}.cpython-*.so'.format(path_py_pyx.name), ))

        if len(list_spath_so) == 1:
            is_success_build_cython = True
        else:
            is_success_build_cython = False
            raise ValueError('The number of built so files should be 1.')

        for _idy, _spath_so in enumerate(list_spath_so):
            path_so = path_.Path(_spath_so, _is_absolute=True)
            path_so.move(_spath_dir_dst=path_py_pyx.parent.str)

        if (is_move_py is True) and (is_success_build_cython is True):
            path_dir_py_dst = path_.Path(os.path.join(os.getcwd(), path_py_pyx.parent.str.replace(path_dir_root.parent.str, './{}'.format(path_dir_py_ori.name))), _is_absolute=True)
            path_dir_py_dst.path.mkdir(mode=0o775, parents=True, exist_ok=True)
            path_py_pyx.move(_spath_dir_dst=path_dir_py_dst.str)

    path_.Path(os.path.join(os.getcwd(), 'build')).rmtree(_ignore_errors=False, _onerror=None)
