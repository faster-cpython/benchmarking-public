# Results vs. base

- fork: python
- ref: v3.13.0a4
- machine: linux-x86_64
- commit hash: 9d34f60
- commit date: 2024-02-15
- overall geometric mean: 1.019x slower
- HPT reliability: 87.78%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20240215-3.13.0a4-9d34f60/bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60.json | results/bm-20240215-3.13.0a4-9d34f60-PYTHON_UOPS/bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60.json |
|----------------|:----------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------:|
| 2to3           | 269 ms                                                                                               | 277 ms: 1.03x slower                                                                                             |
| chameleon      | 6.85 ms                                                                                              | 6.93 ms: 1.01x slower                                                                                            |
| docutils       | 2.65 sec                                                                                             | 2.64 sec: 1.00x faster                                                                                           |
| Geometric mean | (ref)                                                                                                | 1.01x slower                                                                                                     |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20240215-3.13.0a4-9d34f60/bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60.json | results/bm-20240215-3.13.0a4-9d34f60-PYTHON_UOPS/bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60.json |
|----------------------------|:----------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------:|
| async_tree_io              | 1.20 sec                                                                                             | 1.18 sec: 1.02x faster                                                                                           |
| async_tree_memoization_tg  | 585 ms                                                                                               | 576 ms: 1.02x faster                                                                                             |
| async_tree_io_tg           | 1.22 sec                                                                                             | 1.20 sec: 1.02x faster                                                                                           |
| async_tree_none_tg         | 455 ms                                                                                               | 448 ms: 1.01x faster                                                                                             |
| async_tree_cpu_io_mixed_tg | 733 ms                                                                                               | 723 ms: 1.01x faster                                                                                             |
| async_tree_cpu_io_mixed    | 718 ms                                                                                               | 710 ms: 1.01x faster                                                                                             |
| Geometric mean             | (ref)                                                                                                | 1.01x faster                                                                                                     |

Benchmark hidden because not significant (2): async_tree_none, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20240215-3.13.0a4-9d34f60/bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60.json | results/bm-20240215-3.13.0a4-9d34f60-PYTHON_UOPS/bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60.json |
|----------------|:----------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------:|
| pidigits       | 189 ms                                                                                               | 188 ms: 1.01x faster                                                                                             |
| float          | 83.1 ms                                                                                              | 85.3 ms: 1.03x slower                                                                                            |
| nbody          | 92.1 ms                                                                                              | 103 ms: 1.12x slower                                                                                             |
| Geometric mean | (ref)                                                                                                | 1.05x slower                                                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20240215-3.13.0a4-9d34f60/bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60.json | results/bm-20240215-3.13.0a4-9d34f60-PYTHON_UOPS/bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60.json |
|----------------|:----------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------:|
| regex_dna      | 224 ms                                                                                               | 216 ms: 1.03x faster                                                                                             |
| regex_effbot   | 3.66 ms                                                                                              | 3.59 ms: 1.02x faster                                                                                            |
| regex_v8       | 24.4 ms                                                                                              | 25.2 ms: 1.03x slower                                                                                            |
| regex_compile  | 132 ms                                                                                               | 138 ms: 1.05x slower                                                                                             |
| Geometric mean | (ref)                                                                                                | 1.01x slower                                                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20240215-3.13.0a4-9d34f60/bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60.json | results/bm-20240215-3.13.0a4-9d34f60-PYTHON_UOPS/bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60.json |
|----------------------|:----------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------:|
| pickle               | 12.0 us                                                                                              | 11.4 us: 1.06x faster                                                                                            |
| pickle_list          | 5.28 us                                                                                              | 5.00 us: 1.06x faster                                                                                            |
| xml_etree_parse      | 160 ms                                                                                               | 156 ms: 1.03x faster                                                                                             |
| unpickle_list        | 5.09 us                                                                                              | 4.96 us: 1.03x faster                                                                                            |
| json_loads           | 27.9 us                                                                                              | 27.5 us: 1.02x faster                                                                                            |
| pickle_dict          | 34.7 us                                                                                              | 34.2 us: 1.02x faster                                                                                            |
| xml_etree_process    | 59.3 ms                                                                                              | 58.4 ms: 1.01x faster                                                                                            |
| pickle_pure_python   | 302 us                                                                                               | 298 us: 1.01x faster                                                                                             |
| xml_etree_generate   | 86.9 ms                                                                                              | 86.0 ms: 1.01x faster                                                                                            |
| json_dumps           | 10.5 ms                                                                                              | 10.4 ms: 1.01x faster                                                                                            |
| unpickle             | 15.4 us                                                                                              | 15.3 us: 1.00x faster                                                                                            |
| tomli_loads          | 2.20 sec                                                                                             | 2.21 sec: 1.01x slower                                                                                           |
| unpickle_pure_python | 217 us                                                                                               | 230 us: 1.06x slower                                                                                             |
| Geometric mean       | (ref)                                                                                                | 1.01x faster                                                                                                     |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20240215-3.13.0a4-9d34f60/bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60.json | results/bm-20240215-3.13.0a4-9d34f60-PYTHON_UOPS/bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60.json |
|------------------------|:----------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------:|
| python_startup         | 10.3 ms                                                                                              | 10.2 ms: 1.01x faster                                                                                            |
| python_startup_no_site | 8.87 ms                                                                                              | 8.84 ms: 1.00x faster                                                                                            |
| Geometric mean         | (ref)                                                                                                | 1.01x faster                                                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20240215-3.13.0a4-9d34f60/bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60.json | results/bm-20240215-3.13.0a4-9d34f60-PYTHON_UOPS/bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60.json |
|-----------------|:----------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------:|
| django_template | 34.7 ms                                                                                              | 34.2 ms: 1.01x faster                                                                                            |
| genshi_text     | 23.0 ms                                                                                              | 23.4 ms: 1.02x slower                                                                                            |
| mako            | 11.2 ms                                                                                              | 12.1 ms: 1.08x slower                                                                                            |
| Geometric mean  | (ref)                                                                                                | 1.02x slower                                                                                                     |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | results/bm-20240215-3.13.0a4-9d34f60/bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60.json | results/bm-20240215-3.13.0a4-9d34f60-PYTHON_UOPS/bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60.json |
|----------------------------|:----------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------:|
| scimark_sor                | 129 ms                                                                                               | 119 ms: 1.08x faster                                                                                             |
| richards                   | 48.1 ms                                                                                              | 45.3 ms: 1.06x faster                                                                                            |
| pickle                     | 12.0 us                                                                                              | 11.4 us: 1.06x faster                                                                                            |
| pickle_list                | 5.28 us                                                                                              | 5.00 us: 1.06x faster                                                                                            |
| asyncio_tcp                | 501 ms                                                                                               | 478 ms: 1.05x faster                                                                                             |
| richards_super             | 54.1 ms                                                                                              | 51.7 ms: 1.05x faster                                                                                            |
| pycparser                  | 1.23 sec                                                                                             | 1.18 sec: 1.04x faster                                                                                           |
| generators                 | 30.3 ms                                                                                              | 29.2 ms: 1.04x faster                                                                                            |
| regex_dna                  | 224 ms                                                                                               | 216 ms: 1.03x faster                                                                                             |
| asyncio_tcp_ssl            | 1.84 sec                                                                                             | 1.79 sec: 1.03x faster                                                                                           |
| xml_etree_parse            | 160 ms                                                                                               | 156 ms: 1.03x faster                                                                                             |
| unpickle_list              | 5.09 us                                                                                              | 4.96 us: 1.03x faster                                                                                            |
| thrift                     | 807 us                                                                                               | 789 us: 1.02x faster                                                                                             |
| json                       | 5.19 ms                                                                                              | 5.07 ms: 1.02x faster                                                                                            |
| create_gc_cycles           | 1.51 ms                                                                                              | 1.48 ms: 1.02x faster                                                                                            |
| regex_effbot               | 3.66 ms                                                                                              | 3.59 ms: 1.02x faster                                                                                            |
| asyncio_websockets         | 563 ms                                                                                               | 553 ms: 1.02x faster                                                                                             |
| pathlib                    | 18.7 ms                                                                                              | 18.4 ms: 1.02x faster                                                                                            |
| async_tree_io              | 1.20 sec                                                                                             | 1.18 sec: 1.02x faster                                                                                           |
| json_loads                 | 27.9 us                                                                                              | 27.5 us: 1.02x faster                                                                                            |
| coverage                   | 96.3 ms                                                                                              | 94.7 ms: 1.02x faster                                                                                            |
| coroutines                 | 23.0 ms                                                                                              | 22.6 ms: 1.02x faster                                                                                            |
| async_tree_memoization_tg  | 585 ms                                                                                               | 576 ms: 1.02x faster                                                                                             |
| async_tree_io_tg           | 1.22 sec                                                                                             | 1.20 sec: 1.02x faster                                                                                           |
| pickle_dict                | 34.7 us                                                                                              | 34.2 us: 1.02x faster                                                                                            |
| django_template            | 34.7 ms                                                                                              | 34.2 ms: 1.01x faster                                                                                            |
| xml_etree_process          | 59.3 ms                                                                                              | 58.4 ms: 1.01x faster                                                                                            |
| async_tree_none_tg         | 455 ms                                                                                               | 448 ms: 1.01x faster                                                                                             |
| async_tree_cpu_io_mixed_tg | 733 ms                                                                                               | 723 ms: 1.01x faster                                                                                             |
| sqlite_synth               | 2.87 us                                                                                              | 2.83 us: 1.01x faster                                                                                            |
| async_tree_cpu_io_mixed    | 718 ms                                                                                               | 710 ms: 1.01x faster                                                                                             |
| pickle_pure_python         | 302 us                                                                                               | 298 us: 1.01x faster                                                                                             |
| xml_etree_generate         | 86.9 ms                                                                                              | 86.0 ms: 1.01x faster                                                                                            |
| python_startup             | 10.3 ms                                                                                              | 10.2 ms: 1.01x faster                                                                                            |
| async_generators           | 459 ms                                                                                               | 455 ms: 1.01x faster                                                                                             |
| deepcopy_reduce            | 3.06 us                                                                                              | 3.03 us: 1.01x faster                                                                                            |
| pidigits                   | 189 ms                                                                                               | 188 ms: 1.01x faster                                                                                             |
| json_dumps                 | 10.5 ms                                                                                              | 10.4 ms: 1.01x faster                                                                                            |
| docutils                   | 2.65 sec                                                                                             | 2.64 sec: 1.00x faster                                                                                           |
| unpickle                   | 15.4 us                                                                                              | 15.3 us: 1.00x faster                                                                                            |
| python_startup_no_site     | 8.87 ms                                                                                              | 8.84 ms: 1.00x faster                                                                                            |
| sqlglot_normalize          | 108 ms                                                                                               | 108 ms: 1.00x slower                                                                                             |
| bench_mp_pool              | 23.8 ms                                                                                              | 24.0 ms: 1.01x slower                                                                                            |
| tomli_loads                | 2.20 sec                                                                                             | 2.21 sec: 1.01x slower                                                                                           |
| deepcopy                   | 347 us                                                                                               | 350 us: 1.01x slower                                                                                             |
| chameleon                  | 6.85 ms                                                                                              | 6.93 ms: 1.01x slower                                                                                            |
| sqlglot_parse              | 1.26 ms                                                                                              | 1.28 ms: 1.02x slower                                                                                            |
| genshi_text                | 23.0 ms                                                                                              | 23.4 ms: 1.02x slower                                                                                            |
| sqlglot_transpile          | 1.58 ms                                                                                              | 1.61 ms: 1.02x slower                                                                                            |
| deepcopy_memo              | 37.9 us                                                                                              | 38.5 us: 1.02x slower                                                                                            |
| dulwich_log                | 67.0 ms                                                                                              | 68.7 ms: 1.03x slower                                                                                            |
| float                      | 83.1 ms                                                                                              | 85.3 ms: 1.03x slower                                                                                            |
| sqlglot_optimize           | 54.2 ms                                                                                              | 55.7 ms: 1.03x slower                                                                                            |
| scimark_fft                | 359 ms                                                                                               | 369 ms: 1.03x slower                                                                                             |
| 2to3                       | 269 ms                                                                                               | 277 ms: 1.03x slower                                                                                             |
| regex_v8                   | 24.4 ms                                                                                              | 25.2 ms: 1.03x slower                                                                                            |
| sympy_str                  | 274 ms                                                                                               | 283 ms: 1.03x slower                                                                                             |
| logging_silent             | 97.7 ns                                                                                              | 101 ns: 1.04x slower                                                                                             |
| sympy_integrate            | 19.9 ms                                                                                              | 20.6 ms: 1.04x slower                                                                                            |
| mdp                        | 2.61 sec                                                                                             | 2.71 sec: 1.04x slower                                                                                           |
| scimark_lu                 | 113 ms                                                                                               | 117 ms: 1.04x slower                                                                                             |
| deltablue                  | 3.24 ms                                                                                              | 3.37 ms: 1.04x slower                                                                                            |
| djangocms                  | 31.5 us                                                                                              | 32.8 us: 1.04x slower                                                                                            |
| gc_traversal               | 3.55 ms                                                                                              | 3.72 ms: 1.05x slower                                                                                            |
| regex_compile              | 132 ms                                                                                               | 138 ms: 1.05x slower                                                                                             |
| sympy_expand               | 462 ms                                                                                               | 484 ms: 1.05x slower                                                                                             |
| fannkuch                   | 401 ms                                                                                               | 420 ms: 1.05x slower                                                                                             |
| pprint_safe_repr           | 734 ms                                                                                               | 770 ms: 1.05x slower                                                                                             |
| raytrace                   | 265 ms                                                                                               | 279 ms: 1.05x slower                                                                                             |
| sympy_sum                  | 150 ms                                                                                               | 159 ms: 1.05x slower                                                                                             |
| unpickle_pure_python       | 217 us                                                                                               | 230 us: 1.06x slower                                                                                             |
| go                         | 139 ms                                                                                               | 148 ms: 1.06x slower                                                                                             |
| pyflate                    | 474 ms                                                                                               | 507 ms: 1.07x slower                                                                                             |
| flaskblogging              | 8.75 ms                                                                                              | 9.37 ms: 1.07x slower                                                                                            |
| mako                       | 11.2 ms                                                                                              | 12.1 ms: 1.08x slower                                                                                            |
| pprint_pformat             | 1.51 sec                                                                                             | 1.63 sec: 1.08x slower                                                                                           |
| crypto_pyaes               | 72.0 ms                                                                                              | 78.6 ms: 1.09x slower                                                                                            |
| scimark_monte_carlo        | 67.2 ms                                                                                              | 74.5 ms: 1.11x slower                                                                                            |
| nbody                      | 92.1 ms                                                                                              | 103 ms: 1.12x slower                                                                                             |
| nqueens                    | 81.0 ms                                                                                              | 91.0 ms: 1.12x slower                                                                                            |
| comprehensions             | 16.2 us                                                                                              | 18.3 us: 1.13x slower                                                                                            |
| chaos                      | 61.2 ms                                                                                              | 69.5 ms: 1.14x slower                                                                                            |
| scimark_sparse_mat_mult    | 4.64 ms                                                                                              | 5.30 ms: 1.14x slower                                                                                            |
| spectral_norm              | 111 ms                                                                                               | 132 ms: 1.19x slower                                                                                             |
| hexiom                     | 6.20 ms                                                                                              | 7.76 ms: 1.25x slower                                                                                            |
| Geometric mean             | (ref)                                                                                                | 1.02x slower                                                                                                     |

Benchmark hidden because not significant (16): async_tree_none, async_tree_memoization, logging_format, typing_runtime_protocols, logging_simple, genshi_xml, gunicorn, tornado_http, html5lib, xml_etree_iterparse, mypy2, meteor_contest, bench_thread_pool, telco, aiohttp, pylint
Ignored benchmarks (2) of results/bm-20240215-3.13.0a4-9d34f60-PYTHON_UOPS/bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60.json: bpe_tokeniser, unpack_sequence

- Geometric mean (including insignificant results): 1.019x slower
# HPT report

- Reliability score: 87.78% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.04x