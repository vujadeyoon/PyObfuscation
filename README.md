# PyObfuscation


## Table of contents
1. [Notice](#notice)
2. [Required python3 packages](#required_python3_packages)
3. [How to obfuscate python3 scripts and run the encrypted python3 codes](#how_to_obfuscate_run)
4. [License](#license)
5. [Reference](#ref)


## 1. Notice <a name="notice"></a>
- I recommend that you should ignore the commented instructions with an octothorpe, #.


## 2. Required python3 packages <a name="required_python3_packages"></a>
- pyconcrete==0.15.1
- Cython==0.29.24
- vujade==0.6.9.4



## 3. How to obfuscate python3 scripts and run the encrypted python3 codes <a name="how_to_obfuscate_run"></a>
### 1. Pyconcrete
```bash
# Obfuscation
$ path_dir_project_root="./project"
$ bash ./script/bash_build_pyconcrete.sh ${path_dir_project_root}
$ pyconcrete-admin.py compile --source=./main_test.py --pye
# Run
$ pyconcrete ./main_test.pye
```

### 2. Cython
```bash
# Obfuscation
$ path_dir_project_root="./project"
$ is_move_py="true"
$ bash ./script/bash_build_cython.sh ${path_dir_project_root} ${is_move_py}
# Run
$ python3 ./main_test.py
```


## 4. License <a name="license"></a>
- I respect and follow the license of the used libraries including python3 packages.
- The libraries including python3 packages are licensed by their licenses.


## 5. Reference <a name="ref"></a>
1. [Cython](https://cython.org)
2. [Pyconcrete](https://github.com/Falldog/pyconcrete)
3. [vujade-python](https://github.com/vujadeyoon/vujade-python)
4. [vujadeyoon/Pyconcrete-Python](https://github.com/vujadeyoon/Pyconcrete-Python)
5. [Pyarmor](https://pyarmor.dashingsoft.com)
6. [Anubis](https://github.com/0sir1ss/Anubis)
7. [python-minifier](https://github.com/dflook/python-minifier)
8. [Verimatrix::Code obfuscation](https://www.verimatrix.com/cybersecurity/code-obfuscation/?utm_term=python%20obfuscation&utm_campaign=Asia+-+Shielding+-+EN&utm_source=adwords&utm_medium=ppc&hsa_acc=5556708784&hsa_cam=9582165481&hsa_grp=111606949657&hsa_ad=660594057748&hsa_src=g&hsa_tgt=kwd-454811935369&hsa_kw=python%20obfuscation&hsa_mt=e&hsa_net=adwords&hsa_ver=3&gclid=EAIaIQobChMI66W2t56igQMVyxF7Bx3n5wKxEAAYASAAEgKllvD_BwE)
