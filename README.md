# resource-discovery-portal-tools
Tools to interact with the Resource Discovery Portal (RDP)

## Usage

Create and activate the conda environment.

```console
conda create -y --name rdptoolkit python=3.9.7
conda activate rdptoolkit
```

Install this Python package.

```console
pip install -e .
```

Push CCKP tools in JSON format to Elasticsearch.

```console
rdptoolkit push cckp-tools --tools_filepath data/cckp-tools-sample.json
```
