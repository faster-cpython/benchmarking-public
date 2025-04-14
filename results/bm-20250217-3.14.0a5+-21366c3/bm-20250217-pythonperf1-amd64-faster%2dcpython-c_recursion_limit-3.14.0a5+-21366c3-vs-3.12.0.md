# Results vs. 3.12.0

- fork: faster-cpython
- ref: c_recursion_limit
- machine: windows-amd64
- commit hash: 21366c3
- commit date: 2025-02-17
- overall geometric mean: 1.055x faster
- HPT reliability: 76.84%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250217-pythonperf1-amd64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 221 ms: 1.01x slower                                                               |
| docutils       | 1.66 sec                                                    | 1.64 sec: 1.01x faster                                                             |
| Geometric mean | (ref)                                                       | 1.00x faster                                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250217-pythonperf1-amd64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|----------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 407 ms: 1.90x faster                                                               |
| async_tree_io              | 731 ms                                                      | 411 ms: 1.78x faster                                                               |
| async_tree_memoization_tg  | 367 ms                                                      | 217 ms: 1.69x faster                                                               |
| async_tree_none_tg         | 285 ms                                                      | 176 ms: 1.62x faster                                                               |
| async_tree_none            | 291 ms                                                      | 188 ms: 1.55x faster                                                               |
| async_tree_memoization     | 339 ms                                                      | 224 ms: 1.52x faster                                                               |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 347 ms: 1.45x faster                                                               |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 344 ms: 1.42x faster                                                               |
| Geometric mean             | (ref)                                                       | 1.61x faster                                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250217-pythonperf1-amd64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 45.3 ms: 1.25x faster                                                              |
| pidigits       | 152 ms                                                      | 150 ms: 1.01x faster                                                               |
| nbody          | 71.9 ms                                                     | 71.2 ms: 1.01x faster                                                              |
| Geometric mean | (ref)                                                       | 1.09x faster                                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250217-pythonperf1-amd64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.45 ms: 1.12x faster                                                              |
| regex_dna      | 126 ms                                                      | 114 ms: 1.11x faster                                                               |
| regex_compile  | 87.5 ms                                                     | 85.1 ms: 1.03x faster                                                              |
| regex_v8       | 14.2 ms                                                     | 14.4 ms: 1.01x slower                                                              |
| Geometric mean | (ref)                                                       | 1.06x faster                                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250217-pythonperf1-amd64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|----------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| xml_etree_iterparse  | 65.2 ms                                                     | 63.2 ms: 1.03x faster                                                              |
| xml_etree_parse      | 93.0 ms                                                     | 91.1 ms: 1.02x faster                                                              |
| xml_etree_generate   | 55.8 ms                                                     | 56.5 ms: 1.01x slower                                                              |
| tomli_loads          | 1.37 sec                                                    | 1.40 sec: 1.02x slower                                                             |
| json_loads           | 13.9 us                                                     | 14.2 us: 1.02x slower                                                              |
| xml_etree_process    | 37.7 ms                                                     | 40.5 ms: 1.07x slower                                                              |
| unpickle_pure_python | 133 us                                                      | 145 us: 1.09x slower                                                               |
| pickle_pure_python   | 195 us                                                      | 219 us: 1.12x slower                                                               |
| json_dumps           | 5.70 ms                                                     | 6.64 ms: 1.17x slower                                                              |
| Geometric mean       | (ref)                                                       | 1.05x slower                                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250217-pythonperf1-amd64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 18.6 ms: 1.15x slower                                                              |
| python_startup         | 19.5 ms                                                     | 24.8 ms: 1.28x slower                                                              |
| Geometric mean         | (ref)                                                       | 1.21x slower                                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250217-pythonperf1-amd64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|-----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.66 ms: 1.06x faster                                                              |
| django_template | 22.9 ms                                                     | 25.5 ms: 1.11x slower                                                              |
| Geometric mean  | (ref)                                                       | 1.02x slower                                                                       |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250217-pythonperf1-amd64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|----------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 29.1 ms: 2.77x faster                                                              |
| async_tree_io_tg           | 771 ms                                                      | 407 ms: 1.90x faster                                                               |
| async_tree_io              | 731 ms                                                      | 411 ms: 1.78x faster                                                               |
| async_tree_memoization_tg  | 367 ms                                                      | 217 ms: 1.69x faster                                                               |
| async_tree_none_tg         | 285 ms                                                      | 176 ms: 1.62x faster                                                               |
| async_tree_none            | 291 ms                                                      | 188 ms: 1.55x faster                                                               |
| async_tree_memoization     | 339 ms                                                      | 224 ms: 1.52x faster                                                               |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 347 ms: 1.45x faster                                                               |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 344 ms: 1.42x faster                                                               |
| deepcopy                   | 238 us                                                      | 184 us: 1.29x faster                                                               |
| comprehensions             | 14.1 us                                                     | 11.0 us: 1.28x faster                                                              |
| float                      | 56.8 ms                                                     | 45.3 ms: 1.25x faster                                                              |
| deepcopy_memo              | 23.7 us                                                     | 19.7 us: 1.21x faster                                                              |
| generators                 | 22.5 ms                                                     | 19.4 ms: 1.16x faster                                                              |
| spectral_norm              | 66.9 ms                                                     | 57.6 ms: 1.16x faster                                                              |
| sqlite_synth               | 1.76 us                                                     | 1.56 us: 1.13x faster                                                              |
| regex_effbot               | 1.62 ms                                                     | 1.45 ms: 1.12x faster                                                              |
| regex_dna                  | 126 ms                                                      | 114 ms: 1.11x faster                                                               |
| async_generators           | 239 ms                                                      | 218 ms: 1.10x faster                                                               |
| deepcopy_reduce            | 2.09 us                                                     | 1.91 us: 1.09x faster                                                              |
| dulwich_log                | 44.3 ms                                                     | 41.1 ms: 1.08x faster                                                              |
| go                         | 91.6 ms                                                     | 85.0 ms: 1.08x faster                                                              |
| mako                       | 7.09 ms                                                     | 6.66 ms: 1.06x faster                                                              |
| json                       | 3.05 ms                                                     | 2.91 ms: 1.05x faster                                                              |
| coroutines                 | 14.3 ms                                                     | 13.7 ms: 1.04x faster                                                              |
| chaos                      | 43.3 ms                                                     | 41.5 ms: 1.04x faster                                                              |
| sympy_sum                  | 91.5 ms                                                     | 88.2 ms: 1.04x faster                                                              |
| xml_etree_iterparse        | 65.2 ms                                                     | 63.2 ms: 1.03x faster                                                              |
| logging_silent             | 60.5 ns                                                     | 58.8 ns: 1.03x faster                                                              |
| regex_compile              | 87.5 ms                                                     | 85.1 ms: 1.03x faster                                                              |
| xml_etree_parse            | 93.0 ms                                                     | 91.1 ms: 1.02x faster                                                              |
| sympy_str                  | 175 ms                                                      | 173 ms: 1.01x faster                                                               |
| scimark_fft                | 184 ms                                                      | 182 ms: 1.01x faster                                                               |
| docutils                   | 1.66 sec                                                    | 1.64 sec: 1.01x faster                                                             |
| pidigits                   | 152 ms                                                      | 150 ms: 1.01x faster                                                               |
| nbody                      | 71.9 ms                                                     | 71.2 ms: 1.01x faster                                                              |
| deltablue                  | 2.16 ms                                                     | 2.14 ms: 1.01x faster                                                              |
| nqueens                    | 62.8 ms                                                     | 62.3 ms: 1.01x faster                                                              |
| scimark_monte_carlo        | 43.7 ms                                                     | 44.0 ms: 1.01x slower                                                              |
| raytrace                   | 192 ms                                                      | 194 ms: 1.01x slower                                                               |
| regex_v8                   | 14.2 ms                                                     | 14.4 ms: 1.01x slower                                                              |
| 2to3                       | 218 ms                                                      | 221 ms: 1.01x slower                                                               |
| xml_etree_generate         | 55.8 ms                                                     | 56.5 ms: 1.01x slower                                                              |
| logging_simple             | 6.28 us                                                     | 6.35 us: 1.01x slower                                                              |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.59 ms: 1.01x slower                                                              |
| logging_format             | 6.72 us                                                     | 6.81 us: 1.01x slower                                                              |
| sqlglot_optimize           | 34.5 ms                                                     | 35.0 ms: 1.01x slower                                                              |
| sympy_integrate            | 13.0 ms                                                     | 13.2 ms: 1.02x slower                                                              |
| tomli_loads                | 1.37 sec                                                    | 1.40 sec: 1.02x slower                                                             |
| meteor_contest             | 74.6 ms                                                     | 76.4 ms: 1.02x slower                                                              |
| json_loads                 | 13.9 us                                                     | 14.2 us: 1.02x slower                                                              |
| scimark_lu                 | 58.9 ms                                                     | 60.3 ms: 1.02x slower                                                              |
| richards                   | 28.4 ms                                                     | 29.2 ms: 1.03x slower                                                              |
| hexiom                     | 4.10 ms                                                     | 4.22 ms: 1.03x slower                                                              |
| sqlglot_normalize          | 187 ms                                                      | 193 ms: 1.03x slower                                                               |
| pprint_pformat             | 1.05 sec                                                    | 1.08 sec: 1.04x slower                                                             |
| pyflate                    | 295 ms                                                      | 305 ms: 1.04x slower                                                               |
| pycparser                  | 699 ms                                                      | 726 ms: 1.04x slower                                                               |
| sympy_expand               | 284 ms                                                      | 296 ms: 1.04x slower                                                               |
| richards_super             | 32.1 ms                                                     | 33.6 ms: 1.05x slower                                                              |
| pprint_safe_repr           | 513 ms                                                      | 539 ms: 1.05x slower                                                               |
| mdp                        | 1.37 sec                                                    | 1.44 sec: 1.05x slower                                                             |
| sqlglot_transpile          | 1.02 ms                                                     | 1.08 ms: 1.06x slower                                                              |
| scimark_sor                | 78.8 ms                                                     | 83.3 ms: 1.06x slower                                                              |
| xml_etree_process          | 37.7 ms                                                     | 40.5 ms: 1.07x slower                                                              |
| sqlglot_parse              | 804 us                                                      | 873 us: 1.09x slower                                                               |
| unpickle_pure_python       | 133 us                                                      | 145 us: 1.09x slower                                                               |
| coverage                   | 40.8 ms                                                     | 45.2 ms: 1.11x slower                                                              |
| django_template            | 22.9 ms                                                     | 25.5 ms: 1.11x slower                                                              |
| pickle_pure_python         | 195 us                                                      | 219 us: 1.12x slower                                                               |
| typing_runtime_protocols   | 95.1 us                                                     | 107 us: 1.12x slower                                                               |
| fannkuch                   | 247 ms                                                      | 278 ms: 1.13x slower                                                               |
| telco                      | 4.13 ms                                                     | 4.71 ms: 1.14x slower                                                              |
| python_startup_no_site     | 16.2 ms                                                     | 18.6 ms: 1.15x slower                                                              |
| json_dumps                 | 5.70 ms                                                     | 6.64 ms: 1.17x slower                                                              |
| bench_mp_pool              | 69.2 ms                                                     | 84.4 ms: 1.22x slower                                                              |
| python_startup             | 19.5 ms                                                     | 24.8 ms: 1.28x slower                                                              |
| gc_traversal               | 1.52 ms                                                     | 2.01 ms: 1.32x slower                                                              |
| create_gc_cycles           | 752 us                                                      | 1.22 ms: 1.62x slower                                                              |
| Geometric mean             | (ref)                                                       | 1.05x faster                                                                       |

Benchmark hidden because not significant (2): bench_thread_pool, crypto_pyaes
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20250217-3.14.0a5+-21366c3/bm-20250217-pythonperf1-amd64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.055x faster

# HPT report

- Reliability score: 76.84% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown