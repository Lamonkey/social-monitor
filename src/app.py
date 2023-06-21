import panel as pn
from sherlock.sherlock import main as run_sherlock
import sys
from contextlib import redirect_stdout
import io
import time
import threading


class SherlockStream(Stream, io.StringIO):
    def __init__():
        super.__init__()

    def __enter__(self):
        pass


def fake_stream():
    for i in range(5):
        print(i)
        time.sleep(1)


class sherlockStream(io.StringIO):
    def __init__(self):
        super().__init__()


def run_sherlock_adapter() -> str:
    with redirect_stdout(io.StringIO(newline="\n")) as f:
        thread = threading.Thread(target=run_sherlock)
        thread.start()
        while (thread.is_alive()):
            yield f.getvalue()
            f.truncate(0)
            time.sleep(1)
        thread.join()
        # thread.start()
        # yield f.getvalue()
    # thread.join()


# for result in run_sherlock_adapter():
#     print(result)

pn.extension('terminal')
w1 = pn.widgets.TextInput(name='Text:')
w2 = pn.widgets.FloatSlider(name='Slider')

# sherlock_options = box = pn.GridBox(*[pn.widgets.CheckBox(name="Checkbox") for i in range(24)], ncols=6)
options = {
    "help": {
        "description": "show this help message and exit",
        "arg": "-h"
    },
    "version": {
        "description": "Display version information and dependencies.",
        "arg": "--version"
    },
    "verbose": {
        "description": "Display extra debugging information and metrics",
        "arg": "-v"
    },
    "debug": {
        "description": "Display extra debugging information and metrics",
        "arg": "-d"
    },
    "folderoutput": {
        "description": "If using multiple usernames, the output of the results will be saved to this folder.",
        "arg": "--folderoutput FOLDEROUTPUT, -fo FOLDEROUTPUT"
    },
    "output": {
        "description": "If using single username, the output of the result will be saved to this file.",
        "arg": "--output OUTPUT, -o OUTPUT"
    },
    "tor": {
        "description": "Make requests over Tor; increases runtime; requires Tor to be installed and in system path.",
        "arg": "--tor, -t"
    },
    "unique-tor": {
        "description": "Make requests over Tor with new Tor circuit after each request; increases runtime; requires Tor to be installed and in system path.",
        "arg": "--unique-tor, -u"
    },
    "csv": {
        "description": "Create Comma-Separated Values (CSV) File.",
        "arg": "--csv"
    },
    "xlsx": {
        "description": "Create the standard file for the modern Microsoft Excel spreadsheet (xslx).",
        "arg": "--xlsx"
    },
    "site": {
        "description": "Limit analysis to just the listed sites. Add multiple options to specify more than one site.",
        "arg": "--site SITE_NAME"
    },
    "proxy": {
        "description": "Make requests over a proxy. e.g. socks5://127.0.0.1:1080",
        "arg": "--proxy PROXY_URL, -p PROXY_URL"
    },
    "json": {
        "description": "Load data from a JSON file or an online, valid, JSON file.",
        "arg": "--json JSON_FILE, -j JSON_FILE"
    },
    "timeout": {
        "description": "Time (in seconds) to wait for response to requests (Default: 60)",
        "arg": "--timeout TIMEOUT"
    },
    "print-all": {
        "description": "Output sites where the username was not found.",
        "arg": "--print-all"
    },
    "print-found": {
        "description": "Output sites where the username was found.",
        "arg": "--print-found"
    },
    "no-color": {
        "description": "Don't color terminal output",
        "arg": "--no-color"
    },
    "browse": {
        "description": "Browse to all results on default browser.",
        "arg": "--browse, -b"
    },
    "local": {
        "description": "Force the use of the local data.json file.",
        "arg": "--local, -l"
    },
    "nsfw": {
        "description": "Include checking of NSFW sites from default list.",
        "arg": "--nsfw"
    }
}
options_selected = []


text_input = pn.widgets.TextInput(
    name='Text Input', placeholder='Enter username here...')
check_box_group = [pn.widgets.Checkbox(name=key) for key, item in options.items()]

sherlock_result = pn.widgets.Terminal(
    "Welcome to Sherlock Terminal, enter username to search/n",
    options={"cursorBlink": True},
    height=300, sizing_mode='stretch_width'
)


def run_sherlock_module(event):
    # clean argv
    sys.argv = sys.argv[:1]
    # add position arguments
    for user_name in text_input.value.split(" "):
        sys.argv.append(user_name)
    # add options
    for check_box in check_box_group:
        if check_box.value:
            sys.argv.append(options[check_box.name]['arg'])
    # sherlock_result.write(f'search: {text_input.value}')
    # sherlock_result.write(f'args: {sys.argv}')
    for result in run_sherlock_adapter():
        sherlock_result.write(result)
    # for check_box in check_box_group:
    #     print(check_box.name, check_box.value)


sherlock_options = pn.GridBox(
    *check_box_group, ncols=3)
run_button = pn.widgets.Button(name='Click me', button_type='primary')
column1 = pn.Column('# Column', text_input, sherlock_options, run_button)
column2 = pn.Column('# Column', sherlock_result)
sherlock_app = pn.Row(column1, column2)

run_button.on_click(run_sherlock_module)
sherlock_app.servable()
