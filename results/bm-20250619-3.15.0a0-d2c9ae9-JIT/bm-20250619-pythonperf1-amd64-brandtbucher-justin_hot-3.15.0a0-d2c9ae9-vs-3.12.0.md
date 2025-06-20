# Results vs. 3.12.0

- fork: brandtbucher
- ref: justin_hot
- machine: windows-amd64
- commit hash: d2c9ae9
- commit date: 2025-06-19
- overall geometric mean: 1.108x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250619-pythonperf1-amd64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 221 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                       | 1.01x slower                                                           |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250619-pythonperf1-amd64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|----------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 390 ms: 1.98x faster                                                   |
| async_tree_io              | 731 ms                                                      | 398 ms: 1.84x faster                                                   |
| async_tree_memoization_tg  | 367 ms                                                      | 210 ms: 1.75x faster                                                   |
| async_tree_none            | 291 ms                                                      | 171 ms: 1.70x faster                                                   |
| async_tree_none_tg         | 285 ms                                                      | 169 ms: 1.69x faster                                                   |
| async_tree_memoization     | 339 ms                                                      | 207 ms: 1.64x faster                                                   |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 342 ms: 1.47x faster                                                   |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 333 ms: 1.47x faster                                                   |
| Geometric mean             | (ref)                                                       | 1.68x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250619-pythonperf1-amd64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 44.0 ms: 1.29x faster                                                  |
| nbody          | 71.9 ms                                                     | 62.4 ms: 1.15x faster                                                  |
| pidigits       | 152 ms                                                      | 149 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                       | 1.15x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250619-pythonperf1-amd64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 78.9 ms: 1.11x faster                                                  |
| regex_dna      | 126 ms                                                      | 120 ms: 1.05x faster                                                   |
| regex_effbot   | 1.62 ms                                                     | 1.63 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                       | 1.03x faster                                                           |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250619-pythonperf1-amd64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|----------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 1.37 sec                                                    | 1.16 sec: 1.18x faster                                                 |
| unpickle_pure_python | 133 us                                                      | 114 us: 1.17x faster                                                   |
| xml_etree_generate   | 55.8 ms                                                     | 50.7 ms: 1.10x faster                                                  |
| xml_etree_parse      | 93.0 ms                                                     | 88.1 ms: 1.06x faster                                                  |
| xml_etree_iterparse  | 65.2 ms                                                     | 62.8 ms: 1.04x faster                                                  |
| xml_etree_process    | 37.7 ms                                                     | 36.4 ms: 1.04x faster                                                  |
| json_loads           | 13.9 us                                                     | 14.6 us: 1.05x slower                                                  |
| pickle_pure_python   | 195 us                                                      | 205 us: 1.05x slower                                                   |
| json_dumps           | 5.70 ms                                                     | 6.47 ms: 1.14x slower                                                  |
| Geometric mean       | (ref)                                                       | 1.04x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250619-pythonperf1-amd64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 19.3 ms: 1.18x slower                                                  |
| python_startup         | 19.5 ms                                                     | 25.8 ms: 1.32x slower                                                  |
| Geometric mean         | (ref)                                                       | 1.25x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250619-pythonperf1-amd64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|-----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.47 ms: 1.30x faster                                                  |
| django_template | 22.9 ms                                                     | 24.0 ms: 1.05x slower                                                  |
| Geometric mean  | (ref)                                                       | 1.11x faster                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250619-pythonperf1-amd64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|----------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 31.8 ms: 2.53x faster                                                  |
| async_tree_io_tg           | 771 ms                                                      | 390 ms: 1.98x faster                                                   |
| async_tree_io              | 731 ms                                                      | 398 ms: 1.84x faster                                                   |
| async_tree_memoization_tg  | 367 ms                                                      | 210 ms: 1.75x faster                                                   |
| mdp                        | 1.37 sec                                                    | 795 ms: 1.73x faster                                                   |
| async_tree_none            | 291 ms                                                      | 171 ms: 1.70x faster                                                   |
| async_tree_none_tg         | 285 ms                                                      | 169 ms: 1.69x faster                                                   |
| async_tree_memoization     | 339 ms                                                      | 207 ms: 1.64x faster                                                   |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 342 ms: 1.47x faster                                                   |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 333 ms: 1.47x faster                                                   |
| deepcopy                   | 238 us                                                      | 169 us: 1.41x faster                                                   |
| comprehensions             | 14.1 us                                                     | 10.8 us: 1.31x faster                                                  |
| deepcopy_memo              | 23.7 us                                                     | 18.2 us: 1.30x faster                                                  |
| mako                       | 7.09 ms                                                     | 5.47 ms: 1.30x faster                                                  |
| float                      | 56.8 ms                                                     | 44.0 ms: 1.29x faster                                                  |
| tomli_loads                | 1.37 sec                                                    | 1.16 sec: 1.18x faster                                                 |
| go                         | 91.6 ms                                                     | 77.5 ms: 1.18x faster                                                  |
| unpickle_pure_python       | 133 us                                                      | 114 us: 1.17x faster                                                   |
| deepcopy_reduce            | 2.09 us                                                     | 1.79 us: 1.17x faster                                                  |
| nbody                      | 71.9 ms                                                     | 62.4 ms: 1.15x faster                                                  |
| generators                 | 22.5 ms                                                     | 19.6 ms: 1.15x faster                                                  |
| scimark_fft                | 184 ms                                                      | 161 ms: 1.15x faster                                                   |
| sqlite_synth               | 1.76 us                                                     | 1.56 us: 1.13x faster                                                  |
| pyflate                    | 295 ms                                                      | 263 ms: 1.12x faster                                                   |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.29 ms: 1.12x faster                                                  |
| regex_compile              | 87.5 ms                                                     | 78.9 ms: 1.11x faster                                                  |
| xml_etree_generate         | 55.8 ms                                                     | 50.7 ms: 1.10x faster                                                  |
| scimark_monte_carlo        | 43.7 ms                                                     | 40.2 ms: 1.09x faster                                                  |
| spectral_norm              | 66.9 ms                                                     | 61.7 ms: 1.09x faster                                                  |
| nqueens                    | 62.8 ms                                                     | 58.4 ms: 1.07x faster                                                  |
| chaos                      | 43.3 ms                                                     | 40.4 ms: 1.07x faster                                                  |
| dulwich_log                | 44.3 ms                                                     | 41.5 ms: 1.07x faster                                                  |
| fannkuch                   | 247 ms                                                      | 232 ms: 1.06x faster                                                   |
| raytrace                   | 192 ms                                                      | 182 ms: 1.06x faster                                                   |
| xml_etree_parse            | 93.0 ms                                                     | 88.1 ms: 1.06x faster                                                  |
| regex_dna                  | 126 ms                                                      | 120 ms: 1.05x faster                                                   |
| sympy_sum                  | 91.5 ms                                                     | 87.5 ms: 1.05x faster                                                  |
| richards                   | 28.4 ms                                                     | 27.2 ms: 1.04x faster                                                  |
| richards_super             | 32.1 ms                                                     | 30.7 ms: 1.04x faster                                                  |
| crypto_pyaes               | 48.5 ms                                                     | 46.5 ms: 1.04x faster                                                  |
| meteor_contest             | 74.6 ms                                                     | 71.8 ms: 1.04x faster                                                  |
| xml_etree_iterparse        | 65.2 ms                                                     | 62.8 ms: 1.04x faster                                                  |
| xml_etree_process          | 37.7 ms                                                     | 36.4 ms: 1.04x faster                                                  |
| scimark_sor                | 78.8 ms                                                     | 77.0 ms: 1.02x faster                                                  |
| pidigits                   | 152 ms                                                      | 149 ms: 1.02x faster                                                   |
| sympy_str                  | 175 ms                                                      | 172 ms: 1.02x faster                                                   |
| pprint_safe_repr           | 513 ms                                                      | 507 ms: 1.01x faster                                                   |
| logging_format             | 6.72 us                                                     | 6.64 us: 1.01x faster                                                  |
| pprint_pformat             | 1.05 sec                                                    | 1.03 sec: 1.01x faster                                                 |
| sympy_integrate            | 13.0 ms                                                     | 12.8 ms: 1.01x faster                                                  |
| regex_effbot               | 1.62 ms                                                     | 1.63 ms: 1.01x slower                                                  |
| async_generators           | 239 ms                                                      | 243 ms: 1.01x slower                                                   |
| 2to3                       | 218 ms                                                      | 221 ms: 1.01x slower                                                   |
| deltablue                  | 2.16 ms                                                     | 2.24 ms: 1.04x slower                                                  |
| sympy_expand               | 284 ms                                                      | 297 ms: 1.05x slower                                                   |
| django_template            | 22.9 ms                                                     | 24.0 ms: 1.05x slower                                                  |
| json_loads                 | 13.9 us                                                     | 14.6 us: 1.05x slower                                                  |
| pickle_pure_python         | 195 us                                                      | 205 us: 1.05x slower                                                   |
| telco                      | 4.13 ms                                                     | 4.41 ms: 1.07x slower                                                  |
| typing_runtime_protocols   | 95.1 us                                                     | 103 us: 1.08x slower                                                   |
| json_dumps                 | 5.70 ms                                                     | 6.47 ms: 1.14x slower                                                  |
| python_startup_no_site     | 16.2 ms                                                     | 19.3 ms: 1.18x slower                                                  |
| coverage                   | 40.8 ms                                                     | 50.2 ms: 1.23x slower                                                  |
| python_startup             | 19.5 ms                                                     | 25.8 ms: 1.32x slower                                                  |
| gc_traversal               | 1.52 ms                                                     | 2.17 ms: 1.43x slower                                                  |
| create_gc_cycles           | 752 us                                                      | 1.32 ms: 1.75x slower                                                  |
| logging_silent             | 60.5 ns                                                     | 314 ns: 5.19x slower                                                   |
| Geometric mean             | (ref)                                                       | 1.08x faster                                                           |

Benchmark hidden because not significant (8): logging_simple, docutils, scimark_lu, pycparser, hexiom, coroutines, json, regex_v8
Ignored benchmarks (21) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250619-3.15.0a0-d2c9ae9-JIT/bm-20250619-pythonperf1-amd64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.108x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: unknown