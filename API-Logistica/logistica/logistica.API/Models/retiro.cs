namespace logistica.API.Models
{
    public class retiro
    {
        public int id { get; set; }
        public string cliente { get; set; }
        public string producto { get; set; }
        public int cantidad { get; set; }
        public int valorProducto { get; set; }
        public int totalPagar { get; set; }
        public string fecha { get; set; }
    }
}
