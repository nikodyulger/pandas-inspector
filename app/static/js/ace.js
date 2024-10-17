var editor = ace.edit("code-editor");
editor.setTheme("ace/theme/cloud9_day");
editor.session.setMode("ace/mode/python");
editor.setOptions({
    autoScrollEditorIntoView: true,
    copyWithEmptySelection: true,
});