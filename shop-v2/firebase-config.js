// shop-v2/firebase-config.js
// Firebase Konfiguration - werde ich aus der Console holen

const firebaseConfig = {
  apiKey: "DEINE_API_KEY",
  authDomain: "susibot-shop.firebaseapp.com",
  projectId: "susibot-shop",
  storageBucket: "susibot-shop.appspot.com",
  messagingSenderId: "123456789",
  appId: "1:123456789:web:abc123"
};

// Initialisiere Firebase
import { initializeApp } from "firebase/app";
import { getAuth } from "firebase/auth";
import { getFirestore } from "firebase/firestore";

const app = initializeApp(firebaseConfig);
export const auth = getAuth(app);
export const db = getFirestore(app);