#!/usr/bin/env python3
# coding=utf-8
'''
Author: Cosmade
Date: 2024-04-09 15:55:33
LastEditors: deepskystar deepskystar@outlook.com
LastEditTime: 2024-05-14 17:53:21
FilePath: /hikit/hi_setup.py
Description: 

Copyright 2024 Cosmade

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
'''

import os
from hi_basic import *
from hi_installer import *


if __name__ == "__main__":
    # Auto setup the hikit remote.
    install_basic()
    git = HiGit.from_local()
    HiPath.setup_hikitsource(git.remote)
    curdir = os.path.dirname(os.path.abspath(__file__))
    HiInstaller(HiAppInfo.from_local(path=curdir)).install()
    HiSys.setup_path()
    pass
