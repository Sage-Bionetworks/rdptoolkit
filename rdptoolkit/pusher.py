#!/usr/bin/env python3
import json
import os
from elasticsearch import Elasticsearch
from elasticsearch import helpers
from rdptoolkit.config import config


class Pusher:
    tools = []

    def __init__(self):
        self.client = Elasticsearch(
            [config.elasticsearch_host],
            port=config.elasticsearch_port,
            http_auth=(
                config.elasticsearch_username,
                config.elasticsearch_password))
        self.tools = []

    def read_tools(self, tools_path):
        with open(tools_path) as f:
            tools = json.load(f)
        self.tools = tools

    def add_rdp_properties(self):
      for tool in self.tools:
        tool["@type"] = "ComputationalTool"
        tool["resourceTypeName"] = "Tool"
        tool["applicationCategory"] = tool["toolType"]
        tool.pop("toolType")
        # print(tool["applicationCategory"])
      print(f"{json.dumps(self.tools)}")

    def generate_tools_data(self, es_index):
        for tool in self.tools:
            yield {
                "_index": es_index,
                "tool": tool,
            }

    def push_tools(self):
        """
        Upload the documents.
        """
        es_index = config.elasticsearch_indices["csbc_pson_computational_tools"]
        helpers.bulk(self.client, self.generate_tools_data(es_index))
