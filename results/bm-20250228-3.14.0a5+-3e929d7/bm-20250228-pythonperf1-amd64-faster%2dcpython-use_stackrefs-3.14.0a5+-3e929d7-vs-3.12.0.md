# Results vs. 3.12.0

- fork: faster-cpython
- ref: use_stackrefs
- machine: windows-amd64
- commit hash: 3e929d7
- commit date: 2025-02-28
- overall geometric mean: 1.030x faster
- HPT reliability: 83.58%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250228-pythonperf1-amd64-faster%2dcpython-use_stackrefs-3.14.0a5+-3e929d7 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 227 ms: 1.04x slower                                                           |
| docutils       | 1.66 sec                                                    | 1.69 sec: 1.02x slower                                                         |
| Geometric mean | (ref)                                                       | 1.03x slower                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250228-pythonperf1-amd64-faster%2dcpython-use_stackrefs-3.14.0a5+-3e929d7 |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 414 ms: 1.86x faster                                                           |
| async_tree_io              | 731 ms                                                      | 423 ms: 1.73x faster                                                           |
| async_tree_memoization_tg  | 367 ms                                                      | 218 ms: 1.69x faster                                                           |
| async_tree_none_tg         | 285 ms                                                      | 178 ms: 1.60x faster                                                           |
| async_tree_none            | 291 ms                                                      | 188 ms: 1.55x faster                                                           |
| async_tree_memoization     | 339 ms                                                      | 221 ms: 1.53x faster                                                           |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 348 ms: 1.44x faster                                                           |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 345 ms: 1.42x faster                                                           |
| Geometric mean             | (ref)                                                       | 1.60x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250228-pythonperf1-amd64-faster%2dcpython-use_stackrefs-3.14.0a5+-3e929d7 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 46.5 ms: 1.22x faster                                                          |
| nbody          | 71.9 ms                                                     | 68.6 ms: 1.05x faster                                                          |
| pidigits       | 152 ms                                                      | 151 ms: 1.01x faster                                                           |
| Geometric mean | (ref)                                                       | 1.09x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250228-pythonperf1-amd64-faster%2dcpython-use_stackrefs-3.14.0a5+-3e929d7 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.47 ms: 1.10x faster                                                          |
| regex_dna      | 126 ms                                                      | 117 ms: 1.08x faster                                                           |
| regex_compile  | 87.5 ms                                                     | 85.9 ms: 1.02x faster                                                          |
| regex_v8       | 14.2 ms                                                     | 15.5 ms: 1.09x slower                                                          |
| Geometric mean | (ref)                                                       | 1.03x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250228-pythonperf1-amd64-faster%2dcpython-use_stackrefs-3.14.0a5+-3e929d7 |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| xml_etree_parse      | 93.0 ms                                                     | 90.3 ms: 1.03x faster                                                          |
| xml_etree_iterparse  | 65.2 ms                                                     | 63.7 ms: 1.02x faster                                                          |
| tomli_loads          | 1.37 sec                                                    | 1.42 sec: 1.04x slower                                                         |
| xml_etree_generate   | 55.8 ms                                                     | 58.7 ms: 1.05x slower                                                          |
| json_loads           | 13.9 us                                                     | 14.7 us: 1.06x slower                                                          |
| unpickle_pure_python | 133 us                                                      | 148 us: 1.11x slower                                                           |
| xml_etree_process    | 37.7 ms                                                     | 42.3 ms: 1.12x slower                                                          |
| pickle_pure_python   | 195 us                                                      | 230 us: 1.18x slower                                                           |
| json_dumps           | 5.70 ms                                                     | 6.97 ms: 1.22x slower                                                          |
| Geometric mean       | (ref)                                                       | 1.08x slower                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250228-pythonperf1-amd64-faster%2dcpython-use_stackrefs-3.14.0a5+-3e929d7 |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 19.2 ms: 1.18x slower                                                          |
| python_startup         | 19.5 ms                                                     | 25.2 ms: 1.29x slower                                                          |
| Geometric mean         | (ref)                                                       | 1.24x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250228-pythonperf1-amd64-faster%2dcpython-use_stackrefs-3.14.0a5+-3e929d7 |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.93 ms: 1.02x faster                                                          |
| django_template | 22.9 ms                                                     | 26.4 ms: 1.15x slower                                                          |
| Geometric mean  | (ref)                                                       | 1.06x slower                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250228-pythonperf1-amd64-faster%2dcpython-use_stackrefs-3.14.0a5+-3e929d7 |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 32.2 ms: 2.50x faster                                                          |
| async_tree_io_tg           | 771 ms                                                      | 414 ms: 1.86x faster                                                           |
| async_tree_io              | 731 ms                                                      | 423 ms: 1.73x faster                                                           |
| async_tree_memoization_tg  | 367 ms                                                      | 218 ms: 1.69x faster                                                           |
| async_tree_none_tg         | 285 ms                                                      | 178 ms: 1.60x faster                                                           |
| async_tree_none            | 291 ms                                                      | 188 ms: 1.55x faster                                                           |
| async_tree_memoization     | 339 ms                                                      | 221 ms: 1.53x faster                                                           |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 348 ms: 1.44x faster                                                           |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 345 ms: 1.42x faster                                                           |
| deepcopy                   | 238 us                                                      | 183 us: 1.30x faster                                                           |
| float                      | 56.8 ms                                                     | 46.5 ms: 1.22x faster                                                          |
| deepcopy_memo              | 23.7 us                                                     | 19.5 us: 1.22x faster                                                          |
| comprehensions             | 14.1 us                                                     | 12.0 us: 1.18x faster                                                          |
| generators                 | 22.5 ms                                                     | 19.6 ms: 1.15x faster                                                          |
| sqlite_synth               | 1.76 us                                                     | 1.58 us: 1.12x faster                                                          |
| spectral_norm              | 66.9 ms                                                     | 60.0 ms: 1.12x faster                                                          |
| regex_effbot               | 1.62 ms                                                     | 1.47 ms: 1.10x faster                                                          |
| regex_dna                  | 126 ms                                                      | 117 ms: 1.08x faster                                                           |
| deepcopy_reduce            | 2.09 us                                                     | 1.96 us: 1.07x faster                                                          |
| nbody                      | 71.9 ms                                                     | 68.6 ms: 1.05x faster                                                          |
| dulwich_log                | 44.3 ms                                                     | 42.4 ms: 1.04x faster                                                          |
| async_generators           | 239 ms                                                      | 230 ms: 1.04x faster                                                           |
| coroutines                 | 14.3 ms                                                     | 13.7 ms: 1.04x faster                                                          |
| logging_silent             | 60.5 ns                                                     | 58.5 ns: 1.03x faster                                                          |
| go                         | 91.6 ms                                                     | 88.8 ms: 1.03x faster                                                          |
| xml_etree_parse            | 93.0 ms                                                     | 90.3 ms: 1.03x faster                                                          |
| xml_etree_iterparse        | 65.2 ms                                                     | 63.7 ms: 1.02x faster                                                          |
| mako                       | 7.09 ms                                                     | 6.93 ms: 1.02x faster                                                          |
| sympy_sum                  | 91.5 ms                                                     | 89.6 ms: 1.02x faster                                                          |
| regex_compile              | 87.5 ms                                                     | 85.9 ms: 1.02x faster                                                          |
| pidigits                   | 152 ms                                                      | 151 ms: 1.01x faster                                                           |
| sympy_str                  | 175 ms                                                      | 176 ms: 1.01x slower                                                           |
| chaos                      | 43.3 ms                                                     | 43.9 ms: 1.01x slower                                                          |
| docutils                   | 1.66 sec                                                    | 1.69 sec: 1.02x slower                                                         |
| sympy_integrate            | 13.0 ms                                                     | 13.2 ms: 1.02x slower                                                          |
| scimark_sor                | 78.8 ms                                                     | 80.3 ms: 1.02x slower                                                          |
| scimark_monte_carlo        | 43.7 ms                                                     | 44.6 ms: 1.02x slower                                                          |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.61 ms: 1.02x slower                                                          |
| raytrace                   | 192 ms                                                      | 197 ms: 1.02x slower                                                           |
| richards                   | 28.4 ms                                                     | 29.1 ms: 1.03x slower                                                          |
| meteor_contest             | 74.6 ms                                                     | 76.8 ms: 1.03x slower                                                          |
| scimark_fft                | 184 ms                                                      | 190 ms: 1.03x slower                                                           |
| richards_super             | 32.1 ms                                                     | 33.0 ms: 1.03x slower                                                          |
| tomli_loads                | 1.37 sec                                                    | 1.42 sec: 1.04x slower                                                         |
| logging_simple             | 6.28 us                                                     | 6.52 us: 1.04x slower                                                          |
| nqueens                    | 62.8 ms                                                     | 65.3 ms: 1.04x slower                                                          |
| crypto_pyaes               | 48.5 ms                                                     | 50.5 ms: 1.04x slower                                                          |
| 2to3                       | 218 ms                                                      | 227 ms: 1.04x slower                                                           |
| pprint_pformat             | 1.05 sec                                                    | 1.10 sec: 1.05x slower                                                         |
| xml_etree_generate         | 55.8 ms                                                     | 58.7 ms: 1.05x slower                                                          |
| logging_format             | 6.72 us                                                     | 7.06 us: 1.05x slower                                                          |
| pprint_safe_repr           | 513 ms                                                      | 540 ms: 1.05x slower                                                           |
| sqlglot_optimize           | 34.5 ms                                                     | 36.4 ms: 1.05x slower                                                          |
| deltablue                  | 2.16 ms                                                     | 2.28 ms: 1.06x slower                                                          |
| json_loads                 | 13.9 us                                                     | 14.7 us: 1.06x slower                                                          |
| pyflate                    | 295 ms                                                      | 312 ms: 1.06x slower                                                           |
| scimark_lu                 | 58.9 ms                                                     | 62.4 ms: 1.06x slower                                                          |
| sympy_expand               | 284 ms                                                      | 301 ms: 1.06x slower                                                           |
| hexiom                     | 4.10 ms                                                     | 4.36 ms: 1.06x slower                                                          |
| sqlglot_normalize          | 187 ms                                                      | 199 ms: 1.07x slower                                                           |
| sqlglot_transpile          | 1.02 ms                                                     | 1.11 ms: 1.08x slower                                                          |
| pycparser                  | 699 ms                                                      | 761 ms: 1.09x slower                                                           |
| regex_v8                   | 14.2 ms                                                     | 15.5 ms: 1.09x slower                                                          |
| sqlglot_parse              | 804 us                                                      | 892 us: 1.11x slower                                                           |
| unpickle_pure_python       | 133 us                                                      | 148 us: 1.11x slower                                                           |
| xml_etree_process          | 37.7 ms                                                     | 42.3 ms: 1.12x slower                                                          |
| fannkuch                   | 247 ms                                                      | 277 ms: 1.12x slower                                                           |
| django_template            | 22.9 ms                                                     | 26.4 ms: 1.15x slower                                                          |
| mdp                        | 1.37 sec                                                    | 1.59 sec: 1.16x slower                                                         |
| pickle_pure_python         | 195 us                                                      | 230 us: 1.18x slower                                                           |
| python_startup_no_site     | 16.2 ms                                                     | 19.2 ms: 1.18x slower                                                          |
| typing_runtime_protocols   | 95.1 us                                                     | 113 us: 1.18x slower                                                           |
| coverage                   | 40.8 ms                                                     | 48.7 ms: 1.19x slower                                                          |
| telco                      | 4.13 ms                                                     | 4.93 ms: 1.19x slower                                                          |
| json_dumps                 | 5.70 ms                                                     | 6.97 ms: 1.22x slower                                                          |
| bench_mp_pool              | 69.2 ms                                                     | 86.4 ms: 1.25x slower                                                          |
| python_startup             | 19.5 ms                                                     | 25.2 ms: 1.29x slower                                                          |
| gc_traversal               | 1.52 ms                                                     | 2.01 ms: 1.32x slower                                                          |
| create_gc_cycles           | 752 us                                                      | 1.21 ms: 1.61x slower                                                          |
| Geometric mean             | (ref)                                                       | 1.03x faster                                                                   |

Benchmark hidden because not significant (2): json, bench_thread_pool
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20250228-3.14.0a5+-3e929d7/bm-20250228-pythonperf1-amd64-faster%2dcpython-use_stackrefs-3.14.0a5+-3e929d7.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.030x faster

# HPT report

- Reliability score: 83.58% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown