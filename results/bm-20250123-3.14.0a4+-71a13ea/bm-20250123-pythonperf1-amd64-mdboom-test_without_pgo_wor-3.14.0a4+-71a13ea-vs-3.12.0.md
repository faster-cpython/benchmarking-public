# Results vs. 3.12.0

- fork: mdboom
- ref: test_without_pgo_wor
- machine: windows-amd64
- commit hash: 71a13ea
- commit date: 2025-01-23
- overall geometric mean: 1.013x slower
- HPT reliability: 99.31%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250123-pythonperf1-amd64-mdboom-test_without_pgo_wor-3.14.0a4+-71a13ea |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 235 ms: 1.08x slower                                                        |
| docutils       | 1.66 sec                                                    | 1.71 sec: 1.03x slower                                                      |
| Geometric mean | (ref)                                                       | 1.05x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250123-pythonperf1-amd64-mdboom-test_without_pgo_wor-3.14.0a4+-71a13ea |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 410 ms: 1.88x faster                                                        |
| async_tree_io              | 731 ms                                                      | 419 ms: 1.75x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 215 ms: 1.71x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 176 ms: 1.62x faster                                                        |
| async_tree_none            | 291 ms                                                      | 189 ms: 1.54x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 230 ms: 1.48x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 347 ms: 1.45x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 348 ms: 1.41x faster                                                        |
| Geometric mean             | (ref)                                                       | 1.60x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250123-pythonperf1-amd64-mdboom-test_without_pgo_wor-3.14.0a4+-71a13ea |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 52.4 ms: 1.08x faster                                                       |
| pidigits       | 152 ms                                                      | 147 ms: 1.04x faster                                                        |
| nbody          | 71.9 ms                                                     | 77.5 ms: 1.08x slower                                                       |
| Geometric mean | (ref)                                                       | 1.01x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250123-pythonperf1-amd64-mdboom-test_without_pgo_wor-3.14.0a4+-71a13ea |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 116 ms: 1.09x faster                                                        |
| regex_effbot   | 1.62 ms                                                     | 1.50 ms: 1.08x faster                                                       |
| regex_compile  | 87.5 ms                                                     | 89.6 ms: 1.02x slower                                                       |
| regex_v8       | 14.2 ms                                                     | 15.1 ms: 1.06x slower                                                       |
| Geometric mean | (ref)                                                       | 1.02x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250123-pythonperf1-amd64-mdboom-test_without_pgo_wor-3.14.0a4+-71a13ea |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_parse      | 93.0 ms                                                     | 89.7 ms: 1.04x faster                                                       |
| json_loads           | 13.9 us                                                     | 14.5 us: 1.04x slower                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.44 sec: 1.06x slower                                                      |
| xml_etree_generate   | 55.8 ms                                                     | 59.9 ms: 1.07x slower                                                       |
| xml_etree_process    | 37.7 ms                                                     | 43.6 ms: 1.16x slower                                                       |
| json_dumps           | 5.70 ms                                                     | 6.83 ms: 1.20x slower                                                       |
| unpickle_pure_python | 133 us                                                      | 165 us: 1.24x slower                                                        |
| pickle_pure_python   | 195 us                                                      | 244 us: 1.25x slower                                                        |
| Geometric mean       | (ref)                                                       | 1.10x slower                                                                |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250123-pythonperf1-amd64-mdboom-test_without_pgo_wor-3.14.0a4+-71a13ea |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 18.1 ms: 1.12x slower                                                       |
| python_startup         | 19.5 ms                                                     | 24.4 ms: 1.25x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.18x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250123-pythonperf1-amd64-mdboom-test_without_pgo_wor-3.14.0a4+-71a13ea |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 22.9 ms                                                     | 26.1 ms: 1.14x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.07x slower                                                                |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250123-pythonperf1-amd64-mdboom-test_without_pgo_wor-3.14.0a4+-71a13ea |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 410 ms: 1.88x faster                                                        |
| async_tree_io              | 731 ms                                                      | 419 ms: 1.75x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 215 ms: 1.71x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 176 ms: 1.62x faster                                                        |
| async_tree_none            | 291 ms                                                      | 189 ms: 1.54x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 230 ms: 1.48x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 347 ms: 1.45x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 348 ms: 1.41x faster                                                        |
| deepcopy                   | 238 us                                                      | 192 us: 1.24x faster                                                        |
| comprehensions             | 14.1 us                                                     | 12.7 us: 1.11x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 21.7 us: 1.09x faster                                                       |
| regex_dna                  | 126 ms                                                      | 116 ms: 1.09x faster                                                        |
| float                      | 56.8 ms                                                     | 52.4 ms: 1.08x faster                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.50 ms: 1.08x faster                                                       |
| deepcopy_reduce            | 2.09 us                                                     | 1.95 us: 1.07x faster                                                       |
| dulwich_log                | 44.3 ms                                                     | 41.5 ms: 1.07x faster                                                       |
| async_generators           | 239 ms                                                      | 231 ms: 1.04x faster                                                        |
| spectral_norm              | 66.9 ms                                                     | 64.5 ms: 1.04x faster                                                       |
| xml_etree_parse            | 93.0 ms                                                     | 89.7 ms: 1.04x faster                                                       |
| pidigits                   | 152 ms                                                      | 147 ms: 1.04x faster                                                        |
| pathlib                    | 80.5 ms                                                     | 78.4 ms: 1.03x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.72 us: 1.02x faster                                                       |
| bench_thread_pool          | 857 us                                                      | 840 us: 1.02x faster                                                        |
| json                       | 3.05 ms                                                     | 3.01 ms: 1.01x faster                                                       |
| chaos                      | 43.3 ms                                                     | 43.7 ms: 1.01x slower                                                       |
| crypto_pyaes               | 48.5 ms                                                     | 49.3 ms: 1.02x slower                                                       |
| regex_compile              | 87.5 ms                                                     | 89.6 ms: 1.02x slower                                                       |
| go                         | 91.6 ms                                                     | 93.9 ms: 1.03x slower                                                       |
| docutils                   | 1.66 sec                                                    | 1.71 sec: 1.03x slower                                                      |
| sympy_str                  | 175 ms                                                      | 181 ms: 1.03x slower                                                        |
| nqueens                    | 62.8 ms                                                     | 65.2 ms: 1.04x slower                                                       |
| logging_format             | 6.72 us                                                     | 7.00 us: 1.04x slower                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.67 ms: 1.04x slower                                                       |
| json_loads                 | 13.9 us                                                     | 14.5 us: 1.04x slower                                                       |
| meteor_contest             | 74.6 ms                                                     | 78.0 ms: 1.05x slower                                                       |
| logging_simple             | 6.28 us                                                     | 6.58 us: 1.05x slower                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.44 sec: 1.06x slower                                                      |
| coroutines                 | 14.3 ms                                                     | 15.1 ms: 1.06x slower                                                       |
| sympy_integrate            | 13.0 ms                                                     | 13.7 ms: 1.06x slower                                                       |
| scimark_fft                | 184 ms                                                      | 195 ms: 1.06x slower                                                        |
| regex_v8                   | 14.2 ms                                                     | 15.1 ms: 1.06x slower                                                       |
| sqlglot_optimize           | 34.5 ms                                                     | 36.8 ms: 1.07x slower                                                       |
| pycparser                  | 699 ms                                                      | 746 ms: 1.07x slower                                                        |
| xml_etree_generate         | 55.8 ms                                                     | 59.9 ms: 1.07x slower                                                       |
| 2to3                       | 218 ms                                                      | 235 ms: 1.08x slower                                                        |
| nbody                      | 71.9 ms                                                     | 77.5 ms: 1.08x slower                                                       |
| sqlglot_normalize          | 187 ms                                                      | 202 ms: 1.08x slower                                                        |
| raytrace                   | 192 ms                                                      | 210 ms: 1.09x slower                                                        |
| sympy_expand               | 284 ms                                                      | 310 ms: 1.09x slower                                                        |
| pprint_pformat             | 1.05 sec                                                    | 1.14 sec: 1.09x slower                                                      |
| pyflate                    | 295 ms                                                      | 323 ms: 1.10x slower                                                        |
| pprint_safe_repr           | 513 ms                                                      | 566 ms: 1.10x slower                                                        |
| sqlglot_transpile          | 1.02 ms                                                     | 1.13 ms: 1.10x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                     | 18.1 ms: 1.12x slower                                                       |
| deltablue                  | 2.16 ms                                                     | 2.43 ms: 1.13x slower                                                       |
| sqlglot_parse              | 804 us                                                      | 909 us: 1.13x slower                                                        |
| django_template            | 22.9 ms                                                     | 26.1 ms: 1.14x slower                                                       |
| hexiom                     | 4.10 ms                                                     | 4.72 ms: 1.15x slower                                                       |
| xml_etree_process          | 37.7 ms                                                     | 43.6 ms: 1.16x slower                                                       |
| telco                      | 4.13 ms                                                     | 4.81 ms: 1.16x slower                                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 50.9 ms: 1.16x slower                                                       |
| richards_super             | 32.1 ms                                                     | 37.4 ms: 1.17x slower                                                       |
| richards                   | 28.4 ms                                                     | 33.3 ms: 1.17x slower                                                       |
| fannkuch                   | 247 ms                                                      | 290 ms: 1.17x slower                                                        |
| scimark_lu                 | 58.9 ms                                                     | 69.4 ms: 1.18x slower                                                       |
| mdp                        | 1.37 sec                                                    | 1.62 sec: 1.18x slower                                                      |
| json_dumps                 | 5.70 ms                                                     | 6.83 ms: 1.20x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 115 us: 1.20x slower                                                        |
| logging_silent             | 60.5 ns                                                     | 73.0 ns: 1.21x slower                                                       |
| scimark_sor                | 78.8 ms                                                     | 95.4 ms: 1.21x slower                                                       |
| coverage                   | 40.8 ms                                                     | 50.4 ms: 1.24x slower                                                       |
| unpickle_pure_python       | 133 us                                                      | 165 us: 1.24x slower                                                        |
| pickle_pure_python         | 195 us                                                      | 244 us: 1.25x slower                                                        |
| python_startup             | 19.5 ms                                                     | 24.4 ms: 1.25x slower                                                       |
| bench_mp_pool              | 69.2 ms                                                     | 88.6 ms: 1.28x slower                                                       |
| gc_traversal               | 1.52 ms                                                     | 1.97 ms: 1.29x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 1.19 ms: 1.58x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.02x slower                                                                |

Benchmark hidden because not significant (4): generators, xml_etree_iterparse, mako, sympy_sum
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20250123-3.14.0a4+-71a13ea/bm-20250123-pythonperf1-amd64-mdboom-test_without_pgo_wor-3.14.0a4+-71a13ea.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.013x slower

# HPT report

- Reliability score: 99.31% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown