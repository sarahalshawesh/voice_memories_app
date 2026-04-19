"use client";
import { useState, useRef} from "react";

export default function Home() {
  const [hasPermission, setHasPermission] = useState<boolean | null>(null);
  const [isRecording, setIsRecording] = useState(false);
  const [audioBlob, setAudioBlob] = useState<Blob | null>(null);
  const [audioURL, setAudioURL] = useState<string>("");
  const [isUploaded, setIsUploaded] = useState<boolean | null>(null)
  const recorderRef = useRef<MediaRecorder | null>(null);
  const streamRef = useRef<MediaStream | null>(null);


  // function that starts the recorder and handles on stop logic.
  // asynchronous as it waits for a Promise for microphone access
  async function startRecording() {
    try {
      // asks web browser for permission to access microphone
      streamRef.current = await navigator.mediaDevices.getUserMedia({
        audio: true,
        video: false,
      });

      setHasPermission(true);
      // Creates the recorder and an array to collect recorded audio chunks
      const recorder = new MediaRecorder(streamRef.current);
      recorderRef.current = recorder;
      const audioChunks: Blob[] = [];

      // During recording audio chunks are saved as they become available
      recorder.ondataavailable = (event) => { 
        audioChunks.push(event.data);
      };
      
      // Logic for when the recording stops. Ends recording and resets flag for IsRecording
      // Audio chunks are combined and an object URL is created for playback
      recorder.onstop = () => {
        const finalBlob = new Blob(audioChunks, { type: recorder.mimeType });
        setAudioBlob(finalBlob);
        setAudioURL(URL.createObjectURL(finalBlob))
        setIsRecording(false);
        console.log("Recording stopped");
      };
      
      recorder.start();
      setIsUploaded(false)
      setAudioBlob(null)
      setAudioURL("")
      setIsRecording(true);
      console.log("Recording started");

     
    // Updates permission state to false if there's an error with microphone access.
    } catch (err) {
      console.error("Error accessing microphone:", err);
      setHasPermission(false);
    }
  }

  // function that stops the recorder and streams 
  function stopRecording() {
    recorderRef.current?.stop();
    streamRef.current?.getTracks().forEach((track) => track.stop());
  }

  // function that uploads the recording to the backend
  async function uploadRecording() {
    if (!audioBlob) return;
    const formData = new FormData();
    formData.append("recording", audioBlob);
      
    try {
      const res = await fetch("http://127.0.0.1:8000/upload", {
        body: formData, 
        method: "POST"});
        if (res.ok) {
          setIsUploaded(true)
          console.log("Save successful", res.status)
          const parsedRes = await res.json()
          console.log(parsedRes)
        } else {
          setIsUploaded(false)
          console.log("Save failed", res.status)
        }
        
    } catch (err) {
      console.error("Error posting audio", err);
      setIsUploaded(false)
    }
  }
  

  return (
    <main className="p-8">
      {/* Logic for button switch between Record and Stop */}
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
      {/* If the audio URL has been created, the audio controls and a message appear */}
      { audioURL &&  (<audio controls src={audioURL}/>)}
      { audioURL && <p>Recording complete, press play to listen</p>}
      { audioBlob && <button onClick ={uploadRecording}>Save</button>}
      { isUploaded && <p>Recording uploaded</p>}

    </main>
  );
}