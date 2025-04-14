# Results vs. 3.12.0

- fork: python
- ref: v3.14.0a1
- machine: linux-x86_64
- commit hash: 8cdaca8
- commit date: 2024-10-15
- overall geometric mean: 1.006x slower
- HPT reliability: 61.16%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 314 ms: 1.10x slower                                             |
| docutils       | 2.87 sec                                                     | 3.17 sec: 1.11x slower                                           |
| tornado_http   | 121 ms                                                       | 123 ms: 1.02x slower                                             |
| Geometric mean | (ref)                                                        | 1.07x slower                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_memoization_tg  | 540 ms                                                       | 373 ms: 1.45x faster                                             |
| async_tree_none            | 452 ms                                                       | 333 ms: 1.36x faster                                             |
| async_tree_memoization     | 544 ms                                                       | 408 ms: 1.33x faster                                             |
| async_tree_none_tg         | 431 ms                                                       | 323 ms: 1.33x faster                                             |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 557 ms: 1.25x faster                                             |
| async_tree_io              | 1.04 sec                                                     | 846 ms: 1.23x faster                                             |
| async_tree_io_tg           | 1.05 sec                                                     | 865 ms: 1.22x faster                                             |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 574 ms: 1.21x faster                                             |
| Geometric mean             | (ref)                                                        | 1.30x faster                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 251 ms: 1.05x faster                                             |
| nbody          | 88.0 ms                                                      | 83.7 ms: 1.05x faster                                            |
| float          | 76.6 ms                                                      | 79.3 ms: 1.03x slower                                            |
| Geometric mean | (ref)                                                        | 1.02x faster                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_dna      | 239 ms                                                       | 233 ms: 1.03x faster                                             |
| regex_compile  | 144 ms                                                       | 150 ms: 1.04x slower                                             |
| regex_v8       | 23.6 ms                                                      | 25.0 ms: 1.06x slower                                            |
| Geometric mean | (ref)                                                        | 1.02x slower                                                     |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| xml_etree_generate   | 86.1 ms                                                      | 80.6 ms: 1.07x faster                                            |
| xml_etree_iterparse  | 103 ms                                                       | 99.5 ms: 1.03x faster                                            |
| tomli_loads          | 2.16 sec                                                     | 2.12 sec: 1.02x faster                                           |
| xml_etree_process    | 58.4 ms                                                      | 57.7 ms: 1.01x faster                                            |
| xml_etree_parse      | 144 ms                                                       | 145 ms: 1.01x slower                                             |
| pickle_dict          | 32.5 us                                                      | 32.9 us: 1.01x slower                                            |
| json_loads           | 24.4 us                                                      | 24.6 us: 1.01x slower                                            |
| pickle               | 10.5 us                                                      | 10.7 us: 1.02x slower                                            |
| pickle_pure_python   | 318 us                                                       | 333 us: 1.05x slower                                             |
| pickle_list          | 4.43 us                                                      | 4.66 us: 1.05x slower                                            |
| unpickle_pure_python | 210 us                                                       | 221 us: 1.06x slower                                             |
| json_dumps           | 10.2 ms                                                      | 11.2 ms: 1.10x slower                                            |
| Geometric mean       | (ref)                                                        | 1.01x slower                                                     |

Benchmark hidden because not significant (2): unpickle_list, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 9.01 ms: 1.04x slower                                            |
| python_startup         | 11.6 ms                                                      | 14.9 ms: 1.28x slower                                            |
| Geometric mean         | (ref)                                                        | 1.16x slower                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| mako            | 10.0 ms                                                      | 9.52 ms: 1.05x faster                                            |
| django_template | 38.2 ms                                                      | 42.9 ms: 1.12x slower                                            |
| Geometric mean  | (ref)                                                        | 1.03x slower                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_memoization_tg  | 540 ms                                                       | 373 ms: 1.45x faster                                             |
| async_tree_none            | 452 ms                                                       | 333 ms: 1.36x faster                                             |
| async_tree_memoization     | 544 ms                                                       | 408 ms: 1.33x faster                                             |
| async_tree_none_tg         | 431 ms                                                       | 323 ms: 1.33x faster                                             |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 557 ms: 1.25x faster                                             |
| deepcopy_memo              | 36.8 us                                                      | 29.9 us: 1.23x faster                                            |
| async_tree_io              | 1.04 sec                                                     | 846 ms: 1.23x faster                                             |
| async_tree_io_tg           | 1.05 sec                                                     | 865 ms: 1.22x faster                                             |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 574 ms: 1.21x faster                                             |
| deepcopy                   | 368 us                                                       | 309 us: 1.19x faster                                             |
| pathlib                    | 18.9 ms                                                      | 15.9 ms: 1.19x faster                                            |
| comprehensions             | 21.9 us                                                      | 18.8 us: 1.16x faster                                            |
| crypto_pyaes               | 80.3 ms                                                      | 72.2 ms: 1.11x faster                                            |
| deepcopy_reduce            | 3.37 us                                                      | 3.10 us: 1.09x faster                                            |
| xml_etree_generate         | 86.1 ms                                                      | 80.6 ms: 1.07x faster                                            |
| coroutines                 | 23.0 ms                                                      | 21.6 ms: 1.06x faster                                            |
| scimark_sor                | 109 ms                                                       | 103 ms: 1.06x faster                                             |
| pidigits                   | 265 ms                                                       | 251 ms: 1.05x faster                                             |
| nbody                      | 88.0 ms                                                      | 83.7 ms: 1.05x faster                                            |
| mako                       | 10.0 ms                                                      | 9.52 ms: 1.05x faster                                            |
| scimark_fft                | 301 ms                                                       | 290 ms: 1.04x faster                                             |
| logging_format             | 7.48 us                                                      | 7.21 us: 1.04x faster                                            |
| scimark_lu                 | 98.8 ms                                                      | 95.5 ms: 1.03x faster                                            |
| xml_etree_iterparse        | 103 ms                                                       | 99.5 ms: 1.03x faster                                            |
| async_generators           | 390 ms                                                       | 379 ms: 1.03x faster                                             |
| regex_dna                  | 239 ms                                                       | 233 ms: 1.03x faster                                             |
| tomli_loads                | 2.16 sec                                                     | 2.12 sec: 1.02x faster                                           |
| sqlite_synth               | 2.77 us                                                      | 2.73 us: 1.02x faster                                            |
| asyncio_websockets         | 387 ms                                                       | 381 ms: 1.01x faster                                             |
| logging_simple             | 6.71 us                                                      | 6.62 us: 1.01x faster                                            |
| dulwich_log                | 65.4 ms                                                      | 64.5 ms: 1.01x faster                                            |
| xml_etree_process          | 58.4 ms                                                      | 57.7 ms: 1.01x faster                                            |
| pprint_safe_repr           | 807 ms                                                       | 798 ms: 1.01x faster                                             |
| scimark_monte_carlo        | 69.0 ms                                                      | 68.4 ms: 1.01x faster                                            |
| pprint_pformat             | 1.65 sec                                                     | 1.64 sec: 1.01x faster                                           |
| xml_etree_parse            | 144 ms                                                       | 145 ms: 1.01x slower                                             |
| mdp                        | 2.57 sec                                                     | 2.59 sec: 1.01x slower                                           |
| pickle_dict                | 32.5 us                                                      | 32.9 us: 1.01x slower                                            |
| json_loads                 | 24.4 us                                                      | 24.6 us: 1.01x slower                                            |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.26 ms: 1.01x slower                                            |
| spectral_norm              | 91.6 ms                                                      | 93.0 ms: 1.02x slower                                            |
| pickle                     | 10.5 us                                                      | 10.7 us: 1.02x slower                                            |
| tornado_http               | 121 ms                                                       | 123 ms: 1.02x slower                                             |
| go                         | 150 ms                                                       | 152 ms: 1.02x slower                                             |
| richards                   | 45.7 ms                                                      | 46.6 ms: 1.02x slower                                            |
| deltablue                  | 3.24 ms                                                      | 3.30 ms: 1.02x slower                                            |
| fannkuch                   | 350 ms                                                       | 361 ms: 1.03x slower                                             |
| float                      | 76.6 ms                                                      | 79.3 ms: 1.03x slower                                            |
| meteor_contest             | 128 ms                                                       | 133 ms: 1.04x slower                                             |
| chaos                      | 64.0 ms                                                      | 66.5 ms: 1.04x slower                                            |
| python_startup_no_site     | 8.64 ms                                                      | 9.01 ms: 1.04x slower                                            |
| regex_compile              | 144 ms                                                       | 150 ms: 1.04x slower                                             |
| richards_super             | 51.3 ms                                                      | 53.6 ms: 1.04x slower                                            |
| pickle_pure_python         | 318 us                                                       | 333 us: 1.05x slower                                             |
| pycparser                  | 1.23 sec                                                     | 1.29 sec: 1.05x slower                                           |
| generators                 | 37.4 ms                                                      | 39.4 ms: 1.05x slower                                            |
| pickle_list                | 4.43 us                                                      | 4.66 us: 1.05x slower                                            |
| unpickle_pure_python       | 210 us                                                       | 221 us: 1.06x slower                                             |
| raytrace                   | 298 ms                                                       | 315 ms: 1.06x slower                                             |
| sympy_str                  | 302 ms                                                       | 319 ms: 1.06x slower                                             |
| regex_v8                   | 23.6 ms                                                      | 25.0 ms: 1.06x slower                                            |
| sympy_sum                  | 162 ms                                                       | 173 ms: 1.07x slower                                             |
| pyflate                    | 439 ms                                                       | 473 ms: 1.08x slower                                             |
| sqlglot_parse              | 1.38 ms                                                      | 1.50 ms: 1.09x slower                                            |
| sympy_expand               | 484 ms                                                       | 530 ms: 1.09x slower                                             |
| json_dumps                 | 10.2 ms                                                      | 11.2 ms: 1.10x slower                                            |
| 2to3                       | 285 ms                                                       | 314 ms: 1.10x slower                                             |
| docutils                   | 2.87 sec                                                     | 3.17 sec: 1.11x slower                                           |
| sqlglot_transpile          | 1.78 ms                                                      | 1.98 ms: 1.11x slower                                            |
| telco                      | 6.96 ms                                                      | 7.80 ms: 1.12x slower                                            |
| django_template            | 38.2 ms                                                      | 42.9 ms: 1.12x slower                                            |
| sympy_integrate            | 23.9 ms                                                      | 27.3 ms: 1.14x slower                                            |
| sqlglot_normalize          | 116 ms                                                       | 132 ms: 1.15x slower                                             |
| nqueens                    | 89.9 ms                                                      | 104 ms: 1.15x slower                                             |
| typing_runtime_protocols   | 152 us                                                       | 180 us: 1.18x slower                                             |
| coverage                   | 66.7 ms                                                      | 79.2 ms: 1.19x slower                                            |
| hexiom                     | 5.96 ms                                                      | 7.11 ms: 1.19x slower                                            |
| sqlglot_optimize           | 57.5 ms                                                      | 69.7 ms: 1.21x slower                                            |
| python_startup             | 11.6 ms                                                      | 14.9 ms: 1.28x slower                                            |
| gc_traversal               | 3.48 ms                                                      | 5.21 ms: 1.50x slower                                            |
| unpack_sequence            | 53.2 ns                                                      | 89.6 ns: 1.69x slower                                            |
| create_gc_cycles           | 1.59 ms                                                      | 2.90 ms: 1.83x slower                                            |
| bench_mp_pool              | 4.76 ms                                                      | 2.28 sec: 479.50x slower                                         |
| Geometric mean             | (ref)                                                        | 1.08x slower                                                     |

Benchmark hidden because not significant (8): json, logging_silent, asyncio_tcp, asyncio_tcp_ssl, regex_effbot, bench_thread_pool, unpickle_list, unpickle
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (7) of results/bm-20241015-3.14.0a1-8cdaca8-JIT/bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift

- Geometric mean (including insignificant results): 1.006x slower
# HPT report

- Reliability score: 61.16% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.09x