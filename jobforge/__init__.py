# -*- coding: utf-8 -*-
"""求职工作台 · 领域 / 应用 / 适配器 / 持久化 / 运行时 / Web

包入口在这里补上项目根的 sys.path。
原因：`python -m jobforge.web.app` 时，Python 先导入 ``jobforge`` 这个包，
而此时模块里的代码还没执行 —— 如果当前工作目录不在 sys.path 上，
连包本身都找不到，报 ``No module named 'jobforge'``。
在这个包里补 sys.path 早于任何子模块被加载，问题在源头解决。
"""
from __future__ import annotations

import sys
from pathlib import Path

_PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))


def app_data_dir() -> Path:
    """应用数据目录（可写）。

    源码运行时在项目根的 ``data/``；PyInstaller 打包后（``sys.frozen``）在
    exe 旁的 ``data/`` —— ``_MEIPASS`` 是只读临时目录，把简历、数据库、
    API Key 写进去重启就丢，所以打包后必须落到 exe 旁的可写位置。
    """
    if getattr(sys, "frozen", False):
        return Path(sys.executable).resolve().parent / "data"
    return _PROJECT_ROOT / "data"
