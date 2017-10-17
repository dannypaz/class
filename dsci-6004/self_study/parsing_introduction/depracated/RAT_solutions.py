from nltk.tree import Tree
Tree.fromstring(''' (S
          (NP (N John))
          (VP
            (V wrote)
            (NP
              (NP (NP (Det the) (N book)) (PP (P with) (NP (Det a) (N pen))))
              (PP (P in) (NP (Det the) (N room))))))''')

Tree.fromstring(''' (S
          (NP (N John))
          (VP
            (V wrote)
            (NP
              (NP (Det the) (N book))
              (PP
                (P with)
                (NP (NP (Det a) (N pen)) (PP (P in) (NP (Det the) (N room))))))))''')


Tree.fromstring('''(S
          (NP (N John))
          (VP
            (VP
              (VP (V wrote) (NP (Det the) (N book)))
              (PP (P with) (NP (Det a) (N pen))))
            (PP (P in) (NP (Det the) (N room)))))''')



Tree.fromstring(''' (S
          (NP (N John))
          (VP
            (VP
              (V wrote)
              (NP (NP (Det the) (N book)) (PP (P with) (NP (Det a) (N pen)))))
            (PP (P in) (NP (Det the) (N room)))))''')

Tree.fromstring(''' (S
          (NP (N John))
          (VP
            (VP (V wrote) (NP (Det the) (N book)))
            (PP
              (P with)
              (NP (NP (Det a) (N pen)) (PP (P in) (NP (Det the) (N room)))))))''')

(S
          (NP (N John))
          (VP
            (V wrote)
            (NP
              (NP (NP (Det the) (N book)) (PP (P with) (NP (Det a) (N pen))))
              (PP (P in) (NP (Det the) (N room))))))
        (S
          (NP (N John))
          (VP
            (V wrote)
            (NP
              (NP (Det the) (N book))
              (PP
                (P with)
                (NP (NP (Det a) (N pen)) (PP (P in) (NP (Det the) (N room))))))))
        (S
          (NP (N John))
          (VP
            (VP
              (VP (V wrote) (NP (Det the) (N book)))
              (PP (P with) (NP (Det a) (N pen))))
            (PP (P in) (NP (Det the) (N room)))))
        (S
          (NP (N John))
          (VP
            (VP
              (V wrote)
              (NP (NP (Det the) (N book)) (PP (P with) (NP (Det a) (N pen)))))
            (PP (P in) (NP (Det the) (N room)))))
        (S
          (NP (N John))
          (VP
            (VP (V wrote) (NP (Det the) (N book)))
            (PP
              (P with)
              (NP (NP (Det a) (N pen)) (PP (P in) (NP (Det the) (N room)))))))
              
