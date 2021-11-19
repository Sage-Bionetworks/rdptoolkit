#!/usr/bin/env python3

import json

class Pusher:
    tools = []

    def read_tools(self, tools_path):
        with open(tools_path) as f:
            tools = json.load(f)
        self.tools = tools

    def push_tools(self):
        """
        Upload the document.
        """
        print(self.tools)