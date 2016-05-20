from enum import Enum

class Keyword(Enum):
    CLASS = 1
    METHOD = 2
    FUNCTION = 3
    CONSTRUCTOR = 4
    INT = 5
    BOOLEAN = 6
    CHAR = 7
    VOID = 8
    VAR = 9
    STATIC = 10
    FIELD = 11
    LET = 12
    DO = 13
    IF = 14
    ELSE = 15
    WHILE = 16
    RETURN = 17
    TRUE = 18
    FALSE = 19
    NULL = 20
    THIS = 21

class MyTokenizer:

    keyword_table = {
        "class"       : Keyword.CLASS,
        "method"      : Keyword.METHOD,
        "function"    : Keyword.FUNCTION,
        "constructor" : Keyword.CONSTRUCTOR,
        "field"       : Keyword.FIELD,
        "static"      : Keyword.STATIC,
        "var"         : Keyword.VAR,
        "int"         : Keyword.INT,
        "char"        : Keyword.CHAR,
        "boolean"     : Keyword.BOOLEAN,
        "void"        : Keyword.VOID,
        "true"        : Keyword.TRUE,
        "false"       : Keyword.FALSE,
        "null"        : Keyword.NULL,
        "this"        : Keyword.THIS,
        "let"         : Keyword.LET,
        "do"          : Keyword.DO,
        "if"          : Keyword.IF,
        "else"        : Keyword.ELSE,
        "while"       : Keyword.WHILE,
        "return"      : Keyword.RETURN
    }


    def __init__(self, source_text):
        self._source_text = source_text
        self._loc = 0




    def next_keyword(self):
        '''
        Return the next keyword found in the source_text
        :return: one of Keyword enumeration member
        '''
        self._loc += 1                                  ### MODIFY THIS ###
        if self._loc > 10:                              ### MODIFY THIS ###
            keyword = None                              ### MODIFY THIS ###
        else:                                           ### MODIFY THIS ###
            keyword =  self.keyword_table["function"]  ### MODIFY THIS ###

        return keyword


if __name__ == '__main__':

    source = input("Source Filename: ")
    source_file = open(source, "r")
    source_text = source_file.read()

    tokenizer = MyTokenizer(source_text)

    while True:

       keyword = tokenizer.next_keyword()

       if keyword == None: break

       print(keyword)
