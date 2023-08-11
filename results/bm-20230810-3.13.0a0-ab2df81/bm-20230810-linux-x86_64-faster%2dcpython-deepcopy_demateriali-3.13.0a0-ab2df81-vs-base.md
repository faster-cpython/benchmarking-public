
# Results vs. base

- fork: faster-cpython
- ref: deepcopy_demateriali
- machine: linux-x86_64
- commit hash: ab2df81
- commit date: 2023-08-10
- overall geometric mean: 1.00x slower

Benchmarks with tag 'apps':
===========================

Benchmark hidden because not significant (2): docutils, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230811-linux-x86_64-python-666b68e8f252e3c6238d-3.13.0a0-666b68e | bm-20230810-linux-x86_64-faster%2dcpython-deepcopy_demateriali-3.13.0a0-ab2df81 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 91.7 ms                                                               | 89.0 ms: 1.03x faster                                                           |
| pidigits       | 189 ms                                                                | 201 ms: 1.06x slower                                                            |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                                    |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230811-linux-x86_64-python-666b68e8f252e3c6238d-3.13.0a0-666b68e | bm-20230810-linux-x86_64-faster%2dcpython-deepcopy_demateriali-3.13.0a0-ab2df81 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 136 ms                                                                | 137 ms: 1.01x slower                                                            |
| regex_effbot   | 3.43 ms                                                               | 3.55 ms: 1.04x slower                                                           |
| regex_v8       | 21.8 ms                                                               | 23.3 ms: 1.07x slower                                                           |
| regex_dna      | 197 ms                                                                | 214 ms: 1.08x slower                                                            |
| Geometric mean | (ref)                                                                 | 1.05x slower                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230811-linux-x86_64-python-666b68e8f252e3c6238d-3.13.0a0-666b68e | bm-20230810-linux-x86_64-faster%2dcpython-deepcopy_demateriali-3.13.0a0-ab2df81 |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pickle_dict          | 32.9 us                                                               | 30.6 us: 1.08x faster                                                           |
| pickle_list          | 4.77 us                                                               | 4.53 us: 1.05x faster                                                           |
| pickle               | 10.7 us                                                               | 10.3 us: 1.03x faster                                                           |
| xml_etree_generate   | 83.2 ms                                                               | 83.4 ms: 1.00x slower                                                           |
| json_loads           | 25.3 us                                                               | 25.5 us: 1.01x slower                                                           |
| unpickle_pure_python | 213 us                                                                | 215 us: 1.01x slower                                                            |
| pickle_pure_python   | 300 us                                                                | 303 us: 1.01x slower                                                            |
| unpickle_list        | 4.95 us                                                               | 5.09 us: 1.03x slower                                                           |
| Geometric mean       | (ref)                                                                 | 1.01x faster                                                                    |

Benchmark hidden because not significant (6): json_dumps, xml_etree_parse, tomli_loads, xml_etree_process, xml_etree_iterparse, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230811-linux-x86_64-python-666b68e8f252e3c6238d-3.13.0a0-666b68e | bm-20230810-linux-x86_64-faster%2dcpython-deepcopy_demateriali-3.13.0a0-ab2df81 |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 9.32 ms                                                               | 9.32 ms: 1.00x faster                                                           |
| python_startup_no_site | 6.82 ms                                                               | 6.82 ms: 1.00x slower                                                           |
| Geometric mean         | (ref)                                                                 | 1.00x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20230811-linux-x86_64-python-666b68e8f252e3c6238d-3.13.0a0-666b68e | bm-20230810-linux-x86_64-faster%2dcpython-deepcopy_demateriali-3.13.0a0-ab2df81 |
|-----------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako      | 10.7 ms                                                               | 10.8 ms: 1.01x slower                                                           |

All benchmarks:
===============

| Benchmark                | bm-20230811-linux-x86_64-python-666b68e8f252e3c6238d-3.13.0a0-666b68e | bm-20230810-linux-x86_64-faster%2dcpython-deepcopy_demateriali-3.13.0a0-ab2df81 |
|--------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| gc_traversal             | 4.30 ms                                                               | 3.67 ms: 1.17x faster                                                           |
| pickle_dict              | 32.9 us                                                               | 30.6 us: 1.08x faster                                                           |
| pickle_list              | 4.77 us                                                               | 4.53 us: 1.05x faster                                                           |
| pickle                   | 10.7 us                                                               | 10.3 us: 1.03x faster                                                           |
| nbody                    | 91.7 ms                                                               | 89.0 ms: 1.03x faster                                                           |
| nqueens                  | 81.0 ms                                                               | 79.7 ms: 1.02x faster                                                           |
| fannkuch                 | 389 ms                                                                | 383 ms: 1.01x faster                                                            |
| sqlite_synth             | 2.75 us                                                               | 2.72 us: 1.01x faster                                                           |
| sqlglot_normalize        | 106 ms                                                                | 105 ms: 1.01x faster                                                            |
| pathlib                  | 18.6 ms                                                               | 18.4 ms: 1.01x faster                                                           |
| go                       | 141 ms                                                                | 139 ms: 1.01x faster                                                            |
| chaos                    | 60.6 ms                                                               | 60.0 ms: 1.01x faster                                                           |
| logging_simple           | 5.86 us                                                               | 5.81 us: 1.01x faster                                                           |
| sqlglot_optimize         | 53.2 ms                                                               | 53.0 ms: 1.00x faster                                                           |
| pprint_pformat           | 1.49 sec                                                              | 1.48 sec: 1.00x faster                                                          |
| hexiom                   | 6.11 ms                                                               | 6.09 ms: 1.00x faster                                                           |
| python_startup           | 9.32 ms                                                               | 9.32 ms: 1.00x faster                                                           |
| python_startup_no_site   | 6.82 ms                                                               | 6.82 ms: 1.00x slower                                                           |
| asyncio_tcp_ssl          | 1.78 sec                                                              | 1.79 sec: 1.00x slower                                                          |
| xml_etree_generate       | 83.2 ms                                                               | 83.4 ms: 1.00x slower                                                           |
| regex_compile            | 136 ms                                                                | 137 ms: 1.01x slower                                                            |
| deepcopy_reduce          | 3.13 us                                                               | 3.15 us: 1.01x slower                                                           |
| scimark_monte_carlo      | 66.9 ms                                                               | 67.3 ms: 1.01x slower                                                           |
| typing_runtime_protocols | 147 us                                                                | 148 us: 1.01x slower                                                            |
| json_loads               | 25.3 us                                                               | 25.5 us: 1.01x slower                                                           |
| scimark_fft              | 355 ms                                                                | 358 ms: 1.01x slower                                                            |
| asyncio_tcp              | 481 ms                                                                | 485 ms: 1.01x slower                                                            |
| unpickle_pure_python     | 213 us                                                                | 215 us: 1.01x slower                                                            |
| mako                     | 10.7 ms                                                               | 10.8 ms: 1.01x slower                                                           |
| deepcopy                 | 350 us                                                                | 354 us: 1.01x slower                                                            |
| pickle_pure_python       | 300 us                                                                | 303 us: 1.01x slower                                                            |
| deepcopy_memo            | 37.1 us                                                               | 37.6 us: 1.01x slower                                                           |
| async_tree_io            | 1.18 sec                                                              | 1.20 sec: 1.01x slower                                                          |
| coroutines               | 21.6 ms                                                               | 21.9 ms: 1.01x slower                                                           |
| logging_silent           | 101 ns                                                                | 103 ns: 1.02x slower                                                            |
| scimark_sor              | 123 ms                                                                | 125 ms: 1.02x slower                                                            |
| coverage                 | 84.4 ms                                                               | 85.8 ms: 1.02x slower                                                           |
| spectral_norm            | 106 ms                                                                | 108 ms: 1.02x slower                                                            |
| scimark_lu               | 111 ms                                                                | 113 ms: 1.02x slower                                                            |
| unpack_sequence          | 46.4 ns                                                               | 47.3 ns: 1.02x slower                                                           |
| unpickle_list            | 4.95 us                                                               | 5.09 us: 1.03x slower                                                           |
| generators               | 28.4 ms                                                               | 29.3 ms: 1.03x slower                                                           |
| scimark_sparse_mat_mult  | 4.62 ms                                                               | 4.78 ms: 1.04x slower                                                           |
| deltablue                | 3.32 ms                                                               | 3.44 ms: 1.04x slower                                                           |
| regex_effbot             | 3.43 ms                                                               | 3.55 ms: 1.04x slower                                                           |
| mdp                      | 2.54 sec                                                              | 2.65 sec: 1.05x slower                                                          |
| pidigits                 | 189 ms                                                                | 201 ms: 1.06x slower                                                            |
| regex_v8                 | 21.8 ms                                                               | 23.3 ms: 1.07x slower                                                           |
| regex_dna                | 197 ms                                                                | 214 ms: 1.08x slower                                                            |
| Geometric mean           | (ref)                                                                 | 1.00x slower                                                                    |

Benchmark hidden because not significant (33): logging_format, json_dumps, meteor_contest, dulwich_log, xml_etree_parse, richards_super, create_gc_cycles, tomli_loads, float, comprehensions, xml_etree_process, raytrace, tornado_http, dask, xml_etree_iterparse, sqlglot_parse, docutils, bench_mp_pool, telco, pyflate, bench_thread_pool, pprint_safe_repr, async_tree_cpu_io_mixed, richards, crypto_pyaes, sqlglot_transpile, unpickle, json, async_tree_none, pycparser, mypy2, async_generators, async_tree_memoization
