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
    public class despachoController : ControllerBase
    {

        private static IList<despacho> lista = new List<despacho>();

        // GET: api/<despachoController>
        [HttpGet]
        public IEnumerable<despacho> Get()
        {
            return lista;
        }

        // GET api/<despachoController>/5
        [HttpGet("{id}")]
        public despacho Get(int id)
        {
            return lista.FirstOrDefault(x => x.id == id);
        }

        // POST api/<despachoController>
        [HttpPost]
        public void Post([FromBody] despacho value)
        {
            lista.Add(value);
        }

        // PUT api/<despachoController>/5
        [HttpPut("{id}")]
        public void Put(int id, [FromBody] despacho value)
        {
            despacho selection = lista.FirstOrDefault(x => x.id == id);
            lista[lista.IndexOf(selection)] = value;
        }

        // DELETE api/<despachoController>/5
        [HttpDelete("{id}")]
        public void Delete(int id)
        {
            lista.Remove(lista.FirstOrDefault(x => x.id == id));
        }
    }
}