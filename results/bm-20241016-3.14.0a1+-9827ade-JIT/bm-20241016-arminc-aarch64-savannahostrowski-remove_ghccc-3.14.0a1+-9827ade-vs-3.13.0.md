# Results vs. 3.13.0

- fork: savannahostrowski
- ref: remove_ghccc
- machine: linux-aarch64
- commit hash: 9827ade
- commit date: 2024-10-16
- overall geometric mean: 1.15x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower
- Memory change: 1.20x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-arminc-aarch64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 306 ms                                                   | 373 ms: 1.22x slower                                                        |
| docutils       | 2.91 sec                                                 | 3.66 sec: 1.26x slower                                                      |
| html5lib       | 64.3 ms                                                  | 71.4 ms: 1.11x slower                                                       |
| tornado_http   | 131 ms                                                   | 150 ms: 1.14x slower                                                        |
| Geometric mean | (ref)                                                    | 1.18x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-arminc-aarch64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|---------------------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg | 649 ms                                                   | 549 ms: 1.18x faster                                                        |
| async_tree_none           | 493 ms                                                   | 458 ms: 1.08x faster                                                        |
| async_tree_none_tg        | 467 ms                                                   | 448 ms: 1.04x faster                                                        |
| async_tree_memoization    | 626 ms                                                   | 605 ms: 1.03x faster                                                        |
| asyncio_websockets        | 656 ms                                                   | 660 ms: 1.01x slower                                                        |
| coroutines                | 28.2 ms                                                  | 28.8 ms: 1.02x slower                                                       |
| async_generators          | 496 ms                                                   | 508 ms: 1.02x slower                                                        |
| asyncio_tcp_ssl           | 2.18 sec                                                 | 2.26 sec: 1.04x slower                                                      |
| async_tree_io             | 1.11 sec                                                 | 1.19 sec: 1.08x slower                                                      |
| asyncio_tcp               | 568 ms                                                   | 618 ms: 1.09x slower                                                        |
| async_tree_io_tg          | 1.09 sec                                                 | 1.25 sec: 1.15x slower                                                      |
| Geometric mean            | (ref)                                                    | 1.01x slower                                                                |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-arminc-aarch64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 114 ms                                                   | 108 ms: 1.06x faster                                                        |
| float          | 94.4 ms                                                  | 91.9 ms: 1.03x faster                                                       |
| Geometric mean | (ref)                                                    | 1.03x faster                                                                |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-arminc-aarch64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 128 ms                                                   | 165 ms: 1.28x slower                                                        |
| Geometric mean | (ref)                                                    | 1.07x slower                                                                |

Benchmark hidden because not significant (3): regex_dna, regex_effbot, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-arminc-aarch64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|----------------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle             | 20.2 us                                                  | 19.2 us: 1.05x faster                                                       |
| xml_etree_generate   | 113 ms                                                   | 109 ms: 1.04x faster                                                        |
| pickle_list          | 5.34 us                                                  | 5.19 us: 1.03x faster                                                       |
| tomli_loads          | 2.53 sec                                                 | 2.49 sec: 1.02x faster                                                      |
| xml_etree_iterparse  | 147 ms                                                   | 150 ms: 1.02x slower                                                        |
| pickle               | 13.5 us                                                  | 13.8 us: 1.02x slower                                                       |
| unpickle_pure_python | 254 us                                                   | 264 us: 1.04x slower                                                        |
| pickle_pure_python   | 359 us                                                   | 377 us: 1.05x slower                                                        |
| json_dumps           | 13.4 ms                                                  | 14.3 ms: 1.07x slower                                                       |
| Geometric mean       | (ref)                                                    | 1.00x slower                                                                |

Benchmark hidden because not significant (5): xml_etree_process, pickle_dict, json_loads, unpickle_list, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-arminc-aarch64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup | 13.3 ms                                                  | 14.8 ms: 1.12x slower                                                       |
| Geometric mean | (ref)                                                    | 1.06x slower                                                                |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-arminc-aarch64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|-----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 13.3 ms                                                  | 12.8 ms: 1.04x faster                                                       |
| django_template | 42.3 ms                                                  | 49.0 ms: 1.16x slower                                                       |
| genshi_text     | 27.7 ms                                                  | 32.2 ms: 1.16x slower                                                       |
| genshi_xml      | 60.2 ms                                                  | 78.6 ms: 1.31x slower                                                       |
| Geometric mean  | (ref)                                                    | 1.14x slower                                                                |

All benchmarks:
===============

| Benchmark                 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-arminc-aarch64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|---------------------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy_memo             | 51.0 us                                                  | 38.1 us: 1.34x faster                                                       |
| deepcopy                  | 451 us                                                   | 366 us: 1.23x faster                                                        |
| async_tree_memoization_tg | 649 ms                                                   | 549 ms: 1.18x faster                                                        |
| deepcopy_reduce           | 4.07 us                                                  | 3.78 us: 1.08x faster                                                       |
| async_tree_none           | 493 ms                                                   | 458 ms: 1.08x faster                                                        |
| nbody                     | 114 ms                                                   | 108 ms: 1.06x faster                                                        |
| scimark_fft               | 447 ms                                                   | 424 ms: 1.06x faster                                                        |
| unpickle                  | 20.2 us                                                  | 19.2 us: 1.05x faster                                                       |
| mako                      | 13.3 ms                                                  | 12.8 ms: 1.04x faster                                                       |
| async_tree_none_tg        | 467 ms                                                   | 448 ms: 1.04x faster                                                        |
| xml_etree_generate        | 113 ms                                                   | 109 ms: 1.04x faster                                                        |
| bpe_tokeniser             | 5.90 sec                                                 | 5.69 sec: 1.04x faster                                                      |
| async_tree_memoization    | 626 ms                                                   | 605 ms: 1.03x faster                                                        |
| logging_silent            | 135 ns                                                   | 131 ns: 1.03x faster                                                        |
| pickle_list               | 5.34 us                                                  | 5.19 us: 1.03x faster                                                       |
| float                     | 94.4 ms                                                  | 91.9 ms: 1.03x faster                                                       |
| json                      | 5.61 ms                                                  | 5.48 ms: 1.02x faster                                                       |
| telco                     | 9.73 ms                                                  | 9.57 ms: 1.02x faster                                                       |
| tomli_loads               | 2.53 sec                                                 | 2.49 sec: 1.02x faster                                                      |
| asyncio_websockets        | 656 ms                                                   | 660 ms: 1.01x slower                                                        |
| coroutines                | 28.2 ms                                                  | 28.8 ms: 1.02x slower                                                       |
| xml_etree_iterparse       | 147 ms                                                   | 150 ms: 1.02x slower                                                        |
| pickle                    | 13.5 us                                                  | 13.8 us: 1.02x slower                                                       |
| async_generators          | 496 ms                                                   | 508 ms: 1.02x slower                                                        |
| fannkuch                  | 452 ms                                                   | 463 ms: 1.03x slower                                                        |
| logging_format            | 7.83 us                                                  | 8.04 us: 1.03x slower                                                       |
| mdp                       | 3.36 sec                                                 | 3.46 sec: 1.03x slower                                                      |
| scimark_monte_carlo       | 83.8 ms                                                  | 86.4 ms: 1.03x slower                                                       |
| thrift                    | 946 us                                                   | 977 us: 1.03x slower                                                        |
| spectral_norm             | 141 ms                                                   | 146 ms: 1.03x slower                                                        |
| asyncio_tcp_ssl           | 2.18 sec                                                 | 2.26 sec: 1.04x slower                                                      |
| unpickle_pure_python      | 254 us                                                   | 264 us: 1.04x slower                                                        |
| logging_simple            | 7.04 us                                                  | 7.35 us: 1.04x slower                                                       |
| pyflate                   | 556 ms                                                   | 581 ms: 1.05x slower                                                        |
| pickle_pure_python        | 359 us                                                   | 377 us: 1.05x slower                                                        |
| scimark_sparse_mat_mult   | 6.58 ms                                                  | 6.94 ms: 1.05x slower                                                       |
| meteor_contest            | 113 ms                                                   | 120 ms: 1.06x slower                                                        |
| scimark_lu                | 139 ms                                                   | 148 ms: 1.06x slower                                                        |
| json_dumps                | 13.4 ms                                                  | 14.3 ms: 1.07x slower                                                       |
| async_tree_io             | 1.11 sec                                                 | 1.19 sec: 1.08x slower                                                      |
| bench_thread_pool         | 1.28 ms                                                  | 1.37 ms: 1.08x slower                                                       |
| deltablue                 | 3.85 ms                                                  | 4.15 ms: 1.08x slower                                                       |
| asyncio_tcp               | 568 ms                                                   | 618 ms: 1.09x slower                                                        |
| typing_runtime_protocols  | 192 us                                                   | 210 us: 1.10x slower                                                        |
| go                        | 163 ms                                                   | 179 ms: 1.10x slower                                                        |
| html5lib                  | 64.3 ms                                                  | 71.4 ms: 1.11x slower                                                       |
| python_startup            | 13.3 ms                                                  | 14.8 ms: 1.12x slower                                                       |
| richards_super            | 60.3 ms                                                  | 67.9 ms: 1.13x slower                                                       |
| richards                  | 53.5 ms                                                  | 60.9 ms: 1.14x slower                                                       |
| tornado_http              | 131 ms                                                   | 150 ms: 1.14x slower                                                        |
| comprehensions            | 20.4 us                                                  | 23.3 us: 1.14x slower                                                       |
| chaos                     | 68.8 ms                                                  | 78.8 ms: 1.14x slower                                                       |
| pycparser                 | 1.26 sec                                                 | 1.45 sec: 1.15x slower                                                      |
| async_tree_io_tg          | 1.09 sec                                                 | 1.25 sec: 1.15x slower                                                      |
| sqlglot_parse             | 1.38 ms                                                  | 1.59 ms: 1.15x slower                                                       |
| django_template           | 42.3 ms                                                  | 49.0 ms: 1.16x slower                                                       |
| genshi_text               | 27.7 ms                                                  | 32.2 ms: 1.16x slower                                                       |
| raytrace                  | 298 ms                                                   | 350 ms: 1.17x slower                                                        |
| sqlglot_normalize         | 128 ms                                                   | 151 ms: 1.18x slower                                                        |
| nqueens                   | 98.7 ms                                                  | 117 ms: 1.19x slower                                                        |
| sqlglot_transpile         | 1.73 ms                                                  | 2.10 ms: 1.21x slower                                                       |
| 2to3                      | 306 ms                                                   | 373 ms: 1.22x slower                                                        |
| pprint_safe_repr          | 926 ms                                                   | 1.17 sec: 1.26x slower                                                      |
| docutils                  | 2.91 sec                                                 | 3.66 sec: 1.26x slower                                                      |
| sqlglot_optimize          | 62.4 ms                                                  | 79.3 ms: 1.27x slower                                                       |
| generators                | 37.8 ms                                                  | 48.3 ms: 1.28x slower                                                       |
| pprint_pformat            | 1.90 sec                                                 | 2.42 sec: 1.28x slower                                                      |
| sympy_expand              | 455 ms                                                   | 580 ms: 1.28x slower                                                        |
| regex_compile             | 128 ms                                                   | 165 ms: 1.28x slower                                                        |
| genshi_xml                | 60.2 ms                                                  | 78.6 ms: 1.31x slower                                                       |
| sympy_str                 | 264 ms                                                   | 347 ms: 1.31x slower                                                        |
| hexiom                    | 7.13 ms                                                  | 9.54 ms: 1.34x slower                                                       |
| sympy_integrate           | 21.0 ms                                                  | 29.1 ms: 1.39x slower                                                       |
| gc_traversal              | 4.53 ms                                                  | 6.34 ms: 1.40x slower                                                       |
| pylint                    | 343 ms                                                   | 486 ms: 1.42x slower                                                        |
| sympy_sum                 | 143 ms                                                   | 211 ms: 1.47x slower                                                        |
| create_gc_cycles          | 2.12 ms                                                  | 3.73 ms: 1.76x slower                                                       |
| unpack_sequence           | 57.2 ns                                                  | 129 ns: 2.26x slower                                                        |
| bench_mp_pool             | 7.30 ms                                                  | 2.16 sec: 296.11x slower                                                    |
| Geometric mean            | (ref)                                                    | 1.15x slower                                                                |

Benchmark hidden because not significant (17): xml_etree_process, sqlite_synth, pickle_dict, async_tree_cpu_io_mixed, regex_dna, coverage, json_loads, unpickle_list, scimark_sor, regex_effbot, crypto_pyaes, pidigits, pathlib, python_startup_no_site, regex_v8, async_tree_cpu_io_mixed_tg, xml_etree_parse
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (2) of results/bm-20241016-3.14.0a1+-9827ade-JIT/bm-20241016-arminc-aarch64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade.json: dulwich_log, sphinx

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 1.20x