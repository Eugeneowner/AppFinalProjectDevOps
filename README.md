# Final Project

## Задание

1. Create GitHub repo with:
 → test python backend server. Just script which listening on some port and respond 200 on /
 → Dockerfile with everything needed to run this script
 → GitHub action which will build docker image automatically and push to docker hub. Use Github secrets to store your docker hub creds
2. Use terraform code to create EKS cluster `(https://gitlab.com/dan-it/groups/devops_soft/-/tree/main/step-final/EKS?ref_type=heads)`.
 → one node group with one node
 → nginx ingress controller
3. Write terraform code which will install ArgoCD to EKS using helm chart or raw k8s manifest
 → argocd must have dns name in domain: devops1.test-danit.com (change devops1 to your group number) example: argocd.student1.devops1.test-danit.com where student1 is your cluster name.
4. Write K8S manifests to deploy your app from item 1 to EKS.
 → deployment, service, ingress.
 → app must be available by dns name in domain: devops1.test-danit.com (change devops1 to your group number) example: app.student1.devops1.test-danit.com
5. Write ArgoCD app which will deliver code from item 4 to EKS and will update it on new commit.

1. Build docker image for nodejs app located here:

2. Prepare docker-compose file and run EFK stack using it.
3. Run nodejs app in docker and configure it to send logs to EFK stack.
4. Make sure that you can see logs in Kibana

Формат здачі ДЗ:
1. → Код Dockerfile
2. → Код docker-compose.yaml
3. → Код файлів конфігурації
4. → Скріни запуску й роботи EFK
5. → Скріни роботи Kibana

## 🎯 Цель проекта 🚀 Final DevOps Project

Развернуть полностью работоспособную инфраструктуру в AWS с помощью Terraform, Helm и ArgoCD, включающую:
	•	EKS кластер (Kubernetes),
	•	установку NGINX Ingress Controller,
	•	автоматическое получение TLS-сертификатов через cert-manager и Let’s Encrypt,
	•	настройку ExternalDNS для работы с Route53 и публичным DNS,
	•	установку ArgoCD через Helm и деплой приложения через ArgoCD,
	•	поддержку CI/CD пайплайна через GitHub Actions и Docker Hub.

📌 Описание
Этот проект демонстрирует полный цикл CI/CD-подхода с развёртыванием отказоустойчивого приложения в AWS EKS с использованием инфраструктуры как кода (IaC), Helm, ArgoCD и автоматической настройкой DNS и TLS-сертификатов через ExternalDNS и cert-manager.

🧰 Используемые технологии
	•	Terraform — для создания инфраструктуры в AWS
	•	AWS EKS — Kubernetes-кластер
	•	Helm — шаблонизация Kubernetes-манифестов
	•	ArgoCD — GitOps-деплоймент
	•	Docker — контейнеризация приложения
	•	GitHub Actions — CI для сборки и публикации образов CI/CD через GitHub Actions
  •	DockerHub 
	•	ExternalDNS — автоматическая регистрация DNS-записей в Route53
	•	cert-manager + Let’s Encrypt — автоматическая генерация TLS-сертификатов
	•	NGINX Ingress Controller — точка входа в кластер
  •	DNS *.devops1.test-danit.com

  - **Infrastructure as Code:** Terraform
  - **Kubernetes:** EKS (Amazon Elastic Kubernetes Service)
  - **Deployment:** ArgoCD
  - **Ingress Controller:** NGINX
  - **CI/CD:** GitHub Actions
  - **Container Registry:** DockerHub
  - **TLS & HTTPS:** Let's Encrypt via cert-manager
  - **DNS:** `*.devops1.test-danit.com`
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ## Корень проекта
  ```bash
  .
  ├── app/                            # Backend-приложение на Python (FastAPI)
  ├── EKS/                            # Все Terraform-ресурсы для AWS
  │   ├── modules/eks-external-dns/
  │   │   ├── helm/                   # Helm-чарты для ArgoCD Application
  │   │   └── *.tf                    # Модули инфраструктуры
  │   └── *.tf                        # Основные Terraform-ресурсы (EKS, ACM, DNS и т.д.)
  ├── k8s/                            # Kubernetes-манифесты (ingress, deployment)
  ├── .github/workflows/              # GitHub Actions CI/CD
  ├── terraform.tfvars                # Значения переменных Terraform
  ├── task.md                         # Условие задания
  └── README.md                       # Этот файл
  ```

## 🔧 Stack / Структура проекта 

  Файл          Назначение
  
  provider.tf - Подключение к AWS с указанием региона и профиля

  terraform.tfvars - Значения переменных: домен, регион, имена кластеров, количество узлов и т.д.

  variables.tf - Объявление всех переменных для конфигурации

  backend.tf - Настройка удаленного backend-а в S3 для хранения состояния Terraform

  eks-cluster.tf - Создание самого EKS-кластера

  eks-worker-nodes.tf - Создание node group (EC2 инстансы — worker-нодов)

  sg.tf - Security Groups: открытие портов для k8s, SSH, ArgoCD и т.п.

  iam.tf - IAM-политики и роли для EKS, worker-нодов и внешних сервисов

  metrics-server.tf - Установка metrics-server (для HPA и мониторинга нагрузки)

  ingress_controller.tf - Установка NGINX Ingress Controller в кластер

  external-dns.tf - Подключение ExternalDNS для автоматического управления DNS-записями в Route53

  acm.tf - Подключение cert-manager, выпуск Let’s Encrypt сертификатов


  ## Папка modules/eks-external-dns

  Файл          Назначение

  argo.tf - Установка ArgoCD с помощью Helm

  argo-helm.tf - Описание Helm chart для приложения, которое будет деплоиться через ArgoCD

  helm.tf - Общая конфигурация Helm provider

  iam.tf - IAM роли и привязки для работы Helm/ArgoCD с AWS

  values.tf, variables.tf, locals.tf, outputs.tf - Работа с переменными и выводами в модуле

  helm/argocd-application/ - Helm Chart приложения (Chart.yaml, templates, values.yaml)

  examples/basic/ - Пример использования модуля с минимальной конфигурацией

🧱 ArgoCD и Helm
	•	ArgoCD установлен через Helm в namespace argocd, автоматически запускается с использованием Helm chart.
	•	Приложение, которое деплоится через ArgoCD, определено как Helm chart в helm/argocd-application/.
	•	Это приложение отображает красивую страницу с IP, временем суток, emoji и включает dark/light toggle.

⸻

🔐 HTTPS и DNS
	•	Используется cert-manager и ClusterIssuer letsencrypt-prod для автоматического выпуска сертификатов.
	•	ExternalDNS следит за Ingress и обновляет записи в Route53.
	•	Ingress.yaml настроен с аннотациями для HTTPS, автоперенаправлением с HTTP и ссылкой на TLS secret.

  ✅ Презентации
	1.	Цель проекта: автоматизация деплоя инфраструктуры с HTTPS и CI/CD.
	2.	Выбор инструментов: Terraform для IaC, Helm для шаблонизации, ArgoCD для GitOps, cert-manager + ExternalDNS для удобства и безопасности.
	3.	Архитектура:
	•	EKS кластер
	•	ArgoCD + Helm + Ingress + cert-manager
	•	Приложение как Helm chart
	4.	TLS + DNS: сертификация через Let’s Encrypt, DNS обновляется автоматически.
	5.	CI/CD: при пуше в GitHub обновляется DockerHub-образ и ArgoCD автоматически деплоит новую версию.
	6.	UI: веб-интерфейс приложения визуально оформлен, есть динамика по времени суток, emoji, IP отображение и здоровье системы.

 ## Установка и запуск

 1. Клонирование репозитория

  git clone `https://gitlab.com/dan-it/groups/devops_soft/-/tree/main/step-final/EKS?ref_type=heads`
  cd final-devops-project

2. Инициализация Terraform

  cd EKS
  terraform init
  terraform fmt
  terraform validate
  terraform plan
  terraform apply

  Убедитесь, что указан backend S3 и используется AWS CLI профиль с MFA (например, mfa)

3. Развёртывание ArgoCD и Helm-чартов

  cd modules/eks-external-dns/examples/basic
  terraform init
  terraform fmt
  terraform validate
  terraform plan
  terraform apply

 Доступ к ArgoCD UI
	•	URL: https://argocd.devops1.test-danit.com
	•	Пользователь: admin
	•	Пароль:

  kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d

  🌐 DNS и HTTPS
	•	DNS автоматически настраивается через ExternalDNS в зоне *.devops1.test-danit.com
	•	TLS-сертификаты выдаются cert-manager с ClusterIssuer letsencrypt-prod


  📦 CI/CD
	•	GitHub Actions:
	•	Автоматическая сборка Docker-образа
	•	Публикация в Docker Hub
	•	Обновление Helm values.yaml
	•	ArgoCD подтягивает изменения и развёртывает в кластер

  🧪 Проверка

  curl https://app.eugeneowner.devops7.test-danit.com

  📄 Требования
  •	AWS CLI с настроенным профилем
	•	Terraform ≥ 1.3
	•	kubectl + kubeconfig
	•	Helm ≥ 3
	•	Docker
	•	Доступ к приватному DockerHub-репозиторию

  🔒 Безопасность
	•	MFA для AWS CLI
	•	TLS от Let’s Encrypt
	•	Доступ к ArgoCD через HTTPS и пароль
	•	Изоляция пространств имён (argocd, backend)


  📦 Helm Chart и ArgoCD манифесты

Проект использует Helm-чарт для описания ArgoCD Application, которое автоматически разворачивает backend-приложение на основе GitOps-подхода.

📁 Структура Helm-чарта

Путь: modules/eks-external-dns/helm/argocd-application/

🔧 Базовые команды:

  Команда          Назначение

  terraform init - Инициализирует рабочую директорию, загружает плагины, backend, модули

  terraform plan - Показывает, какие изменения будут внесены

  terraform apply - Применяет изменения к инфраструктуре

  terraform destroy - Полностью удаляет созданную инфраструктуру

  terraform validate - Проверяет синтаксис и структуру Terraform-конфигурации 

  terraform fmt - Автоматически форматирует .tf файлы по стандарту

  terraform output - Показывает выходные значения (output) после apply

  terraform show - Показывает текущее состояние инфраструктуры (читаемый формат)

  terraform state - Управление локальным state-файлом (в т.ч. просмотр, перемещение, удаление ресурсов)

  terraform import - Импортирует уже существующие ресурсы в Terraform state

  terraform taint - Помечает ресурс как “испорченный” → он будет пересоздан при следующем apply

  terraform untaint - Убирает пометку “taint” с ресурса

  terraform graph - Создаёт граф зависимостей ресурсов (в формате DOT)


  🧪 Расширенные и менее известные команды:

  Команда               Назначение
  
  terraform providers - Показывает, какие провайдеры используются и их зависимости

  terraform console - Открывает интерактивную консоль Terraform (полезна для отладки выражений)

  erraform login - Аутентификация в Terraform Cloud (если используешь его)

  terraform state list - Список всех ресурсов в state-файле

  terraform state show <resource> - Подробная информация по конкретному ресурсу

  terraform state rm <resource> - Удаление ресурса из state-файла (без удаления из облака)

  terraform state mv - Перемещение ресурса в state-файле (например, при смене имени)



