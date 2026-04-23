"use client";
import { useState, useRef, useEffect} from "react";

export default function Home() {
  const [hasPermission, setHasPermission] = useState<boolean | null>(null);
  const [isRecording, setIsRecording] = useState(false);
  const [audioBlob, setAudioBlob] = useState<Blob | null>(null);
  const [audioURL, setAudioURL] = useState<string>("");
  const [isUploaded, setIsUploaded] = useState<boolean | null>(null);
  const recorderRef = useRef<MediaRecorder | null>(null);
  const streamRef = useRef<MediaStream | null>(null);
  const [personName, setPersonName] = useState<string>("");
  const [isNameStored, setIsNameStored] = useState<boolean>(false);
  const [isHomeScreen, setIsHomeScreen] = useState<boolean>(true);

  const prompts = [{promptId: 1, text: "Where were you when Zain was born?"}, {promptId: 2, text: "Who taught you to ride a bike?"}, {promptId: 3, text: "What's the furthest you've ever swam?"}, {promptId: 4, text: "What was your first job like?"}]

  const [currentPromptId, setCurrentPromptId] = useState<number>(0);
  // When Home first appears, check if a saved name exists in localStorage and put it into state
  useEffect (() => {
    const storedName = localStorage.getItem("personName");
    if (storedName) {
      setPersonName(storedName)
      setIsNameStored(true)
    }
  }, []);

  function changeScreen(selectedPromptId: number) {
    setIsHomeScreen(false)
    setCurrentPromptId(selectedPromptId)
  }


  // Adds name to localStorage 
  function storeName() {
    localStorage.setItem('personName', personName);
    setIsNameStored(true)
  }

  // When user types into the name bix, it's saved to personName
  function typeName(event: React.ChangeEvent<HTMLInputElement>) {
    setPersonName(event.target.value);
  }

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
    // Stores the recording audio in a form to be sent to the backend
    const formData = new FormData();
    formData.append("file", audioBlob, "recording.webm");
    formData.append("prompt_id", currentPromptId.toString());
    formData.append("person_name", personName);

    try {
      // POST request to send the recording audio form to the backend
      const res = await fetch("http://127.0.0.1:8000/upload/", {
        body: formData, 
        method: "POST"});
        // Log whether the POST request is successful or not and parse the json output
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
      {/* Home screen */}
      {isHomeScreen ? (
      <div>
      
        {/* If there is no name saved in localStorage, an input box for user to add name shows and a save button */}
        {!isNameStored ? (
        <div>
        <label>Enter your name:
            <input
              type="text" 
              value={personName}
              onChange={typeName}
            />
        </label>
        <button
          onClick={storeName}
          className="rounded bg-black px-4 py-2 text-white"
          >
          Save
        </button>
        </div>
          ) : (
        <label> 
          Hello {personName} 
          </label>)}
        <p></p>
        <ul>
          {prompts.map((prompt, index) => 
          <li key={index}>
            <button 
              onClick={() => changeScreen(prompt.promptId)}  
              className="rounded bg-black px-4 py-2 text-white"
              >
                {prompt.text} 
            </button>
          </li>)}
        </ul>
      </div>
      ) : (
        /* Prompt screen */ 
      <div>
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
        {/* If the audio has been created, the audio controls and messages appear */}
        { audioURL &&  (<audio controls src={audioURL}/>)}
        { audioURL && <p>Recording complete, press play to listen</p>}
        { audioBlob && <button onClick ={uploadRecording}>Save</button>}
        { isUploaded && <p>Recording uploaded</p>}
      </div>
      )}
    </main>
  );
}