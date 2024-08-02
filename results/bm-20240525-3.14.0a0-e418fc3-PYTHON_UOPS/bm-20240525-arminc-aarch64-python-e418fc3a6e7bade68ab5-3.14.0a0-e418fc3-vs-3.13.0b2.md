# Results vs. 3.13.0b2

- fork: python
- ref: e418fc3a6e7bade68ab5
- machine: linux-aarch64
- commit hash: e418fc3
- commit date: 2024-05-25
- overall geometric mean: 1.16x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.09x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-arminc-aarch64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 305 ms                                                       | 359 ms: 1.18x slower                                                    |
| chameleon      | 8.95 ms                                                      | 10.2 ms: 1.14x slower                                                   |
| docutils       | 3.10 sec                                                     | 3.54 sec: 1.14x slower                                                  |
| html5lib       | 66.1 ms                                                      | 74.4 ms: 1.13x slower                                                   |
| tornado_http   | 128 ms                                                       | 138 ms: 1.08x slower                                                    |
| Geometric mean | (ref)                                                        | 1.13x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-arminc-aarch64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.27 sec                                                     | 1.24 sec: 1.03x faster                                                  |
| async_tree_none_tg         | 476 ms                                                       | 501 ms: 1.05x slower                                                    |
| async_tree_memoization_tg  | 604 ms                                                       | 640 ms: 1.06x slower                                                    |
| async_tree_io              | 1.22 sec                                                     | 1.30 sec: 1.06x slower                                                  |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 809 ms: 1.06x slower                                                    |
| async_tree_none            | 492 ms                                                       | 529 ms: 1.07x slower                                                    |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 850 ms: 1.07x slower                                                    |
| async_tree_memoization     | 645 ms                                                       | 697 ms: 1.08x slower                                                    |
| Geometric mean             | (ref)                                                        | 1.05x slower                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-arminc-aarch64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pidigits       | 234 ms                                                       | 237 ms: 1.01x slower                                                    |
| float          | 91.4 ms                                                      | 117 ms: 1.28x slower                                                    |
| nbody          | 114 ms                                                       | 151 ms: 1.32x slower                                                    |
| Geometric mean | (ref)                                                        | 1.19x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-arminc-aarch64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 4.98 ms                                                      | 4.93 ms: 1.01x faster                                                   |
| regex_compile  | 128 ms                                                       | 171 ms: 1.34x slower                                                    |
| Geometric mean | (ref)                                                        | 1.07x slower                                                            |

Benchmark hidden because not significant (2): regex_v8, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-arminc-aarch64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pickle               | 13.4 us                                                      | 13.8 us: 1.03x slower                                                   |
| json_dumps           | 13.1 ms                                                      | 13.7 ms: 1.04x slower                                                   |
| xml_etree_process    | 80.8 ms                                                      | 88.2 ms: 1.09x slower                                                   |
| xml_etree_iterparse  | 147 ms                                                       | 162 ms: 1.10x slower                                                    |
| xml_etree_generate   | 114 ms                                                       | 128 ms: 1.12x slower                                                    |
| tomli_loads          | 2.57 sec                                                     | 3.25 sec: 1.26x slower                                                  |
| pickle_pure_python   | 359 us                                                       | 467 us: 1.30x slower                                                    |
| unpickle_pure_python | 251 us                                                       | 367 us: 1.46x slower                                                    |
| Geometric mean       | (ref)                                                        | 1.09x slower                                                            |

Benchmark hidden because not significant (6): xml_etree_parse, unpickle, unpickle_list, pickle_dict, json_loads, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-arminc-aarch64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup | 13.0 ms                                                      | 12.8 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                        | 1.01x faster                                                            |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-arminc-aarch64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|-----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| django_template | 42.3 ms                                                      | 50.1 ms: 1.18x slower                                                   |
| genshi_xml      | 60.4 ms                                                      | 78.5 ms: 1.30x slower                                                   |
| mako            | 13.2 ms                                                      | 17.3 ms: 1.31x slower                                                   |
| genshi_text     | 27.4 ms                                                      | 37.6 ms: 1.37x slower                                                   |
| Geometric mean  | (ref)                                                        | 1.29x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-arminc-aarch64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.27 sec                                                     | 1.24 sec: 1.03x faster                                                  |
| pathlib                    | 22.8 ms                                                      | 22.3 ms: 1.02x faster                                                   |
| python_startup             | 13.0 ms                                                      | 12.8 ms: 1.02x faster                                                   |
| regex_effbot               | 4.98 ms                                                      | 4.93 ms: 1.01x faster                                                   |
| asyncio_websockets         | 657 ms                                                       | 662 ms: 1.01x slower                                                    |
| pidigits                   | 234 ms                                                       | 237 ms: 1.01x slower                                                    |
| asyncio_tcp_ssl            | 2.21 sec                                                     | 2.23 sec: 1.01x slower                                                  |
| gc_traversal               | 5.17 ms                                                      | 5.28 ms: 1.02x slower                                                   |
| logging_simple             | 7.21 us                                                      | 7.36 us: 1.02x slower                                                   |
| logging_format             | 7.82 us                                                      | 8.01 us: 1.02x slower                                                   |
| thrift                     | 962 us                                                       | 987 us: 1.03x slower                                                    |
| create_gc_cycles           | 2.33 ms                                                      | 2.39 ms: 1.03x slower                                                   |
| coverage                   | 98.4 ms                                                      | 101 ms: 1.03x slower                                                    |
| pickle                     | 13.4 us                                                      | 13.8 us: 1.03x slower                                                   |
| json                       | 5.64 ms                                                      | 5.83 ms: 1.03x slower                                                   |
| json_dumps                 | 13.1 ms                                                      | 13.7 ms: 1.04x slower                                                   |
| dask                       | 370 ms                                                       | 389 ms: 1.05x slower                                                    |
| async_tree_none_tg         | 476 ms                                                       | 501 ms: 1.05x slower                                                    |
| async_generators           | 488 ms                                                       | 515 ms: 1.06x slower                                                    |
| async_tree_memoization_tg  | 604 ms                                                       | 640 ms: 1.06x slower                                                    |
| async_tree_io              | 1.22 sec                                                     | 1.30 sec: 1.06x slower                                                  |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 809 ms: 1.06x slower                                                    |
| coroutines                 | 29.0 ms                                                      | 30.8 ms: 1.06x slower                                                   |
| async_tree_none            | 492 ms                                                       | 529 ms: 1.07x slower                                                    |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 850 ms: 1.07x slower                                                    |
| telco                      | 10.0 ms                                                      | 10.8 ms: 1.08x slower                                                   |
| mdp                        | 3.33 sec                                                     | 3.60 sec: 1.08x slower                                                  |
| tornado_http               | 128 ms                                                       | 138 ms: 1.08x slower                                                    |
| async_tree_memoization     | 645 ms                                                       | 697 ms: 1.08x slower                                                    |
| xml_etree_process          | 80.8 ms                                                      | 88.2 ms: 1.09x slower                                                   |
| generators                 | 37.1 ms                                                      | 40.7 ms: 1.10x slower                                                   |
| xml_etree_iterparse        | 147 ms                                                       | 162 ms: 1.10x slower                                                    |
| bench_thread_pool          | 1.26 ms                                                      | 1.39 ms: 1.11x slower                                                   |
| flaskblogging              | 4.70 ms                                                      | 5.22 ms: 1.11x slower                                                   |
| xml_etree_generate         | 114 ms                                                       | 128 ms: 1.12x slower                                                    |
| html5lib                   | 66.1 ms                                                      | 74.4 ms: 1.13x slower                                                   |
| dulwich_log                | 58.5 ms                                                      | 66.1 ms: 1.13x slower                                                   |
| docutils                   | 3.10 sec                                                     | 3.54 sec: 1.14x slower                                                  |
| pycparser                  | 1.22 sec                                                     | 1.40 sec: 1.14x slower                                                  |
| chameleon                  | 8.95 ms                                                      | 10.2 ms: 1.14x slower                                                   |
| sqlglot_normalize          | 129 ms                                                       | 149 ms: 1.16x slower                                                    |
| sympy_expand               | 457 ms                                                       | 533 ms: 1.16x slower                                                    |
| sqlglot_optimize           | 62.6 ms                                                      | 72.9 ms: 1.16x slower                                                   |
| typing_runtime_protocols   | 193 us                                                       | 226 us: 1.17x slower                                                    |
| raytrace                   | 297 ms                                                       | 348 ms: 1.17x slower                                                    |
| 2to3                       | 305 ms                                                       | 359 ms: 1.18x slower                                                    |
| django_template            | 42.3 ms                                                      | 50.1 ms: 1.18x slower                                                   |
| meteor_contest             | 113 ms                                                       | 135 ms: 1.19x slower                                                    |
| pylint                     | 337 ms                                                       | 401 ms: 1.19x slower                                                    |
| richards_super             | 62.3 ms                                                      | 74.7 ms: 1.20x slower                                                   |
| deepcopy_reduce            | 4.04 us                                                      | 4.88 us: 1.21x slower                                                   |
| sympy_str                  | 265 ms                                                       | 321 ms: 1.21x slower                                                    |
| richards                   | 55.9 ms                                                      | 68.2 ms: 1.22x slower                                                   |
| sympy_sum                  | 144 ms                                                       | 176 ms: 1.22x slower                                                    |
| bench_mp_pool              | 7.03 ms                                                      | 8.62 ms: 1.23x slower                                                   |
| deepcopy                   | 448 us                                                       | 553 us: 1.23x slower                                                    |
| scimark_fft                | 445 ms                                                       | 558 ms: 1.25x slower                                                    |
| go                         | 161 ms                                                       | 202 ms: 1.26x slower                                                    |
| tomli_loads                | 2.57 sec                                                     | 3.25 sec: 1.26x slower                                                  |
| scimark_sor                | 159 ms                                                       | 202 ms: 1.27x slower                                                    |
| sqlglot_parse              | 1.42 ms                                                      | 1.81 ms: 1.27x slower                                                   |
| scimark_sparse_mat_mult    | 6.55 ms                                                      | 8.35 ms: 1.27x slower                                                   |
| float                      | 91.4 ms                                                      | 117 ms: 1.28x slower                                                    |
| sympy_integrate            | 20.9 ms                                                      | 26.6 ms: 1.28x slower                                                   |
| pprint_pformat             | 1.93 sec                                                     | 2.47 sec: 1.28x slower                                                  |
| crypto_pyaes               | 82.0 ms                                                      | 106 ms: 1.29x slower                                                    |
| pprint_safe_repr           | 933 ms                                                       | 1.21 sec: 1.29x slower                                                  |
| genshi_xml                 | 60.4 ms                                                      | 78.5 ms: 1.30x slower                                                   |
| pickle_pure_python         | 359 us                                                       | 467 us: 1.30x slower                                                    |
| chaos                      | 68.3 ms                                                      | 89.4 ms: 1.31x slower                                                   |
| mako                       | 13.2 ms                                                      | 17.3 ms: 1.31x slower                                                   |
| sqlglot_transpile          | 1.71 ms                                                      | 2.26 ms: 1.32x slower                                                   |
| nbody                      | 114 ms                                                       | 151 ms: 1.32x slower                                                    |
| fannkuch                   | 451 ms                                                       | 598 ms: 1.32x slower                                                    |
| regex_compile              | 128 ms                                                       | 171 ms: 1.34x slower                                                    |
| pyflate                    | 557 ms                                                       | 760 ms: 1.37x slower                                                    |
| deltablue                  | 3.88 ms                                                      | 5.31 ms: 1.37x slower                                                   |
| genshi_text                | 27.4 ms                                                      | 37.6 ms: 1.37x slower                                                   |
| nqueens                    | 98.9 ms                                                      | 136 ms: 1.37x slower                                                    |
| spectral_norm              | 141 ms                                                       | 194 ms: 1.37x slower                                                    |
| scimark_monte_carlo        | 82.3 ms                                                      | 119 ms: 1.44x slower                                                    |
| unpickle_pure_python       | 251 us                                                       | 367 us: 1.46x slower                                                    |
| logging_silent             | 133 ns                                                       | 197 ns: 1.48x slower                                                    |
| scimark_lu                 | 141 ms                                                       | 211 ms: 1.49x slower                                                    |
| deepcopy_memo              | 50.8 us                                                      | 75.9 us: 1.49x slower                                                   |
| comprehensions             | 20.5 us                                                      | 31.8 us: 1.55x slower                                                   |
| hexiom                     | 7.08 ms                                                      | 11.3 ms: 1.60x slower                                                   |
| Geometric mean             | (ref)                                                        | 1.16x slower                                                            |

Benchmark hidden because not significant (11): regex_v8, regex_dna, xml_etree_parse, python_startup_no_site, unpickle, unpickle_list, pickle_dict, json_loads, asyncio_tcp, sqlite_synth, pickle_list
Ignored benchmarks (4) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, bpe_tokeniser, gunicorn, mypy2

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.11x
- 95% likely to have a slowdown of 1.10x
- 99% likely to have a slowdown of 1.09x

# Memory
- memory change: 1.01x