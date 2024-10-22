# Results vs. 3.13.0

- fork: Fidget-Spinner
- ref: fix_unsafe_refcounti
- machine: linux-x86_64
- commit hash: 8278d07
- commit date: 2024-10-12
- overall geometric mean: 1.00x faster
- HPT reliability: 99.88%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241012-linux-x86_64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 252 ms: 1.05x faster                                                            |
| docutils       | 2.58 sec                                               | 2.63 sec: 1.02x slower                                                          |
| html5lib       | 64.5 ms                                                | 61.9 ms: 1.04x faster                                                           |
| tornado_http   | 91.5 ms                                                | 89.9 ms: 1.02x faster                                                           |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241012-linux-x86_64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|---------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg | 465 ms                                                 | 403 ms: 1.15x faster                                                            |
| async_tree_memoization    | 442 ms                                                 | 391 ms: 1.13x faster                                                            |
| async_tree_none           | 354 ms                                                 | 320 ms: 1.11x faster                                                            |
| async_tree_none_tg        | 320 ms                                                 | 309 ms: 1.03x faster                                                            |
| async_tree_cpu_io_mixed   | 574 ms                                                 | 562 ms: 1.02x faster                                                            |
| asyncio_tcp               | 488 ms                                                 | 480 ms: 1.02x faster                                                            |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.79 sec: 1.00x faster                                                          |
| coroutines                | 22.5 ms                                                | 23.2 ms: 1.03x slower                                                           |
| async_tree_io             | 843 ms                                                 | 929 ms: 1.10x slower                                                            |
| async_tree_io_tg          | 825 ms                                                 | 915 ms: 1.11x slower                                                            |
| Geometric mean            | (ref)                                                  | 1.02x faster                                                                    |

Benchmark hidden because not significant (3): async_generators, async_tree_cpu_io_mixed_tg, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241012-linux-x86_64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 77.8 ms: 1.01x faster                                                           |
| pidigits       | 186 ms                                                 | 187 ms: 1.01x slower                                                            |
| nbody          | 85.7 ms                                                | 88.9 ms: 1.04x slower                                                           |
| Geometric mean | (ref)                                                  | 1.01x slower                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241012-linux-x86_64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.61 ms: 1.08x faster                                                           |
| regex_compile  | 131 ms                                                 | 128 ms: 1.03x faster                                                            |
| regex_v8       | 25.3 ms                                                | 24.9 ms: 1.01x faster                                                           |
| regex_dna      | 220 ms                                                 | 217 ms: 1.01x faster                                                            |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241012-linux-x86_64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_generate   | 87.0 ms                                                | 85.5 ms: 1.02x faster                                                           |
| xml_etree_process    | 60.4 ms                                                | 59.4 ms: 1.02x faster                                                           |
| pickle               | 11.6 us                                                | 11.4 us: 1.01x faster                                                           |
| tomli_loads          | 2.11 sec                                               | 2.10 sec: 1.01x faster                                                          |
| json_loads           | 27.0 us                                                | 26.8 us: 1.01x faster                                                           |
| unpickle_pure_python | 213 us                                                 | 215 us: 1.01x slower                                                            |
| pickle_pure_python   | 300 us                                                 | 306 us: 1.02x slower                                                            |
| pickle_list          | 5.01 us                                                | 5.14 us: 1.03x slower                                                           |
| xml_etree_iterparse  | 102 ms                                                 | 105 ms: 1.03x slower                                                            |
| pickle_dict          | 33.2 us                                                | 34.5 us: 1.04x slower                                                           |
| unpickle_list        | 4.96 us                                                | 5.43 us: 1.09x slower                                                           |
| json_dumps           | 10.4 ms                                                | 11.8 ms: 1.13x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.02x slower                                                                    |

Benchmark hidden because not significant (2): xml_etree_parse, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241012-linux-x86_64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.6 ms: 1.00x faster                                                           |
| python_startup_no_site | 6.99 ms                                                | 7.03 ms: 1.01x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.00x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241012-linux-x86_64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_text     | 22.9 ms                                                | 21.9 ms: 1.05x faster                                                           |
| genshi_xml      | 50.3 ms                                                | 49.3 ms: 1.02x faster                                                           |
| django_template | 34.4 ms                                                | 33.8 ms: 1.02x faster                                                           |
| mako            | 11.1 ms                                                | 11.5 ms: 1.03x slower                                                           |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                                    |

All benchmarks:
===============

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241012-linux-x86_64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|---------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| deepcopy                  | 352 us                                                 | 262 us: 1.35x faster                                                            |
| deepcopy_memo             | 38.0 us                                                | 30.7 us: 1.24x faster                                                           |
| deepcopy_reduce           | 3.17 us                                                | 2.66 us: 1.19x faster                                                           |
| go                        | 142 ms                                                 | 119 ms: 1.19x faster                                                            |
| async_tree_memoization_tg | 465 ms                                                 | 403 ms: 1.15x faster                                                            |
| async_tree_memoization    | 442 ms                                                 | 391 ms: 1.13x faster                                                            |
| async_tree_none           | 354 ms                                                 | 320 ms: 1.11x faster                                                            |
| generators                | 28.8 ms                                                | 26.3 ms: 1.09x faster                                                           |
| regex_effbot              | 3.88 ms                                                | 3.61 ms: 1.08x faster                                                           |
| mdp                       | 2.74 sec                                               | 2.57 sec: 1.07x faster                                                          |
| telco                     | 8.45 ms                                                | 7.93 ms: 1.07x faster                                                           |
| pathlib                   | 17.1 ms                                                | 16.1 ms: 1.06x faster                                                           |
| pycparser                 | 1.19 sec                                               | 1.13 sec: 1.06x faster                                                          |
| spectral_norm             | 115 ms                                                 | 109 ms: 1.05x faster                                                            |
| 2to3                      | 265 ms                                                 | 252 ms: 1.05x faster                                                            |
| genshi_text               | 22.9 ms                                                | 21.9 ms: 1.05x faster                                                           |
| html5lib                  | 64.5 ms                                                | 61.9 ms: 1.04x faster                                                           |
| async_tree_none_tg        | 320 ms                                                 | 309 ms: 1.03x faster                                                            |
| richards                  | 48.1 ms                                                | 46.7 ms: 1.03x faster                                                           |
| thrift                    | 796 us                                                 | 774 us: 1.03x faster                                                            |
| richards_super            | 54.4 ms                                                | 52.9 ms: 1.03x faster                                                           |
| json                      | 5.20 ms                                                | 5.06 ms: 1.03x faster                                                           |
| regex_compile             | 131 ms                                                 | 128 ms: 1.03x faster                                                            |
| pprint_safe_repr          | 744 ms                                                 | 727 ms: 1.02x faster                                                            |
| sympy_expand              | 462 ms                                                 | 451 ms: 1.02x faster                                                            |
| sympy_str                 | 274 ms                                                 | 268 ms: 1.02x faster                                                            |
| async_tree_cpu_io_mixed   | 574 ms                                                 | 562 ms: 1.02x faster                                                            |
| genshi_xml                | 50.3 ms                                                | 49.3 ms: 1.02x faster                                                           |
| scimark_sparse_mat_mult   | 5.03 ms                                                | 4.92 ms: 1.02x faster                                                           |
| sympy_sum                 | 150 ms                                                 | 147 ms: 1.02x faster                                                            |
| django_template           | 34.4 ms                                                | 33.8 ms: 1.02x faster                                                           |
| asyncio_tcp               | 488 ms                                                 | 480 ms: 1.02x faster                                                            |
| tornado_http              | 91.5 ms                                                | 89.9 ms: 1.02x faster                                                           |
| pprint_pformat            | 1.51 sec                                               | 1.48 sec: 1.02x faster                                                          |
| xml_etree_generate        | 87.0 ms                                                | 85.5 ms: 1.02x faster                                                           |
| sqlglot_optimize          | 53.9 ms                                                | 53.1 ms: 1.02x faster                                                           |
| xml_etree_process         | 60.4 ms                                                | 59.4 ms: 1.02x faster                                                           |
| sqlglot_normalize         | 107 ms                                                 | 106 ms: 1.02x faster                                                            |
| scimark_fft               | 369 ms                                                 | 363 ms: 1.02x faster                                                            |
| pickle                    | 11.6 us                                                | 11.4 us: 1.01x faster                                                           |
| regex_v8                  | 25.3 ms                                                | 24.9 ms: 1.01x faster                                                           |
| regex_dna                 | 220 ms                                                 | 217 ms: 1.01x faster                                                            |
| scimark_lu                | 115 ms                                                 | 114 ms: 1.01x faster                                                            |
| float                     | 78.5 ms                                                | 77.8 ms: 1.01x faster                                                           |
| logging_simple            | 5.66 us                                                | 5.63 us: 1.01x faster                                                           |
| tomli_loads               | 2.11 sec                                               | 2.10 sec: 1.01x faster                                                          |
| json_loads                | 27.0 us                                                | 26.8 us: 1.01x faster                                                           |
| nqueens                   | 80.6 ms                                                | 80.2 ms: 1.01x faster                                                           |
| sympy_integrate           | 19.9 ms                                                | 19.8 ms: 1.00x faster                                                           |
| bpe_tokeniser             | 4.69 sec                                               | 4.67 sec: 1.00x faster                                                          |
| meteor_contest            | 108 ms                                                 | 107 ms: 1.00x faster                                                            |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.79 sec: 1.00x faster                                                          |
| python_startup            | 10.6 ms                                                | 10.6 ms: 1.00x faster                                                           |
| pidigits                  | 186 ms                                                 | 187 ms: 1.01x slower                                                            |
| sqlglot_transpile         | 1.57 ms                                                | 1.58 ms: 1.01x slower                                                           |
| python_startup_no_site    | 6.99 ms                                                | 7.03 ms: 1.01x slower                                                           |
| unpickle_pure_python      | 213 us                                                 | 215 us: 1.01x slower                                                            |
| chaos                     | 58.4 ms                                                | 58.9 ms: 1.01x slower                                                           |
| comprehensions            | 16.4 us                                                | 16.6 us: 1.01x slower                                                           |
| coverage                  | 83.7 ms                                                | 84.7 ms: 1.01x slower                                                           |
| scimark_sor               | 122 ms                                                 | 124 ms: 1.01x slower                                                            |
| typing_runtime_protocols  | 159 us                                                 | 162 us: 1.01x slower                                                            |
| sqlglot_parse             | 1.27 ms                                                | 1.29 ms: 1.02x slower                                                           |
| docutils                  | 2.58 sec                                               | 2.63 sec: 1.02x slower                                                          |
| pyflate                   | 460 ms                                                 | 468 ms: 1.02x slower                                                            |
| deltablue                 | 3.15 ms                                                | 3.21 ms: 1.02x slower                                                           |
| pickle_pure_python        | 300 us                                                 | 306 us: 1.02x slower                                                            |
| hexiom                    | 6.13 ms                                                | 6.29 ms: 1.03x slower                                                           |
| pickle_list               | 5.01 us                                                | 5.14 us: 1.03x slower                                                           |
| xml_etree_iterparse       | 102 ms                                                 | 105 ms: 1.03x slower                                                            |
| dulwich_log               | 63.0 ms                                                | 64.8 ms: 1.03x slower                                                           |
| gc_traversal              | 3.81 ms                                                | 3.92 ms: 1.03x slower                                                           |
| scimark_monte_carlo       | 66.3 ms                                                | 68.3 ms: 1.03x slower                                                           |
| coroutines                | 22.5 ms                                                | 23.2 ms: 1.03x slower                                                           |
| mako                      | 11.1 ms                                                | 11.5 ms: 1.03x slower                                                           |
| bench_thread_pool         | 815 us                                                 | 844 us: 1.04x slower                                                            |
| nbody                     | 85.7 ms                                                | 88.9 ms: 1.04x slower                                                           |
| pickle_dict               | 33.2 us                                                | 34.5 us: 1.04x slower                                                           |
| fannkuch                  | 381 ms                                                 | 399 ms: 1.05x slower                                                            |
| unpickle_list             | 4.96 us                                                | 5.43 us: 1.09x slower                                                           |
| async_tree_io             | 843 ms                                                 | 929 ms: 1.10x slower                                                            |
| async_tree_io_tg          | 825 ms                                                 | 915 ms: 1.11x slower                                                            |
| create_gc_cycles          | 1.61 ms                                                | 1.79 ms: 1.11x slower                                                           |
| json_dumps                | 10.4 ms                                                | 11.8 ms: 1.13x slower                                                           |
| unpack_sequence           | 42.4 ns                                                | 50.4 ns: 1.19x slower                                                           |
| bench_mp_pool             | 24.0 ms                                                | 56.0 ms: 2.33x slower                                                           |
| Geometric mean            | (ref)                                                  | 1.00x faster                                                                    |

Benchmark hidden because not significant (11): async_generators, xml_etree_parse, crypto_pyaes, raytrace, sqlite_synth, logging_format, async_tree_cpu_io_mixed_tg, asyncio_websockets, logging_silent, pylint, unpickle
Ignored benchmarks (7) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 99.88% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x