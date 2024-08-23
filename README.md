# Kubernetes worked example

The following is a worked example of using kubernetes to deploy a simple python application that reads a file from a mounted volume, and creates an output file in the same directory in which the data has been processed in a trivial way. The goal is to use Kubernetes to deploy the application for many input files.

Given the Dockerfile and the python app `main.py` in the same directory, the following steps will create a docker image, push it to a docker registry, and deploy it to a kubernetes cluster.

`docker build -t bjarnold/python-app-kube:latest .`

Verify the image was created successfully:
`docker images`

Verify that the image works as expected by running a Docker container directly:
`bash 00_test_docker.sh`

Push the image to a docker registry:
`docker push bjarnold/python-app-kube:latest`

To test out Kubernetes on a single job, start a cluster and mount the directory with the input data:

`minikube start`
`minikube mount /Users/bjarnold/Documents/docker/test_projects/python_app_with_kube/data:/data`

The mount command needs to run in the background, so it is recommended to run it in a separate terminal window. So, open up a new terminal and confirm that the directory is mounted:
` minikube ssh`
`ls /data`
`exit`

You should see the input files.

Finally, deploy the job to the cluster:
`kubectl apply -f job_single.yml`

To track jobs use:
`kubectl get jobs`

To get more information, get the pod name:
`kubectl get pods`

and use:
`kubectl logs <pod-name>`
`kubectl describe pod <pod-name>`

Note that if you already ran this job, you will need to delete the job before running it again (you can give multiple job names separated by spaces):
`kubectl delete jobs <job-name>`

Then, to run all 3 jobs in parallel, use:
`kubectl apply -f job_multi_1.yml`


To read more about parallel processing using kubernetes, see [this](https://kubernetes.io/docs/tasks/job/parallel-processing-expansion/) link:
