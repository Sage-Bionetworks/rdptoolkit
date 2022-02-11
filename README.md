# Research Discovery Portal (RDP) toolkit
Tools to interact with the Resource Discovery Portal (RDP)

## Usage

Create and activate the conda environment.

```console
conda create -y --name rdptoolkit python=3.9.7
conda activate rdptoolkit
```

Create the configuration file and export its parameters to environment
variables.

```console
cp .env.example .env
export $(grep -v '^#' .env | xargs)
```

Install this Python package.

```console
pip install -e .
```

Push CCKP tools in JSON format to Elasticsearch:

```console
rdptoolkit push cckp-tools --tools_filepath data/cckp-tools-sample.json
```

Push NLP Sandbox tools to Elasticsearch:

```console
rdptoolkit push nlpsandbox-tools
```

## Indices pushed

- `csbc-pson-computational-tools` (13 tools)
- `csbc-pson-computational-tools-20211209` (205 tools)
