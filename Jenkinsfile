pipeline {
    agent any

    tools {
        // Le dice a Jenkins que inyecte la herramienta que configuramos en el Paso 1
        python 'Python3'
    }

    stages {
        stage('Clonar y Verificar') {
            steps {
                echo 'Analizando los archivos del repositorio...'
                sh 'ls -la'
            }
        }
        stage('Ejecutar Pruebas (CI)') {
            steps {
                echo 'Corriendo pruebas de software automáticas con la herramienta nativa de Jenkins...'
                // Al usar la sección tools, el comando python ya estará disponible directamente
                sh 'python3 test_app.py'
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