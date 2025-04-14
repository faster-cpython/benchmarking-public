# Results vs. 3.12.0

- fork: python
- ref: v3.14.0a5
- machine: windows-amd64
- commit hash: 3ae9101
- commit date: 2025-02-11
- overall geometric mean: 1.057x faster
- HPT reliability: 93.26%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250211-pythonperf1-amd64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 222 ms: 1.02x slower                                            |
| docutils       | 1.66 sec                                                    | 1.75 sec: 1.06x slower                                          |
| Geometric mean | (ref)                                                       | 1.04x slower                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250211-pythonperf1-amd64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 424 ms: 1.82x faster                                            |
| async_tree_io              | 731 ms                                                      | 417 ms: 1.75x faster                                            |
| async_tree_memoization_tg  | 367 ms                                                      | 217 ms: 1.69x faster                                            |
| async_tree_none_tg         | 285 ms                                                      | 177 ms: 1.61x faster                                            |
| async_tree_none            | 291 ms                                                      | 189 ms: 1.55x faster                                            |
| async_tree_memoization     | 339 ms                                                      | 224 ms: 1.52x faster                                            |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 343 ms: 1.47x faster                                            |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 341 ms: 1.43x faster                                            |
| Geometric mean             | (ref)                                                       | 1.60x faster                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250211-pythonperf1-amd64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| nbody          | 71.9 ms                                                     | 60.5 ms: 1.19x faster                                           |
| float          | 56.8 ms                                                     | 48.4 ms: 1.17x faster                                           |
| pidigits       | 152 ms                                                      | 150 ms: 1.01x faster                                            |
| Geometric mean | (ref)                                                       | 1.12x faster                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250211-pythonperf1-amd64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.42 ms: 1.14x faster                                           |
| regex_dna      | 126 ms                                                      | 114 ms: 1.11x faster                                            |
| regex_compile  | 87.5 ms                                                     | 81.0 ms: 1.08x faster                                           |
| regex_v8       | 14.2 ms                                                     | 14.7 ms: 1.03x slower                                           |
| Geometric mean | (ref)                                                       | 1.07x faster                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250211-pythonperf1-amd64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| tomli_loads          | 1.37 sec                                                    | 1.18 sec: 1.16x faster                                          |
| unpickle_pure_python | 133 us                                                      | 115 us: 1.16x faster                                            |
| xml_etree_generate   | 55.8 ms                                                     | 51.1 ms: 1.09x faster                                           |
| xml_etree_iterparse  | 65.2 ms                                                     | 61.0 ms: 1.07x faster                                           |
| xml_etree_parse      | 93.0 ms                                                     | 90.5 ms: 1.03x faster                                           |
| xml_etree_process    | 37.7 ms                                                     | 36.7 ms: 1.03x faster                                           |
| pickle_pure_python   | 195 us                                                      | 211 us: 1.08x slower                                            |
| json_loads           | 13.9 us                                                     | 16.2 us: 1.16x slower                                           |
| json_dumps           | 5.70 ms                                                     | 6.66 ms: 1.17x slower                                           |
| Geometric mean       | (ref)                                                       | 1.01x faster                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250211-pythonperf1-amd64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 18.9 ms: 1.16x slower                                           |
| python_startup         | 19.5 ms                                                     | 25.1 ms: 1.29x slower                                           |
| Geometric mean         | (ref)                                                       | 1.23x slower                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250211-pythonperf1-amd64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.26 ms: 1.35x faster                                           |
| django_template | 22.9 ms                                                     | 25.5 ms: 1.11x slower                                           |
| Geometric mean  | (ref)                                                       | 1.10x faster                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250211-pythonperf1-amd64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 29.5 ms: 2.73x faster                                           |
| async_tree_io_tg           | 771 ms                                                      | 424 ms: 1.82x faster                                            |
| async_tree_io              | 731 ms                                                      | 417 ms: 1.75x faster                                            |
| async_tree_memoization_tg  | 367 ms                                                      | 217 ms: 1.69x faster                                            |
| async_tree_none_tg         | 285 ms                                                      | 177 ms: 1.61x faster                                            |
| async_tree_none            | 291 ms                                                      | 189 ms: 1.55x faster                                            |
| async_tree_memoization     | 339 ms                                                      | 224 ms: 1.52x faster                                            |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 343 ms: 1.47x faster                                            |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 341 ms: 1.43x faster                                            |
| mako                       | 7.09 ms                                                     | 5.26 ms: 1.35x faster                                           |
| deepcopy                   | 238 us                                                      | 188 us: 1.27x faster                                            |
| scimark_fft                | 184 ms                                                      | 148 ms: 1.25x faster                                            |
| comprehensions             | 14.1 us                                                     | 11.5 us: 1.23x faster                                           |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.15 ms: 1.19x faster                                           |
| nbody                      | 71.9 ms                                                     | 60.5 ms: 1.19x faster                                           |
| float                      | 56.8 ms                                                     | 48.4 ms: 1.17x faster                                           |
| tomli_loads                | 1.37 sec                                                    | 1.18 sec: 1.16x faster                                          |
| unpickle_pure_python       | 133 us                                                      | 115 us: 1.16x faster                                            |
| sqlite_synth               | 1.76 us                                                     | 1.53 us: 1.15x faster                                           |
| regex_effbot               | 1.62 ms                                                     | 1.42 ms: 1.14x faster                                           |
| dulwich_log                | 44.3 ms                                                     | 39.8 ms: 1.11x faster                                           |
| deepcopy_memo              | 23.7 us                                                     | 21.3 us: 1.11x faster                                           |
| regex_dna                  | 126 ms                                                      | 114 ms: 1.11x faster                                            |
| generators                 | 22.5 ms                                                     | 20.4 ms: 1.10x faster                                           |
| xml_etree_generate         | 55.8 ms                                                     | 51.1 ms: 1.09x faster                                           |
| regex_compile              | 87.5 ms                                                     | 81.0 ms: 1.08x faster                                           |
| fannkuch                   | 247 ms                                                      | 229 ms: 1.08x faster                                            |
| spectral_norm              | 66.9 ms                                                     | 62.3 ms: 1.07x faster                                           |
| xml_etree_iterparse        | 65.2 ms                                                     | 61.0 ms: 1.07x faster                                           |
| pyflate                    | 295 ms                                                      | 278 ms: 1.06x faster                                            |
| deepcopy_reduce            | 2.09 us                                                     | 1.97 us: 1.06x faster                                           |
| crypto_pyaes               | 48.5 ms                                                     | 45.9 ms: 1.06x faster                                           |
| pprint_pformat             | 1.05 sec                                                    | 995 ms: 1.05x faster                                            |
| go                         | 91.6 ms                                                     | 88.1 ms: 1.04x faster                                           |
| xml_etree_parse            | 93.0 ms                                                     | 90.5 ms: 1.03x faster                                           |
| xml_etree_process          | 37.7 ms                                                     | 36.7 ms: 1.03x faster                                           |
| chaos                      | 43.3 ms                                                     | 42.2 ms: 1.03x faster                                           |
| sympy_sum                  | 91.5 ms                                                     | 90.1 ms: 1.02x faster                                           |
| pidigits                   | 152 ms                                                      | 150 ms: 1.01x faster                                            |
| pprint_safe_repr           | 513 ms                                                      | 506 ms: 1.01x faster                                            |
| pycparser                  | 699 ms                                                      | 706 ms: 1.01x slower                                            |
| 2to3                       | 218 ms                                                      | 222 ms: 1.02x slower                                            |
| logging_format             | 6.72 us                                                     | 6.88 us: 1.02x slower                                           |
| regex_v8                   | 14.2 ms                                                     | 14.7 ms: 1.03x slower                                           |
| meteor_contest             | 74.6 ms                                                     | 77.0 ms: 1.03x slower                                           |
| logging_simple             | 6.28 us                                                     | 6.48 us: 1.03x slower                                           |
| sqlglot_parse              | 804 us                                                      | 839 us: 1.04x slower                                            |
| coroutines                 | 14.3 ms                                                     | 14.9 ms: 1.04x slower                                           |
| sqlglot_transpile          | 1.02 ms                                                     | 1.07 ms: 1.05x slower                                           |
| async_generators           | 239 ms                                                      | 251 ms: 1.05x slower                                            |
| json                       | 3.05 ms                                                     | 3.22 ms: 1.06x slower                                           |
| docutils                   | 1.66 sec                                                    | 1.75 sec: 1.06x slower                                          |
| telco                      | 4.13 ms                                                     | 4.39 ms: 1.06x slower                                           |
| scimark_monte_carlo        | 43.7 ms                                                     | 46.6 ms: 1.07x slower                                           |
| sympy_integrate            | 13.0 ms                                                     | 13.8 ms: 1.07x slower                                           |
| sympy_expand               | 284 ms                                                      | 303 ms: 1.07x slower                                            |
| pickle_pure_python         | 195 us                                                      | 211 us: 1.08x slower                                            |
| raytrace                   | 192 ms                                                      | 208 ms: 1.08x slower                                            |
| sqlglot_optimize           | 34.5 ms                                                     | 37.3 ms: 1.08x slower                                           |
| sqlglot_normalize          | 187 ms                                                      | 203 ms: 1.09x slower                                            |
| logging_silent             | 60.5 ns                                                     | 66.1 ns: 1.09x slower                                           |
| mdp                        | 1.37 sec                                                    | 1.51 sec: 1.10x slower                                          |
| hexiom                     | 4.10 ms                                                     | 4.54 ms: 1.11x slower                                           |
| django_template            | 22.9 ms                                                     | 25.5 ms: 1.11x slower                                           |
| deltablue                  | 2.16 ms                                                     | 2.42 ms: 1.12x slower                                           |
| scimark_lu                 | 58.9 ms                                                     | 66.1 ms: 1.12x slower                                           |
| richards_super             | 32.1 ms                                                     | 36.2 ms: 1.13x slower                                           |
| richards                   | 28.4 ms                                                     | 32.5 ms: 1.14x slower                                           |
| typing_runtime_protocols   | 95.1 us                                                     | 110 us: 1.16x slower                                            |
| json_loads                 | 13.9 us                                                     | 16.2 us: 1.16x slower                                           |
| python_startup_no_site     | 16.2 ms                                                     | 18.9 ms: 1.16x slower                                           |
| json_dumps                 | 5.70 ms                                                     | 6.66 ms: 1.17x slower                                           |
| scimark_sor                | 78.8 ms                                                     | 92.5 ms: 1.17x slower                                           |
| coverage                   | 40.8 ms                                                     | 48.2 ms: 1.18x slower                                           |
| bench_mp_pool              | 69.2 ms                                                     | 84.2 ms: 1.22x slower                                           |
| python_startup             | 19.5 ms                                                     | 25.1 ms: 1.29x slower                                           |
| gc_traversal               | 1.52 ms                                                     | 1.99 ms: 1.30x slower                                           |
| create_gc_cycles           | 752 us                                                      | 1.21 ms: 1.61x slower                                           |
| Geometric mean             | (ref)                                                       | 1.05x faster                                                    |

Benchmark hidden because not significant (3): sympy_str, bench_thread_pool, nqueens
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20250211-3.14.0a5-3ae9101-JIT/bm-20250211-pythonperf1-amd64-python-v3.14.0a5-3.14.0a5-3ae9101.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.057x faster

# HPT report

- Reliability score: 93.26% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown