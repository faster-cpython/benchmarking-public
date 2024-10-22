# Results vs. 3.13.0

- fork: python
- ref: v3.13.0a5
- machine: windows-amd64
- commit hash: 076d169
- commit date: 2024-03-12
- overall geometric mean: 1.02x slower
- HPT reliability: 96.46%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240312-pythonperf1-amd64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| chameleon      | 4.72 ms                                                     | 4.84 ms: 1.03x slower                                           |
| docutils       | 1.57 sec                                                    | 1.54 sec: 1.02x faster                                          |
| html5lib       | 38.6 ms                                                     | 36.5 ms: 1.06x faster                                           |
| tornado_http   | 92.8 ms                                                     | 84.8 ms: 1.10x faster                                           |
| Geometric mean | (ref)                                                       | 1.03x faster                                                    |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240312-pythonperf1-amd64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| asyncio_tcp                | 654 ms                                                      | 478 ms: 1.37x faster                                            |
| async_generators           | 223 ms                                                      | 224 ms: 1.01x slower                                            |
| coroutines                 | 12.5 ms                                                     | 13.2 ms: 1.05x slower                                           |
| asyncio_tcp_ssl            | 1.64 sec                                                    | 1.80 sec: 1.10x slower                                          |
| async_tree_cpu_io_mixed    | 387 ms                                                      | 454 ms: 1.17x slower                                            |
| async_tree_none            | 223 ms                                                      | 270 ms: 1.21x slower                                            |
| async_tree_memoization_tg  | 288 ms                                                      | 349 ms: 1.21x slower                                            |
| async_tree_memoization     | 271 ms                                                      | 340 ms: 1.25x slower                                            |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 474 ms: 1.26x slower                                            |
| async_tree_none_tg         | 206 ms                                                      | 274 ms: 1.33x slower                                            |
| async_tree_io              | 521 ms                                                      | 738 ms: 1.42x slower                                            |
| async_tree_io_tg           | 512 ms                                                      | 758 ms: 1.48x slower                                            |
| Geometric mean             | (ref)                                                       | 1.17x slower                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240312-pythonperf1-amd64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| pidigits       | 148 ms                                                      | 147 ms: 1.01x faster                                            |
| float          | 48.1 ms                                                     | 50.8 ms: 1.06x slower                                           |
| nbody          | 64.5 ms                                                     | 68.2 ms: 1.06x slower                                           |
| Geometric mean | (ref)                                                       | 1.04x slower                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240312-pythonperf1-amd64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.57 ms: 1.03x faster                                           |
| regex_compile  | 80.1 ms                                                     | 78.2 ms: 1.03x faster                                           |
| regex_dna      | 114 ms                                                      | 118 ms: 1.03x slower                                            |
| Geometric mean | (ref)                                                       | 1.01x slower                                                    |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240312-pythonperf1-amd64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| unpickle             | 8.63 us                                                     | 8.29 us: 1.04x faster                                           |
| json_loads           | 14.3 us                                                     | 13.9 us: 1.03x faster                                           |
| json_dumps           | 5.76 ms                                                     | 5.63 ms: 1.02x faster                                           |
| pickle               | 7.34 us                                                     | 7.17 us: 1.02x faster                                           |
| pickle_pure_python   | 183 us                                                      | 180 us: 1.02x faster                                            |
| unpickle_list        | 2.72 us                                                     | 2.68 us: 1.02x faster                                           |
| unpickle_pure_python | 127 us                                                      | 125 us: 1.02x faster                                            |
| xml_etree_process    | 36.5 ms                                                     | 36.7 ms: 1.01x slower                                           |
| xml_etree_generate   | 53.3 ms                                                     | 53.8 ms: 1.01x slower                                           |
| xml_etree_iterparse  | 62.3 ms                                                     | 62.9 ms: 1.01x slower                                           |
| pickle_dict          | 18.0 us                                                     | 18.5 us: 1.03x slower                                           |
| tomli_loads          | 1.36 sec                                                    | 1.43 sec: 1.05x slower                                          |
| Geometric mean       | (ref)                                                       | 1.00x faster                                                    |

Benchmark hidden because not significant (2): pickle_list, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240312-pythonperf1-amd64-python-v3.13.0a5-3.13.0a5-076d169 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup         | 22.2 ms                                                     | 20.3 ms: 1.09x faster                                           |
| python_startup_no_site | 17.8 ms                                                     | 18.1 ms: 1.02x slower                                           |
| Geometric mean         | (ref)                                                       | 1.04x faster                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240312-pythonperf1-amd64-python-v3.13.0a5-3.13.0a5-076d169 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| django_template | 21.8 ms                                                     | 22.1 ms: 1.02x slower                                           |
| genshi_xml      | 32.8 ms                                                     | 34.6 ms: 1.06x slower                                           |
| genshi_text     | 14.9 ms                                                     | 15.8 ms: 1.07x slower                                           |
| Geometric mean  | (ref)                                                       | 1.03x slower                                                    |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240312-pythonperf1-amd64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| asyncio_tcp                | 654 ms                                                      | 478 ms: 1.37x faster                                            |
| typing_runtime_protocols   | 100 us                                                      | 75.1 us: 1.34x faster                                           |
| create_gc_cycles           | 829 us                                                      | 745 us: 1.11x faster                                            |
| tornado_http               | 92.8 ms                                                     | 84.8 ms: 1.10x faster                                           |
| pycparser                  | 758 ms                                                      | 693 ms: 1.09x faster                                            |
| python_startup             | 22.2 ms                                                     | 20.3 ms: 1.09x faster                                           |
| thrift                     | 8.68 ms                                                     | 8.19 ms: 1.06x faster                                           |
| sympy_expand               | 285 ms                                                      | 270 ms: 1.06x faster                                            |
| html5lib                   | 38.6 ms                                                     | 36.5 ms: 1.06x faster                                           |
| sympy_str                  | 166 ms                                                      | 158 ms: 1.05x faster                                            |
| bench_mp_pool              | 69.6 ms                                                     | 66.6 ms: 1.04x faster                                           |
| sympy_sum                  | 86.4 ms                                                     | 82.9 ms: 1.04x faster                                           |
| unpickle                   | 8.63 us                                                     | 8.29 us: 1.04x faster                                           |
| aiohttp                    | 932 us                                                      | 896 us: 1.04x faster                                            |
| mypy2                      | 429 ms                                                      | 413 ms: 1.04x faster                                            |
| deepcopy_reduce            | 2.02 us                                                     | 1.95 us: 1.04x faster                                           |
| gc_traversal               | 1.55 ms                                                     | 1.50 ms: 1.04x faster                                           |
| json_loads                 | 14.3 us                                                     | 13.9 us: 1.03x faster                                           |
| regex_effbot               | 1.62 ms                                                     | 1.57 ms: 1.03x faster                                           |
| scimark_monte_carlo        | 40.3 ms                                                     | 39.2 ms: 1.03x faster                                           |
| regex_compile              | 80.1 ms                                                     | 78.2 ms: 1.03x faster                                           |
| docutils                   | 1.57 sec                                                    | 1.54 sec: 1.02x faster                                          |
| json_dumps                 | 5.76 ms                                                     | 5.63 ms: 1.02x faster                                           |
| pickle                     | 7.34 us                                                     | 7.17 us: 1.02x faster                                           |
| telco                      | 4.85 ms                                                     | 4.75 ms: 1.02x faster                                           |
| pickle_pure_python         | 183 us                                                      | 180 us: 1.02x faster                                            |
| unpickle_list              | 2.72 us                                                     | 2.68 us: 1.02x faster                                           |
| unpickle_pure_python       | 127 us                                                      | 125 us: 1.02x faster                                            |
| deepcopy                   | 223 us                                                      | 220 us: 1.02x faster                                            |
| sqlglot_optimize           | 33.1 ms                                                     | 32.6 ms: 1.01x faster                                           |
| scimark_fft                | 174 ms                                                      | 172 ms: 1.01x faster                                            |
| pathlib                    | 81.2 ms                                                     | 80.3 ms: 1.01x faster                                           |
| pprint_safe_repr           | 493 ms                                                      | 487 ms: 1.01x faster                                            |
| mdp                        | 1.38 sec                                                    | 1.37 sec: 1.01x faster                                          |
| fannkuch                   | 245 ms                                                      | 243 ms: 1.01x faster                                            |
| pidigits                   | 148 ms                                                      | 147 ms: 1.01x faster                                            |
| flaskblogging              | 2.04 sec                                                    | 2.03 sec: 1.01x faster                                          |
| crypto_pyaes               | 42.8 ms                                                     | 42.6 ms: 1.00x faster                                           |
| sqlite_synth               | 1.60 us                                                     | 1.59 us: 1.00x faster                                           |
| scimark_sparse_mat_mult    | 2.34 ms                                                     | 2.35 ms: 1.00x slower                                           |
| xml_etree_process          | 36.5 ms                                                     | 36.7 ms: 1.01x slower                                           |
| sympy_integrate            | 12.3 ms                                                     | 12.3 ms: 1.01x slower                                           |
| async_generators           | 223 ms                                                      | 224 ms: 1.01x slower                                            |
| sqlglot_normalize          | 171 ms                                                      | 172 ms: 1.01x slower                                            |
| meteor_contest             | 72.3 ms                                                     | 72.8 ms: 1.01x slower                                           |
| spectral_norm              | 59.2 ms                                                     | 59.7 ms: 1.01x slower                                           |
| xml_etree_generate         | 53.3 ms                                                     | 53.8 ms: 1.01x slower                                           |
| coverage                   | 46.7 ms                                                     | 47.1 ms: 1.01x slower                                           |
| xml_etree_iterparse        | 62.3 ms                                                     | 62.9 ms: 1.01x slower                                           |
| chaos                      | 37.9 ms                                                     | 38.4 ms: 1.01x slower                                           |
| django_template            | 21.8 ms                                                     | 22.1 ms: 1.02x slower                                           |
| go                         | 84.6 ms                                                     | 86.1 ms: 1.02x slower                                           |
| python_startup_no_site     | 17.8 ms                                                     | 18.1 ms: 1.02x slower                                           |
| deepcopy_memo              | 21.8 us                                                     | 22.3 us: 1.02x slower                                           |
| pyflate                    | 275 ms                                                      | 281 ms: 1.02x slower                                            |
| chameleon                  | 4.72 ms                                                     | 4.84 ms: 1.03x slower                                           |
| pickle_dict                | 18.0 us                                                     | 18.5 us: 1.03x slower                                           |
| raytrace                   | 156 ms                                                      | 160 ms: 1.03x slower                                            |
| scimark_lu                 | 54.0 ms                                                     | 55.5 ms: 1.03x slower                                           |
| sqlglot_transpile          | 952 us                                                      | 980 us: 1.03x slower                                            |
| regex_dna                  | 114 ms                                                      | 118 ms: 1.03x slower                                            |
| logging_format             | 6.15 us                                                     | 6.41 us: 1.04x slower                                           |
| logging_simple             | 5.72 us                                                     | 5.97 us: 1.04x slower                                           |
| richards_super             | 29.3 ms                                                     | 30.6 ms: 1.04x slower                                           |
| scimark_sor                | 72.0 ms                                                     | 75.4 ms: 1.05x slower                                           |
| coroutines                 | 12.5 ms                                                     | 13.2 ms: 1.05x slower                                           |
| logging_silent             | 51.0 ns                                                     | 53.5 ns: 1.05x slower                                           |
| tomli_loads                | 1.36 sec                                                    | 1.43 sec: 1.05x slower                                          |
| richards                   | 26.0 ms                                                     | 27.5 ms: 1.05x slower                                           |
| float                      | 48.1 ms                                                     | 50.8 ms: 1.06x slower                                           |
| generators                 | 19.5 ms                                                     | 20.6 ms: 1.06x slower                                           |
| genshi_xml                 | 32.8 ms                                                     | 34.6 ms: 1.06x slower                                           |
| nbody                      | 64.5 ms                                                     | 68.2 ms: 1.06x slower                                           |
| hexiom                     | 3.69 ms                                                     | 3.91 ms: 1.06x slower                                           |
| deltablue                  | 1.86 ms                                                     | 1.98 ms: 1.06x slower                                           |
| genshi_text                | 14.9 ms                                                     | 15.8 ms: 1.07x slower                                           |
| comprehensions             | 10.2 us                                                     | 11.0 us: 1.08x slower                                           |
| nqueens                    | 55.5 ms                                                     | 59.9 ms: 1.08x slower                                           |
| json                       | 2.98 ms                                                     | 3.23 ms: 1.08x slower                                           |
| asyncio_tcp_ssl            | 1.64 sec                                                    | 1.80 sec: 1.10x slower                                          |
| async_tree_cpu_io_mixed    | 387 ms                                                      | 454 ms: 1.17x slower                                            |
| async_tree_none            | 223 ms                                                      | 270 ms: 1.21x slower                                            |
| async_tree_memoization_tg  | 288 ms                                                      | 349 ms: 1.21x slower                                            |
| async_tree_memoization     | 271 ms                                                      | 340 ms: 1.25x slower                                            |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 474 ms: 1.26x slower                                            |
| async_tree_none_tg         | 206 ms                                                      | 274 ms: 1.33x slower                                            |
| async_tree_io              | 521 ms                                                      | 738 ms: 1.42x slower                                            |
| async_tree_io_tg           | 512 ms                                                      | 758 ms: 1.48x slower                                            |
| Geometric mean             | (ref)                                                       | 1.02x slower                                                    |

Benchmark hidden because not significant (10): pylint, mako, 2to3, dulwich_log, pprint_pformat, sqlglot_parse, pickle_list, xml_etree_parse, bench_thread_pool, regex_v8
Ignored benchmarks (1) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: unpack_sequence

# HPT report

- Reliability score: 96.46% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown