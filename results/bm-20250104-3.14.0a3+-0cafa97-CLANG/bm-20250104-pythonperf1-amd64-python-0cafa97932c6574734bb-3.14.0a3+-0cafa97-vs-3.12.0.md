# Results vs. 3.12.0

- fork: python
- ref: 0cafa97932c6574734bb
- machine: windows-amd64
- commit hash: 0cafa97
- commit date: 2025-01-04
- overall geometric mean: 1.009x slower
- HPT reliability: 99.29%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250104-pythonperf1-amd64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 235 ms: 1.08x slower                                                        |
| docutils       | 1.66 sec                                                    | 1.76 sec: 1.06x slower                                                      |
| Geometric mean | (ref)                                                       | 1.07x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250104-pythonperf1-amd64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 382 ms: 2.02x faster                                                        |
| async_tree_io              | 731 ms                                                      | 388 ms: 1.89x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 205 ms: 1.79x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 164 ms: 1.74x faster                                                        |
| async_tree_none            | 291 ms                                                      | 174 ms: 1.68x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 215 ms: 1.58x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 368 ms: 1.36x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 372 ms: 1.31x faster                                                        |
| Geometric mean             | (ref)                                                       | 1.65x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250104-pythonperf1-amd64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 52.8 ms: 1.07x faster                                                       |
| nbody          | 71.9 ms                                                     | 67.5 ms: 1.07x faster                                                       |
| pidigits       | 152 ms                                                      | 156 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                       | 1.04x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250104-pythonperf1-amd64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 87.9 ms: 1.00x slower                                                       |
| regex_dna      | 126 ms                                                      | 130 ms: 1.03x slower                                                        |
| regex_effbot   | 1.62 ms                                                     | 1.88 ms: 1.16x slower                                                       |
| regex_v8       | 14.2 ms                                                     | 23.4 ms: 1.64x slower                                                       |
| Geometric mean | (ref)                                                       | 1.18x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250104-pythonperf1-amd64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 1.37 sec                                                    | 1.38 sec: 1.01x slower                                                      |
| xml_etree_iterparse  | 65.2 ms                                                     | 69.5 ms: 1.07x slower                                                       |
| xml_etree_parse      | 93.0 ms                                                     | 103 ms: 1.11x slower                                                        |
| pickle_pure_python   | 195 us                                                      | 222 us: 1.14x slower                                                        |
| unpickle_pure_python | 133 us                                                      | 154 us: 1.15x slower                                                        |
| xml_etree_generate   | 55.8 ms                                                     | 66.0 ms: 1.18x slower                                                       |
| xml_etree_process    | 37.7 ms                                                     | 45.7 ms: 1.21x slower                                                       |
| json_dumps           | 5.70 ms                                                     | 7.84 ms: 1.38x slower                                                       |
| json_loads           | 13.9 us                                                     | 19.3 us: 1.39x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.18x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250104-pythonperf1-amd64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 18.6 ms: 1.15x slower                                                       |
| python_startup         | 19.5 ms                                                     | 25.6 ms: 1.32x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.23x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250104-pythonperf1-amd64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 22.9 ms                                                     | 24.8 ms: 1.08x slower                                                       |
| mako            | 7.09 ms                                                     | 8.22 ms: 1.16x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.12x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250104-pythonperf1-amd64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 382 ms: 2.02x faster                                                        |
| async_tree_io              | 731 ms                                                      | 388 ms: 1.89x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 205 ms: 1.79x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 164 ms: 1.74x faster                                                        |
| async_tree_none            | 291 ms                                                      | 174 ms: 1.68x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 215 ms: 1.58x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 368 ms: 1.36x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 372 ms: 1.31x faster                                                        |
| generators                 | 22.5 ms                                                     | 17.2 ms: 1.31x faster                                                       |
| deepcopy                   | 238 us                                                      | 184 us: 1.30x faster                                                        |
| go                         | 91.6 ms                                                     | 78.2 ms: 1.17x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 20.7 us: 1.14x faster                                                       |
| comprehensions             | 14.1 us                                                     | 12.5 us: 1.13x faster                                                       |
| raytrace                   | 192 ms                                                      | 177 ms: 1.09x faster                                                        |
| deepcopy_reduce            | 2.09 us                                                     | 1.93 us: 1.09x faster                                                       |
| float                      | 56.8 ms                                                     | 52.8 ms: 1.07x faster                                                       |
| deltablue                  | 2.16 ms                                                     | 2.02 ms: 1.07x faster                                                       |
| nbody                      | 71.9 ms                                                     | 67.5 ms: 1.07x faster                                                       |
| dulwich_log                | 44.3 ms                                                     | 42.2 ms: 1.05x faster                                                       |
| coroutines                 | 14.3 ms                                                     | 13.7 ms: 1.04x faster                                                       |
| meteor_contest             | 74.6 ms                                                     | 73.6 ms: 1.01x faster                                                       |
| logging_simple             | 6.28 us                                                     | 6.20 us: 1.01x faster                                                       |
| pathlib                    | 80.5 ms                                                     | 79.6 ms: 1.01x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.75 us: 1.01x faster                                                       |
| logging_format             | 6.72 us                                                     | 6.68 us: 1.00x faster                                                       |
| regex_compile              | 87.5 ms                                                     | 87.9 ms: 1.00x slower                                                       |
| scimark_sor                | 78.8 ms                                                     | 79.2 ms: 1.01x slower                                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 44.0 ms: 1.01x slower                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.38 sec: 1.01x slower                                                      |
| chaos                      | 43.3 ms                                                     | 43.9 ms: 1.01x slower                                                       |
| nqueens                    | 62.8 ms                                                     | 63.7 ms: 1.01x slower                                                       |
| pprint_pformat             | 1.05 sec                                                    | 1.07 sec: 1.02x slower                                                      |
| pidigits                   | 152 ms                                                      | 156 ms: 1.02x slower                                                        |
| regex_dna                  | 126 ms                                                      | 130 ms: 1.03x slower                                                        |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.63 ms: 1.03x slower                                                       |
| spectral_norm              | 66.9 ms                                                     | 68.9 ms: 1.03x slower                                                       |
| sympy_str                  | 175 ms                                                      | 180 ms: 1.03x slower                                                        |
| pprint_safe_repr           | 513 ms                                                      | 529 ms: 1.03x slower                                                        |
| sympy_integrate            | 13.0 ms                                                     | 13.5 ms: 1.04x slower                                                       |
| pycparser                  | 699 ms                                                      | 730 ms: 1.04x slower                                                        |
| async_generators           | 239 ms                                                      | 251 ms: 1.05x slower                                                        |
| sqlglot_transpile          | 1.02 ms                                                     | 1.07 ms: 1.05x slower                                                       |
| sqlglot_parse              | 804 us                                                      | 845 us: 1.05x slower                                                        |
| scimark_fft                | 184 ms                                                      | 195 ms: 1.05x slower                                                        |
| richards_super             | 32.1 ms                                                     | 33.9 ms: 1.06x slower                                                       |
| sqlglot_normalize          | 187 ms                                                      | 197 ms: 1.06x slower                                                        |
| sqlglot_optimize           | 34.5 ms                                                     | 36.6 ms: 1.06x slower                                                       |
| richards                   | 28.4 ms                                                     | 30.1 ms: 1.06x slower                                                       |
| docutils                   | 1.66 sec                                                    | 1.76 sec: 1.06x slower                                                      |
| hexiom                     | 4.10 ms                                                     | 4.37 ms: 1.07x slower                                                       |
| xml_etree_iterparse        | 65.2 ms                                                     | 69.5 ms: 1.07x slower                                                       |
| pyflate                    | 295 ms                                                      | 316 ms: 1.07x slower                                                        |
| 2to3                       | 218 ms                                                      | 235 ms: 1.08x slower                                                        |
| django_template            | 22.9 ms                                                     | 24.8 ms: 1.08x slower                                                       |
| sympy_expand               | 284 ms                                                      | 308 ms: 1.09x slower                                                        |
| xml_etree_parse            | 93.0 ms                                                     | 103 ms: 1.11x slower                                                        |
| logging_silent             | 60.5 ns                                                     | 67.3 ns: 1.11x slower                                                       |
| crypto_pyaes               | 48.5 ms                                                     | 54.8 ms: 1.13x slower                                                       |
| pickle_pure_python         | 195 us                                                      | 222 us: 1.14x slower                                                        |
| fannkuch                   | 247 ms                                                      | 283 ms: 1.15x slower                                                        |
| python_startup_no_site     | 16.2 ms                                                     | 18.6 ms: 1.15x slower                                                       |
| scimark_lu                 | 58.9 ms                                                     | 67.7 ms: 1.15x slower                                                       |
| unpickle_pure_python       | 133 us                                                      | 154 us: 1.15x slower                                                        |
| regex_effbot               | 1.62 ms                                                     | 1.88 ms: 1.16x slower                                                       |
| mako                       | 7.09 ms                                                     | 8.22 ms: 1.16x slower                                                       |
| xml_etree_generate         | 55.8 ms                                                     | 66.0 ms: 1.18x slower                                                       |
| json                       | 3.05 ms                                                     | 3.61 ms: 1.18x slower                                                       |
| xml_etree_process          | 37.7 ms                                                     | 45.7 ms: 1.21x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 115 us: 1.21x slower                                                        |
| mdp                        | 1.37 sec                                                    | 1.67 sec: 1.22x slower                                                      |
| coverage                   | 40.8 ms                                                     | 50.1 ms: 1.23x slower                                                       |
| telco                      | 4.13 ms                                                     | 5.24 ms: 1.27x slower                                                       |
| python_startup             | 19.5 ms                                                     | 25.6 ms: 1.32x slower                                                       |
| bench_mp_pool              | 69.2 ms                                                     | 93.9 ms: 1.36x slower                                                       |
| json_dumps                 | 5.70 ms                                                     | 7.84 ms: 1.38x slower                                                       |
| json_loads                 | 13.9 us                                                     | 19.3 us: 1.39x slower                                                       |
| regex_v8                   | 14.2 ms                                                     | 23.4 ms: 1.64x slower                                                       |
| gc_traversal               | 1.52 ms                                                     | 2.54 ms: 1.67x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 1.35 ms: 1.79x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.02x slower                                                                |

Benchmark hidden because not significant (2): bench_thread_pool, sympy_sum
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20250104-3.14.0a3+-0cafa97-CLANG/bm-20250104-pythonperf1-amd64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.009x slower

# HPT report

- Reliability score: 99.29% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown