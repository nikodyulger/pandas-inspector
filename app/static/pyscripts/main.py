from js import window


async def run_code_click(event):

    editor = window.ace.edit("code-editor")
    code = editor.getValue()

    exec(code)
