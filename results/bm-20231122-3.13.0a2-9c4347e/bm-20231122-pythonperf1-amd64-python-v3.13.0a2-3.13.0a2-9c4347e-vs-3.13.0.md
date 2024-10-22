# Results vs. 3.13.0

- fork: python
- ref: v3.13.0a2
- machine: windows-amd64
- commit hash: 9c4347e
- commit date: 2023-11-22
- overall geometric mean: 1.02x slower
- HPT reliability: 92.76%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-pythonperf1-amd64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 217 ms                                                      | 210 ms: 1.04x faster                                            |
| chameleon      | 4.72 ms                                                     | 4.81 ms: 1.02x slower                                           |
| docutils       | 1.57 sec                                                    | 1.55 sec: 1.02x faster                                          |
| html5lib       | 38.6 ms                                                     | 36.6 ms: 1.05x faster                                           |
| tornado_http   | 92.8 ms                                                     | 86.1 ms: 1.08x faster                                           |
| Geometric mean | (ref)                                                       | 1.03x faster                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-pythonperf1-amd64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| asyncio_tcp                | 654 ms                                                      | 465 ms: 1.40x faster                                            |
| async_generators           | 223 ms                                                      | 227 ms: 1.02x slower                                            |
| coroutines                 | 12.5 ms                                                     | 13.2 ms: 1.06x slower                                           |
| async_tree_cpu_io_mixed    | 387 ms                                                      | 453 ms: 1.17x slower                                            |
| async_tree_none            | 223 ms                                                      | 264 ms: 1.18x slower                                            |
| asyncio_tcp_ssl            | 1.64 sec                                                    | 2.02 sec: 1.23x slower                                          |
| async_tree_memoization_tg  | 288 ms                                                      | 361 ms: 1.25x slower                                            |
| async_tree_memoization     | 271 ms                                                      | 341 ms: 1.26x slower                                            |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 482 ms: 1.29x slower                                            |
| async_tree_none_tg         | 206 ms                                                      | 281 ms: 1.37x slower                                            |
| async_tree_io              | 521 ms                                                      | 731 ms: 1.40x slower                                            |
| async_tree_io_tg           | 512 ms                                                      | 769 ms: 1.50x slower                                            |
| Geometric mean             | (ref)                                                       | 1.18x slower                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-pythonperf1-amd64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| pidigits       | 148 ms                                                      | 147 ms: 1.01x faster                                            |
| float          | 48.1 ms                                                     | 52.3 ms: 1.09x slower                                           |
| nbody          | 64.5 ms                                                     | 72.0 ms: 1.12x slower                                           |
| Geometric mean | (ref)                                                       | 1.06x slower                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-pythonperf1-amd64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_compile  | 80.1 ms                                                     | 78.9 ms: 1.02x faster                                           |
| regex_v8       | 14.7 ms                                                     | 15.3 ms: 1.05x slower                                           |
| regex_dna      | 114 ms                                                      | 122 ms: 1.07x slower                                            |
| Geometric mean | (ref)                                                       | 1.03x slower                                                    |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-pythonperf1-amd64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| json_loads           | 14.3 us                                                     | 13.4 us: 1.07x faster                                           |
| unpickle             | 8.63 us                                                     | 8.09 us: 1.07x faster                                           |
| pickle               | 7.34 us                                                     | 6.94 us: 1.06x faster                                           |
| json_dumps           | 5.76 ms                                                     | 5.50 ms: 1.05x faster                                           |
| pickle_pure_python   | 183 us                                                      | 179 us: 1.03x faster                                            |
| xml_etree_parse      | 93.2 ms                                                     | 92.3 ms: 1.01x faster                                           |
| unpickle_list        | 2.72 us                                                     | 2.70 us: 1.01x faster                                           |
| tomli_loads          | 1.36 sec                                                    | 1.37 sec: 1.00x slower                                          |
| unpickle_pure_python | 127 us                                                      | 128 us: 1.01x slower                                            |
| xml_etree_iterparse  | 62.3 ms                                                     | 64.5 ms: 1.03x slower                                           |
| pickle_dict          | 18.0 us                                                     | 19.1 us: 1.06x slower                                           |
| Geometric mean       | (ref)                                                       | 1.01x faster                                                    |

Benchmark hidden because not significant (3): pickle_list, xml_etree_process, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-pythonperf1-amd64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup | 22.2 ms                                                     | 19.9 ms: 1.11x faster                                           |
| Geometric mean | (ref)                                                       | 1.06x faster                                                    |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-pythonperf1-amd64-python-v3.13.0a2-3.13.0a2-9c4347e |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| django_template | 21.8 ms                                                     | 21.9 ms: 1.01x slower                                           |
| genshi_text     | 14.9 ms                                                     | 15.0 ms: 1.01x slower                                           |
| mako            | 6.24 ms                                                     | 6.48 ms: 1.04x slower                                           |
| Geometric mean  | (ref)                                                       | 1.02x slower                                                    |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-pythonperf1-amd64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| asyncio_tcp                | 654 ms                                                      | 465 ms: 1.40x faster                                            |
| typing_runtime_protocols   | 100 us                                                      | 73.9 us: 1.36x faster                                           |
| python_startup             | 22.2 ms                                                     | 19.9 ms: 1.11x faster                                           |
| create_gc_cycles           | 829 us                                                      | 746 us: 1.11x faster                                            |
| bench_mp_pool              | 69.6 ms                                                     | 64.0 ms: 1.09x faster                                           |
| tornado_http               | 92.8 ms                                                     | 86.1 ms: 1.08x faster                                           |
| json_loads                 | 14.3 us                                                     | 13.4 us: 1.07x faster                                           |
| unpickle                   | 8.63 us                                                     | 8.09 us: 1.07x faster                                           |
| sympy_str                  | 166 ms                                                      | 156 ms: 1.06x faster                                            |
| telco                      | 4.85 ms                                                     | 4.57 ms: 1.06x faster                                           |
| sympy_expand               | 285 ms                                                      | 269 ms: 1.06x faster                                            |
| pickle                     | 7.34 us                                                     | 6.94 us: 1.06x faster                                           |
| html5lib                   | 38.6 ms                                                     | 36.6 ms: 1.05x faster                                           |
| sympy_sum                  | 86.4 ms                                                     | 82.3 ms: 1.05x faster                                           |
| aiohttp                    | 932 us                                                      | 889 us: 1.05x faster                                            |
| json_dumps                 | 5.76 ms                                                     | 5.50 ms: 1.05x faster                                           |
| json                       | 2.98 ms                                                     | 2.85 ms: 1.05x faster                                           |
| thrift                     | 8.68 ms                                                     | 8.35 ms: 1.04x faster                                           |
| deepcopy_reduce            | 2.02 us                                                     | 1.95 us: 1.04x faster                                           |
| 2to3                       | 217 ms                                                      | 210 ms: 1.04x faster                                            |
| pprint_safe_repr           | 493 ms                                                      | 479 ms: 1.03x faster                                            |
| pickle_pure_python         | 183 us                                                      | 179 us: 1.03x faster                                            |
| gc_traversal               | 1.55 ms                                                     | 1.52 ms: 1.02x faster                                           |
| deepcopy                   | 223 us                                                      | 218 us: 1.02x faster                                            |
| sqlite_synth               | 1.60 us                                                     | 1.56 us: 1.02x faster                                           |
| mdp                        | 1.38 sec                                                    | 1.36 sec: 1.02x faster                                          |
| coverage                   | 46.7 ms                                                     | 45.8 ms: 1.02x faster                                           |
| sqlglot_optimize           | 33.1 ms                                                     | 32.5 ms: 1.02x faster                                           |
| docutils                   | 1.57 sec                                                    | 1.55 sec: 1.02x faster                                          |
| regex_compile              | 80.1 ms                                                     | 78.9 ms: 1.02x faster                                           |
| pathlib                    | 81.2 ms                                                     | 79.9 ms: 1.02x faster                                           |
| fannkuch                   | 245 ms                                                      | 241 ms: 1.02x faster                                            |
| pprint_pformat             | 991 ms                                                      | 979 ms: 1.01x faster                                            |
| sqlglot_parse              | 761 us                                                      | 752 us: 1.01x faster                                            |
| xml_etree_parse            | 93.2 ms                                                     | 92.3 ms: 1.01x faster                                           |
| pidigits                   | 148 ms                                                      | 147 ms: 1.01x faster                                            |
| sympy_integrate            | 12.3 ms                                                     | 12.2 ms: 1.01x faster                                           |
| unpickle_list              | 2.72 us                                                     | 2.70 us: 1.01x faster                                           |
| flaskblogging              | 2.04 sec                                                    | 2.03 sec: 1.01x faster                                          |
| meteor_contest             | 72.3 ms                                                     | 72.6 ms: 1.00x slower                                           |
| tomli_loads                | 1.36 sec                                                    | 1.37 sec: 1.00x slower                                          |
| django_template            | 21.8 ms                                                     | 21.9 ms: 1.01x slower                                           |
| unpickle_pure_python       | 127 us                                                      | 128 us: 1.01x slower                                            |
| genshi_text                | 14.9 ms                                                     | 15.0 ms: 1.01x slower                                           |
| crypto_pyaes               | 42.8 ms                                                     | 43.3 ms: 1.01x slower                                           |
| sqlglot_transpile          | 952 us                                                      | 965 us: 1.01x slower                                            |
| scimark_monte_carlo        | 40.3 ms                                                     | 40.9 ms: 1.01x slower                                           |
| async_generators           | 223 ms                                                      | 227 ms: 1.02x slower                                            |
| chameleon                  | 4.72 ms                                                     | 4.81 ms: 1.02x slower                                           |
| bench_thread_pool          | 828 us                                                      | 848 us: 1.02x slower                                            |
| dulwich_log                | 40.4 ms                                                     | 41.4 ms: 1.02x slower                                           |
| generators                 | 19.5 ms                                                     | 20.0 ms: 1.03x slower                                           |
| hexiom                     | 3.69 ms                                                     | 3.81 ms: 1.03x slower                                           |
| xml_etree_iterparse        | 62.3 ms                                                     | 64.5 ms: 1.03x slower                                           |
| chaos                      | 37.9 ms                                                     | 39.2 ms: 1.04x slower                                           |
| mako                       | 6.24 ms                                                     | 6.48 ms: 1.04x slower                                           |
| raytrace                   | 156 ms                                                      | 163 ms: 1.04x slower                                            |
| scimark_lu                 | 54.0 ms                                                     | 56.4 ms: 1.04x slower                                           |
| regex_v8                   | 14.7 ms                                                     | 15.3 ms: 1.05x slower                                           |
| nqueens                    | 55.5 ms                                                     | 58.2 ms: 1.05x slower                                           |
| richards_super             | 29.3 ms                                                     | 30.8 ms: 1.05x slower                                           |
| richards                   | 26.0 ms                                                     | 27.3 ms: 1.05x slower                                           |
| scimark_sparse_mat_mult    | 2.34 ms                                                     | 2.46 ms: 1.05x slower                                           |
| pyflate                    | 275 ms                                                      | 291 ms: 1.05x slower                                            |
| coroutines                 | 12.5 ms                                                     | 13.2 ms: 1.06x slower                                           |
| pickle_dict                | 18.0 us                                                     | 19.1 us: 1.06x slower                                           |
| logging_format             | 6.15 us                                                     | 6.51 us: 1.06x slower                                           |
| scimark_fft                | 174 ms                                                      | 184 ms: 1.06x slower                                            |
| logging_simple             | 5.72 us                                                     | 6.07 us: 1.06x slower                                           |
| logging_silent             | 51.0 ns                                                     | 54.1 ns: 1.06x slower                                           |
| regex_dna                  | 114 ms                                                      | 122 ms: 1.07x slower                                            |
| spectral_norm              | 59.2 ms                                                     | 63.6 ms: 1.07x slower                                           |
| deepcopy_memo              | 21.8 us                                                     | 23.5 us: 1.08x slower                                           |
| deltablue                  | 1.86 ms                                                     | 2.01 ms: 1.08x slower                                           |
| float                      | 48.1 ms                                                     | 52.3 ms: 1.09x slower                                           |
| nbody                      | 64.5 ms                                                     | 72.0 ms: 1.12x slower                                           |
| async_tree_cpu_io_mixed    | 387 ms                                                      | 453 ms: 1.17x slower                                            |
| async_tree_none            | 223 ms                                                      | 264 ms: 1.18x slower                                            |
| scimark_sor                | 72.0 ms                                                     | 85.4 ms: 1.19x slower                                           |
| asyncio_tcp_ssl            | 1.64 sec                                                    | 2.02 sec: 1.23x slower                                          |
| async_tree_memoization_tg  | 288 ms                                                      | 361 ms: 1.25x slower                                            |
| async_tree_memoization     | 271 ms                                                      | 341 ms: 1.26x slower                                            |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 482 ms: 1.29x slower                                            |
| mypy2                      | 429 ms                                                      | 584 ms: 1.36x slower                                            |
| async_tree_none_tg         | 206 ms                                                      | 281 ms: 1.37x slower                                            |
| async_tree_io              | 521 ms                                                      | 731 ms: 1.40x slower                                            |
| async_tree_io_tg           | 512 ms                                                      | 769 ms: 1.50x slower                                            |
| Geometric mean             | (ref)                                                       | 1.02x slower                                                    |

Benchmark hidden because not significant (11): pycparser, pylint, pickle_list, python_startup_no_site, go, xml_etree_process, xml_etree_generate, sqlglot_normalize, regex_effbot, comprehensions, genshi_xml
Ignored benchmarks (1) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: unpack_sequence

# HPT report

- Reliability score: 92.76% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown