namespace logistica.API.Models
{
    public class envio
    {
        public int id { get; set; }
        public string cliente { get; set; }
        public string direccion { get; set; }
        public string producto { get; set; }
        public int cantidad { get; set; }
        public int valorProducto { get; set; }
        public int valorDespacho { get; set; }
        public int totalPagar { get; set; }
        public string fecha { get; set; }
        public bool estado { get; set; }
    }
}
