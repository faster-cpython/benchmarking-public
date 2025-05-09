# Results vs. 3.12.0

- fork: python
- ref: 4617d68d73409e83d6ab
- machine: windows-amd64
- commit hash: 4617d68
- commit date: 2025-05-08
- overall geometric mean: 1.057x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.01x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250508-pythonperf1-amd64-python-4617d68d73409e83d6ab-3.15.0a0-4617d68 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 228 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                       | 1.02x slower                                                               |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250508-pythonperf1-amd64-python-4617d68d73409e83d6ab-3.15.0a0-4617d68 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 405 ms: 1.90x faster                                                       |
| async_tree_io              | 731 ms                                                      | 404 ms: 1.81x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 213 ms: 1.72x faster                                                       |
| async_tree_none            | 291 ms                                                      | 174 ms: 1.67x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 173 ms: 1.64x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 223 ms: 1.52x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 333 ms: 1.47x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 344 ms: 1.46x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.64x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250508-pythonperf1-amd64-python-4617d68d73409e83d6ab-3.15.0a0-4617d68 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 43.9 ms: 1.29x faster                                                      |
| nbody          | 71.9 ms                                                     | 62.7 ms: 1.15x faster                                                      |
| pidigits       | 152 ms                                                      | 149 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                       | 1.15x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250508-pythonperf1-amd64-python-4617d68d73409e83d6ab-3.15.0a0-4617d68 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 81.4 ms: 1.08x faster                                                      |
| regex_dna      | 126 ms                                                      | 121 ms: 1.05x faster                                                       |
| regex_effbot   | 1.62 ms                                                     | 1.63 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                       | 1.03x faster                                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250508-pythonperf1-amd64-python-4617d68d73409e83d6ab-3.15.0a0-4617d68 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| unpickle_pure_python | 133 us                                                      | 134 us: 1.01x slower                                                       |
| xml_etree_generate   | 55.8 ms                                                     | 56.7 ms: 1.02x slower                                                      |
| tomli_loads          | 1.37 sec                                                    | 1.41 sec: 1.03x slower                                                     |
| xml_etree_process    | 37.7 ms                                                     | 39.9 ms: 1.06x slower                                                      |
| json_loads           | 13.9 us                                                     | 15.1 us: 1.08x slower                                                      |
| pickle_pure_python   | 195 us                                                      | 213 us: 1.09x slower                                                       |
| json_dumps           | 5.70 ms                                                     | 6.78 ms: 1.19x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.05x slower                                                               |

Benchmark hidden because not significant (2): xml_etree_parse, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250508-pythonperf1-amd64-python-4617d68d73409e83d6ab-3.15.0a0-4617d68 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 19.6 ms: 1.21x slower                                                      |
| python_startup         | 19.5 ms                                                     | 26.6 ms: 1.37x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.28x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250508-pythonperf1-amd64-python-4617d68d73409e83d6ab-3.15.0a0-4617d68 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.77 ms: 1.05x faster                                                      |
| django_template | 22.9 ms                                                     | 24.6 ms: 1.07x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.01x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250508-pythonperf1-amd64-python-4617d68d73409e83d6ab-3.15.0a0-4617d68 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 32.1 ms: 2.51x faster                                                      |
| async_tree_io_tg           | 771 ms                                                      | 405 ms: 1.90x faster                                                       |
| async_tree_io              | 731 ms                                                      | 404 ms: 1.81x faster                                                       |
| mdp                        | 1.37 sec                                                    | 795 ms: 1.73x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 213 ms: 1.72x faster                                                       |
| async_tree_none            | 291 ms                                                      | 174 ms: 1.67x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 173 ms: 1.64x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 223 ms: 1.52x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 333 ms: 1.47x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 344 ms: 1.46x faster                                                       |
| deepcopy                   | 238 us                                                      | 171 us: 1.39x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 18.3 us: 1.30x faster                                                      |
| float                      | 56.8 ms                                                     | 43.9 ms: 1.29x faster                                                      |
| comprehensions             | 14.1 us                                                     | 11.5 us: 1.23x faster                                                      |
| generators                 | 22.5 ms                                                     | 19.2 ms: 1.17x faster                                                      |
| go                         | 91.6 ms                                                     | 78.3 ms: 1.17x faster                                                      |
| nbody                      | 71.9 ms                                                     | 62.7 ms: 1.15x faster                                                      |
| spectral_norm              | 66.9 ms                                                     | 58.8 ms: 1.14x faster                                                      |
| deepcopy_reduce            | 2.09 us                                                     | 1.84 us: 1.14x faster                                                      |
| chaos                      | 43.3 ms                                                     | 38.4 ms: 1.13x faster                                                      |
| scimark_monte_carlo        | 43.7 ms                                                     | 39.7 ms: 1.10x faster                                                      |
| sqlite_synth               | 1.76 us                                                     | 1.60 us: 1.10x faster                                                      |
| logging_silent             | 60.5 ns                                                     | 55.4 ns: 1.09x faster                                                      |
| regex_compile              | 87.5 ms                                                     | 81.4 ms: 1.08x faster                                                      |
| scimark_fft                | 184 ms                                                      | 172 ms: 1.07x faster                                                       |
| raytrace                   | 192 ms                                                      | 181 ms: 1.06x faster                                                       |
| dulwich_log                | 44.3 ms                                                     | 42.2 ms: 1.05x faster                                                      |
| regex_dna                  | 126 ms                                                      | 121 ms: 1.05x faster                                                       |
| coroutines                 | 14.3 ms                                                     | 13.6 ms: 1.05x faster                                                      |
| mako                       | 7.09 ms                                                     | 6.77 ms: 1.05x faster                                                      |
| scimark_sor                | 78.8 ms                                                     | 75.5 ms: 1.04x faster                                                      |
| sympy_integrate            | 13.0 ms                                                     | 12.4 ms: 1.04x faster                                                      |
| pyflate                    | 295 ms                                                      | 284 ms: 1.04x faster                                                       |
| pprint_safe_repr           | 513 ms                                                      | 495 ms: 1.04x faster                                                       |
| nqueens                    | 62.8 ms                                                     | 60.7 ms: 1.03x faster                                                      |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.48 ms: 1.03x faster                                                      |
| crypto_pyaes               | 48.5 ms                                                     | 47.0 ms: 1.03x faster                                                      |
| sympy_sum                  | 91.5 ms                                                     | 88.8 ms: 1.03x faster                                                      |
| scimark_lu                 | 58.9 ms                                                     | 57.1 ms: 1.03x faster                                                      |
| pprint_pformat             | 1.05 sec                                                    | 1.02 sec: 1.03x faster                                                     |
| async_generators           | 239 ms                                                      | 233 ms: 1.03x faster                                                       |
| pidigits                   | 152 ms                                                      | 149 ms: 1.02x faster                                                       |
| sympy_str                  | 175 ms                                                      | 171 ms: 1.02x faster                                                       |
| json                       | 3.05 ms                                                     | 2.99 ms: 1.02x faster                                                      |
| richards                   | 28.4 ms                                                     | 27.9 ms: 1.02x faster                                                      |
| richards_super             | 32.1 ms                                                     | 31.7 ms: 1.01x faster                                                      |
| deltablue                  | 2.16 ms                                                     | 2.14 ms: 1.01x faster                                                      |
| hexiom                     | 4.10 ms                                                     | 4.07 ms: 1.01x faster                                                      |
| unpickle_pure_python       | 133 us                                                      | 134 us: 1.01x slower                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.63 ms: 1.01x slower                                                      |
| xml_etree_generate         | 55.8 ms                                                     | 56.7 ms: 1.02x slower                                                      |
| fannkuch                   | 247 ms                                                      | 251 ms: 1.02x slower                                                       |
| pycparser                  | 699 ms                                                      | 717 ms: 1.03x slower                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.41 sec: 1.03x slower                                                     |
| sympy_expand               | 284 ms                                                      | 292 ms: 1.03x slower                                                       |
| bench_thread_pool          | 857 us                                                      | 883 us: 1.03x slower                                                       |
| 2to3                       | 218 ms                                                      | 228 ms: 1.04x slower                                                       |
| xml_etree_process          | 37.7 ms                                                     | 39.9 ms: 1.06x slower                                                      |
| django_template            | 22.9 ms                                                     | 24.6 ms: 1.07x slower                                                      |
| json_loads                 | 13.9 us                                                     | 15.1 us: 1.08x slower                                                      |
| pickle_pure_python         | 195 us                                                      | 213 us: 1.09x slower                                                       |
| telco                      | 4.13 ms                                                     | 4.67 ms: 1.13x slower                                                      |
| typing_runtime_protocols   | 95.1 us                                                     | 110 us: 1.16x slower                                                       |
| json_dumps                 | 5.70 ms                                                     | 6.78 ms: 1.19x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                     | 19.6 ms: 1.21x slower                                                      |
| python_startup             | 19.5 ms                                                     | 26.6 ms: 1.37x slower                                                      |
| bench_mp_pool              | 69.2 ms                                                     | 97.6 ms: 1.41x slower                                                      |
| gc_traversal               | 1.52 ms                                                     | 2.23 ms: 1.46x slower                                                      |
| create_gc_cycles           | 752 us                                                      | 1.31 ms: 1.75x slower                                                      |
| coverage                   | 40.8 ms                                                     | 294 ms: 7.19x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.05x faster                                                               |

Benchmark hidden because not significant (7): regex_v8, xml_etree_parse, logging_simple, logging_format, docutils, meteor_contest, xml_etree_iterparse
Ignored benchmarks (19) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250508-3.15.0a0-4617d68/bm-20250508-pythonperf1-amd64-python-4617d68d73409e83d6ab-3.15.0a0-4617d68.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.057x faster

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: unknown