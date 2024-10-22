# Results vs. 3.13.0

- fork: faster-cpython
- ref: specialize_shadowed_
- machine: linux-x86_64
- commit hash: 975089f
- commit date: 2024-08-21
- overall geometric mean: 1.01x faster
- HPT reliability: 95.98%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240821-linux-x86_64-faster%2dcpython-specialize_shadowed_-3.14.0a0-975089f |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 255 ms: 1.04x faster                                                            |
| docutils       | 2.58 sec                                               | 2.70 sec: 1.04x slower                                                          |
| html5lib       | 64.5 ms                                                | 66.2 ms: 1.03x slower                                                           |
| tornado_http   | 91.5 ms                                                | 90.1 ms: 1.02x faster                                                           |
| Geometric mean | (ref)                                                  | 1.00x slower                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240821-linux-x86_64-faster%2dcpython-specialize_shadowed_-3.14.0a0-975089f |
|---------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg | 465 ms                                                 | 403 ms: 1.15x faster                                                            |
| async_tree_memoization    | 442 ms                                                 | 392 ms: 1.13x faster                                                            |
| async_tree_none           | 354 ms                                                 | 324 ms: 1.09x faster                                                            |
| async_tree_none_tg        | 320 ms                                                 | 311 ms: 1.03x faster                                                            |
| async_tree_cpu_io_mixed   | 574 ms                                                 | 558 ms: 1.03x faster                                                            |
| asyncio_tcp               | 488 ms                                                 | 477 ms: 1.02x faster                                                            |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.79 sec: 1.00x faster                                                          |
| asyncio_websockets        | 555 ms                                                 | 558 ms: 1.00x slower                                                            |
| async_generators          | 433 ms                                                 | 435 ms: 1.00x slower                                                            |
| coroutines                | 22.5 ms                                                | 23.3 ms: 1.03x slower                                                           |
| async_tree_io_tg          | 825 ms                                                 | 895 ms: 1.08x slower                                                            |
| async_tree_io             | 843 ms                                                 | 927 ms: 1.10x slower                                                            |
| Geometric mean            | (ref)                                                  | 1.02x faster                                                                    |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240821-linux-x86_64-faster%2dcpython-specialize_shadowed_-3.14.0a0-975089f |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 77.7 ms: 1.01x faster                                                           |
| pidigits       | 186 ms                                                 | 187 ms: 1.00x slower                                                            |
| nbody          | 85.7 ms                                                | 86.8 ms: 1.01x slower                                                           |
| Geometric mean | (ref)                                                  | 1.00x slower                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240821-linux-x86_64-faster%2dcpython-specialize_shadowed_-3.14.0a0-975089f |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_v8       | 25.3 ms                                                | 23.7 ms: 1.07x faster                                                           |
| regex_effbot   | 3.88 ms                                                | 3.69 ms: 1.05x faster                                                           |
| regex_compile  | 131 ms                                                 | 128 ms: 1.03x faster                                                            |
| regex_dna      | 220 ms                                                 | 225 ms: 1.03x slower                                                            |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240821-linux-x86_64-faster%2dcpython-specialize_shadowed_-3.14.0a0-975089f |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_generate   | 87.0 ms                                                | 84.4 ms: 1.03x faster                                                           |
| xml_etree_process    | 60.4 ms                                                | 58.6 ms: 1.03x faster                                                           |
| tomli_loads          | 2.11 sec                                               | 2.08 sec: 1.02x faster                                                          |
| unpickle_pure_python | 213 us                                                 | 211 us: 1.01x faster                                                            |
| pickle_pure_python   | 300 us                                                 | 302 us: 1.00x slower                                                            |
| xml_etree_iterparse  | 102 ms                                                 | 106 ms: 1.04x slower                                                            |
| json_loads           | 27.0 us                                                | 28.6 us: 1.06x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.00x slower                                                                    |

Benchmark hidden because not significant (2): xml_etree_parse, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240821-linux-x86_64-faster%2dcpython-specialize_shadowed_-3.14.0a0-975089f |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.5 ms: 1.01x faster                                                           |
| python_startup_no_site | 6.99 ms                                                | 7.05 ms: 1.01x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.00x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240821-linux-x86_64-faster%2dcpython-specialize_shadowed_-3.14.0a0-975089f |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| django_template | 34.4 ms                                                | 33.6 ms: 1.02x faster                                                           |
| genshi_text     | 22.9 ms                                                | 22.6 ms: 1.01x faster                                                           |
| mako            | 11.1 ms                                                | 11.4 ms: 1.03x slower                                                           |
| Geometric mean  | (ref)                                                  | 1.00x faster                                                                    |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240821-linux-x86_64-faster%2dcpython-specialize_shadowed_-3.14.0a0-975089f |
|---------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| deepcopy                  | 352 us                                                 | 260 us: 1.36x faster                                                            |
| deepcopy_memo             | 38.0 us                                                | 29.6 us: 1.29x faster                                                           |
| deepcopy_reduce           | 3.17 us                                                | 2.66 us: 1.19x faster                                                           |
| async_tree_memoization_tg | 465 ms                                                 | 403 ms: 1.15x faster                                                            |
| async_tree_memoization    | 442 ms                                                 | 392 ms: 1.13x faster                                                            |
| async_tree_none           | 354 ms                                                 | 324 ms: 1.09x faster                                                            |
| mdp                       | 2.74 sec                                               | 2.52 sec: 1.09x faster                                                          |
| pathlib                   | 17.1 ms                                                | 15.9 ms: 1.07x faster                                                           |
| regex_v8                  | 25.3 ms                                                | 23.7 ms: 1.07x faster                                                           |
| regex_effbot              | 3.88 ms                                                | 3.69 ms: 1.05x faster                                                           |
| scimark_sparse_mat_mult   | 5.03 ms                                                | 4.78 ms: 1.05x faster                                                           |
| richards_super            | 54.4 ms                                                | 52.0 ms: 1.05x faster                                                           |
| pycparser                 | 1.19 sec                                               | 1.14 sec: 1.04x faster                                                          |
| richards                  | 48.1 ms                                                | 46.1 ms: 1.04x faster                                                           |
| telco                     | 8.45 ms                                                | 8.12 ms: 1.04x faster                                                           |
| 2to3                      | 265 ms                                                 | 255 ms: 1.04x faster                                                            |
| bench_thread_pool         | 815 us                                                 | 783 us: 1.04x faster                                                            |
| thrift                    | 796 us                                                 | 766 us: 1.04x faster                                                            |
| pprint_safe_repr          | 744 ms                                                 | 717 ms: 1.04x faster                                                            |
| generators                | 28.8 ms                                                | 27.9 ms: 1.03x faster                                                           |
| pprint_pformat            | 1.51 sec                                               | 1.47 sec: 1.03x faster                                                          |
| xml_etree_generate        | 87.0 ms                                                | 84.4 ms: 1.03x faster                                                           |
| xml_etree_process         | 60.4 ms                                                | 58.6 ms: 1.03x faster                                                           |
| async_tree_none_tg        | 320 ms                                                 | 311 ms: 1.03x faster                                                            |
| async_tree_cpu_io_mixed   | 574 ms                                                 | 558 ms: 1.03x faster                                                            |
| logging_silent            | 102 ns                                                 | 99.3 ns: 1.03x faster                                                           |
| regex_compile             | 131 ms                                                 | 128 ms: 1.03x faster                                                            |
| sympy_integrate           | 19.9 ms                                                | 19.4 ms: 1.03x faster                                                           |
| scimark_lu                | 115 ms                                                 | 112 ms: 1.02x faster                                                            |
| asyncio_tcp               | 488 ms                                                 | 477 ms: 1.02x faster                                                            |
| django_template           | 34.4 ms                                                | 33.6 ms: 1.02x faster                                                           |
| logging_format            | 6.25 us                                                | 6.12 us: 1.02x faster                                                           |
| sympy_str                 | 274 ms                                                 | 268 ms: 1.02x faster                                                            |
| spectral_norm             | 115 ms                                                 | 113 ms: 1.02x faster                                                            |
| logging_simple            | 5.66 us                                                | 5.54 us: 1.02x faster                                                           |
| sympy_sum                 | 150 ms                                                 | 147 ms: 1.02x faster                                                            |
| tomli_loads               | 2.11 sec                                               | 2.08 sec: 1.02x faster                                                          |
| tornado_http              | 91.5 ms                                                | 90.1 ms: 1.02x faster                                                           |
| genshi_text               | 22.9 ms                                                | 22.6 ms: 1.01x faster                                                           |
| sympy_expand              | 462 ms                                                 | 456 ms: 1.01x faster                                                            |
| unpickle_pure_python      | 213 us                                                 | 211 us: 1.01x faster                                                            |
| scimark_fft               | 369 ms                                                 | 364 ms: 1.01x faster                                                            |
| sqlglot_optimize          | 53.9 ms                                                | 53.3 ms: 1.01x faster                                                           |
| float                     | 78.5 ms                                                | 77.7 ms: 1.01x faster                                                           |
| python_startup            | 10.6 ms                                                | 10.5 ms: 1.01x faster                                                           |
| raytrace                  | 262 ms                                                 | 260 ms: 1.01x faster                                                            |
| crypto_pyaes              | 73.0 ms                                                | 72.6 ms: 1.01x faster                                                           |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.79 sec: 1.00x faster                                                          |
| sqlglot_transpile         | 1.57 ms                                                | 1.57 ms: 1.00x faster                                                           |
| pidigits                  | 186 ms                                                 | 187 ms: 1.00x slower                                                            |
| asyncio_websockets        | 555 ms                                                 | 558 ms: 1.00x slower                                                            |
| pickle_pure_python        | 300 us                                                 | 302 us: 1.00x slower                                                            |
| async_generators          | 433 ms                                                 | 435 ms: 1.00x slower                                                            |
| chaos                     | 58.4 ms                                                | 58.7 ms: 1.01x slower                                                           |
| nqueens                   | 80.6 ms                                                | 81.3 ms: 1.01x slower                                                           |
| python_startup_no_site    | 6.99 ms                                                | 7.05 ms: 1.01x slower                                                           |
| scimark_sor               | 122 ms                                                 | 124 ms: 1.01x slower                                                            |
| sqlglot_parse             | 1.27 ms                                                | 1.28 ms: 1.01x slower                                                           |
| nbody                     | 85.7 ms                                                | 86.8 ms: 1.01x slower                                                           |
| gc_traversal              | 3.81 ms                                                | 3.86 ms: 1.01x slower                                                           |
| comprehensions            | 16.4 us                                                | 16.6 us: 1.01x slower                                                           |
| hexiom                    | 6.13 ms                                                | 6.22 ms: 1.01x slower                                                           |
| deltablue                 | 3.15 ms                                                | 3.20 ms: 1.02x slower                                                           |
| coverage                  | 83.7 ms                                                | 85.3 ms: 1.02x slower                                                           |
| pyflate                   | 460 ms                                                 | 470 ms: 1.02x slower                                                            |
| scimark_monte_carlo       | 66.3 ms                                                | 67.8 ms: 1.02x slower                                                           |
| regex_dna                 | 220 ms                                                 | 225 ms: 1.03x slower                                                            |
| html5lib                  | 64.5 ms                                                | 66.2 ms: 1.03x slower                                                           |
| mako                      | 11.1 ms                                                | 11.4 ms: 1.03x slower                                                           |
| json                      | 5.20 ms                                                | 5.35 ms: 1.03x slower                                                           |
| bpe_tokeniser             | 4.69 sec                                               | 4.84 sec: 1.03x slower                                                          |
| coroutines                | 22.5 ms                                                | 23.3 ms: 1.03x slower                                                           |
| xml_etree_iterparse       | 102 ms                                                 | 106 ms: 1.04x slower                                                            |
| docutils                  | 2.58 sec                                               | 2.70 sec: 1.04x slower                                                          |
| json_loads                | 27.0 us                                                | 28.6 us: 1.06x slower                                                           |
| fannkuch                  | 381 ms                                                 | 404 ms: 1.06x slower                                                            |
| async_tree_io_tg          | 825 ms                                                 | 895 ms: 1.08x slower                                                            |
| create_gc_cycles          | 1.61 ms                                                | 1.76 ms: 1.09x slower                                                           |
| async_tree_io             | 843 ms                                                 | 927 ms: 1.10x slower                                                            |
| go                        | 142 ms                                                 | 161 ms: 1.14x slower                                                            |
| Geometric mean            | (ref)                                                  | 1.01x faster                                                                    |

Benchmark hidden because not significant (9): async_tree_cpu_io_mixed_tg, typing_runtime_protocols, meteor_contest, sqlglot_normalize, bench_mp_pool, xml_etree_parse, genshi_xml, json_dumps, pylint
Ignored benchmarks (15) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 95.98% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x