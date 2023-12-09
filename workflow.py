import jsons
import sys


class WorkFlow:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def out_put(self):
        return sys.stdout.write(jsons.dumps(self, jdkwargs={"indent": 4}))


class WorkFlowItem:
    def __init__(self):
        self.title = None
        self.subtitle = None
        self.arg = None
        self.icon = None

    def set_title(self, title):
        self.title = title

    def set_subtitle(self, subtitle):
        self.subtitle = subtitle

    def set_arg(self, arg):
        self.arg = arg

    def set_icon(self, icon):
        self.icon = icon


class WorkFlowItemIcon:
    def __init__(self):
        self.type = None
        self.path = None

    def set_type(self, type):
        self.type = type

    def set_path(self, path):
        self.path = path


# 输出结果示意：
# {
#     "items": [
#         {
#             "arg": "this is arg",
#             "icon": {
#                 "path": "/icon_path",
#                 "type": "filetype"
#             },
#             "subtitle": "this is subtitle",
#             "title": "this is title"
#         }
#     ]
# }


if __name__ == "__main__":
    wf = WorkFlow()

    # custom process start
    item = WorkFlowItem()
    item.set_title("this is title")
    item.set_subtitle("this is subtitle")
    item.set_arg("this is arg")

    item_icon = WorkFlowItemIcon()
    item_icon.set_path("/icon_path")
    item_icon.set_type("filetype")
    item.set_icon(item_icon)
    wf.add_item(item)
    # custom process finish

    wf.out_put()
