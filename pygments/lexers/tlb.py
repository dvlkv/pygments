"""
    pygments.lexers.tlb
    ~~~~~~~~~~~~~~~~~~~

    Lexers for TL-b.

    :copyright: Copyright 2006-2022 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

from pygments.lexer import RegexLexer, include, words
from pygments.token import Operator, Name, \
    Number, Whitespace, Punctuation, Comment

__all__ = ['TlbLexer']


class TlbLexer(RegexLexer):
    """
    For TL-b source code.
    """

    name = 'Tl-b'
    aliases = ['tlb']
    filenames = ['*.tlb']

    tokens = {
        'root': [
            (r'\s+', Whitespace),

            include('comments'),

            (r'[0-9]+', Number),
            (words((
                '+', '-', '*', '=', '?', '~', '.',
                '^', '==', '<', '>', '<=', '>=', '!='
            )), Operator),
            (r'#[0-9a-f]*_?', Name.Tag),
            (r'\$[01]*_?', Name.Tag),
            (words(('##', '#<', '#<=', '#')), Name.Tag),

            (r'[a-zA-Z_][0-9a-zA-Z_]*', Name),

            (r'[;():\[\]{}]', Punctuation)
        ],

        'comments': [
            (r'//.*', Comment.Singleline),
            (r'/\*', Comment.Multiline, 'comment'),
        ],
        'comment': [
            (r'[^/*]+', Comment.Multiline),
            (r'/\*', Comment.Multiline, '#push'),
            (r'\*/', Comment.Multiline, '#pop'),
            (r'[*/]', Comment.Multiline),
        ],
    }
