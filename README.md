# Delete-kubernetes-deployment-using-kubernetes-sdk-for-python

In the above code what I have achived is that I have deleted the deployment inside the Kubernetes cluster using the k8s sdk for
python.

1. I have wiritten a python file named for_k8s_delete_dploy.py in this file I have created a function named delete_a_deploy() 
this function will delete a deployment.

2. I am feteching the names and creation time of deployment a file named deployment_creation_time.txt this file is created using 
my own logic I am not using any sdk for this.

3. I will pass the name of deployment in delete_a_deploy() and deployment will be deleted by checking it's creation time.
I have used if else condition for deletion (based on some time constratients)

4. When I have successfully deleted the deployment then I have used a cronJob for the deployment deletion.
Using cronJob I have learned some things how to attach persitanent volume to a CronJob.

I am opening the file named deployment_creation_time.txt from PVC that is shared between different containers.
and one more thing the file named deployment_creation_time.txt is genereted inside the PVC folder named /data/get_deployment_files

