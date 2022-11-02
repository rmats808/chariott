// Copyright (c) Microsoft Corporation. All rights reserved.
// Licensed under the MIT license.
 
use anyhow::{Error};

use examples_common::chariott::{
    api::{Chariott,  GrpcChariott},   
    value::Value,
};

use tracing::{Level};
use tracing_subscriber::{util::SubscriberInitExt, EnvFilter};

// Namespaces
pub const KEY_VALUE_STORE_NAMESPACE: &str = "sdv.kvs";

#[tokio::main]
pub async fn main() -> Result<(), Error> {
    tracing_subscriber::fmt()
        .with_env_filter(
            EnvFilter::builder().with_default_directive(Level::INFO.into()).from_env_lossy(),
        )
        .finish()
        .init();

    // Connect to Chariott
    let mut chariott = setup().await;

    // Let's setup the Key and Value we want to write to the 
    // Key Value Store
    let hello_value: Value = "Hello ".into();
    let world_value: Value = "World!!".into();

    let first_test_key = get_uuid();
    let second_test_key = get_uuid();

    println!("first test key: {:?}", first_test_key);
    println!("second test key: {:?}", second_test_key);

    //Let's print out the value we wrote to the key store 
    println!("Here is first value that we are writing to the first test key: {:?}", 
    hello_value.clone()
    .into_string()
    .unwrap());
    
    println!("Here is the second value that we are writing to the second test key: {:?}", 
    world_value.clone()
    .into_string()
    .unwrap());

    // Let's now write the value to the specific key to KVS
    chariott.write(KEY_VALUE_STORE_NAMESPACE, first_test_key.clone(), hello_value.clone()).await?;
    chariott.write(KEY_VALUE_STORE_NAMESPACE, second_test_key.clone(), world_value.clone()).await?;

    // Read key from KVS
    let response = chariott.read(KEY_VALUE_STORE_NAMESPACE, first_test_key.clone()).await?;
    let _response2 = chariott.read(KEY_VALUE_STORE_NAMESPACE, second_test_key.clone()).await?;

    // Let's print out the Value we retrieved from the Key Value Store
    println!("Here is key/value pair retrieved from the Key Value Store: {:?}:{:?}", first_test_key.clone(), 
        response.clone()
            .unwrap()
            .as_str()
            .unwrap());
    println!("Here is key/value pair retrieved from the Key Value Store: {:?}:{:?}", second_test_key.clone(), 
        _response2.clone()
            .unwrap()
            .as_str()
            .unwrap());

    // assert
    assert_eq!(Some(hello_value), response);
    Ok(())

   
}

async fn setup() -> impl Chariott {
    // Use Chariott Grpc boilerplate code in api.rs to connect to Chariott
    GrpcChariott::connect().await.unwrap()
}


fn get_uuid() -> Box<str> {
    uuid::Uuid::new_v4().to_string().into()
}