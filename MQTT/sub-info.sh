#!/bin/sh

docker service inspect --format='{{.ID}}' subscriber
docker service inspect --format='{{.CreatedAt}}' subscriber
docker service inspect --format='{{.Spec.Name}}' subscriber

