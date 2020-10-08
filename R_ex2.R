
minutos = data.frame(x = c(runif(510, 0, 1)))
eventos = c()

     for (i in 1:510){
  if (minutos$x[i] <= 0.0196){eventos <- append(eventos, i)
  }
}

tempo_input = c(2.24, 0.76, 1.30, 0.13, 0.10, 0.02,  0.16, 0.06, 0.91, 0.26)
tempo_input <- sort(tempo_input)
plot (ecdf(tempo_input))

prob_tempo = runif(length(eventos),0,1)

tempo = c()

for (i in 1:11){
    if (prob_tempo[[i]] <= 0.1) {
      tempo <- append(tempo,
                      runif( 1, 0, tempo_input[[1]]),
                      after = i - 1)}
    else if (prob_tempo[[i]] <= 0.2) {
      tempo <- append(tempo,
                      runif( 1, tempo_input[[1]], tempo_input[[2]]),
                      after = i - 1)}
  else if (prob_tempo[[i]] <= 0.3) {
    tempo <- append(tempo,
                    runif( 1, tempo_input[[2]], tempo_input[[3]]),
                    after = i - 1)}
  else if (prob_tempo[[i]] <= 0.4) {
    tempo <- append(tempo,
                    runif( 1, tempo_input[[3]], tempo_input[[4]]),
                    after = i - 1)}
  else if (prob_tempo[[i]] <= 0.5) {
    tempo <- append(tempo,
                    runif( 1, tempo_input[[4]], tempo_input[[5]]),
                    after = i - 1)}
  else if (prob_tempo[[i]] <= 0.6) {
    tempo <- append(tempo,
                    runif( 1, tempo_input[[5]], tempo_input[[6]]),
                    after = i - 1)}
  else if (prob_tempo[[i]] <= 0.7) {
    tempo <- append(tempo,
                    runif( 1, tempo_input[[6]], tempo_input[[7]]),
                    after = i - 1)}
  else if (prob_tempo[[i]] <= 0.8) {
    tempo <- append(tempo,
                    runif( 1, tempo_input[[7]], tempo_input[[8]]),
                    after = i - 1)}
  else if (prob_tempo[[i]] <= 0.9) {
    tempo <- append(tempo,
                    runif( 1, tempo_input[[8]], tempo_input[[9]]),
                    after = i - 1)}
  else if (prob_tempo[[i]] <= 10.) {
    tempo <- append(tempo,
                    runif( 1, tempo_input[[9]], tempo_input[[10]]),
                    after = i - 1)}
}
output <- data.frame(eventos = eventos, servico = tempo)

library(writexl)
write_xlsx(output, path = "C:/Users/Lucas/Downloads/Ex2.xlsx")

