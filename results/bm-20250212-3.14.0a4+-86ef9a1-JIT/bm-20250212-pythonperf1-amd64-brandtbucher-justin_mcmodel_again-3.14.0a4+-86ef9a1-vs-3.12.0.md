# Results vs. 3.12.0

- fork: brandtbucher
- ref: justin_mcmodel_again
- machine: windows-amd64
- commit hash: 86ef9a1
- commit date: 2025-02-12
- overall geometric mean: 1.034x faster
- HPT reliability: 57.95%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250212-pythonperf1-amd64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 227 ms: 1.04x slower                                                              |
| docutils       | 1.66 sec                                                    | 1.77 sec: 1.07x slower                                                            |
| Geometric mean | (ref)                                                       | 1.05x slower                                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250212-pythonperf1-amd64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 411 ms: 1.88x faster                                                              |
| async_tree_io              | 731 ms                                                      | 414 ms: 1.77x faster                                                              |
| async_tree_memoization_tg  | 367 ms                                                      | 215 ms: 1.71x faster                                                              |
| async_tree_none_tg         | 285 ms                                                      | 176 ms: 1.62x faster                                                              |
| async_tree_none            | 291 ms                                                      | 185 ms: 1.57x faster                                                              |
| async_tree_memoization     | 339 ms                                                      | 222 ms: 1.53x faster                                                              |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 343 ms: 1.46x faster                                                              |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 340 ms: 1.44x faster                                                              |
| Geometric mean             | (ref)                                                       | 1.62x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250212-pythonperf1-amd64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| nbody          | 71.9 ms                                                     | 55.0 ms: 1.31x faster                                                             |
| float          | 56.8 ms                                                     | 45.4 ms: 1.25x faster                                                             |
| pidigits       | 152 ms                                                      | 150 ms: 1.02x faster                                                              |
| Geometric mean | (ref)                                                       | 1.18x faster                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250212-pythonperf1-amd64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.41 ms: 1.15x faster                                                             |
| regex_dna      | 126 ms                                                      | 113 ms: 1.12x faster                                                              |
| regex_compile  | 87.5 ms                                                     | 88.6 ms: 1.01x slower                                                             |
| Geometric mean | (ref)                                                       | 1.06x faster                                                                      |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250212-pythonperf1-amd64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| xml_etree_generate   | 55.8 ms                                                     | 52.1 ms: 1.07x faster                                                             |
| xml_etree_parse      | 93.0 ms                                                     | 89.7 ms: 1.04x faster                                                             |
| xml_etree_iterparse  | 65.2 ms                                                     | 62.9 ms: 1.04x faster                                                             |
| tomli_loads          | 1.37 sec                                                    | 1.33 sec: 1.03x faster                                                            |
| xml_etree_process    | 37.7 ms                                                     | 38.1 ms: 1.01x slower                                                             |
| unpickle_pure_python | 133 us                                                      | 138 us: 1.03x slower                                                              |
| json_loads           | 13.9 us                                                     | 15.4 us: 1.11x slower                                                             |
| pickle_pure_python   | 195 us                                                      | 220 us: 1.12x slower                                                              |
| json_dumps           | 5.70 ms                                                     | 6.55 ms: 1.15x slower                                                             |
| Geometric mean       | (ref)                                                       | 1.03x slower                                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250212-pythonperf1-amd64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 19.2 ms: 1.18x slower                                                             |
| python_startup         | 19.5 ms                                                     | 25.3 ms: 1.30x slower                                                             |
| Geometric mean         | (ref)                                                       | 1.24x slower                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250212-pythonperf1-amd64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.89 ms: 1.20x faster                                                             |
| django_template | 22.9 ms                                                     | 25.6 ms: 1.12x slower                                                             |
| Geometric mean  | (ref)                                                       | 1.04x faster                                                                      |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250212-pythonperf1-amd64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 411 ms: 1.88x faster                                                              |
| async_tree_io              | 731 ms                                                      | 414 ms: 1.77x faster                                                              |
| async_tree_memoization_tg  | 367 ms                                                      | 215 ms: 1.71x faster                                                              |
| async_tree_none_tg         | 285 ms                                                      | 176 ms: 1.62x faster                                                              |
| async_tree_none            | 291 ms                                                      | 185 ms: 1.57x faster                                                              |
| async_tree_memoization     | 339 ms                                                      | 222 ms: 1.53x faster                                                              |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 343 ms: 1.46x faster                                                              |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 340 ms: 1.44x faster                                                              |
| pathlib                    | 80.5 ms                                                     | 57.9 ms: 1.39x faster                                                             |
| nbody                      | 71.9 ms                                                     | 55.0 ms: 1.31x faster                                                             |
| deepcopy                   | 238 us                                                      | 182 us: 1.31x faster                                                              |
| deepcopy_memo              | 23.7 us                                                     | 18.5 us: 1.28x faster                                                             |
| float                      | 56.8 ms                                                     | 45.4 ms: 1.25x faster                                                             |
| mako                       | 7.09 ms                                                     | 5.89 ms: 1.20x faster                                                             |
| spectral_norm              | 66.9 ms                                                     | 57.7 ms: 1.16x faster                                                             |
| regex_effbot               | 1.62 ms                                                     | 1.41 ms: 1.15x faster                                                             |
| comprehensions             | 14.1 us                                                     | 12.3 us: 1.15x faster                                                             |
| sqlite_synth               | 1.76 us                                                     | 1.54 us: 1.15x faster                                                             |
| scimark_fft                | 184 ms                                                      | 163 ms: 1.13x faster                                                              |
| regex_dna                  | 126 ms                                                      | 113 ms: 1.12x faster                                                              |
| generators                 | 22.5 ms                                                     | 20.1 ms: 1.12x faster                                                             |
| coroutines                 | 14.3 ms                                                     | 12.9 ms: 1.10x faster                                                             |
| deepcopy_reduce            | 2.09 us                                                     | 1.91 us: 1.10x faster                                                             |
| xml_etree_generate         | 55.8 ms                                                     | 52.1 ms: 1.07x faster                                                             |
| logging_silent             | 60.5 ns                                                     | 56.8 ns: 1.06x faster                                                             |
| pyflate                    | 295 ms                                                      | 278 ms: 1.06x faster                                                              |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.44 ms: 1.05x faster                                                             |
| xml_etree_parse            | 93.0 ms                                                     | 89.7 ms: 1.04x faster                                                             |
| xml_etree_iterparse        | 65.2 ms                                                     | 62.9 ms: 1.04x faster                                                             |
| chaos                      | 43.3 ms                                                     | 42.0 ms: 1.03x faster                                                             |
| dulwich_log                | 44.3 ms                                                     | 43.0 ms: 1.03x faster                                                             |
| tomli_loads                | 1.37 sec                                                    | 1.33 sec: 1.03x faster                                                            |
| go                         | 91.6 ms                                                     | 89.5 ms: 1.02x faster                                                             |
| scimark_lu                 | 58.9 ms                                                     | 57.8 ms: 1.02x faster                                                             |
| logging_simple             | 6.28 us                                                     | 6.17 us: 1.02x faster                                                             |
| scimark_monte_carlo        | 43.7 ms                                                     | 43.0 ms: 1.02x faster                                                             |
| pidigits                   | 152 ms                                                      | 150 ms: 1.02x faster                                                              |
| logging_format             | 6.72 us                                                     | 6.67 us: 1.01x faster                                                             |
| xml_etree_process          | 37.7 ms                                                     | 38.1 ms: 1.01x slower                                                             |
| richards_super             | 32.1 ms                                                     | 32.5 ms: 1.01x slower                                                             |
| regex_compile              | 87.5 ms                                                     | 88.6 ms: 1.01x slower                                                             |
| richards                   | 28.4 ms                                                     | 28.8 ms: 1.01x slower                                                             |
| json                       | 3.05 ms                                                     | 3.10 ms: 1.02x slower                                                             |
| raytrace                   | 192 ms                                                      | 196 ms: 1.02x slower                                                              |
| scimark_sor                | 78.8 ms                                                     | 80.3 ms: 1.02x slower                                                             |
| sympy_sum                  | 91.5 ms                                                     | 93.6 ms: 1.02x slower                                                             |
| crypto_pyaes               | 48.5 ms                                                     | 49.7 ms: 1.02x slower                                                             |
| unpickle_pure_python       | 133 us                                                      | 138 us: 1.03x slower                                                              |
| 2to3                       | 218 ms                                                      | 227 ms: 1.04x slower                                                              |
| sympy_str                  | 175 ms                                                      | 183 ms: 1.05x slower                                                              |
| async_generators           | 239 ms                                                      | 251 ms: 1.05x slower                                                              |
| sympy_integrate            | 13.0 ms                                                     | 13.7 ms: 1.06x slower                                                             |
| docutils                   | 1.66 sec                                                    | 1.77 sec: 1.07x slower                                                            |
| sqlglot_normalize          | 187 ms                                                      | 202 ms: 1.08x slower                                                              |
| nqueens                    | 62.8 ms                                                     | 67.8 ms: 1.08x slower                                                             |
| deltablue                  | 2.16 ms                                                     | 2.34 ms: 1.08x slower                                                             |
| pycparser                  | 699 ms                                                      | 760 ms: 1.09x slower                                                              |
| meteor_contest             | 74.6 ms                                                     | 82.3 ms: 1.10x slower                                                             |
| sqlglot_optimize           | 34.5 ms                                                     | 38.2 ms: 1.11x slower                                                             |
| telco                      | 4.13 ms                                                     | 4.57 ms: 1.11x slower                                                             |
| json_loads                 | 13.9 us                                                     | 15.4 us: 1.11x slower                                                             |
| sqlglot_transpile          | 1.02 ms                                                     | 1.14 ms: 1.11x slower                                                             |
| django_template            | 22.9 ms                                                     | 25.6 ms: 1.12x slower                                                             |
| pickle_pure_python         | 195 us                                                      | 220 us: 1.12x slower                                                              |
| sympy_expand               | 284 ms                                                      | 320 ms: 1.13x slower                                                              |
| sqlglot_parse              | 804 us                                                      | 911 us: 1.13x slower                                                              |
| hexiom                     | 4.10 ms                                                     | 4.68 ms: 1.14x slower                                                             |
| json_dumps                 | 5.70 ms                                                     | 6.55 ms: 1.15x slower                                                             |
| coverage                   | 40.8 ms                                                     | 47.0 ms: 1.15x slower                                                             |
| typing_runtime_protocols   | 95.1 us                                                     | 111 us: 1.17x slower                                                              |
| python_startup_no_site     | 16.2 ms                                                     | 19.2 ms: 1.18x slower                                                             |
| fannkuch                   | 247 ms                                                      | 298 ms: 1.21x slower                                                              |
| pprint_pformat             | 1.05 sec                                                    | 1.29 sec: 1.24x slower                                                            |
| pprint_safe_repr           | 513 ms                                                      | 637 ms: 1.24x slower                                                              |
| bench_mp_pool              | 69.2 ms                                                     | 87.9 ms: 1.27x slower                                                             |
| mdp                        | 1.37 sec                                                    | 1.75 sec: 1.27x slower                                                            |
| gc_traversal               | 1.52 ms                                                     | 1.97 ms: 1.29x slower                                                             |
| python_startup             | 19.5 ms                                                     | 25.3 ms: 1.30x slower                                                             |
| create_gc_cycles           | 752 us                                                      | 1.21 ms: 1.61x slower                                                             |
| Geometric mean             | (ref)                                                       | 1.03x faster                                                                      |

Benchmark hidden because not significant (2): regex_v8, bench_thread_pool
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20250212-3.14.0a4+-86ef9a1-JIT/bm-20250212-pythonperf1-amd64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.034x faster

# HPT report

- Reliability score: 57.95% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown