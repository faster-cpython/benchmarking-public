# Results vs. 3.12.0

- fork: mdboom
- ref: msvc_musttail_clang_
- machine: windows-amd64
- commit hash: 18326e0
- commit date: 2025-04-01
- overall geometric mean: 1.256x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.16x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250401-pythonperf1-amd64-mdboom-msvc_musttail_clang_-3.14.0a6+-18326e0 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 207 ms: 1.05x faster                                                        |
| docutils       | 1.66 sec                                                    | 1.56 sec: 1.07x faster                                                      |
| Geometric mean | (ref)                                                       | 1.06x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250401-pythonperf1-amd64-mdboom-msvc_musttail_clang_-3.14.0a6+-18326e0 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 351 ms: 2.20x faster                                                        |
| async_tree_io              | 731 ms                                                      | 353 ms: 2.07x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 150 ms: 1.90x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 197 ms: 1.86x faster                                                        |
| async_tree_none            | 291 ms                                                      | 159 ms: 1.83x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 187 ms: 1.81x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 316 ms: 1.59x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 313 ms: 1.56x faster                                                        |
| Geometric mean             | (ref)                                                       | 1.84x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250401-pythonperf1-amd64-mdboom-msvc_musttail_clang_-3.14.0a6+-18326e0 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 36.9 ms: 1.54x faster                                                       |
| nbody          | 71.9 ms                                                     | 49.1 ms: 1.47x faster                                                       |
| pidigits       | 152 ms                                                      | 145 ms: 1.05x faster                                                        |
| Geometric mean | (ref)                                                       | 1.33x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250401-pythonperf1-amd64-mdboom-msvc_musttail_clang_-3.14.0a6+-18326e0 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 69.8 ms: 1.25x faster                                                       |
| regex_v8       | 14.2 ms                                                     | 13.0 ms: 1.10x faster                                                       |
| regex_dna      | 126 ms                                                      | 117 ms: 1.08x faster                                                        |
| regex_effbot   | 1.62 ms                                                     | 1.54 ms: 1.05x faster                                                       |
| Geometric mean | (ref)                                                       | 1.12x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250401-pythonperf1-amd64-mdboom-msvc_musttail_clang_-3.14.0a6+-18326e0 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 1.37 sec                                                    | 1.09 sec: 1.26x faster                                                      |
| unpickle_pure_python | 133 us                                                      | 107 us: 1.24x faster                                                        |
| xml_etree_generate   | 55.8 ms                                                     | 49.1 ms: 1.14x faster                                                       |
| pickle_pure_python   | 195 us                                                      | 173 us: 1.13x faster                                                        |
| xml_etree_process    | 37.7 ms                                                     | 34.0 ms: 1.11x faster                                                       |
| xml_etree_iterparse  | 65.2 ms                                                     | 61.5 ms: 1.06x faster                                                       |
| xml_etree_parse      | 93.0 ms                                                     | 89.4 ms: 1.04x faster                                                       |
| json_loads           | 13.9 us                                                     | 14.1 us: 1.01x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.10x faster                                                                |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250401-pythonperf1-amd64-mdboom-msvc_musttail_clang_-3.14.0a6+-18326e0 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 20.9 ms: 1.29x slower                                                       |
| python_startup         | 19.5 ms                                                     | 26.4 ms: 1.36x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.32x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250401-pythonperf1-amd64-mdboom-msvc_musttail_clang_-3.14.0a6+-18326e0 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.83 ms: 1.22x faster                                                       |
| django_template | 22.9 ms                                                     | 21.3 ms: 1.08x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.14x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250401-pythonperf1-amd64-mdboom-msvc_musttail_clang_-3.14.0a6+-18326e0 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 30.7 ms: 2.62x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 351 ms: 2.20x faster                                                        |
| async_tree_io              | 731 ms                                                      | 353 ms: 2.07x faster                                                        |
| mdp                        | 1.37 sec                                                    | 682 ms: 2.01x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 150 ms: 1.90x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 197 ms: 1.86x faster                                                        |
| async_tree_none            | 291 ms                                                      | 159 ms: 1.83x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 187 ms: 1.81x faster                                                        |
| deepcopy_memo              | 23.7 us                                                     | 14.0 us: 1.70x faster                                                       |
| deepcopy                   | 238 us                                                      | 144 us: 1.65x faster                                                        |
| comprehensions             | 14.1 us                                                     | 8.64 us: 1.64x faster                                                       |
| scimark_sor                | 78.8 ms                                                     | 49.3 ms: 1.60x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 316 ms: 1.59x faster                                                        |
| spectral_norm              | 66.9 ms                                                     | 42.8 ms: 1.56x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 313 ms: 1.56x faster                                                        |
| float                      | 56.8 ms                                                     | 36.9 ms: 1.54x faster                                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 28.6 ms: 1.53x faster                                                       |
| generators                 | 22.5 ms                                                     | 14.8 ms: 1.53x faster                                                       |
| go                         | 91.6 ms                                                     | 61.5 ms: 1.49x faster                                                       |
| logging_silent             | 60.5 ns                                                     | 41.1 ns: 1.47x faster                                                       |
| nbody                      | 71.9 ms                                                     | 49.1 ms: 1.47x faster                                                       |
| deepcopy_reduce            | 2.09 us                                                     | 1.52 us: 1.38x faster                                                       |
| chaos                      | 43.3 ms                                                     | 31.4 ms: 1.38x faster                                                       |
| hexiom                     | 4.10 ms                                                     | 2.98 ms: 1.37x faster                                                       |
| raytrace                   | 192 ms                                                      | 142 ms: 1.35x faster                                                        |
| scimark_lu                 | 58.9 ms                                                     | 43.5 ms: 1.35x faster                                                       |
| coroutines                 | 14.3 ms                                                     | 10.7 ms: 1.33x faster                                                       |
| scimark_fft                | 184 ms                                                      | 139 ms: 1.32x faster                                                        |
| deltablue                  | 2.16 ms                                                     | 1.64 ms: 1.31x faster                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 1.99 ms: 1.28x faster                                                       |
| async_generators           | 239 ms                                                      | 187 ms: 1.28x faster                                                        |
| nqueens                    | 62.8 ms                                                     | 49.8 ms: 1.26x faster                                                       |
| pyflate                    | 295 ms                                                      | 234 ms: 1.26x faster                                                        |
| tomli_loads                | 1.37 sec                                                    | 1.09 sec: 1.26x faster                                                      |
| regex_compile              | 87.5 ms                                                     | 69.8 ms: 1.25x faster                                                       |
| pprint_pformat             | 1.05 sec                                                    | 835 ms: 1.25x faster                                                        |
| unpickle_pure_python       | 133 us                                                      | 107 us: 1.24x faster                                                        |
| pprint_safe_repr           | 513 ms                                                      | 415 ms: 1.24x faster                                                        |
| mako                       | 7.09 ms                                                     | 5.83 ms: 1.22x faster                                                       |
| crypto_pyaes               | 48.5 ms                                                     | 39.9 ms: 1.21x faster                                                       |
| fannkuch                   | 247 ms                                                      | 207 ms: 1.19x faster                                                        |
| sympy_str                  | 175 ms                                                      | 149 ms: 1.18x faster                                                        |
| sqlite_synth               | 1.76 us                                                     | 1.51 us: 1.17x faster                                                       |
| dulwich_log                | 44.3 ms                                                     | 38.0 ms: 1.16x faster                                                       |
| sympy_integrate            | 13.0 ms                                                     | 11.2 ms: 1.16x faster                                                       |
| sympy_sum                  | 91.5 ms                                                     | 79.2 ms: 1.16x faster                                                       |
| xml_etree_generate         | 55.8 ms                                                     | 49.1 ms: 1.14x faster                                                       |
| logging_simple             | 6.28 us                                                     | 5.55 us: 1.13x faster                                                       |
| pickle_pure_python         | 195 us                                                      | 173 us: 1.13x faster                                                        |
| logging_format             | 6.72 us                                                     | 5.96 us: 1.13x faster                                                       |
| meteor_contest             | 74.6 ms                                                     | 66.8 ms: 1.12x faster                                                       |
| xml_etree_process          | 37.7 ms                                                     | 34.0 ms: 1.11x faster                                                       |
| sympy_expand               | 284 ms                                                      | 256 ms: 1.11x faster                                                        |
| regex_v8                   | 14.2 ms                                                     | 13.0 ms: 1.10x faster                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 87.6 us: 1.09x faster                                                       |
| json                       | 3.05 ms                                                     | 2.81 ms: 1.08x faster                                                       |
| richards                   | 28.4 ms                                                     | 26.3 ms: 1.08x faster                                                       |
| pycparser                  | 699 ms                                                      | 647 ms: 1.08x faster                                                        |
| django_template            | 22.9 ms                                                     | 21.3 ms: 1.08x faster                                                       |
| regex_dna                  | 126 ms                                                      | 117 ms: 1.08x faster                                                        |
| docutils                   | 1.66 sec                                                    | 1.56 sec: 1.07x faster                                                      |
| richards_super             | 32.1 ms                                                     | 30.2 ms: 1.06x faster                                                       |
| xml_etree_iterparse        | 65.2 ms                                                     | 61.5 ms: 1.06x faster                                                       |
| 2to3                       | 218 ms                                                      | 207 ms: 1.05x faster                                                        |
| regex_effbot               | 1.62 ms                                                     | 1.54 ms: 1.05x faster                                                       |
| pidigits                   | 152 ms                                                      | 145 ms: 1.05x faster                                                        |
| bench_thread_pool          | 857 us                                                      | 823 us: 1.04x faster                                                        |
| xml_etree_parse            | 93.0 ms                                                     | 89.4 ms: 1.04x faster                                                       |
| coverage                   | 40.8 ms                                                     | 39.8 ms: 1.03x faster                                                       |
| json_loads                 | 13.9 us                                                     | 14.1 us: 1.01x slower                                                       |
| telco                      | 4.13 ms                                                     | 4.25 ms: 1.03x slower                                                       |
| bench_mp_pool              | 69.2 ms                                                     | 88.6 ms: 1.28x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                     | 20.9 ms: 1.29x slower                                                       |
| python_startup             | 19.5 ms                                                     | 26.4 ms: 1.36x slower                                                       |
| gc_traversal               | 1.52 ms                                                     | 2.76 ms: 1.81x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 1.36 ms: 1.81x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.25x faster                                                                |

Benchmark hidden because not significant (1): json_dumps
Ignored benchmarks (19) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250401-3.14.0a6+-18326e0-CLANG/bm-20250401-pythonperf1-amd64-mdboom-msvc_musttail_clang_-3.14.0a6+-18326e0.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.256x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.22x
- 95% likely to have a speedup of 1.20x
- 99% likely to have a speedup of 1.16x

# Memory
- memory change: unknown