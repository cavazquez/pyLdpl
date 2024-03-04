import pyparsing as pp

# Definir las reglas gramaticales
procedure_kw = pp.CaselessKeyword("procedure:")
data_kw = pp.CaselessKeyword("data:")
display_kw = pp.CaselessKeyword("display")
control_kw = pp.CaselessKeyword("crlf")
for_kw = pp.CaselessKeyword("for")
from_kw = pp.CaselessKeyword("from")
to_kw = pp.CaselessKeyword("to")
step_kw = pp.CaselessKeyword("step")
do_kw = pp.CaselessKeyword("do")
repeat_kw = pp.CaselessKeyword("repeat")

identifier = pp.Word(pp.alphas)
string_literal = pp.QuotedString('"', escChar='\\')
numbers = pp.Word(pp.nums).setParseAction(lambda t: int(t[0]))

display = display_kw + string_literal + control_kw
line = pp.MatchFirst([display , for_p])
for_p = pp.Group(for_kw + identifier + from_kw + numbers + to_kw + numbers + step_kw + numbers + do_kw + pp.OneOrMore(line) + repeat_kw )

type_var = pp.CaselessKeyword("number")
variables = identifier + "is" + type_var
procedure = pp.Group(pp.Suppress(procedure_kw) + pp.ZeroOrMore(line))
data = pp.Group(pp.Suppress(data_kw) + pp.OneOrMore(variables))

# Crear la expresión a analizar
grammar = pp.Optional(data) + procedure








