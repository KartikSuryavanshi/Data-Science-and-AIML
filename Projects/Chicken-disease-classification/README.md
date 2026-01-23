# Chicken Disease Classification

A deep learning project for classifying chicken diseases using Convolutional Neural Networks (CNN). This project uses transfer learning to detect Coccidiosis and identify Healthy chickens from fecal images.

## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Development Workflow](#development-workflow)
- [DVC Commands](#dvc-commands)
- [Deployment](#deployment)

## Features

- **Deep Learning Classification**: Uses pretrained CNN models for disease detection
- **Transfer Learning**: Leverages base models for improved accuracy
- **Automated Pipeline**: DVC-based reproducible pipeline
- **Web Interface**: Flask-based application for predictions
- **CI/CD Ready**: GitHub Actions integration for AWS and Azure deployment

## Project Structure

```
├── src/
│   └── cnn_image_classification/
│       ├── components/          # Pipeline components
│       ├── config/              # Configuration management
│       ├── constants/           # Constants and configurations
│       ├── entity/              # Data entity definitions
│       ├── pipeline/            # ML pipeline stages
│       └── utils/               # Utility functions
├── artifacts/                   # Generated models and data
│   ├── data_ingestion/          # Ingested dataset
│   ├── prepare_base_model/      # Base model files
│   ├── prepare_callbacks/       # Callbacks and logs
│   └── training/                # Trained model
├── research/                    # Jupyter notebooks for experimentation
├── config/                      # YAML configuration files
├── app.py                       # Flask web application
├── main.py                      # Main execution script
├── dvc.yaml                     # DVC pipeline definition
├── params.yaml                  # Pipeline parameters
└── requirements.txt             # Python dependencies
```

## Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/KartikSuryavanshi/Chicken-disease-classification.git
cd Chicken-disease-classification
```

### Step 2: Create Conda Environment

```bash
conda create -n cnncls python=3.8 -y
conda activate cnncls
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

## Usage

### Running the Web Application

```bash
python app.py
```

Open your browser and navigate to `http://localhost:5000` to access the application.

### Running the Pipeline

```bash
python main.py
```

## Development Workflow

Follow these steps when making changes to the project:

1. Update `config/config.yaml` - Configuration parameters
2. Update `params.yaml` (optional) - Pipeline parameters
3. Update `secrets.yaml` (optional) - Sensitive information
4. Update entity classes in `src/cnn_image_classification/entity/`
5. Update configuration manager in `src/cnn_image_classification/config/`
6. Update components in `src/cnn_image_classification/components/`
7. Update pipeline stages in `src/cnn_image_classification/pipeline/`
8. Update `main.py` - Main execution script
9. Update `dvc.yaml` - DVC pipeline definition

## DVC Commands

```bash
# Initialize DVC
dvc init

# Run the entire pipeline
dvc repro

# View pipeline DAG
dvc dag
```

## Deployment

### AWS Deployment with GitHub Actions

#### Prerequisites

1. **AWS Account & IAM User**
   - Create an IAM user with the following permissions:
     - `AmazonEC2ContainerRegistryFullAccess`
     - `AmazonEC2FullAccess`

2. **Create ECR Repository**
   - Save your ECR URI (example: `566373416292.dkr.ecr.us-east-1.amazonaws.com/chicken`)

3. **Launch EC2 Instance**
   - Use Ubuntu OS for better Docker compatibility

4. **Install Docker on EC2**

   ```bash
   # Optional updates
   sudo apt-get update -y
   sudo apt-get upgrade

   # Install Docker
   curl -fsSL https://get.docker.com -o get-docker.sh
   sudo sh get-docker.sh
   sudo usermod -aG docker ubuntu
   newgrp docker
   ```

5. **Configure Self-Hosted Runner**
   - Go to: Settings > Actions > Runners > New self-hosted runner
   - Follow the on-screen instructions for your OS

6. **Set GitHub Secrets**

   Add the following secrets to your GitHub repository:

   ```
   AWS_ACCESS_KEY_ID: <your-access-key>
   AWS_SECRET_ACCESS_KEY: <your-secret-key>
   AWS_REGION: us-east-1
   AWS_ECR_LOGIN_URI: <your-ecr-uri>
   ECR_REPOSITORY_NAME: chicken
   ```

### Azure Deployment with GitHub Actions

#### Build and Push Docker Image

```bash
# Build Docker image
docker build -t chickenapp.azurecr.io/chicken:latest .

# Login to Azure Container Registry
docker login chickenapp.azurecr.io

# Push image
docker push chickenapp.azurecr.io/chicken:latest
```

#### Deployment Steps

1. Build Docker image of the source code
2. Push Docker image to Azure Container Registry
3. Launch Web App Server in Azure
4. Pull Docker image from container registry to Web App server
5. Run the container on Web App server

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss proposed changes.
