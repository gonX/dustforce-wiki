![Site Icon](/website/assets/siteicon.png)

Welcome to the dustforce-wiki!

For contributing, please see [CONTRIBUTING.md](/CONTRIBUTING.md).

For a somewhat up to date representation view of the compiled repo, see [dustforce.info](https://www.dustforce.info/)

# Building the site locally

## Prerequisites

- Ruby (tested with 2.7.1)
- [bundler](https://bundler.io/) (tested with 2.1.4)

Bundler is technically not necessary if you can manage the Ruby dependencies (such as Jekyll) by yourself, but it is easier to get started by using Bundler.

#### Rubygem users

If you have a working [rubygems](https://rubygems.org/) (`gem`) install, you should be able to simply `gem install bundler` to cover the prerequisites.

## Building

On your very first run:

```
$ cd website/
$ bundle install
```

then on any following runs, you can simply do:

```
$ cd website/
$ bundle exec jekyll build
```

## Serving site from Jekyll

This will also build the site for you, and present it to you at `http://127.0.0.1:4000` while keeping the site updated as content changes.

Some files are not or can not be monitored by the serve process (such as `website/_config.yml`), requiring you to restart.

```
$ cd website/
$ bundle exec jekyll serve --incremental
```
