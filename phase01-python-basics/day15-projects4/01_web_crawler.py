import requests
from bs4 import BeautifulSoup
import os
import json
import logging
import time

# 基础配置
BASE_URL = 'https://www.sudugu.org'
CATEGORY_URL = 'https://www.sudugu.org/fenlei/'

# 目录配置
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
NOVELS_DIR = os.path.join(SCRIPT_DIR, 'novels')
LOGS_DIR = os.path.join(SCRIPT_DIR, 'logs')
PROGRESS_DIR = os.path.join(SCRIPT_DIR, 'progress')

# 创建必要的目录
for directory in [NOVELS_DIR, LOGS_DIR, PROGRESS_DIR]:
    if not os.path.exists(directory):
        os.makedirs(directory)

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(os.path.join(LOGS_DIR, 'crawler.log'), encoding='utf-8'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# 进度文件路径
PROGRESS_FILE = os.path.join(PROGRESS_DIR, 'progress.json')

# 浏览器模拟
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

def get_response(url, max_retries=3):
    """获取网页响应，带重试机制"""
    retry = 0
    while retry < max_retries:
        try:
            response = requests.get(url, headers=HEADERS, timeout=10)
            if response.status_code == 200:
                return response
            else:
                logger.warning(f"请求失败，状态码: {response.status_code}, URL: {url}")
                retry += 1
                time.sleep(2)
        except Exception as e:
            logger.error(f"请求异常: {str(e)}, URL: {url}")
            retry += 1
            time.sleep(2)
    logger.error(f"获取页面失败: {url}")
    return None

def get_categories():
    """获取小说分类"""
    logger.info("开始获取小说分类")
    response = get_response(CATEGORY_URL)
    if not response:
        logger.error("获取分类页面失败")
        return []
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # 查找分类链接
    categories = []
    # 从导航菜单中提取分类
    nav_menu = soup.select_one('div.menu ul')
    if nav_menu:
        links = nav_menu.select('a')
        for link in links:
            href = link.get('href')
            text = link.text.strip()
            if href and '小说' in text and href != '/fenlei/':
                # 提取分类名称和URL
                category_name = text
                category_url = BASE_URL + href if not href.startswith('http') else href
                categories.append({
                    'name': category_name,
                    'url': category_url
                })
    
    logger.info(f"成功获取 {len(categories)} 个分类")
    return categories

def get_novels(category_url, category_name):
    """获取分类下的小说列表"""
    logger.info(f"开始获取 {category_name} 分类的小说列表")
    novels = []
    page = 1
    
    while True:
        # 构建分页URL
        if page == 1:
            url = category_url
        else:
            url = f"{category_url}{page}.html"
        
        logger.info(f"爬取页面: {url}")
        response = get_response(url)
        if not response:
            break
        
        # 保存页面内容到日志目录，便于调试
        page_file = os.path.join(LOGS_DIR, f"{category_name}_page{page}.html")
        with open(page_file, 'w', encoding='utf-8') as f:
            f.write(response.text)
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 查找小说列表
        # 尝试不同的选择器
        novel_elements = soup.select('.item a')
        logger.info(f"使用选择器 .item a 找到 {len(novel_elements)} 个小说元素")
        
        if not novel_elements:
            novel_elements = soup.select('.list a')
            logger.info(f"使用选择器 .list a 找到 {len(novel_elements)} 个小说元素")
        
        # 提取小说信息
        novel_count = 0
        for i, element in enumerate(novel_elements):
            href = element.get('href')
            text = element.text.strip()
            
            # 过滤无效链接
            if not href or not text or 'http' in href or '#' in href:
                continue
            
            # 构建完整的小说URL
            if not href.startswith('http'):
                novel_url = BASE_URL + href
            else:
                novel_url = href
            
            # 过滤章节链接和作者链接
            if '/chapter/' in novel_url or '/author/' in novel_url or '.html' in novel_url:
                continue
            
            # 检查小说是否已经添加
            novel_exists = False
            for novel in novels:
                if novel['url'] == novel_url:
                    novel_exists = True
                    break
            
            if not novel_exists:
                novels.append({
                    'name': text,
                    'url': novel_url
                })
                novel_count += 1
                logger.info(f"小说 {novel_count}: {text} - {href}")
        
        if novel_count == 0:
            logger.warning(f"未找到小说元素，停止爬取")
            break
        
        # 检查是否有下一页
        next_page = soup.select_one('a[class*="next"]') or soup.select_one('a:-soup-contains("下一页")')
        if not next_page:
            break
        
        page += 1
        # 避免请求过快
        time.sleep(1)
    
    logger.info(f"成功获取 {category_name} 分类的 {len(novels)} 本小说")
    return novels

def get_txt_download_url(novel_url):
    """获取小说的TXT下载链接"""
    logger.info(f"获取小说详情: {novel_url}")
    response = get_response(novel_url)
    if not response:
        logger.error(f"获取小说详情失败: {novel_url}")
        return None
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # 查找下载链接
    download_links = soup.select('a[href*="download"]') 
    if not download_links:
        download_links = soup.select('a:-soup-contains("下载")')
    
    for link in download_links:
        href = link.get('href')
        if href:
            if not href.startswith('http'):
                href = BASE_URL + href
            # 检查是否为TXT下载链接
            if 'txt' in href.lower() or 'download' in href.lower():
                # 如果是txt.html页面，需要进一步提取实际的TXT文件链接
                if 'txt.html' in href:
                    logger.info(f"获取TXT下载页面: {href}")
                    txt_response = get_response(href)
                    if txt_response:
                        txt_soup = BeautifulSoup(txt_response.text, 'html.parser')
                        # 查找实际的TXT文件链接，从id="list"或class="dir"中提取
                        dir_div = txt_soup.select_one('#list')
                        if not dir_div:
                            dir_div = txt_soup.select_one('.dir')
                        if dir_div:
                            actual_links = dir_div.select('a')
                            for actual_link in actual_links:
                                actual_href = actual_link.get('href')
                                if actual_href and '/txt/' in actual_href:
                                    if not actual_href.startswith('http'):
                                        actual_href = BASE_URL + actual_href
                                    logger.info(f"找到实际TXT下载链接: {actual_href}")
                                    return actual_href
    
    logger.warning(f"未找到TXT下载链接: {novel_url}")
    return None

def download_txt(url, save_path):
    """下载TXT文件"""
    logger.info(f"开始下载TXT文件: {url}")
    response = get_response(url)
    if not response:
        logger.error(f"下载TXT文件失败: {url}")
        return False
    
    # 确保目录存在
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    
    # 保存文件
    try:
        with open(save_path, 'w', encoding='utf-8') as f:
            f.write(response.text)
        logger.info(f"下载成功: {save_path}")
        return True
    except Exception as e:
        logger.error(f"保存TXT文件失败: {str(e)}")
        return False

def load_progress():
    """加载爬取进度"""
    if os.path.exists(PROGRESS_FILE):
        try:
            with open(PROGRESS_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            logger.error(f"加载进度文件失败: {str(e)}")
            return {}
    return {}

def save_progress(progress):
    """保存爬取进度"""
    try:
        with open(PROGRESS_FILE, 'w', encoding='utf-8') as f:
            json.dump(progress, f, ensure_ascii=False, indent=2)
        logger.info("进度保存成功")
    except Exception as e:
        logger.error(f"保存进度文件失败: {str(e)}")

def main():
    """主函数"""
    # 加载进度
    progress = load_progress()
    
    # 获取分类
    categories = get_categories()
    
    # 遍历分类
    for category in categories:
        category_name = category['name']
        category_url = category['url']
        
        # 检查分类是否已爬取
        if category_name in progress and progress[category_name]['completed']:
            logger.info(f"分类 {category_name} 已爬取完成，跳过")
            continue
        
        # 获取小说列表
        novels = get_novels(category_url, category_name)
        
        # 初始化分类进度
        if category_name not in progress:
            progress[category_name] = {
                'completed': False,
                'novels': []
            }
        
        # 遍历小说
        for novel in novels:
            novel_name = novel['name']
            novel_url = novel['url']
            
            # 检查小说是否已下载
            novel_exists = False
            for downloaded_novel in progress[category_name]['novels']:
                if downloaded_novel['url'] == novel_url:
                    novel_exists = True
                    break
            
            if novel_exists:
                logger.info(f"小说 {novel_name} 已下载，跳过")
                continue
            
            # 检查小说是否属于当前分类
            # 获取小说详情页，提取分类信息
            response = get_response(novel_url)
            if response:
                soup = BeautifulSoup(response.text, 'html.parser')
                # 查找小说分类信息
                # 尝试不同的选择器来找到分类信息
                category_elements = soup.select('p span') or soup.select('div[class*="info"] span') or soup.select('span[class*="category"]')
                
                novel_category = ""
                for element in category_elements:
                    text = element.text.strip()
                    if '小说' in text:
                        novel_category = text
                        break
                
                # 检查小说分类是否与当前分类匹配
                if category_name not in novel_category:
                    logger.info(f"小说 {novel_name} 实际分类为 {novel_category}，不属于 {category_name} 分类，跳过")
                    continue
                else:
                    logger.info(f"小说 {novel_name} 属于 {category_name} 分类，开始下载")
            else:
                logger.warning(f"无法获取小说详情页，跳过分类验证")
                logger.info(f"小说 {novel_name} 属于 {category_name} 分类，开始下载")
            
            # 获取TXT下载链接
            txt_url = get_txt_download_url(novel_url)
            if not txt_url:
                logger.warning(f"未找到TXT下载链接，跳过: {novel_name}")
                continue
            
            # 构建保存路径
            category_dir = os.path.join(NOVELS_DIR, category_name)
            save_path = os.path.join(category_dir, f"{novel_name}.txt")
            
            # 下载TXT文件
            if download_txt(txt_url, save_path):
                # 记录下载进度
                progress[category_name]['novels'].append({
                    'name': novel_name,
                    'url': novel_url
                })
                # 保存进度
                save_progress(progress)
                # 记录日志信息
                logger.info(f"小说类型: {category_name}, 小说名称: {novel_name}, URL: {novel_url}")
            
            # 避免请求过快
            time.sleep(2)
        
        # 标记分类为已完成
        progress[category_name]['completed'] = True
        save_progress(progress)
    
    logger.info("所有分类爬取完成")

if __name__ == '__main__':
    main()
