A Határtorony 10 éjszakája

Konzolos tower defense / túlélőjáték Pythonban. A játékos 10 napon és éjszakán át védi a határtornyot: nappal erőforrásokat gyűjt és fejleszt, éjszaka pedig különböző támadásokat kell kivédenie.

Egyetemi projekt a Szoftverfolyamatok tárgy keretében (Szegedi Tudományegyetem, programtervező informatikus BSc).

Mit tud a játék?
10 nap, 10 éjszaka. Ha a játékos életereje vagy a torony élete elfogy, a játék véget ér. Aki túléli a 10. éjszakát, nyer.
Nappali szakasz: naponta 2 akció – fa, kő, étel és gyógynövény gyűjtése, torony javítása, csapdák és barikádok építése, főzetek készítése, pihenés, felderítés.
Éjszakai szakasz: eszköz használata (jelzőkürt, főzet), majd harci állás választása. A támadások három típusa: vadállatok, fosztogatók és ostrom.
Fejlesztések: minden éjszaka után választható egy fejlesztés véletlenszerűen felkínált lehetőségek közül.
Az általam készített részek

A projekt alapjátékát a tárgy keretében választottam ki. Az alábbi két funkciót és a hozzájuk tartozó teszteket én készítettem el, egyedül.

1. Nehézségi szintek (feature1.py)

A játék elején három szint közül lehet választani: könnyű, közepes, nehéz. A választás beállítja a kezdőértékeket és a szorzókat:

	Könnyű	Közepes	Nehéz
Támadás erőssége	×0,8	×1,1	×1,4

Gyűjtés hatékonysága	×1,2	×1,0	×0,7

Kezdő életerő (játékos / torony)	25 / 25	20 / 22	16 / 18

Kezdő fa és kő	7 és 7	4 és 4	2 és 2

Kezdő étel	6	4	2

Egyszer használatos eszközök	több	kevesebb	nincs
2. Véletlenszerű nappali események (feature2.py)

Minden nap elején 30% eséllyel történik valami, naponta legfeljebb egy esemény. Hat különböző esemény van:

elhagyott készletek megtalálása,
egy őr megsérül (életerő csökken),
vihar (csökken a gyűjtés hatékonysága),
megromlott étel,
vándor érkezik (védelmi bónusz a következő éjszakára),
felderítők térnek vissza (életerő nő, étel fogy, védelmi bónusz).
3. Tesztek (test_feature1.py, test_feature2.py)

A funkciókhoz pytest tesztek tartoznak, például azt ellenőrzik, hogy a nehézségi szintek a megfelelő szorzókat állítják be, és hogy a nappali események sosem okoznak hibát és nem hagynak negatív étel-készletet.

Futtatás

Szükséges: Python 3.

bash
python border_tower_game.py

A játék számok beírásával irányítható. A játék végén újra lehet kezdeni.

Tesztek futtatása
bash
pip install pytest
pytest
Fájlok
Fájl	Tartalom
border_tower_game.py	az alapjáték és a belépési pont
feature1.py	nehézségi szintek
feature2.py	véletlenszerű nappali események
test_feature1.py	a nehézségi szintek tesztjei
test_feature2.py	a nappali események tesztjei
Készítő

Cséplő Bálint Gábor – github.com/csepike
