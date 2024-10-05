# My Python Library

Welcome to the Python library that allows you to create simple yet powerful graphical applications using basic concepts such as windows, entities, and components. This library is designed to be easy to use and extend, enabling you to quickly build 3D applications.

## Installation

To install this library, clone this repository and install the required dependencies. Ensure you have Python 3.x installed on your machine.

```bash
git clone https://github.com/your-username/repo-name.git
cd repo-name
pip install -r requirements.txt
```

## Usage

Here’s a sample code snippet to help you get started with your library:

```python
from app import App, Window
from components import Material, Mesh
from entity import Entity
from vector import Vector3

if __name__ == '__main__':
    # Create windows
    window = Window()
    window2 = Window()
    app = App()

    # Define a mesh for a cube
    mesh = Mesh([
        Vector3(-0.5, -0.5, -0.5), Vector3(0.5, -0.5, -0.5),
        Vector3(0.5, 0.5, -0.5), Vector3(-0.5, 0.5, -0.5),
        Vector3(-0.5, -0.5, 0.5), Vector3(0.5, -0.5, 0.5),
        Vector3(0.5, 0.5, 0.5), Vector3(-0.5, 0.5, 0.5)
    ])

    # Create a material for the cube
    cube_material = Material(diffuse=[1.0, 0.0, 0.0, 1.0], shininess=[50.0])

    # Create an entity for the cube and add components to it
    cube_entity = Entity()
    cube_entity.add_component(cube_material)
    cube_entity.add_component(mesh)

    # Define update events
    @app.event
    def update(dt):
        print(1/dt)

    @app.event
    def fixed_update(fixed_dt):
        print(1/fixed_dt)

    @window.event
    def on_draw():
        window.clear()

    # Run the application
    app.run()
```

## Features

- **Window Management**: Create multiple windows for your application.
- **Components**: Add components such as materials and meshes to entities.
- **Entities**: Manage your game objects using an entity-component system.
- **Events**: Define events to update and draw your objects.

## Contribution

Contributions are welcome! If you would like to contribute to this library, feel free to open a pull request or report an issue.
