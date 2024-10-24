# Results vs. 3.13.0

- fork: faster-cpython
- ref: bound_method_instrum
- machine: linux-x86_64
- commit hash: 5787d3e
- commit date: 2024-07-23
- overall geometric mean: 1.02x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240723-linux-x86_64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 261 ms: 1.02x faster                                                            |
| docutils       | 2.58 sec                                               | 2.70 sec: 1.05x slower                                                          |
| tornado_http   | 91.5 ms                                                | 89.5 ms: 1.02x faster                                                           |
| Geometric mean | (ref)                                                  | 1.00x slower                                                                    |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240723-linux-x86_64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|---------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg | 465 ms                                                 | 376 ms: 1.23x faster                                                            |
| async_tree_none_tg        | 320 ms                                                 | 294 ms: 1.09x faster                                                            |
| async_tree_none           | 354 ms                                                 | 326 ms: 1.09x faster                                                            |
| async_tree_memoization    | 442 ms                                                 | 409 ms: 1.08x faster                                                            |
| async_generators          | 433 ms                                                 | 429 ms: 1.01x faster                                                            |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.78 sec: 1.00x faster                                                          |
| asyncio_tcp               | 488 ms                                                 | 491 ms: 1.01x slower                                                            |
| async_tree_io_tg          | 825 ms                                                 | 850 ms: 1.03x slower                                                            |
| Geometric mean            | (ref)                                                  | 1.04x faster                                                                    |

Benchmark hidden because not significant (5): async_tree_cpu_io_mixed, coroutines, async_tree_cpu_io_mixed_tg, asyncio_websockets, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240723-linux-x86_64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 76.4 ms: 1.03x faster                                                           |
| nbody          | 85.7 ms                                                | 85.2 ms: 1.01x faster                                                           |
| pidigits       | 186 ms                                                 | 187 ms: 1.00x slower                                                            |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240723-linux-x86_64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.64 ms: 1.07x faster                                                           |
| regex_compile  | 131 ms                                                 | 129 ms: 1.01x faster                                                            |
| regex_dna      | 220 ms                                                 | 220 ms: 1.00x slower                                                            |
| regex_v8       | 25.3 ms                                                | 25.4 ms: 1.01x slower                                                           |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240723-linux-x86_64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 2.11 sec                                               | 2.04 sec: 1.04x faster                                                          |
| xml_etree_process    | 60.4 ms                                                | 58.3 ms: 1.04x faster                                                           |
| xml_etree_generate   | 87.0 ms                                                | 84.6 ms: 1.03x faster                                                           |
| pickle_pure_python   | 300 us                                                 | 295 us: 1.02x faster                                                            |
| unpickle_pure_python | 213 us                                                 | 210 us: 1.02x faster                                                            |
| json_loads           | 27.0 us                                                | 27.5 us: 1.02x slower                                                           |
| xml_etree_iterparse  | 102 ms                                                 | 105 ms: 1.02x slower                                                            |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                                    |

Benchmark hidden because not significant (2): json_dumps, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240723-linux-x86_64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.5 ms: 1.00x faster                                                           |
| python_startup_no_site | 6.99 ms                                                | 7.07 ms: 1.01x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.00x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240723-linux-x86_64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_xml      | 50.3 ms                                                | 48.6 ms: 1.04x faster                                                           |
| genshi_text     | 22.9 ms                                                | 22.1 ms: 1.03x faster                                                           |
| mako            | 11.1 ms                                                | 10.7 ms: 1.03x faster                                                           |
| django_template | 34.4 ms                                                | 33.7 ms: 1.02x faster                                                           |
| Geometric mean  | (ref)                                                  | 1.03x faster                                                                    |

All benchmarks:
===============

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240723-linux-x86_64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|---------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| deepcopy                  | 352 us                                                 | 258 us: 1.37x faster                                                            |
| deepcopy_memo             | 38.0 us                                                | 28.6 us: 1.33x faster                                                           |
| async_tree_memoization_tg | 465 ms                                                 | 376 ms: 1.23x faster                                                            |
| deepcopy_reduce           | 3.17 us                                                | 2.64 us: 1.20x faster                                                           |
| pathlib                   | 17.1 ms                                                | 15.6 ms: 1.09x faster                                                           |
| async_tree_none_tg        | 320 ms                                                 | 294 ms: 1.09x faster                                                            |
| async_tree_none           | 354 ms                                                 | 326 ms: 1.09x faster                                                            |
| async_tree_memoization    | 442 ms                                                 | 409 ms: 1.08x faster                                                            |
| scimark_sparse_mat_mult   | 5.03 ms                                                | 4.66 ms: 1.08x faster                                                           |
| regex_effbot              | 3.88 ms                                                | 3.64 ms: 1.07x faster                                                           |
| logging_silent            | 102 ns                                                 | 95.7 ns: 1.07x faster                                                           |
| mdp                       | 2.74 sec                                               | 2.57 sec: 1.07x faster                                                          |
| telco                     | 8.45 ms                                                | 7.95 ms: 1.06x faster                                                           |
| richards_super            | 54.4 ms                                                | 51.2 ms: 1.06x faster                                                           |
| richards                  | 48.1 ms                                                | 45.8 ms: 1.05x faster                                                           |
| logging_format            | 6.25 us                                                | 5.96 us: 1.05x faster                                                           |
| bench_thread_pool         | 815 us                                                 | 784 us: 1.04x faster                                                            |
| logging_simple            | 5.66 us                                                | 5.46 us: 1.04x faster                                                           |
| tomli_loads               | 2.11 sec                                               | 2.04 sec: 1.04x faster                                                          |
| thrift                    | 796 us                                                 | 768 us: 1.04x faster                                                            |
| xml_etree_process         | 60.4 ms                                                | 58.3 ms: 1.04x faster                                                           |
| genshi_xml                | 50.3 ms                                                | 48.6 ms: 1.04x faster                                                           |
| genshi_text               | 22.9 ms                                                | 22.1 ms: 1.03x faster                                                           |
| generators                | 28.8 ms                                                | 27.9 ms: 1.03x faster                                                           |
| mako                      | 11.1 ms                                                | 10.7 ms: 1.03x faster                                                           |
| spectral_norm             | 115 ms                                                 | 111 ms: 1.03x faster                                                            |
| pprint_safe_repr          | 744 ms                                                 | 721 ms: 1.03x faster                                                            |
| xml_etree_generate        | 87.0 ms                                                | 84.6 ms: 1.03x faster                                                           |
| scimark_fft               | 369 ms                                                 | 359 ms: 1.03x faster                                                            |
| float                     | 78.5 ms                                                | 76.4 ms: 1.03x faster                                                           |
| pprint_pformat            | 1.51 sec                                               | 1.47 sec: 1.03x faster                                                          |
| hexiom                    | 6.13 ms                                                | 5.98 ms: 1.02x faster                                                           |
| tornado_http              | 91.5 ms                                                | 89.5 ms: 1.02x faster                                                           |
| django_template           | 34.4 ms                                                | 33.7 ms: 1.02x faster                                                           |
| raytrace                  | 262 ms                                                 | 256 ms: 1.02x faster                                                            |
| pickle_pure_python        | 300 us                                                 | 295 us: 1.02x faster                                                            |
| unpickle_pure_python      | 213 us                                                 | 210 us: 1.02x faster                                                            |
| sqlglot_optimize          | 53.9 ms                                                | 53.0 ms: 1.02x faster                                                           |
| nqueens                   | 80.6 ms                                                | 79.4 ms: 1.02x faster                                                           |
| scimark_sor               | 122 ms                                                 | 121 ms: 1.02x faster                                                            |
| sympy_str                 | 274 ms                                                 | 269 ms: 1.02x faster                                                            |
| 2to3                      | 265 ms                                                 | 261 ms: 1.02x faster                                                            |
| regex_compile             | 131 ms                                                 | 129 ms: 1.01x faster                                                            |
| pycparser                 | 1.19 sec                                               | 1.18 sec: 1.01x faster                                                          |
| meteor_contest            | 108 ms                                                 | 106 ms: 1.01x faster                                                            |
| go                        | 142 ms                                                 | 140 ms: 1.01x faster                                                            |
| sympy_integrate           | 19.9 ms                                                | 19.6 ms: 1.01x faster                                                           |
| sympy_expand              | 462 ms                                                 | 456 ms: 1.01x faster                                                            |
| json                      | 5.20 ms                                                | 5.13 ms: 1.01x faster                                                           |
| scimark_lu                | 115 ms                                                 | 114 ms: 1.01x faster                                                            |
| deltablue                 | 3.15 ms                                                | 3.11 ms: 1.01x faster                                                           |
| crypto_pyaes              | 73.0 ms                                                | 72.2 ms: 1.01x faster                                                           |
| sqlglot_normalize         | 107 ms                                                 | 106 ms: 1.01x faster                                                            |
| async_generators          | 433 ms                                                 | 429 ms: 1.01x faster                                                            |
| gc_traversal              | 3.81 ms                                                | 3.78 ms: 1.01x faster                                                           |
| nbody                     | 85.7 ms                                                | 85.2 ms: 1.01x faster                                                           |
| python_startup            | 10.6 ms                                                | 10.5 ms: 1.00x faster                                                           |
| sqlglot_transpile         | 1.57 ms                                                | 1.57 ms: 1.00x faster                                                           |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.78 sec: 1.00x faster                                                          |
| pyflate                   | 460 ms                                                 | 458 ms: 1.00x faster                                                            |
| comprehensions            | 16.4 us                                                | 16.4 us: 1.00x slower                                                           |
| regex_dna                 | 220 ms                                                 | 220 ms: 1.00x slower                                                            |
| chaos                     | 58.4 ms                                                | 58.6 ms: 1.00x slower                                                           |
| pidigits                  | 186 ms                                                 | 187 ms: 1.00x slower                                                            |
| asyncio_tcp               | 488 ms                                                 | 491 ms: 1.01x slower                                                            |
| regex_v8                  | 25.3 ms                                                | 25.4 ms: 1.01x slower                                                           |
| dulwich_log               | 63.0 ms                                                | 63.5 ms: 1.01x slower                                                           |
| typing_runtime_protocols  | 159 us                                                 | 161 us: 1.01x slower                                                            |
| python_startup_no_site    | 6.99 ms                                                | 7.07 ms: 1.01x slower                                                           |
| json_loads                | 27.0 us                                                | 27.5 us: 1.02x slower                                                           |
| bpe_tokeniser             | 4.69 sec                                               | 4.80 sec: 1.02x slower                                                          |
| xml_etree_iterparse       | 102 ms                                                 | 105 ms: 1.02x slower                                                            |
| async_tree_io_tg          | 825 ms                                                 | 850 ms: 1.03x slower                                                            |
| scimark_monte_carlo       | 66.3 ms                                                | 68.3 ms: 1.03x slower                                                           |
| docutils                  | 2.58 sec                                               | 2.70 sec: 1.05x slower                                                          |
| dask                      | 338 ms                                                 | 356 ms: 1.05x slower                                                            |
| fannkuch                  | 381 ms                                                 | 407 ms: 1.07x slower                                                            |
| coverage                  | 83.7 ms                                                | 90.5 ms: 1.08x slower                                                           |
| create_gc_cycles          | 1.61 ms                                                | 1.74 ms: 1.08x slower                                                           |
| Geometric mean            | (ref)                                                  | 1.02x faster                                                                    |

Benchmark hidden because not significant (12): async_tree_cpu_io_mixed, coroutines, async_tree_cpu_io_mixed_tg, json_dumps, html5lib, bench_mp_pool, sqlglot_parse, sympy_sum, xml_etree_parse, asyncio_websockets, async_tree_io, pylint
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x