# Results vs. 3.13.0

- fork: python
- ref: v3.13.0a1
- machine: linux-x86_64
- commit hash: ad056f0
- commit date: 2023-10-13
- overall geometric mean: 1.11x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: 0.57x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231013-linux-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 276 ms: 1.04x slower                                       |
| chameleon      | 6.85 ms                                                | 7.13 ms: 1.04x slower                                      |
| docutils       | 2.58 sec                                               | 2.71 sec: 1.05x slower                                     |
| html5lib       | 64.5 ms                                                | 67.3 ms: 1.04x slower                                      |
| tornado_http   | 91.5 ms                                                | 99.1 ms: 1.08x slower                                      |
| Geometric mean | (ref)                                                  | 1.05x slower                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231013-linux-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| asyncio_websockets         | 555 ms                                                 | 563 ms: 1.01x slower                                       |
| asyncio_tcp                | 488 ms                                                 | 498 ms: 1.02x slower                                       |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.83 sec: 1.02x slower                                     |
| coroutines                 | 22.5 ms                                                | 23.7 ms: 1.05x slower                                      |
| async_generators           | 433 ms                                                 | 472 ms: 1.09x slower                                       |
| async_tree_none            | 354 ms                                                 | 446 ms: 1.26x slower                                       |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 726 ms: 1.26x slower                                       |
| async_tree_memoization     | 442 ms                                                 | 572 ms: 1.29x slower                                       |
| async_tree_memoization_tg  | 465 ms                                                 | 610 ms: 1.31x slower                                       |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 759 ms: 1.40x slower                                       |
| async_tree_io              | 843 ms                                                 | 1.21 sec: 1.44x slower                                     |
| async_tree_none_tg         | 320 ms                                                 | 463 ms: 1.45x slower                                       |
| async_tree_io_tg           | 825 ms                                                 | 1.25 sec: 1.51x slower                                     |
| Geometric mean             | (ref)                                                  | 1.23x slower                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231013-linux-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pidigits       | 186 ms                                                 | 190 ms: 1.02x slower                                       |
| float          | 78.5 ms                                                | 83.4 ms: 1.06x slower                                      |
| nbody          | 85.7 ms                                                | 95.7 ms: 1.12x slower                                      |
| Geometric mean | (ref)                                                  | 1.07x slower                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231013-linux-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.56 ms: 1.09x faster                                      |
| regex_dna      | 220 ms                                                 | 209 ms: 1.05x faster                                       |
| regex_compile  | 131 ms                                                 | 142 ms: 1.08x slower                                       |
| Geometric mean | (ref)                                                  | 1.01x faster                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231013-linux-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| json_dumps           | 10.4 ms                                                | 10.5 ms: 1.01x slower                                      |
| pickle               | 11.6 us                                                | 11.7 us: 1.01x slower                                      |
| xml_etree_generate   | 87.0 ms                                                | 87.7 ms: 1.01x slower                                      |
| pickle_pure_python   | 300 us                                                 | 307 us: 1.02x slower                                       |
| unpickle_list        | 4.96 us                                                | 5.08 us: 1.02x slower                                      |
| xml_etree_parse      | 156 ms                                                 | 160 ms: 1.03x slower                                       |
| json_loads           | 27.0 us                                                | 27.9 us: 1.03x slower                                      |
| pickle_list          | 5.01 us                                                | 5.21 us: 1.04x slower                                      |
| xml_etree_iterparse  | 102 ms                                                 | 107 ms: 1.05x slower                                       |
| unpickle_pure_python | 213 us                                                 | 226 us: 1.06x slower                                       |
| tomli_loads          | 2.11 sec                                               | 2.25 sec: 1.06x slower                                     |
| pickle_dict          | 33.2 us                                                | 35.4 us: 1.07x slower                                      |
| Geometric mean       | (ref)                                                  | 1.03x slower                                               |

Benchmark hidden because not significant (2): xml_etree_process, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231013-linux-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.4 ms: 1.02x faster                                      |
| python_startup_no_site | 6.99 ms                                                | 7.05 ms: 1.01x slower                                      |
| Geometric mean         | (ref)                                                  | 1.00x faster                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231013-linux-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| genshi_text     | 22.9 ms                                                | 23.1 ms: 1.01x slower                                      |
| django_template | 34.4 ms                                                | 34.7 ms: 1.01x slower                                      |
| genshi_xml      | 50.3 ms                                                | 52.0 ms: 1.03x slower                                      |
| mako            | 11.1 ms                                                | 11.7 ms: 1.06x slower                                      |
| Geometric mean  | (ref)                                                  | 1.03x slower                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231013-linux-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| mypy2                      | 1.07 sec                                               | 863 ms: 1.24x faster                                       |
| regex_effbot               | 3.88 ms                                                | 3.56 ms: 1.09x faster                                      |
| create_gc_cycles           | 1.61 ms                                                | 1.50 ms: 1.07x faster                                      |
| mdp                        | 2.74 sec                                               | 2.58 sec: 1.06x faster                                     |
| regex_dna                  | 220 ms                                                 | 209 ms: 1.05x faster                                       |
| flaskblogging              | 9.11 ms                                                | 8.77 ms: 1.04x faster                                      |
| typing_runtime_protocols   | 159 us                                                 | 153 us: 1.04x faster                                       |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.93 ms: 1.02x faster                                      |
| python_startup             | 10.6 ms                                                | 10.4 ms: 1.02x faster                                      |
| bench_mp_pool              | 24.0 ms                                                | 23.9 ms: 1.01x faster                                      |
| nqueens                    | 80.6 ms                                                | 81.0 ms: 1.00x slower                                      |
| sqlglot_normalize          | 107 ms                                                 | 108 ms: 1.01x slower                                       |
| json_dumps                 | 10.4 ms                                                | 10.5 ms: 1.01x slower                                      |
| genshi_text                | 22.9 ms                                                | 23.1 ms: 1.01x slower                                      |
| django_template            | 34.4 ms                                                | 34.7 ms: 1.01x slower                                      |
| pickle                     | 11.6 us                                                | 11.7 us: 1.01x slower                                      |
| xml_etree_generate         | 87.0 ms                                                | 87.7 ms: 1.01x slower                                      |
| python_startup_no_site     | 6.99 ms                                                | 7.05 ms: 1.01x slower                                      |
| sqlglot_optimize           | 53.9 ms                                                | 54.5 ms: 1.01x slower                                      |
| pprint_safe_repr           | 744 ms                                                 | 752 ms: 1.01x slower                                       |
| spectral_norm              | 115 ms                                                 | 116 ms: 1.01x slower                                       |
| deepcopy_reduce            | 3.17 us                                                | 3.20 us: 1.01x slower                                      |
| json                       | 5.20 ms                                                | 5.27 ms: 1.01x slower                                      |
| asyncio_websockets         | 555 ms                                                 | 563 ms: 1.01x slower                                       |
| scimark_fft                | 369 ms                                                 | 375 ms: 1.02x slower                                       |
| scimark_lu                 | 115 ms                                                 | 117 ms: 1.02x slower                                       |
| asyncio_tcp                | 488 ms                                                 | 498 ms: 1.02x slower                                       |
| pidigits                   | 186 ms                                                 | 190 ms: 1.02x slower                                       |
| pprint_pformat             | 1.51 sec                                               | 1.54 sec: 1.02x slower                                     |
| bench_thread_pool          | 815 us                                                 | 833 us: 1.02x slower                                       |
| pickle_pure_python         | 300 us                                                 | 307 us: 1.02x slower                                       |
| deepcopy                   | 352 us                                                 | 361 us: 1.02x slower                                       |
| unpickle_list              | 4.96 us                                                | 5.08 us: 1.02x slower                                      |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.83 sec: 1.02x slower                                     |
| generators                 | 28.8 ms                                                | 29.5 ms: 1.02x slower                                      |
| xml_etree_parse            | 156 ms                                                 | 160 ms: 1.03x slower                                       |
| meteor_contest             | 108 ms                                                 | 111 ms: 1.03x slower                                       |
| aiohttp                    | 1.14 ms                                                | 1.18 ms: 1.03x slower                                      |
| richards_super             | 54.4 ms                                                | 56.0 ms: 1.03x slower                                      |
| crypto_pyaes               | 73.0 ms                                                | 75.1 ms: 1.03x slower                                      |
| go                         | 142 ms                                                 | 146 ms: 1.03x slower                                       |
| json_loads                 | 27.0 us                                                | 27.9 us: 1.03x slower                                      |
| genshi_xml                 | 50.3 ms                                                | 52.0 ms: 1.03x slower                                      |
| sqlglot_parse              | 1.27 ms                                                | 1.31 ms: 1.04x slower                                      |
| richards                   | 48.1 ms                                                | 49.9 ms: 1.04x slower                                      |
| scimark_sor                | 122 ms                                                 | 127 ms: 1.04x slower                                       |
| sqlglot_transpile          | 1.57 ms                                                | 1.63 ms: 1.04x slower                                      |
| gunicorn                   | 1.23 ms                                                | 1.27 ms: 1.04x slower                                      |
| deepcopy_memo              | 38.0 us                                                | 39.6 us: 1.04x slower                                      |
| pickle_list                | 5.01 us                                                | 5.21 us: 1.04x slower                                      |
| chameleon                  | 6.85 ms                                                | 7.13 ms: 1.04x slower                                      |
| 2to3                       | 265 ms                                                 | 276 ms: 1.04x slower                                       |
| pycparser                  | 1.19 sec                                               | 1.24 sec: 1.04x slower                                     |
| html5lib                   | 64.5 ms                                                | 67.3 ms: 1.04x slower                                      |
| sympy_integrate            | 19.9 ms                                                | 20.8 ms: 1.04x slower                                      |
| sympy_str                  | 274 ms                                                 | 286 ms: 1.05x slower                                       |
| hexiom                     | 6.13 ms                                                | 6.40 ms: 1.05x slower                                      |
| docutils                   | 2.58 sec                                               | 2.71 sec: 1.05x slower                                     |
| pyflate                    | 460 ms                                                 | 482 ms: 1.05x slower                                       |
| xml_etree_iterparse        | 102 ms                                                 | 107 ms: 1.05x slower                                       |
| coroutines                 | 22.5 ms                                                | 23.7 ms: 1.05x slower                                      |
| mako                       | 11.1 ms                                                | 11.7 ms: 1.06x slower                                      |
| unpickle_pure_python       | 213 us                                                 | 226 us: 1.06x slower                                       |
| scimark_monte_carlo        | 66.3 ms                                                | 70.2 ms: 1.06x slower                                      |
| tomli_loads                | 2.11 sec                                               | 2.25 sec: 1.06x slower                                     |
| logging_simple             | 5.66 us                                                | 6.02 us: 1.06x slower                                      |
| float                      | 78.5 ms                                                | 83.4 ms: 1.06x slower                                      |
| logging_silent             | 102 ns                                                 | 109 ns: 1.06x slower                                       |
| pickle_dict                | 33.2 us                                                | 35.4 us: 1.07x slower                                      |
| sympy_sum                  | 150 ms                                                 | 160 ms: 1.07x slower                                       |
| logging_format             | 6.25 us                                                | 6.71 us: 1.07x slower                                      |
| deltablue                  | 3.15 ms                                                | 3.40 ms: 1.08x slower                                      |
| tornado_http               | 91.5 ms                                                | 99.1 ms: 1.08x slower                                      |
| regex_compile              | 131 ms                                                 | 142 ms: 1.08x slower                                       |
| dulwich_log                | 63.0 ms                                                | 68.5 ms: 1.09x slower                                      |
| raytrace                   | 262 ms                                                 | 285 ms: 1.09x slower                                       |
| async_generators           | 433 ms                                                 | 472 ms: 1.09x slower                                       |
| gc_traversal               | 3.81 ms                                                | 4.15 ms: 1.09x slower                                      |
| sqlite_synth               | 2.85 us                                                | 3.11 us: 1.09x slower                                      |
| chaos                      | 58.4 ms                                                | 64.0 ms: 1.10x slower                                      |
| fannkuch                   | 381 ms                                                 | 420 ms: 1.10x slower                                       |
| nbody                      | 85.7 ms                                                | 95.7 ms: 1.12x slower                                      |
| pathlib                    | 17.1 ms                                                | 19.6 ms: 1.15x slower                                      |
| async_tree_none            | 354 ms                                                 | 446 ms: 1.26x slower                                       |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 726 ms: 1.26x slower                                       |
| async_tree_memoization     | 442 ms                                                 | 572 ms: 1.29x slower                                       |
| async_tree_memoization_tg  | 465 ms                                                 | 610 ms: 1.31x slower                                       |
| comprehensions             | 16.4 us                                                | 21.5 us: 1.31x slower                                      |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 759 ms: 1.40x slower                                       |
| async_tree_io              | 843 ms                                                 | 1.21 sec: 1.44x slower                                     |
| async_tree_none_tg         | 320 ms                                                 | 463 ms: 1.45x slower                                       |
| async_tree_io_tg           | 825 ms                                                 | 1.25 sec: 1.51x slower                                     |
| dask                       | 338 ms                                                 | 544 ms: 1.61x slower                                       |
| coverage                   | 83.7 ms                                                | 700 ms: 8.36x slower                                       |
| thrift                     | 796 us                                                 | 9.24 ms: 11.60x slower                                     |
| Geometric mean             | (ref)                                                  | 1.11x slower                                               |

Benchmark hidden because not significant (6): telco, regex_v8, xml_etree_process, sympy_expand, unpickle, pylint
Ignored benchmarks (3) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: bpe_tokeniser, djangocms, unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: 0.57x