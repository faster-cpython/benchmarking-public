# Results vs. 3.12.0

- fork: python
- ref: cb640b659e14cb0a0576
- machine: windows-amd64
- commit hash: cb640b6
- commit date: 2025-02-06
- overall geometric mean: 1.041x faster
- HPT reliability: 79.10%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250206-pythonperf1-amd64-python-cb640b659e14cb0a0576-3.14.0a4+-cb640b6 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 228 ms: 1.04x slower                                                        |
| docutils       | 1.66 sec                                                    | 1.64 sec: 1.01x faster                                                      |
| Geometric mean | (ref)                                                       | 1.02x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250206-pythonperf1-amd64-python-cb640b659e14cb0a0576-3.14.0a4+-cb640b6 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 405 ms: 1.91x faster                                                        |
| async_tree_io              | 731 ms                                                      | 417 ms: 1.75x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 216 ms: 1.70x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 175 ms: 1.63x faster                                                        |
| async_tree_none            | 291 ms                                                      | 185 ms: 1.57x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 220 ms: 1.54x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 341 ms: 1.47x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 336 ms: 1.45x faster                                                        |
| Geometric mean             | (ref)                                                       | 1.62x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250206-pythonperf1-amd64-python-cb640b659e14cb0a0576-3.14.0a4+-cb640b6 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 45.7 ms: 1.24x faster                                                       |
| pidigits       | 152 ms                                                      | 152 ms: 1.00x faster                                                        |
| Geometric mean | (ref)                                                       | 1.08x faster                                                                |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250206-pythonperf1-amd64-python-cb640b659e14cb0a0576-3.14.0a4+-cb640b6 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.46 ms: 1.11x faster                                                       |
| regex_compile  | 87.5 ms                                                     | 84.7 ms: 1.03x faster                                                       |
| regex_dna      | 126 ms                                                      | 124 ms: 1.02x faster                                                        |
| regex_v8       | 14.2 ms                                                     | 15.5 ms: 1.09x slower                                                       |
| Geometric mean | (ref)                                                       | 1.02x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250206-pythonperf1-amd64-python-cb640b659e14cb0a0576-3.14.0a4+-cb640b6 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 1.37 sec                                                    | 1.36 sec: 1.01x faster                                                      |
| xml_etree_parse      | 93.0 ms                                                     | 94.1 ms: 1.01x slower                                                       |
| xml_etree_iterparse  | 65.2 ms                                                     | 67.3 ms: 1.03x slower                                                       |
| xml_etree_process    | 37.7 ms                                                     | 39.1 ms: 1.04x slower                                                       |
| unpickle_pure_python | 133 us                                                      | 140 us: 1.05x slower                                                        |
| pickle_pure_python   | 195 us                                                      | 214 us: 1.10x slower                                                        |
| json_loads           | 13.9 us                                                     | 15.3 us: 1.10x slower                                                       |
| json_dumps           | 5.70 ms                                                     | 6.78 ms: 1.19x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.05x slower                                                                |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250206-pythonperf1-amd64-python-cb640b659e14cb0a0576-3.14.0a4+-cb640b6 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 19.4 ms: 1.19x slower                                                       |
| python_startup         | 19.5 ms                                                     | 26.2 ms: 1.35x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.27x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250206-pythonperf1-amd64-python-cb640b659e14cb0a0576-3.14.0a4+-cb640b6 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.61 ms: 1.07x faster                                                       |
| django_template | 22.9 ms                                                     | 25.5 ms: 1.11x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.02x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250206-pythonperf1-amd64-python-cb640b659e14cb0a0576-3.14.0a4+-cb640b6 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 405 ms: 1.91x faster                                                        |
| async_tree_io              | 731 ms                                                      | 417 ms: 1.75x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 216 ms: 1.70x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 175 ms: 1.63x faster                                                        |
| async_tree_none            | 291 ms                                                      | 185 ms: 1.57x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 220 ms: 1.54x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 341 ms: 1.47x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 336 ms: 1.45x faster                                                        |
| deepcopy                   | 238 us                                                      | 182 us: 1.31x faster                                                        |
| pathlib                    | 80.5 ms                                                     | 61.5 ms: 1.31x faster                                                       |
| comprehensions             | 14.1 us                                                     | 10.9 us: 1.29x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 18.9 us: 1.25x faster                                                       |
| float                      | 56.8 ms                                                     | 45.7 ms: 1.24x faster                                                       |
| generators                 | 22.5 ms                                                     | 19.7 ms: 1.14x faster                                                       |
| spectral_norm              | 66.9 ms                                                     | 59.0 ms: 1.13x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.57 us: 1.12x faster                                                       |
| deepcopy_reduce            | 2.09 us                                                     | 1.87 us: 1.12x faster                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.46 ms: 1.11x faster                                                       |
| coroutines                 | 14.3 ms                                                     | 13.0 ms: 1.10x faster                                                       |
| mako                       | 7.09 ms                                                     | 6.61 ms: 1.07x faster                                                       |
| go                         | 91.6 ms                                                     | 86.1 ms: 1.06x faster                                                       |
| async_generators           | 239 ms                                                      | 227 ms: 1.06x faster                                                        |
| dulwich_log                | 44.3 ms                                                     | 42.3 ms: 1.05x faster                                                       |
| chaos                      | 43.3 ms                                                     | 41.8 ms: 1.04x faster                                                       |
| regex_compile              | 87.5 ms                                                     | 84.7 ms: 1.03x faster                                                       |
| logging_silent             | 60.5 ns                                                     | 58.9 ns: 1.03x faster                                                       |
| regex_dna                  | 126 ms                                                      | 124 ms: 1.02x faster                                                        |
| sympy_sum                  | 91.5 ms                                                     | 90.0 ms: 1.02x faster                                                       |
| logging_format             | 6.72 us                                                     | 6.62 us: 1.01x faster                                                       |
| logging_simple             | 6.28 us                                                     | 6.20 us: 1.01x faster                                                       |
| docutils                   | 1.66 sec                                                    | 1.64 sec: 1.01x faster                                                      |
| tomli_loads                | 1.37 sec                                                    | 1.36 sec: 1.01x faster                                                      |
| crypto_pyaes               | 48.5 ms                                                     | 48.1 ms: 1.01x faster                                                       |
| pidigits                   | 152 ms                                                      | 152 ms: 1.00x faster                                                        |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.55 ms: 1.00x faster                                                       |
| raytrace                   | 192 ms                                                      | 193 ms: 1.00x slower                                                        |
| nqueens                    | 62.8 ms                                                     | 63.2 ms: 1.01x slower                                                       |
| sqlglot_normalize          | 187 ms                                                      | 188 ms: 1.01x slower                                                        |
| meteor_contest             | 74.6 ms                                                     | 75.3 ms: 1.01x slower                                                       |
| xml_etree_parse            | 93.0 ms                                                     | 94.1 ms: 1.01x slower                                                       |
| sqlglot_optimize           | 34.5 ms                                                     | 35.0 ms: 1.01x slower                                                       |
| richards_super             | 32.1 ms                                                     | 32.5 ms: 1.01x slower                                                       |
| pprint_pformat             | 1.05 sec                                                    | 1.06 sec: 1.02x slower                                                      |
| sympy_integrate            | 13.0 ms                                                     | 13.2 ms: 1.02x slower                                                       |
| scimark_lu                 | 58.9 ms                                                     | 60.2 ms: 1.02x slower                                                       |
| pprint_safe_repr           | 513 ms                                                      | 528 ms: 1.03x slower                                                        |
| richards                   | 28.4 ms                                                     | 29.2 ms: 1.03x slower                                                       |
| xml_etree_iterparse        | 65.2 ms                                                     | 67.3 ms: 1.03x slower                                                       |
| xml_etree_process          | 37.7 ms                                                     | 39.1 ms: 1.04x slower                                                       |
| sqlglot_transpile          | 1.02 ms                                                     | 1.06 ms: 1.04x slower                                                       |
| hexiom                     | 4.10 ms                                                     | 4.27 ms: 1.04x slower                                                       |
| pycparser                  | 699 ms                                                      | 728 ms: 1.04x slower                                                        |
| 2to3                       | 218 ms                                                      | 228 ms: 1.04x slower                                                        |
| json                       | 3.05 ms                                                     | 3.18 ms: 1.04x slower                                                       |
| sympy_expand               | 284 ms                                                      | 299 ms: 1.05x slower                                                        |
| unpickle_pure_python       | 133 us                                                      | 140 us: 1.05x slower                                                        |
| scimark_sor                | 78.8 ms                                                     | 83.5 ms: 1.06x slower                                                       |
| sqlglot_parse              | 804 us                                                      | 863 us: 1.07x slower                                                        |
| regex_v8                   | 14.2 ms                                                     | 15.5 ms: 1.09x slower                                                       |
| pickle_pure_python         | 195 us                                                      | 214 us: 1.10x slower                                                        |
| json_loads                 | 13.9 us                                                     | 15.3 us: 1.10x slower                                                       |
| fannkuch                   | 247 ms                                                      | 272 ms: 1.10x slower                                                        |
| django_template            | 22.9 ms                                                     | 25.5 ms: 1.11x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 106 us: 1.12x slower                                                        |
| telco                      | 4.13 ms                                                     | 4.72 ms: 1.14x slower                                                       |
| mdp                        | 1.37 sec                                                    | 1.59 sec: 1.16x slower                                                      |
| coverage                   | 40.8 ms                                                     | 47.6 ms: 1.17x slower                                                       |
| json_dumps                 | 5.70 ms                                                     | 6.78 ms: 1.19x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                     | 19.4 ms: 1.19x slower                                                       |
| bench_mp_pool              | 69.2 ms                                                     | 89.4 ms: 1.29x slower                                                       |
| gc_traversal               | 1.52 ms                                                     | 2.03 ms: 1.33x slower                                                       |
| python_startup             | 19.5 ms                                                     | 26.2 ms: 1.35x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 1.22 ms: 1.62x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.04x faster                                                                |

Benchmark hidden because not significant (8): bench_thread_pool, xml_etree_generate, scimark_fft, pyflate, sympy_str, deltablue, scimark_monte_carlo, nbody
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20250206-3.14.0a4+-cb640b6/bm-20250206-pythonperf1-amd64-python-cb640b659e14cb0a0576-3.14.0a4+-cb640b6.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.041x faster

# HPT report

- Reliability score: 79.10% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown