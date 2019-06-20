import builtins as _mod_builtins

__doc__ = None
__file__ = '/usr/lib/python3/dist-packages/cryptography/hazmat/bindings/_openssl.abi3.so'
__name__ = 'cryptography.hazmat.bindings._openssl'
__package__ = 'cryptography.hazmat.bindings'
ffi = _mod_builtins.CompiledFFI()
class lib(_mod_builtins.object):
    @staticmethod
    def ACCESS_DESCRIPTION_free():
        'void ACCESS_DESCRIPTION_free(ACCESS_DESCRIPTION *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ACCESS_DESCRIPTION_new():
        'ACCESS_DESCRIPTION *ACCESS_DESCRIPTION_new();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def AES_set_decrypt_key():
        'int AES_set_decrypt_key(unsigned char *, int, struct aes_key_st *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def AES_set_encrypt_key():
        'int AES_set_encrypt_key(unsigned char *, int, struct aes_key_st *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def AES_unwrap_key():
        'int AES_unwrap_key(struct aes_key_st *, unsigned char *, unsigned char *, unsigned char *, unsigned int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def AES_wrap_key():
        'int AES_wrap_key(struct aes_key_st *, unsigned char *, unsigned char *, unsigned char *, unsigned int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ASN1_BIT_STRING_free():
        'void ASN1_BIT_STRING_free(struct asn1_string_st *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ASN1_BIT_STRING_get_bit():
        'int ASN1_BIT_STRING_get_bit(struct asn1_string_st *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ASN1_BIT_STRING_new():
        'struct asn1_string_st *ASN1_BIT_STRING_new();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ASN1_BIT_STRING_set_bit():
        'int ASN1_BIT_STRING_set_bit(struct asn1_string_st *, int, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ASN1_ENUMERATED_free():
        'void ASN1_ENUMERATED_free(ASN1_ENUMERATED *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ASN1_ENUMERATED_get():
        'long ASN1_ENUMERATED_get(ASN1_ENUMERATED *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ASN1_ENUMERATED_new():
        'ASN1_ENUMERATED *ASN1_ENUMERATED_new();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ASN1_ENUMERATED_set():
        'int ASN1_ENUMERATED_set(ASN1_ENUMERATED *, long);\n\nCFFI C function from _openssl.lib'
        pass
    
    ASN1_F_ASN1_CHECK_TLEN = 104
    ASN1_F_ASN1_EX_C2I = 204
    ASN1_F_ASN1_FIND_END = 190
    ASN1_F_ASN1_GENERATE_V3 = 178
    ASN1_F_ASN1_GET_OBJECT = 114
    ASN1_F_ASN1_ITEM_I2D_FP = 193
    ASN1_F_ASN1_ITEM_PACK = 198
    ASN1_F_ASN1_ITEM_SIGN = 195
    ASN1_F_ASN1_ITEM_UNPACK = 199
    ASN1_F_ASN1_ITEM_VERIFY = 197
    ASN1_F_ASN1_MBSTRING_NCOPY = 122
    ASN1_F_ASN1_TEMPLATE_EX_D2I = 132
    ASN1_F_ASN1_TEMPLATE_NEW = 133
    ASN1_F_ASN1_TEMPLATE_NOEXP_D2I = 131
    ASN1_F_ASN1_TYPE_GET_INT_OCTETSTRING = 134
    ASN1_F_ASN1_TYPE_GET_OCTETSTRING = 135
    ASN1_F_ASN1_VERIFY = 137
    ASN1_F_B64_READ_ASN1 = 209
    ASN1_F_B64_WRITE_ASN1 = 210
    ASN1_F_BITSTR_CB = 180
    ASN1_F_D2I_ASN1_UINTEGER = 150
    ASN1_F_D2I_PRIVATEKEY = 154
    ASN1_F_I2D_DSA_PUBKEY = 161
    ASN1_F_LONG_C2I = 166
    ASN1_F_OID_MODULE_INIT = 174
    ASN1_F_PARSE_TAGGING = 182
    ASN1_F_PKCS5_PBE_SET = 202
    ASN1_F_SMIME_READ_ASN1 = 212
    ASN1_F_SMIME_TEXT = 213
    @staticmethod
    def ASN1_GENERALIZEDTIME_check():
        'int ASN1_GENERALIZEDTIME_check(ASN1_GENERALIZEDTIME *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ASN1_GENERALIZEDTIME_free():
        'void ASN1_GENERALIZEDTIME_free(ASN1_GENERALIZEDTIME *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ASN1_GENERALIZEDTIME_set():
        'ASN1_GENERALIZEDTIME *ASN1_GENERALIZEDTIME_set(ASN1_GENERALIZEDTIME *, int64_t);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ASN1_GENERALIZEDTIME_set_string():
        'int ASN1_GENERALIZEDTIME_set_string(ASN1_GENERALIZEDTIME *, char *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ASN1_IA5STRING_new():
        'struct asn1_string_st *ASN1_IA5STRING_new();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ASN1_INTEGER_cmp():
        'int ASN1_INTEGER_cmp(ASN1_INTEGER *, ASN1_INTEGER *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ASN1_INTEGER_dup():
        'ASN1_INTEGER *ASN1_INTEGER_dup(ASN1_INTEGER *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ASN1_INTEGER_free():
        'void ASN1_INTEGER_free(ASN1_INTEGER *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ASN1_INTEGER_get():
        'long ASN1_INTEGER_get(ASN1_INTEGER *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ASN1_INTEGER_new():
        'ASN1_INTEGER *ASN1_INTEGER_new();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ASN1_INTEGER_set():
        'int ASN1_INTEGER_set(ASN1_INTEGER *, long);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ASN1_INTEGER_to_BN():
        'BIGNUM *ASN1_INTEGER_to_BN(ASN1_INTEGER *, BIGNUM *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ASN1_ITEM_ptr():
        'ASN1_ITEM *ASN1_ITEM_ptr(ASN1_ITEM_EXP *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ASN1_OBJECT_free():
        'void ASN1_OBJECT_free(ASN1_OBJECT *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ASN1_OBJECT_new():
        'ASN1_OBJECT *ASN1_OBJECT_new();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ASN1_OCTET_STRING_cmp():
        'int ASN1_OCTET_STRING_cmp(struct asn1_string_st *, struct asn1_string_st *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ASN1_OCTET_STRING_dup():
        'struct asn1_string_st *ASN1_OCTET_STRING_dup(struct asn1_string_st *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ASN1_OCTET_STRING_free():
        'void ASN1_OCTET_STRING_free(struct asn1_string_st *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ASN1_OCTET_STRING_new():
        'struct asn1_string_st *ASN1_OCTET_STRING_new();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ASN1_OCTET_STRING_set():
        'int ASN1_OCTET_STRING_set(struct asn1_string_st *, unsigned char *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    ASN1_R_BOOLEAN_IS_WRONG_LENGTH = 106
    ASN1_R_BUFFER_TOO_SMALL = 107
    ASN1_R_CIPHER_HAS_NO_OBJECT_IDENTIFIER = 108
    ASN1_R_DATA_IS_WRONG = 109
    ASN1_R_DECODE_ERROR = 110
    ASN1_R_DEPTH_EXCEEDED = 174
    ASN1_R_ENCODE_ERROR = 112
    ASN1_R_ERROR_GETTING_TIME = 173
    ASN1_R_ERROR_LOADING_SECTION = 172
    ASN1_R_HEADER_TOO_LONG = 123
    ASN1_R_MSTRING_WRONG_TAG = 140
    ASN1_R_NESTED_ASN1_STRING = 197
    ASN1_R_NO_CONTENT_TYPE = 209
    ASN1_R_NO_MATCHING_CHOICE_TYPE = 143
    ASN1_R_NO_MULTIPART_BODY_FAILURE = 210
    ASN1_R_NO_MULTIPART_BOUNDARY = 211
    ASN1_R_UNKNOWN_MESSAGE_DIGEST_ALGORITHM = 161
    ASN1_R_UNKNOWN_OBJECT_TYPE = 162
    ASN1_R_UNKNOWN_PUBLIC_KEY_TYPE = 163
    ASN1_R_UNKNOWN_TAG = 194
    ASN1_R_UNSUPPORTED_ANY_DEFINED_BY_TYPE = 164
    ASN1_R_UNSUPPORTED_PUBLIC_KEY_TYPE = 167
    ASN1_R_UNSUPPORTED_TYPE = 196
    ASN1_R_WRONG_TAG = 168
    @staticmethod
    def ASN1_STRING_cmp():
        'int ASN1_STRING_cmp(struct asn1_string_st *, struct asn1_string_st *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ASN1_STRING_data():
        'unsigned char *ASN1_STRING_data(struct asn1_string_st *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ASN1_STRING_dup():
        'struct asn1_string_st *ASN1_STRING_dup(struct asn1_string_st *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ASN1_STRING_free():
        'void ASN1_STRING_free(struct asn1_string_st *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ASN1_STRING_length():
        'int ASN1_STRING_length(struct asn1_string_st *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ASN1_STRING_new():
        'struct asn1_string_st *ASN1_STRING_new();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ASN1_STRING_set():
        'int ASN1_STRING_set(struct asn1_string_st *, void *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ASN1_STRING_set_default_mask_asc():
        'int ASN1_STRING_set_default_mask_asc(char *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ASN1_STRING_to_UTF8():
        'int ASN1_STRING_to_UTF8(unsigned char * *, struct asn1_string_st *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ASN1_STRING_type():
        'int ASN1_STRING_type(struct asn1_string_st *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ASN1_STRING_type_new():
        'struct asn1_string_st *ASN1_STRING_type_new(int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ASN1_TIME_check():
        'int ASN1_TIME_check(struct asn1_string_st *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ASN1_TIME_free():
        'void ASN1_TIME_free(struct asn1_string_st *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ASN1_TIME_new():
        'struct asn1_string_st *ASN1_TIME_new();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ASN1_TIME_print():
        'int ASN1_TIME_print(struct bio_st *, struct asn1_string_st *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ASN1_TIME_set():
        'struct asn1_string_st *ASN1_TIME_set(struct asn1_string_st *, int64_t);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ASN1_TIME_set_string():
        'int ASN1_TIME_set_string(struct asn1_string_st *, char *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ASN1_TIME_to_generalizedtime():
        'ASN1_GENERALIZEDTIME *ASN1_TIME_to_generalizedtime(struct asn1_string_st *, ASN1_GENERALIZEDTIME * *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ASN1_UTCTIME_check():
        'int ASN1_UTCTIME_check(ASN1_UTCTIME *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ASN1_UTCTIME_cmp_time_t():
        'int ASN1_UTCTIME_cmp_time_t(ASN1_UTCTIME *, int64_t);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ASN1_UTCTIME_free():
        'void ASN1_UTCTIME_free(ASN1_UTCTIME *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ASN1_UTCTIME_new():
        'ASN1_UTCTIME *ASN1_UTCTIME_new();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ASN1_UTCTIME_print():
        'int ASN1_UTCTIME_print(struct bio_st *, ASN1_UTCTIME *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ASN1_UTCTIME_set():
        'ASN1_UTCTIME *ASN1_UTCTIME_set(ASN1_UTCTIME *, int64_t);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ASN1_UTF8STRING_free():
        'void ASN1_UTF8STRING_free(struct asn1_string_st *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ASN1_UTF8STRING_new():
        'struct asn1_string_st *ASN1_UTF8STRING_new();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ASN1_item_d2i():
        'ASN1_VALUE *ASN1_item_d2i(ASN1_VALUE * *, unsigned char * *, long, ASN1_ITEM *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def AUTHORITY_KEYID_free():
        'void AUTHORITY_KEYID_free(AUTHORITY_KEYID *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def AUTHORITY_KEYID_new():
        'AUTHORITY_KEYID *AUTHORITY_KEYID_new();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BASIC_CONSTRAINTS_free():
        'void BASIC_CONSTRAINTS_free(BASIC_CONSTRAINTS *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BASIC_CONSTRAINTS_new():
        'BASIC_CONSTRAINTS *BASIC_CONSTRAINTS_new();\n\nCFFI C function from _openssl.lib'
        pass
    
    BIO_CLOSE = 1
    BIO_CTRL_DUP = 12
    BIO_CTRL_EOF = 2
    BIO_CTRL_FLUSH = 11
    BIO_CTRL_GET = 5
    BIO_CTRL_GET_CLOSE = 8
    BIO_CTRL_INFO = 3
    BIO_CTRL_PENDING = 10
    BIO_CTRL_RESET = 1
    BIO_CTRL_SET = 4
    BIO_CTRL_SET_CLOSE = 9
    BIO_CTRL_WPENDING = 13
    BIO_C_FILE_SEEK = 128
    BIO_C_FILE_TELL = 133
    BIO_FLAGS_IO_SPECIAL = 4
    BIO_FLAGS_READ = 1
    BIO_FLAGS_RWS = 7
    BIO_FLAGS_SHOULD_RETRY = 8
    BIO_FLAGS_WRITE = 2
    BIO_NOCLOSE = 0
    BIO_TYPE_ACCEPT = 1293
    BIO_TYPE_BASE64 = 523
    BIO_TYPE_BIO = 1043
    BIO_TYPE_BUFFER = 521
    BIO_TYPE_CIPHER = 522
    BIO_TYPE_CONNECT = 1292
    BIO_TYPE_DESCRIPTOR = 256
    BIO_TYPE_FD = 1284
    BIO_TYPE_FILE = 1026
    BIO_TYPE_FILTER = 512
    BIO_TYPE_MD = 520
    BIO_TYPE_MEM = 1025
    BIO_TYPE_NBIO_TEST = 528
    BIO_TYPE_NONE = 0
    BIO_TYPE_NULL = 1030
    BIO_TYPE_NULL_FILTER = 529
    BIO_TYPE_SOCKET = 1285
    BIO_TYPE_SOURCE_SINK = 1024
    BIO_TYPE_SSL = 519
    @staticmethod
    def BIO_append_filename():
        'long BIO_append_filename(struct bio_st *, char *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BIO_callback_ctrl():
        'long BIO_callback_ctrl(struct bio_st *, int, void(*)(struct bio_st *, int, char *, int, long, long));\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BIO_clear_retry_flags():
        'void BIO_clear_retry_flags(struct bio_st *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BIO_ctrl():
        'long BIO_ctrl(struct bio_st *, int, long, void *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BIO_ctrl_pending():
        'size_t BIO_ctrl_pending(struct bio_st *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BIO_ctrl_wpending():
        'size_t BIO_ctrl_wpending(struct bio_st *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BIO_eof():
        'int BIO_eof(struct bio_st *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BIO_f_buffer():
        'BIO_METHOD *BIO_f_buffer();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BIO_f_null():
        'BIO_METHOD *BIO_f_null();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BIO_find_type():
        'struct bio_st *BIO_find_type(struct bio_st *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BIO_flush():
        'int BIO_flush(struct bio_st *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BIO_free():
        'int BIO_free(struct bio_st *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BIO_free_all():
        'void BIO_free_all(struct bio_st *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BIO_get_buffer_num_lines():
        'long BIO_get_buffer_num_lines(struct bio_st *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BIO_get_close():
        'int BIO_get_close(struct bio_st *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BIO_get_fd():
        'long BIO_get_fd(struct bio_st *, char *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BIO_get_fp():
        'long BIO_get_fp(struct bio_st *, FILE * *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BIO_get_info_callback():
        'int BIO_get_info_callback(struct bio_st *, void(* *)(struct bio_st *, int, char *, int, long, long));\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BIO_get_mem_data():
        'long BIO_get_mem_data(struct bio_st *, char * *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BIO_get_mem_ptr():
        'long BIO_get_mem_ptr(struct bio_st *, BUF_MEM * *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BIO_gets():
        'int BIO_gets(struct bio_st *, char *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BIO_int_ctrl():
        'long BIO_int_ctrl(struct bio_st *, int, long, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BIO_method_type():
        'int BIO_method_type(struct bio_st *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BIO_new():
        'struct bio_st *BIO_new(BIO_METHOD *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BIO_new_CMS():
        'struct bio_st *BIO_new_CMS(struct bio_st *, CMS_ContentInfo *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BIO_new_fd():
        'struct bio_st *BIO_new_fd(int, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BIO_new_file():
        'struct bio_st *BIO_new_file(char *, char *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BIO_new_fp():
        'struct bio_st *BIO_new_fp(FILE *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BIO_new_mem_buf():
        'struct bio_st *BIO_new_mem_buf(void *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BIO_new_socket():
        'struct bio_st *BIO_new_socket(int, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BIO_next():
        'struct bio_st *BIO_next(struct bio_st *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BIO_pending():
        'int BIO_pending(struct bio_st *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BIO_pop():
        'struct bio_st *BIO_pop(struct bio_st *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BIO_push():
        'struct bio_st *BIO_push(struct bio_st *, struct bio_st *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BIO_puts():
        'int BIO_puts(struct bio_st *, char *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BIO_read():
        'int BIO_read(struct bio_st *, void *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BIO_read_filename():
        'long BIO_read_filename(struct bio_st *, char *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BIO_reset():
        'int BIO_reset(struct bio_st *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BIO_retry_type():
        'int BIO_retry_type(struct bio_st *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BIO_rw_filename():
        'long BIO_rw_filename(struct bio_st *, char *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BIO_s_fd():
        'BIO_METHOD *BIO_s_fd();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BIO_s_file():
        'BIO_METHOD *BIO_s_file();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BIO_s_mem():
        'BIO_METHOD *BIO_s_mem();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BIO_s_null():
        'BIO_METHOD *BIO_s_null();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BIO_s_socket():
        'BIO_METHOD *BIO_s_socket();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BIO_seek():
        'int BIO_seek(struct bio_st *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BIO_set_buffer_read_data():
        'long BIO_set_buffer_read_data(struct bio_st *, void *, long);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BIO_set_buffer_size():
        'long BIO_set_buffer_size(struct bio_st *, long);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BIO_set_close():
        'int BIO_set_close(struct bio_st *, long);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BIO_set_fd():
        'long BIO_set_fd(struct bio_st *, int, long);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BIO_set_fp():
        'long BIO_set_fp(struct bio_st *, FILE *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BIO_set_info_callback():
        'int BIO_set_info_callback(struct bio_st *, void(*)(struct bio_st *, int, char *, int, long, long));\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BIO_set_mem_buf():
        'long BIO_set_mem_buf(struct bio_st *, BUF_MEM *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BIO_set_mem_eof_return():
        'long BIO_set_mem_eof_return(struct bio_st *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BIO_set_nbio():
        'long BIO_set_nbio(struct bio_st *, long);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BIO_set_read_buffer_size():
        'long BIO_set_read_buffer_size(struct bio_st *, long);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BIO_set_retry_read():
        'void BIO_set_retry_read(struct bio_st *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BIO_set_write_buffer_size():
        'long BIO_set_write_buffer_size(struct bio_st *, long);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BIO_should_io_special():
        'int BIO_should_io_special(struct bio_st *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BIO_should_read():
        'int BIO_should_read(struct bio_st *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BIO_should_retry():
        'int BIO_should_retry(struct bio_st *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BIO_should_write():
        'int BIO_should_write(struct bio_st *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BIO_tell():
        'int BIO_tell(struct bio_st *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BIO_up_ref():
        'int BIO_up_ref(struct bio_st *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BIO_vfree():
        'void BIO_vfree(struct bio_st *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BIO_wpending():
        'int BIO_wpending(struct bio_st *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BIO_write():
        'int BIO_write(struct bio_st *, void *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BIO_write_filename():
        'long BIO_write_filename(struct bio_st *, char *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BN_CTX_end():
        'void BN_CTX_end(BN_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BN_CTX_free():
        'void BN_CTX_free(BN_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BN_CTX_get():
        'BIGNUM *BN_CTX_get(BN_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BN_CTX_new():
        'BN_CTX *BN_CTX_new();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BN_CTX_start():
        'void BN_CTX_start(BN_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BN_add():
        'int BN_add(BIGNUM *, BIGNUM *, BIGNUM *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BN_bin2bn():
        'BIGNUM *BN_bin2bn(unsigned char *, int, BIGNUM *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BN_bn2bin():
        'int BN_bn2bin(BIGNUM *, unsigned char *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BN_bn2hex():
        'char *BN_bn2hex(BIGNUM *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BN_clear_bit():
        'int BN_clear_bit(BIGNUM *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BN_cmp():
        'int BN_cmp(BIGNUM *, BIGNUM *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BN_copy():
        'BIGNUM *BN_copy(BIGNUM *, BIGNUM *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BN_dec2bn():
        'int BN_dec2bn(BIGNUM * *, char *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BN_div():
        'int BN_div(BIGNUM *, BIGNUM *, BIGNUM *, BIGNUM *, BN_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BN_dup():
        'BIGNUM *BN_dup(BIGNUM *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BN_exp():
        'int BN_exp(BIGNUM *, BIGNUM *, BIGNUM *, BN_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BN_free():
        'void BN_free(BIGNUM *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BN_gcd():
        'int BN_gcd(BIGNUM *, BIGNUM *, BIGNUM *, BN_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BN_get_word():
        'uint64_t BN_get_word(BIGNUM *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BN_hex2bn():
        'int BN_hex2bn(BIGNUM * *, char *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BN_is_bit_set():
        'int BN_is_bit_set(BIGNUM *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BN_lshift():
        'int BN_lshift(BIGNUM *, BIGNUM *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BN_lshift1():
        'int BN_lshift1(BIGNUM *, BIGNUM *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BN_mask_bits():
        'int BN_mask_bits(BIGNUM *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BN_mod():
        'int BN_mod(BIGNUM *, BIGNUM *, BIGNUM *, BN_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BN_mod_add():
        'int BN_mod_add(BIGNUM *, BIGNUM *, BIGNUM *, BIGNUM *, BN_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BN_mod_exp():
        'int BN_mod_exp(BIGNUM *, BIGNUM *, BIGNUM *, BIGNUM *, BN_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BN_mod_inverse():
        'BIGNUM *BN_mod_inverse(BIGNUM *, BIGNUM *, BIGNUM *, BN_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BN_mod_mul():
        'int BN_mod_mul(BIGNUM *, BIGNUM *, BIGNUM *, BIGNUM *, BN_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BN_mod_sqr():
        'int BN_mod_sqr(BIGNUM *, BIGNUM *, BIGNUM *, BN_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BN_mod_sub():
        'int BN_mod_sub(BIGNUM *, BIGNUM *, BIGNUM *, BIGNUM *, BN_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BN_mul():
        'int BN_mul(BIGNUM *, BIGNUM *, BIGNUM *, BN_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BN_new():
        'BIGNUM *BN_new();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BN_nnmod():
        'int BN_nnmod(BIGNUM *, BIGNUM *, BIGNUM *, BN_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BN_num_bits():
        'int BN_num_bits(BIGNUM *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BN_num_bytes():
        'int BN_num_bytes(BIGNUM *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BN_one():
        'int BN_one(BIGNUM *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BN_rshift():
        'int BN_rshift(BIGNUM *, BIGNUM *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BN_rshift1():
        'int BN_rshift1(BIGNUM *, BIGNUM *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BN_set_bit():
        'int BN_set_bit(BIGNUM *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BN_set_word():
        'int BN_set_word(BIGNUM *, uint64_t);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BN_sqr():
        'int BN_sqr(BIGNUM *, BIGNUM *, BN_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BN_sub():
        'int BN_sub(BIGNUM *, BIGNUM *, BIGNUM *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BN_to_ASN1_INTEGER():
        'ASN1_INTEGER *BN_to_ASN1_INTEGER(BIGNUM *, ASN1_INTEGER *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BN_value_one():
        'BIGNUM *BN_value_one();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BN_zero():
        'int BN_zero(BIGNUM *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def CERTIFICATEPOLICIES_free():
        'void CERTIFICATEPOLICIES_free(Cryptography_STACK_OF_POLICYINFO *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def CMAC_CTX_copy():
        'int CMAC_CTX_copy(CMAC_CTX *, CMAC_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def CMAC_CTX_free():
        'void CMAC_CTX_free(CMAC_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def CMAC_CTX_new():
        'CMAC_CTX *CMAC_CTX_new();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def CMAC_Final():
        'int CMAC_Final(CMAC_CTX *, unsigned char *, size_t *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def CMAC_Init():
        'int CMAC_Init(CMAC_CTX *, void *, size_t, EVP_CIPHER *, ENGINE *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def CMAC_Update():
        'int CMAC_Update(CMAC_CTX *, void *, size_t);\n\nCFFI C function from _openssl.lib'
        pass
    
    CMS_BINARY = 128
    CMS_CRLFEOL = 2048
    CMS_DEBUG_DECRYPT = 131072
    CMS_DETACHED = 64
    CMS_NOATTR = 256
    CMS_NOCERTS = 2
    CMS_NOCRL = 8192
    CMS_NOINTERN = 16
    CMS_NOOLDMIMETYPE = 1024
    CMS_NOSIGS = 12
    CMS_NOSMIMECAP = 512
    CMS_NOVERIFY = 32
    CMS_NO_ATTR_VERIFY = 8
    CMS_NO_CONTENT_VERIFY = 4
    CMS_NO_SIGNER_CERT_VERIFY = 32
    CMS_PARTIAL = 16384
    CMS_REUSE_DIGEST = 32768
    CMS_STREAM = 4096
    CMS_TEXT = 1
    CMS_USE_KEYID = 65536
    @staticmethod
    def CMS_add1_signer():
        'CMS_SignerInfo *CMS_add1_signer(CMS_ContentInfo *, X509 *, EVP_PKEY *, EVP_MD *, unsigned int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def CMS_decrypt():
        'int CMS_decrypt(CMS_ContentInfo *, EVP_PKEY *, X509 *, struct bio_st *, struct bio_st *, unsigned int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def CMS_encrypt():
        'CMS_ContentInfo *CMS_encrypt(Cryptography_STACK_OF_X509 *, struct bio_st *, EVP_CIPHER *, unsigned int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def CMS_final():
        'int CMS_final(CMS_ContentInfo *, struct bio_st *, struct bio_st *, unsigned int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def CMS_sign():
        'CMS_ContentInfo *CMS_sign(X509 *, EVP_PKEY *, Cryptography_STACK_OF_X509 *, struct bio_st *, unsigned int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def CMS_verify():
        'int CMS_verify(CMS_ContentInfo *, Cryptography_STACK_OF_X509 *, X509_STORE *, struct bio_st *, struct bio_st *, unsigned int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def CRL_DIST_POINTS_free():
        'void CRL_DIST_POINTS_free(Cryptography_STACK_OF_DIST_POINT *);\n\nCFFI C function from _openssl.lib'
        pass
    
    CRYPTOGRAPHY_IS_LIBRESSL = 0
    CRYPTOGRAPHY_OPENSSL_102L_OR_GREATER = 1
    CRYPTOGRAPHY_OPENSSL_110F_OR_GREATER = 1
    CRYPTOGRAPHY_OPENSSL_110_OR_GREATER = 1
    CRYPTOGRAPHY_OPENSSL_LESS_THAN_102 = 0
    CRYPTOGRAPHY_OPENSSL_LESS_THAN_102I = 0
    CRYPTO_LOCK = 1
    CRYPTO_LOCK_SSL = 0
    CRYPTO_MEM_CHECK_DISABLE = 3
    CRYPTO_MEM_CHECK_ENABLE = 2
    CRYPTO_MEM_CHECK_OFF = 0
    CRYPTO_MEM_CHECK_ON = 1
    CRYPTO_READ = 4
    CRYPTO_UNLOCK = 2
    @staticmethod
    def CRYPTO_cleanup_all_ex_data():
        'void CRYPTO_cleanup_all_ex_data();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def CRYPTO_get_locking_callback():
        'void(*CRYPTO_get_locking_callback())(int, int, char *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def CRYPTO_lock():
        'void CRYPTO_lock(int, int, char *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def CRYPTO_mem_ctrl():
        'int CRYPTO_mem_ctrl(int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def CRYPTO_num_locks():
        'int CRYPTO_num_locks();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def CRYPTO_set_locking_callback():
        'void CRYPTO_set_locking_callback(void(*)(int, int, char *, int));\n\nCFFI C function from _openssl.lib'
        pass
    
    CT_LOG_ENTRY_TYPE_NOT_SET = -1
    CT_LOG_ENTRY_TYPE_PRECERT = 1
    CT_LOG_ENTRY_TYPE_X509 = 0
    @staticmethod
    def Cryptography_CRYPTO_set_mem_functions():
        'int Cryptography_CRYPTO_set_mem_functions(void *(*)(size_t, char *, int), void *(*)(void *, size_t, char *, int), void(*)(void *, char *, int));\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def Cryptography_DH_check():
        'int Cryptography_DH_check(DH *, int *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def Cryptography_DTLSv1_get_timeout():
        'long Cryptography_DTLSv1_get_timeout(SSL *, int64_t *, long *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def Cryptography_EVP_MD_CTX_free():
        'void Cryptography_EVP_MD_CTX_free(EVP_MD_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def Cryptography_EVP_MD_CTX_new():
        'EVP_MD_CTX *Cryptography_EVP_MD_CTX_new();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def Cryptography_EVP_PKEY_id():
        'int Cryptography_EVP_PKEY_id(EVP_PKEY *);\n\nCFFI C function from _openssl.lib'
        pass
    
    Cryptography_HAS_102_VERIFICATION_ERROR_CODES = 1
    Cryptography_HAS_102_VERIFICATION_PARAMS = 1
    Cryptography_HAS_AES_WRAP = 1
    Cryptography_HAS_ALPN = 1
    Cryptography_HAS_CMAC = 1
    Cryptography_HAS_CMS = 1
    Cryptography_HAS_CMS_BIO_FUNCTIONS = 1
    Cryptography_HAS_COMPRESSION = 1
    Cryptography_HAS_DTLS = 1
    Cryptography_HAS_EC = 1
    Cryptography_HAS_EC2M = 1
    Cryptography_HAS_ECDH = 1
    Cryptography_HAS_ECDSA = 1
    Cryptography_HAS_EC_1_0_2 = 1
    Cryptography_HAS_EC_CODES = 1
    Cryptography_HAS_EGD = 0
    Cryptography_HAS_EVP_PKEY_DHX = 1
    Cryptography_HAS_EVP_PKEY_get_set_tls_encodedpoint = 1
    Cryptography_HAS_FIPS = 1
    Cryptography_HAS_GCM = 1
    Cryptography_HAS_GENERIC_DTLS_METHOD = 1
    Cryptography_HAS_GET_SERVER_TMP_KEY = 1
    Cryptography_HAS_LOCKING_CALLBACKS = 0
    Cryptography_HAS_MEM_FUNCTIONS = 1
    Cryptography_HAS_NEXTPROTONEG = 1
    Cryptography_HAS_OP_NO_COMPRESSION = 1
    Cryptography_HAS_PBKDF2_HMAC = 1
    Cryptography_HAS_PKEY_CTX = 1
    Cryptography_HAS_PSS_PADDING = 1
    Cryptography_HAS_RELEASE_BUFFERS = 1
    Cryptography_HAS_RSA_OAEP_LABEL = 1
    Cryptography_HAS_RSA_OAEP_MD = 1
    Cryptography_HAS_RSA_R_PKCS_DECODING_ERROR = 1
    Cryptography_HAS_SCRYPT = 1
    Cryptography_HAS_SCT = 1
    Cryptography_HAS_SECURE_RENEGOTIATION = 1
    Cryptography_HAS_SET_CERT_CB = 1
    Cryptography_HAS_SET_ECDH_AUTO = 1
    Cryptography_HAS_SSL2 = 0
    Cryptography_HAS_SSL3_METHOD = 0
    Cryptography_HAS_SSL_CTX_CLEAR_OPTIONS = 1
    Cryptography_HAS_SSL_CTX_SET_CLIENT_CERT_ENGINE = 1
    Cryptography_HAS_SSL_OP_MSIE_SSLV2_RSA_PADDING = 1
    Cryptography_HAS_SSL_OP_NO_TICKET = 1
    Cryptography_HAS_SSL_SET_SSL_CTX = 1
    Cryptography_HAS_SSL_ST = 0
    Cryptography_HAS_STATUS_REQ_OCSP_RESP = 1
    Cryptography_HAS_TLSEXT_HOSTNAME = 1
    Cryptography_HAS_TLSEXT_STATUS_REQ_CB = 1
    Cryptography_HAS_TLSEXT_STATUS_REQ_TYPE = 1
    Cryptography_HAS_TLS_ST = 1
    Cryptography_HAS_TLSv1_1 = 1
    Cryptography_HAS_TLSv1_2 = 1
    Cryptography_HAS_X25519 = 1
    Cryptography_HAS_X509_STORE_CTX_GET_ISSUER = 1
    Cryptography_HAS_X509_V_FLAG_PARTIAL_CHAIN = 1
    Cryptography_HAS_X509_V_FLAG_TRUSTED_FIRST = 1
    @staticmethod
    def Cryptography_HMAC_CTX_free():
        'void Cryptography_HMAC_CTX_free(HMAC_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def Cryptography_HMAC_CTX_new():
        'HMAC_CTX *Cryptography_HMAC_CTX_new();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def Cryptography_X509_NAME_ENTRY_set():
        'int Cryptography_X509_NAME_ENTRY_set(X509_NAME_ENTRY *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def Cryptography_X509_REVOKED_dup():
        'X509_REVOKED *Cryptography_X509_REVOKED_dup(X509_REVOKED *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def Cryptography_add_osrandom_engine():
        'int Cryptography_add_osrandom_engine();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def Cryptography_d2i_DHxparams_bio():
        'DH *Cryptography_d2i_DHxparams_bio(struct bio_st *, DH * *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def Cryptography_free_wrapper():
        'void Cryptography_free_wrapper(void *, char *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def Cryptography_i2d_DHxparams_bio():
        'int Cryptography_i2d_DHxparams_bio(struct bio_st *, DH *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def Cryptography_malloc_wrapper():
        'void *Cryptography_malloc_wrapper(size_t, char *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def Cryptography_osrandom_engine_id():
        pass
    
    @staticmethod
    def Cryptography_osrandom_engine_name():
        pass
    
    @staticmethod
    def Cryptography_pem_password_cb():
        'int Cryptography_pem_password_cb(char *, int, int, void *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def Cryptography_realloc_wrapper():
        'void *Cryptography_realloc_wrapper(void *, size_t, char *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    DH_F_COMPUTE_KEY = 102
    DH_NOT_SUITABLE_GENERATOR = 8
    DH_R_INVALID_PUBKEY = 102
    @staticmethod
    def DH_check_pub_key():
        'int DH_check_pub_key(DH *, BIGNUM *, int *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def DH_compute_key():
        'int DH_compute_key(unsigned char *, BIGNUM *, DH *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def DH_free():
        'void DH_free(DH *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def DH_generate_key():
        'int DH_generate_key(DH *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def DH_generate_parameters_ex():
        'int DH_generate_parameters_ex(DH *, int, int, BN_GENCB *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def DH_get0_key():
        'void DH_get0_key(DH *, BIGNUM * *, BIGNUM * *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def DH_get0_pqg():
        'void DH_get0_pqg(DH *, BIGNUM * *, BIGNUM * *, BIGNUM * *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def DH_get_ex_data():
        'void *DH_get_ex_data(DH *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def DH_new():
        'DH *DH_new();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def DH_set0_key():
        'int DH_set0_key(DH *, BIGNUM *, BIGNUM *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def DH_set0_pqg():
        'int DH_set0_pqg(DH *, BIGNUM *, BIGNUM *, BIGNUM *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def DH_set_ex_data():
        'int DH_set_ex_data(DH *, int, void *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def DH_size():
        'int DH_size(DH *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def DHparams_dup():
        'DH *DHparams_dup(DH *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def DHparams_print():
        'int DHparams_print(struct bio_st *, DH *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def DHparams_print_fp():
        'int DHparams_print_fp(FILE *, DH *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def DIST_POINT_NAME_free():
        'void DIST_POINT_NAME_free(DIST_POINT_NAME *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def DIST_POINT_NAME_new():
        'DIST_POINT_NAME *DIST_POINT_NAME_new();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def DIST_POINT_free():
        'void DIST_POINT_free(DIST_POINT *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def DIST_POINT_new():
        'DIST_POINT *DIST_POINT_new();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def DSA_free():
        'void DSA_free(DSA *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def DSA_generate_key():
        'int DSA_generate_key(DSA *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def DSA_generate_parameters_ex():
        'int DSA_generate_parameters_ex(DSA *, int, unsigned char *, int, int *, unsigned long *, BN_GENCB *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def DSA_get0_key():
        'void DSA_get0_key(DSA *, BIGNUM * *, BIGNUM * *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def DSA_get0_pqg():
        'void DSA_get0_pqg(DSA *, BIGNUM * *, BIGNUM * *, BIGNUM * *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def DSA_new():
        'DSA *DSA_new();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def DSA_set0_key():
        'int DSA_set0_key(DSA *, BIGNUM *, BIGNUM *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def DSA_set0_pqg():
        'int DSA_set0_pqg(DSA *, BIGNUM *, BIGNUM *, BIGNUM *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def DSA_sign():
        'int DSA_sign(int, unsigned char *, int, unsigned char *, unsigned int *, DSA *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def DSA_size():
        'int DSA_size(DSA *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def DSA_verify():
        'int DSA_verify(int, unsigned char *, int, unsigned char *, int, DSA *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def DSAparams_dup():
        'DSA *DSAparams_dup(DSA *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def DTLS_client_method():
        'SSL_METHOD *DTLS_client_method();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def DTLS_method():
        'SSL_METHOD *DTLS_method();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def DTLS_server_method():
        'SSL_METHOD *DTLS_server_method();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def DTLSv1_client_method():
        'SSL_METHOD *DTLSv1_client_method();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def DTLSv1_handle_timeout():
        'long DTLSv1_handle_timeout(SSL *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def DTLSv1_method():
        'SSL_METHOD *DTLSv1_method();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def DTLSv1_server_method():
        'SSL_METHOD *DTLSv1_server_method();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ECDH_compute_key():
        'int ECDH_compute_key(void *, size_t, EC_POINT *, EC_KEY *, void *(*)(void *, size_t, void *, size_t *));\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ECDSA_SIG_free():
        'void ECDSA_SIG_free(ECDSA_SIG *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ECDSA_SIG_new():
        'ECDSA_SIG *ECDSA_SIG_new();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ECDSA_do_sign():
        'ECDSA_SIG *ECDSA_do_sign(unsigned char *, int, EC_KEY *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ECDSA_do_sign_ex():
        'ECDSA_SIG *ECDSA_do_sign_ex(unsigned char *, int, BIGNUM *, BIGNUM *, EC_KEY *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ECDSA_do_verify():
        'int ECDSA_do_verify(unsigned char *, int, ECDSA_SIG *, EC_KEY *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ECDSA_sign():
        'int ECDSA_sign(int, unsigned char *, int, unsigned char *, unsigned int *, EC_KEY *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ECDSA_sign_ex():
        'int ECDSA_sign_ex(int, unsigned char *, int, unsigned char *, unsigned int *, BIGNUM *, BIGNUM *, EC_KEY *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ECDSA_sign_setup():
        'int ECDSA_sign_setup(EC_KEY *, BN_CTX *, BIGNUM * *, BIGNUM * *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ECDSA_size():
        'int ECDSA_size(EC_KEY *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ECDSA_verify():
        'int ECDSA_verify(int, unsigned char *, int, unsigned char *, int, EC_KEY *);\n\nCFFI C function from _openssl.lib'
        pass
    
    EC_F_EC_GROUP_NEW_BY_CURVE_NAME = 174
    @staticmethod
    def EC_GF2m_simple_method():
        'EC_METHOD *EC_GF2m_simple_method();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EC_GFp_mont_method():
        'EC_METHOD *EC_GFp_mont_method();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EC_GFp_nist_method():
        'EC_METHOD *EC_GFp_nist_method();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EC_GFp_simple_method():
        'EC_METHOD *EC_GFp_simple_method();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EC_GROUP_clear_free():
        'void EC_GROUP_clear_free(EC_GROUP *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EC_GROUP_free():
        'void EC_GROUP_free(EC_GROUP *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EC_GROUP_get0_generator():
        'EC_POINT *EC_GROUP_get0_generator(EC_GROUP *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EC_GROUP_get_curve_GF2m():
        'int EC_GROUP_get_curve_GF2m(EC_GROUP *, BIGNUM *, BIGNUM *, BIGNUM *, BN_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EC_GROUP_get_curve_GFp():
        'int EC_GROUP_get_curve_GFp(EC_GROUP *, BIGNUM *, BIGNUM *, BIGNUM *, BN_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EC_GROUP_get_curve_name():
        'int EC_GROUP_get_curve_name(EC_GROUP *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EC_GROUP_get_degree():
        'int EC_GROUP_get_degree(EC_GROUP *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EC_GROUP_get_order():
        'int EC_GROUP_get_order(EC_GROUP *, BIGNUM *, BN_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EC_GROUP_have_precompute_mult():
        'int EC_GROUP_have_precompute_mult(EC_GROUP *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EC_GROUP_method_of():
        'EC_METHOD *EC_GROUP_method_of(EC_GROUP *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EC_GROUP_new():
        'EC_GROUP *EC_GROUP_new(EC_METHOD *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EC_GROUP_new_by_curve_name():
        'EC_GROUP *EC_GROUP_new_by_curve_name(int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EC_GROUP_new_curve_GF2m():
        'EC_GROUP *EC_GROUP_new_curve_GF2m(BIGNUM *, BIGNUM *, BIGNUM *, BN_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EC_GROUP_new_curve_GFp():
        'EC_GROUP *EC_GROUP_new_curve_GFp(BIGNUM *, BIGNUM *, BIGNUM *, BN_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EC_GROUP_precompute_mult():
        'int EC_GROUP_precompute_mult(EC_GROUP *, BN_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EC_GROUP_set_asn1_flag():
        'void EC_GROUP_set_asn1_flag(EC_GROUP *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EC_GROUP_set_curve_GF2m():
        'int EC_GROUP_set_curve_GF2m(EC_GROUP *, BIGNUM *, BIGNUM *, BIGNUM *, BN_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EC_GROUP_set_curve_GFp():
        'int EC_GROUP_set_curve_GFp(EC_GROUP *, BIGNUM *, BIGNUM *, BIGNUM *, BN_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EC_GROUP_set_point_conversion_form():
        'void EC_GROUP_set_point_conversion_form(EC_GROUP *, point_conversion_form_t);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EC_KEY_check_key():
        'int EC_KEY_check_key(EC_KEY *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EC_KEY_clear_flags():
        'void EC_KEY_clear_flags(EC_KEY *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EC_KEY_copy():
        'EC_KEY *EC_KEY_copy(EC_KEY *, EC_KEY *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EC_KEY_dup():
        'EC_KEY *EC_KEY_dup(EC_KEY *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EC_KEY_free():
        'void EC_KEY_free(EC_KEY *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EC_KEY_generate_key():
        'int EC_KEY_generate_key(EC_KEY *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EC_KEY_get0_group():
        'EC_GROUP *EC_KEY_get0_group(EC_KEY *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EC_KEY_get0_private_key():
        'BIGNUM *EC_KEY_get0_private_key(EC_KEY *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EC_KEY_get0_public_key():
        'EC_POINT *EC_KEY_get0_public_key(EC_KEY *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EC_KEY_get_conv_form():
        'point_conversion_form_t EC_KEY_get_conv_form(EC_KEY *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EC_KEY_get_enc_flags():
        'unsigned int EC_KEY_get_enc_flags(EC_KEY *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EC_KEY_get_flags():
        'int EC_KEY_get_flags(EC_KEY *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EC_KEY_new():
        'EC_KEY *EC_KEY_new();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EC_KEY_new_by_curve_name():
        'EC_KEY *EC_KEY_new_by_curve_name(int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EC_KEY_precompute_mult():
        'int EC_KEY_precompute_mult(EC_KEY *, BN_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EC_KEY_set_asn1_flag():
        'void EC_KEY_set_asn1_flag(EC_KEY *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EC_KEY_set_conv_form():
        'void EC_KEY_set_conv_form(EC_KEY *, point_conversion_form_t);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EC_KEY_set_enc_flags():
        'void EC_KEY_set_enc_flags(EC_KEY *, unsigned int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EC_KEY_set_flags():
        'void EC_KEY_set_flags(EC_KEY *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EC_KEY_set_group():
        'int EC_KEY_set_group(EC_KEY *, EC_GROUP *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EC_KEY_set_private_key():
        'int EC_KEY_set_private_key(EC_KEY *, BIGNUM *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EC_KEY_set_public_key():
        'int EC_KEY_set_public_key(EC_KEY *, EC_POINT *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EC_KEY_set_public_key_affine_coordinates():
        'int EC_KEY_set_public_key_affine_coordinates(EC_KEY *, BIGNUM *, BIGNUM *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EC_KEY_up_ref():
        'int EC_KEY_up_ref(EC_KEY *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EC_METHOD_get_field_type():
        'int EC_METHOD_get_field_type(EC_METHOD *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EC_POINT_add():
        'int EC_POINT_add(EC_GROUP *, EC_POINT *, EC_POINT *, EC_POINT *, BN_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EC_POINT_bn2point():
        'EC_POINT *EC_POINT_bn2point(EC_GROUP *, BIGNUM *, EC_POINT *, BN_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EC_POINT_clear_free():
        'void EC_POINT_clear_free(EC_POINT *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EC_POINT_cmp():
        'int EC_POINT_cmp(EC_GROUP *, EC_POINT *, EC_POINT *, BN_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EC_POINT_copy():
        'int EC_POINT_copy(EC_POINT *, EC_POINT *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EC_POINT_dbl():
        'int EC_POINT_dbl(EC_GROUP *, EC_POINT *, EC_POINT *, BN_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EC_POINT_dup():
        'EC_POINT *EC_POINT_dup(EC_POINT *, EC_GROUP *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EC_POINT_free():
        'void EC_POINT_free(EC_POINT *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EC_POINT_get_Jprojective_coordinates_GFp():
        'int EC_POINT_get_Jprojective_coordinates_GFp(EC_GROUP *, EC_POINT *, BIGNUM *, BIGNUM *, BIGNUM *, BN_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EC_POINT_get_affine_coordinates_GF2m():
        'int EC_POINT_get_affine_coordinates_GF2m(EC_GROUP *, EC_POINT *, BIGNUM *, BIGNUM *, BN_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EC_POINT_get_affine_coordinates_GFp():
        'int EC_POINT_get_affine_coordinates_GFp(EC_GROUP *, EC_POINT *, BIGNUM *, BIGNUM *, BN_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EC_POINT_hex2point():
        'EC_POINT *EC_POINT_hex2point(EC_GROUP *, char *, EC_POINT *, BN_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EC_POINT_invert():
        'int EC_POINT_invert(EC_GROUP *, EC_POINT *, BN_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EC_POINT_is_at_infinity():
        'int EC_POINT_is_at_infinity(EC_GROUP *, EC_POINT *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EC_POINT_is_on_curve():
        'int EC_POINT_is_on_curve(EC_GROUP *, EC_POINT *, BN_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EC_POINT_make_affine():
        'int EC_POINT_make_affine(EC_GROUP *, EC_POINT *, BN_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EC_POINT_method_of():
        'EC_METHOD *EC_POINT_method_of(EC_POINT *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EC_POINT_mul():
        'int EC_POINT_mul(EC_GROUP *, EC_POINT *, BIGNUM *, EC_POINT *, BIGNUM *, BN_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EC_POINT_new():
        'EC_POINT *EC_POINT_new(EC_GROUP *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EC_POINT_oct2point():
        'int EC_POINT_oct2point(EC_GROUP *, EC_POINT *, unsigned char *, size_t, BN_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EC_POINT_point2bn():
        'BIGNUM *EC_POINT_point2bn(EC_GROUP *, EC_POINT *, point_conversion_form_t, BIGNUM *, BN_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EC_POINT_point2hex():
        'char *EC_POINT_point2hex(EC_GROUP *, EC_POINT *, point_conversion_form_t, BN_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EC_POINT_point2oct():
        'size_t EC_POINT_point2oct(EC_GROUP *, EC_POINT *, point_conversion_form_t, unsigned char *, size_t, BN_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EC_POINT_set_Jprojective_coordinates_GFp():
        'int EC_POINT_set_Jprojective_coordinates_GFp(EC_GROUP *, EC_POINT *, BIGNUM *, BIGNUM *, BIGNUM *, BN_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EC_POINT_set_affine_coordinates_GF2m():
        'int EC_POINT_set_affine_coordinates_GF2m(EC_GROUP *, EC_POINT *, BIGNUM *, BIGNUM *, BN_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EC_POINT_set_affine_coordinates_GFp():
        'int EC_POINT_set_affine_coordinates_GFp(EC_GROUP *, EC_POINT *, BIGNUM *, BIGNUM *, BN_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EC_POINT_set_compressed_coordinates_GF2m():
        'int EC_POINT_set_compressed_coordinates_GF2m(EC_GROUP *, EC_POINT *, BIGNUM *, int, BN_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EC_POINT_set_compressed_coordinates_GFp():
        'int EC_POINT_set_compressed_coordinates_GFp(EC_GROUP *, EC_POINT *, BIGNUM *, int, BN_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EC_POINT_set_to_infinity():
        'int EC_POINT_set_to_infinity(EC_GROUP *, EC_POINT *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EC_POINTs_make_affine():
        'int EC_POINTs_make_affine(EC_GROUP *, size_t, EC_POINT * *, BN_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EC_POINTs_mul():
        'int EC_POINTs_mul(EC_GROUP *, EC_POINT *, BIGNUM *, size_t, EC_POINT * *, BIGNUM * *, BN_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    EC_R_UNKNOWN_GROUP = 129
    @staticmethod
    def EC_curve_nid2nist():
        'char *EC_curve_nid2nist(int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EC_get_builtin_curves():
        'size_t EC_get_builtin_curves(EC_builtin_curve *, size_t);\n\nCFFI C function from _openssl.lib'
        pass
    
    ENGINE_METHOD_ALL = 65535
    ENGINE_METHOD_CIPHERS = 64
    ENGINE_METHOD_DIGESTS = 128
    ENGINE_METHOD_DSA = 2
    ENGINE_METHOD_NONE = 0
    ENGINE_METHOD_RAND = 8
    ENGINE_METHOD_RSA = 1
    ENGINE_R_CONFLICTING_ENGINE_ID = 103
    @staticmethod
    def ENGINE_add():
        'int ENGINE_add(ENGINE *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ENGINE_add_conf_module():
        'void ENGINE_add_conf_module();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ENGINE_by_id():
        'ENGINE *ENGINE_by_id(char *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ENGINE_cleanup():
        'void ENGINE_cleanup();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ENGINE_cmd_is_executable():
        'int ENGINE_cmd_is_executable(ENGINE *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ENGINE_ctrl():
        'int ENGINE_ctrl(ENGINE *, int, long, void *, void(*)());\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ENGINE_ctrl_cmd():
        'int ENGINE_ctrl_cmd(ENGINE *, char *, long, void *, void(*)(), int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ENGINE_ctrl_cmd_string():
        'int ENGINE_ctrl_cmd_string(ENGINE *, char *, char *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ENGINE_finish():
        'int ENGINE_finish(ENGINE *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ENGINE_free():
        'int ENGINE_free(ENGINE *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ENGINE_get_DH():
        'DH_METHOD *ENGINE_get_DH(ENGINE *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ENGINE_get_DSA():
        'DSA_METHOD *ENGINE_get_DSA(ENGINE *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ENGINE_get_RAND():
        'RAND_METHOD *ENGINE_get_RAND(ENGINE *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ENGINE_get_RSA():
        'RSA_METHOD *ENGINE_get_RSA(ENGINE *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ENGINE_get_cipher():
        'EVP_CIPHER *ENGINE_get_cipher(ENGINE *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ENGINE_get_cipher_engine():
        'ENGINE *ENGINE_get_cipher_engine(int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ENGINE_get_cmd_defns():
        'ENGINE_CMD_DEFN *ENGINE_get_cmd_defns(ENGINE *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ENGINE_get_default_DH():
        'ENGINE *ENGINE_get_default_DH();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ENGINE_get_default_DSA():
        'ENGINE *ENGINE_get_default_DSA();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ENGINE_get_default_RAND():
        'ENGINE *ENGINE_get_default_RAND();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ENGINE_get_default_RSA():
        'ENGINE *ENGINE_get_default_RSA();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ENGINE_get_digest():
        'EVP_MD *ENGINE_get_digest(ENGINE *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ENGINE_get_digest_engine():
        'ENGINE *ENGINE_get_digest_engine(int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ENGINE_get_first():
        'ENGINE *ENGINE_get_first();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ENGINE_get_flags():
        'int ENGINE_get_flags(ENGINE *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ENGINE_get_id():
        'char *ENGINE_get_id(ENGINE *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ENGINE_get_last():
        'ENGINE *ENGINE_get_last();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ENGINE_get_name():
        'char *ENGINE_get_name(ENGINE *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ENGINE_get_next():
        'ENGINE *ENGINE_get_next(ENGINE *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ENGINE_get_prev():
        'ENGINE *ENGINE_get_prev(ENGINE *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ENGINE_get_table_flags():
        'unsigned int ENGINE_get_table_flags();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ENGINE_init():
        'int ENGINE_init(ENGINE *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ENGINE_load_builtin_engines():
        'void ENGINE_load_builtin_engines();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ENGINE_load_dynamic():
        'void ENGINE_load_dynamic();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ENGINE_load_openssl():
        'void ENGINE_load_openssl();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ENGINE_load_private_key():
        'EVP_PKEY *ENGINE_load_private_key(ENGINE *, char *, UI_METHOD *, void *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ENGINE_load_public_key():
        'EVP_PKEY *ENGINE_load_public_key(ENGINE *, char *, UI_METHOD *, void *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ENGINE_new():
        'ENGINE *ENGINE_new();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ENGINE_register_DH():
        'int ENGINE_register_DH(ENGINE *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ENGINE_register_DSA():
        'int ENGINE_register_DSA(ENGINE *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ENGINE_register_RAND():
        'int ENGINE_register_RAND(ENGINE *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ENGINE_register_RSA():
        'int ENGINE_register_RSA(ENGINE *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ENGINE_register_all_DH():
        'void ENGINE_register_all_DH();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ENGINE_register_all_DSA():
        'void ENGINE_register_all_DSA();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ENGINE_register_all_RAND():
        'void ENGINE_register_all_RAND();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ENGINE_register_all_RSA():
        'void ENGINE_register_all_RSA();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ENGINE_register_all_ciphers():
        'void ENGINE_register_all_ciphers();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ENGINE_register_all_complete():
        'int ENGINE_register_all_complete();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ENGINE_register_all_digests():
        'void ENGINE_register_all_digests();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ENGINE_register_ciphers():
        'int ENGINE_register_ciphers(ENGINE *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ENGINE_register_complete():
        'int ENGINE_register_complete(ENGINE *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ENGINE_register_digests():
        'int ENGINE_register_digests(ENGINE *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ENGINE_remove():
        'int ENGINE_remove(ENGINE *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ENGINE_set_DH():
        'int ENGINE_set_DH(ENGINE *, DH_METHOD *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ENGINE_set_DSA():
        'int ENGINE_set_DSA(ENGINE *, DSA_METHOD *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ENGINE_set_RAND():
        'int ENGINE_set_RAND(ENGINE *, RAND_METHOD *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ENGINE_set_RSA():
        'int ENGINE_set_RSA(ENGINE *, RSA_METHOD *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ENGINE_set_ciphers():
        'int ENGINE_set_ciphers(ENGINE *, struct $$ENGINE_CIPHERS_PTR *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ENGINE_set_cmd_defns():
        'int ENGINE_set_cmd_defns(ENGINE *, ENGINE_CMD_DEFN *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ENGINE_set_ctrl_function():
        'int ENGINE_set_ctrl_function(ENGINE *, struct $$ENGINE_CTRL_FUNC_PTR *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ENGINE_set_default():
        'int ENGINE_set_default(ENGINE *, unsigned int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ENGINE_set_default_DH():
        'int ENGINE_set_default_DH(ENGINE *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ENGINE_set_default_DSA():
        'int ENGINE_set_default_DSA(ENGINE *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ENGINE_set_default_RAND():
        'int ENGINE_set_default_RAND(ENGINE *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ENGINE_set_default_RSA():
        'int ENGINE_set_default_RSA(ENGINE *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ENGINE_set_default_ciphers():
        'int ENGINE_set_default_ciphers(ENGINE *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ENGINE_set_default_digests():
        'int ENGINE_set_default_digests(ENGINE *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ENGINE_set_default_string():
        'int ENGINE_set_default_string(ENGINE *, char *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ENGINE_set_destroy_function():
        'int ENGINE_set_destroy_function(ENGINE *, int(*)(ENGINE *));\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ENGINE_set_digests():
        'int ENGINE_set_digests(ENGINE *, struct $$ENGINE_DIGESTS_PTR *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ENGINE_set_finish_function():
        'int ENGINE_set_finish_function(ENGINE *, int(*)(ENGINE *));\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ENGINE_set_flags():
        'int ENGINE_set_flags(ENGINE *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ENGINE_set_id():
        'int ENGINE_set_id(ENGINE *, char *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ENGINE_set_init_function():
        'int ENGINE_set_init_function(ENGINE *, int(*)(ENGINE *));\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ENGINE_set_load_privkey_function():
        'int ENGINE_set_load_privkey_function(ENGINE *, struct $$ENGINE_LOAD_KEY_PTR *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ENGINE_set_load_pubkey_function():
        'int ENGINE_set_load_pubkey_function(ENGINE *, struct $$ENGINE_LOAD_KEY_PTR *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ENGINE_set_name():
        'int ENGINE_set_name(ENGINE *, char *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ENGINE_set_table_flags():
        'void ENGINE_set_table_flags(unsigned int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ENGINE_unregister_DH():
        'void ENGINE_unregister_DH(ENGINE *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ENGINE_unregister_DSA():
        'void ENGINE_unregister_DSA(ENGINE *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ENGINE_unregister_RAND():
        'void ENGINE_unregister_RAND(ENGINE *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ENGINE_unregister_RSA():
        'void ENGINE_unregister_RSA(ENGINE *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ENGINE_unregister_ciphers():
        'void ENGINE_unregister_ciphers(ENGINE *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ENGINE_unregister_digests():
        'void ENGINE_unregister_digests(ENGINE *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ENGINE_up_ref():
        'int ENGINE_up_ref(ENGINE *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ERR_GET_FUNC():
        'int ERR_GET_FUNC(unsigned long);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ERR_GET_LIB():
        'int ERR_GET_LIB(unsigned long);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ERR_GET_REASON():
        'int ERR_GET_REASON(unsigned long);\n\nCFFI C function from _openssl.lib'
        pass
    
    ERR_LIB_ASN1 = 13
    ERR_LIB_DH = 5
    ERR_LIB_EC = 16
    ERR_LIB_EVP = 6
    ERR_LIB_PEM = 9
    ERR_LIB_PKCS12 = 35
    ERR_LIB_RSA = 4
    ERR_LIB_SSL = 20
    ERR_LIB_X509 = 11
    @staticmethod
    def ERR_PACK():
        'unsigned long ERR_PACK(int, int, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ERR_add_error_data():
        pass
    
    @staticmethod
    def ERR_clear_error():
        'void ERR_clear_error();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ERR_error_string():
        'char *ERR_error_string(unsigned long, char *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ERR_error_string_n():
        'void ERR_error_string_n(unsigned long, char *, size_t);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ERR_free_strings():
        'void ERR_free_strings();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ERR_func_error_string():
        'char *ERR_func_error_string(unsigned long);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ERR_get_error():
        'unsigned long ERR_get_error();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ERR_get_error_line():
        'unsigned long ERR_get_error_line(char * *, int *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ERR_get_error_line_data():
        'unsigned long ERR_get_error_line_data(char * *, int *, char * *, int *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ERR_get_next_error_library():
        'int ERR_get_next_error_library();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ERR_get_state():
        'ERR_STATE *ERR_get_state();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ERR_lib_error_string():
        'char *ERR_lib_error_string(unsigned long);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ERR_load_RAND_strings():
        'void ERR_load_RAND_strings();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ERR_peek_error():
        'unsigned long ERR_peek_error();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ERR_peek_error_line():
        'unsigned long ERR_peek_error_line(char * *, int *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ERR_peek_error_line_data():
        'unsigned long ERR_peek_error_line_data(char * *, int *, char * *, int *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ERR_peek_last_error():
        'unsigned long ERR_peek_last_error();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ERR_peek_last_error_line():
        'unsigned long ERR_peek_last_error_line(char * *, int *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ERR_peek_last_error_line_data():
        'unsigned long ERR_peek_last_error_line_data(char * *, int *, char * *, int *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ERR_print_errors():
        'void ERR_print_errors(struct bio_st *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ERR_print_errors_fp():
        'void ERR_print_errors_fp(FILE *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ERR_put_error():
        'void ERR_put_error(int, int, int, char *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ERR_reason_error_string():
        'char *ERR_reason_error_string(unsigned long);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_CIPHER_CTX_block_size():
        'int EVP_CIPHER_CTX_block_size(EVP_CIPHER_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_CIPHER_CTX_cipher():
        'EVP_CIPHER *EVP_CIPHER_CTX_cipher(EVP_CIPHER_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_CIPHER_CTX_cleanup():
        'int EVP_CIPHER_CTX_cleanup(EVP_CIPHER_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_CIPHER_CTX_ctrl():
        'int EVP_CIPHER_CTX_ctrl(EVP_CIPHER_CTX *, int, int, void *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_CIPHER_CTX_free():
        'void EVP_CIPHER_CTX_free(EVP_CIPHER_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_CIPHER_CTX_init():
        'void EVP_CIPHER_CTX_init(EVP_CIPHER_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_CIPHER_CTX_new():
        'EVP_CIPHER_CTX *EVP_CIPHER_CTX_new();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_CIPHER_CTX_set_key_length():
        'int EVP_CIPHER_CTX_set_key_length(EVP_CIPHER_CTX *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_CIPHER_CTX_set_padding():
        'int EVP_CIPHER_CTX_set_padding(EVP_CIPHER_CTX *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_CIPHER_block_size():
        'int EVP_CIPHER_block_size(EVP_CIPHER *);\n\nCFFI C function from _openssl.lib'
        pass
    
    EVP_CTRL_AEAD_GET_TAG = 16
    EVP_CTRL_AEAD_SET_IVLEN = 9
    EVP_CTRL_AEAD_SET_TAG = 17
    @staticmethod
    def EVP_CipherFinal_ex():
        'int EVP_CipherFinal_ex(EVP_CIPHER_CTX *, unsigned char *, int *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_CipherInit_ex():
        'int EVP_CipherInit_ex(EVP_CIPHER_CTX *, EVP_CIPHER *, ENGINE *, unsigned char *, unsigned char *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_CipherUpdate():
        'int EVP_CipherUpdate(EVP_CIPHER_CTX *, unsigned char *, int *, unsigned char *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_DecryptFinal_ex():
        'int EVP_DecryptFinal_ex(EVP_CIPHER_CTX *, unsigned char *, int *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_DecryptInit_ex():
        'int EVP_DecryptInit_ex(EVP_CIPHER_CTX *, EVP_CIPHER *, ENGINE *, unsigned char *, unsigned char *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_DecryptUpdate():
        'int EVP_DecryptUpdate(EVP_CIPHER_CTX *, unsigned char *, int *, unsigned char *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_DigestFinal_ex():
        'int EVP_DigestFinal_ex(EVP_MD_CTX *, unsigned char *, unsigned int *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_DigestInit_ex():
        'int EVP_DigestInit_ex(EVP_MD_CTX *, EVP_MD *, ENGINE *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_DigestUpdate():
        'int EVP_DigestUpdate(EVP_MD_CTX *, void *, size_t);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_EncryptFinal_ex():
        'int EVP_EncryptFinal_ex(EVP_CIPHER_CTX *, unsigned char *, int *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_EncryptInit_ex():
        'int EVP_EncryptInit_ex(EVP_CIPHER_CTX *, EVP_CIPHER *, ENGINE *, unsigned char *, unsigned char *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_EncryptUpdate():
        'int EVP_EncryptUpdate(EVP_CIPHER_CTX *, unsigned char *, int *, unsigned char *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    EVP_F_AES_INIT_KEY = 133
    EVP_F_CAMELLIA_INIT_KEY = 159
    EVP_F_EVP_CIPHERINIT_EX = 123
    EVP_F_EVP_CIPHER_CTX_CTRL = 124
    EVP_F_EVP_CIPHER_CTX_SET_KEY_LENGTH = 122
    EVP_F_EVP_DECRYPTFINAL_EX = 101
    EVP_F_EVP_DIGESTINIT_EX = 128
    EVP_F_EVP_ENCRYPTFINAL_EX = 127
    EVP_F_EVP_MD_CTX_COPY_EX = 110
    EVP_F_EVP_OPENINIT = 102
    EVP_F_EVP_PBE_ALG_ADD = 115
    EVP_F_EVP_PBE_CIPHERINIT = 116
    EVP_F_EVP_PKCS82PKEY = 111
    EVP_F_EVP_PKEY_COPY_PARAMETERS = 103
    EVP_F_EVP_PKEY_DECRYPT = 104
    EVP_F_EVP_PKEY_ENCRYPT = 105
    EVP_F_EVP_PKEY_NEW = 106
    EVP_F_EVP_SIGNFINAL = 107
    EVP_F_EVP_VERIFYFINAL = 108
    EVP_F_PKCS5_PBE_KEYIVGEN = 117
    EVP_F_PKCS5_V2_PBE_KEYIVGEN = 118
    EVP_F_RC2_MAGIC_TO_METH = 109
    EVP_F_RC5_CTRL = 125
    EVP_MAX_MD_SIZE = 64
    @staticmethod
    def EVP_MD_CTX_block_size():
        'int EVP_MD_CTX_block_size(EVP_MD_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_MD_CTX_copy_ex():
        'int EVP_MD_CTX_copy_ex(EVP_MD_CTX *, EVP_MD_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_MD_CTX_md():
        'EVP_MD *EVP_MD_CTX_md(EVP_MD_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_MD_size():
        'int EVP_MD_size(EVP_MD *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_PBE_scrypt():
        'int EVP_PBE_scrypt(char *, size_t, unsigned char *, size_t, uint64_t, uint64_t, uint64_t, uint64_t, unsigned char *, size_t);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_PKCS82PKEY():
        'EVP_PKEY *EVP_PKCS82PKEY(PKCS8_PRIV_KEY_INFO *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_PKEY_CTX_dup():
        'EVP_PKEY_CTX *EVP_PKEY_CTX_dup(EVP_PKEY_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_PKEY_CTX_free():
        'void EVP_PKEY_CTX_free(EVP_PKEY_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_PKEY_CTX_new():
        'EVP_PKEY_CTX *EVP_PKEY_CTX_new(EVP_PKEY *, ENGINE *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_PKEY_CTX_new_id():
        'EVP_PKEY_CTX *EVP_PKEY_CTX_new_id(int, ENGINE *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_PKEY_CTX_set0_rsa_oaep_label():
        'int EVP_PKEY_CTX_set0_rsa_oaep_label(EVP_PKEY_CTX *, unsigned char *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_PKEY_CTX_set_rsa_mgf1_md():
        'int EVP_PKEY_CTX_set_rsa_mgf1_md(EVP_PKEY_CTX *, EVP_MD *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_PKEY_CTX_set_rsa_oaep_md():
        'int EVP_PKEY_CTX_set_rsa_oaep_md(EVP_PKEY_CTX *, EVP_MD *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_PKEY_CTX_set_rsa_padding():
        'int EVP_PKEY_CTX_set_rsa_padding(EVP_PKEY_CTX *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_PKEY_CTX_set_rsa_pss_saltlen():
        'int EVP_PKEY_CTX_set_rsa_pss_saltlen(EVP_PKEY_CTX *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_PKEY_CTX_set_signature_md():
        'int EVP_PKEY_CTX_set_signature_md(EVP_PKEY_CTX *, EVP_MD *);\n\nCFFI C function from _openssl.lib'
        pass
    
    EVP_PKEY_DH = 28
    EVP_PKEY_DHX = 920
    EVP_PKEY_DSA = 116
    EVP_PKEY_EC = 408
    EVP_PKEY_RSA = 6
    @staticmethod
    def EVP_PKEY_add1_attr():
        'int EVP_PKEY_add1_attr(EVP_PKEY *, X509_ATTRIBUTE *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_PKEY_add1_attr_by_NID():
        'int EVP_PKEY_add1_attr_by_NID(EVP_PKEY *, int, int, unsigned char *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_PKEY_add1_attr_by_OBJ():
        'int EVP_PKEY_add1_attr_by_OBJ(EVP_PKEY *, ASN1_OBJECT *, int, unsigned char *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_PKEY_add1_attr_by_txt():
        'int EVP_PKEY_add1_attr_by_txt(EVP_PKEY *, char *, int, unsigned char *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_PKEY_assign_DSA():
        'int EVP_PKEY_assign_DSA(EVP_PKEY *, DSA *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_PKEY_assign_EC_KEY():
        'int EVP_PKEY_assign_EC_KEY(EVP_PKEY *, EC_KEY *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_PKEY_assign_RSA():
        'int EVP_PKEY_assign_RSA(EVP_PKEY *, RSA *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_PKEY_bits():
        'int EVP_PKEY_bits(EVP_PKEY *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_PKEY_cmp():
        'int EVP_PKEY_cmp(EVP_PKEY *, EVP_PKEY *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_PKEY_decrypt():
        'int EVP_PKEY_decrypt(EVP_PKEY_CTX *, unsigned char *, size_t *, unsigned char *, size_t);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_PKEY_decrypt_init():
        'int EVP_PKEY_decrypt_init(EVP_PKEY_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_PKEY_delete_attr():
        'X509_ATTRIBUTE *EVP_PKEY_delete_attr(EVP_PKEY *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_PKEY_derive():
        'int EVP_PKEY_derive(EVP_PKEY_CTX *, unsigned char *, size_t *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_PKEY_derive_init():
        'int EVP_PKEY_derive_init(EVP_PKEY_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_PKEY_derive_set_peer():
        'int EVP_PKEY_derive_set_peer(EVP_PKEY_CTX *, EVP_PKEY *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_PKEY_encrypt():
        'int EVP_PKEY_encrypt(EVP_PKEY_CTX *, unsigned char *, size_t *, unsigned char *, size_t);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_PKEY_encrypt_init():
        'int EVP_PKEY_encrypt_init(EVP_PKEY_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_PKEY_free():
        'void EVP_PKEY_free(EVP_PKEY *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_PKEY_get1_DH():
        'DH *EVP_PKEY_get1_DH(EVP_PKEY *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_PKEY_get1_DSA():
        'DSA *EVP_PKEY_get1_DSA(EVP_PKEY *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_PKEY_get1_EC_KEY():
        'EC_KEY *EVP_PKEY_get1_EC_KEY(EVP_PKEY *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_PKEY_get1_RSA():
        'RSA *EVP_PKEY_get1_RSA(EVP_PKEY *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_PKEY_get1_tls_encodedpoint():
        'size_t EVP_PKEY_get1_tls_encodedpoint(EVP_PKEY *, unsigned char * *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_PKEY_get_attr():
        'X509_ATTRIBUTE *EVP_PKEY_get_attr(EVP_PKEY *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_PKEY_get_attr_by_NID():
        'int EVP_PKEY_get_attr_by_NID(EVP_PKEY *, int, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_PKEY_get_attr_count():
        'int EVP_PKEY_get_attr_count(EVP_PKEY *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_PKEY_id():
        'int EVP_PKEY_id(EVP_PKEY *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_PKEY_keygen():
        'int EVP_PKEY_keygen(EVP_PKEY_CTX *, EVP_PKEY * *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_PKEY_keygen_init():
        'int EVP_PKEY_keygen_init(EVP_PKEY_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_PKEY_new():
        'EVP_PKEY *EVP_PKEY_new();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_PKEY_set1_DH():
        'int EVP_PKEY_set1_DH(EVP_PKEY *, DH *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_PKEY_set1_DSA():
        'int EVP_PKEY_set1_DSA(EVP_PKEY *, DSA *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_PKEY_set1_EC_KEY():
        'int EVP_PKEY_set1_EC_KEY(EVP_PKEY *, EC_KEY *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_PKEY_set1_RSA():
        'int EVP_PKEY_set1_RSA(EVP_PKEY *, RSA *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_PKEY_set1_tls_encodedpoint():
        'int EVP_PKEY_set1_tls_encodedpoint(EVP_PKEY *, unsigned char *, size_t);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_PKEY_set_type():
        'int EVP_PKEY_set_type(EVP_PKEY *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_PKEY_sign():
        'int EVP_PKEY_sign(EVP_PKEY_CTX *, unsigned char *, size_t *, unsigned char *, size_t);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_PKEY_sign_init():
        'int EVP_PKEY_sign_init(EVP_PKEY_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_PKEY_size():
        'int EVP_PKEY_size(EVP_PKEY *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_PKEY_type():
        'int EVP_PKEY_type(int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_PKEY_verify():
        'int EVP_PKEY_verify(EVP_PKEY_CTX *, unsigned char *, size_t, unsigned char *, size_t);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_PKEY_verify_init():
        'int EVP_PKEY_verify_init(EVP_PKEY_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    EVP_R_AES_KEY_SETUP_FAILED = 143
    EVP_R_BAD_DECRYPT = 100
    EVP_R_CAMELLIA_KEY_SETUP_FAILED = 157
    EVP_R_CIPHER_PARAMETER_ERROR = 122
    EVP_R_CTRL_NOT_IMPLEMENTED = 132
    EVP_R_CTRL_OPERATION_NOT_IMPLEMENTED = 133
    EVP_R_DATA_NOT_MULTIPLE_OF_BLOCK_LENGTH = 138
    EVP_R_DECODE_ERROR = 114
    EVP_R_DIFFERENT_KEY_TYPES = 101
    EVP_R_INITIALIZATION_ERROR = 134
    EVP_R_INPUT_NOT_INITIALIZED = 111
    EVP_R_INVALID_KEY_LENGTH = 130
    EVP_R_KEYGEN_FAILURE = 120
    EVP_R_MISSING_PARAMETERS = 103
    EVP_R_NO_CIPHER_SET = 131
    EVP_R_NO_DIGEST_SET = 139
    EVP_R_PUBLIC_KEY_NOT_RSA = 106
    EVP_R_UNKNOWN_PBE_ALGORITHM = 121
    EVP_R_UNSUPPORTED_CIPHER = 107
    EVP_R_UNSUPPORTED_KEYLENGTH = 123
    EVP_R_UNSUPPORTED_KEY_DERIVATION_FUNCTION = 124
    EVP_R_UNSUPPORTED_PRIVATE_KEY_ALGORITHM = 118
    EVP_R_UNSUPPORTED_SALT_TYPE = 126
    EVP_R_WRONG_FINAL_BLOCK_LENGTH = 109
    @staticmethod
    def EVP_SignFinal():
        'int EVP_SignFinal(EVP_MD_CTX *, unsigned char *, unsigned int *, EVP_PKEY *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_SignInit():
        'int EVP_SignInit(EVP_MD_CTX *, EVP_MD *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_SignUpdate():
        'int EVP_SignUpdate(EVP_MD_CTX *, void *, size_t);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_VerifyFinal():
        'int EVP_VerifyFinal(EVP_MD_CTX *, unsigned char *, unsigned int, EVP_PKEY *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_VerifyInit():
        'int EVP_VerifyInit(EVP_MD_CTX *, EVP_MD *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_VerifyUpdate():
        'int EVP_VerifyUpdate(EVP_MD_CTX *, void *, size_t);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_get_cipherbyname():
        'EVP_CIPHER *EVP_get_cipherbyname(char *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_get_digestbyname():
        'EVP_MD *EVP_get_digestbyname(char *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_md5():
        'EVP_MD *EVP_md5();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_ripemd160():
        'EVP_MD *EVP_ripemd160();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_sha1():
        'EVP_MD *EVP_sha1();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_sha224():
        'EVP_MD *EVP_sha224();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_sha256():
        'EVP_MD *EVP_sha256();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_sha384():
        'EVP_MD *EVP_sha384();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_sha512():
        'EVP_MD *EVP_sha512();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def FIPS_mode():
        'int FIPS_mode();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def FIPS_mode_set():
        'int FIPS_mode_set(int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def GENERAL_NAMES_free():
        'void GENERAL_NAMES_free(struct stack_st_GENERAL_NAME *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def GENERAL_NAMES_new():
        'struct stack_st_GENERAL_NAME *GENERAL_NAMES_new();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def GENERAL_NAME_free():
        'void GENERAL_NAME_free(GENERAL_NAME *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def GENERAL_NAME_new():
        'GENERAL_NAME *GENERAL_NAME_new();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def GENERAL_NAME_print():
        'int GENERAL_NAME_print(struct bio_st *, GENERAL_NAME *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def GENERAL_SUBTREE_new():
        'GENERAL_SUBTREE *GENERAL_SUBTREE_new();\n\nCFFI C function from _openssl.lib'
        pass
    
    GEN_DIRNAME = 4
    GEN_DNS = 2
    GEN_EDIPARTY = 5
    GEN_EMAIL = 1
    GEN_IPADD = 7
    GEN_OTHERNAME = 0
    GEN_RID = 8
    GEN_URI = 6
    GEN_X400 = 3
    @staticmethod
    def HMAC_CTX_copy():
        'int HMAC_CTX_copy(HMAC_CTX *, HMAC_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def HMAC_Final():
        'int HMAC_Final(HMAC_CTX *, unsigned char *, unsigned int *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def HMAC_Init_ex():
        'int HMAC_Init_ex(HMAC_CTX *, void *, int, EVP_MD *, ENGINE *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def HMAC_Update():
        'int HMAC_Update(HMAC_CTX *, unsigned char *, size_t);\n\nCFFI C function from _openssl.lib'
        pass
    
    MBSTRING_ASC = 4097
    MBSTRING_BMP = 4098
    MBSTRING_FLAG = 4096
    MBSTRING_UNIV = 4100
    MBSTRING_UTF8 = 4096
    @staticmethod
    def NAME_CONSTRAINTS_free():
        'void NAME_CONSTRAINTS_free(NAME_CONSTRAINTS *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def NAME_CONSTRAINTS_new():
        'NAME_CONSTRAINTS *NAME_CONSTRAINTS_new();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def NETSCAPE_SPKI_b64_decode():
        'NETSCAPE_SPKI *NETSCAPE_SPKI_b64_decode(char *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def NETSCAPE_SPKI_b64_encode():
        'char *NETSCAPE_SPKI_b64_encode(NETSCAPE_SPKI *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def NETSCAPE_SPKI_free():
        'void NETSCAPE_SPKI_free(NETSCAPE_SPKI *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def NETSCAPE_SPKI_get_pubkey():
        'EVP_PKEY *NETSCAPE_SPKI_get_pubkey(NETSCAPE_SPKI *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def NETSCAPE_SPKI_new():
        'NETSCAPE_SPKI *NETSCAPE_SPKI_new();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def NETSCAPE_SPKI_set_pubkey():
        'int NETSCAPE_SPKI_set_pubkey(NETSCAPE_SPKI *, EVP_PKEY *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def NETSCAPE_SPKI_sign():
        'int NETSCAPE_SPKI_sign(NETSCAPE_SPKI *, EVP_PKEY *, EVP_MD *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def NETSCAPE_SPKI_verify():
        'int NETSCAPE_SPKI_verify(NETSCAPE_SPKI *, EVP_PKEY *);\n\nCFFI C function from _openssl.lib'
        pass
    
    NID_X25519 = 1034
    NID_X9_62_c2onb191v4 = 691
    NID_X9_62_c2onb191v5 = 692
    NID_X9_62_c2onb239v4 = 697
    NID_X9_62_c2onb239v5 = 698
    NID_X9_62_c2pnb163v1 = 684
    NID_X9_62_c2pnb163v2 = 685
    NID_X9_62_c2pnb163v3 = 686
    NID_X9_62_c2pnb176v1 = 687
    NID_X9_62_c2pnb208w1 = 693
    NID_X9_62_c2pnb272w1 = 699
    NID_X9_62_c2pnb304w1 = 700
    NID_X9_62_c2pnb368w1 = 702
    NID_X9_62_c2tnb191v1 = 688
    NID_X9_62_c2tnb191v2 = 689
    NID_X9_62_c2tnb191v3 = 690
    NID_X9_62_c2tnb239v1 = 694
    NID_X9_62_c2tnb239v2 = 695
    NID_X9_62_c2tnb239v3 = 696
    NID_X9_62_c2tnb359v1 = 701
    NID_X9_62_c2tnb431r1 = 703
    NID_X9_62_prime192v1 = 409
    NID_X9_62_prime192v2 = 410
    NID_X9_62_prime192v3 = 411
    NID_X9_62_prime239v1 = 412
    NID_X9_62_prime239v2 = 413
    NID_X9_62_prime239v3 = 414
    NID_X9_62_prime256v1 = 415
    NID_ad_OCSP = 178
    NID_ad_ca_issuers = 179
    NID_any_policy = 746
    NID_authority_key_identifier = 90
    NID_basic_constraints = 87
    NID_certificate_issuer = 771
    NID_certificate_policies = 89
    NID_commonName = 13
    NID_countryName = 14
    NID_crl_distribution_points = 103
    NID_crl_number = 88
    NID_crl_reason = 141
    NID_delta_crl = 140
    NID_dnQualifier = 174
    NID_domainComponent = 391
    NID_dsa = 116
    NID_dsaWithSHA = 66
    NID_dsaWithSHA1 = 113
    NID_ecdsa_with_SHA1 = 416
    NID_ecdsa_with_SHA224 = 793
    NID_ecdsa_with_SHA256 = 794
    NID_ecdsa_with_SHA384 = 795
    NID_ecdsa_with_SHA512 = 796
    NID_ext_key_usage = 126
    NID_generationQualifier = 509
    NID_givenName = 99
    NID_info_access = 177
    NID_inhibit_any_policy = 748
    NID_invalidity_date = 142
    NID_ipsec3 = 749
    NID_ipsec4 = 750
    NID_issuer_alt_name = 86
    NID_issuing_distribution_point = 770
    NID_key_usage = 83
    NID_localityName = 15
    NID_md2 = 3
    NID_md4 = 257
    NID_md5 = 4
    NID_mdc2 = 95
    NID_name_constraints = 666
    NID_no_rev_avail = 403
    NID_organizationName = 17
    NID_organizationalUnitName = 18
    NID_pbe_WithSHA1And3_Key_TripleDES_CBC = 146
    NID_pkcs9_emailAddress = 48
    NID_policy_constraints = 401
    NID_policy_mappings = 747
    NID_private_key_usage_period = 84
    NID_pseudonym = 510
    NID_ripemd160 = 117
    NID_secp112r1 = 704
    NID_secp112r2 = 705
    NID_secp128r1 = 706
    NID_secp128r2 = 707
    NID_secp160k1 = 708
    NID_secp160r1 = 709
    NID_secp160r2 = 710
    NID_secp192k1 = 711
    NID_secp224k1 = 712
    NID_secp224r1 = 713
    NID_secp256k1 = 714
    NID_secp384r1 = 715
    NID_secp521r1 = 716
    NID_sect113r1 = 717
    NID_sect113r2 = 718
    NID_sect131r1 = 719
    NID_sect131r2 = 720
    NID_sect163k1 = 721
    NID_sect163r1 = 722
    NID_sect163r2 = 723
    NID_sect193r1 = 724
    NID_sect193r2 = 725
    NID_sect233k1 = 726
    NID_sect233r1 = 727
    NID_sect239k1 = 728
    NID_sect283k1 = 729
    NID_sect283r1 = 730
    NID_sect409k1 = 731
    NID_sect409r1 = 732
    NID_sect571k1 = 733
    NID_sect571r1 = 734
    NID_serialNumber = 105
    NID_sha = 41
    NID_sha1 = 64
    NID_sha224 = 675
    NID_sha256 = 672
    NID_sha384 = 673
    NID_sha512 = 674
    NID_stateOrProvinceName = 16
    NID_subject_alt_name = 85
    NID_subject_key_identifier = 82
    NID_surname = 100
    NID_target_information = 402
    NID_title = 106
    NID_undef = 0
    NID_wap_wsg_idm_ecid_wtls1 = 735
    NID_wap_wsg_idm_ecid_wtls10 = 743
    NID_wap_wsg_idm_ecid_wtls11 = 744
    NID_wap_wsg_idm_ecid_wtls12 = 745
    NID_wap_wsg_idm_ecid_wtls3 = 736
    NID_wap_wsg_idm_ecid_wtls4 = 737
    NID_wap_wsg_idm_ecid_wtls5 = 738
    NID_wap_wsg_idm_ecid_wtls6 = 739
    NID_wap_wsg_idm_ecid_wtls7 = 740
    NID_wap_wsg_idm_ecid_wtls8 = 741
    NID_wap_wsg_idm_ecid_wtls9 = 742
    @staticmethod
    def NOTICEREF_free():
        'void NOTICEREF_free(NOTICEREF *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def NOTICEREF_new():
        'NOTICEREF *NOTICEREF_new();\n\nCFFI C function from _openssl.lib'
        pass
    
    OBJ_NAME_TYPE_MD_METH = 1
    @staticmethod
    def OBJ_NAME_do_all():
        'void OBJ_NAME_do_all(int, void(*)(OBJ_NAME *, void *), void *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def OBJ_cleanup():
        'void OBJ_cleanup();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def OBJ_cmp():
        'int OBJ_cmp(ASN1_OBJECT *, ASN1_OBJECT *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def OBJ_create():
        'int OBJ_create(char *, char *, char *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def OBJ_dup():
        'ASN1_OBJECT *OBJ_dup(ASN1_OBJECT *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def OBJ_ln2nid():
        'int OBJ_ln2nid(char *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def OBJ_nid2ln():
        'char *OBJ_nid2ln(int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def OBJ_nid2obj():
        'ASN1_OBJECT *OBJ_nid2obj(int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def OBJ_nid2sn():
        'char *OBJ_nid2sn(int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def OBJ_obj2nid():
        'int OBJ_obj2nid(ASN1_OBJECT *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def OBJ_obj2txt():
        'int OBJ_obj2txt(char *, int, ASN1_OBJECT *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def OBJ_sn2nid():
        'int OBJ_sn2nid(char *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def OBJ_txt2nid():
        'int OBJ_txt2nid(char *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def OBJ_txt2obj():
        'ASN1_OBJECT *OBJ_txt2obj(char *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def OCSP_BASICRESP_add1_ext_i2d():
        'int OCSP_BASICRESP_add1_ext_i2d(OCSP_BASICRESP *, int, void *, int, unsigned long);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def OCSP_BASICRESP_free():
        'void OCSP_BASICRESP_free(OCSP_BASICRESP *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def OCSP_BASICRESP_get_ext():
        'X509_EXTENSION *OCSP_BASICRESP_get_ext(OCSP_BASICRESP *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def OCSP_BASICRESP_get_ext_count():
        'int OCSP_BASICRESP_get_ext_count(OCSP_BASICRESP *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def OCSP_BASICRESP_new():
        'OCSP_BASICRESP *OCSP_BASICRESP_new();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def OCSP_ONEREQ_get_ext():
        'X509_EXTENSION *OCSP_ONEREQ_get_ext(OCSP_ONEREQ *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def OCSP_ONEREQ_get_ext_count():
        'int OCSP_ONEREQ_get_ext_count(OCSP_ONEREQ *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def OCSP_REQUEST_add1_ext_i2d():
        'int OCSP_REQUEST_add1_ext_i2d(OCSP_REQUEST *, int, void *, int, unsigned long);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def OCSP_REQUEST_free():
        'void OCSP_REQUEST_free(OCSP_REQUEST *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def OCSP_REQUEST_new():
        'OCSP_REQUEST *OCSP_REQUEST_new();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def OCSP_SINGLERESP_get_ext():
        'X509_EXTENSION *OCSP_SINGLERESP_get_ext(OCSP_SINGLERESP *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def OCSP_SINGLERESP_get_ext_count():
        'int OCSP_SINGLERESP_get_ext_count(OCSP_SINGLERESP *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def OCSP_basic_add1_cert():
        'int OCSP_basic_add1_cert(OCSP_BASICRESP *, X509 *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def OCSP_basic_add1_nonce():
        'int OCSP_basic_add1_nonce(OCSP_BASICRESP *, unsigned char *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def OCSP_basic_add1_status():
        'OCSP_SINGLERESP *OCSP_basic_add1_status(OCSP_BASICRESP *, OCSP_CERTID *, int, int, struct asn1_string_st *, struct asn1_string_st *, struct asn1_string_st *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def OCSP_basic_sign():
        'int OCSP_basic_sign(OCSP_BASICRESP *, X509 *, EVP_PKEY *, EVP_MD *, Cryptography_STACK_OF_X509 *, unsigned long);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def OCSP_id_get0_info():
        'int OCSP_id_get0_info(struct asn1_string_st * *, ASN1_OBJECT * *, struct asn1_string_st * *, ASN1_INTEGER * *, OCSP_CERTID *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def OCSP_onereq_get0_id():
        'OCSP_CERTID *OCSP_onereq_get0_id(OCSP_ONEREQ *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def OCSP_request_add1_nonce():
        'int OCSP_request_add1_nonce(OCSP_REQUEST *, unsigned char *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def OCSP_request_onereq_count():
        'int OCSP_request_onereq_count(OCSP_REQUEST *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def OCSP_request_onereq_get0():
        'OCSP_ONEREQ *OCSP_request_onereq_get0(OCSP_REQUEST *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def OCSP_resp_count():
        'int OCSP_resp_count(OCSP_BASICRESP *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def OCSP_resp_get0():
        'OCSP_SINGLERESP *OCSP_resp_get0(OCSP_BASICRESP *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def OCSP_response_create():
        'OCSP_RESPONSE *OCSP_response_create(int, OCSP_BASICRESP *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def OCSP_response_get1_basic():
        'OCSP_BASICRESP *OCSP_response_get1_basic(OCSP_RESPONSE *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def OCSP_response_status():
        'int OCSP_response_status(OCSP_RESPONSE *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def OCSP_single_get0_status():
        'int OCSP_single_get0_status(OCSP_SINGLERESP *, int *, ASN1_GENERALIZEDTIME * *, ASN1_GENERALIZEDTIME * *, ASN1_GENERALIZEDTIME * *);\n\nCFFI C function from _openssl.lib'
        pass
    
    OPENSSL_BUILT_ON = 2
    OPENSSL_CFLAGS = 1
    OPENSSL_DIR = 4
    OPENSSL_EC_NAMED_CURVE = 1
    OPENSSL_NPN_NEGOTIATED = 1
    OPENSSL_PLATFORM = 3
    OPENSSL_VERSION = 0
    OPENSSL_VERSION_NUMBER = 269484159
    @staticmethod
    def OPENSSL_VERSION_TEXT():
        pass
    
    @staticmethod
    def OPENSSL_config():
        'void OPENSSL_config(char *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def OPENSSL_free():
        'void OPENSSL_free(void *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def OPENSSL_malloc():
        'void *OPENSSL_malloc(size_t);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def OPENSSL_no_config():
        'void OPENSSL_no_config();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def OTHERNAME_free():
        'void OTHERNAME_free(OTHERNAME *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def OTHERNAME_new():
        'OTHERNAME *OTHERNAME_new();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def OpenSSL_add_all_algorithms():
        'void OpenSSL_add_all_algorithms();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def OpenSSL_version():
        'char *OpenSSL_version(int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def OpenSSL_version_num():
        'unsigned long OpenSSL_version_num();\n\nCFFI C function from _openssl.lib'
        pass
    
    PEM_F_D2I_PKCS8PRIVATEKEY_BIO = 120
    PEM_F_D2I_PKCS8PRIVATEKEY_FP = 121
    PEM_F_DO_PK8PKEY = 126
    PEM_F_DO_PK8PKEY_FP = 125
    PEM_F_LOAD_IV = 101
    PEM_F_PEM_ASN1_READ = 102
    PEM_F_PEM_ASN1_READ_BIO = 103
    PEM_F_PEM_ASN1_WRITE = 104
    PEM_F_PEM_ASN1_WRITE_BIO = 105
    PEM_F_PEM_DEF_CALLBACK = 100
    PEM_F_PEM_DO_HEADER = 106
    PEM_F_PEM_GET_EVP_CIPHER_INFO = 107
    PEM_F_PEM_READ = 108
    PEM_F_PEM_READ_BIO = 109
    PEM_F_PEM_READ_BIO_PRIVATEKEY = 123
    PEM_F_PEM_READ_PRIVATEKEY = 124
    PEM_F_PEM_SIGNFINAL = 112
    PEM_F_PEM_WRITE = 113
    PEM_F_PEM_WRITE_BIO = 114
    PEM_F_PEM_X509_INFO_READ = 115
    PEM_F_PEM_X509_INFO_READ_BIO = 116
    PEM_F_PEM_X509_INFO_WRITE_BIO = 117
    PEM_R_BAD_BASE64_DECODE = 100
    PEM_R_BAD_DECRYPT = 101
    PEM_R_BAD_END_LINE = 102
    PEM_R_BAD_IV_CHARS = 103
    PEM_R_BAD_PASSWORD_READ = 104
    PEM_R_ERROR_CONVERTING_PRIVATE_KEY = 115
    PEM_R_NOT_DEK_INFO = 105
    PEM_R_NOT_ENCRYPTED = 106
    PEM_R_NOT_PROC_TYPE = 107
    PEM_R_NO_START_LINE = 108
    PEM_R_PROBLEMS_GETTING_PASSWORD = 109
    PEM_R_READ_KEY = 111
    PEM_R_SHORT_HEADER = 112
    PEM_R_UNSUPPORTED_CIPHER = 113
    PEM_R_UNSUPPORTED_ENCRYPTION = 114
    @staticmethod
    def PEM_read_bio_DHparams():
        'DH *PEM_read_bio_DHparams(struct bio_st *, DH * *, int(*)(char *, int, int, void *), void *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def PEM_read_bio_DSAPrivateKey():
        'DSA *PEM_read_bio_DSAPrivateKey(struct bio_st *, DSA * *, int(*)(char *, int, int, void *), void *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def PEM_read_bio_DSA_PUBKEY():
        'DSA *PEM_read_bio_DSA_PUBKEY(struct bio_st *, DSA * *, int(*)(char *, int, int, void *), void *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def PEM_read_bio_PKCS7():
        'PKCS7 *PEM_read_bio_PKCS7(struct bio_st *, PKCS7 * *, int(*)(char *, int, int, void *), void *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def PEM_read_bio_PUBKEY():
        'EVP_PKEY *PEM_read_bio_PUBKEY(struct bio_st *, EVP_PKEY * *, int(*)(char *, int, int, void *), void *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def PEM_read_bio_PrivateKey():
        'EVP_PKEY *PEM_read_bio_PrivateKey(struct bio_st *, EVP_PKEY * *, int(*)(char *, int, int, void *), void *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def PEM_read_bio_RSAPrivateKey():
        'RSA *PEM_read_bio_RSAPrivateKey(struct bio_st *, RSA * *, int(*)(char *, int, int, void *), void *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def PEM_read_bio_RSAPublicKey():
        'RSA *PEM_read_bio_RSAPublicKey(struct bio_st *, RSA * *, int(*)(char *, int, int, void *), void *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def PEM_read_bio_X509():
        'X509 *PEM_read_bio_X509(struct bio_st *, X509 * *, int(*)(char *, int, int, void *), void *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def PEM_read_bio_X509_AUX():
        'X509 *PEM_read_bio_X509_AUX(struct bio_st *, X509 * *, int(*)(char *, int, int, void *), void *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def PEM_read_bio_X509_CRL():
        'X509_CRL *PEM_read_bio_X509_CRL(struct bio_st *, X509_CRL * *, int(*)(char *, int, int, void *), void *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def PEM_read_bio_X509_REQ():
        'X509_REQ *PEM_read_bio_X509_REQ(struct bio_st *, X509_REQ * *, int(*)(char *, int, int, void *), void *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def PEM_write_bio_CMS_stream():
        'int PEM_write_bio_CMS_stream(struct bio_st *, CMS_ContentInfo *, struct bio_st *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def PEM_write_bio_DHparams():
        'int PEM_write_bio_DHparams(struct bio_st *, DH *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def PEM_write_bio_DHxparams():
        'int PEM_write_bio_DHxparams(struct bio_st *, DH *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def PEM_write_bio_DSAPrivateKey():
        'int PEM_write_bio_DSAPrivateKey(struct bio_st *, DSA *, EVP_CIPHER *, unsigned char *, int, int(*)(char *, int, int, void *), void *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def PEM_write_bio_DSA_PUBKEY():
        'int PEM_write_bio_DSA_PUBKEY(struct bio_st *, DSA *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def PEM_write_bio_ECPrivateKey():
        'int PEM_write_bio_ECPrivateKey(struct bio_st *, EC_KEY *, EVP_CIPHER *, unsigned char *, int, int(*)(char *, int, int, void *), void *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def PEM_write_bio_PKCS7():
        'int PEM_write_bio_PKCS7(struct bio_st *, PKCS7 *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def PEM_write_bio_PKCS8PrivateKey():
        'int PEM_write_bio_PKCS8PrivateKey(struct bio_st *, EVP_PKEY *, EVP_CIPHER *, char *, int, int(*)(char *, int, int, void *), void *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def PEM_write_bio_PKCS8PrivateKey_nid():
        'int PEM_write_bio_PKCS8PrivateKey_nid(struct bio_st *, EVP_PKEY *, int, char *, int, int(*)(char *, int, int, void *), void *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def PEM_write_bio_PUBKEY():
        'int PEM_write_bio_PUBKEY(struct bio_st *, EVP_PKEY *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def PEM_write_bio_PrivateKey():
        'int PEM_write_bio_PrivateKey(struct bio_st *, EVP_PKEY *, EVP_CIPHER *, unsigned char *, int, int(*)(char *, int, int, void *), void *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def PEM_write_bio_RSAPrivateKey():
        'int PEM_write_bio_RSAPrivateKey(struct bio_st *, RSA *, EVP_CIPHER *, unsigned char *, int, int(*)(char *, int, int, void *), void *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def PEM_write_bio_RSAPublicKey():
        'int PEM_write_bio_RSAPublicKey(struct bio_st *, RSA *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def PEM_write_bio_X509():
        'int PEM_write_bio_X509(struct bio_st *, X509 *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def PEM_write_bio_X509_CRL():
        'int PEM_write_bio_X509_CRL(struct bio_st *, X509_CRL *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def PEM_write_bio_X509_REQ():
        'int PEM_write_bio_X509_REQ(struct bio_st *, X509_REQ *);\n\nCFFI C function from _openssl.lib'
        pass
    
    PKCS12_F_PKCS12_PBE_CRYPT = 119
    PKCS12_R_PKCS12_CIPHERFINAL_ERROR = 116
    @staticmethod
    def PKCS12_create():
        'PKCS12 *PKCS12_create(char *, char *, EVP_PKEY *, X509 *, Cryptography_STACK_OF_X509 *, int, int, int, int, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def PKCS12_free():
        'void PKCS12_free(PKCS12 *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def PKCS12_parse():
        'int PKCS12_parse(PKCS12 *, char *, EVP_PKEY * *, X509 * *, Cryptography_STACK_OF_X509 * *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def PKCS5_PBKDF2_HMAC():
        'int PKCS5_PBKDF2_HMAC(char *, int, unsigned char *, int, int, EVP_MD *, int, unsigned char *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def PKCS5_PBKDF2_HMAC_SHA1():
        'int PKCS5_PBKDF2_HMAC_SHA1(char *, int, unsigned char *, int, int, int, unsigned char *);\n\nCFFI C function from _openssl.lib'
        pass
    
    PKCS7_BINARY = 128
    PKCS7_DETACHED = 64
    PKCS7_NOATTR = 256
    PKCS7_NOCERTS = 2
    PKCS7_NOCHAIN = 8
    PKCS7_NOINTERN = 16
    PKCS7_NOSIGS = 4
    PKCS7_NOSMIMECAP = 512
    PKCS7_NOVERIFY = 32
    PKCS7_STREAM = 4096
    PKCS7_TEXT = 1
    @staticmethod
    def PKCS7_dataInit():
        'struct bio_st *PKCS7_dataInit(PKCS7 *, struct bio_st *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def PKCS7_decrypt():
        'int PKCS7_decrypt(PKCS7 *, EVP_PKEY *, X509 *, struct bio_st *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def PKCS7_encrypt():
        'PKCS7 *PKCS7_encrypt(Cryptography_STACK_OF_X509 *, struct bio_st *, EVP_CIPHER *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def PKCS7_free():
        'void PKCS7_free(PKCS7 *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def PKCS7_get0_signers():
        'Cryptography_STACK_OF_X509 *PKCS7_get0_signers(PKCS7 *, Cryptography_STACK_OF_X509 *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def PKCS7_sign():
        'PKCS7 *PKCS7_sign(X509 *, EVP_PKEY *, Cryptography_STACK_OF_X509 *, struct bio_st *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def PKCS7_type_is_data():
        'int PKCS7_type_is_data(PKCS7 *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def PKCS7_type_is_digest():
        'int PKCS7_type_is_digest(PKCS7 *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def PKCS7_type_is_encrypted():
        'int PKCS7_type_is_encrypted(PKCS7 *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def PKCS7_type_is_enveloped():
        'int PKCS7_type_is_enveloped(PKCS7 *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def PKCS7_type_is_signed():
        'int PKCS7_type_is_signed(PKCS7 *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def PKCS7_type_is_signedAndEnveloped():
        'int PKCS7_type_is_signedAndEnveloped(PKCS7 *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def PKCS7_verify():
        'int PKCS7_verify(PKCS7 *, Cryptography_STACK_OF_X509 *, X509_STORE *, struct bio_st *, struct bio_st *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def PKCS8_PRIV_KEY_INFO_free():
        'void PKCS8_PRIV_KEY_INFO_free(PKCS8_PRIV_KEY_INFO *);\n\nCFFI C function from _openssl.lib'
        pass
    
    POINT_CONVERSION_COMPRESSED = 2
    POINT_CONVERSION_HYBRID = 6
    POINT_CONVERSION_UNCOMPRESSED = 4
    @staticmethod
    def POLICYINFO_free():
        'void POLICYINFO_free(POLICYINFO *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def POLICYINFO_new():
        'POLICYINFO *POLICYINFO_new();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def POLICYQUALINFO_free():
        'void POLICYQUALINFO_free(POLICYQUALINFO *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def POLICYQUALINFO_new():
        'POLICYQUALINFO *POLICYQUALINFO_new();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def POLICY_CONSTRAINTS_free():
        'void POLICY_CONSTRAINTS_free(POLICY_CONSTRAINTS *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def POLICY_CONSTRAINTS_new():
        'POLICY_CONSTRAINTS *POLICY_CONSTRAINTS_new();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def RAND_add():
        'void RAND_add(void *, int, double);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def RAND_bytes():
        'int RAND_bytes(unsigned char *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def RAND_cleanup():
        'void RAND_cleanup();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def RAND_file_name():
        'char *RAND_file_name(char *, size_t);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def RAND_load_file():
        'int RAND_load_file(char *, long);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def RAND_seed():
        'void RAND_seed(void *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def RAND_status():
        'int RAND_status();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def RAND_write_file():
        'int RAND_write_file(char *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def RSAPublicKey_dup():
        'RSA *RSAPublicKey_dup(RSA *);\n\nCFFI C function from _openssl.lib'
        pass
    
    RSA_F4 = 65537
    RSA_F_RSA_SIGN = 117
    RSA_NO_PADDING = 3
    RSA_PKCS1_OAEP_PADDING = 4
    RSA_PKCS1_PADDING = 1
    RSA_PKCS1_PSS_PADDING = 6
    RSA_R_BLOCK_TYPE_IS_NOT_01 = 106
    RSA_R_BLOCK_TYPE_IS_NOT_02 = 107
    RSA_R_DATA_TOO_LARGE_FOR_KEY_SIZE = 110
    RSA_R_DATA_TOO_LARGE_FOR_MODULUS = 132
    RSA_R_DIGEST_TOO_BIG_FOR_RSA_KEY = 112
    RSA_R_OAEP_DECODING_ERROR = 121
    RSA_R_PKCS_DECODING_ERROR = 159
    RSA_SSLV23_PADDING = 2
    RSA_X931_PADDING = 5
    @staticmethod
    def RSA_blinding_off():
        'void RSA_blinding_off(RSA *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def RSA_blinding_on():
        'int RSA_blinding_on(RSA *, BN_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def RSA_check_key():
        'int RSA_check_key(RSA *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def RSA_free():
        'void RSA_free(RSA *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def RSA_generate_key_ex():
        'int RSA_generate_key_ex(RSA *, int, BIGNUM *, BN_GENCB *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def RSA_get0_crt_params():
        'void RSA_get0_crt_params(RSA *, BIGNUM * *, BIGNUM * *, BIGNUM * *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def RSA_get0_factors():
        'void RSA_get0_factors(RSA *, BIGNUM * *, BIGNUM * *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def RSA_get0_key():
        'void RSA_get0_key(RSA *, BIGNUM * *, BIGNUM * *, BIGNUM * *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def RSA_new():
        'RSA *RSA_new();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def RSA_padding_add_PKCS1_OAEP():
        'int RSA_padding_add_PKCS1_OAEP(unsigned char *, int, unsigned char *, int, unsigned char *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def RSA_padding_add_PKCS1_PSS():
        'int RSA_padding_add_PKCS1_PSS(RSA *, unsigned char *, unsigned char *, EVP_MD *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def RSA_padding_check_PKCS1_OAEP():
        'int RSA_padding_check_PKCS1_OAEP(unsigned char *, int, unsigned char *, int, int, unsigned char *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def RSA_print():
        'int RSA_print(struct bio_st *, RSA *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def RSA_private_decrypt():
        'int RSA_private_decrypt(int, unsigned char *, unsigned char *, RSA *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def RSA_private_encrypt():
        'int RSA_private_encrypt(int, unsigned char *, unsigned char *, RSA *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def RSA_public_decrypt():
        'int RSA_public_decrypt(int, unsigned char *, unsigned char *, RSA *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def RSA_public_encrypt():
        'int RSA_public_encrypt(int, unsigned char *, unsigned char *, RSA *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def RSA_set0_crt_params():
        'int RSA_set0_crt_params(RSA *, BIGNUM *, BIGNUM *, BIGNUM *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def RSA_set0_factors():
        'int RSA_set0_factors(RSA *, BIGNUM *, BIGNUM *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def RSA_set0_key():
        'int RSA_set0_key(RSA *, BIGNUM *, BIGNUM *, BIGNUM *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def RSA_size():
        'int RSA_size(RSA *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def RSA_verify_PKCS1_PSS():
        'int RSA_verify_PKCS1_PSS(RSA *, unsigned char *, EVP_MD *, unsigned char *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SCT_LIST_free():
        'void SCT_LIST_free(Cryptography_STACK_OF_SCT *);\n\nCFFI C function from _openssl.lib'
        pass
    
    SCT_SOURCE_OCSP_STAPLED_RESPONSE = 3
    SCT_SOURCE_TLS_EXTENSION = 1
    SCT_SOURCE_UNKNOWN = 0
    SCT_SOURCE_X509V3_EXTENSION = 2
    SCT_VERSION_NOT_SET = -1
    SCT_VERSION_V1 = 0
    @staticmethod
    def SCT_get0_log_id():
        'size_t SCT_get0_log_id(SCT *, unsigned char * *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SCT_get_log_entry_type():
        'ct_log_entry_type_t SCT_get_log_entry_type(SCT *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SCT_get_timestamp():
        'uint64_t SCT_get_timestamp(SCT *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SCT_get_version():
        'sct_version_t SCT_get_version(SCT *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SCT_set_source():
        'int SCT_set_source(SCT *, sct_source_t);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SMIME_read_PKCS7():
        'PKCS7 *SMIME_read_PKCS7(struct bio_st *, struct bio_st * *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SMIME_write_PKCS7():
        'int SMIME_write_PKCS7(struct bio_st *, PKCS7 *, struct bio_st *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SN_X9_62_c2onb191v4():
        pass
    
    @staticmethod
    def SN_X9_62_c2onb191v5():
        pass
    
    @staticmethod
    def SN_X9_62_c2onb239v4():
        pass
    
    @staticmethod
    def SN_X9_62_c2onb239v5():
        pass
    
    @staticmethod
    def SN_X9_62_c2pnb163v1():
        pass
    
    @staticmethod
    def SN_X9_62_c2pnb163v2():
        pass
    
    @staticmethod
    def SN_X9_62_c2pnb163v3():
        pass
    
    @staticmethod
    def SN_X9_62_c2pnb176v1():
        pass
    
    @staticmethod
    def SN_X9_62_c2pnb208w1():
        pass
    
    @staticmethod
    def SN_X9_62_c2pnb272w1():
        pass
    
    @staticmethod
    def SN_X9_62_c2pnb304w1():
        pass
    
    @staticmethod
    def SN_X9_62_c2pnb368w1():
        pass
    
    @staticmethod
    def SN_X9_62_c2tnb191v1():
        pass
    
    @staticmethod
    def SN_X9_62_c2tnb191v2():
        pass
    
    @staticmethod
    def SN_X9_62_c2tnb191v3():
        pass
    
    @staticmethod
    def SN_X9_62_c2tnb239v1():
        pass
    
    @staticmethod
    def SN_X9_62_c2tnb239v2():
        pass
    
    @staticmethod
    def SN_X9_62_c2tnb239v3():
        pass
    
    @staticmethod
    def SN_X9_62_c2tnb359v1():
        pass
    
    @staticmethod
    def SN_X9_62_c2tnb431r1():
        pass
    
    @staticmethod
    def SN_X9_62_prime192v1():
        pass
    
    @staticmethod
    def SN_X9_62_prime192v2():
        pass
    
    @staticmethod
    def SN_X9_62_prime192v3():
        pass
    
    @staticmethod
    def SN_X9_62_prime239v1():
        pass
    
    @staticmethod
    def SN_X9_62_prime239v2():
        pass
    
    @staticmethod
    def SN_X9_62_prime239v3():
        pass
    
    @staticmethod
    def SN_X9_62_prime256v1():
        pass
    
    @staticmethod
    def SN_ipsec3():
        pass
    
    @staticmethod
    def SN_ipsec4():
        pass
    
    @staticmethod
    def SN_secp112r1():
        pass
    
    @staticmethod
    def SN_secp112r2():
        pass
    
    @staticmethod
    def SN_secp128r1():
        pass
    
    @staticmethod
    def SN_secp128r2():
        pass
    
    @staticmethod
    def SN_secp160k1():
        pass
    
    @staticmethod
    def SN_secp160r1():
        pass
    
    @staticmethod
    def SN_secp160r2():
        pass
    
    @staticmethod
    def SN_secp192k1():
        pass
    
    @staticmethod
    def SN_secp224k1():
        pass
    
    @staticmethod
    def SN_secp224r1():
        pass
    
    @staticmethod
    def SN_secp256k1():
        pass
    
    @staticmethod
    def SN_secp384r1():
        pass
    
    @staticmethod
    def SN_secp521r1():
        pass
    
    @staticmethod
    def SN_sect113r1():
        pass
    
    @staticmethod
    def SN_sect113r2():
        pass
    
    @staticmethod
    def SN_sect131r1():
        pass
    
    @staticmethod
    def SN_sect131r2():
        pass
    
    @staticmethod
    def SN_sect163k1():
        pass
    
    @staticmethod
    def SN_sect163r1():
        pass
    
    @staticmethod
    def SN_sect163r2():
        pass
    
    @staticmethod
    def SN_sect193r1():
        pass
    
    @staticmethod
    def SN_sect193r2():
        pass
    
    @staticmethod
    def SN_sect233k1():
        pass
    
    @staticmethod
    def SN_sect233r1():
        pass
    
    @staticmethod
    def SN_sect239k1():
        pass
    
    @staticmethod
    def SN_sect283k1():
        pass
    
    @staticmethod
    def SN_sect283r1():
        pass
    
    @staticmethod
    def SN_sect409k1():
        pass
    
    @staticmethod
    def SN_sect409r1():
        pass
    
    @staticmethod
    def SN_sect571k1():
        pass
    
    @staticmethod
    def SN_sect571r1():
        pass
    
    @staticmethod
    def SN_wap_wsg_idm_ecid_wtls1():
        pass
    
    @staticmethod
    def SN_wap_wsg_idm_ecid_wtls10():
        pass
    
    @staticmethod
    def SN_wap_wsg_idm_ecid_wtls11():
        pass
    
    @staticmethod
    def SN_wap_wsg_idm_ecid_wtls12():
        pass
    
    @staticmethod
    def SN_wap_wsg_idm_ecid_wtls3():
        pass
    
    @staticmethod
    def SN_wap_wsg_idm_ecid_wtls4():
        pass
    
    @staticmethod
    def SN_wap_wsg_idm_ecid_wtls5():
        pass
    
    @staticmethod
    def SN_wap_wsg_idm_ecid_wtls6():
        pass
    
    @staticmethod
    def SN_wap_wsg_idm_ecid_wtls7():
        pass
    
    @staticmethod
    def SN_wap_wsg_idm_ecid_wtls8():
        pass
    
    @staticmethod
    def SN_wap_wsg_idm_ecid_wtls9():
        pass
    
    SSL3_RANDOM_SIZE = 32
    SSLEAY_BUILT_ON = 2
    SSLEAY_CFLAGS = 1
    SSLEAY_DIR = 4
    SSLEAY_PLATFORM = 3
    SSLEAY_VERSION = 0
    SSL_AD_ACCESS_DENIED = 49
    SSL_AD_BAD_CERTIFICATE = 42
    SSL_AD_BAD_CERTIFICATE_HASH_VALUE = 114
    SSL_AD_BAD_CERTIFICATE_STATUS_RESPONSE = 113
    SSL_AD_BAD_RECORD_MAC = 20
    SSL_AD_CERTIFICATE_EXPIRED = 45
    SSL_AD_CERTIFICATE_REVOKED = 44
    SSL_AD_CERTIFICATE_UNKNOWN = 46
    SSL_AD_CERTIFICATE_UNOBTAINABLE = 111
    SSL_AD_CLOSE_NOTIFY = 0
    SSL_AD_DECODE_ERROR = 50
    SSL_AD_DECOMPRESSION_FAILURE = 30
    SSL_AD_DECRYPT_ERROR = 51
    SSL_AD_HANDSHAKE_FAILURE = 40
    SSL_AD_ILLEGAL_PARAMETER = 47
    SSL_AD_INSUFFICIENT_SECURITY = 71
    SSL_AD_INTERNAL_ERROR = 80
    SSL_AD_NO_RENEGOTIATION = 100
    SSL_AD_PROTOCOL_VERSION = 70
    SSL_AD_RECORD_OVERFLOW = 22
    SSL_AD_UNEXPECTED_MESSAGE = 10
    SSL_AD_UNKNOWN_CA = 48
    SSL_AD_UNKNOWN_PSK_IDENTITY = 115
    SSL_AD_UNRECOGNIZED_NAME = 112
    SSL_AD_UNSUPPORTED_CERTIFICATE = 43
    SSL_AD_UNSUPPORTED_EXTENSION = 110
    SSL_AD_USER_CANCELLED = 90
    SSL_CB_ACCEPT_EXIT = 8194
    SSL_CB_ACCEPT_LOOP = 8193
    SSL_CB_ALERT = 16384
    SSL_CB_CONNECT_EXIT = 4098
    SSL_CB_CONNECT_LOOP = 4097
    SSL_CB_EXIT = 2
    SSL_CB_HANDSHAKE_DONE = 32
    SSL_CB_HANDSHAKE_START = 16
    SSL_CB_LOOP = 1
    SSL_CB_READ = 4
    SSL_CB_READ_ALERT = 16388
    SSL_CB_WRITE = 8
    SSL_CB_WRITE_ALERT = 16392
    @staticmethod
    def SSL_CIPHER_description():
        'char *SSL_CIPHER_description(SSL_CIPHER *, char *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CIPHER_get_bits():
        'int SSL_CIPHER_get_bits(SSL_CIPHER *, int *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CIPHER_get_name():
        'char *SSL_CIPHER_get_name(SSL_CIPHER *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CIPHER_get_version():
        'char *SSL_CIPHER_get_version(SSL_CIPHER *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_COMP_get_name():
        'char *SSL_COMP_get_name(COMP_METHOD *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_add_client_CA():
        'int SSL_CTX_add_client_CA(SSL_CTX *, X509 *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_add_extra_chain_cert():
        'unsigned long SSL_CTX_add_extra_chain_cert(SSL_CTX *, X509 *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_check_private_key():
        'int SSL_CTX_check_private_key(SSL_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_clear_options():
        'unsigned long SSL_CTX_clear_options(SSL_CTX *, unsigned long);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_free():
        'void SSL_CTX_free(SSL_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_get_cert_store():
        'X509_STORE *SSL_CTX_get_cert_store(SSL_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_get_ex_data():
        'void *SSL_CTX_get_ex_data(SSL_CTX *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_get_ex_new_index():
        'int SSL_CTX_get_ex_new_index(long, void *, CRYPTO_EX_new *, CRYPTO_EX_dup *, CRYPTO_EX_free *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_get_info_callback():
        'void(*SSL_CTX_get_info_callback(SSL_CTX *))(SSL *, int, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_get_mode():
        'unsigned long SSL_CTX_get_mode(SSL_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_get_options():
        'unsigned long SSL_CTX_get_options(SSL_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_get_session_cache_mode():
        'unsigned long SSL_CTX_get_session_cache_mode(SSL_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_get_ssl_method():
        'SSL_METHOD *SSL_CTX_get_ssl_method(SSL_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_get_timeout():
        'long SSL_CTX_get_timeout(SSL_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_get_verify_callback():
        'int(*SSL_CTX_get_verify_callback(SSL_CTX *))(int, X509_STORE_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_get_verify_depth():
        'int SSL_CTX_get_verify_depth(SSL_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_get_verify_mode():
        'int SSL_CTX_get_verify_mode(SSL_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_load_verify_locations():
        'int SSL_CTX_load_verify_locations(SSL_CTX *, char *, char *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_new():
        'SSL_CTX *SSL_CTX_new(SSL_METHOD *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_sess_accept():
        'long SSL_CTX_sess_accept(SSL_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_sess_accept_good():
        'long SSL_CTX_sess_accept_good(SSL_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_sess_accept_renegotiate():
        'long SSL_CTX_sess_accept_renegotiate(SSL_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_sess_cache_full():
        'long SSL_CTX_sess_cache_full(SSL_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_sess_cb_hits():
        'long SSL_CTX_sess_cb_hits(SSL_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_sess_connect():
        'long SSL_CTX_sess_connect(SSL_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_sess_connect_good():
        'long SSL_CTX_sess_connect_good(SSL_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_sess_connect_renegotiate():
        'long SSL_CTX_sess_connect_renegotiate(SSL_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_sess_hits():
        'long SSL_CTX_sess_hits(SSL_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_sess_misses():
        'long SSL_CTX_sess_misses(SSL_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_sess_number():
        'long SSL_CTX_sess_number(SSL_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_sess_timeouts():
        'long SSL_CTX_sess_timeouts(SSL_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_set_alpn_protos():
        'int SSL_CTX_set_alpn_protos(SSL_CTX *, unsigned char *, unsigned int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_set_alpn_select_cb():
        'void SSL_CTX_set_alpn_select_cb(SSL_CTX *, int(*)(SSL *, unsigned char * *, unsigned char *, unsigned char *, unsigned int, void *), void *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_set_cert_cb():
        'void SSL_CTX_set_cert_cb(SSL_CTX *, int(*)(SSL *, void *), void *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_set_cert_store():
        'void SSL_CTX_set_cert_store(SSL_CTX *, X509_STORE *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_set_cert_verify_callback():
        'void SSL_CTX_set_cert_verify_callback(SSL_CTX *, int(*)(X509_STORE_CTX *, void *), void *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_set_cipher_list():
        'int SSL_CTX_set_cipher_list(SSL_CTX *, char *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_set_client_CA_list():
        'void SSL_CTX_set_client_CA_list(SSL_CTX *, Cryptography_STACK_OF_X509_NAME *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_set_client_cert_engine():
        'int SSL_CTX_set_client_cert_engine(SSL_CTX *, ENGINE *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_set_default_passwd_cb():
        'void SSL_CTX_set_default_passwd_cb(SSL_CTX *, int(*)(char *, int, int, void *));\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_set_default_passwd_cb_userdata():
        'void SSL_CTX_set_default_passwd_cb_userdata(SSL_CTX *, void *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_set_default_verify_paths():
        'int SSL_CTX_set_default_verify_paths(SSL_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_set_ecdh_auto():
        'long SSL_CTX_set_ecdh_auto(SSL_CTX *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_set_ex_data():
        'int SSL_CTX_set_ex_data(SSL_CTX *, int, void *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_set_info_callback():
        'void SSL_CTX_set_info_callback(SSL_CTX *, void(*)(SSL *, int, int));\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_set_mode():
        'unsigned long SSL_CTX_set_mode(SSL_CTX *, unsigned long);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_set_next_proto_select_cb():
        'void SSL_CTX_set_next_proto_select_cb(SSL_CTX *, int(*)(SSL *, unsigned char * *, unsigned char *, unsigned char *, unsigned int, void *), void *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_set_next_protos_advertised_cb():
        'void SSL_CTX_set_next_protos_advertised_cb(SSL_CTX *, int(*)(SSL *, unsigned char * *, unsigned int *, void *), void *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_set_options():
        'unsigned long SSL_CTX_set_options(SSL_CTX *, unsigned long);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_set_session_cache_mode():
        'unsigned long SSL_CTX_set_session_cache_mode(SSL_CTX *, unsigned long);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_set_session_id_context():
        'int SSL_CTX_set_session_id_context(SSL_CTX *, unsigned char *, unsigned int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_set_timeout():
        'long SSL_CTX_set_timeout(SSL_CTX *, long);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_set_tlsext_servername_arg():
        'void SSL_CTX_set_tlsext_servername_arg(SSL_CTX *, void *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_set_tlsext_servername_callback():
        'void SSL_CTX_set_tlsext_servername_callback(SSL_CTX *, int(*)(SSL *, int *, void *));\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_set_tlsext_status_arg():
        'long SSL_CTX_set_tlsext_status_arg(SSL_CTX *, void *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_set_tlsext_status_cb():
        'long SSL_CTX_set_tlsext_status_cb(SSL_CTX *, int(*)(SSL *, void *));\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_set_tmp_dh():
        'unsigned long SSL_CTX_set_tmp_dh(SSL_CTX *, DH *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_set_tmp_ecdh():
        'unsigned long SSL_CTX_set_tmp_ecdh(SSL_CTX *, EC_KEY *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_set_verify():
        'void SSL_CTX_set_verify(SSL_CTX *, int, int(*)(int, X509_STORE_CTX *));\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_set_verify_depth():
        'void SSL_CTX_set_verify_depth(SSL_CTX *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_use_PrivateKey():
        'int SSL_CTX_use_PrivateKey(SSL_CTX *, EVP_PKEY *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_use_PrivateKey_ASN1():
        'int SSL_CTX_use_PrivateKey_ASN1(int, SSL_CTX *, unsigned char *, long);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_use_PrivateKey_file():
        'int SSL_CTX_use_PrivateKey_file(SSL_CTX *, char *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_use_certificate():
        'int SSL_CTX_use_certificate(SSL_CTX *, X509 *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_use_certificate_ASN1():
        'int SSL_CTX_use_certificate_ASN1(SSL_CTX *, int, unsigned char *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_use_certificate_chain_file():
        'int SSL_CTX_use_certificate_chain_file(SSL_CTX *, char *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_use_certificate_file():
        'int SSL_CTX_use_certificate_file(SSL_CTX *, char *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    SSL_ERROR_NONE = 0
    SSL_ERROR_SSL = 1
    SSL_ERROR_SYSCALL = 5
    SSL_ERROR_WANT_CONNECT = 7
    SSL_ERROR_WANT_READ = 2
    SSL_ERROR_WANT_WRITE = 3
    SSL_ERROR_WANT_X509_LOOKUP = 4
    SSL_ERROR_ZERO_RETURN = 6
    SSL_FILETYPE_ASN1 = 2
    SSL_FILETYPE_PEM = 1
    SSL_MODE_ACCEPT_MOVING_WRITE_BUFFER = 2
    SSL_MODE_AUTO_RETRY = 4
    SSL_MODE_ENABLE_PARTIAL_WRITE = 1
    SSL_MODE_RELEASE_BUFFERS = 16
    SSL_OP_ALL = 2147485780
    SSL_OP_ALLOW_UNSAFE_LEGACY_RENEGOTIATION = 262144
    SSL_OP_CIPHER_SERVER_PREFERENCE = 4194304
    SSL_OP_COOKIE_EXCHANGE = 8192
    SSL_OP_DONT_INSERT_EMPTY_FRAGMENTS = 2048
    SSL_OP_EPHEMERAL_RSA = 0
    SSL_OP_LEGACY_SERVER_CONNECT = 4
    SSL_OP_MICROSOFT_BIG_SSLV3_BUFFER = 0
    SSL_OP_MICROSOFT_SESS_ID_BUG = 0
    SSL_OP_MSIE_SSLV2_RSA_PADDING = 0
    SSL_OP_NETSCAPE_CA_DN_BUG = 0
    SSL_OP_NETSCAPE_CHALLENGE_BUG = 0
    SSL_OP_NETSCAPE_DEMO_CIPHER_CHANGE_BUG = 0
    SSL_OP_NETSCAPE_REUSE_CIPHER_CHANGE_BUG = 0
    SSL_OP_NO_COMPRESSION = 131072
    SSL_OP_NO_QUERY_MTU = 4096
    SSL_OP_NO_SSLv2 = 0
    SSL_OP_NO_SSLv3 = 33554432
    SSL_OP_NO_TICKET = 16384
    SSL_OP_NO_TLSv1 = 67108864
    SSL_OP_NO_TLSv1_1 = 268435456
    SSL_OP_NO_TLSv1_2 = 134217728
    SSL_OP_PKCS1_CHECK_1 = 0
    SSL_OP_PKCS1_CHECK_2 = 0
    SSL_OP_SINGLE_DH_USE = 0
    SSL_OP_SINGLE_ECDH_USE = 0
    SSL_OP_SSLEAY_080_CLIENT_DH_BUG = 0
    SSL_OP_SSLREF2_REUSE_CERT_TYPE_BUG = 0
    SSL_OP_TLS_BLOCK_PADDING_BUG = 0
    SSL_OP_TLS_D5_BUG = 0
    SSL_OP_TLS_ROLLBACK_BUG = 8388608
    SSL_RECEIVED_SHUTDOWN = 2
    SSL_SENT_SHUTDOWN = 1
    @staticmethod
    def SSL_SESSION_free():
        'void SSL_SESSION_free(SSL_SESSION *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_SESSION_get_id():
        'unsigned char *SSL_SESSION_get_id(SSL_SESSION *, unsigned int *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_SESSION_get_master_key():
        'size_t SSL_SESSION_get_master_key(SSL_SESSION *, unsigned char *, size_t);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_SESSION_print():
        'int SSL_SESSION_print(struct bio_st *, SSL_SESSION *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_SESSION_set1_id_context():
        'int SSL_SESSION_set1_id_context(SSL_SESSION *, unsigned char *, unsigned int);\n\nCFFI C function from _openssl.lib'
        pass
    
    SSL_SESS_CACHE_BOTH = 3
    SSL_SESS_CACHE_CLIENT = 1
    SSL_SESS_CACHE_NO_AUTO_CLEAR = 128
    SSL_SESS_CACHE_NO_INTERNAL = 768
    SSL_SESS_CACHE_NO_INTERNAL_LOOKUP = 256
    SSL_SESS_CACHE_NO_INTERNAL_STORE = 512
    SSL_SESS_CACHE_OFF = 0
    SSL_SESS_CACHE_SERVER = 2
    SSL_ST_ACCEPT = 8192
    SSL_ST_BEFORE = 0
    SSL_ST_CONNECT = 4096
    SSL_ST_INIT = 0
    SSL_ST_MASK = 4095
    SSL_ST_OK = 0
    SSL_ST_RENEGOTIATE = 0
    SSL_TLSEXT_ERR_ALERT_FATAL = 2
    SSL_TLSEXT_ERR_ALERT_WARNING = 1
    SSL_TLSEXT_ERR_NOACK = 3
    SSL_TLSEXT_ERR_OK = 0
    SSL_VERIFY_CLIENT_ONCE = 4
    SSL_VERIFY_FAIL_IF_NO_PEER_CERT = 2
    SSL_VERIFY_NONE = 0
    SSL_VERIFY_PEER = 1
    @staticmethod
    def SSL_check_private_key():
        'int SSL_check_private_key(SSL *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_do_handshake():
        'int SSL_do_handshake(SSL *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_export_keying_material():
        'int SSL_export_keying_material(SSL *, unsigned char *, size_t, char *, size_t, unsigned char *, size_t, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_free():
        'void SSL_free(SSL *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_get0_alpn_selected():
        'void SSL_get0_alpn_selected(SSL *, unsigned char * *, unsigned int *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_get0_next_proto_negotiated():
        'void SSL_get0_next_proto_negotiated(SSL *, unsigned char * *, unsigned int *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_get1_session():
        'SSL_SESSION *SSL_get1_session(SSL *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_get_SSL_CTX():
        'SSL_CTX *SSL_get_SSL_CTX(SSL *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_get_app_data():
        'char *SSL_get_app_data(SSL *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_get_cipher_list():
        'char *SSL_get_cipher_list(SSL *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_get_ciphers():
        'Cryptography_STACK_OF_SSL_CIPHER *SSL_get_ciphers(SSL *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_get_client_CA_list():
        'Cryptography_STACK_OF_X509_NAME *SSL_get_client_CA_list(SSL *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_get_client_random():
        'size_t SSL_get_client_random(SSL *, unsigned char *, size_t);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_get_current_cipher():
        'SSL_CIPHER *SSL_get_current_cipher(SSL *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_get_current_compression():
        'COMP_METHOD *SSL_get_current_compression(SSL *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_get_current_expansion():
        'COMP_METHOD *SSL_get_current_expansion(SSL *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_get_error():
        'int SSL_get_error(SSL *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_get_ex_data():
        'void *SSL_get_ex_data(SSL *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_get_ex_data_X509_STORE_CTX_idx():
        'int SSL_get_ex_data_X509_STORE_CTX_idx();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_get_ex_new_index():
        'int SSL_get_ex_new_index(long, void *, CRYPTO_EX_new *, CRYPTO_EX_dup *, CRYPTO_EX_free *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_get_finished():
        'size_t SSL_get_finished(SSL *, void *, size_t);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_get_info_callback():
        'void(*SSL_get_info_callback(SSL *))(SSL *, int, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_get_mode():
        'unsigned long SSL_get_mode(SSL *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_get_options():
        'unsigned long SSL_get_options(SSL *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_get_peer_cert_chain():
        'Cryptography_STACK_OF_X509 *SSL_get_peer_cert_chain(SSL *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_get_peer_certificate():
        'X509 *SSL_get_peer_certificate(SSL *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_get_peer_finished():
        'size_t SSL_get_peer_finished(SSL *, void *, size_t);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_get_rbio():
        'struct bio_st *SSL_get_rbio(SSL *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_get_secure_renegotiation_support():
        'long SSL_get_secure_renegotiation_support(SSL *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_get_server_random():
        'size_t SSL_get_server_random(SSL *, unsigned char *, size_t);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_get_server_tmp_key():
        'long SSL_get_server_tmp_key(SSL *, EVP_PKEY * *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_get_servername():
        'char *SSL_get_servername(SSL *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_get_session():
        'SSL_SESSION *SSL_get_session(SSL *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_get_shutdown():
        'int SSL_get_shutdown(SSL *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_get_tlsext_status_ocsp_resp():
        'long SSL_get_tlsext_status_ocsp_resp(SSL *, unsigned char * *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_get_verify_callback():
        'int(*SSL_get_verify_callback(SSL *))(int, X509_STORE_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_get_verify_depth():
        'int SSL_get_verify_depth(SSL *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_get_verify_mode():
        'int SSL_get_verify_mode(SSL *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_get_version():
        'char *SSL_get_version(SSL *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_get_wbio():
        'struct bio_st *SSL_get_wbio(SSL *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_library_init():
        'int SSL_library_init();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_load_client_CA_file():
        'Cryptography_STACK_OF_X509_NAME *SSL_load_client_CA_file(char *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_load_error_strings():
        'void SSL_load_error_strings();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_new():
        'SSL *SSL_new(SSL_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_peek():
        'int SSL_peek(SSL *, void *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_pending():
        'int SSL_pending(SSL *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_read():
        'int SSL_read(SSL *, void *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_renegotiate():
        'int SSL_renegotiate(SSL *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_renegotiate_pending():
        'int SSL_renegotiate_pending(SSL *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_select_next_proto():
        'int SSL_select_next_proto(unsigned char * *, unsigned char *, unsigned char *, unsigned int, unsigned char *, unsigned int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_session_reused():
        'long SSL_session_reused(SSL *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_set_SSL_CTX():
        'SSL_CTX *SSL_set_SSL_CTX(SSL *, SSL_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_set_accept_state():
        'void SSL_set_accept_state(SSL *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_set_alpn_protos():
        'int SSL_set_alpn_protos(SSL *, unsigned char *, unsigned int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_set_app_data():
        'void SSL_set_app_data(SSL *, char *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_set_bio():
        'void SSL_set_bio(SSL *, struct bio_st *, struct bio_st *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_set_cert_cb():
        'void SSL_set_cert_cb(SSL *, int(*)(SSL *, void *), void *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_set_connect_state():
        'void SSL_set_connect_state(SSL *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_set_ex_data():
        'int SSL_set_ex_data(SSL *, int, void *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_set_fd():
        'int SSL_set_fd(SSL *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_set_info_callback():
        'void SSL_set_info_callback(SSL *, void(*)(SSL *, int, int));\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_set_mode():
        'unsigned long SSL_set_mode(SSL *, unsigned long);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_set_options():
        'unsigned long SSL_set_options(SSL *, unsigned long);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_set_read_ahead():
        'void SSL_set_read_ahead(SSL *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_set_session():
        'int SSL_set_session(SSL *, SSL_SESSION *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_set_shutdown():
        'void SSL_set_shutdown(SSL *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_set_tlsext_host_name():
        'void SSL_set_tlsext_host_name(SSL *, char *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_set_tlsext_status_ocsp_resp():
        'long SSL_set_tlsext_status_ocsp_resp(SSL *, unsigned char *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_set_tlsext_status_type():
        'long SSL_set_tlsext_status_type(SSL *, long);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_set_verify():
        'void SSL_set_verify(SSL *, int, int(*)(int, X509_STORE_CTX *));\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_set_verify_depth():
        'void SSL_set_verify_depth(SSL *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_shutdown():
        'int SSL_shutdown(SSL *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_state_string_long():
        'char *SSL_state_string_long(SSL *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_total_renegotiations():
        'long SSL_total_renegotiations(SSL *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_use_PrivateKey():
        'int SSL_use_PrivateKey(SSL *, EVP_PKEY *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_use_PrivateKey_ASN1():
        'int SSL_use_PrivateKey_ASN1(int, SSL *, unsigned char *, long);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_use_PrivateKey_file():
        'int SSL_use_PrivateKey_file(SSL *, char *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_use_certificate():
        'int SSL_use_certificate(SSL *, X509 *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_use_certificate_ASN1():
        'int SSL_use_certificate_ASN1(SSL *, unsigned char *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_use_certificate_file():
        'int SSL_use_certificate_file(SSL *, char *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_version():
        'int SSL_version(SSL *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_want_read():
        'int SSL_want_read(SSL *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_want_write():
        'int SSL_want_write(SSL *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_write():
        'int SSL_write(SSL *, void *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSLeay():
        'unsigned long SSLeay();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSLeay_version():
        'char *SSLeay_version(int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSLv23_client_method():
        'SSL_METHOD *SSLv23_client_method();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSLv23_method():
        'SSL_METHOD *SSLv23_method();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSLv23_server_method():
        'SSL_METHOD *SSLv23_server_method();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSLv3_client_method():
        'SSL_METHOD *SSLv3_client_method();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSLv3_method():
        'SSL_METHOD *SSLv3_method();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSLv3_server_method():
        'SSL_METHOD *SSLv3_server_method();\n\nCFFI C function from _openssl.lib'
        pass
    
    TLSEXT_NAMETYPE_host_name = 0
    TLSEXT_STATUSTYPE_ocsp = 1
    TLS_ST_BEFORE = 0
    TLS_ST_OK = 1
    @staticmethod
    def TLSv1_1_client_method():
        'SSL_METHOD *TLSv1_1_client_method();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def TLSv1_1_method():
        'SSL_METHOD *TLSv1_1_method();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def TLSv1_1_server_method():
        'SSL_METHOD *TLSv1_1_server_method();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def TLSv1_2_client_method():
        'SSL_METHOD *TLSv1_2_client_method();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def TLSv1_2_method():
        'SSL_METHOD *TLSv1_2_method();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def TLSv1_2_server_method():
        'SSL_METHOD *TLSv1_2_server_method();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def TLSv1_client_method():
        'SSL_METHOD *TLSv1_client_method();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def TLSv1_method():
        'SSL_METHOD *TLSv1_method();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def TLSv1_server_method():
        'SSL_METHOD *TLSv1_server_method();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def USERNOTICE_free():
        'void USERNOTICE_free(USERNOTICE *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def USERNOTICE_new():
        'USERNOTICE *USERNOTICE_new();\n\nCFFI C function from _openssl.lib'
        pass
    
    V_ASN1_GENERALIZEDTIME = 24
    @staticmethod
    def X509V3_EXT_add_alias():
        'int X509V3_EXT_add_alias(int, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509V3_EXT_conf_nid():
        'X509_EXTENSION *X509V3_EXT_conf_nid(Cryptography_LHASH_OF_CONF_VALUE *, X509V3_CTX *, int, char *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509V3_EXT_d2i():
        'void *X509V3_EXT_d2i(X509_EXTENSION *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509V3_EXT_get():
        'X509V3_EXT_METHOD *X509V3_EXT_get(X509_EXTENSION *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509V3_EXT_get_nid():
        'X509V3_EXT_METHOD *X509V3_EXT_get_nid(int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509V3_EXT_i2d():
        'X509_EXTENSION *X509V3_EXT_i2d(int, int, void *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509V3_EXT_nconf():
        'X509_EXTENSION *X509V3_EXT_nconf(CONF *, X509V3_CTX *, char *, char *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509V3_EXT_print():
        'int X509V3_EXT_print(struct bio_st *, X509_EXTENSION *, unsigned long, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509V3_set_ctx():
        'void X509V3_set_ctx(X509V3_CTX *, X509 *, X509 *, X509_REQ *, X509_CRL *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509V3_set_ctx_nodb():
        'void *X509V3_set_ctx_nodb(X509V3_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_CRL_add0_revoked():
        'int X509_CRL_add0_revoked(X509_CRL *, X509_REVOKED *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_CRL_add_ext():
        'int X509_CRL_add_ext(X509_CRL *, X509_EXTENSION *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_CRL_cmp():
        'int X509_CRL_cmp(X509_CRL *, X509_CRL *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_CRL_free():
        'void X509_CRL_free(X509_CRL *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_CRL_get0_signature():
        'void X509_CRL_get0_signature(X509_CRL *, struct asn1_string_st * *, X509_ALGOR * *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_CRL_get_REVOKED():
        'Cryptography_STACK_OF_X509_REVOKED *X509_CRL_get_REVOKED(X509_CRL *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_CRL_get_ext():
        'X509_EXTENSION *X509_CRL_get_ext(X509_CRL *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_CRL_get_ext_count():
        'int X509_CRL_get_ext_count(X509_CRL *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_CRL_get_issuer():
        'X509_NAME *X509_CRL_get_issuer(X509_CRL *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_CRL_get_lastUpdate():
        'struct asn1_string_st *X509_CRL_get_lastUpdate(X509_CRL *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_CRL_get_nextUpdate():
        'struct asn1_string_st *X509_CRL_get_nextUpdate(X509_CRL *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_CRL_get_version():
        'long X509_CRL_get_version(X509_CRL *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_CRL_new():
        'X509_CRL *X509_CRL_new();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_CRL_print():
        'int X509_CRL_print(struct bio_st *, X509_CRL *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_CRL_set_issuer_name():
        'int X509_CRL_set_issuer_name(X509_CRL *, X509_NAME *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_CRL_set_lastUpdate():
        'int X509_CRL_set_lastUpdate(X509_CRL *, struct asn1_string_st *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_CRL_set_nextUpdate():
        'int X509_CRL_set_nextUpdate(X509_CRL *, struct asn1_string_st *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_CRL_set_version():
        'int X509_CRL_set_version(X509_CRL *, long);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_CRL_sign():
        'int X509_CRL_sign(X509_CRL *, EVP_PKEY *, EVP_MD *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_CRL_sort():
        'int X509_CRL_sort(X509_CRL *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_CRL_verify():
        'int X509_CRL_verify(X509_CRL *, EVP_PKEY *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_EXTENSION_create_by_OBJ():
        'X509_EXTENSION *X509_EXTENSION_create_by_OBJ(X509_EXTENSION * *, ASN1_OBJECT *, int, struct asn1_string_st *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_EXTENSION_dup():
        'X509_EXTENSION *X509_EXTENSION_dup(X509_EXTENSION *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_EXTENSION_free():
        'void X509_EXTENSION_free(X509_EXTENSION *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_EXTENSION_get_critical():
        'int X509_EXTENSION_get_critical(X509_EXTENSION *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_EXTENSION_get_data():
        'struct asn1_string_st *X509_EXTENSION_get_data(X509_EXTENSION *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_EXTENSION_get_object():
        'ASN1_OBJECT *X509_EXTENSION_get_object(X509_EXTENSION *);\n\nCFFI C function from _openssl.lib'
        pass
    
    X509_FLAG_COMPAT = 0
    X509_FLAG_NO_ATTRIBUTES = 2048
    X509_FLAG_NO_AUX = 1024
    X509_FLAG_NO_EXTENSIONS = 256
    X509_FLAG_NO_HEADER = 1
    X509_FLAG_NO_ISSUER = 16
    X509_FLAG_NO_PUBKEY = 128
    X509_FLAG_NO_SERIAL = 4
    X509_FLAG_NO_SIGDUMP = 512
    X509_FLAG_NO_SIGNAME = 8
    X509_FLAG_NO_SUBJECT = 64
    X509_FLAG_NO_VALIDITY = 32
    X509_FLAG_NO_VERSION = 2
    X509_LU_CRL = 2
    X509_LU_X509 = 1
    @staticmethod
    def X509_NAME_ENTRY_create_by_OBJ():
        'X509_NAME_ENTRY *X509_NAME_ENTRY_create_by_OBJ(X509_NAME_ENTRY * *, ASN1_OBJECT *, int, unsigned char *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_NAME_ENTRY_free():
        'void X509_NAME_ENTRY_free(X509_NAME_ENTRY *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_NAME_ENTRY_get_data():
        'struct asn1_string_st *X509_NAME_ENTRY_get_data(X509_NAME_ENTRY *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_NAME_ENTRY_get_object():
        'ASN1_OBJECT *X509_NAME_ENTRY_get_object(X509_NAME_ENTRY *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_NAME_add_entry():
        'int X509_NAME_add_entry(X509_NAME *, X509_NAME_ENTRY *, int, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_NAME_add_entry_by_NID():
        'int X509_NAME_add_entry_by_NID(X509_NAME *, int, int, unsigned char *, int, int, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_NAME_add_entry_by_OBJ():
        'int X509_NAME_add_entry_by_OBJ(X509_NAME *, ASN1_OBJECT *, int, unsigned char *, int, int, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_NAME_add_entry_by_txt():
        'int X509_NAME_add_entry_by_txt(X509_NAME *, char *, int, unsigned char *, int, int, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_NAME_cmp():
        'int X509_NAME_cmp(X509_NAME *, X509_NAME *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_NAME_delete_entry():
        'X509_NAME_ENTRY *X509_NAME_delete_entry(X509_NAME *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_NAME_dup():
        'X509_NAME *X509_NAME_dup(X509_NAME *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_NAME_entry_count():
        'int X509_NAME_entry_count(X509_NAME *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_NAME_free():
        'void X509_NAME_free(X509_NAME *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_NAME_get_entry():
        'X509_NAME_ENTRY *X509_NAME_get_entry(X509_NAME *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_NAME_get_index_by_NID():
        'int X509_NAME_get_index_by_NID(X509_NAME *, int, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_NAME_hash():
        'unsigned long X509_NAME_hash(X509_NAME *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_NAME_new():
        'X509_NAME *X509_NAME_new();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_NAME_oneline():
        'char *X509_NAME_oneline(X509_NAME *, char *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_OBJECT_get0_X509():
        'X509 *X509_OBJECT_get0_X509(X509_OBJECT *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_OBJECT_get_type():
        'int X509_OBJECT_get_type(X509_OBJECT *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_REQ_add_extensions():
        'int X509_REQ_add_extensions(X509_REQ *, X509_EXTENSIONS *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_REQ_digest():
        'int X509_REQ_digest(X509_REQ *, EVP_MD *, unsigned char *, unsigned int *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_REQ_free():
        'void X509_REQ_free(X509_REQ *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_REQ_get0_signature():
        'void X509_REQ_get0_signature(X509_REQ *, struct asn1_string_st * *, X509_ALGOR * *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_REQ_get_extensions():
        'X509_EXTENSIONS *X509_REQ_get_extensions(X509_REQ *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_REQ_get_pubkey():
        'EVP_PKEY *X509_REQ_get_pubkey(X509_REQ *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_REQ_get_subject_name():
        'X509_NAME *X509_REQ_get_subject_name(X509_REQ *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_REQ_get_version():
        'long X509_REQ_get_version(X509_REQ *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_REQ_new():
        'X509_REQ *X509_REQ_new();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_REQ_print():
        'int X509_REQ_print(struct bio_st *, X509_REQ *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_REQ_print_ex():
        'int X509_REQ_print_ex(struct bio_st *, X509_REQ *, unsigned long, unsigned long);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_REQ_set_pubkey():
        'int X509_REQ_set_pubkey(X509_REQ *, EVP_PKEY *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_REQ_set_subject_name():
        'int X509_REQ_set_subject_name(X509_REQ *, X509_NAME *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_REQ_set_version():
        'int X509_REQ_set_version(X509_REQ *, long);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_REQ_sign():
        'int X509_REQ_sign(X509_REQ *, EVP_PKEY *, EVP_MD *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_REQ_verify():
        'int X509_REQ_verify(X509_REQ *, EVP_PKEY *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_REVOKED_add1_ext_i2d():
        'int X509_REVOKED_add1_ext_i2d(X509_REVOKED *, int, void *, int, unsigned long);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_REVOKED_add_ext():
        'int X509_REVOKED_add_ext(X509_REVOKED *, X509_EXTENSION *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_REVOKED_delete_ext():
        'X509_EXTENSION *X509_REVOKED_delete_ext(X509_REVOKED *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_REVOKED_free():
        'void X509_REVOKED_free(X509_REVOKED *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_REVOKED_get0_revocationDate():
        'struct asn1_string_st *X509_REVOKED_get0_revocationDate(X509_REVOKED *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_REVOKED_get0_serialNumber():
        'ASN1_INTEGER *X509_REVOKED_get0_serialNumber(X509_REVOKED *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_REVOKED_get_ext():
        'X509_EXTENSION *X509_REVOKED_get_ext(X509_REVOKED *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_REVOKED_get_ext_count():
        'int X509_REVOKED_get_ext_count(X509_REVOKED *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_REVOKED_new():
        'X509_REVOKED *X509_REVOKED_new();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_REVOKED_set_revocationDate():
        'int X509_REVOKED_set_revocationDate(X509_REVOKED *, struct asn1_string_st *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_REVOKED_set_serialNumber():
        'int X509_REVOKED_set_serialNumber(X509_REVOKED *, ASN1_INTEGER *);\n\nCFFI C function from _openssl.lib'
        pass
    
    X509_R_CERT_ALREADY_IN_HASH_TABLE = 101
    @staticmethod
    def X509_STORE_CTX_cleanup():
        'void X509_STORE_CTX_cleanup(X509_STORE_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_STORE_CTX_free():
        'void X509_STORE_CTX_free(X509_STORE_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_STORE_CTX_get0_cert():
        'X509 *X509_STORE_CTX_get0_cert(X509_STORE_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_STORE_CTX_get0_param():
        'X509_VERIFY_PARAM *X509_STORE_CTX_get0_param(X509_STORE_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_STORE_CTX_get1_chain():
        'Cryptography_STACK_OF_X509 *X509_STORE_CTX_get1_chain(X509_STORE_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_STORE_CTX_get1_issuer():
        'int X509_STORE_CTX_get1_issuer(X509 * *, X509_STORE_CTX *, X509 *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_STORE_CTX_get_chain():
        'Cryptography_STACK_OF_X509 *X509_STORE_CTX_get_chain(X509_STORE_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_STORE_CTX_get_current_cert():
        'X509 *X509_STORE_CTX_get_current_cert(X509_STORE_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_STORE_CTX_get_error():
        'int X509_STORE_CTX_get_error(X509_STORE_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_STORE_CTX_get_error_depth():
        'int X509_STORE_CTX_get_error_depth(X509_STORE_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_STORE_CTX_get_ex_data():
        'void *X509_STORE_CTX_get_ex_data(X509_STORE_CTX *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_STORE_CTX_get_ex_new_index():
        'int X509_STORE_CTX_get_ex_new_index(long, void *, CRYPTO_EX_new *, CRYPTO_EX_dup *, CRYPTO_EX_free *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_STORE_CTX_init():
        'int X509_STORE_CTX_init(X509_STORE_CTX *, X509_STORE *, X509 *, Cryptography_STACK_OF_X509 *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_STORE_CTX_new():
        'X509_STORE_CTX *X509_STORE_CTX_new();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_STORE_CTX_set0_crls():
        'void X509_STORE_CTX_set0_crls(X509_STORE_CTX *, Cryptography_STACK_OF_X509_CRL *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_STORE_CTX_set0_param():
        'void X509_STORE_CTX_set0_param(X509_STORE_CTX *, X509_VERIFY_PARAM *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_STORE_CTX_set_cert():
        'void X509_STORE_CTX_set_cert(X509_STORE_CTX *, X509 *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_STORE_CTX_set_chain():
        'void X509_STORE_CTX_set_chain(X509_STORE_CTX *, Cryptography_STACK_OF_X509 *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_STORE_CTX_set_default():
        'int X509_STORE_CTX_set_default(X509_STORE_CTX *, char *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_STORE_CTX_set_error():
        'void X509_STORE_CTX_set_error(X509_STORE_CTX *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_STORE_CTX_set_ex_data():
        'int X509_STORE_CTX_set_ex_data(X509_STORE_CTX *, int, void *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_STORE_CTX_set_verify_cb():
        'void X509_STORE_CTX_set_verify_cb(X509_STORE_CTX *, int(*)(int, X509_STORE_CTX *));\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_STORE_CTX_trusted_stack():
        'void X509_STORE_CTX_trusted_stack(X509_STORE_CTX *, Cryptography_STACK_OF_X509 *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_STORE_add_cert():
        'int X509_STORE_add_cert(X509_STORE *, X509 *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_STORE_add_crl():
        'int X509_STORE_add_crl(X509_STORE *, X509_CRL *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_STORE_free():
        'void X509_STORE_free(X509_STORE *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_STORE_get0_objects():
        'Cryptography_STACK_OF_X509_OBJECT *X509_STORE_get0_objects(X509_STORE *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_STORE_get0_param():
        'X509_VERIFY_PARAM *X509_STORE_get0_param(X509_STORE *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_STORE_get_get_issuer():
        'int(*X509_STORE_get_get_issuer(X509_STORE *))(X509 * *, X509_STORE_CTX *, X509 *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_STORE_load_locations():
        'int X509_STORE_load_locations(X509_STORE *, char *, char *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_STORE_new():
        'X509_STORE *X509_STORE_new();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_STORE_set1_param():
        'int X509_STORE_set1_param(X509_STORE *, X509_VERIFY_PARAM *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_STORE_set_default_paths():
        'int X509_STORE_set_default_paths(X509_STORE *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_STORE_set_flags():
        'int X509_STORE_set_flags(X509_STORE *, unsigned long);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_STORE_set_get_issuer():
        'void X509_STORE_set_get_issuer(X509_STORE *, int(*)(X509 * *, X509_STORE_CTX *, X509 *));\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_VERIFY_PARAM_add0_policy():
        'int X509_VERIFY_PARAM_add0_policy(X509_VERIFY_PARAM *, ASN1_OBJECT *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_VERIFY_PARAM_clear_flags():
        'int X509_VERIFY_PARAM_clear_flags(X509_VERIFY_PARAM *, unsigned long);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_VERIFY_PARAM_free():
        'void X509_VERIFY_PARAM_free(X509_VERIFY_PARAM *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_VERIFY_PARAM_get_depth():
        'int X509_VERIFY_PARAM_get_depth(X509_VERIFY_PARAM *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_VERIFY_PARAM_get_flags():
        'unsigned long X509_VERIFY_PARAM_get_flags(X509_VERIFY_PARAM *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_VERIFY_PARAM_new():
        'X509_VERIFY_PARAM *X509_VERIFY_PARAM_new();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_VERIFY_PARAM_set1_email():
        'int X509_VERIFY_PARAM_set1_email(X509_VERIFY_PARAM *, char *, size_t);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_VERIFY_PARAM_set1_host():
        'int X509_VERIFY_PARAM_set1_host(X509_VERIFY_PARAM *, char *, size_t);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_VERIFY_PARAM_set1_ip():
        'int X509_VERIFY_PARAM_set1_ip(X509_VERIFY_PARAM *, unsigned char *, size_t);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_VERIFY_PARAM_set1_ip_asc():
        'int X509_VERIFY_PARAM_set1_ip_asc(X509_VERIFY_PARAM *, char *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_VERIFY_PARAM_set1_policies():
        'int X509_VERIFY_PARAM_set1_policies(X509_VERIFY_PARAM *, Cryptography_STACK_OF_ASN1_OBJECT *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_VERIFY_PARAM_set_depth():
        'void X509_VERIFY_PARAM_set_depth(X509_VERIFY_PARAM *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_VERIFY_PARAM_set_flags():
        'int X509_VERIFY_PARAM_set_flags(X509_VERIFY_PARAM *, unsigned long);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_VERIFY_PARAM_set_hostflags():
        'void X509_VERIFY_PARAM_set_hostflags(X509_VERIFY_PARAM *, unsigned int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_VERIFY_PARAM_set_purpose():
        'int X509_VERIFY_PARAM_set_purpose(X509_VERIFY_PARAM *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_VERIFY_PARAM_set_time():
        'void X509_VERIFY_PARAM_set_time(X509_VERIFY_PARAM *, int64_t);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_VERIFY_PARAM_set_trust():
        'int X509_VERIFY_PARAM_set_trust(X509_VERIFY_PARAM *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    X509_V_ERR_AKID_ISSUER_SERIAL_MISMATCH = 31
    X509_V_ERR_AKID_SKID_MISMATCH = 30
    X509_V_ERR_APPLICATION_VERIFICATION = 50
    X509_V_ERR_CERT_CHAIN_TOO_LONG = 22
    X509_V_ERR_CERT_HAS_EXPIRED = 10
    X509_V_ERR_CERT_NOT_YET_VALID = 9
    X509_V_ERR_CERT_REJECTED = 28
    X509_V_ERR_CERT_REVOKED = 23
    X509_V_ERR_CERT_SIGNATURE_FAILURE = 7
    X509_V_ERR_CERT_UNTRUSTED = 27
    X509_V_ERR_CRL_HAS_EXPIRED = 12
    X509_V_ERR_CRL_NOT_YET_VALID = 11
    X509_V_ERR_CRL_PATH_VALIDATION_ERROR = 54
    X509_V_ERR_CRL_SIGNATURE_FAILURE = 8
    X509_V_ERR_DEPTH_ZERO_SELF_SIGNED_CERT = 18
    X509_V_ERR_DIFFERENT_CRL_SCOPE = 44
    X509_V_ERR_EMAIL_MISMATCH = 63
    X509_V_ERR_ERROR_IN_CERT_NOT_AFTER_FIELD = 14
    X509_V_ERR_ERROR_IN_CERT_NOT_BEFORE_FIELD = 13
    X509_V_ERR_ERROR_IN_CRL_LAST_UPDATE_FIELD = 15
    X509_V_ERR_ERROR_IN_CRL_NEXT_UPDATE_FIELD = 16
    X509_V_ERR_EXCLUDED_VIOLATION = 48
    X509_V_ERR_HOSTNAME_MISMATCH = 62
    X509_V_ERR_INVALID_CA = 24
    X509_V_ERR_INVALID_EXTENSION = 41
    X509_V_ERR_INVALID_NON_CA = 37
    X509_V_ERR_INVALID_POLICY_EXTENSION = 42
    X509_V_ERR_INVALID_PURPOSE = 26
    X509_V_ERR_IP_ADDRESS_MISMATCH = 64
    X509_V_ERR_KEYUSAGE_NO_CERTSIGN = 32
    X509_V_ERR_KEYUSAGE_NO_CRL_SIGN = 35
    X509_V_ERR_KEYUSAGE_NO_DIGITAL_SIGNATURE = 39
    X509_V_ERR_NO_EXPLICIT_POLICY = 43
    X509_V_ERR_OUT_OF_MEM = 17
    X509_V_ERR_PATH_LENGTH_EXCEEDED = 25
    X509_V_ERR_PERMITTED_VIOLATION = 47
    X509_V_ERR_PROXY_CERTIFICATES_NOT_ALLOWED = 40
    X509_V_ERR_PROXY_PATH_LENGTH_EXCEEDED = 38
    X509_V_ERR_SELF_SIGNED_CERT_IN_CHAIN = 19
    X509_V_ERR_SUBJECT_ISSUER_MISMATCH = 29
    X509_V_ERR_SUBTREE_MINMAX = 49
    X509_V_ERR_SUITE_B_CANNOT_SIGN_P_384_WITH_P_256 = 61
    X509_V_ERR_SUITE_B_INVALID_ALGORITHM = 57
    X509_V_ERR_SUITE_B_INVALID_CURVE = 58
    X509_V_ERR_SUITE_B_INVALID_SIGNATURE_ALGORITHM = 59
    X509_V_ERR_SUITE_B_INVALID_VERSION = 56
    X509_V_ERR_SUITE_B_LOS_NOT_ALLOWED = 60
    X509_V_ERR_UNABLE_TO_DECODE_ISSUER_PUBLIC_KEY = 6
    X509_V_ERR_UNABLE_TO_DECRYPT_CERT_SIGNATURE = 4
    X509_V_ERR_UNABLE_TO_DECRYPT_CRL_SIGNATURE = 5
    X509_V_ERR_UNABLE_TO_GET_CRL = 3
    X509_V_ERR_UNABLE_TO_GET_CRL_ISSUER = 33
    X509_V_ERR_UNABLE_TO_GET_ISSUER_CERT = 2
    X509_V_ERR_UNABLE_TO_GET_ISSUER_CERT_LOCALLY = 20
    X509_V_ERR_UNABLE_TO_VERIFY_LEAF_SIGNATURE = 21
    X509_V_ERR_UNHANDLED_CRITICAL_CRL_EXTENSION = 36
    X509_V_ERR_UNHANDLED_CRITICAL_EXTENSION = 34
    X509_V_ERR_UNNESTED_RESOURCE = 46
    X509_V_ERR_UNSUPPORTED_CONSTRAINT_SYNTAX = 52
    X509_V_ERR_UNSUPPORTED_CONSTRAINT_TYPE = 51
    X509_V_ERR_UNSUPPORTED_EXTENSION_FEATURE = 45
    X509_V_ERR_UNSUPPORTED_NAME_SYNTAX = 53
    X509_V_FLAG_ALLOW_PROXY_CERTS = 64
    X509_V_FLAG_CB_ISSUER_CHECK = 0
    X509_V_FLAG_CHECK_SS_SIGNATURE = 16384
    X509_V_FLAG_CRL_CHECK = 4
    X509_V_FLAG_CRL_CHECK_ALL = 8
    X509_V_FLAG_EXPLICIT_POLICY = 256
    X509_V_FLAG_EXTENDED_CRL_SUPPORT = 4096
    X509_V_FLAG_IGNORE_CRITICAL = 16
    X509_V_FLAG_INHIBIT_ANY = 512
    X509_V_FLAG_INHIBIT_MAP = 1024
    X509_V_FLAG_NOTIFY_POLICY = 2048
    X509_V_FLAG_PARTIAL_CHAIN = 524288
    X509_V_FLAG_POLICY_CHECK = 128
    X509_V_FLAG_SUITEB_128_LOS = 196608
    X509_V_FLAG_SUITEB_128_LOS_ONLY = 65536
    X509_V_FLAG_SUITEB_192_LOS = 131072
    X509_V_FLAG_TRUSTED_FIRST = 32768
    X509_V_FLAG_USE_CHECK_TIME = 2
    X509_V_FLAG_USE_DELTAS = 8192
    X509_V_FLAG_X509_STRICT = 32
    X509_V_OK = 0
    @staticmethod
    def X509_add_ext():
        'int X509_add_ext(X509 *, X509_EXTENSION *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_alias_get0():
        'unsigned char *X509_alias_get0(X509 *, int *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_check_ca():
        'int X509_check_ca(X509 *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_cmp():
        'int X509_cmp(X509 *, X509 *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_delete_ext():
        'X509_EXTENSION *X509_delete_ext(X509 *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_digest():
        'int X509_digest(X509 *, EVP_MD *, unsigned char *, unsigned int *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_dup():
        'X509 *X509_dup(X509 *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_free():
        'void X509_free(X509 *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_get0_signature():
        'void X509_get0_signature(struct asn1_string_st * *, X509_ALGOR * *, X509 *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_get0_tbs_sigalg():
        'X509_ALGOR *X509_get0_tbs_sigalg(X509 *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_get_default_cert_area():
        'char *X509_get_default_cert_area();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_get_default_cert_dir():
        'char *X509_get_default_cert_dir();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_get_default_cert_dir_env():
        'char *X509_get_default_cert_dir_env();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_get_default_cert_file():
        'char *X509_get_default_cert_file();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_get_default_cert_file_env():
        'char *X509_get_default_cert_file_env();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_get_default_private_dir():
        'char *X509_get_default_private_dir();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_get_ex_data():
        'void *X509_get_ex_data(X509 *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_get_ex_new_index():
        'int X509_get_ex_new_index(long, void *, CRYPTO_EX_new *, CRYPTO_EX_dup *, CRYPTO_EX_free *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_get_ext():
        'X509_EXTENSION *X509_get_ext(X509 *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_get_ext_by_NID():
        'int X509_get_ext_by_NID(X509 *, int, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_get_ext_count():
        'int X509_get_ext_count(X509 *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_get_ext_d2i():
        'void *X509_get_ext_d2i(X509 *, int, int *, int *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_get_issuer_name():
        'X509_NAME *X509_get_issuer_name(X509 *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_get_notAfter():
        'struct asn1_string_st *X509_get_notAfter(X509 *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_get_notBefore():
        'struct asn1_string_st *X509_get_notBefore(X509 *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_get_pubkey():
        'EVP_PKEY *X509_get_pubkey(X509 *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_get_serialNumber():
        'ASN1_INTEGER *X509_get_serialNumber(X509 *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_get_signature_nid():
        'int X509_get_signature_nid(X509 *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_get_subject_name():
        'X509_NAME *X509_get_subject_name(X509 *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_get_version():
        'long X509_get_version(X509 *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_gmtime_adj():
        'struct asn1_string_st *X509_gmtime_adj(struct asn1_string_st *, long);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_new():
        'X509 *X509_new();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_print_ex():
        'int X509_print_ex(struct bio_st *, X509 *, unsigned long, unsigned long);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_set_ex_data():
        'int X509_set_ex_data(X509 *, int, void *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_set_issuer_name():
        'int X509_set_issuer_name(X509 *, X509_NAME *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_set_notAfter():
        'int X509_set_notAfter(X509 *, struct asn1_string_st *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_set_notBefore():
        'int X509_set_notBefore(X509 *, struct asn1_string_st *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_set_pubkey():
        'int X509_set_pubkey(X509 *, EVP_PKEY *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_set_serialNumber():
        'int X509_set_serialNumber(X509 *, ASN1_INTEGER *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_set_subject_name():
        'int X509_set_subject_name(X509 *, X509_NAME *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_set_version():
        'int X509_set_version(X509 *, long);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_sign():
        'int X509_sign(X509 *, EVP_PKEY *, EVP_MD *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_subject_name_hash():
        'unsigned long X509_subject_name_hash(X509 *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_up_ref():
        'int X509_up_ref(X509 *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_verify_cert():
        'int X509_verify_cert(X509_STORE_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_verify_cert_error_string():
        'char *X509_verify_cert_error_string(long);\n\nCFFI C function from _openssl.lib'
        pass
    
    XN_FLAG_COMPAT = 0
    XN_FLAG_DN_REV = 1048576
    XN_FLAG_DUMP_UNKNOWN_FIELDS = 16777216
    XN_FLAG_FN_ALIGN = 33554432
    XN_FLAG_FN_LN = 2097152
    XN_FLAG_FN_MASK = 6291456
    XN_FLAG_FN_NONE = 6291456
    XN_FLAG_FN_OID = 4194304
    XN_FLAG_FN_SN = 0
    XN_FLAG_MULTILINE = 44302342
    XN_FLAG_ONELINE = 8520479
    XN_FLAG_RFC2253 = 17892119
    XN_FLAG_SEP_COMMA_PLUS = 65536
    XN_FLAG_SEP_CPLUS_SPC = 131072
    XN_FLAG_SEP_MASK = 983040
    XN_FLAG_SEP_MULTILINE = 262144
    XN_FLAG_SEP_SPLUS_SPC = 196608
    XN_FLAG_SPC_EQ = 8388608
    @staticmethod
    def _setup_ssl_threads():
        'int _setup_ssl_threads();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def d2i_ASN1_OBJECT():
        'ASN1_OBJECT *d2i_ASN1_OBJECT(ASN1_OBJECT * *, unsigned char * *, long);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def d2i_ASN1_TYPE():
        'ASN1_TYPE *d2i_ASN1_TYPE(ASN1_TYPE * *, unsigned char * *, long);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def d2i_DHparams():
        'DH *d2i_DHparams(DH * *, unsigned char * *, long);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def d2i_DHparams_bio():
        'DH *d2i_DHparams_bio(struct bio_st *, DH * *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def d2i_DSAPrivateKey():
        'DSA *d2i_DSAPrivateKey(DSA * *, unsigned char * *, long);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def d2i_DSAPrivateKey_bio():
        'DSA *d2i_DSAPrivateKey_bio(struct bio_st *, DSA * *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def d2i_DSAPublicKey():
        'DSA *d2i_DSAPublicKey(DSA * *, unsigned char * *, long);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def d2i_DSA_PUBKEY():
        'DSA *d2i_DSA_PUBKEY(DSA * *, unsigned char * *, long);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def d2i_DSA_PUBKEY_bio():
        'DSA *d2i_DSA_PUBKEY_bio(struct bio_st *, DSA * *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def d2i_ECDSA_SIG():
        'ECDSA_SIG *d2i_ECDSA_SIG(ECDSA_SIG * *, unsigned char * *, long);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def d2i_ECPrivateKey():
        'EC_KEY *d2i_ECPrivateKey(EC_KEY * *, unsigned char * *, long);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def d2i_ECPrivateKey_bio():
        'EC_KEY *d2i_ECPrivateKey_bio(struct bio_st *, EC_KEY * *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def d2i_EC_PUBKEY():
        'EC_KEY *d2i_EC_PUBKEY(EC_KEY * *, unsigned char * *, long);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def d2i_EC_PUBKEY_bio():
        'EC_KEY *d2i_EC_PUBKEY_bio(struct bio_st *, EC_KEY * *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def d2i_GENERAL_NAMES():
        'struct stack_st_GENERAL_NAME *d2i_GENERAL_NAMES(struct stack_st_GENERAL_NAME * *, unsigned char * *, long);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def d2i_OCSP_REQUEST_bio():
        'OCSP_REQUEST *d2i_OCSP_REQUEST_bio(struct bio_st *, OCSP_REQUEST * *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def d2i_OCSP_RESPONSE_bio():
        'OCSP_RESPONSE *d2i_OCSP_RESPONSE_bio(struct bio_st *, OCSP_RESPONSE * *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def d2i_PKCS12_bio():
        'PKCS12 *d2i_PKCS12_bio(struct bio_st *, PKCS12 * *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def d2i_PKCS7_bio():
        'PKCS7 *d2i_PKCS7_bio(struct bio_st *, PKCS7 * *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def d2i_PKCS8PrivateKey_bio():
        'EVP_PKEY *d2i_PKCS8PrivateKey_bio(struct bio_st *, EVP_PKEY * *, int(*)(char *, int, int, void *), void *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def d2i_PKCS8_PRIV_KEY_INFO_bio():
        'PKCS8_PRIV_KEY_INFO *d2i_PKCS8_PRIV_KEY_INFO_bio(struct bio_st *, PKCS8_PRIV_KEY_INFO * *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def d2i_PUBKEY_bio():
        'EVP_PKEY *d2i_PUBKEY_bio(struct bio_st *, EVP_PKEY * *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def d2i_PrivateKey_bio():
        'EVP_PKEY *d2i_PrivateKey_bio(struct bio_st *, EVP_PKEY * *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def d2i_RSAPrivateKey():
        'RSA *d2i_RSAPrivateKey(RSA * *, unsigned char * *, long);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def d2i_RSAPrivateKey_bio():
        'RSA *d2i_RSAPrivateKey_bio(struct bio_st *, RSA * *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def d2i_RSAPublicKey():
        'RSA *d2i_RSAPublicKey(RSA * *, unsigned char * *, long);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def d2i_RSAPublicKey_bio():
        'RSA *d2i_RSAPublicKey_bio(struct bio_st *, RSA * *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def d2i_RSA_PUBKEY():
        'RSA *d2i_RSA_PUBKEY(RSA * *, unsigned char * *, long);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def d2i_RSA_PUBKEY_bio():
        'RSA *d2i_RSA_PUBKEY_bio(struct bio_st *, RSA * *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def d2i_X509_CRL_bio():
        'X509_CRL *d2i_X509_CRL_bio(struct bio_st *, X509_CRL * *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def d2i_X509_REQ_bio():
        'X509_REQ *d2i_X509_REQ_bio(struct bio_st *, X509_REQ * *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def d2i_X509_bio():
        'X509 *d2i_X509_bio(struct bio_st *, X509 * *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def i2a_ASN1_INTEGER():
        'int i2a_ASN1_INTEGER(struct bio_st *, ASN1_INTEGER *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def i2d_ASN1_BIT_STRING():
        'int i2d_ASN1_BIT_STRING(struct asn1_string_st *, unsigned char * *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def i2d_ASN1_ENUMERATED():
        'int i2d_ASN1_ENUMERATED(ASN1_ENUMERATED *, unsigned char * *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def i2d_ASN1_GENERALIZEDTIME():
        'int i2d_ASN1_GENERALIZEDTIME(ASN1_GENERALIZEDTIME *, unsigned char * *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def i2d_ASN1_INTEGER():
        'int i2d_ASN1_INTEGER(ASN1_INTEGER *, unsigned char * *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def i2d_ASN1_OBJECT():
        'int i2d_ASN1_OBJECT(ASN1_OBJECT *, unsigned char * *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def i2d_ASN1_OCTET_STRING():
        'int i2d_ASN1_OCTET_STRING(struct asn1_string_st *, unsigned char * *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def i2d_ASN1_TYPE():
        'int i2d_ASN1_TYPE(ASN1_TYPE *, unsigned char * *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def i2d_CMS_bio_stream():
        'int i2d_CMS_bio_stream(struct bio_st *, CMS_ContentInfo *, struct bio_st *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def i2d_DHparams():
        'int i2d_DHparams(DH *, unsigned char * *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def i2d_DHparams_bio():
        'int i2d_DHparams_bio(struct bio_st *, DH *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def i2d_DSAPrivateKey():
        'int i2d_DSAPrivateKey(DSA *, unsigned char * *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def i2d_DSAPrivateKey_bio():
        'int i2d_DSAPrivateKey_bio(struct bio_st *, DSA *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def i2d_DSAPublicKey():
        'int i2d_DSAPublicKey(DSA *, unsigned char * *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def i2d_DSA_PUBKEY():
        'int i2d_DSA_PUBKEY(DSA *, unsigned char * *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def i2d_DSA_PUBKEY_bio():
        'int i2d_DSA_PUBKEY_bio(struct bio_st *, DSA *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def i2d_ECDSA_SIG():
        'int i2d_ECDSA_SIG(ECDSA_SIG *, unsigned char * *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def i2d_ECPrivateKey():
        'int i2d_ECPrivateKey(EC_KEY *, unsigned char * *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def i2d_ECPrivateKey_bio():
        'int i2d_ECPrivateKey_bio(struct bio_st *, EC_KEY *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def i2d_EC_PUBKEY():
        'int i2d_EC_PUBKEY(EC_KEY *, unsigned char * *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def i2d_EC_PUBKEY_bio():
        'int i2d_EC_PUBKEY_bio(struct bio_st *, EC_KEY *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def i2d_GENERAL_NAMES():
        'int i2d_GENERAL_NAMES(struct stack_st_GENERAL_NAME *, unsigned char * *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def i2d_OCSP_REQUEST_bio():
        'int i2d_OCSP_REQUEST_bio(struct bio_st *, OCSP_REQUEST *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def i2d_OCSP_RESPONSE_bio():
        'int i2d_OCSP_RESPONSE_bio(struct bio_st *, OCSP_RESPONSE *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def i2d_PKCS12_bio():
        'int i2d_PKCS12_bio(struct bio_st *, PKCS12 *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def i2d_PKCS7_bio():
        'int i2d_PKCS7_bio(struct bio_st *, PKCS7 *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def i2d_PKCS8PrivateKey_bio():
        'int i2d_PKCS8PrivateKey_bio(struct bio_st *, EVP_PKEY *, EVP_CIPHER *, char *, int, int(*)(char *, int, int, void *), void *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def i2d_PKCS8PrivateKey_nid_bio():
        'int i2d_PKCS8PrivateKey_nid_bio(struct bio_st *, EVP_PKEY *, int, char *, int, int(*)(char *, int, int, void *), void *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def i2d_PUBKEY_bio():
        'int i2d_PUBKEY_bio(struct bio_st *, EVP_PKEY *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def i2d_PrivateKey_bio():
        'int i2d_PrivateKey_bio(struct bio_st *, EVP_PKEY *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def i2d_RSAPrivateKey():
        'int i2d_RSAPrivateKey(RSA *, unsigned char * *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def i2d_RSAPrivateKey_bio():
        'int i2d_RSAPrivateKey_bio(struct bio_st *, RSA *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def i2d_RSAPublicKey():
        'int i2d_RSAPublicKey(RSA *, unsigned char * *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def i2d_RSAPublicKey_bio():
        'int i2d_RSAPublicKey_bio(struct bio_st *, RSA *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def i2d_RSA_PUBKEY():
        'int i2d_RSA_PUBKEY(RSA *, unsigned char * *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def i2d_RSA_PUBKEY_bio():
        'int i2d_RSA_PUBKEY_bio(struct bio_st *, RSA *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def i2d_X509():
        'int i2d_X509(X509 *, unsigned char * *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def i2d_X509_CINF():
        'int i2d_X509_CINF(X509_CINF *, unsigned char * *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def i2d_X509_CRL_INFO():
        'int i2d_X509_CRL_INFO(X509_CRL_INFO *, unsigned char * *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def i2d_X509_CRL_bio():
        'int i2d_X509_CRL_bio(struct bio_st *, X509_CRL *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def i2d_X509_NAME():
        'int i2d_X509_NAME(X509_NAME *, unsigned char * *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def i2d_X509_REQ_INFO():
        'int i2d_X509_REQ_INFO(X509_REQ_INFO *, unsigned char * *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def i2d_X509_REQ_bio():
        'int i2d_X509_REQ_bio(struct bio_st *, X509_REQ *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def i2d_X509_bio():
        'int i2d_X509_bio(struct bio_st *, X509 *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def i2d_re_X509_CRL_tbs():
        'int i2d_re_X509_CRL_tbs(X509_CRL *, unsigned char * *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def i2d_re_X509_REQ_tbs():
        'int i2d_re_X509_REQ_tbs(X509_REQ *, unsigned char * *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def i2d_re_X509_tbs():
        'int i2d_re_X509_tbs(X509 *, unsigned char * *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def i2o_ECPublicKey():
        'int i2o_ECPublicKey(EC_KEY *, unsigned char * *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def o2i_ECPublicKey():
        'EC_KEY *o2i_ECPublicKey(EC_KEY * *, unsigned char * *, long);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_ACCESS_DESCRIPTION_free():
        'void sk_ACCESS_DESCRIPTION_free(Cryptography_STACK_OF_ACCESS_DESCRIPTION *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_ACCESS_DESCRIPTION_new_null():
        'Cryptography_STACK_OF_ACCESS_DESCRIPTION *sk_ACCESS_DESCRIPTION_new_null();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_ACCESS_DESCRIPTION_num():
        'int sk_ACCESS_DESCRIPTION_num(Cryptography_STACK_OF_ACCESS_DESCRIPTION *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_ACCESS_DESCRIPTION_push():
        'int sk_ACCESS_DESCRIPTION_push(Cryptography_STACK_OF_ACCESS_DESCRIPTION *, ACCESS_DESCRIPTION *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_ACCESS_DESCRIPTION_value():
        'ACCESS_DESCRIPTION *sk_ACCESS_DESCRIPTION_value(Cryptography_STACK_OF_ACCESS_DESCRIPTION *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_ASN1_INTEGER_free():
        'void sk_ASN1_INTEGER_free(Cryptography_STACK_OF_ASN1_INTEGER *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_ASN1_INTEGER_new_null():
        'Cryptography_STACK_OF_ASN1_INTEGER *sk_ASN1_INTEGER_new_null();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_ASN1_INTEGER_num():
        'int sk_ASN1_INTEGER_num(Cryptography_STACK_OF_ASN1_INTEGER *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_ASN1_INTEGER_push():
        'int sk_ASN1_INTEGER_push(Cryptography_STACK_OF_ASN1_INTEGER *, ASN1_INTEGER *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_ASN1_INTEGER_value():
        'ASN1_INTEGER *sk_ASN1_INTEGER_value(Cryptography_STACK_OF_ASN1_INTEGER *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_ASN1_OBJECT_free():
        'void sk_ASN1_OBJECT_free(Cryptography_STACK_OF_ASN1_OBJECT *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_ASN1_OBJECT_new_null():
        'Cryptography_STACK_OF_ASN1_OBJECT *sk_ASN1_OBJECT_new_null();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_ASN1_OBJECT_num():
        'int sk_ASN1_OBJECT_num(Cryptography_STACK_OF_ASN1_OBJECT *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_ASN1_OBJECT_push():
        'int sk_ASN1_OBJECT_push(Cryptography_STACK_OF_ASN1_OBJECT *, ASN1_OBJECT *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_ASN1_OBJECT_value():
        'ASN1_OBJECT *sk_ASN1_OBJECT_value(Cryptography_STACK_OF_ASN1_OBJECT *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_DIST_POINT_free():
        'void sk_DIST_POINT_free(Cryptography_STACK_OF_DIST_POINT *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_DIST_POINT_new_null():
        'Cryptography_STACK_OF_DIST_POINT *sk_DIST_POINT_new_null();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_DIST_POINT_num():
        'int sk_DIST_POINT_num(Cryptography_STACK_OF_DIST_POINT *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_DIST_POINT_pop_free():
        'void sk_DIST_POINT_pop_free(Cryptography_STACK_OF_DIST_POINT *, void(*)(DIST_POINT *));\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_DIST_POINT_push():
        'int sk_DIST_POINT_push(Cryptography_STACK_OF_DIST_POINT *, DIST_POINT *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_DIST_POINT_value():
        'DIST_POINT *sk_DIST_POINT_value(Cryptography_STACK_OF_DIST_POINT *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_GENERAL_NAME_num():
        'int sk_GENERAL_NAME_num(struct stack_st_GENERAL_NAME *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_GENERAL_NAME_pop_free():
        'void sk_GENERAL_NAME_pop_free(struct stack_st_GENERAL_NAME *, void(*)(GENERAL_NAME *));\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_GENERAL_NAME_push():
        'int sk_GENERAL_NAME_push(struct stack_st_GENERAL_NAME *, GENERAL_NAME *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_GENERAL_NAME_value():
        'GENERAL_NAME *sk_GENERAL_NAME_value(struct stack_st_GENERAL_NAME *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_GENERAL_SUBTREE_free():
        'void sk_GENERAL_SUBTREE_free(Cryptography_STACK_OF_GENERAL_SUBTREE *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_GENERAL_SUBTREE_new_null():
        'Cryptography_STACK_OF_GENERAL_SUBTREE *sk_GENERAL_SUBTREE_new_null();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_GENERAL_SUBTREE_num():
        'int sk_GENERAL_SUBTREE_num(Cryptography_STACK_OF_GENERAL_SUBTREE *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_GENERAL_SUBTREE_push():
        'int sk_GENERAL_SUBTREE_push(Cryptography_STACK_OF_GENERAL_SUBTREE *, GENERAL_SUBTREE *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_GENERAL_SUBTREE_value():
        'GENERAL_SUBTREE *sk_GENERAL_SUBTREE_value(Cryptography_STACK_OF_GENERAL_SUBTREE *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_POLICYINFO_free():
        'void sk_POLICYINFO_free(Cryptography_STACK_OF_POLICYINFO *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_POLICYINFO_new_null():
        'Cryptography_STACK_OF_POLICYINFO *sk_POLICYINFO_new_null();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_POLICYINFO_num():
        'int sk_POLICYINFO_num(Cryptography_STACK_OF_POLICYINFO *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_POLICYINFO_pop_free():
        'void sk_POLICYINFO_pop_free(Cryptography_STACK_OF_POLICYINFO *, void(*)(POLICYINFO *));\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_POLICYINFO_push():
        'int sk_POLICYINFO_push(Cryptography_STACK_OF_POLICYINFO *, POLICYINFO *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_POLICYINFO_value():
        'POLICYINFO *sk_POLICYINFO_value(Cryptography_STACK_OF_POLICYINFO *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_POLICYQUALINFO_free():
        'void sk_POLICYQUALINFO_free(Cryptography_STACK_OF_POLICYQUALINFO *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_POLICYQUALINFO_new_null():
        'Cryptography_STACK_OF_POLICYQUALINFO *sk_POLICYQUALINFO_new_null();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_POLICYQUALINFO_num():
        'int sk_POLICYQUALINFO_num(Cryptography_STACK_OF_POLICYQUALINFO *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_POLICYQUALINFO_push():
        'int sk_POLICYQUALINFO_push(Cryptography_STACK_OF_POLICYQUALINFO *, POLICYQUALINFO *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_POLICYQUALINFO_value():
        'POLICYQUALINFO *sk_POLICYQUALINFO_value(Cryptography_STACK_OF_POLICYQUALINFO *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_SCT_num():
        'int sk_SCT_num(Cryptography_STACK_OF_SCT *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_SCT_value():
        'SCT *sk_SCT_value(Cryptography_STACK_OF_SCT *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_SSL_CIPHER_num():
        'int sk_SSL_CIPHER_num(Cryptography_STACK_OF_SSL_CIPHER *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_SSL_CIPHER_value():
        'SSL_CIPHER *sk_SSL_CIPHER_value(Cryptography_STACK_OF_SSL_CIPHER *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_X509_CRL_free():
        'void sk_X509_CRL_free(Cryptography_STACK_OF_X509_CRL *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_X509_CRL_new_null():
        'Cryptography_STACK_OF_X509_CRL *sk_X509_CRL_new_null();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_X509_CRL_num():
        'int sk_X509_CRL_num(Cryptography_STACK_OF_X509_CRL *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_X509_CRL_push():
        'int sk_X509_CRL_push(Cryptography_STACK_OF_X509_CRL *, X509_CRL *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_X509_CRL_value():
        'X509_CRL *sk_X509_CRL_value(Cryptography_STACK_OF_X509_CRL *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_X509_EXTENSION_delete():
        'X509_EXTENSION *sk_X509_EXTENSION_delete(X509_EXTENSIONS *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_X509_EXTENSION_free():
        'void sk_X509_EXTENSION_free(X509_EXTENSIONS *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_X509_EXTENSION_insert():
        'int sk_X509_EXTENSION_insert(X509_EXTENSIONS *, X509_EXTENSION *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_X509_EXTENSION_new_null():
        'X509_EXTENSIONS *sk_X509_EXTENSION_new_null();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_X509_EXTENSION_num():
        'int sk_X509_EXTENSION_num(X509_EXTENSIONS *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_X509_EXTENSION_push():
        'int sk_X509_EXTENSION_push(X509_EXTENSIONS *, X509_EXTENSION *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_X509_EXTENSION_value():
        'X509_EXTENSION *sk_X509_EXTENSION_value(X509_EXTENSIONS *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_X509_NAME_ENTRY_dup():
        'Cryptography_STACK_OF_X509_NAME_ENTRY *sk_X509_NAME_ENTRY_dup(Cryptography_STACK_OF_X509_NAME_ENTRY *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_X509_NAME_ENTRY_new_null():
        'Cryptography_STACK_OF_X509_NAME_ENTRY *sk_X509_NAME_ENTRY_new_null();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_X509_NAME_ENTRY_num():
        'int sk_X509_NAME_ENTRY_num(Cryptography_STACK_OF_X509_NAME_ENTRY *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_X509_NAME_ENTRY_push():
        'int sk_X509_NAME_ENTRY_push(Cryptography_STACK_OF_X509_NAME_ENTRY *, X509_NAME_ENTRY *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_X509_NAME_ENTRY_value():
        'X509_NAME_ENTRY *sk_X509_NAME_ENTRY_value(Cryptography_STACK_OF_X509_NAME_ENTRY *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_X509_NAME_free():
        'void sk_X509_NAME_free(Cryptography_STACK_OF_X509_NAME *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_X509_NAME_new_null():
        'Cryptography_STACK_OF_X509_NAME *sk_X509_NAME_new_null();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_X509_NAME_num():
        'int sk_X509_NAME_num(Cryptography_STACK_OF_X509_NAME *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_X509_NAME_push():
        'int sk_X509_NAME_push(Cryptography_STACK_OF_X509_NAME *, X509_NAME *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_X509_NAME_value():
        'X509_NAME *sk_X509_NAME_value(Cryptography_STACK_OF_X509_NAME *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_X509_OBJECT_num():
        'int sk_X509_OBJECT_num(Cryptography_STACK_OF_X509_OBJECT *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_X509_OBJECT_value():
        'X509_OBJECT *sk_X509_OBJECT_value(Cryptography_STACK_OF_X509_OBJECT *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_X509_REVOKED_num():
        'int sk_X509_REVOKED_num(Cryptography_STACK_OF_X509_REVOKED *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_X509_REVOKED_value():
        'X509_REVOKED *sk_X509_REVOKED_value(Cryptography_STACK_OF_X509_REVOKED *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_X509_free():
        'void sk_X509_free(Cryptography_STACK_OF_X509 *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_X509_new_null():
        'Cryptography_STACK_OF_X509 *sk_X509_new_null();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_X509_num():
        'int sk_X509_num(Cryptography_STACK_OF_X509 *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_X509_push():
        'int sk_X509_push(Cryptography_STACK_OF_X509 *, X509 *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_X509_value():
        'X509 *sk_X509_value(Cryptography_STACK_OF_X509 *, int);\n\nCFFI C function from _openssl.lib'
        pass
    

