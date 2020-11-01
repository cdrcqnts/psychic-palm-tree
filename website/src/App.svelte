<script>
  export let name;

  let myIP = 0;
  let apiRes = {};

  async function getIP() {
    await fetch("http://ip.jsontest.com/")
      .then((res) => res.json())
      .then((data) => {
        console.log(data);
        myIP = data.ip;
      });
  }

  async function getGreeting() {
    await fetch("http://api:8000")
      .then((res) => res.json())
      .then((data) => {
        console.log(data);
		apiRes = data;
	  });

  }
</script>

<style>
  main {
    text-align: center;
    padding: 1em;
    max-width: 240px;
    margin: 0 auto;
  }

  h1 {
    color: #ff3e00;
    text-transform: uppercase;
    font-size: 4em;
    font-weight: 100;
  }

  @media (min-width: 640px) {
    main {
      max-width: none;
    }
  }
</style>

<svelte:head>
  <!-- Milligram CSS -->
  <link
    rel="stylesheet"
    href="https://cdnjs.cloudflare.com/ajax/libs/milligram/1.4.1/milligram.css" />
</svelte:head>

<main>
  <h1>Hola {name}!</h1>
  <button on:click|once={getIP}> Get my IP </button>
  <button on:click|once={getGreeting}>Get greeting</button>
  <blockquote>
    <p><em>My IP is: {myIP}</em></p>
  </blockquote>
  <blockquote>
    <p><em>{apiRes}</em></p>
  </blockquote>
</main>
