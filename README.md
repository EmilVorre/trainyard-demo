# Trainyard Demo

This is the official demo repository for [Trainyard](https://github.com/Emilvorre/trainyard) — a lightweight framework for ephemeral Kubernetes preview environments per pull request.

## How it works

1. Open a pull request
2. Add the `preview` label
3. Trainyard automatically builds and deploys the app to `pr-{number}.preview.vorre.dev`
4. A comment is posted on the PR with the live URL
5. Every new commit redeploys automatically
6. When the label is removed or the PR is closed, the environment is torn down

## Stack

- **App:** Go — simple HTTP server
- **Framework:** [Trainyard](https://github.com/Emilvorre/trainyard)
- **Cluster:** k3s
- **Ingress:** Nginx + cert-manager (Let's Encrypt)

## Try it yourself

1. Fork this repo
2. Follow the [Trainyard setup guide](https://github.com/Emilvorre/trainyard)
3. Open a PR and apply the `preview` label
