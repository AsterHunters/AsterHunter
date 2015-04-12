<?php
defined('BASEPATH') OR exit('No direct script access allowed');
 
 /* Author: AsterHunting
 * Description: User controller class
 */
 
class Survey extends CI_Controller{
    
    function __construct(){
            
        parent::__construct();
        
        $this->load->helper('url');
        
        $this->load->model('database_model');
    }

    /**
    * Mostra la pagina iniziale delle rilevazioni
    * 
    * @access public
    * @param
    * @return 
    */
    public function index(){
        $this->load->view('survey_view');
    }
    
    /**
    * Mostra la pagina dettaglio delle rilevazioni
    * 
    * @access public
    * @param
    * @return 
    */
    public function detail($id){
        
        switch ($id) {
            case '1':
                $this->load->view('survey_detail1_view');
                break;
            case '2':
                $this->load->view('survey_detail2_view');
                break;
            default:
                $this->load->view('survey_detail1_view');
                break;
        }
    }
    
    /**
    * Inserisce una rilevazione sul database
    * Ritorna il risultato dell'inserimento sul database
    * 
    * @access public
    * @param json string
    * @return boolean
    */
    public function addSurvey(){
        
        $idUtente   = $this->input->post('id');
        $success    = $this->input->post('success');
        $images     = $this->input->post('images');
        $datetime   = $this->input->post('datetime');
        $coord      = $this->input->post('coord');
        
        log_error("error", "Images: ".$images);
                
        //$result = $this->database_model->addSuvery($idUtente, $datetime, $ascension, $declension, $images);
    }
}

/* End of file user.php */
/* Location: ./application/controllers/survey.php */