#include "Header.h"

/*
Самые популрные биграмы
ст, но, то, на, ен
x = a * 31 + b
545, 417, 572, 403, 168
*/

int func(char ch)
{
	int r = -1;
	if (ch == 'А' || ch == 'а') r = 0;
	else if (ch == 'Б' || ch == 'б') r = 1;
	else if (ch == 'В' || ch == 'в') r = 2;
	else if (ch == 'Г' || ch == 'г') r = 3;
	else if (ch == 'Д' || ch == 'д') r = 4;
	else if (ch == 'Е' || ch == 'е') r = 5;

	else if (ch == 'Ж' || ch == 'ж') r = 6;
	else if (ch == 'З' || ch == 'з') r = 7;
	else if (ch == 'И' || ch == 'и') r = 8;
	else if (ch == 'Й' || ch == 'й') r = 9;
	else if (ch == 'К' || ch == 'к') r = 10;
	else if (ch == 'Л' || ch == 'л') r = 11;
	else if (ch == 'М' || ch == 'м') r = 12;
	else if (ch == 'Н' || ch == 'н') r = 13;
	else if (ch == 'О' || ch == 'о') r = 14;
	else if (ch == 'П' || ch == 'п') r = 15;
	else if (ch == 'Р' || ch == 'р') r = 16;
	else if (ch == 'С' || ch == 'с') r = 17;
	else if (ch == 'Т' || ch == 'т') r = 18;
	else if (ch == 'У' || ch == 'у') r = 19;
	else if (ch == 'Ф' || ch == 'ф') r = 20;
	else if (ch == 'Х' || ch == 'х') r = 21;
	else if (ch == 'Ц' || ch == 'ц') r = 22;
	else if (ch == 'Ч' || ch == 'ч') r = 23;
	else if (ch == 'Ш' || ch == 'ш') r = 24;
	else if (ch == 'Щ' || ch == 'щ') r = 25;

	else if (ch == 'Ы' || ch == 'ы') r = 26;
	else if (ch == 'Ь' || ch == 'ь') r = 27;
	else if (ch == 'Э' || ch == 'э') r = 28;
	else if (ch == 'Ю' || ch == 'ю') r = 29;
	else if (ch == 'Я' || ch == 'я') r = 30;
	else if (ch == ' ') r = 31;
	return r;
}

char refunc(int n)
{
	switch (n)
	{
	case 0: return 'а';
		break;
	case 1: return 'б';
		break;
	case 2: return 'в';
		break;
	case 3: return 'г';
		break;
	case 4: return 'д';
		break;
	case 5: return 'е';
		break;

	case 6: return 'ж';
		break;
	case 7: return 'з';
		break;
	case 8: return 'и';
		break;
	case 9: return 'й';
		break;
	case 10: return 'к';
		break;
	case 11: return 'л';
		break;
	case 12: return 'м';
		break;
	case 13: return 'н';
		break;
	case 14: return 'о';
		break;
	case 15: return 'п';
		break;
	case 16: return 'р';
		break;
	case 17: return 'с';
		break;
	case 18: return 'т';
		break;
	case 19: return 'у';
		break;
	case 20: return 'ф';
		break;
	case 21: return 'х';
		break;
	case 22: return 'ц';
		break;
	case 23: return 'ч';
		break;
	case 24: return 'ш';
		break;
	case 25: return 'щ';
		break;

	case 26: return 'ы';
		break;
	case 27: return 'ь';
		break;
	case 28: return 'э';
		break;
	case 29: return 'ю';
		break;
	case 30: return 'я';
		break;
	case 31: return '_';
		break;
	default:
		return '0';
		break;
	}
}

vector<int> Engramm(vector<int> fulltext)
{
	int m = MODULE;
	int size = fulltext.size();
	vector<int> text;
	int i = 0;
	while (i < size)
	{
		if (i + 1 <= size)
		{
			text.push_back(fulltext[i] * m + fulltext[i + 1]);
			i += 2;
		}
	}
	return text;
}

vector<int> Degramm(vector<int> text)
{
	int m = MODULE;
	int size = text.size();
	vector<int> fulltext;
	int i = 0;
	while (i < size)
	{
		int x = text[i] / m;
		fulltext.push_back(x);
		x = text[i] - x * m;
		fulltext.push_back(x);
		i++;
	}
	return fulltext;
}

vector<int> Monogram(vector<int> text)
{
	vector<int> oftenMomogram;
	map<int, int> alphabet =
	{
		{0, 0}, {1, 0}, {2, 0}, {3, 0}, {4, 0},
		{5, 0}, {6, 0}, {7, 0}, {8, 0}, {9, 0},
		{10, 0}, {11, 0},{12, 0}, {13, 0}, {14, 0},
		{15, 0}, {16, 0}, {17, 0}, {18, 0}, {19, 0},
		{20, 0}, {21, 0}, {22, 0}, {23, 0}, {24, 0},
		{25, 0}, {26, 0}, {27, 0}, {28, 0}, {29, 0},
		{30, 0}
	};
	
	for (int i = 0; i < text.size(); i++)
	{
		alphabet[text[i]]++;
	}
	//Работает, только если второе значение в паре тоже уникально. Для больших текстов эт не проблема
	map<int, int> reverseMyMap;
	for (pair<int, int> pair : alphabet) 
	{
		reverseMyMap[pair.second] = pair.first;
	}

	map<int, int>::reverse_iterator it = reverseMyMap.rbegin();
	while (it != reverseMyMap.rend()) //Заносит все монограммы в вектор в порядке уменьшения частоты
	{
		//cout << it->first << ": " << it->second << '\n';
		oftenMomogram.push_back(it->second);
		it++;
	}
	return oftenMomogram;
}

vector<int> TopMonogram(vector<int> text)
{
	vector<int> mono = Monogram(text);
	vector<int> top;
	for (int i = 0; i < 5; i++)
	{
		top.push_back(mono[i]);
	}
	return top;
}

vector<int> AntiTopMonogram(vector<int> text)
{
	vector<int> mono = Monogram(text);
	vector<int> antiTop;
	int size = mono.size() - 1;
	for (int i = size; i > size - 5; i--)
	{
		antiTop.push_back(mono[i]);
	}
	return antiTop;
}

vector<int> bigram_ncross(vector<char> buff)
{
	int count = 0;
	int matrix[31][31] = { 0 };
	for (int i = 0; i < buff.size() - 1; i += 2)
	{
		if (buff[i] != ' ' && buff[i + 1] != ' ' && buff[i + 1] != '\0')
		{
			//cout << refunc(func(buff[i])) << "" << refunc(func(buff[i + 1])) << endl;
			matrix[func(buff[i + 1])][func(buff[i])]++;
			count++;
		}
	}
	//cout << "Count: " << count << endl;
	//cout << "\t";
	vector<int> bigramm; //Вектор самых частых биграмм

	for (int k = 0; k < 5; k++) // Формируем 5 самых частых биграмм
	{
		int max = 0; // значение максимума в настоящей итерации цикла k
		int bg = 0; // Закодированное по числу 31 значение биграммы 
		for (int i = 0; i < 31; i++) //Пробежка по каждому элементу матрицы
		{
			for (int j = 0; j < 31; j++)
			{
				if (matrix[i][j] == max && max != 0) //Если элемент имеет такое же количество вхождений, как и максимальный, идет проверка на то, одна и та же ли это биграмма 
				{
					bool ch = true;
					for (int p = 0; p < bigramm.size(); p++)
					{
						if(bigramm[p] == j * 31 + i)
						{
							ch = false;
							break;
						}
					}
					if (ch) 
					{ 
						bg = j * 31 + i; // Если биграммы отличаются, то значение актульной биграммы присваивается, а максимум остается тот же
					} 
				}
				else if (matrix[i][j] > max) // Если значение элемента больше, чем максимум на данном этапе. 
				{
					int temp = 1;
					int tempBg = j * 31 + i;
					for (int p = 0; p < k; p++)
					{
						if (tempBg == bigramm[p]) //Проверка есть ли эта биграмма в векторе
						{
							temp = 0; //Если есть, то значение не заносится 
							break;
						}
					}
					if (temp == 1) //Если в векторе такой биграммы нет, то присваиваем значения максимальным 
					{
						max = matrix[i][j];
						bg = tempBg;
					}
				}
			}
		}
		bigramm.push_back(bg); //Заносим биграмму в вектор
	}
	return bigramm;
}

int Gcd( int a, int b) 
{
	return b ? Gcd(b, a % b) : a;
}

int Gcd(int a, int b, int & x, int & y) {
	if (a == 0) {
		x = 0; y = 1;
		return b;
	}
	 int x1, y1;
	 int d = Gcd(b%a, a, x1, y1);
	x = y1 - (b / a) * x1;
	y = x1;
	return d;
}

int BackElement(int a, int m)
{
	int x, y;
	int g = Gcd(a, m, x, y);
	if (g != 1)
	{ 
		//cout << "no solution";
		}
	else {
		x = (x % m + m) % m;
		if (x < 0){	x += m; }
		return x;
	}
}

vector<int> line(int a, int b, int m)
{
	vector<int> res;
	int g = Gcd(a, m);
	//cout << " x = " << x << ", y = " << y << endl;
	if (g == 1)
	{
		a = BackElement(a, m);
		int x = (a * b) % m;
		if (x < 0) { x += m; }
		res.push_back(x);
	}
	else if (g > 1 && b % g == 0)
	{
		int a1 = a / g;
		int b1 = b / g;
		int m1 = m / g;
		a1 = BackElement(a1, m1);
		int x = (a1 * b1) % m1;
		if (x < 0) { x += m1; }
		res.push_back(x);
		for (int i = 0; i < g; i++)
		{
			x += m1;
			if (x < m)
			{
				res.push_back(x);
			}
		}
	}
	else
	{
		//cout << "no solution";
	}

	return res;
}

vector<int> TryKey(vector<int> ciphertext, int a, int b)
{
	int size = ciphertext.size();
	vector<int> text;
	int m2 = pow(31, 2);
	int a1 = BackElement(a, m2);
	for (int i = 0; i < size; i++)
	{
		int x = a1 * (ciphertext[i] - b) % m2;
		if (x < 0) {
			x += m2; }
		text.push_back(x);
	}
	return text;
}

vector<pair<int, int>> GetKey(int x1, int x2, int y1, int y2)
{
	int a, b;
	int m2 = pow(31, 2);
	vector<int> lineRes;
	vector<pair<int, int>> key;
	if (x1 - x2 != 0 && y1 - y2 != 0)
	{
		lineRes = line(x1 - x2, y1 - y2, m2);
	}

	for (int i = 0; i < lineRes.size(); i++)
	{
		a = lineRes[i]; 
		if (a == 0) { continue; }
		b = (y1 - a * x1) % m2;
		if (b < 0) { b += m2; }
		pair<int, int> k = make_pair(a, b);
		key.push_back(k);
	}
	return key;
}

bool Filter(vector<int> btext)
{
	vector<int> text = Degramm(btext);
	vector<int> topOpen = { 14, 0, 5, 8, 13};
	vector<int> antiTopOpen = { 20, 25, 27, 22, 29};
	vector<int> topCipher = TopMonogram(text);
	vector<int> antiTopCipher = AntiTopMonogram(text);
	int check = 0;
	for (int i = 0; i < 5; i++)
	{
		for (int j = 0; j < 5; j++)
		{
			if (topOpen[i] == topCipher[j])
			{
				check++;
			}

			if (antiTopOpen[i] == antiTopCipher[j])
			{
				check++;
			}
		}
	}
	if (check > 5) return true; //Проверка на совпадение с ОТ
	else return false;
	
}

vector<pair<int,int>> ActualKey(vector<int> ciphertext, vector<int> Y)
{
	vector<int> X = MostPopulatBigram;
	vector<pair<int, int>> candidat;

	for (int i = 0; i < X.size(); i++)
	{
		for (int j = 0; j < X.size(); j++)
		{
			if (i == j) { continue; }
			for (int k = 0; k < Y.size(); k++)
			{
				for (int q = 0; q < Y.size(); q++)
				{
					if (k == q) { continue; }
					vector<pair<int, int>> key = GetKey(X[i], X[j], Y[k], Y[q]);
					for (int t = 0; t < key.size(); t++)
					{
						vector<int> temp = TryKey(ciphertext, key[t].first, key[t].second);
						if (Filter(temp))
						{
							pair<int, int> k = make_pair(key[t].first, key[t].second);
							bool ch = true;
							for (int f = 0; f < candidat.size(); f++)
							{
								if (candidat[f] == k)
								{ 
									ch = false;}
							}
							if(ch){ candidat.push_back(k); }
						}
					}

				}
			}
		}
	}
	return candidat;
}

void Decode(vector<int> ciphertext)
{
	vector<char> txtCp;
	for (int i = 0; i < ciphertext.size(); i++)
	{ 
		txtCp.push_back(refunc(ciphertext[i]));
	}
	vector<int> oftenBg = bigram_ncross(txtCp);
	vector<int> BgCp = Engramm(ciphertext);
	vector<pair<int, int>> keys = ActualKey(BgCp, oftenBg);
	if (keys.size() == 0)
	{
		cout << "Key not found!" << endl;
		return;
	}

	for (int i = 0; i < keys.size(); i++)
	{
		vector<int> temp = TryKey(BgCp, keys[i].first, keys[i].second);
		//vector<int> temp = TryKey(BgCp, 5, 960);
		vector<int> itxt = Degramm(temp);
		vector<char> opentext;
		for (int k = 0; k < itxt.size(); k++)
		{
			opentext.push_back(refunc(itxt[k]));
		}
		cout << "(" << keys[i].first << ", " << keys[i].second << "):" << endl;
		
		for (int j = 0; j < opentext.size(); j++)
		{
			cout << opentext[j];
		}
		cout << endl << "_______________________________________________" << endl;
	}
}

int main()
{
	setlocale(LC_ALL, "RU");
	char text[] = "щжуяжущпккфшчфбждоцпюдйсвжбэдуэыйэдцмодпмурзфбряцкмдыйдосштцмижбчфипмугфбзчшохдодвзбряцкмдбэдцхзнощкяоэоюэтцюзныертзилгфоцбчполфмэдцщкйкшйэысйрэйкчозычфждьмйшотдотзьоюйсщзоюдууюзсшшстзрэыосяфоешыенывдьмиыыяшцрбгянямзюдшскдмыайыяаоешезвжпонорэкжцчжшбчдофшщофбяоязфыщжвонцеырайхмучмсшывчфвэрфешмяояйывщеыйсбжощлзшярфбждоцпюдлвюпщкмзешжзмоуяхямзюдлвзбкзешдбшящксавотзябйкжзшцопсйкоефтцрзюэдцсшямсканзомыжуэыыцсшмычмэжглрзщыезскщквкшятоьэйштибяшкочщкфмыйеыйывдьмиыщчвккцощеызонорйвкхпшсзунрмоншзоязшяэдхпезхлсопжипеызохлншплбйщждоыкфоскщквкшягоефоцэзччскщквканвказешюшлцромглтдоккжшскзыядншууезжурфешщпнзшятоужертцлвяхщжпофожущпккшяэывдьмиыйсжусжощккшйжррэсзешьоктдоскыкфотфлцжшвдзылвхзпмжущжеляыцдюппкгфкшскщквкшяозноюуйэвзхягжжзщрфяоэщпсчкжйэцшвдрйрэйкчофолжыймывдьмиыщчдорддокыбзлжвочыезыяюйеытяьочмскмзшядяешмуяхщжбягжрйашайюпмогйжшфшайрмлзннтзхаокшйбчаощяанбччйтжмкжучбуфпошфбждоцпюдлвюпюпэзкбтцзопзаоешйшохзодонофшайсщзожурфмовоцяанфшляйбмуьосклкюнсккжеьзоешшоешоцэжлыдяюйеызопыщжфоочсквжаббжнзбляьхзсккцезшяййсщзоюдьмйшнхдоаоешезвжбяршвдшяполфзятзбжьоиосяйжгоелзурмеыйссожзешопхпимсжсказкзшяшйнэюшшомглтдонзпксзеыэжюпщжхявушйгожурфлцгцншвдрздвщоцыыиеыхзнфылтфаляяыжфзйквбждэечяыжхыхоцыыиеыыяпомггднотлккжжипеызохлщпдоряпзелцджзкзсэлвщпчзгпшсмыжумилцэбтцзохлмофхэыеынеткзеадьгпуротынщйайкбазущпязхлдырйпоазсяслщяджипщплзджипюшлцлыбжхяскыосяэищеештцедууьмншйкрзшяцпдвзбряцкмдррхфщжэпмуапзчвомощкхыхзиоюнязхпрэчфлоешщпоцбжщлтзноьобцэжхякзуяяяямзокбмырфзбюжщкяьрйсозыеыйсхпрфеыщчфоефзббжнзтыссжяилнахпезфщпмшявжядтцйэоцбчазгфьпмушсбэчмиоцяшйдвюптжждйсэйтзмоыптцыцшййычмыйзхйшмшжшалтыбжхябжюакцопиыщчыдншуусйжуопчфюшжзйкмяефопифбкюнзовбюпдокзшярйдуюплвляешууяхщжпонойкыпюшщчмысклзыцбчмялзоцнрряешиыфсхядаыосябжьоиогфеыхзншзунрюпыяябтцюмюпйшажьосжрэешжзщыцзешйкккшячхдосажуюшимйшлыпутцурряешбзкцколппотзуыайжхжшеыабряязодхпрэчфдяешоцкзвдаямымуайдосшщоччдыозлжцшшйфшщоцьзхлцюпзхщжщккжюыюпцчзпэыиывдншуушсешяоюшбчкзуяяяямзозхьпешьоаоешывмкйыдвбжжзщрэысямяблоцлышсгялаэышйлвмксаанжутоаонзскккрздвюптжждшсэыпзьцяделоцлыбжанхмлзннскюдьмоцбжпэсйсщзодбкзвыкшэпдойхдоюаншщкбаекшйбчншузябряешйкешзоешчбгяыоиыоцпмзямодпмучкшйаоешезвжпоновгеыьзрйхесзкбйкьосктлсзешьоекшялцмиажжусжюуэжцышсдондпмкзшягожурфлцеызоножяяоьоэмкзшяпдмыэзгпйшууешоцсаскдондымкзшязплццдлвляудмяйядойккощзшяекшэйфбждоцпюдлвляскмздбкзцжжущпрфуяшфсчдвбждчвхеыщчфочытцмиажщквканфшууфиеыхзаоешезвжпонодаыпиыщомзмятыямйшалтыеызоешыедвайнинзшязпкцрфешмяеыцпяовкрфекуяжубждоджгллкпыбжанцйсщзорэкжшяанфшншряязлзфуыйдуюпшсуяпзйкелиавжнрфушйеыюувделдшчфилюшощжшшйкшшйцомгулщяджипюгпуотсяужзюждмкчкнцжшязцжюяйкбэйканпдпуыйьмюпйфбждоцпюдлвюпюпэзпшкзхуэжйуппбзлжфяфохяшфвчшякжядтлоцлыезсочзсыяхщжипляэмнщеычяражуййюзвждвждмызхзосшзбкззжокуцеыюпщуыйтодыюпиызопызвкзмзюдайюдьмиыыяхфщжцфвчшящжюпмуюкжшбчбьщжыйрйшзяошйзоузяждчвхеыщчпмщпбкуяяоекшярбптхямзюдечрэйкиордиыцпямфочыхордяожзщыезжупмскшяцпсказкзшяллщяанншшкщкпоноюааощяекшйбчжучбгяыоиыоцпмяднщжшбчтзчзкззогяюалэчмиыоцюшяхщжпокбчфнодоздопзузхщжпоьфйказтзрэыосяфощждчвхеыхзжусжфрйктзшясжеьзоешрйэжпзжжбяаоешывбзлжцшшйфшрэщжсокыйшлцлыксфохямвмуйчжуезаяалжшбчшфссешмяпзюнзоешедвдвлгфезшйдбряилгфеыхзсккчвкщыезтлыниоовмушссожзбибзвфвчшяеыабкзтыыймуеызочбюпэзбпифрйбжхяузыпуяхыщчрзхьэыэявжкщитдоешзхеыхзрэешйчпзюнешибряшяякжшбчфуэжмзчшвдщкпонйсщжшвкьоцпйшбгпутгэййшмштцедзббжнзмоошууеыщчдонорзлзджипщчьоцыыиеыыявлаомяркгяшптцпмдущесзноншшкмокцжшлвждвдрэскалцяекжшбчкожцчибзлжозномясктзлзмкжшбчшящкбяйбзбяшжддыцшдзщжэзччамекуяанюзскжуэыощлзшящжбждояоратлынсаскрэууншмяскжупмскжшбчцдвдвжьглцечмяскскщкбаекжшбчфшууэжтлмдэйсщжшмощквканбчтзябйкжзшцопсйзоужертцлвяхщжбямэсоеецызбйкмяюнзоекшвуяджпоьфйказсшлячовунщеырэтцюзпохпеызомоешдбждсожзбибзлжхыщжыйрйшзяошйуфаляятфсчподояоносшншмоешдбждтззпсчжшбчншщзнэйсешьовбптдохлжурфбжффюшлцлыксфохявжядтлоцлылвбжзбмушямзешекощеычяратзилгфбзлжзпвкылоцдуюпиыыяйкныляыфчбюпповбнзцжшзяоййппифрйщкжэппншйкрзщыайхпжшжшвдщкхйппифрйуяпндощкпорфссешмяабяопмьосяцызвмуйчмоешдбждщуивлвщоефтцрзюэдцсавксшншмоешдбждншайешюшлыбжюуиырафовуьмайтзвжгцррсшбжлзмканюакыбзйхдодвууэжкцмэсчжшсопжипеызозхьпешьомяравжщоипжшешмясжжкйкгшмуайтзфуншяхщжбялчуцеыйсжулямрчфюшпфмяяявлвжипюпэышбмунрчфюшьосокыиыхзхпезпыщжмосоьыбжхядамофыюшотдовкккшяабйчуцжелжрбрякывдюшлвохдошзяобпбжжуэырйбзщтелмяилщкцжжзщрэысяныблоцлыщемыжучмдубзвфаляяоышйеыюзмзыжйэозкцкогрчфюшажкжщкгфсймовккцивыйгшьльфжшншмолдопсшайскжущпнзшядуайиыалшжпоноюяыкпзсчсрчфюшскюклфоцьидяхфщжщлщяджипбжюпмуяззощуиврймзвожзпофотывдохлцюпядайхпимиыраыжнэюшсйокбяжярзьазонырйкоцыыиеыщчжящкбяшзяоьфжяюуйсгдншуулвайншопэзцжбкюнзоносочзсыяхщжипхордяожзщызбрякыбзлжкжюпмуяззощуиврйвуйшайподояохлщкбяьшмущжзовказхяанаоешезвжбякбмурфоцхпэесопжипеыилзэтцчмгнпдрэбтюянзужнепзыжыйсйщкжэгщлцечпфлцйшжбрякыиыхзфшайтцлбгцабхявыцпяохяупайтзншщзнэйсшкопншфузхпмдьюшшящксктллзокрзпмжзешскхыэжазадиыуфужертцлвхзэоскфопбоцщкчфылидмышкбмщпбкуяяоекзожзуяпонзяыншвдщкцждоюшвжитдочзкзжзсыкшкяскыосяпнжцнэохфсфлчжеьзоешэпбжжущчхябфбждоцпюдлвямэжглцяекжшскчйфибяншкеынтзужертцлвщчэжффйэракбяощзшжаокыиыщчсожзбиеызоузсуьмуяуыжддосшншмоешдбждсожзбигцскыкфотфлцабгяыовояяфяьшмущжвзлжыцмимшшйгшезновжьошйэзэфщзрзмкуягшзбезносожзбиеыыядвзбряжзлжипюпоцчбптдохлибвоанаопоьшйкешзокюыврухкнзеявжйэйканэущпзомязоныйфмяцяюакбмумяуысйчбямппыйыяюдйшлцлыэжмкгфеыйсмофыксюдабгяыкаяшябялбгцабхямзюдйсжущжеляыцдсэйканюрщкйкякчодаззешажщзскяптжязджпзчзшяжкйкгшмускбфсчаоешезвжпонопмйкйвюпууэжжйюшряшйешпуьгмоешывбзшхдожйюшряпыбжюшвжйэдвншюпзоешедншщзнэйсешылбэяоыкжшбччзкзтырйскпонзшясшмышйсщжшзпсчанбчдайкрзшяшйьомршьеыщчуфтцчыщокыкхйшнхдохпцшшсншешйкцчжшншэзччсжрлязшядяябтцшяанбчжучмкзшяшйрлщяегдяуярймоаышийшажфямосшайдбмурфшяыжжяочжшбчгявбйшщчаоешезвжпоноэбкзешдбшярллзджипюшлцлырэчмзуиыяхскмыуфоцядюпжрчфюшвкжурфлцтжбжюууфиыщчскподояоеыщжлкешраояазжшжущпщоскскможяскжшбцзвлвюпеыхзюдншуусйшфкзныбжхяншзогяуяннетюянзашцдияблязнырэтцлыайдбкзешдбшянфсчтзномофшсжцкгяпзюнамзпеяпыэжйэзпэыгдншуущешфалноыжгллкеыщжуясащуивхзак";
	vector<int> test;
	for (int i = 0; i < 5848; i++)
	{ 
		test.push_back(func(text[i]));
	}
	Decode(test);

	return 0;
}