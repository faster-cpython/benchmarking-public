# Results vs. 3.12.0

- fork: mdboom
- ref: msvc_musttail_aa
- machine: windows-amd64
- commit hash: 90d131f
- commit date: 2025-03-10
- overall geometric mean: 1.290x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.36x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250310-pythonperf1-amd64-mdboom-msvc_musttail_aa-3.14.0a5+-90d131f |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 309 ms: 1.42x slower                                                    |
| docutils       | 1.66 sec                                                    | 2.31 sec: 1.39x slower                                                  |
| Geometric mean | (ref)                                                       | 1.40x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250310-pythonperf1-amd64-mdboom-msvc_musttail_aa-3.14.0a5+-90d131f |
|----------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 576 ms: 1.34x faster                                                    |
| async_tree_io              | 731 ms                                                      | 570 ms: 1.28x faster                                                    |
| async_tree_memoization_tg  | 367 ms                                                      | 304 ms: 1.21x faster                                                    |
| async_tree_none_tg         | 285 ms                                                      | 243 ms: 1.17x faster                                                    |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 444 ms: 1.13x faster                                                    |
| async_tree_none            | 291 ms                                                      | 267 ms: 1.09x faster                                                    |
| async_tree_memoization     | 339 ms                                                      | 313 ms: 1.08x faster                                                    |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 455 ms: 1.07x faster                                                    |
| Geometric mean             | (ref)                                                       | 1.17x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250310-pythonperf1-amd64-mdboom-msvc_musttail_aa-3.14.0a5+-90d131f |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pidigits       | 152 ms                                                      | 156 ms: 1.03x slower                                                    |
| float          | 56.8 ms                                                     | 78.0 ms: 1.37x slower                                                   |
| nbody          | 71.9 ms                                                     | 103 ms: 1.44x slower                                                    |
| Geometric mean | (ref)                                                       | 1.27x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250310-pythonperf1-amd64-mdboom-msvc_musttail_aa-3.14.0a5+-90d131f |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 123 ms: 1.03x faster                                                    |
| regex_effbot   | 1.62 ms                                                     | 1.87 ms: 1.15x slower                                                   |
| regex_v8       | 14.2 ms                                                     | 17.5 ms: 1.23x slower                                                   |
| regex_compile  | 87.5 ms                                                     | 130 ms: 1.48x slower                                                    |
| Geometric mean | (ref)                                                       | 1.20x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250310-pythonperf1-amd64-mdboom-msvc_musttail_aa-3.14.0a5+-90d131f |
|----------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse      | 93.0 ms                                                     | 112 ms: 1.21x slower                                                    |
| xml_etree_iterparse  | 65.2 ms                                                     | 94.3 ms: 1.45x slower                                                   |
| tomli_loads          | 1.37 sec                                                    | 2.07 sec: 1.51x slower                                                  |
| xml_etree_generate   | 55.8 ms                                                     | 92.6 ms: 1.66x slower                                                   |
| json_dumps           | 5.70 ms                                                     | 9.44 ms: 1.66x slower                                                   |
| json_loads           | 13.9 us                                                     | 23.3 us: 1.68x slower                                                   |
| xml_etree_process    | 37.7 ms                                                     | 66.9 ms: 1.77x slower                                                   |
| pickle_pure_python   | 195 us                                                      | 364 us: 1.86x slower                                                    |
| unpickle_pure_python | 133 us                                                      | 284 us: 2.13x slower                                                    |
| Geometric mean       | (ref)                                                       | 1.64x slower                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250310-pythonperf1-amd64-mdboom-msvc_musttail_aa-3.14.0a5+-90d131f |
|------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 22.0 ms: 1.36x slower                                                   |
| python_startup         | 19.5 ms                                                     | 29.5 ms: 1.51x slower                                                   |
| Geometric mean         | (ref)                                                       | 1.43x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250310-pythonperf1-amd64-mdboom-msvc_musttail_aa-3.14.0a5+-90d131f |
|-----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| django_template | 22.9 ms                                                     | 38.0 ms: 1.66x slower                                                   |
| mako            | 7.09 ms                                                     | 12.1 ms: 1.70x slower                                                   |
| Geometric mean  | (ref)                                                       | 1.68x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250310-pythonperf1-amd64-mdboom-msvc_musttail_aa-3.14.0a5+-90d131f |
|----------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 37.5 ms: 2.15x faster                                                   |
| async_tree_io_tg           | 771 ms                                                      | 576 ms: 1.34x faster                                                    |
| async_tree_io              | 731 ms                                                      | 570 ms: 1.28x faster                                                    |
| async_tree_memoization_tg  | 367 ms                                                      | 304 ms: 1.21x faster                                                    |
| async_tree_none_tg         | 285 ms                                                      | 243 ms: 1.17x faster                                                    |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 444 ms: 1.13x faster                                                    |
| async_tree_none            | 291 ms                                                      | 267 ms: 1.09x faster                                                    |
| async_tree_memoization     | 339 ms                                                      | 313 ms: 1.08x faster                                                    |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 455 ms: 1.07x faster                                                    |
| regex_dna                  | 126 ms                                                      | 123 ms: 1.03x faster                                                    |
| pidigits                   | 152 ms                                                      | 156 ms: 1.03x slower                                                    |
| sqlite_synth               | 1.76 us                                                     | 1.96 us: 1.11x slower                                                   |
| regex_effbot               | 1.62 ms                                                     | 1.87 ms: 1.15x slower                                                   |
| deepcopy                   | 238 us                                                      | 278 us: 1.17x slower                                                    |
| dulwich_log                | 44.3 ms                                                     | 52.4 ms: 1.18x slower                                                   |
| xml_etree_parse            | 93.0 ms                                                     | 112 ms: 1.21x slower                                                    |
| regex_v8                   | 14.2 ms                                                     | 17.5 ms: 1.23x slower                                                   |
| meteor_contest             | 74.6 ms                                                     | 99.5 ms: 1.33x slower                                                   |
| json                       | 3.05 ms                                                     | 4.07 ms: 1.34x slower                                                   |
| sympy_sum                  | 91.5 ms                                                     | 123 ms: 1.35x slower                                                    |
| python_startup_no_site     | 16.2 ms                                                     | 22.0 ms: 1.36x slower                                                   |
| deepcopy_reduce            | 2.09 us                                                     | 2.86 us: 1.37x slower                                                   |
| float                      | 56.8 ms                                                     | 78.0 ms: 1.37x slower                                                   |
| mdp                        | 1.37 sec                                                    | 1.89 sec: 1.38x slower                                                  |
| docutils                   | 1.66 sec                                                    | 2.31 sec: 1.39x slower                                                  |
| sympy_str                  | 175 ms                                                      | 247 ms: 1.41x slower                                                    |
| 2to3                       | 218 ms                                                      | 309 ms: 1.42x slower                                                    |
| sympy_integrate            | 13.0 ms                                                     | 18.4 ms: 1.42x slower                                                   |
| comprehensions             | 14.1 us                                                     | 20.1 us: 1.42x slower                                                   |
| deepcopy_memo              | 23.7 us                                                     | 34.0 us: 1.44x slower                                                   |
| nbody                      | 71.9 ms                                                     | 103 ms: 1.44x slower                                                    |
| xml_etree_iterparse        | 65.2 ms                                                     | 94.3 ms: 1.45x slower                                                   |
| pycparser                  | 699 ms                                                      | 1.01 sec: 1.45x slower                                                  |
| async_generators           | 239 ms                                                      | 348 ms: 1.45x slower                                                    |
| bench_mp_pool              | 69.2 ms                                                     | 101 ms: 1.46x slower                                                    |
| sympy_expand               | 284 ms                                                      | 419 ms: 1.48x slower                                                    |
| logging_format             | 6.72 us                                                     | 9.92 us: 1.48x slower                                                   |
| logging_simple             | 6.28 us                                                     | 9.30 us: 1.48x slower                                                   |
| regex_compile              | 87.5 ms                                                     | 130 ms: 1.48x slower                                                    |
| bench_thread_pool          | 857 us                                                      | 1.28 ms: 1.49x slower                                                   |
| scimark_fft                | 184 ms                                                      | 276 ms: 1.50x slower                                                    |
| tomli_loads                | 1.37 sec                                                    | 2.07 sec: 1.51x slower                                                  |
| python_startup             | 19.5 ms                                                     | 29.5 ms: 1.51x slower                                                   |
| spectral_norm              | 66.9 ms                                                     | 102 ms: 1.52x slower                                                    |
| go                         | 91.6 ms                                                     | 140 ms: 1.53x slower                                                    |
| nqueens                    | 62.8 ms                                                     | 96.9 ms: 1.54x slower                                                   |
| coverage                   | 40.8 ms                                                     | 63.7 ms: 1.56x slower                                                   |
| coroutines                 | 14.3 ms                                                     | 22.4 ms: 1.57x slower                                                   |
| generators                 | 22.5 ms                                                     | 35.6 ms: 1.58x slower                                                   |
| pprint_pformat             | 1.05 sec                                                    | 1.66 sec: 1.59x slower                                                  |
| telco                      | 4.13 ms                                                     | 6.56 ms: 1.59x slower                                                   |
| chaos                      | 43.3 ms                                                     | 69.3 ms: 1.60x slower                                                   |
| pprint_safe_repr           | 513 ms                                                      | 825 ms: 1.61x slower                                                    |
| typing_runtime_protocols   | 95.1 us                                                     | 154 us: 1.62x slower                                                    |
| pyflate                    | 295 ms                                                      | 477 ms: 1.62x slower                                                    |
| raytrace                   | 192 ms                                                      | 313 ms: 1.62x slower                                                    |
| crypto_pyaes               | 48.5 ms                                                     | 80.1 ms: 1.65x slower                                                   |
| django_template            | 22.9 ms                                                     | 38.0 ms: 1.66x slower                                                   |
| xml_etree_generate         | 55.8 ms                                                     | 92.6 ms: 1.66x slower                                                   |
| json_dumps                 | 5.70 ms                                                     | 9.44 ms: 1.66x slower                                                   |
| json_loads                 | 13.9 us                                                     | 23.3 us: 1.68x slower                                                   |
| fannkuch                   | 247 ms                                                      | 418 ms: 1.69x slower                                                    |
| mako                       | 7.09 ms                                                     | 12.1 ms: 1.70x slower                                                   |
| scimark_monte_carlo        | 43.7 ms                                                     | 75.8 ms: 1.73x slower                                                   |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 4.43 ms: 1.73x slower                                                   |
| scimark_sor                | 78.8 ms                                                     | 139 ms: 1.76x slower                                                    |
| xml_etree_process          | 37.7 ms                                                     | 66.9 ms: 1.77x slower                                                   |
| hexiom                     | 4.10 ms                                                     | 7.44 ms: 1.82x slower                                                   |
| pickle_pure_python         | 195 us                                                      | 364 us: 1.86x slower                                                    |
| create_gc_cycles           | 752 us                                                      | 1.42 ms: 1.89x slower                                                   |
| deltablue                  | 2.16 ms                                                     | 4.22 ms: 1.96x slower                                                   |
| scimark_lu                 | 58.9 ms                                                     | 119 ms: 2.03x slower                                                    |
| logging_silent             | 60.5 ns                                                     | 124 ns: 2.05x slower                                                    |
| richards                   | 28.4 ms                                                     | 59.0 ms: 2.08x slower                                                   |
| richards_super             | 32.1 ms                                                     | 67.7 ms: 2.11x slower                                                   |
| unpickle_pure_python       | 133 us                                                      | 284 us: 2.13x slower                                                    |
| gc_traversal               | 1.52 ms                                                     | 3.25 ms: 2.14x slower                                                   |
| Geometric mean             | (ref)                                                       | 1.42x slower                                                            |
Ignored benchmarks (19) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250310-3.14.0a5+-90d131f/bm-20250310-pythonperf1-amd64-mdboom-msvc_musttail_aa-3.14.0a5+-90d131f.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.290x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.40x
- 95% likely to have a slowdown of 1.38x
- 99% likely to have a slowdown of 1.36x

# Memory
- memory change: unknown