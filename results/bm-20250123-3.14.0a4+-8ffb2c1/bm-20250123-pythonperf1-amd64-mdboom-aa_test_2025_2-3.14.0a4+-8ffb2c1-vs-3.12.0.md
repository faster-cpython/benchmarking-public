# Results vs. 3.12.0

- fork: mdboom
- ref: aa_test_2025_2
- machine: windows-amd64
- commit hash: 8ffb2c1
- commit date: 2025-01-23
- overall geometric mean: 1.006x faster
- HPT reliability: 94.14%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250123-pythonperf1-amd64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 233 ms: 1.07x slower                                                  |
| docutils       | 1.66 sec                                                    | 1.70 sec: 1.02x slower                                                |
| Geometric mean | (ref)                                                       | 1.04x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250123-pythonperf1-amd64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 404 ms: 1.91x faster                                                  |
| async_tree_io              | 731 ms                                                      | 413 ms: 1.77x faster                                                  |
| async_tree_memoization_tg  | 367 ms                                                      | 214 ms: 1.72x faster                                                  |
| async_tree_none_tg         | 285 ms                                                      | 175 ms: 1.63x faster                                                  |
| async_tree_none            | 291 ms                                                      | 186 ms: 1.56x faster                                                  |
| async_tree_memoization     | 339 ms                                                      | 226 ms: 1.50x faster                                                  |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 348 ms: 1.44x faster                                                  |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 347 ms: 1.41x faster                                                  |
| Geometric mean             | (ref)                                                       | 1.61x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250123-pythonperf1-amd64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 51.4 ms: 1.11x faster                                                 |
| pidigits       | 152 ms                                                      | 148 ms: 1.03x faster                                                  |
| nbody          | 71.9 ms                                                     | 77.3 ms: 1.07x slower                                                 |
| Geometric mean | (ref)                                                       | 1.02x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250123-pythonperf1-amd64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.46 ms: 1.11x faster                                                 |
| regex_dna      | 126 ms                                                      | 117 ms: 1.08x faster                                                  |
| regex_compile  | 87.5 ms                                                     | 88.2 ms: 1.01x slower                                                 |
| regex_v8       | 14.2 ms                                                     | 16.5 ms: 1.16x slower                                                 |
| Geometric mean | (ref)                                                       | 1.01x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250123-pythonperf1-amd64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_parse      | 93.0 ms                                                     | 88.5 ms: 1.05x faster                                                 |
| tomli_loads          | 1.37 sec                                                    | 1.39 sec: 1.01x slower                                                |
| json_loads           | 13.9 us                                                     | 14.5 us: 1.04x slower                                                 |
| xml_etree_generate   | 55.8 ms                                                     | 59.4 ms: 1.06x slower                                                 |
| xml_etree_process    | 37.7 ms                                                     | 43.7 ms: 1.16x slower                                                 |
| unpickle_pure_python | 133 us                                                      | 159 us: 1.19x slower                                                  |
| json_dumps           | 5.70 ms                                                     | 6.82 ms: 1.20x slower                                                 |
| pickle_pure_python   | 195 us                                                      | 239 us: 1.22x slower                                                  |
| Geometric mean       | (ref)                                                       | 1.09x slower                                                          |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250123-pythonperf1-amd64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 18.0 ms: 1.11x slower                                                 |
| python_startup         | 19.5 ms                                                     | 24.3 ms: 1.25x slower                                                 |
| Geometric mean         | (ref)                                                       | 1.17x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250123-pythonperf1-amd64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.89 ms: 1.03x faster                                                 |
| django_template | 22.9 ms                                                     | 25.9 ms: 1.13x slower                                                 |
| Geometric mean  | (ref)                                                       | 1.05x slower                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250123-pythonperf1-amd64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 404 ms: 1.91x faster                                                  |
| async_tree_io              | 731 ms                                                      | 413 ms: 1.77x faster                                                  |
| async_tree_memoization_tg  | 367 ms                                                      | 214 ms: 1.72x faster                                                  |
| async_tree_none_tg         | 285 ms                                                      | 175 ms: 1.63x faster                                                  |
| async_tree_none            | 291 ms                                                      | 186 ms: 1.56x faster                                                  |
| async_tree_memoization     | 339 ms                                                      | 226 ms: 1.50x faster                                                  |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 348 ms: 1.44x faster                                                  |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 347 ms: 1.41x faster                                                  |
| deepcopy                   | 238 us                                                      | 184 us: 1.29x faster                                                  |
| deepcopy_memo              | 23.7 us                                                     | 20.0 us: 1.19x faster                                                 |
| comprehensions             | 14.1 us                                                     | 12.4 us: 1.14x faster                                                 |
| deepcopy_reduce            | 2.09 us                                                     | 1.86 us: 1.13x faster                                                 |
| regex_effbot               | 1.62 ms                                                     | 1.46 ms: 1.11x faster                                                 |
| float                      | 56.8 ms                                                     | 51.4 ms: 1.11x faster                                                 |
| regex_dna                  | 126 ms                                                      | 117 ms: 1.08x faster                                                  |
| async_generators           | 239 ms                                                      | 225 ms: 1.06x faster                                                  |
| spectral_norm              | 66.9 ms                                                     | 63.4 ms: 1.06x faster                                                 |
| xml_etree_parse            | 93.0 ms                                                     | 88.5 ms: 1.05x faster                                                 |
| generators                 | 22.5 ms                                                     | 21.6 ms: 1.04x faster                                                 |
| dulwich_log                | 44.3 ms                                                     | 42.5 ms: 1.04x faster                                                 |
| chaos                      | 43.3 ms                                                     | 41.7 ms: 1.04x faster                                                 |
| go                         | 91.6 ms                                                     | 88.5 ms: 1.03x faster                                                 |
| pathlib                    | 80.5 ms                                                     | 77.9 ms: 1.03x faster                                                 |
| json                       | 3.05 ms                                                     | 2.95 ms: 1.03x faster                                                 |
| mako                       | 7.09 ms                                                     | 6.89 ms: 1.03x faster                                                 |
| pidigits                   | 152 ms                                                      | 148 ms: 1.03x faster                                                  |
| bench_thread_pool          | 857 us                                                      | 834 us: 1.03x faster                                                  |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.50 ms: 1.02x faster                                                 |
| sqlite_synth               | 1.76 us                                                     | 1.74 us: 1.01x faster                                                 |
| crypto_pyaes               | 48.5 ms                                                     | 48.0 ms: 1.01x faster                                                 |
| regex_compile              | 87.5 ms                                                     | 88.2 ms: 1.01x slower                                                 |
| meteor_contest             | 74.6 ms                                                     | 75.5 ms: 1.01x slower                                                 |
| tomli_loads                | 1.37 sec                                                    | 1.39 sec: 1.01x slower                                                |
| scimark_fft                | 184 ms                                                      | 187 ms: 1.02x slower                                                  |
| docutils                   | 1.66 sec                                                    | 1.70 sec: 1.02x slower                                                |
| sympy_str                  | 175 ms                                                      | 179 ms: 1.02x slower                                                  |
| nqueens                    | 62.8 ms                                                     | 64.6 ms: 1.03x slower                                                 |
| logging_format             | 6.72 us                                                     | 6.99 us: 1.04x slower                                                 |
| logging_simple             | 6.28 us                                                     | 6.53 us: 1.04x slower                                                 |
| json_loads                 | 13.9 us                                                     | 14.5 us: 1.04x slower                                                 |
| pprint_safe_repr           | 513 ms                                                      | 536 ms: 1.05x slower                                                  |
| pprint_pformat             | 1.05 sec                                                    | 1.10 sec: 1.05x slower                                                |
| pyflate                    | 295 ms                                                      | 310 ms: 1.05x slower                                                  |
| sympy_integrate            | 13.0 ms                                                     | 13.6 ms: 1.05x slower                                                 |
| pycparser                  | 699 ms                                                      | 737 ms: 1.05x slower                                                  |
| xml_etree_generate         | 55.8 ms                                                     | 59.4 ms: 1.06x slower                                                 |
| sqlglot_optimize           | 34.5 ms                                                     | 36.7 ms: 1.06x slower                                                 |
| sqlglot_normalize          | 187 ms                                                      | 199 ms: 1.06x slower                                                  |
| 2to3                       | 218 ms                                                      | 233 ms: 1.07x slower                                                  |
| coroutines                 | 14.3 ms                                                     | 15.3 ms: 1.07x slower                                                 |
| sympy_expand               | 284 ms                                                      | 305 ms: 1.07x slower                                                  |
| nbody                      | 71.9 ms                                                     | 77.3 ms: 1.07x slower                                                 |
| sqlglot_transpile          | 1.02 ms                                                     | 1.10 ms: 1.08x slower                                                 |
| scimark_monte_carlo        | 43.7 ms                                                     | 47.3 ms: 1.08x slower                                                 |
| raytrace                   | 192 ms                                                      | 209 ms: 1.09x slower                                                  |
| fannkuch                   | 247 ms                                                      | 269 ms: 1.09x slower                                                  |
| scimark_lu                 | 58.9 ms                                                     | 64.9 ms: 1.10x slower                                                 |
| deltablue                  | 2.16 ms                                                     | 2.38 ms: 1.10x slower                                                 |
| hexiom                     | 4.10 ms                                                     | 4.54 ms: 1.11x slower                                                 |
| sqlglot_parse              | 804 us                                                      | 890 us: 1.11x slower                                                  |
| python_startup_no_site     | 16.2 ms                                                     | 18.0 ms: 1.11x slower                                                 |
| richards_super             | 32.1 ms                                                     | 35.8 ms: 1.11x slower                                                 |
| scimark_sor                | 78.8 ms                                                     | 87.8 ms: 1.12x slower                                                 |
| richards                   | 28.4 ms                                                     | 31.8 ms: 1.12x slower                                                 |
| django_template            | 22.9 ms                                                     | 25.9 ms: 1.13x slower                                                 |
| mdp                        | 1.37 sec                                                    | 1.56 sec: 1.14x slower                                                |
| xml_etree_process          | 37.7 ms                                                     | 43.7 ms: 1.16x slower                                                 |
| regex_v8                   | 14.2 ms                                                     | 16.5 ms: 1.16x slower                                                 |
| typing_runtime_protocols   | 95.1 us                                                     | 111 us: 1.17x slower                                                  |
| unpickle_pure_python       | 133 us                                                      | 159 us: 1.19x slower                                                  |
| json_dumps                 | 5.70 ms                                                     | 6.82 ms: 1.20x slower                                                 |
| logging_silent             | 60.5 ns                                                     | 72.5 ns: 1.20x slower                                                 |
| coverage                   | 40.8 ms                                                     | 49.4 ms: 1.21x slower                                                 |
| pickle_pure_python         | 195 us                                                      | 239 us: 1.22x slower                                                  |
| python_startup             | 19.5 ms                                                     | 24.3 ms: 1.25x slower                                                 |
| bench_mp_pool              | 69.2 ms                                                     | 88.0 ms: 1.27x slower                                                 |
| gc_traversal               | 1.52 ms                                                     | 2.00 ms: 1.31x slower                                                 |
| telco                      | 4.13 ms                                                     | 5.44 ms: 1.32x slower                                                 |
| create_gc_cycles           | 752 us                                                      | 1.22 ms: 1.62x slower                                                 |
| Geometric mean             | (ref)                                                       | 1.00x faster                                                          |

Benchmark hidden because not significant (2): sympy_sum, xml_etree_iterparse
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20250123-3.14.0a4+-8ffb2c1/bm-20250123-pythonperf1-amd64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.006x faster

# HPT report

- Reliability score: 94.14% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown