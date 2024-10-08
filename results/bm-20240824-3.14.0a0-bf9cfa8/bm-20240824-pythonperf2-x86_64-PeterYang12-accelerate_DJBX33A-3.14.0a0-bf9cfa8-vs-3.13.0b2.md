# Results vs. 3.13.0b2

- fork: PeterYang12
- ref: accelerate_DJBX33A
- machine: linux-x86_64
- commit hash: bf9cfa8
- commit date: 2024-08-24
- overall geometric mean: 1.02x faster
- HPT reliability: 99.86%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240824-pythonperf2-x86_64-PeterYang12-accelerate_DJBX33A-3.14.0a0-bf9cfa8 |
|----------------|:----------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                           | 282 ms: 1.04x faster                                                           |
| docutils       | 2.98 sec                                                         | 2.96 sec: 1.01x faster                                                         |
| html5lib       | 74.7 ms                                                          | 74.0 ms: 1.01x faster                                                          |
| tornado_http   | 119 ms                                                           | 117 ms: 1.02x faster                                                           |
| Geometric mean | (ref)                                                            | 1.02x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240824-pythonperf2-x86_64-PeterYang12-accelerate_DJBX33A-3.14.0a0-bf9cfa8 |
|----------------------------|:----------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_memoization     | 460 ms                                                           | 397 ms: 1.16x faster                                                           |
| async_tree_io_tg           | 900 ms                                                           | 784 ms: 1.15x faster                                                           |
| async_tree_none            | 365 ms                                                           | 320 ms: 1.14x faster                                                           |
| async_tree_none_tg         | 340 ms                                                           | 309 ms: 1.10x faster                                                           |
| async_tree_io              | 873 ms                                                           | 803 ms: 1.09x faster                                                           |
| async_tree_memoization_tg  | 421 ms                                                           | 389 ms: 1.08x faster                                                           |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 571 ms: 1.06x faster                                                           |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 548 ms: 1.05x faster                                                           |
| Geometric mean             | (ref)                                                            | 1.10x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240824-pythonperf2-x86_64-PeterYang12-accelerate_DJBX33A-3.14.0a0-bf9cfa8 |
|----------------|:----------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 254 ms                                                           | 254 ms: 1.00x slower                                                           |
| nbody          | 87.8 ms                                                          | 92.6 ms: 1.05x slower                                                          |
| Geometric mean | (ref)                                                            | 1.02x slower                                                                   |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240824-pythonperf2-x86_64-PeterYang12-accelerate_DJBX33A-3.14.0a0-bf9cfa8 |
|----------------|:----------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                           | 141 ms: 1.02x faster                                                           |
| regex_dna      | 249 ms                                                           | 255 ms: 1.02x slower                                                           |
| regex_effbot   | 3.40 ms                                                          | 3.51 ms: 1.03x slower                                                          |
| regex_v8       | 26.0 ms                                                          | 27.1 ms: 1.04x slower                                                          |
| Geometric mean | (ref)                                                            | 1.02x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240824-pythonperf2-x86_64-PeterYang12-accelerate_DJBX33A-3.14.0a0-bf9cfa8 |
|----------------------|:----------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| unpickle_pure_python | 224 us                                                           | 218 us: 1.03x faster                                                           |
| xml_etree_iterparse  | 103 ms                                                           | 100 ms: 1.02x faster                                                           |
| json_dumps           | 10.8 ms                                                          | 10.6 ms: 1.02x faster                                                          |
| xml_etree_parse      | 144 ms                                                           | 142 ms: 1.01x faster                                                           |
| json_loads           | 25.0 us                                                          | 24.9 us: 1.00x faster                                                          |
| xml_etree_process    | 59.7 ms                                                          | 60.2 ms: 1.01x slower                                                          |
| pickle_pure_python   | 307 us                                                           | 313 us: 1.02x slower                                                           |
| tomli_loads          | 2.40 sec                                                         | 2.51 sec: 1.04x slower                                                         |
| Geometric mean       | (ref)                                                            | 1.00x faster                                                                   |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240824-pythonperf2-x86_64-PeterYang12-accelerate_DJBX33A-3.14.0a0-bf9cfa8 |
|------------------------|:----------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 13.2 ms                                                          | 13.3 ms: 1.01x slower                                                          |
| python_startup_no_site | 8.85 ms                                                          | 9.04 ms: 1.02x slower                                                          |
| Geometric mean         | (ref)                                                            | 1.02x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240824-pythonperf2-x86_64-PeterYang12-accelerate_DJBX33A-3.14.0a0-bf9cfa8 |
|-----------------|:----------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| genshi_xml      | 58.1 ms                                                          | 52.2 ms: 1.11x faster                                                          |
| genshi_text     | 25.9 ms                                                          | 24.1 ms: 1.07x faster                                                          |
| django_template | 39.0 ms                                                          | 40.5 ms: 1.04x slower                                                          |
| Geometric mean  | (ref)                                                            | 1.04x faster                                                                   |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240824-pythonperf2-x86_64-PeterYang12-accelerate_DJBX33A-3.14.0a0-bf9cfa8 |
|----------------------------|:----------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| deepcopy                   | 377 us                                                           | 290 us: 1.30x faster                                                           |
| deepcopy_memo              | 37.3 us                                                          | 30.2 us: 1.23x faster                                                          |
| deepcopy_reduce            | 3.39 us                                                          | 2.92 us: 1.16x faster                                                          |
| async_tree_memoization     | 460 ms                                                           | 397 ms: 1.16x faster                                                           |
| async_tree_io_tg           | 900 ms                                                           | 784 ms: 1.15x faster                                                           |
| generators                 | 33.5 ms                                                          | 29.3 ms: 1.14x faster                                                          |
| async_tree_none            | 365 ms                                                           | 320 ms: 1.14x faster                                                           |
| genshi_xml                 | 58.1 ms                                                          | 52.2 ms: 1.11x faster                                                          |
| async_tree_none_tg         | 340 ms                                                           | 309 ms: 1.10x faster                                                           |
| richards_super             | 61.2 ms                                                          | 55.7 ms: 1.10x faster                                                          |
| bench_mp_pool              | 4.91 ms                                                          | 4.48 ms: 1.09x faster                                                          |
| async_tree_io              | 873 ms                                                           | 803 ms: 1.09x faster                                                           |
| pathlib                    | 17.1 ms                                                          | 15.8 ms: 1.08x faster                                                          |
| async_tree_memoization_tg  | 421 ms                                                           | 389 ms: 1.08x faster                                                           |
| richards                   | 53.4 ms                                                          | 49.6 ms: 1.08x faster                                                          |
| genshi_text                | 25.9 ms                                                          | 24.1 ms: 1.07x faster                                                          |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 571 ms: 1.06x faster                                                           |
| bench_thread_pool          | 908 us                                                           | 862 us: 1.05x faster                                                           |
| gc_traversal               | 4.69 ms                                                          | 4.46 ms: 1.05x faster                                                          |
| scimark_fft                | 312 ms                                                           | 298 ms: 1.05x faster                                                           |
| coverage                   | 83.5 ms                                                          | 79.7 ms: 1.05x faster                                                          |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 548 ms: 1.05x faster                                                           |
| scimark_sparse_mat_mult    | 4.28 ms                                                          | 4.12 ms: 1.04x faster                                                          |
| bpe_tokeniser              | 5.14 sec                                                         | 4.96 sec: 1.04x faster                                                         |
| 2to3                       | 291 ms                                                           | 282 ms: 1.04x faster                                                           |
| thrift                     | 880 us                                                           | 853 us: 1.03x faster                                                           |
| unpickle_pure_python       | 224 us                                                           | 218 us: 1.03x faster                                                           |
| logging_format             | 7.11 us                                                          | 6.92 us: 1.03x faster                                                          |
| coroutines                 | 22.0 ms                                                          | 21.4 ms: 1.03x faster                                                          |
| logging_simple             | 6.40 us                                                          | 6.24 us: 1.03x faster                                                          |
| asyncio_tcp                | 378 ms                                                           | 368 ms: 1.03x faster                                                           |
| telco                      | 8.40 ms                                                          | 8.19 ms: 1.02x faster                                                          |
| xml_etree_iterparse        | 103 ms                                                           | 100 ms: 1.02x faster                                                           |
| regex_compile              | 144 ms                                                           | 141 ms: 1.02x faster                                                           |
| tornado_http               | 119 ms                                                           | 117 ms: 1.02x faster                                                           |
| hexiom                     | 6.35 ms                                                          | 6.22 ms: 1.02x faster                                                          |
| spectral_norm              | 97.3 ms                                                          | 95.3 ms: 1.02x faster                                                          |
| pyflate                    | 482 ms                                                           | 472 ms: 1.02x faster                                                           |
| json_dumps                 | 10.8 ms                                                          | 10.6 ms: 1.02x faster                                                          |
| crypto_pyaes               | 73.6 ms                                                          | 72.4 ms: 1.02x faster                                                          |
| sympy_sum                  | 155 ms                                                           | 153 ms: 1.02x faster                                                           |
| meteor_contest             | 128 ms                                                           | 127 ms: 1.01x faster                                                           |
| sqlglot_optimize           | 59.5 ms                                                          | 58.8 ms: 1.01x faster                                                          |
| xml_etree_parse            | 144 ms                                                           | 142 ms: 1.01x faster                                                           |
| asyncio_websockets         | 395 ms                                                           | 391 ms: 1.01x faster                                                           |
| scimark_lu                 | 97.5 ms                                                          | 96.5 ms: 1.01x faster                                                          |
| sympy_integrate            | 23.2 ms                                                          | 23.0 ms: 1.01x faster                                                          |
| docutils                   | 2.98 sec                                                         | 2.96 sec: 1.01x faster                                                         |
| html5lib                   | 74.7 ms                                                          | 74.0 ms: 1.01x faster                                                          |
| sympy_str                  | 295 ms                                                           | 292 ms: 1.01x faster                                                           |
| pprint_safe_repr           | 818 ms                                                           | 813 ms: 1.01x faster                                                           |
| asyncio_tcp_ssl            | 1.58 sec                                                         | 1.57 sec: 1.00x faster                                                         |
| sqlglot_normalize          | 120 ms                                                           | 120 ms: 1.00x faster                                                           |
| scimark_sor                | 119 ms                                                           | 118 ms: 1.00x faster                                                           |
| json_loads                 | 25.0 us                                                          | 24.9 us: 1.00x faster                                                          |
| pidigits                   | 254 ms                                                           | 254 ms: 1.00x slower                                                           |
| nqueens                    | 88.4 ms                                                          | 88.9 ms: 1.01x slower                                                          |
| xml_etree_process          | 59.7 ms                                                          | 60.2 ms: 1.01x slower                                                          |
| sympy_expand               | 501 ms                                                           | 505 ms: 1.01x slower                                                           |
| python_startup             | 13.2 ms                                                          | 13.3 ms: 1.01x slower                                                          |
| pycparser                  | 1.22 sec                                                         | 1.24 sec: 1.01x slower                                                         |
| sqlglot_transpile          | 1.76 ms                                                          | 1.79 ms: 1.02x slower                                                          |
| comprehensions             | 17.0 us                                                          | 17.3 us: 1.02x slower                                                          |
| pickle_pure_python         | 307 us                                                           | 313 us: 1.02x slower                                                           |
| sqlglot_parse              | 1.39 ms                                                          | 1.42 ms: 1.02x slower                                                          |
| python_startup_no_site     | 8.85 ms                                                          | 9.04 ms: 1.02x slower                                                          |
| regex_dna                  | 249 ms                                                           | 255 ms: 1.02x slower                                                           |
| mdp                        | 2.46 sec                                                         | 2.52 sec: 1.02x slower                                                         |
| typing_runtime_protocols   | 171 us                                                           | 175 us: 1.02x slower                                                           |
| scimark_monte_carlo        | 65.5 ms                                                          | 67.2 ms: 1.03x slower                                                          |
| chaos                      | 59.6 ms                                                          | 61.2 ms: 1.03x slower                                                          |
| logging_silent             | 96.3 ns                                                          | 98.9 ns: 1.03x slower                                                          |
| regex_effbot               | 3.40 ms                                                          | 3.51 ms: 1.03x slower                                                          |
| fannkuch                   | 353 ms                                                           | 365 ms: 1.04x slower                                                           |
| raytrace                   | 260 ms                                                           | 270 ms: 1.04x slower                                                           |
| django_template            | 39.0 ms                                                          | 40.5 ms: 1.04x slower                                                          |
| regex_v8                   | 26.0 ms                                                          | 27.1 ms: 1.04x slower                                                          |
| tomli_loads                | 2.40 sec                                                         | 2.51 sec: 1.04x slower                                                         |
| nbody                      | 87.8 ms                                                          | 92.6 ms: 1.05x slower                                                          |
| go                         | 165 ms                                                           | 177 ms: 1.07x slower                                                           |
| Geometric mean             | (ref)                                                            | 1.02x faster                                                                   |

Benchmark hidden because not significant (9): create_gc_cycles, mako, deltablue, json, async_generators, pprint_pformat, xml_etree_generate, float, pylint
Ignored benchmarks (13) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 99.86% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x