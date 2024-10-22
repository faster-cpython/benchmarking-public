# Results vs. 3.13.0

- fork: python
- ref: v3.13.0a4
- machine: linux-x86_64
- commit hash: 9d34f60
- commit date: 2024-02-15
- overall geometric mean: 1.03x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.96x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 269 ms: 1.02x slower                                       |
| docutils       | 2.58 sec                                               | 2.65 sec: 1.03x slower                                     |
| html5lib       | 64.5 ms                                                | 67.4 ms: 1.04x slower                                      |
| tornado_http   | 91.5 ms                                                | 97.1 ms: 1.06x slower                                      |
| Geometric mean | (ref)                                                  | 1.03x slower                                               |

Benchmark hidden because not significant (1): chameleon

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| asyncio_websockets         | 555 ms                                                 | 563 ms: 1.01x slower                                       |
| coroutines                 | 22.5 ms                                                | 23.0 ms: 1.02x slower                                      |
| asyncio_tcp                | 488 ms                                                 | 501 ms: 1.03x slower                                       |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.84 sec: 1.03x slower                                     |
| async_generators           | 433 ms                                                 | 459 ms: 1.06x slower                                       |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 718 ms: 1.25x slower                                       |
| async_tree_none            | 354 ms                                                 | 444 ms: 1.25x slower                                       |
| async_tree_memoization_tg  | 465 ms                                                 | 585 ms: 1.26x slower                                       |
| async_tree_memoization     | 442 ms                                                 | 571 ms: 1.29x slower                                       |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 733 ms: 1.35x slower                                       |
| async_tree_none_tg         | 320 ms                                                 | 455 ms: 1.42x slower                                       |
| async_tree_io              | 843 ms                                                 | 1.20 sec: 1.43x slower                                     |
| async_tree_io_tg           | 825 ms                                                 | 1.22 sec: 1.48x slower                                     |
| Geometric mean             | (ref)                                                  | 1.21x slower                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pidigits       | 186 ms                                                 | 189 ms: 1.02x slower                                       |
| float          | 78.5 ms                                                | 83.1 ms: 1.06x slower                                      |
| nbody          | 85.7 ms                                                | 92.1 ms: 1.07x slower                                      |
| Geometric mean | (ref)                                                  | 1.05x slower                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.66 ms: 1.06x faster                                      |
| regex_v8       | 25.3 ms                                                | 24.4 ms: 1.03x faster                                      |
| regex_compile  | 131 ms                                                 | 132 ms: 1.00x slower                                       |
| regex_dna      | 220 ms                                                 | 224 ms: 1.02x slower                                       |
| Geometric mean | (ref)                                                  | 1.02x faster                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| xml_etree_process    | 60.4 ms                                                | 59.3 ms: 1.02x faster                                      |
| pickle_pure_python   | 300 us                                                 | 302 us: 1.00x slower                                       |
| unpickle_pure_python | 213 us                                                 | 217 us: 1.01x slower                                       |
| unpickle_list        | 4.96 us                                                | 5.09 us: 1.03x slower                                      |
| xml_etree_parse      | 156 ms                                                 | 160 ms: 1.03x slower                                       |
| unpickle             | 14.9 us                                                | 15.4 us: 1.03x slower                                      |
| json_loads           | 27.0 us                                                | 27.9 us: 1.04x slower                                      |
| pickle               | 11.6 us                                                | 12.0 us: 1.04x slower                                      |
| tomli_loads          | 2.11 sec                                               | 2.20 sec: 1.04x slower                                     |
| pickle_dict          | 33.2 us                                                | 34.7 us: 1.05x slower                                      |
| xml_etree_iterparse  | 102 ms                                                 | 107 ms: 1.05x slower                                       |
| pickle_list          | 5.01 us                                                | 5.28 us: 1.05x slower                                      |
| Geometric mean       | (ref)                                                  | 1.03x slower                                               |

Benchmark hidden because not significant (2): xml_etree_generate, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.3 ms: 1.03x faster                                      |
| python_startup_no_site | 6.99 ms                                                | 8.87 ms: 1.27x slower                                      |
| Geometric mean         | (ref)                                                  | 1.11x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| django_template | 34.4 ms                                                | 34.7 ms: 1.01x slower                                      |
| mako            | 11.1 ms                                                | 11.2 ms: 1.01x slower                                      |
| genshi_xml      | 50.3 ms                                                | 52.8 ms: 1.05x slower                                      |
| Geometric mean  | (ref)                                                  | 1.02x slower                                               |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| typing_runtime_protocols   | 159 us                                                 | 112 us: 1.42x faster                                       |
| mypy2                      | 1.07 sec                                               | 865 ms: 1.24x faster                                       |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.64 ms: 1.08x faster                                      |
| gc_traversal               | 3.81 ms                                                | 3.55 ms: 1.07x faster                                      |
| create_gc_cycles           | 1.61 ms                                                | 1.51 ms: 1.07x faster                                      |
| regex_effbot               | 3.88 ms                                                | 3.66 ms: 1.06x faster                                      |
| mdp                        | 2.74 sec                                               | 2.61 sec: 1.05x faster                                     |
| logging_silent             | 102 ns                                                 | 97.7 ns: 1.04x faster                                      |
| flaskblogging              | 9.11 ms                                                | 8.75 ms: 1.04x faster                                      |
| spectral_norm              | 115 ms                                                 | 111 ms: 1.04x faster                                       |
| deepcopy_reduce            | 3.17 us                                                | 3.06 us: 1.04x faster                                      |
| regex_v8                   | 25.3 ms                                                | 24.4 ms: 1.03x faster                                      |
| scimark_fft                | 369 ms                                                 | 359 ms: 1.03x faster                                       |
| python_startup             | 10.6 ms                                                | 10.3 ms: 1.03x faster                                      |
| scimark_lu                 | 115 ms                                                 | 113 ms: 1.02x faster                                       |
| xml_etree_process          | 60.4 ms                                                | 59.3 ms: 1.02x faster                                      |
| go                         | 142 ms                                                 | 139 ms: 1.02x faster                                       |
| deepcopy                   | 352 us                                                 | 347 us: 1.02x faster                                       |
| pprint_safe_repr           | 744 ms                                                 | 734 ms: 1.01x faster                                       |
| crypto_pyaes               | 73.0 ms                                                | 72.0 ms: 1.01x faster                                      |
| comprehensions             | 16.4 us                                                | 16.2 us: 1.01x faster                                      |
| bench_mp_pool              | 24.0 ms                                                | 23.8 ms: 1.01x faster                                      |
| richards_super             | 54.4 ms                                                | 54.1 ms: 1.01x faster                                      |
| regex_compile              | 131 ms                                                 | 132 ms: 1.00x slower                                       |
| nqueens                    | 80.6 ms                                                | 81.0 ms: 1.00x slower                                      |
| pickle_pure_python         | 300 us                                                 | 302 us: 1.00x slower                                       |
| sympy_sum                  | 150 ms                                                 | 150 ms: 1.01x slower                                       |
| sqlglot_optimize           | 53.9 ms                                                | 54.2 ms: 1.01x slower                                      |
| sqlglot_normalize          | 107 ms                                                 | 108 ms: 1.01x slower                                       |
| meteor_contest             | 108 ms                                                 | 108 ms: 1.01x slower                                       |
| sqlglot_transpile          | 1.57 ms                                                | 1.58 ms: 1.01x slower                                      |
| django_template            | 34.4 ms                                                | 34.7 ms: 1.01x slower                                      |
| mako                       | 11.1 ms                                                | 11.2 ms: 1.01x slower                                      |
| hexiom                     | 6.13 ms                                                | 6.20 ms: 1.01x slower                                      |
| thrift                     | 796 us                                                 | 807 us: 1.01x slower                                       |
| asyncio_websockets         | 555 ms                                                 | 563 ms: 1.01x slower                                       |
| scimark_monte_carlo        | 66.3 ms                                                | 67.2 ms: 1.01x slower                                      |
| raytrace                   | 262 ms                                                 | 265 ms: 1.01x slower                                       |
| unpickle_pure_python       | 213 us                                                 | 217 us: 1.01x slower                                       |
| 2to3                       | 265 ms                                                 | 269 ms: 1.02x slower                                       |
| pidigits                   | 186 ms                                                 | 189 ms: 1.02x slower                                       |
| regex_dna                  | 220 ms                                                 | 224 ms: 1.02x slower                                       |
| coroutines                 | 22.5 ms                                                | 23.0 ms: 1.02x slower                                      |
| docutils                   | 2.58 sec                                               | 2.65 sec: 1.03x slower                                     |
| unpickle_list              | 4.96 us                                                | 5.09 us: 1.03x slower                                      |
| aiohttp                    | 1.14 ms                                                | 1.17 ms: 1.03x slower                                      |
| asyncio_tcp                | 488 ms                                                 | 501 ms: 1.03x slower                                       |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.84 sec: 1.03x slower                                     |
| pycparser                  | 1.19 sec                                               | 1.23 sec: 1.03x slower                                     |
| xml_etree_parse            | 156 ms                                                 | 160 ms: 1.03x slower                                       |
| deltablue                  | 3.15 ms                                                | 3.24 ms: 1.03x slower                                      |
| logging_simple             | 5.66 us                                                | 5.83 us: 1.03x slower                                      |
| bench_thread_pool          | 815 us                                                 | 838 us: 1.03x slower                                       |
| pyflate                    | 460 ms                                                 | 474 ms: 1.03x slower                                       |
| unpickle                   | 14.9 us                                                | 15.4 us: 1.03x slower                                      |
| json_loads                 | 27.0 us                                                | 27.9 us: 1.04x slower                                      |
| gunicorn                   | 1.23 ms                                                | 1.27 ms: 1.04x slower                                      |
| pickle                     | 11.6 us                                                | 12.0 us: 1.04x slower                                      |
| tomli_loads                | 2.11 sec                                               | 2.20 sec: 1.04x slower                                     |
| html5lib                   | 64.5 ms                                                | 67.4 ms: 1.04x slower                                      |
| logging_format             | 6.25 us                                                | 6.53 us: 1.04x slower                                      |
| pickle_dict                | 33.2 us                                                | 34.7 us: 1.05x slower                                      |
| chaos                      | 58.4 ms                                                | 61.2 ms: 1.05x slower                                      |
| xml_etree_iterparse        | 102 ms                                                 | 107 ms: 1.05x slower                                       |
| genshi_xml                 | 50.3 ms                                                | 52.8 ms: 1.05x slower                                      |
| generators                 | 28.8 ms                                                | 30.3 ms: 1.05x slower                                      |
| scimark_sor                | 122 ms                                                 | 129 ms: 1.05x slower                                       |
| fannkuch                   | 381 ms                                                 | 401 ms: 1.05x slower                                       |
| pickle_list                | 5.01 us                                                | 5.28 us: 1.05x slower                                      |
| float                      | 78.5 ms                                                | 83.1 ms: 1.06x slower                                      |
| async_generators           | 433 ms                                                 | 459 ms: 1.06x slower                                       |
| tornado_http               | 91.5 ms                                                | 97.1 ms: 1.06x slower                                      |
| dulwich_log                | 63.0 ms                                                | 67.0 ms: 1.06x slower                                      |
| nbody                      | 85.7 ms                                                | 92.1 ms: 1.07x slower                                      |
| pathlib                    | 17.1 ms                                                | 18.7 ms: 1.10x slower                                      |
| coverage                   | 83.7 ms                                                | 96.3 ms: 1.15x slower                                      |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 718 ms: 1.25x slower                                       |
| async_tree_none            | 354 ms                                                 | 444 ms: 1.25x slower                                       |
| async_tree_memoization_tg  | 465 ms                                                 | 585 ms: 1.26x slower                                       |
| python_startup_no_site     | 6.99 ms                                                | 8.87 ms: 1.27x slower                                      |
| async_tree_memoization     | 442 ms                                                 | 571 ms: 1.29x slower                                       |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 733 ms: 1.35x slower                                       |
| async_tree_none_tg         | 320 ms                                                 | 455 ms: 1.42x slower                                       |
| async_tree_io              | 843 ms                                                 | 1.20 sec: 1.43x slower                                     |
| async_tree_io_tg           | 825 ms                                                 | 1.22 sec: 1.48x slower                                     |
| Geometric mean             | (ref)                                                  | 1.03x slower                                               |

Benchmark hidden because not significant (16): djangocms, pylint, telco, deepcopy_memo, sqlglot_parse, json, pprint_pformat, xml_etree_generate, sympy_integrate, richards, chameleon, sympy_expand, sympy_str, json_dumps, genshi_text, sqlite_synth
Ignored benchmarks (3) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: bpe_tokeniser, dask, unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.96x