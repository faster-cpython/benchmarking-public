# Results vs. 3.12.0

- fork: faster-cpython
- ref: tier_2_tos_caching
- machine: windows-amd64
- commit hash: 6041480
- commit date: 2025-08-11
- overall geometric mean: 1.133x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250811-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-6041480 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 222 ms: 1.02x slower                                                               |
| Geometric mean | (ref)                                                       | 1.01x slower                                                                       |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250811-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-6041480 |
|----------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 387 ms: 1.99x faster                                                               |
| async_tree_io              | 731 ms                                                      | 383 ms: 1.91x faster                                                               |
| async_tree_memoization_tg  | 367 ms                                                      | 209 ms: 1.75x faster                                                               |
| async_tree_none_tg         | 285 ms                                                      | 166 ms: 1.72x faster                                                               |
| async_tree_none            | 291 ms                                                      | 172 ms: 1.69x faster                                                               |
| async_tree_memoization     | 339 ms                                                      | 204 ms: 1.66x faster                                                               |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 339 ms: 1.48x faster                                                               |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 335 ms: 1.46x faster                                                               |
| Geometric mean             | (ref)                                                       | 1.70x faster                                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250811-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-6041480 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| nbody          | 71.9 ms                                                     | 45.2 ms: 1.59x faster                                                              |
| float          | 56.8 ms                                                     | 43.7 ms: 1.30x faster                                                              |
| pidigits       | 152 ms                                                      | 146 ms: 1.04x faster                                                               |
| Geometric mean | (ref)                                                       | 1.29x faster                                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250811-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-6041480 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 78.0 ms: 1.12x faster                                                              |
| regex_dna      | 126 ms                                                      | 115 ms: 1.10x faster                                                               |
| regex_v8       | 14.2 ms                                                     | 13.3 ms: 1.07x faster                                                              |
| regex_effbot   | 1.62 ms                                                     | 1.54 ms: 1.05x faster                                                              |
| Geometric mean | (ref)                                                       | 1.09x faster                                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250811-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-6041480 |
|----------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| unpickle_pure_python | 133 us                                                      | 108 us: 1.24x faster                                                               |
| tomli_loads          | 1.37 sec                                                    | 1.11 sec: 1.23x faster                                                             |
| xml_etree_generate   | 55.8 ms                                                     | 50.2 ms: 1.11x faster                                                              |
| xml_etree_process    | 37.7 ms                                                     | 35.0 ms: 1.08x faster                                                              |
| xml_etree_parse      | 93.0 ms                                                     | 87.1 ms: 1.07x faster                                                              |
| xml_etree_iterparse  | 65.2 ms                                                     | 63.1 ms: 1.03x faster                                                              |
| json_dumps           | 5.70 ms                                                     | 5.60 ms: 1.02x faster                                                              |
| json_loads           | 13.9 us                                                     | 14.3 us: 1.03x slower                                                              |
| pickle_pure_python   | 195 us                                                      | 204 us: 1.04x slower                                                               |
| Geometric mean       | (ref)                                                       | 1.07x faster                                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250811-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-6041480 |
|------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 19.7 ms: 1.21x slower                                                              |
| python_startup         | 19.5 ms                                                     | 26.5 ms: 1.36x slower                                                              |
| Geometric mean         | (ref)                                                       | 1.28x slower                                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250811-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-6041480 |
|-----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.47 ms: 1.30x faster                                                              |
| django_template | 22.9 ms                                                     | 24.4 ms: 1.06x slower                                                              |
| Geometric mean  | (ref)                                                       | 1.10x faster                                                                       |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250811-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-6041480 |
|----------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 31.7 ms: 2.54x faster                                                              |
| async_tree_io_tg           | 771 ms                                                      | 387 ms: 1.99x faster                                                               |
| async_tree_io              | 731 ms                                                      | 383 ms: 1.91x faster                                                               |
| async_tree_memoization_tg  | 367 ms                                                      | 209 ms: 1.75x faster                                                               |
| mdp                        | 1.37 sec                                                    | 796 ms: 1.72x faster                                                               |
| async_tree_none_tg         | 285 ms                                                      | 166 ms: 1.72x faster                                                               |
| async_tree_none            | 291 ms                                                      | 172 ms: 1.69x faster                                                               |
| async_tree_memoization     | 339 ms                                                      | 204 ms: 1.66x faster                                                               |
| nbody                      | 71.9 ms                                                     | 45.2 ms: 1.59x faster                                                              |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 339 ms: 1.48x faster                                                               |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 335 ms: 1.46x faster                                                               |
| deepcopy                   | 238 us                                                      | 166 us: 1.43x faster                                                               |
| deepcopy_memo              | 23.7 us                                                     | 17.2 us: 1.38x faster                                                              |
| comprehensions             | 14.1 us                                                     | 10.5 us: 1.35x faster                                                              |
| float                      | 56.8 ms                                                     | 43.7 ms: 1.30x faster                                                              |
| mako                       | 7.09 ms                                                     | 5.47 ms: 1.30x faster                                                              |
| scimark_fft                | 184 ms                                                      | 147 ms: 1.25x faster                                                               |
| unpickle_pure_python       | 133 us                                                      | 108 us: 1.24x faster                                                               |
| tomli_loads                | 1.37 sec                                                    | 1.11 sec: 1.23x faster                                                             |
| go                         | 91.6 ms                                                     | 75.7 ms: 1.21x faster                                                              |
| pprint_safe_repr           | 513 ms                                                      | 437 ms: 1.17x faster                                                               |
| pprint_pformat             | 1.05 sec                                                    | 898 ms: 1.16x faster                                                               |
| generators                 | 22.5 ms                                                     | 19.4 ms: 1.16x faster                                                              |
| fannkuch                   | 247 ms                                                      | 212 ms: 1.16x faster                                                               |
| deepcopy_reduce            | 2.09 us                                                     | 1.81 us: 1.16x faster                                                              |
| sqlite_synth               | 1.76 us                                                     | 1.54 us: 1.14x faster                                                              |
| pyflate                    | 295 ms                                                      | 262 ms: 1.13x faster                                                               |
| regex_compile              | 87.5 ms                                                     | 78.0 ms: 1.12x faster                                                              |
| xml_etree_generate         | 55.8 ms                                                     | 50.2 ms: 1.11x faster                                                              |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.32 ms: 1.10x faster                                                              |
| regex_dna                  | 126 ms                                                      | 115 ms: 1.10x faster                                                               |
| scimark_monte_carlo        | 43.7 ms                                                     | 39.8 ms: 1.10x faster                                                              |
| logging_silent             | 60.5 ns                                                     | 55.3 ns: 1.09x faster                                                              |
| raytrace                   | 192 ms                                                      | 177 ms: 1.09x faster                                                               |
| xml_etree_process          | 37.7 ms                                                     | 35.0 ms: 1.08x faster                                                              |
| dulwich_log                | 44.3 ms                                                     | 41.3 ms: 1.07x faster                                                              |
| regex_v8                   | 14.2 ms                                                     | 13.3 ms: 1.07x faster                                                              |
| chaos                      | 43.3 ms                                                     | 40.5 ms: 1.07x faster                                                              |
| richards                   | 28.4 ms                                                     | 26.6 ms: 1.07x faster                                                              |
| xml_etree_parse            | 93.0 ms                                                     | 87.1 ms: 1.07x faster                                                              |
| richards_super             | 32.1 ms                                                     | 30.1 ms: 1.06x faster                                                              |
| crypto_pyaes               | 48.5 ms                                                     | 45.6 ms: 1.06x faster                                                              |
| meteor_contest             | 74.6 ms                                                     | 70.2 ms: 1.06x faster                                                              |
| nqueens                    | 62.8 ms                                                     | 59.1 ms: 1.06x faster                                                              |
| regex_effbot               | 1.62 ms                                                     | 1.54 ms: 1.05x faster                                                              |
| scimark_sor                | 78.8 ms                                                     | 75.4 ms: 1.05x faster                                                              |
| sympy_sum                  | 91.5 ms                                                     | 87.8 ms: 1.04x faster                                                              |
| pidigits                   | 152 ms                                                      | 146 ms: 1.04x faster                                                               |
| scimark_lu                 | 58.9 ms                                                     | 56.9 ms: 1.03x faster                                                              |
| logging_simple             | 6.28 us                                                     | 6.08 us: 1.03x faster                                                              |
| xml_etree_iterparse        | 65.2 ms                                                     | 63.1 ms: 1.03x faster                                                              |
| sympy_str                  | 175 ms                                                      | 171 ms: 1.03x faster                                                               |
| logging_format             | 6.72 us                                                     | 6.60 us: 1.02x faster                                                              |
| sympy_integrate            | 13.0 ms                                                     | 12.7 ms: 1.02x faster                                                              |
| json_dumps                 | 5.70 ms                                                     | 5.60 ms: 1.02x faster                                                              |
| pycparser                  | 699 ms                                                      | 688 ms: 1.02x faster                                                               |
| spectral_norm              | 66.9 ms                                                     | 66.5 ms: 1.01x faster                                                              |
| hexiom                     | 4.10 ms                                                     | 4.13 ms: 1.01x slower                                                              |
| 2to3                       | 218 ms                                                      | 222 ms: 1.02x slower                                                               |
| async_generators           | 239 ms                                                      | 246 ms: 1.03x slower                                                               |
| telco                      | 4.13 ms                                                     | 4.25 ms: 1.03x slower                                                              |
| json_loads                 | 13.9 us                                                     | 14.3 us: 1.03x slower                                                              |
| coroutines                 | 14.3 ms                                                     | 14.8 ms: 1.04x slower                                                              |
| pickle_pure_python         | 195 us                                                      | 204 us: 1.04x slower                                                               |
| sympy_expand               | 284 ms                                                      | 297 ms: 1.05x slower                                                               |
| deltablue                  | 2.16 ms                                                     | 2.29 ms: 1.06x slower                                                              |
| django_template            | 22.9 ms                                                     | 24.4 ms: 1.06x slower                                                              |
| typing_runtime_protocols   | 95.1 us                                                     | 103 us: 1.08x slower                                                               |
| python_startup_no_site     | 16.2 ms                                                     | 19.7 ms: 1.21x slower                                                              |
| coverage                   | 40.8 ms                                                     | 49.5 ms: 1.21x slower                                                              |
| python_startup             | 19.5 ms                                                     | 26.5 ms: 1.36x slower                                                              |
| gc_traversal               | 1.52 ms                                                     | 2.13 ms: 1.40x slower                                                              |
| create_gc_cycles           | 752 us                                                      | 1.31 ms: 1.74x slower                                                              |
| Geometric mean             | (ref)                                                       | 1.13x faster                                                                       |

Benchmark hidden because not significant (2): docutils, json
Ignored benchmarks (21) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250811-3.15.0a0-6041480-JIT/bm-20250811-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-6041480.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.133x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: unknown