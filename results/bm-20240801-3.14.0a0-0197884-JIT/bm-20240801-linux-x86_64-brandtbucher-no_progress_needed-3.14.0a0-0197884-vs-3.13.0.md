# Results vs. 3.13.0

- fork: brandtbucher
- ref: no_progress_needed
- machine: linux-x86_64
- commit hash: 0197884
- commit date: 2024-08-01
- overall geometric mean: 1.01x faster
- HPT reliability: 54.26%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240801-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-0197884 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 284 ms: 1.07x slower                                                      |
| docutils       | 2.58 sec                                               | 2.99 sec: 1.16x slower                                                    |
| html5lib       | 64.5 ms                                                | 67.1 ms: 1.04x slower                                                     |
| tornado_http   | 91.5 ms                                                | 94.3 ms: 1.03x slower                                                     |
| Geometric mean | (ref)                                                  | 1.07x slower                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240801-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-0197884 |
|---------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization_tg | 465 ms                                                 | 395 ms: 1.18x faster                                                      |
| async_tree_none           | 354 ms                                                 | 328 ms: 1.08x faster                                                      |
| async_tree_memoization    | 442 ms                                                 | 415 ms: 1.07x faster                                                      |
| async_tree_none_tg        | 320 ms                                                 | 303 ms: 1.06x faster                                                      |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.80 sec: 1.01x slower                                                    |
| coroutines                | 22.5 ms                                                | 22.9 ms: 1.02x slower                                                     |
| asyncio_tcp               | 488 ms                                                 | 505 ms: 1.03x slower                                                      |
| async_tree_io_tg          | 825 ms                                                 | 868 ms: 1.05x slower                                                      |
| async_generators          | 433 ms                                                 | 458 ms: 1.06x slower                                                      |
| async_tree_io             | 843 ms                                                 | 908 ms: 1.08x slower                                                      |
| Geometric mean            | (ref)                                                  | 1.01x faster                                                              |

Benchmark hidden because not significant (3): async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240801-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-0197884 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 70.4 ms: 1.12x faster                                                     |
| nbody          | 85.7 ms                                                | 80.8 ms: 1.06x faster                                                     |
| pidigits       | 186 ms                                                 | 187 ms: 1.00x slower                                                      |
| Geometric mean | (ref)                                                  | 1.06x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240801-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-0197884 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.55 ms: 1.10x faster                                                     |
| regex_v8       | 25.3 ms                                                | 24.0 ms: 1.05x faster                                                     |
| regex_dna      | 220 ms                                                 | 224 ms: 1.02x slower                                                      |
| regex_compile  | 131 ms                                                 | 145 ms: 1.11x slower                                                      |
| Geometric mean | (ref)                                                  | 1.01x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240801-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-0197884 |
|---------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads         | 2.11 sec                                               | 1.94 sec: 1.09x faster                                                    |
| xml_etree_generate  | 87.0 ms                                                | 80.2 ms: 1.08x faster                                                     |
| xml_etree_process   | 60.4 ms                                                | 55.9 ms: 1.08x faster                                                     |
| xml_etree_parse     | 156 ms                                                 | 146 ms: 1.07x faster                                                      |
| xml_etree_iterparse | 102 ms                                                 | 98.3 ms: 1.04x faster                                                     |
| pickle_pure_python  | 300 us                                                 | 306 us: 1.02x slower                                                      |
| json_loads          | 27.0 us                                                | 28.2 us: 1.05x slower                                                     |
| Geometric mean      | (ref)                                                  | 1.03x faster                                                              |

Benchmark hidden because not significant (2): unpickle_pure_python, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240801-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-0197884 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.6 ms: 1.00x slower                                                     |
| python_startup_no_site | 6.99 ms                                                | 7.18 ms: 1.03x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240801-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-0197884 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.78 ms: 1.13x faster                                                     |
| genshi_text     | 22.9 ms                                                | 23.7 ms: 1.04x slower                                                     |
| django_template | 34.4 ms                                                | 36.1 ms: 1.05x slower                                                     |
| genshi_xml      | 50.3 ms                                                | 53.3 ms: 1.06x slower                                                     |
| Geometric mean  | (ref)                                                  | 1.00x slower                                                              |

All benchmarks:
===============

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240801-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-0197884 |
|---------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| deepcopy_memo             | 38.0 us                                                | 27.3 us: 1.39x faster                                                     |
| deepcopy                  | 352 us                                                 | 265 us: 1.33x faster                                                      |
| scimark_fft               | 369 ms                                                 | 309 ms: 1.19x faster                                                      |
| scimark_sparse_mat_mult   | 5.03 ms                                                | 4.21 ms: 1.19x faster                                                     |
| async_tree_memoization_tg | 465 ms                                                 | 395 ms: 1.18x faster                                                      |
| deepcopy_reduce           | 3.17 us                                                | 2.71 us: 1.17x faster                                                     |
| mako                      | 11.1 ms                                                | 9.78 ms: 1.13x faster                                                     |
| spectral_norm             | 115 ms                                                 | 103 ms: 1.12x faster                                                      |
| richards                  | 48.1 ms                                                | 43.1 ms: 1.12x faster                                                     |
| float                     | 78.5 ms                                                | 70.4 ms: 1.12x faster                                                     |
| richards_super            | 54.4 ms                                                | 49.2 ms: 1.11x faster                                                     |
| crypto_pyaes              | 73.0 ms                                                | 66.4 ms: 1.10x faster                                                     |
| regex_effbot              | 3.88 ms                                                | 3.55 ms: 1.10x faster                                                     |
| tomli_loads               | 2.11 sec                                               | 1.94 sec: 1.09x faster                                                    |
| xml_etree_generate        | 87.0 ms                                                | 80.2 ms: 1.08x faster                                                     |
| xml_etree_process         | 60.4 ms                                                | 55.9 ms: 1.08x faster                                                     |
| async_tree_none           | 354 ms                                                 | 328 ms: 1.08x faster                                                      |
| mdp                       | 2.74 sec                                               | 2.54 sec: 1.08x faster                                                    |
| xml_etree_parse           | 156 ms                                                 | 146 ms: 1.07x faster                                                      |
| telco                     | 8.45 ms                                                | 7.91 ms: 1.07x faster                                                     |
| async_tree_memoization    | 442 ms                                                 | 415 ms: 1.07x faster                                                      |
| nbody                     | 85.7 ms                                                | 80.8 ms: 1.06x faster                                                     |
| scimark_lu                | 115 ms                                                 | 109 ms: 1.06x faster                                                      |
| scimark_monte_carlo       | 66.3 ms                                                | 62.6 ms: 1.06x faster                                                     |
| async_tree_none_tg        | 320 ms                                                 | 303 ms: 1.06x faster                                                      |
| scimark_sor               | 122 ms                                                 | 116 ms: 1.06x faster                                                      |
| regex_v8                  | 25.3 ms                                                | 24.0 ms: 1.05x faster                                                     |
| pathlib                   | 17.1 ms                                                | 16.3 ms: 1.05x faster                                                     |
| pyflate                   | 460 ms                                                 | 440 ms: 1.04x faster                                                      |
| xml_etree_iterparse       | 102 ms                                                 | 98.3 ms: 1.04x faster                                                     |
| logging_format            | 6.25 us                                                | 6.04 us: 1.04x faster                                                     |
| bpe_tokeniser             | 4.69 sec                                               | 4.55 sec: 1.03x faster                                                    |
| logging_simple            | 5.66 us                                                | 5.51 us: 1.03x faster                                                     |
| deltablue                 | 3.15 ms                                                | 3.08 ms: 1.02x faster                                                     |
| pycparser                 | 1.19 sec                                               | 1.17 sec: 1.02x faster                                                    |
| fannkuch                  | 381 ms                                                 | 375 ms: 1.02x faster                                                      |
| json                      | 5.20 ms                                                | 5.13 ms: 1.01x faster                                                     |
| logging_silent            | 102 ns                                                 | 101 ns: 1.01x faster                                                      |
| thrift                    | 796 us                                                 | 787 us: 1.01x faster                                                      |
| chaos                     | 58.4 ms                                                | 57.9 ms: 1.01x faster                                                     |
| pidigits                  | 186 ms                                                 | 187 ms: 1.00x slower                                                      |
| python_startup            | 10.6 ms                                                | 10.6 ms: 1.00x slower                                                     |
| gc_traversal              | 3.81 ms                                                | 3.82 ms: 1.00x slower                                                     |
| bench_thread_pool         | 815 us                                                 | 820 us: 1.01x slower                                                      |
| comprehensions            | 16.4 us                                                | 16.5 us: 1.01x slower                                                     |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.80 sec: 1.01x slower                                                    |
| coroutines                | 22.5 ms                                                | 22.9 ms: 1.02x slower                                                     |
| regex_dna                 | 220 ms                                                 | 224 ms: 1.02x slower                                                      |
| pickle_pure_python        | 300 us                                                 | 306 us: 1.02x slower                                                      |
| python_startup_no_site    | 6.99 ms                                                | 7.18 ms: 1.03x slower                                                     |
| tornado_http              | 91.5 ms                                                | 94.3 ms: 1.03x slower                                                     |
| pprint_pformat            | 1.51 sec                                               | 1.56 sec: 1.03x slower                                                    |
| asyncio_tcp               | 488 ms                                                 | 505 ms: 1.03x slower                                                      |
| genshi_text               | 22.9 ms                                                | 23.7 ms: 1.04x slower                                                     |
| html5lib                  | 64.5 ms                                                | 67.1 ms: 1.04x slower                                                     |
| json_loads                | 27.0 us                                                | 28.2 us: 1.05x slower                                                     |
| django_template           | 34.4 ms                                                | 36.1 ms: 1.05x slower                                                     |
| async_tree_io_tg          | 825 ms                                                 | 868 ms: 1.05x slower                                                      |
| raytrace                  | 262 ms                                                 | 276 ms: 1.05x slower                                                      |
| async_generators          | 433 ms                                                 | 458 ms: 1.06x slower                                                      |
| genshi_xml                | 50.3 ms                                                | 53.3 ms: 1.06x slower                                                     |
| sqlglot_parse             | 1.27 ms                                                | 1.34 ms: 1.06x slower                                                     |
| go                        | 142 ms                                                 | 150 ms: 1.06x slower                                                      |
| nqueens                   | 80.6 ms                                                | 85.7 ms: 1.06x slower                                                     |
| sqlglot_normalize         | 107 ms                                                 | 114 ms: 1.06x slower                                                      |
| sqlglot_transpile         | 1.57 ms                                                | 1.69 ms: 1.07x slower                                                     |
| 2to3                      | 265 ms                                                 | 284 ms: 1.07x slower                                                      |
| typing_runtime_protocols  | 159 us                                                 | 171 us: 1.07x slower                                                      |
| async_tree_io             | 843 ms                                                 | 908 ms: 1.08x slower                                                      |
| dask                      | 338 ms                                                 | 364 ms: 1.08x slower                                                      |
| coverage                  | 83.7 ms                                                | 90.4 ms: 1.08x slower                                                     |
| sqlglot_optimize          | 53.9 ms                                                | 58.6 ms: 1.09x slower                                                     |
| create_gc_cycles          | 1.61 ms                                                | 1.76 ms: 1.10x slower                                                     |
| regex_compile             | 131 ms                                                 | 145 ms: 1.11x slower                                                      |
| sympy_expand              | 462 ms                                                 | 517 ms: 1.12x slower                                                      |
| sympy_str                 | 274 ms                                                 | 310 ms: 1.13x slower                                                      |
| generators                | 28.8 ms                                                | 32.9 ms: 1.14x slower                                                     |
| docutils                  | 2.58 sec                                               | 2.99 sec: 1.16x slower                                                    |
| sympy_integrate           | 19.9 ms                                                | 23.1 ms: 1.16x slower                                                     |
| pylint                    | 313 ms                                                 | 370 ms: 1.18x slower                                                      |
| sympy_sum                 | 150 ms                                                 | 178 ms: 1.19x slower                                                      |
| hexiom                    | 6.13 ms                                                | 7.64 ms: 1.25x slower                                                     |
| Geometric mean            | (ref)                                                  | 1.01x faster                                                              |

Benchmark hidden because not significant (8): async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, bench_mp_pool, asyncio_websockets, meteor_contest, unpickle_pure_python, json_dumps, pprint_safe_repr
Ignored benchmarks (14) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 54.26% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.09x