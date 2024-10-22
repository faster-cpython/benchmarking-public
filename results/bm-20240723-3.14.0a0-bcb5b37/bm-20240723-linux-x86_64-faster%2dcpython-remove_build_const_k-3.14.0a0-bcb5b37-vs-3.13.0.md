# Results vs. 3.13.0

- fork: faster-cpython
- ref: remove_build_const_k
- machine: linux-x86_64
- commit hash: bcb5b37
- commit date: 2024-07-23
- overall geometric mean: 1.03x faster
- HPT reliability: 99.97%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240723-linux-x86_64-faster%2dcpython-remove_build_const_k-3.14.0a0-bcb5b37 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 260 ms: 1.02x faster                                                            |
| docutils       | 2.58 sec                                               | 2.70 sec: 1.04x slower                                                          |
| html5lib       | 64.5 ms                                                | 63.5 ms: 1.02x faster                                                           |
| tornado_http   | 91.5 ms                                                | 89.7 ms: 1.02x faster                                                           |
| Geometric mean | (ref)                                                  | 1.00x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240723-linux-x86_64-faster%2dcpython-remove_build_const_k-3.14.0a0-bcb5b37 |
|---------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg | 465 ms                                                 | 373 ms: 1.25x faster                                                            |
| async_tree_none_tg        | 320 ms                                                 | 291 ms: 1.10x faster                                                            |
| async_tree_none           | 354 ms                                                 | 323 ms: 1.09x faster                                                            |
| async_tree_memoization    | 442 ms                                                 | 406 ms: 1.09x faster                                                            |
| async_generators          | 433 ms                                                 | 427 ms: 1.01x faster                                                            |
| coroutines                | 22.5 ms                                                | 22.2 ms: 1.01x faster                                                           |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.78 sec: 1.00x faster                                                          |
| asyncio_tcp               | 488 ms                                                 | 490 ms: 1.00x slower                                                            |
| async_tree_io_tg          | 825 ms                                                 | 843 ms: 1.02x slower                                                            |
| Geometric mean            | (ref)                                                  | 1.04x faster                                                                    |

Benchmark hidden because not significant (4): async_tree_cpu_io_mixed, async_tree_io, async_tree_cpu_io_mixed_tg, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240723-linux-x86_64-faster%2dcpython-remove_build_const_k-3.14.0a0-bcb5b37 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 77.3 ms: 1.02x faster                                                           |
| pidigits       | 186 ms                                                 | 188 ms: 1.01x slower                                                            |
| nbody          | 85.7 ms                                                | 86.5 ms: 1.01x slower                                                           |
| Geometric mean | (ref)                                                  | 1.00x slower                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240723-linux-x86_64-faster%2dcpython-remove_build_const_k-3.14.0a0-bcb5b37 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.69 ms: 1.05x faster                                                           |
| regex_compile  | 131 ms                                                 | 129 ms: 1.01x faster                                                            |
| regex_v8       | 25.3 ms                                                | 25.4 ms: 1.00x slower                                                           |
| regex_dna      | 220 ms                                                 | 225 ms: 1.02x slower                                                            |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240723-linux-x86_64-faster%2dcpython-remove_build_const_k-3.14.0a0-bcb5b37 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 2.11 sec                                               | 2.02 sec: 1.05x faster                                                          |
| xml_etree_process    | 60.4 ms                                                | 58.1 ms: 1.04x faster                                                           |
| xml_etree_generate   | 87.0 ms                                                | 84.5 ms: 1.03x faster                                                           |
| unpickle_pure_python | 213 us                                                 | 209 us: 1.02x faster                                                            |
| xml_etree_parse      | 156 ms                                                 | 153 ms: 1.02x faster                                                            |
| pickle_pure_python   | 300 us                                                 | 296 us: 1.01x faster                                                            |
| xml_etree_iterparse  | 102 ms                                                 | 104 ms: 1.02x slower                                                            |
| json_loads           | 27.0 us                                                | 28.1 us: 1.04x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                                    |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240723-linux-x86_64-faster%2dcpython-remove_build_const_k-3.14.0a0-bcb5b37 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.5 ms: 1.00x faster                                                           |
| python_startup_no_site | 6.99 ms                                                | 7.09 ms: 1.01x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240723-linux-x86_64-faster%2dcpython-remove_build_const_k-3.14.0a0-bcb5b37 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 10.8 ms: 1.03x faster                                                           |
| genshi_xml      | 50.3 ms                                                | 49.1 ms: 1.03x faster                                                           |
| django_template | 34.4 ms                                                | 33.6 ms: 1.03x faster                                                           |
| genshi_text     | 22.9 ms                                                | 22.5 ms: 1.02x faster                                                           |
| Geometric mean  | (ref)                                                  | 1.03x faster                                                                    |

All benchmarks:
===============

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240723-linux-x86_64-faster%2dcpython-remove_build_const_k-3.14.0a0-bcb5b37 |
|---------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| deepcopy                  | 352 us                                                 | 261 us: 1.35x faster                                                            |
| deepcopy_memo             | 38.0 us                                                | 29.0 us: 1.31x faster                                                           |
| async_tree_memoization_tg | 465 ms                                                 | 373 ms: 1.25x faster                                                            |
| deepcopy_reduce           | 3.17 us                                                | 2.65 us: 1.19x faster                                                           |
| scimark_sparse_mat_mult   | 5.03 ms                                                | 4.35 ms: 1.16x faster                                                           |
| spectral_norm             | 115 ms                                                 | 104 ms: 1.10x faster                                                            |
| async_tree_none_tg        | 320 ms                                                 | 291 ms: 1.10x faster                                                            |
| async_tree_none           | 354 ms                                                 | 323 ms: 1.09x faster                                                            |
| pathlib                   | 17.1 ms                                                | 15.6 ms: 1.09x faster                                                           |
| async_tree_memoization    | 442 ms                                                 | 406 ms: 1.09x faster                                                            |
| mdp                       | 2.74 sec                                               | 2.53 sec: 1.09x faster                                                          |
| gc_traversal              | 3.81 ms                                                | 3.54 ms: 1.07x faster                                                           |
| richards                  | 48.1 ms                                                | 45.6 ms: 1.06x faster                                                           |
| regex_effbot              | 3.88 ms                                                | 3.69 ms: 1.05x faster                                                           |
| richards_super            | 54.4 ms                                                | 51.7 ms: 1.05x faster                                                           |
| logging_simple            | 5.66 us                                                | 5.40 us: 1.05x faster                                                           |
| scimark_lu                | 115 ms                                                 | 110 ms: 1.05x faster                                                            |
| tomli_loads               | 2.11 sec                                               | 2.02 sec: 1.05x faster                                                          |
| generators                | 28.8 ms                                                | 27.7 ms: 1.04x faster                                                           |
| logging_silent            | 102 ns                                                 | 98.1 ns: 1.04x faster                                                           |
| xml_etree_process         | 60.4 ms                                                | 58.1 ms: 1.04x faster                                                           |
| bench_thread_pool         | 815 us                                                 | 785 us: 1.04x faster                                                            |
| logging_format            | 6.25 us                                                | 6.03 us: 1.04x faster                                                           |
| telco                     | 8.45 ms                                                | 8.15 ms: 1.04x faster                                                           |
| scimark_fft               | 369 ms                                                 | 356 ms: 1.04x faster                                                            |
| crypto_pyaes              | 73.0 ms                                                | 70.5 ms: 1.04x faster                                                           |
| raytrace                  | 262 ms                                                 | 253 ms: 1.03x faster                                                            |
| mako                      | 11.1 ms                                                | 10.8 ms: 1.03x faster                                                           |
| pprint_safe_repr          | 744 ms                                                 | 722 ms: 1.03x faster                                                            |
| xml_etree_generate        | 87.0 ms                                                | 84.5 ms: 1.03x faster                                                           |
| json                      | 5.20 ms                                                | 5.06 ms: 1.03x faster                                                           |
| genshi_xml                | 50.3 ms                                                | 49.1 ms: 1.03x faster                                                           |
| django_template           | 34.4 ms                                                | 33.6 ms: 1.03x faster                                                           |
| thrift                    | 796 us                                                 | 777 us: 1.02x faster                                                            |
| sqlglot_normalize         | 107 ms                                                 | 105 ms: 1.02x faster                                                            |
| sqlglot_optimize          | 53.9 ms                                                | 52.8 ms: 1.02x faster                                                           |
| tornado_http              | 91.5 ms                                                | 89.7 ms: 1.02x faster                                                           |
| unpickle_pure_python      | 213 us                                                 | 209 us: 1.02x faster                                                            |
| 2to3                      | 265 ms                                                 | 260 ms: 1.02x faster                                                            |
| pprint_pformat            | 1.51 sec                                               | 1.48 sec: 1.02x faster                                                          |
| genshi_text               | 22.9 ms                                                | 22.5 ms: 1.02x faster                                                           |
| go                        | 142 ms                                                 | 139 ms: 1.02x faster                                                            |
| pycparser                 | 1.19 sec                                               | 1.17 sec: 1.02x faster                                                          |
| xml_etree_parse           | 156 ms                                                 | 153 ms: 1.02x faster                                                            |
| html5lib                  | 64.5 ms                                                | 63.5 ms: 1.02x faster                                                           |
| float                     | 78.5 ms                                                | 77.3 ms: 1.02x faster                                                           |
| pickle_pure_python        | 300 us                                                 | 296 us: 1.01x faster                                                            |
| chaos                     | 58.4 ms                                                | 57.6 ms: 1.01x faster                                                           |
| regex_compile             | 131 ms                                                 | 129 ms: 1.01x faster                                                            |
| async_generators          | 433 ms                                                 | 427 ms: 1.01x faster                                                            |
| coroutines                | 22.5 ms                                                | 22.2 ms: 1.01x faster                                                           |
| hexiom                    | 6.13 ms                                                | 6.06 ms: 1.01x faster                                                           |
| scimark_sor               | 122 ms                                                 | 121 ms: 1.01x faster                                                            |
| sympy_integrate           | 19.9 ms                                                | 19.7 ms: 1.01x faster                                                           |
| sympy_expand              | 462 ms                                                 | 457 ms: 1.01x faster                                                            |
| sympy_str                 | 274 ms                                                 | 271 ms: 1.01x faster                                                            |
| sqlglot_parse             | 1.27 ms                                                | 1.25 ms: 1.01x faster                                                           |
| sqlglot_transpile         | 1.57 ms                                                | 1.56 ms: 1.01x faster                                                           |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.78 sec: 1.00x faster                                                          |
| meteor_contest            | 108 ms                                                 | 107 ms: 1.00x faster                                                            |
| python_startup            | 10.6 ms                                                | 10.5 ms: 1.00x faster                                                           |
| regex_v8                  | 25.3 ms                                                | 25.4 ms: 1.00x slower                                                           |
| asyncio_tcp               | 488 ms                                                 | 490 ms: 1.00x slower                                                            |
| deltablue                 | 3.15 ms                                                | 3.16 ms: 1.00x slower                                                           |
| comprehensions            | 16.4 us                                                | 16.5 us: 1.00x slower                                                           |
| scimark_monte_carlo       | 66.3 ms                                                | 66.6 ms: 1.01x slower                                                           |
| dulwich_log               | 63.0 ms                                                | 63.4 ms: 1.01x slower                                                           |
| pidigits                  | 186 ms                                                 | 188 ms: 1.01x slower                                                            |
| nbody                     | 85.7 ms                                                | 86.5 ms: 1.01x slower                                                           |
| python_startup_no_site    | 6.99 ms                                                | 7.09 ms: 1.01x slower                                                           |
| xml_etree_iterparse       | 102 ms                                                 | 104 ms: 1.02x slower                                                            |
| bpe_tokeniser             | 4.69 sec                                               | 4.79 sec: 1.02x slower                                                          |
| async_tree_io_tg          | 825 ms                                                 | 843 ms: 1.02x slower                                                            |
| regex_dna                 | 220 ms                                                 | 225 ms: 1.02x slower                                                            |
| typing_runtime_protocols  | 159 us                                                 | 164 us: 1.03x slower                                                            |
| fannkuch                  | 381 ms                                                 | 395 ms: 1.04x slower                                                            |
| json_loads                | 27.0 us                                                | 28.1 us: 1.04x slower                                                           |
| dask                      | 338 ms                                                 | 352 ms: 1.04x slower                                                            |
| docutils                  | 2.58 sec                                               | 2.70 sec: 1.04x slower                                                          |
| pyflate                   | 460 ms                                                 | 482 ms: 1.05x slower                                                            |
| create_gc_cycles          | 1.61 ms                                                | 1.73 ms: 1.07x slower                                                           |
| coverage                  | 83.7 ms                                                | 90.9 ms: 1.09x slower                                                           |
| Geometric mean            | (ref)                                                  | 1.03x faster                                                                    |

Benchmark hidden because not significant (9): pylint, async_tree_cpu_io_mixed, async_tree_io, async_tree_cpu_io_mixed_tg, json_dumps, nqueens, bench_mp_pool, sympy_sum, asyncio_websockets
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 99.97% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x