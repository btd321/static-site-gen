

class HTMLNODE:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        final_str = ""
        for key,value in self.props.items():
            final_str += f" {key}={value}"
        if not final_str or final_str == "":
            return None 
        return final_str

    def __repr__(self):
        print(f"object:{self} tag:{self.tag} value:{self.value} children:{self.children} props:{self.props}")

