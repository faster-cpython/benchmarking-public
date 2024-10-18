# Results vs. 3.13.0b2

- fork: python
- ref: v3.14.0a1
- machine: linux-aarch64
- commit hash: 8cdaca8
- commit date: 2024-10-15
- overall geometric mean: 1.16x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: 1.20x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 305 ms                                                       | 382 ms: 1.25x slower                                         |
| docutils       | 3.10 sec                                                     | 3.61 sec: 1.17x slower                                       |
| html5lib       | 66.1 ms                                                      | 71.8 ms: 1.09x slower                                        |
| tornado_http   | 128 ms                                                       | 147 ms: 1.15x slower                                         |
| Geometric mean | (ref)                                                        | 1.16x slower                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|---------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_memoization_tg | 604 ms                                                       | 542 ms: 1.12x faster                                         |
| async_tree_memoization    | 645 ms                                                       | 605 ms: 1.07x faster                                         |
| async_tree_none           | 492 ms                                                       | 463 ms: 1.06x faster                                         |
| async_tree_none_tg        | 476 ms                                                       | 451 ms: 1.06x faster                                         |
| async_tree_cpu_io_mixed   | 791 ms                                                       | 759 ms: 1.04x faster                                         |
| async_tree_io_tg          | 1.27 sec                                                     | 1.25 sec: 1.02x faster                                       |
| Geometric mean            | (ref)                                                        | 1.05x faster                                                 |

Benchmark hidden because not significant (2): async_tree_io, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| float          | 91.4 ms                                                      | 97.2 ms: 1.06x slower                                        |
| Geometric mean | (ref)                                                        | 1.03x slower                                                 |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| regex_dna      | 259 ms                                                       | 244 ms: 1.06x faster                                         |
| regex_v8       | 31.1 ms                                                      | 31.6 ms: 1.02x slower                                        |
| regex_compile  | 128 ms                                                       | 179 ms: 1.40x slower                                         |
| Geometric mean | (ref)                                                        | 1.07x slower                                                 |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| unpickle             | 19.8 us                                                      | 19.0 us: 1.04x faster                                        |
| pickle_list          | 5.27 us                                                      | 5.12 us: 1.03x faster                                        |
| xml_etree_generate   | 114 ms                                                       | 111 ms: 1.02x faster                                         |
| json_loads           | 32.1 us                                                      | 31.7 us: 1.01x faster                                        |
| pickle               | 13.4 us                                                      | 13.8 us: 1.03x slower                                        |
| tomli_loads          | 2.57 sec                                                     | 2.65 sec: 1.03x slower                                       |
| xml_etree_iterparse  | 147 ms                                                       | 151 ms: 1.03x slower                                         |
| unpickle_pure_python | 251 us                                                       | 268 us: 1.06x slower                                         |
| pickle_pure_python   | 359 us                                                       | 389 us: 1.08x slower                                         |
| json_dumps           | 13.1 ms                                                      | 14.4 ms: 1.10x slower                                        |
| Geometric mean       | (ref)                                                        | 1.01x slower                                                 |

Benchmark hidden because not significant (4): xml_etree_parse, xml_etree_process, unpickle_list, pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup_no_site | 8.60 ms                                                      | 8.79 ms: 1.02x slower                                        |
| python_startup         | 13.0 ms                                                      | 14.7 ms: 1.13x slower                                        |
| Geometric mean         | (ref)                                                        | 1.08x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|-----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| mako            | 13.2 ms                                                      | 13.2 ms: 1.00x slower                                        |
| django_template | 42.3 ms                                                      | 52.4 ms: 1.24x slower                                        |
| genshi_text     | 27.4 ms                                                      | 34.2 ms: 1.25x slower                                        |
| genshi_xml      | 60.4 ms                                                      | 84.1 ms: 1.39x slower                                        |
| Geometric mean  | (ref)                                                        | 1.21x slower                                                 |

All benchmarks:
===============

| Benchmark                 | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|---------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| deepcopy_memo             | 50.8 us                                                      | 39.2 us: 1.29x faster                                        |
| deepcopy                  | 448 us                                                       | 377 us: 1.19x faster                                         |
| async_tree_memoization_tg | 604 ms                                                       | 542 ms: 1.12x faster                                         |
| async_tree_memoization    | 645 ms                                                       | 605 ms: 1.07x faster                                         |
| async_tree_none           | 492 ms                                                       | 463 ms: 1.06x faster                                         |
| regex_dna                 | 259 ms                                                       | 244 ms: 1.06x faster                                         |
| async_tree_none_tg        | 476 ms                                                       | 451 ms: 1.06x faster                                         |
| pathlib                   | 22.8 ms                                                      | 21.6 ms: 1.06x faster                                        |
| async_tree_cpu_io_mixed   | 791 ms                                                       | 759 ms: 1.04x faster                                         |
| scimark_sor               | 159 ms                                                       | 154 ms: 1.04x faster                                         |
| unpickle                  | 19.8 us                                                      | 19.0 us: 1.04x faster                                        |
| pickle_list               | 5.27 us                                                      | 5.12 us: 1.03x faster                                        |
| telco                     | 10.0 ms                                                      | 9.74 ms: 1.03x faster                                        |
| xml_etree_generate        | 114 ms                                                       | 111 ms: 1.02x faster                                         |
| async_tree_io_tg          | 1.27 sec                                                     | 1.25 sec: 1.02x faster                                       |
| deepcopy_reduce           | 4.04 us                                                      | 3.98 us: 1.01x faster                                        |
| json_loads                | 32.1 us                                                      | 31.7 us: 1.01x faster                                        |
| mako                      | 13.2 ms                                                      | 13.2 ms: 1.00x slower                                        |
| asyncio_websockets        | 657 ms                                                       | 664 ms: 1.01x slower                                         |
| regex_v8                  | 31.1 ms                                                      | 31.6 ms: 1.02x slower                                        |
| scimark_fft               | 445 ms                                                       | 454 ms: 1.02x slower                                         |
| python_startup_no_site    | 8.60 ms                                                      | 8.79 ms: 1.02x slower                                        |
| bpe_tokeniser             | 5.83 sec                                                     | 5.97 sec: 1.02x slower                                       |
| coverage                  | 98.4 ms                                                      | 101 ms: 1.03x slower                                         |
| pickle                    | 13.4 us                                                      | 13.8 us: 1.03x slower                                        |
| asyncio_tcp_ssl           | 2.21 sec                                                     | 2.27 sec: 1.03x slower                                       |
| tomli_loads               | 2.57 sec                                                     | 2.65 sec: 1.03x slower                                       |
| logging_format            | 7.82 us                                                      | 8.08 us: 1.03x slower                                        |
| xml_etree_iterparse       | 147 ms                                                       | 151 ms: 1.03x slower                                         |
| logging_simple            | 7.21 us                                                      | 7.45 us: 1.03x slower                                        |
| async_generators          | 488 ms                                                       | 507 ms: 1.04x slower                                         |
| mdp                       | 3.33 sec                                                     | 3.51 sec: 1.05x slower                                       |
| float                     | 91.4 ms                                                      | 97.2 ms: 1.06x slower                                        |
| unpickle_pure_python      | 251 us                                                       | 268 us: 1.06x slower                                         |
| scimark_lu                | 141 ms                                                       | 151 ms: 1.07x slower                                         |
| asyncio_tcp               | 584 ms                                                       | 630 ms: 1.08x slower                                         |
| pickle_pure_python        | 359 us                                                       | 389 us: 1.08x slower                                         |
| meteor_contest            | 113 ms                                                       | 123 ms: 1.08x slower                                         |
| html5lib                  | 66.1 ms                                                      | 71.8 ms: 1.09x slower                                        |
| scimark_monte_carlo       | 82.3 ms                                                      | 89.5 ms: 1.09x slower                                        |
| bench_thread_pool         | 1.26 ms                                                      | 1.37 ms: 1.09x slower                                        |
| scimark_sparse_mat_mult   | 6.55 ms                                                      | 7.16 ms: 1.09x slower                                        |
| spectral_norm             | 141 ms                                                       | 155 ms: 1.10x slower                                         |
| json_dumps                | 13.1 ms                                                      | 14.4 ms: 1.10x slower                                        |
| pyflate                   | 557 ms                                                       | 615 ms: 1.11x slower                                         |
| crypto_pyaes              | 82.0 ms                                                      | 90.8 ms: 1.11x slower                                        |
| fannkuch                  | 451 ms                                                       | 503 ms: 1.12x slower                                         |
| typing_runtime_protocols  | 193 us                                                       | 218 us: 1.12x slower                                         |
| python_startup            | 13.0 ms                                                      | 14.7 ms: 1.13x slower                                        |
| go                        | 161 ms                                                       | 184 ms: 1.14x slower                                         |
| richards_super            | 62.3 ms                                                      | 71.4 ms: 1.15x slower                                        |
| richards                  | 55.9 ms                                                      | 64.2 ms: 1.15x slower                                        |
| tornado_http              | 128 ms                                                       | 147 ms: 1.15x slower                                         |
| docutils                  | 3.10 sec                                                     | 3.61 sec: 1.17x slower                                       |
| deltablue                 | 3.88 ms                                                      | 4.55 ms: 1.17x slower                                        |
| raytrace                  | 297 ms                                                       | 349 ms: 1.18x slower                                         |
| sqlglot_parse             | 1.42 ms                                                      | 1.70 ms: 1.19x slower                                        |
| gc_traversal              | 5.17 ms                                                      | 6.22 ms: 1.20x slower                                        |
| comprehensions            | 20.5 us                                                      | 24.7 us: 1.20x slower                                        |
| sqlglot_normalize         | 129 ms                                                       | 157 ms: 1.21x slower                                         |
| django_template           | 42.3 ms                                                      | 52.4 ms: 1.24x slower                                        |
| pycparser                 | 1.22 sec                                                     | 1.52 sec: 1.25x slower                                       |
| chaos                     | 68.3 ms                                                      | 85.0 ms: 1.25x slower                                        |
| genshi_text               | 27.4 ms                                                      | 34.2 ms: 1.25x slower                                        |
| 2to3                      | 305 ms                                                       | 382 ms: 1.25x slower                                         |
| nqueens                   | 98.9 ms                                                      | 125 ms: 1.26x slower                                         |
| sqlglot_transpile         | 1.71 ms                                                      | 2.20 ms: 1.29x slower                                        |
| pprint_safe_repr          | 933 ms                                                       | 1.21 sec: 1.30x slower                                       |
| sympy_expand              | 457 ms                                                       | 594 ms: 1.30x slower                                         |
| sqlglot_optimize          | 62.6 ms                                                      | 82.2 ms: 1.31x slower                                        |
| pprint_pformat            | 1.93 sec                                                     | 2.55 sec: 1.32x slower                                       |
| dulwich_log               | 58.5 ms                                                      | 77.6 ms: 1.33x slower                                        |
| sympy_str                 | 265 ms                                                       | 357 ms: 1.34x slower                                         |
| genshi_xml                | 60.4 ms                                                      | 84.1 ms: 1.39x slower                                        |
| regex_compile             | 128 ms                                                       | 179 ms: 1.40x slower                                         |
| sympy_integrate           | 20.9 ms                                                      | 29.4 ms: 1.41x slower                                        |
| hexiom                    | 7.08 ms                                                      | 10.3 ms: 1.45x slower                                        |
| pylint                    | 337 ms                                                       | 494 ms: 1.47x slower                                         |
| sympy_sum                 | 144 ms                                                       | 215 ms: 1.49x slower                                         |
| create_gc_cycles          | 2.33 ms                                                      | 3.67 ms: 1.57x slower                                        |
| generators                | 37.1 ms                                                      | 59.0 ms: 1.59x slower                                        |
| bench_mp_pool             | 7.03 ms                                                      | 1.45 sec: 206.34x slower                                     |
| Geometric mean            | (ref)                                                        | 1.16x slower                                                 |

Benchmark hidden because not significant (14): async_tree_io, async_tree_cpu_io_mixed_tg, xml_etree_parse, regex_effbot, xml_etree_process, thrift, coroutines, sqlite_synth, unpickle_list, logging_silent, pidigits, pickle_dict, json, nbody
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (2) of results/bm-20241015-3.14.0a1-8cdaca8-JIT/bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8.json: sphinx, unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: 1.20x