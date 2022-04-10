
class BaseElement:
    idn_lvl = 2
    idn_char = ' '
    tag = "<BaseElement @atr>@children</BaseElement>"
    

    def __init__(self):
        self.children = list()
        self.attributes = dict()

    def describe(self, description_dict):
        self.attributes.update(description_dict)

    def addChildren(self, children_list):
        if self.hasChildren:
            self.children.extend(children_list)
            

    def __repr__(self):
        repr_string = ""
        attr_string = ' '.join(
           [f'{k}="{v}"' for k, v in self.attributes.items()]
        )
        
        if self.hasChildren:
            for child in self.children:
                if issubclass(type(child), BaseElement):
                    child.idn_lvl += self.idn_lvl
                else: 
                    Exception("dfd")
            repr_string = self.tag.replace('@children', f"@children\n{(self.idn_lvl - 2 ) * ' '}")
            formated_children = '\n' + '\n'.join(map(str, self.children))
            repr_string = f"{(self.idn_lvl - 2 ) * ' '}{repr_string.replace('@children', formated_children)}"
        else:
            repr_string = f"{(self.idn_lvl - 2 ) * ' '}{self.tag}"
        return f"{repr_string.replace('@atr', attr_string)}"


class Input(BaseElement):
    tag = "<input @atr>"
    hasChildren = False

    def __init__(self):
        super().__init__()
    
class Select(BaseElement):
    tag = "<select @atr>@children</select>"
    hasChildren = True

    def __init__(self):
        super().__init__()


class Link(BaseElement):
    tag = "<a @atr>@children</a>"
    hasChildren = True

    def __init__(self):
        super().__init__()

class Image(BaseElement):
    tag = "<img @atr />"
    hasChildren = False

    def __init__(self):
        super().__init__()

class Div(BaseElement):
    tag = "<div @atr>@children</div>"
    hasChildren = True

    def __init__(self):
        super().__init__()

class Form(BaseElement):
    tag = "<form @atr>@children</form>"
    hasChildren = True

    def __init__(self):
        super().__init__()

class Text(BaseElement):
    tag = ""
    hasChildren = False

    def __init__(self, text):
        super().__init__()
        self.tag = text
        




class Examples:
    
    @classmethod
    def simple_example(self):
        form = Form()
        form.describe({'method':'POST', 'action':'/'})

        container1 = Div()
        container1.describe({'class':'md'})

        image = Image()
        image.describe({'class':'centered-logo'})

        container1.addChildren([image])

        inp = Input()
        inp.describe({'type':'text', 'name':'username'})

        link = Link()
        link.describe({'href':'/recover-password'})
        forgot_pass_text = Text("Forgot Password?")
        link.addChildren([forgot_pass_text])

        submit = Div()
        submit.describe({"onClick":'submit()'})

        form.addChildren([container1, inp, link, submit])
        return form