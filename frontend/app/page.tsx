"use client";
import { useState } from "react";

export default function Home() {
  const [hasPermission, setHasPermission] = useState<boolean | null>(null);
  const [isRecording, setIsRecording] = useState(false);
  const [audioBlob, setAudioBlob] = useState<Blob | null>(null);
  async function getMedia() {
    try {
      const stream = await navigator.mediaDevices.getUserMedia({
        audio: true,
        video: false,
      });

      setHasPermission(true);

      const recorder = new MediaRecorder(stream);
      const audioChunks: Blob[] = [];

      
      recorder.ondataavailable = (event) => { 
        audioChunks.push(event.data);
      };
      
      recorder.onstop = () => {
        const finalBlob = new Blob(audioChunks, { type: recorder.mimeType });
        setAudioBlob(finalBlob);
        setIsRecording(false);
        console.log("Recording stopped");
      };
      
      recorder.start();
      setIsRecording(true);
      console.log("Recording started");

      setTimeout(() => {
        recorder.stop();
        stream.getTracks().forEach((track) => track.stop());
      }, 5000);
    } catch (err) {
      console.error("Error accessing microphone:", err);
      setHasPermission(false);
    }
  }

  return (
    <main className="p-8">
      <button
        onClick={getMedia}
        className="rounded bg-black px-4 py-2 text-white"
      >
        Test microphone
      </button>
    </main>
  );
}