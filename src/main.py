import chromadb
import asyncio
import os
import time

# Get Chroma DB connection details from environment variables
CHROMA_HOST = os.getenv("CHROMA_HOST", "localhost")
CHROMA_PORT = os.getenv("CHROMA_PORT", 8000)


async def main():
    print(f"Connecting to Chroma DB at {CHROMA_HOST}:{CHROMA_PORT}")

    # Sometimes it takes a moment for the Chroma container to be ready
    # Implement a simple retry mechanism
    client = None
    retries = 5
    while retries > 0:
        try:
            client = chromadb.HttpClient(host=CHROMA_HOST, port=8000)
            client.heartbeat()
            print("Successfully connected to Chroma DB!")
            break
        except Exception as e:
            print(f"Failed to connect to Chroma DB: {e}")
            retries -= 1
            time.sleep(2)

    if not client:
        print("Could not connect to Chroma DB after multiple retries. Exiting.")
        exit(1)


if __name__ == "__main__":
    asyncio.run(main())
