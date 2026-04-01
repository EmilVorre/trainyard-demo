package main

import (
	"fmt"
	"net/http"
	"os"
)

func main() {
	port := os.Getenv("PORT")
	if port == "" {
		port = "3000"
	}

	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		hostname, _ := os.Hostname()
		fmt.Fprintf(w, `<!DOCTYPE html>
<html>
<head>
  <title>Trainyard Demo</title>
  <style>
    body {
      font-family: monospace;
      background: #0d1117;
      color: #c9d1d9;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
      margin: 0;
    }
    .card {
      border: 1px solid #30363d;
      border-radius: 8px;
      padding: 2rem 3rem;
      text-align: center;
      max-width: 500px;
    }
    h1 { color: #58a6ff; font-size: 2rem; }
    .tag {
      display: inline-block;
      background: #21262d;
      border: 1px solid #30363d;
      border-radius: 4px;
      padding: 0.2rem 0.6rem;
      font-size: 0.85rem;
      margin: 0.2rem;
    }
    .green { color: #3fb950; }
  </style>
</head>
<body>
  <div class="card">
    <h1>Trainyard</h1>
    <p class="green">Preview environment is live</p>
    <p>This environment was automatically deployed by Trainyard when the <span class="tag">preview</span> label was applied to the pull request.</p>
    <hr style="border-color:#30363d; margin: 1.5rem 0"/>
    <p><span class="tag">host: %s</span></p>
    <p style="color:#8b949e; font-size:0.8rem">It will be torn down when the label is removed or the PR is closed.</p>
  </div>
</body>
</html>`, hostname)
	})

	http.HandleFunc("/health", func(w http.ResponseWriter, r *http.Request) {
		w.WriteHeader(http.StatusOK)
		fmt.Fprint(w, "ok")
	})

	fmt.Printf("Trainyard demo running on :%s\n", port)
	http.ListenAndServe(":"+port, nil)
}
// test
