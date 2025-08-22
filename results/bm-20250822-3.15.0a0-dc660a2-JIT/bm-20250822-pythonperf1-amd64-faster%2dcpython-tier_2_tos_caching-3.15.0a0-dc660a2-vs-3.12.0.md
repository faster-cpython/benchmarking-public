# Results vs. 3.12.0

- fork: faster-cpython
- ref: tier_2_tos_caching
- machine: windows-amd64
- commit hash: dc660a2
- commit date: 2025-08-22
- overall geometric mean: 1.151x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250822-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-dc660a2 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 215 ms: 1.01x faster                                                               |
| docutils       | 1.66 sec                                                    | 1.61 sec: 1.03x faster                                                             |
| Geometric mean | (ref)                                                       | 1.02x faster                                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250822-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-dc660a2 |
|----------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 377 ms: 2.04x faster                                                               |
| async_tree_io              | 731 ms                                                      | 385 ms: 1.90x faster                                                               |
| async_tree_memoization_tg  | 367 ms                                                      | 209 ms: 1.76x faster                                                               |
| async_tree_none            | 291 ms                                                      | 171 ms: 1.71x faster                                                               |
| async_tree_none_tg         | 285 ms                                                      | 168 ms: 1.69x faster                                                               |
| async_tree_memoization     | 339 ms                                                      | 203 ms: 1.67x faster                                                               |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 333 ms: 1.51x faster                                                               |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 330 ms: 1.48x faster                                                               |
| Geometric mean             | (ref)                                                       | 1.71x faster                                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250822-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-dc660a2 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| nbody          | 71.9 ms                                                     | 42.6 ms: 1.69x faster                                                              |
| float          | 56.8 ms                                                     | 43.6 ms: 1.30x faster                                                              |
| pidigits       | 152 ms                                                      | 145 ms: 1.05x faster                                                               |
| Geometric mean | (ref)                                                       | 1.32x faster                                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250822-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-dc660a2 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 78.3 ms: 1.12x faster                                                              |
| regex_dna      | 126 ms                                                      | 119 ms: 1.07x faster                                                               |
| regex_effbot   | 1.62 ms                                                     | 1.54 ms: 1.05x faster                                                              |
| regex_v8       | 14.2 ms                                                     | 14.0 ms: 1.02x faster                                                              |
| Geometric mean | (ref)                                                       | 1.06x faster                                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250822-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-dc660a2 |
|----------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| tomli_loads          | 1.37 sec                                                    | 1.08 sec: 1.27x faster                                                             |
| unpickle_pure_python | 133 us                                                      | 105 us: 1.26x faster                                                               |
| xml_etree_generate   | 55.8 ms                                                     | 48.8 ms: 1.14x faster                                                              |
| xml_etree_parse      | 93.0 ms                                                     | 83.1 ms: 1.12x faster                                                              |
| xml_etree_process    | 37.7 ms                                                     | 35.0 ms: 1.08x faster                                                              |
| xml_etree_iterparse  | 65.2 ms                                                     | 60.7 ms: 1.07x faster                                                              |
| json_dumps           | 5.70 ms                                                     | 5.32 ms: 1.07x faster                                                              |
| pickle_pure_python   | 195 us                                                      | 203 us: 1.04x slower                                                               |
| Geometric mean       | (ref)                                                       | 1.10x faster                                                                       |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250822-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-dc660a2 |
|------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 19.3 ms: 1.19x slower                                                              |
| python_startup         | 19.5 ms                                                     | 25.3 ms: 1.30x slower                                                              |
| Geometric mean         | (ref)                                                       | 1.24x slower                                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250822-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-dc660a2 |
|-----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.53 ms: 1.28x faster                                                              |
| django_template | 22.9 ms                                                     | 24.1 ms: 1.05x slower                                                              |
| Geometric mean  | (ref)                                                       | 1.11x faster                                                                       |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250822-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-dc660a2 |
|----------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 29.5 ms: 2.72x faster                                                              |
| async_tree_io_tg           | 771 ms                                                      | 377 ms: 2.04x faster                                                               |
| async_tree_io              | 731 ms                                                      | 385 ms: 1.90x faster                                                               |
| async_tree_memoization_tg  | 367 ms                                                      | 209 ms: 1.76x faster                                                               |
| mdp                        | 1.37 sec                                                    | 793 ms: 1.73x faster                                                               |
| async_tree_none            | 291 ms                                                      | 171 ms: 1.71x faster                                                               |
| async_tree_none_tg         | 285 ms                                                      | 168 ms: 1.69x faster                                                               |
| nbody                      | 71.9 ms                                                     | 42.6 ms: 1.69x faster                                                              |
| async_tree_memoization     | 339 ms                                                      | 203 ms: 1.67x faster                                                               |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 333 ms: 1.51x faster                                                               |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 330 ms: 1.48x faster                                                               |
| deepcopy                   | 238 us                                                      | 169 us: 1.41x faster                                                               |
| comprehensions             | 14.1 us                                                     | 10.4 us: 1.35x faster                                                              |
| float                      | 56.8 ms                                                     | 43.6 ms: 1.30x faster                                                              |
| scimark_fft                | 184 ms                                                      | 142 ms: 1.30x faster                                                               |
| mako                       | 7.09 ms                                                     | 5.53 ms: 1.28x faster                                                              |
| tomli_loads                | 1.37 sec                                                    | 1.08 sec: 1.27x faster                                                             |
| unpickle_pure_python       | 133 us                                                      | 105 us: 1.26x faster                                                               |
| deepcopy_memo              | 23.7 us                                                     | 19.0 us: 1.25x faster                                                              |
| pprint_safe_repr           | 513 ms                                                      | 412 ms: 1.24x faster                                                               |
| pprint_pformat             | 1.05 sec                                                    | 851 ms: 1.23x faster                                                               |
| go                         | 91.6 ms                                                     | 77.1 ms: 1.19x faster                                                              |
| fannkuch                   | 247 ms                                                      | 209 ms: 1.18x faster                                                               |
| deepcopy_reduce            | 2.09 us                                                     | 1.81 us: 1.15x faster                                                              |
| generators                 | 22.5 ms                                                     | 19.6 ms: 1.15x faster                                                              |
| xml_etree_generate         | 55.8 ms                                                     | 48.8 ms: 1.14x faster                                                              |
| pyflate                    | 295 ms                                                      | 258 ms: 1.14x faster                                                               |
| sqlite_synth               | 1.76 us                                                     | 1.54 us: 1.14x faster                                                              |
| dulwich_log                | 44.3 ms                                                     | 39.3 ms: 1.13x faster                                                              |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.28 ms: 1.12x faster                                                              |
| xml_etree_parse            | 93.0 ms                                                     | 83.1 ms: 1.12x faster                                                              |
| regex_compile              | 87.5 ms                                                     | 78.3 ms: 1.12x faster                                                              |
| raytrace                   | 192 ms                                                      | 173 ms: 1.12x faster                                                               |
| crypto_pyaes               | 48.5 ms                                                     | 43.5 ms: 1.12x faster                                                              |
| logging_silent             | 60.5 ns                                                     | 55.1 ns: 1.10x faster                                                              |
| telco                      | 4.13 ms                                                     | 3.77 ms: 1.10x faster                                                              |
| json                       | 3.05 ms                                                     | 2.82 ms: 1.08x faster                                                              |
| chaos                      | 43.3 ms                                                     | 40.3 ms: 1.08x faster                                                              |
| xml_etree_process          | 37.7 ms                                                     | 35.0 ms: 1.08x faster                                                              |
| nqueens                    | 62.8 ms                                                     | 58.4 ms: 1.07x faster                                                              |
| xml_etree_iterparse        | 65.2 ms                                                     | 60.7 ms: 1.07x faster                                                              |
| json_dumps                 | 5.70 ms                                                     | 5.32 ms: 1.07x faster                                                              |
| sympy_sum                  | 91.5 ms                                                     | 85.6 ms: 1.07x faster                                                              |
| meteor_contest             | 74.6 ms                                                     | 69.8 ms: 1.07x faster                                                              |
| spectral_norm              | 66.9 ms                                                     | 62.7 ms: 1.07x faster                                                              |
| scimark_monte_carlo        | 43.7 ms                                                     | 41.0 ms: 1.07x faster                                                              |
| regex_dna                  | 126 ms                                                      | 119 ms: 1.07x faster                                                               |
| regex_effbot               | 1.62 ms                                                     | 1.54 ms: 1.05x faster                                                              |
| richards                   | 28.4 ms                                                     | 27.0 ms: 1.05x faster                                                              |
| pidigits                   | 152 ms                                                      | 145 ms: 1.05x faster                                                               |
| sympy_str                  | 175 ms                                                      | 167 ms: 1.05x faster                                                               |
| richards_super             | 32.1 ms                                                     | 30.7 ms: 1.05x faster                                                              |
| logging_simple             | 6.28 us                                                     | 6.02 us: 1.04x faster                                                              |
| hexiom                     | 4.10 ms                                                     | 3.94 ms: 1.04x faster                                                              |
| sympy_integrate            | 13.0 ms                                                     | 12.5 ms: 1.04x faster                                                              |
| logging_format             | 6.72 us                                                     | 6.48 us: 1.04x faster                                                              |
| docutils                   | 1.66 sec                                                    | 1.61 sec: 1.03x faster                                                             |
| pycparser                  | 699 ms                                                      | 684 ms: 1.02x faster                                                               |
| scimark_sor                | 78.8 ms                                                     | 77.3 ms: 1.02x faster                                                              |
| regex_v8                   | 14.2 ms                                                     | 14.0 ms: 1.02x faster                                                              |
| 2to3                       | 218 ms                                                      | 215 ms: 1.01x faster                                                               |
| sympy_expand               | 284 ms                                                      | 287 ms: 1.01x slower                                                               |
| pickle_pure_python         | 195 us                                                      | 203 us: 1.04x slower                                                               |
| deltablue                  | 2.16 ms                                                     | 2.26 ms: 1.05x slower                                                              |
| django_template            | 22.9 ms                                                     | 24.1 ms: 1.05x slower                                                              |
| typing_runtime_protocols   | 95.1 us                                                     | 103 us: 1.08x slower                                                               |
| python_startup_no_site     | 16.2 ms                                                     | 19.3 ms: 1.19x slower                                                              |
| coverage                   | 40.8 ms                                                     | 49.8 ms: 1.22x slower                                                              |
| python_startup             | 19.5 ms                                                     | 25.3 ms: 1.30x slower                                                              |
| gc_traversal               | 1.52 ms                                                     | 2.07 ms: 1.36x slower                                                              |
| create_gc_cycles           | 752 us                                                      | 1.29 ms: 1.71x slower                                                              |
| Geometric mean             | (ref)                                                       | 1.15x faster                                                                       |

Benchmark hidden because not significant (4): async_generators, scimark_lu, json_loads, coroutines
Ignored benchmarks (21) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250822-3.15.0a0-dc660a2-JIT/bm-20250822-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-dc660a2.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.151x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.08x
- 95% likely to have a speedup of 1.07x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: unknown