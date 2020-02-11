from kubernetes import client, config, watch
from time import localtime, strftime
import os


def delete_a_deploy(deploy_name):
    # config.load_kube_config()       #use this line when you are executing this program at local machine 
    config.load_incluster_config()   # use this line when you are executing in k8s.
    k8s_apps_v1 = client.AppsV1Api()
    resp = k8s_apps_v1.delete_namespaced_deployment(name=deploy_name,namespace="default")
    # resp = k8s_apps_v1.delete_namespaced_deployment(name="gottygedit-delete",namespace="default")
    print("yes your ",deploy_name," deployment in default namespace is deleted successfully")

def delete_deployment():
    for i in data:
        deploy_name = i[0:i.index(' ')]
        deploy_time = i[i.index(" ")+1 :]
        
        print(deploy_time)

        current_local_time = str(strftime("%H:%M", localtime()))
        print(current_local_time)
        h1 = int(deploy_time[:deploy_time.index(":")])
        h2 = int(current_local_time[:current_local_time.index(":")])
        m1 = int(deploy_time[deploy_time.index(":")+1:])
        m2 = int(current_local_time[current_local_time.index(":")+1:])
        # print("h1 ",h1," h2 ",h2," m1 ",m1," m2 ",m2)
        # print(current_local_time)
        h_diff = abs(h2-h1)
        m_diff = abs(m2-m1)

        if(h_diff >=check_hours_time):  #hours comaparison  time is >=2 hours
            # delete_deployment()
            delete_a_deploy(deploy_name)
            print("if condition executed ")
        elif(m_diff>=check_minutes_time and h_diff>1):       #for 1:30 minutes
            delete_a_deploy(deploy_name)        #deleting deployment after time comparison
            print("first elif condition executed ")
        elif(h_diff>1 and m_diff>=30):
            # delete_deployment()
            delete_a_deploy(deploy_name)
            print("second elif condition executed ")
        elif (m_diff >=5):      # this elif is used for 5 minutes difference while I am TESTING
            delete_a_deploy(deploy_name)

    return "Your deployment and service deleted successfully"


if __name__ == "__main__":
    f = open("/data/get_deployment_files/deployment_creation_time.txt","r")
    data = f.readlines()
    check_hours_time =2       
    check_minutes_time=30 
    delete_deployment()