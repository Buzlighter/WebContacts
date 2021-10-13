-- Table: public.contacts

-- DROP TABLE public.contacts;

CREATE TABLE IF NOT EXISTS public.contacts
(
    id integer NOT NULL DEFAULT nextval('contacts_id_seq'::regclass),
    name character varying COLLATE pg_catalog."default",
    ser_name character varying COLLATE pg_catalog."default",
    second_name character varying COLLATE pg_catalog."default",
    organisation character varying COLLATE pg_catalog."default",
    "position" character varying COLLATE pg_catalog."default",
    email character varying COLLATE pg_catalog."default",
    tel character varying COLLATE pg_catalog."default",
    CONSTRAINT contacts_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE public.contacts
    OWNER to postgres;