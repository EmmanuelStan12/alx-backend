import { createClient, print } from 'redis';

const client = createClient();

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.toString()}`);
});

const setHash = (hashName, field, value) => {
  client.HSET(hashName, field, value, print);
}

const printHash = (hashName) => {
  client.HGETALL(hashName, (_err, reply) => console.log(reply));
}

function main() {
  const data = {
    Portland: 50,
    Seattle: 80,
    'New York': 20,
    Bogota: 20,
    Cali: 40,
    Paris: 2,
  };

  for (const [field, value] of Object.entries(data)) {
    setHash('HolbertonSchools', field, value);
  }
  printHash('HolbertonSchools');
}

client.on('connect', () => {
  console.log('Redis client connected to the server');
  main();
});
