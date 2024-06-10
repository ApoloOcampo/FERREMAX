using Microsoft.AspNetCore.Mvc;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using logistica.API.Models;

// For more information on enabling Web API for empty projects, visit https://go.microsoft.com/fwlink/?LinkID=397860

namespace logistica.API.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class envioController : ControllerBase
    {

        private static IList<envio> lista = new List<envio>();

        // GET: api/<envioController>
        [HttpGet]
        public IEnumerable<envio> Get()
        {
            return lista;
        }

        // GET api/<envioController>/5
        [HttpGet("{id}")]
        public envio Get(int id)
        {
            return lista.FirstOrDefault(x => x.id == id);
        }

        // POST api/<envioController>
        [HttpPost]
        public void Post([FromBody] envio value)
        {
            lista.Add(value);
        }

        // PUT api/<envioController>/5
        [HttpPut("{id}")]
        public void Put(int id, [FromBody] envio value)
        {
            envio selection = lista.FirstOrDefault(x => x.id == id);
            lista[lista.IndexOf(selection)] = value;
        }

        // DELETE api/<envioController>/5
        [HttpDelete("{id}")]
        public void Delete(int id)
        {
            lista.Remove(lista.FirstOrDefault(x => x.id == id));
        }
    }
}