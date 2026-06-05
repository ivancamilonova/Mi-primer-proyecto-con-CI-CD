pipeline {
    agent any

    stages {
        stage('Clonar y Verificar') {
            steps {
                echo 'Analizando los archivos del repositorio...'
                sh 'ls -la'
            }
        }
        stage('Ejecutar Pruebas (CI)') {
            agent {
                // Le dice a Jenkins: "Baja una imagen oficial de Python aislada para correr esta prueba"
                docker { image 'python:3.10-slim' }
            }
            steps {
                echo 'Corriendo pruebas de software automáticas dentro de un entorno aislado de Python...'
                sh 'python test_app.py'
            }
        }
        stage('Desplegar en Producción (CD)') {
            steps {
                echo '¡Pruebas exitosas! Moviendo la aplicación al entorno de producción...'
                echo 'Aplicación desplegada y operando al 100%.'
            }
        }
    }
}