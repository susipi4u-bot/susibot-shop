#!/usr/bin/env node
// Script to add products to Firestore
// Run: node scripts/add-products-firestore.js

const { initializeApp } = require('firebase/data-connect');
const { getFirestore, collection, addDoc } = require('firebase/firestore');

const firebaseConfig = {
  apiKey: "AIzaSyAyv3r-TC6cNuk9Dp655K79h2K4L-9tZAs",
  authDomain: "susibot-shop.firebaseapp.com",
  projectId: "susibot-shop",
  storageBucket: "susibot-shop.firebasestorage.app",
  messagingSenderId: "171492719283",
  appId: "1:171492719283:web:2f2053d340573d1f594ec6"
};

// Produkte mit ausführlichen Details
const products = [
  {
    id: "serverwatch",
    name: "ServerWatch",
    price: 14.99,
    desc: "Umfassendes Server-Monitoring-Tool",
    features: [
      "Echtzeit CPU-, RAM- und Disk-Überwachung",
      "Benachrichtigungen bei临界 Werten",
      "Web-Dashboard mit Grafiken",
      "Historisches Daten-Logging"
    ],
    system: "Linux (Ubuntu, Debian, CentOS, Raspberry Pi OS)",
    requirements: "Python 3.8+, 100MB RAM, Netzwerkzugang",
    installation: "pip install serverwatch",
    support: "Email-Support inklusive",
    version: "1.0.0"
  },
  {
    id: "pistats",
    name: "PiStats",
    price: 4.99,
    desc: "Raspberry Pi System-Monitoring",
    features: [
      "CPU-Temperatur und -Takt",
      "RAM- und Speichernutzung",
      "Network Traffic Analyse",
      "GPIO-Status Überwachung",
      "Web-Interface mit Live-Daten"
    ],
    system: "Raspberry Pi (alle Modelle mit Raspberry Pi OS)",
    requirements: "Python 3.5+, Raspberry Pi",
    installation: "curl -s https://raw.githubusercontent.com/susipi4u/pistats/install.sh | bash",
    support: "Community-Support",
    version: "2.1.0"
  },
  {
    id: "autobackup",
    name: "AutoBackup",
    price: 4.99,
    desc: "Automatische Backup-Lösung",
    features: [
      "Planbare Backup-Zeiten",
      "Incremental Backups",
      "Remote-Backup zu S3/Google Drive",
      "Komprimierung und Verschlüsselung",
      "Backup-Verification"
    ],
    system: "Linux, macOS, BSD",
    requirements: "Python 3.6+, crontab",
    installation: "pip install autobackup-pro",
    support: "Email-Support",
    version: "3.0.1"
  },
  {
    id: "healthcheck",
    name: "HealthCheck",
    price: 9.99,
    desc: "Server Health Monitoring Suite",
    features: [
      "Service-Status Prüfung (HTTP, SSH, MySQL, etc.)",
      "SSL-Zertifikat Monitoring",
      "DNS-Checker",
      "Port-Scanner",
      "Automatisierte Remediation-Scripts"
    ],
    system: "Linux Server, VPS, Cloud-Instanzen",
    requirements: "Python 3.8+, Root-Zugriff für einige Features",
    installation: "pip install healthcheck-pro",
    support: "Priority Email-Support",
    version: "1.5.0"
  },
  {
    id: "docker-manager",
    name: "Docker Manager",
    price: 9.99,
    desc: "Docker Container Management",
    features: [
      "Container-Überwachung",
      "Auto-Restart bei Ausfällen",
      "Resource-Limit Management",
      "Log-Aggregation",
      "Backup und Restore von Volumes"
    ],
    system: "Linux mit Docker installiert",
    requirements: "Docker 20.10+, Python 3.8+",
    installation: "docker run -d -v /var/run/docker.sock:/var/run/docker.sock susipi4u/docker-manager",
    support: "Email + Docker Hub Support",
    version: "2.0.0"
  },
  {
    id: "network-scanner",
    name: "Network Scanner",
    price: 7.99,
    desc: "Netzwerk-Scanner und Analyzer",
    features: [
      "IP-Scan im lokalen Netzwerk",
      "Offene Ports erkennen",
      "Gerätetyp-Erkennung",
      "Netzwerk-Latenz Monitoring",
      "Subnetz-Analyse"
    ],
    system: "Linux, macOS, Windows (WSL)",
    requirements: "Python 3.6+, Nmap (optional)",
    installation: "pip install net-scan-pro",
    support: "Community-Support",
    version: "1.2.0"
  },
  {
    id: "logwatcher",
    name: "LogWatcher",
    price: 6.99,
    desc: "Intelligent Log Monitoring",
    features: [
      "Echtzeit Log-Überwachung",
      "Pattern-Matching und Alerts",
      "Fehler-Erkennung und Kategorisierung",
      "Log-Rotation Support",
      "Export zu Elasticsearch"
    ],
    system: "Linux Server, Docker",
    requirements: "Python 3.7+",
    installation: "pip install logwatcher-pro",
    support: "Email-Support",
    version: "1.8.0"
  },
  {
    id: "passgen",
    name: "PassGen Pro",
    price: 4.99,
    desc: "Professioneller Passwort-Generator",
    features: [
      "Kryptographisch sichere Zufallszahlen",
      "Anpassbare Komplexität",
      "Passwort-Stärke-Analyse",
      "CLI und Web-Interface",
      "Passwort-Vault Integration"
    ],
    system: "Cross-Platform (Linux, macOS, Windows)",
    requirements: "Python 3.6+",
    installation: "pip install passgen-pro",
    support: "Community-Support",
    version: "2.0.0"
  }
];

console.log('Produkte werden zu Firestore hinzugefügt...');
console.log('Achtung: Dies erfordert Firebase Admin SDK mit Service Account.');
console.log('');
console.log('Da wir keinen Service Account haben, erstelle ich eine JSON-Datei');
console.log('die du manuell importieren oder mir geben kannst.');
console.log('');

console.log(JSON.stringify(products, null, 2));