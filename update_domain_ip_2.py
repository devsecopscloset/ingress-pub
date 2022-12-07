import os

print(str(os.popen("kubectl get svc -n ingress-nginx | grep 'ingress-nginx-controller' | grep 'LoadBalancer' | awk '{print $4}'").read()[:-1]))

ingress_ip=str(os.popen("kubectl get svc -n ingress-nginx | grep 'ingress-nginx-controller' | grep 'LoadBalancer' | awk '{print $4}' | tr '\n' ' '").read()[:-1])
# ingress_ip = str(ingress_ip)

print("hello" + ingress_ip)

vm_ip="172.173.136.198"

defectdojo="closetdojo.strangled.net"
prometheus="closetprometheus.strangled.net"
grafana="closetgrafana.strangled.net"

username="devsecopscloset"
password="closetadmin"


update_defect_dojo="http://devsecopscloset:"+password+"@sync.afraid.org/u/?h=closetdojo.strangled.net&ip="+vm_ip
update_prometheus="http://devsecopscloset:"+password+"@sync.afraid.org/u/?h=closetprometheus.strangled.net&ip="+ingress_ip
update_grafana="http://devsecopscloset:"+password+"@sync.afraid.org/u/?h=closetgrafana.strangled.net&ip="+ingress_ip

os.system("curl "+"\""+update_defect_dojo+"\"")
os.system("curl "+"\""+update_prometheus+"\"")
os.system("curl "+"\""+update_grafana+"\"")
