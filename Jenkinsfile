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
                echo 'Corriendo pruebas de software automáticas usando el entorno de desarrollo...'
                
                // Explicación técnica: Como el comando 'python3' no existe dentro del contenedor de Jenkins,
                // usamos el binario estático de Python para entornos embebidos si es necesario,
                // o forzamos la instalación rápida de Python dentro del contenedor usando los comandos nativos.
                
                sh '''
                    if ! command -v python3 &> /dev/null; then
                        echo "Instalando un entorno ligero de Python en el contenedor para la prueba..."
                        apt-get update && apt-get install -y python3
                    fi
                    python3 test_app.py
                '''
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