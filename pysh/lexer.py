#!/usr/bin/python3
## Copyright 2015 Kevin Boxhoorn
##
## Licensed under the Apache License, Version 2.0 (the "License");
## you may not use this file except in compliance with the License.
## You may obtain a copy of the License at
##
##   http://www.apache.org/licenses/LICENSE-2.0
##
## Unless required by applicable law or agreed to in writing, software
## distributed under the License is distributed on an "AS IS" BASIS,
## WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
## See the License for the specific language governing permissions and
## limitations under the License.
##
## lexer.py
##
## Tokenizing of PySH commands.

import ply.lex as lex
import os

tokens = (
    "COMMENT",
    "HISTCMD",
    "OPTIONS",
    "PATH",
    "TEXT",
    "VARIABLE"
)

t_HISTCMD = r"\!(?:\!|-|\d+)"
t_OPTIONS = r"-\w+"
t_TEXT = r"\w+"

def t_PATH(t):
    r"(?:\.{1,2}|\~)(?:\/?(?:\S|\.)+)*"
    if t.value.startswith("~"):
        t.value = t.value.replace("~", os.environ["HOME"], 1)
    return t
def t_VARIABLE(t):
    r"\$\w+"
    t.value = os.environ[t.value[1:]]
    return t

def t_error(t):
    print("error: cannot parse character \"{0}\"".format(t.value[0]))
    t.lexer.skip(1)

t_ignore = " \t"
t_ignore_COMMENT = r"\#.*"

lexer = lex.lex()
