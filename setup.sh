#launch demon Docker
sudo service docker start

#download image
docker image pull datascientest/fastapi:1.0.0

#create network
docker network create --subnet 172.50.0.0/16 --gateway 172.50.0.1 raph_net

#create volume
docker volume create --name raph_volume

#create authentification image
cp Dockerfile_authentification Dockerfile
docker image build . -t authentification_image:latest

#create authorization image
cp Dockerfile_authorization Dockerfile
docker image build . -t authorization_image:latest

#create content image
cp Dockerfile_content Dockerfile
docker image build . -t content_image:latest

#create docker compose
docker-compose up
