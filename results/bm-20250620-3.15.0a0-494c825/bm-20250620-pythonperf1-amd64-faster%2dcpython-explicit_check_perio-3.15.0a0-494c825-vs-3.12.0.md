# Results vs. 3.12.0

- fork: faster-cpython
- ref: explicit_check_perio
- machine: windows-amd64
- commit hash: 494c825
- commit date: 2025-06-20
- overall geometric mean: 1.073x faster
- HPT reliability: 99.66%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250620-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-494c825 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 221 ms: 1.02x slower                                                                 |
| docutils       | 1.66 sec                                                    | 1.63 sec: 1.02x faster                                                               |
| Geometric mean | (ref)                                                       | 1.00x faster                                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250620-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-494c825 |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 406 ms: 1.90x faster                                                                 |
| async_tree_io              | 731 ms                                                      | 415 ms: 1.76x faster                                                                 |
| async_tree_memoization_tg  | 367 ms                                                      | 218 ms: 1.69x faster                                                                 |
| async_tree_none            | 291 ms                                                      | 177 ms: 1.65x faster                                                                 |
| async_tree_none_tg         | 285 ms                                                      | 174 ms: 1.64x faster                                                                 |
| async_tree_memoization     | 339 ms                                                      | 214 ms: 1.59x faster                                                                 |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 333 ms: 1.47x faster                                                                 |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 347 ms: 1.45x faster                                                                 |
| Geometric mean             | (ref)                                                       | 1.64x faster                                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250620-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-494c825 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 44.5 ms: 1.28x faster                                                                |
| nbody          | 71.9 ms                                                     | 65.2 ms: 1.10x faster                                                                |
| pidigits       | 152 ms                                                      | 146 ms: 1.04x faster                                                                 |
| Geometric mean | (ref)                                                       | 1.14x faster                                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250620-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-494c825 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 82.0 ms: 1.07x faster                                                                |
| regex_effbot   | 1.62 ms                                                     | 1.52 ms: 1.07x faster                                                                |
| regex_dna      | 126 ms                                                      | 121 ms: 1.04x faster                                                                 |
| Geometric mean | (ref)                                                       | 1.04x faster                                                                         |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250620-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-494c825 |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| xml_etree_parse      | 93.0 ms                                                     | 88.4 ms: 1.05x faster                                                                |
| xml_etree_iterparse  | 65.2 ms                                                     | 64.5 ms: 1.01x faster                                                                |
| xml_etree_generate   | 55.8 ms                                                     | 57.1 ms: 1.02x slower                                                                |
| unpickle_pure_python | 133 us                                                      | 138 us: 1.04x slower                                                                 |
| tomli_loads          | 1.37 sec                                                    | 1.43 sec: 1.05x slower                                                               |
| json_loads           | 13.9 us                                                     | 14.6 us: 1.05x slower                                                                |
| xml_etree_process    | 37.7 ms                                                     | 39.7 ms: 1.05x slower                                                                |
| json_dumps           | 5.70 ms                                                     | 6.24 ms: 1.10x slower                                                                |
| pickle_pure_python   | 195 us                                                      | 219 us: 1.12x slower                                                                 |
| Geometric mean       | (ref)                                                       | 1.04x slower                                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250620-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-494c825 |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 19.4 ms: 1.19x slower                                                                |
| python_startup         | 19.5 ms                                                     | 26.0 ms: 1.34x slower                                                                |
| Geometric mean         | (ref)                                                       | 1.26x slower                                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250620-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-494c825 |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.81 ms: 1.04x faster                                                                |
| django_template | 22.9 ms                                                     | 24.4 ms: 1.06x slower                                                                |
| Geometric mean  | (ref)                                                       | 1.01x slower                                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250620-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-494c825 |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 31.8 ms: 2.53x faster                                                                |
| async_tree_io_tg           | 771 ms                                                      | 406 ms: 1.90x faster                                                                 |
| async_tree_io              | 731 ms                                                      | 415 ms: 1.76x faster                                                                 |
| mdp                        | 1.37 sec                                                    | 813 ms: 1.69x faster                                                                 |
| async_tree_memoization_tg  | 367 ms                                                      | 218 ms: 1.69x faster                                                                 |
| async_tree_none            | 291 ms                                                      | 177 ms: 1.65x faster                                                                 |
| async_tree_none_tg         | 285 ms                                                      | 174 ms: 1.64x faster                                                                 |
| async_tree_memoization     | 339 ms                                                      | 214 ms: 1.59x faster                                                                 |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 333 ms: 1.47x faster                                                                 |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 347 ms: 1.45x faster                                                                 |
| deepcopy                   | 238 us                                                      | 176 us: 1.35x faster                                                                 |
| float                      | 56.8 ms                                                     | 44.5 ms: 1.28x faster                                                                |
| comprehensions             | 14.1 us                                                     | 11.1 us: 1.27x faster                                                                |
| deepcopy_memo              | 23.7 us                                                     | 18.8 us: 1.26x faster                                                                |
| go                         | 91.6 ms                                                     | 77.8 ms: 1.18x faster                                                                |
| generators                 | 22.5 ms                                                     | 19.6 ms: 1.15x faster                                                                |
| deepcopy_reduce            | 2.09 us                                                     | 1.85 us: 1.13x faster                                                                |
| sqlite_synth               | 1.76 us                                                     | 1.59 us: 1.11x faster                                                                |
| nbody                      | 71.9 ms                                                     | 65.2 ms: 1.10x faster                                                                |
| spectral_norm              | 66.9 ms                                                     | 62.2 ms: 1.08x faster                                                                |
| chaos                      | 43.3 ms                                                     | 40.5 ms: 1.07x faster                                                                |
| regex_compile              | 87.5 ms                                                     | 82.0 ms: 1.07x faster                                                                |
| scimark_monte_carlo        | 43.7 ms                                                     | 41.0 ms: 1.07x faster                                                                |
| regex_effbot               | 1.62 ms                                                     | 1.52 ms: 1.07x faster                                                                |
| dulwich_log                | 44.3 ms                                                     | 41.6 ms: 1.06x faster                                                                |
| xml_etree_parse            | 93.0 ms                                                     | 88.4 ms: 1.05x faster                                                                |
| raytrace                   | 192 ms                                                      | 183 ms: 1.05x faster                                                                 |
| regex_dna                  | 126 ms                                                      | 121 ms: 1.04x faster                                                                 |
| pidigits                   | 152 ms                                                      | 146 ms: 1.04x faster                                                                 |
| mako                       | 7.09 ms                                                     | 6.81 ms: 1.04x faster                                                                |
| async_generators           | 239 ms                                                      | 231 ms: 1.04x faster                                                                 |
| sympy_sum                  | 91.5 ms                                                     | 88.8 ms: 1.03x faster                                                                |
| sympy_integrate            | 13.0 ms                                                     | 12.7 ms: 1.02x faster                                                                |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.51 ms: 1.02x faster                                                                |
| docutils                   | 1.66 sec                                                    | 1.63 sec: 1.02x faster                                                               |
| sympy_str                  | 175 ms                                                      | 172 ms: 1.02x faster                                                                 |
| nqueens                    | 62.8 ms                                                     | 62.1 ms: 1.01x faster                                                                |
| xml_etree_iterparse        | 65.2 ms                                                     | 64.5 ms: 1.01x faster                                                                |
| scimark_fft                | 184 ms                                                      | 183 ms: 1.01x faster                                                                 |
| scimark_sor                | 78.8 ms                                                     | 78.2 ms: 1.01x faster                                                                |
| richards_super             | 32.1 ms                                                     | 31.9 ms: 1.01x faster                                                                |
| logging_simple             | 6.28 us                                                     | 6.36 us: 1.01x slower                                                                |
| logging_format             | 6.72 us                                                     | 6.81 us: 1.01x slower                                                                |
| 2to3                       | 218 ms                                                      | 221 ms: 1.02x slower                                                                 |
| scimark_lu                 | 58.9 ms                                                     | 59.9 ms: 1.02x slower                                                                |
| coroutines                 | 14.3 ms                                                     | 14.5 ms: 1.02x slower                                                                |
| xml_etree_generate         | 55.8 ms                                                     | 57.1 ms: 1.02x slower                                                                |
| pycparser                  | 699 ms                                                      | 717 ms: 1.03x slower                                                                 |
| hexiom                     | 4.10 ms                                                     | 4.22 ms: 1.03x slower                                                                |
| sympy_expand               | 284 ms                                                      | 292 ms: 1.03x slower                                                                 |
| unpickle_pure_python       | 133 us                                                      | 138 us: 1.04x slower                                                                 |
| tomli_loads                | 1.37 sec                                                    | 1.43 sec: 1.05x slower                                                               |
| json_loads                 | 13.9 us                                                     | 14.6 us: 1.05x slower                                                                |
| xml_etree_process          | 37.7 ms                                                     | 39.7 ms: 1.05x slower                                                                |
| deltablue                  | 2.16 ms                                                     | 2.29 ms: 1.06x slower                                                                |
| pprint_pformat             | 1.05 sec                                                    | 1.11 sec: 1.06x slower                                                               |
| django_template            | 22.9 ms                                                     | 24.4 ms: 1.06x slower                                                                |
| pprint_safe_repr           | 513 ms                                                      | 548 ms: 1.07x slower                                                                 |
| fannkuch                   | 247 ms                                                      | 265 ms: 1.08x slower                                                                 |
| json_dumps                 | 5.70 ms                                                     | 6.24 ms: 1.10x slower                                                                |
| typing_runtime_protocols   | 95.1 us                                                     | 104 us: 1.10x slower                                                                 |
| pickle_pure_python         | 195 us                                                      | 219 us: 1.12x slower                                                                 |
| telco                      | 4.13 ms                                                     | 4.63 ms: 1.12x slower                                                                |
| coverage                   | 40.8 ms                                                     | 48.7 ms: 1.19x slower                                                                |
| python_startup_no_site     | 16.2 ms                                                     | 19.4 ms: 1.19x slower                                                                |
| python_startup             | 19.5 ms                                                     | 26.0 ms: 1.34x slower                                                                |
| gc_traversal               | 1.52 ms                                                     | 2.14 ms: 1.41x slower                                                                |
| create_gc_cycles           | 752 us                                                      | 1.32 ms: 1.76x slower                                                                |
| logging_silent             | 60.5 ns                                                     | 318 ns: 5.26x slower                                                                 |
| Geometric mean             | (ref)                                                       | 1.05x faster                                                                         |

Benchmark hidden because not significant (6): richards, regex_v8, meteor_contest, json, crypto_pyaes, pyflate
Ignored benchmarks (21) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250620-3.15.0a0-494c825/bm-20250620-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-494c825.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.073x faster

# HPT report

- Reliability score: 99.66% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown