pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Compilando / Preparando el código...'
                sleep 5
            }
        }
        stage('Test') {
            steps {
                echo 'Ejecutando pruebas básicas...'
                sleep 5
            }
        }
        stage('Analyze') {
            steps {
                echo 'Ejecutando análisis estático con SonarQube...'
                sleep 5
            }
        }
        stage('Security Test') {
            steps {
                echo 'Ejecutando OWASP Dependency-Check y OWASP ZAP...'
                sleep 5
            }
        }
        stage('Deploy') {
            steps {
                echo 'Desplegando la aplicación en entorno de prueba...'
                sleep 5
            }
        }
    }
}