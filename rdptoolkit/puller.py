#!/usr/bin/env python3
import json
import os
import synapseclient

from rdptoolkit.config import config


class Puller:
    tools = []

    def __init__(self):
        self.tools = []

    def pull_from_cckp(self):
        print("Pulling tools from local CCKP data")
        with open("data/cckp-tools-sample.json") as f:
            tools = json.load(f)
        for tool in tools:
            new_tool = {
                "resourceTypeName": "Tool",
                "@context": "https://schema.org",
                "@type": "ComputationalTool",
                # "@id": f"https://cancercomplexity.synapse.org/#{tool.toolId}",
                "description": tool["description"],
                "name": tool["toolName"],
                "url": tool["homepage"],
                "applicationCategory": tool["toolType"],
                "license": tool["license"],
                "softwareVersion": tool["version"],
                "downloadUrl": tool["downloadUrl"],
                "operatingSystem": tool["operatingSystem"],
                "programmingLanguage": tool["language"],
            }
            self.tools.append(new_tool)
        with open("data/computational-tools/cckp-tools.json", "w") as f:
            json.dump(self.tools, f, indent=2)

    def pull_from_nlpsandbox(self):
        print("Pulling tools from nlpsandbox.io")
        syn = synapseclient.Synapse(silent=True)
        syn.login()
        # main_leaderboard_table_id = "syn23747126"
        evaluation_queue_ids = {
            "date_annotator": "9614652",
            "person_name_annotator": "9614657",
            "location_annotator": "9614658",
            "contact_annotator": "9614799",
            "id_annotator": "9614797",
        }

        query_template = (
            'select id as "sub_id", createdOn as "created_on", '
            "submitterid as submitter_id, tool__api_version as "
            '"tool_version",  location_F1_token_strict as '
            '"i2b2_score", MCW_location_F1_token_strict as '
            '"mcw_score", Mayo_location_F1_token_strict as '
            '"mayo_score", tool__name as "tool_name",  tool__version as '
            '"tool_version", tool__url as "tool_url", tool__description '
            'as "tool_description", tool__license as "tool_license", '
            'dockerrepositoryname as "image", dockerdigest as '
            '"image_digest", dataset_name as "i2b2_dataset_name", dataset_version '
            'as "i2b2_dataset_version", MCW_dataset_name as '
            '"mcw_dataset_name", MCW_dataset_version as '
            '"mcw_dataset_version", Mayo_dataset_name as '
            '"mayo_dataset_name", Mayo_dataset_version as '
            '"mayo_dataset_version" from syn23747126 where evaluationid =%s and '
            "status = 'ACCEPTED' and MCW_submission_status = "
            "'SCORED' and (Mayo_submission_status = 'SCORED' or "
            "Mayo_submission_status is null)"
        )

        for tool_type in evaluation_queue_ids:
            print(f"Fetching NLP Sandbox tool data for {tool_type}")
            sub_queue_id = evaluation_queue_ids[tool_type]

            query = query_template % (sub_queue_id)
            results = syn.tableQuery(query)

            for _, tool in results.asDataFrame().iterrows():
                new_tool = {
                    "resourceTypeName": "Tool",
                    "@context": "https://schema.org",
                    "@type": "ComputationalTool",
                    "@id": f"https://nlpsandbox.io/#{tool['sub_id']}",
                    "description": tool["tool_description"],
                    "name": tool["tool_name"],
                    "url": tool["tool_url"],
                    "applicationCategory": ["Docker image"],
                    "license": tool["tool_license"],
                    "softwareVersion": tool["tool_version"],
                    "downloadUrl": "https://nlpsandbox.io",
                    "operatingSystem": ["Windows", "Mac", "Linux"],
                    "programmingLanguage": [],
                    # "grantId": None,
                    # "grantName": None,
                    # "grantNumber": None,
                    # "consortium": ["CD2H"],
                    # "publicationTitle": None,
                    # "operation": "http://edamontology.org/operation_0226",
                    # "inputData": ["Clinical record"],
                    # "outputData": ["Annotations"],
                    # "inputFormat": ["Textual format"],
                    # "outputFormat": ["JSON"],
                    # "functionNote": None,
                    # "cmd": "docker compose up",
                    # "topic": ["NLP", "PHI annotation"],
                    # "operatingSystem": ["Windows", "Mac", "Linux"],
                    # "language": [],
                    # "license": row["tool_license"],
                    # "cost": "Free of charge",
                    # "accessibility": "Open access",  # depends on the license
                    # "downloadUrl": "https://nlpsandbox.io",
                    # "downloadType": ["Docker image"],
                    # "downloadNote": None,
                    # "downloadVersion": row["tool_version"],
                    # "documentationUrl": "https://nlpsandbox.io",
                    # "documentationType": [
                    #     "Installation instructions",
                    #     "Quick start guide",
                    #     "User manual",
                    # ],
                    # "documentationNote": None,
                    # "linkUrl": row["tool_url"],
                    # "linkType": "Repository",
                    # "linkNote": None,
                    # "portalDisplay": None,
                }
                self.tools.append(new_tool)

        with open("data/computational-tools/nlpsandbox-tools.json", "w") as f:
            json.dump(self.tools, f, indent=2)
