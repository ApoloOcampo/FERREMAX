namespace Ferremax.API.Models
{
    public class Cliente
    {
        public int id { get; set; }
        public string razonSocial { get; set; }
        public string rut { get; set; }
        public string direccion { get; set; }
        public string telefono { get; set; }
        public string email { get; set; }
        public bool activo { get; set; }
    }
}
