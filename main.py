import sys
import quickjs


class MiniJSRuntime:
    def __init__(self):
        self.output = []
        self.context = quickjs.Context()
        self.setup_console()

    def setup_console(self):
        def console_log(*args):
            values = []

            for arg in args:
                if isinstance(arg, bool):
                    values.append(str(arg).lower())
                elif arg is None:
                    values.append("null")
                else:
                    values.append(str(arg))

            self.output.append(" ".join(values))

        self.context.add_callable("__console_log", console_log)

        self.context.eval("""
        var console = {
            log: function(...args) {
                __console_log(...args);
            }
        };
        """)

    def run(self, code):
        self.context.eval(code)
        return "\n".join(self.output)


def load_js_code():
    if len(sys.argv) == 1:
        return sys.stdin.read()

    if sys.argv[1] == "--version":
        print("ThunderJS Runtime v1.0")
        print("Built with Python")
        sys.exit()

    input_data = sys.argv[1]

    if input_data.endswith(".js"):
        with open(input_data, "r", encoding="utf-8") as file:
            return file.read()

    return input_data


def main():
    try:
        js_code = load_js_code()

        if not js_code.strip():
            print("Usage:")
            print("python main.py <file.js>")
            print('python main.py "console.log(123)"')
            print("cat test.js | python main.py")
            return

        runtime = MiniJSRuntime()
        result = runtime.run(js_code)

        if result:
            print(result)

    except FileNotFoundError:
        print("Error: JavaScript file not found")

    except Exception as error:
        print(f"Runtime Error: {error}")


if __name__ == "__main__":
    main()