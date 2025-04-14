# Results vs. 3.12.0

- fork: python
- ref: c6b1a073438d93d4e629
- machine: windows-amd64
- commit hash: c6b1a07
- commit date: 2025-03-29
- overall geometric mean: 1.265x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.19x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250329-pythonperf1-amd64-python-c6b1a073438d93d4e629-3.14.0a6+-c6b1a07 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 204 ms: 1.07x faster                                                        |
| docutils       | 1.66 sec                                                    | 1.54 sec: 1.08x faster                                                      |
| Geometric mean | (ref)                                                       | 1.07x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250329-pythonperf1-amd64-python-c6b1a073438d93d4e629-3.14.0a6+-c6b1a07 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 348 ms: 2.22x faster                                                        |
| async_tree_io              | 731 ms                                                      | 349 ms: 2.09x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 151 ms: 1.89x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 199 ms: 1.84x faster                                                        |
| async_tree_none            | 291 ms                                                      | 158 ms: 1.84x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 190 ms: 1.79x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 316 ms: 1.59x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 312 ms: 1.57x faster                                                        |
| Geometric mean             | (ref)                                                       | 1.84x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250329-pythonperf1-amd64-python-c6b1a073438d93d4e629-3.14.0a6+-c6b1a07 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 37.1 ms: 1.53x faster                                                       |
| nbody          | 71.9 ms                                                     | 47.7 ms: 1.51x faster                                                       |
| pidigits       | 152 ms                                                      | 145 ms: 1.05x faster                                                        |
| Geometric mean | (ref)                                                       | 1.34x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250329-pythonperf1-amd64-python-c6b1a073438d93d4e629-3.14.0a6+-c6b1a07 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 69.1 ms: 1.27x faster                                                       |
| regex_v8       | 14.2 ms                                                     | 13.3 ms: 1.07x faster                                                       |
| regex_dna      | 126 ms                                                      | 124 ms: 1.02x faster                                                        |
| regex_effbot   | 1.62 ms                                                     | 1.66 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                       | 1.08x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250329-pythonperf1-amd64-python-c6b1a073438d93d4e629-3.14.0a6+-c6b1a07 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 133 us                                                      | 105 us: 1.27x faster                                                        |
| tomli_loads          | 1.37 sec                                                    | 1.09 sec: 1.25x faster                                                      |
| xml_etree_generate   | 55.8 ms                                                     | 47.6 ms: 1.17x faster                                                       |
| xml_etree_process    | 37.7 ms                                                     | 33.5 ms: 1.12x faster                                                       |
| pickle_pure_python   | 195 us                                                      | 175 us: 1.12x faster                                                        |
| xml_etree_iterparse  | 65.2 ms                                                     | 61.0 ms: 1.07x faster                                                       |
| xml_etree_parse      | 93.0 ms                                                     | 88.2 ms: 1.06x faster                                                       |
| json_loads           | 13.9 us                                                     | 14.2 us: 1.02x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.11x faster                                                                |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250329-pythonperf1-amd64-python-c6b1a073438d93d4e629-3.14.0a6+-c6b1a07 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 21.0 ms: 1.29x slower                                                       |
| python_startup         | 19.5 ms                                                     | 26.7 ms: 1.37x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.33x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250329-pythonperf1-amd64-python-c6b1a073438d93d4e629-3.14.0a6+-c6b1a07 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.78 ms: 1.23x faster                                                       |
| django_template | 22.9 ms                                                     | 20.4 ms: 1.12x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.17x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250329-pythonperf1-amd64-python-c6b1a073438d93d4e629-3.14.0a6+-c6b1a07 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 30.6 ms: 2.63x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 348 ms: 2.22x faster                                                        |
| async_tree_io              | 731 ms                                                      | 349 ms: 2.09x faster                                                        |
| mdp                        | 1.37 sec                                                    | 684 ms: 2.01x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 151 ms: 1.89x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 199 ms: 1.84x faster                                                        |
| async_tree_none            | 291 ms                                                      | 158 ms: 1.84x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 190 ms: 1.79x faster                                                        |
| deepcopy_memo              | 23.7 us                                                     | 14.0 us: 1.70x faster                                                       |
| deepcopy                   | 238 us                                                      | 142 us: 1.68x faster                                                        |
| comprehensions             | 14.1 us                                                     | 8.54 us: 1.65x faster                                                       |
| scimark_sor                | 78.8 ms                                                     | 49.2 ms: 1.60x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 316 ms: 1.59x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 312 ms: 1.57x faster                                                        |
| spectral_norm              | 66.9 ms                                                     | 42.9 ms: 1.56x faster                                                       |
| float                      | 56.8 ms                                                     | 37.1 ms: 1.53x faster                                                       |
| nbody                      | 71.9 ms                                                     | 47.7 ms: 1.51x faster                                                       |
| generators                 | 22.5 ms                                                     | 15.0 ms: 1.50x faster                                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 29.3 ms: 1.49x faster                                                       |
| go                         | 91.6 ms                                                     | 62.2 ms: 1.47x faster                                                       |
| logging_silent             | 60.5 ns                                                     | 41.8 ns: 1.45x faster                                                       |
| hexiom                     | 4.10 ms                                                     | 2.96 ms: 1.39x faster                                                       |
| chaos                      | 43.3 ms                                                     | 31.4 ms: 1.38x faster                                                       |
| raytrace                   | 192 ms                                                      | 140 ms: 1.37x faster                                                        |
| deltablue                  | 2.16 ms                                                     | 1.59 ms: 1.36x faster                                                       |
| deepcopy_reduce            | 2.09 us                                                     | 1.54 us: 1.36x faster                                                       |
| scimark_lu                 | 58.9 ms                                                     | 43.5 ms: 1.35x faster                                                       |
| coroutines                 | 14.3 ms                                                     | 10.9 ms: 1.31x faster                                                       |
| nqueens                    | 62.8 ms                                                     | 48.5 ms: 1.29x faster                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 1.99 ms: 1.29x faster                                                       |
| scimark_fft                | 184 ms                                                      | 144 ms: 1.28x faster                                                        |
| pyflate                    | 295 ms                                                      | 230 ms: 1.28x faster                                                        |
| richards                   | 28.4 ms                                                     | 22.2 ms: 1.28x faster                                                       |
| async_generators           | 239 ms                                                      | 188 ms: 1.27x faster                                                        |
| unpickle_pure_python       | 133 us                                                      | 105 us: 1.27x faster                                                        |
| regex_compile              | 87.5 ms                                                     | 69.1 ms: 1.27x faster                                                       |
| richards_super             | 32.1 ms                                                     | 25.4 ms: 1.27x faster                                                       |
| pprint_pformat             | 1.05 sec                                                    | 834 ms: 1.25x faster                                                        |
| tomli_loads                | 1.37 sec                                                    | 1.09 sec: 1.25x faster                                                      |
| fannkuch                   | 247 ms                                                      | 197 ms: 1.25x faster                                                        |
| crypto_pyaes               | 48.5 ms                                                     | 38.8 ms: 1.25x faster                                                       |
| pprint_safe_repr           | 513 ms                                                      | 411 ms: 1.25x faster                                                        |
| mako                       | 7.09 ms                                                     | 5.78 ms: 1.23x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.48 us: 1.19x faster                                                       |
| sympy_str                  | 175 ms                                                      | 148 ms: 1.18x faster                                                        |
| dulwich_log                | 44.3 ms                                                     | 37.8 ms: 1.17x faster                                                       |
| sympy_sum                  | 91.5 ms                                                     | 78.1 ms: 1.17x faster                                                       |
| xml_etree_generate         | 55.8 ms                                                     | 47.6 ms: 1.17x faster                                                       |
| sympy_integrate            | 13.0 ms                                                     | 11.3 ms: 1.15x faster                                                       |
| logging_format             | 6.72 us                                                     | 5.94 us: 1.13x faster                                                       |
| django_template            | 22.9 ms                                                     | 20.4 ms: 1.12x faster                                                       |
| xml_etree_process          | 37.7 ms                                                     | 33.5 ms: 1.12x faster                                                       |
| logging_simple             | 6.28 us                                                     | 5.60 us: 1.12x faster                                                       |
| meteor_contest             | 74.6 ms                                                     | 66.6 ms: 1.12x faster                                                       |
| pickle_pure_python         | 195 us                                                      | 175 us: 1.12x faster                                                        |
| sympy_expand               | 284 ms                                                      | 255 ms: 1.11x faster                                                        |
| typing_runtime_protocols   | 95.1 us                                                     | 86.5 us: 1.10x faster                                                       |
| docutils                   | 1.66 sec                                                    | 1.54 sec: 1.08x faster                                                      |
| pycparser                  | 699 ms                                                      | 648 ms: 1.08x faster                                                        |
| json                       | 3.05 ms                                                     | 2.83 ms: 1.08x faster                                                       |
| regex_v8                   | 14.2 ms                                                     | 13.3 ms: 1.07x faster                                                       |
| xml_etree_iterparse        | 65.2 ms                                                     | 61.0 ms: 1.07x faster                                                       |
| 2to3                       | 218 ms                                                      | 204 ms: 1.07x faster                                                        |
| xml_etree_parse            | 93.0 ms                                                     | 88.2 ms: 1.06x faster                                                       |
| pidigits                   | 152 ms                                                      | 145 ms: 1.05x faster                                                        |
| bench_thread_pool          | 857 us                                                      | 819 us: 1.05x faster                                                        |
| coverage                   | 40.8 ms                                                     | 39.3 ms: 1.04x faster                                                       |
| regex_dna                  | 126 ms                                                      | 124 ms: 1.02x faster                                                        |
| json_loads                 | 13.9 us                                                     | 14.2 us: 1.02x slower                                                       |
| telco                      | 4.13 ms                                                     | 4.23 ms: 1.02x slower                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.66 ms: 1.03x slower                                                       |
| bench_mp_pool              | 69.2 ms                                                     | 88.7 ms: 1.28x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                     | 21.0 ms: 1.29x slower                                                       |
| python_startup             | 19.5 ms                                                     | 26.7 ms: 1.37x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 1.34 ms: 1.79x slower                                                       |
| gc_traversal               | 1.52 ms                                                     | 2.74 ms: 1.80x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.26x faster                                                                |

Benchmark hidden because not significant (1): json_dumps
Ignored benchmarks (19) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250329-3.14.0a6+-c6b1a07-CLANG/bm-20250329-pythonperf1-amd64-python-c6b1a073438d93d4e629-3.14.0a6+-c6b1a07.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.265x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.24x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.19x

# Memory
- memory change: unknown