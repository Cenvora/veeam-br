<h1 align="center">
<br>
<img src="https://raw.githubusercontent.com/Cenvora/veeam-br/main/media/Veeam_logo_2024_RGB_main_20.png"
     alt="Veeam Logo"
     height="100">
<br>
<br>
Veeam Service Provider Console Python API Wrapper
</h1>

<h4 align="center">
Python package for interacting with the Veeam Service Provider Console REST API
</h4>

<!-- Summary -->
This project is an independent, open source Python client for the Veeam Service Provider Console <a href="https://helpcenter.veeam.com/docs/vac/rest/reference/vspc-rest.html">REST API</a>. It is not affiliated with, endorsed by, or sponsored by Veeam Software.
<!-- Summary -->

## Supported Versions

<table>
  <thead>
    <tr>
      <th>VBR Version</th>
      <th>API Version</th>
      <th>Supported</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>13.0.1.180</td>
      <td>1.3-rev1</td>
      <td style="text-align:center;">&#9989;</td>
    </tr>
    <tr>
      <td>&lt; 13.0.1.180</td>
      <td>&lt; 1.3-rev1</td>
      <td style="text-align:center;">&#10060;</td>
    </tr>
  </tbody>
</table>

## How to support new API versions
1. Download the OpenAPI yaml into openapi_schemas
2. Install the openapi-python-client package
2. Fix the OpenAPI yaml to conform to proper standards: `python fix_openapi_yaml.py .\openapi_schemas\vspc_rest_{vspc_version}.yaml .\openapi_schemas\vspc_rest_{vspc_version}_fixed.yaml`
3. Run `openapi-python-client generate --path ".\openapi_schemas\vspc_rest_{vspc_version}_fixed.yaml" --output-path ".\veeam_spc" --overwrite`
4. Fix any warnings/errors (application/binary+base64 can be ignored)
5. Rename the folder to match the API version (i.e., `v3_5_1`)
6. Update pyproject.toml to support the new packages
7. Write pytest tests
8. If an older API has been deprecated, delete its folder and yaml, then update the supported versions section of the readme

## Install
### From PyPi
`pip install veeam-br`


### From Source
Clone the repository and install dependencies:
```sh
git clone https://github.com/Cenvora/veeam-br.git
cd veeam-br
pip install -e .
```

## Contributing
Contributions are welcome! To contribute:
- Fork the repository
- Create a feature branch
- Make your changes and add tests
- Submit a pull request with a clear description

Please follow PEP8 style and include docstrings for new functions/classes.

## 🤝 Core Contributors
This project is made possible thanks to the efforts of our core contributors:

- [Jonah May](https://github.com/JonahMMay)  
- [Maurice Kevenaar](https://github.com/mkevenaar)  

We’re grateful for their continued support and contributions.