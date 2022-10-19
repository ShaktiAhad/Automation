def call(cmd) {
  return sh(
    script: cmd,
    returnStdout: true
  ).trim()
}
