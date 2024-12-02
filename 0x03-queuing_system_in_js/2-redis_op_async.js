import { createClient, print } from 'redis';
import { promisify } from 'util';

const client = createClient()

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.toString()}`);
});

function setNewSchool(schoolName, value) {
  client.SET(schoolName, value, print);
}

async function displaySchoolValue(schoolName) {
  const result = await promisify(client.GET).bind(client)(schoolName);
  console.log(result);
}

async function main() {
  displaySchoolValue('Holberton');
  setNewSchool('HolbertonSanFrancisco', '100');
  displaySchoolValue('HolbertonSanFrancisco');
}

client.on('connect', async () => {
  console.log('Redis client connected to the server');
  await main();
});
