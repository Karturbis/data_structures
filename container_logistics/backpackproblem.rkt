#lang racket
; Von Lukas und Caspian
(define (container-gen)
  (define container-size (random 1 100));; max container size is: 4294967088
  container-size
  )

(define container-size (container-gen))

(define (packet-gen-inner liset running-sum)
  (define ski (random 1 (add1 (ceiling (/ container-size 4)))))
  (if (> running-sum container-size)
      liset
      (packet-gen-inner (list* ski liset) (+ running-sum ski))
  )
)

(define (pkg); wrapper function for packet-gen-inner
  (sort (packet-gen-inner '() 0)>)
)

(define pkgv (pkg)); define package variable

(define (stuff-container packet-lst stuffing-lst container-size exceeding-lst)
  (if (empty? packet-lst)
      (list stuffing-lst exceeding-lst)
      (if (> (first packet-lst) container-size)
          (stuff-container (rest packet-lst) stuffing-lst container-size (list* (first packet-lst) exceeding-lst))
          (stuff-container (rest packet-lst) (list* (first packet-lst) stuffing-lst) (- container-size (first packet-lst)) exceeding-lst)
      )
  )
)

(define (sc);; wrapper function for stuff container
  (stuff-container pkgv '() container-size '())
  )

(define rsult (sc))
(define rsult-1 (car rsult))
(define rsult-2 (cdr rsult))

(printf "Die Containergröße ist: ~a\n" container-size)
(printf "Die Pakete sind: ~a\n" (reverse pkgv))
(printf "In den Container passen folgende Pakete: ~a\n" rsult-1)
(printf "Übrig bleiben die Pakete: ~a\n" (car rsult-2))
(printf "Der Material-Verschnitt beträgt: ~a\n" (foldr + 0 (car rsult-2)))
(printf "Der Platz-Verschnitt beträgt: ~a" (- container-size (foldr + 0 rsult-1)))