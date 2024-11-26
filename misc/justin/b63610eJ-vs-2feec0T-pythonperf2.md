Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231218-pythonperf2-x86_64-python-2feec0fc7fd0b9caae7a-3.13.0a2+-2feec0f | bm-20231219-pythonperf2-x86_64-brandtbucher-justin-3.13.0a2+-b63610e |
|----------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 310 ms                                                                       | 302 ms: 1.03x faster                                                 |
| chameleon      | 8.13 ms                                                                      | 7.78 ms: 1.04x faster                                                |
| docutils       | 2.95 sec                                                                     | 2.88 sec: 1.03x faster                                               |
| tornado_http   | 124 ms                                                                       | 121 ms: 1.03x faster                                                 |
| Geometric mean | (ref)                                                                        | 1.03x faster                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20231218-pythonperf2-x86_64-python-2feec0fc7fd0b9caae7a-3.13.0a2+-2feec0f | bm-20231219-pythonperf2-x86_64-brandtbucher-justin-3.13.0a2+-b63610e |
|---------------------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_io_tg          | 1.09 sec                                                                     | 1.09 sec: 1.00x slower                                               |
| async_tree_memoization_tg | 554 ms                                                                       | 570 ms: 1.03x slower                                                 |
| Geometric mean            | (ref)                                                                        | 1.00x slower                                                         |

Benchmark hidden because not significant (6): async_tree_none, async_tree_memoization, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_none_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231218-pythonperf2-x86_64-python-2feec0fc7fd0b9caae7a-3.13.0a2+-2feec0f | bm-20231219-pythonperf2-x86_64-brandtbucher-justin-3.13.0a2+-b63610e |
|----------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| float          | 105 ms                                                                       | 82.2 ms: 1.27x faster                                                |
| nbody          | 128 ms                                                                       | 108 ms: 1.19x faster                                                 |
| pidigits       | 265 ms                                                                       | 263 ms: 1.01x faster                                                 |
| Geometric mean | (ref)                                                                        | 1.15x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231218-pythonperf2-x86_64-python-2feec0fc7fd0b9caae7a-3.13.0a2+-2feec0f | bm-20231219-pythonperf2-x86_64-brandtbucher-justin-3.13.0a2+-b63610e |
|----------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 172 ms                                                                       | 150 ms: 1.15x faster                                                 |
| regex_effbot   | 3.80 ms                                                                      | 3.60 ms: 1.06x faster                                                |
| regex_dna      | 246 ms                                                                       | 244 ms: 1.01x faster                                                 |
| regex_v8       | 25.5 ms                                                                      | 25.3 ms: 1.01x faster                                                |
| Geometric mean | (ref)                                                                        | 1.05x faster                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231218-pythonperf2-x86_64-python-2feec0fc7fd0b9caae7a-3.13.0a2+-2feec0f | bm-20231219-pythonperf2-x86_64-brandtbucher-justin-3.13.0a2+-b63610e |
|----------------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| tomli_loads          | 2.80 sec                                                                     | 2.36 sec: 1.19x faster                                               |
| xml_etree_iterparse  | 118 ms                                                                       | 107 ms: 1.10x faster                                                 |
| pickle_list          | 4.44 us                                                                      | 4.23 us: 1.05x faster                                                |
| xml_etree_process    | 62.3 ms                                                                      | 59.5 ms: 1.05x faster                                                |
| xml_etree_generate   | 91.8 ms                                                                      | 88.0 ms: 1.04x faster                                                |
| unpickle_pure_python | 229 us                                                                       | 221 us: 1.04x faster                                                 |
| pickle               | 10.1 us                                                                      | 9.88 us: 1.03x faster                                                |
| unpickle             | 14.9 us                                                                      | 14.8 us: 1.01x faster                                                |
| xml_etree_parse      | 150 ms                                                                       | 148 ms: 1.01x faster                                                 |
| unpickle_list        | 4.66 us                                                                      | 4.71 us: 1.01x slower                                                |
| pickle_pure_python   | 309 us                                                                       | 313 us: 1.01x slower                                                 |
| pickle_dict          | 31.6 us                                                                      | 32.4 us: 1.02x slower                                                |
| Geometric mean       | (ref)                                                                        | 1.03x faster                                                         |

Benchmark hidden because not significant (2): json_loads, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231218-pythonperf2-x86_64-python-2feec0fc7fd0b9caae7a-3.13.0a2+-2feec0f | bm-20231219-pythonperf2-x86_64-brandtbucher-justin-3.13.0a2+-b63610e |
|------------------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup_no_site | 11.1 ms                                                                      | 11.1 ms: 1.01x slower                                                |
| Geometric mean         | (ref)                                                                        | 1.00x slower                                                         |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20231218-pythonperf2-x86_64-python-2feec0fc7fd0b9caae7a-3.13.0a2+-2feec0f | bm-20231219-pythonperf2-x86_64-brandtbucher-justin-3.13.0a2+-b63610e |
|-----------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako      | 14.9 ms                                                                      | 12.0 ms: 1.24x faster                                                |

All benchmarks:
===============

| Benchmark                 | bm-20231218-pythonperf2-x86_64-python-2feec0fc7fd0b9caae7a-3.13.0a2+-2feec0f | bm-20231219-pythonperf2-x86_64-brandtbucher-justin-3.13.0a2+-b63610e |
|---------------------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| deltablue                 | 5.49 ms                                                                      | 4.06 ms: 1.35x faster                                                |
| spectral_norm             | 161 ms                                                                       | 121 ms: 1.33x faster                                                 |
| scimark_sparse_mat_mult   | 6.68 ms                                                                      | 5.11 ms: 1.31x faster                                                |
| float                     | 105 ms                                                                       | 82.2 ms: 1.27x faster                                                |
| mako                      | 14.9 ms                                                                      | 12.0 ms: 1.24x faster                                                |
| hexiom                    | 9.75 ms                                                                      | 7.96 ms: 1.22x faster                                                |
| nbody                     | 128 ms                                                                       | 108 ms: 1.19x faster                                                 |
| tomli_loads               | 2.80 sec                                                                     | 2.36 sec: 1.19x faster                                               |
| comprehensions            | 24.9 us                                                                      | 21.0 us: 1.18x faster                                                |
| scimark_fft               | 429 ms                                                                       | 371 ms: 1.16x faster                                                 |
| regex_compile             | 172 ms                                                                       | 150 ms: 1.15x faster                                                 |
| pyflate                   | 572 ms                                                                       | 517 ms: 1.11x faster                                                 |
| scimark_monte_carlo       | 86.8 ms                                                                      | 79.1 ms: 1.10x faster                                                |
| xml_etree_iterparse       | 118 ms                                                                       | 107 ms: 1.10x faster                                                 |
| raytrace                  | 299 ms                                                                       | 277 ms: 1.08x faster                                                 |
| nqueens                   | 110 ms                                                                       | 102 ms: 1.08x faster                                                 |
| chaos                     | 76.2 ms                                                                      | 71.2 ms: 1.07x faster                                                |
| sympy_str                 | 325 ms                                                                       | 304 ms: 1.07x faster                                                 |
| fannkuch                  | 468 ms                                                                       | 439 ms: 1.07x faster                                                 |
| dulwich_log               | 72.5 ms                                                                      | 68.2 ms: 1.06x faster                                                |
| pprint_pformat            | 1.88 sec                                                                     | 1.77 sec: 1.06x faster                                               |
| sympy_expand              | 540 ms                                                                       | 509 ms: 1.06x faster                                                 |
| richards                  | 54.8 ms                                                                      | 51.7 ms: 1.06x faster                                                |
| deepcopy_memo             | 39.6 us                                                                      | 37.4 us: 1.06x faster                                                |
| pycparser                 | 1.36 sec                                                                     | 1.28 sec: 1.06x faster                                               |
| pprint_safe_repr          | 911 ms                                                                       | 861 ms: 1.06x faster                                                 |
| regex_effbot              | 3.80 ms                                                                      | 3.60 ms: 1.06x faster                                                |
| typing_runtime_protocols  | 127 us                                                                       | 120 us: 1.05x faster                                                 |
| sympy_sum                 | 169 ms                                                                       | 161 ms: 1.05x faster                                                 |
| go                        | 183 ms                                                                       | 174 ms: 1.05x faster                                                 |
| meteor_contest            | 139 ms                                                                       | 133 ms: 1.05x faster                                                 |
| pickle_list               | 4.44 us                                                                      | 4.23 us: 1.05x faster                                                |
| xml_etree_process         | 62.3 ms                                                                      | 59.5 ms: 1.05x faster                                                |
| scimark_lu                | 107 ms                                                                       | 103 ms: 1.05x faster                                                 |
| richards_super            | 60.3 ms                                                                      | 57.8 ms: 1.04x faster                                                |
| chameleon                 | 8.13 ms                                                                      | 7.78 ms: 1.04x faster                                                |
| xml_etree_generate        | 91.8 ms                                                                      | 88.0 ms: 1.04x faster                                                |
| logging_format            | 7.52 us                                                                      | 7.24 us: 1.04x faster                                                |
| unpickle_pure_python      | 229 us                                                                       | 221 us: 1.04x faster                                                 |
| logging_simple            | 6.83 us                                                                      | 6.61 us: 1.03x faster                                                |
| sympy_integrate           | 25.2 ms                                                                      | 24.4 ms: 1.03x faster                                                |
| create_gc_cycles          | 1.61 ms                                                                      | 1.56 ms: 1.03x faster                                                |
| telco                     | 8.48 ms                                                                      | 8.25 ms: 1.03x faster                                                |
| sqlglot_optimize          | 63.6 ms                                                                      | 62.0 ms: 1.03x faster                                                |
| sqlglot_normalize         | 123 ms                                                                       | 120 ms: 1.03x faster                                                 |
| docutils                  | 2.95 sec                                                                     | 2.88 sec: 1.03x faster                                               |
| tornado_http              | 124 ms                                                                       | 121 ms: 1.03x faster                                                 |
| pickle                    | 10.1 us                                                                      | 9.88 us: 1.03x faster                                                |
| sqlglot_parse             | 1.44 ms                                                                      | 1.41 ms: 1.03x faster                                                |
| 2to3                      | 310 ms                                                                       | 302 ms: 1.03x faster                                                 |
| mdp                       | 2.67 sec                                                                     | 2.62 sec: 1.02x faster                                               |
| crypto_pyaes              | 85.1 ms                                                                      | 83.6 ms: 1.02x faster                                                |
| sqlglot_transpile         | 1.86 ms                                                                      | 1.82 ms: 1.02x faster                                                |
| pathlib                   | 19.5 ms                                                                      | 19.2 ms: 1.02x faster                                                |
| coverage                  | 84.5 ms                                                                      | 83.1 ms: 1.02x faster                                                |
| deepcopy                  | 377 us                                                                       | 371 us: 1.01x faster                                                 |
| asyncio_tcp               | 374 ms                                                                       | 369 ms: 1.01x faster                                                 |
| pidigits                  | 265 ms                                                                       | 263 ms: 1.01x faster                                                 |
| unpickle                  | 14.9 us                                                                      | 14.8 us: 1.01x faster                                                |
| xml_etree_parse           | 150 ms                                                                       | 148 ms: 1.01x faster                                                 |
| regex_dna                 | 246 ms                                                                       | 244 ms: 1.01x faster                                                 |
| deepcopy_reduce           | 3.40 us                                                                      | 3.37 us: 1.01x faster                                                |
| regex_v8                  | 25.5 ms                                                                      | 25.3 ms: 1.01x faster                                                |
| asyncio_tcp_ssl           | 1.59 sec                                                                     | 1.58 sec: 1.01x faster                                               |
| async_tree_io_tg          | 1.09 sec                                                                     | 1.09 sec: 1.00x slower                                               |
| python_startup_no_site    | 11.1 ms                                                                      | 11.1 ms: 1.01x slower                                                |
| coroutines                | 22.4 ms                                                                      | 22.5 ms: 1.01x slower                                                |
| scimark_sor               | 142 ms                                                                       | 144 ms: 1.01x slower                                                 |
| unpack_sequence           | 43.5 ns                                                                      | 44.0 ns: 1.01x slower                                                |
| unpickle_list             | 4.66 us                                                                      | 4.71 us: 1.01x slower                                                |
| json                      | 5.19 ms                                                                      | 5.25 ms: 1.01x slower                                                |
| pickle_pure_python        | 309 us                                                                       | 313 us: 1.01x slower                                                 |
| generators                | 34.4 ms                                                                      | 34.9 ms: 1.02x slower                                                |
| pickle_dict               | 31.6 us                                                                      | 32.4 us: 1.02x slower                                                |
| async_tree_memoization_tg | 554 ms                                                                       | 570 ms: 1.03x slower                                                 |
| bench_mp_pool             | 4.68 ms                                                                      | 4.90 ms: 1.05x slower                                                |
| gc_traversal              | 3.69 ms                                                                      | 4.10 ms: 1.11x slower                                                |
| Geometric mean            | (ref)                                                                        | 1.05x faster                                                         |

Benchmark hidden because not significant (16): sqlite_synth, dask, async_tree_none, bench_thread_pool, asyncio_websockets, mypy2, async_tree_memoization, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, json_loads, async_generators, async_tree_none_tg, json_dumps, python_startup, async_tree_io, logging_silent


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x
