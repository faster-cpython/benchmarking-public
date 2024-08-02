# Results vs. 3.13.0b2

- fork: python
- ref: 5b941e57c71d7d0ab983
- machine: linux-aarch64
- commit hash: 5b941e5
- commit date: 2024-05-11
- overall geometric mean: 1.17x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240511-arminc-aarch64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 305 ms                                                       | 354 ms: 1.16x slower                                                    |
| chameleon      | 8.95 ms                                                      | 9.96 ms: 1.11x slower                                                   |
| docutils       | 3.10 sec                                                     | 3.54 sec: 1.14x slower                                                  |
| html5lib       | 66.1 ms                                                      | 74.8 ms: 1.13x slower                                                   |
| tornado_http   | 128 ms                                                       | 136 ms: 1.06x slower                                                    |
| Geometric mean | (ref)                                                        | 1.12x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240511-arminc-aarch64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_cpu_io_mixed    | 791 ms                                                       | 816 ms: 1.03x slower                                                    |
| async_tree_memoization     | 645 ms                                                       | 670 ms: 1.04x slower                                                    |
| async_tree_memoization_tg  | 604 ms                                                       | 629 ms: 1.04x slower                                                    |
| async_tree_none            | 492 ms                                                       | 517 ms: 1.05x slower                                                    |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 802 ms: 1.05x slower                                                    |
| Geometric mean             | (ref)                                                        | 1.03x slower                                                            |

Benchmark hidden because not significant (3): async_tree_io_tg, async_tree_none_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240511-arminc-aarch64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pidigits       | 234 ms                                                       | 237 ms: 1.01x slower                                                    |
| nbody          | 114 ms                                                       | 138 ms: 1.21x slower                                                    |
| float          | 91.4 ms                                                      | 114 ms: 1.24x slower                                                    |
| Geometric mean | (ref)                                                        | 1.15x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240511-arminc-aarch64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 128 ms                                                       | 167 ms: 1.30x slower                                                    |
| Geometric mean | (ref)                                                        | 1.07x slower                                                            |

Benchmark hidden because not significant (3): regex_effbot, regex_v8, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240511-arminc-aarch64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pickle_list          | 5.27 us                                                      | 5.23 us: 1.01x faster                                                   |
| unpickle             | 19.8 us                                                      | 19.6 us: 1.01x faster                                                   |
| json_loads           | 32.1 us                                                      | 32.6 us: 1.01x slower                                                   |
| pickle               | 13.4 us                                                      | 13.9 us: 1.04x slower                                                   |
| json_dumps           | 13.1 ms                                                      | 14.0 ms: 1.07x slower                                                   |
| xml_etree_process    | 80.8 ms                                                      | 88.5 ms: 1.10x slower                                                   |
| xml_etree_generate   | 114 ms                                                       | 125 ms: 1.10x slower                                                    |
| xml_etree_iterparse  | 147 ms                                                       | 162 ms: 1.11x slower                                                    |
| tomli_loads          | 2.57 sec                                                     | 3.08 sec: 1.20x slower                                                  |
| pickle_pure_python   | 359 us                                                       | 449 us: 1.25x slower                                                    |
| unpickle_pure_python | 251 us                                                       | 349 us: 1.39x slower                                                    |
| Geometric mean       | (ref)                                                        | 1.09x slower                                                            |

Benchmark hidden because not significant (3): unpickle_list, pickle_dict, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240511-arminc-aarch64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup | 13.0 ms                                                      | 12.5 ms: 1.03x faster                                                   |
| Geometric mean | (ref)                                                        | 1.03x faster                                                            |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240511-arminc-aarch64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|-----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| django_template | 42.3 ms                                                      | 49.9 ms: 1.18x slower                                                   |
| mako            | 13.2 ms                                                      | 16.5 ms: 1.25x slower                                                   |
| genshi_xml      | 60.4 ms                                                      | 77.7 ms: 1.29x slower                                                   |
| genshi_text     | 27.4 ms                                                      | 36.6 ms: 1.34x slower                                                   |
| Geometric mean  | (ref)                                                        | 1.26x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240511-arminc-aarch64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup             | 13.0 ms                                                      | 12.5 ms: 1.03x faster                                                   |
| pickle_list                | 5.27 us                                                      | 5.23 us: 1.01x faster                                                   |
| unpickle                   | 19.8 us                                                      | 19.6 us: 1.01x faster                                                   |
| asyncio_websockets         | 657 ms                                                       | 662 ms: 1.01x slower                                                    |
| pidigits                   | 234 ms                                                       | 237 ms: 1.01x slower                                                    |
| asyncio_tcp_ssl            | 2.21 sec                                                     | 2.24 sec: 1.01x slower                                                  |
| json_loads                 | 32.1 us                                                      | 32.6 us: 1.01x slower                                                   |
| sqlite_synth               | 3.90 us                                                      | 3.96 us: 1.02x slower                                                   |
| thrift                     | 962 us                                                       | 985 us: 1.02x slower                                                    |
| json                       | 5.64 ms                                                      | 5.79 ms: 1.03x slower                                                   |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 816 ms: 1.03x slower                                                    |
| logging_format             | 7.82 us                                                      | 8.09 us: 1.03x slower                                                   |
| pickle                     | 13.4 us                                                      | 13.9 us: 1.04x slower                                                   |
| async_tree_memoization     | 645 ms                                                       | 670 ms: 1.04x slower                                                    |
| async_tree_memoization_tg  | 604 ms                                                       | 629 ms: 1.04x slower                                                    |
| create_gc_cycles           | 2.33 ms                                                      | 2.43 ms: 1.04x slower                                                   |
| dask                       | 370 ms                                                       | 387 ms: 1.04x slower                                                    |
| coroutines                 | 29.0 ms                                                      | 30.4 ms: 1.05x slower                                                   |
| async_tree_none            | 492 ms                                                       | 517 ms: 1.05x slower                                                    |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 802 ms: 1.05x slower                                                    |
| tornado_http               | 128 ms                                                       | 136 ms: 1.06x slower                                                    |
| json_dumps                 | 13.1 ms                                                      | 14.0 ms: 1.07x slower                                                   |
| pathlib                    | 22.8 ms                                                      | 24.3 ms: 1.07x slower                                                   |
| generators                 | 37.1 ms                                                      | 39.7 ms: 1.07x slower                                                   |
| async_generators           | 488 ms                                                       | 523 ms: 1.07x slower                                                    |
| flaskblogging              | 4.70 ms                                                      | 5.05 ms: 1.07x slower                                                   |
| bench_thread_pool          | 1.26 ms                                                      | 1.36 ms: 1.08x slower                                                   |
| mdp                        | 3.33 sec                                                     | 3.60 sec: 1.08x slower                                                  |
| xml_etree_process          | 80.8 ms                                                      | 88.5 ms: 1.10x slower                                                   |
| xml_etree_generate         | 114 ms                                                       | 125 ms: 1.10x slower                                                    |
| xml_etree_iterparse        | 147 ms                                                       | 162 ms: 1.11x slower                                                    |
| dulwich_log                | 58.5 ms                                                      | 64.9 ms: 1.11x slower                                                   |
| chameleon                  | 8.95 ms                                                      | 9.96 ms: 1.11x slower                                                   |
| pycparser                  | 1.22 sec                                                     | 1.37 sec: 1.13x slower                                                  |
| html5lib                   | 66.1 ms                                                      | 74.8 ms: 1.13x slower                                                   |
| docutils                   | 3.10 sec                                                     | 3.54 sec: 1.14x slower                                                  |
| sympy_expand               | 457 ms                                                       | 522 ms: 1.14x slower                                                    |
| raytrace                   | 297 ms                                                       | 342 ms: 1.15x slower                                                    |
| sqlglot_normalize          | 129 ms                                                       | 149 ms: 1.15x slower                                                    |
| richards_super             | 62.3 ms                                                      | 71.9 ms: 1.15x slower                                                   |
| sqlglot_optimize           | 62.6 ms                                                      | 72.4 ms: 1.16x slower                                                   |
| 2to3                       | 305 ms                                                       | 354 ms: 1.16x slower                                                    |
| pylint                     | 337 ms                                                       | 392 ms: 1.16x slower                                                    |
| meteor_contest             | 113 ms                                                       | 132 ms: 1.17x slower                                                    |
| richards                   | 55.9 ms                                                      | 65.4 ms: 1.17x slower                                                   |
| typing_runtime_protocols   | 193 us                                                       | 227 us: 1.18x slower                                                    |
| django_template            | 42.3 ms                                                      | 49.9 ms: 1.18x slower                                                   |
| sympy_str                  | 265 ms                                                       | 317 ms: 1.19x slower                                                    |
| tomli_loads                | 2.57 sec                                                     | 3.08 sec: 1.20x slower                                                  |
| deepcopy_reduce            | 4.04 us                                                      | 4.84 us: 1.20x slower                                                   |
| sympy_sum                  | 144 ms                                                       | 172 ms: 1.20x slower                                                    |
| deepcopy                   | 448 us                                                       | 541 us: 1.21x slower                                                    |
| scimark_fft                | 445 ms                                                       | 537 ms: 1.21x slower                                                    |
| nbody                      | 114 ms                                                       | 138 ms: 1.21x slower                                                    |
| scimark_sparse_mat_mult    | 6.55 ms                                                      | 7.98 ms: 1.22x slower                                                   |
| bench_mp_pool              | 7.03 ms                                                      | 8.60 ms: 1.22x slower                                                   |
| pprint_pformat             | 1.93 sec                                                     | 2.37 sec: 1.23x slower                                                  |
| sqlglot_parse              | 1.42 ms                                                      | 1.75 ms: 1.23x slower                                                   |
| go                         | 161 ms                                                       | 198 ms: 1.23x slower                                                    |
| float                      | 91.4 ms                                                      | 114 ms: 1.24x slower                                                    |
| scimark_sor                | 159 ms                                                       | 198 ms: 1.24x slower                                                    |
| pprint_safe_repr           | 933 ms                                                       | 1.16 sec: 1.24x slower                                                  |
| crypto_pyaes               | 82.0 ms                                                      | 102 ms: 1.24x slower                                                    |
| chaos                      | 68.3 ms                                                      | 85.1 ms: 1.25x slower                                                   |
| pickle_pure_python         | 359 us                                                       | 449 us: 1.25x slower                                                    |
| mako                       | 13.2 ms                                                      | 16.5 ms: 1.25x slower                                                   |
| sympy_integrate            | 20.9 ms                                                      | 26.3 ms: 1.26x slower                                                   |
| fannkuch                   | 451 ms                                                       | 575 ms: 1.28x slower                                                    |
| genshi_xml                 | 60.4 ms                                                      | 77.7 ms: 1.29x slower                                                   |
| sqlglot_transpile          | 1.71 ms                                                      | 2.21 ms: 1.29x slower                                                   |
| regex_compile              | 128 ms                                                       | 167 ms: 1.30x slower                                                    |
| pyflate                    | 557 ms                                                       | 726 ms: 1.30x slower                                                    |
| nqueens                    | 98.9 ms                                                      | 130 ms: 1.31x slower                                                    |
| spectral_norm              | 141 ms                                                       | 186 ms: 1.32x slower                                                    |
| genshi_text                | 27.4 ms                                                      | 36.6 ms: 1.34x slower                                                   |
| deltablue                  | 3.88 ms                                                      | 5.19 ms: 1.34x slower                                                   |
| scimark_monte_carlo        | 82.3 ms                                                      | 114 ms: 1.39x slower                                                    |
| unpickle_pure_python       | 251 us                                                       | 349 us: 1.39x slower                                                    |
| logging_silent             | 133 ns                                                       | 188 ns: 1.41x slower                                                    |
| deepcopy_memo              | 50.8 us                                                      | 71.6 us: 1.41x slower                                                   |
| comprehensions             | 20.5 us                                                      | 30.0 us: 1.46x slower                                                   |
| scimark_lu                 | 141 ms                                                       | 207 ms: 1.46x slower                                                    |
| hexiom                     | 7.08 ms                                                      | 10.5 ms: 1.49x slower                                                   |
| telco                      | 10.0 ms                                                      | 166 ms: 16.52x slower                                                   |
| Geometric mean             | (ref)                                                        | 1.17x slower                                                            |

Benchmark hidden because not significant (14): asyncio_tcp, python_startup_no_site, async_tree_io_tg, gc_traversal, regex_effbot, unpickle_list, regex_v8, pickle_dict, async_tree_none_tg, coverage, regex_dna, logging_simple, async_tree_io, xml_etree_parse
Ignored benchmarks (4) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, bpe_tokeniser, gunicorn, mypy2

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.11x
- 95% likely to have a slowdown of 1.09x
- 99% likely to have a slowdown of 1.08x

# Memory
- memory change: 1.01x