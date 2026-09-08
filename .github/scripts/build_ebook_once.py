from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor, Color
from reportlab.lib.styles import ParagraphStyle,getSampleStyleSheet
from reportlab.lib.enums import TA_LEFT
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer,PageBreak,Table,TableStyle,KeepTogether
from reportlab.pdfgen import canvas
from pathlib import Path
import math
OUT='assets/ebooks/kurs-numerologii-ewa-milek.pdf'; W,H=A4
pdfmetrics.registerFont(TTFont('Serif','/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf'));pdfmetrics.registerFont(TTFont('SerifB','/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf'));pdfmetrics.registerFont(TTFont('Sans','/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'));pdfmetrics.registerFont(TTFont('SansB','/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'))
INK=HexColor('#2d213d');MUTED=HexColor('#6f6278');IND=HexColor('#6f4bc2');ROSE=HexColor('#d889b7');PAPER=HexColor('#fffafd');LINE=HexColor('#dfd0e6')
ss=getSampleStyleSheet(); BODY=ParagraphStyle('Body',fontName='Sans',fontSize=10.2,leading=15.1,textColor=MUTED,spaceAfter=8);H1=ParagraphStyle('H1',fontName='SerifB',fontSize=27,leading=31,textColor=INK,spaceAfter=11);H2=ParagraphStyle('H2',fontName='SerifB',fontSize=17,leading=21,textColor=INK,spaceBefore=10,spaceAfter=7);H3=ParagraphStyle('H3',fontName='SansB',fontSize=11.5,leading=15,textColor=IND,spaceBefore=7,spaceAfter=5);SMALL=ParagraphStyle('Small',fontName='Sans',fontSize=8.7,leading=12.5,textColor=MUTED);QUOTE=ParagraphStyle('Quote',fontName='Serif',fontSize=13.5,leading=20,textColor=HexColor('#68427d'),leftIndent=10*mm,rightIndent=10*mm,spaceBefore=8,spaceAfter=12)
def E(s):return s.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')
def P(s,st=BODY):return Paragraph(E(s),st)
def R(s,st=BODY):return Paragraph(s,st)
def butterfly(c,x,y,sc=.8,a=.15):
 c.saveState();c.setFillColor(Color(.43,.29,.76,alpha=a));c.ellipse(x-15*sc,y,x-2*sc,y+10*sc,fill=1,stroke=0);c.setFillColor(Color(.85,.54,.72,alpha=a));c.ellipse(x+2*sc,y,x+15*sc,y+10*sc,fill=1,stroke=0);c.setFillColor(Color(.18,.13,.24,alpha=a));c.rect(x-1*sc,y-5*sc,2*sc,12*sc,fill=1,stroke=0);c.restoreState()
def flower(c,x,y,sc=.7,a=.12):
 c.saveState();c.setFillColor(Color(.85,.54,.72,alpha=a));
 for d in range(0,360,60):
  r=math.radians(d);c.circle(x+math.cos(r)*8*sc,y+math.sin(r)*8*sc,5*sc,fill=1,stroke=0)
 c.setFillColor(Color(.43,.29,.76,alpha=a*1.2));c.circle(x,y,3*sc,fill=1,stroke=0);c.restoreState()
def page(c,d):
 c.saveState();c.setFillColor(PAPER);c.rect(0,0,W,H,fill=1,stroke=0);c.setFillColor(Color(.43,.29,.76,alpha=.055));c.circle(-15*mm,H-12*mm,42*mm,fill=1,stroke=0);c.setFillColor(Color(.85,.54,.72,alpha=.075));c.circle(W+8*mm,H-48*mm,53*mm,fill=1,stroke=0);butterfly(c,W-17*mm,H-24*mm,.7,.12);flower(c,12*mm,27*mm,.6,.09);c.setFont('SerifB',8.3);c.setFillColor(HexColor('#5a426b'));c.drawString(18*mm,H-11*mm,'EwaMiłek');c.setFont('Sans',6.5);c.setFillColor(HexColor('#9b8aa3'));c.drawRightString(W-18*mm,H-11*mm,'Kurs z Numerologii');c.setStrokeColor(Color(.43,.29,.76,alpha=.13));c.line(18*mm,14*mm,W-18*mm,14*mm);c.setFont('Sans',6.6);c.drawString(18*mm,9*mm,'ewamilek.pl  •  milekewa@o2.pl');c.setFont('Serif',8);c.drawRightString(W-18*mm,9*mm,str(d.page));c.restoreState()
def cover(c,d):
 c.saveState();c.setFillColor(PAPER);c.rect(0,0,W,H,fill=1,stroke=0);c.setFillColor(HexColor('#efe6fb'));c.circle(W*.84,H*.82,58*mm,fill=1,stroke=0);c.setFillColor(HexColor('#f7dfe9'));c.circle(W*.93,H*.88,40*mm,fill=1,stroke=0);c.setFillColor(HexColor('#f3e9ee'));c.circle(-12*mm,20*mm,45*mm,fill=1,stroke=0);butterfly(c,W*.74,H*.35,1.8,.27);flower(c,W*.15,H*.19,1.55,.18);c.setFillColor(IND);c.setFont('SansB',8);c.drawString(24*mm,H-34*mm,'EWA MIŁEK  •  NUMEROLOGIA');c.setFillColor(INK);c.setFont('SerifB',43);c.drawString(24*mm,H-75*mm,'Kurs z');c.setFillColor(HexColor('#985bb0'));c.setFont('Serif',43);c.drawString(24*mm,H-94*mm,'Numerologii');c.setFillColor(MUTED);c.setFont('Sans',12.5);c.drawString(24*mm,H-116*mm,'Praktyczne wskazówki, jak odczytywać datę urodzenia');c.setFillColor(HexColor('#593b70'));c.setFont('SerifB',16);c.drawString(24*mm,35*mm,'Ewa Miłek');c.setFont('Sans',7.5);c.setFillColor(HexColor('#9b8aa3'));c.drawString(24*mm,27*mm,'AUTORSKI E-BOOK • WERSJA 2026');c.restoreState()
about=['Życie jest dla mnie najlepszą szkołą. Rozwijam się poprzez relacje międzyludzkie, potrzebę serca i świadomie wybierany proces wzrastania. Od kilkunastu lat zawodowo zajmuję się numerologią. Zanim zaczęłam sporządzać Portrety Numerologiczne, przez kilka lat zgłębiałam tę obszerną wiedzę i sprawdzałam ją w praktyce.','Poprzez numerologię pokazuję, jak wiele talentów, możliwości i wewnętrznych zasobów może kryć się w każdym człowieku. Moją pasją jest również malowanie - Mandale i Anioły są ważną częścią mojej twórczej drogi. Joga pomaga mi się koncentrować, wyciszać i pracować z uważnością.','Ukończyłam Studium Psychologii Psychotronicznej oraz Szkołę Sztuk Pięknych. Jestem nauczycielką Vedic Art i prowadzę kursy malowania intuicyjnego. W 2018 roku wydałam tomik wierszy „Zapisane w Duszy”, zawierający 80 wierszy z przesłaniem.']
pos={1:'pomysłowość, samodzielność, inicjatywa, wiara we własne siły',2:'intuicja, wrażliwość, empatia, takt i współpraca',3:'towarzyskość, kreatywność, dynamizm i twórcza ekspresja',4:'solidność, odpowiedzialność, praktyczność i organizacja',5:'ruch, ciekawość świata, wolność, przygoda i odwaga',6:'rodzinność, opiekuńczość, czułość i harmonia',7:'analiza, dociekliwość, refleksja i poszukiwanie wiedzy',8:'konkret, dyscyplina, odpowiedzialność i skuteczność',9:'empatia, pomoc innym, współczucie i życzliwość'}
shadow={1:'wybuchowość, egoizm, nadmierna kontrola',2:'niepewność, zależność, nadmierna uczuciowość',3:'konfliktowość, krytycyzm, gadulstwo',4:'sztywność, rutyna, nieustępliwość',5:'impulsywność, niecierpliwość, niepokój',6:'zazdrość, krytycyzm, nadmierna kontrola',7:'izolacja, chłód, brak praktycyzmu',8:'agresja, żądza władzy, niezrównoważenie',9:'upór, smutek, lęk, rezygnacja'}
masters={11:'przekazywanie wiedzy, inspiracja, intuicja i rola nauczyciela',22:'potencjał sprawczy, budowanie i odpowiedzialność za wspólnotę',33:'miłość uniwersalna, współodczuwanie, służba i harmonia',44:'wytrwałość, profesjonalizm, samodyscyplina i realizacja dużych zadań',55:'odkrywanie, ciekawość, niezależność i pionierskie pomysły'}
karm={13:'praca, odpowiedzialność, cierpliwość i systematyczność',14:'wolność, granice i odpowiedzialne korzystanie z niezależności',16:'relacje, lojalność i odpowiedzialność uczuciowa',19:'władza, wpływ, szacunek dla innych i ich granic',26:'ciało, codzienna troska o siebie i równowaga'}
other={17:'osobista ochrona, intuicja i twórczość',27:'wrażliwość, inteligencja, współpraca i pomaganie',41:'ochrona w sferze zawodowej i społecznej, etyka i odpowiedzialność'}
doc=SimpleDocTemplate(OUT,pagesize=A4,leftMargin=18*mm,rightMargin=18*mm,topMargin=20*mm,bottomMargin=18*mm,title='Kurs z Numerologii - Ewa Miłek',author='Ewa Miłek')
st=[]
# cover is first page through page callback
st += [Spacer(1,245*mm),PageBreak(),P('Witaj…',H1),P('Dziękuję za zakup mojego e-booka. Cieszę się, że chcesz poznać tajniki numerologii i zobaczyć, jak można pracować z datą urodzenia.'),P('Poprowadzę Cię krok po kroku: od krótkiej historii i podstaw, przez obliczanie Drogi Życia, aż po znaczenia poszczególnych wibracji, liczb mistrzowskich i karmicznych.'),R('„Idź zawsze za głosem swojego serca i słuchaj, co ono Tobie podpowiada”.',QUOTE),Spacer(1,8*mm),P('COPYRIGHT © EWA MIŁEK 2021',H3),P('Autor: Ewa Miłek  •  Redakcja pierwotna: Mieszko Miłek  •  Redakcja i projekt wydania: 2026',SMALL),PageBreak()]
st += [P('Spis treści',H1),P('1. Kilka słów o mnie'),P('2. Historia numerologii'),P('3. O numerologii i jak działa'),P('4. Jak obliczyć Drogę Życia'),P('5. Droga Życia 1-9'),P('6. Ważne liczby: mistrzowskie i karmiczne'),P('7. Portret Numerologiczny'),P('8. Na zakończenie'),PageBreak()]
def chapter(n,title,lead):
 st.extend([P(f'ROZDZIAŁ {n}',H3),P(title,H1),P(lead),Spacer(1,4*mm)])
chapter(1,'Kilka słów o mnie','Numerologia, sztuka i intuicja w jednej drodze.')
for x in about:st.append(P(x))
st += [R('„Idź zawsze za głosem swojego serca i słuchaj, co ono Tobie podpowiada”.',QUOTE),PageBreak()]
chapter(2,'Historia numerologii','Skąd wzięła się fascynacja symboliką liczb.')
st += [P('Numerologia jest przedstawiana jako pradawna wiedza o symbolice liczb. W różnych kulturach liczby łączono z porządkiem świata, cyklami życia i znaczeniami przypisywanymi człowiekowi. W materiałach dotyczących numerologii często przywołuje się Egipt, Babilonię oraz tradycje greckie.'),P('Szczególne miejsce w historii numerologii zajmuje Pitagoras - grecki filozof i matematyk, któremu przypisuje się duży wpływ na rozwój zachodniego sposobu myślenia o liczbach.'),P('Ciekawostka',H2),R('„Liczby są uniwersalnym językiem oferowanym ludziom przez bóstwo jako potwierdzenie prawdy”.',QUOTE),P('Warto traktować historyczne i ezoteryczne przekazy o liczbach jako element tradycji symbolicznej, a nie jako współczesne ustalenia naukowe.',SMALL),PageBreak()]
chapter(3,'O numerologii','Co liczby mogą symbolicznie opowiadać o człowieku.')
st += [P('Liczby są wszędzie wokół nas i w nas. W numerologii każdej liczbie przypisuje się określone jakości, a data urodzenia, imiona i nazwiska traktowane są jako ważne elementy opisu człowieka.'),P('Przedmiotem numerologii są również nazwy własne, które można zamieniać na wartości liczbowe przez przyporządkowanie literom odpowiednich liczb, a następnie ich sumowanie.'),P('Jak działa numerologia?',H2),P('Kiedy po raz pierwszy spotkałam się z ideą wibracji liczb, podeszłam do niej z ciekawością, ale także z potrzebą sprawdzania. Korzystałam z książek, szkoleń i własnych analiz. Zaczęłam od swojej Drogi Życia.'),P('Z czasem numerologia stała się dla mnie sposobem porządkowania obserwacji dotyczących charakteru, aspiracji, talentów i źródeł inspiracji. Pojedyncza liczba nie powinna być etykietą - warto patrzeć na cały układ i konkretnego człowieka.'),PageBreak()]
chapter(4,'Jak obliczyć Drogę Życia','Trzy proste sposoby pracy z datą urodzenia.')
st += [P('Przykład: 10.12.1984',H2)]
for name,lines,result in [('Metoda wertykalna',['1 + 0 + 1 + 2 + 1 + 9 + 8 + 4 = 26','2 + 6 = 8'],'Wynik: 8 z podliczby 26.'),('Metoda horyzontalna',['10 + 12 + 1984 = 2006','2 + 0 + 0 + 6 = 8'],'Wynik: 8.'),('Metoda redukcji',['1 + 0 = 1; 1 + 2 = 3; 1 + 9 + 8 + 4 = 22','1 + 3 + 22 = 26; 2 + 6 = 8'],'Wynik: 8; warto zapisać też podliczby.')]:
 t=Table([[R('<b>'+name+'</b>',H3)],[R('<br/>'.join(lines),SMALL)],[P(result,SMALL)]],colWidths=[174*mm]);t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),HexColor('#fbf5fa')),('BOX',(0,0),(-1,-1),.6,LINE),('LEFTPADDING',(0,0),(-1,-1),6*mm),('RIGHTPADDING',(0,0),(-1,-1),6*mm),('TOPPADDING',(0,0),(-1,-1),4*mm),('BOTTOMPADDING',(0,0),(-1,-1),4*mm)]));st += [t,Spacer(1,4*mm)]
st += [P('Zapisuj zarówno wynik główny, jak i wartości pojawiające się przed redukcją.'),PageBreak()]
chapter(5,'Droga Życia 1-9','Pozytywne możliwości i obszary do obserwacji.')
st += [P('Poniższe opisy są skrótowym kompasem. Nie traktuj ich jak etykiet - jedna liczba nie opisuje całego człowieka.')]
for n in range(1,10):
 t=Table([[R(f'<b>{n}</b>',H2),R(f'<b>Potencjał:</b> {pos[n]}<br/><b>Cień / obszar do obserwacji:</b> {shadow[n]}',SMALL)]],colWidths=[18*mm,156*mm]);t.setStyle(TableStyle([('BACKGROUND',(0,0),(0,0),HexColor('#f2e8fa')),('BACKGROUND',(1,0),(1,0),HexColor('#fbf4f9')),('BOX',(0,0),(-1,-1),.5,LINE),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),4*mm),('RIGHTPADDING',(0,0),(-1,-1),4*mm),('TOPPADDING',(0,0),(-1,-1),3*mm),('BOTTOMPADDING',(0,0),(-1,-1),3*mm)]));st += [KeepTogether(t),Spacer(1,2*mm)]
st += [PageBreak()]
chapter(6,'Ważne liczby w numerologii','Liczby mistrzowskie, karmiczne i dodatkowe.')
st += [P('Numerologia opiera się na dziewięciu liczbach głównych: 1-9. W wielu szkołach analizuje się także liczby mistrzowskie i karmiczne oraz podliczby pojawiające się podczas obliczeń.'),P('Liczby mistrzowskie',H2)]
for n,v in masters.items():st += [P(f'Mistrzostwo {n}',H3),P(v+'.')]
st += [P('Liczby karmiczne',H2),P('W autorskim podejściu Ewy są traktowane jako symbole tematów, którym warto poświęcić więcej świadomości.')]
for n,v in karm.items():st += [P(f'Karmiczna {n}',H3),P(v+'.')]
st += [P('Inne ważne liczby',H2)]
for n,v in other.items():st += [P(str(n),H3),P(v+'.')]
st += [PageBreak()]
chapter(7,'Portret Numerologiczny','Jak połączyć pojedyncze liczby w szerszy obraz.')
st += [P('Portret Numerologiczny jest rozbudowanym opisem przygotowywanym na podstawie daty urodzenia, imion i nazwiska. W praktyce Ewy obejmuje m.in. Drogę Życia, talenty, wyzwania, cykle i szczyty życiowe oraz dodatkowe wibracje wynikające z imienia i nazwiska.'),P('Taki portret ma służyć lepszemu przyjrzeniu się własnym predyspozycjom, wyborom i relacjom. Dla dziecka może być dla rodziców inspiracją do obserwowania jego naturalnych talentów; dla dorosłych - punktem wyjścia do refleksji nad pracą, relacjami i kierunkiem rozwoju.'),P('Jeżeli chcesz zamówić Portret Numerologiczny lub zapytać o zakres analizy, napisz: milekewa@o2.pl.'),PageBreak()]
chapter(8,'Na zakończenie','Numerologia jako praktyka uważności i obserwacji.')
st += [P('Badanie liczb wymaga czegoś więcej niż jednorazowego przeczytania opisu. Warto analizować przykłady, robić własne notatki, porównywać obserwacje i z czasem budować własne rozumienie symboliki.'),P('Na początku szczególnie zachęcam do dostrzegania potencjału i pozytywnych możliwości danej wibracji. Zbyt szybkie przypisywanie komuś negatywnych cech może zamknąć rozmowę zamiast ją otworzyć.'),R('„Niech liczby będą zaproszeniem do refleksji, a nie gotową etykietą”.',QUOTE),Spacer(1,10*mm),P('Dziękuję, że jesteś tutaj.',H2),P('Ewa Miłek',H3)]
Path('assets/ebooks').mkdir(parents=True,exist_ok=True)
doc.build(st,onFirstPage=cover,onLaterPages=page)
print(OUT)
