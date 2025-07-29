CREATE DATABASE IF NOT EXISTS transport

CREATE TABLE IF NOT EXISTS public.cities(
    cep character varying(255) PRIMARY KEY,
    city character varying(255),
    uf character varying(2),
    sunday BOOLEAN,
    monday BOOLEAN,
    tuesday BOOLEAN,
    wednesday BOOLEAN,
    thursday BOOLEAN,
    friday BOOLEAN,
    saturday BOOLEAN
);

CREATE OR REPLACE FUNCTION fnc_calcular_prazo(
    cep_origem varchar, 
    cep_destino varchar, 
    data_embarque date
) RETURNS date AS $$
DECLARE
    cidade_destino cities%ROWTYPE;
    dias_uteis boolean[];
    qtd_dias integer;
BEGIN

    SELECT * INTO cidade_destino 
    FROM cities 
    WHERE cep = cep_destino;
    
    IF NOT FOUND THEN
        RAISE EXCEPTION 'Cep inexistente';
    END IF;
    
    IF NOT (
        cidade_destino.monday OR 
        cidade_destino.tuesday OR 
        cidade_destino.wednsdays OR 
        cidade_destino.thursday OR 
        cidade_destino.friday
    ) THEN
        RAISE EXCEPTION 'Sem dias úteis';
    END IF;
    
    IF cep_origem = cep_destino THEN
        qtd_dias := 3;
    ELSE
        qtd_dias := 5;
    END IF;
    
    dias_uteis := ARRAY[
        cidade_destino.monday,
        cidade_destino.tuesday,
        cidade_destino.wednsdays,
        cidade_destino.thursday,
        cidade_destino.friday,
        false,
        false
    ];
    
    -- Use helper function to add the required number of valid days
    RETURN fnc_somar_dias_uteis(data_embarque, dias_uteis, qtd_dias);
END;
$$ LANGUAGE plpgsql;

-- Helper function remains unchanged
CREATE OR REPLACE FUNCTION fnc_somar_dias_uteis(
    data_inicial date,
    dias_uteis boolean[],
    qtd_dias integer
) RETURNS date AS $$
DECLARE
    data_entrega date := data_inicial;
    dias integer := 0;
    contador integer := 0;
    dia_semana integer;
BEGIN
    WHILE dias < qtd_dias LOOP
        contador := contador + 1;
        
        data_entrega := data_entrega + INTERVAL '1 day';
        dia_semana := EXTRACT(ISODOW FROM data_entrega);
        
        IF dias_uteis[dia_semana] THEN
            dias := dias + 1;
        END IF;
    END LOOP;
    
    RETURN data_entrega;
END;
$$ LANGUAGE plpgsql;
