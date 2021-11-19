# resource-discovery-portal-tools
Tools to interact with the Resource DIscovery Portal (RDP)

## Usage

Create and activate the conda environment.

```console
conda create -y --name rdp-tools python=3.9.7
conda activate rdp-tools
```

Install this Python package.

```console
pip install -e .
```

Push CCKP tools in JSON format to Elasticsearch.

```console
rdptoolkit push cckp-tools --tools_filepath data/cckp-tools-sample.json
```
