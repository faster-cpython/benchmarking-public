# Results vs. 3.12.0

- fork: faster-cpython
- ref: tier_2_tos_caching
- machine: windows-amd64
- commit hash: 53a50eb
- commit date: 2025-07-21
- overall geometric mean: 1.132x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250721-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-53a50eb |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| docutils       | 1.66 sec                                                    | 1.65 sec: 1.01x faster                                                             |
| Geometric mean | (ref)                                                       | 1.00x faster                                                                       |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250721-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-53a50eb |
|----------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 389 ms: 1.98x faster                                                               |
| async_tree_io              | 731 ms                                                      | 394 ms: 1.86x faster                                                               |
| async_tree_memoization_tg  | 367 ms                                                      | 209 ms: 1.76x faster                                                               |
| async_tree_none            | 291 ms                                                      | 167 ms: 1.74x faster                                                               |
| async_tree_none_tg         | 285 ms                                                      | 165 ms: 1.72x faster                                                               |
| async_tree_memoization     | 339 ms                                                      | 202 ms: 1.68x faster                                                               |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 332 ms: 1.48x faster                                                               |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 342 ms: 1.47x faster                                                               |
| Geometric mean             | (ref)                                                       | 1.70x faster                                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250721-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-53a50eb |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| nbody          | 71.9 ms                                                     | 46.2 ms: 1.56x faster                                                              |
| float          | 56.8 ms                                                     | 43.0 ms: 1.32x faster                                                              |
| pidigits       | 152 ms                                                      | 145 ms: 1.05x faster                                                               |
| Geometric mean | (ref)                                                       | 1.29x faster                                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250721-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-53a50eb |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 78.9 ms: 1.11x faster                                                              |
| regex_dna      | 126 ms                                                      | 119 ms: 1.06x faster                                                               |
| regex_effbot   | 1.62 ms                                                     | 1.56 ms: 1.03x faster                                                              |
| regex_v8       | 14.2 ms                                                     | 14.5 ms: 1.02x slower                                                              |
| Geometric mean | (ref)                                                       | 1.05x faster                                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250721-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-53a50eb |
|----------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| unpickle_pure_python | 133 us                                                      | 107 us: 1.24x faster                                                               |
| tomli_loads          | 1.37 sec                                                    | 1.10 sec: 1.24x faster                                                             |
| xml_etree_generate   | 55.8 ms                                                     | 51.1 ms: 1.09x faster                                                              |
| xml_etree_parse      | 93.0 ms                                                     | 86.8 ms: 1.07x faster                                                              |
| xml_etree_process    | 37.7 ms                                                     | 35.6 ms: 1.06x faster                                                              |
| xml_etree_iterparse  | 65.2 ms                                                     | 63.4 ms: 1.03x faster                                                              |
| pickle_pure_python   | 195 us                                                      | 200 us: 1.02x slower                                                               |
| json_loads           | 13.9 us                                                     | 14.5 us: 1.05x slower                                                              |
| json_dumps           | 5.70 ms                                                     | 6.24 ms: 1.10x slower                                                              |
| Geometric mean       | (ref)                                                       | 1.06x faster                                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250721-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-53a50eb |
|------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 19.5 ms: 1.20x slower                                                              |
| python_startup         | 19.5 ms                                                     | 25.9 ms: 1.33x slower                                                              |
| Geometric mean         | (ref)                                                       | 1.26x slower                                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250721-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-53a50eb |
|-----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.62 ms: 1.26x faster                                                              |
| django_template | 22.9 ms                                                     | 24.2 ms: 1.05x slower                                                              |
| Geometric mean  | (ref)                                                       | 1.09x faster                                                                       |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250721-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-53a50eb |
|----------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 30.1 ms: 2.67x faster                                                              |
| async_tree_io_tg           | 771 ms                                                      | 389 ms: 1.98x faster                                                               |
| async_tree_io              | 731 ms                                                      | 394 ms: 1.86x faster                                                               |
| async_tree_memoization_tg  | 367 ms                                                      | 209 ms: 1.76x faster                                                               |
| async_tree_none            | 291 ms                                                      | 167 ms: 1.74x faster                                                               |
| async_tree_none_tg         | 285 ms                                                      | 165 ms: 1.72x faster                                                               |
| mdp                        | 1.37 sec                                                    | 798 ms: 1.72x faster                                                               |
| async_tree_memoization     | 339 ms                                                      | 202 ms: 1.68x faster                                                               |
| nbody                      | 71.9 ms                                                     | 46.2 ms: 1.56x faster                                                              |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 332 ms: 1.48x faster                                                               |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 342 ms: 1.47x faster                                                               |
| deepcopy                   | 238 us                                                      | 170 us: 1.40x faster                                                               |
| comprehensions             | 14.1 us                                                     | 10.3 us: 1.37x faster                                                              |
| float                      | 56.8 ms                                                     | 43.0 ms: 1.32x faster                                                              |
| deepcopy_memo              | 23.7 us                                                     | 17.9 us: 1.32x faster                                                              |
| mako                       | 7.09 ms                                                     | 5.62 ms: 1.26x faster                                                              |
| scimark_fft                | 184 ms                                                      | 147 ms: 1.26x faster                                                               |
| unpickle_pure_python       | 133 us                                                      | 107 us: 1.24x faster                                                               |
| tomli_loads                | 1.37 sec                                                    | 1.10 sec: 1.24x faster                                                             |
| go                         | 91.6 ms                                                     | 75.3 ms: 1.22x faster                                                              |
| pyflate                    | 295 ms                                                      | 252 ms: 1.17x faster                                                               |
| pprint_pformat             | 1.05 sec                                                    | 902 ms: 1.16x faster                                                               |
| pprint_safe_repr           | 513 ms                                                      | 443 ms: 1.16x faster                                                               |
| deepcopy_reduce            | 2.09 us                                                     | 1.81 us: 1.16x faster                                                              |
| generators                 | 22.5 ms                                                     | 19.6 ms: 1.15x faster                                                              |
| sqlite_synth               | 1.76 us                                                     | 1.56 us: 1.13x faster                                                              |
| logging_silent             | 60.5 ns                                                     | 54.2 ns: 1.12x faster                                                              |
| regex_compile              | 87.5 ms                                                     | 78.9 ms: 1.11x faster                                                              |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.31 ms: 1.11x faster                                                              |
| dulwich_log                | 44.3 ms                                                     | 40.1 ms: 1.10x faster                                                              |
| fannkuch                   | 247 ms                                                      | 224 ms: 1.10x faster                                                               |
| xml_etree_generate         | 55.8 ms                                                     | 51.1 ms: 1.09x faster                                                              |
| chaos                      | 43.3 ms                                                     | 39.9 ms: 1.09x faster                                                              |
| raytrace                   | 192 ms                                                      | 177 ms: 1.08x faster                                                               |
| scimark_monte_carlo        | 43.7 ms                                                     | 40.4 ms: 1.08x faster                                                              |
| spectral_norm              | 66.9 ms                                                     | 62.2 ms: 1.08x faster                                                              |
| xml_etree_parse            | 93.0 ms                                                     | 86.8 ms: 1.07x faster                                                              |
| richards                   | 28.4 ms                                                     | 26.6 ms: 1.07x faster                                                              |
| richards_super             | 32.1 ms                                                     | 30.2 ms: 1.06x faster                                                              |
| regex_dna                  | 126 ms                                                      | 119 ms: 1.06x faster                                                               |
| scimark_sor                | 78.8 ms                                                     | 74.1 ms: 1.06x faster                                                              |
| xml_etree_process          | 37.7 ms                                                     | 35.6 ms: 1.06x faster                                                              |
| crypto_pyaes               | 48.5 ms                                                     | 45.8 ms: 1.06x faster                                                              |
| logging_simple             | 6.28 us                                                     | 5.95 us: 1.06x faster                                                              |
| pidigits                   | 152 ms                                                      | 145 ms: 1.05x faster                                                               |
| nqueens                    | 62.8 ms                                                     | 60.0 ms: 1.05x faster                                                              |
| sympy_sum                  | 91.5 ms                                                     | 87.6 ms: 1.04x faster                                                              |
| logging_format             | 6.72 us                                                     | 6.44 us: 1.04x faster                                                              |
| regex_effbot               | 1.62 ms                                                     | 1.56 ms: 1.03x faster                                                              |
| sympy_str                  | 175 ms                                                      | 170 ms: 1.03x faster                                                               |
| xml_etree_iterparse        | 65.2 ms                                                     | 63.4 ms: 1.03x faster                                                              |
| meteor_contest             | 74.6 ms                                                     | 73.2 ms: 1.02x faster                                                              |
| sympy_integrate            | 13.0 ms                                                     | 12.7 ms: 1.02x faster                                                              |
| pycparser                  | 699 ms                                                      | 691 ms: 1.01x faster                                                               |
| docutils                   | 1.66 sec                                                    | 1.65 sec: 1.01x faster                                                             |
| hexiom                     | 4.10 ms                                                     | 4.08 ms: 1.00x faster                                                              |
| regex_v8                   | 14.2 ms                                                     | 14.5 ms: 1.02x slower                                                              |
| scimark_lu                 | 58.9 ms                                                     | 60.0 ms: 1.02x slower                                                              |
| pickle_pure_python         | 195 us                                                      | 200 us: 1.02x slower                                                               |
| telco                      | 4.13 ms                                                     | 4.24 ms: 1.03x slower                                                              |
| sympy_expand               | 284 ms                                                      | 292 ms: 1.03x slower                                                               |
| async_generators           | 239 ms                                                      | 248 ms: 1.04x slower                                                               |
| json_loads                 | 13.9 us                                                     | 14.5 us: 1.05x slower                                                              |
| django_template            | 22.9 ms                                                     | 24.2 ms: 1.05x slower                                                              |
| typing_runtime_protocols   | 95.1 us                                                     | 103 us: 1.08x slower                                                               |
| json_dumps                 | 5.70 ms                                                     | 6.24 ms: 1.10x slower                                                              |
| python_startup_no_site     | 16.2 ms                                                     | 19.5 ms: 1.20x slower                                                              |
| coverage                   | 40.8 ms                                                     | 49.1 ms: 1.20x slower                                                              |
| python_startup             | 19.5 ms                                                     | 25.9 ms: 1.33x slower                                                              |
| gc_traversal               | 1.52 ms                                                     | 2.14 ms: 1.40x slower                                                              |
| create_gc_cycles           | 752 us                                                      | 1.33 ms: 1.76x slower                                                              |
| Geometric mean             | (ref)                                                       | 1.13x faster                                                                       |

Benchmark hidden because not significant (4): json, deltablue, 2to3, coroutines
Ignored benchmarks (21) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250721-3.15.0a0-53a50eb-JIT/bm-20250721-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-53a50eb.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.132x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: unknown