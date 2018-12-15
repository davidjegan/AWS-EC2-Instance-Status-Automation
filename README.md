# EC2 Instance Automated Controller Script

### Description
Running EC2 Instances can be stopped in an automated server-less way using this script. The key services utilized here are 
  * [AWS Lambda] - To run our script!
  * [AWS SES] - For notifying stackholders!

### Architecture overview

[![ArchDiagram](https://github.com/davidjegan/AWS-EC2-Instance-Status-Automation/blob/master/assets/imgs/Arch.png)](https://github.com/davidjegan/AWS-EC2-Instance-Status-Automation/blob/master/assets/imgs/Arch.png)



### Steps

| Lambda |
| ------ |
| Create a new author from scratch function in AWS Lambda |
| Choose Python as the Programming language |
| Choose a suitable role which can access EC2 |
| Upload the [code] in the [Lambda](https://console.aws.amazon.com/lambda/home?region=us-east-1#/home) console |

| Cloudwatch |
| ------ |
| Create a new [rule](https://console.aws.amazon.com/cloudwatch/home?region=us-east-1#rules:) under the event heading |
| Provide a CRON expression |
| Click **Target** and select the previously created Lambda function |


### Development
Want to contribute? Great! Contact me in [Linkedin](https://linkedin.com/in/david-jegan-abishek-39556684/) or [Twitter](https://twitter.com/JeganAbishek)

License
----
MIT



   [AWS Lambda]: <https://aws.amazon.com/lambda/>
   [AWS SES]: <https://aws.amazon.com/ses/>
   [code]: <https://github.com/davidjegan/AWS-EC2-Instance-Status-Automation/blob/master/check_ec2_instance_status.py>
