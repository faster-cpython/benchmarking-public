# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: main
- machine: linux-aarch64
- commit hash: e256a75
- commit date: 2024-09-24
- overall geometric mean: 1.09x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240924-arminc-aarch64-brandtbucher-main-3.14.0a0-e256a75 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------:|
| 2to3           | 305 ms                                                       | 380 ms: 1.25x slower                                          |
| docutils       | 3.10 sec                                                     | 4.02 sec: 1.30x slower                                        |
| html5lib       | 66.1 ms                                                      | 72.5 ms: 1.10x slower                                         |
| tornado_http   | 128 ms                                                       | 150 ms: 1.18x slower                                          |
| Geometric mean | (ref)                                                        | 1.20x slower                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240924-arminc-aarch64-brandtbucher-main-3.14.0a0-e256a75 |
|----------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------:|
| async_tree_none            | 492 ms                                                       | 445 ms: 1.11x faster                                          |
| async_tree_none_tg         | 476 ms                                                       | 432 ms: 1.10x faster                                          |
| async_tree_memoization     | 645 ms                                                       | 588 ms: 1.10x faster                                          |
| async_tree_io              | 1.22 sec                                                     | 1.14 sec: 1.07x faster                                        |
| async_tree_io_tg           | 1.27 sec                                                     | 1.19 sec: 1.07x faster                                        |
| async_tree_memoization_tg  | 604 ms                                                       | 568 ms: 1.07x faster                                          |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 754 ms: 1.05x faster                                          |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 737 ms: 1.04x faster                                          |
| Geometric mean             | (ref)                                                        | 1.07x faster                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240924-arminc-aarch64-brandtbucher-main-3.14.0a0-e256a75 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------:|
| float          | 91.4 ms                                                      | 88.5 ms: 1.03x faster                                         |
| Geometric mean | (ref)                                                        | 1.01x faster                                                  |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240924-arminc-aarch64-brandtbucher-main-3.14.0a0-e256a75 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------:|
| regex_v8       | 31.1 ms                                                      | 30.5 ms: 1.02x faster                                         |
| regex_dna      | 259 ms                                                       | 255 ms: 1.01x faster                                          |
| regex_compile  | 128 ms                                                       | 197 ms: 1.54x slower                                          |
| Geometric mean | (ref)                                                        | 1.10x slower                                                  |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240924-arminc-aarch64-brandtbucher-main-3.14.0a0-e256a75 |
|----------------------|:------------------------------------------------------------:|:-------------------------------------------------------------:|
| xml_etree_generate   | 114 ms                                                       | 110 ms: 1.03x faster                                          |
| unpickle_list        | 6.52 us                                                      | 6.37 us: 1.02x faster                                         |
| unpickle             | 19.8 us                                                      | 19.5 us: 1.01x faster                                         |
| pickle_list          | 5.27 us                                                      | 5.22 us: 1.01x faster                                         |
| xml_etree_iterparse  | 147 ms                                                       | 148 ms: 1.01x slower                                          |
| pickle_dict          | 37.6 us                                                      | 38.2 us: 1.01x slower                                         |
| tomli_loads          | 2.57 sec                                                     | 2.63 sec: 1.02x slower                                        |
| json_dumps           | 13.1 ms                                                      | 13.4 ms: 1.02x slower                                         |
| pickle               | 13.4 us                                                      | 13.8 us: 1.03x slower                                         |
| unpickle_pure_python | 251 us                                                       | 266 us: 1.06x slower                                          |
| pickle_pure_python   | 359 us                                                       | 399 us: 1.11x slower                                          |
| Geometric mean       | (ref)                                                        | 1.01x slower                                                  |

Benchmark hidden because not significant (3): xml_etree_parse, json_loads, xml_etree_process

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240924-arminc-aarch64-brandtbucher-main-3.14.0a0-e256a75 |
|-----------------|:------------------------------------------------------------:|:-------------------------------------------------------------:|
| django_template | 42.3 ms                                                      | 51.0 ms: 1.21x slower                                         |
| genshi_text     | 27.4 ms                                                      | 34.6 ms: 1.26x slower                                         |
| genshi_xml      | 60.4 ms                                                      | 80.5 ms: 1.33x slower                                         |
| Geometric mean  | (ref)                                                        | 1.19x slower                                                  |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240924-arminc-aarch64-brandtbucher-main-3.14.0a0-e256a75 |
|----------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------:|
| deepcopy_memo              | 50.8 us                                                      | 37.5 us: 1.35x faster                                         |
| deepcopy                   | 448 us                                                       | 398 us: 1.13x faster                                          |
| async_tree_none            | 492 ms                                                       | 445 ms: 1.11x faster                                          |
| async_tree_none_tg         | 476 ms                                                       | 432 ms: 1.10x faster                                          |
| async_tree_memoization     | 645 ms                                                       | 588 ms: 1.10x faster                                          |
| async_tree_io              | 1.22 sec                                                     | 1.14 sec: 1.07x faster                                        |
| async_tree_io_tg           | 1.27 sec                                                     | 1.19 sec: 1.07x faster                                        |
| async_tree_memoization_tg  | 604 ms                                                       | 568 ms: 1.07x faster                                          |
| scimark_sor                | 159 ms                                                       | 151 ms: 1.06x faster                                          |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 754 ms: 1.05x faster                                          |
| pathlib                    | 22.8 ms                                                      | 21.8 ms: 1.04x faster                                         |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 737 ms: 1.04x faster                                          |
| xml_etree_generate         | 114 ms                                                       | 110 ms: 1.03x faster                                          |
| deepcopy_reduce            | 4.04 us                                                      | 3.90 us: 1.03x faster                                         |
| float                      | 91.4 ms                                                      | 88.5 ms: 1.03x faster                                         |
| unpickle_list              | 6.52 us                                                      | 6.37 us: 1.02x faster                                         |
| coroutines                 | 29.0 ms                                                      | 28.4 ms: 1.02x faster                                         |
| regex_v8                   | 31.1 ms                                                      | 30.5 ms: 1.02x faster                                         |
| unpickle                   | 19.8 us                                                      | 19.5 us: 1.01x faster                                         |
| regex_dna                  | 259 ms                                                       | 255 ms: 1.01x faster                                          |
| pickle_list                | 5.27 us                                                      | 5.22 us: 1.01x faster                                         |
| xml_etree_iterparse        | 147 ms                                                       | 148 ms: 1.01x slower                                          |
| asyncio_websockets         | 657 ms                                                       | 663 ms: 1.01x slower                                          |
| pickle_dict                | 37.6 us                                                      | 38.2 us: 1.01x slower                                         |
| bpe_tokeniser              | 5.83 sec                                                     | 5.91 sec: 1.01x slower                                        |
| tomli_loads                | 2.57 sec                                                     | 2.63 sec: 1.02x slower                                        |
| logging_silent             | 133 ns                                                       | 136 ns: 1.02x slower                                          |
| json_dumps                 | 13.1 ms                                                      | 13.4 ms: 1.02x slower                                         |
| scimark_fft                | 445 ms                                                       | 459 ms: 1.03x slower                                          |
| pickle                     | 13.4 us                                                      | 13.8 us: 1.03x slower                                         |
| spectral_norm              | 141 ms                                                       | 146 ms: 1.04x slower                                          |
| async_generators           | 488 ms                                                       | 507 ms: 1.04x slower                                          |
| logging_simple             | 7.21 us                                                      | 7.49 us: 1.04x slower                                         |
| logging_format             | 7.82 us                                                      | 8.16 us: 1.04x slower                                         |
| coverage                   | 98.4 ms                                                      | 103 ms: 1.04x slower                                          |
| bench_mp_pool              | 7.03 ms                                                      | 7.35 ms: 1.05x slower                                         |
| scimark_sparse_mat_mult    | 6.55 ms                                                      | 6.86 ms: 1.05x slower                                         |
| mdp                        | 3.33 sec                                                     | 3.49 sec: 1.05x slower                                        |
| scimark_lu                 | 141 ms                                                       | 149 ms: 1.06x slower                                          |
| unpickle_pure_python       | 251 us                                                       | 266 us: 1.06x slower                                          |
| asyncio_tcp                | 584 ms                                                       | 623 ms: 1.07x slower                                          |
| telco                      | 10.0 ms                                                      | 10.7 ms: 1.07x slower                                         |
| bench_thread_pool          | 1.26 ms                                                      | 1.36 ms: 1.08x slower                                         |
| meteor_contest             | 113 ms                                                       | 124 ms: 1.09x slower                                          |
| crypto_pyaes               | 82.0 ms                                                      | 89.9 ms: 1.10x slower                                         |
| html5lib                   | 66.1 ms                                                      | 72.5 ms: 1.10x slower                                         |
| typing_runtime_protocols   | 193 us                                                       | 215 us: 1.11x slower                                          |
| pickle_pure_python         | 359 us                                                       | 399 us: 1.11x slower                                          |
| deltablue                  | 3.88 ms                                                      | 4.36 ms: 1.12x slower                                         |
| pyflate                    | 557 ms                                                       | 628 ms: 1.13x slower                                          |
| fannkuch                   | 451 ms                                                       | 510 ms: 1.13x slower                                          |
| scimark_monte_carlo        | 82.3 ms                                                      | 93.0 ms: 1.13x slower                                         |
| go                         | 161 ms                                                       | 186 ms: 1.16x slower                                          |
| raytrace                   | 297 ms                                                       | 347 ms: 1.17x slower                                          |
| tornado_http               | 128 ms                                                       | 150 ms: 1.18x slower                                          |
| comprehensions             | 20.5 us                                                      | 24.3 us: 1.19x slower                                         |
| sqlglot_normalize          | 129 ms                                                       | 154 ms: 1.19x slower                                          |
| richards                   | 55.9 ms                                                      | 66.6 ms: 1.19x slower                                         |
| django_template            | 42.3 ms                                                      | 51.0 ms: 1.21x slower                                         |
| richards_super             | 62.3 ms                                                      | 76.3 ms: 1.23x slower                                         |
| sqlglot_parse              | 1.42 ms                                                      | 1.75 ms: 1.23x slower                                         |
| pycparser                  | 1.22 sec                                                     | 1.51 sec: 1.24x slower                                        |
| 2to3                       | 305 ms                                                       | 380 ms: 1.25x slower                                          |
| sqlglot_optimize           | 62.6 ms                                                      | 79.1 ms: 1.26x slower                                         |
| genshi_text                | 27.4 ms                                                      | 34.6 ms: 1.26x slower                                         |
| nqueens                    | 98.9 ms                                                      | 127 ms: 1.28x slower                                          |
| sqlglot_transpile          | 1.71 ms                                                      | 2.21 ms: 1.29x slower                                         |
| docutils                   | 3.10 sec                                                     | 4.02 sec: 1.30x slower                                        |
| chaos                      | 68.3 ms                                                      | 90.8 ms: 1.33x slower                                         |
| genshi_xml                 | 60.4 ms                                                      | 80.5 ms: 1.33x slower                                         |
| sympy_expand               | 457 ms                                                       | 613 ms: 1.34x slower                                          |
| pprint_safe_repr           | 933 ms                                                       | 1.26 sec: 1.35x slower                                        |
| pprint_pformat             | 1.93 sec                                                     | 2.61 sec: 1.35x slower                                        |
| sympy_integrate            | 20.9 ms                                                      | 28.4 ms: 1.36x slower                                         |
| sympy_str                  | 265 ms                                                       | 366 ms: 1.38x slower                                          |
| dulwich_log                | 58.5 ms                                                      | 81.1 ms: 1.39x slower                                         |
| pylint                     | 337 ms                                                       | 476 ms: 1.41x slower                                          |
| hexiom                     | 7.08 ms                                                      | 10.2 ms: 1.44x slower                                         |
| sympy_sum                  | 144 ms                                                       | 209 ms: 1.46x slower                                          |
| generators                 | 37.1 ms                                                      | 56.5 ms: 1.52x slower                                         |
| regex_compile              | 128 ms                                                       | 197 ms: 1.54x slower                                          |
| Geometric mean             | (ref)                                                        | 1.09x slower                                                  |

Benchmark hidden because not significant (15): xml_etree_parse, json_loads, gc_traversal, thrift, mako, sqlite_synth, regex_effbot, pidigits, create_gc_cycles, nbody, xml_etree_process, asyncio_tcp_ssl, json, python_startup, python_startup_no_site
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20240924-3.14.0a0-e256a75-JIT/bm-20240924-arminc-aarch64-brandtbucher-main-3.14.0a0-e256a75.json: unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 1.09x