

class Code:

    def __init__(self):
        self.code = ""
        self.code += "def main():" + "\n"
        self.space = 4

    def add_print(self, text, end):
        self.code += " "*self.space + f"print(\"{text}\", end={end})" + "\r\n"

    def exporter(self):
        self.code += """if __name__ == "__main__":\n"""        
        self.code += " "*self.space + "main()"
        return self.code
