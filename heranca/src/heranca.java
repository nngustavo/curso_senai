class Animal {

    void fazerSom(){
        System.out.println("Fazendo som genérico");
    }
}

class Cachorro extends Animal {
    @Override
    void fazerSom(){
        System.out.println("Au Au");
    }
}



public class heranca {
    public static void main(String[] args) throws Exception {

        //cria a instância cachorro
        Cachorro meuCachorro = new Cachorro();
        meuCachorro.fazerSom();
    }
}
