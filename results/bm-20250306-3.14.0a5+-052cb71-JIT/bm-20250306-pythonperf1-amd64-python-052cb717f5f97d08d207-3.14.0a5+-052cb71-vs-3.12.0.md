# Results vs. 3.12.0

- fork: python
- ref: 052cb717f5f97d08d207
- machine: windows-amd64
- commit hash: 052cb71
- commit date: 2025-03-06
- overall geometric mean: 1.053x faster
- HPT reliability: 84.20%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250306-pythonperf1-amd64-python-052cb717f5f97d08d207-3.14.0a5+-052cb71 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 224 ms: 1.03x slower                                                        |
| docutils       | 1.66 sec                                                    | 1.74 sec: 1.05x slower                                                      |
| Geometric mean | (ref)                                                       | 1.04x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250306-pythonperf1-amd64-python-052cb717f5f97d08d207-3.14.0a5+-052cb71 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 406 ms: 1.90x faster                                                        |
| async_tree_io              | 731 ms                                                      | 419 ms: 1.74x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 215 ms: 1.70x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 177 ms: 1.61x faster                                                        |
| async_tree_none            | 291 ms                                                      | 188 ms: 1.55x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 220 ms: 1.54x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 347 ms: 1.45x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 344 ms: 1.42x faster                                                        |
| Geometric mean             | (ref)                                                       | 1.61x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250306-pythonperf1-amd64-python-052cb717f5f97d08d207-3.14.0a5+-052cb71 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 41.3 ms: 1.38x faster                                                       |
| nbody          | 71.9 ms                                                     | 59.7 ms: 1.20x faster                                                       |
| Geometric mean | (ref)                                                       | 1.18x faster                                                                |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250306-pythonperf1-amd64-python-052cb717f5f97d08d207-3.14.0a5+-052cb71 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.48 ms: 1.09x faster                                                       |
| regex_compile  | 87.5 ms                                                     | 85.2 ms: 1.03x faster                                                       |
| regex_v8       | 14.2 ms                                                     | 15.3 ms: 1.07x slower                                                       |
| Geometric mean | (ref)                                                       | 1.01x faster                                                                |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250306-pythonperf1-amd64-python-052cb717f5f97d08d207-3.14.0a5+-052cb71 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 133 us                                                      | 116 us: 1.15x faster                                                        |
| tomli_loads          | 1.37 sec                                                    | 1.24 sec: 1.10x faster                                                      |
| xml_etree_generate   | 55.8 ms                                                     | 52.7 ms: 1.06x faster                                                       |
| xml_etree_iterparse  | 65.2 ms                                                     | 63.8 ms: 1.02x faster                                                       |
| xml_etree_parse      | 93.0 ms                                                     | 92.1 ms: 1.01x faster                                                       |
| xml_etree_process    | 37.7 ms                                                     | 37.4 ms: 1.01x faster                                                       |
| json_loads           | 13.9 us                                                     | 14.6 us: 1.05x slower                                                       |
| pickle_pure_python   | 195 us                                                      | 219 us: 1.12x slower                                                        |
| json_dumps           | 5.70 ms                                                     | 6.88 ms: 1.21x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.00x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250306-pythonperf1-amd64-python-052cb717f5f97d08d207-3.14.0a5+-052cb71 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 20.2 ms: 1.24x slower                                                       |
| python_startup         | 19.5 ms                                                     | 26.1 ms: 1.34x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.29x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250306-pythonperf1-amd64-python-052cb717f5f97d08d207-3.14.0a5+-052cb71 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.35 ms: 1.32x faster                                                       |
| django_template | 22.9 ms                                                     | 25.9 ms: 1.13x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.08x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250306-pythonperf1-amd64-python-052cb717f5f97d08d207-3.14.0a5+-052cb71 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 32.2 ms: 2.50x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 406 ms: 1.90x faster                                                        |
| async_tree_io              | 731 ms                                                      | 419 ms: 1.74x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 215 ms: 1.70x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 177 ms: 1.61x faster                                                        |
| async_tree_none            | 291 ms                                                      | 188 ms: 1.55x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 220 ms: 1.54x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 347 ms: 1.45x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 344 ms: 1.42x faster                                                        |
| float                      | 56.8 ms                                                     | 41.3 ms: 1.38x faster                                                       |
| mako                       | 7.09 ms                                                     | 5.35 ms: 1.32x faster                                                       |
| deepcopy                   | 238 us                                                      | 189 us: 1.26x faster                                                        |
| comprehensions             | 14.1 us                                                     | 11.5 us: 1.23x faster                                                       |
| nbody                      | 71.9 ms                                                     | 59.7 ms: 1.20x faster                                                       |
| scimark_fft                | 184 ms                                                      | 156 ms: 1.18x faster                                                        |
| deepcopy_memo              | 23.7 us                                                     | 20.1 us: 1.18x faster                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.18 ms: 1.17x faster                                                       |
| unpickle_pure_python       | 133 us                                                      | 116 us: 1.15x faster                                                        |
| sqlite_synth               | 1.76 us                                                     | 1.55 us: 1.14x faster                                                       |
| generators                 | 22.5 ms                                                     | 20.3 ms: 1.11x faster                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.24 sec: 1.10x faster                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.48 ms: 1.09x faster                                                       |
| pprint_pformat             | 1.05 sec                                                    | 974 ms: 1.07x faster                                                        |
| spectral_norm              | 66.9 ms                                                     | 62.5 ms: 1.07x faster                                                       |
| xml_etree_generate         | 55.8 ms                                                     | 52.7 ms: 1.06x faster                                                       |
| deepcopy_reduce            | 2.09 us                                                     | 1.99 us: 1.05x faster                                                       |
| pprint_safe_repr           | 513 ms                                                      | 488 ms: 1.05x faster                                                        |
| pyflate                    | 295 ms                                                      | 281 ms: 1.05x faster                                                        |
| coroutines                 | 14.3 ms                                                     | 13.7 ms: 1.04x faster                                                       |
| json                       | 3.05 ms                                                     | 2.96 ms: 1.03x faster                                                       |
| regex_compile              | 87.5 ms                                                     | 85.2 ms: 1.03x faster                                                       |
| chaos                      | 43.3 ms                                                     | 42.2 ms: 1.03x faster                                                       |
| xml_etree_iterparse        | 65.2 ms                                                     | 63.8 ms: 1.02x faster                                                       |
| dulwich_log                | 44.3 ms                                                     | 43.7 ms: 1.01x faster                                                       |
| sympy_sum                  | 91.5 ms                                                     | 90.3 ms: 1.01x faster                                                       |
| xml_etree_parse            | 93.0 ms                                                     | 92.1 ms: 1.01x faster                                                       |
| crypto_pyaes               | 48.5 ms                                                     | 48.1 ms: 1.01x faster                                                       |
| xml_etree_process          | 37.7 ms                                                     | 37.4 ms: 1.01x faster                                                       |
| raytrace                   | 192 ms                                                      | 194 ms: 1.01x slower                                                        |
| fannkuch                   | 247 ms                                                      | 250 ms: 1.01x slower                                                        |
| sympy_str                  | 175 ms                                                      | 178 ms: 1.02x slower                                                        |
| meteor_contest             | 74.6 ms                                                     | 76.7 ms: 1.03x slower                                                       |
| 2to3                       | 218 ms                                                      | 224 ms: 1.03x slower                                                        |
| scimark_monte_carlo        | 43.7 ms                                                     | 45.6 ms: 1.04x slower                                                       |
| sympy_integrate            | 13.0 ms                                                     | 13.5 ms: 1.04x slower                                                       |
| docutils                   | 1.66 sec                                                    | 1.74 sec: 1.05x slower                                                      |
| json_loads                 | 13.9 us                                                     | 14.6 us: 1.05x slower                                                       |
| logging_format             | 6.72 us                                                     | 7.07 us: 1.05x slower                                                       |
| logging_simple             | 6.28 us                                                     | 6.62 us: 1.06x slower                                                       |
| deltablue                  | 2.16 ms                                                     | 2.28 ms: 1.06x slower                                                       |
| sqlglot_parse              | 804 us                                                      | 853 us: 1.06x slower                                                        |
| telco                      | 4.13 ms                                                     | 4.39 ms: 1.06x slower                                                       |
| sqlglot_normalize          | 187 ms                                                      | 199 ms: 1.06x slower                                                        |
| sqlglot_optimize           | 34.5 ms                                                     | 36.9 ms: 1.07x slower                                                       |
| regex_v8                   | 14.2 ms                                                     | 15.3 ms: 1.07x slower                                                       |
| sqlglot_transpile          | 1.02 ms                                                     | 1.10 ms: 1.07x slower                                                       |
| pycparser                  | 699 ms                                                      | 750 ms: 1.07x slower                                                        |
| richards                   | 28.4 ms                                                     | 30.6 ms: 1.08x slower                                                       |
| richards_super             | 32.1 ms                                                     | 34.7 ms: 1.08x slower                                                       |
| sympy_expand               | 284 ms                                                      | 308 ms: 1.08x slower                                                        |
| hexiom                     | 4.10 ms                                                     | 4.46 ms: 1.09x slower                                                       |
| logging_silent             | 60.5 ns                                                     | 66.0 ns: 1.09x slower                                                       |
| scimark_lu                 | 58.9 ms                                                     | 65.0 ms: 1.10x slower                                                       |
| scimark_sor                | 78.8 ms                                                     | 87.4 ms: 1.11x slower                                                       |
| pickle_pure_python         | 195 us                                                      | 219 us: 1.12x slower                                                        |
| django_template            | 22.9 ms                                                     | 25.9 ms: 1.13x slower                                                       |
| mdp                        | 1.37 sec                                                    | 1.58 sec: 1.15x slower                                                      |
| typing_runtime_protocols   | 95.1 us                                                     | 110 us: 1.15x slower                                                        |
| coverage                   | 40.8 ms                                                     | 48.9 ms: 1.20x slower                                                       |
| json_dumps                 | 5.70 ms                                                     | 6.88 ms: 1.21x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                     | 20.2 ms: 1.24x slower                                                       |
| bench_mp_pool              | 69.2 ms                                                     | 87.3 ms: 1.26x slower                                                       |
| python_startup             | 19.5 ms                                                     | 26.1 ms: 1.34x slower                                                       |
| gc_traversal               | 1.52 ms                                                     | 2.09 ms: 1.37x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 1.24 ms: 1.65x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.05x faster                                                                |

Benchmark hidden because not significant (6): regex_dna, go, bench_thread_pool, nqueens, async_generators, pidigits
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20250306-3.14.0a5+-052cb71-JIT/bm-20250306-pythonperf1-amd64-python-052cb717f5f97d08d207-3.14.0a5+-052cb71.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.053x faster

# HPT report

- Reliability score: 84.20% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown