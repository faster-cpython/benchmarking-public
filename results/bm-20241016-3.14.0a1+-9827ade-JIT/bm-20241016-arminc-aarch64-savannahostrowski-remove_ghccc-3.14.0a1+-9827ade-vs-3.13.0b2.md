# Results vs. 3.13.0b2

- fork: savannahostrowski
- ref: remove_ghccc
- machine: linux-aarch64
- commit hash: 9827ade
- commit date: 2024-10-16
- overall geometric mean: 1.14x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower
- Memory change: 1.20x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241016-arminc-aarch64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 305 ms                                                       | 373 ms: 1.22x slower                                                        |
| docutils       | 3.10 sec                                                     | 3.66 sec: 1.18x slower                                                      |
| html5lib       | 66.1 ms                                                      | 71.4 ms: 1.08x slower                                                       |
| tornado_http   | 128 ms                                                       | 150 ms: 1.17x slower                                                        |
| Geometric mean | (ref)                                                        | 1.16x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241016-arminc-aarch64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|---------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg | 604 ms                                                       | 549 ms: 1.10x faster                                                        |
| async_tree_none           | 492 ms                                                       | 458 ms: 1.07x faster                                                        |
| async_tree_memoization    | 645 ms                                                       | 605 ms: 1.07x faster                                                        |
| async_tree_none_tg        | 476 ms                                                       | 448 ms: 1.06x faster                                                        |
| async_tree_cpu_io_mixed   | 791 ms                                                       | 760 ms: 1.04x faster                                                        |
| async_tree_io_tg          | 1.27 sec                                                     | 1.25 sec: 1.02x faster                                                      |
| Geometric mean            | (ref)                                                        | 1.05x faster                                                                |

Benchmark hidden because not significant (2): async_tree_io, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241016-arminc-aarch64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 114 ms                                                       | 108 ms: 1.06x faster                                                        |
| float          | 91.4 ms                                                      | 91.9 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241016-arminc-aarch64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 259 ms                                                       | 245 ms: 1.06x faster                                                        |
| regex_effbot   | 4.98 ms                                                      | 4.89 ms: 1.02x faster                                                       |
| regex_v8       | 31.1 ms                                                      | 31.8 ms: 1.02x slower                                                       |
| regex_compile  | 128 ms                                                       | 165 ms: 1.29x slower                                                        |
| Geometric mean | (ref)                                                        | 1.05x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241016-arminc-aarch64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_generate   | 114 ms                                                       | 109 ms: 1.04x faster                                                        |
| xml_etree_process    | 80.8 ms                                                      | 78.0 ms: 1.04x faster                                                       |
| tomli_loads          | 2.57 sec                                                     | 2.49 sec: 1.03x faster                                                      |
| unpickle             | 19.8 us                                                      | 19.2 us: 1.03x faster                                                       |
| json_loads           | 32.1 us                                                      | 31.5 us: 1.02x faster                                                       |
| pickle_list          | 5.27 us                                                      | 5.19 us: 1.02x faster                                                       |
| xml_etree_iterparse  | 147 ms                                                       | 150 ms: 1.02x slower                                                        |
| unpickle_list        | 6.52 us                                                      | 6.66 us: 1.02x slower                                                       |
| pickle               | 13.4 us                                                      | 13.8 us: 1.03x slower                                                       |
| unpickle_pure_python | 251 us                                                       | 264 us: 1.05x slower                                                        |
| pickle_pure_python   | 359 us                                                       | 377 us: 1.05x slower                                                        |
| json_dumps           | 13.1 ms                                                      | 14.3 ms: 1.09x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.01x slower                                                                |

Benchmark hidden because not significant (2): xml_etree_parse, pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241016-arminc-aarch64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 8.60 ms                                                      | 8.83 ms: 1.03x slower                                                       |
| python_startup         | 13.0 ms                                                      | 14.8 ms: 1.14x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.08x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241016-arminc-aarch64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 13.2 ms                                                      | 12.8 ms: 1.03x faster                                                       |
| django_template | 42.3 ms                                                      | 49.0 ms: 1.16x slower                                                       |
| genshi_text     | 27.4 ms                                                      | 32.2 ms: 1.18x slower                                                       |
| genshi_xml      | 60.4 ms                                                      | 78.6 ms: 1.30x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.15x slower                                                                |

All benchmarks:
===============

| Benchmark                 | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241016-arminc-aarch64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|---------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy_memo             | 50.8 us                                                      | 38.1 us: 1.33x faster                                                       |
| deepcopy                  | 448 us                                                       | 366 us: 1.23x faster                                                        |
| async_tree_memoization_tg | 604 ms                                                       | 549 ms: 1.10x faster                                                        |
| async_tree_none           | 492 ms                                                       | 458 ms: 1.07x faster                                                        |
| deepcopy_reduce           | 4.04 us                                                      | 3.78 us: 1.07x faster                                                       |
| async_tree_memoization    | 645 ms                                                       | 605 ms: 1.07x faster                                                        |
| async_tree_none_tg        | 476 ms                                                       | 448 ms: 1.06x faster                                                        |
| nbody                     | 114 ms                                                       | 108 ms: 1.06x faster                                                        |
| regex_dna                 | 259 ms                                                       | 245 ms: 1.06x faster                                                        |
| scimark_fft               | 445 ms                                                       | 424 ms: 1.05x faster                                                        |
| telco                     | 10.0 ms                                                      | 9.57 ms: 1.05x faster                                                       |
| async_tree_cpu_io_mixed   | 791 ms                                                       | 760 ms: 1.04x faster                                                        |
| xml_etree_generate        | 114 ms                                                       | 109 ms: 1.04x faster                                                        |
| xml_etree_process         | 80.8 ms                                                      | 78.0 ms: 1.04x faster                                                       |
| tomli_loads               | 2.57 sec                                                     | 2.49 sec: 1.03x faster                                                      |
| mako                      | 13.2 ms                                                      | 12.8 ms: 1.03x faster                                                       |
| json                      | 5.64 ms                                                      | 5.48 ms: 1.03x faster                                                       |
| sqlite_synth              | 3.90 us                                                      | 3.80 us: 1.03x faster                                                       |
| unpickle                  | 19.8 us                                                      | 19.2 us: 1.03x faster                                                       |
| bpe_tokeniser             | 5.83 sec                                                     | 5.69 sec: 1.02x faster                                                      |
| json_loads                | 32.1 us                                                      | 31.5 us: 1.02x faster                                                       |
| logging_silent            | 133 ns                                                       | 131 ns: 1.02x faster                                                        |
| regex_effbot              | 4.98 ms                                                      | 4.89 ms: 1.02x faster                                                       |
| pickle_list               | 5.27 us                                                      | 5.19 us: 1.02x faster                                                       |
| async_tree_io_tg          | 1.27 sec                                                     | 1.25 sec: 1.02x faster                                                      |
| float                     | 91.4 ms                                                      | 91.9 ms: 1.01x slower                                                       |
| crypto_pyaes              | 82.0 ms                                                      | 83.0 ms: 1.01x slower                                                       |
| xml_etree_iterparse       | 147 ms                                                       | 150 ms: 1.02x slower                                                        |
| logging_simple            | 7.21 us                                                      | 7.35 us: 1.02x slower                                                       |
| asyncio_tcp_ssl           | 2.21 sec                                                     | 2.26 sec: 1.02x slower                                                      |
| unpickle_list             | 6.52 us                                                      | 6.66 us: 1.02x slower                                                       |
| regex_v8                  | 31.1 ms                                                      | 31.8 ms: 1.02x slower                                                       |
| fannkuch                  | 451 ms                                                       | 463 ms: 1.03x slower                                                        |
| python_startup_no_site    | 8.60 ms                                                      | 8.83 ms: 1.03x slower                                                       |
| logging_format            | 7.82 us                                                      | 8.04 us: 1.03x slower                                                       |
| pickle                    | 13.4 us                                                      | 13.8 us: 1.03x slower                                                       |
| spectral_norm             | 141 ms                                                       | 146 ms: 1.03x slower                                                        |
| mdp                       | 3.33 sec                                                     | 3.46 sec: 1.04x slower                                                      |
| async_generators          | 488 ms                                                       | 508 ms: 1.04x slower                                                        |
| pyflate                   | 557 ms                                                       | 581 ms: 1.04x slower                                                        |
| scimark_lu                | 141 ms                                                       | 148 ms: 1.05x slower                                                        |
| scimark_monte_carlo       | 82.3 ms                                                      | 86.4 ms: 1.05x slower                                                       |
| unpickle_pure_python      | 251 us                                                       | 264 us: 1.05x slower                                                        |
| pickle_pure_python        | 359 us                                                       | 377 us: 1.05x slower                                                        |
| meteor_contest            | 113 ms                                                       | 120 ms: 1.06x slower                                                        |
| asyncio_tcp               | 584 ms                                                       | 618 ms: 1.06x slower                                                        |
| scimark_sparse_mat_mult   | 6.55 ms                                                      | 6.94 ms: 1.06x slower                                                       |
| deltablue                 | 3.88 ms                                                      | 4.15 ms: 1.07x slower                                                       |
| html5lib                  | 66.1 ms                                                      | 71.4 ms: 1.08x slower                                                       |
| typing_runtime_protocols  | 193 us                                                       | 210 us: 1.09x slower                                                        |
| richards                  | 55.9 ms                                                      | 60.9 ms: 1.09x slower                                                       |
| richards_super            | 62.3 ms                                                      | 67.9 ms: 1.09x slower                                                       |
| bench_thread_pool         | 1.26 ms                                                      | 1.37 ms: 1.09x slower                                                       |
| json_dumps                | 13.1 ms                                                      | 14.3 ms: 1.09x slower                                                       |
| go                        | 161 ms                                                       | 179 ms: 1.11x slower                                                        |
| sqlglot_parse             | 1.42 ms                                                      | 1.59 ms: 1.12x slower                                                       |
| comprehensions            | 20.5 us                                                      | 23.3 us: 1.14x slower                                                       |
| python_startup            | 13.0 ms                                                      | 14.8 ms: 1.14x slower                                                       |
| chaos                     | 68.3 ms                                                      | 78.8 ms: 1.15x slower                                                       |
| django_template           | 42.3 ms                                                      | 49.0 ms: 1.16x slower                                                       |
| sqlglot_normalize         | 129 ms                                                       | 151 ms: 1.17x slower                                                        |
| tornado_http              | 128 ms                                                       | 150 ms: 1.17x slower                                                        |
| genshi_text               | 27.4 ms                                                      | 32.2 ms: 1.18x slower                                                       |
| raytrace                  | 297 ms                                                       | 350 ms: 1.18x slower                                                        |
| docutils                  | 3.10 sec                                                     | 3.66 sec: 1.18x slower                                                      |
| nqueens                   | 98.9 ms                                                      | 117 ms: 1.19x slower                                                        |
| pycparser                 | 1.22 sec                                                     | 1.45 sec: 1.19x slower                                                      |
| 2to3                      | 305 ms                                                       | 373 ms: 1.22x slower                                                        |
| gc_traversal              | 5.17 ms                                                      | 6.34 ms: 1.22x slower                                                       |
| sqlglot_transpile         | 1.71 ms                                                      | 2.10 ms: 1.23x slower                                                       |
| pprint_safe_repr          | 933 ms                                                       | 1.17 sec: 1.25x slower                                                      |
| pprint_pformat            | 1.93 sec                                                     | 2.42 sec: 1.25x slower                                                      |
| sqlglot_optimize          | 62.6 ms                                                      | 79.3 ms: 1.27x slower                                                       |
| sympy_expand              | 457 ms                                                       | 580 ms: 1.27x slower                                                        |
| regex_compile             | 128 ms                                                       | 165 ms: 1.29x slower                                                        |
| generators                | 37.1 ms                                                      | 48.3 ms: 1.30x slower                                                       |
| genshi_xml                | 60.4 ms                                                      | 78.6 ms: 1.30x slower                                                       |
| sympy_str                 | 265 ms                                                       | 347 ms: 1.31x slower                                                        |
| hexiom                    | 7.08 ms                                                      | 9.54 ms: 1.35x slower                                                       |
| dulwich_log               | 58.5 ms                                                      | 80.8 ms: 1.38x slower                                                       |
| sympy_integrate           | 20.9 ms                                                      | 29.1 ms: 1.39x slower                                                       |
| pylint                    | 337 ms                                                       | 486 ms: 1.44x slower                                                        |
| sympy_sum                 | 144 ms                                                       | 211 ms: 1.47x slower                                                        |
| create_gc_cycles          | 2.33 ms                                                      | 3.73 ms: 1.60x slower                                                       |
| bench_mp_pool             | 7.03 ms                                                      | 2.16 sec: 307.45x slower                                                    |
| Geometric mean            | (ref)                                                        | 1.14x slower                                                                |

Benchmark hidden because not significant (11): async_tree_io, async_tree_cpu_io_mixed_tg, coroutines, pathlib, xml_etree_parse, scimark_sor, coverage, pickle_dict, pidigits, asyncio_websockets, thrift
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (2) of results/bm-20241016-3.14.0a1+-9827ade-JIT/bm-20241016-arminc-aarch64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade.json: sphinx, unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 1.20x