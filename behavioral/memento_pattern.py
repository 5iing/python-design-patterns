class Editor:
    def __init__(self):
        self.text = ""

    def type(self, word) -> None:
        self.text += word

    def save(self) -> str:
        return self.text

    def restore(self, snapshot) -> None:
        self.text = snapshot


class SnapshotHistory:
    def __init__(self):
        self.history = []

    def push(self, snapshot) -> None:
        self.history.append(snapshot)

    def pop(self) -> None:
        return self.history.pop() if self.history else None

if __name__ == '__main__':
    editor = Editor()
    history = SnapshotHistory()

    editor.type("Hello ")
    editor.type("World!")
    history.push(editor.save())
    print(f"1: {editor.text}")

    editor.type(" More text.")
    print(f"2: {editor.text}")

    editor.restore(history.pop())
    print(f"3: {editor.text}")
    