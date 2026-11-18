from pathlib import Path
import hashlib, json, unittest

ROOT=Path(__file__).resolve().parents[1]
def read(name):return json.loads((ROOT/'data/curriculum_2022'/name).read_text(encoding='utf-8'))

class CurriculumContentTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.batch=read('passage_drafts_batch_02.json')
        cls.by_id={p['id']:p for p in cls.batch}
        cls.reg=read('curriculum_registry.json')
        cls.placements={p['id']:p for p in cls.reg['placements']}

    def test_published_sources_and_exact_evidence(self):
        criteria=set()
        for p in self.batch:
            placement=self.placements[p['placementId']]
            self.assertEqual(placement['placementStatus'],'교과서 목차 확인')
            self.assertTrue(set(p['conceptIds']).issubset(placement['conceptIds']))
            self.assertIn(p['curriculumAlignment']['standardId'],placement['relatedStandardIds'])
            for it in p['diagnostic']['items']:
                self.assertNotIn(it['criterionId'],criteria)
                criteria.add(it['criterionId'])
                for e in it['evidenceLocations']:
                    self.assertIn(e['quote'],p['paragraphs'][e['paragraph']-1])
                self.assertEqual(it['targetGoalId'],p['goalIds'][0])

    def test_pairs_do_not_treat_seen_training_as_new_transfer(self):
        for p in self.batch:
            pair=[x for x in self.batch if x['pairId']==p['pairId'] and x['id']!=p['id']]
            self.assertEqual(len(pair),1)
            other=pair[0]
            self.assertEqual(p['goalIds'],other['goalIds'])
            self.assertNotEqual(p['conceptIds'],other['conceptIds'])
            self.assertEqual(p['operationalGoal']['behavior'],other['operationalGoal']['behavior'])
            if p['purpose']=='transfer_check':
                self.assertEqual(p['teacherThinkingModel']['visibility'],'teacher_only_after_response')
                self.assertFalse(any(s['phase']=='transfer' for s in p['readingProcess']))
                for s in p['readingProcess']:
                    if s['phase'] in ('model','guided','faded'):
                        self.assertEqual(s['visibility'],'after_independent_response_only')

    def test_mathematical_examples_and_units(self):
        triangles=self.by_id['P22-B02-G4-M-01']['table']['rows']
        for _,a,b,c in triangles:
            self.assertLess(max(a,b,c),sum((a,b,c))-max(a,b,c))
        self.assertEqual(triangles[1][1:],[4,4,4])
        for position,value in self.by_id['P22-B02-G4-M-02']['table']['rows']:
            self.assertEqual(value,3+(position-1)*4)
        for _,original,rounded in self.by_id['P22-B02-G5-M-02']['table']['rows']:
            self.assertEqual(rounded,(original+5)//10*10)
        for _,diameter,circumference in self.by_id['P22-B02-G6-M-01']['table']['rows']:
            self.assertAlmostEqual(diameter*3.14,circumference)
        plans=self.by_id['P22-B02-G6-M-02']['table']['rows']
        for _,a,b,total in plans:self.assertEqual(a+b,total)
        self.assertEqual(plans[1][1]/plans[1][2],2)
        self.assertNotEqual(plans[0][1]/plans[0][2],2)

    def test_standard_text_is_not_explanatory_prose(self):
        standards={s['id']:s for s in read('achievement_standards.json')}
        self.assertTrue(standards['4사01-01']['statement'].startswith('주변 여러 장소에서의 경험과 느낌을'))
        self.assertTrue(standards['4사01-02']['statement'].startswith('주변의 여러 장소를 살펴보고'))
        self.assertEqual(len(standards),611)
        self.assertFalse(any(s['statement'].startswith(('은 ','는 ')) for s in standards.values()))

    def test_corpus_retains_originals_and_approval_boundary(self):
        corpus=read('passage_corpus.json')
        self.assertEqual(corpus['counts'],{'newDrafts':48,'legacyDrafts':96,'uniqueTexts':144,'approved':0})
        self.assertEqual(len({p['contentHash'] for p in corpus['passages']}),144)
        for p in self.batch:
            self.assertEqual(p['publicationState'],'unpublished')
            self.assertFalse(p['editorialReview']['independentReviewer'])
            self.assertEqual(p['editorialReview']['studentCalibration'],'pending')
            self.assertEqual(p['contentHash'],hashlib.sha256('\n'.join(p['paragraphs']).encode()).hexdigest())
        original=read('passage_drafts_batch_01.json')
        combined={p['id']:p for p in read('revisions/baseline-v1.json')['passages']}
        for p in original:self.assertEqual(combined[p['id']]['paragraphs'],p['paragraphs'])

    def test_all_revisions_replace_active_text_without_changing_identity(self):
        corpus=read('passage_corpus.json')
        baseline={p['id']:p for p in read('revisions/baseline-v1.json')['passages']}
        self.assertEqual(corpus['revisionCoverage'],dict(revised=144,total=144,levelVariants=432,practiceQuestions=720,challengeReplacements=80))
        for p in corpus['passages']:
            self.assertEqual(p['version'],2)
            self.assertEqual(p['purpose'],'practice')
            self.assertEqual(p['goalIds'],baseline[p['id']]['goalIds'])
            self.assertEqual(p['editorialReview']['baselineHash'],baseline[p['id']]['contentHash'])
            self.assertNotEqual(p['paragraphs'],baseline[p['id']]['paragraphs'])
            self.assertEqual(p['contentHash'],hashlib.sha256('\n'.join(p['paragraphs']).encode()).hexdigest())
            self.assertEqual(p['paragraphs'],p['readingVariants']['standard'])
            self.assertNotIn('table',p)
            self.assertNotIn('independentCheck',p)
            self.assertEqual(len(p['diagnostic']['items']),5)
            self.assertEqual(p['editorialReview']['teacherReview'],'pending')
            self.assertEqual(p['editorialReview']['studentCalibration'],'pending')

if __name__=='__main__':unittest.main()
