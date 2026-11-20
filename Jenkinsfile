pipeline {
    agent {
        docker { image 'python:3.9-slim' } 
    }

    stages {
        stage('Build') {
            steps {
                echo 'Compilando / preparando entorno...'
                sh 'pip install --upgrade pip'
            }
        }
        stage('Test') {
            steps {
                echo 'Ejecutando pruebas...'
                
            }
        }
        stage('Analyze') {
            steps {
                echo 'Análisis de calidad de código...'
            }
        }
        stage('Dependency Management') {
            steps {
                
                sh 'pip install pipenv' 
                sh 'pipenv install'
                sh 'pipenv update'
                sh 'pipenv graph'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Desplegando aplicación en entorno de prueba (simulado)...'
            }
        }
    }
}