# Research Discovery Portal (RDP) toolkit
Tools to interact with the Resource Discovery Portal (RDP)

## Requirements

- [pipenv]

## Usage

Create and activate the pipenv environment.

```console
pipenv install --deploy --dev
pipenv shell
```

Create the configuration file `.env` and export its parameters to environment
variables.

```console
cp .env.example .env
export $(grep -v '^#' .env | xargs)
```

Install this Python package.

```console
pip install -e .
```

### Prepare data

Pull and format computational tool data from the [Cancer Complexity Knowledge
Portal (CCKP)], then save them locally. Currently, data are not pulled directly
from the portal. Instead, we are working with a data dump provided by Verena
Chung (`data/cckp-tools.json`).

    rdptoolkit pull cckp-tools  // => data/computational-tools/cckp-tools.json

Pull and format data from [NLPSandbox.io], then save them locally.

    rdptoolkit pull nlpsandbox-tools  // => data/computational-tools/nlpsandbox-tools.json

### Push data to Elasticsearch

Push CCKP tools to Elasticsearch:

```console
rdptoolkit push tools \
  --tools_filepath data/computational-tools/cckp-tools.json \
  --es_index cckp-computational-tools-20220401

Reading data/computational-tools/cckp-tools.json
Pushing tools to ES index cckp-computational-tools-20220401
```

Push NLP Sandbox tools to Elasticsearch.

```console
rdptoolkit push tools \
  --tools_filepath data/computational-tools/nlpsandbox-tools.json \
  --es_index nlpsandbox-computational-tools-20220301

Reading data/computational-tools/nlpsandbox-tools.json
Pushing tools to ES index nlpsandbox-computational-tools-20220301
```

<!-- Links -->

[pipenv]: https://pipenv.pypa.io/en/latest/
[Cancer Complexity Knowledge Portal (CCKP)]: https://www.cancercomplexity.synapse.org/
[NLPSandbox.io]: https://nlpsandbox.io