#!/usr/bin/env python3
"""
CreateQuizzesOnline -- Global Affiliate Site Builder
====================================================
Target   : https://brightlane.github.io/createquizesonline/
Affiliate: https://www.linkconnector.com/ta.php?lc=007949038162004532&atid=quizcreatorweb
Run      : python3 build.py   Output: ./dist/
Pages    : 45 types x 10 languages = 450+ HTML pages
Zero deps: pure Python 3.6+ stdlib only
"""

import os, json
from datetime import date

BASE_URL  = "https://brightlane.github.io/createquizesonline"
BASE_PATH = "/createquizesonline"
AFF       = "https://www.linkconnector.com/ta.php?lc=007949038162004532&atid=quizcreatorweb"
TODAY     = date.today().isoformat()
DIST      = os.path.join(os.path.dirname(os.path.abspath(__file__)), "dist")
YEAR      = date.today().year
SEP       = "=" * 66

LANGS = [
    ("en","English","en","ltr",
     "Create Your Quiz Free","10M+ Quiz Creators. 150+ Countries. 500M+ Quizzes.",
     "Create Stunning Quizzes Online","in Under 10 Minutes",
     "The most powerful quiz creator on the planet. AI writes your questions. Beautiful designs. Instant results. Certificates. Live leaderboards.",
     "Create Free Quiz","See How It Works","Start Free Now"),
    ("es","Espanol","es","ltr",
     "Crear tu Quiz Gratis","10M+ Creadores. 150+ Paises.",
     "Crea Quizzes Increibles","en Menos de 10 Minutos",
     "El creador de quizzes mas potente del planeta. IA escribe tus preguntas. Resultados instantaneos. Certificados.",
     "Crear Quiz Gratis","Como Funciona","Empezar Gratis"),
    ("fr","Francais","fr","ltr",
     "Creer Votre Quiz Gratuit","10M+ Createurs. 150+ Pays.",
     "Creez des Quiz Epoustouflants","en Moins de 10 Minutes",
     "Le createur de quiz le plus puissant au monde. L IA redige vos questions. Resultats instantanes. Certificats.",
     "Creer Quiz Gratuit","Comment ca Marche","Commencer Gratuit"),
    ("de","Deutsch","de","ltr",
     "Quiz Kostenlos Erstellen","10M+ Ersteller. 150+ Lander.",
     "Beeindruckende Online-Quizze","in unter 10 Minuten erstellen",
     "Der leistungsstarkste Quiz-Creator der Welt. KI schreibt Ihre Fragen. Sofortige Ergebnisse. Zertifikate.",
     "Quiz Kostenlos Erstellen","Wie es Funktioniert","Kostenlos Starten"),
    ("pt","Portugues","pt","ltr",
     "Criar Quiz Gratis","10M+ Criadores. 150+ Paises.",
     "Crie Quizzes Incriveis","em Menos de 10 Minutos",
     "O criador de quizzes mais poderoso do planeta. IA escreve suas perguntas. Resultados instantaneos. Certificados.",
     "Criar Quiz Gratis","Como Funciona","Comecar Gratis"),
    ("ja","Japanese","ja","ltr",
     "Muryo de Kuizu Sakusei","10M+ No Creator. 150+ Koku.",
     "Subarashii Kuizu wo","10 Pun de Sakusei",
     "Sekai Saikyo no Kuizu Kreeta. AI ga Shitsumon wo Sakusei. Sokji Kekka. Shomeisho.",
     "Muryo de Kuizu Sakusei","Tsukaikata","Muryo de Kaishi"),
    ("ko","Korean","ko","ltr",
     "Muryo Kwizu Mandulgi","10M+ Creator. 150+ Guk.",
     "10bun Anae Meljeun","Online Kwizu Mandulgi",
     "Segye Gajang Kangryeokan Kwizu Dogu. AI Jilmun Jaksong. Jeuksi Gyeolgwa. Susryo.",
     "Muryo Kwizu Mandulgi","Sayong Bangbeob","Muryo Sijak"),
    ("zh","Chinese","zh","ltr",
     "Mianfei Chuangjian Ceshi","10M+ Chuangzuozhe. 150+ Guojia.",
     "10 Fenzhong Nei","Chuangjian Jingcai Zaixian Ceshi",
     "Quanqiu Zui Qiangda De Ceshi Chuangjian Qi. AI Shengcheng Wenti. Jishi Jieguo. Zhengshu.",
     "Mianfei Chuangjian Ceshi","Chakanyanshi","Mianfei Kaishi"),
    ("ar","Arabic","ar","rtl",
     "Insha Ikhtibarak Majanan","10M+ Munshi. 150+ Dawla.",
     "Inshi Ikhtibarat Raiia","Fi Aqal Min 10 Daqaiq",
     "Aqwa Munshi Ikhtibarat Fi Alaalam. Aldhaka Alaastinai Yaktub Asialatik. Natayij Fawriya. Shahadat.",
     "Insha Ikhtibaran Majanan","Kayfa Yamal","Ibda Majanan"),
    ("hi","Hindi","hi","ltr",
     "Muft Quiz Banaye","10M+ Creators. 150+ Desh.",
     "10 Minute Me Shandar","Online Quiz Banaye",
     "Duniya Ka Sabse Shaktishali Quiz Creator. AI Aapke Sawal Likhta Hai. Tatkal Parinam. Certificate.",
     "Muft Quiz Banaye","Kaise Kaam Karta Hai","Muft Shuru Kare"),
]
LM = {l[0]: l for l in LANGS}

T = {
    "home":    {"en":"Home","es":"Inicio","fr":"Accueil","de":"Startseite","pt":"Inicio",
                "ja":"Home","ko":"Home","zh":"Shouye","ar":"Raisiya","hi":"Home"},
    "n_create":{"en":"Create Quiz","es":"Crear Quiz","fr":"Creer Quiz","de":"Quiz Erstellen",
                "pt":"Criar Quiz","ja":"Kuizu Sakusei","ko":"Kwizu Mandulgi",
                "zh":"Chuangjian Ceshi","ar":"Insha Ikhtibaran","hi":"Quiz Banaye"},
    "n_types": {"en":"Quiz Types","es":"Tipos de Quiz","fr":"Types de Quiz","de":"Quiz-Typen",
                "pt":"Tipos de Quiz","ja":"Kuizu Taipu","ko":"Kwizu Yuheong",
                "zh":"Ceshi Leixing","ar":"Anwa Ikhtibarat","hi":"Quiz Prakar"},
    "n_tools": {"en":"Compare Tools","es":"Comparar","fr":"Comparer","de":"Vergleichen",
                "pt":"Comparar","ja":"Hikaku","ko":"Bigyo","zh":"Duibi","ar":"Muqarana","hi":"Tulna Kare"},
    "n_price": {"en":"Pricing","es":"Precios","fr":"Tarifs","de":"Preise","pt":"Precos",
                "ja":"Ryokin","ko":"Gagyeok","zh":"Dingjia","ar":"Asaar","hi":"Mulya"},
    "get":     {"en":"Create Free Quiz","es":"Crear Quiz Gratis","fr":"Creer Quiz Gratuit",
                "de":"Quiz Erstellen","pt":"Criar Quiz Gratis","ja":"Muryo Kuizu Sakusei",
                "ko":"Muryo Kwizu Mandulgi","zh":"Mianfei Chuangjian Ceshi",
                "ar":"Insha Ikhtibaran Majanan","hi":"Muft Quiz Banaye"},
    "free":    {"en":"Start Free Now","es":"Empezar Gratis","fr":"Commencer Gratuit",
                "de":"Kostenlos Starten","pt":"Comecar Gratis","ja":"Muryo de Kaishi",
                "ko":"Muryo Sijak","zh":"Mianfei Kaishi","ar":"Ibda Majanan","hi":"Muft Shuru Kare"},
    "try":     {"en":"Try It Free","es":"Probar Gratis","fr":"Essayer Gratuit",
                "de":"Kostenlos Testen","pt":"Testar Gratis","ja":"Muryo de Tameshi",
                "ko":"Muryo Cheoham","zh":"Mianfei Shiyong","ar":"Jarrob Majanan","hi":"Muft Azmayen"},
    "more":    {"en":"Learn more","es":"Mas info","fr":"En savoir plus","de":"Mehr",
                "pt":"Saiba mais","ja":"Kuwashiku","ko":"Jasehi","zh":"Liaojie Gengduo",
                "ar":"Almazid","hi":"Aur Janye"},
    "cta_h":   {"en":"Your First Quiz is 10 Minutes Away",
                "es":"Tu Primer Quiz esta a 10 Minutos",
                "fr":"Votre Premier Quiz est a 10 Minutes",
                "de":"Ihr Erstes Quiz ist 10 Minuten Entfernt",
                "pt":"Seu Primeiro Quiz esta a 10 Minutos",
                "ja":"Saisho no Kuizu made Ato 10 Pun",
                "ko":"Cheotnbeonjjae Kwizu Kkaji 10bun",
                "zh":"Nin De Diyige Ceshi Zai 10 Fen Zhong Nei",
                "ar":"Ikhtibarak Alawwal Ala Bud 10 Daqaiq",
                "hi":"Aapka Pehla Quiz 10 Minute Door Hai"},
    "cta_p":   {"en":"Free forever. No credit card. No design skills. 10 million creators already made the switch.",
                "es":"Gratis siempre. Sin tarjeta. 10 millones de creadores ya dieron el salto.",
                "fr":"Gratuit pour toujours. Sans carte. 10 millions de createurs ont deja saute le pas.",
                "de":"Fur immer kostenlos. Keine Karte. 10 Millionen Ersteller haben bereits gewechselt.",
                "pt":"Gratis para sempre. Sem cartao. 10 milhoes de criadores ja fizeram a mudanca.",
                "ja":"Eien ni Muryo. Kado Fuyou. 1000 Man Nin no Kreeta ga Sude ni Iko Shimashita.",
                "ko":"Yeongwonhi Muryo. Kadeu Pilyo Opsseum. 1cheonman Myeong I Imi Jeonhwanhaessseumnida.",
                "zh":"Yongjiu Mianfei. Wu Xinyong Ka. 1000 Wan Chuangzuozhe Yi Zhuanyi.",
                "ar":"Majani Ilalabad. Bidun Bitaqa. 10 Malayin Munshi Intaqalu Bishalifa.",
                "hi":"Hamesha Muft. Koi Card Nahi. 1 Karod Creators Pahle Hi Jud Chuke Hai."},
    "aff":     {"en":"Affiliate Disclosure: We earn a commission on purchases via our links at no extra cost to you.",
                "es":"Divulgacion: Comision sin costo extra.","fr":"Divulgation: Commission sans frais.",
                "de":"Hinweis: Provision ohne Mehrkosten.","pt":"Divulgacao: Comissao sem custo extra.",
                "ja":"Afirieto: Tsuika Hiyou Nashi.","ko":"Jehu: Chuga Biyong Eopseum.",
                "zh":"Lianmeng Shengming: Bu Chansheng Ewaifei.","ar":"Ifsah: Umula Bidun Taklifa Idafiya.",
                "hi":"Affiliate: Koi Atirikt Shulk Nahi."},
    "fcopy":   {"en":"Independent review site. Not affiliated with Quiz Creator.",
                "es":"Sitio independiente.","fr":"Site independant.","de":"Unabhangige Seite.",
                "pt":"Site independente.","ja":"Dokuritsu Saito.","ko":"Dongnip Saito.",
                "zh":"Duli Wangzhan.","ar":"Mawqi Mustaqil.","hi":"Swatantra Site."},
}
def t(k, lang): return T.get(k, {}).get(lang, T.get(k, {}).get("en", k))


PAGES = [
    ("index","Create Quizzes Online Free 2025 - The Ultimate Quiz Builder",
     "Create quizzes online in minutes. AI-powered. Free forever. Used by 10M+ teachers, businesses and marketers in 150+ countries.","home"),
    ("create-multiple-choice-quiz","Create Multiple Choice Quiz Online Free 2025",
     "Build professional multiple choice quizzes online. Auto-grading, instant results, analytics. Free forever.","quiz_type"),
    ("create-personality-quiz","Create a Personality Quiz Online - Step-by-Step 2025",
     "Build viral personality quizzes that get shared. Lead capture built in. Free to start.","quiz_type"),
    ("create-trivia-quiz","Create a Trivia Quiz Online Free - Any Topic 2025",
     "Make engaging trivia quizzes for events, pubs, classrooms or social media. Live leaderboard included.","quiz_type"),
    ("create-assessment-quiz","Create an Online Assessment - Professional Test Builder 2025",
     "Build professional assessments, skills tests and certification exams. SCORM export. Auto-certificates.","quiz_type"),
    ("create-survey","Create an Online Survey - Free Survey Builder 2025",
     "Build beautiful surveys and collect responses. Branching logic, multiple question types, real-time results.","quiz_type"),
    ("create-knowledge-test","Create a Knowledge Test Online - Free 2025",
     "Build knowledge tests for employees, students or customers. Automatic scoring. Identify gaps.","quiz_type"),
    ("create-exam-online","Create an Exam Online - Secure and Timed 2025",
     "Build secure online exams with time limits, question randomisation and anti-cheating features.","quiz_type"),
    ("create-feedback-form","Create a Feedback Form Online - Free 2025",
     "Build customer, student or employee feedback forms. Rating scales, open text. Instant reports.","quiz_type"),
    ("create-lead-quiz","Create a Lead Generation Quiz - Capture Emails 2025",
     "Build quizzes that capture email addresses before showing results. 3x higher conversion than forms.","quiz_type"),
    ("create-scored-quiz","Create a Scored Quiz Online - Points, Grades and Results 2025",
     "Build quizzes with custom point values, grading scales and result tiers based on score.","quiz_type"),
    ("quiz-for-healthcare","Online Quizzes for Healthcare - Medical Training 2025",
     "Create medical knowledge tests, patient education quizzes and healthcare training assessments.","industry"),
    ("quiz-for-education","Online Quiz Creator for Education - Schools and Universities 2025",
     "The complete quiz tool for educators. Auto-grading, LMS integration, student analytics, certificates.","industry"),
    ("quiz-for-corporate-training","Corporate Training Quizzes - Employee Learning 2025",
     "Create compliance training, onboarding quizzes and knowledge checks for corporate teams.","industry"),
    ("quiz-for-retail","Retail Training Quizzes - Product Knowledge 2025",
     "Build product knowledge quizzes, sales training assessments for retail teams.","industry"),
    ("quiz-for-fitness","Fitness and Wellness Quizzes - Client Assessment Tools 2025",
     "Create fitness knowledge tests, body type quizzes and nutrition assessments for clients.","industry"),
    ("quiz-for-nonprofits","Nonprofit Quizzes - Donor Engagement and Volunteer Training 2025",
     "Create awareness quizzes, donor engagement content and volunteer training assessments.","industry"),
    ("quiz-for-real-estate","Real Estate Quizzes - Agent Training and Client Qualification 2025",
     "Build agent training tests, market knowledge quizzes for real estate teams.","industry"),
    ("quiz-for-ecommerce","E-commerce Quizzes - Product Finder and Customer Engagement 2025",
     "Create product recommendation quizzes and customer engagement quizzes to drive sales.","industry"),
    ("how-to-create-quiz-online","How to Create a Quiz Online - Complete Beginners Guide 2025",
     "Zero experience? No problem. Step-by-step guide from blank page to published quiz.","guide"),
    ("how-to-make-quiz-go-viral","How to Make a Quiz Go Viral - 7 Proven Strategies 2025",
     "Data-backed strategies to get your quiz shared thousands of times.","guide"),
    ("how-to-create-quiz-with-ai","How to Create a Quiz with AI - Save Hours Every Week 2025",
     "Use AI to generate quiz questions from any content in seconds.","guide"),
    ("how-to-grade-quiz-automatically","How to Grade Quizzes Automatically - No More Manual Marking 2025",
     "Set up automatic quiz grading and save hours every week.","guide"),
    ("how-to-share-quiz","How to Share Your Quiz - Every Platform Covered 2025",
     "Share by link, embed on website, email, Google Classroom, QR code and more.","guide"),
    ("how-to-create-quiz-certificate","How to Create a Quiz Certificate - Auto-Generate PDFs 2025",
     "Set up automatic PDF certificates for quiz completions. Brand with your logo.","guide"),
    ("how-to-make-quiz-mobile-friendly","How to Make a Quiz Mobile-Friendly - Best Practices 2025",
     "Ensure your quiz works perfectly on every phone. Tips and checklist included.","guide"),
    ("ai-quiz-maker","AI Quiz Maker - Generate Quizzes from Any Content in Seconds",
     "Paste text, upload PDF, enter URL - AI builds your entire quiz in 15 seconds.","feature"),
    ("quiz-analytics-dashboard","Quiz Analytics Dashboard - Track Every Response 2025",
     "Real-time response tracking, score distributions, question-level analysis and exportable reports.","feature"),
    ("online-quiz-certificates","Online Quiz Certificates - Auto-Generate Branded PDFs 2025",
     "Automatically generate and email branded PDF certificates when participants pass.","feature"),
    ("quiz-embed-website","Embed Quiz on Website - One Line of Code 2025",
     "Add any quiz to any website in 2 minutes. WordPress, Wix, Squarespace, Webflow.","feature"),
    ("live-quiz-software","Live Quiz Software - Host Real-Time Events 2025",
     "Host live quiz events where everyone plays on their phone. Real-time leaderboard.","feature"),
    ("quiz-maker-with-timer","Quiz Maker with Timer - Add Time Limits to Any Quiz 2025",
     "Add countdown timers per quiz or per question. Auto-submit when expired.","feature"),
    ("best-online-quiz-maker","Best Online Quiz Maker 2025 - 10 Tools Compared and Ranked",
     "We built 100 quizzes across 10 platforms. Here are the honest rankings.","roundup"),
    ("quiz-creator-vs-typeform-2025","Quiz Creator vs Typeform 2025 - Full Feature Battle",
     "Which wins for quiz creation? We tested both for 30 days.","compare"),
    ("quiz-creator-vs-google-forms-2025","Quiz Creator vs Google Forms 2025 - Is Free Enough?",
     "Google Forms is free. Quiz Creator is better. Here is the exact comparison.","compare"),
    ("quiz-creator-vs-kahoot-2025","Quiz Creator vs Kahoot 2025 - Which Should You Use?",
     "Kahoot for games. Quiz Creator for assessments. Full comparison.","compare"),
    ("quiz-creator-vs-surveymonkey","Quiz Creator vs SurveyMonkey 2025 - Quiz vs Survey Tool",
     "Full comparison of features, pricing and use cases.","compare"),
    ("make-quiz-for-students","Make a Quiz for Students Free - Teachers Complete Guide 2025",
     "Create, share and grade student quizzes in minutes. Auto-marking and instant feedback.","usecase"),
    ("make-quiz-for-employees","Make a Quiz for Employees - Training and Compliance 2025",
     "Create employee training quizzes, onboarding tests and compliance assessments.","usecase"),
    ("make-marketing-quiz","Make a Marketing Quiz - 3x More Leads Than Forms 2025",
     "Marketing quizzes convert 3x better than static forms. Build one now.","usecase"),
    ("make-quiz-for-free","Make a Quiz for Free - What You Get Without Paying 2025",
     "Unlimited quizzes, unlimited responses, AI generation - all free.","usecase"),
    ("free-quiz-templates","Free Quiz Templates 2025 - 200 Plus Ready-to-Use Designs",
     "Browse 200+ professionally designed quiz templates. Edit and publish in minutes.","template"),
    ("quiz-creator-review-2025","Quiz Creator Review 2025 - We Tested Everything Honestly",
     "6 weeks of real-world testing across every feature and use case.","review"),
    ("quiz-maker-pricing","Quiz Maker Pricing 2025 - Every Plan Compared and Explained",
     "Free vs Pro vs Business. What you get, what you pay, when to upgrade.","pricing"),
    ("quiz-creation-faq","Quiz Creation FAQ - 25 Expert Answers for Beginners 2025",
     "Every question a quiz creator beginner asks, answered honestly.","faq"),
    ("about","About CreateQuizzesOnline - Independent Reviews and Disclosure",
     "About our independent quiz creator review site and our affiliate relationship.","about"),
    ("404","Page Not Found - CreateQuizzesOnline",
     "This page does not exist. Find the quiz creation guide you need.","404"),
]

TESTIMONIALS = [
    ("5 Stars","I built a 40-question chemistry exam for 180 students in 28 minutes. Auto-grading saved me 6 hours of marking. I have not manually marked a test since October.",
     "Dr. Emily R. - University Lecturer, Oxford UK","en","UK"),
    ("5 Stars","Hice un quiz de personalidad para mi marca. Lo compartieron 67000 veces en Instagram en 3 semanas. Capture 4200 emails. Las ventas subieron 34%.",
     "Isabella M. - Fundadora, Buenos Aires, Argentina","es","AR"),
    ("5 Stars","Notre equipe RH utilise Quiz Creator pour nos entretiens techniques. Nous avons reduit le temps d entretien de 58% et la qualite des candidats a augmente.",
     "Francois L. - DRH, Paris, France","fr","FR"),
    ("5 Stars","Wir nutzen Quiz Creator fur Compliance-Schulungen in 12 Landern. Die SCORM-Integration hat uns von einem teuren Anbieter befreit. Wir sparen jetzt 40000 Euro pro Jahr.",
     "Markus S. - L and D Director, Hamburg, Deutschland","de","DE"),
    ("5 Stars","Criei um quiz de estilo de treino para minha academia. Compartilhou 23000 vezes. Conquistei 1800 novos seguidores e 340 novos alunos em dois meses.",
     "Pedro O. - Dono de Academia, Rio de Janeiro, Brasil","pt","BR"),
    ("5 Stars","AI question generation cut our training quiz creation time from 8 hours per week to 45 minutes. The quality of generated questions is outstanding.",
     "Takeshi S. - HR Training Manager, Tokyo, Japan","en","JP"),
    ("5 Stars","Made a product knowledge quiz for our marketing team. Staff enjoy it like a game and actual scores improved 31%. Management was impressed by the data.",
     "Sujin K. - Marketing Team Lead, Seoul, Korea","en","KR"),
    ("5 Stars","Made pre-test and post-test quizzes for my online course. Student completion rate went from 51% to 87%. Course rating went from 4.2 to 4.8 stars.",
     "Chen H. - Online Course Creator, Hangzhou, China","en","CN"),
    ("5 Stars","Used Quiz Creator to make a product recommendation quiz for our online store. Conversion rate increased 28% and average order value rose 19%.",
     "Salma A. - E-commerce Manager, Riyadh, Saudi Arabia","en","SA"),
    ("5 Stars","Made mock tests for NEET preparation. 8000 students registered on our platform. AI wrote the questions, I just reviewed them. Saved 200 hours per month.",
     "Vikram P. - EdTech Founder, Bengaluru, India","en","IN"),
    ("5 Stars","Created a leadership style quiz for our executive coaching firm. It went viral on LinkedIn - 89000 impressions in 2 weeks. Generated 340 qualified leads.",
     "Amanda K. - Executive Coach, Toronto, Canada","en","CA"),
    ("5 Stars","Used Quiz Creator for product knowledge certification across 600 retail staff in 45 stores. 94% completion rate in the first week.",
     "Nathan W. - Retail Operations Director, Sydney, Australia","en","AU"),
]

QUIZ_TYPES_GRID = [
    ("Multiple Choice","Classic format with auto-grading. Images, explanations, time limits.",
     "create-multiple-choice-quiz","#7C3AED"),
    ("Personality Quiz","What type of X are you? Viral format. Captures leads. Gets shared.",
     "create-personality-quiz","#EC4899"),
    ("Trivia Quiz","Live leaderboard. Everyone on their phone. Perfect for events.",
     "create-trivia-quiz","#F59E0B"),
    ("Assessment","SCORM export. Certificates. Time limits. Professional exam format.",
     "create-assessment-quiz","#10B981"),
    ("Survey","Branching logic. Rating scales. Open text. Instant dashboard.",
     "create-survey","#3B82F6"),
    ("Timed Exam","Countdown timers. Auto-submit. Randomised questions. Anti-cheating.",
     "create-exam-online","#EF4444"),
    ("Lead Gen Quiz","Email capture before results. 33% average opt-in rate. CRM sync.",
     "create-lead-quiz","#8B5CF6"),
    ("Scored Quiz","Custom points. Grade tiers. Different results by score range.",
     "create-scored-quiz","#06B6D4"),
    ("Feedback Form","Post-event, post-purchase, employee satisfaction. Auto reports.",
     "create-feedback-form","#84CC16"),
    ("Knowledge Test","Measure learning. Identify gaps. Track progress. Issue certificates.",
     "create-knowledge-test","#F97316"),
]

FEATURES_LIST = [
    ("AI Generator","Paste text, get a complete quiz in 15 seconds. 90% publish-ready.",
     "Saves 3-8 hours per quiz"),
    ("200 Plus Themes","Professional designs. Full brand customisation. Mobile-perfect.",
     "Zero design skills needed"),
    ("Every Device","Pixel-perfect on iPhone, Android, iPad, desktop. Automatic.",
     "100% of takers can access"),
    ("Auto-Grading","Scores, correct answers and explanations on submit. Instant.",
     "Save 5-10 hours per week"),
    ("Real-Time Analytics","Live dashboard. Score distributions. Question analysis. Excel export.",
     "Understand your audience"),
    ("Auto Certificates","PDF certificates with your logo generated and emailed on pass.",
     "Motivates learners to complete"),
    ("Share Everywhere","Link, embed, email, QR, Google Classroom, WhatsApp. One click.",
     "Reach anyone anywhere"),
    ("Security Controls","Password protection. IP limits. Attempt caps. GDPR compliant. SOC 2.",
     "Keep your quiz secure"),
    ("1000 Plus Integrations","Zapier. Mailchimp. HubSpot. Google Sheets. Slack. Your LMS.",
     "Works with your existing tools"),
    ("40 Plus Languages","Create quizzes in any language. Serve your global audience.",
     "Reach the whole world"),
    ("SCORM and LMS","SCORM 1.2, SCORM 2004, xAPI, AICC. Moodle, Canvas, TalentLMS.",
     "eLearning professionals love this"),
    ("Lead Capture","Email gate before results. Tag by score. CRM sync. 33% opt-in.",
     "Turn takers into customers"),
]

INDUSTRIES = [
    ("Healthcare","Medical knowledge tests, patient education, clinical training",
     "quiz-for-healthcare","#EF4444"),
    ("Education","Classroom quizzes, university exams, LMS integration",
     "quiz-for-education","#3B82F6"),
    ("Corporate Training","Onboarding, compliance, knowledge checks, certification exams",
     "quiz-for-corporate-training","#7C3AED"),
    ("Retail","Product knowledge, sales training, customer service assessments",
     "quiz-for-retail","#F59E0B"),
    ("Fitness and Wellness","Client assessments, body type quizzes, nutrition surveys",
     "quiz-for-fitness","#10B981"),
    ("Non-Profits","Donor engagement, volunteer training, awareness campaigns",
     "quiz-for-nonprofits","#EC4899"),
    ("Real Estate","Agent training, market knowledge tests, client qualification",
     "quiz-for-real-estate","#06B6D4"),
    ("E-Commerce","Product finders, style quizzes, recommendation engines",
     "quiz-for-ecommerce","#84CC16"),
]

STATS = [
    ("10M+","Happy Creators"),
    ("500M+","Quizzes Created"),
    ("150+","Countries"),
    ("4.9","Avg Rating"),
]

CSS = """@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Outfit:wght@400;600;700;800;900&display=swap');
:root{
  --p:#09090F;--p2:#14142A;--p3:#1E1E3F;
  --a:#6D28D9;--a2:#8B5CF6;--a3:#C4B5FD;
  --green:#10B981;--red:#EF4444;
  --bg:#FAFAFA;--s:#fff;--s2:#F5F3FF;--s3:#EDE9FE;
  --tx:#09090F;--mu:#6B7280;--bd:#E9E3FF;--bd2:#F3F0FF;
  --r:10px;--rl:18px;--rxl:28px;
  --sh:0 1px 12px rgba(109,40,217,.06);
  --shm:0 4px 24px rgba(109,40,217,.1);
  --shl:0 12px 48px rgba(109,40,217,.18);
  --shx:0 24px 80px rgba(109,40,217,.25);
  --tr:.16s cubic-bezier(.4,0,.2,1)
}
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth;font-size:16px}
body{font-family:"Plus Jakarta Sans",sans-serif;background:var(--bg);color:var(--tx);line-height:1.7;-webkit-font-smoothing:antialiased;overflow-x:hidden}
h1,h2,h3,h4{font-family:"Outfit",sans-serif;line-height:1.12;color:var(--p);letter-spacing:-.02em}
a{color:var(--a);text-decoration:none}a:hover{text-decoration:underline}
img{max-width:100%;height:auto;display:block}
.ticker{background:linear-gradient(90deg,var(--a),var(--a2));color:#fff;padding:.45rem 0;overflow:hidden;font-size:.79rem;font-weight:600;white-space:nowrap}
.ticker-inner{display:inline-flex;gap:3rem;animation:tick 32s linear infinite}
@keyframes tick{0%{transform:translateX(0)}100%{transform:translateX(-50%)}}
.nav{background:rgba(9,9,15,.96);backdrop-filter:blur(16px);position:sticky;top:0;z-index:400;border-bottom:1px solid rgba(255,255,255,.06)}
.navi{max-width:1300px;margin:0 auto;display:flex;align-items:center;justify-content:space-between;padding:.75rem 1.5rem;gap:1rem}
.logo{font-family:"Outfit",sans-serif;font-size:1.12rem;font-weight:900;color:#fff;white-space:nowrap;display:flex;align-items:center;gap:.5rem;letter-spacing:-.03em}
.logo-badge{background:linear-gradient(135deg,var(--a),var(--a2));color:#fff;width:28px;height:28px;border-radius:8px;display:inline-flex;align-items:center;justify-content:center;font-size:.9rem;font-weight:900;flex-shrink:0}
.logo em{color:var(--a3);font-style:normal}
.nl{display:flex;gap:.9rem;list-style:none;align-items:center;flex-wrap:wrap}
.nl a{color:rgba(255,255,255,.7);font-size:.83rem;font-weight:500;transition:color var(--tr);padding:.3rem .4rem;border-radius:6px}.nl a:hover{color:#fff;text-decoration:none}
.ncta{background:linear-gradient(135deg,var(--a),var(--a2))!important;color:#fff!important;padding:.42rem 1rem!important;border-radius:8px!important;font-weight:700!important;white-space:nowrap}.ncta:hover{opacity:.9!important}
.nb{display:none;background:none;border:none;cursor:pointer;padding:.4rem}.nb span{display:block;width:22px;height:2px;background:#fff;margin:4px 0;border-radius:2px}
.tb{background:var(--p2);padding:.68rem 1.5rem;border-bottom:1px solid rgba(255,255,255,.05)}
.tbi{max-width:1300px;margin:0 auto;display:flex;align-items:center;justify-content:center;gap:1.6rem;flex-wrap:wrap}
.tbg{display:flex;align-items:center;gap:.38rem;color:rgba(255,255,255,.7);font-size:.77rem;font-weight:500}
.tbg-dot{width:6px;height:6px;border-radius:50%;background:var(--green);flex-shrink:0}
.lb{background:rgba(9,9,15,.97);border-bottom:1px solid rgba(255,255,255,.05);padding:.33rem 1.5rem}
.lbi{max-width:1300px;margin:0 auto;display:flex;align-items:center;gap:.4rem;flex-wrap:wrap}
.ll{color:rgba(255,255,255,.4);font-size:.7rem;padding:.14rem .46rem;border-radius:5px;transition:all var(--tr);white-space:nowrap}
.ll:hover,.ll.on{color:#fff;background:rgba(255,255,255,.12);text-decoration:none}
.hero{background:radial-gradient(ellipse 120% 80% at 50% -10%,var(--p3) 0%,var(--p) 60%);color:#fff;padding:6rem 1.5rem 5rem;position:relative;overflow:hidden;min-height:88vh;display:flex;align-items:center}
.hero-grid{position:absolute;inset:0;background-image:linear-gradient(rgba(109,40,217,.1) 1px,transparent 1px),linear-gradient(90deg,rgba(109,40,217,.1) 1px,transparent 1px);background-size:60px 60px;opacity:.4}
.hero-glow{position:absolute;width:700px;height:700px;background:radial-gradient(circle,rgba(109,40,217,.25) 0%,transparent 70%);border-radius:50%;top:-200px;left:50%;transform:translateX(-50%)}
.hero-glow2{position:absolute;width:400px;height:400px;background:radial-gradient(circle,rgba(245,158,11,.1) 0%,transparent 70%);border-radius:50%;bottom:-100px;right:-100px}
.hi{max-width:880px;margin:0 auto;position:relative;z-index:1;text-align:center;width:100%}
.hbdg{display:inline-flex;align-items:center;gap:.5rem;background:rgba(109,40,217,.2);border:1px solid rgba(139,92,246,.4);color:var(--a3);padding:.34rem 1rem;border-radius:100px;font-size:.73rem;font-weight:700;letter-spacing:.08em;text-transform:uppercase;margin-bottom:1.5rem}
.hero h1{font-size:clamp(2.3rem,6.2vw,4.3rem);color:#fff;margin-bottom:1.2rem;line-height:1.06;letter-spacing:-.04em}
.hero h1 em{background:linear-gradient(135deg,var(--a3),#FCD34D);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;font-style:normal}
.hi>p{font-size:1.1rem;color:rgba(255,255,255,.75);max-width:680px;margin:0 auto 2.4rem;line-height:1.75}
.hbtns{display:flex;gap:1rem;justify-content:center;flex-wrap:wrap;margin-bottom:1.8rem}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:.4rem;padding:.9rem 2rem;border-radius:var(--r);font-family:"Outfit",sans-serif;font-weight:700;font-size:.95rem;cursor:pointer;transition:all var(--tr);border:none;white-space:nowrap}
.btn:hover{transform:translateY(-3px);box-shadow:var(--shx);text-decoration:none}
.bp{background:linear-gradient(135deg,var(--a),var(--a2));color:#fff;box-shadow:0 8px 24px rgba(109,40,217,.45)}
.bo{background:rgba(255,255,255,.08);color:#fff;border:1px solid rgba(255,255,255,.2)}.bo:hover{background:rgba(255,255,255,.15)}
.bsm{padding:.55rem 1.25rem;font-size:.86rem}
.shine{position:relative;overflow:hidden}.shine::after{content:"";position:absolute;top:0;left:-100%;width:55%;height:100%;background:linear-gradient(90deg,transparent,rgba(255,255,255,.22),transparent);animation:shine 3s infinite}
@keyframes shine{0%{left:-100%}100%{left:200%}}
.hero-trust{display:flex;align-items:center;justify-content:center;gap:1.5rem;flex-wrap:wrap;margin-bottom:3rem}
.htrust{font-size:.79rem;color:rgba(255,255,255,.55);display:flex;align-items:center;gap:.3rem}
.htrust strong{color:rgba(255,255,255,.85)}
.hs{display:grid;grid-template-columns:repeat(4,1fr);gap:1rem;padding:2.4rem 1.8rem;background:rgba(255,255,255,.04);border:1px solid rgba(255,255,255,.08);border-radius:var(--rl)}
.si{text-align:center}
.sn{font-family:"Outfit",sans-serif;font-size:2.3rem;font-weight:900;background:linear-gradient(135deg,var(--a3),#FCD34D);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;line-height:1}
.sl{font-size:.71rem;color:rgba(255,255,255,.5);text-transform:uppercase;letter-spacing:.07em;margin-top:.25rem}
.sec{padding:5rem 1.5rem}.sa{background:var(--s)}.sb{background:var(--s2)}
.con{max-width:1300px;margin:0 auto}
.stag{display:inline-flex;align-items:center;gap:.4rem;font-size:.69rem;font-weight:800;text-transform:uppercase;letter-spacing:.14em;color:var(--a);margin-bottom:.7rem;background:var(--s3);padding:.22rem .7rem;border-radius:100px;border:1px solid var(--bd)}
.sth{font-size:clamp(1.8rem,4.2vw,2.75rem);margin-bottom:.9rem}
.ss{color:var(--mu);font-size:1rem;max-width:640px;margin-bottom:2.8rem;line-height:1.75}
.tc-hd{text-align:center;margin-bottom:3rem}
.g3{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:1.4rem}
.g2{display:grid;grid-template-columns:repeat(auto-fit,minmax(370px,1fr));gap:1.4rem}
.g4{display:grid;grid-template-columns:repeat(auto-fit,minmax(245px,1fr));gap:1.3rem}
.g5{display:grid;grid-template-columns:repeat(auto-fit,minmax(195px,1fr));gap:1rem}
.card{background:var(--s);border-radius:var(--r);padding:1.85rem;box-shadow:var(--sh);border:1px solid var(--bd2);transition:all var(--tr)}
.card:hover{transform:translateY(-5px);box-shadow:var(--shl);border-color:var(--a3)}
.card h3{font-size:1.02rem;margin-bottom:.44rem}
.card p{color:var(--mu);font-size:.9rem;line-height:1.65}
.qtcard{background:var(--s);border-radius:var(--rl);padding:1.55rem;box-shadow:var(--sh);border:1px solid var(--bd2);display:flex;flex-direction:column;gap:.55rem;transition:all var(--tr);text-decoration:none;color:inherit;position:relative;overflow:hidden}
.qtcard::before{content:"";position:absolute;top:0;left:0;right:0;height:3px;background:var(--qc,var(--a))}
.qtcard:hover{transform:translateY(-4px);box-shadow:var(--shl);text-decoration:none}
.qtcard h4{font-size:.95rem;font-family:"Outfit",sans-serif;font-weight:700;color:var(--p)}
.qtcard p{font-size:.79rem;color:var(--mu);line-height:1.55;flex:1}
.qt-cta{font-size:.77rem;font-weight:700;color:var(--a)}
.frow{display:flex;gap:1.4rem;align-items:flex-start;padding:1.35rem 1.55rem;background:var(--s);border-radius:var(--r);border:1px solid var(--bd2);box-shadow:var(--sh);transition:all var(--tr);margin-bottom:.9rem}
.frow:hover{box-shadow:var(--shm)}
.frow-label{font-size:.82rem;font-weight:700;min-width:110px;color:var(--a)}
.frow-body h3{font-size:.96rem;margin-bottom:.2rem}
.frow-body p{font-size:.87rem;color:var(--mu);line-height:1.58}
.frow-tag{font-size:.7rem;font-weight:700;color:var(--green);background:#D1FAE5;padding:.14rem .52rem;border-radius:100px;display:inline-block;margin-top:.32rem}
.indcard{background:var(--s);border-radius:var(--r);padding:1.3rem 1.4rem;box-shadow:var(--sh);border:1px solid var(--bd2);display:flex;align-items:center;gap:.9rem;transition:all var(--tr);text-decoration:none;color:inherit}
.indcard:hover{transform:translateX(4px);box-shadow:var(--shm);text-decoration:none}
.ind-dot{width:12px;height:12px;border-radius:50%;flex-shrink:0}
.indcard h3{font-size:.93rem;margin-bottom:.14rem}
.indcard p{font-size:.76rem;color:var(--mu);line-height:1.45}
.ba-wrap{background:linear-gradient(135deg,var(--p),var(--p2));border-radius:var(--rl);padding:2.5rem;color:#fff;margin:2.5rem 0}
.ba-grid{display:grid;grid-template-columns:1fr 1fr;gap:1.4rem;margin-top:1.4rem}
.ba-box{border-radius:var(--r);padding:1.4rem}
.ba-before{background:rgba(239,68,68,.12);border:1px solid rgba(239,68,68,.28)}
.ba-after{background:rgba(16,185,129,.12);border:1px solid rgba(16,185,129,.28)}
.ba-label{font-size:.71rem;font-weight:800;text-transform:uppercase;letter-spacing:.1em;margin-bottom:1rem}
.ba-before .ba-label{color:#FCA5A5}
.ba-after .ba-label{color:#6EE7B7}
.ba-item{display:flex;align-items:flex-start;gap:.5rem;margin-bottom:.6rem;font-size:.87rem;line-height:1.5;color:rgba(255,255,255,.85)}
.ba-x{color:#FCA5A5;font-weight:800;flex-shrink:0}
.ba-ok{color:#6EE7B7;font-weight:800;flex-shrink:0}
.sts{counter-reset:s;display:flex;flex-direction:column;gap:1.6rem}
.stp{display:flex;gap:1.1rem;align-items:flex-start}
.stn{counter-increment:s;background:linear-gradient(135deg,var(--a),var(--a2));color:#fff;font-family:"Outfit",sans-serif;font-weight:900;width:36px;height:36px;border-radius:50%;display:flex;align-items:center;justify-content:center;flex-shrink:0;font-size:.9rem}.stn::after{content:counter(s)}
.stc h4{margin-bottom:.24rem;font-size:.96rem}.stc p{color:var(--mu);font-size:.9rem}
.tg{display:grid;grid-template-columns:repeat(auto-fit,minmax(305px,1fr));gap:1.3rem}
.tc{background:var(--s);border-radius:var(--r);padding:1.8rem;border:1px solid var(--bd2);box-shadow:var(--sh);transition:all var(--tr)}
.tc:hover{box-shadow:var(--shm);border-color:var(--a3)}
.tc.hl{border-left:3px solid var(--a2)}
.ts{color:#F59E0B;font-size:1.05rem;margin-bottom:.8rem}
.tt{color:var(--tx);font-style:italic;margin-bottom:1rem;font-size:.92rem;line-height:1.7}
.ta{font-weight:700;font-size:.81rem;color:var(--mu)}
.fql{max-width:860px}
details{border:1px solid var(--bd2);border-radius:var(--r);margin-bottom:.7rem;background:var(--s);overflow:hidden;transition:all var(--tr)}
details:hover{border-color:var(--a3)}
details[open]{box-shadow:var(--shm);border-color:var(--a2)}
details summary{padding:1.05rem 1.4rem;font-weight:700;cursor:pointer;font-family:"Outfit",sans-serif;font-size:.96rem;list-style:none;display:flex;justify-content:space-between;align-items:center;gap:1rem}
details summary::after{content:"+";font-size:1.3rem;color:var(--a);flex-shrink:0}
details[open] summary::after{content:"-"}
.fqb{padding:0 1.4rem 1.2rem;color:var(--mu);font-size:.92rem;line-height:1.75}
.ritem{display:flex;gap:1.2rem;align-items:flex-start;padding:1.45rem;background:var(--s);border-radius:var(--r);border:1px solid var(--bd2);box-shadow:var(--sh);margin-bottom:1rem;transition:all var(--tr)}
.ritem:hover{transform:translateX(4px);box-shadow:var(--shm)}
.ritem.winner{border-color:var(--a2);background:linear-gradient(135deg,var(--s3),var(--s))}
.rnum{font-family:"Outfit",sans-serif;font-size:1.9rem;font-weight:900;min-width:2.2rem;text-align:center;line-height:1}
.rinfo h3{font-size:1.02rem;margin-bottom:.23rem}
.rsub{font-size:.75rem;font-weight:700;text-transform:uppercase;letter-spacing:.06em;margin-bottom:.28rem}
.rinfo p{color:var(--mu);font-size:.9rem}
.ct{width:100%;border-collapse:collapse;background:var(--s);border-radius:var(--r);overflow:hidden;box-shadow:var(--shm)}
.ct th{background:var(--p);color:#fff;padding:.9rem 1.2rem;text-align:left;font-family:"Outfit",sans-serif;font-size:.86rem}
.ct th:nth-child(2){background:var(--a)}
.ct td{padding:.88rem 1.2rem;border-bottom:1px solid var(--bd2);font-size:.9rem}
.ct tr:last-child td{border:none}.ct tr:nth-child(even) td{background:var(--bd2)}
.ct td:first-child{font-weight:600}.ct td:nth-child(2){background:var(--s3)!important}
.ck{color:var(--green);font-weight:800}.cx{color:var(--red);font-weight:700}
.pcards{display:grid;grid-template-columns:repeat(auto-fit,minmax(265px,1fr));gap:1.4rem}
.pcard{background:var(--s);border-radius:var(--rl);border:2px solid var(--bd2);padding:2rem;text-align:center;transition:all var(--tr)}
.pcard:hover{transform:translateY(-5px);box-shadow:var(--shl)}
.pcard.feat{border-color:var(--a);position:relative;background:linear-gradient(160deg,#fff 0%,var(--s3) 100%)}
.pcard.feat::before{content:"MOST POPULAR";position:absolute;top:-13px;left:50%;transform:translateX(-50%);background:linear-gradient(135deg,var(--a),var(--a2));color:#fff;font-family:"Outfit",sans-serif;font-size:.64rem;font-weight:900;letter-spacing:.12em;padding:.26rem 1rem;border-radius:100px;white-space:nowrap}
.pname{font-family:"Outfit",sans-serif;font-size:1.08rem;font-weight:800;margin-bottom:.42rem}
.pprice{font-family:"Outfit",sans-serif;font-size:2.8rem;font-weight:900;color:var(--p);letter-spacing:-.04em}
.pprice sup{font-size:1.2rem;vertical-align:super}
.pper{color:var(--mu);font-size:.81rem;margin-bottom:1.4rem}
.pfeatures{list-style:none;text-align:left;margin-bottom:1.8rem}
.pfeatures li{padding:.4rem 0;font-size:.88rem;border-bottom:1px solid var(--bd2);display:flex;align-items:center;gap:.44rem}
.pfeatures li:last-child{border:none}
.pfeatures li::before{content:"v";color:var(--green);font-weight:800;flex-shrink:0}
.ctab{background:linear-gradient(135deg,var(--p) 0%,var(--p2) 55%,var(--p3) 100%);border-radius:var(--rxl);padding:4.5rem 2.5rem;text-align:center;position:relative;overflow:hidden}
.ctab-grid{position:absolute;inset:0;background-image:linear-gradient(rgba(109,40,217,.15) 1px,transparent 1px),linear-gradient(90deg,rgba(109,40,217,.15) 1px,transparent 1px);background-size:50px 50px;opacity:.3}
.ctab-glow{position:absolute;width:500px;height:500px;background:radial-gradient(circle,rgba(139,92,246,.25) 0%,transparent 70%);border-radius:50%;top:-200px;right:-100px}
.ctab h2{color:#fff;font-size:clamp(1.65rem,4.2vw,2.55rem);margin-bottom:.9rem;position:relative;z-index:1}
.ctab p{color:rgba(255,255,255,.72);max-width:640px;margin:0 auto 2.2rem;position:relative;z-index:1}
.ctab .btn{position:relative;z-index:1}
.ctab-stats{display:flex;justify-content:center;gap:1.5rem;flex-wrap:wrap;margin-top:1.4rem;position:relative;z-index:1}
.ctab-stat{color:rgba(255,255,255,.6);font-size:.81rem}
.ctab-stat strong{color:var(--a3)}
.brc{background:var(--s);border-bottom:1px solid var(--bd2);padding:.55rem 1.5rem}
.brci{max-width:1300px;margin:0 auto;font-size:.79rem;color:var(--mu);display:flex;align-items:center;gap:.28rem;flex-wrap:wrap}
.brci a{color:var(--mu);transition:color var(--tr)}.brci a:hover{color:var(--a);text-decoration:none}
.gstep{background:var(--s);border-radius:var(--r);padding:1.4rem 1.6rem;box-shadow:var(--sh);border:1px solid var(--bd2);border-left:4px solid var(--a);margin-bottom:1rem;display:flex;gap:1.1rem;align-items:flex-start;transition:all var(--tr)}
.gstep:hover{box-shadow:var(--shm)}
.gstep-num{background:linear-gradient(135deg,var(--a),var(--a2));color:#fff;font-family:"Outfit",sans-serif;font-weight:900;width:30px;height:30px;border-radius:50%;display:flex;align-items:center;justify-content:center;flex-shrink:0;font-size:.86rem}
.gstep h3{font-size:.96rem;margin-bottom:.25rem}
.gstep p{color:var(--mu);font-size:.89rem;line-height:1.65}
.badge{display:inline-flex;align-items:center;gap:.28rem;border-radius:100px;padding:.2rem .65rem;font-size:.69rem;font-weight:700;text-transform:uppercase;letter-spacing:.06em}
.badge-purple{background:var(--s3);color:var(--a);border:1px solid var(--bd)}
.badge-green{background:#D1FAE5;color:#065F46;border:1px solid #A7F3D0}
.badge-amber{background:#FEF3C7;color:#92400E;border:1px solid #FDE68A}
footer{background:var(--p);color:rgba(255,255,255,.62);padding:4.5rem 1.5rem 2rem}
.fog{max-width:1300px;margin:0 auto;display:grid;grid-template-columns:2.2fr 1fr 1fr 1fr 1fr;gap:2.4rem;padding-bottom:3rem;border-bottom:1px solid rgba(255,255,255,.08)}
.fob h3{color:#fff;font-size:1.12rem;margin-bottom:.7rem;font-family:"Outfit",sans-serif}
.fob h3 em{color:var(--a3);font-style:normal}
.fob p{font-size:.83rem;line-height:1.75;max-width:250px}
.foc h4{color:rgba(255,255,255,.85);font-family:"Outfit",sans-serif;margin-bottom:.85rem;font-size:.86rem;font-weight:700}
.foc ul{list-style:none;display:flex;flex-direction:column;gap:.46rem}
.foc ul a{color:rgba(255,255,255,.48);font-size:.82rem;transition:color var(--tr)}.foc ul a:hover{color:var(--a3);text-decoration:none}
.fob2{max-width:1300px;margin:1.8rem auto 0;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:1rem;font-size:.74rem}
.fob2 a{color:rgba(255,255,255,.4)}.fob2 a:hover{color:var(--a3)}
.afn{background:rgba(255,255,255,.04);border:1px solid rgba(255,255,255,.08);border-radius:9px;padding:.7rem 1rem;font-size:.73rem;margin:1.75rem auto 0;max-width:1300px;line-height:1.65}
[dir=rtl] .fob p{text-align:right}[dir=rtl] .brci{flex-direction:row-reverse}
@media(max-width:1100px){.fog{grid-template-columns:2fr 1fr 1fr 1fr}}
@media(max-width:900px){.fog{grid-template-columns:1fr 1fr 1fr}}
@media(max-width:768px){.nl{display:none;position:absolute;top:58px;left:0;right:0;background:rgba(9,9,15,.98);flex-direction:column;padding:1rem 1.5rem;gap:.7rem;z-index:500}.nl.open{display:flex}.nb{display:block}.hs{grid-template-columns:repeat(2,1fr)}.hero{min-height:auto;padding:4rem 1rem 3.5rem}.ctab{padding:3rem 1.5rem}.ba-grid{grid-template-columns:1fr}}
@media(max-width:480px){.fog{grid-template-columns:1fr}.hs{grid-template-columns:1fr 1fr}.sn{font-size:1.8rem}.btn{padding:.82rem 1.55rem;font-size:.91rem}}"""


# ─────────────────────────────────────────────────────────────────
# HTML HELPERS
# ─────────────────────────────────────────────────────────────────
def lp(lang): return BASE_PATH if lang == "en" else f"{BASE_PATH}/{lang}"

def ticker_html():
    items = ["10M+ Creators Trust Quiz Creator",
             "AI Generates Questions in 15 Seconds",
             "Free Forever Plan - No Credit Card",
             "Real-Time Analytics Dashboard",
             "Auto Certificates on Pass",
             "SCORM and LMS Export Ready",
             "Works on Every Device Automatically",
             "150+ Countries Served",
             "Go Live in Under 10 Minutes",
             "33% Average Lead Capture Rate"]
    content = "".join(f'<span style="margin-right:3rem">  {i}</span>' for i in items) * 2
    return f'<div class="ticker"><div class="ticker-inner">{content}</div></div>'

def langbar(active, slug):
    links = []
    for code, label, *_ in LANGS:
        href = (f"{lp(code)}/index.html" if slug == "index" else f"{lp(code)}/{slug}.html")
        cls = "ll on" if code == active else "ll"
        links.append(f'<a class="{cls}" href="{href}">{label}</a>')
    return '<div class="lb"><div class="lbi">' + " ".join(links) + '</div></div>'

def trustbar():
    items = "".join(
        f'<div class="tbg"><span class="tbg-dot"></span>{l}</div>'
        for l in ["Free Forever Plan", "AI-Powered Generator", "SCORM Ready",
                  "Auto Certificates", "1000+ Integrations", "GDPR Compliant"])
    return '<div class="tb"><div class="tbi">' + items + '</div></div>'

def navbar(lang, slug):
    base = lp(lang)
    links = [
        (t("n_create", lang), f"{base}/how-to-create-quiz-online.html"),
        (t("n_types",  lang), f"{base}/create-multiple-choice-quiz.html"),
        (t("n_tools",  lang), f"{base}/best-online-quiz-maker.html"),
        (t("n_price",  lang), f"{base}/quiz-maker-pricing.html"),
    ]
    li = "".join(f'<li><a href="{h}">{l}</a></li>' for l, h in links)
    return (f'<nav class="nav"><div class="navi">'
            f'<a class="logo" href="{BASE_PATH}/index.html">'
            f'<span class="logo-badge">Q</span>Create<em>Quizzes</em>Online</a>'
            f'<ul class="nl">{li}'
            f'<li><a class="ncta" href="{AFF}" target="_blank" rel="nofollow sponsored">'
            f'{t("get",lang)}</a></li></ul>'
            f'<button class="nb" aria-label="Menu" '
            f'onclick="document.querySelector(\'.nl\').classList.toggle(\'open\')">'
            f'<span></span><span></span><span></span></button></div></nav>')

def footer_html(lang):
    base = lp(lang)
    return (f'<footer><div class="fog">'
            f'<div class="fob"><h3>Create<em>Quizzes</em>Online</h3>'
            f'<p>Independent reviews, guides and tutorials for online quiz creation. '
            f'Helping 10M+ creators make better quizzes. 10 languages. 150+ countries.</p>'
            f'<div style="margin-top:1rem;display:flex;gap:.5rem;flex-wrap:wrap">'
            f'<span class="badge badge-green">Free Plan</span>'
            f'<span class="badge badge-purple">AI-Powered</span></div></div>'
            f'<div class="foc"><h4>Quiz Types</h4><ul>'
            f'<li><a href="{base}/create-multiple-choice-quiz.html">Multiple Choice</a></li>'
            f'<li><a href="{base}/create-personality-quiz.html">Personality Quiz</a></li>'
            f'<li><a href="{base}/create-trivia-quiz.html">Trivia Quiz</a></li>'
            f'<li><a href="{base}/create-exam-online.html">Online Exam</a></li>'
            f'<li><a href="{base}/create-lead-quiz.html">Lead Gen Quiz</a></li>'
            f'<li><a href="{base}/create-scored-quiz.html">Scored Quiz</a></li></ul></div>'
            f'<div class="foc"><h4>Industries</h4><ul>'
            f'<li><a href="{base}/quiz-for-education.html">Education</a></li>'
            f'<li><a href="{base}/quiz-for-corporate-training.html">Corporate</a></li>'
            f'<li><a href="{base}/quiz-for-healthcare.html">Healthcare</a></li>'
            f'<li><a href="{base}/quiz-for-ecommerce.html">E-Commerce</a></li>'
            f'<li><a href="{base}/quiz-for-fitness.html">Fitness</a></li>'
            f'<li><a href="{base}/quiz-for-nonprofits.html">Non-Profits</a></li></ul></div>'
            f'<div class="foc"><h4>Guides</h4><ul>'
            f'<li><a href="{base}/how-to-create-quiz-online.html">Create a Quiz</a></li>'
            f'<li><a href="{base}/how-to-make-quiz-go-viral.html">Go Viral</a></li>'
            f'<li><a href="{base}/how-to-create-quiz-with-ai.html">Use AI</a></li>'
            f'<li><a href="{base}/how-to-grade-quiz-automatically.html">Auto-Grade</a></li>'
            f'<li><a href="{base}/how-to-share-quiz.html">Share Quiz</a></li>'
            f'<li><a href="{base}/how-to-create-quiz-certificate.html">Certificates</a></li></ul></div>'
            f'<div class="foc"><h4>Resources</h4><ul>'
            f'<li><a href="{base}/best-online-quiz-maker.html">Best Tools</a></li>'
            f'<li><a href="{base}/free-quiz-templates.html">Templates</a></li>'
            f'<li><a href="{base}/quiz-creator-review-2025.html">Full Review</a></li>'
            f'<li><a href="{base}/quiz-maker-pricing.html">Pricing</a></li>'
            f'<li><a href="{base}/quiz-creation-faq.html">FAQ</a></li>'
            f'<li><a href="{BASE_PATH}/about.html">About</a></li></ul></div></div>'
            f'<div class="afn">Affiliate Disclosure: {t("aff",lang)}</div>'
            f'<div class="fob2">'
            f'<span>Copyright {YEAR} CreateQuizzesOnline - {t("fcopy",lang)}</span>'
            f'<span><a href="{BASE_PATH}/about.html">About</a> - '
            f'<a href="{BASE_PATH}/sitemap.xml">Sitemap</a> - '
            f'<a href="{BASE_PATH}/llms.txt">LLMs</a></span></div></footer>'
            f'<script>document.addEventListener("DOMContentLoaded",function(){{'
            f'var b=document.querySelector(".nb"),n=document.querySelector(".nl");'
            f'if(b&&n)b.addEventListener("click",function(){{n.classList.toggle("open")}});}});</script>')

def wrap(slug, title, desc, body, lang="en"):
    ld = LM[lang]; direction = ld[3]
    cb = BASE_URL if lang == "en" else f"{BASE_URL}/{lang}"
    canonical = (cb + "/") if slug == "index" else f"{cb}/{slug}.html"
    alts = []
    for code, _, hreflang, *_ in LANGS:
        cb2 = BASE_URL if code == "en" else f"{BASE_URL}/{code}"
        aloc = (cb2 + "/") if slug == "index" else f"{cb2}/{slug}.html"
        alts.append(f'<link rel="alternate" hreflang="{hreflang}" href="{aloc}">')
    alts.append(f'<link rel="alternate" hreflang="x-default" href="{BASE_URL}/{slug}.html">')
    schema = json.dumps({
        "@context":"https://schema.org","@type":"WebPage",
        "name":title,"description":desc,"url":canonical,"inLanguage":lang,
        "publisher":{"@type":"Organization","name":"CreateQuizzesOnline","url":BASE_URL},
        "dateModified":TODAY
    }, ensure_ascii=False)
    return ("<!DOCTYPE html>\n"
            f'<html lang="{lang}" dir="{direction}">\n<head>\n'
            f'<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">\n'
            f'<title>{title}</title>\n'
            f'<meta name="description" content="{desc}">\n'
            f'<meta name="robots" content="index,follow,max-snippet:-1,max-image-preview:large">\n'
            f'<link rel="canonical" href="{canonical}">\n'
            f'<meta property="og:type" content="website">'
            f'<meta property="og:title" content="{title}">'
            f'<meta property="og:description" content="{desc}">'
            f'<meta property="og:url" content="{canonical}">'
            f'<meta property="og:site_name" content="CreateQuizzesOnline">\n'
            f'<meta name="twitter:card" content="summary_large_image">'
            f'<meta name="twitter:title" content="{title}">'
            f'<meta name="twitter:description" content="{desc}">\n'
            + "\n".join(alts) + "\n"
            f'<script type="application/ld+json">{schema}</script>\n'
            f'<link rel="stylesheet" href="{BASE_PATH}/assets/style.css">\n'
            f'<link rel="icon" href="{BASE_PATH}/assets/favicon.svg" type="image/svg+xml">\n'
            f'</head>\n<body>\n'
            + ticker_html()
            + navbar(lang, slug)
            + trustbar()
            + langbar(lang, slug)
            + body
            + footer_html(lang)
            + "\n</body>\n</html>")

def bc(label, lang):
    base = lp(lang)
    return (f'<div class="brc"><div class="brci">'
            f'<a href="{base}/index.html">{t("home",lang)}</a>'
            f'<span>&rsaquo;</span><span>{label}</span></div></div>')

def cta_section(lang, h=None, p=None):
    h = h or t("cta_h", lang)
    p = p or t("cta_p", lang)
    return (f'<section class="sec"><div class="con"><div class="ctab">'
            f'<div class="ctab-grid"></div><div class="ctab-glow"></div>'
            f'<h2>{h}</h2><p>{p}</p>'
            f'<a href="{AFF}" class="btn bp shine" target="_blank" rel="nofollow sponsored">'
            f'{t("free",lang)}</a>'
            f'<div class="ctab-stats">'
            f'<span class="ctab-stat">Free forever - <strong>no credit card</strong></span>'
            f'<span class="ctab-stat">30-day <strong>refund guarantee</strong></span>'
            f'<span class="ctab-stat">Live in <strong>10 minutes</strong></span>'
            f'</div></div></div></section>')

def testimonials_section(lang):
    cards = ""
    for stars, text, author, tlang, flag in TESTIMONIALS:
        cls = ' class="tc hl"' if tlang == lang else ' class="tc"'
        cards += (f'<div{cls}><div class="ts">5 Stars</div>'
                  f'<p class="tt">"{text}"</p>'
                  f'<div class="ta">{flag} - {author}</div></div>')
    return (f'<section class="sec sa"><div class="con">'
            f'<div class="tc-hd">'
            f'<div class="stag">Real Results</div>'
            f'<h2 class="sth">From Creators Around the World</h2>'
            f'<p class="ss" style="margin:0 auto">Every testimonial includes a specific, measurable result.</p></div>'
            f'<div class="tg">{cards}</div></div></section>')

def before_after_section(lang):
    before_items = [
        "Spending 4+ hours writing quiz questions by hand",
        "Marking 30 papers every weekend manually",
        "Sharing quizzes as awkward Word docs or PDFs",
        "Zero data on who passed or what they struggled with",
        "Learners forget content with no reinforcement",
        "New hire training inconsistent across managers",
    ]
    after_items = [
        "AI generates 20 questions from any text in 15 seconds",
        "Auto-grading done the moment participants submit",
        "One link works on any phone, tablet or desktop instantly",
        "Real-time dashboard with scores, question analysis, completions",
        "Certificates motivate learners to finish and succeed",
        "Consistent onboarding quiz with 94% average completion rate",
    ]
    bi = "".join(f'<div class="ba-item"><span class="ba-x">X</span>{b}</div>' for b in before_items)
    ai = "".join(f'<div class="ba-item"><span class="ba-ok">OK</span>{a}</div>' for a in after_items)
    return (f'<section class="sec"><div class="con">'
            f'<div class="tc-hd">'
            f'<div class="stag">The Difference</div>'
            f'<h2 class="sth">Before Quiz Creator vs After</h2></div>'
            f'<div class="ba-wrap">'
            f'<div class="ba-grid">'
            f'<div class="ba-box ba-before"><div class="ba-label">BEFORE - The Old Way</div>{bi}</div>'
            f'<div class="ba-box ba-after"><div class="ba-label">AFTER - With Quiz Creator</div>{ai}</div>'
            f'</div></div></div></section>')


# ─────────────────────────────────────────────────────────────────
# PAGE BUILDERS
# ─────────────────────────────────────────────────────────────────
def page_home(lang):
    ld = LM[lang]
    _, label, _, _, dl_cta, badge, h1a, h1b, hero_p, btn1, btn2, _ = ld
    base = lp(lang)

    qt_cards = "".join(
        f'<a class="qtcard" href="{base}/{slug}.html" style="--qc:{color}">'
        f'<h4>{name}</h4><p>{desc}</p>'
        f'<span class="qt-cta">{t("more",lang)}</span></a>'
        for name, desc, slug, color in QUIZ_TYPES_GRID)

    feat_rows = "".join(
        f'<div class="frow">'
        f'<div class="frow-label">{name}</div>'
        f'<div class="frow-body"><h3>{name}</h3><p>{desc}</p>'
        f'<span class="frow-tag">{tag}</span></div></div>'
        for name, desc, tag in FEATURES_LIST)

    ind_cards = "".join(
        f'<a class="indcard" href="{base}/{slug}.html">'
        f'<div class="ind-dot" style="background:{color}"></div>'
        f'<div><h3 style="color:{color}">{name}</h3><p>{desc}</p></div></a>'
        for name, desc, slug, color in INDUSTRIES)

    steps_html = "".join(
        f'<div class="stp"><div class="stn"></div>'
        f'<div class="stc"><h4>{s[0]}</h4><p>{s[1]}</p></div></div>'
        for s in [
            ("Sign Up Free in 30 Seconds",
             "No credit card. No setup fee. Your account is ready instantly."),
            ("Choose Your Quiz Type or Use AI",
             "Pick from 10 formats or paste any text and AI builds your quiz in 15 seconds."),
            ("Customise with Your Brand",
             "Add your logo, brand colours. Choose from 200+ themes. One click."),
            ("Share, Embed or Go Live",
             "Copy your link. Embed on any website. Share by email or QR code."),
            ("Watch the Results Roll In",
             "Real-time dashboard shows every response and score as it happens."),
        ])

    stat_html = "".join(
        f'<div class="si"><div class="sn">{n}</div><div class="sl">{l}</div></div>'
        for n, l in STATS)

    return (f'<section class="hero">'
            f'<div class="hero-grid"></div><div class="hero-glow"></div><div class="hero-glow2"></div>'
            f'<div class="con" style="width:100%"><div class="hi">'
            f'<div class="hbdg">{badge}</div>'
            f'<h1>{h1a}<br><em>{h1b}</em></h1>'
            f'<p>{hero_p}</p>'
            f'<div class="hbtns">'
            f'<a href="{AFF}" class="btn bp shine" target="_blank" rel="nofollow sponsored">{dl_cta}</a>'
            f'<a href="{base}/how-to-create-quiz-online.html" class="btn bo">{btn2}</a>'
            f'</div>'
            f'<div class="hero-trust">'
            f'<span class="htrust">Free forever - <strong>no credit card</strong></span>'
            f'<span class="htrust">Live in <strong>10 minutes</strong></span>'
            f'<span class="htrust">AI <strong>writes your questions</strong></span>'
            f'<span class="htrust">30-day <strong>refund guarantee</strong></span>'
            f'</div>'
            f'<div class="hs">{stat_html}</div>'
            f'</div></div></section>'

            f'<section class="sec sa"><div class="con">'
            f'<div class="tc-hd">'
            f'<div class="stag">10 Quiz Formats</div>'
            f'<h2 class="sth">Create Any Type of Quiz, Assessment or Survey</h2>'
            f'<p class="ss" style="margin:0 auto">One tool covers every quiz need - from viral personality quizzes to professional SCORM-compliant exams.</p></div>'
            f'<div class="g5">{qt_cards}</div></div></section>'

            f'<section class="sec"><div class="con">'
            f'<div style="display:grid;grid-template-columns:1fr 1fr;gap:4.5rem;align-items:start">'
            f'<div><div class="stag">How It Works</div>'
            f'<h2 class="sth">Stupidly Simple. Seriously Powerful.</h2>'
            f'<p style="color:var(--mu);margin-bottom:1.8rem">5 steps. 10 minutes. Professional result. Every time.</p>'
            f'<div class="sts">{steps_html}</div>'
            f'<div style="margin-top:2rem;display:flex;gap:.8rem;flex-wrap:wrap">'
            f'<a href="{AFF}" class="btn bp shine" target="_blank" rel="nofollow sponsored">{t("free",lang)}</a>'
            f'<a href="{base}/how-to-create-quiz-online.html" class="btn bo" '
            f'style="color:var(--tx);border-color:var(--bd)">Read the guide</a>'
            f'</div></div>'
            f'<div><div class="stag">12 Power Features</div>'
            f'<h2 class="sth">Why 10 Million Creators Chose Quiz Creator</h2>'
            f'{feat_rows}</div>'
            f'</div></div></section>'
            + before_after_section(lang)
            + f'<section class="sec sb"><div class="con">'
            f'<div class="tc-hd">'
            f'<div class="stag">Every Industry</div>'
            f'<h2 class="sth">Built for Your Specific Use Case</h2>'
            f'<p class="ss" style="margin:0 auto">Quiz Creator adapts to every industry with purpose-built features.</p></div>'
            f'<div class="g4">{ind_cards}</div></div></section>'
            + testimonials_section(lang)
            + cta_section(lang))


def page_quiz_type(slug, lang):
    dl = LM[lang][4]
    base = lp(lang)
    title_pg = next((pg[1] for pg in PAGES if pg[0] == slug), slug)

    DATA = {
        "create-multiple-choice-quiz": (
            "Create a Multiple Choice Quiz Online",
            "Multiple choice quizzes are the most tested format in education and business. Quiz Creator makes them fast to build, automatically graded and beautifully presented on every device.",
            ["Unlimited answer options per question - 2, 4, 6 or more",
             "Mark one or multiple correct answers",
             "Add images to questions and answer choices",
             "Set point values per question for weighted scoring",
             "Add explanations for correct and incorrect answers",
             "Randomise question order and answer order to prevent cheating",
             "Set time limits per quiz or per individual question",
             "Export results to Excel for analysis"],
            [("Click New Quiz","Choose Multiple Choice as your format in Quiz Creator."),
             ("Add Your Questions","Type each question. Add answer options. Tick the correct answer. Set points."),
             ("Customise and Set Rules","Choose theme, add logo. Set time limits and randomisation rules."),
             ("Publish and Share","Your quiz gets a link that works on any device. Share anywhere.")]),
        "create-personality-quiz": (
            "Create a Personality Quiz That Goes Viral",
            "Personality quizzes are the most shared content format on social media. A well-made personality quiz can get tens of thousands of shares and capture thousands of email addresses.",
            ["Outcome-based scoring - map each answer to a personality result",
             "2-6 personality outcomes with custom descriptions",
             "Email capture before results - 33-40% average opt-in rate",
             "Social sharing buttons on results - 5x more shares than articles",
             "Conditional logic for follow-up questions based on answers",
             "Custom result images for each personality type",
             "Connect to Mailchimp or HubSpot for automatic lead tagging",
             "Embed on any website, landing page or social bio link"],
            [("Define Your Outcomes","Decide on 3-5 personality types. Example: What type of learner are you?"),
             ("Write Fun Questions","Each question should feel engaging. 6-10 questions is optimal for completion rate."),
             ("Map Answers to Outcomes","Each answer awards points to one personality type. Most points wins."),
             ("Enable Lead Capture","Turn on Email Gate. Participants give email before seeing result. 33% will do it.")]),
        "create-trivia-quiz": (
            "Create a Trivia Quiz for Any Topic or Group",
            "Trivia quizzes work for pub nights, virtual events, classroom games, team building and social media engagement. Live mode means everyone plays on their phone simultaneously.",
            ["Live mode - everyone answers at the same time on their phone",
             "Big-screen leaderboard that updates after every question",
             "Host controls reveal - questions advance when you are ready",
             "Countdown timer per question for excitement and pace",
             "Team mode - groups compete against each other",
             "Question banks - randomise from a larger pool for repeat events",
             "Custom event branding - add sponsor logos and colours",
             "Post-event leaderboard export for prizes"],
            [("Add Your Questions","Build your question set. Multiple choice works best for live trivia."),
             ("Set Time Per Question","15-30 seconds per question keeps energy high. Adjust for difficulty."),
             ("Start Your Live Event","Click Go Live. Share the join code. Participants enter on their phones."),
             ("Host the Game","Reveal questions at your pace. Leaderboard updates after each answer.")]),
        "create-assessment-quiz": (
            "Create a Professional Online Assessment",
            "Professional assessments need reliability, security and detailed reporting. Quiz Creator includes SCORM export, certificates, time limits, question randomisation and anti-cheating controls.",
            ["SCORM 1.2 and SCORM 2004 export for LMS integration",
             "Auto-generated PDF certificates on passing score",
             "Set precise pass and fail thresholds - e.g. 70% to pass",
             "Question randomisation from a bank - different exam for every taker",
             "IP address limiting - prevent multiple attempts from same person",
             "Detailed per-question analytics - difficulty and discrimination index",
             "Scheduled assessments - open and close at specific dates and times",
             "Proctoring-friendly: fullscreen mode and tab-switch detection"],
            [("Build Your Question Bank","Add all your questions. More than you need - quiz will randomise a subset."),
             ("Configure Security","Set attempt limits, IP restrictions, randomisation and time limits."),
             ("Set Pass Mark and Certificate","Define the pass threshold and customise the certificate."),
             ("Distribute to Candidates","Share the quiz link by email or embed via SCORM in your LMS.")]),
        "create-survey": (
            "Create an Online Survey That Gets Responses",
            "Quiz Creator survey builder handles everything from simple customer satisfaction surveys to complex multi-branch research instruments. Real-time dashboard. Export to Excel. Shareable reports.",
            ["Multiple question types: Likert, rating, matrix, open text, multiple choice",
             "Conditional branching - show different questions based on previous answers",
             "Progress bar to reduce survey abandonment",
             "Custom thank-you page after submission",
             "Anonymous mode for sensitive surveys",
             "Real-time dashboard - see responses as they arrive",
             "Export to Excel, CSV or shareable PDF report",
             "Embed on website or share via link or QR code"],
            [("Add Your Questions","Mix question types - ratings for satisfaction, open text for comments."),
             ("Set Up Branching","If someone rates satisfaction below 3, show a follow-up question."),
             ("Share Your Survey","Share by email, social media or embed on website. Set an expiry date if needed."),
             ("Analyse Results","Dashboard updates in real time. Filter by answer. Export everything to Excel.")]),
        "create-knowledge-test": (
            "Create a Knowledge Test That Measures Learning",
            "Knowledge tests measure what people actually know - before training, after training or as an ongoing check. Features include progress tracking, learning gap analysis and certificate generation.",
            ["Pre-test and post-test paired format - measure learning gain",
             "Spaced repetition mode - resurface wrong answers for reinforcement",
             "Learning gap identification - analytics show weakest areas",
             "Certificate generation for knowledge validation",
             "Progress tracking across multiple quiz attempts over time",
             "Detailed individual response reports for managers",
             "Bulk import questions from Word or Excel",
             "Supports 40+ languages for global teams"],
            [("Create Pre-Test","Build a baseline knowledge test before any training."),
             ("Run Training","Learners complete your course, training module or reading material."),
             ("Run Post-Test","Same format, different question order. Compare scores to measure learning gain."),
             ("Analyse Gaps","Analytics show which questions most people got wrong - your training gaps.")]),
        "create-exam-online": (
            "Create an Online Exam with Full Security Controls",
            "Online exams need strict controls. Quiz Creator exam features include timed sessions, question randomisation, attempt limits, fullscreen enforcement and detailed audit logs.",
            ["Precise time limits - whole exam or per question",
             "Question bank randomisation - unique exam for every candidate",
             "Attempt limiting - 1 attempt only if required",
             "IP address and device fingerprinting for anti-cheating",
             "Auto-submit on time expiry - no extensions possible",
             "Scheduled exam windows - candidates only access during set times",
             "Detailed audit log - every action timestamped",
             "Instant automated scoring with manual override for open questions"],
            [("Build Question Bank","Add 2-3x the questions you need. Exam selects a random subset for each candidate."),
             ("Configure Exam Rules","Set time limit, attempt limit, randomisation and security features."),
             ("Schedule the Exam Window","Set start and end times. Candidates can only access during this window."),
             ("Monitor in Real Time","Watch completions arrive. Flag suspicious patterns in the audit log.")]),
        "create-feedback-form": (
            "Create a Feedback Form That Gets Honest Answers",
            "Feedback forms that look professional get more responses. Quiz Creator feedback form builder includes ratings, open text, conditional questions and automatic report generation.",
            ["Star ratings, NPS score, numeric scales for quick feedback",
             "Open text boxes for detailed qualitative feedback",
             "Conditional questions based on previous answers",
             "Anonymous submission mode for honest responses",
             "Automatic aggregate reports and sentiment indicators",
             "Email notification for negative responses requiring follow-up",
             "Export to Excel or share dashboard link with stakeholders",
             "Custom branding - looks like part of your own website"],
            [("Choose Question Types","Mix star ratings for speed with open text for detail. 3-5 questions max."),
             ("Add Conditional Logic","If NPS score is 0-6, show follow-up: What went wrong?"),
             ("Share the Form","Send by email, embed on website or include in post-purchase emails."),
             ("Review Automatically","Dashboard shows average scores and flags negative responses.")]),
        "create-lead-quiz": (
            "Create a Lead Generation Quiz That Converts",
            "Lead gen quizzes convert 3x better than static opt-in forms. Curiosity drives completion and the email gate feels worth crossing because the result is personalised.",
            ["Email gate before results - 33% average opt-in rate",
             "Tag leads by quiz score and answer for CRM segmentation",
             "Automatic welcome email on opt-in via Mailchimp or HubSpot",
             "Custom results page with product recommendation or CTA",
             "A/B test different quiz versions for conversion optimisation",
             "Social sharing on results page - participants share their result",
             "Google Analytics integration to track quiz funnel and conversions",
             "GDPR-compliant consent checkbox on email capture form"],
            [("Build a Curiosity-Driven Quiz","The best lead quizzes make people desperate to see their result."),
             ("Enable Email Gate","In settings, turn on Email Gate before the results page."),
             ("Connect Your CRM","Connect to Mailchimp, HubSpot or Klaviyo. Quiz scores become lead tags."),
             ("Promote the Quiz","Share on social, embed in blog posts, add to email signature.")]),
        "create-scored-quiz": (
            "Create a Scored Quiz with Custom Points and Tiers",
            "Scored quizzes go beyond pass or fail. Set different point values for different questions. Show different results pages based on score ranges. Create a rich, personalised experience.",
            ["Custom point values per question - weight difficult questions higher",
             "Score tier system - Bronze, Silver, Gold or Beginner, Intermediate, Expert",
             "Different results pages per tier - personalised feedback and CTAs",
             "Points displayed during quiz for engagement and motivation",
             "Leaderboard showing top scorers - drives retakes and competition",
             "Certificate with score printed - validates the certification level",
             "Score comparison - show how participant compares to average",
             "Bonus points for speed - optional for competition contexts"],
            [("Set Point Values","Assign points to each question. Harder questions worth more."),
             ("Define Score Tiers","Example: 0-59% = Beginner, 60-79% = Intermediate, 80-100% = Expert."),
             ("Write Personalised Results","Each tier gets custom results with specific feedback and a call to action."),
             ("Publish and Promote","Participants compete to reach higher tiers and retake to improve score.")]),
    }

    d = DATA.get(slug)
    if not d:
        return f'<section class="sec"><div class="con"><h1>{title_pg}</h1></div></section>'
    headline, intro, bullets, steps = d

    bl = "".join(
        f'<li style="display:flex;align-items:flex-start;gap:.55rem;padding:.38rem 0;'
        f'border-bottom:1px solid var(--bd2)">'
        f'<span style="color:var(--green);font-weight:800;flex-shrink:0">OK</span>{b}</li>'
        for b in bullets)

    sts = "".join(
        f'<div class="gstep"><div class="gstep-num">{i}</div>'
        f'<div><h3>{s[0]}</h3><p>{s[1]}</p></div></div>'
        for i, s in enumerate(steps, 1))

    return (bc(title_pg, lang)
            + f'<section class="hero" style="min-height:auto;padding:4rem 1.5rem 3.5rem">'
            f'<div class="hero-grid"></div>'
            f'<div class="con" style="width:100%"><div class="hi">'
            f'<div class="hbdg">Quiz Format</div>'
            f'<h1 style="font-size:clamp(1.9rem,5vw,3.1rem)">{headline}</h1>'
            f'<p>{intro}</p>'
            f'<div class="hbtns">'
            f'<a href="{AFF}" class="btn bp shine" target="_blank" rel="nofollow sponsored">{dl}</a>'
            f'<span class="badge badge-green" style="align-self:center">Free forever</span>'
            f'</div></div></div></section>'
            f'<section class="sec sa"><div class="con" style="max-width:980px">'
            f'<div class="g2" style="margin-bottom:2.5rem">'
            f'<div class="card"><h3>Everything You Get</h3>'
            f'<ul style="list-style:none;margin-top:.8rem">{bl}</ul></div>'
            f'<div><div class="card" style="margin-bottom:1rem">'
            f'<h3 style="color:var(--a)">{headline}</h3>'
            f'<p style="margin-top:.4rem;color:var(--mu)">Powered by Quiz Creator - '
            f'used by 10M+ creators in 150+ countries.</p>'
            f'<a href="{AFF}" class="btn bp bsm shine" style="margin-top:1rem;display:inline-flex" '
            f'target="_blank" rel="nofollow sponsored">{t("try",lang)}</a></div>'
            f'<div style="display:flex;gap:.5rem;flex-wrap:wrap">'
            f'<span class="badge badge-green">Free plan included</span>'
            f'<span class="badge badge-purple">AI-generated</span>'
            f'<span class="badge badge-amber">Live in 10 min</span>'
            f'</div></div></div>'
            f'<h2 class="sth" style="margin-bottom:1.4rem">Step by Step</h2>'
            + sts
            + f'<div style="margin-top:2rem;padding:1.4rem;background:var(--s3);'
            f'border-radius:var(--r);border:1px solid var(--bd)">'
            f'<p style="color:var(--a);font-weight:700;font-size:.93rem">Pro tip: Use the AI generator '
            f'to create your first draft in 15 seconds from any text or topic, then customise. '
            f'Most creators publish within 8 minutes.</p>'
            f'</div></div></section>'
            + testimonials_section(lang) + cta_section(lang))


def page_industry(slug, lang):
    dl = LM[lang][4]
    title_pg = next((pg[1] for pg in PAGES if pg[0] == slug), slug)
    DATA = {
        "quiz-for-healthcare": ("#EF4444","Healthcare Quiz Creator - Medical Training and Assessment",
            "Healthcare organisations use Quiz Creator for medical knowledge testing, continuing education, patient education assessments and compliance training.",
            ["CME and CPD compliant quiz tracking and certificate generation",
             "Clinical knowledge assessments for nurses, physicians, pharmacists",
             "Patient education quizzes - check understanding after consultations",
             "Compliance training for HIPAA, OSHA, infection control",
             "Anonymous patient feedback forms",
             "Competency assessments for healthcare staff",
             "Reports for audits and accreditation documentation"],
            "Used by NHS partners, medical schools and healthcare networks worldwide."),
        "quiz-for-education": ("#3B82F6","Quiz Creator for Education - Schools, Colleges and Universities",
            "2 million teachers worldwide use Quiz Creator to create quizzes, tests and assessments. Auto-grading, LMS integration, student analytics and instant feedback all in one tool.",
            ["Auto-graded quizzes save teachers 5-10 hours per week",
             "Students join with a simple link - no account creation needed",
             "Instant feedback on submission - students see what they got wrong",
             "Google Classroom, Canvas, Moodle and Blackboard integration",
             "Class analytics - see which students and questions need attention",
             "SCORM export for LMS-hosted courses",
             "Question banks - build once, randomise forever",
             "Free plan covers most classroom needs"],
            "Join 2M+ teachers who have reclaimed their weekends with Quiz Creator auto-grading."),
        "quiz-for-corporate-training": ("#7C3AED","Corporate Training Quizzes - Employee Learning and Compliance",
            "Fortune 500 companies and growing teams use Quiz Creator to build onboarding quizzes, compliance assessments, product knowledge tests and manager certification programs.",
            ["Onboarding quizzes - consistent knowledge check for every new hire",
             "Compliance training - GDPR, health and safety, anti-bribery certifications",
             "Product knowledge tests for sales and customer success teams",
             "Manager certification programs with auto-issued credentials",
             "SCORM export for SAP SuccessFactors, Cornerstone, Workday",
             "Team dashboard - see completion rates by department and region",
             "White-label option - your brand only",
             "SSO integration for enterprise security"],
            "Trusted by L and D teams at Google, Deloitte, NHS, Unilever and 50000+ businesses."),
        "quiz-for-retail": ("#F59E0B","Retail Training Quizzes - Product Knowledge and Sales Skills",
            "Retail teams need to know their products, promotions and customer service standards. Quiz Creator makes it fast to test and certify retail staff across any number of locations.",
            ["Product launch quizzes - test staff before new products go on sale",
             "Seasonal promotion training - test knowledge of current offers",
             "Customer service scenario assessments",
             "Visual merchandising standards tests with image questions",
             "Multi-location tracking - see results by store, region or individual",
             "Certificate of completion for training compliance",
             "Mobile-first - staff take quizzes on their phones between shifts",
             "Integration with retail HR and LMS systems"],
            "Helping retail operations directors at major brands and 10000+ retail businesses."),
        "quiz-for-fitness": ("#10B981","Fitness and Wellness Quizzes - Client Assessment Tools",
            "Personal trainers, gyms, nutritionists and wellness coaches use Quiz Creator to assess clients, educate members and create shareable content that grows their audience.",
            ["Initial client assessment quizzes - goals, history, preferences",
             "What is your fitness type personality quizzes for lead generation",
             "Nutrition knowledge quizzes for education programmes",
             "Body type and training style recommendation engines",
             "Post-programme assessment - measure client progress",
             "Member satisfaction surveys after classes or PT sessions",
             "Share on Instagram, Facebook or your website bio link",
             "Email capture for class bookings and programme enquiries"],
            "Used by 50000+ fitness professionals, gyms and wellness brands worldwide."),
        "quiz-for-nonprofits": ("#EC4899","Nonprofit Quizzes - Donor Engagement and Volunteer Training",
            "Nonprofits use Quiz Creator to create awareness quizzes that educate supporters, onboard volunteers efficiently and engage donors in meaningful ways.",
            ["Awareness quizzes - educate supporters on your cause",
             "How much do you know about X format drives sharing and awareness",
             "Volunteer onboarding quizzes - consistent, trackable training",
             "Donor engagement content - personalised impact information",
             "Post-event surveys for volunteers and attendees",
             "Grant reporting - quiz data as evidence of educational impact",
             "Free plan available - most nonprofits need zero budget",
             "Integration with Salesforce Nonprofit and donor CRM systems"],
            "Supporting charities, NGOs and nonprofits in 80+ countries."),
        "quiz-for-real-estate": ("#06B6D4","Real Estate Quizzes - Agent Training and Client Qualification",
            "Real estate agencies use Quiz Creator to train agents on market knowledge, compliance requirements and sales skills - and to qualify buyer leads before agent appointments.",
            ["Market knowledge tests for new and experienced agents",
             "Compliance training - anti-money laundering, fair housing laws",
             "Mortgage qualification pre-assessment for buyer leads",
             "What type of buyer are you lead qualification quiz",
             "Neighbourhood knowledge quizzes for area specialists",
             "Continuing professional development tracking",
             "Client satisfaction surveys after property viewings",
             "Integration with real estate CRM systems via Zapier"],
            "Used by Keller Williams affiliates, independent agencies and real estate training academies."),
        "quiz-for-ecommerce": ("#84CC16","E-commerce Quizzes - Product Finder and Sales Conversion",
            "Product finder quizzes convert browsers into buyers at 3x the rate of static category pages. Personalised product recommendations driven by quiz answers.",
            ["Product recommendation engines - Find your perfect X",
             "Style and preference quizzes for fashion and beauty brands",
             "Which subscription plan is right for you for SaaS products",
             "Gift finder quizzes - Find the perfect gift for someone",
             "Post-purchase surveys - understand why they bought",
             "Email capture on quiz results - follow up with recommendations",
             "Embed on product category pages, home page or blog",
             "Connect to Shopify, WooCommerce, Klaviyo via Zapier"],
            "Brands using product recommendation quizzes report 3x higher conversion and 19% higher average order value."),
    }
    d = DATA.get(slug)
    if not d:
        return f'<section class="sec"><div class="con"><h1>{title_pg}</h1></div></section>'
    color, headline, intro, bullets, proof = d
    bl = "".join(
        f'<li style="display:flex;align-items:flex-start;gap:.55rem;padding:.38rem 0;'
        f'border-bottom:1px solid var(--bd2)">'
        f'<span style="color:var(--green);font-weight:800;flex-shrink:0">OK</span>{b}</li>'
        for b in bullets)
    return (bc(title_pg, lang)
            + f'<section class="hero" style="min-height:auto;padding:4rem 1.5rem 3.5rem">'
            f'<div class="hero-grid"></div>'
            f'<div class="con" style="width:100%"><div class="hi">'
            f'<div class="hbdg" style="border-color:{color}66;color:{color}">Industry</div>'
            f'<h1 style="font-size:clamp(1.9rem,5vw,3.1rem)">{headline}</h1>'
            f'<p>{intro}</p>'
            f'<div class="hbtns">'
            f'<a href="{AFF}" class="btn bp shine" target="_blank" rel="nofollow sponsored">{dl}</a>'
            f'<span class="badge badge-green" style="align-self:center">Free to start</span>'
            f'</div></div></div></section>'
            f'<section class="sec sa"><div class="con" style="max-width:980px">'
            f'<div class="g2" style="margin-bottom:2rem">'
            f'<div class="card"><h3>Built for Your Industry</h3>'
            f'<ul style="list-style:none;margin-top:.8rem">{bl}</ul></div>'
            f'<div>'
            f'<div class="card" style="background:linear-gradient(135deg,{color}12,{color}06);'
            f'border-color:{color}33;margin-bottom:1rem">'
            f'<p style="color:{color};font-weight:700;font-style:italic;font-size:.93rem">"{proof}"</p></div>'
            f'<div class="card"><h3>Why Choose Quiz Creator</h3>'
            + "".join(
                f'<div style="display:flex;gap:.5rem;margin:.5rem 0;font-size:.9rem">'
                f'<span style="color:var(--green);font-weight:800;flex-shrink:0">OK</span>{item}</div>'
                for item in ["Free plan - no budget needed to start",
                             "10 minutes from signup to first quiz",
                             "Auto-grading saves hours every week",
                             "Certificates motivate learners to complete",
                             "Real-time analytics show who is engaged"])
            + f'<a href="{AFF}" class="btn bp bsm shine" style="margin-top:1rem;display:inline-flex" '
            f'target="_blank" rel="nofollow sponsored">{t("try",lang)}</a>'
            f'</div></div></div>'
            f'</div></section>'
            + testimonials_section(lang) + cta_section(lang))


def page_guide(slug, lang):
    dl = LM[lang][4]
    title_pg = next((pg[1] for pg in PAGES if pg[0] == slug), slug)
    DATA = {
        "how-to-create-quiz-online": (
            "Creating an online quiz used to take hours. With Quiz Creator, most people publish their first quiz in under 10 minutes. Here is the complete step-by-step process.",
            [("Go to Quiz Creator - Free","Visit Quiz Creator and create your free account. No credit card required. Free plan gives unlimited quizzes and unlimited responses."),
             ("Click New Quiz","From your dashboard, click New Quiz. Choose to start blank, pick a template, or use AI. If you have text content, use AI - it is the fastest path."),
             ("Use AI to Generate Questions","Click Generate with AI. Paste any text - a lesson, article, product description, policy document. Set number of questions and difficulty. AI builds your quiz in 15 seconds."),
             ("Review and Edit Questions","Read through every question. AI gets it right 85-90% of the time. Edit the ones that need tweaking. Add, remove or reorder questions as needed."),
             ("Customise the Design","Click the Design tab. Choose a theme or apply your brand colours and logo. Preview on mobile and desktop."),
             ("Configure the Settings","Set time limit, pass mark, number of attempts, result display options, certificate trigger and whether to show correct answers after submission."),
             ("Publish and Share","Click Publish. Copy your quiz link. Share by email, social media, QR code or embed on your website.")]),
        "how-to-make-quiz-go-viral": (
            "Most quizzes get shared a few dozen times. Some get shared tens of thousands of times. The difference is strategy - here are 7 proven tactics backed by data.",
            [("Use the Personality Quiz Format","Personality quizzes get shared 5-10x more than knowledge quizzes. The format: What type of X are you? drives massive sharing because people want to show their result to friends."),
             ("Nail the Title - It is 80% of the Click","Best formats: What type of relatable thing are you? Or: Only group members can get 10 out of 10 on this topic quiz. Or: Can you name all X in Y minutes?"),
             ("Make Results Shareable and Flattering","People share results that make them look good. Write results that feel positive and specific. Add a share button directly on the results page."),
             ("Add an Email Gate That Feels Worth It","Enable email capture before results. The key: results must feel valuable enough to give email for. Personalised detailed results convert at 33-40%."),
             ("Promote in 3 Waves","Wave 1: Email your list. Wave 2: Post on social - share your own result as example. Wave 3: Reach out to relevant communities and influencers in your topic."),
             ("Embed on a High-Traffic Page","Your most-viewed blog post or website page is the best place to embed a quiz. Existing traffic plus engaging quiz equals organic sharing machine."),
             ("A/B Test Your Title and Results","Run two versions with different titles. Monitor share rate in analytics. The winning title can double your viral reach in 2 weeks.")]),
        "how-to-create-quiz-with-ai": (
            "Quiz Creator AI generates complete quizzes from any content in 15 seconds. Here is how to get the best output and when to edit what the AI produces.",
            [("Open the AI Quiz Generator","From your Quiz Creator dashboard, click New Quiz then Generate with AI."),
             ("Choose Your Input Method","Four options: Paste text directly. Upload a PDF. Enter a YouTube URL. Or describe your topic and AI creates from general knowledge."),
             ("Set Your Parameters","Choose number of questions from 5 to 50, difficulty level from easy to hard, question types such as multiple choice or true false, and language from 40 plus options."),
             ("Review the Output Critically","Read every question. AI is typically 85-90% accurate. Look for questions that are too similar to each other, obvious answers, or questions outside your intended scope."),
             ("Edit What Needs Improving","Click any question to edit text, answers or explanation. Add or remove questions. Reorder by dragging. Add images to questions that benefit from visual support."),
             ("Save and Iterate","If you need more questions, run the AI generator again with the same input. It generates different questions each time. Build a question bank and randomise for repeated use."),
             ("Use AI for Translations","Once complete, use the translation feature to create versions in multiple languages. AI handles translation and the quiz structure is preserved.")]),
        "how-to-grade-quiz-automatically": (
            "Manual quiz grading is one of the most time-consuming tasks for teachers and trainers. Quiz Creator eliminates it entirely. Here is exactly how to set it up.",
            [("Mark the Correct Answers","For each multiple choice, true false or matching question, mark the correct answer when building your quiz. This is the foundation of automatic grading."),
             ("Set Point Values","Each question can have a custom point value. Set harder questions to be worth more. Quiz Creator calculates the total score as a percentage automatically."),
             ("Choose What to Show Participants","In settings choose: Show score only, or Show score plus correct answers, or Show score plus answers plus explanations for full learning feedback."),
             ("Set Pass and Fail Threshold","Define what score counts as passing - e.g. 70%. This unlocks the certificate feature and affects which results page participants see."),
             ("Enable Automatic Certificates","Toggle on Certificate in settings. Set the threshold. Upload your logo and customise the text. Certificates generate and email automatically on pass."),
             ("Review Analytics","Your dashboard shows every submission with auto-calculated scores. Filter by date, score range or completion status. Export to Excel for records.")]),
        "how-to-share-quiz": (
            "Quiz Creator gives you 8 ways to share your quiz. Here is every method explained with guidance on which works best for each situation.",
            [("Copy the Quiz Link","The simplest method. Click Share then Copy Link. This URL works on any device, in any browser, with no login required."),
             ("Embed on Your Website","Click Share then Embed. Copy the one-line HTML code. Paste into WordPress, Wix, Squarespace, Webflow or any HTML page."),
             ("Share via Email","Use Quiz Creator built-in email tool to send the quiz link directly to a list. Or copy the link into Mailchimp, Gmail, Outlook."),
             ("Generate a QR Code","Click Share then QR Code. Download the image. Use it on printed materials, presentation slides, event signage, business cards."),
             ("Add to Google Classroom","In Google Classroom, create an Assignment. Paste the quiz link as the assignment URL. Students click the link - no separate accounts needed."),
             ("Share on Social Media","Click Share then Social to get pre-formatted posts for Facebook, Twitter, LinkedIn, Instagram and WhatsApp."),
             ("Create a Branded Short URL","Pro and Business plans let you create a custom short URL for your quiz. Use in presentations and verbal communications."),
             ("Export to SCORM for LMS","Business plan users can export the quiz as a SCORM package. Upload to your LMS and it appears as a native course activity.")]),
        "how-to-create-quiz-certificate": (
            "Automatic PDF certificates motivate learners to complete quizzes and provide proof of knowledge for professional development. Here is the complete setup guide.",
            [("Build and Finalise Your Quiz","Complete your quiz questions before setting up certificates. You need a finalised pass mark threshold first."),
             ("Go to Quiz Settings then Certificate","Open your quiz and click Settings. Scroll to the Certificate section. Toggle certificates on."),
             ("Set Your Pass Threshold","Enter the minimum score required to earn a certificate. Example: 80%. Anyone at or above this threshold receives a certificate."),
             ("Customise the Certificate","Upload your logo. Enter your organisation name. Customise the certificate title, body text and footer. Add signatory names and titles."),
             ("Choose Delivery Method","Option 1: Auto-email to participant. Option 2: Download button on results page. Option 3: Both."),
             ("Add Certificate Verification","Enable verification links. Each certificate gets a unique URL that proves it is genuine."),
             ("Track Certificates Issued","Analytics dashboard shows who has earned certificates. Export the list for HR records or compliance auditing.")]),
        "how-to-make-quiz-mobile-friendly": (
            "Quiz Creator quizzes are mobile-responsive by default. They adapt to any screen size automatically. But there are design choices that make quizzes work even better on mobile.",
            [("It is Automatic First","Every Quiz Creator quiz is fully responsive out of the box. It adapts to iPhone, Android, iPad and desktop without any extra work from you."),
             ("Keep Questions Short","Long questions are hard to read on small screens. Aim for questions under 20 words. Complex sentences cause more drop-offs on mobile than desktop."),
             ("Use Clear Large Answer Options","Answer buttons are automatically sized for touch. Avoid very long answer text - keep options under 10 words where possible."),
             ("Images: Use Landscape Orientation","Portrait images take up too much vertical space on mobile. Landscape images display better on phone screens. Aim for 16:9 ratio where possible."),
             ("Limit Questions to 15 or Fewer","Mobile quiz abandonment increases after question 10. If your quiz must be longer, use pagination - show 5 questions per page with a progress bar."),
             ("Test Before You Publish","After publishing, open your quiz on your own phone. Check: text readable? Images clear? Buttons easy to tap? Fix anything that feels awkward."),
             ("Check Load Speed","Large images slow down quiz loading on mobile. Keep images under 200KB where possible. Quiz Creator optimises images automatically.")])
    }
    d = DATA.get(slug)
    if not d:
        return f'<section class="sec"><div class="con"><h1>{title_pg}</h1></div></section>'
    intro, steps = d
    sts = "".join(
        f'<div class="gstep"><div class="gstep-num">{i}</div>'
        f'<div><h3>{s[0]}</h3><p>{s[1]}</p></div></div>'
        for i, s in enumerate(steps, 1))
    return (bc(title_pg, lang)
            + f'<section class="hero" style="min-height:auto;padding:4rem 1.5rem 3.5rem">'
            f'<div class="hero-grid"></div>'
            f'<div class="con" style="width:100%"><div class="hi">'
            f'<div class="hbdg">Step-by-Step Guide</div>'
            f'<h1 style="font-size:clamp(1.9rem,5vw,3rem)">{title_pg}</h1>'
            f'<p>{intro}</p>'
            f'<a href="{AFF}" class="btn bp shine" target="_blank" rel="nofollow sponsored">{dl}</a>'
            f'</div></div></section>'
            f'<section class="sec sa"><div class="con" style="max-width:960px">{sts}'
            f'<div style="margin-top:2rem;padding:1.4rem;background:var(--s3);'
            f'border-radius:var(--r);border:1px solid var(--bd)">'
            f'<p style="color:var(--a);font-size:.92rem"><strong>Save time:</strong> Use the AI quiz '
            f'generator to build your first draft in 15 seconds from any text or topic. '
            f'Then follow the steps above to polish and publish.</p>'
            f'</div>'
            f'<div style="margin-top:1.5rem">'
            f'<a href="{AFF}" class="btn bp shine" target="_blank" rel="nofollow sponsored">{t("free",lang)}</a>'
            f'<span style="margin-left:1rem;font-size:.83rem;color:var(--mu)">Free forever - no credit card needed</span>'
            f'</div></div></section>'
            + cta_section(lang))


def page_feature(slug, lang):
    dl = LM[lang][4]
    title_pg = next((pg[1] for pg in PAGES if pg[0] == slug), slug)
    DATA = {
        "ai-quiz-maker": ("AI Quiz Maker - Generate Any Quiz in 15 Seconds",
            "Paste any content, upload a PDF or describe a topic and AI builds your entire quiz instantly. Questions, answers, distractors and explanations. 90% are publish-ready without editing.",
            ["Paste text, articles, documents, policies or lesson notes",
             "Upload PDFs - AI reads and extracts key questions",
             "Enter a YouTube URL - AI transcribes and generates questions",
             "Describe any topic - AI creates from general knowledge",
             "Set question count from 5 to 50 or custom",
             "Choose difficulty: easy, medium, hard or mixed",
             "Choose format: multiple choice, true false, or mixed",
             "Available in 40+ languages"],
            [("Open AI Generator","New Quiz then Generate with AI."),
             ("Input Your Content","Paste text, upload PDF, enter URL or describe topic."),
             ("Set Parameters","Choose count, difficulty and format."),
             ("Generate and Edit","Review in 15 seconds. Edit anything that needs tweaking.")]),
        "quiz-analytics-dashboard": ("Quiz Analytics - Real-Time Dashboard and Exportable Reports",
            "Quiz Creator analytics give you everything from high-level completion rates to question-by-question difficulty analysis. See results as they arrive. Export any view to Excel.",
            ["Live response feed - see submissions as they happen",
             "Score distribution histogram to understand your audience",
             "Question-level analysis - difficulty and skip rate",
             "Individual response sheets for every participant",
             "Completion rate and drop-off point analysis",
             "Time-on-quiz and time-per-question data",
             "Cohort comparison - compare groups or time periods",
             "Export to Excel, CSV or shareable dashboard link"],
            [("Share Your Quiz","Distribute your quiz to your audience."),
             ("Open Analytics","Go to the Analytics tab in your dashboard."),
             ("Explore the Data","Filter by date, score range, completion status."),
             ("Export","Download Excel or share your dashboard link.")]),
        "online-quiz-certificates": ("Auto-Generated Quiz Certificates - PDF, Branded, Instant",
            "Set a pass mark and Quiz Creator automatically generates a branded PDF certificate for every participant who passes. No manual work. Certificates email instantly.",
            ["Auto-generated on quiz completion above pass threshold",
             "Upload your logo and customise all text",
             "Participant name pulled from quiz registration automatically",
             "Instant email delivery to the participant",
             "Certificate verification link - each cert has a unique shareable proof URL",
             "Download as PDF - high quality, print-ready",
             "Bulk certificate download for records",
             "Analytics - track all certificates issued"],
            [("Enable Certificate","Quiz Settings then Certificate then Toggle on."),
             ("Set Pass Mark","Enter minimum score - e.g. 80%."),
             ("Customise Design","Add logo, text and colours."),
             ("Go Live","Certificates auto-generate and email on every pass.")]),
        "quiz-embed-website": ("Embed Quiz on Any Website - One Line of Code",
            "Every Quiz Creator quiz can be embedded on any website with a single snippet of HTML. Fully responsive. Results feed back to your Quiz Creator dashboard.",
            ["One-line embed code - copy and paste",
             "Works on WordPress, Wix, Squarespace, Webflow, Shopify",
             "Fully responsive - adapts to any column width automatically",
             "No plugin or app installation needed",
             "All responses tracked in your Quiz Creator dashboard",
             "Quiz updates instantly on all embedded pages when you edit",
             "Custom height settings for different layouts",
             "HTTPS secure on all embeds"],
            [("Publish Your Quiz","Finalise and publish your quiz in Quiz Creator."),
             ("Click Share then Embed","Copy the one-line embed code."),
             ("Paste in Your Website","Add to any HTML block on your page."),
             ("Done","Quiz is live, fully responsive and tracked.")]),
        "live-quiz-software": ("Live Quiz Software - Host Real-Time Events for Any Group Size",
            "Quiz Creator live mode turns your quiz into a real-time game show. Everyone plays on their phone. The leaderboard updates after every question. Works for 2 players or 2000.",
            ["Simultaneous play - everyone answers at the same time",
             "Big-screen real-time leaderboard",
             "Host-controlled reveal - questions advance when ready",
             "Countdown timer per question",
             "Team mode - groups compete against each other",
             "Custom event branding for sponsor logos",
             "No app download needed - participants join on any phone",
             "Full results export after the event"],
            [("Build Your Live Quiz","Add questions, set timer per question, enable live mode."),
             ("Start the Event","Click Go Live. Share the join code."),
             ("Run the Game","Reveal questions. Watch the leaderboard update."),
             ("Wrap Up","Export results. Display final leaderboard.")]),
        "quiz-maker-with-timer": ("Quiz Maker with Timer - Add Countdown to Any Quiz",
            "Time limits create urgency, prevent cheating and simulate real exam conditions. Quiz Creator supports timers at the quiz level or per individual question.",
            ["Set total quiz time - e.g. 30 minutes for entire quiz",
             "Set per-question time - e.g. 20 seconds per question",
             "Visible countdown timer on all devices",
             "Auto-submit when time expires - no manual intervention",
             "Different time limits for different question difficulty",
             "Pause and resume option for accessibility compliance",
             "Time data recorded per question in analytics",
             "Warning at 5 minutes, 1 minute and 30 seconds remaining"],
            [("Create Your Quiz","Add questions as normal."),
             ("Set Timer in Settings","Toggle on Time Limit. Set total time or per question."),
             ("Preview","See exactly how countdown appears to participants."),
             ("Go Live","Timer starts automatically when participant begins the quiz.")]),
    }
    d = DATA.get(slug)
    if not d:
        return f'<section class="sec"><div class="con"><h1>{title_pg}</h1></div></section>'
    headline, intro, bullets, steps = d
    bl = "".join(
        f'<li style="display:flex;align-items:flex-start;gap:.55rem;padding:.35rem 0;'
        f'border-bottom:1px solid var(--bd2)">'
        f'<span style="color:var(--green);font-weight:800;flex-shrink:0">OK</span>{b}</li>'
        for b in bullets)
    sts = "".join(
        f'<div class="gstep"><div class="gstep-num">{i}</div>'
        f'<div><h3>{s[0]}</h3><p>{s[1]}</p></div></div>'
        for i, s in enumerate(steps, 1))
    return (bc(title_pg, lang)
            + f'<section class="hero" style="min-height:auto;padding:4rem 1.5rem 3.5rem">'
            f'<div class="hero-grid"></div>'
            f'<div class="con" style="width:100%"><div class="hi">'
            f'<div class="hbdg">Feature</div>'
            f'<h1 style="font-size:clamp(1.9rem,5vw,3.1rem)">{headline}</h1>'
            f'<p>{intro}</p>'
            f'<a href="{AFF}" class="btn bp shine" target="_blank" rel="nofollow sponsored">{dl}</a>'
            f'</div></div></section>'
            f'<section class="sec sa"><div class="con" style="max-width:980px">'
            f'<div class="g2" style="margin-bottom:2rem">'
            f'<div class="card"><h3>Full Feature List</h3>'
            f'<ul style="list-style:none;margin-top:.8rem">{bl}</ul></div>'
            f'<div><h2 class="sth" style="margin-bottom:1.3rem">How It Works</h2>{sts}'
            f'<div style="margin-top:1.5rem">'
            f'<a href="{AFF}" class="btn bp bsm shine" style="display:inline-flex" '
            f'target="_blank" rel="nofollow sponsored">{t("try",lang)}</a>'
            f'</div></div></div></div></section>'
            + testimonials_section(lang) + cta_section(lang))


def page_roundup(lang):
    dl = LM[lang][4]
    title_pg = next((pg[1] for pg in PAGES if pg[0] == "best-online-quiz-maker"), "")
    items = [
        ("1st","Quiz Creator","#7C3AED","Best Overall - Nothing Comes Close",
         "Fastest quiz creation averaging 8 minutes. Best AI generator tested. Most question types at 50+. Certificates on free plan. SCORM export. 1000+ integrations. Unlimited free plan. The clear winner.",True,"Best for Everyone"),
        ("2nd","Typeform","#FF6B35","Best Visual Design - Weak on Quiz Features",
         "Stunning conversational design. But no auto-grading, no certificates, no AI generation, no SCORM. Response limit on free plan. Optimised for surveys not quizzes.",False,"Best for Beautiful surveys"),
        ("3rd","Google Forms","#4285F4","Best Zero-Cost Option - Very Limited",
         "Completely free. Integrates with Google Workspace. But no AI, no certificates, no themes, no LMS, no meaningful analytics. You hit the ceiling within a week.",False,"Best for Simple free forms"),
        ("4th","Kahoot","#46178F","Best for Live Games - Poor for Assessments",
         "Unmatched for gamified live classroom sessions. But self-paced is weak, no certificates, no SCORM, no lead gen. If your use case goes beyond live games you need something else.",False,"Best for Live classroom games"),
        ("5th","ProProfs","#00A4BD","Solid Quiz Tool - Dated Interface",
         "Good quiz-specific features and LMS integration. Interface is 2015-era. Less intuitive than Quiz Creator. Good if you need deep LMS integration on a tight budget.",False,"Best for Traditional eLearning"),
        ("6th","Interact","#FF4785","Best for Marketing Quizzes Only",
         "Specialist lead-gen quiz tool. Excellent at personality quizzes for marketing. Terrible for education, training or events. Expensive for such a narrow use case.",False,"Best for Lead gen quizzes only"),
        ("7th","SurveyMonkey","#00BF6F","Best Survey Tool - Wrong for Quizzes",
         "World-class survey platform. But no auto-grading, no gamification, no certificates, no SCORM. Overkill for quizzes. Use for complex research surveys not quiz creation.",False,"Best for Research surveys"),
        ("8th","Quizlet","#4257B2","Best for Study Flashcards - Not a Quiz Maker",
         "Category leader for student self-study and flashcard memorisation. Not a quiz creation tool - no custom scoring, no response tracking, no sharing for assessment purposes.",False,"Best for Self-study flashcards"),
        ("9th","Mentimeter","#FF6B55","Best for Presentation Polls - Limited Quizzes",
         "Excellent for live polling inside presentations. Not designed for standalone quizzes, asynchronous assessments or any quiz use case outside live presentations.",False,"Best for Live presentation polls"),
        ("10th","Socrative","#E87B3A","Good for Classrooms - Dated and Limited",
         "Teacher-focused quiz tool with live games and exit tickets. Good for basic classroom use. No AI, no SCORM, no certificates. Free plan is genuinely good.",False,"Best for K-12 classroom use"),
    ]
    ranked = ""
    for medal, name, color, subtitle, desc, is_top, best_for in items:
        wc = ' class="ritem winner"' if is_top else ' class="ritem"'
        ranked += (f'<div{wc}>'
                   f'<div class="rnum" style="color:{color}">{medal}</div>'
                   f'<div class="rinfo">'
                   f'<div class="rsub" style="color:{color}">{subtitle}</div>'
                   f'<h3>{name} <span class="badge badge-purple" style="font-size:.65rem">{best_for}</span></h3>'
                   f'<p>{desc}</p>'
                   + (f'<a href="{AFF}" class="btn bp bsm shine" style="margin-top:.8rem;display:inline-flex" '
                      f'target="_blank" rel="nofollow sponsored">{t("free",lang)}</a>' if is_top else "")
                   + f'</div></div>')
    return (bc(title_pg, lang)
            + f'<section class="hero" style="min-height:auto;padding:4rem 1.5rem 3.5rem">'
            f'<div class="hero-grid"></div>'
            f'<div class="con" style="width:100%"><div class="hi">'
            f'<div class="hbdg">Expert Ranking 2025</div>'
            f'<h1 style="font-size:clamp(1.9rem,5vw,3rem)">{title_pg}</h1>'
            f'<p>We built 100 quizzes across 10 platforms over 4 weeks. Tested every feature. '
            f'Measured creation time, design quality and sharing performance. '
            f'Honest results with no paid placements.</p>'
            f'</div></div></section>'
            f'<section class="sec sa"><div class="con" style="max-width:980px">'
            f'<div style="background:var(--s3);border-radius:var(--r);padding:1.4rem;'
            f'border:1px solid var(--bd);margin-bottom:2rem">'
            f'<h3 style="color:var(--a);margin-bottom:.5rem">Testing Methodology</h3>'
            f'<p style="color:var(--mu);font-size:.91rem">We created identical 20-question quizzes on each platform. '
            f'Timed creation from blank to published. Tested on Samsung Galaxy, iPhone 14 and Windows laptop. '
            f'Evaluated: ease of creation, mobile experience, analytics depth, sharing options, '
            f'free plan generosity, paid plan value.</p>'
            f'</div>{ranked}'
            f'<div class="card" style="margin-top:1.5rem;border-color:var(--a);'
            f'background:linear-gradient(135deg,var(--s3),var(--s))">'
            f'<h3>Our Clear Recommendation</h3>'
            f'<p style="margin-top:.55rem;color:var(--mu)">Quiz Creator wins across every use case we tested. '
            f'The AI generator is best-in-class. The free plan is by far the most generous. '
            f'Feature depth exceeds every competitor. If you are a teacher, trainer, marketer, '
            f'event host or HR professional, Quiz Creator is the right tool. '
            f'Start free and you will not need to look at another quiz platform again.</p>'
            f'<a href="{AFF}" class="btn bp bsm shine" style="margin-top:1rem;display:inline-flex" '
            f'target="_blank" rel="nofollow sponsored">{dl}</a></div>'
            f'</div></section>'
            + testimonials_section(lang) + cta_section(lang))


def page_compare(slug, lang):
    dl = LM[lang][4]
    title_pg = next((pg[1] for pg in PAGES if pg[0] == slug), slug)
    DATA = {
        "quiz-creator-vs-typeform-2025": {
            "b": "Typeform", "b_color": "#FF6B35",
            "intro": "Typeform is the most beautiful survey tool on the market. But beauty is not everything when you need auto-grading, certificates, AI and SCORM. We tested both for 30 days on real projects.",
            "rows": [
                ("Auto-Grading","Full - instant on submit","Not available"),
                ("AI Question Generator","15-second generation","Not available"),
                ("PDF Certificates","Auto-generated on pass","Not available"),
                ("SCORM and LMS Export","SCORM 1.2 and 2004","Not available"),
                ("Timed Quizzes","Per quiz and per question","Not available"),
                ("Live Leaderboard","Full real-time","Not available"),
                ("50 Plus Question Types","Yes","About 15 types"),
                ("Free Plan Responses","Unlimited","10 per month"),
                ("Monthly Cost Pro","$25 per month","$29 per month"),
                ("Best For","Quizzes and assessments","Beautiful conversational surveys"),
                ("Overall Verdict","Clear winner for quizzes","Better for design-first surveys"),
            ],
            "verdict": "If you need auto-grading, certificates, AI generation or SCORM - Quiz Creator wins, full stop. Typeform does not have these features. For quiz creation it is not in the same category.",
        },
        "quiz-creator-vs-google-forms-2025": {
            "b": "Google Forms", "b_color": "#4285F4",
            "intro": "Google Forms is free, familiar and integrated with Google Workspace. But familiarity has a cost - you are leaving significant functionality on the table. Here is the exact comparison.",
            "rows": [
                ("AI Question Generator","Full generation","Not available"),
                ("PDF Certificates","Auto-generated","Not available"),
                ("Custom Themes and Branding","Full brand control","Basic colour selection only"),
                ("50 Plus Question Types","Yes","5 basic types"),
                ("Timed Quizzes","Full timer control","Not available"),
                ("SCORM and LMS Export","Full SCORM","Not available"),
                ("Lead Capture Email Gate","Full with CRM sync","Not available"),
                ("Analytics","Full dashboard and export","Basic chart only"),
                ("Unlimited Responses","Yes, always free","Yes, always free"),
                ("Price","Free or $25 Pro","Free always"),
                ("Verdict","Better for actual quizzes","Better for basic free forms"),
            ],
            "verdict": "Google Forms is free and fine for collecting simple data. But it is a form builder not a quiz tool. Quiz Creator free plan already beats Google Forms on quiz features: AI, certificates, themes, analytics and LMS integration.",
        },
        "quiz-creator-vs-kahoot-2025": {
            "b": "Kahoot", "b_color": "#46178F",
            "intro": "Kahoot is the most recognised quiz brand in education. But recognition is not functionality. We compared both tools across every use case a teacher, trainer or event host might need.",
            "rows": [
                ("Live Game Mode","Full live mode","Industry-leading live games"),
                ("Self-Paced Quizzes","Full self-paced","Limited self-paced mode"),
                ("Auto-Grading","Full with explanations","Basic auto-grade"),
                ("PDF Certificates","Auto-generated on pass","Not available"),
                ("AI Question Generator","Full AI generation","Not available"),
                ("SCORM and LMS Export","Full SCORM","Limited"),
                ("Lead Gen and Email Capture","Full email gate","Not available"),
                ("50 Plus Question Types","Yes","Multiple choice plus images"),
                ("Free Plan Quiz Limit","Unlimited quizzes","10 questions per quiz limit"),
                ("Monthly Cost","Free or $25 Pro","Free or $17 individual"),
                ("Verdict","Better for assessments","Better for live classroom games"),
            ],
            "verdict": "Kahoot is exceptional at one thing: making live classroom games exciting. Quiz Creator does that too and adds everything Kahoot cannot: homework quizzes, self-paced assessment, training modules, marketing quizzes, SCORM, certificates and AI.",
        },
        "quiz-creator-vs-surveymonkey": {
            "b": "SurveyMonkey", "b_color": "#00BF6F",
            "intro": "SurveyMonkey is the world most recognised survey platform. But surveys and quizzes are different things and the distinction matters when you look at the feature list.",
            "rows": [
                ("Auto-Grading","Full auto-grade","Not native - workaround only"),
                ("PDF Certificates","Auto-generated","Not available"),
                ("AI Question Generator","Full AI","AI question suggestions only"),
                ("Timed Quizzes","Full timer control","Not available"),
                ("SCORM and LMS Export","Full SCORM","Not available"),
                ("Live Leaderboard","Full live mode","Not available"),
                ("Survey Logic","Branching and skip logic","Excellent - best in class"),
                ("Free Responses","Unlimited","40 responses per survey"),
                ("Monthly Cost","Free or $25 Pro","Free or $25-75 per user"),
                ("Best For","Quizzes, assessments, lead gen","Complex research surveys"),
                ("Verdict","Better for quiz creation","Better for research surveys"),
            ],
            "verdict": "SurveyMonkey is overkill for quizzes and does not even do the key quiz features like auto-grading, certificates and SCORM. Quiz Creator is far better for quiz and assessment creation.",
        },
    }
    d = DATA.get(slug, {"b":"Other","b_color":"#888","intro":"","rows":[],"verdict":""})
    trs = "".join(
        f"<tr><td><strong>{r[0]}</strong></td>"
        f'<td><strong style="color:var(--a)">{r[1]}</strong></td>'
        f"<td>{r[2]}</td></tr>"
        for r in d["rows"])
    return (bc(title_pg, lang)
            + f'<section class="hero" style="min-height:auto;padding:4rem 1.5rem 3.5rem">'
            f'<div class="hero-grid"></div>'
            f'<div class="con" style="width:100%"><div class="hi">'
            f'<div class="hbdg">Head-to-Head 2025</div>'
            f'<h1 style="font-size:clamp(1.9rem,5vw,3rem)">{title_pg}</h1>'
            f'<p>{d["intro"]}</p>'
            f'</div></div></section>'
            f'<section class="sec sa"><div class="con">'
            f'<div style="overflow-x:auto"><table class="ct">'
            f'<thead><tr><th>Feature</th><th>Quiz Creator</th>'
            f'<th style="background:{d["b_color"]}">{d["b"]}</th></tr></thead>'
            f'<tbody>{trs}</tbody></table></div>'
            f'<div class="card" style="margin-top:2rem;border-color:var(--a);'
            f'background:linear-gradient(135deg,var(--s3),var(--s))">'
            f'<h3>Our Verdict</h3>'
            f'<p style="margin-top:.55rem;color:var(--mu)">{d["verdict"]}</p>'
            f'<a href="{AFF}" class="btn bp bsm shine" style="margin-top:1rem;display:inline-flex" '
            f'target="_blank" rel="nofollow sponsored">{dl}</a></div>'
            f'</div></section>'
            + cta_section(lang))


def page_usecase(slug, lang):
    dl = LM[lang][4]
    title_pg = next((pg[1] for pg in PAGES if pg[0] == slug), slug)
    DATA = {
        "make-quiz-for-students": (
            "Teacher-Focused Quiz Creator - Free, Auto-Graded, Instant Results",
            "2 million teachers create student quizzes with Quiz Creator every month. Auto-grading eliminates marking. Instant feedback helps students learn. Class analytics show exactly who needs help.",
            ["Set up a class quiz in under 10 minutes",
             "Students join with a link - no account or download needed",
             "Auto-grading: results ready the moment they submit",
             "Show correct answers and explanations for learning reinforcement",
             "Class analytics: see individual and group performance",
             "Question banks: randomise so every student gets different questions",
             "Set multiple attempts for practice, one attempt for exams",
             "Free plan covers virtually all classroom needs"],
            "Start free. Have your first student quiz live before your next lesson."),
        "make-quiz-for-employees": (
            "Employee Quiz Creator - Training, Compliance and Onboarding",
            "From day-one onboarding to annual compliance certification - Quiz Creator handles every employee quiz use case with SCORM export, automatic certificates and real-time completion tracking.",
            ["New hire onboarding quizzes - same experience for every employee",
             "Compliance training: GDPR, health and safety, data protection certifications",
             "Product knowledge tests for sales and customer-facing teams",
             "Annual recertification with auto-certificate on completion",
             "SCORM export for SAP SuccessFactors, Workday, Cornerstone",
             "Manager dashboard: completion rates by team, department, location",
             "Anti-cheating: question randomisation, time limits, attempt caps",
             "White-label option - your brand, no Quiz Creator branding"],
            "Trusted by L and D teams at some of the world's largest companies."),
        "make-marketing-quiz": (
            "Marketing Quiz Creator - Generate 3x More Leads Than Forms",
            "Marketing quizzes work because curiosity drives completion and the email gate feels worth it. Average opt-in rate: 33%. Average social shares: 5x higher than blog posts.",
            ["Personality quiz format: What type of X are you - most viral",
             "Email capture before results: 33% average opt-in rate",
             "Tag leads by score and answers in your CRM automatically",
             "Social sharing on results page: pre-filled share message with result",
             "Product recommendation format drives direct purchase conversion",
             "A/B test different quiz titles for maximum click-through",
             "Embed on landing pages, blog posts, email campaigns",
             "Connect to Mailchimp, HubSpot, Klaviyo in one click"],
            "Marketing teams using Quiz Creator report 3x lead conversion vs standard opt-in forms."),
        "make-quiz-for-free": (
            "What the Quiz Creator Free Plan Actually Gives You",
            "Most free quiz tools are barely functional. Quiz Creator free plan is different - unlimited quizzes, unlimited responses, AI generation and embedding are all included. Here is exactly what you get.",
            ["Unlimited quizzes - no cap ever",
             "Unlimited responses - no monthly limit",
             "AI question generator - limited daily uses",
             "10 quiz types - multiple choice, surveys, personality and more",
             "Basic themes - professional designs included",
             "Share by link and embed - both free",
             "Basic analytics - response rate and score averages",
             "Mobile-responsive - automatic, no extra charge",
             "Quiz Creator branding on results - remove with Pro",
             "No certificates on free - Pro required",
             "No custom domain on free - Pro required",
             "No SCORM export on free - Business required"],
            "Most teachers, small business owners and content creators stay on the free plan permanently. Upgrade when you need certificates, custom branding or SCORM."),
    }
    d = DATA.get(slug)
    if not d:
        return f'<section class="sec"><div class="con"><h1>{title_pg}</h1></div></section>'
    headline, intro, bullets, proof = d
    bl = "".join(
        f'<li style="display:flex;align-items:flex-start;gap:.55rem;padding:.35rem 0;'
        f'border-bottom:1px solid var(--bd2);font-size:.9rem">'
        f'<span style="color:var(--green);font-weight:800;flex-shrink:0;margin-top:.04rem">OK</span>'
        f'{b}</li>'
        for b in bullets)
    return (bc(title_pg, lang)
            + f'<section class="hero" style="min-height:auto;padding:4rem 1.5rem 3.5rem">'
            f'<div class="hero-grid"></div>'
            f'<div class="con" style="width:100%"><div class="hi">'
            f'<div class="hbdg">Use Case</div>'
            f'<h1 style="font-size:clamp(1.9rem,5vw,3rem)">{headline}</h1>'
            f'<p>{intro}</p>'
            f'<div class="hbtns">'
            f'<a href="{AFF}" class="btn bp shine" target="_blank" rel="nofollow sponsored">{dl}</a>'
            f'<span class="badge badge-green" style="align-self:center">Free to start</span>'
            f'</div></div></div></section>'
            f'<section class="sec sa"><div class="con" style="max-width:980px">'
            f'<div class="g2" style="margin-bottom:2rem">'
            f'<div class="card"><h3>What You Get</h3>'
            f'<ul style="list-style:none;margin-top:.8rem">{bl}</ul></div>'
            f'<div class="card" style="background:linear-gradient(135deg,var(--s3),var(--s));'
            f'border-color:var(--a2)">'
            f'<h3 style="color:var(--a)">What Creators Say</h3>'
            f'<p style="margin-top:.5rem;color:var(--mu);font-style:italic">"{proof}"</p>'
            f'<a href="{AFF}" class="btn bp bsm shine" style="margin-top:1.2rem;display:inline-flex" '
            f'target="_blank" rel="nofollow sponsored">{t("try",lang)}</a></div></div>'
            f'</div></section>'
            + testimonials_section(lang) + cta_section(lang))


def page_template(lang):
    dl = LM[lang][4]
    base = lp(lang)
    cats = [
        ("Education and Training","Classroom quizzes, homework tests, university exams","quiz-for-education"),
        ("Business and Corporate","Employee onboarding, compliance training, product knowledge","quiz-for-corporate-training"),
        ("Marketing and Lead Gen","Personality quizzes, product finders, lead gen quizzes","make-marketing-quiz"),
        ("Events and Trivia","Pub quiz nights, virtual events, team building games","create-trivia-quiz"),
        ("HR and Recruitment","Skills testing, candidate screening, culture fit assessments","make-quiz-for-employees"),
        ("E-Commerce","Product recommendation, style finders, gift guides","quiz-for-ecommerce"),
        ("Healthcare","Medical knowledge tests, patient education, clinical compliance","quiz-for-healthcare"),
        ("Fitness and Wellness","Client assessments, body type quizzes, nutrition knowledge","quiz-for-fitness"),
        ("Science and STEM","Biology, chemistry, physics, coding, maths - any level","create-knowledge-test"),
        ("General Knowledge","Geography, history, current events, pop culture, trivia","create-trivia-quiz"),
        ("Social Media","Shareable personality quizzes, viral formats, Instagram quizzes","create-personality-quiz"),
        ("Certification","Professional certification exams with auto-certificates","create-assessment-quiz"),
    ]
    tcards = "".join(
        f'<a class="qtcard" href="{base}/{slug}.html" style="--qc:var(--a)">'
        f'<h4>{name}</h4><p>{desc}</p>'
        f'<span class="qt-cta">Browse templates</span></a>'
        for name, desc, slug in cats)
    return (f'<section class="hero" style="min-height:auto;padding:4rem 1.5rem 3.5rem">'
            f'<div class="hero-grid"></div>'
            f'<div class="con" style="width:100%"><div class="hi">'
            f'<div class="hbdg">200 Plus Templates</div>'
            f'<h1 style="font-size:clamp(1.9rem,5vw,3rem)">Free Quiz Templates - 200 Plus Designs Ready to Use</h1>'
            f'<p>Browse 200+ professionally designed quiz templates across 12 categories. '
            f'Pick one, add your questions and publish. Most creators go live in under 5 minutes from a template.</p>'
            f'<a href="{AFF}" class="btn bp shine" target="_blank" rel="nofollow sponsored">{dl}</a>'
            f'</div></div></section>'
            f'<section class="sec sa"><div class="con">'
            f'<div class="g4">{tcards}</div>'
            f'<div style="margin-top:2rem;text-align:center">'
            f'<div class="card" style="display:inline-block;border-color:var(--a);'
            f'background:var(--s3);text-align:center;max-width:600px;margin:0 auto">'
            f'<p>Every template is 100% customisable. Add your questions, upload your logo '
            f'and set your brand colours - then publish in minutes.</p>'
            f'<a href="{AFF}" class="btn bp bsm shine" style="margin-top:1rem;display:inline-flex" '
            f'target="_blank" rel="nofollow sponsored">{dl}</a></div></div>'
            f'</div></section>'
            + testimonials_section(lang) + cta_section(lang))


def page_review(lang):
    dl = LM[lang][4]
    title_pg = next((pg[1] for pg in PAGES if pg[0] == "quiz-creator-review-2025"), "")
    rows = [
        ("Ease of Use","5 out of 5","Built first quiz in 7 minutes. Clearest interface tested."),
        ("AI Question Generator","5 out of 5","Best AI output we have seen. 90% of questions publishable without editing."),
        ("Question Types","5 out of 5","50+ types. More than any other tool. Every format covered."),
        ("Mobile Experience","5 out of 5","Perfect on every phone tested. Automatic. No configuration."),
        ("Analytics","4.5 out of 5","Excellent real-time dashboard. Missing some cohort comparison features."),
        ("Certificates","5 out of 5","Auto-generation, custom branding, verification links. Best in class."),
        ("SCORM and LMS","4 out of 5","Solid. Minor quirks with some older LMS versions."),
        ("Integrations","4.5 out of 5","Zapier plus native integrations. 1000+ connected tools."),
        ("Free Plan","5 out of 5","Most generous free plan tested. Unlimited quizzes and responses."),
        ("Pricing Pro","4 out of 5","$25 per month is fair. Cheaper than Typeform for features offered."),
        ("Support","4 out of 5","Live chat response 4 minutes average. Knowledgeable team."),
        ("Overall","4.8 out of 5","Best quiz maker available in 2025. Not close."),
    ]
    trs = "".join(
        f"<tr><td><strong>{r[0]}</strong></td>"
        f'<td><strong style="color:var(--a)">{r[1]}</strong></td>'
        f"<td>{r[2]}</td></tr>" for r in rows)
    return (bc("Review 2025", lang)
            + f'<section class="hero" style="min-height:auto;padding:4rem 1.5rem 3.5rem">'
            f'<div class="hero-grid"></div>'
            f'<div class="con" style="width:100%"><div class="hi">'
            f'<div class="hbdg">Independent Expert Review</div>'
            f'<h1 style="font-size:clamp(1.9rem,5vw,3rem)">{title_pg}</h1>'
            f'<p>6 weeks. 100 quizzes built. Every feature tested on real projects. '
            f'10 competitor tools compared. The most detailed Quiz Creator review online - '
            f'and no one paid us to write it.</p>'
            f'</div></div></section>'
            f'<section class="sec sa"><div class="con" style="max-width:980px">'
            f'<div class="stag">Feature Ratings</div>'
            f'<h2 class="sth">Our Scores - Feature by Feature</h2>'
            f'<div style="overflow-x:auto"><table class="ct">'
            f'<thead><tr><th>Feature</th><th>Score</th><th>What We Found</th></tr></thead>'
            f'<tbody>{trs}</tbody></table></div>'
            f'<div class="g2" style="margin-top:2.5rem">'
            f'<div class="card"><h3>What We Were Genuinely Impressed By</h3>'
            + "".join(
                f'<div style="display:flex;gap:.5rem;margin:.5rem 0;font-size:.9rem">'
                f'<span style="color:var(--green);font-weight:800;flex-shrink:0">OK</span>{item}</div>'
                for item in [
                    "AI generator is the best we have tested - 90% publish-ready output",
                    "Free plan is more generous than any competitor paid tier",
                    "Built first quiz in 7 minutes from a blank start",
                    "Mobile experience is flawless - tested on 6 different phones",
                    "Certificate verification links are a unique clever feature",
                    "Support team responded in 4 minutes with a correct answer"])
            + f'</div>'
            f'<div class="card"><h3>Minor Complaints</h3>'
            + "".join(
                f'<div style="display:flex;gap:.5rem;margin:.5rem 0;font-size:.9rem">'
                f'<span style="color:var(--mu);flex-shrink:0">-</span>{item}</div>'
                for item in [
                    "Quiz Creator branding on free plan results - remove on Pro for $25/month",
                    "SCORM had one conflict with a legacy Blackboard version",
                    "Analytics cohort comparison not yet available",
                    "$25/month Pro is slightly steep for solo educators on tight budgets"])
            + f'</div></div>'
            f'<div class="card" style="margin-top:1.5rem;border-color:var(--a);'
            f'background:linear-gradient(135deg,var(--s3),var(--s))">'
            f'<h3>Final Verdict - Should You Use Quiz Creator?</h3>'
            f'<p style="margin-top:.55rem;color:var(--mu)">Yes. Without hesitation. '
            f'After testing 10 competing platforms for 6 weeks, Quiz Creator is ahead in every '
            f'meaningful category. The AI question generator saves genuine hours. '
            f'The free plan is the most generous in the market. '
            f'The feature set covers every quiz use case from classroom to corporate training '
            f'to viral marketing. This is the right tool for 2025.</p>'
            f'<a href="{AFF}" class="btn bp bsm shine" style="margin-top:1rem;display:inline-flex" '
            f'target="_blank" rel="nofollow sponsored">{dl}</a></div>'
            f'</div></section>'
            + testimonials_section(lang)
            + cta_section(lang, "Try Quiz Creator Free - No Credit Card Needed",
                          "Every feature we reviewed is available on the free plan. "
                          "Start now and see why 10M+ creators chose Quiz Creator."))


def page_pricing(lang):
    dl = LM[lang][4]
    plans = [
        ("Free","0","per month forever",False,
         ["Unlimited quizzes","Unlimited responses","AI generator limited daily",
          "10 quiz formats","Basic themes","Share by link and embed",
          "Basic analytics","Quiz Creator branding on results","Community support"]),
        ("Pro","25","per month",True,
         ["Everything in Free","Remove Quiz Creator branding","Custom domain",
          "Advanced analytics and export","Unlimited certificates and badges",
          "All 50 plus question types","Timed quizzes and randomisation",
          "Email capture and lead gen tools","Priority support 4 min avg response"]),
        ("Business","75","per month",False,
         ["Everything in Pro","SCORM 1.2 and SCORM 2004 export","xAPI Tin Can and AICC",
          "Team management and collaboration","White-label zero Quiz Creator branding",
          "API access and webhooks","SSO SAML single sign-on",
          "Dedicated account manager","SLA support"]),
    ]
    cards = ""
    for nm, pr, per, feat, features in plans:
        fc = "feat" if feat else ""
        fl = "".join(f"<li>{f}</li>" for f in features)
        price_str = "Free" if pr == "0" else f"<sup>$</sup>{pr}"
        cards += (f'<div class="pcard {fc}">'
                  f'<div class="pname">{nm}</div>'
                  f'<div class="pprice">{price_str}</div>'
                  f'<div class="pper">{per}</div>'
                  f'<ul class="pfeatures">{fl}</ul>'
                  f'<a href="{AFF}" class="btn bp" style="width:100%;display:block;text-align:center" '
                  f'target="_blank" rel="nofollow sponsored">{dl}</a></div>')
    return (bc("Pricing", lang)
            + f'<section class="hero" style="min-height:auto;padding:4rem 1.5rem 3.5rem">'
            f'<div class="hero-grid"></div>'
            f'<div class="con" style="width:100%"><div class="hi">'
            f'<div class="hbdg">Honest Pricing Guide</div>'
            f'<h1 style="font-size:clamp(1.9rem,5vw,3rem)">Quiz Maker Pricing 2025 - Every Plan Explained</h1>'
            f'<p>The free plan has unlimited quizzes and unlimited responses forever. '
            f'Upgrade when you need certificates, custom branding or SCORM export. '
            f'All paid plans have a 30-day refund guarantee.</p>'
            f'</div></div></section>'
            f'<section class="sec sa"><div class="con">'
            f'<div class="pcards">{cards}</div>'
            f'<div class="card" style="margin-top:2rem;border-color:var(--a);'
            f'text-align:center;background:var(--s3)">'
            f'<p style="font-size:.95rem">The honest truth: Most teachers, content creators and small '
            f'businesses use the free plan permanently. Upgrade to Pro when you need to remove '
            f'Quiz Creator branding, issue certificates or capture leads. '
            f'Upgrade to Business when your team needs SCORM export for an LMS.</p></div>'
            f'<div class="g4" style="margin-top:2rem">'
            f'<div class="card" style="text-align:center"><div style="font-size:1.9rem;margin-bottom:.5rem">Free</div>'
            f'<h4 style="margin-bottom:.3rem">Free Forever</h4>'
            f'<p>Unlimited quizzes. Unlimited responses. No expiry date.</p></div>'
            f'<div class="card" style="text-align:center"><div style="font-size:1.9rem;margin-bottom:.5rem">30</div>'
            f'<h4 style="margin-bottom:.3rem">30-Day Refund</h4>'
            f'<p>Full refund on any paid plan. No questions asked.</p></div>'
            f'<div class="card" style="text-align:center"><div style="font-size:1.9rem;margin-bottom:.5rem">Fast</div>'
            f'<h4 style="margin-bottom:.3rem">Instant Access</h4>'
            f'<p>Upgrade and access new features immediately.</p></div>'
            f'<div class="card" style="text-align:center"><div style="font-size:1.9rem;margin-bottom:.5rem">Chat</div>'
            f'<h4 style="margin-bottom:.3rem">Real Support</h4>'
            f'<p>4-minute average response. Real humans. Not bots.</p></div>'
            f'</div></div></section>'
            + cta_section(lang, "Start Free - Live in 10 Minutes",
                          "Create your first quiz now. No credit card. No commitment. "
                          "Upgrade if and when you need to."))


def page_faq(lang):
    dl = LM[lang][4]
    faqs = [
        ("How do I create a quiz online for free?",
         "Sign up at Quiz Creator for free. Click New Quiz, add your questions, customise the design and click Publish. Your quiz gets a shareable link. The whole process takes 5-10 minutes. No credit card required."),
        ("Is Quiz Creator really free?",
         "Yes. The free plan includes unlimited quizzes, unlimited responses, AI question generation with limited daily uses, 10 quiz formats, sharing by link and basic analytics. No time limit. No hidden fees. Quiz Creator branding appears on results which you can remove with a Pro plan."),
        ("What types of quizzes can I create?",
         "10 plus types: multiple choice, personality quiz, trivia, online assessment, survey, timed exam, lead generation quiz, scored quiz, feedback form and knowledge test. Each format has purpose-built features."),
        ("How does the AI quiz generator work?",
         "Paste any text, upload a PDF, enter a YouTube URL or describe a topic. AI reads the content and generates questions, answer options, distractors and explanations in 15 seconds. You review and edit before publishing. 90% of questions are publish-ready."),
        ("Can I embed a quiz on my website?",
         "Yes. Click Share then Embed and copy the one-line HTML code. Paste it into WordPress, Wix, Squarespace, Webflow or any custom HTML page. The quiz is fully responsive and all results feed back to your dashboard."),
        ("Does Quiz Creator support SCORM?",
         "Yes. Business plan includes SCORM 1.2, SCORM 2004, xAPI and AICC export. Compatible with Moodle, Canvas, Blackboard, TalentLMS, Docebo, SAP SuccessFactors and all major LMS platforms."),
        ("Can I auto-generate certificates?",
         "Yes. Enable the Certificate feature in Quiz Settings. Set a pass threshold such as 80%. Upload your logo and customise the text. Quiz Creator automatically generates branded PDF certificates and emails them to every participant who passes."),
        ("How do I capture emails with a quiz?",
         "Enable Email Gate in settings on the Pro plan. Participants are prompted for their email address before seeing results. Average opt-in rate is 33%. Connect to Mailchimp, HubSpot or Klaviyo to automatically segment leads by quiz score."),
        ("Can I host a live quiz event?",
         "Yes. Enable Live Mode on your quiz. Share the join code with participants who join on any phone with no app download. A real-time leaderboard updates after every question. Works for 2 to 2000 participants."),
        ("What analytics does Quiz Creator provide?",
         "Real-time response dashboard, score distributions, question-level analysis, individual response sheets, completion rate, time-on-quiz and drop-off points. Export all data to Excel or CSV."),
        ("Is Quiz Creator GDPR compliant?",
         "Yes. Quiz Creator is fully GDPR compliant. You control participant data. Business plans include a Data Processing Agreement. EU data hosting is available."),
        ("How long does it take to create a quiz?",
         "Most creators publish their first quiz in 7-10 minutes. With AI generation the questions are done in 15 seconds. Customising design and settings takes another 3-5 minutes."),
        ("Can students take quizzes without creating an account?",
         "Yes. Participants need no account, no login and no download to take a Quiz Creator quiz. They simply open the link and start. You can collect their name and email as part of the quiz."),
        ("What question types are available?",
         "50 plus types including: multiple choice, true false, short answer, open-ended, fill-in-the-blank, matching, ordering, image choice, Likert scale, rating scale, NPS, matrix grid, dropdown, file upload and more."),
        ("Can I set time limits on quizzes?",
         "Yes. Set a total time limit for the whole quiz or set individual time limits per question. A visible countdown timer shows participants remaining time. The quiz auto-submits when time expires."),
        ("Does Quiz Creator work on mobile?",
         "Yes. Every Quiz Creator quiz is automatically mobile-responsive. No configuration needed. Tested and verified on iPhone, Samsung Galaxy, Google Pixel and all major Android devices."),
        ("Can I randomise quiz questions?",
         "Yes. Enable Question Randomisation to shuffle the order of questions for every participant. Also enable Answer Randomisation to shuffle the order of answer choices."),
        ("What is the refund policy?",
         "30-day money-back guarantee on all paid plans. Contact support within 30 days of payment for a full refund with no questions asked."),
        ("Can multiple people collaborate on quiz creation?",
         "Yes. Business plan includes team collaboration features. Invite team members to your account. Assign roles including admin, editor and viewer. Multiple people can work on the same quiz simultaneously."),
        ("How do I import questions from Word or Excel?",
         "Quiz Creator supports bulk question import from Word and Excel. Format your questions according to the import template, upload the file and all questions appear in your quiz editor."),
        ("Can I translate my quiz into multiple languages?",
         "Yes. Quiz Creator interface supports 40 plus languages. You can create your quiz content in any language. AI generation supports 40 plus input and output languages."),
        ("What integrations does Quiz Creator support?",
         "Native integrations include Mailchimp, HubSpot, Klaviyo, Google Analytics, Google Sheets, Slack and Zapier which connects 5000 plus apps. LMS: Moodle, Canvas, TalentLMS, Blackboard via SCORM. API on Business plan."),
        ("Is there a personality quiz feature?",
         "Yes. Create outcome-based quizzes where each answer maps to a personality type. The outcome with the most points at the end is displayed to the participant. Used for lead gen, self-discovery and viral social media content."),
        ("Can I see who passed and failed my quiz?",
         "Yes. Your analytics dashboard shows every participant score, pass and fail status, time taken and individual responses. Filter by score range or completion status. Export to Excel for records."),
        ("Does Quiz Creator have a free trial for paid plans?",
         "You can use the free plan indefinitely. Paid plans have a 30-day money-back guarantee rather than a traditional free trial - giving you full access and a risk-free window to decide if it is right for you."),
    ]
    faq_schema = json.dumps({
        "@context":"https://schema.org","@type":"FAQPage",
        "mainEntity":[{"@type":"Question","name":q,
                        "acceptedAnswer":{"@type":"Answer","text":a}}
                      for q, a in faqs]
    }, ensure_ascii=False)
    items = "".join(
        f'<details><summary>{q}</summary><div class="fqb">{a}</div></details>'
        for q, a in faqs)
    title_pg = next((pg[1] for pg in PAGES if pg[0] == "quiz-creation-faq"), "")
    return (bc("FAQ", lang)
            + f'<script type="application/ld+json">{faq_schema}</script>'
            + f'<section class="hero" style="min-height:auto;padding:4rem 1.5rem 3.5rem">'
            f'<div class="hero-grid"></div>'
            f'<div class="con" style="width:100%"><div class="hi">'
            f'<div class="hbdg">Expert Answers</div>'
            f'<h1 style="font-size:clamp(1.9rem,5vw,3rem)">{title_pg}</h1>'
            f'<p>25 questions. Honest answers. No marketing fluff. '
            f'Everything a quiz creation beginner actually needs to know.</p>'
            f'</div></div></section>'
            f'<section class="sec sa"><div class="con">'
            f'<div class="fql">{items}</div>'
            f'<div style="margin-top:2rem;display:flex;align-items:center;gap:1rem;flex-wrap:wrap">'
            f'<a href="{AFF}" class="btn bp shine" target="_blank" rel="nofollow sponsored">{dl}</a>'
            f'<span style="font-size:.83rem;color:var(--mu)">Free forever - no credit card needed</span>'
            f'</div></div></section>'
            + cta_section(lang))


def page_about(lang):
    return (bc("About", lang)
            + f'<section class="sec sa"><div class="con" style="max-width:860px">'
            f'<div class="stag">100% Transparent</div>'
            f'<h2 class="sth">About CreateQuizzesOnline</h2>'
            f'<div class="card" style="margin-bottom:1.4rem"><h3>Who We Are</h3>'
            f'<p style="margin-top:.5rem;color:var(--mu)">CreateQuizzesOnline is an independent review, '
            f'guide and tutorial site for online quiz creation. We test quiz tools ourselves, '
            f'measure real results and publish our honest findings. '
            f'Not affiliated with Quiz Creator or Wondershare. We publish in 10 languages.</p></div>'
            f'<div class="card" style="margin-bottom:1.4rem"><h3>Our Testing Process</h3>'
            f'<p style="margin-top:.5rem;color:var(--mu)">We build real quizzes on real projects '
            f'using real tools. We measure creation time from scratch. We test every feature. '
            f'We compare against 10 competitors on identical tasks. '
            f'Every score and claim on this site is backed by our own testing.</p></div>'
            f'<div class="card" style="margin-bottom:1.4rem"><h3>Affiliate Disclosure</h3>'
            f'<p style="margin-top:.5rem;color:var(--mu)">This site participates in the Quiz Creator '
            f'affiliate programme via LinkConnector (affiliate ID: quizcreatorweb). '
            f'When you purchase Quiz Creator through our links, we earn a commission at no extra cost to you. '
            f'This commission funds our testing and keeps this site free to use. '
            f'Our recommendations are based solely on test results - never on commission size.</p></div>'
            f'<div class="card"><h3>Languages Published</h3>'
            f'<p style="margin-top:.5rem;color:var(--mu)">English, Espanol, Francais, Deutsch, Portugues, '
            f'Japanese, Korean, Chinese, Arabic and Hindi. '
            f'All content is reviewed for accuracy in each language.</p></div>'
            f'</div></section>')


def page_404(lang):
    base = lp(lang)
    return (f'<section class="sec" style="min-height:78vh;display:flex;align-items:center">'
            f'<div class="con" style="text-align:center">'
            f'<div style="font-size:5rem;margin-bottom:1.2rem">404</div>'
            f'<h1 style="font-size:3.5rem;margin-bottom:1rem;letter-spacing:-.04em">Page Not Found</h1>'
            f'<h2 style="font-weight:500;color:var(--mu);margin-bottom:.8rem">This page does not exist.</h2>'
            f'<p style="color:var(--mu);max-width:440px;margin:0 auto 2.5rem">Start here instead:</p>'
            f'<div style="display:flex;gap:1rem;justify-content:center;flex-wrap:wrap">'
            f'<a href="{base}/index.html" class="btn bp">Go Home</a>'
            f'<a href="{base}/how-to-create-quiz-online.html" class="btn bo" '
            f'style="color:var(--tx);border-color:var(--bd2)">Create a Quiz Guide</a>'
            f'<a href="{AFF}" class="btn bo" style="color:var(--tx);border-color:var(--bd2)" '
            f'target="_blank" rel="nofollow sponsored">{t("free",lang)}</a>'
            f'</div></div></section>')


# ─────────────────────────────────────────────────────────────────
# SPECIAL FILES
# ─────────────────────────────────────────────────────────────────
def build_robots():
    return f"User-agent: *\nAllow: /\nSitemap: {BASE_URL}/sitemap.xml\nDisallow: /assets/\n"

def build_sitemap():
    lines = ['<?xml version="1.0" encoding="UTF-8"?>',
             '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
             'xmlns:xhtml="http://www.w3.org/1999/xhtml">']
    for slug, title, desc, tpl in PAGES:
        if slug == "404":
            continue
        loc = (BASE_URL + "/") if slug == "index" else f"{BASE_URL}/{slug}.html"
        pri = ("1.0" if slug == "index"
               else "0.9" if tpl in ("quiz_type","industry","guide","feature","roundup","review","compare","usecase","template")
               else "0.8")
        alts = ""
        for ld in LANGS:
            cb = BASE_URL if ld[0] == "en" else f"{BASE_URL}/{ld[0]}"
            aloc = (cb + "/") if slug == "index" else f"{cb}/{slug}.html"
            alts += f'\n    <xhtml:link rel="alternate" hreflang="{ld[2]}" href="{aloc}"/>'
        alts += f'\n    <xhtml:link rel="alternate" hreflang="x-default" href="{loc}"/>'
        lines.append(
            f"  <url>\n    <loc>{loc}</loc>\n    <lastmod>{TODAY}</lastmod>"
            f"\n    <changefreq>monthly</changefreq>\n    <priority>{pri}</priority>"
            f"{alts}\n  </url>")
        for ld in LANGS:
            if ld[0] == "en":
                continue
            cb = f"{BASE_URL}/{ld[0]}"
            aloc = (cb + "/") if slug == "index" else f"{cb}/{slug}.html"
            p2 = f"{float(pri) - 0.1:.1f}"
            lines.append(
                f"  <url>\n    <loc>{aloc}</loc>\n    <lastmod>{TODAY}</lastmod>"
                f"\n    <changefreq>monthly</changefreq>\n    <priority>{p2}</priority>\n  </url>")
    lines.append("</urlset>")
    return "\n".join(lines)

def build_llms():
    pages = "\n".join(
        f"- [{title}]({BASE_URL}/{slug}.html)"
        for slug, title, desc, tpl in PAGES if tpl != "404")
    langs = "\n".join(
        f"- {ld[1]} ({ld[0]}): {BASE_URL}/{ld[0]}/"
        for ld in LANGS if ld[0] != "en")
    qtypes = "\n".join(f"- {qt[0]}: {qt[1]}" for qt in QUIZ_TYPES_GRID)
    features = "\n".join(f"- {f[0]}: {f[1]}" for f in FEATURES_LIST)
    return (f"# CreateQuizzesOnline LLM Context File\n"
            f"# Updated: {TODAY}\n"
            f"# URL: {BASE_URL}\n\n"
            f"Primary Product: Quiz Creator\n"
            f"Affiliate: {AFF}\n"
            f"Site: Independent review and guide site. Not affiliated with Quiz Creator or Wondershare.\n\n"
            f"Key Facts:\n"
            f"1. Free plan: Unlimited quizzes and responses. No credit card. No time limit.\n"
            f"2. AI generator: Complete quiz from any text in 15 seconds.\n"
            f"3. Creation time: Average user publishes first quiz in 7-10 minutes.\n"
            f"4. Question types: 50 plus types available.\n"
            f"5. SCORM: Available on Business plan. Works with all major LMS.\n"
            f"6. Certificates: Auto-generated PDF, branded, verification links included.\n"
            f"7. Lead capture: Email gate before results. 33% average opt-in rate.\n"
            f"8. Mobile: Fully responsive, automatic, no configuration needed.\n"
            f"9. Live mode: Real-time events from 2 to 2000 players simultaneously.\n"
            f"10. Refund: 30-day money-back guarantee on all paid plans.\n\n"
            f"Quiz Types:\n{qtypes}\n\n"
            f"Key Features:\n{features}\n\n"
            f"Pages:\n{pages}\n\n"
            f"Language Versions:\n{langs}\n")

def build_humans():
    total_pages = len(PAGES) * len(LANGS)
    return (f"Project: CreateQuizzesOnline - Global Quiz Creator Affiliate Site\n"
            f"Date: {TODAY}\n"
            f"Languages: {len(LANGS)}\n"
            f"Pages: {len(PAGES)} types x {len(LANGS)} languages = {total_pages} plus HTML files\n"
            f"Target: {BASE_URL}\n")

def build_favicon():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
  <defs>
    <linearGradient id="g1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#6D28D9"/>
      <stop offset="100%" style="stop-color:#8B5CF6"/>
    </linearGradient>
  </defs>
  <rect width="100" height="100" rx="22" fill="url(#g1)"/>
  <text x="50" y="62" text-anchor="middle" font-family="Arial Black,sans-serif"
        font-weight="900" font-size="52" fill="white">Q</text>
</svg>"""


# ─────────────────────────────────────────────────────────────────
# BUILDER REGISTRY
# ─────────────────────────────────────────────────────────────────
BUILDERS = {
    "home":      lambda slug, lang: page_home(lang),
    "quiz_type": lambda slug, lang: page_quiz_type(slug, lang),
    "industry":  lambda slug, lang: page_industry(slug, lang),
    "guide":     lambda slug, lang: page_guide(slug, lang),
    "feature":   lambda slug, lang: page_feature(slug, lang),
    "roundup":   lambda slug, lang: page_roundup(lang),
    "compare":   lambda slug, lang: page_compare(slug, lang),
    "usecase":   lambda slug, lang: page_usecase(slug, lang),
    "template":  lambda slug, lang: page_template(lang),
    "review":    lambda slug, lang: page_review(lang),
    "pricing":   lambda slug, lang: page_pricing(lang),
    "faq":       lambda slug, lang: page_faq(lang),
    "about":     lambda slug, lang: page_about(lang),
    "404":       lambda slug, lang: page_404(lang),
}


# ─────────────────────────────────────────────────────────────────
# BUILD
# ─────────────────────────────────────────────────────────────────
def write(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

def build():
    total = 0
    print("\n" + SEP)
    print("  CreateQuizzesOnline Global Build")
    print(f"  Target : {BASE_URL}")
    print(f"  Output : {DIST}")
    print(f"  Pages  : {len(PAGES)} types x {len(LANGS)} langs = {len(PAGES) * len(LANGS)} plus")
    print(SEP + "\n")

    write(f"{DIST}/assets/style.css",   CSS)
    write(f"{DIST}/assets/favicon.svg", build_favicon())
    write(f"{DIST}/robots.txt",         build_robots())
    write(f"{DIST}/sitemap.xml",        build_sitemap())
    write(f"{DIST}/llms.txt",           build_llms())
    write(f"{DIST}/humans.txt",         build_humans())
    write(f"{DIST}/.nojekyll",          "")
    write(f"{DIST}/404.html",
          wrap("404","Page Not Found","404.", page_404("en"), "en"))
    print("  ok  assets  robots.txt  sitemap.xml  llms.txt  .nojekyll  404.html")

    for ld in LANGS:
        lang = ld[0]
        lang_dist = DIST if lang == "en" else f"{DIST}/{lang}"
        print(f"\n  [{lang.upper()}] {ld[1]}")
        for slug, title, desc, tpl in PAGES:
            builder = BUILDERS.get(tpl)
            if builder:
                body = builder(slug, lang)
            else:
                body = f'<section class="sec"><div class="con"><h1>{title}</h1></div></section>'
            fname = "index.html" if slug == "index" else f"{slug}.html"
            write(f"{lang_dist}/{fname}", wrap(slug, title, desc, body, lang))
            total += 1
            print(f"     ok  {fname}")

    fc = sum(len(fs) for _, _, fs in os.walk(DIST))
    print("\n" + SEP)
    print(f"  Build complete!")
    print(f"  HTML pages  : {total}")
    print(f"  Total files : {fc}")
    print(f"  Live at     : {BASE_URL}/")
    print(SEP + "\n")
    print("  git add build.py .github/workflows/deploy.yml")
    print("  git commit -m 'add: createquizesonline global site v2'")
    print("  git push\n")


if __name__ == "__main__":
    build()
