value = "\\t\\n"
class encryption_decryption():
    def encrypt(self):
        global value
        if value == "\\t\\n":
            msg = "\n\nERROR:\n\nYou need to define a value first!"
            raise Exception(msg)
        _list = []
        ret = ""
        for x in range(len(value)):
            try:
                _list.append(value[x-x+(x%(x+2)-2)])
            except IndexError:
                _list.append(value[x-x+(x//(x+1))])
        for y in range(len(_list)):
            ret = ret + _list[y]
        return ret
    def decrypt(self):
        return encrypt()
    def set_value(self, new_value):
        global value
        value = new_value
