package main

import (
  "fmt"
  "net/http"
)

func handler(w http.ResponseWriter, r *http.Request) {
  fmt.Fprintf(w, "¡Hola, aplicación Go Dockerizada!")
}

func main() {
  http.HandleFunc("/", handler)
  fmt.Println("El servidor se está ejecutando en el puerto 8000")
  http.ListenAndServe(":8000", nil)
}
