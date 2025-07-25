# Results vs. 3.12.0

- fork: faster-cpython
- ref: check_periodic_at_en
- machine: windows-amd64
- commit hash: 021fc09
- commit date: 2025-07-25
- overall geometric mean: 1.109x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250725-pythonperf1-amd64-faster%2dcpython-check_periodic_at_en-3.15.0a0-021fc09 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 222 ms: 1.02x slower                                                                 |
| Geometric mean | (ref)                                                       | 1.01x slower                                                                         |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250725-pythonperf1-amd64-faster%2dcpython-check_periodic_at_en-3.15.0a0-021fc09 |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 385 ms: 2.00x faster                                                                 |
| async_tree_io              | 731 ms                                                      | 393 ms: 1.86x faster                                                                 |
| async_tree_memoization_tg  | 367 ms                                                      | 215 ms: 1.71x faster                                                                 |
| async_tree_none_tg         | 285 ms                                                      | 173 ms: 1.64x faster                                                                 |
| async_tree_none            | 291 ms                                                      | 180 ms: 1.62x faster                                                                 |
| async_tree_memoization     | 339 ms                                                      | 214 ms: 1.58x faster                                                                 |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 342 ms: 1.47x faster                                                                 |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 337 ms: 1.45x faster                                                                 |
| Geometric mean             | (ref)                                                       | 1.66x faster                                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250725-pythonperf1-amd64-faster%2dcpython-check_periodic_at_en-3.15.0a0-021fc09 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| nbody          | 71.9 ms                                                     | 55.8 ms: 1.29x faster                                                                |
| float          | 56.8 ms                                                     | 44.5 ms: 1.28x faster                                                                |
| pidigits       | 152 ms                                                      | 150 ms: 1.01x faster                                                                 |
| Geometric mean | (ref)                                                       | 1.19x faster                                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250725-pythonperf1-amd64-faster%2dcpython-check_periodic_at_en-3.15.0a0-021fc09 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 78.7 ms: 1.11x faster                                                                |
| regex_dna      | 126 ms                                                      | 119 ms: 1.06x faster                                                                 |
| Geometric mean | (ref)                                                       | 1.05x faster                                                                         |

Benchmark hidden because not significant (2): regex_v8, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250725-pythonperf1-amd64-faster%2dcpython-check_periodic_at_en-3.15.0a0-021fc09 |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| tomli_loads          | 1.37 sec                                                    | 1.11 sec: 1.23x faster                                                               |
| unpickle_pure_python | 133 us                                                      | 113 us: 1.18x faster                                                                 |
| xml_etree_generate   | 55.8 ms                                                     | 51.4 ms: 1.09x faster                                                                |
| xml_etree_process    | 37.7 ms                                                     | 36.2 ms: 1.04x faster                                                                |
| xml_etree_parse      | 93.0 ms                                                     | 91.1 ms: 1.02x faster                                                                |
| xml_etree_iterparse  | 65.2 ms                                                     | 66.7 ms: 1.02x slower                                                                |
| pickle_pure_python   | 195 us                                                      | 207 us: 1.06x slower                                                                 |
| json_loads           | 13.9 us                                                     | 14.8 us: 1.07x slower                                                                |
| json_dumps           | 5.70 ms                                                     | 6.30 ms: 1.11x slower                                                                |
| Geometric mean       | (ref)                                                       | 1.03x faster                                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250725-pythonperf1-amd64-faster%2dcpython-check_periodic_at_en-3.15.0a0-021fc09 |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 19.9 ms: 1.23x slower                                                                |
| python_startup         | 19.5 ms                                                     | 26.7 ms: 1.37x slower                                                                |
| Geometric mean         | (ref)                                                       | 1.30x slower                                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250725-pythonperf1-amd64-faster%2dcpython-check_periodic_at_en-3.15.0a0-021fc09 |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.51 ms: 1.29x faster                                                                |
| django_template | 22.9 ms                                                     | 24.1 ms: 1.05x slower                                                                |
| Geometric mean  | (ref)                                                       | 1.11x faster                                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250725-pythonperf1-amd64-faster%2dcpython-check_periodic_at_en-3.15.0a0-021fc09 |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 33.2 ms: 2.43x faster                                                                |
| async_tree_io_tg           | 771 ms                                                      | 385 ms: 2.00x faster                                                                 |
| async_tree_io              | 731 ms                                                      | 393 ms: 1.86x faster                                                                 |
| async_tree_memoization_tg  | 367 ms                                                      | 215 ms: 1.71x faster                                                                 |
| mdp                        | 1.37 sec                                                    | 823 ms: 1.67x faster                                                                 |
| async_tree_none_tg         | 285 ms                                                      | 173 ms: 1.64x faster                                                                 |
| async_tree_none            | 291 ms                                                      | 180 ms: 1.62x faster                                                                 |
| async_tree_memoization     | 339 ms                                                      | 214 ms: 1.58x faster                                                                 |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 342 ms: 1.47x faster                                                                 |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 337 ms: 1.45x faster                                                                 |
| deepcopy                   | 238 us                                                      | 170 us: 1.40x faster                                                                 |
| comprehensions             | 14.1 us                                                     | 10.5 us: 1.34x faster                                                                |
| deepcopy_memo              | 23.7 us                                                     | 18.0 us: 1.31x faster                                                                |
| nbody                      | 71.9 ms                                                     | 55.8 ms: 1.29x faster                                                                |
| mako                       | 7.09 ms                                                     | 5.51 ms: 1.29x faster                                                                |
| float                      | 56.8 ms                                                     | 44.5 ms: 1.28x faster                                                                |
| tomli_loads                | 1.37 sec                                                    | 1.11 sec: 1.23x faster                                                               |
| scimark_fft                | 184 ms                                                      | 151 ms: 1.22x faster                                                                 |
| unpickle_pure_python       | 133 us                                                      | 113 us: 1.18x faster                                                                 |
| pprint_pformat             | 1.05 sec                                                    | 896 ms: 1.17x faster                                                                 |
| go                         | 91.6 ms                                                     | 78.8 ms: 1.16x faster                                                                |
| pyflate                    | 295 ms                                                      | 257 ms: 1.15x faster                                                                 |
| generators                 | 22.5 ms                                                     | 19.8 ms: 1.14x faster                                                                |
| fannkuch                   | 247 ms                                                      | 217 ms: 1.14x faster                                                                 |
| pprint_safe_repr           | 513 ms                                                      | 454 ms: 1.13x faster                                                                 |
| deepcopy_reduce            | 2.09 us                                                     | 1.85 us: 1.13x faster                                                                |
| sqlite_synth               | 1.76 us                                                     | 1.58 us: 1.12x faster                                                                |
| regex_compile              | 87.5 ms                                                     | 78.7 ms: 1.11x faster                                                                |
| raytrace                   | 192 ms                                                      | 177 ms: 1.09x faster                                                                 |
| logging_silent             | 60.5 ns                                                     | 55.6 ns: 1.09x faster                                                                |
| xml_etree_generate         | 55.8 ms                                                     | 51.4 ms: 1.09x faster                                                                |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.39 ms: 1.07x faster                                                                |
| regex_dna                  | 126 ms                                                      | 119 ms: 1.06x faster                                                                 |
| dulwich_log                | 44.3 ms                                                     | 42.0 ms: 1.05x faster                                                                |
| scimark_monte_carlo        | 43.7 ms                                                     | 41.8 ms: 1.05x faster                                                                |
| sympy_sum                  | 91.5 ms                                                     | 87.7 ms: 1.04x faster                                                                |
| chaos                      | 43.3 ms                                                     | 41.6 ms: 1.04x faster                                                                |
| richards_super             | 32.1 ms                                                     | 30.8 ms: 1.04x faster                                                                |
| xml_etree_process          | 37.7 ms                                                     | 36.2 ms: 1.04x faster                                                                |
| crypto_pyaes               | 48.5 ms                                                     | 46.6 ms: 1.04x faster                                                                |
| nqueens                    | 62.8 ms                                                     | 60.4 ms: 1.04x faster                                                                |
| richards                   | 28.4 ms                                                     | 27.5 ms: 1.03x faster                                                                |
| xml_etree_parse            | 93.0 ms                                                     | 91.1 ms: 1.02x faster                                                                |
| sympy_str                  | 175 ms                                                      | 172 ms: 1.02x faster                                                                 |
| logging_simple             | 6.28 us                                                     | 6.17 us: 1.02x faster                                                                |
| pidigits                   | 152 ms                                                      | 150 ms: 1.01x faster                                                                 |
| json                       | 3.05 ms                                                     | 3.02 ms: 1.01x faster                                                                |
| sympy_integrate            | 13.0 ms                                                     | 12.8 ms: 1.01x faster                                                                |
| hexiom                     | 4.10 ms                                                     | 4.16 ms: 1.01x slower                                                                |
| coroutines                 | 14.3 ms                                                     | 14.5 ms: 1.01x slower                                                                |
| 2to3                       | 218 ms                                                      | 222 ms: 1.02x slower                                                                 |
| xml_etree_iterparse        | 65.2 ms                                                     | 66.7 ms: 1.02x slower                                                                |
| spectral_norm              | 66.9 ms                                                     | 68.8 ms: 1.03x slower                                                                |
| scimark_lu                 | 58.9 ms                                                     | 60.6 ms: 1.03x slower                                                                |
| sympy_expand               | 284 ms                                                      | 294 ms: 1.04x slower                                                                 |
| telco                      | 4.13 ms                                                     | 4.30 ms: 1.04x slower                                                                |
| django_template            | 22.9 ms                                                     | 24.1 ms: 1.05x slower                                                                |
| async_generators           | 239 ms                                                      | 252 ms: 1.05x slower                                                                 |
| deltablue                  | 2.16 ms                                                     | 2.28 ms: 1.06x slower                                                                |
| pickle_pure_python         | 195 us                                                      | 207 us: 1.06x slower                                                                 |
| json_loads                 | 13.9 us                                                     | 14.8 us: 1.07x slower                                                                |
| typing_runtime_protocols   | 95.1 us                                                     | 105 us: 1.10x slower                                                                 |
| json_dumps                 | 5.70 ms                                                     | 6.30 ms: 1.11x slower                                                                |
| python_startup_no_site     | 16.2 ms                                                     | 19.9 ms: 1.23x slower                                                                |
| coverage                   | 40.8 ms                                                     | 50.9 ms: 1.25x slower                                                                |
| python_startup             | 19.5 ms                                                     | 26.7 ms: 1.37x slower                                                                |
| gc_traversal               | 1.52 ms                                                     | 2.17 ms: 1.43x slower                                                                |
| create_gc_cycles           | 752 us                                                      | 1.34 ms: 1.79x slower                                                                |
| Geometric mean             | (ref)                                                       | 1.10x faster                                                                         |

Benchmark hidden because not significant (7): regex_v8, meteor_contest, regex_effbot, docutils, scimark_sor, pycparser, logging_format
Ignored benchmarks (21) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250725-3.15.0a0-021fc09-JIT/bm-20250725-pythonperf1-amd64-faster%2dcpython-check_periodic_at_en-3.15.0a0-021fc09.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.109x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: unknown