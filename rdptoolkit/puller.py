#!/usr/bin/env python3
import json
import os
import synapseclient

from rdptoolkit.config import config


class Puller:
    tools = []

    def __init__(self):
        self.tools = []

    def pull_from_nlpsandbox(self):
        print(f"Pull from nlpsandbox")
        syn = synapseclient.Synapse()
        syn.login()
        main_leaderboard_table_id = "syn23747126"
        evaluation_queue_ids = {
            "date_annotator": "9614652",
            "person_name_annotator": "9614657",
            "location_annotator": "9614658",
            "contact_annotator": "9614799",
            "id_annotator": "9614797",
        }

        query_template = (
            'select id as "Submission Id", createdOn as "CreatedOn", '
            "submitterid as Submitter, tool__api_version as "
            '"NLP Sandbox Version",  location_F1_token_strict as '
            '"i2b2 Score", MCW_location_F1_token_strict as '
            '"MCW score", Mayo_location_F1_token_strict as '
            '"Mayo score", tool__name as "Tool Name",  tool__version as '
            '"Tool Version", tool__url as "Tool URL", tool__description '
            'as "Tool Description", tool__license as "License", '
            'dockerrepositoryname as "Image", dockerdigest as '
            '"Image Digest", dataset_name as "i2b2 dataset", dataset_version '
            'as "i2b2 dataset version", MCW_dataset_name as '
            '"MCW dataset name", MCW_dataset_version as '
            '"MCW dataset version", Mayo_dataset_name as '
            '"Mayo dataset name", Mayo_dataset_version as "Mayo dataset '
            'version" from  syn23747126 where evaluationid =%s and '
            "status = 'ACCEPTED' and MCW_submission_status = "
            "'SCORED' and (Mayo_submission_status = 'SCORED' or "
            "Mayo_submission_status is null)"
        )

        query = query_template % (evaluation_queue_ids["date_annotator"])

        results = syn.tableQuery(query)
        for row in results:
            print(row)

        # print(f"{evaluation_queue_ids['date_annotator']}")
        # print(f"{results}")
        # pusher = Pusher()
        # pusher.read_tools(tools_filepath)
        # pusher.add_rdp_properties()
        # pusher.push_tools()
