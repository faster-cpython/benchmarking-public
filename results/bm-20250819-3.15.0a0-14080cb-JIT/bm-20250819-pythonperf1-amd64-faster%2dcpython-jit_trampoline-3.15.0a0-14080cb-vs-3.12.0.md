# Results vs. 3.12.0

- fork: faster-cpython
- ref: jit_trampoline
- machine: windows-amd64
- commit hash: 14080cb
- commit date: 2025-08-19
- overall geometric mean: 1.128x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

Benchmark hidden because not significant (2): 2to3, docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250819-pythonperf1-amd64-faster%2dcpython-jit_trampoline-3.15.0a0-14080cb |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 388 ms: 1.99x faster                                                           |
| async_tree_io              | 731 ms                                                      | 393 ms: 1.86x faster                                                           |
| async_tree_memoization_tg  | 367 ms                                                      | 207 ms: 1.77x faster                                                           |
| async_tree_none_tg         | 285 ms                                                      | 168 ms: 1.70x faster                                                           |
| async_tree_none            | 291 ms                                                      | 173 ms: 1.69x faster                                                           |
| async_tree_memoization     | 339 ms                                                      | 204 ms: 1.66x faster                                                           |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 336 ms: 1.50x faster                                                           |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 331 ms: 1.48x faster                                                           |
| Geometric mean             | (ref)                                                       | 1.70x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250819-pythonperf1-amd64-faster%2dcpython-jit_trampoline-3.15.0a0-14080cb |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 43.6 ms: 1.30x faster                                                          |
| nbody          | 71.9 ms                                                     | 58.0 ms: 1.24x faster                                                          |
| pidigits       | 152 ms                                                      | 148 ms: 1.03x faster                                                           |
| Geometric mean | (ref)                                                       | 1.18x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250819-pythonperf1-amd64-faster%2dcpython-jit_trampoline-3.15.0a0-14080cb |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 79.2 ms: 1.11x faster                                                          |
| regex_dna      | 126 ms                                                      | 118 ms: 1.07x faster                                                           |
| regex_effbot   | 1.62 ms                                                     | 1.57 ms: 1.03x faster                                                          |
| regex_v8       | 14.2 ms                                                     | 13.9 ms: 1.02x faster                                                          |
| Geometric mean | (ref)                                                       | 1.06x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250819-pythonperf1-amd64-faster%2dcpython-jit_trampoline-3.15.0a0-14080cb |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| unpickle_pure_python | 133 us                                                      | 105 us: 1.27x faster                                                           |
| tomli_loads          | 1.37 sec                                                    | 1.12 sec: 1.22x faster                                                         |
| xml_etree_generate   | 55.8 ms                                                     | 50.9 ms: 1.10x faster                                                          |
| json_dumps           | 5.70 ms                                                     | 5.34 ms: 1.07x faster                                                          |
| xml_etree_parse      | 93.0 ms                                                     | 88.6 ms: 1.05x faster                                                          |
| xml_etree_process    | 37.7 ms                                                     | 36.2 ms: 1.04x faster                                                          |
| xml_etree_iterparse  | 65.2 ms                                                     | 64.5 ms: 1.01x faster                                                          |
| json_loads           | 13.9 us                                                     | 14.0 us: 1.01x slower                                                          |
| pickle_pure_python   | 195 us                                                      | 205 us: 1.05x slower                                                           |
| Geometric mean       | (ref)                                                       | 1.07x faster                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250819-pythonperf1-amd64-faster%2dcpython-jit_trampoline-3.15.0a0-14080cb |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 19.0 ms: 1.17x slower                                                          |
| python_startup         | 19.5 ms                                                     | 25.8 ms: 1.32x slower                                                          |
| Geometric mean         | (ref)                                                       | 1.24x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250819-pythonperf1-amd64-faster%2dcpython-jit_trampoline-3.15.0a0-14080cb |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.34 ms: 1.33x faster                                                          |
| django_template | 22.9 ms                                                     | 24.2 ms: 1.06x slower                                                          |
| Geometric mean  | (ref)                                                       | 1.12x faster                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250819-pythonperf1-amd64-faster%2dcpython-jit_trampoline-3.15.0a0-14080cb |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 29.3 ms: 2.75x faster                                                          |
| async_tree_io_tg           | 771 ms                                                      | 388 ms: 1.99x faster                                                           |
| async_tree_io              | 731 ms                                                      | 393 ms: 1.86x faster                                                           |
| async_tree_memoization_tg  | 367 ms                                                      | 207 ms: 1.77x faster                                                           |
| mdp                        | 1.37 sec                                                    | 802 ms: 1.71x faster                                                           |
| async_tree_none_tg         | 285 ms                                                      | 168 ms: 1.70x faster                                                           |
| async_tree_none            | 291 ms                                                      | 173 ms: 1.69x faster                                                           |
| async_tree_memoization     | 339 ms                                                      | 204 ms: 1.66x faster                                                           |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 336 ms: 1.50x faster                                                           |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 331 ms: 1.48x faster                                                           |
| deepcopy                   | 238 us                                                      | 171 us: 1.39x faster                                                           |
| comprehensions             | 14.1 us                                                     | 10.5 us: 1.34x faster                                                          |
| mako                       | 7.09 ms                                                     | 5.34 ms: 1.33x faster                                                          |
| deepcopy_memo              | 23.7 us                                                     | 18.0 us: 1.31x faster                                                          |
| float                      | 56.8 ms                                                     | 43.6 ms: 1.30x faster                                                          |
| unpickle_pure_python       | 133 us                                                      | 105 us: 1.27x faster                                                           |
| nbody                      | 71.9 ms                                                     | 58.0 ms: 1.24x faster                                                          |
| tomli_loads                | 1.37 sec                                                    | 1.12 sec: 1.22x faster                                                         |
| scimark_fft                | 184 ms                                                      | 153 ms: 1.20x faster                                                           |
| go                         | 91.6 ms                                                     | 77.8 ms: 1.18x faster                                                          |
| pprint_pformat             | 1.05 sec                                                    | 890 ms: 1.17x faster                                                           |
| fannkuch                   | 247 ms                                                      | 210 ms: 1.17x faster                                                           |
| pprint_safe_repr           | 513 ms                                                      | 440 ms: 1.17x faster                                                           |
| generators                 | 22.5 ms                                                     | 19.5 ms: 1.15x faster                                                          |
| sqlite_synth               | 1.76 us                                                     | 1.54 us: 1.14x faster                                                          |
| pyflate                    | 295 ms                                                      | 261 ms: 1.13x faster                                                           |
| deepcopy_reduce            | 2.09 us                                                     | 1.87 us: 1.12x faster                                                          |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.29 ms: 1.12x faster                                                          |
| logging_silent             | 60.5 ns                                                     | 54.3 ns: 1.11x faster                                                          |
| regex_compile              | 87.5 ms                                                     | 79.2 ms: 1.11x faster                                                          |
| xml_etree_generate         | 55.8 ms                                                     | 50.9 ms: 1.10x faster                                                          |
| dulwich_log                | 44.3 ms                                                     | 40.4 ms: 1.10x faster                                                          |
| scimark_monte_carlo        | 43.7 ms                                                     | 40.2 ms: 1.09x faster                                                          |
| regex_dna                  | 126 ms                                                      | 118 ms: 1.07x faster                                                           |
| json_dumps                 | 5.70 ms                                                     | 5.34 ms: 1.07x faster                                                          |
| crypto_pyaes               | 48.5 ms                                                     | 45.5 ms: 1.07x faster                                                          |
| chaos                      | 43.3 ms                                                     | 40.7 ms: 1.07x faster                                                          |
| raytrace                   | 192 ms                                                      | 183 ms: 1.05x faster                                                           |
| logging_simple             | 6.28 us                                                     | 5.97 us: 1.05x faster                                                          |
| sympy_sum                  | 91.5 ms                                                     | 87.2 ms: 1.05x faster                                                          |
| xml_etree_parse            | 93.0 ms                                                     | 88.6 ms: 1.05x faster                                                          |
| meteor_contest             | 74.6 ms                                                     | 71.4 ms: 1.04x faster                                                          |
| logging_format             | 6.72 us                                                     | 6.45 us: 1.04x faster                                                          |
| xml_etree_process          | 37.7 ms                                                     | 36.2 ms: 1.04x faster                                                          |
| nqueens                    | 62.8 ms                                                     | 60.8 ms: 1.03x faster                                                          |
| regex_effbot               | 1.62 ms                                                     | 1.57 ms: 1.03x faster                                                          |
| pidigits                   | 152 ms                                                      | 148 ms: 1.03x faster                                                           |
| sympy_str                  | 175 ms                                                      | 170 ms: 1.03x faster                                                           |
| richards_super             | 32.1 ms                                                     | 31.3 ms: 1.03x faster                                                          |
| spectral_norm              | 66.9 ms                                                     | 65.3 ms: 1.03x faster                                                          |
| scimark_sor                | 78.8 ms                                                     | 76.9 ms: 1.02x faster                                                          |
| regex_v8                   | 14.2 ms                                                     | 13.9 ms: 1.02x faster                                                          |
| richards                   | 28.4 ms                                                     | 27.9 ms: 1.02x faster                                                          |
| telco                      | 4.13 ms                                                     | 4.06 ms: 1.02x faster                                                          |
| sympy_integrate            | 13.0 ms                                                     | 12.8 ms: 1.02x faster                                                          |
| json                       | 3.05 ms                                                     | 3.00 ms: 1.01x faster                                                          |
| xml_etree_iterparse        | 65.2 ms                                                     | 64.5 ms: 1.01x faster                                                          |
| json_loads                 | 13.9 us                                                     | 14.0 us: 1.01x slower                                                          |
| pycparser                  | 699 ms                                                      | 708 ms: 1.01x slower                                                           |
| coroutines                 | 14.3 ms                                                     | 14.5 ms: 1.02x slower                                                          |
| deltablue                  | 2.16 ms                                                     | 2.22 ms: 1.03x slower                                                          |
| async_generators           | 239 ms                                                      | 247 ms: 1.03x slower                                                           |
| scimark_lu                 | 58.9 ms                                                     | 61.1 ms: 1.04x slower                                                          |
| sympy_expand               | 284 ms                                                      | 298 ms: 1.05x slower                                                           |
| pickle_pure_python         | 195 us                                                      | 205 us: 1.05x slower                                                           |
| django_template            | 22.9 ms                                                     | 24.2 ms: 1.06x slower                                                          |
| typing_runtime_protocols   | 95.1 us                                                     | 102 us: 1.07x slower                                                           |
| python_startup_no_site     | 16.2 ms                                                     | 19.0 ms: 1.17x slower                                                          |
| coverage                   | 40.8 ms                                                     | 50.0 ms: 1.23x slower                                                          |
| python_startup             | 19.5 ms                                                     | 25.8 ms: 1.32x slower                                                          |
| gc_traversal               | 1.52 ms                                                     | 2.10 ms: 1.38x slower                                                          |
| create_gc_cycles           | 752 us                                                      | 1.27 ms: 1.68x slower                                                          |
| Geometric mean             | (ref)                                                       | 1.13x faster                                                                   |

Benchmark hidden because not significant (3): hexiom, docutils, 2to3
Ignored benchmarks (21) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250819-3.15.0a0-14080cb-JIT/bm-20250819-pythonperf1-amd64-faster%2dcpython-jit_trampoline-3.15.0a0-14080cb.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.128x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: unknown