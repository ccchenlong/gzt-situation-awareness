from html.parser import HTMLParser

class TagValidator(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack = []
        self.void = {'area','base','br','col','embed','hr','img','input','link','meta','param','source','track','wbr'}
        self.errors = []
    def handle_starttag(self, tag, attrs):
        if tag not in self.void:
            self.stack.append(tag)
    def handle_endtag(self, tag):
        if tag in self.void:
            return
        if self.stack and self.stack[-1] == tag:
            self.stack.pop()
        else:
            self.errors.append(f'期望闭合 </{self.stack[-1] if self.stack else "?"}>，但遇到 </{tag}>')

p = r'd:\00 云上江西\03 赣政通\需求设计\态势感知\gzt-prototype\index.html'
with open(p, 'r', encoding='utf-8') as f:
    html = f.read()

v = TagValidator()
v.feed(html)
print('未闭合标签:', v.stack)
print('错误数:', len(v.errors))
if v.errors:
    for e in v.errors[:20]:
        print(e)
