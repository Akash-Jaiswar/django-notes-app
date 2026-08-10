// @Library('Shared')_
// pipeline{
//     agent { label 'dev-server'}
    
//     stages{
//         stage("Code clone"){
//             steps{
//                 sh "whoami"
//             clone("https://github.com/LondheShubham153/django-notes-app.git","main")
//             }
//         }
//         stage("Code Build"){
//             steps{
//             dockerbuild("notes-app","latest")
//             }
//         }
//         stage("Push to DockerHub"){
//             steps{
//                 dockerpush("dockerHubCreds","notes-app","latest")
//             }
//         }
//         stage("Deploy"){
//             steps{
//                 deploy()
//             }
//         }
        
//     }
// }




@Library("Shared") _
pipeline {
    agent {label "vinod"}
    
    stages {
        
        stage("Hello") {
            steps {
                script{
                    hello()
                }
            }
        }
        
        stage("Code") {
            steps {
               script {
                clone("https://github.com/Akash-Jaiswar/django-notes-app.git", "main")
               }
            }
        }
        
        stage("Build") {
            steps {
                echo "This testing the code"
                sh "docker build -t notes-app:latest ."
            }
        }
        
        stage("Test") {
            steps {
                echo "This is testing the code"
            }
        }
        
        stage("Push to Dockerhub") {
            steps {
                 
                 script {
                    docker_push(
                        imageName: 'notes-app',
                        imageTag: 'latest',
                        credentials: 'dockerHubCred'
                    )
                }
            }
        }
        
        stage("Deploy") {
            steps {
                echo "This is deploying the code"
                sh "docker compose down && docker compose up -d"
            }    
        }
    }
}
