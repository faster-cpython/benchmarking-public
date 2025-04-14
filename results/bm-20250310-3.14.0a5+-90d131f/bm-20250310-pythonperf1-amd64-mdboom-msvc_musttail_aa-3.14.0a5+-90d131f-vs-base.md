# Results vs. base

- fork: mdboom
- ref: msvc_musttail_aa
- machine: windows-amd64
- commit hash: 90d131f
- commit date: 2025-03-10
- overall geometric mean: 1.301x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.37x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250225-pythonperf1-amd64-python-f963239ff1f986742d4c-3.14.0a5+-f963239 | bm-20250310-pythonperf1-amd64-mdboom-msvc_musttail_aa-3.14.0a5+-90d131f |
|----------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 227 ms                                                                      | 309 ms: 1.36x slower                                                    |
| docutils       | 1.68 sec                                                                    | 2.31 sec: 1.37x slower                                                  |
| html5lib       | 40.8 ms                                                                     | 52.5 ms: 1.29x slower                                                   |
| sphinx         | 658 ms                                                                      | 933 ms: 1.42x slower                                                    |
| Geometric mean | (ref)                                                                       | 1.36x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250225-pythonperf1-amd64-python-f963239ff1f986742d4c-3.14.0a5+-f963239 | bm-20250310-pythonperf1-amd64-mdboom-msvc_musttail_aa-3.14.0a5+-90d131f |
|----------------------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| asyncio_websockets         | 318 ms                                                                      | 330 ms: 1.04x slower                                                    |
| async_tree_cpu_io_mixed_tg | 343 ms                                                                      | 444 ms: 1.29x slower                                                    |
| async_tree_cpu_io_mixed    | 339 ms                                                                      | 455 ms: 1.34x slower                                                    |
| async_tree_io              | 423 ms                                                                      | 570 ms: 1.35x slower                                                    |
| async_tree_none_tg         | 176 ms                                                                      | 243 ms: 1.38x slower                                                    |
| async_tree_memoization     | 224 ms                                                                      | 313 ms: 1.39x slower                                                    |
| async_tree_io_tg           | 410 ms                                                                      | 576 ms: 1.40x slower                                                    |
| async_tree_memoization_tg  | 216 ms                                                                      | 304 ms: 1.41x slower                                                    |
| async_tree_none            | 187 ms                                                                      | 267 ms: 1.43x slower                                                    |
| async_generators           | 226 ms                                                                      | 348 ms: 1.54x slower                                                    |
| coroutines                 | 13.5 ms                                                                     | 22.4 ms: 1.66x slower                                                   |
| Geometric mean             | (ref)                                                                       | 1.38x slower                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250225-pythonperf1-amd64-python-f963239ff1f986742d4c-3.14.0a5+-f963239 | bm-20250310-pythonperf1-amd64-mdboom-msvc_musttail_aa-3.14.0a5+-90d131f |
|----------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pidigits       | 152 ms                                                                      | 156 ms: 1.03x slower                                                    |
| nbody          | 74.1 ms                                                                     | 103 ms: 1.40x slower                                                    |
| float          | 47.8 ms                                                                     | 78.0 ms: 1.63x slower                                                   |
| Geometric mean | (ref)                                                                       | 1.33x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250225-pythonperf1-amd64-python-f963239ff1f986742d4c-3.14.0a5+-f963239 | bm-20250310-pythonperf1-amd64-mdboom-msvc_musttail_aa-3.14.0a5+-90d131f |
|----------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_dna      | 112 ms                                                                      | 123 ms: 1.10x slower                                                    |
| regex_v8       | 13.5 ms                                                                     | 17.5 ms: 1.29x slower                                                   |
| regex_effbot   | 1.42 ms                                                                     | 1.87 ms: 1.31x slower                                                   |
| regex_compile  | 88.2 ms                                                                     | 130 ms: 1.47x slower                                                    |
| Geometric mean | (ref)                                                                       | 1.29x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250225-pythonperf1-amd64-python-f963239ff1f986742d4c-3.14.0a5+-f963239 | bm-20250310-pythonperf1-amd64-mdboom-msvc_musttail_aa-3.14.0a5+-90d131f |
|----------------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse      | 91.2 ms                                                                     | 112 ms: 1.23x slower                                                    |
| json_dumps           | 7.05 ms                                                                     | 9.44 ms: 1.34x slower                                                   |
| tomli_loads          | 1.47 sec                                                                    | 2.07 sec: 1.41x slower                                                  |
| xml_etree_iterparse  | 63.7 ms                                                                     | 94.3 ms: 1.48x slower                                                   |
| pickle_pure_python   | 237 us                                                                      | 364 us: 1.54x slower                                                    |
| xml_etree_generate   | 58.7 ms                                                                     | 92.6 ms: 1.58x slower                                                   |
| json_loads           | 14.7 us                                                                     | 23.3 us: 1.58x slower                                                   |
| xml_etree_process    | 41.5 ms                                                                     | 66.9 ms: 1.61x slower                                                   |
| unpickle_pure_python | 155 us                                                                      | 284 us: 1.83x slower                                                    |
| Geometric mean       | (ref)                                                                       | 1.50x slower                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250225-pythonperf1-amd64-python-f963239ff1f986742d4c-3.14.0a5+-f963239 | bm-20250310-pythonperf1-amd64-mdboom-msvc_musttail_aa-3.14.0a5+-90d131f |
|------------------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 19.8 ms                                                                     | 22.0 ms: 1.11x slower                                                   |
| python_startup         | 26.1 ms                                                                     | 29.5 ms: 1.13x slower                                                   |
| Geometric mean         | (ref)                                                                       | 1.12x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250225-pythonperf1-amd64-python-f963239ff1f986742d4c-3.14.0a5+-f963239 | bm-20250310-pythonperf1-amd64-mdboom-msvc_musttail_aa-3.14.0a5+-90d131f |
|-----------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml      | 36.3 ms                                                                     | 50.4 ms: 1.39x slower                                                   |
| genshi_text     | 16.5 ms                                                                     | 23.9 ms: 1.45x slower                                                   |
| django_template | 25.1 ms                                                                     | 38.0 ms: 1.51x slower                                                   |
| mako            | 6.86 ms                                                                     | 12.1 ms: 1.76x slower                                                   |
| Geometric mean  | (ref)                                                                       | 1.52x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20250225-pythonperf1-amd64-python-f963239ff1f986742d4c-3.14.0a5+-f963239 | bm-20250310-pythonperf1-amd64-mdboom-msvc_musttail_aa-3.14.0a5+-90d131f |
|----------------------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pidigits                   | 152 ms                                                                      | 156 ms: 1.03x slower                                                    |
| asyncio_websockets         | 318 ms                                                                      | 330 ms: 1.04x slower                                                    |
| regex_dna                  | 112 ms                                                                      | 123 ms: 1.10x slower                                                    |
| python_startup_no_site     | 19.8 ms                                                                     | 22.0 ms: 1.11x slower                                                   |
| python_startup             | 26.1 ms                                                                     | 29.5 ms: 1.13x slower                                                   |
| create_gc_cycles           | 1.25 ms                                                                     | 1.42 ms: 1.13x slower                                                   |
| bench_mp_pool              | 88.7 ms                                                                     | 101 ms: 1.14x slower                                                    |
| mdp                        | 1.64 sec                                                                    | 1.89 sec: 1.15x slower                                                  |
| pathlib                    | 32.1 ms                                                                     | 37.5 ms: 1.17x slower                                                   |
| connected_components       | 329 ms                                                                      | 395 ms: 1.20x slower                                                    |
| dulwich_log                | 43.4 ms                                                                     | 52.4 ms: 1.21x slower                                                   |
| shortest_path              | 359 ms                                                                      | 437 ms: 1.22x slower                                                    |
| sqlite_synth               | 1.59 us                                                                     | 1.96 us: 1.23x slower                                                   |
| xml_etree_parse            | 91.2 ms                                                                     | 112 ms: 1.23x slower                                                    |
| k_core                     | 1.73 sec                                                                    | 2.18 sec: 1.26x slower                                                  |
| many_optionals             | 438 us                                                                      | 559 us: 1.28x slower                                                    |
| html5lib                   | 40.8 ms                                                                     | 52.5 ms: 1.29x slower                                                   |
| regex_v8                   | 13.5 ms                                                                     | 17.5 ms: 1.29x slower                                                   |
| meteor_contest             | 76.9 ms                                                                     | 99.5 ms: 1.29x slower                                                   |
| async_tree_cpu_io_mixed_tg | 343 ms                                                                      | 444 ms: 1.29x slower                                                    |
| json                       | 3.14 ms                                                                     | 4.07 ms: 1.30x slower                                                   |
| regex_effbot               | 1.42 ms                                                                     | 1.87 ms: 1.31x slower                                                   |
| subparsers                 | 16.1 ms                                                                     | 21.5 ms: 1.34x slower                                                   |
| pylint                     | 201 ms                                                                      | 269 ms: 1.34x slower                                                    |
| json_dumps                 | 7.05 ms                                                                     | 9.44 ms: 1.34x slower                                                   |
| telco                      | 4.89 ms                                                                     | 6.56 ms: 1.34x slower                                                   |
| async_tree_cpu_io_mixed    | 339 ms                                                                      | 455 ms: 1.34x slower                                                    |
| async_tree_io              | 423 ms                                                                      | 570 ms: 1.35x slower                                                    |
| 2to3                       | 227 ms                                                                      | 309 ms: 1.36x slower                                                    |
| coverage                   | 46.8 ms                                                                     | 63.7 ms: 1.36x slower                                                   |
| sympy_integrate            | 13.5 ms                                                                     | 18.4 ms: 1.36x slower                                                   |
| sympy_sum                  | 90.5 ms                                                                     | 123 ms: 1.36x slower                                                    |
| docutils                   | 1.68 sec                                                                    | 2.31 sec: 1.37x slower                                                  |
| pycparser                  | 738 ms                                                                      | 1.01 sec: 1.37x slower                                                  |
| async_tree_none_tg         | 176 ms                                                                      | 243 ms: 1.38x slower                                                    |
| sympy_expand               | 302 ms                                                                      | 419 ms: 1.39x slower                                                    |
| genshi_xml                 | 36.3 ms                                                                     | 50.4 ms: 1.39x slower                                                   |
| async_tree_memoization     | 224 ms                                                                      | 313 ms: 1.39x slower                                                    |
| nbody                      | 74.1 ms                                                                     | 103 ms: 1.40x slower                                                    |
| thrift                     | 507 us                                                                      | 710 us: 1.40x slower                                                    |
| sympy_str                  | 176 ms                                                                      | 247 ms: 1.40x slower                                                    |
| async_tree_io_tg           | 410 ms                                                                      | 576 ms: 1.40x slower                                                    |
| async_tree_memoization_tg  | 216 ms                                                                      | 304 ms: 1.41x slower                                                    |
| tomli_loads                | 1.47 sec                                                                    | 2.07 sec: 1.41x slower                                                  |
| logging_format             | 7.03 us                                                                     | 9.92 us: 1.41x slower                                                   |
| fannkuch                   | 296 ms                                                                      | 418 ms: 1.41x slower                                                    |
| sphinx                     | 658 ms                                                                      | 933 ms: 1.42x slower                                                    |
| logging_simple             | 6.53 us                                                                     | 9.30 us: 1.42x slower                                                   |
| async_tree_none            | 187 ms                                                                      | 267 ms: 1.43x slower                                                    |
| scimark_fft                | 192 ms                                                                      | 276 ms: 1.43x slower                                                    |
| genshi_text                | 16.5 ms                                                                     | 23.9 ms: 1.45x slower                                                   |
| typing_runtime_protocols   | 106 us                                                                      | 154 us: 1.45x slower                                                    |
| deepcopy                   | 190 us                                                                      | 278 us: 1.47x slower                                                    |
| regex_compile              | 88.2 ms                                                                     | 130 ms: 1.47x slower                                                    |
| pprint_pformat             | 1.13 sec                                                                    | 1.66 sec: 1.47x slower                                                  |
| deepcopy_reduce            | 1.94 us                                                                     | 2.86 us: 1.48x slower                                                   |
| bench_thread_pool          | 864 us                                                                      | 1.28 ms: 1.48x slower                                                   |
| pprint_safe_repr           | 558 ms                                                                      | 825 ms: 1.48x slower                                                    |
| xml_etree_iterparse        | 63.7 ms                                                                     | 94.3 ms: 1.48x slower                                                   |
| sqlglot_v2_normalize       | 73.6 ms                                                                     | 109 ms: 1.48x slower                                                    |
| bpe_tokeniser              | 2.96 sec                                                                    | 4.45 sec: 1.50x slower                                                  |
| sqlglot_v2_optimize        | 35.0 ms                                                                     | 52.8 ms: 1.51x slower                                                   |
| django_template            | 25.1 ms                                                                     | 38.0 ms: 1.51x slower                                                   |
| pyflate                    | 315 ms                                                                      | 477 ms: 1.51x slower                                                    |
| scimark_sor                | 91.0 ms                                                                     | 139 ms: 1.52x slower                                                    |
| nqueens                    | 63.6 ms                                                                     | 96.9 ms: 1.52x slower                                                   |
| sqlglot_v2_transpile       | 1.10 ms                                                                     | 1.69 ms: 1.53x slower                                                   |
| async_generators           | 226 ms                                                                      | 348 ms: 1.54x slower                                                    |
| pickle_pure_python         | 237 us                                                                      | 364 us: 1.54x slower                                                    |
| sqlglot_v2_parse           | 892 us                                                                      | 1.41 ms: 1.58x slower                                                   |
| xml_etree_generate         | 58.7 ms                                                                     | 92.6 ms: 1.58x slower                                                   |
| gc_traversal               | 2.06 ms                                                                     | 3.25 ms: 1.58x slower                                                   |
| json_loads                 | 14.7 us                                                                     | 23.3 us: 1.58x slower                                                   |
| go                         | 88.6 ms                                                                     | 140 ms: 1.58x slower                                                    |
| chaos                      | 43.6 ms                                                                     | 69.3 ms: 1.59x slower                                                   |
| crypto_pyaes               | 50.0 ms                                                                     | 80.1 ms: 1.60x slower                                                   |
| scimark_monte_carlo        | 47.1 ms                                                                     | 75.8 ms: 1.61x slower                                                   |
| xml_etree_process          | 41.5 ms                                                                     | 66.9 ms: 1.61x slower                                                   |
| deepcopy_memo              | 21.0 us                                                                     | 34.0 us: 1.62x slower                                                   |
| scimark_sparse_mat_mult    | 2.72 ms                                                                     | 4.43 ms: 1.63x slower                                                   |
| float                      | 47.8 ms                                                                     | 78.0 ms: 1.63x slower                                                   |
| raytrace                   | 191 ms                                                                      | 313 ms: 1.64x slower                                                    |
| spectral_norm              | 61.5 ms                                                                     | 102 ms: 1.65x slower                                                    |
| coroutines                 | 13.5 ms                                                                     | 22.4 ms: 1.66x slower                                                   |
| hexiom                     | 4.38 ms                                                                     | 7.44 ms: 1.70x slower                                                   |
| mako                       | 6.86 ms                                                                     | 12.1 ms: 1.76x slower                                                   |
| comprehensions             | 11.3 us                                                                     | 20.1 us: 1.78x slower                                                   |
| scimark_lu                 | 66.9 ms                                                                     | 119 ms: 1.79x slower                                                    |
| unpickle_pure_python       | 155 us                                                                      | 284 us: 1.83x slower                                                    |
| deltablue                  | 2.29 ms                                                                     | 4.22 ms: 1.84x slower                                                   |
| generators                 | 19.3 ms                                                                     | 35.6 ms: 1.84x slower                                                   |
| logging_silent             | 65.2 ns                                                                     | 124 ns: 1.91x slower                                                    |
| richards                   | 30.7 ms                                                                     | 59.0 ms: 1.92x slower                                                   |
| richards_super             | 35.1 ms                                                                     | 67.7 ms: 1.93x slower                                                   |
| Geometric mean             | (ref)                                                                       | 1.43x slower                                                            |

- Geometric mean (including insignificant results): 1.301x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.39x
- 95% likely to have a slowdown of 1.38x
- 99% likely to have a slowdown of 1.37x

# Memory
- memory change: unknown