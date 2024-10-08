# Results vs. 3.13.0b2

- fork: mdboom
- ref: marshal_slice
- machine: linux-x86_64
- commit hash: 0e19ac7
- commit date: 2024-10-07
- overall geometric mean: 1.03x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-pythonperf2-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------|:----------------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 291 ms                                                           | 279 ms: 1.05x faster                                                 |
| docutils       | 2.98 sec                                                         | 2.90 sec: 1.03x faster                                               |
| html5lib       | 74.7 ms                                                          | 70.8 ms: 1.05x faster                                                |
| tornado_http   | 119 ms                                                           | 115 ms: 1.03x faster                                                 |
| Geometric mean | (ref)                                                            | 1.04x faster                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-pythonperf2-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------------------|:----------------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_io_tg           | 900 ms                                                           | 780 ms: 1.15x faster                                                 |
| async_tree_memoization     | 460 ms                                                           | 398 ms: 1.15x faster                                                 |
| async_tree_none            | 365 ms                                                           | 318 ms: 1.15x faster                                                 |
| async_tree_none_tg         | 340 ms                                                           | 305 ms: 1.12x faster                                                 |
| async_tree_io              | 873 ms                                                           | 806 ms: 1.08x faster                                                 |
| async_tree_memoization_tg  | 421 ms                                                           | 389 ms: 1.08x faster                                                 |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 571 ms: 1.06x faster                                                 |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 546 ms: 1.05x faster                                                 |
| Geometric mean             | (ref)                                                            | 1.10x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-pythonperf2-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------|:----------------------------------------------------------------:|:--------------------------------------------------------------------:|
| float          | 80.2 ms                                                          | 78.8 ms: 1.02x faster                                                |
| pidigits       | 254 ms                                                           | 253 ms: 1.00x faster                                                 |
| Geometric mean | (ref)                                                            | 1.01x faster                                                         |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-pythonperf2-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------|:----------------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                           | 139 ms: 1.03x faster                                                 |
| regex_dna      | 249 ms                                                           | 252 ms: 1.01x slower                                                 |
| regex_effbot   | 3.40 ms                                                          | 3.50 ms: 1.03x slower                                                |
| regex_v8       | 26.0 ms                                                          | 26.9 ms: 1.03x slower                                                |
| Geometric mean | (ref)                                                            | 1.01x slower                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-pythonperf2-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------------|:----------------------------------------------------------------:|:--------------------------------------------------------------------:|
| xml_etree_iterparse  | 103 ms                                                           | 98.5 ms: 1.04x faster                                                |
| unpickle             | 15.7 us                                                          | 15.1 us: 1.04x faster                                                |
| unpickle_pure_python | 224 us                                                           | 217 us: 1.03x faster                                                 |
| xml_etree_parse      | 144 ms                                                           | 140 ms: 1.03x faster                                                 |
| json_loads           | 25.0 us                                                          | 24.6 us: 1.02x faster                                                |
| pickle_dict          | 32.8 us                                                          | 32.4 us: 1.01x faster                                                |
| xml_etree_generate   | 85.7 ms                                                          | 85.1 ms: 1.01x faster                                                |
| pickle               | 10.6 us                                                          | 10.7 us: 1.01x slower                                                |
| pickle_pure_python   | 307 us                                                           | 310 us: 1.01x slower                                                 |
| pickle_list          | 4.44 us                                                          | 4.65 us: 1.05x slower                                                |
| tomli_loads          | 2.40 sec                                                         | 2.52 sec: 1.05x slower                                               |
| Geometric mean       | (ref)                                                            | 1.00x faster                                                         |

Benchmark hidden because not significant (3): xml_etree_process, unpickle_list, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-pythonperf2-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|------------------------|:----------------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup_no_site | 8.85 ms                                                          | 9.01 ms: 1.02x slower                                                |
| python_startup         | 13.2 ms                                                          | 13.5 ms: 1.02x slower                                                |
| Geometric mean         | (ref)                                                            | 1.02x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-pythonperf2-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------|:----------------------------------------------------------------:|:--------------------------------------------------------------------:|
| genshi_xml     | 58.1 ms                                                          | 52.8 ms: 1.10x faster                                                |
| genshi_text    | 25.9 ms                                                          | 24.2 ms: 1.07x faster                                                |
| Geometric mean | (ref)                                                            | 1.04x faster                                                         |

Benchmark hidden because not significant (2): mako, django_template

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-pythonperf2-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------------------|:----------------------------------------------------------------:|:--------------------------------------------------------------------:|
| deepcopy                   | 377 us                                                           | 285 us: 1.32x faster                                                 |
| deepcopy_memo              | 37.3 us                                                          | 29.0 us: 1.29x faster                                                |
| go                         | 165 ms                                                           | 133 ms: 1.24x faster                                                 |
| generators                 | 33.5 ms                                                          | 28.1 ms: 1.19x faster                                                |
| deepcopy_reduce            | 3.39 us                                                          | 2.89 us: 1.17x faster                                                |
| async_tree_io_tg           | 900 ms                                                           | 780 ms: 1.15x faster                                                 |
| async_tree_memoization     | 460 ms                                                           | 398 ms: 1.15x faster                                                 |
| async_tree_none            | 365 ms                                                           | 318 ms: 1.15x faster                                                 |
| async_tree_none_tg         | 340 ms                                                           | 305 ms: 1.12x faster                                                 |
| genshi_xml                 | 58.1 ms                                                          | 52.8 ms: 1.10x faster                                                |
| richards_super             | 61.2 ms                                                          | 55.8 ms: 1.10x faster                                                |
| scimark_fft                | 312 ms                                                           | 284 ms: 1.10x faster                                                 |
| pathlib                    | 17.1 ms                                                          | 15.7 ms: 1.09x faster                                                |
| async_tree_io              | 873 ms                                                           | 806 ms: 1.08x faster                                                 |
| async_tree_memoization_tg  | 421 ms                                                           | 389 ms: 1.08x faster                                                 |
| genshi_text                | 25.9 ms                                                          | 24.2 ms: 1.07x faster                                                |
| scimark_sor                | 119 ms                                                           | 111 ms: 1.07x faster                                                 |
| bpe_tokeniser              | 5.14 sec                                                         | 4.82 sec: 1.07x faster                                               |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 571 ms: 1.06x faster                                                 |
| html5lib                   | 74.7 ms                                                          | 70.8 ms: 1.05x faster                                                |
| telco                      | 8.40 ms                                                          | 7.96 ms: 1.05x faster                                                |
| coroutines                 | 22.0 ms                                                          | 20.9 ms: 1.05x faster                                                |
| richards                   | 53.4 ms                                                          | 50.8 ms: 1.05x faster                                                |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 546 ms: 1.05x faster                                                 |
| scimark_lu                 | 97.5 ms                                                          | 93.1 ms: 1.05x faster                                                |
| 2to3                       | 291 ms                                                           | 279 ms: 1.05x faster                                                 |
| logging_simple             | 6.40 us                                                          | 6.14 us: 1.04x faster                                                |
| xml_etree_iterparse        | 103 ms                                                           | 98.5 ms: 1.04x faster                                                |
| unpickle                   | 15.7 us                                                          | 15.1 us: 1.04x faster                                                |
| regex_compile              | 144 ms                                                           | 139 ms: 1.03x faster                                                 |
| tornado_http               | 119 ms                                                           | 115 ms: 1.03x faster                                                 |
| gc_traversal               | 4.69 ms                                                          | 4.53 ms: 1.03x faster                                                |
| unpickle_pure_python       | 224 us                                                           | 217 us: 1.03x faster                                                 |
| json                       | 5.35 ms                                                          | 5.19 ms: 1.03x faster                                                |
| logging_format             | 7.11 us                                                          | 6.89 us: 1.03x faster                                                |
| hexiom                     | 6.35 ms                                                          | 6.16 ms: 1.03x faster                                                |
| docutils                   | 2.98 sec                                                         | 2.90 sec: 1.03x faster                                               |
| xml_etree_parse            | 144 ms                                                           | 140 ms: 1.03x faster                                                 |
| async_generators           | 363 ms                                                           | 353 ms: 1.03x faster                                                 |
| scimark_sparse_mat_mult    | 4.28 ms                                                          | 4.17 ms: 1.03x faster                                                |
| meteor_contest             | 128 ms                                                           | 125 ms: 1.03x faster                                                 |
| scimark_monte_carlo        | 65.5 ms                                                          | 63.8 ms: 1.03x faster                                                |
| sqlglot_normalize          | 120 ms                                                           | 117 ms: 1.03x faster                                                 |
| pprint_safe_repr           | 818 ms                                                           | 797 ms: 1.03x faster                                                 |
| sympy_sum                  | 155 ms                                                           | 152 ms: 1.02x faster                                                 |
| sqlite_synth               | 2.80 us                                                          | 2.74 us: 1.02x faster                                                |
| thrift                     | 880 us                                                           | 864 us: 1.02x faster                                                 |
| pprint_pformat             | 1.66 sec                                                         | 1.63 sec: 1.02x faster                                               |
| float                      | 80.2 ms                                                          | 78.8 ms: 1.02x faster                                                |
| crypto_pyaes               | 73.6 ms                                                          | 72.3 ms: 1.02x faster                                                |
| json_loads                 | 25.0 us                                                          | 24.6 us: 1.02x faster                                                |
| asyncio_websockets         | 395 ms                                                           | 389 ms: 1.02x faster                                                 |
| sympy_str                  | 295 ms                                                           | 291 ms: 1.01x faster                                                 |
| pickle_dict                | 32.8 us                                                          | 32.4 us: 1.01x faster                                                |
| sqlglot_optimize           | 59.5 ms                                                          | 59.0 ms: 1.01x faster                                                |
| dulwich_log                | 67.3 ms                                                          | 66.7 ms: 1.01x faster                                                |
| sympy_expand               | 501 ms                                                           | 497 ms: 1.01x faster                                                 |
| xml_etree_generate         | 85.7 ms                                                          | 85.1 ms: 1.01x faster                                                |
| spectral_norm              | 97.3 ms                                                          | 96.8 ms: 1.01x faster                                                |
| asyncio_tcp                | 378 ms                                                           | 376 ms: 1.00x faster                                                 |
| pidigits                   | 254 ms                                                           | 253 ms: 1.00x faster                                                 |
| sympy_integrate            | 23.2 ms                                                          | 23.3 ms: 1.01x slower                                                |
| nqueens                    | 88.4 ms                                                          | 89.0 ms: 1.01x slower                                                |
| pickle                     | 10.6 us                                                          | 10.7 us: 1.01x slower                                                |
| pickle_pure_python         | 307 us                                                           | 310 us: 1.01x slower                                                 |
| regex_dna                  | 249 ms                                                           | 252 ms: 1.01x slower                                                 |
| sqlglot_parse              | 1.39 ms                                                          | 1.41 ms: 1.01x slower                                                |
| sqlglot_transpile          | 1.76 ms                                                          | 1.79 ms: 1.01x slower                                                |
| pyflate                    | 482 ms                                                           | 488 ms: 1.01x slower                                                 |
| mdp                        | 2.46 sec                                                         | 2.50 sec: 1.01x slower                                               |
| fannkuch                   | 353 ms                                                           | 359 ms: 1.02x slower                                                 |
| python_startup_no_site     | 8.85 ms                                                          | 9.01 ms: 1.02x slower                                                |
| python_startup             | 13.2 ms                                                          | 13.5 ms: 1.02x slower                                                |
| raytrace                   | 260 ms                                                           | 266 ms: 1.02x slower                                                 |
| comprehensions             | 17.0 us                                                          | 17.3 us: 1.02x slower                                                |
| regex_effbot               | 3.40 ms                                                          | 3.50 ms: 1.03x slower                                                |
| logging_silent             | 96.3 ns                                                          | 99.3 ns: 1.03x slower                                                |
| regex_v8                   | 26.0 ms                                                          | 26.9 ms: 1.03x slower                                                |
| pickle_list                | 4.44 us                                                          | 4.65 us: 1.05x slower                                                |
| chaos                      | 59.6 ms                                                          | 62.5 ms: 1.05x slower                                                |
| tomli_loads                | 2.40 sec                                                         | 2.52 sec: 1.05x slower                                               |
| bench_mp_pool              | 4.91 ms                                                          | 1.98 sec: 402.72x slower                                             |
| Geometric mean             | (ref)                                                            | 1.03x slower                                                         |

Benchmark hidden because not significant (14): bench_thread_pool, nbody, pycparser, typing_runtime_protocols, xml_etree_process, asyncio_tcp_ssl, mako, coverage, django_template, deltablue, unpickle_list, json_dumps, create_gc_cycles, pylint
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20241007-3.14.0a0-0e19ac7/bm-20241007-pythonperf2-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7.json: unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.00x