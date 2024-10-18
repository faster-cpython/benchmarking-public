# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: justin_likely
- machine: linux-aarch64
- commit hash: bad9944
- commit date: 2024-10-18
- overall geometric mean: 1.17x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: 1.20x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241018-arminc-aarch64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 305 ms                                                       | 382 ms: 1.25x slower                                                    |
| docutils       | 3.10 sec                                                     | 3.58 sec: 1.15x slower                                                  |
| html5lib       | 66.1 ms                                                      | 71.9 ms: 1.09x slower                                                   |
| tornado_http   | 128 ms                                                       | 147 ms: 1.15x slower                                                    |
| Geometric mean | (ref)                                                        | 1.16x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241018-arminc-aarch64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|---------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg | 604 ms                                                       | 536 ms: 1.13x faster                                                    |
| async_tree_none           | 492 ms                                                       | 457 ms: 1.08x faster                                                    |
| async_tree_memoization    | 645 ms                                                       | 600 ms: 1.07x faster                                                    |
| async_tree_none_tg        | 476 ms                                                       | 446 ms: 1.07x faster                                                    |
| async_tree_cpu_io_mixed   | 791 ms                                                       | 755 ms: 1.05x faster                                                    |
| async_tree_io             | 1.22 sec                                                     | 1.18 sec: 1.03x faster                                                  |
| async_tree_io_tg          | 1.27 sec                                                     | 1.25 sec: 1.02x faster                                                  |
| Geometric mean            | (ref)                                                        | 1.06x faster                                                            |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241018-arminc-aarch64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 91.4 ms                                                      | 97.8 ms: 1.07x slower                                                   |
| Geometric mean | (ref)                                                        | 1.03x slower                                                            |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241018-arminc-aarch64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_dna      | 259 ms                                                       | 254 ms: 1.02x faster                                                    |
| regex_compile  | 128 ms                                                       | 179 ms: 1.40x slower                                                    |
| Geometric mean | (ref)                                                        | 1.08x slower                                                            |

Benchmark hidden because not significant (2): regex_effbot, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241018-arminc-aarch64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_generate   | 114 ms                                                       | 112 ms: 1.02x faster                                                    |
| json_loads           | 32.1 us                                                      | 31.6 us: 1.01x faster                                                   |
| unpickle_list        | 6.52 us                                                      | 6.42 us: 1.01x faster                                                   |
| xml_etree_iterparse  | 147 ms                                                       | 150 ms: 1.02x slower                                                    |
| tomli_loads          | 2.57 sec                                                     | 2.66 sec: 1.04x slower                                                  |
| pickle               | 13.4 us                                                      | 13.9 us: 1.04x slower                                                   |
| unpickle_pure_python | 251 us                                                       | 270 us: 1.07x slower                                                    |
| pickle_pure_python   | 359 us                                                       | 392 us: 1.09x slower                                                    |
| json_dumps           | 13.1 ms                                                      | 14.6 ms: 1.11x slower                                                   |
| Geometric mean       | (ref)                                                        | 1.02x slower                                                            |

Benchmark hidden because not significant (5): xml_etree_parse, unpickle, pickle_list, pickle_dict, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241018-arminc-aarch64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.60 ms                                                      | 8.73 ms: 1.02x slower                                                   |
| python_startup         | 13.0 ms                                                      | 14.5 ms: 1.12x slower                                                   |
| Geometric mean         | (ref)                                                        | 1.07x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241018-arminc-aarch64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|-----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 13.2 ms                                                      | 13.6 ms: 1.03x slower                                                   |
| django_template | 42.3 ms                                                      | 52.6 ms: 1.24x slower                                                   |
| genshi_text     | 27.4 ms                                                      | 34.1 ms: 1.24x slower                                                   |
| genshi_xml      | 60.4 ms                                                      | 83.9 ms: 1.39x slower                                                   |
| Geometric mean  | (ref)                                                        | 1.22x slower                                                            |

All benchmarks:
===============

| Benchmark                 | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241018-arminc-aarch64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|---------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy_memo             | 50.8 us                                                      | 39.3 us: 1.29x faster                                                   |
| deepcopy                  | 448 us                                                       | 380 us: 1.18x faster                                                    |
| async_tree_memoization_tg | 604 ms                                                       | 536 ms: 1.13x faster                                                    |
| async_tree_none           | 492 ms                                                       | 457 ms: 1.08x faster                                                    |
| async_tree_memoization    | 645 ms                                                       | 600 ms: 1.07x faster                                                    |
| async_tree_none_tg        | 476 ms                                                       | 446 ms: 1.07x faster                                                    |
| async_tree_cpu_io_mixed   | 791 ms                                                       | 755 ms: 1.05x faster                                                    |
| pathlib                   | 22.8 ms                                                      | 21.8 ms: 1.05x faster                                                   |
| telco                     | 10.0 ms                                                      | 9.64 ms: 1.04x faster                                                   |
| async_tree_io             | 1.22 sec                                                     | 1.18 sec: 1.03x faster                                                  |
| scimark_sor               | 159 ms                                                       | 154 ms: 1.03x faster                                                    |
| async_tree_io_tg          | 1.27 sec                                                     | 1.25 sec: 1.02x faster                                                  |
| regex_dna                 | 259 ms                                                       | 254 ms: 1.02x faster                                                    |
| xml_etree_generate        | 114 ms                                                       | 112 ms: 1.02x faster                                                    |
| json_loads                | 32.1 us                                                      | 31.6 us: 1.01x faster                                                   |
| unpickle_list             | 6.52 us                                                      | 6.42 us: 1.01x faster                                                   |
| deepcopy_reduce           | 4.04 us                                                      | 3.98 us: 1.01x faster                                                   |
| asyncio_websockets        | 657 ms                                                       | 663 ms: 1.01x slower                                                    |
| python_startup_no_site    | 8.60 ms                                                      | 8.73 ms: 1.02x slower                                                   |
| xml_etree_iterparse       | 147 ms                                                       | 150 ms: 1.02x slower                                                    |
| scimark_fft               | 445 ms                                                       | 455 ms: 1.02x slower                                                    |
| asyncio_tcp_ssl           | 2.21 sec                                                     | 2.26 sec: 1.02x slower                                                  |
| bpe_tokeniser             | 5.83 sec                                                     | 5.96 sec: 1.02x slower                                                  |
| sqlite_synth              | 3.90 us                                                      | 4.00 us: 1.03x slower                                                   |
| mako                      | 13.2 ms                                                      | 13.6 ms: 1.03x slower                                                   |
| tomli_loads               | 2.57 sec                                                     | 2.66 sec: 1.04x slower                                                  |
| logging_format            | 7.82 us                                                      | 8.12 us: 1.04x slower                                                   |
| logging_simple            | 7.21 us                                                      | 7.49 us: 1.04x slower                                                   |
| pickle                    | 13.4 us                                                      | 13.9 us: 1.04x slower                                                   |
| scimark_lu                | 141 ms                                                       | 148 ms: 1.05x slower                                                    |
| mdp                       | 3.33 sec                                                     | 3.50 sec: 1.05x slower                                                  |
| async_generators          | 488 ms                                                       | 515 ms: 1.05x slower                                                    |
| asyncio_tcp               | 584 ms                                                       | 621 ms: 1.06x slower                                                    |
| float                     | 91.4 ms                                                      | 97.8 ms: 1.07x slower                                                   |
| unpickle_pure_python      | 251 us                                                       | 270 us: 1.07x slower                                                    |
| scimark_monte_carlo       | 82.3 ms                                                      | 88.7 ms: 1.08x slower                                                   |
| html5lib                  | 66.1 ms                                                      | 71.9 ms: 1.09x slower                                                   |
| crypto_pyaes              | 82.0 ms                                                      | 89.2 ms: 1.09x slower                                                   |
| meteor_contest            | 113 ms                                                       | 124 ms: 1.09x slower                                                    |
| spectral_norm             | 141 ms                                                       | 154 ms: 1.09x slower                                                    |
| pickle_pure_python        | 359 us                                                       | 392 us: 1.09x slower                                                    |
| bench_thread_pool         | 1.26 ms                                                      | 1.38 ms: 1.10x slower                                                   |
| scimark_sparse_mat_mult   | 6.55 ms                                                      | 7.23 ms: 1.10x slower                                                   |
| json_dumps                | 13.1 ms                                                      | 14.6 ms: 1.11x slower                                                   |
| python_startup            | 13.0 ms                                                      | 14.5 ms: 1.12x slower                                                   |
| typing_runtime_protocols  | 193 us                                                       | 219 us: 1.13x slower                                                    |
| fannkuch                  | 451 ms                                                       | 512 ms: 1.13x slower                                                    |
| tornado_http              | 128 ms                                                       | 147 ms: 1.15x slower                                                    |
| pyflate                   | 557 ms                                                       | 642 ms: 1.15x slower                                                    |
| docutils                  | 3.10 sec                                                     | 3.58 sec: 1.15x slower                                                  |
| richards                  | 55.9 ms                                                      | 64.6 ms: 1.16x slower                                                   |
| richards_super            | 62.3 ms                                                      | 72.2 ms: 1.16x slower                                                   |
| deltablue                 | 3.88 ms                                                      | 4.50 ms: 1.16x slower                                                   |
| go                        | 161 ms                                                       | 187 ms: 1.16x slower                                                    |
| raytrace                  | 297 ms                                                       | 352 ms: 1.19x slower                                                    |
| sqlglot_parse             | 1.42 ms                                                      | 1.71 ms: 1.20x slower                                                   |
| gc_traversal              | 5.17 ms                                                      | 6.24 ms: 1.21x slower                                                   |
| comprehensions            | 20.5 us                                                      | 24.8 us: 1.21x slower                                                   |
| sqlglot_normalize         | 129 ms                                                       | 159 ms: 1.23x slower                                                    |
| django_template           | 42.3 ms                                                      | 52.6 ms: 1.24x slower                                                   |
| genshi_text               | 27.4 ms                                                      | 34.1 ms: 1.24x slower                                                   |
| pycparser                 | 1.22 sec                                                     | 1.52 sec: 1.25x slower                                                  |
| chaos                     | 68.3 ms                                                      | 85.7 ms: 1.25x slower                                                   |
| 2to3                      | 305 ms                                                       | 382 ms: 1.25x slower                                                    |
| nqueens                   | 98.9 ms                                                      | 124 ms: 1.26x slower                                                    |
| sympy_expand              | 457 ms                                                       | 589 ms: 1.29x slower                                                    |
| sqlglot_transpile         | 1.71 ms                                                      | 2.25 ms: 1.32x slower                                                   |
| pprint_safe_repr          | 933 ms                                                       | 1.23 sec: 1.32x slower                                                  |
| sqlglot_optimize          | 62.6 ms                                                      | 83.1 ms: 1.33x slower                                                   |
| sympy_str                 | 265 ms                                                       | 356 ms: 1.34x slower                                                    |
| pprint_pformat            | 1.93 sec                                                     | 2.62 sec: 1.36x slower                                                  |
| dulwich_log               | 58.5 ms                                                      | 79.9 ms: 1.37x slower                                                   |
| genshi_xml                | 60.4 ms                                                      | 83.9 ms: 1.39x slower                                                   |
| regex_compile             | 128 ms                                                       | 179 ms: 1.40x slower                                                    |
| sympy_integrate           | 20.9 ms                                                      | 29.3 ms: 1.40x slower                                                   |
| hexiom                    | 7.08 ms                                                      | 10.3 ms: 1.45x slower                                                   |
| pylint                    | 337 ms                                                       | 492 ms: 1.46x slower                                                    |
| sympy_sum                 | 144 ms                                                       | 214 ms: 1.49x slower                                                    |
| generators                | 37.1 ms                                                      | 59.1 ms: 1.59x slower                                                   |
| create_gc_cycles          | 2.33 ms                                                      | 3.73 ms: 1.60x slower                                                   |
| bench_mp_pool             | 7.03 ms                                                      | 2.25 sec: 320.22x slower                                                |
| Geometric mean            | (ref)                                                        | 1.17x slower                                                            |

Benchmark hidden because not significant (15): async_tree_cpu_io_mixed_tg, xml_etree_parse, unpickle, logging_silent, coroutines, regex_effbot, json, regex_v8, pickle_list, pickle_dict, coverage, pidigits, xml_etree_process, nbody, thrift
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (2) of results/bm-20241018-3.14.0a1+-bad9944-JIT/bm-20241018-arminc-aarch64-brandtbucher-justin_likely-3.14.0a1+-bad9944.json: sphinx, unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: 1.20x