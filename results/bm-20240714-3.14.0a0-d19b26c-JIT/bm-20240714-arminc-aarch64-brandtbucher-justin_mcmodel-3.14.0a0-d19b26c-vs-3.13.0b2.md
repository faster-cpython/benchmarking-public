# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: justin_mcmodel
- machine: linux-aarch64
- commit hash: d19b26c
- commit date: 2024-07-14
- overall geometric mean: 1.07x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240714-arminc-aarch64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 305 ms                                                       | 361 ms: 1.18x slower                                                    |
| docutils       | 3.10 sec                                                     | 3.55 sec: 1.15x slower                                                  |
| html5lib       | 66.1 ms                                                      | 71.2 ms: 1.08x slower                                                   |
| tornado_http   | 128 ms                                                       | 144 ms: 1.13x slower                                                    |
| Geometric mean | (ref)                                                        | 1.13x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240714-arminc-aarch64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none_tg         | 476 ms                                                       | 408 ms: 1.17x faster                                                    |
| async_tree_io_tg           | 1.27 sec                                                     | 1.11 sec: 1.15x faster                                                  |
| async_tree_io              | 1.22 sec                                                     | 1.07 sec: 1.15x faster                                                  |
| async_tree_memoization_tg  | 604 ms                                                       | 541 ms: 1.12x faster                                                    |
| async_tree_none            | 492 ms                                                       | 447 ms: 1.10x faster                                                    |
| async_tree_memoization     | 645 ms                                                       | 587 ms: 1.10x faster                                                    |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 737 ms: 1.07x faster                                                    |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 722 ms: 1.06x faster                                                    |
| Geometric mean             | (ref)                                                        | 1.11x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240714-arminc-aarch64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 91.4 ms                                                      | 89.2 ms: 1.02x faster                                                   |
| nbody          | 114 ms                                                       | 122 ms: 1.07x slower                                                    |
| Geometric mean | (ref)                                                        | 1.01x slower                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240714-arminc-aarch64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 31.1 ms                                                      | 30.3 ms: 1.03x faster                                                   |
| regex_compile  | 128 ms                                                       | 175 ms: 1.37x slower                                                    |
| Geometric mean | (ref)                                                        | 1.07x slower                                                            |

Benchmark hidden because not significant (2): regex_effbot, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240714-arminc-aarch64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_generate   | 114 ms                                                       | 111 ms: 1.02x faster                                                    |
| xml_etree_iterparse  | 147 ms                                                       | 148 ms: 1.01x slower                                                    |
| json_dumps           | 13.1 ms                                                      | 13.5 ms: 1.03x slower                                                   |
| json_loads           | 32.1 us                                                      | 33.2 us: 1.04x slower                                                   |
| tomli_loads          | 2.57 sec                                                     | 2.67 sec: 1.04x slower                                                  |
| unpickle_pure_python | 251 us                                                       | 279 us: 1.11x slower                                                    |
| pickle_pure_python   | 359 us                                                       | 411 us: 1.15x slower                                                    |
| Geometric mean       | (ref)                                                        | 1.03x slower                                                            |

Benchmark hidden because not significant (2): xml_etree_parse, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240714-arminc-aarch64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 13.0 ms                                                      | 13.1 ms: 1.01x slower                                                   |
| python_startup_no_site | 8.60 ms                                                      | 8.90 ms: 1.03x slower                                                   |
| Geometric mean         | (ref)                                                        | 1.02x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240714-arminc-aarch64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|-----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 13.2 ms                                                      | 13.4 ms: 1.02x slower                                                   |
| django_template | 42.3 ms                                                      | 50.3 ms: 1.19x slower                                                   |
| genshi_text     | 27.4 ms                                                      | 34.6 ms: 1.26x slower                                                   |
| genshi_xml      | 60.4 ms                                                      | 84.9 ms: 1.41x slower                                                   |
| Geometric mean  | (ref)                                                        | 1.21x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240714-arminc-aarch64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy_memo              | 50.8 us                                                      | 38.8 us: 1.31x faster                                                   |
| deepcopy                   | 448 us                                                       | 382 us: 1.17x faster                                                    |
| async_tree_none_tg         | 476 ms                                                       | 408 ms: 1.17x faster                                                    |
| async_tree_io_tg           | 1.27 sec                                                     | 1.11 sec: 1.15x faster                                                  |
| async_tree_io              | 1.22 sec                                                     | 1.07 sec: 1.15x faster                                                  |
| async_tree_memoization_tg  | 604 ms                                                       | 541 ms: 1.12x faster                                                    |
| async_tree_none            | 492 ms                                                       | 447 ms: 1.10x faster                                                    |
| async_tree_memoization     | 645 ms                                                       | 587 ms: 1.10x faster                                                    |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 737 ms: 1.07x faster                                                    |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 722 ms: 1.06x faster                                                    |
| gc_traversal               | 5.17 ms                                                      | 5.04 ms: 1.03x faster                                                   |
| regex_v8                   | 31.1 ms                                                      | 30.3 ms: 1.03x faster                                                   |
| float                      | 91.4 ms                                                      | 89.2 ms: 1.02x faster                                                   |
| xml_etree_generate         | 114 ms                                                       | 111 ms: 1.02x faster                                                    |
| richards                   | 55.9 ms                                                      | 54.8 ms: 1.02x faster                                                   |
| asyncio_websockets         | 657 ms                                                       | 662 ms: 1.01x slower                                                    |
| python_startup             | 13.0 ms                                                      | 13.1 ms: 1.01x slower                                                   |
| xml_etree_iterparse        | 147 ms                                                       | 148 ms: 1.01x slower                                                    |
| logging_format             | 7.82 us                                                      | 7.90 us: 1.01x slower                                                   |
| coverage                   | 98.4 ms                                                      | 99.7 ms: 1.01x slower                                                   |
| thrift                     | 962 us                                                       | 978 us: 1.02x slower                                                    |
| mako                       | 13.2 ms                                                      | 13.4 ms: 1.02x slower                                                   |
| coroutines                 | 29.0 ms                                                      | 29.6 ms: 1.02x slower                                                   |
| asyncio_tcp_ssl            | 2.21 sec                                                     | 2.26 sec: 1.02x slower                                                  |
| json_dumps                 | 13.1 ms                                                      | 13.5 ms: 1.03x slower                                                   |
| json                       | 5.64 ms                                                      | 5.81 ms: 1.03x slower                                                   |
| mdp                        | 3.33 sec                                                     | 3.43 sec: 1.03x slower                                                  |
| generators                 | 37.1 ms                                                      | 38.3 ms: 1.03x slower                                                   |
| bpe_tokeniser              | 5.83 sec                                                     | 6.02 sec: 1.03x slower                                                  |
| python_startup_no_site     | 8.60 ms                                                      | 8.90 ms: 1.03x slower                                                   |
| json_loads                 | 32.1 us                                                      | 33.2 us: 1.04x slower                                                   |
| tomli_loads                | 2.57 sec                                                     | 2.67 sec: 1.04x slower                                                  |
| telco                      | 10.0 ms                                                      | 10.4 ms: 1.04x slower                                                   |
| meteor_contest             | 113 ms                                                       | 118 ms: 1.04x slower                                                    |
| deepcopy_reduce            | 4.04 us                                                      | 4.21 us: 1.04x slower                                                   |
| async_generators           | 488 ms                                                       | 511 ms: 1.05x slower                                                    |
| fannkuch                   | 451 ms                                                       | 474 ms: 1.05x slower                                                    |
| dask                       | 370 ms                                                       | 390 ms: 1.05x slower                                                    |
| spectral_norm              | 141 ms                                                       | 149 ms: 1.06x slower                                                    |
| scimark_fft                | 445 ms                                                       | 472 ms: 1.06x slower                                                    |
| logging_silent             | 133 ns                                                       | 142 ns: 1.07x slower                                                    |
| nbody                      | 114 ms                                                       | 122 ms: 1.07x slower                                                    |
| scimark_sparse_mat_mult    | 6.55 ms                                                      | 7.00 ms: 1.07x slower                                                   |
| asyncio_tcp                | 584 ms                                                       | 625 ms: 1.07x slower                                                    |
| bench_thread_pool          | 1.26 ms                                                      | 1.35 ms: 1.07x slower                                                   |
| typing_runtime_protocols   | 193 us                                                       | 208 us: 1.07x slower                                                    |
| html5lib                   | 66.1 ms                                                      | 71.2 ms: 1.08x slower                                                   |
| sqlglot_optimize           | 62.6 ms                                                      | 68.5 ms: 1.09x slower                                                   |
| raytrace                   | 297 ms                                                       | 325 ms: 1.09x slower                                                    |
| crypto_pyaes               | 82.0 ms                                                      | 90.0 ms: 1.10x slower                                                   |
| sqlglot_normalize          | 129 ms                                                       | 143 ms: 1.11x slower                                                    |
| scimark_sor                | 159 ms                                                       | 177 ms: 1.11x slower                                                    |
| unpickle_pure_python       | 251 us                                                       | 279 us: 1.11x slower                                                    |
| scimark_monte_carlo        | 82.3 ms                                                      | 91.5 ms: 1.11x slower                                                   |
| go                         | 161 ms                                                       | 179 ms: 1.11x slower                                                    |
| pycparser                  | 1.22 sec                                                     | 1.36 sec: 1.11x slower                                                  |
| pyflate                    | 557 ms                                                       | 621 ms: 1.12x slower                                                    |
| tornado_http               | 128 ms                                                       | 144 ms: 1.13x slower                                                    |
| sqlglot_parse              | 1.42 ms                                                      | 1.61 ms: 1.13x slower                                                   |
| docutils                   | 3.10 sec                                                     | 3.55 sec: 1.15x slower                                                  |
| pickle_pure_python         | 359 us                                                       | 411 us: 1.15x slower                                                    |
| deltablue                  | 3.88 ms                                                      | 4.47 ms: 1.15x slower                                                   |
| comprehensions             | 20.5 us                                                      | 23.7 us: 1.15x slower                                                   |
| 2to3                       | 305 ms                                                       | 361 ms: 1.18x slower                                                    |
| sympy_expand               | 457 ms                                                       | 542 ms: 1.19x slower                                                    |
| nqueens                    | 98.9 ms                                                      | 117 ms: 1.19x slower                                                    |
| django_template            | 42.3 ms                                                      | 50.3 ms: 1.19x slower                                                   |
| sqlglot_transpile          | 1.71 ms                                                      | 2.04 ms: 1.19x slower                                                   |
| pylint                     | 337 ms                                                       | 408 ms: 1.21x slower                                                    |
| sympy_str                  | 265 ms                                                       | 323 ms: 1.22x slower                                                    |
| dulwich_log                | 58.5 ms                                                      | 72.6 ms: 1.24x slower                                                   |
| hexiom                     | 7.08 ms                                                      | 8.81 ms: 1.24x slower                                                   |
| pprint_safe_repr           | 933 ms                                                       | 1.16 sec: 1.25x slower                                                  |
| pprint_pformat             | 1.93 sec                                                     | 2.42 sec: 1.25x slower                                                  |
| sympy_integrate            | 20.9 ms                                                      | 26.3 ms: 1.26x slower                                                   |
| genshi_text                | 27.4 ms                                                      | 34.6 ms: 1.26x slower                                                   |
| sympy_sum                  | 144 ms                                                       | 183 ms: 1.27x slower                                                    |
| scimark_lu                 | 141 ms                                                       | 184 ms: 1.30x slower                                                    |
| regex_compile              | 128 ms                                                       | 175 ms: 1.37x slower                                                    |
| chaos                      | 68.3 ms                                                      | 93.3 ms: 1.37x slower                                                   |
| genshi_xml                 | 60.4 ms                                                      | 84.9 ms: 1.41x slower                                                   |
| bench_mp_pool              | 7.03 ms                                                      | 13.2 ms: 1.88x slower                                                   |
| Geometric mean             | (ref)                                                        | 1.07x slower                                                            |

Benchmark hidden because not significant (9): xml_etree_parse, xml_etree_process, pathlib, regex_effbot, richards_super, regex_dna, pidigits, logging_simple, create_gc_cycles
Ignored benchmarks (11) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: 1.08x