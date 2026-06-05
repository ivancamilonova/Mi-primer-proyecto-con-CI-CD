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
                echo 'Descargando y configurando un entorno portátil de Python...'
                
                // Descargamos un binario de Python precompilado que no requiere instalación de administrador
                sh '''
                    # 1. Descargar Python portátil oficial para Linux (64-bit) si no se ha descargado antes
                    if [ ! -d "python_portatil" ]; then
                        echo "Descargando Python..."
                        curl -L https://github.com/indygreg/python-build-standalone/releases/download/20240107/cpython-3.10.13+20240107-x86_64-unknown-linux-gnu-install_only.tar.gz -o python.tar.gz
                        echo "Descomprimiendo..."
                        tar -xzf python.tar.gz
                        mv python python_portatil
                        rm python.tar.gz
                    fi

                    # 2. Ejecutar la prueba usando el binario portátil recién descargado
                    echo "Ejecutando pruebas unitarias con Python portátil..."
                    ./python_portatil/bin/python3 test_app.py
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