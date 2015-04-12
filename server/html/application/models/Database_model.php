<?php
defined('BASEPATH') OR exit('No direct script access allowed');
 
 /* Author: AsterHunting
 * Description: User controller class
 */
 
class Database_model extends CI_Model{
    
    function __construct(){
            
        parent::__construct();
        $this->load->database();
    }
    
    /* USER */
    
    /**
    * Resituisce l'id utente se l'utente è registrato altrimenti ritorna 0
    *
    * @access public
    * @param username, password
    * @return string
    */
    public function validateUser($username, $password){
        
        $this->db->select('id_user');
        $this->db->where('email', $username);
        $this->db->where('password', md5($password));
        
        $query = $this->db->get('user');
        
        if ($query->num_rows() > 0){
            $row   = $query->row();
            return $row->id_user;
        }
        
        return "0";
        
    }
    
    /* SURVEY */
        /**
    * Resituisce l'id utente se l'utente è registrato altrimenti ritorna 0
    *
    * @access public
    * @param username, password
    * @return string
    */
    public function addSuvery($idUtente, $datetime, $ascension, $declension, $images){
        
        //start transaction
        /*$this->db->trans_start();
        
        $data = array(
            'datetime'      => $datetime,
            'ascension'     => $ascension,
            'declension'    => $declension,
            'user_id_user'  => $idUtente
        );
        
        $this->db->insert('survey',$data);
        
        if ($this->db->_error_message())
            return FALSE;
        else
            return TRUE;
        
        for ($i=0; $i < $images; $i++) { 
            
        }
        
        $idSurvey = $this->db->insert_id();

        //complete transaction
        $this->db->trans_complete();
        
        return $this->db->trans_status();*/        
    }
}

/* End of file user.php */
/* Location: ./application/controllers/user.php */
