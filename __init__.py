import json

from anki.hooks import wrap
from anki.lang import _
from aqt.editor import Editor

from .config import getUserOption
from .from_file import add_style_in_web, str_from_file_name


def setBrowserResizeImage(self):
    js = ["js", "jquery-ui"]
    css = ["jquery-ui"]
    css = "\n".join(str_from_file_name(f"{file}.css") for file in css)
    js = "\n".join(str_from_file_name(f"{file}.js") for file in js)
    add_style_in_web(self, css)
    self.web.eval(js)
    style = getUserOption("resizable-style", "border:1px dashed black;")
    if style:
        add_style_in_web(self, f".ui-wrapper {{   {style} }}")
    for m, default in [
            ("min", "10px"),
            ("max", "200px")
    ]:
        for direction in ["width", "height"]:
            if getUserOption(f"apply {m}imum {direction} when not resizing", False):
                limit = getUserOption(f"{m}-{direction}", default)
                add_style_in_web(
                    self, f""".field img {{{m}-{direction}: {limit} }}""")
                self.web.eval(f"""{m}_{direction} = "{limit}";""")
    self.web.eval(
        f"""preserve_ratio={json.dumps(getUserOption("preserve ratio while resizing", "current"))}""")


Editor.setupWeb = wrap(Editor.setupWeb, setBrowserResizeImage)
# use webview_will_set_content when .21 goes out
