// shop-v2/firebase-config.js
// Firebase Konfiguration - aus der Console geholt
const firebaseConfig = {
  apiKey: "AIzaSyAyv3r-TC6cNuk9Dp655K79h2K4L-9tZAs",
  authDomain: "susibot-shop.firebaseapp.com",
  projectId: "susibot-shop",
  storageBucket: "susibot-shop.firebasestorage.app",
  messagingSenderId: "171492719283",
  appId: "1:171492719283:web:2f2053d340573d1f594ec6",
  measurementId: "G-M16BQETJWW"
};

// Initialisiere Firebase
import { initializeApp } from "firebase/app";
import { getAuth } from "firebase/auth";
import { getFirestore } from "firebase/firestore";

const app = initializeApp(firebaseConfig);
export const auth = getAuth(app);
export const db = getFirestore(app);