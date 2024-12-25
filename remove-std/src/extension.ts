import * as vscode from 'vscode';

export function activate(context: vscode.ExtensionContext) {
    console.log('Расширение "remove-std" активировано.');

    // Регистрируем команду
    let disposable = vscode.commands.registerCommand('remove-std.removeStd', () => {
        const editor = vscode.window.activeTextEditor;
        if (!editor) {
            vscode.window.showInformationMessage('Нет открытого редактора.');
            return;
        }

        const selection = editor.selection;
        const text = editor.document.getText(selection.isEmpty ? editor.document.validateRange(new vscode.Range(0, 0, editor.document.lineCount, 0)) : selection);
        const newText = text.replace(/std::/g, '');

        editor.edit(editBuilder => {
            if (selection.isEmpty) {
                const entireRange = new vscode.Range(0, 0, editor.document.lineCount, 0);
                editBuilder.replace(entireRange, newText);
            } else {
                editBuilder.replace(selection, newText);
            }
        });
    });

    // Добавляем команду в контекст
    context.subscriptions.push(disposable);
}

export function deactivate() {}
