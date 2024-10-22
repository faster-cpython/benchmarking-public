# Results vs. 3.13.0

- fork: faster-cpython
- ref: more_robust_immortal
- machine: linux-x86_64
- commit hash: 9f86e46
- commit date: 2024-10-10
- overall geometric mean: 1.00x slower
- HPT reliability: 79.53%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241010-linux-x86_64-faster%2dcpython-more_robust_immortal-3.14.0a0-9f86e46 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 254 ms: 1.04x faster                                                            |
| docutils       | 2.58 sec                                               | 2.62 sec: 1.01x slower                                                          |
| html5lib       | 64.5 ms                                                | 61.7 ms: 1.05x faster                                                           |
| tornado_http   | 91.5 ms                                                | 90.4 ms: 1.01x faster                                                           |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241010-linux-x86_64-faster%2dcpython-more_robust_immortal-3.14.0a0-9f86e46 |
|---------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg | 465 ms                                                 | 404 ms: 1.15x faster                                                            |
| async_tree_memoization    | 442 ms                                                 | 396 ms: 1.12x faster                                                            |
| async_tree_none           | 354 ms                                                 | 325 ms: 1.09x faster                                                            |
| async_tree_cpu_io_mixed   | 574 ms                                                 | 559 ms: 1.03x faster                                                            |
| async_tree_none_tg        | 320 ms                                                 | 312 ms: 1.03x faster                                                            |
| asyncio_tcp               | 488 ms                                                 | 477 ms: 1.02x faster                                                            |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.78 sec: 1.01x faster                                                          |
| async_generators          | 433 ms                                                 | 437 ms: 1.01x slower                                                            |
| coroutines                | 22.5 ms                                                | 23.8 ms: 1.06x slower                                                           |
| async_tree_io             | 843 ms                                                 | 937 ms: 1.11x slower                                                            |
| async_tree_io_tg          | 825 ms                                                 | 919 ms: 1.11x slower                                                            |
| Geometric mean            | (ref)                                                  | 1.01x faster                                                                    |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed_tg, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241010-linux-x86_64-faster%2dcpython-more_robust_immortal-3.14.0a0-9f86e46 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 78.8 ms: 1.00x slower                                                           |
| pidigits       | 186 ms                                                 | 188 ms: 1.01x slower                                                            |
| nbody          | 85.7 ms                                                | 92.7 ms: 1.08x slower                                                           |
| Geometric mean | (ref)                                                  | 1.03x slower                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241010-linux-x86_64-faster%2dcpython-more_robust_immortal-3.14.0a0-9f86e46 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.62 ms: 1.07x faster                                                           |
| regex_v8       | 25.3 ms                                                | 24.3 ms: 1.04x faster                                                           |
| regex_compile  | 131 ms                                                 | 129 ms: 1.02x faster                                                            |
| regex_dna      | 220 ms                                                 | 222 ms: 1.01x slower                                                            |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241010-linux-x86_64-faster%2dcpython-more_robust_immortal-3.14.0a0-9f86e46 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| json_loads           | 27.0 us                                                | 26.3 us: 1.03x faster                                                           |
| tomli_loads          | 2.11 sec                                               | 2.08 sec: 1.01x faster                                                          |
| xml_etree_process    | 60.4 ms                                                | 59.6 ms: 1.01x faster                                                           |
| pickle               | 11.6 us                                                | 11.4 us: 1.01x faster                                                           |
| json_dumps           | 10.4 ms                                                | 10.6 ms: 1.02x slower                                                           |
| unpickle             | 14.9 us                                                | 15.1 us: 1.02x slower                                                           |
| pickle_list          | 5.01 us                                                | 5.11 us: 1.02x slower                                                           |
| xml_etree_iterparse  | 102 ms                                                 | 105 ms: 1.03x slower                                                            |
| pickle_dict          | 33.2 us                                                | 34.2 us: 1.03x slower                                                           |
| pickle_pure_python   | 300 us                                                 | 309 us: 1.03x slower                                                            |
| unpickle_pure_python | 213 us                                                 | 220 us: 1.03x slower                                                            |
| unpickle_list        | 4.96 us                                                | 5.19 us: 1.05x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                                    |

Benchmark hidden because not significant (2): xml_etree_parse, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241010-linux-x86_64-faster%2dcpython-more_robust_immortal-3.14.0a0-9f86e46 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.6 ms: 1.00x slower                                                           |
| python_startup_no_site | 6.99 ms                                                | 7.05 ms: 1.01x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241010-linux-x86_64-faster%2dcpython-more_robust_immortal-3.14.0a0-9f86e46 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_xml      | 50.3 ms                                                | 49.1 ms: 1.03x faster                                                           |
| django_template | 34.4 ms                                                | 34.2 ms: 1.01x faster                                                           |
| mako            | 11.1 ms                                                | 11.6 ms: 1.05x slower                                                           |
| Geometric mean  | (ref)                                                  | 1.00x slower                                                                    |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241010-linux-x86_64-faster%2dcpython-more_robust_immortal-3.14.0a0-9f86e46 |
|---------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| deepcopy                  | 352 us                                                 | 260 us: 1.35x faster                                                            |
| deepcopy_memo             | 38.0 us                                                | 31.3 us: 1.21x faster                                                           |
| deepcopy_reduce           | 3.17 us                                                | 2.66 us: 1.19x faster                                                           |
| go                        | 142 ms                                                 | 121 ms: 1.17x faster                                                            |
| async_tree_memoization_tg | 465 ms                                                 | 404 ms: 1.15x faster                                                            |
| async_tree_memoization    | 442 ms                                                 | 396 ms: 1.12x faster                                                            |
| mdp                       | 2.74 sec                                               | 2.51 sec: 1.09x faster                                                          |
| async_tree_none           | 354 ms                                                 | 325 ms: 1.09x faster                                                            |
| regex_effbot              | 3.88 ms                                                | 3.62 ms: 1.07x faster                                                           |
| generators                | 28.8 ms                                                | 26.9 ms: 1.07x faster                                                           |
| pathlib                   | 17.1 ms                                                | 16.0 ms: 1.07x faster                                                           |
| json                      | 5.20 ms                                                | 4.93 ms: 1.05x faster                                                           |
| telco                     | 8.45 ms                                                | 8.01 ms: 1.05x faster                                                           |
| scimark_sparse_mat_mult   | 5.03 ms                                                | 4.80 ms: 1.05x faster                                                           |
| html5lib                  | 64.5 ms                                                | 61.7 ms: 1.05x faster                                                           |
| 2to3                      | 265 ms                                                 | 254 ms: 1.04x faster                                                            |
| regex_v8                  | 25.3 ms                                                | 24.3 ms: 1.04x faster                                                           |
| richards                  | 48.1 ms                                                | 46.8 ms: 1.03x faster                                                           |
| richards_super            | 54.4 ms                                                | 52.9 ms: 1.03x faster                                                           |
| async_tree_cpu_io_mixed   | 574 ms                                                 | 559 ms: 1.03x faster                                                            |
| pprint_safe_repr          | 744 ms                                                 | 725 ms: 1.03x faster                                                            |
| async_tree_none_tg        | 320 ms                                                 | 312 ms: 1.03x faster                                                            |
| json_loads                | 27.0 us                                                | 26.3 us: 1.03x faster                                                           |
| genshi_xml                | 50.3 ms                                                | 49.1 ms: 1.03x faster                                                           |
| asyncio_tcp               | 488 ms                                                 | 477 ms: 1.02x faster                                                            |
| thrift                    | 796 us                                                 | 780 us: 1.02x faster                                                            |
| pycparser                 | 1.19 sec                                               | 1.17 sec: 1.02x faster                                                          |
| sympy_str                 | 274 ms                                                 | 268 ms: 1.02x faster                                                            |
| regex_compile             | 131 ms                                                 | 129 ms: 1.02x faster                                                            |
| tomli_loads               | 2.11 sec                                               | 2.08 sec: 1.01x faster                                                          |
| xml_etree_process         | 60.4 ms                                                | 59.6 ms: 1.01x faster                                                           |
| logging_format            | 6.25 us                                                | 6.18 us: 1.01x faster                                                           |
| tornado_http              | 91.5 ms                                                | 90.4 ms: 1.01x faster                                                           |
| logging_simple            | 5.66 us                                                | 5.60 us: 1.01x faster                                                           |
| pickle                    | 11.6 us                                                | 11.4 us: 1.01x faster                                                           |
| sympy_sum                 | 150 ms                                                 | 148 ms: 1.01x faster                                                            |
| pprint_pformat            | 1.51 sec                                               | 1.50 sec: 1.01x faster                                                          |
| meteor_contest            | 108 ms                                                 | 107 ms: 1.01x faster                                                            |
| sqlglot_optimize          | 53.9 ms                                                | 53.6 ms: 1.01x faster                                                           |
| django_template           | 34.4 ms                                                | 34.2 ms: 1.01x faster                                                           |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.78 sec: 1.01x faster                                                          |
| sqlglot_normalize         | 107 ms                                                 | 107 ms: 1.01x faster                                                            |
| pyflate                   | 460 ms                                                 | 457 ms: 1.01x faster                                                            |
| python_startup            | 10.6 ms                                                | 10.6 ms: 1.00x slower                                                           |
| float                     | 78.5 ms                                                | 78.8 ms: 1.00x slower                                                           |
| crypto_pyaes              | 73.0 ms                                                | 73.3 ms: 1.00x slower                                                           |
| spectral_norm             | 115 ms                                                 | 116 ms: 1.01x slower                                                            |
| pidigits                  | 186 ms                                                 | 188 ms: 1.01x slower                                                            |
| python_startup_no_site    | 6.99 ms                                                | 7.05 ms: 1.01x slower                                                           |
| scimark_lu                | 115 ms                                                 | 116 ms: 1.01x slower                                                            |
| async_generators          | 433 ms                                                 | 437 ms: 1.01x slower                                                            |
| regex_dna                 | 220 ms                                                 | 222 ms: 1.01x slower                                                            |
| scimark_fft               | 369 ms                                                 | 373 ms: 1.01x slower                                                            |
| docutils                  | 2.58 sec                                               | 2.62 sec: 1.01x slower                                                          |
| json_dumps                | 10.4 ms                                                | 10.6 ms: 1.02x slower                                                           |
| sqlglot_transpile         | 1.57 ms                                                | 1.60 ms: 1.02x slower                                                           |
| unpickle                  | 14.9 us                                                | 15.1 us: 1.02x slower                                                           |
| pickle_list               | 5.01 us                                                | 5.11 us: 1.02x slower                                                           |
| dulwich_log               | 63.0 ms                                                | 64.3 ms: 1.02x slower                                                           |
| xml_etree_iterparse       | 102 ms                                                 | 105 ms: 1.03x slower                                                            |
| scimark_sor               | 122 ms                                                 | 126 ms: 1.03x slower                                                            |
| hexiom                    | 6.13 ms                                                | 6.29 ms: 1.03x slower                                                           |
| comprehensions            | 16.4 us                                                | 16.9 us: 1.03x slower                                                           |
| raytrace                  | 262 ms                                                 | 269 ms: 1.03x slower                                                            |
| pickle_dict               | 33.2 us                                                | 34.2 us: 1.03x slower                                                           |
| sqlglot_parse             | 1.27 ms                                                | 1.30 ms: 1.03x slower                                                           |
| pickle_pure_python        | 300 us                                                 | 309 us: 1.03x slower                                                            |
| chaos                     | 58.4 ms                                                | 60.2 ms: 1.03x slower                                                           |
| unpickle_pure_python      | 213 us                                                 | 220 us: 1.03x slower                                                            |
| scimark_monte_carlo       | 66.3 ms                                                | 68.5 ms: 1.03x slower                                                           |
| bench_thread_pool         | 815 us                                                 | 849 us: 1.04x slower                                                            |
| mako                      | 11.1 ms                                                | 11.6 ms: 1.05x slower                                                           |
| unpickle_list             | 4.96 us                                                | 5.19 us: 1.05x slower                                                           |
| gc_traversal              | 3.81 ms                                                | 3.99 ms: 1.05x slower                                                           |
| deltablue                 | 3.15 ms                                                | 3.32 ms: 1.05x slower                                                           |
| logging_silent            | 102 ns                                                 | 108 ns: 1.06x slower                                                            |
| coroutines                | 22.5 ms                                                | 23.8 ms: 1.06x slower                                                           |
| fannkuch                  | 381 ms                                                 | 403 ms: 1.06x slower                                                            |
| nbody                     | 85.7 ms                                                | 92.7 ms: 1.08x slower                                                           |
| create_gc_cycles          | 1.61 ms                                                | 1.78 ms: 1.11x slower                                                           |
| unpack_sequence           | 42.4 ns                                                | 47.0 ns: 1.11x slower                                                           |
| async_tree_io             | 843 ms                                                 | 937 ms: 1.11x slower                                                            |
| async_tree_io_tg          | 825 ms                                                 | 919 ms: 1.11x slower                                                            |
| bench_mp_pool             | 24.0 ms                                                | 56.3 ms: 2.35x slower                                                           |
| Geometric mean            | (ref)                                                  | 1.00x slower                                                                    |

Benchmark hidden because not significant (13): sympy_expand, xml_etree_parse, genshi_text, async_tree_cpu_io_mixed_tg, typing_runtime_protocols, asyncio_websockets, sympy_integrate, sqlite_synth, xml_etree_generate, nqueens, bpe_tokeniser, coverage, pylint
Ignored benchmarks (7) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 79.53% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x