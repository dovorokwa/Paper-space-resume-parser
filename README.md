## Model Deployment
#### Deployment Steps

* Create a new Project in PaperSpace cloud
* Create and push the docker image into Docker Hub
* Install Gradient CLI using the following command `pip install -U gradient`
* Login to the Gradient Paperspace using the following command `gradient apiKey <YOUR_API_KEY>`
* Run the command to deploy the model `gradient deployments create --name my-first-deployment --projectId <YOUR_PROJECT_ID> --spec ./deployment.yaml`

The commands to build and push the docker image into docker hub are given in ```Dockerfile```