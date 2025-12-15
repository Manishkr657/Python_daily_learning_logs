import docker

CLIENT = docker.from_env()

IMAGE_NAME = "ubuntu:latest"
COMMAND_TO_RUN = "echo Hello from container"

try:
    container = CLIENT.containers.run(
        image=IMAGE_NAME,
        command=COMMAND_TO_RUN,
        name="My_first_container",
        detach=True,
        tty=True
    )

    print(f"Container started successfully with name '{container.name}' and ID '{container.id}'")

    container.wait()

    logs = container.logs().decode()
    print("Container output:\n", logs)

    container.remove()
    print("Container removed successfully.")

except docker.errors.ImageNotFound:
    print(f"Error: Image '{IMAGE_NAME}' not found. Pull it first using 'docker pull {IMAGE_NAME}'.")

except docker.errors.ContainerError as e:
    print(f"Error starting container: {e}")

except docker.errors.APIError as e:
    print(f"Docker API error: {e}")

except Exception as e:
    print(f"An unexpected error occurred: {e}")
