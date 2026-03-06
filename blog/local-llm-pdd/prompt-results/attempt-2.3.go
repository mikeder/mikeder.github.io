package main

import (
	"image/color"
	"math"

	raylib "github.com/gen2brain/raylib-go/raylib"
)

func main() {
	// Initialize raylib
	raylib.InitWindow(800, 600, "Raylib Shader Example")
	defer raylib.CloseWindow()

	// Create vertex shader
	// 	vertexShaderSource := `
	// #version 330 core
	// layout (location = 0) in vec3 aPos;
	// void main()
	// {
	//    gl_Position = vec4(aPos, 1.0);
	// }
	// `

	// 	// Create fragment shader
	// 	fragmentShaderSource := `
	// #version 330 core
	// out vec4 FragColor;
	// void main()
	// {
	//    FragColor = vec4(1.0f, 0.5f, 0.2f, 1.0f);
	// }
	// `

	// Create shader
	// shader := raylib.LoadShaderCode(vertexShaderSource, fragmentShaderSource)

	// Main loop
	for !raylib.WindowShouldClose() {
		// Clear the screen
		raylib.BeginDrawing()
		raylib.ClearBackground(raylib.Blue)
		// raylib.EnableShader(shader)
		// Draw the triangle
		raylib.DrawTriangle3D(
			raylib.Vector3{X: -0.5, Y: -0.5, Z: 0},
			raylib.Vector3{X: 0.5, Y: -0.5, Z: 0},
			raylib.Vector3{X: 0, Y: 0.5, Z: 0},
			color.RGBA{math.MaxUint8, 100, 100, math.MaxUint8},
		)

		raylib.EndDrawing()
	}
}
