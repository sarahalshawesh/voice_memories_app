"use client";

export default function Home() {
  async function getMedia() {
    try {
      const stream = await navigator.mediaDevices.getUserMedia({
        audio: true,
        video: false,
      });

      const recorder = new MediaRecorder(stream);
      recorder.start();
      console.log("Recording started");

      setTimeout(() => {
        recorder.stop();
        console.log("Recording stopped");

        stream.getTracks().forEach((track) => track.stop());
      }, 5000);
    } catch (err) {
      console.error("Error accessing microphone:", err);
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