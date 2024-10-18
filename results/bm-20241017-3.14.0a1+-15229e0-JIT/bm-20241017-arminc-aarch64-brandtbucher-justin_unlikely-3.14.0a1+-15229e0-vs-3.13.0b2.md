# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: justin_unlikely
- machine: linux-aarch64
- commit hash: 15229e0
- commit date: 2024-10-17
- overall geometric mean: 1.17x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: 1.20x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241017-arminc-aarch64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 305 ms                                                       | 385 ms: 1.26x slower                                                      |
| docutils       | 3.10 sec                                                     | 3.62 sec: 1.17x slower                                                    |
| html5lib       | 66.1 ms                                                      | 71.1 ms: 1.08x slower                                                     |
| tornado_http   | 128 ms                                                       | 146 ms: 1.14x slower                                                      |
| Geometric mean | (ref)                                                        | 1.16x slower                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241017-arminc-aarch64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|---------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization_tg | 604 ms                                                       | 539 ms: 1.12x faster                                                      |
| async_tree_none           | 492 ms                                                       | 458 ms: 1.07x faster                                                      |
| async_tree_memoization    | 645 ms                                                       | 603 ms: 1.07x faster                                                      |
| async_tree_none_tg        | 476 ms                                                       | 448 ms: 1.06x faster                                                      |
| async_tree_io             | 1.22 sec                                                     | 1.16 sec: 1.06x faster                                                    |
| async_tree_cpu_io_mixed   | 791 ms                                                       | 755 ms: 1.05x faster                                                      |
| async_tree_io_tg          | 1.27 sec                                                     | 1.25 sec: 1.02x faster                                                    |
| Geometric mean            | (ref)                                                        | 1.06x faster                                                              |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241017-arminc-aarch64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 114 ms                                                       | 119 ms: 1.04x slower                                                      |
| float          | 91.4 ms                                                      | 97.2 ms: 1.06x slower                                                     |
| Geometric mean | (ref)                                                        | 1.04x slower                                                              |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241017-arminc-aarch64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_dna      | 259 ms                                                       | 245 ms: 1.05x faster                                                      |
| regex_effbot   | 4.98 ms                                                      | 4.88 ms: 1.02x faster                                                     |
| regex_v8       | 31.1 ms                                                      | 31.4 ms: 1.01x slower                                                     |
| regex_compile  | 128 ms                                                       | 183 ms: 1.43x slower                                                      |
| Geometric mean | (ref)                                                        | 1.08x slower                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241017-arminc-aarch64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| unpickle             | 19.8 us                                                      | 19.0 us: 1.04x faster                                                     |
| xml_etree_parse      | 191 ms                                                       | 185 ms: 1.03x faster                                                      |
| json_loads           | 32.1 us                                                      | 31.7 us: 1.01x faster                                                     |
| pickle_list          | 5.27 us                                                      | 5.22 us: 1.01x faster                                                     |
| pickle               | 13.4 us                                                      | 13.7 us: 1.03x slower                                                     |
| xml_etree_iterparse  | 147 ms                                                       | 151 ms: 1.03x slower                                                      |
| tomli_loads          | 2.57 sec                                                     | 2.65 sec: 1.03x slower                                                    |
| unpickle_pure_python | 251 us                                                       | 266 us: 1.06x slower                                                      |
| pickle_pure_python   | 359 us                                                       | 387 us: 1.08x slower                                                      |
| json_dumps           | 13.1 ms                                                      | 14.3 ms: 1.09x slower                                                     |
| Geometric mean       | (ref)                                                        | 1.01x slower                                                              |

Benchmark hidden because not significant (4): xml_etree_generate, unpickle_list, xml_etree_process, pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241017-arminc-aarch64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 8.60 ms                                                      | 8.73 ms: 1.01x slower                                                     |
| python_startup         | 13.0 ms                                                      | 14.6 ms: 1.13x slower                                                     |
| Geometric mean         | (ref)                                                        | 1.07x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241017-arminc-aarch64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|-----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 13.2 ms                                                      | 13.4 ms: 1.02x slower                                                     |
| django_template | 42.3 ms                                                      | 50.9 ms: 1.20x slower                                                     |
| genshi_text     | 27.4 ms                                                      | 34.2 ms: 1.25x slower                                                     |
| genshi_xml      | 60.4 ms                                                      | 84.6 ms: 1.40x slower                                                     |
| Geometric mean  | (ref)                                                        | 1.21x slower                                                              |

All benchmarks:
===============

| Benchmark                 | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241017-arminc-aarch64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|---------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| deepcopy_memo             | 50.8 us                                                      | 39.3 us: 1.29x faster                                                     |
| deepcopy                  | 448 us                                                       | 379 us: 1.18x faster                                                      |
| async_tree_memoization_tg | 604 ms                                                       | 539 ms: 1.12x faster                                                      |
| async_tree_none           | 492 ms                                                       | 458 ms: 1.07x faster                                                      |
| async_tree_memoization    | 645 ms                                                       | 603 ms: 1.07x faster                                                      |
| async_tree_none_tg        | 476 ms                                                       | 448 ms: 1.06x faster                                                      |
| async_tree_io             | 1.22 sec                                                     | 1.16 sec: 1.06x faster                                                    |
| pathlib                   | 22.8 ms                                                      | 21.5 ms: 1.06x faster                                                     |
| regex_dna                 | 259 ms                                                       | 245 ms: 1.05x faster                                                      |
| async_tree_cpu_io_mixed   | 791 ms                                                       | 755 ms: 1.05x faster                                                      |
| unpickle                  | 19.8 us                                                      | 19.0 us: 1.04x faster                                                     |
| xml_etree_parse           | 191 ms                                                       | 185 ms: 1.03x faster                                                      |
| async_tree_io_tg          | 1.27 sec                                                     | 1.25 sec: 1.02x faster                                                    |
| regex_effbot              | 4.98 ms                                                      | 4.88 ms: 1.02x faster                                                     |
| scimark_sor               | 159 ms                                                       | 157 ms: 1.02x faster                                                      |
| coroutines                | 29.0 ms                                                      | 28.6 ms: 1.01x faster                                                     |
| deepcopy_reduce           | 4.04 us                                                      | 3.99 us: 1.01x faster                                                     |
| json_loads                | 32.1 us                                                      | 31.7 us: 1.01x faster                                                     |
| pickle_list               | 5.27 us                                                      | 5.22 us: 1.01x faster                                                     |
| asyncio_websockets        | 657 ms                                                       | 662 ms: 1.01x slower                                                      |
| regex_v8                  | 31.1 ms                                                      | 31.4 ms: 1.01x slower                                                     |
| python_startup_no_site    | 8.60 ms                                                      | 8.73 ms: 1.01x slower                                                     |
| mako                      | 13.2 ms                                                      | 13.4 ms: 1.02x slower                                                     |
| json                      | 5.64 ms                                                      | 5.74 ms: 1.02x slower                                                     |
| thrift                    | 962 us                                                       | 979 us: 1.02x slower                                                      |
| pickle                    | 13.4 us                                                      | 13.7 us: 1.03x slower                                                     |
| logging_simple            | 7.21 us                                                      | 7.41 us: 1.03x slower                                                     |
| logging_format            | 7.82 us                                                      | 8.06 us: 1.03x slower                                                     |
| xml_etree_iterparse       | 147 ms                                                       | 151 ms: 1.03x slower                                                      |
| tomli_loads               | 2.57 sec                                                     | 2.65 sec: 1.03x slower                                                    |
| asyncio_tcp_ssl           | 2.21 sec                                                     | 2.29 sec: 1.03x slower                                                    |
| bpe_tokeniser             | 5.83 sec                                                     | 6.04 sec: 1.04x slower                                                    |
| scimark_fft               | 445 ms                                                       | 463 ms: 1.04x slower                                                      |
| nbody                     | 114 ms                                                       | 119 ms: 1.04x slower                                                      |
| scimark_lu                | 141 ms                                                       | 148 ms: 1.05x slower                                                      |
| mdp                       | 3.33 sec                                                     | 3.49 sec: 1.05x slower                                                    |
| async_generators          | 488 ms                                                       | 513 ms: 1.05x slower                                                      |
| unpickle_pure_python      | 251 us                                                       | 266 us: 1.06x slower                                                      |
| float                     | 91.4 ms                                                      | 97.2 ms: 1.06x slower                                                     |
| html5lib                  | 66.1 ms                                                      | 71.1 ms: 1.08x slower                                                     |
| pickle_pure_python        | 359 us                                                       | 387 us: 1.08x slower                                                      |
| json_dumps                | 13.1 ms                                                      | 14.3 ms: 1.09x slower                                                     |
| bench_thread_pool         | 1.26 ms                                                      | 1.37 ms: 1.09x slower                                                     |
| meteor_contest            | 113 ms                                                       | 124 ms: 1.09x slower                                                      |
| scimark_sparse_mat_mult   | 6.55 ms                                                      | 7.16 ms: 1.09x slower                                                     |
| asyncio_tcp               | 584 ms                                                       | 639 ms: 1.10x slower                                                      |
| spectral_norm             | 141 ms                                                       | 155 ms: 1.10x slower                                                      |
| scimark_monte_carlo       | 82.3 ms                                                      | 90.7 ms: 1.10x slower                                                     |
| crypto_pyaes              | 82.0 ms                                                      | 90.7 ms: 1.11x slower                                                     |
| fannkuch                  | 451 ms                                                       | 508 ms: 1.12x slower                                                      |
| python_startup            | 13.0 ms                                                      | 14.6 ms: 1.13x slower                                                     |
| typing_runtime_protocols  | 193 us                                                       | 218 us: 1.13x slower                                                      |
| richards                  | 55.9 ms                                                      | 63.8 ms: 1.14x slower                                                     |
| tornado_http              | 128 ms                                                       | 146 ms: 1.14x slower                                                      |
| richards_super            | 62.3 ms                                                      | 71.7 ms: 1.15x slower                                                     |
| go                        | 161 ms                                                       | 185 ms: 1.15x slower                                                      |
| pyflate                   | 557 ms                                                       | 643 ms: 1.15x slower                                                      |
| docutils                  | 3.10 sec                                                     | 3.62 sec: 1.17x slower                                                    |
| raytrace                  | 297 ms                                                       | 352 ms: 1.19x slower                                                      |
| deltablue                 | 3.88 ms                                                      | 4.63 ms: 1.19x slower                                                     |
| django_template           | 42.3 ms                                                      | 50.9 ms: 1.20x slower                                                     |
| gc_traversal              | 5.17 ms                                                      | 6.23 ms: 1.20x slower                                                     |
| sqlglot_parse             | 1.42 ms                                                      | 1.71 ms: 1.20x slower                                                     |
| sqlglot_normalize         | 129 ms                                                       | 156 ms: 1.21x slower                                                      |
| comprehensions            | 20.5 us                                                      | 24.9 us: 1.21x slower                                                     |
| pycparser                 | 1.22 sec                                                     | 1.52 sec: 1.24x slower                                                    |
| nqueens                   | 98.9 ms                                                      | 123 ms: 1.24x slower                                                      |
| genshi_text               | 27.4 ms                                                      | 34.2 ms: 1.25x slower                                                     |
| 2to3                      | 305 ms                                                       | 385 ms: 1.26x slower                                                      |
| chaos                     | 68.3 ms                                                      | 87.2 ms: 1.28x slower                                                     |
| sympy_expand              | 457 ms                                                       | 592 ms: 1.29x slower                                                      |
| sqlglot_transpile         | 1.71 ms                                                      | 2.24 ms: 1.31x slower                                                     |
| sqlglot_optimize          | 62.6 ms                                                      | 82.9 ms: 1.32x slower                                                     |
| dulwich_log               | 58.5 ms                                                      | 77.4 ms: 1.32x slower                                                     |
| pprint_safe_repr          | 933 ms                                                       | 1.24 sec: 1.33x slower                                                    |
| pprint_pformat            | 1.93 sec                                                     | 2.61 sec: 1.35x slower                                                    |
| sympy_str                 | 265 ms                                                       | 363 ms: 1.37x slower                                                      |
| genshi_xml                | 60.4 ms                                                      | 84.6 ms: 1.40x slower                                                     |
| sympy_integrate           | 20.9 ms                                                      | 29.3 ms: 1.40x slower                                                     |
| regex_compile             | 128 ms                                                       | 183 ms: 1.43x slower                                                      |
| hexiom                    | 7.08 ms                                                      | 10.2 ms: 1.44x slower                                                     |
| pylint                    | 337 ms                                                       | 493 ms: 1.46x slower                                                      |
| sympy_sum                 | 144 ms                                                       | 216 ms: 1.51x slower                                                      |
| create_gc_cycles          | 2.33 ms                                                      | 3.68 ms: 1.58x slower                                                     |
| generators                | 37.1 ms                                                      | 58.9 ms: 1.59x slower                                                     |
| bench_mp_pool             | 7.03 ms                                                      | 1.92 sec: 273.60x slower                                                  |
| Geometric mean            | (ref)                                                        | 1.17x slower                                                              |

Benchmark hidden because not significant (10): async_tree_cpu_io_mixed_tg, telco, xml_etree_generate, unpickle_list, xml_etree_process, sqlite_synth, pidigits, pickle_dict, coverage, logging_silent
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (2) of results/bm-20241017-3.14.0a1+-15229e0-JIT/bm-20241017-arminc-aarch64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0.json: sphinx, unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: 1.20x