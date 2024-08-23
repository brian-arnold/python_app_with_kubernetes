# this command was run via `bash test_docker.sh` from the root of the project
# to confirm that the docker image was built correctly and that the python script 
# could be run from the docker container

DATA_DIR=/Users/bjarnold/Documents/docker/test_projects/python_app_with_kube/data
docker run -v ${DATA_DIR}:/data \
bjarnold/python-app-kube \
/data/input_file1.txt