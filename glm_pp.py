import gdb.printing

_type_letters = {
    gdb.TYPE_CODE_FLT: "d", # or "f"
    gdb.TYPE_CODE_INT: "i",
    gdb.TYPE_CODE_BOOL: "b"
}

def _vec_info(v):
    # vec contains either a union of structs or a struct of unions, depending on
    # configuration. gdb can't properly access the named members.
    # Instead, simply cast to an array. This is similar to how operator[] is
    # implemented.
    T = v.type.template_argument(0)
    letter = _type_letters.get(T.code, "t")
    length = v.type.sizeof // T.sizeof
    V = v.address.cast(T.array(length-1).pointer()).dereference()
    items = tuple(str(V[i]) for i in range(length))
    return letter, length, items

class VecPrinter:
    def __init__(self, v):
        self.v = v

    def to_string(self):
        letter, length, items = _vec_info(self.v)
        return "{}vec{}({})".format(letter, length, ", ".join(items))

class MatPrinter:
    def __init__(self, v):
        self.v = v

    def to_string(self):
        V = self.v["value"]
        columns = []
        for i in range(V.type.range()[1] + 1):
            letter, length, items = _vec_info(V[i])
            columns.append("({})".format(", ".join(items)))
        return "{}mat{}x{}({})".format(
            letter, len(columns), length, ", ".join(columns))

def build_pretty_printer():
    pp = gdb.printing.RegexpCollectionPrettyPrinter("glm_pp")
    pp.add_printer(
        "glm::vec", r"^glm::(detail::)?tvec\d<[^<>]*>$", VecPrinter)
    pp.add_printer(
        "glm::mat", r"^glm::(detail::)?tmat\dx\d<[^<>]*>$", MatPrinter)
    return pp

gdb.printing.register_pretty_printer(gdb.current_objfile(),
                                     build_pretty_printer())
