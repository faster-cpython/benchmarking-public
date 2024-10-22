# Results vs. 3.13.0

- fork: brandtbucher
- ref: no_progress_needed
- machine: linux-x86_64
- commit hash: 363fca1
- commit date: 2024-07-13
- overall geometric mean: 1.05x slower
- HPT reliability: 88.63%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-363fca1 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 290 ms: 1.09x slower                                                      |
| docutils       | 2.58 sec                                               | 7.91 sec: 3.06x slower                                                    |
| html5lib       | 64.5 ms                                                | 76.3 ms: 1.18x slower                                                     |
| tornado_http   | 91.5 ms                                                | 95.1 ms: 1.04x slower                                                     |
| Geometric mean | (ref)                                                  | 1.42x slower                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-363fca1 |
|---------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization_tg | 465 ms                                                 | 379 ms: 1.23x faster                                                      |
| async_tree_none           | 354 ms                                                 | 327 ms: 1.08x faster                                                      |
| async_tree_memoization    | 442 ms                                                 | 411 ms: 1.08x faster                                                      |
| async_tree_none_tg        | 320 ms                                                 | 301 ms: 1.06x faster                                                      |
| async_tree_cpu_io_mixed   | 574 ms                                                 | 563 ms: 1.02x faster                                                      |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.81 sec: 1.01x slower                                                    |
| asyncio_tcp               | 488 ms                                                 | 503 ms: 1.03x slower                                                      |
| async_tree_io_tg          | 825 ms                                                 | 850 ms: 1.03x slower                                                      |
| coroutines                | 22.5 ms                                                | 23.2 ms: 1.03x slower                                                     |
| async_generators          | 433 ms                                                 | 456 ms: 1.05x slower                                                      |
| Geometric mean            | (ref)                                                  | 1.02x faster                                                              |

Benchmark hidden because not significant (3): async_tree_cpu_io_mixed_tg, asyncio_websockets, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-363fca1 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 70.5 ms: 1.11x faster                                                     |
| nbody          | 85.7 ms                                                | 79.8 ms: 1.07x faster                                                     |
| pidigits       | 186 ms                                                 | 188 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                  | 1.06x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-363fca1 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.86 ms: 1.01x faster                                                     |
| regex_v8       | 25.3 ms                                                | 25.4 ms: 1.00x slower                                                     |
| regex_dna      | 220 ms                                                 | 224 ms: 1.02x slower                                                      |
| regex_compile  | 131 ms                                                 | 135 ms: 1.03x slower                                                      |
| Geometric mean | (ref)                                                  | 1.01x slower                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-363fca1 |
|---------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads         | 2.11 sec                                               | 1.90 sec: 1.11x faster                                                    |
| xml_etree_parse     | 156 ms                                                 | 150 ms: 1.04x faster                                                      |
| xml_etree_generate  | 87.0 ms                                                | 84.4 ms: 1.03x faster                                                     |
| xml_etree_iterparse | 102 ms                                                 | 99.3 ms: 1.03x faster                                                     |
| xml_etree_process   | 60.4 ms                                                | 59.8 ms: 1.01x faster                                                     |
| json_dumps          | 10.4 ms                                                | 10.5 ms: 1.01x slower                                                     |
| json_loads          | 27.0 us                                                | 27.6 us: 1.02x slower                                                     |
| pickle_pure_python  | 300 us                                                 | 313 us: 1.04x slower                                                      |
| Geometric mean      | (ref)                                                  | 1.02x faster                                                              |

Benchmark hidden because not significant (1): unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-363fca1 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.5 ms: 1.01x faster                                                     |
| python_startup_no_site | 6.99 ms                                                | 7.08 ms: 1.01x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.00x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-363fca1 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.81 ms: 1.13x faster                                                     |
| django_template | 34.4 ms                                                | 38.6 ms: 1.12x slower                                                     |
| genshi_xml      | 50.3 ms                                                | 75.1 ms: 1.49x slower                                                     |
| genshi_text     | 22.9 ms                                                | 34.1 ms: 1.49x slower                                                     |
| Geometric mean  | (ref)                                                  | 1.22x slower                                                              |

All benchmarks:
===============

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-363fca1 |
|---------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| deepcopy_memo             | 38.0 us                                                | 26.9 us: 1.41x faster                                                     |
| deepcopy                  | 352 us                                                 | 270 us: 1.31x faster                                                      |
| async_tree_memoization_tg | 465 ms                                                 | 379 ms: 1.23x faster                                                      |
| richards                  | 48.1 ms                                                | 39.3 ms: 1.22x faster                                                     |
| scimark_sparse_mat_mult   | 5.03 ms                                                | 4.20 ms: 1.20x faster                                                     |
| richards_super            | 54.4 ms                                                | 45.5 ms: 1.20x faster                                                     |
| scimark_fft               | 369 ms                                                 | 309 ms: 1.19x faster                                                      |
| deepcopy_reduce           | 3.17 us                                                | 2.69 us: 1.18x faster                                                     |
| spectral_norm             | 115 ms                                                 | 101 ms: 1.14x faster                                                      |
| mako                      | 11.1 ms                                                | 9.81 ms: 1.13x faster                                                     |
| float                     | 78.5 ms                                                | 70.5 ms: 1.11x faster                                                     |
| tomli_loads               | 2.11 sec                                               | 1.90 sec: 1.11x faster                                                    |
| async_tree_none           | 354 ms                                                 | 327 ms: 1.08x faster                                                      |
| crypto_pyaes              | 73.0 ms                                                | 67.4 ms: 1.08x faster                                                     |
| async_tree_memoization    | 442 ms                                                 | 411 ms: 1.08x faster                                                      |
| nbody                     | 85.7 ms                                                | 79.8 ms: 1.07x faster                                                     |
| gc_traversal              | 3.81 ms                                                | 3.55 ms: 1.07x faster                                                     |
| async_tree_none_tg        | 320 ms                                                 | 301 ms: 1.06x faster                                                      |
| pathlib                   | 17.1 ms                                                | 16.1 ms: 1.06x faster                                                     |
| telco                     | 8.45 ms                                                | 7.99 ms: 1.06x faster                                                     |
| scimark_monte_carlo       | 66.3 ms                                                | 62.7 ms: 1.06x faster                                                     |
| xml_etree_parse           | 156 ms                                                 | 150 ms: 1.04x faster                                                      |
| fannkuch                  | 381 ms                                                 | 367 ms: 1.04x faster                                                      |
| logging_simple            | 5.66 us                                                | 5.47 us: 1.04x faster                                                     |
| logging_format            | 6.25 us                                                | 6.06 us: 1.03x faster                                                     |
| xml_etree_generate        | 87.0 ms                                                | 84.4 ms: 1.03x faster                                                     |
| xml_etree_iterparse       | 102 ms                                                 | 99.3 ms: 1.03x faster                                                     |
| pycparser                 | 1.19 sec                                               | 1.17 sec: 1.02x faster                                                    |
| async_tree_cpu_io_mixed   | 574 ms                                                 | 563 ms: 1.02x faster                                                      |
| json                      | 5.20 ms                                                | 5.11 ms: 1.02x faster                                                     |
| pyflate                   | 460 ms                                                 | 452 ms: 1.02x faster                                                      |
| pprint_safe_repr          | 744 ms                                                 | 735 ms: 1.01x faster                                                      |
| xml_etree_process         | 60.4 ms                                                | 59.8 ms: 1.01x faster                                                     |
| chaos                     | 58.4 ms                                                | 57.9 ms: 1.01x faster                                                     |
| python_startup            | 10.6 ms                                                | 10.5 ms: 1.01x faster                                                     |
| regex_effbot              | 3.88 ms                                                | 3.86 ms: 1.01x faster                                                     |
| mdp                       | 2.74 sec                                               | 2.73 sec: 1.00x faster                                                    |
| regex_v8                  | 25.3 ms                                                | 25.4 ms: 1.00x slower                                                     |
| json_dumps                | 10.4 ms                                                | 10.5 ms: 1.01x slower                                                     |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.81 sec: 1.01x slower                                                    |
| pidigits                  | 186 ms                                                 | 188 ms: 1.01x slower                                                      |
| bpe_tokeniser             | 4.69 sec                                               | 4.75 sec: 1.01x slower                                                    |
| meteor_contest            | 108 ms                                                 | 109 ms: 1.01x slower                                                      |
| python_startup_no_site    | 6.99 ms                                                | 7.08 ms: 1.01x slower                                                     |
| scimark_lu                | 115 ms                                                 | 117 ms: 1.01x slower                                                      |
| comprehensions            | 16.4 us                                                | 16.7 us: 1.02x slower                                                     |
| regex_dna                 | 220 ms                                                 | 224 ms: 1.02x slower                                                      |
| json_loads                | 27.0 us                                                | 27.6 us: 1.02x slower                                                     |
| asyncio_tcp               | 488 ms                                                 | 503 ms: 1.03x slower                                                      |
| async_tree_io_tg          | 825 ms                                                 | 850 ms: 1.03x slower                                                      |
| coroutines                | 22.5 ms                                                | 23.2 ms: 1.03x slower                                                     |
| regex_compile             | 131 ms                                                 | 135 ms: 1.03x slower                                                      |
| tornado_http              | 91.5 ms                                                | 95.1 ms: 1.04x slower                                                     |
| sqlglot_normalize         | 107 ms                                                 | 112 ms: 1.04x slower                                                      |
| go                        | 142 ms                                                 | 147 ms: 1.04x slower                                                      |
| pickle_pure_python        | 300 us                                                 | 313 us: 1.04x slower                                                      |
| generators                | 28.8 ms                                                | 30.2 ms: 1.05x slower                                                     |
| async_generators          | 433 ms                                                 | 456 ms: 1.05x slower                                                      |
| scimark_sor               | 122 ms                                                 | 129 ms: 1.06x slower                                                      |
| sqlglot_parse             | 1.27 ms                                                | 1.34 ms: 1.06x slower                                                     |
| dulwich_log               | 63.0 ms                                                | 67.3 ms: 1.07x slower                                                     |
| sqlglot_transpile         | 1.57 ms                                                | 1.68 ms: 1.07x slower                                                     |
| sympy_expand              | 462 ms                                                 | 497 ms: 1.08x slower                                                      |
| typing_runtime_protocols  | 159 us                                                 | 172 us: 1.08x slower                                                      |
| hexiom                    | 6.13 ms                                                | 6.67 ms: 1.09x slower                                                     |
| create_gc_cycles          | 1.61 ms                                                | 1.75 ms: 1.09x slower                                                     |
| dask                      | 338 ms                                                 | 369 ms: 1.09x slower                                                      |
| sqlglot_optimize          | 53.9 ms                                                | 58.9 ms: 1.09x slower                                                     |
| 2to3                      | 265 ms                                                 | 290 ms: 1.09x slower                                                      |
| sympy_str                 | 274 ms                                                 | 300 ms: 1.10x slower                                                      |
| sympy_sum                 | 150 ms                                                 | 166 ms: 1.11x slower                                                      |
| coverage                  | 83.7 ms                                                | 93.4 ms: 1.12x slower                                                     |
| django_template           | 34.4 ms                                                | 38.6 ms: 1.12x slower                                                     |
| nqueens                   | 80.6 ms                                                | 91.4 ms: 1.13x slower                                                     |
| bench_thread_pool         | 815 us                                                 | 958 us: 1.18x slower                                                      |
| html5lib                  | 64.5 ms                                                | 76.3 ms: 1.18x slower                                                     |
| sympy_integrate           | 19.9 ms                                                | 24.5 ms: 1.23x slower                                                     |
| pylint                    | 313 ms                                                 | 390 ms: 1.25x slower                                                      |
| deltablue                 | 3.15 ms                                                | 3.94 ms: 1.25x slower                                                     |
| genshi_xml                | 50.3 ms                                                | 75.1 ms: 1.49x slower                                                     |
| genshi_text               | 22.9 ms                                                | 34.1 ms: 1.49x slower                                                     |
| docutils                  | 2.58 sec                                               | 7.91 sec: 3.06x slower                                                    |
| raytrace                  | 262 ms                                                 | 5.99 sec: 22.92x slower                                                   |
| Geometric mean            | (ref)                                                  | 1.05x slower                                                              |

Benchmark hidden because not significant (8): async_tree_cpu_io_mixed_tg, unpickle_pure_python, thrift, bench_mp_pool, logging_silent, pprint_pformat, asyncio_websockets, async_tree_io
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 88.63% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.09x