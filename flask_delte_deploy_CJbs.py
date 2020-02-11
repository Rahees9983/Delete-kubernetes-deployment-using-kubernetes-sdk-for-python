import flask
from kubernetes import client, config, watch
from time import localtime, strftime
import os

app = flask.Flask(__name__)

def delete_a_deploy():
    config.load_kube_config()       #use this line when you are executing this program at local machine 
    # config.load_incluster_config()   # use this line when you are executing in k8s.
    k8s_apps_v1 = client.AppsV1Api()
    resp = k8s_apps_v1.delete_namespaced_deployment(name="gottygedit-delete",namespace="default")
    print("yes your gottygedit-delete deployment in default namespace is deleted successfully")


def list_all_deployment_in_ur_default():
    config.load_kube_config()
    # config.load_incluster_config()
    k8s_apps_v1 = client.AppsV1Api()
    resp3 = k8s_apps_v1.list_namespaced_deployment(namespace="scp-namespace")
    # resp4 = k8s_apps_v1.l
    # print(resp3)
    # f1 = open("time_name_of_deploy_file.txt",'a') 
    # f1.write(str(resp3))

def store_time_name_of_deploy():
    # f2 = open("filtered_time_name.txt",'a')
    config.load_kube_config()

    v1 = client.CoreV1Api()
    v2 = client.ExtensionsV1beta1DeploymentCondition()
    # v3 = client.V1ObjectMeta.
    print(v2.attribute_map("default"))
    
    
    print("value of a  is ",a)
    count = 10
    w = watch.Watch()
    # v1.delete_namespaced_service(name="scp-cntr1-service",namespace="scp-namespace")   # BHUT MAST HAI BHAI EIS SE MAINE 
    # SERVIC DELETE KR DE HAI 

    # for event in w.stream(v1.delete_namespaced_service(name="tanya-service",namespace="default"), _request_timeout=60):
    #     print("Event: %s %s" % (event['type'], event['object'].metadata.name))
    #     count -= 1
    #     if not count:
    #         w.stop()

    print("Ended.")
    
# f = open("/data/get_deployment_files/cron_job_rahees.txt","r")
# data = f.readlines()
# check_hours_time =2       
# #declaring our test time for deployment deletion in hours
# check_minutes_time=2      #declaring our test time for deployment deletion in minutes


def delete_a_deploy(deploy_name):
    # config.load_kube_config()       #use this line when you are executing this program at local machine 
    config.load_incluster_config()   # use this line when you are executing in k8s.
    k8s_apps_v1 = client.AppsV1Api()
    resp = k8s_apps_v1.delete_namespaced_deployment(name=deploy_name,namespace="default")
    # resp = k8s_apps_v1.delete_namespaced_deployment(name="gottygedit-delete",namespace="default")
    print("yes your ",deploy_name," deployment in default namespace is deleted successfully")



@app.route("/delete_deploy_service")
def delete_deploy_service():
    # deploy_k8s.create_gotty_deployment()
    # deploy_k8s.create_gotty_service()
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

        if(h_diff >=check_hours_time):  #hours comaparison
            # delete_deployment()
            delete_a_deploy(deploy_name)
            print("if condition executed ")
        elif(m_diff>=check_minutes_time and h_diff>1):       #m
            delete_a_deploy(deploy_name)        #deleting deployment after time comparison
            print("first elif condition executed ")
        elif(h_diff>1 and m_diff>=30):
            # delete_deployment()
            delete_a_deploy(deploy_name)
            print("second elif condition executed ")
        elif (m_diff >=5):      # this elif is used for 5 minutes difference while I am testing 
            delete_a_deploy(deploy_name)

    return "Your deployment and service deleted successfully"


if __name__ == "__main__":
    f = open("/data/get_deployment_files/cron_job_rahees.txt","r")
    data = f.readlines()
    check_hours_time =2       
    check_minutes_time=2 
    delete_deploy_service()
    app.run(debug=True,host='0.0.0.0',port=5777)


