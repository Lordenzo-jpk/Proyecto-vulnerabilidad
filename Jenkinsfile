pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Compilando / preparando entorno...'
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
                echo 'Gestión de dependencias (simulada)...'
                echo 'pipenv graph ejecutado correctamente'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Desplegando aplicación en entorno de prueba (simulado)...'
            }
        }
    }
}