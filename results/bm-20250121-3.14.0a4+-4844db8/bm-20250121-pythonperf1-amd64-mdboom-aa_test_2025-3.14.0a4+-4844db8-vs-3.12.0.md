# Results vs. 3.12.0

- fork: mdboom
- ref: aa_test_2025
- machine: windows-amd64
- commit hash: 4844db8
- commit date: 2025-01-21
- overall geometric mean: 1.004x faster
- HPT reliability: 95.85%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250121-pythonperf1-amd64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 232 ms: 1.07x slower                                                |
| docutils       | 1.66 sec                                                    | 1.69 sec: 1.02x slower                                              |
| Geometric mean | (ref)                                                       | 1.04x slower                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250121-pythonperf1-amd64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 402 ms: 1.92x faster                                                |
| async_tree_io              | 731 ms                                                      | 414 ms: 1.77x faster                                                |
| async_tree_memoization_tg  | 367 ms                                                      | 213 ms: 1.72x faster                                                |
| async_tree_none_tg         | 285 ms                                                      | 174 ms: 1.64x faster                                                |
| async_tree_none            | 291 ms                                                      | 186 ms: 1.57x faster                                                |
| async_tree_memoization     | 339 ms                                                      | 226 ms: 1.50x faster                                                |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 346 ms: 1.45x faster                                                |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 348 ms: 1.40x faster                                                |
| Geometric mean             | (ref)                                                       | 1.61x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250121-pythonperf1-amd64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 51.6 ms: 1.10x faster                                               |
| pidigits       | 152 ms                                                      | 146 ms: 1.04x faster                                                |
| nbody          | 71.9 ms                                                     | 74.5 ms: 1.04x slower                                               |
| Geometric mean | (ref)                                                       | 1.03x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250121-pythonperf1-amd64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 115 ms: 1.10x faster                                                |
| regex_effbot   | 1.62 ms                                                     | 1.47 ms: 1.10x faster                                               |
| regex_compile  | 87.5 ms                                                     | 87.9 ms: 1.00x slower                                               |
| regex_v8       | 14.2 ms                                                     | 14.8 ms: 1.04x slower                                               |
| Geometric mean | (ref)                                                       | 1.04x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250121-pythonperf1-amd64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------:|
| xml_etree_parse      | 93.0 ms                                                     | 89.4 ms: 1.04x faster                                               |
| tomli_loads          | 1.37 sec                                                    | 1.40 sec: 1.03x slower                                              |
| json_loads           | 13.9 us                                                     | 14.4 us: 1.04x slower                                               |
| xml_etree_generate   | 55.8 ms                                                     | 60.3 ms: 1.08x slower                                               |
| xml_etree_process    | 37.7 ms                                                     | 43.3 ms: 1.15x slower                                               |
| json_dumps           | 5.70 ms                                                     | 6.89 ms: 1.21x slower                                               |
| unpickle_pure_python | 133 us                                                      | 162 us: 1.21x slower                                                |
| pickle_pure_python   | 195 us                                                      | 238 us: 1.22x slower                                                |
| Geometric mean       | (ref)                                                       | 1.09x slower                                                        |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250121-pythonperf1-amd64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 18.2 ms: 1.12x slower                                               |
| python_startup         | 19.5 ms                                                     | 24.4 ms: 1.25x slower                                               |
| Geometric mean         | (ref)                                                       | 1.18x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250121-pythonperf1-amd64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|-----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.97 ms: 1.02x faster                                               |
| django_template | 22.9 ms                                                     | 25.9 ms: 1.13x slower                                               |
| Geometric mean  | (ref)                                                       | 1.05x slower                                                        |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250121-pythonperf1-amd64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 402 ms: 1.92x faster                                                |
| async_tree_io              | 731 ms                                                      | 414 ms: 1.77x faster                                                |
| async_tree_memoization_tg  | 367 ms                                                      | 213 ms: 1.72x faster                                                |
| async_tree_none_tg         | 285 ms                                                      | 174 ms: 1.64x faster                                                |
| async_tree_none            | 291 ms                                                      | 186 ms: 1.57x faster                                                |
| async_tree_memoization     | 339 ms                                                      | 226 ms: 1.50x faster                                                |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 346 ms: 1.45x faster                                                |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 348 ms: 1.40x faster                                                |
| deepcopy                   | 238 us                                                      | 189 us: 1.26x faster                                                |
| deepcopy_memo              | 23.7 us                                                     | 20.3 us: 1.17x faster                                               |
| comprehensions             | 14.1 us                                                     | 12.6 us: 1.13x faster                                               |
| deepcopy_reduce            | 2.09 us                                                     | 1.89 us: 1.11x faster                                               |
| sqlite_synth               | 1.76 us                                                     | 1.60 us: 1.10x faster                                               |
| regex_dna                  | 126 ms                                                      | 115 ms: 1.10x faster                                                |
| float                      | 56.8 ms                                                     | 51.6 ms: 1.10x faster                                               |
| regex_effbot               | 1.62 ms                                                     | 1.47 ms: 1.10x faster                                               |
| spectral_norm              | 66.9 ms                                                     | 63.7 ms: 1.05x faster                                               |
| generators                 | 22.5 ms                                                     | 21.5 ms: 1.05x faster                                               |
| pidigits                   | 152 ms                                                      | 146 ms: 1.04x faster                                                |
| xml_etree_parse            | 93.0 ms                                                     | 89.4 ms: 1.04x faster                                               |
| json                       | 3.05 ms                                                     | 2.93 ms: 1.04x faster                                               |
| dulwich_log                | 44.3 ms                                                     | 42.6 ms: 1.04x faster                                               |
| go                         | 91.6 ms                                                     | 88.3 ms: 1.04x faster                                               |
| async_generators           | 239 ms                                                      | 231 ms: 1.03x faster                                                |
| pathlib                    | 80.5 ms                                                     | 78.3 ms: 1.03x faster                                               |
| mako                       | 7.09 ms                                                     | 6.97 ms: 1.02x faster                                               |
| chaos                      | 43.3 ms                                                     | 42.9 ms: 1.01x faster                                               |
| regex_compile              | 87.5 ms                                                     | 87.9 ms: 1.00x slower                                               |
| crypto_pyaes               | 48.5 ms                                                     | 48.7 ms: 1.01x slower                                               |
| logging_format             | 6.72 us                                                     | 6.81 us: 1.01x slower                                               |
| docutils                   | 1.66 sec                                                    | 1.69 sec: 1.02x slower                                              |
| meteor_contest             | 74.6 ms                                                     | 76.0 ms: 1.02x slower                                               |
| logging_simple             | 6.28 us                                                     | 6.43 us: 1.03x slower                                               |
| tomli_loads                | 1.37 sec                                                    | 1.40 sec: 1.03x slower                                              |
| sympy_str                  | 175 ms                                                      | 180 ms: 1.03x slower                                                |
| coroutines                 | 14.3 ms                                                     | 14.8 ms: 1.03x slower                                               |
| json_loads                 | 13.9 us                                                     | 14.4 us: 1.04x slower                                               |
| nbody                      | 71.9 ms                                                     | 74.5 ms: 1.04x slower                                               |
| regex_v8                   | 14.2 ms                                                     | 14.8 ms: 1.04x slower                                               |
| nqueens                    | 62.8 ms                                                     | 65.2 ms: 1.04x slower                                               |
| pprint_safe_repr           | 513 ms                                                      | 535 ms: 1.04x slower                                                |
| pprint_pformat             | 1.05 sec                                                    | 1.09 sec: 1.05x slower                                              |
| sympy_integrate            | 13.0 ms                                                     | 13.6 ms: 1.05x slower                                               |
| sqlglot_optimize           | 34.5 ms                                                     | 36.3 ms: 1.05x slower                                               |
| pycparser                  | 699 ms                                                      | 736 ms: 1.05x slower                                                |
| sqlglot_normalize          | 187 ms                                                      | 197 ms: 1.06x slower                                                |
| pyflate                    | 295 ms                                                      | 312 ms: 1.06x slower                                                |
| 2to3                       | 218 ms                                                      | 232 ms: 1.07x slower                                                |
| scimark_fft                | 184 ms                                                      | 198 ms: 1.07x slower                                                |
| sqlglot_transpile          | 1.02 ms                                                     | 1.10 ms: 1.08x slower                                               |
| xml_etree_generate         | 55.8 ms                                                     | 60.3 ms: 1.08x slower                                               |
| sympy_expand               | 284 ms                                                      | 310 ms: 1.09x slower                                                |
| deltablue                  | 2.16 ms                                                     | 2.37 ms: 1.10x slower                                               |
| sqlglot_parse              | 804 us                                                      | 891 us: 1.11x slower                                                |
| raytrace                   | 192 ms                                                      | 214 ms: 1.11x slower                                                |
| python_startup_no_site     | 16.2 ms                                                     | 18.2 ms: 1.12x slower                                               |
| hexiom                     | 4.10 ms                                                     | 4.60 ms: 1.12x slower                                               |
| fannkuch                   | 247 ms                                                      | 277 ms: 1.12x slower                                                |
| django_template            | 22.9 ms                                                     | 25.9 ms: 1.13x slower                                               |
| richards_super             | 32.1 ms                                                     | 36.3 ms: 1.13x slower                                               |
| scimark_sor                | 78.8 ms                                                     | 89.6 ms: 1.14x slower                                               |
| mdp                        | 1.37 sec                                                    | 1.56 sec: 1.14x slower                                              |
| richards                   | 28.4 ms                                                     | 32.3 ms: 1.14x slower                                               |
| scimark_monte_carlo        | 43.7 ms                                                     | 49.9 ms: 1.14x slower                                               |
| xml_etree_process          | 37.7 ms                                                     | 43.3 ms: 1.15x slower                                               |
| logging_silent             | 60.5 ns                                                     | 69.9 ns: 1.16x slower                                               |
| telco                      | 4.13 ms                                                     | 4.81 ms: 1.17x slower                                               |
| coverage                   | 40.8 ms                                                     | 48.3 ms: 1.18x slower                                               |
| scimark_lu                 | 58.9 ms                                                     | 69.8 ms: 1.19x slower                                               |
| json_dumps                 | 5.70 ms                                                     | 6.89 ms: 1.21x slower                                               |
| typing_runtime_protocols   | 95.1 us                                                     | 115 us: 1.21x slower                                                |
| unpickle_pure_python       | 133 us                                                      | 162 us: 1.21x slower                                                |
| pickle_pure_python         | 195 us                                                      | 238 us: 1.22x slower                                                |
| python_startup             | 19.5 ms                                                     | 24.4 ms: 1.25x slower                                               |
| bench_mp_pool              | 69.2 ms                                                     | 88.2 ms: 1.28x slower                                               |
| gc_traversal               | 1.52 ms                                                     | 1.99 ms: 1.31x slower                                               |
| create_gc_cycles           | 752 us                                                      | 1.21 ms: 1.61x slower                                               |
| Geometric mean             | (ref)                                                       | 1.00x slower                                                        |

Benchmark hidden because not significant (4): sympy_sum, xml_etree_iterparse, bench_thread_pool, scimark_sparse_mat_mult
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20250121-3.14.0a4+-4844db8/bm-20250121-pythonperf1-amd64-mdboom-aa_test_2025-3.14.0a4+-4844db8.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.004x faster

# HPT report

- Reliability score: 95.85% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown