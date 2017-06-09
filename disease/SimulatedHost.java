import java.util.*;

public class SimulatedHost {
    
    public static void main(String[] args) {
        DiseaseBlueprint dd = new DeltaDisease();
        SimulatedHost host = new SimulatedHost(AgeGroup.ADULT);
        List<String> events = host.infect(dd);
        System.out.println("Patient infection log for " + host + ":");
        for(String res : events){
            System.out.println(res);
        }
        List<Integer[]> data = host.getDiseaseData();
        int day = 1;
        System.out.println("Day\tEnergy\tBacteria");
        for(Integer[] vals : data){
            System.out.println(day + "\t" + vals[0] + "\t" + vals[1]);
            day++;
        }
    }
    
    private AgeGroup ageGroup;
    private List<String> diseaseEvents;
    private List<Integer[]> diseaseData;
    
    SimulatedHost(AgeGroup ageGroup) {
        this.ageGroup = ageGroup;
        this.diseaseEvents = new ArrayList<String>();
        this.diseaseData = new ArrayList<Integer[]>();
    }
    
    private int energy;
    private int INITIAL_ENERGY = 100;
    private int MIN_ENERGY = 0;
    private int TOXIN_COST = 60;
    private int DAY_COST = 10;
    
    private int bacteria;
    private int INITIAL_BACTERIA = 0;
    private int BACTERIA_GROWTH = 10;
    private int ENERGY_PER_BACTERIA = 5;
    private int INCUBATION_TRESHOLD = 50;
    private int LATENT_THRESHOLD = 30;
    
    public boolean isIncubated() {
        return bacteria > INCUBATION_TRESHOLD;
    }
    
    public boolean isLatent() {
        return bacteria > LATENT_THRESHOLD;
    }
    
    public List<String> infect(DiseaseBlueprint disease) {
        int day = 1;
        bacteria = INITIAL_BACTERIA;
        energy = INITIAL_ENERGY;
        Integer[] initialData = {energy, bacteria};
        diseaseData.add(initialData);
        while(energy > MIN_ENERGY){
            energy -= DAY_COST;
            DiseaseAction action = disease.move(this, energy);
            switch(action){
                case MULTIPLY:
                    bacteria += BACTERIA_GROWTH;
                    energy += (ENERGY_PER_BACTERIA * bacteria);
                    diseaseEvents.add("Day " + day + ":\tInfection multiplied.");
                    break;
                case RELEASE:
                    if(isIncubated()){
                        energy -= TOXIN_COST;
                        if(energy > MIN_ENERGY){
                            diseaseEvents.add("Day " + day + ":\tToxin released.");
                        }
                        else{
                            diseaseEvents.add("Day " + day + ":\tFailed to release toxin.");
                        }   
                    }
                    else{
                        diseaseEvents.add("Day " + day + ":\tFailed to release toxin.");
                    }
                    break;
                case EXIT:
                    if(isLatent()){
                        diseaseEvents.add("Day " + day + ":\tInfection exited the host.");
                    }
                    else{
                        diseaseEvents.add("Day " + day + ":\tFailed to exit host.");
                    }
                    break;
                default:
                    diseaseEvents.add("Day " + day + ":\tNo activity.");
                    break;
            }
            Integer[] data = {energy, bacteria};
            diseaseData.add(data);
            day++;
        }
        diseaseEvents.add("Day " + day + ":\tInfection died out.");
        return this.diseaseEvents;
    }
    
    public List<String> getDiseaseEvents() {
        return this.diseaseEvents;
    }
    
    public List<Integer[]> getDiseaseData() {
        return this.diseaseData;
    }
    
    @Override
    public String toString() {
        switch(ageGroup){
            case CHILD: return "a child host";
            case TEEN: return "a teenage host";
            case ADULT: return "an adult host";
            case ELDER: return "an elderly host";
            default: return "a simulated host";
        }
    }
    
}