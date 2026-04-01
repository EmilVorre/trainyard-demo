# Build stage
FROM golang:1.22-alpine AS builder
WORKDIR /app
COPY main.go .
RUN go mod init trainyard-demo && \
    go build -o demo .

# Run stage — tiny final image
FROM alpine:3.19
WORKDIR /app
COPY --from=builder /app/demo .
EXPOSE 8080
CMD ["./demo"]
