namespace Ferremax.API.Models
{
    public class Producto
    {
        public int id { get; set; }
        public string nombre { get; set; }
        public string categoria { get; set; }
        public int precio { get; set; }
        public bool enStock { get; set; }
    }
}
