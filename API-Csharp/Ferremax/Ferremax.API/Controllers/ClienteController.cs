using Microsoft.AspNetCore.Mvc;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Ferremax.API.Models;

// For more information on enabling Web API for empty projects, visit https://go.microsoft.com/fwlink/?LinkID=397860

namespace Ferremax.API.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class ClienteController : ControllerBase
    {
        private static IList<Cliente> lista = new List<Cliente>();

        [HttpGet]
        public IEnumerable<Cliente> Get()
        {
            return lista;
        }

        [HttpGet("{id}")]
        public ActionResult<Cliente> Get(int id)
        {
            var cliente = lista.FirstOrDefault(x => x.id == id);
        }

        [HttpPost]
        public ActionResult Post([FromBody] Cliente value)
        {
            lista.Add(value);
        }

        [HttpPut("{id}")]
        public ActionResult Put(int id, [FromBody] Cliente value)
        {
            var cliente = lista.FirstOrDefault(x => x.id == id);
            if (cliente == null)
        }

        [HttpDelete("{id}")]
        public ActionResult Delete(int id)
        {
            var cliente = lista.FirstOrDefault(x => x.id == id);
        }
    }
}