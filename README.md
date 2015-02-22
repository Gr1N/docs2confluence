# docs2confluence

Solution for uploading markdown formatted documents to [Atlassian Confluence](https://www.atlassian.com/software/confluence)


# Install

Install Ruby dependency...

```shell
% gem install markdown2confluence
```

Install `docs2confluence`

```shell
% git clone https://github.com/Gr1N/docs2confluence.git && cd ./docs2confluence
% python setup.py install
```


# Usage

With env variables:

```shell
% CONFLUENCE_USER="username" CONFLUENCE_PASSWORD="userpassword" CONFLUENCE_DOMAIN="https://confluence.com" docs2confluence --config config.json
```

...or with command line arguments:

```shell
% docs2confluence --confluence-user username --confluence-password userpassword --confluence-domain https://confluence.com --config config.json
```


# TODO

- [ ] Handle network errors
- [ ] Handle Confluence errors (404, 409, 500...)
- [ ] Tests...
- [ ] Add CHANGELOG.md
- [ ] Python 3.x support


# License

*docs2confluence* is licensed under the MIT license. See the license file for details.
