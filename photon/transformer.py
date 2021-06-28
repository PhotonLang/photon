from lark import Transformer, v_args, Tree, Token

@v_args(inline = True)
class PhotonTransformer(Transformer):
    def open_stmt(self, fp_tree: Tree, vnt: Token):
        # vnt - variable name token
        print(fp_tree)
        print(vnt)
        print(type(fp_tree))
        print(type(vnt))
        return "OPEN STATEMENT FOUND"


