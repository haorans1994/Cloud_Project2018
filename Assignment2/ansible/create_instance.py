"""
Team 7:
Fei Teng 809370
Haoran Sun 839693
Niu Tong 811179
Qingqian Yang 736563
Yunpeng Shao 854611
Function to automatically develop server and database on nectar
"""
import boto as Boy
import boto.ec2
import time
import configparser

# Set up the region
region = Boy.ec2.regioninfo.RegionInfo(name='melbourne', endpoint='nova.rc.nectar.org.au')

# Establish the connection
connection = Boy.connect_ec2(aws_access_key_id='9f216f38513b4149ba853209df9c1639',
							 aws_secret_access_key='94867b26d40b4ccdb8cf8461ee8761b4', 
							 is_secure=True, 
							 region=region, 
							 port=8773, 
							 path='/services/Cloud', 
							 validate_certs=False)

# Database instance set up
newreservation_db1 = connection.run_instances('ami-00003837', 
											 key_name='team7', 
											 placement='melbourne-qh2', 
											 instance_type='m1.medium', 
											 security_groups=['default','ssh','team7'])

instance_db1 = newreservation_db1.instances[0]
print('Creating instance_db1 {}'.format(instance_db1.id))
while instance_db1.state != 'running':
	print('instance_db1 {} is {}'.format(instance_db1.id, instance_db1.state))
	time.sleep(5)
	instance_db1.update()	
print('New instance_db1 {} has been created'.format(instance_db1.id))

# Database volume set up
vol_req_db1 = connection.create_volume(100, 'melbourne-qh2')
curr_vols_db1 = connection.get_all_volumes([vol_req_db1.id])
connection.attach_volume(vol_req_db1.id, instance_db1.id, '/dev/vdc')

instance_db1.update()
print('Volume {} has been attached to {} on dev/vdc'.format(vol_req_db1.id, instance_db1.id))

# Write the web config file
user_db1 = 'ubuntu'
user_db1 = user_db1.strip()
config_db1 = configparser.RawConfigParser(allow_no_value=True)
config_db1.add_section('database')
config_db1.add_section('webserver')
config_db1.add_section('webserver:vars')
config_db1.add_section('database:vars')
config_db1.set('database:vars', 'ansible_ssh_private_key_file', 'team7.key')
config_db1.set('database:vars', 'ansible_port', '22')
config_db1.set('database:vars', 'ansible_user', user_db1)
config_db1.set('database', instance_db1.private_ip_address)
config_db1.set('webserver', instance_db1.private_ip_address)

with open('./host_db1.ini', 'w') as config_db1_file:
        config_db1.write(config_db1_file)

# Database instance set up
newreservation_db2 = connection.run_instances('ami-00003837', 
											 key_name='team7', 
											 placement='melbourne-qh2', 
											 instance_type='m1.medium', 
											 security_groups=['default','ssh','team7'])

instance_db2 = newreservation_db2.instances[0]
print('Creating instance_db2 {}'.format(instance_db2.id))
while instance_db2.state != 'running':
	print('instance_db2 {} is {}'.format(instance_db2.id, instance_db2.state))
	time.sleep(5)
	instance_db2.update()	
print('New instance_db2 {} has been created'.format(instance_db2.id))

# Database volume set up
vol_req_db2 = connection.create_volume(30, 'melbourne-qh2')
curr_vols_db2 = connection.get_all_volumes([vol_req_db2.id])
connection.attach_volume(vol_req_db2.id, instance_db2.id, '/dev/vdc')

instance_db2.update()
print('Volume {} has been attached to {} on dev/vdc'.format(vol_req_db2.id, instance_db2.id))

# Write the web config file
user_db2 = 'ubuntu'
user_db2 = user_db2.strip()
config_db2 = configparser.RawConfigParser(allow_no_value=True)
config_db2.add_section('database')
config_db2.add_section('webserver')
config_db2.add_section('webserver:vars')
config_db2.add_section('database:vars')
config_db2.set('database:vars', 'ansible_ssh_private_key_file', 'team7.key')
config_db2.set('database:vars', 'ansible_port', '22')
config_db2.set('database:vars', 'ansible_user', user_db2)
config_db2.set('database', instance_db2.private_ip_address)
config_db2.set('webserver', instance_db2.private_ip_address)

with open('./host_db2.ini', 'w') as config_db2_file:
        config_db2.write(config_db2_file)

# web instance set up
newreservation_web = connection.run_instances('ami-00003837',
											  key_name='team7', 
											  placement='melbourne-qh2', 
											  instance_type='m1.medium', 
											  security_groups=['default','ssh','team7'])

instance_web = newreservation_web.instances[0]
print('Creating instance_web {}'.format(instance_web.id))
while instance_web.state != 'running':
	print('instance_web {} is {}'.format(instance_web.id, instance_web.state))
	time.sleep(5)
	instance_web.update()	
print('New instance_web {} has been created'.format(instance_web.id))

# web volume set up
vol_req_web = connection.create_volume(30, 'melbourne-qh2')
curr_vols_web = connection.get_all_volumes([vol_req_web.id])
connection.attach_volume(vol_req_web.id, instance_web.id, '/dev/vdc')

instance_web.update()
print('Volume {} has been attached to {} on dev/vdc'.format(vol_req_web.id, instance_web.id))

# Write the web config file
user_web = 'ubuntu'
user_web = user_web.strip()
config_web = configparser.RawConfigParser(allow_no_value=True)
config_web.add_section('database')
config_web.add_section('webserver')
config_web.add_section('webserver:vars')
config_web.add_section('database:vars')
config_web.set('database:vars', 'ansible_ssh_private_key_file', 'team7.key')
config_web.set('database:vars', 'ansible_port', '22')
config_web.set('database:vars', 'ansible_user', user_web)
config_web.set('database', instance_web.private_ip_address)
config_web.set('webserver', instance_web.private_ip_address)

with open('./host_web.ini', 'w') as config_web_file:
        config_web.write(config_web_file)
