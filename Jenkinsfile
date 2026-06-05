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
            steps {
                echo 'Corriendo pruebas de software automáticas...'
                // Jenkins ejecuta la prueba de Python
                sh 'python3 test_app.py'
            }
        }
        stage('Desplegar en Producción (CD)') {
            steps {
                echo '¡Pruebas exitosas! Moviendo la aplicación al entorno de producción...'
                // Aquí iría el comando para empaquetar en Docker o subir a la nube
                echo 'Aplicación desplegada y operando al 100%.'
            }
        }
    }
}