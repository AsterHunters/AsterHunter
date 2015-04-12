<?php defined('BASEPATH') OR exit('No direct script access allowed'); ?>
<!DOCTYPE html>
<html lang="en">

<head>

    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="">

    <title>Portfolio Item - Start Bootstrap Template</title>

    <!-- Bootstrap Core CSS -->
    <link href="http://192.168.1.202:1080/assets/css/bootstrap.css" rel="stylesheet">

    <!-- Custom CSS -->
    <link href="http://192.168.1.202:1080/assets/css/portfolio-item.css" rel="stylesheet">

    <!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    <!--[if lt IE 9]>
        <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
        <script src="https://oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js"></script>
    <![endif]-->

</head>

<body>

    <!-- Navigation -->
    <nav class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
            <!-- Brand and toggle get grouped for better mobile display -->
            <div class="navbar-header">
                <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">
                    <span class="sr-only"> <?php base_url() ?></span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                </button>
                <a class="navbar-brand" href="#">Aster Hunters</a>
            </div>
        </div>
        <!-- /.container -->
    </nav>

    <!-- Page Content -->
    <div class="container">

        <!-- Portfolio Item Heading -->
        <div class="row">
            <div class="col-lg-12">
                <h1 class="page-header">Portfolio Item
                    <small>Item Subheading</small>
                </h1>
            </div>
        </div>
        <!-- /.row -->

        <!-- Portfolio Item Row -->
        <div class="row">

            <div class="col-md-8">
                <img class="img-responsive" src="http://192.168.1.202:1080/assets/img/image_2.gif" alt="">
            </div>

            <div class="col-md-4">
                <h3>Project Description</h3>
                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam viverra euismod odio, gravida pellentesque urna varius vitae. Sed dui lorem, adipiscing in adipiscing et, interdum nec metus. Mauris ultricies, justo eu convallis placerat, felis enim.</p>
                <h3>Project Details</h3>
                <ul>
                    <li>Lorem Ipsum</li>
                    <li>Dolor Sit Amet</li>
                    <li>Consectetur</li>
                    <li>Adipiscing Elit</li>
                </ul>
                
                <button type="button" class="btn btn-success">Join</button>
            </div>

        </div>
        <!-- /.row -->
        
                <div class="row">
            <div class="col-lg-12">
                <h1 class="page-header">Observation</h1>
            </div>
            <table width="100%" class="table table-striped">
                <tr>
                    <td><b>Data</b></td>
                    <td><b>RA</b></td>
                    <td><b>Dec</b></td>
                    <td><b>Mag</b></td>
                    <td><b>Observer</b></td>
                </tr>
                <tr>
                    <td>2015/04/03.118</td>
                    <td>15h 32m 12.226s</td>
                    <td>+44° 25' 20.225"</td>
                    <td>+17.2</td>
                    <td>Nebula</td>
                </tr>
                <tr>
                    <td>2015/04/03.118</td>
                    <td>11h 22m 11.226s</td>
                    <td>+22° 15' 20.225"</td>
                    <td>+17.2</td>
                    <td>Nebula</td>
                </tr>
                <tr>
                    <td>2015/04/03.118</td>
                    <td>16h11m 9.226s</td>
                    <td>+46° 15' 20.215"</td>
                    <td>+17.2</td>
                    <td>Nebula</td>
                </tr>
            </table>
        </div>

        <!-- Related Projects Row -->
        <div class="row">

            <div class="col-lg-12">
                <h3 class="page-header">Related Projects</h3>
            </div>

            <div class="col-sm-3 col-xs-6">
                <a href="#">
                    <img class="img-responsive portfolio-item" src="http://192.168.1.202:1080/assets/img/image_1.png" alt="">
                </a>
            </div>

            <div class="col-sm-3 col-xs-6">
                <a href="#">
                    <img class="img-responsive portfolio-item" src="http://192.168.1.202:1080/assets/img/image_2.png" alt="">
                </a>
            </div>

            <div class="col-sm-3 col-xs-6">
                <a href="#">
                    <img class="img-responsive portfolio-item" src="http://192.168.1.202:1080/assets/img/image_3.png" alt="">
                </a>
            </div>

            <div class="col-sm-3 col-xs-6">
                <a href="#">
                    <img class="img-responsive portfolio-item" src="http://192.168.1.202:1080/assets/img/image_4.png" alt="">
                </a>
            </div>

        </div>
        <!-- /.row -->

        <hr>

        <!-- Footer -->
        <footer>
            <div class="row">
                <div class="col-lg-12">
                    <p>Copyright &copy; SpaceApps 2015</p>
                </div>
            </div>
            <!-- /.row -->
        </footer>

    </div>
    <!-- /.container -->

    <!-- jQuery -->
    <script src="http://192.168.1.202:1080/assets/js/jquery.js"></script>

    <!-- Bootstrap Core JavaScript -->
    <script src="http://192.168.1.202:1080/assets/js/bootstrap.min.js"></script>

</body>

</html>
