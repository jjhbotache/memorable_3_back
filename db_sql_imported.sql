
            CREATE TABLE IF NOT EXISTS users (
                google_sub TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                phone TEXT,
                img_url TEXT
            );
            CREATE TABLE IF NOT EXISTS designs (
                id SERIAL PRIMARY KEY,
                name TEXT NOT NULL,
                img_url TEXT,
                ai_url TEXT
            );
            CREATE TABLE IF NOT EXISTS tags (
                id SERIAL PRIMARY KEY,
                name TEXT NOT NULL
            );
            CREATE TABLE IF NOT EXISTS cart_design (
                id SERIAL PRIMARY KEY,
                id_user TEXT,
                id_designs INTEGER,
                FOREIGN KEY (id_user) REFERENCES users(google_sub) ON DELETE CASCADE,
                FOREIGN KEY (id_designs) REFERENCES designs(id) ON DELETE CASCADE
            );
            ALTER TABLE cart_design
            ADD CONSTRAINT fk_cart_design_users
            FOREIGN KEY (id_user) REFERENCES users(google_sub) ON DELETE CASCADE;
            CREATE TABLE IF NOT EXISTS favorite_list_design (
                id SERIAL PRIMARY KEY,
                id_user TEXT,
                id_designs INTEGER,
                FOREIGN KEY (id_user) REFERENCES users(google_sub) ON DELETE CASCADE,
                FOREIGN KEY (id_designs) REFERENCES designs(id) ON DELETE CASCADE
            );
            CREATE TABLE IF NOT EXISTS tag_design (
                id SERIAL PRIMARY KEY,
                id_tag INTEGER,
                id_design INTEGER,
                FOREIGN KEY (id_tag) REFERENCES tags(id) ON DELETE CASCADE,
                FOREIGN KEY (id_design) REFERENCES designs(id) ON DELETE CASCADE
            );
            CREATE TABLE IF NOT EXISTS extra_info (
                name TEXT NOT NULL,
                value TEXT
            );
        
INSERT INTO users VALUES ('113517231390547201079', 'JUAN JOSE HUERTAS BOTACHE', 'jjhuertasbotache@gmail.com', '3012167977', 'https://lh3.googleusercontent.com/a/ACg8ocLN7SVWsu3JCOIKTdBi0b6zJIUm3laI4L52nqSZRBt87u48wxsF=s96-c');
INSERT INTO users VALUES ('103671930126618354340', 'Juan Jose Huertas Botache', 'jjhuertas3@misena.edu.co', NULL, 'https://pbs.twimg.com/profile_images/1701878932176351232/AlNU3WTK_400x400.jpg');
INSERT INTO users VALUES ('117521364309723588901', 'sap ito', 'sapohpta4@gmail.com', NULL, 'https://lh3.googleusercontent.com/a/ACg8ocJtSzsxIwYNn02BYly2etovUoSmDv7DWyLORL0uVqtCLJTNsQ=s96-c');
INSERT INTO users VALUES ('102892313633594583380', 'JUAN JOSE HUERTAS BOTACHE', 'jjhuertasb@ut.edu.co', NULL, 'https://lh3.googleusercontent.com/a/ACg8ocINdKO1x3JQXZXUOGBp24JfbrCljYCFlLRVivFEyc4Pe_3fDA=s96-c');
INSERT INTO users VALUES ('101336061289786159784', 'Camilo Pachon', 'crisbilincamilo2003@gmail.com', NULL, 'https://lh3.googleusercontent.com/a/ACg8ocLw_8N1DnWUAIcPal93I3-XqLZM5NCKrxmEcaWMc8GBf1PYl1EA=s96-c');
INSERT INTO users VALUES ('116113044305033282030', 'Juan Diego García Mora', 'jdgarcia20050910@gmail.com', NULL, 'https://lh3.googleusercontent.com/a/ACg8ocKjDH9s6mE0vlSInRdclapZxlKKEVPnFw7IxVJ7xfm-mCHnAw=s96-c');

INSERT INTO designs VALUES (10, '20 pero a que costo', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1718744733/designs/lc4ro4lk3jtsfbozqy2y.png', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1718744732/ais/sfxqkd3zvd7epdnsqzid.ai');
INSERT INTO designs VALUES (11, 'Brilla hoy y siempre feliz cumple', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1718744808/designs/kvftuokirehlchiijcdn.png', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1718744807/ais/kswpx8g5uj5dqvgavrfk.ai');
INSERT INTO designs VALUES (13, 'Dale a cada dia la posibilidad de convertirse en tu mejor dia', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1718744880/designs/fz90artldv1b3ryg0up6.png', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1718744879/ais/ma211oc4lxa8ri5m5jtl.ai');
INSERT INTO designs VALUES (14, 'Feliz cumpleaños', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1718744919/designs/qn1tfglubcp736mcu1hs.png', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1718744918/ais/kk3tyaso8raomruzf0gw.ai');
INSERT INTO designs VALUES (15, 'Feliz cumpleaños a alguien que tiene más años de exper iencia que un vino fino', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1718744974/designs/ucxsvk4v0kcz8x0bkgzf.png', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1718744972/ais/tnh4qsbxjsyyy5owlp2s.ai');
INSERT INTO designs VALUES (16, 'Feliz cumpleaños aura', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1718745003/designs/pde6fekr2oqhqfmzmpbg.png', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1718745003/ais/wqniq4ouhrn3iechnelh.ai');
INSERT INTO designs VALUES (17, 'Feliz cumpleaños juan', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1718745025/designs/be8xn03bczwbw5tbardk.png', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1718745024/ais/vtz5mtfwtpu2vvwtlfvd.ai');
INSERT INTO designs VALUES (18, 'Feliz cumple princesa', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1718745074/designs/fzaebbviphheekrwjk2k.png', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1718745073/ais/jent8lr6br7as6anib0x.ai');
INSERT INTO designs VALUES (19, 'Happy birthday to you julian', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1718745117/designs/hth93pwbcx2v4h6x4h3t.png', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1718745116/ais/g3fcv9wwn7kmjgq8ihjm.ai');
INSERT INTO designs VALUES (20, 'Hoy agradezco a Dios por tenernos un año màs juntos', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1718745141/designs/bkytbtitb1izurfusovv.png', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1718745140/ais/eqx6k64jjlel5tedgtln.ai');
INSERT INTO designs VALUES (21, 'It''s mario''s birthday', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1718745194/designs/sm9myni4yuqkfrrbhjyh.png', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1718745193/ais/zvezqjfwoixjfoo2kolb.ai');
INSERT INTO designs VALUES (22, 'Julian edicion limitada', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1718745240/designs/hmxbausx4uov1frij78p.png', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1718745239/ais/a51dffkvpb8ca3zje1x6.ai');
INSERT INTO designs VALUES (23, 'Mi poder favorito es poder estar contigo feliz cumpleaños', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1718745261/designs/xyx1lqp2lgrqvgg1fd53.png', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1718745260/ais/vosvmq1puadk9z0ay9ky.ai');
INSERT INTO designs VALUES (24, 'Que todo lo bueno te siga, te encuentra y se quede contigo', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1718745294/designs/uf0yjzwrh6wpbewcbwjf.png', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1718745294/ais/sx8q9rgwbyc8nyeesr0e.ai');
INSERT INTO designs VALUES (25, 'Amor el mundo tiene sus maravillas pero tu eres maravillas de mi mundo', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1718745421/designs/m8zq12vzdjk0hcyf02ql.png', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1718745421/ais/omxtqooblfer8jkc9zjx.ai');
INSERT INTO designs VALUES (26, 'Guapa, no importa la distancia entre nosotros, el amor nos une. camilo', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1718745522/designs/hwniztd2uublutkqjsal.png', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1718745521/ais/pimhuxdkgrscnoycvj6l.ai');
INSERT INTO designs VALUES (27, 'Cada botella vacia esta llena con una gran historia', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1718745562/designs/uv5ftiebcsn2wheebxgr.png', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1718745561/ais/drvhgatoo4fxrzwko3n3.ai');
INSERT INTO designs VALUES (28, 'Como flores llenas de luz encanto y belleza asi son ustedes las mujeres nuestra luz en esta tierra', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1718745646/designs/cqw2q6h2vhq8idxkqtdw.png', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1718745613/ais/zreabmgdsidbr699mjb9.ai');
INSERT INTO designs VALUES (29, 'Como no te voy a querer si dices puras pendejadas igual que yo', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1718745773/designs/anpntayffvuj5fypxltv.png', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1718745772/ais/qgzwktyfrmmldfq0x3wt.ai');
INSERT INTO designs VALUES (30, 'Contigo lo bonito se vuelve infinito', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1718745846/designs/uxx65krmbsntidqfemon.png', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1718745845/ais/s7xszsg1hhw3ku58rfbv.ai');
INSERT INTO designs VALUES (31, 'Descubrí que la magia existe estando con vos', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1718745876/designs/hngwrgvck8th2zyfvoy8.png', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1718745875/ais/whsu2bv3ogitmgcq5vg9.ai');
INSERT INTO designs VALUES (32, 'Drink wine feel fine', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1718745911/designs/nqeb8iehlzsv9bkudmao.png', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1718745910/ais/imnkz2l96itb4ck7h27r.ai');
INSERT INTO designs VALUES (33, 'El amor que se cuida es el que crece y dura para siempre', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1718745990/designs/dzxog9bezhtvtn1xw9wr.png', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1718745990/ais/ehhsjxvu9l6saidd3qu4.ai');
INSERT INTO designs VALUES (34, 'El vino es el lenguaje más universal del corazón', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1718746035/designs/lcjytkfjkbk0roj8d4xm.png', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1718746034/ais/khcfa08whjlyb3tdnedp.ai');
INSERT INTO designs VALUES (35, 'En esta navidad tu eres la estrella que mas alumbra', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1718746224/designs/t9xkcipv7f761y4olqn4.png', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1718746224/ais/fi7frkcyyzpuguabyst8.ai');
INSERT INTO designs VALUES (36, 'Eres el mas bonito de mis milagros', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1718746315/designs/wjh6j0nwcodw9h3tiwoe.png', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1718746315/ais/bxnfej7pztxkipgxbbfi.ai');
INSERT INTO designs VALUES (37, 'Eres ese amigo que me dio vida', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1718746408/designs/hpxwlnby44chmjrt9lbc.png', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1718746407/ais/bdsr4zxsgohjtaljjag4.ai');
INSERT INTO designs VALUES (38, 'Es un buen tipo mi viejo i love you father', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1718746425/designs/ij54bpg9pqustjg5xw4i.png', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1718746424/ais/wzh0scwklj38yhc4xeur.ai');
INSERT INTO designs VALUES (39, 'Gracias por estar en las buenas en las malas y en las peores', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1718746495/designs/u0xyhwdbffcidnt3hfqi.png', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1718746495/ais/ra49cssjauhikuypnof0.ai');
INSERT INTO designs VALUES (41, 'La vida se mide en momentos, Coleccionalos', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1718746932/designs/iyj5ystkdldkbvc0qehn.png', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1718746931/ais/bazjelj2sdcxlbuizyk1.ai');
INSERT INTO designs VALUES (42, 'El amor es una planta que debe cultivarse con cuidado', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1718747072/designs/iij5vianty9tbvfdvqbh.png', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1718747072/ais/w4tzsr9vlg40cmx4xlls.ai');
INSERT INTO designs VALUES (43, 'La vida es mia pero el corazon es tuyo la sonrisa es mia pero el motivo eres tu', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1718747193/designs/lphnd7ldwdi8qnbqwxko.png', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1718747192/ais/jbxinjisrbfyd2yxpcmy.ai');
INSERT INTO designs VALUES (44, 'La vida se mide en momentos coleccionalos', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1718747254/designs/v9xx7ljmas7ghayfe0ab.png', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1718747253/ais/hrvlzoylpebyw6gotta8.ai');
INSERT INTO designs VALUES (45, 'Lisen more talk less', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1718747279/designs/gmzo6docxecmgekgiq0b.png', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1718747278/ais/rs0ltpxu3fhqx3xp9kou.ai');
INSERT INTO designs VALUES (46, 'Lo eres todo para mi maria', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1718747347/designs/gu8gphjt3vl4gzamlbpm.png', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1718747346/ais/vdlvkyqozv9bgqg02c5i.ai');
INSERT INTO designs VALUES (47, 'Mama tu eres mi bendicion favorita', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1718747709/designs/py6rhdhohuw07ifzbuio.png', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1718747709/ais/tcugab3ytxsopnchd7tt.ai');
INSERT INTO designs VALUES (49, 'Mi mayor miedo es perderte', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1718747945/designs/dtctkf6ll8hw3oeinsl4.png', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1718747944/ais/fwuc4xua9awk9hlr2zbj.ai');
INSERT INTO designs VALUES (50, 'Mis demonios se quejan continuamente de que me he vuelto un angel contigo', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1718748023/designs/ccxebv5oscdfqjbdxhff.png', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1718748023/ais/e67j65browhueyyzimb9.ai');
INSERT INTO designs VALUES (51, 'Mujer eres arte', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1718748137/designs/sl268eg0jnojmatqjhey.png', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1718748137/ais/ey2s0dpccpiweqnbykzy.ai');
INSERT INTO designs VALUES (52, 'No eres google pero tienes todo lo que busco', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1718748179/designs/d1xqcyuvnwhtbf2esowo.png', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1718748179/ais/mshrl5xsblgxb5sygyw1.ai');
INSERT INTO designs VALUES (53, 'Por mas años juntas happy birthday', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1718748261/designs/dwdvsoqb38jpsxozh3qd.png', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1718748260/ais/vapnijldxikuenvvdu4j.ai');
INSERT INTO designs VALUES (54, 'Porque elegirnos fue es y será la mejor opción', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1718748314/designs/re1klfhdphxhyjkq6xed.gif', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1718748313/ais/vctxub7ffybeghmazwul.ai');
INSERT INTO designs VALUES (55, 'Que nuestro amor sea como un buen vino te amo', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1718748422/designs/eilephlv83cjlg4bhdpv.png', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1718748421/ais/cjyqim6bvqchbc602bjm.ai');
INSERT INTO designs VALUES (56, 'Que si, si lo quiero cansón', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1718748500/designs/z8zckxailukjavarqhhj.png', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1718748499/ais/iuz3dztbprlzzhnc7upz.ai');
INSERT INTO designs VALUES (57, 'Que tu niña interior viva orgullosa del mujeron que eres', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1718748543/designs/wy9cnqmsfkd6qii7gxpj.png', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1718748542/ais/k9uu4bvgsicaveh5t2yw.ai');
INSERT INTO designs VALUES (59, 'Sin locas amigas no tendriamos locos momentos', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1718748661/designs/scqyyqhrkvrm2cjmrf7p.png', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1718748661/ais/bdyusdkddxfwtcwmisoi.ai');
INSERT INTO designs VALUES (58, 'Ser mujer es tu poder', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1718748610/designs/nkvibjejht7i97nolywd.png', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1718748609/ais/vffg2cjx2y1ysc9vbzzg.ai');
INSERT INTO designs VALUES (60, 'Si tu quisieras esta noche ir a bailar un chachacha yo te puedo enamorar', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1718748699/designs/yypvgbspjrssr1elnmhf.png', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1718748699/ais/glwt9grpz5vtlqr9hnun.ai');
INSERT INTO designs VALUES (61, 'Te amo mas que ayer y menos que mañana', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1718748899/designs/pfmeudzgugpdv3qzc1ml.png', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1718748898/ais/ompc9tumgxaxdmpy4q9i.ai');
INSERT INTO designs VALUES (62, 'Te amo mi amor', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1718748999/designs/lgxba3dypjootrcpd8tf.png', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1718748998/ais/ulvu2q98bvbnqf4e8tdp.ai');
INSERT INTO designs VALUES (63, 'Te amo valentina', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1718749072/designs/vynlnl2pjlxp6cx3ibxd.png', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1718749071/ais/izdxiipbihow0vecwlhv.ai');
INSERT INTO designs VALUES (64, 'Toda historia de amor es hermosa', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1718749140/designs/ke43f8cna50fbzqtbjky.png', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1718749139/ais/cbwznhyhza7areyuzwyt.ai');
INSERT INTO designs VALUES (65, 'Toda historia de amor es hermosa pero la nuestra es mi favorita', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1718749211/designs/kglj2odnwevwlbad0z5y.png', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1718749211/ais/c70wpqvuowb3uo32xvyu.ai');
INSERT INTO designs VALUES (66, 'Un brindis por los años de buenos momentos que hemos compartido juntos', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1718749505/designs/tu2ihbsw3ryz0gyeqz9i.png', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1718749504/ais/jpee0hujwqf1ubc4sqbw.ai');
INSERT INTO designs VALUES (67, 'Vuela alto', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1718749532/designs/m4mtdswaewqhbi6o1du6.png', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1718749531/ais/p25lcl2xs15qy9zyhurp.ai');
INSERT INTO designs VALUES (68, 'Wishing you a peace of mind and a happy heart!', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1718749550/designs/ybpa2dnlc171bc5nddw3.png', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1718749549/ais/hfdfwrkcrdreetdspcpk.ai');
INSERT INTO designs VALUES (69, 'You did it', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1718749611/designs/thovuzr9m8annmpdphwi.png', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1718749611/ais/m2xdwjxlm27xvxawwx20.ai');
INSERT INTO designs VALUES (70, 'Y si nos perdonamos', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1718749632/designs/x9u7shodrzzvehbsgylh.png', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1718749632/ais/r1mgqum3tg4bpemukgof.ai');
INSERT INTO designs VALUES (48, 'Mi lugar favorito es junto a ti', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1718747783/designs/ypigpimyhdoqkp5eyjyb.png', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1718747782/ais/nlrei5ac9ubqypvjsdzt.ai');
INSERT INTO designs VALUES (72, 'No me hará daño graduarme así? así cómo? así sin saber nada', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1722711664/designs/zhqazptsie6jzxjfla3c.png', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1722711665/ais/oobtziynarswxc7ynl3n.ai');
INSERT INTO designs VALUES (12, 'Brilla mas que nunca hoy es tu dia', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1718744838/designs/emevqmtbklbdllgpbhxu.png', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1718744838/ais/whqvqiscbcycviawhemd.ai');
INSERT INTO designs VALUES (40, 'Hoy es un gran dia pa celebrar brindemos feliz dia del padre', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1718746642/designs/veacf4rk8edmkwk8nd3f.png', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1718746641/ais/oefpfzfnsujctytmpuf7.png');
INSERT INTO designs VALUES (71, 'Yury para navidad felicidad para año nuevo prosperidad y para siempre amistad', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1718749663/designs/lofnkxxiztyml1g0stv4.png', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1718749663/ais/lxfugefnk77ozxyiiyoq.ai');
INSERT INTO designs VALUES (77, 'Un año más de historias por escribir', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1723729673/designs/zw9zt04tukpy6vjou8td.png', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1723729672/ais/r1m9qu3jj53v0byccewg.ai');
INSERT INTO designs VALUES (2, 'Eres la hermana que elegi', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1722870316/designs/cxl56tywzxw6ezh25pb6.png', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1722870315/ais/ad6n8oj4zzn46uai103p.ai');
INSERT INTO designs VALUES (3, 'Eres mi persona favorita', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1722871207/designs/l4viypkikmtvsolakd5s.png', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1722871206/ais/sedeesqg6ehxookz0rye.ai');
INSERT INTO designs VALUES (4, 'No estás viejo eres un clásico', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1722871595/designs/tdkm66l4xkwm4ddjaiib.png', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1722871594/ais/rodyvueidzi2oceiceaj.ai');
INSERT INTO designs VALUES (5, 'Friends + wine = happyness', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1722871638/designs/ogl0qhyjxncssbyydezy.png', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1722871637/ais/cbbhnvgd5zadslb2bdw5.ai');
INSERT INTO designs VALUES (6, 'Feliz cumpleaños a la reina del drama', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1722871678/designs/ktofuok161sgl5islzah.png', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1722871677/ais/ctxvoxc9znzv1rcovwwt.ai');
INSERT INTO designs VALUES (1, 'En todas mis 9 vidas te elegiría', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1722874051/designs/t05rox0roxuk2httmsap.png', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1722874054/ais/yflvmazpsxf82pkjzlod.ai');
INSERT INTO designs VALUES (7, 'Ya son 30 años siendo irresistible', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1722953830/designs/rh3egfoxhuybmrwdpev8.png', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1722953828/ais/dgjzudhjcyqayywoh4ki.ai');
INSERT INTO designs VALUES (8, 'Corazones entrelazados, amor eterno', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1723037747/designs/ua1dfk0zbxgw8qvbfssp.png', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1723037746/ais/jfcjcvzhcewtduauplzk.ai');
INSERT INTO designs VALUES (9, 'Contigo hasta el próximo meteorito', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1723126204/designs/viut5nnq7x7dnp3yzipa.png', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1723126203/ais/odvp7nwwph5s6opmol3a.ai');
INSERT INTO designs VALUES (73, 'En las buenas en las malas y en las peores que chimba tenerlo pana', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1723217790/designs/ptdrxkfuetazeci8ow9i.png', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1723217789/ais/kgdommwqzsb7nolubu7g.ai');
INSERT INTO designs VALUES (74, 'Lady eres la mejor amiga del mundo', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1723472470/designs/dehtstvjc1pezw8qseqz.png', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1723472469/ais/uaculbs9fqvpxaxna1np.ai');
INSERT INTO designs VALUES (75, 'Amarte es mi mejor decisión', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1723559023/designs/f6p2tooxycak4oikppug.png', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1723559022/ais/omtceylfledugofvnppo.ai');
INSERT INTO designs VALUES (76, 'Hay amistades que son como las estrellas aunque no siempre las veas sabes que están ahí brillando para ti en los momentos más oscuros', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1723646182/designs/qk0ns2gcip3eye399ume.png', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1723646180/ais/syicsrwrrdiyoifvazn3.ai');
INSERT INTO designs VALUES (78, 'Te graduaste y estoy muy orgulloso felicidades', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1723812057/designs/janfm3vrpxzpnkm0t9nt.png', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1723812056/ais/pfwtvzlh85jahuuyunbp.ai');
INSERT INTO designs VALUES (79, 'El viaje es más dulce cuando persigues lo que amas', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1724162522/designs/ke4cyvvczqnicipksjvb.png', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1724162521/ais/ye87pej0ovxikibvmgyx.ai');
INSERT INTO designs VALUES (80, 'Viajar es encontrar partes de ti en lugares que jamás imaginaste', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1724243969/designs/k9aunz3juhluhitq4ey5.png', 'http://res.cloudinary.com/dgm8uzbpd/image/upload/v1724243968/ais/xqmirqzzbwrryquesmx6.ai');

INSERT INTO tags VALUES (2, 'Cumpleaños');
INSERT INTO tags VALUES (5, 'Grado');
INSERT INTO tags VALUES (6, 'Viaje');
INSERT INTO tags VALUES (7, 'Aniversario');
INSERT INTO tags VALUES (8, 'Amor');
INSERT INTO tags VALUES (9, 'Casual');
INSERT INTO tags VALUES (10, 'Navidad');
INSERT INTO tags VALUES (11, 'Día del padre');
INSERT INTO tags VALUES (12, 'Amistad');
INSERT INTO tags VALUES (13, 'Recuerdos');
INSERT INTO tags VALUES (14, 'Familia');
INSERT INTO tags VALUES (15, 'Día de la madre');
INSERT INTO tags VALUES (16, 'Octubre');

INSERT INTO cart_design VALUES (7, '113517231390547201079', 52);
INSERT INTO cart_design VALUES (1, '116113044305033282030', 29);

INSERT INTO favorite_list_design VALUES (12, '113517231390547201079', 52);
INSERT INTO favorite_list_design VALUES (1, '101336061289786159784', 1);
INSERT INTO favorite_list_design VALUES (4, '113517231390547201079', 1);
INSERT INTO favorite_list_design VALUES (5, '116113044305033282030', 29);

INSERT INTO tag_design VALUES (1, 5, 72);
INSERT INTO tag_design VALUES (2, 2, 10);
INSERT INTO tag_design VALUES (3, 9, 10);
INSERT INTO tag_design VALUES (4, 12, 10);
INSERT INTO tag_design VALUES (5, 13, 10);
INSERT INTO tag_design VALUES (6, 2, 11);
INSERT INTO tag_design VALUES (12, 2, 12);
INSERT INTO tag_design VALUES (13, 5, 12);
INSERT INTO tag_design VALUES (14, 11, 12);
INSERT INTO tag_design VALUES (15, 15, 12);
INSERT INTO tag_design VALUES (16, 9, 13);
INSERT INTO tag_design VALUES (17, 13, 13);
INSERT INTO tag_design VALUES (18, 14, 13);
INSERT INTO tag_design VALUES (19, 2, 14);
INSERT INTO tag_design VALUES (20, 2, 15);
INSERT INTO tag_design VALUES (21, 14, 15);
INSERT INTO tag_design VALUES (22, 2, 16);
INSERT INTO tag_design VALUES (23, 2, 17);
INSERT INTO tag_design VALUES (24, 2, 18);
INSERT INTO tag_design VALUES (25, 8, 18);
INSERT INTO tag_design VALUES (26, 2, 19);
INSERT INTO tag_design VALUES (27, 7, 20);
INSERT INTO tag_design VALUES (28, 8, 20);
INSERT INTO tag_design VALUES (29, 2, 21);
INSERT INTO tag_design VALUES (30, 12, 21);
INSERT INTO tag_design VALUES (31, 2, 22);
INSERT INTO tag_design VALUES (32, 2, 23);
INSERT INTO tag_design VALUES (33, 8, 23);
INSERT INTO tag_design VALUES (34, 2, 24);
INSERT INTO tag_design VALUES (35, 12, 24);
INSERT INTO tag_design VALUES (36, 14, 24);
INSERT INTO tag_design VALUES (37, 7, 25);
INSERT INTO tag_design VALUES (38, 8, 25);
INSERT INTO tag_design VALUES (39, 7, 26);
INSERT INTO tag_design VALUES (40, 8, 26);
INSERT INTO tag_design VALUES (42, 6, 27);
INSERT INTO tag_design VALUES (43, 13, 27);
INSERT INTO tag_design VALUES (44, 8, 28);
INSERT INTO tag_design VALUES (45, 13, 28);
INSERT INTO tag_design VALUES (46, 15, 28);
INSERT INTO tag_design VALUES (47, 2, 29);
INSERT INTO tag_design VALUES (48, 7, 29);
INSERT INTO tag_design VALUES (49, 8, 29);
INSERT INTO tag_design VALUES (50, 9, 29);
INSERT INTO tag_design VALUES (51, 12, 29);
INSERT INTO tag_design VALUES (52, 13, 29);
INSERT INTO tag_design VALUES (53, 7, 30);
INSERT INTO tag_design VALUES (54, 8, 30);
INSERT INTO tag_design VALUES (55, 7, 31);
INSERT INTO tag_design VALUES (56, 8, 31);
INSERT INTO tag_design VALUES (57, 9, 32);
INSERT INTO tag_design VALUES (58, 12, 32);
INSERT INTO tag_design VALUES (59, 13, 32);
INSERT INTO tag_design VALUES (60, 7, 33);
INSERT INTO tag_design VALUES (61, 8, 33);
INSERT INTO tag_design VALUES (62, 15, 33);
INSERT INTO tag_design VALUES (63, 7, 34);
INSERT INTO tag_design VALUES (64, 8, 34);
INSERT INTO tag_design VALUES (65, 9, 34);
INSERT INTO tag_design VALUES (66, 12, 34);
INSERT INTO tag_design VALUES (67, 10, 35);
INSERT INTO tag_design VALUES (69, 7, 36);
INSERT INTO tag_design VALUES (70, 8, 36);
INSERT INTO tag_design VALUES (71, 10, 36);
INSERT INTO tag_design VALUES (72, 11, 37);
INSERT INTO tag_design VALUES (73, 11, 38);
INSERT INTO tag_design VALUES (74, 14, 38);
INSERT INTO tag_design VALUES (75, 12, 39);
INSERT INTO tag_design VALUES (76, 14, 39);
INSERT INTO tag_design VALUES (77, 11, 40);
INSERT INTO tag_design VALUES (78, 14, 40);
INSERT INTO tag_design VALUES (79, 13, 41);
INSERT INTO tag_design VALUES (80, 7, 42);
INSERT INTO tag_design VALUES (81, 8, 42);
INSERT INTO tag_design VALUES (83, 7, 43);
INSERT INTO tag_design VALUES (84, 8, 43);
INSERT INTO tag_design VALUES (85, 13, 44);
INSERT INTO tag_design VALUES (86, 9, 45);
INSERT INTO tag_design VALUES (87, 13, 45);
INSERT INTO tag_design VALUES (88, 7, 46);
INSERT INTO tag_design VALUES (89, 8, 46);
INSERT INTO tag_design VALUES (90, 15, 47);
INSERT INTO tag_design VALUES (95, 8, 49);
INSERT INTO tag_design VALUES (96, 16, 49);
INSERT INTO tag_design VALUES (97, 7, 50);
INSERT INTO tag_design VALUES (98, 8, 50);
INSERT INTO tag_design VALUES (99, 8, 51);
INSERT INTO tag_design VALUES (101, 7, 52);
INSERT INTO tag_design VALUES (102, 8, 52);
INSERT INTO tag_design VALUES (103, 2, 53);
INSERT INTO tag_design VALUES (104, 12, 53);
INSERT INTO tag_design VALUES (105, 13, 53);
INSERT INTO tag_design VALUES (106, 14, 53);
INSERT INTO tag_design VALUES (108, 7, 54);
INSERT INTO tag_design VALUES (109, 8, 54);
INSERT INTO tag_design VALUES (110, 8, 55);
INSERT INTO tag_design VALUES (111, 7, 56);
INSERT INTO tag_design VALUES (112, 8, 56);
INSERT INTO tag_design VALUES (113, 8, 57);
INSERT INTO tag_design VALUES (114, 15, 57);
INSERT INTO tag_design VALUES (117, 15, 58);
INSERT INTO tag_design VALUES (118, 12, 59);
INSERT INTO tag_design VALUES (119, 13, 59);
INSERT INTO tag_design VALUES (120, 14, 59);
INSERT INTO tag_design VALUES (121, 8, 60);
INSERT INTO tag_design VALUES (122, 7, 61);
INSERT INTO tag_design VALUES (123, 8, 61);
INSERT INTO tag_design VALUES (124, 7, 62);
INSERT INTO tag_design VALUES (125, 8, 62);
INSERT INTO tag_design VALUES (126, 7, 63);
INSERT INTO tag_design VALUES (127, 8, 63);
INSERT INTO tag_design VALUES (128, 7, 64);
INSERT INTO tag_design VALUES (129, 8, 64);
INSERT INTO tag_design VALUES (130, 7, 65);
INSERT INTO tag_design VALUES (131, 8, 65);
INSERT INTO tag_design VALUES (132, 7, 66);
INSERT INTO tag_design VALUES (133, 8, 66);
INSERT INTO tag_design VALUES (134, 12, 66);
INSERT INTO tag_design VALUES (135, 6, 67);
INSERT INTO tag_design VALUES (136, 10, 68);
INSERT INTO tag_design VALUES (137, 5, 69);
INSERT INTO tag_design VALUES (138, 8, 70);
INSERT INTO tag_design VALUES (139, 10, 71);
INSERT INTO tag_design VALUES (140, 12, 71);
INSERT INTO tag_design VALUES (145, 12, 2);
INSERT INTO tag_design VALUES (146, 7, 3);
INSERT INTO tag_design VALUES (147, 8, 3);
INSERT INTO tag_design VALUES (148, 2, 4);
INSERT INTO tag_design VALUES (149, 13, 4);
INSERT INTO tag_design VALUES (150, 14, 4);
INSERT INTO tag_design VALUES (151, 12, 5);
INSERT INTO tag_design VALUES (152, 13, 5);
INSERT INTO tag_design VALUES (153, 2, 6);
INSERT INTO tag_design VALUES (154, 12, 6);
INSERT INTO tag_design VALUES (155, 7, 1);
INSERT INTO tag_design VALUES (156, 8, 1);
INSERT INTO tag_design VALUES (157, 2, 7);
INSERT INTO tag_design VALUES (158, 7, 8);
INSERT INTO tag_design VALUES (159, 8, 8);
INSERT INTO tag_design VALUES (160, 7, 9);
INSERT INTO tag_design VALUES (161, 8, 9);
INSERT INTO tag_design VALUES (162, 2, 73);
INSERT INTO tag_design VALUES (163, 9, 73);
INSERT INTO tag_design VALUES (164, 12, 73);
INSERT INTO tag_design VALUES (165, 2, 74);
INSERT INTO tag_design VALUES (166, 9, 74);
INSERT INTO tag_design VALUES (167, 12, 74);
INSERT INTO tag_design VALUES (168, 7, 75);
INSERT INTO tag_design VALUES (169, 8, 75);
INSERT INTO tag_design VALUES (170, 12, 76);
INSERT INTO tag_design VALUES (171, 2, 77);
INSERT INTO tag_design VALUES (172, 7, 77);
INSERT INTO tag_design VALUES (173, 13, 77);
INSERT INTO tag_design VALUES (174, 5, 78);
INSERT INTO tag_design VALUES (175, 7, 48);
INSERT INTO tag_design VALUES (176, 8, 48);
INSERT INTO tag_design VALUES (177, 6, 79);
INSERT INTO tag_design VALUES (178, 9, 79);
INSERT INTO tag_design VALUES (179, 6, 80);
INSERT INTO tag_design VALUES (180, 13, 80);

INSERT INTO extra_info VALUES ('bottle_price', '80000');
INSERT INTO extra_info VALUES ('shipment_price', '6000');
INSERT INTO extra_info VALUES ('wines', '["Merlot","Moscatel","Cabernet Sauvignon"]');
INSERT INTO extra_info VALUES ('whatsapp_phone', '3232512182');
INSERT INTO extra_info VALUES ('facebook_id', '100064300652407');
INSERT INTO extra_info VALUES ('instagram_name', 'botellasmemorable');
INSERT INTO extra_info VALUES ('db psw', 'VinosMemorable*');

