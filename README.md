# 🚀 Elite DevOps Portfolio & Live Skill Tracker

<p align="center">
  <img src="https://img.shields.io/badge/🚀%20DevOps-Portfolio-blueviolet?style=for-the-badge">
  <img src="https://img.shields.io/badge/☁️%20Cloud-AWS-orange?style=for-the-badge&logo=amazonaws">
  <img src="https://img.shields.io/badge/🐳%20Docker-Container-blue?style=for-the-badge&logo=docker">
  <img src="https://img.shields.io/badge/⚙️%20Kubernetes-Orchestration-326CE5?style=for-the-badge&logo=kubernetes">
</p>

## 👨‍💻 About Me  
- Name: Paras Thakur  
- Education: B.Tech Computer Science  
- College: CGC Landran (CEC)  
- Focus: DevOps, Cloud, Kubernetes  

## 🌟 Project Overview  
This project is a full-stack DevOps dashboard built with cloud-native technologies. It showcases deployment skills, architecture design, and real-time insights.  

## 🏆 Cloud Achievements  
<p align="center">  
  <img src="https://img.shields.io/badge/Uptime-99.9%25-brightgreen?style=for-the-badge">  
  <img src="https://img.shields.io/badge/Performance-Optimized-blue?style=for-the-badge">  
  <img src="https://img.shields.io/badge/Kubernetes-Self--Healing-326CE5?style=for-the-badge">  
</p>  
After migrating to a professional **AWS Cloud** environment, I achieved the following results:

* **99.9% Uptime Engineering:** Implemented a **High-Availability** strategy with 2 active replicas. If one instance fails, Kubernetes automatically self-heals and restarts the pod.
    > <img width="929" height="273" alt="Screenshot 2026-03-20 221117" src="https://github.com/user-attachments/assets/bce769f7-afc5-4fdc-9277-56f4d8a1d95e" />


* **Resource Optimization:** Successfully resolved an **81% RAM bottleneck** by migrating from a t2.micro to a **t3.small (2GB RAM)** instance and tuning the K3s runtime for peak stability.
    > <img width="930" height="169" alt="Screenshot 2026-03-20 221144" src="https://github.com/user-attachments/assets/45b85c5a-3e24-4eb2-9b35-b97277794e14" />


* **Automation Impact:** Designed for 80% faster delivery cycles using CI/CD principles and **Infrastructure as Code (IaC)**.

---

## 💻 Local Setup (Docker)  
Run the following commands:  
`git clone https://github.com/paras-thakur/my-web-app.git`  
`cd my-web-app`  
`docker build -t skill-tracker-app .`  
`docker rm -f skill-tracker-app`  
`docker run -d -p 5000:5000 --name skill-tracker-app skill-tracker-app`  
Then open your browser to: http://localhost:5000  

## ☁️ Production Deployment (AWS + K3s)  
Install Kubernetes:  
`curl -sfL https://get.k3s.io | sh -`  
`sudo chmod 644 /etc/rancher/k3s/k3s.yaml`  
Deploy the app:  
`kubectl apply -f k8s/deployment.yaml`  
Access at: http://<YOUR_PUBLIC_IP>:5000  

## 🛠️ Tech Stack  
<p align="center">  
  <img src="https://skillicons.dev/icons?i=aws,docker,kubernetes,python,flask,sqlite" />  
</p>  
Tech stack includes AWS, Docker, Kubernetes (K3s), Python (Flask), and SQLite3.  

## 📈 DevOps Highlights  
- CI/CD ready architecture  
- Containerized microservices  
- Kubernetes auto-healing  
- Scalable cloud deployment  

## 📧 Connect With Me  
<p align="center">  
  <a href="#"><img src="https://img.shields.io/badge/LinkedIn-Connect-blue?style=for-the-badge&logo=linkedin"></a>  
  <a href="mailto:thakurparas330@gmail.com"><img src="https://img.shields.io/badge/Email-Contact-red?style=for-the-badge&logo=gmail"></a>  
</p>  

## 📸 Portfolio Showcase

<img width="1919" height="1030" alt="Screenshot 2026-03-20 011221" src="https://github.com/user-attachments/assets/2b048f4a-f3be-4c03-9bda-d43c23cfec88" />


## ⭐ Support  
- Star the repository  
- Fork the project  
- Share it with others  

## 🏁 Final Note  
This project demonstrates real-world DevOps and Cloud Engineering skills. Built as a Final Year Project at CGC Landran.  

<p align="center">  
  💡 Build • Deploy • Scale • Repeat  
</p>
