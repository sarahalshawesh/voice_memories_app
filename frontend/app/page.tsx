"use client";
import { useState, useRef} from "react";

export default function Home() {
  const [hasPermission, setHasPermission] = useState<boolean | null>(null);
  const [isRecording, setIsRecording] = useState(false);
  const [audioBlob, setAudioBlob] = useState<Blob | null>(null);
  const recorderRef = useRef<MediaRecorder | null>(null);
  const streamRef = useRef<MediaStream | null>(null);
  async function startRecording() {
    try {
      streamRef.current = await navigator.mediaDevices.getUserMedia({
        audio: true,
        video: false,
      });

      setHasPermission(true);
      const recorder = new MediaRecorder(streamRef.current);
      recorderRef.current = recorder;
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

     

    } catch (err) {
      console.error("Error accessing microphone:", err);
      setHasPermission(false);
    }
  }

  function stopRecording() {
    recorderRef.current?.stop();
    streamRef.current?.getTracks().forEach((track) => track.stop());
  }

  return (
    <main className="p-8">
      {!isRecording ? (
        <button
        onClick={startRecording}
        className="rounded bg-black px-4 py-2 text-white"
        >
        Record
      </button>
      ) : (
        <button
          onClick={stopRecording}
          className="rounded bg-black px-4 py-2 text-white"
        >
          Stop
        </button>
      )}
    </main>
  );
}