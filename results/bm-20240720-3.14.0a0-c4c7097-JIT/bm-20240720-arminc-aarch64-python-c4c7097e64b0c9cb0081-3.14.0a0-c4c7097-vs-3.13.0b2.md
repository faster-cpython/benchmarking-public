# Results vs. 3.13.0b2

- fork: python
- ref: c4c7097e64b0c9cb0081
- machine: linux-aarch64
- commit hash: c4c7097
- commit date: 2024-07-20
- overall geometric mean: 1.06x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 305 ms                                                       | 362 ms: 1.19x slower                                                    |
| docutils       | 3.10 sec                                                     | 3.63 sec: 1.17x slower                                                  |
| html5lib       | 66.1 ms                                                      | 70.9 ms: 1.07x slower                                                   |
| tornado_http   | 128 ms                                                       | 136 ms: 1.07x slower                                                    |
| Geometric mean | (ref)                                                        | 1.12x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none_tg         | 476 ms                                                       | 413 ms: 1.15x faster                                                    |
| async_tree_memoization     | 645 ms                                                       | 573 ms: 1.12x faster                                                    |
| async_tree_io_tg           | 1.27 sec                                                     | 1.14 sec: 1.12x faster                                                  |
| async_tree_memoization_tg  | 604 ms                                                       | 547 ms: 1.10x faster                                                    |
| async_tree_io              | 1.22 sec                                                     | 1.11 sec: 1.10x faster                                                  |
| async_tree_none            | 492 ms                                                       | 451 ms: 1.09x faster                                                    |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 742 ms: 1.07x faster                                                    |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 725 ms: 1.05x faster                                                    |
| Geometric mean             | (ref)                                                        | 1.10x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 91.4 ms                                                      | 90.5 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                        | 1.00x faster                                                            |

Benchmark hidden because not significant (2): nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 31.1 ms                                                      | 30.7 ms: 1.01x faster                                                   |
| regex_dna      | 259 ms                                                       | 256 ms: 1.01x faster                                                    |
| regex_compile  | 128 ms                                                       | 176 ms: 1.38x slower                                                    |
| Geometric mean | (ref)                                                        | 1.08x slower                                                            |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_generate   | 114 ms                                                       | 111 ms: 1.02x faster                                                    |
| tomli_loads          | 2.57 sec                                                     | 2.61 sec: 1.01x slower                                                  |
| json_dumps           | 13.1 ms                                                      | 13.4 ms: 1.02x slower                                                   |
| json_loads           | 32.1 us                                                      | 32.9 us: 1.02x slower                                                   |
| pickle_pure_python   | 359 us                                                       | 385 us: 1.07x slower                                                    |
| unpickle_pure_python | 251 us                                                       | 272 us: 1.08x slower                                                    |
| Geometric mean       | (ref)                                                        | 1.03x slower                                                            |

Benchmark hidden because not significant (3): xml_etree_process, xml_etree_parse, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.60 ms                                                      | 8.85 ms: 1.03x slower                                                   |
| Geometric mean         | (ref)                                                        | 1.01x slower                                                            |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|-----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 13.2 ms                                                      | 13.1 ms: 1.01x faster                                                   |
| django_template | 42.3 ms                                                      | 50.3 ms: 1.19x slower                                                   |
| genshi_text     | 27.4 ms                                                      | 34.5 ms: 1.26x slower                                                   |
| genshi_xml      | 60.4 ms                                                      | 81.2 ms: 1.34x slower                                                   |
| Geometric mean  | (ref)                                                        | 1.19x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy_memo              | 50.8 us                                                      | 37.8 us: 1.34x faster                                                   |
| deepcopy                   | 448 us                                                       | 376 us: 1.19x faster                                                    |
| async_tree_none_tg         | 476 ms                                                       | 413 ms: 1.15x faster                                                    |
| async_tree_memoization     | 645 ms                                                       | 573 ms: 1.12x faster                                                    |
| async_tree_io_tg           | 1.27 sec                                                     | 1.14 sec: 1.12x faster                                                  |
| async_tree_memoization_tg  | 604 ms                                                       | 547 ms: 1.10x faster                                                    |
| async_tree_io              | 1.22 sec                                                     | 1.11 sec: 1.10x faster                                                  |
| async_tree_none            | 492 ms                                                       | 451 ms: 1.09x faster                                                    |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 742 ms: 1.07x faster                                                    |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 725 ms: 1.05x faster                                                    |
| richards                   | 55.9 ms                                                      | 53.8 ms: 1.04x faster                                                   |
| richards_super             | 62.3 ms                                                      | 60.7 ms: 1.03x faster                                                   |
| pathlib                    | 22.8 ms                                                      | 22.2 ms: 1.03x faster                                                   |
| xml_etree_generate         | 114 ms                                                       | 111 ms: 1.02x faster                                                    |
| coroutines                 | 29.0 ms                                                      | 28.5 ms: 1.02x faster                                                   |
| generators                 | 37.1 ms                                                      | 36.5 ms: 1.02x faster                                                   |
| regex_v8                   | 31.1 ms                                                      | 30.7 ms: 1.01x faster                                                   |
| float                      | 91.4 ms                                                      | 90.5 ms: 1.01x faster                                                   |
| regex_dna                  | 259 ms                                                       | 256 ms: 1.01x faster                                                    |
| mako                       | 13.2 ms                                                      | 13.1 ms: 1.01x faster                                                   |
| deepcopy_reduce            | 4.04 us                                                      | 4.02 us: 1.00x faster                                                   |
| bpe_tokeniser              | 5.83 sec                                                     | 5.87 sec: 1.01x slower                                                  |
| asyncio_websockets         | 657 ms                                                       | 666 ms: 1.01x slower                                                    |
| meteor_contest             | 113 ms                                                       | 115 ms: 1.01x slower                                                    |
| tomli_loads                | 2.57 sec                                                     | 2.61 sec: 1.01x slower                                                  |
| asyncio_tcp_ssl            | 2.21 sec                                                     | 2.25 sec: 1.02x slower                                                  |
| coverage                   | 98.4 ms                                                      | 100 ms: 1.02x slower                                                    |
| json_dumps                 | 13.1 ms                                                      | 13.4 ms: 1.02x slower                                                   |
| json_loads                 | 32.1 us                                                      | 32.9 us: 1.02x slower                                                   |
| scimark_fft                | 445 ms                                                       | 456 ms: 1.02x slower                                                    |
| bench_thread_pool          | 1.26 ms                                                      | 1.29 ms: 1.03x slower                                                   |
| fannkuch                   | 451 ms                                                       | 464 ms: 1.03x slower                                                    |
| scimark_sparse_mat_mult    | 6.55 ms                                                      | 6.74 ms: 1.03x slower                                                   |
| python_startup_no_site     | 8.60 ms                                                      | 8.85 ms: 1.03x slower                                                   |
| async_generators           | 488 ms                                                       | 505 ms: 1.04x slower                                                    |
| mdp                        | 3.33 sec                                                     | 3.45 sec: 1.04x slower                                                  |
| json                       | 5.64 ms                                                      | 5.85 ms: 1.04x slower                                                   |
| telco                      | 10.0 ms                                                      | 10.4 ms: 1.04x slower                                                   |
| spectral_norm              | 141 ms                                                       | 147 ms: 1.04x slower                                                    |
| asyncio_tcp                | 584 ms                                                       | 612 ms: 1.05x slower                                                    |
| pyflate                    | 557 ms                                                       | 589 ms: 1.06x slower                                                    |
| tornado_http               | 128 ms                                                       | 136 ms: 1.07x slower                                                    |
| dask                       | 370 ms                                                       | 396 ms: 1.07x slower                                                    |
| html5lib                   | 66.1 ms                                                      | 70.9 ms: 1.07x slower                                                   |
| pickle_pure_python         | 359 us                                                       | 385 us: 1.07x slower                                                    |
| typing_runtime_protocols   | 193 us                                                       | 209 us: 1.08x slower                                                    |
| unpickle_pure_python       | 251 us                                                       | 272 us: 1.08x slower                                                    |
| scimark_monte_carlo        | 82.3 ms                                                      | 89.4 ms: 1.09x slower                                                   |
| raytrace                   | 297 ms                                                       | 323 ms: 1.09x slower                                                    |
| scimark_sor                | 159 ms                                                       | 175 ms: 1.10x slower                                                    |
| sqlglot_normalize          | 129 ms                                                       | 142 ms: 1.10x slower                                                    |
| crypto_pyaes               | 82.0 ms                                                      | 90.3 ms: 1.10x slower                                                   |
| go                         | 161 ms                                                       | 177 ms: 1.10x slower                                                    |
| pycparser                  | 1.22 sec                                                     | 1.36 sec: 1.11x slower                                                  |
| sqlglot_optimize           | 62.6 ms                                                      | 70.0 ms: 1.12x slower                                                   |
| bench_mp_pool              | 7.03 ms                                                      | 7.86 ms: 1.12x slower                                                   |
| sqlglot_parse              | 1.42 ms                                                      | 1.60 ms: 1.13x slower                                                   |
| deltablue                  | 3.88 ms                                                      | 4.40 ms: 1.13x slower                                                   |
| comprehensions             | 20.5 us                                                      | 23.3 us: 1.13x slower                                                   |
| nqueens                    | 98.9 ms                                                      | 116 ms: 1.17x slower                                                    |
| docutils                   | 3.10 sec                                                     | 3.63 sec: 1.17x slower                                                  |
| django_template            | 42.3 ms                                                      | 50.3 ms: 1.19x slower                                                   |
| 2to3                       | 305 ms                                                       | 362 ms: 1.19x slower                                                    |
| pylint                     | 337 ms                                                       | 403 ms: 1.19x slower                                                    |
| sqlglot_transpile          | 1.71 ms                                                      | 2.05 ms: 1.20x slower                                                   |
| pprint_pformat             | 1.93 sec                                                     | 2.33 sec: 1.21x slower                                                  |
| pprint_safe_repr           | 933 ms                                                       | 1.13 sec: 1.21x slower                                                  |
| sympy_expand               | 457 ms                                                       | 569 ms: 1.25x slower                                                    |
| dulwich_log                | 58.5 ms                                                      | 72.9 ms: 1.25x slower                                                   |
| genshi_text                | 27.4 ms                                                      | 34.5 ms: 1.26x slower                                                   |
| sympy_integrate            | 20.9 ms                                                      | 26.7 ms: 1.28x slower                                                   |
| scimark_lu                 | 141 ms                                                       | 181 ms: 1.28x slower                                                    |
| hexiom                     | 7.08 ms                                                      | 9.12 ms: 1.29x slower                                                   |
| sympy_str                  | 265 ms                                                       | 343 ms: 1.29x slower                                                    |
| chaos                      | 68.3 ms                                                      | 89.1 ms: 1.31x slower                                                   |
| genshi_xml                 | 60.4 ms                                                      | 81.2 ms: 1.34x slower                                                   |
| sympy_sum                  | 144 ms                                                       | 197 ms: 1.37x slower                                                    |
| regex_compile              | 128 ms                                                       | 176 ms: 1.38x slower                                                    |
| Geometric mean             | (ref)                                                        | 1.06x slower                                                            |

Benchmark hidden because not significant (13): gc_traversal, logging_simple, xml_etree_process, regex_effbot, logging_silent, nbody, python_startup, thrift, logging_format, pidigits, create_gc_cycles, xml_etree_parse, xml_etree_iterparse
Ignored benchmarks (11) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 1.08x