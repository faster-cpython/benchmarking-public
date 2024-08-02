# Results vs. 3.13.0b2

- fork: python
- ref: caf6064a1bc15ac344af
- machine: linux-aarch64
- commit hash: caf6064
- commit date: 2024-05-18
- overall geometric mean: 1.17x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-arminc-aarch64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 305 ms                                                       | 353 ms: 1.16x slower                                                    |
| chameleon      | 8.95 ms                                                      | 9.93 ms: 1.11x slower                                                   |
| docutils       | 3.10 sec                                                     | 3.51 sec: 1.13x slower                                                  |
| html5lib       | 66.1 ms                                                      | 73.7 ms: 1.12x slower                                                   |
| tornado_http   | 128 ms                                                       | 139 ms: 1.08x slower                                                    |
| Geometric mean | (ref)                                                        | 1.12x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-arminc-aarch64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_cpu_io_mixed    | 791 ms                                                       | 814 ms: 1.03x slower                                                    |
| async_tree_none            | 492 ms                                                       | 507 ms: 1.03x slower                                                    |
| async_tree_memoization     | 645 ms                                                       | 665 ms: 1.03x slower                                                    |
| async_tree_memoization_tg  | 604 ms                                                       | 646 ms: 1.07x slower                                                    |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 816 ms: 1.07x slower                                                    |
| Geometric mean             | (ref)                                                        | 1.03x slower                                                            |

Benchmark hidden because not significant (3): async_tree_io_tg, async_tree_none_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-arminc-aarch64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pidigits       | 234 ms                                                       | 237 ms: 1.01x slower                                                    |
| nbody          | 114 ms                                                       | 137 ms: 1.20x slower                                                    |
| float          | 91.4 ms                                                      | 113 ms: 1.24x slower                                                    |
| Geometric mean | (ref)                                                        | 1.15x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-arminc-aarch64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_dna      | 259 ms                                                       | 249 ms: 1.04x faster                                                    |
| regex_effbot   | 4.98 ms                                                      | 4.88 ms: 1.02x faster                                                   |
| regex_compile  | 128 ms                                                       | 166 ms: 1.30x slower                                                    |
| Geometric mean | (ref)                                                        | 1.05x slower                                                            |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-arminc-aarch64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| unpickle             | 19.8 us                                                      | 19.5 us: 1.01x faster                                                   |
| json_loads           | 32.1 us                                                      | 32.2 us: 1.00x slower                                                   |
| unpickle_list        | 6.52 us                                                      | 6.77 us: 1.04x slower                                                   |
| pickle               | 13.4 us                                                      | 14.0 us: 1.04x slower                                                   |
| json_dumps           | 13.1 ms                                                      | 13.9 ms: 1.06x slower                                                   |
| xml_etree_process    | 80.8 ms                                                      | 87.2 ms: 1.08x slower                                                   |
| xml_etree_generate   | 114 ms                                                       | 125 ms: 1.10x slower                                                    |
| xml_etree_iterparse  | 147 ms                                                       | 162 ms: 1.10x slower                                                    |
| tomli_loads          | 2.57 sec                                                     | 3.09 sec: 1.20x slower                                                  |
| pickle_pure_python   | 359 us                                                       | 440 us: 1.23x slower                                                    |
| unpickle_pure_python | 251 us                                                       | 349 us: 1.39x slower                                                    |
| Geometric mean       | (ref)                                                        | 1.08x slower                                                            |

Benchmark hidden because not significant (3): pickle_dict, pickle_list, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-arminc-aarch64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup | 13.0 ms                                                      | 12.6 ms: 1.03x faster                                                   |
| Geometric mean | (ref)                                                        | 1.01x faster                                                            |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-arminc-aarch64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|-----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| django_template | 42.3 ms                                                      | 48.9 ms: 1.16x slower                                                   |
| genshi_xml      | 60.4 ms                                                      | 76.1 ms: 1.26x slower                                                   |
| mako            | 13.2 ms                                                      | 16.8 ms: 1.28x slower                                                   |
| genshi_text     | 27.4 ms                                                      | 35.6 ms: 1.30x slower                                                   |
| Geometric mean  | (ref)                                                        | 1.25x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-arminc-aarch64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_dna                  | 259 ms                                                       | 249 ms: 1.04x faster                                                    |
| python_startup             | 13.0 ms                                                      | 12.6 ms: 1.03x faster                                                   |
| regex_effbot               | 4.98 ms                                                      | 4.88 ms: 1.02x faster                                                   |
| unpickle                   | 19.8 us                                                      | 19.5 us: 1.01x faster                                                   |
| json_loads                 | 32.1 us                                                      | 32.2 us: 1.00x slower                                                   |
| pidigits                   | 234 ms                                                       | 237 ms: 1.01x slower                                                    |
| gc_traversal               | 5.17 ms                                                      | 5.25 ms: 1.01x slower                                                   |
| asyncio_websockets         | 657 ms                                                       | 668 ms: 1.02x slower                                                    |
| coverage                   | 98.4 ms                                                      | 100 ms: 1.02x slower                                                    |
| sqlite_synth               | 3.90 us                                                      | 3.98 us: 1.02x slower                                                   |
| asyncio_tcp_ssl            | 2.21 sec                                                     | 2.26 sec: 1.02x slower                                                  |
| thrift                     | 962 us                                                       | 983 us: 1.02x slower                                                    |
| logging_simple             | 7.21 us                                                      | 7.38 us: 1.02x slower                                                   |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 814 ms: 1.03x slower                                                    |
| json                       | 5.64 ms                                                      | 5.81 ms: 1.03x slower                                                   |
| async_tree_none            | 492 ms                                                       | 507 ms: 1.03x slower                                                    |
| logging_format             | 7.82 us                                                      | 8.07 us: 1.03x slower                                                   |
| async_tree_memoization     | 645 ms                                                       | 665 ms: 1.03x slower                                                    |
| unpickle_list              | 6.52 us                                                      | 6.77 us: 1.04x slower                                                   |
| pickle                     | 13.4 us                                                      | 14.0 us: 1.04x slower                                                   |
| dask                       | 370 ms                                                       | 391 ms: 1.06x slower                                                    |
| create_gc_cycles           | 2.33 ms                                                      | 2.47 ms: 1.06x slower                                                   |
| async_generators           | 488 ms                                                       | 517 ms: 1.06x slower                                                    |
| coroutines                 | 29.0 ms                                                      | 30.8 ms: 1.06x slower                                                   |
| json_dumps                 | 13.1 ms                                                      | 13.9 ms: 1.06x slower                                                   |
| generators                 | 37.1 ms                                                      | 39.5 ms: 1.06x slower                                                   |
| async_tree_memoization_tg  | 604 ms                                                       | 646 ms: 1.07x slower                                                    |
| flaskblogging              | 4.70 ms                                                      | 5.02 ms: 1.07x slower                                                   |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 816 ms: 1.07x slower                                                    |
| bench_thread_pool          | 1.26 ms                                                      | 1.35 ms: 1.07x slower                                                   |
| mdp                        | 3.33 sec                                                     | 3.59 sec: 1.08x slower                                                  |
| xml_etree_process          | 80.8 ms                                                      | 87.2 ms: 1.08x slower                                                   |
| tornado_http               | 128 ms                                                       | 139 ms: 1.08x slower                                                    |
| bench_mp_pool              | 7.03 ms                                                      | 7.71 ms: 1.10x slower                                                   |
| xml_etree_generate         | 114 ms                                                       | 125 ms: 1.10x slower                                                    |
| xml_etree_iterparse        | 147 ms                                                       | 162 ms: 1.10x slower                                                    |
| chameleon                  | 8.95 ms                                                      | 9.93 ms: 1.11x slower                                                   |
| dulwich_log                | 58.5 ms                                                      | 65.2 ms: 1.11x slower                                                   |
| html5lib                   | 66.1 ms                                                      | 73.7 ms: 1.12x slower                                                   |
| pycparser                  | 1.22 sec                                                     | 1.37 sec: 1.13x slower                                                  |
| docutils                   | 3.10 sec                                                     | 3.51 sec: 1.13x slower                                                  |
| sympy_expand               | 457 ms                                                       | 522 ms: 1.14x slower                                                    |
| sqlglot_normalize          | 129 ms                                                       | 149 ms: 1.15x slower                                                    |
| raytrace                   | 297 ms                                                       | 342 ms: 1.15x slower                                                    |
| richards                   | 55.9 ms                                                      | 64.4 ms: 1.15x slower                                                   |
| sqlglot_optimize           | 62.6 ms                                                      | 72.3 ms: 1.15x slower                                                   |
| django_template            | 42.3 ms                                                      | 48.9 ms: 1.16x slower                                                   |
| 2to3                       | 305 ms                                                       | 353 ms: 1.16x slower                                                    |
| richards_super             | 62.3 ms                                                      | 72.5 ms: 1.16x slower                                                   |
| meteor_contest             | 113 ms                                                       | 133 ms: 1.17x slower                                                    |
| typing_runtime_protocols   | 193 us                                                       | 227 us: 1.17x slower                                                    |
| pylint                     | 337 ms                                                       | 396 ms: 1.17x slower                                                    |
| deepcopy_reduce            | 4.04 us                                                      | 4.80 us: 1.19x slower                                                   |
| sympy_str                  | 265 ms                                                       | 317 ms: 1.19x slower                                                    |
| deepcopy                   | 448 us                                                       | 535 us: 1.19x slower                                                    |
| tomli_loads                | 2.57 sec                                                     | 3.09 sec: 1.20x slower                                                  |
| nbody                      | 114 ms                                                       | 137 ms: 1.20x slower                                                    |
| scimark_fft                | 445 ms                                                       | 539 ms: 1.21x slower                                                    |
| go                         | 161 ms                                                       | 195 ms: 1.21x slower                                                    |
| sympy_sum                  | 144 ms                                                       | 175 ms: 1.22x slower                                                    |
| pickle_pure_python         | 359 us                                                       | 440 us: 1.23x slower                                                    |
| scimark_sparse_mat_mult    | 6.55 ms                                                      | 8.05 ms: 1.23x slower                                                   |
| crypto_pyaes               | 82.0 ms                                                      | 101 ms: 1.24x slower                                                    |
| float                      | 91.4 ms                                                      | 113 ms: 1.24x slower                                                    |
| scimark_sor                | 159 ms                                                       | 198 ms: 1.24x slower                                                    |
| sympy_integrate            | 20.9 ms                                                      | 25.9 ms: 1.24x slower                                                   |
| sqlglot_parse              | 1.42 ms                                                      | 1.77 ms: 1.24x slower                                                   |
| pprint_pformat             | 1.93 sec                                                     | 2.41 sec: 1.25x slower                                                  |
| chaos                      | 68.3 ms                                                      | 85.6 ms: 1.25x slower                                                   |
| genshi_xml                 | 60.4 ms                                                      | 76.1 ms: 1.26x slower                                                   |
| pprint_safe_repr           | 933 ms                                                       | 1.18 sec: 1.27x slower                                                  |
| fannkuch                   | 451 ms                                                       | 574 ms: 1.27x slower                                                    |
| mako                       | 13.2 ms                                                      | 16.8 ms: 1.28x slower                                                   |
| genshi_text                | 27.4 ms                                                      | 35.6 ms: 1.30x slower                                                   |
| sqlglot_transpile          | 1.71 ms                                                      | 2.22 ms: 1.30x slower                                                   |
| regex_compile              | 128 ms                                                       | 166 ms: 1.30x slower                                                    |
| pyflate                    | 557 ms                                                       | 727 ms: 1.31x slower                                                    |
| spectral_norm              | 141 ms                                                       | 185 ms: 1.31x slower                                                    |
| nqueens                    | 98.9 ms                                                      | 130 ms: 1.32x slower                                                    |
| deltablue                  | 3.88 ms                                                      | 5.14 ms: 1.32x slower                                                   |
| scimark_monte_carlo        | 82.3 ms                                                      | 114 ms: 1.38x slower                                                    |
| unpickle_pure_python       | 251 us                                                       | 349 us: 1.39x slower                                                    |
| logging_silent             | 133 ns                                                       | 189 ns: 1.41x slower                                                    |
| deepcopy_memo              | 50.8 us                                                      | 71.9 us: 1.42x slower                                                   |
| scimark_lu                 | 141 ms                                                       | 207 ms: 1.46x slower                                                    |
| comprehensions             | 20.5 us                                                      | 30.1 us: 1.47x slower                                                   |
| hexiom                     | 7.08 ms                                                      | 10.5 ms: 1.49x slower                                                   |
| telco                      | 10.0 ms                                                      | 168 ms: 16.79x slower                                                   |
| Geometric mean             | (ref)                                                        | 1.17x slower                                                            |

Benchmark hidden because not significant (10): async_tree_io_tg, pickle_dict, pickle_list, pathlib, regex_v8, python_startup_no_site, async_tree_none_tg, asyncio_tcp, xml_etree_parse, async_tree_io
Ignored benchmarks (4) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, bpe_tokeniser, gunicorn, mypy2

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.10x
- 95% likely to have a slowdown of 1.09x
- 99% likely to have a slowdown of 1.08x

# Memory
- memory change: 1.01x