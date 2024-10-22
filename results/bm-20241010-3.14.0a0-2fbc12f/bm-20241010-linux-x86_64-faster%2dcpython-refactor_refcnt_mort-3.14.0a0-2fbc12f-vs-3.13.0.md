# Results vs. 3.13.0

- fork: faster-cpython
- ref: refactor_refcnt_mort
- machine: linux-x86_64
- commit hash: 2fbc12f
- commit date: 2024-10-10
- overall geometric mean: 1.01x slower
- HPT reliability: 98.03%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241010-linux-x86_64-faster%2dcpython-refactor_refcnt_mort-3.14.0a0-2fbc12f |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 256 ms: 1.03x faster                                                            |
| docutils       | 2.58 sec                                               | 2.65 sec: 1.03x slower                                                          |
| html5lib       | 64.5 ms                                                | 62.6 ms: 1.03x faster                                                           |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                    |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241010-linux-x86_64-faster%2dcpython-refactor_refcnt_mort-3.14.0a0-2fbc12f |
|---------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg | 465 ms                                                 | 405 ms: 1.15x faster                                                            |
| async_tree_memoization    | 442 ms                                                 | 408 ms: 1.08x faster                                                            |
| async_tree_none           | 354 ms                                                 | 327 ms: 1.08x faster                                                            |
| async_tree_none_tg        | 320 ms                                                 | 311 ms: 1.03x faster                                                            |
| async_tree_cpu_io_mixed   | 574 ms                                                 | 561 ms: 1.02x faster                                                            |
| asyncio_tcp               | 488 ms                                                 | 479 ms: 1.02x faster                                                            |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.79 sec: 1.00x faster                                                          |
| async_generators          | 433 ms                                                 | 438 ms: 1.01x slower                                                            |
| coroutines                | 22.5 ms                                                | 24.2 ms: 1.07x slower                                                           |
| async_tree_io             | 843 ms                                                 | 930 ms: 1.10x slower                                                            |
| async_tree_io_tg          | 825 ms                                                 | 917 ms: 1.11x slower                                                            |
| Geometric mean            | (ref)                                                  | 1.01x faster                                                                    |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed_tg, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241010-linux-x86_64-faster%2dcpython-refactor_refcnt_mort-3.14.0a0-2fbc12f |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 79.1 ms: 1.01x slower                                                           |
| pidigits       | 186 ms                                                 | 189 ms: 1.01x slower                                                            |
| nbody          | 85.7 ms                                                | 93.0 ms: 1.08x slower                                                           |
| Geometric mean | (ref)                                                  | 1.03x slower                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241010-linux-x86_64-faster%2dcpython-refactor_refcnt_mort-3.14.0a0-2fbc12f |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.57 ms: 1.09x faster                                                           |
| regex_v8       | 25.3 ms                                                | 24.4 ms: 1.03x faster                                                           |
| regex_dna      | 220 ms                                                 | 217 ms: 1.02x faster                                                            |
| regex_compile  | 131 ms                                                 | 130 ms: 1.01x faster                                                            |
| Geometric mean | (ref)                                                  | 1.04x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241010-linux-x86_64-faster%2dcpython-refactor_refcnt_mort-3.14.0a0-2fbc12f |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| json_loads           | 27.0 us                                                | 26.7 us: 1.01x faster                                                           |
| xml_etree_process    | 60.4 ms                                                | 60.7 ms: 1.00x slower                                                           |
| xml_etree_generate   | 87.0 ms                                                | 87.8 ms: 1.01x slower                                                           |
| pickle_dict          | 33.2 us                                                | 34.0 us: 1.03x slower                                                           |
| tomli_loads          | 2.11 sec                                               | 2.17 sec: 1.03x slower                                                          |
| xml_etree_iterparse  | 102 ms                                                 | 105 ms: 1.03x slower                                                            |
| pickle_pure_python   | 300 us                                                 | 315 us: 1.05x slower                                                            |
| unpickle_pure_python | 213 us                                                 | 224 us: 1.05x slower                                                            |
| unpickle_list        | 4.96 us                                                | 5.38 us: 1.08x slower                                                           |
| json_dumps           | 10.4 ms                                                | 11.6 ms: 1.12x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.03x slower                                                                    |

Benchmark hidden because not significant (4): pickle_list, xml_etree_parse, pickle, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241010-linux-x86_64-faster%2dcpython-refactor_refcnt_mort-3.14.0a0-2fbc12f |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.6 ms: 1.00x slower                                                           |
| python_startup_no_site | 6.99 ms                                                | 7.06 ms: 1.01x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241010-linux-x86_64-faster%2dcpython-refactor_refcnt_mort-3.14.0a0-2fbc12f |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| django_template | 34.4 ms                                                | 35.0 ms: 1.02x slower                                                           |
| genshi_text     | 22.9 ms                                                | 23.5 ms: 1.03x slower                                                           |
| genshi_xml      | 50.3 ms                                                | 51.8 ms: 1.03x slower                                                           |
| mako            | 11.1 ms                                                | 11.6 ms: 1.05x slower                                                           |
| Geometric mean  | (ref)                                                  | 1.03x slower                                                                    |

All benchmarks:
===============

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241010-linux-x86_64-faster%2dcpython-refactor_refcnt_mort-3.14.0a0-2fbc12f |
|---------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| deepcopy                  | 352 us                                                 | 268 us: 1.31x faster                                                            |
| deepcopy_memo             | 38.0 us                                                | 32.2 us: 1.18x faster                                                           |
| go                        | 142 ms                                                 | 123 ms: 1.15x faster                                                            |
| async_tree_memoization_tg | 465 ms                                                 | 405 ms: 1.15x faster                                                            |
| deepcopy_reduce           | 3.17 us                                                | 2.76 us: 1.15x faster                                                           |
| regex_effbot              | 3.88 ms                                                | 3.57 ms: 1.09x faster                                                           |
| mdp                       | 2.74 sec                                               | 2.52 sec: 1.09x faster                                                          |
| async_tree_memoization    | 442 ms                                                 | 408 ms: 1.08x faster                                                            |
| async_tree_none           | 354 ms                                                 | 327 ms: 1.08x faster                                                            |
| json                      | 5.20 ms                                                | 4.85 ms: 1.07x faster                                                           |
| pathlib                   | 17.1 ms                                                | 16.1 ms: 1.06x faster                                                           |
| telco                     | 8.45 ms                                                | 8.02 ms: 1.05x faster                                                           |
| regex_v8                  | 25.3 ms                                                | 24.4 ms: 1.03x faster                                                           |
| 2to3                      | 265 ms                                                 | 256 ms: 1.03x faster                                                            |
| html5lib                  | 64.5 ms                                                | 62.6 ms: 1.03x faster                                                           |
| async_tree_none_tg        | 320 ms                                                 | 311 ms: 1.03x faster                                                            |
| async_tree_cpu_io_mixed   | 574 ms                                                 | 561 ms: 1.02x faster                                                            |
| richards                  | 48.1 ms                                                | 47.1 ms: 1.02x faster                                                           |
| richards_super            | 54.4 ms                                                | 53.3 ms: 1.02x faster                                                           |
| generators                | 28.8 ms                                                | 28.2 ms: 1.02x faster                                                           |
| scimark_sparse_mat_mult   | 5.03 ms                                                | 4.93 ms: 1.02x faster                                                           |
| asyncio_tcp               | 488 ms                                                 | 479 ms: 1.02x faster                                                            |
| thrift                    | 796 us                                                 | 783 us: 1.02x faster                                                            |
| regex_dna                 | 220 ms                                                 | 217 ms: 1.02x faster                                                            |
| crypto_pyaes              | 73.0 ms                                                | 72.1 ms: 1.01x faster                                                           |
| pprint_safe_repr          | 744 ms                                                 | 736 ms: 1.01x faster                                                            |
| json_loads                | 27.0 us                                                | 26.7 us: 1.01x faster                                                           |
| regex_compile             | 131 ms                                                 | 130 ms: 1.01x faster                                                            |
| nqueens                   | 80.6 ms                                                | 80.3 ms: 1.00x faster                                                           |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.79 sec: 1.00x faster                                                          |
| meteor_contest            | 108 ms                                                 | 107 ms: 1.00x faster                                                            |
| python_startup            | 10.6 ms                                                | 10.6 ms: 1.00x slower                                                           |
| xml_etree_process         | 60.4 ms                                                | 60.7 ms: 1.00x slower                                                           |
| float                     | 78.5 ms                                                | 79.1 ms: 1.01x slower                                                           |
| xml_etree_generate        | 87.0 ms                                                | 87.8 ms: 1.01x slower                                                           |
| python_startup_no_site    | 6.99 ms                                                | 7.06 ms: 1.01x slower                                                           |
| scimark_fft               | 369 ms                                                 | 373 ms: 1.01x slower                                                            |
| sqlglot_optimize          | 53.9 ms                                                | 54.5 ms: 1.01x slower                                                           |
| sympy_integrate           | 19.9 ms                                                | 20.1 ms: 1.01x slower                                                           |
| async_generators          | 433 ms                                                 | 438 ms: 1.01x slower                                                            |
| pidigits                  | 186 ms                                                 | 189 ms: 1.01x slower                                                            |
| logging_format            | 6.25 us                                                | 6.35 us: 1.02x slower                                                           |
| django_template           | 34.4 ms                                                | 35.0 ms: 1.02x slower                                                           |
| spectral_norm             | 115 ms                                                 | 117 ms: 1.02x slower                                                            |
| sqlglot_normalize         | 107 ms                                                 | 110 ms: 1.02x slower                                                            |
| bpe_tokeniser             | 4.69 sec                                               | 4.79 sec: 1.02x slower                                                          |
| sqlglot_transpile         | 1.57 ms                                                | 1.61 ms: 1.03x slower                                                           |
| typing_runtime_protocols  | 159 us                                                 | 163 us: 1.03x slower                                                            |
| docutils                  | 2.58 sec                                               | 2.65 sec: 1.03x slower                                                          |
| pickle_dict               | 33.2 us                                                | 34.0 us: 1.03x slower                                                           |
| genshi_text               | 22.9 ms                                                | 23.5 ms: 1.03x slower                                                           |
| genshi_xml                | 50.3 ms                                                | 51.8 ms: 1.03x slower                                                           |
| tomli_loads               | 2.11 sec                                               | 2.17 sec: 1.03x slower                                                          |
| scimark_lu                | 115 ms                                                 | 119 ms: 1.03x slower                                                            |
| xml_etree_iterparse       | 102 ms                                                 | 105 ms: 1.03x slower                                                            |
| logging_silent            | 102 ns                                                 | 106 ns: 1.03x slower                                                            |
| sqlglot_parse             | 1.27 ms                                                | 1.31 ms: 1.04x slower                                                           |
| comprehensions            | 16.4 us                                                | 17.0 us: 1.04x slower                                                           |
| dulwich_log               | 63.0 ms                                                | 65.4 ms: 1.04x slower                                                           |
| scimark_monte_carlo       | 66.3 ms                                                | 69.2 ms: 1.04x slower                                                           |
| bench_thread_pool         | 815 us                                                 | 850 us: 1.04x slower                                                            |
| hexiom                    | 6.13 ms                                                | 6.39 ms: 1.04x slower                                                           |
| gc_traversal              | 3.81 ms                                                | 3.98 ms: 1.05x slower                                                           |
| chaos                     | 58.4 ms                                                | 61.2 ms: 1.05x slower                                                           |
| pickle_pure_python        | 300 us                                                 | 315 us: 1.05x slower                                                            |
| mako                      | 11.1 ms                                                | 11.6 ms: 1.05x slower                                                           |
| raytrace                  | 262 ms                                                 | 275 ms: 1.05x slower                                                            |
| unpickle_pure_python      | 213 us                                                 | 224 us: 1.05x slower                                                            |
| pyflate                   | 460 ms                                                 | 483 ms: 1.05x slower                                                            |
| scimark_sor               | 122 ms                                                 | 129 ms: 1.05x slower                                                            |
| deltablue                 | 3.15 ms                                                | 3.36 ms: 1.07x slower                                                           |
| coroutines                | 22.5 ms                                                | 24.2 ms: 1.07x slower                                                           |
| unpickle_list             | 4.96 us                                                | 5.38 us: 1.08x slower                                                           |
| nbody                     | 85.7 ms                                                | 93.0 ms: 1.08x slower                                                           |
| fannkuch                  | 381 ms                                                 | 413 ms: 1.09x slower                                                            |
| coverage                  | 83.7 ms                                                | 91.8 ms: 1.10x slower                                                           |
| async_tree_io             | 843 ms                                                 | 930 ms: 1.10x slower                                                            |
| create_gc_cycles          | 1.61 ms                                                | 1.78 ms: 1.11x slower                                                           |
| async_tree_io_tg          | 825 ms                                                 | 917 ms: 1.11x slower                                                            |
| json_dumps                | 10.4 ms                                                | 11.6 ms: 1.12x slower                                                           |
| unpack_sequence           | 42.4 ns                                                | 49.7 ns: 1.17x slower                                                           |
| bench_mp_pool             | 24.0 ms                                                | 56.3 ms: 2.35x slower                                                           |
| Geometric mean            | (ref)                                                  | 1.01x slower                                                                    |

Benchmark hidden because not significant (15): sympy_str, pycparser, async_tree_cpu_io_mixed_tg, sympy_sum, tornado_http, asyncio_websockets, pickle_list, xml_etree_parse, sqlite_synth, sympy_expand, pprint_pformat, logging_simple, pickle, unpickle, pylint
Ignored benchmarks (7) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 98.03% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x