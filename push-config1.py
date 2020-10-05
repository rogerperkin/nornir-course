from nornir import InitNornir
from nornir_napalm.plugins.tasks import napalm_get
from nornir_utils.plugins.functions import print_result, print_title
from nornir_netmiko.tasks import netmiko_send_config, netmiko_send_command, netmiko_save_config
from nornir.core.filter import F

nr = InitNornir(config_file="./config.yml")



def configbasic(task):
    task.run(task=netmiko_send_config, config_file="config_text.txt")
    task.run(task=netmiko_send_command, command_string="sh ip int brief")
    task.run(task=netmiko_save_config)
#   task.run(task=netmiko_send_command, command_string="wr mem")
    
devices = nr.filter(F(groups__contains="CSR"))

results = devices.run(task = configbasic)

print_title("Pushing Config with Nornir")
print_result(results)



