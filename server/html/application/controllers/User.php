<?php
defined('BASEPATH') OR exit('No direct script access allowed');
 
 /* Author: AsterHunting
 * Description: User controller class
 */
 
class User extends CI_Controller{
    
    function __construct(){
            
        parent::__construct();
        $this->load->model('database_model');
    }
    
    /**
    * Richiama il modello per verificare la validità di una registrazione
    *
    * @access public
    * @param username, password
    * @return string, id dell'utente
    */
    public function validate($username, $password){
        
        $result = $this->database_model->validateUser($username, $password);
        die($result);
    }
}

/* End of file user.php */
/* Location: ./application/controllers/user.php */