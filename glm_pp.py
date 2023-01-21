import gdb.printing

def _vec_info(v):
    # vec contains either a union of structs or a struct of unions, depending on
    # configuration. gdb can't properly access the named members, and in some
    # cases the names are wrong.
    # It would be simple to cast to an array, similarly to how operator[] is
    # implemented, but values returned by functions called from gdb don't have
    # an address.
    # Instead, recursively find all fields of required type and sort by offset.

    if v.type.code == gdb.TYPE_CODE_REF:
      v = v.referenced_value()

    T = v.type.template_argument(1)

    if T.code == gdb.TYPE_CODE_FLT:
        if T.sizeof == 4:
            type_prefix = ""
        elif T.sizeof == 8:
            type_prefix = "d"
        else:
            raise NotImplementedError
    elif T.code == gdb.TYPE_CODE_INT:
        if T.is_signed:
            type_prefix = "i"
        else:
            type_prefix = "u"
    elif T.code == gdb.TYPE_CODE_BOOL:
        type_prefix = "b"
    else:
        raise NotImplementedError

    length = v.type.sizeof // T.sizeof
    items = {}
    def find(v, bitpos):
        t = v.type.strip_typedefs()
        if t.code in (gdb.TYPE_CODE_STRUCT, gdb.TYPE_CODE_UNION):
            for f in t.fields():
                if hasattr(f, "bitpos"): # not static
                    find(v[f], bitpos + f.bitpos)
        elif t == T:
            items[bitpos] = v
    find(v, 0)
    assert len(items) == length
    items = [str(f) for k, f in sorted(items.items())]
    return type_prefix, length, items

class VecPrinter:
    def __init__(self, v):
        self.v = v

    def to_string(self):
        type_prefix, length, items = _vec_info(self.v)
        return "{}vec{}({})".format(type_prefix, length, ", ".join(items))

class MatPrinter:
    def __init__(self, v):
        self.v = v

    def to_string(self):
        V = self.v["value"]
        columns = []
        for i in range(V.type.range()[1] + 1):
            type_prefix, length, items = _vec_info(V[i])
            columns.append("({})".format(", ".join(items)))
        return "{}mat{}x{}({})".format(
            type_prefix, len(columns), length, ", ".join(columns))

def build_pretty_printer():
    pp = gdb.printing.RegexpCollectionPrettyPrinter("glm_pp")
    pp.add_printer("glm::vec", r"^glm::vec<", VecPrinter)
    pp.add_printer("glm::vec", r"^glm::mat<", MatPrinter)
    return pp

gdb.printing.register_pretty_printer(gdb.current_objfile(),
                                     build_pretty_printer())
