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
    public class retiroController : ControllerBase
    {

        private static IList<retiro> lista = new List<retiro>();

        // GET: api/<retiroController>
        [HttpGet]
        public IEnumerable<retiro> Get()
        {
            return lista;
        }

        // GET api/<retiroController>/5
        [HttpGet("{id}")]
        public retiro Get(int id)
        {
            return lista.FirstOrDefault(x => x.id == id);
        }

        // POST api/<retiroController>
        [HttpPost]
        public void Post([FromBody] retiro value)
        {
            lista.Add(value);
        }

        // PUT api/<retiroController>/5
        [HttpPut("{id}")]
        public void Put(int id, [FromBody] retiro value)
        {
            retiro selection = lista.FirstOrDefault(x => x.id == id);
            lista[lista.IndexOf(selection)] = value;
        }

        // DELETE api/<retiroController>/5
        [HttpDelete("{id}")]
        public void Delete(int id)
        {
            lista.Remove(lista.FirstOrDefault(x => x.id == id));
        }
    }
}