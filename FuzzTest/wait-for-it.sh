#!/usr/bin/env bash
# wait-for-it.sh

set -e

host="$1"
shift
cmd="$@"

until curl -s $host > /dev/null; do
  >&2 echo "Service at $host is unavailable - sleeping"
  sleep 3
done

>&2 echo "Service at $host is up - executing command"
exec $cmd
