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
    public class ProductoController : ControllerBase
    {
        private static IList<Producto> lista = new List<Producto>();

        [HttpGet]
        public IEnumerable<Producto> Get()
        {
            return lista;
        }

        [HttpGet("{id}")]
        public ActionResult<Producto> Get(int id)
        {
            var producto = lista.FirstOrDefault(x => x.id == id);
        }

        [HttpPost]
        public ActionResult Post([FromBody] Producto value)
        {
            lista.Add(value);
        }

        [HttpPut("{id}")]
        public ActionResult Put(int id, [FromBody] Producto value)
        {
            var producto = lista.FirstOrDefault(x => x.id == id);
            if (producto == null)
        }

        [HttpDelete("{id}")]
        public ActionResult Delete(int id)
        {
            var producto = lista.FirstOrDefault(x => x.id == id);
        }
    }
}