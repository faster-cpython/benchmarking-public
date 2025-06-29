# Results vs. 3.12.0

- fork: gpshead
- ref: traceback_timestamps
- machine: windows-amd64
- commit hash: e4f54d4
- commit date: 2025-06-08
- overall geometric mean: 1.063x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.02x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250608-pythonperf1-amd64-gpshead-traceback_timestamps-3.15.0a0-e4f54d4 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 222 ms: 1.02x slower                                                        |
| docutils       | 1.66 sec                                                    | 1.62 sec: 1.03x faster                                                      |
| Geometric mean | (ref)                                                       | 1.01x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250608-pythonperf1-amd64-gpshead-traceback_timestamps-3.15.0a0-e4f54d4 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 392 ms: 1.97x faster                                                        |
| async_tree_io              | 731 ms                                                      | 389 ms: 1.88x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 208 ms: 1.76x faster                                                        |
| async_tree_none            | 291 ms                                                      | 170 ms: 1.71x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 171 ms: 1.67x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 206 ms: 1.65x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 338 ms: 1.49x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 331 ms: 1.48x faster                                                        |
| Geometric mean             | (ref)                                                       | 1.69x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250608-pythonperf1-amd64-gpshead-traceback_timestamps-3.15.0a0-e4f54d4 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 44.0 ms: 1.29x faster                                                       |
| nbody          | 71.9 ms                                                     | 62.8 ms: 1.14x faster                                                       |
| pidigits       | 152 ms                                                      | 149 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                       | 1.15x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250608-pythonperf1-amd64-gpshead-traceback_timestamps-3.15.0a0-e4f54d4 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 80.4 ms: 1.09x faster                                                       |
| regex_effbot   | 1.62 ms                                                     | 1.53 ms: 1.06x faster                                                       |
| regex_dna      | 126 ms                                                      | 121 ms: 1.05x faster                                                        |
| regex_v8       | 14.2 ms                                                     | 13.9 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                       | 1.05x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250608-pythonperf1-amd64-gpshead-traceback_timestamps-3.15.0a0-e4f54d4 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_parse      | 93.0 ms                                                     | 89.7 ms: 1.04x faster                                                       |
| json_loads           | 13.9 us                                                     | 14.1 us: 1.02x slower                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.39 sec: 1.02x slower                                                      |
| unpickle_pure_python | 133 us                                                      | 137 us: 1.03x slower                                                        |
| xml_etree_process    | 37.7 ms                                                     | 39.0 ms: 1.03x slower                                                       |
| pickle_pure_python   | 195 us                                                      | 212 us: 1.08x slower                                                        |
| json_dumps           | 5.70 ms                                                     | 6.31 ms: 1.11x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.03x slower                                                                |

Benchmark hidden because not significant (2): xml_etree_iterparse, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250608-pythonperf1-amd64-gpshead-traceback_timestamps-3.15.0a0-e4f54d4 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 19.6 ms: 1.21x slower                                                       |
| python_startup         | 19.5 ms                                                     | 26.2 ms: 1.35x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.28x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250608-pythonperf1-amd64-gpshead-traceback_timestamps-3.15.0a0-e4f54d4 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.65 ms: 1.07x faster                                                       |
| django_template | 22.9 ms                                                     | 24.0 ms: 1.04x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.01x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250608-pythonperf1-amd64-gpshead-traceback_timestamps-3.15.0a0-e4f54d4 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 32.4 ms: 2.48x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 392 ms: 1.97x faster                                                        |
| async_tree_io              | 731 ms                                                      | 389 ms: 1.88x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 208 ms: 1.76x faster                                                        |
| mdp                        | 1.37 sec                                                    | 801 ms: 1.71x faster                                                        |
| async_tree_none            | 291 ms                                                      | 170 ms: 1.71x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 171 ms: 1.67x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 206 ms: 1.65x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 338 ms: 1.49x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 331 ms: 1.48x faster                                                        |
| deepcopy                   | 238 us                                                      | 171 us: 1.40x faster                                                        |
| comprehensions             | 14.1 us                                                     | 10.9 us: 1.30x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 18.3 us: 1.30x faster                                                       |
| float                      | 56.8 ms                                                     | 44.0 ms: 1.29x faster                                                       |
| go                         | 91.6 ms                                                     | 77.3 ms: 1.18x faster                                                       |
| generators                 | 22.5 ms                                                     | 19.5 ms: 1.16x faster                                                       |
| nbody                      | 71.9 ms                                                     | 62.8 ms: 1.14x faster                                                       |
| deepcopy_reduce            | 2.09 us                                                     | 1.84 us: 1.14x faster                                                       |
| spectral_norm              | 66.9 ms                                                     | 60.1 ms: 1.11x faster                                                       |
| regex_compile              | 87.5 ms                                                     | 80.4 ms: 1.09x faster                                                       |
| chaos                      | 43.3 ms                                                     | 39.8 ms: 1.09x faster                                                       |
| dulwich_log                | 44.3 ms                                                     | 40.9 ms: 1.08x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.64 us: 1.08x faster                                                       |
| mako                       | 7.09 ms                                                     | 6.65 ms: 1.07x faster                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.53 ms: 1.06x faster                                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 41.5 ms: 1.05x faster                                                       |
| raytrace                   | 192 ms                                                      | 183 ms: 1.05x faster                                                        |
| sympy_integrate            | 13.0 ms                                                     | 12.3 ms: 1.05x faster                                                       |
| regex_dna                  | 126 ms                                                      | 121 ms: 1.05x faster                                                        |
| sympy_sum                  | 91.5 ms                                                     | 87.4 ms: 1.05x faster                                                       |
| scimark_sor                | 78.8 ms                                                     | 75.2 ms: 1.05x faster                                                       |
| sympy_str                  | 175 ms                                                      | 168 ms: 1.04x faster                                                        |
| xml_etree_parse            | 93.0 ms                                                     | 89.7 ms: 1.04x faster                                                       |
| scimark_fft                | 184 ms                                                      | 178 ms: 1.03x faster                                                        |
| async_generators           | 239 ms                                                      | 232 ms: 1.03x faster                                                        |
| docutils                   | 1.66 sec                                                    | 1.62 sec: 1.03x faster                                                      |
| coroutines                 | 14.3 ms                                                     | 13.9 ms: 1.03x faster                                                       |
| pyflate                    | 295 ms                                                      | 287 ms: 1.03x faster                                                        |
| pidigits                   | 152 ms                                                      | 149 ms: 1.02x faster                                                        |
| scimark_lu                 | 58.9 ms                                                     | 57.4 ms: 1.02x faster                                                       |
| richards                   | 28.4 ms                                                     | 27.7 ms: 1.02x faster                                                       |
| regex_v8                   | 14.2 ms                                                     | 13.9 ms: 1.02x faster                                                       |
| nqueens                    | 62.8 ms                                                     | 61.6 ms: 1.02x faster                                                       |
| crypto_pyaes               | 48.5 ms                                                     | 47.6 ms: 1.02x faster                                                       |
| richards_super             | 32.1 ms                                                     | 31.5 ms: 1.02x faster                                                       |
| meteor_contest             | 74.6 ms                                                     | 73.4 ms: 1.02x faster                                                       |
| hexiom                     | 4.10 ms                                                     | 4.14 ms: 1.01x slower                                                       |
| logging_format             | 6.72 us                                                     | 6.79 us: 1.01x slower                                                       |
| json_loads                 | 13.9 us                                                     | 14.1 us: 1.02x slower                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.39 sec: 1.02x slower                                                      |
| 2to3                       | 218 ms                                                      | 222 ms: 1.02x slower                                                        |
| unpickle_pure_python       | 133 us                                                      | 137 us: 1.03x slower                                                        |
| deltablue                  | 2.16 ms                                                     | 2.23 ms: 1.03x slower                                                       |
| xml_etree_process          | 37.7 ms                                                     | 39.0 ms: 1.03x slower                                                       |
| fannkuch                   | 247 ms                                                      | 256 ms: 1.04x slower                                                        |
| django_template            | 22.9 ms                                                     | 24.0 ms: 1.04x slower                                                       |
| pprint_pformat             | 1.05 sec                                                    | 1.12 sec: 1.07x slower                                                      |
| pprint_safe_repr           | 513 ms                                                      | 554 ms: 1.08x slower                                                        |
| typing_runtime_protocols   | 95.1 us                                                     | 103 us: 1.08x slower                                                        |
| pickle_pure_python         | 195 us                                                      | 212 us: 1.08x slower                                                        |
| telco                      | 4.13 ms                                                     | 4.57 ms: 1.11x slower                                                       |
| json_dumps                 | 5.70 ms                                                     | 6.31 ms: 1.11x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                     | 19.6 ms: 1.21x slower                                                       |
| python_startup             | 19.5 ms                                                     | 26.2 ms: 1.35x slower                                                       |
| gc_traversal               | 1.52 ms                                                     | 2.17 ms: 1.43x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 1.32 ms: 1.76x slower                                                       |
| logging_silent             | 60.5 ns                                                     | 324 ns: 5.35x slower                                                        |
| coverage                   | 40.8 ms                                                     | 291 ms: 7.13x slower                                                        |
| Geometric mean             | (ref)                                                       | 1.04x faster                                                                |

Benchmark hidden because not significant (7): xml_etree_iterparse, json, xml_etree_generate, scimark_sparse_mat_mult, sympy_expand, logging_simple, pycparser
Ignored benchmarks (21) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250608-3.15.0a0-e4f54d4/bm-20250608-pythonperf1-amd64-gpshead-traceback_timestamps-3.15.0a0-e4f54d4.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.063x faster

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: unknown