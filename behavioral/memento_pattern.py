class Editor:
    def __init__(self):
        self.text = ""

    def type(self, word):
        self.text += word

    def save(self):              # 메멘토 역할을 문자열이 직접 수행
        return self.text

    def restore(self, snapshot): # 문자열로 복원
        self.text = snapshot


class SnapshotHistory:
    def __init__(self):
        self.history = []

    def push(self, snapshot):
        self.history.append(snapshot)

    def pop(self):
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
    