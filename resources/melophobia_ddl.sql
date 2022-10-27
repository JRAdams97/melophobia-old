-- =====================================================================================================================
--   INITIALISATION
-- =====================================================================================================================
DROP SCHEMA IF EXISTS melophobia CASCADE;

-- =====================================================================================================================
--   SCHEMA
-- =====================================================================================================================
CREATE SCHEMA melophobia;
GRANT ALL ON SCHEMA melophobia TO postgres;
GRANT ALL ON SCHEMA melophobia TO public;

-- =====================================================================================================================
--   TABLES
-- =====================================================================================================================
-- ARTIST --------------------------------------------------------------------------------------------------------------
CREATE TABLE melophobia.artist (
                    id serial   NOT NULL,
                  name text     NOT NULL,
        formation_date char(10),
        formation_area text,
  formation_country_id int      NOT NULL,
          disband_date char(10),
          disband_area text,
    disband_country_id int,
             favourite boolean  DEFAULT FALSE NOT NULL,
        artist_type_id int      NOT NULL,
                  isni char(19) UNIQUE,
       amazon_music_id text     UNIQUE,
           wikidata_id text     UNIQUE,
            CONSTRAINT artist_pk PRIMARY KEY (id)
);

-- ARTIST_GENRES -------------------------------------------------------------------------------------------------------
CREATE TABLE melophobia.artist_genres (
   artist_id int NOT NULL,
    genre_id int NOT NULL,
  CONSTRAINT artist_genres_pk PRIMARY KEY (artist_id, genre_id)
);

-- ARTIST_IPIS ---------------------------------------------------------------------------------------------------------
CREATE TABLE melophobia.artist_ipis (
   artist_id int    NOT NULL,
      ipi_id text   UNIQUE NOT NULL,
  CONSTRAINT artist_ipis_pk PRIMARY KEY (artist_id, ipi_id)
);

-- ARTIST_TYPE ---------------------------------------------------------------------------------------------------------
CREATE TABLE melophobia.artist_type (
          id serial  NOT NULL,
        name text    UNIQUE NOT NULL,
  CONSTRAINT artist_type_pk PRIMARY KEY (id)
);

-- CATALOGUE_ITEMS -----------------------------------------------------------------------------------------------------
CREATE TABLE melophobia.catalogue_items (
                 id serial NOT NULL,
           label_id int    NOT NULL,
         release_id int,
       catalogue_id text   NOT NULL,
  release_status_id int    NOT NULL,
         CONSTRAINT catalogue_items_pk PRIMARY KEY (id)
);

-- CATALOGUE_MEDIA -----------------------------------------------------------------------------------------------------
CREATE TABLE melophobia.catalogue_media (
  global_catalogue_id int NOT NULL,
             media_id int NOT NULL,
           CONSTRAINT catalogue_media_pk PRIMARY KEY (global_catalogue_id, media_id)
);

-- COUNTRY -------------------------------------------------------------------------------------------------------------
CREATE TABLE melophobia.country (
           id serial NOT NULL,
         name text   UNIQUE NOT NULL,
  wikidata_id text   UNIQUE,
   CONSTRAINT country_pk PRIMARY KEY (id)
);

-- GENRE ---------------------------------------------------------------------------------------------------------------
CREATE TABLE melophobia.genre (
            id serial   NOT NULL,
          name text     UNIQUE NOT NULL,
   origin_year smallint NOT NULL,
     favourite boolean  DEFAULT FALSE NOT NULL,
  parent_genre int,
   wikidata_id text     UNIQUE,
    CONSTRAINT genre_pk PRIMARY KEY (id)
);

-- IPI -----------------------------------------------------------------------------------------------------------------
CREATE TABLE melophobia.ipi (
      ipi_id text UNIQUE NOT NULL,
  CONSTRAINT ipi_pk PRIMARY KEY (ipi_id)
);

-- LABEL ---------------------------------------------------------------------------------------------------------------
CREATE TABLE melophobia.label (
                    id serial   NOT NULL,
                  name text     NOT NULL,
        formation_date char(10),
        formation_area text,
  formation_country_id int      NOT NULL,
          closing_date char(10),
             favourite boolean  DEFAULT FALSE NOT NULL,
            label_code text     UNIQUE,
           wikidata_id text     UNIQUE,
            CONSTRAINT label_pk PRIMARY KEY (id)
);

-- LABEL_IPIS ----------------------------------------------------------------------------------------------------------
CREATE TABLE melophobia.label_ipis (
    label_id int  NOT NULL,
      ipi_id text UNIQUE NOT NULL,
  CONSTRAINT label_ipis_pk PRIMARY KEY (label_id, ipi_id)
);

-- LANGUAGE ------------------------------------------------------------------------------------------------------------
CREATE TABLE melophobia.language (
           id serial NOT NULL,
         name text   UNIQUE NOT NULL,
      charset text   NOT NULL,
  wikidata_id text   UNIQUE,
   CONSTRAINT language_pk PRIMARY KEY (id)
);

-- MEDIA ---------------------------------------------------------------------------------------------------------------
CREATE TABLE melophobia.media (
           id serial NOT NULL,
         name text   UNIQUE NOT NULL,
         type text   NOT NULL,
  wikidata_id text   UNIQUE,
   CONSTRAINT media_pk PRIMARY KEY (id)
);

-- PRODUCER ------------------------------------------------------------------------------------------------------------
CREATE TABLE melophobia.producer (
                id serial   NOT NULL,
              name text     NOT NULL,
        birth_date char(10),
        birth_area text,
  birth_country_id int      NOT NULL,
        death_date char(10),
        death_area text,
  death_country_id int,
         favourite boolean  DEFAULT FALSE NOT NULL,
              isni char(19) UNIQUE,
       wikidata_id text     UNIQUE,
        CONSTRAINT producer_pk PRIMARY KEY (id)
);

-- PRODUCER_IPIS -------------------------------------------------------------------------------------------------------
CREATE TABLE melophobia.producer_ipis (
  producer_id int  NOT NULL,
       ipi_id text UNIQUE NOT NULL,
   CONSTRAINT producer_ipis_pk PRIMARY KEY (producer_id, ipi_id)
);

-- RELEASE -------------------------------------------------------------------------------------------------------------
CREATE TABLE melophobia.release (
                 id serial   NOT NULL,
              title text     NOT NULL,
       release_date char(10) NOT NULL,
       total_tracks smallint DEFAULT 0 NOT NULL,
     missing_tracks smallint DEFAULT 0 NOT NULL,
        total_discs smallint DEFAULT 0 NOT NULL,
      missing_discs smallint DEFAULT 0 NOT NULL,
          favourite boolean  DEFAULT FALSE NOT NULL,
         rym_rating numeric,
          aoty_rank smallint,
           bea_rank smallint,
   christgau_rating text,
        hull_rating text,
    scaruffi_rating numeric,
         metacritic smallint,
   pitchfork_rating numeric,
        art_quality smallint DEFAULT 0 NOT NULL,
        tag_quality smallint DEFAULT 0 NOT NULL,
            bitrate text     DEFAULT 0 NOT NULL,
               asin char(10) UNIQUE,
        wikidata_id text     UNIQUE,
  release_status_id int      NOT NULL,
      log_status_id int      NOT NULL,
        description text,
         CONSTRAINT release_pk PRIMARY KEY (id)
);

-- RELEASE_ARTISTS -----------------------------------------------------------------------------------------------------
CREATE TABLE melophobia.release_artists (
  release_id int NOT NULL,
   artist_id int NOT NULL,
  CONSTRAINT release_artists_pk PRIMARY KEY (release_id, artist_id)
);

-- RELEASE_GENRES ------------------------------------------------------------------------------------------------------
CREATE TABLE melophobia.release_genres (
  release_id int NOT NULL,
    genre_id int NOT NULL,
  CONSTRAINT release_genres_pk PRIMARY KEY (release_id, genre_id)
);

-- RELEASE_LANGUAGES ---------------------------------------------------------------------------------------------------
CREATE TABLE melophobia.release_languages (
   release_id int NOT NULL,
  language_id int NOT NULL,
   CONSTRAINT release_languages_pk PRIMARY KEY (release_id, language_id)
);

-- RELEASE_PRODUCERS ---------------------------------------------------------------------------------------------------
CREATE TABLE melophobia.release_producers (
   release_id int NOT NULL,
  producer_id int NOT NULL,
   CONSTRAINT release_producers_pk PRIMARY KEY (release_id, producer_id)
);

-- RELEASE_STATUS ------------------------------------------------------------------------------------------------------
CREATE TABLE melophobia.release_status (
          id serial NOT NULL,
        name text   UNIQUE NOT NULL,
  CONSTRAINT release_status_pk PRIMARY KEY (id)
);

-- RELEASE_TYPE --------------------------------------------------------------------------------------------------------
CREATE TABLE melophobia.release_type (
          id serial NOT NULL,
        name text   UNIQUE NOT NULL,
  CONSTRAINT release_type_pk PRIMARY KEY (id)
);

-- RELEASE_TYPES -------------------------------------------------------------------------------------------------------
CREATE TABLE melophobia.release_types (
       release_id int NOT NULL,
  release_type_id int NOT NULL,
       CONSTRAINT release_types_pk PRIMARY KEY (release_id, release_type_id)
);

-- STATUS --------------------------------------------------------------------------------------------------------------
CREATE TABLE melophobia.status (
          id serial  NOT NULL,
        name text    UNIQUE NOT NULL,
      colour char(7) UNIQUE NOT NULL,
  CONSTRAINT status_pk PRIMARY KEY (id)
);

-- TRACK ---------------------------------------------------------------------------------------------------------------
CREATE TABLE melophobia.track (
                  id serial  NOT NULL,
               title text    NOT NULL,
       track_type_id int     NOT NULL,
           artist_id int     NOT NULL,
  original_artist_id int,
           favourite boolean DEFAULT FALSE NOT NULL,
         wikidata_id text    UNIQUE,
          CONSTRAINT track_pk PRIMARY KEY (id)
);

-- TRACK_ISRC ----------------------------------------------------------------------------------------------------------
CREATE TABLE melophobia.track_isrc (
    track_id int      NOT NULL,
        isrc char(15) UNIQUE NOT NULL,
  CONSTRAINT track_isrc_pk PRIMARY KEY (track_id, isrc)
);

-- TRACK_ISWC ----------------------------------------------------------------------------------------------------------
CREATE TABLE melophobia.track_iswc (
    track_id int      NOT NULL,
        iswc char(15) UNIQUE NOT NULL,
  CONSTRAINT track_iswc_pk PRIMARY KEY (track_id, iswc)
);

-- TRACK_TYPE ----------------------------------------------------------------------------------------------------------
CREATE TABLE melophobia.track_type (
          id serial NOT NULL,
        name text   UNIQUE NOT NULL,
  CONSTRAINT track_type_pk PRIMARY KEY (id)
);

-- =====================================================================================================================
--   OWNERSHIP
-- =====================================================================================================================
ALTER TABLE melophobia.artist OWNER TO postgres;
ALTER TABLE melophobia.artist_genres OWNER TO postgres;
ALTER TABLE melophobia.artist_ipis OWNER TO postgres;
ALTER TABLE melophobia.artist_type OWNER TO postgres;
ALTER TABLE melophobia.catalogue_items OWNER TO postgres;
ALTER TABLE melophobia.catalogue_media OWNER TO postgres;
ALTER TABLE melophobia.country OWNER TO postgres;
ALTER TABLE melophobia.genre OWNER TO postgres;
ALTER TABLE melophobia.ipi OWNER TO postgres;
ALTER TABLE melophobia.label OWNER TO postgres;
ALTER TABLE melophobia.label_ipis OWNER TO postgres;
ALTER TABLE melophobia.language OWNER TO postgres;
ALTER TABLE melophobia.media OWNER TO postgres;
ALTER TABLE melophobia.producer OWNER TO postgres;
ALTER TABLE melophobia.producer_ipis OWNER TO postgres;
ALTER TABLE melophobia.release OWNER TO postgres;
ALTER TABLE melophobia.release_artists OWNER TO postgres;
ALTER TABLE melophobia.release_genres OWNER TO postgres;
ALTER TABLE melophobia.release_languages OWNER TO postgres;
ALTER TABLE melophobia.release_producers OWNER TO postgres;
ALTER TABLE melophobia.release_status OWNER TO postgres;
ALTER TABLE melophobia.release_type OWNER TO postgres;
ALTER TABLE melophobia.release_types OWNER TO postgres;
ALTER TABLE melophobia.status OWNER TO postgres;
ALTER TABLE melophobia.track OWNER TO postgres;
ALTER TABLE melophobia.track_isrc OWNER TO postgres;
ALTER TABLE melophobia.track_iswc OWNER TO postgres;
ALTER TABLE melophobia.track_type OWNER TO postgres;

-- =====================================================================================================================
--   CONSTRAINTS
-- =====================================================================================================================
ALTER TABLE ONLY melophobia.artist
  ADD CONSTRAINT artist_formation_country_fk
     FOREIGN KEY (formation_country_id) REFERENCES melophobia.country(id);

ALTER TABLE ONLY melophobia.artist
  ADD CONSTRAINT artist_disband_country_fk
     FOREIGN KEY (disband_country_id) REFERENCES melophobia.country(id);

ALTER TABLE ONLY melophobia.artist
  ADD CONSTRAINT artist_type_fk
     FOREIGN KEY (artist_type_id) REFERENCES melophobia.artist_type(id);

ALTER TABLE ONLY melophobia.artist_genres
  ADD CONSTRAINT artist_fk
     FOREIGN KEY (artist_id) REFERENCES melophobia.artist(id);

ALTER TABLE ONLY melophobia.artist_genres
  ADD CONSTRAINT genre_fk
     FOREIGN KEY (genre_id) REFERENCES melophobia.genre(id);

ALTER TABLE ONLY melophobia.artist_ipis
  ADD CONSTRAINT artist_fk
     FOREIGN KEY (artist_id) REFERENCES melophobia.artist(id);

ALTER TABLE ONLY melophobia.artist_ipis
  ADD CONSTRAINT ipi_fk
     FOREIGN KEY (ipi_id) REFERENCES melophobia.ipi(ipi_id);

ALTER TABLE ONLY melophobia.catalogue_items
  ADD CONSTRAINT label_fk
     FOREIGN KEY (label_id) REFERENCES melophobia.label(id);

ALTER TABLE ONLY melophobia.catalogue_items
  ADD CONSTRAINT release_fk
     FOREIGN KEY (release_id) REFERENCES melophobia.release(id);

ALTER TABLE ONLY melophobia.catalogue_items
  ADD CONSTRAINT release_status_fk
     FOREIGN KEY (release_status_id) REFERENCES melophobia.release_status(id);

ALTER TABLE ONLY melophobia.catalogue_media
  ADD CONSTRAINT catalogue_fk
     FOREIGN KEY (global_catalogue_id) REFERENCES melophobia.catalogue_items(id);

ALTER TABLE ONLY melophobia.catalogue_media
  ADD CONSTRAINT media_fk
     FOREIGN KEY (media_id) REFERENCES melophobia.media(id);

ALTER TABLE ONLY melophobia.genre
  ADD CONSTRAINT genre_fk
     FOREIGN KEY (parent_genre) REFERENCES melophobia.genre(id);

ALTER TABLE ONLY melophobia.label
  ADD CONSTRAINT formation_country_fk
     FOREIGN KEY (formation_country_id) REFERENCES melophobia.country(id);

ALTER TABLE ONLY melophobia.label_ipis
  ADD CONSTRAINT label_fk
     FOREIGN KEY (label_id) REFERENCES melophobia.label(id);

ALTER TABLE ONLY melophobia.label_ipis
  ADD CONSTRAINT ipi_fk
     FOREIGN KEY (ipi_id) REFERENCES melophobia.ipi(ipi_id);

ALTER TABLE ONLY melophobia.producer
  ADD CONSTRAINT birth_country_fk
     FOREIGN KEY (birth_country_id) REFERENCES melophobia.country(id);

ALTER TABLE ONLY melophobia.producer
  ADD CONSTRAINT death_country_fk
     FOREIGN KEY (death_country_id) REFERENCES melophobia.country(id);

ALTER TABLE ONLY melophobia.producer_ipis
  ADD CONSTRAINT producer_fk
     FOREIGN KEY (producer_id) REFERENCES melophobia.producer(id);

ALTER TABLE ONLY melophobia.producer_ipis
  ADD CONSTRAINT ipi_fk
     FOREIGN KEY (ipi_id) REFERENCES melophobia.ipi(ipi_id);

ALTER TABLE ONLY melophobia.release
  ADD CONSTRAINT release_status_fk
     FOREIGN KEY (release_status_id) REFERENCES melophobia.release_status(id);

ALTER TABLE ONLY melophobia.release
  ADD CONSTRAINT status_fk
     FOREIGN KEY (log_status_id) REFERENCES melophobia.status(id);

ALTER TABLE ONLY melophobia.release_artists
  ADD CONSTRAINT release_fk
     FOREIGN KEY (release_id) REFERENCES melophobia.release(id);

ALTER TABLE ONLY melophobia.release_artists
  ADD CONSTRAINT artist_fk
     FOREIGN KEY (artist_id) REFERENCES melophobia.artist(id);

ALTER TABLE ONLY melophobia.release_genres
  ADD CONSTRAINT release_fk
     FOREIGN KEY (release_id) REFERENCES melophobia.release(id);

ALTER TABLE ONLY melophobia.release_genres
  ADD CONSTRAINT genre_fk
     FOREIGN KEY (genre_id) REFERENCES melophobia.genre(id);

ALTER TABLE ONLY melophobia.release_languages
  ADD CONSTRAINT release_fk
     FOREIGN KEY (release_id) REFERENCES melophobia.release(id);

ALTER TABLE ONLY melophobia.release_languages
  ADD CONSTRAINT language_fk
     FOREIGN KEY (language_id) REFERENCES melophobia.language(id);

ALTER TABLE ONLY melophobia.release_producers
  ADD CONSTRAINT release_fk
     FOREIGN KEY (release_id) REFERENCES melophobia.release(id);

ALTER TABLE ONLY melophobia.release_producers
  ADD CONSTRAINT producer_fk
     FOREIGN KEY (producer_id) REFERENCES melophobia.producer(id);

ALTER TABLE ONLY melophobia.release_types
  ADD CONSTRAINT release_fk
     FOREIGN KEY (release_id) REFERENCES melophobia.release(id);

ALTER TABLE ONLY melophobia.release_types
  ADD CONSTRAINT release_type_fk
     FOREIGN KEY (release_type_id) REFERENCES melophobia.release_type(id);

ALTER TABLE ONLY melophobia.track
  ADD CONSTRAINT track_type_fk
     FOREIGN KEY (track_type_id) REFERENCES melophobia.track_type(id);

ALTER TABLE ONLY melophobia.track
  ADD CONSTRAINT artist_fk
     FOREIGN KEY (artist_id) REFERENCES melophobia.artist(id);

ALTER TABLE ONLY melophobia.track
  ADD CONSTRAINT original_artist_fk
     FOREIGN KEY (original_artist_id) REFERENCES melophobia.artist(id);

ALTER TABLE ONLY melophobia.track_isrc
  ADD CONSTRAINT track_fk
     FOREIGN KEY (track_id) REFERENCES melophobia.track(id);

ALTER TABLE ONLY melophobia.track_iswc
  ADD CONSTRAINT track_fk
     FOREIGN KEY (track_id) REFERENCES melophobia.track(id);
