import streamlit as st
import math


def main():
    st.title('الآلة الحاسبة')

    # اختيار نوع العملية
    operation = st.selectbox('اختر العملية:', [
        'الجمع (+)',
        'الطرح (-)',
        'الضرب (×)',
        'القسمة (÷)',
        'الأس (^)',
        'الجذر التربيعي (√)'
    ])

    # إدخال الأرقام
    if operation != 'الجذر التربيعي (√)':
        num1 = st.number_input('أدخل الرقم الأول', value=0.0)
        num2 = st.number_input('أدخل الرقم الثاني', value=0.0)
    else:
        num1 = st.number_input('أدخل الرقم', value=0.0)
        num2 = 0

    # زر الحساب
    if st.button('احسب'):
        try:
            # حساب النتيجة حسب العملية
            if operation == 'الجمع (+)':
                result = num1 + num2
            elif operation == 'الطرح (-)':
                result = num1 - num2
            elif operation == 'الضرب (×)':
                result = num1 * num2
            elif operation == 'القسمة (÷)':
                if num2 != 0:
                    result = num1 / num2
                else:
                    st.error('خطأ: لا يمكن القسمة على الصفر')
                    return
            elif operation == 'الأس (^)':
                result = math.pow(num1, num2)
            elif operation == 'الجذر التربيعي (√)':
                result = math.sqrt(num1)

            # عرض النتيجة
            st.success(f'النتيجة: {result}')

        except Exception as e:
            st.error(f'حدث خطأ: {str(e)}')


if __name__ == '__main__':
    main()