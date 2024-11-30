from .constants import * 
from django.db import models 

class UserChoices(models.TextChoices):
    ADMIN              = ADMIN,ADMIN
    CUSTOMER           = CUSTOMER ,CUSTOMER 
    DELIVERY_MAN       = DELIVERY_MAN,DELIVERY_MAN
    STORE_ADMIN        = STORE_ADMIN,STORE_ADMIN 

class PriceChoices(models.TextChoices):
    BEGINNER         = BEGINNER,BEGINNER
    INTERMEDIATE     = INTERMEDIATE,INTERMEDIATE
    PRO              = PRO,PRO


class OrderChoices(models.TextChoices):
    PENDING          = PENDING,PENDING
    CONFIRMED        = CONFIRMED,CONFIRMED
    PREPARING        = PREPARING,PREPARING
    OUT_FOR_DELIVERY = OUT_FOR_DELIVERY,OUT_FOR_DELIVERY
    DELIVERED        = DELIVERED,DELIVERED
    CANCELLED        = CANCELLED,CANCELLED
    
class PaymentStatusChoices(models.TextChoices):
    PAID            = PAID,PAID
    UNPAID          = UNPAID,UNPAID
    FAILED          = FAILED,FAILED
    REFUNDED        = REFUNDED,REFUNDED
    
    
class BookingChoices(models.TextChoices):
    PENDING          = PENDING,PENDING
    APPROVED         = APPROVED,APPROVED
    ASSIGNED         = ASSIGNED,ASSIGNED
    ONGOING          = ONGOING,ONGOING
    REFUNDED         = REFUNDED,REFUNDED
    COMPLETED        = COMPLETED,COMPLETED
    CANCELLED        = CANCELLED,CANCELLED
    REJECTED         = REJECTED,REJECTED
    FAILED           = FAILED,FAILED
    RESCHEDULED      = RESCHEDULED,RESCHEDULED

    # wordpress site is updated from here 
    # We can upload the docs here 
    # 
# <p>[vc_row section_back_opt="section-bg-dark-2" sec_text_color_opt="text-color-white" row_padding_bottom="no-padding-bottom"][vc_column width="1/2"][wr_vc_titles text_align="text-left" title_style="headline-m" title_color="text-color-white"][wr_vc_title title="We `{`span`}`Create`{`/span`}`" animation_delay="00"][wr_vc_title title="`{`span`}`Solutions`{`/span`}`" animation_delay="01"][/wr_vc_titles][/vc_column][vc_column width="1/2"][wr_vc_simple_title title="Our Belief" title_tag="h5" text_align="text-left" padding_bottom="padding-bottom-20"][umaya_text text_color="text-color-white" font_size="24px"]We firmly believe in the transformative power of dreams. That's why we collaborate with brands worldwide, from start-ups to multinational corporations. With our team of experts, we turn creative visions into tangible results, driving robust business growth for our clients.[/umaya_text][vc_empty_space height="100px"][wr_vc_simple_title title="About Connecting Dots" title_tag="h5" text_align="text-left" padding_bottom="padding-bottom-20"][umaya_text text_color="text-color-white"]<strong>As a Global IT Solutions Provider with bases in Canada and India, we're committed to realizing the potential of every dream.</strong></p>
# <p>From start-ups to multinational giants, we collaborate with clients worldwide to translate visions into reality.</p>
# <p>With our team of subject matter experts, we seamlessly integrate creative design with pragmatic solutions, driving robust brand growth and enduring success in the IT landscape.[/umaya_text][/vc_column][/vc_row][vc_row section_back_opt="section-bg-dark-1" sec_text_color_opt="text-color-white"][vc_column][vc_row_inner][vc_column_inner][wr_vc_titles text_align="text-left" title_color="text-color-white"][wr_vc_title title="`{`span`}`Fine Folks`{`/span`}`" animation_delay="00"][wr_vc_title title="We’ve Worked" animation_delay="01"][wr_vc_title title="With" animation_delay="03"][/wr_vc_titles][/vc_column_inner][/vc_row_inner][vc_row_inner][vc_column_inner][wr_vc_clients][wr_vc_client button_url="#" image="1109" image_hover="1110"][wr_vc_client button_url="#" image="1087" image_hover="1088"][wr_vc_client button_url="#" image="1091" image_hover="1092"][wr_vc_client button_url="#" image="1107" image_hover="1108"][wr_vc_client button_url="#" image="1111" image_hover="1112"][wr_vc_client button_url="#" image="1105" image_hover="1106"][wr_vc_client button_url="#" image="1097" image_hover="1098"][wr_vc_client button_url="#" image="1093" image_hover="1094"][wr_vc_client button_url="#" image="1103" image_hover="1104"][wr_vc_client button_url="#" image="1095" image_hover="1096"][wr_vc_client button_url="#" image="1367" image_hover="1368"][wr_vc_client button_url="#" image="1359" image_hover="1360"][wr_vc_client button_url="#" image="1369" image_hover="1370"][wr_vc_client button_url="#" image="1365" image_hover="1366"][wr_vc_client button_url="#" image="1321" image_hover="1323"][wr_vc_client button_url="#" image="1357" image_hover="1358"][wr_vc_client button_url="#" image="1374" image_hover="1375"][wr_vc_client button_url="#" image="1361" image_hover="1362"][wr_vc_client_blank data_title_1="This spot" data_title_2="awaits" data_title_3="You" button_url="#"][/wr_vc_clients][/vc_column_inner][/vc_row_inner][/vc_column][/vc_row][vc_row enable_container="st2" section_back_opt="section-bg-dark-2" sec_text_color_opt="text-color-white"][vc_column][vc_row_inner][vc_column_inner][wr_vc_titles2 title_style="headline-xl"][wr_vc_title2 ani_type_opt="st2" title="Client's"][wr_vc_title2 ani_type_opt="st2" title="Feedback" animation_delay="01"][/wr_vc_titles2][/vc_column_inner][/vc_row_inner][vc_row_inner][vc_column_inner][wr_vc_testimonials_4][wr_vc_testimonial_4 clientname="Prashant Kamble" designation="Showroom Manager,Parneeti Honda." image="178"]Working with Connecting Dots was an absolute game-changer for our business! Their expertise in digital marketing helped us increase our online visibility, reach new audiences, and boost our sales significantly. Their team is dedicated, creative, and always goes above and beyond to deliver results. Highly recommend their services![/wr_vc_testimonial_4][wr_vc_testimonial_4 clientname="Mary Ross" designation="Fashion designer" image="180"]Connecting Dots  has been instrumental in our online success. From developing a comprehensive digital marketing strategy to executing targeted campaigns, they have consistently exceeded our expectations. Their deep understanding of our industry and audience has helped us achieve remarkable growth. Thank you, Connecting Dots, for your exceptional work![/wr_vc_testimonial_4][wr_vc_testimonial_4 clientname="Lucille Hatcher" designation="Investor" image="177"]Choosing Connecting Dots  was one of the best decisions we made for our business. Their team is highly skilled and knowledgeable, and they genuinely care about our success. They took the time to understand our goals and tailored a digital marketing plan that aligns perfectly with our objectives. We've seen a significant increase in website traffic and leads since partnering with them. Couldn't be happier with the results.[/wr_vc_testimonial_4][wr_vc_testimonial_4 clientname="Dwight Bell" designation="Banquet manager" image="181"]Connecting Dots has been an invaluable partner for our digital marketing efforts. Their strategic approach, combined with their creativity and attention to detail, has helped us achieve remarkable growth in a highly competitive market. They are responsive, professional, and always proactive in suggesting new ideas to improve our online presence. Highly recommend their services to anyone looking to elevate their digital marketing game.[/wr_vc_testimonial_4][wr_vc_testimonial_4 clientname="Edward Jordan" designation="Cytotechnologist" image="182"]We've been working with Connecting Dots for over a year now, and we're extremely impressed with the results they've delivered. Their team is incredibly talented and dedicated, and they have a deep understanding of the ever-evolving digital landscape. They've helped us optimize our online campaigns, increase our brand visibility, and generate more leads. If you're looking for a digital marketing partner that truly cares about your success, look no further than Connecting Dots.[/wr_vc_testimonial_4][/wr_vc_testimonials_4][/vc_column_inner][/vc_row_inner][/vc_column][/vc_row][vc_row section_back_opt="section-bg-dark-1" sec_text_color_opt="text-color-white" row_padding_bottom="no-padding-bottom"][vc_column][umaya_popup_img_shortcode image_overlay="st2" image="200"][umaya_popup_video video_url="https://www.youtube.com/watch?v=WqB1LDuORTQ"][/vc_column][/vc_row]</p>














