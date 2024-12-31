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

2. **Upload files to S3 Bucket**  
  

https://github.com/user-attachments/assets/d9005a2e-2eac-4a9d-95ea-751fafef9989

After creation, it will create a S3 webpoint. In this case, it would be http://awsresume.online.s3-website-us-east-1.amazonaws.com/


https://github.com/user-attachments/assets/de9ebe2f-226e-4969-9224-e5fa70143bb6

<p align="center">
  <img src="https://i.imgur.com/OKDE67x.png" 
</p>
---

3. **Create a Cloudfront Distribution**
   

https://github.com/user-attachments/assets/bf262c0b-e4f5-4af0-90fc-76cdcfdb5a05



After creation, a cloudfrount domain name will be created with an HTTPS resolver. In this case, the address would be https://d2ygp4l15ss99c.cloudfront.net

<p align="center">
  <img src="https://i.imgur.com/OKDE67x.png" 
</p>

4. **Create a hosted zone with Route 53 for a custom domain and create an alias record with Cloudfront**


https://github.com/user-attachments/assets/bb49c1df-014c-41a7-8bc5-08faf7d91b37

<p align="center">
  <img src="https://i.imgur.com/OKDE67x.png" 
</p>
Even after creating the zone and alias record for the custom domain, it will show a 443 request error. We still need to request a certificate for our new  domain, as shown below:

5. **Requesting a  Public Certificate with Amazon Certificate Manager in order to resolve a HTTPS request with the custom domain**

<p align="center">
  <img src="https://i.imgur.com/OKDE67x.png" 
</p>


 ---

<h2>Conclusion</h2>
This projects demostrates a real-world scenario where we can create a website hosted with an S3 bucket utilizing AWS. In this example we also utilized .HTML and .CSS files to load our resume file into the bucket. By utilizing secure dns protocols and traffic through Route 53 and Cloudfront, we made sure that our website is fully compliant and accessible, as well as providing our own custom domain. This project was made with AWS free tier on all tools except for Route 53, where creating hosted zones has a cost as well. You can add a CNAME to a Cloudfront endpoint address using godaddy instead if you wish to cut on costs. Note that CNAMEs are not available at the root (apex) of the domain, so unless godaddy provides a CNAME flattening service (equivalent to Alias) you can only set it on a subdomain. There is also a cost in purchasing a third party domain or inside AWS. With this feature, you can utilize both without issues.
☁️
