# Results vs. 3.13.0b2

- fork: python
- ref: e418fc3a6e7bade68ab5
- machine: linux-aarch64
- commit hash: e418fc3
- commit date: 2024-05-25
- overall geometric mean: 1.08x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-arminc-aarch64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 305 ms                                                       | 360 ms: 1.18x slower                                                    |
| chameleon      | 8.95 ms                                                      | 9.19 ms: 1.03x slower                                                   |
| docutils       | 3.10 sec                                                     | 3.58 sec: 1.16x slower                                                  |
| html5lib       | 66.1 ms                                                      | 71.3 ms: 1.08x slower                                                   |
| tornado_http   | 128 ms                                                       | 140 ms: 1.09x slower                                                    |
| Geometric mean | (ref)                                                        | 1.11x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-arminc-aarch64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.27 sec                                                     | 1.23 sec: 1.04x faster                                                  |
| async_tree_none            | 492 ms                                                       | 508 ms: 1.03x slower                                                    |
| async_tree_none_tg         | 476 ms                                                       | 491 ms: 1.03x slower                                                    |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 788 ms: 1.03x slower                                                    |
| async_tree_io              | 1.22 sec                                                     | 1.27 sec: 1.04x slower                                                  |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 822 ms: 1.04x slower                                                    |
| async_tree_memoization_tg  | 604 ms                                                       | 630 ms: 1.04x slower                                                    |
| async_tree_memoization     | 645 ms                                                       | 685 ms: 1.06x slower                                                    |
| Geometric mean             | (ref)                                                        | 1.03x slower                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-arminc-aarch64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 91.4 ms                                                      | 89.3 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                        | 1.01x faster                                                            |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-arminc-aarch64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 31.1 ms                                                      | 30.2 ms: 1.03x faster                                                   |
| regex_dna      | 259 ms                                                       | 251 ms: 1.03x faster                                                    |
| regex_effbot   | 4.98 ms                                                      | 4.90 ms: 1.02x faster                                                   |
| regex_compile  | 128 ms                                                       | 174 ms: 1.36x slower                                                    |
| Geometric mean | (ref)                                                        | 1.06x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-arminc-aarch64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| unpickle             | 19.8 us                                                      | 19.5 us: 1.01x faster                                                   |
| json_loads           | 32.1 us                                                      | 32.0 us: 1.00x faster                                                   |
| xml_etree_generate   | 114 ms                                                       | 115 ms: 1.02x slower                                                    |
| pickle               | 13.4 us                                                      | 13.7 us: 1.02x slower                                                   |
| xml_etree_iterparse  | 147 ms                                                       | 151 ms: 1.03x slower                                                    |
| tomli_loads          | 2.57 sec                                                     | 2.66 sec: 1.03x slower                                                  |
| unpickle_pure_python | 251 us                                                       | 275 us: 1.09x slower                                                    |
| pickle_pure_python   | 359 us                                                       | 405 us: 1.13x slower                                                    |
| Geometric mean       | (ref)                                                        | 1.02x slower                                                            |

Benchmark hidden because not significant (6): unpickle_list, pickle_list, xml_etree_process, pickle_dict, json_dumps, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-arminc-aarch64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 13.0 ms                                                      | 15.2 ms: 1.17x slower                                                   |
| python_startup_no_site | 8.60 ms                                                      | 10.7 ms: 1.25x slower                                                   |
| Geometric mean         | (ref)                                                        | 1.21x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-arminc-aarch64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|-----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 13.2 ms                                                      | 12.9 ms: 1.02x faster                                                   |
| django_template | 42.3 ms                                                      | 50.4 ms: 1.19x slower                                                   |
| genshi_text     | 27.4 ms                                                      | 34.8 ms: 1.27x slower                                                   |
| genshi_xml      | 60.4 ms                                                      | 81.7 ms: 1.35x slower                                                   |
| Geometric mean  | (ref)                                                        | 1.19x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-arminc-aarch64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pathlib                    | 22.8 ms                                                      | 21.9 ms: 1.04x faster                                                   |
| async_tree_io_tg           | 1.27 sec                                                     | 1.23 sec: 1.04x faster                                                  |
| regex_v8                   | 31.1 ms                                                      | 30.2 ms: 1.03x faster                                                   |
| regex_dna                  | 259 ms                                                       | 251 ms: 1.03x faster                                                    |
| float                      | 91.4 ms                                                      | 89.3 ms: 1.02x faster                                                   |
| deepcopy_memo              | 50.8 us                                                      | 49.7 us: 1.02x faster                                                   |
| richards                   | 55.9 ms                                                      | 54.7 ms: 1.02x faster                                                   |
| mako                       | 13.2 ms                                                      | 12.9 ms: 1.02x faster                                                   |
| regex_effbot               | 4.98 ms                                                      | 4.90 ms: 1.02x faster                                                   |
| unpickle                   | 19.8 us                                                      | 19.5 us: 1.01x faster                                                   |
| json_loads                 | 32.1 us                                                      | 32.0 us: 1.00x faster                                                   |
| asyncio_tcp_ssl            | 2.21 sec                                                     | 2.23 sec: 1.01x slower                                                  |
| asyncio_websockets         | 657 ms                                                       | 663 ms: 1.01x slower                                                    |
| coverage                   | 98.4 ms                                                      | 99.5 ms: 1.01x slower                                                   |
| xml_etree_generate         | 114 ms                                                       | 115 ms: 1.02x slower                                                    |
| telco                      | 10.0 ms                                                      | 10.2 ms: 1.02x slower                                                   |
| pickle                     | 13.4 us                                                      | 13.7 us: 1.02x slower                                                   |
| logging_simple             | 7.21 us                                                      | 7.38 us: 1.02x slower                                                   |
| chameleon                  | 8.95 ms                                                      | 9.19 ms: 1.03x slower                                                   |
| xml_etree_iterparse        | 147 ms                                                       | 151 ms: 1.03x slower                                                    |
| async_tree_none            | 492 ms                                                       | 508 ms: 1.03x slower                                                    |
| async_tree_none_tg         | 476 ms                                                       | 491 ms: 1.03x slower                                                    |
| mdp                        | 3.33 sec                                                     | 3.43 sec: 1.03x slower                                                  |
| logging_silent             | 133 ns                                                       | 138 ns: 1.03x slower                                                    |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 788 ms: 1.03x slower                                                    |
| spectral_norm              | 141 ms                                                       | 146 ms: 1.03x slower                                                    |
| async_generators           | 488 ms                                                       | 505 ms: 1.03x slower                                                    |
| tomli_loads                | 2.57 sec                                                     | 2.66 sec: 1.03x slower                                                  |
| async_tree_io              | 1.22 sec                                                     | 1.27 sec: 1.04x slower                                                  |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 822 ms: 1.04x slower                                                    |
| scimark_fft                | 445 ms                                                       | 462 ms: 1.04x slower                                                    |
| logging_format             | 7.82 us                                                      | 8.13 us: 1.04x slower                                                   |
| meteor_contest             | 113 ms                                                       | 118 ms: 1.04x slower                                                    |
| async_tree_memoization_tg  | 604 ms                                                       | 630 ms: 1.04x slower                                                    |
| asyncio_tcp                | 584 ms                                                       | 611 ms: 1.05x slower                                                    |
| fannkuch                   | 451 ms                                                       | 475 ms: 1.05x slower                                                    |
| dask                       | 370 ms                                                       | 391 ms: 1.05x slower                                                    |
| flaskblogging              | 4.70 ms                                                      | 4.96 ms: 1.06x slower                                                   |
| scimark_sparse_mat_mult    | 6.55 ms                                                      | 6.95 ms: 1.06x slower                                                   |
| async_tree_memoization     | 645 ms                                                       | 685 ms: 1.06x slower                                                    |
| bench_thread_pool          | 1.26 ms                                                      | 1.34 ms: 1.07x slower                                                   |
| generators                 | 37.1 ms                                                      | 39.9 ms: 1.07x slower                                                   |
| scimark_monte_carlo        | 82.3 ms                                                      | 88.6 ms: 1.08x slower                                                   |
| html5lib                   | 66.1 ms                                                      | 71.3 ms: 1.08x slower                                                   |
| scimark_sor                | 159 ms                                                       | 173 ms: 1.09x slower                                                    |
| tornado_http               | 128 ms                                                       | 140 ms: 1.09x slower                                                    |
| crypto_pyaes               | 82.0 ms                                                      | 89.5 ms: 1.09x slower                                                   |
| unpickle_pure_python       | 251 us                                                       | 275 us: 1.09x slower                                                    |
| raytrace                   | 297 ms                                                       | 325 ms: 1.10x slower                                                    |
| typing_runtime_protocols   | 193 us                                                       | 212 us: 1.10x slower                                                    |
| sqlglot_parse              | 1.42 ms                                                      | 1.57 ms: 1.10x slower                                                   |
| pyflate                    | 557 ms                                                       | 616 ms: 1.11x slower                                                    |
| sqlglot_normalize          | 129 ms                                                       | 143 ms: 1.11x slower                                                    |
| sqlglot_optimize           | 62.6 ms                                                      | 69.5 ms: 1.11x slower                                                   |
| pycparser                  | 1.22 sec                                                     | 1.36 sec: 1.11x slower                                                  |
| deepcopy                   | 448 us                                                       | 499 us: 1.11x slower                                                    |
| go                         | 161 ms                                                       | 179 ms: 1.12x slower                                                    |
| comprehensions             | 20.5 us                                                      | 22.9 us: 1.12x slower                                                   |
| pickle_pure_python         | 359 us                                                       | 405 us: 1.13x slower                                                    |
| docutils                   | 3.10 sec                                                     | 3.58 sec: 1.16x slower                                                  |
| sqlglot_transpile          | 1.71 ms                                                      | 1.98 ms: 1.16x slower                                                   |
| python_startup             | 13.0 ms                                                      | 15.2 ms: 1.17x slower                                                   |
| deepcopy_reduce            | 4.04 us                                                      | 4.74 us: 1.17x slower                                                   |
| 2to3                       | 305 ms                                                       | 360 ms: 1.18x slower                                                    |
| pprint_pformat             | 1.93 sec                                                     | 2.30 sec: 1.19x slower                                                  |
| django_template            | 42.3 ms                                                      | 50.4 ms: 1.19x slower                                                   |
| pprint_safe_repr           | 933 ms                                                       | 1.11 sec: 1.19x slower                                                  |
| bench_mp_pool              | 7.03 ms                                                      | 8.41 ms: 1.20x slower                                                   |
| sympy_expand               | 457 ms                                                       | 548 ms: 1.20x slower                                                    |
| deltablue                  | 3.88 ms                                                      | 4.69 ms: 1.21x slower                                                   |
| dulwich_log                | 58.5 ms                                                      | 70.8 ms: 1.21x slower                                                   |
| nqueens                    | 98.9 ms                                                      | 120 ms: 1.21x slower                                                    |
| sympy_str                  | 265 ms                                                       | 323 ms: 1.22x slower                                                    |
| python_startup_no_site     | 8.60 ms                                                      | 10.7 ms: 1.25x slower                                                   |
| pylint                     | 337 ms                                                       | 423 ms: 1.26x slower                                                    |
| hexiom                     | 7.08 ms                                                      | 8.96 ms: 1.27x slower                                                   |
| sympy_integrate            | 20.9 ms                                                      | 26.4 ms: 1.27x slower                                                   |
| genshi_text                | 27.4 ms                                                      | 34.8 ms: 1.27x slower                                                   |
| scimark_lu                 | 141 ms                                                       | 181 ms: 1.28x slower                                                    |
| chaos                      | 68.3 ms                                                      | 88.2 ms: 1.29x slower                                                   |
| sympy_sum                  | 144 ms                                                       | 187 ms: 1.30x slower                                                    |
| genshi_xml                 | 60.4 ms                                                      | 81.7 ms: 1.35x slower                                                   |
| regex_compile              | 128 ms                                                       | 174 ms: 1.36x slower                                                    |
| Geometric mean             | (ref)                                                        | 1.08x slower                                                            |

Benchmark hidden because not significant (15): unpickle_list, json, sqlite_synth, coroutines, pickle_list, pidigits, thrift, xml_etree_process, richards_super, pickle_dict, nbody, json_dumps, create_gc_cycles, gc_traversal, xml_etree_parse
Ignored benchmarks (4) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, bpe_tokeniser, gunicorn, mypy2

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: 1.09x