--
-- PostgreSQL database dump
--

-- Dumped from database version 15.2
-- Dumped by pg_dump version 15.2

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;
--
-- Name: adminpack; Type: EXTENSION; Schema: -; Owner: -
--

CREATE EXTENSION IF NOT EXISTS adminpack WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION adminpack; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION adminpack IS 'administrative functions for PostgreSQL';


SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: criteria; Type: TABLE; Schema: public; Owner: postgres
--
CREATE TABLE public.criteria (
    id numeric(5,0) NOT NULL,
    criteria_name character varying(200) NOT NULL,
    criteria_types_name character varying(40) NOT NULL,
    data_types_name character varying(20) NOT NULL,
    adding_date date NOT NULL,
    termination_date date,
    minimum_value character varying(40),
    maximum_value character varying(40),
    comment character varying(120),
    unit character varying(10)
);


ALTER TABLE public.criteria OWNER TO postgres;

--
-- Name: code_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.code_seq
    START WITH 31
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.code_seq OWNER TO postgres;

--
-- Name: code_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.code_seq OWNED BY public.criteria.id;


--
-- Name: criteria_allowed_values; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.criteria_allowed_values (
    id numeric(5,0) NOT NULL,
    criteria_id numeric(5,0) NOT NULL,
    allowed_value character varying(100) NOT NULL,
    criteria_adding_date date NOT NULL,
    criteria_deletion_date date,
    comment character varying(120)
);


ALTER TABLE public.criteria_allowed_values OWNER TO postgres;

--
-- Name: criteria_types; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.criteria_types (
    criteria_type_name character varying(40) NOT NULL,
    comment character varying(120)
);


ALTER TABLE public.criteria_types OWNER TO postgres;

--
-- Name: criteria_values; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.criteria_values (
    id numeric(5,0) NOT NULL,
    criteria_allowed_values_id numeric(5,0),
    dbms_id numeric(5,0),
    criteria_value character varying(100) NOT NULL,
    filling_date date NOT NULL,
    deletion_date date,
    comment character varying(120)
);


ALTER TABLE public.criteria_values OWNER TO postgres;

--
-- Name: data_types; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.data_types (
    data_type_name character varying(20) NOT NULL,
    type_code character(1),
    comment character varying(120),
    CONSTRAINT data_types_type_code_check CHECK ((type_code = ANY (ARRAY['N'::bpchar, 'C'::bpchar, 'D'::bpchar])))
);


ALTER TABLE public.data_types OWNER TO postgres;

--
-- Name: dbms; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.dbms (
    id numeric(5,0) NOT NULL,
    dbms_name character varying(120) NOT NULL,
    dbms_firm_name character varying(120) NOT NULL,
    dbms_release_date date NOT NULL,
    dmbs_support_stop_date date,
    comment character varying(120)
);


ALTER TABLE public.dbms OWNER TO postgres;

--
-- Name: dbms_versions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.dbms_versions (
    id numeric(5,0) NOT NULL,
    version_name character varying(120) NOT NULL,
    dbms_id numeric(5,0),
    version_release_date date NOT NULL,
    version_support_stop_date date,
    comment character varying(120)
);


ALTER TABLE public.dbms_versions OWNER TO postgres;

--
-- Name: results; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.results (
    result_id numeric(5,0) NOT NULL,
    tasks_id numeric(5,0),
    dbms_version_id numeric(5,0),
    calculation_date date NOT NULL,
    dbms_rank numeric(5,0) NOT NULL,
    dbms_weight numeric(4,3),
    comment character varying(120)
);


ALTER TABLE public.results OWNER TO postgres;

--
-- Name: results_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.results_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.results_seq OWNER TO postgres;

--
-- Name: results_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.results_seq OWNED BY public.results.result_id;


--
-- Name: task_info; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.task_info (
    task_info_id numeric(5,0) NOT NULL,
    criteria_id numeric(5,0),
    tasks_id numeric(5,0),
    task_value character varying(100),
    filling_date date NOT NULL,
    deletion_date date,
    comparison character varying(20) DEFAULT '='::character varying,
    comment character varying(120)
);


ALTER TABLE public.task_info OWNER TO postgres;

--
-- Name: task_info_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.task_info_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.task_info_seq OWNER TO postgres;

--
-- Name: task_info_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.task_info_seq OWNED BY public.task_info.task_info_id;


--
-- Name: tasks; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.tasks (
    id numeric(5,0) NOT NULL,
    threshold_task numeric(2,0),
    task_name character varying(40),
    filling_date date NOT NULL,
    deletion_date date,
    comment character varying(120),
    selected_method character varying(100) NOT NULL
);


ALTER TABLE public.tasks OWNER TO postgres;

--
-- Name: tasks_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.tasks_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.tasks_seq OWNER TO postgres;

--
-- Name: tasks_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.tasks_seq OWNED BY public.tasks.id;



--
-- Name: dbms_values; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.dbms_values (
    id numeric(5,0) NOT NULL,
    criteria_id numeric(5,0),
    dbms_version_id numeric(5,0),
    value_ numeric(2,0) NOT NULL,
    comment character varying(120)
);


ALTER TABLE public.dbms_values OWNER TO postgres;

--
-- Name: check_allowed_value_update(); Type: FUNCTION; Schema: public; Owner: postgres
--

CREATE FUNCTION public.check_allowed_value_update() RETURNS trigger
    LANGUAGE plpgsql
    AS $$
declare
vtype varchar :='N';
minvalue numeric := 100;
maxvalue numeric := 30000;
begin
select type_code, minimum_value, maximum_value INTO vtype, minvalue, maxvalue from criteria cr, data_types dt
where cr.data_types_name = dt.data_type_name and NEW.criteria_id = cr.id;
if vtype='N' and (cast(new.allowed_value as numeric) < cast(minvalue as numeric) or
cast(new.allowed_value as numeric) > cast(maxvalue as numeric))
then RAISE EXCEPTION 'The entered value is outside the acceptable range between % and %', minvalue, maxvalue;
elsif vtype='D' and (cast(new.allowed_value as date) < cast(minvalue as date) or
cast(new.allowed_value as date)>cast(maxvalue as date))
then RAISE EXCEPTION 'The entered value is outside the acceptable range between % and %', minvalue, maxvalue;
end if;
return new;
END;
$$;


ALTER FUNCTION public.check_allowed_value_update() OWNER TO postgres;

--
-- Name: set_default_value(); Type: FUNCTION; Schema: public; Owner: postgres
--

CREATE FUNCTION public.set_default_value() RETURNS trigger
    LANGUAGE plpgsql
    AS $$
declare
vvalue varchar;
vtype varchar;
minvalue varchar;
maxvalue varchar;
BEGIN
select type_code, minimum_value, maximum_value, allowed_value INTO vtype, minvalue, maxvalue, vvalue
from criteria cr, data_types dt, criteria_allowed_values ca
where cr.data_types_name = dt.data_type_name and ca.criteria_id = cr.id
and new.criteria_allowed_values_id = ca.id;
IF NEW.criteria_value IS NULL THEN new.criteria_value := vvalue;
elsif new.criteria_value != vvalue then
if vtype='C' then
RAISE EXCEPTION 'The entered value is not allowed';
elsif vtype='N' and cast(new.criteria_value as numeric) not BETWEEN cast(minvalue as numeric) AND cast(maxvalue as numeric)
then RAISE EXCEPTION 'The entered value is outside the acceptable range between % and %', minvalue, maxvalue;
elsif vtype='D' and cast(new.criteria_value as date) not BETWEEN cast(minvalue as date) AND cast(maxvalue as date)
then RAISE EXCEPTION 'The entered value is outside the acceptable range between % and %', minvalue, maxvalue;
end if;
end if;
RETURN NEW;
END;
$$;


ALTER FUNCTION public.set_default_value() OWNER TO postgres;

--
-- Name: criteria id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.criteria ALTER COLUMN id SET DEFAULT nextval('public.code_seq'::regclass);


--
-- Name: results result_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.results ALTER COLUMN result_id SET DEFAULT nextval('public.results_seq'::regclass);


--
-- Name: task_info task_info_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.task_info ALTER COLUMN task_info_id SET DEFAULT nextval('public.task_info_seq'::regclass);


--
-- Name: tasks id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tasks ALTER COLUMN id SET DEFAULT nextval('public.tasks_seq'::regclass);


--
-- Data for Name: criteria; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.criteria (id, criteria_name, criteria_types_name, data_types_name, adding_date, termination_date, minimum_value, maximum_value, comment, unit) FROM stdin;
3	К1.2. Триггеры и хранимые процедуры	бинарный	varchar	2025-01-07	\N	\N	\N	\N	\N
4	К1.3. Предусмотренные типы данных	список	varchar	2025-01-07	\N	\N	\N	\N	\N
6	К2.1. Масштабируемость	список	varchar	2025-01-07	\N	\N	\N	\N	\N
7	К2.2. Распределенность	бинарный	varchar	2025-01-07	\N	\N	\N	\N	\N
9	К3.1. Контроль использования памяти компьютера	бинарный	varchar	2025-01-07	\N	\N	\N	\N	\N
10	К3.2. Автонастройка	бинарный	varchar	2025-01-07	\N	\N	\N	\N	\N
12	К4.1. Наличие средств разработки приложений	бинарный	varchar	2025-01-07	\N	\N	\N	\N	\N
13	К4.2. Наличие средств проектирования	список	varchar	2025-01-07	\N	\N	\N	\N	\N
14	К4.3. Наличие многоязыковой поддержки	список	varchar	2025-01-07	\N	\N	\N	\N	\N
15	К4.4. Поддерживаемые языки программирования	список	varchar	2025-01-07	\N	\N	\N	\N	\N
19	К6.1. Восстановление после сбоев	список	varchar	2025-01-07	\N	\N	\N	\N	\N
20	К6.2. Резервное копирование	список	varchar	2025-01-07	\N	\N	\N	\N	\N
21	К6.3. Откат изменений	список	varchar	2025-01-07	\N	\N	\N	\N	\N
22	К6.4. Многоуровневая система защиты	список	varchar	2025-01-07	\N	\N	\N	\N	\N
24	К7.1. Поддерживаемые аппаратные платформы	список	varchar	2025-01-07	\N	\N	\N	\N	\N
27	К7.4. Поддерживаемые операционные системы	список	varchar	2025-01-07	\N	\N	\N	\N	\N
2	К1.1. Используемая модель данных	список	varchar	2025-01-07	\N	\N	\N	\N	\N
25	К7.2. Минимальная тактовая частота процессора	диапазон	numeric	2025-01-07	\N	1.0	4.0	\N	GHz
29	К8.1. Максимальная стоимость лицензии	диапазон	numeric	2025-01-07	\N	0	25000	\N	USD
30	К8.2. Рейтинг СУБД	диапазон	numeric	2025-01-07	\N	1	100	\N	\N
17	К5.1. Минимальный рейтинг транзакций	диапазон	numeric	2025-01-07	\N	1	1000000	\N	TPC
26	К7.3. Максимальный размер адресуемой памяти	диапазон	numeric	2025-01-07	\N	0	4000	\N	GB
1	К1. Моделирование данных	диапазон	varchar	2025-04-20	\N	\N	\N	\N	\N
5	К2. Особенности архитектуры и функциональные возможности	диапазон	varchar	2025-04-20	\N	\N	\N	\N	\N
8	К3. Контроль работы системы	диапазон	varchar	2025-04-20	\N	\N	\N	\N	\N
11	К4. Особенности разработки приложений	диапазон	varchar	2025-04-20	\N	\N	\N	\N	\N
16	К5. Производительность	диапазон	varchar	2025-04-20	\N	\N	\N	\N	\N
18	К6. Надежность	диапазон	varchar	2025-04-20	\N	\N	\N	\N	\N
23	К7. Требования к рабочей среде	диапазон	varchar	2025-04-20	\N	\N	\N	\N	\N
28	К8. Смешанные критерии	диапазон	varchar	2025-04-20	\N	\N	\N	\N	\N
\.


--
-- Data for Name: criteria_allowed_values; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.criteria_allowed_values (id, criteria_id, allowed_value, criteria_adding_date, criteria_deletion_date, comment) FROM stdin;
1	2	Реляционная	2025-01-07	\N	\N
2	2	Документо-ориентированная	2025-01-07	\N	\N
3	2	Объектно-ориентированная	2025-01-07	\N	\N
4	2	Сущность-связь	2025-01-07	\N	\N
5	2	Графовая	2025-01-07	\N	\N
6	2	Иерархическая	2025-01-07	\N	\N
7	2	Сетевая	2025-01-07	\N	\N
8	2	Нереляционная (NoSQL)	2025-01-07	\N	\N
9	3	да	2025-01-07	\N	\N
10	3	нет	2025-01-07	\N	\N
11	4	Строковые	2025-01-07	\N	\N
12	4	Числовые	2025-01-07	\N	\N
13	4	Логические	2025-01-07	\N	\N
14	4	Дата и время	2025-01-07	\N	\N
15	4	Геометрические	2025-01-07	\N	\N
16	4	JSON	2025-01-07	\N	\N
17	4	Структурированные	2025-01-07	\N	\N
18	6	Горизонтальное	2025-01-07	\N	\N
19	6	Вертикальное	2025-01-07	\N	\N
20	7	да	2025-01-07	\N	\N
21	7	нет	2025-01-07	\N	\N
22	9	Динамическое выделение	2025-01-07	\N	\N
23	9	Статическое выделение	2025-01-07	\N	\N
24	10	да	2025-01-07	\N	\N
25	10	нет	2025-01-07	\N	\N
26	12	да	2025-01-07	\N	\N
27	12	нет	2025-01-07	\N	\N
35	14	Русский	2025-01-07	\N	\N
36	14	Английский	2025-01-07	\N	\N
37	14	Испанский	2025-01-07	\N	\N
38	14	Китайский	2025-01-07	\N	\N
39	14	Арабский	2025-01-07	\N	\N
40	14	Французский	2025-01-07	\N	\N
41	14	Немецкий	2025-01-07	\N	\N
42	14	Японский	2025-01-07	\N	\N
43	15	SQL	2025-01-07	\N	\N
44	15	PL/SQL	2025-01-07	\N	\N
45	15	T-SQL	2025-01-07	\N	\N
46	15	PL/pgSQL	2025-01-07	\N	\N
48	15	JavaScript	2025-01-07	\N	\N
49	15	Python	2025-01-07	\N	\N
50	15	Java	2025-01-07	\N	\N
51	15	C#	2025-01-07	\N	\N
52	15	Lua	2025-01-07	\N	\N
53	15	PHP	2025-01-07	\N	\N
54	15	Ruby	2025-01-07	\N	\N
55	15	Go	2025-01-07	\N	\N
56	15	C	2025-01-07	\N	\N
57	15	C++	2025-01-07	\N	\N
58	15	R	2025-01-07	\N	\N
59	15	Scala	2025-01-07	\N	\N
60	15	Kotlin	2025-01-07	\N	\N
61	15	Swift	2025-01-07	\N	\N
62	19	Журналирование (Logging)	2025-01-12	\N	\N
63	19	Резервное копирование (Backup)	2025-01-12	\N	\N
67	19	Flashback	2025-01-12	\N	\N
68	19	Point-in-Time Recovery	2025-01-12	\N	\N
69	20	Полное	2025-01-12	\N	\N
70	20	Инкрементное	2025-01-12	\N	\N
71	20	Дифференциальное	2025-01-12	\N	\N
72	20	Горячее	2025-01-12	\N	\N
73	20	Холодное	2025-01-12	\N	\N
74	20	Физическое	2025-01-12	\N	\N
75	20	Логическое	2025-01-12	\N	\N
76	21	Поддержка транзакций на уровне отдельных строк	2025-01-12	\N	\N
77	21	Поддержка транзакций на уровне таблиц	2025-01-12	\N	\N
78	22	Аутентификация	2025-01-12	\N	\N
79	22	Авторизация	2025-01-12	\N	\N
80	22	Шифрование	2025-01-12	\N	\N
81	22	Мониторинг и аудит	2025-01-12	\N	\N
82	22	Контроль доступа	2025-01-12	\N	\N
83	22	Защита от SQL-инъекций	2025-01-12	\N	\N
84	22	Резервное копирование и восстановление	2025-01-12	\N	\N
85	22	Физическая безопасность	2025-01-12	\N	\N
86	22	Обновление и патчинг	2025-01-12	\N	\N
87	24	Intel	2025-01-12	\N	\N
88	24	AMD	2025-01-12	\N	\N
89	24	IBM	2025-01-12	\N	\N
90	27	Windows	2025-01-12	\N	\N
91	27	Linux	2025-01-12	\N	\N
92	27	macOS	2025-01-12	\N	\N
93	27	FreeBSD	2025-01-12	\N	\N
94	27	Solaris	2025-01-12	\N	\N
95	27	Docker	2025-01-12	\N	\N
96	27	OpenBSD	2025-01-12	\N	\N
97	27	NetBSD	2025-01-12	\N	\N
98	27	OS X	2025-01-12	\N	\N
99	27	AIX	2025-01-12	\N	\N
100	27	HP/UX	2025-01-12	\N	\N
101	27	Tru64 Unix	2025-01-12	\N	\N
102	27	UnixWare	2025-01-12	\N	\N
103	27	z/OS	2025-01-12	\N	\N
104	17	1000	2025-01-19	\N	\N
105	26	1	2025-01-19	\N	\N
106	29	1000	2025-01-19	\N	\N
107	30	5	2025-01-19	\N	\N
64	19	Восстановление (Recovery)	2025-01-12	\N	\N
65	19	Репликация (Replication)	2025-01-12	\N	\N
66	19	Технологии высокой доступности (High Availability)	2025-01-12	\N	\N
108	25	2.6	2025-04-14	\N	\N
28	13	pgModeler	2025-01-07	\N	\N
29	13	DbSchema	2025-01-07	\N	\N
30	13	SQL Power Architect	2025-01-07	\N	\N
31	13	Toad Data Modeler	2025-01-07	\N	\N
32	13	ER/Studio	2025-01-07	\N	\N
33	13	Vertabelo	2025-01-07	\N	\N
34	13	Lucidchart	2025-01-07	\N	\N
109	13	DrawSQL	2025-04-15	\N	\N
110	13	Microsoft Visual Studio	2025-04-15	\N	\N
111	13	IntelliJ IDEA	2025-04-15	\N	\N
112	13	Xojo	2025-04-15	\N	\N
113	13	Liquibase	2025-04-15	\N	\N
114	13	Flyway	2025-04-15	\N	\N
115	13	Redgate SQL Source Control	2025-04-15	\N	\N
116	13	OutSystems	2025-04-15	\N	\N
117	13	Mendix	2025-04-15	\N	\N
118	13	AppGyver	2025-04-15	\N	\N
119	13	Bubble	2025-04-15	\N	\N
\.


--
-- Data for Name: criteria_types; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.criteria_types (criteria_type_name, comment) FROM stdin;
список	\N
диапазон	\N
бинарный	\N
\.


--
-- Data for Name: criteria_values; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.criteria_values (id, criteria_allowed_values_id, dbms_id, criteria_value, filling_date, deletion_date, comment) FROM stdin;
1	1	1	Реляционная	2025-03-15	\N	\N
2	9	1	да	2025-04-02	\N	\N
3	11	1	Строковые	2025-04-02	\N	\N
4	12	1	Числовые	2025-04-02	\N	\N
6	14	1	Дата и время	2025-04-02	\N	\N
5	15	1	Геометрические	2025-04-02	\N	\N
7	17	1	Структурированные	2025-04-02	\N	\N
8	18	1	Горизонтальное	2025-04-02	\N	\N
9	20	1	да	2025-04-02	\N	\N
10	22	1	Динамическое выделение	2025-04-02	\N	\N
11	23	1	Статическое выделение	2025-04-02	\N	\N
12	24	1	да	2025-04-02	\N	\N
13	26	1	да	2025-04-02	\N	\N
20	35	1	Русский	2025-04-02	\N	\N
21	36	1	Английский	2025-04-02	\N	\N
22	37	1	Испанский	2025-04-02	\N	\N
23	38	1	Китайский	2025-04-02	\N	\N
24	39	1	Арабский	2025-04-02	\N	\N
25	40	1	Французский	2025-04-02	\N	\N
26	41	1	Немецкий	2025-04-02	\N	\N
27	42	1	Японский	2025-04-02	\N	\N
28	43	1	SQL	2025-04-02	\N	\N
29	44	1	PL/SQL	2025-04-02	\N	\N
30	49	1	Python	2025-04-02	\N	\N
31	50	1	Java	2025-04-02	\N	\N
32	56	1	C	2025-04-02	\N	\N
33	57	1	C++	2025-04-02	\N	\N
34	58	1	R	2025-04-02	\N	\N
35	62	1	Журналирование (Logging)	2025-04-03	\N	\N
36	63	1	Резервное копирование (Backup)	2025-04-03	\N	\N
37	64	1	Восстановление (Recovery)	2025-04-03	\N	\N
38	65	1	Репликация (Replication)	2025-04-03	\N	\N
39	66	1	Технологии высокой доступности (High Availability)	2025-04-03	\N	\N
40	67	1	Flashback	2025-04-03	\N	\N
41	68	1	Point-in-Time Recovery	2025-04-03	\N	\N
42	69	1	Полное	2025-04-03	\N	\N
43	70	1	Инкрементное	2025-04-03	\N	\N
44	71	1	Дифференциальное	2025-04-03	\N	\N
45	72	1	Горячее	2025-04-03	\N	\N
46	73	1	Холодное	2025-04-03	\N	\N
47	74	1	Физическое	2025-04-03	\N	\N
48	75	1	Логическое	2025-04-03	\N	\N
49	78	1	Аутентификация	2025-04-03	\N	\N
50	79	1	Авторизация	2025-04-03	\N	\N
51	80	1	Шифрование	2025-04-03	\N	\N
52	81	1	Мониторинг и аудит	2025-04-03	\N	\N
53	82	1	Контроль доступа	2025-04-03	\N	\N
54	83	1	Защита от SQL-инъекций	2025-04-03	\N	\N
55	84	1	Резервное копирование и восстановление	2025-04-03	\N	\N
56	85	1	Физическая безопасность	2025-04-03	\N	\N
57	86	1	Обновление и патчинг	2025-04-03	\N	\N
58	87	1	Intel	2025-04-03	\N	\N
59	88	1	AMD	2025-04-03	\N	\N
60	89	1	IBM	2025-04-03	\N	\N
61	90	1	Windows	2025-04-03	\N	\N
62	91	1	Linux	2025-04-03	\N	\N
63	94	1	Solaris	2025-04-03	\N	\N
64	95	1	Docker	2025-04-03	\N	\N
65	99	1	AIX	2025-04-03	\N	\N
66	100	1	HP/UX	2025-04-03	\N	\N
67	108	1	2.6	2025-04-14	\N	\N
68	1	4	Реляционная	2025-04-14	\N	\N
69	9	4	да	2025-04-14	\N	\N
70	11	4	Строковые	2025-04-14	\N	\N
71	12	4	Числовые	2025-04-14	\N	\N
72	13	4	Логические	2025-04-14	\N	\N
73	14	4	Дата и время	2025-04-14	\N	\N
74	15	4	Геометрические	2025-04-14	\N	\N
75	16	4	JSON	2025-04-14	\N	\N
76	17	4	Структурированные	2025-04-14	\N	\N
77	19	4	Вертикальное	2025-04-14	\N	\N
78	21	4	нет	2025-04-14	\N	\N
79	22	4	Динамическое выделение	2025-04-14	\N	\N
80	25	4	нет	2025-04-14	\N	\N
81	26	4	да	2025-04-14	\N	\N
91	28	4	pgModeler	2025-04-15	\N	\N
15	29	1	DbSchema	2025-04-02	\N	\N
16	30	1	SQL Power Architect	2025-04-02	\N	\N
17	32	1	ER/Studio	2025-04-02	\N	\N
18	33	1	Vertabelo	2025-04-02	\N	\N
19	34	1	Lucidchart	2025-04-02	\N	\N
82	31	1	Toad Data Modeler	2025-04-15	\N	\N
83	109	1	DrawSQL	2025-04-15	\N	\N
84	110	1	Microsoft Visual Studio	2025-04-15	\N	\N
85	111	1	IntelliJ IDEA	2025-04-15	\N	\N
86	112	1	Xojo	2025-04-15	\N	\N
87	113	1	Liquibase	2025-04-15	\N	\N
88	114	1	Flyway	2025-04-15	\N	\N
89	116	1	OutSystems	2025-04-15	\N	\N
90	117	1	Mendix	2025-04-15	\N	\N
92	29	4	DbSchema	2025-04-15	\N	\N
93	30	4	SQL Power Architect	2025-04-15	\N	\N
94	31	4	Toad Data Modeler	2025-04-15	\N	\N
95	32	4	ER/Studio	2025-04-15	\N	\N
96	33	4	Vertabelo	2025-04-15	\N	\N
97	34	4	Lucidchart	2025-04-15	\N	\N
98	109	4	DrawSQL	2025-04-15	\N	\N
99	110	4	Microsoft Visual Studio	2025-04-15	\N	\N
100	111	4	IntelliJ IDEA	2025-04-15	\N	\N
101	112	4	Xojo	2025-04-15	\N	\N
102	113	4	Liquibase	2025-04-15	\N	\N
103	114	4	Flyway	2025-04-15	\N	\N
104	116	4	OutSystems	2025-04-15	\N	\N
105	117	4	Mendix	2025-04-15	\N	\N
106	104	1	10000	2025-04-15	\N	\N
108	106	1	500	2025-04-15	\N	\N
109	107	1	1	2025-04-15	\N	\N
107	105	1	4000	2025-04-15	\N	\N
110	35	4	Русский	2025-04-15	\N	\N
111	36	4	Английский	2025-04-15	\N	\N
112	37	4	Испанский	2025-04-15	\N	\N
113	38	4	Китайский	2025-04-15	\N	\N
114	39	4	Арабский	2025-04-15	\N	\N
115	40	4	Французский	2025-04-15	\N	\N
116	41	4	Немецкий	2025-04-15	\N	\N
117	42	4	Японский	2025-04-15	\N	\N
118	43	4	SQL	2025-04-15	\N	\N
119	46	4	PL/pgSQL	2025-04-15	\N	\N
120	48	4	JavaScript	2025-04-15	\N	\N
121	49	4	Python	2025-04-15	\N	\N
122	50	4	Java	2025-04-15	\N	\N
123	52	4	Lua	2025-04-15	\N	\N
124	54	4	Ruby	2025-04-15	\N	\N
125	55	4	Go	2025-04-15	\N	\N
126	56	4	C	2025-04-15	\N	\N
127	57	4	C++	2025-04-15	\N	\N
128	58	4	R	2025-04-15	\N	\N
129	62	4	Журналирование (Logging)	2025-04-18	\N	\N
130	63	4	Резервное копирование (Backup)	2025-04-18	\N	\N
131	64	4	Восстановление (Recovery)	2025-04-18	\N	\N
132	65	4	Репликация (Replication)	2025-04-18	\N	\N
133	66	4	Технологии высокой доступности (High Availability)	2025-04-18	\N	\N
134	68	4	Point-in-Time Recovery	2025-04-18	\N	\N
135	69	4	Полное	2025-04-18	\N	\N
136	72	4	Горячее	2025-04-18	\N	\N
137	73	4	Холодное	2025-04-18	\N	\N
138	74	4	Физическое	2025-04-18	\N	\N
139	75	4	Логическое	2025-04-18	\N	\N
140	76	4	Поддержка транзакций на уровне отдельных строк	2025-04-18	\N	\N
141	78	4	Аутентификация	2025-04-18	\N	\N
142	79	4	Авторизация	2025-04-18	\N	\N
143	80	4	Шифрование	2025-04-18	\N	\N
144	81	4	Мониторинг и аудит	2025-04-18	\N	\N
145	82	4	Контроль доступа	2025-04-18	\N	\N
146	83	4	Защита от SQL-инъекций	2025-04-18	\N	\N
147	84	4	Резервное копирование и восстановление	2025-04-18	\N	\N
148	86	4	Обновление и патчинг	2025-04-18	\N	\N
149	87	4	Intel	2025-04-19	\N	\N
150	88	4	AMD	2025-04-19	\N	\N
151	90	4	Windows	2025-04-19	\N	\N
152	91	4	Linux	2025-04-19	\N	\N
153	92	4	macOS	2025-04-19	\N	\N
154	93	4	FreeBSD	2025-04-19	\N	\N
155	95	4	Docker	2025-04-19	\N	\N
156	96	4	OpenBSD	2025-04-19	\N	\N
157	97	4	NetBSD	2025-04-19	\N	\N
158	98	4	OS X	2025-04-19	\N	\N
159	104	4	5000	2025-04-19	\N	\N
160	105	4	4000	2025-04-19	\N	\N
161	106	4	0	2025-04-26	\N	\N
162	107	4	4	2025-04-26	\N	\N
163	108	4	1	2025-04-26	\N	\N
\.


--
-- Data for Name: data_types; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.data_types (data_type_name, type_code, comment) FROM stdin;
numeric	N	\N
char	C	\N
varchar	C	\N
date	D	\N
\.


--
-- Data for Name: dbms; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.dbms (id, dbms_name, dbms_firm_name, dbms_release_date, dmbs_support_stop_date, comment) FROM stdin;
1	Oracle Database	Oracle Corporation	1979-11-10	\N	\N
2	PostgreSQL	PostgreSQL Global Development Group	1996-07-08	\N	\N
3	MySQL	Oracle Corporation	1995-05-23	\N	\N
4	Microsoft SQL Server	Microsoft	1989-04-24	\N	\N
\.


--
-- Data for Name: dbms_versions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.dbms_versions (id, version_name, dbms_id, version_release_date, version_support_stop_date, comment) FROM stdin;
1	Oracle Database 19c	1	2019-02-01	\N	\N
2	Oracle Database 21c	1	2020-12-01	\N	\N
3	Oracle Database 23ai	1	2024-05-02	\N	\N
4	PostgreSQL 13	2	2020-09-24	\N	\N
5	PostgreSQL 14	2	2021-09-30	\N	\N
6	PostgreSQL 15	2	2022-10-13	\N	\N
7	PostgreSQL 16	2	2023-09-14	\N	\N
8	PostgreSQL 17	2	2024-09-26	\N	\N
9	MySQL 8.0 LTS	3	2018-04-19	\N	\N
10	MySQL 8.1 IR	3	2023-07-18	2023-10-01	\N
11	MySQL 8.2 IR	3	2023-10-25	2024-01-01	\N
12	MySQL 8.3 IR	3	2024-01-16	2024-04-01	\N
13	MySQL 8.4 LTS	3	2024-04-30	\N	\N
14	MySQL 9.0 IR	3	2024-07-01	2024-10-01	\N
15	MySQL 9.1 IR	3	2024-10-15	\N	\N
16	SQL Server 2016	4	2016-06-01	\N	\N
17	SQL Server 2017	4	2017-10-02	\N	\N
18	SQL Server 2019	4	2019-11-04	\N	\N
19	SQL Server 2022	4	2022-11-16	\N	\N
\.


--
-- Data for Name: dbms_values; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.dbms_values (id, criteria_id, dbms_version_id, value_, comment) FROM stdin;
1	2	1	10	\N
2	2	4	9	\N
3	2	15	8	\N
4	2	19	9	\N
5	3	1	10	\N
6	3	4	9	\N
7	3	15	8	\N
8	3	19	10	\N
9	4	1	10	\N
10	4	4	9	\N
11	4	15	8	\N
12	4	19	9	\N
13	6	1	9	\N
14	6	4	8	\N
15	6	15	7	\N
16	6	19	9	\N
17	7	1	9	\N
18	7	4	8	\N
19	7	15	6	\N
20	7	19	8	\N
21	9	1	9	\N
22	9	4	8	\N
23	9	15	7	\N
24	9	19	9	\N
25	10	1	10	\N
26	10	4	8	\N
27	10	15	7	\N
28	10	19	9	\N
29	12	1	10	\N
30	12	4	7	\N
31	12	15	6	\N
32	12	19	10	\N
33	13	1	9	\N
34	13	4	7	\N
35	13	15	6	\N
36	13	19	9	\N
37	14	1	10	\N
38	14	4	9	\N
39	14	15	7	\N
40	14	19	9	\N
41	15	1	10	\N
42	15	4	9	\N
43	15	15	8	\N
44	15	19	9	\N
45	19	1	10	\N
46	19	4	8	\N
47	19	15	7	\N
48	19	19	9	\N
49	20	1	10	\N
50	20	4	8	\N
51	20	15	7	\N
52	20	19	9	\N
53	21	1	10	\N
54	21	4	8	\N
55	21	15	7	\N
56	21	19	9	\N
57	22	1	10	\N
58	22	4	9	\N
59	22	15	8	\N
60	22	19	10	\N
61	24	1	10	\N
62	24	4	8	\N
63	24	15	7	\N
64	24	19	9	\N
65	25	1	8	\N
66	25	4	7	\N
67	25	15	6	\N
68	25	19	8	\N
69	26	1	10	\N
70	26	4	8	\N
71	26	15	7	\N
72	26	19	9	\N
73	27	1	10	\N
74	27	4	9	\N
75	27	15	8	\N
76	27	19	9	\N
77	29	1	2	\N
78	29	4	10	\N
79	29	15	10	\N
80	29	19	5	\N
81	30	1	10	\N
82	30	4	8	\N
83	30	15	7	\N
84	30	19	9	\N
\.


--
-- Name: code_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.code_seq', 31, false);


--
-- Name: results_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.results_seq', 54, true);


--
-- Name: task_info_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.task_info_seq', 220, true);


--
-- Name: tasks_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.tasks_seq', 97, true);


--
-- Name: criteria_allowed_values criteria_allowed_values_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.criteria_allowed_values
    ADD CONSTRAINT criteria_allowed_values_pkey PRIMARY KEY (id);


--
-- Name: criteria criteria_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.criteria
    ADD CONSTRAINT criteria_pkey PRIMARY KEY (id);


--
-- Name: criteria_types criteria_types_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.criteria_types
    ADD CONSTRAINT criteria_types_pkey PRIMARY KEY (criteria_type_name);


--
-- Name: criteria_values criteria_values_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.criteria_values
    ADD CONSTRAINT criteria_values_pkey PRIMARY KEY (id);


--
-- Name: data_types data_types_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.data_types
    ADD CONSTRAINT data_types_pkey PRIMARY KEY (data_type_name);


--
-- Name: dbms dbms_dbms_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dbms
    ADD CONSTRAINT dbms_dbms_name_key UNIQUE (dbms_name);


--
-- Name: dbms dbms_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dbms
    ADD CONSTRAINT dbms_pkey PRIMARY KEY (id);


--
-- Name: dbms_versions dbms_versions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dbms_versions
    ADD CONSTRAINT dbms_versions_pkey PRIMARY KEY (id);


--
-- Name: dbms_versions dbms_versions_version_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dbms_versions
    ADD CONSTRAINT dbms_versions_version_name_key UNIQUE (version_name);


--
-- Name: results results_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.results
    ADD CONSTRAINT results_pkey PRIMARY KEY (result_id);


--
-- Name: task_info task_info_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.task_info
    ADD CONSTRAINT task_info_pkey PRIMARY KEY (task_info_id);


--
-- Name: tasks tasks_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tasks
    ADD CONSTRAINT tasks_pkey PRIMARY KEY (id);


--
-- Name: dbms_values dbms_values_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dbms_values
    ADD CONSTRAINT dbms_values_pkey PRIMARY KEY (id);

--
-- Name: criteria_allowed_values check_allowed_value; Type: TRIGGER; Schema: public; Owner: postgres
--

CREATE TRIGGER check_allowed_value BEFORE INSERT OR UPDATE OF allowed_value ON public.criteria_allowed_values FOR EACH ROW EXECUTE FUNCTION public.check_allowed_value_update();


--
-- Name: criteria_values set_default_values; Type: TRIGGER; Schema: public; Owner: postgres
--

CREATE TRIGGER set_default_values BEFORE INSERT OR UPDATE OF criteria_value ON public.criteria_values FOR EACH ROW EXECUTE FUNCTION public.set_default_value();


--
-- Name: criteria_allowed_values criteria_allowed_values_criteria_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.criteria_allowed_values
    ADD CONSTRAINT criteria_allowed_values_criteria_id_fkey FOREIGN KEY (criteria_id) REFERENCES public.criteria(id);


--
-- Name: criteria criteria_criteria_types_name_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.criteria
    ADD CONSTRAINT criteria_criteria_types_name_fkey FOREIGN KEY (criteria_types_name) REFERENCES public.criteria_types(criteria_type_name);


--
-- Name: criteria criteria_data_types_name_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.criteria
    ADD CONSTRAINT criteria_data_types_name_fkey FOREIGN KEY (data_types_name) REFERENCES public.data_types(data_type_name);


--
-- Name: criteria_values criteria_values_criteria_allowed_values_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.criteria_values
    ADD CONSTRAINT criteria_values_criteria_allowed_values_id_fkey FOREIGN KEY (criteria_allowed_values_id) REFERENCES public.criteria_allowed_values(id);


--
-- Name: criteria_values criteria_values_dbms_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.criteria_values
    ADD CONSTRAINT criteria_values_dbms_id_fkey FOREIGN KEY (dbms_id) REFERENCES public.dbms_versions(id);


--
-- Name: dbms_versions dbms_versions_dbms_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dbms_versions
    ADD CONSTRAINT dbms_versions_dbms_id_fkey FOREIGN KEY (dbms_id) REFERENCES public.dbms(id);


--
-- Name: results results_dbms_version_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.results
    ADD CONSTRAINT results_dbms_version_id_fkey FOREIGN KEY (dbms_version_id) REFERENCES public.dbms_versions(id);


--
-- Name: results results_tasks_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.results
    ADD CONSTRAINT results_tasks_id_fkey FOREIGN KEY (tasks_id) REFERENCES public.tasks(id);


--
-- Name: task_info task_info_criteria_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.task_info
    ADD CONSTRAINT task_info_criteria_id_fkey FOREIGN KEY (criteria_id) REFERENCES public.criteria(id);


--
-- Name: task_info task_info_tasks_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.task_info
    ADD CONSTRAINT task_info_tasks_id_fkey FOREIGN KEY (tasks_id) REFERENCES public.tasks(id);


--
-- Name: dbms_values dbms_values_criteria_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dbms_values
    ADD CONSTRAINT dbms_values_criteria_id_fkey FOREIGN KEY (criteria_id) REFERENCES public.criteria(id);


--
-- Name: dbms_values dbms_values_dbms_version_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dbms_values
    ADD CONSTRAINT dbms_values_dbms_version_id_fkey FOREIGN KEY (dbms_version_id) REFERENCES public.dbms_versions(id);

--
-- PostgreSQL database dump complete
--


