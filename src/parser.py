from parsimonious.grammar import Grammar


grammar = Grammar(
    r"""
    code        = (entry / emptyline)*
    entry       = (procedure / emptyline) line*
    line        = display
    
    procedure   = "procedure:"
    display     = "display" quoted text
    string      = quoted text quoted
    control     = "crlf"
    quoted      = ~'"[^\"]+"'
    text        = ~"[a-z A-Z 0-9]*"i
    emptyline   = ws+
    ws          = ~"\s*"
    """
)


