-- Список уникальных типов самолётов, зарегистрированных в России
select vw_aircraft.Вид_воздушного_судна, vw_aircraft.Наменование_воздушного_судна from vw_aircraft where vw_aircraft.Вид_воздушного_судна = "самолет" GROUP by vw_aircraft.Наменование_воздушного_судна;

-- Какой тип самолета имеет самую раннюю дату выдачи сертификата?
select vw_aircraft.Вид_воздушного_судна, vw_aircraft.Наменование_воздушного_судна, min(vw_aircraft.Дата_действующего_свидетельства_о_регистрации) from vw_aircraft;

-- Создание представлений
CREATE VIEW "vw_aircraft" as
select 
type_aircraft.type_name as "Вид_воздушного_судна",
name_aircraft.nazvanie as "Наменование_воздушного_судна",
aircraft.Znaki as "Опознавательные_знаки",
aircraft.Serial as "Серийный_№",
aircraft.Ident as "Идентификац_№",
aircraft.Number_svid as "Номер_свидетельства_о_регистрации",
Data_Svids.name_data_svid as "Дата_действующего_свидетельства_о_регистрации"
from aircraft, type_aircraft, name_aircraft, Data_Svids
where aircraft.id_data_svid = Data_Svids.id_data_svid and aircraft.id_naimen = name_aircraft.id_naimen and type_aircraft.id_type = aircraft.id_type

CREATE VIEW "vw_airlines" as 
select airlines.id_line as "Номер_линии", 
airlines.firm_name as "Название_фирмы", 
airlines.firm_full_name as "Полное_наименование_фирмы", 
names_airlines.name_airlines as "Аэропорт", 
planes_airlines.spisok as "Закреплённые_ВС"
from airlines, names_airlines, planes_airlines 
where airlines.id_names_lines = names_airlines.id_names_lines and airlines.id_planes = planes_airlines.id_planes

CREATE VIEW "vw_airports" as 
select airports.airoport_name as "Наименование_аэродрома", 
airports.svidetelstvo as "Свидетельство_об_эксплуатации", 
holder_airport.holder_name as "Владелец", 
buk_airports.Nachertanie as "Класс_аэродрома"
from airports, holder_airport, buk_airports 
where airports.id_bukva = buk_airports.id_bukva and holder_airport.id_holder = airports.id_holder

CREATE VIEW "vw_cargo_transportation" as
select airports_cargo_pass.cargo_pass_name as "Наименование_аэропорта_в_РФ", period_cargo_pass.cargo_pass_year as "Год_периода_данных", Jan as "Январь", Feb as "Февраль", Mar as "Март", Apr as "Апрель", May as "Май", Jun as "Июнь", Jul as "Июль", Aug as "Август", Sep as "Сентябрь", Oct as "Октябрь", Nov As "Ноябрь", cargo.Dec as "Декабрь", cargo.Itogo as "Январь-Декабрь"
FROM airports_cargo_pass, period_cargo_pass, cargo 
where cargo.id_name_airport = airports_cargo_pass.id_name_airport and period_cargo_pass.id_year_period = cargo.id_year_period

CREATE VIEW "vw_passangers_transportation" as
select airports_cargo_pass.cargo_pass_name as "Наименование_аэропорта_в_РФ", period_cargo_pass.cargo_pass_year as "Год_периода_данных", Jan as "Январь", Feb as "Февраль", Mar as "Март", Apr as "Апрель", May as "Май", Jun as "Июнь", Jul as "Июль", Aug as "Август", Sep as "Сентябрь", Oct as "Октябрь", Nov As "Ноябрь", passangers.Dec as "Декабрь", passangers.Itogo as "Январь-Декабрь"
FROM airports_cargo_pass, period_cargo_pass, passangers 
where passangers.id_name_airport = airports_cargo_pass.id_name_airport and period_cargo_pass.id_year_period = passangers.id_year_period