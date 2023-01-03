import unittest

import sys
sys.path.append('../src')

from src.chromosome import Chromosome

class ChromosomeTest(unittest.TestCase):
    def test_generate_schedule(self):
        chromosome = Chromosome([1, 2, 3], 
                                ['Tutor1', 'Tutor2', 'Tutor3', 'Tutor4'], 
                                ['CIS311', 'CIS312', 'CIS313'])
                                
        print(chromosome.schedule)
        self.assertEqual(len(chromosome.schedule), 10)

if __name__ == '__main__':
    unittest.main()
