#import ply tool
import ply.lex as lex


#List of token names
tokens=(
   #OPERATORS#
   'PLUS',      #+
   'MULTIPLY',  #*
   'EQUALS',    #=
   'SEMICOLON'  #;

   #COMPARATORS#
   'GT',        #>

   #CONDITIONS#
   'IF',        #if
   'ELSE',      #else

   #BRACKETS#
   'LPAREN',     #(
   'RPAREN',     #)
   'BLOCKSTART', #{
   'BLOCKEND',   #}

   'PRINT',      #print
   'ID',         #x,y 

   'NUMBER',      #2,3,5 

   #DATA TYPES#
   'INTEGER',     #int

)

#regular expression for more complex tokens 
def t_INTEGER(T):
    r'\d+'
    t.value = int(t.value)
    return t 

def t_newline(t):
    r'|n+'
    t.lexer.lineno+=let(t.value)

def t_error(t):
    print("Illegal character '%s"% t.value[0])
    t.lexer.skip(1)


#Regular expression 
t_PLUS = r'\+'
t_MULTIPLY = r'\*'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_BLOCKSTART = r'\{'
t_BLOCKEND = r'\}'
t_EQUALS = r'\='
t_GT = r'\>'
t_SEMICOLON = r'\;'
t_ignore = '\t' #ignore spaces ant tabs 


reserved = {
'if':'IF',
'else': 'ELSE',
'print': 'PRINT',
'id': 'ID',
        
    }

lexer=lex.lex()
data=[3+5]

lexer.input(data)
for tok in lexer:
    print(tok)