drop table if exists users;
create table users (
    id integer primary key autoincrement,
    name text not null,
    date text not null,
    registration_id text not null,
    public_key text not null
);

drop table if exists decrees;
create table decrees (
    id text primary key,
    text text not null,
    date text not null,
    creator integer not null
);

drop table if exists decree_signatures;
create table decree_signatures (
    signer integer not null,
    decree integer not null,
    signature text not null
);

drop table if exists demerits;
create table demerits (
    issuer integer not null,
    receiver integer not null,
    reason text not null,
    date text not null,
    issuer_signature text not null,
    receiver_signature text
);

