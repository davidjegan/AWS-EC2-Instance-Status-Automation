'''
Author: David Jegan Abishek
Mail: mailtodavidjegan@gmail.com
Github: @davidjegan
'''

import boto3

def stopinstanceshandler(event, context):
    ec2client = boto3.client('ec2')
    sesclient = boto3.client('ses')

    #Determine the region name
    regions = [region['RegionName'] for region in ec2client.describe_regions()['Regions']]

    #loop through the regions
    for regionoftheinstanceis in regions:
        ec2 = boto3.resource('ec2', region_name=regionoftheinstanceis)
        #filter instances in running state. If needed stopped instances can also be added
        instances = ec2.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
        #extract instance name,id and region
        for instance in instances:
            idoftheinstanceis = instance.id
            for tag in instance.tags:
                if tag['Key'] == 'Name':
                    nameoftheinstanceis =  tag['Value']
            print("HOSTID" + idoftheinstanceis )
            print("Region" + regionoftheinstanceis )
            print("NAME" + nameoftheinstanceis)
            #prepare the mail contents
            sender = 'orgsender@gmail.com'
            pysubject = 'Instance Status'
            pybody = 'Found Instances Running. Lambda has successfully stopped  the following instances'
            pytoaddresses = ['devteamhead@gmail.com', 'adminguru@gmail.com']
            mybody = pybody + " Name :" + nameoftheinstanceis + " ID " + idoftheinstanceis + " Region " + regionoftheinstanceis
            #stop the instance in running state and mail the concerned people
            ec2.instances.filter(InstanceIds=[instance.id]).stop()
            response = sesclient.send_email(Source=sender,Destination={'ToAddresses': pytoaddresses},Message={'Subject': {'Data':pysubject},'Body': {'Text': {'Data': pybody + " \n" + mybody},'Html': {'Data': pybody + "<br> " + mybody}}})
    return 'Successfully executed'