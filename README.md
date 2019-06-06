Welcome to the dustforce-wiki!

For contributing, please see [CONTRIBUTING.md](/CONTRIBUTING.md).

# Building the site locally

## Prerequisites

- Ruby
- [Jekyll](https://jekyllrb.com/) (tested with 3.8.5)
- [bundler](https://bundler.io/) (tested with 2.0.1)

### Building for the first time

On your very first run:
```
$ cd website/
$ bundle install
```

## Building

```
$ cd website/
$ bundle exec jekyll build
```

## Serving site from Jekyll

This will also build the site for you, but present it to you at `http://127.0.0.1:4000` while keeping the site updated as content changes.

If you're changing `website/_config.yml`, restarting `jekyll serve` is necessary to load those changes.

```
$ cd website/
$ bundle exec jekyll serve --incremental
```
