tar -czh --exclude=build.sh --exclude=*.tar.gz . | docker build -t gocd-agent-dfwiki:latest -
