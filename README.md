<p align="center">
  <img src="https://i.imgur.com/OKDE67x.png" 
</p>
  
##  Building an image labels generator using Amazon Rekognition

In this project, I created an image labels generator using Amazon Rekognition. With this tool, we can easily identify individual parts of an image and assign a label. For instance, if you have a photo of a high traffic environment, Amazon Recognition will be able to identify what it is, and label the image with it's parts.


<h2>Environments and Technologies Used</h2>

  - Amazon Web Services (AWS)
  - S3 
  - AWS CLI
  - Python
  - Amazon Rekognition
  - IAM
  
  
<h2>How to Build</h2>

1. **Create a S3 Bucket and upload files**  

![image](/assets/image1.png)
![image](/assets/image2.png)

For this project, we will use a sample image from Orlando city.

![image](/assets/image3.png)

2. **Install and configure AWS CLI**  
Open the terminal for your operating system and use these commands accordingly:

To check if the AWS CLI (Command Line Interface) was installed successfully on your system, you can run the following command in your terminal or command prompt:

`aws --version`

Next, we will need to configure AWS CLI with command `AWS configure`. For this, we will need to set up a user in IAM with an access key and secret access key through the console so that we can execute actions and commands with our AWS account:
![image](/assets/image5.png)

After searching `IAM` in the AWS console we start creating a user:
![image](/assets/image6.png)
![image](/assets/image7.png)

Next, after assigning a name we create permissions for our new user:
![image](/assets/image8.png)

NOTE: The permission policies that we are assigning to this user will be giving access to all AWS services. It is generally not recommended if the user will be used by someone else.

Then, we click on the user and create an access key:
![image](/assets/image9.png)

---

3. **Importing Libraries from Python**
   


4. **Define Functions**




5. **Final code with results**




 ---

<h2>Conclusion</h2>
This projects demostrates a real-world scenario where we can create a website hosted with an S3 bucket utilizing AWS. In this example we also utilized .HTML and .CSS files to load our resume file into the bucket. By utilizing secure dns protocols and traffic through Route 53 and Cloudfront, we made sure that our website is fully compliant and accessible, as well as providing our own custom domain. This project was made with AWS free tier on all tools except for Route 53, where creating hosted zones has a cost as well. You can add a CNAME to a Cloudfront endpoint address using godaddy instead if you wish to cut on costs. Note that CNAMEs are not available at the root (apex) of the domain, so unless godaddy provides a CNAME flattening service (equivalent to Alias) you can only set it on a subdomain. There is also a cost in purchasing a third party domain or inside AWS. With this feature, you can utilize both without issues.
☁️
