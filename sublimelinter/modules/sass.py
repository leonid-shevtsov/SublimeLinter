# -*- coding: utf-8 -*-
# sass.py - sublimelint package for checking Sass and SCSS files

import re
import os.path

from base_linter import BaseLinter

CONFIG = {
    'language': 'Sass',
    'executable': 'sass',
}


class Linter(BaseLinter):
    def __init__(self, config):
        super(Linter, self).__init__(config)

    def get_lint_args(self, view, code, filename):
        args = ['--no-cache', '--check']

        _, ext = os.path.splitext(filename.lower())
        if ext == '.scss':
            args.append('--scss')

        return args

    def parse_errors(self, view, errors, lines, errorUnderlines, violationUnderlines, warningUnderlines, errorMessages, violationMessages, warningMessages):
        matches = re.findall(r'^Syntax error: (.*)$\s+on line (\d+) of (.*)$', errors, re.MULTILINE)
        for match in matches:
            if match[2] == 'standard input':
                self.add_message(int(match[1]), lines, match[0], errorMessages)
