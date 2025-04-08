# Results vs. 3.12.0

- fork: python
- ref: 275056a7fdcbe36aaac4
- machine: windows-amd64
- commit hash: 275056a
- commit date: 2025-04-03
- overall geometric mean: 1.283x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.20x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250403-pythonperf1-amd64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 203 ms: 1.08x faster                                                        |
| docutils       | 1.66 sec                                                    | 1.54 sec: 1.08x faster                                                      |
| Geometric mean | (ref)                                                       | 1.08x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250403-pythonperf1-amd64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 345 ms: 2.23x faster                                                        |
| async_tree_io              | 731 ms                                                      | 342 ms: 2.14x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 149 ms: 1.92x faster                                                        |
| async_tree_none            | 291 ms                                                      | 155 ms: 1.88x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 195 ms: 1.88x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 182 ms: 1.86x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 313 ms: 1.60x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 310 ms: 1.58x faster                                                        |
| Geometric mean             | (ref)                                                       | 1.87x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250403-pythonperf1-amd64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 35.5 ms: 1.60x faster                                                       |
| nbody          | 71.9 ms                                                     | 50.4 ms: 1.43x faster                                                       |
| pidigits       | 152 ms                                                      | 145 ms: 1.05x faster                                                        |
| Geometric mean | (ref)                                                       | 1.34x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250403-pythonperf1-amd64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 67.8 ms: 1.29x faster                                                       |
| regex_v8       | 14.2 ms                                                     | 13.3 ms: 1.07x faster                                                       |
| regex_dna      | 126 ms                                                      | 121 ms: 1.04x faster                                                        |
| regex_effbot   | 1.62 ms                                                     | 1.59 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                       | 1.10x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250403-pythonperf1-amd64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 1.37 sec                                                    | 1.01 sec: 1.35x faster                                                      |
| unpickle_pure_python | 133 us                                                      | 102 us: 1.30x faster                                                        |
| pickle_pure_python   | 195 us                                                      | 165 us: 1.19x faster                                                        |
| xml_etree_generate   | 55.8 ms                                                     | 48.1 ms: 1.16x faster                                                       |
| xml_etree_process    | 37.7 ms                                                     | 33.0 ms: 1.14x faster                                                       |
| xml_etree_iterparse  | 65.2 ms                                                     | 60.1 ms: 1.08x faster                                                       |
| xml_etree_parse      | 93.0 ms                                                     | 88.4 ms: 1.05x faster                                                       |
| json_loads           | 13.9 us                                                     | 13.5 us: 1.03x faster                                                       |
| json_dumps           | 5.70 ms                                                     | 5.59 ms: 1.02x faster                                                       |
| Geometric mean       | (ref)                                                       | 1.14x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250403-pythonperf1-amd64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 21.0 ms: 1.29x slower                                                       |
| python_startup         | 19.5 ms                                                     | 26.5 ms: 1.36x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.33x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250403-pythonperf1-amd64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.66 ms: 1.25x faster                                                       |
| django_template | 22.9 ms                                                     | 19.5 ms: 1.18x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.21x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250403-pythonperf1-amd64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 30.9 ms: 2.60x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 345 ms: 2.23x faster                                                        |
| async_tree_io              | 731 ms                                                      | 342 ms: 2.14x faster                                                        |
| mdp                        | 1.37 sec                                                    | 669 ms: 2.05x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 149 ms: 1.92x faster                                                        |
| async_tree_none            | 291 ms                                                      | 155 ms: 1.88x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 195 ms: 1.88x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 182 ms: 1.86x faster                                                        |
| deepcopy_memo              | 23.7 us                                                     | 13.1 us: 1.80x faster                                                       |
| deepcopy                   | 238 us                                                      | 138 us: 1.73x faster                                                        |
| comprehensions             | 14.1 us                                                     | 8.36 us: 1.69x faster                                                       |
| scimark_sor                | 78.8 ms                                                     | 47.8 ms: 1.65x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 313 ms: 1.60x faster                                                        |
| scimark_monte_carlo        | 43.7 ms                                                     | 27.3 ms: 1.60x faster                                                       |
| float                      | 56.8 ms                                                     | 35.5 ms: 1.60x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 310 ms: 1.58x faster                                                        |
| go                         | 91.6 ms                                                     | 58.2 ms: 1.57x faster                                                       |
| generators                 | 22.5 ms                                                     | 15.0 ms: 1.50x faster                                                       |
| logging_silent             | 60.5 ns                                                     | 41.0 ns: 1.48x faster                                                       |
| spectral_norm              | 66.9 ms                                                     | 46.8 ms: 1.43x faster                                                       |
| raytrace                   | 192 ms                                                      | 135 ms: 1.43x faster                                                        |
| nbody                      | 71.9 ms                                                     | 50.4 ms: 1.43x faster                                                       |
| deltablue                  | 2.16 ms                                                     | 1.52 ms: 1.42x faster                                                       |
| deepcopy_reduce            | 2.09 us                                                     | 1.48 us: 1.42x faster                                                       |
| chaos                      | 43.3 ms                                                     | 30.7 ms: 1.41x faster                                                       |
| hexiom                     | 4.10 ms                                                     | 2.91 ms: 1.41x faster                                                       |
| richards                   | 28.4 ms                                                     | 20.7 ms: 1.37x faster                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.01 sec: 1.35x faster                                                      |
| richards_super             | 32.1 ms                                                     | 24.3 ms: 1.32x faster                                                       |
| coroutines                 | 14.3 ms                                                     | 10.9 ms: 1.31x faster                                                       |
| scimark_fft                | 184 ms                                                      | 141 ms: 1.31x faster                                                        |
| pprint_safe_repr           | 513 ms                                                      | 393 ms: 1.31x faster                                                        |
| scimark_lu                 | 58.9 ms                                                     | 45.1 ms: 1.31x faster                                                       |
| unpickle_pure_python       | 133 us                                                      | 102 us: 1.30x faster                                                        |
| regex_compile              | 87.5 ms                                                     | 67.8 ms: 1.29x faster                                                       |
| pyflate                    | 295 ms                                                      | 229 ms: 1.29x faster                                                        |
| fannkuch                   | 247 ms                                                      | 192 ms: 1.29x faster                                                        |
| async_generators           | 239 ms                                                      | 186 ms: 1.29x faster                                                        |
| pprint_pformat             | 1.05 sec                                                    | 817 ms: 1.28x faster                                                        |
| nqueens                    | 62.8 ms                                                     | 49.6 ms: 1.26x faster                                                       |
| mako                       | 7.09 ms                                                     | 5.66 ms: 1.25x faster                                                       |
| crypto_pyaes               | 48.5 ms                                                     | 38.9 ms: 1.25x faster                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.15 ms: 1.19x faster                                                       |
| pickle_pure_python         | 195 us                                                      | 165 us: 1.19x faster                                                        |
| sqlite_synth               | 1.76 us                                                     | 1.49 us: 1.18x faster                                                       |
| django_template            | 22.9 ms                                                     | 19.5 ms: 1.18x faster                                                       |
| sympy_str                  | 175 ms                                                      | 149 ms: 1.18x faster                                                        |
| dulwich_log                | 44.3 ms                                                     | 37.8 ms: 1.17x faster                                                       |
| sympy_sum                  | 91.5 ms                                                     | 78.6 ms: 1.16x faster                                                       |
| xml_etree_generate         | 55.8 ms                                                     | 48.1 ms: 1.16x faster                                                       |
| sympy_integrate            | 13.0 ms                                                     | 11.2 ms: 1.16x faster                                                       |
| xml_etree_process          | 37.7 ms                                                     | 33.0 ms: 1.14x faster                                                       |
| logging_simple             | 6.28 us                                                     | 5.53 us: 1.13x faster                                                       |
| meteor_contest             | 74.6 ms                                                     | 66.3 ms: 1.12x faster                                                       |
| logging_format             | 6.72 us                                                     | 6.00 us: 1.12x faster                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 85.9 us: 1.11x faster                                                       |
| sympy_expand               | 284 ms                                                      | 257 ms: 1.10x faster                                                        |
| pycparser                  | 699 ms                                                      | 636 ms: 1.10x faster                                                        |
| xml_etree_iterparse        | 65.2 ms                                                     | 60.1 ms: 1.08x faster                                                       |
| docutils                   | 1.66 sec                                                    | 1.54 sec: 1.08x faster                                                      |
| 2to3                       | 218 ms                                                      | 203 ms: 1.08x faster                                                        |
| json                       | 3.05 ms                                                     | 2.84 ms: 1.07x faster                                                       |
| regex_v8                   | 14.2 ms                                                     | 13.3 ms: 1.07x faster                                                       |
| xml_etree_parse            | 93.0 ms                                                     | 88.4 ms: 1.05x faster                                                       |
| pidigits                   | 152 ms                                                      | 145 ms: 1.05x faster                                                        |
| regex_dna                  | 126 ms                                                      | 121 ms: 1.04x faster                                                        |
| coverage                   | 40.8 ms                                                     | 39.5 ms: 1.03x faster                                                       |
| json_loads                 | 13.9 us                                                     | 13.5 us: 1.03x faster                                                       |
| bench_thread_pool          | 857 us                                                      | 831 us: 1.03x faster                                                        |
| regex_effbot               | 1.62 ms                                                     | 1.59 ms: 1.02x faster                                                       |
| json_dumps                 | 5.70 ms                                                     | 5.59 ms: 1.02x faster                                                       |
| telco                      | 4.13 ms                                                     | 4.16 ms: 1.01x slower                                                       |
| bench_mp_pool              | 69.2 ms                                                     | 87.8 ms: 1.27x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                     | 21.0 ms: 1.29x slower                                                       |
| python_startup             | 19.5 ms                                                     | 26.5 ms: 1.36x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 1.32 ms: 1.76x slower                                                       |
| gc_traversal               | 1.52 ms                                                     | 2.79 ms: 1.83x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.27x faster                                                                |
Ignored benchmarks (19) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250403-3.14.0a6+-275056a-CLANG/bm-20250403-pythonperf1-amd64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.283x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.26x
- 95% likely to have a speedup of 1.24x
- 99% likely to have a speedup of 1.20x

# Memory
- memory change: unknown