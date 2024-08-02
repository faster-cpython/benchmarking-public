# Results vs. 3.13.0b2

- fork: python
- ref: caf6064a1bc15ac344af
- machine: linux-aarch64
- commit hash: caf6064
- commit date: 2024-05-18
- overall geometric mean: 1.11x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-arminc-aarch64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 305 ms                                                       | 360 ms: 1.18x slower                                                    |
| chameleon      | 8.95 ms                                                      | 9.20 ms: 1.03x slower                                                   |
| docutils       | 3.10 sec                                                     | 3.54 sec: 1.14x slower                                                  |
| html5lib       | 66.1 ms                                                      | 70.6 ms: 1.07x slower                                                   |
| tornado_http   | 128 ms                                                       | 145 ms: 1.13x slower                                                    |
| Geometric mean | (ref)                                                        | 1.11x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-arminc-aarch64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.27 sec                                                     | 1.25 sec: 1.02x faster                                                  |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 813 ms: 1.07x slower                                                    |
| Geometric mean             | (ref)                                                        | 1.01x slower                                                            |

Benchmark hidden because not significant (6): async_tree_none_tg, async_tree_io, async_tree_none, async_tree_memoization, async_tree_cpu_io_mixed, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): float, nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-arminc-aarch64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_dna      | 259 ms                                                       | 251 ms: 1.03x faster                                                    |
| regex_v8       | 31.1 ms                                                      | 30.3 ms: 1.03x faster                                                   |
| regex_effbot   | 4.98 ms                                                      | 4.89 ms: 1.02x faster                                                   |
| regex_compile  | 128 ms                                                       | 171 ms: 1.33x slower                                                    |
| Geometric mean | (ref)                                                        | 1.06x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-arminc-aarch64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| unpickle             | 19.8 us                                                      | 19.6 us: 1.01x faster                                                   |
| pickle_list          | 5.27 us                                                      | 5.32 us: 1.01x slower                                                   |
| json_dumps           | 13.1 ms                                                      | 13.2 ms: 1.01x slower                                                   |
| pickle_dict          | 37.6 us                                                      | 38.2 us: 1.01x slower                                                   |
| tomli_loads          | 2.57 sec                                                     | 2.65 sec: 1.03x slower                                                  |
| pickle               | 13.4 us                                                      | 13.8 us: 1.03x slower                                                   |
| xml_etree_iterparse  | 147 ms                                                       | 154 ms: 1.05x slower                                                    |
| pickle_pure_python   | 359 us                                                       | 387 us: 1.08x slower                                                    |
| unpickle_pure_python | 251 us                                                       | 276 us: 1.10x slower                                                    |
| Geometric mean       | (ref)                                                        | 1.02x slower                                                            |

Benchmark hidden because not significant (5): xml_etree_parse, json_loads, xml_etree_process, unpickle_list, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-arminc-aarch64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 13.0 ms                                                      | 14.9 ms: 1.15x slower                                                   |
| python_startup_no_site | 8.60 ms                                                      | 10.8 ms: 1.25x slower                                                   |
| Geometric mean         | (ref)                                                        | 1.20x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-arminc-aarch64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|-----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 13.2 ms                                                      | 13.1 ms: 1.01x faster                                                   |
| django_template | 42.3 ms                                                      | 49.6 ms: 1.17x slower                                                   |
| genshi_text     | 27.4 ms                                                      | 35.2 ms: 1.28x slower                                                   |
| genshi_xml      | 60.4 ms                                                      | 83.5 ms: 1.38x slower                                                   |
| Geometric mean  | (ref)                                                        | 1.20x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-arminc-aarch64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pathlib                    | 22.8 ms                                                      | 22.0 ms: 1.03x faster                                                   |
| richards                   | 55.9 ms                                                      | 54.1 ms: 1.03x faster                                                   |
| regex_dna                  | 259 ms                                                       | 251 ms: 1.03x faster                                                    |
| regex_v8                   | 31.1 ms                                                      | 30.3 ms: 1.03x faster                                                   |
| sqlite_synth               | 3.90 us                                                      | 3.82 us: 1.02x faster                                                   |
| async_tree_io_tg           | 1.27 sec                                                     | 1.25 sec: 1.02x faster                                                  |
| regex_effbot               | 4.98 ms                                                      | 4.89 ms: 1.02x faster                                                   |
| deepcopy_memo              | 50.8 us                                                      | 50.0 us: 1.02x faster                                                   |
| unpickle                   | 19.8 us                                                      | 19.6 us: 1.01x faster                                                   |
| mako                       | 13.2 ms                                                      | 13.1 ms: 1.01x faster                                                   |
| pickle_list                | 5.27 us                                                      | 5.32 us: 1.01x slower                                                   |
| json_dumps                 | 13.1 ms                                                      | 13.2 ms: 1.01x slower                                                   |
| asyncio_websockets         | 657 ms                                                       | 665 ms: 1.01x slower                                                    |
| pickle_dict                | 37.6 us                                                      | 38.2 us: 1.01x slower                                                   |
| coverage                   | 98.4 ms                                                      | 100 ms: 1.02x slower                                                    |
| scimark_fft                | 445 ms                                                       | 456 ms: 1.02x slower                                                    |
| asyncio_tcp_ssl            | 2.21 sec                                                     | 2.27 sec: 1.03x slower                                                  |
| chameleon                  | 8.95 ms                                                      | 9.20 ms: 1.03x slower                                                   |
| tomli_loads                | 2.57 sec                                                     | 2.65 sec: 1.03x slower                                                  |
| generators                 | 37.1 ms                                                      | 38.3 ms: 1.03x slower                                                   |
| spectral_norm              | 141 ms                                                       | 146 ms: 1.03x slower                                                    |
| pickle                     | 13.4 us                                                      | 13.8 us: 1.03x slower                                                   |
| create_gc_cycles           | 2.33 ms                                                      | 2.42 ms: 1.04x slower                                                   |
| mdp                        | 3.33 sec                                                     | 3.48 sec: 1.04x slower                                                  |
| logging_silent             | 133 ns                                                       | 140 ns: 1.05x slower                                                    |
| meteor_contest             | 113 ms                                                       | 119 ms: 1.05x slower                                                    |
| scimark_sparse_mat_mult    | 6.55 ms                                                      | 6.88 ms: 1.05x slower                                                   |
| xml_etree_iterparse        | 147 ms                                                       | 154 ms: 1.05x slower                                                    |
| bench_thread_pool          | 1.26 ms                                                      | 1.32 ms: 1.05x slower                                                   |
| async_generators           | 488 ms                                                       | 514 ms: 1.05x slower                                                    |
| asyncio_tcp                | 584 ms                                                       | 615 ms: 1.05x slower                                                    |
| fannkuch                   | 451 ms                                                       | 477 ms: 1.06x slower                                                    |
| dask                       | 370 ms                                                       | 393 ms: 1.06x slower                                                    |
| scimark_monte_carlo        | 82.3 ms                                                      | 87.5 ms: 1.06x slower                                                   |
| crypto_pyaes               | 82.0 ms                                                      | 87.2 ms: 1.06x slower                                                   |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 813 ms: 1.07x slower                                                    |
| html5lib                   | 66.1 ms                                                      | 70.6 ms: 1.07x slower                                                   |
| typing_runtime_protocols   | 193 us                                                       | 208 us: 1.08x slower                                                    |
| pickle_pure_python         | 359 us                                                       | 387 us: 1.08x slower                                                    |
| raytrace                   | 297 ms                                                       | 325 ms: 1.10x slower                                                    |
| unpickle_pure_python       | 251 us                                                       | 276 us: 1.10x slower                                                    |
| scimark_sor                | 159 ms                                                       | 176 ms: 1.10x slower                                                    |
| deepcopy                   | 448 us                                                       | 494 us: 1.10x slower                                                    |
| sqlglot_parse              | 1.42 ms                                                      | 1.58 ms: 1.11x slower                                                   |
| pycparser                  | 1.22 sec                                                     | 1.36 sec: 1.11x slower                                                  |
| flaskblogging              | 4.70 ms                                                      | 5.23 ms: 1.11x slower                                                   |
| sqlglot_optimize           | 62.6 ms                                                      | 69.8 ms: 1.11x slower                                                   |
| go                         | 161 ms                                                       | 179 ms: 1.12x slower                                                    |
| pyflate                    | 557 ms                                                       | 623 ms: 1.12x slower                                                    |
| sqlglot_normalize          | 129 ms                                                       | 145 ms: 1.12x slower                                                    |
| comprehensions             | 20.5 us                                                      | 23.0 us: 1.12x slower                                                   |
| tornado_http               | 128 ms                                                       | 145 ms: 1.13x slower                                                    |
| docutils                   | 3.10 sec                                                     | 3.54 sec: 1.14x slower                                                  |
| python_startup             | 13.0 ms                                                      | 14.9 ms: 1.15x slower                                                   |
| deepcopy_reduce            | 4.04 us                                                      | 4.67 us: 1.16x slower                                                   |
| django_template            | 42.3 ms                                                      | 49.6 ms: 1.17x slower                                                   |
| sqlglot_transpile          | 1.71 ms                                                      | 2.01 ms: 1.17x slower                                                   |
| 2to3                       | 305 ms                                                       | 360 ms: 1.18x slower                                                    |
| deltablue                  | 3.88 ms                                                      | 4.58 ms: 1.18x slower                                                   |
| pprint_safe_repr           | 933 ms                                                       | 1.10 sec: 1.18x slower                                                  |
| pprint_pformat             | 1.93 sec                                                     | 2.28 sec: 1.18x slower                                                  |
| sympy_expand               | 457 ms                                                       | 541 ms: 1.18x slower                                                    |
| dulwich_log                | 58.5 ms                                                      | 69.7 ms: 1.19x slower                                                   |
| sympy_str                  | 265 ms                                                       | 317 ms: 1.19x slower                                                    |
| nqueens                    | 98.9 ms                                                      | 119 ms: 1.20x slower                                                    |
| pylint                     | 337 ms                                                       | 411 ms: 1.22x slower                                                    |
| bench_mp_pool              | 7.03 ms                                                      | 8.66 ms: 1.23x slower                                                   |
| sympy_integrate            | 20.9 ms                                                      | 26.0 ms: 1.24x slower                                                   |
| python_startup_no_site     | 8.60 ms                                                      | 10.8 ms: 1.25x slower                                                   |
| sympy_sum                  | 144 ms                                                       | 184 ms: 1.28x slower                                                    |
| hexiom                     | 7.08 ms                                                      | 9.07 ms: 1.28x slower                                                   |
| genshi_text                | 27.4 ms                                                      | 35.2 ms: 1.28x slower                                                   |
| scimark_lu                 | 141 ms                                                       | 182 ms: 1.29x slower                                                    |
| chaos                      | 68.3 ms                                                      | 88.5 ms: 1.30x slower                                                   |
| regex_compile              | 128 ms                                                       | 171 ms: 1.33x slower                                                    |
| genshi_xml                 | 60.4 ms                                                      | 83.5 ms: 1.38x slower                                                   |
| telco                      | 10.0 ms                                                      | 167 ms: 16.63x slower                                                   |
| Geometric mean             | (ref)                                                        | 1.11x slower                                                            |

Benchmark hidden because not significant (21): xml_etree_parse, float, richards_super, thrift, async_tree_none_tg, logging_format, nbody, coroutines, json_loads, gc_traversal, xml_etree_process, logging_simple, unpickle_list, pidigits, async_tree_io, async_tree_none, json, async_tree_memoization, async_tree_cpu_io_mixed, async_tree_memoization_tg, xml_etree_generate
Ignored benchmarks (4) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, bpe_tokeniser, gunicorn, mypy2

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: 1.10x