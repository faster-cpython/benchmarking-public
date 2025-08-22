# Results vs. 3.12.0

- fork: faster-cpython
- ref: tier_2_tos_caching
- machine: windows-amd64
- commit hash: efe4628
- commit date: 2025-08-22
- overall geometric mean: 1.131x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250822-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-efe4628 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 220 ms: 1.01x slower                                                               |
| Geometric mean | (ref)                                                       | 1.00x slower                                                                       |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250822-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-efe4628 |
|----------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 397 ms: 1.94x faster                                                               |
| async_tree_io              | 731 ms                                                      | 392 ms: 1.86x faster                                                               |
| async_tree_memoization_tg  | 367 ms                                                      | 208 ms: 1.76x faster                                                               |
| async_tree_none_tg         | 285 ms                                                      | 171 ms: 1.67x faster                                                               |
| async_tree_none            | 291 ms                                                      | 175 ms: 1.66x faster                                                               |
| async_tree_memoization     | 339 ms                                                      | 206 ms: 1.65x faster                                                               |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 332 ms: 1.47x faster                                                               |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 343 ms: 1.46x faster                                                               |
| Geometric mean             | (ref)                                                       | 1.68x faster                                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250822-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-efe4628 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| nbody          | 71.9 ms                                                     | 43.6 ms: 1.65x faster                                                              |
| float          | 56.8 ms                                                     | 45.1 ms: 1.26x faster                                                              |
| pidigits       | 152 ms                                                      | 147 ms: 1.03x faster                                                               |
| Geometric mean | (ref)                                                       | 1.29x faster                                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250822-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-efe4628 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 79.6 ms: 1.10x faster                                                              |
| regex_effbot   | 1.62 ms                                                     | 1.52 ms: 1.07x faster                                                              |
| regex_dna      | 126 ms                                                      | 120 ms: 1.06x faster                                                               |
| regex_v8       | 14.2 ms                                                     | 13.9 ms: 1.03x faster                                                              |
| Geometric mean | (ref)                                                       | 1.06x faster                                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250822-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-efe4628 |
|----------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| unpickle_pure_python | 133 us                                                      | 106 us: 1.25x faster                                                               |
| tomli_loads          | 1.37 sec                                                    | 1.12 sec: 1.22x faster                                                             |
| xml_etree_generate   | 55.8 ms                                                     | 51.0 ms: 1.09x faster                                                              |
| xml_etree_process    | 37.7 ms                                                     | 35.5 ms: 1.06x faster                                                              |
| xml_etree_parse      | 93.0 ms                                                     | 88.4 ms: 1.05x faster                                                              |
| json_dumps           | 5.70 ms                                                     | 5.50 ms: 1.04x faster                                                              |
| xml_etree_iterparse  | 65.2 ms                                                     | 64.4 ms: 1.01x faster                                                              |
| json_loads           | 13.9 us                                                     | 14.2 us: 1.02x slower                                                              |
| pickle_pure_python   | 195 us                                                      | 206 us: 1.06x slower                                                               |
| Geometric mean       | (ref)                                                       | 1.07x faster                                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250822-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-efe4628 |
|------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 19.2 ms: 1.18x slower                                                              |
| python_startup         | 19.5 ms                                                     | 26.5 ms: 1.36x slower                                                              |
| Geometric mean         | (ref)                                                       | 1.27x slower                                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250822-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-efe4628 |
|-----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.43 ms: 1.30x faster                                                              |
| django_template | 22.9 ms                                                     | 24.3 ms: 1.06x slower                                                              |
| Geometric mean  | (ref)                                                       | 1.11x faster                                                                       |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250822-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-efe4628 |
|----------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 29.5 ms: 2.72x faster                                                              |
| async_tree_io_tg           | 771 ms                                                      | 397 ms: 1.94x faster                                                               |
| async_tree_io              | 731 ms                                                      | 392 ms: 1.86x faster                                                               |
| async_tree_memoization_tg  | 367 ms                                                      | 208 ms: 1.76x faster                                                               |
| mdp                        | 1.37 sec                                                    | 810 ms: 1.69x faster                                                               |
| async_tree_none_tg         | 285 ms                                                      | 171 ms: 1.67x faster                                                               |
| async_tree_none            | 291 ms                                                      | 175 ms: 1.66x faster                                                               |
| nbody                      | 71.9 ms                                                     | 43.6 ms: 1.65x faster                                                              |
| async_tree_memoization     | 339 ms                                                      | 206 ms: 1.65x faster                                                               |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 332 ms: 1.47x faster                                                               |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 343 ms: 1.46x faster                                                               |
| deepcopy                   | 238 us                                                      | 175 us: 1.36x faster                                                               |
| comprehensions             | 14.1 us                                                     | 10.6 us: 1.33x faster                                                              |
| mako                       | 7.09 ms                                                     | 5.43 ms: 1.30x faster                                                              |
| deepcopy_memo              | 23.7 us                                                     | 18.7 us: 1.27x faster                                                              |
| scimark_fft                | 184 ms                                                      | 146 ms: 1.27x faster                                                               |
| float                      | 56.8 ms                                                     | 45.1 ms: 1.26x faster                                                              |
| unpickle_pure_python       | 133 us                                                      | 106 us: 1.25x faster                                                               |
| pprint_pformat             | 1.05 sec                                                    | 845 ms: 1.24x faster                                                               |
| tomli_loads                | 1.37 sec                                                    | 1.12 sec: 1.22x faster                                                             |
| pprint_safe_repr           | 513 ms                                                      | 421 ms: 1.22x faster                                                               |
| fannkuch                   | 247 ms                                                      | 206 ms: 1.20x faster                                                               |
| go                         | 91.6 ms                                                     | 78.4 ms: 1.17x faster                                                              |
| sqlite_synth               | 1.76 us                                                     | 1.54 us: 1.14x faster                                                              |
| pyflate                    | 295 ms                                                      | 260 ms: 1.13x faster                                                               |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.28 ms: 1.12x faster                                                              |
| generators                 | 22.5 ms                                                     | 20.2 ms: 1.11x faster                                                              |
| deepcopy_reduce            | 2.09 us                                                     | 1.89 us: 1.11x faster                                                              |
| regex_compile              | 87.5 ms                                                     | 79.6 ms: 1.10x faster                                                              |
| xml_etree_generate         | 55.8 ms                                                     | 51.0 ms: 1.09x faster                                                              |
| raytrace                   | 192 ms                                                      | 176 ms: 1.09x faster                                                               |
| dulwich_log                | 44.3 ms                                                     | 40.6 ms: 1.09x faster                                                              |
| crypto_pyaes               | 48.5 ms                                                     | 45.4 ms: 1.07x faster                                                              |
| regex_effbot               | 1.62 ms                                                     | 1.52 ms: 1.07x faster                                                              |
| logging_silent             | 60.5 ns                                                     | 56.7 ns: 1.07x faster                                                              |
| nqueens                    | 62.8 ms                                                     | 58.9 ms: 1.07x faster                                                              |
| chaos                      | 43.3 ms                                                     | 40.8 ms: 1.06x faster                                                              |
| xml_etree_process          | 37.7 ms                                                     | 35.5 ms: 1.06x faster                                                              |
| regex_dna                  | 126 ms                                                      | 120 ms: 1.06x faster                                                               |
| scimark_monte_carlo        | 43.7 ms                                                     | 41.4 ms: 1.06x faster                                                              |
| xml_etree_parse            | 93.0 ms                                                     | 88.4 ms: 1.05x faster                                                              |
| logging_simple             | 6.28 us                                                     | 5.99 us: 1.05x faster                                                              |
| sympy_sum                  | 91.5 ms                                                     | 87.9 ms: 1.04x faster                                                              |
| richards_super             | 32.1 ms                                                     | 30.9 ms: 1.04x faster                                                              |
| json_dumps                 | 5.70 ms                                                     | 5.50 ms: 1.04x faster                                                              |
| json                       | 3.05 ms                                                     | 2.94 ms: 1.04x faster                                                              |
| pidigits                   | 152 ms                                                      | 147 ms: 1.03x faster                                                               |
| richards                   | 28.4 ms                                                     | 27.4 ms: 1.03x faster                                                              |
| logging_format             | 6.72 us                                                     | 6.51 us: 1.03x faster                                                              |
| telco                      | 4.13 ms                                                     | 4.01 ms: 1.03x faster                                                              |
| regex_v8                   | 14.2 ms                                                     | 13.9 ms: 1.03x faster                                                              |
| sympy_str                  | 175 ms                                                      | 171 ms: 1.02x faster                                                               |
| meteor_contest             | 74.6 ms                                                     | 73.4 ms: 1.02x faster                                                              |
| sympy_integrate            | 13.0 ms                                                     | 12.8 ms: 1.01x faster                                                              |
| xml_etree_iterparse        | 65.2 ms                                                     | 64.4 ms: 1.01x faster                                                              |
| scimark_sor                | 78.8 ms                                                     | 79.3 ms: 1.01x slower                                                              |
| 2to3                       | 218 ms                                                      | 220 ms: 1.01x slower                                                               |
| spectral_norm              | 66.9 ms                                                     | 67.5 ms: 1.01x slower                                                              |
| async_generators           | 239 ms                                                      | 243 ms: 1.01x slower                                                               |
| scimark_lu                 | 58.9 ms                                                     | 60.1 ms: 1.02x slower                                                              |
| json_loads                 | 13.9 us                                                     | 14.2 us: 1.02x slower                                                              |
| coroutines                 | 14.3 ms                                                     | 14.6 ms: 1.03x slower                                                              |
| deltablue                  | 2.16 ms                                                     | 2.25 ms: 1.04x slower                                                              |
| sympy_expand               | 284 ms                                                      | 296 ms: 1.04x slower                                                               |
| pickle_pure_python         | 195 us                                                      | 206 us: 1.06x slower                                                               |
| django_template            | 22.9 ms                                                     | 24.3 ms: 1.06x slower                                                              |
| typing_runtime_protocols   | 95.1 us                                                     | 106 us: 1.11x slower                                                               |
| python_startup_no_site     | 16.2 ms                                                     | 19.2 ms: 1.18x slower                                                              |
| coverage                   | 40.8 ms                                                     | 50.5 ms: 1.24x slower                                                              |
| python_startup             | 19.5 ms                                                     | 26.5 ms: 1.36x slower                                                              |
| gc_traversal               | 1.52 ms                                                     | 2.11 ms: 1.38x slower                                                              |
| create_gc_cycles           | 752 us                                                      | 1.30 ms: 1.72x slower                                                              |
| Geometric mean             | (ref)                                                       | 1.13x faster                                                                       |

Benchmark hidden because not significant (2): hexiom, docutils
Ignored benchmarks (22) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, pycparser, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250822-3.15.0a0-efe4628-JIT/bm-20250822-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-efe4628.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.131x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: unknown