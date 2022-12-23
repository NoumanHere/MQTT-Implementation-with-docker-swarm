#!/bin/sh

docker service inspect --format='{{.ID}}' publisher
docker service inspect --format='{{.CreatedAt}}' publisher
docker service inspect --format='{{.Spec.Name}}' publisher



