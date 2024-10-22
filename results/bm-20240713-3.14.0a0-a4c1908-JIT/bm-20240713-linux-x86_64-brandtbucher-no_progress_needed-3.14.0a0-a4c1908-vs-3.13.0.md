# Results vs. 3.13.0

- fork: brandtbucher
- ref: no_progress_needed
- machine: linux-x86_64
- commit hash: a4c1908
- commit date: 2024-07-13
- overall geometric mean: 1.01x faster
- HPT reliability: 71.63%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-a4c1908 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 275 ms: 1.04x slower                                                      |
| docutils       | 2.58 sec                                               | 2.92 sec: 1.13x slower                                                    |
| html5lib       | 64.5 ms                                                | 63.6 ms: 1.01x faster                                                     |
| tornado_http   | 91.5 ms                                                | 92.2 ms: 1.01x slower                                                     |
| Geometric mean | (ref)                                                  | 1.04x slower                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-a4c1908 |
|---------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization_tg | 465 ms                                                 | 379 ms: 1.23x faster                                                      |
| async_tree_none           | 354 ms                                                 | 327 ms: 1.08x faster                                                      |
| async_tree_memoization    | 442 ms                                                 | 411 ms: 1.08x faster                                                      |
| async_tree_none_tg        | 320 ms                                                 | 301 ms: 1.06x faster                                                      |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.81 sec: 1.01x slower                                                    |
| async_tree_io_tg          | 825 ms                                                 | 846 ms: 1.02x slower                                                      |
| coroutines                | 22.5 ms                                                | 23.3 ms: 1.03x slower                                                     |
| asyncio_tcp               | 488 ms                                                 | 507 ms: 1.04x slower                                                      |
| async_generators          | 433 ms                                                 | 452 ms: 1.04x slower                                                      |
| Geometric mean            | (ref)                                                  | 1.02x faster                                                              |

Benchmark hidden because not significant (4): async_tree_cpu_io_mixed, asyncio_websockets, async_tree_cpu_io_mixed_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-a4c1908 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 69.5 ms: 1.13x faster                                                     |
| nbody          | 85.7 ms                                                | 80.5 ms: 1.06x faster                                                     |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                      |
| Geometric mean | (ref)                                                  | 1.06x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-a4c1908 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.75 ms: 1.04x faster                                                     |
| regex_v8       | 25.3 ms                                                | 25.4 ms: 1.00x slower                                                     |
| regex_dna      | 220 ms                                                 | 228 ms: 1.04x slower                                                      |
| regex_compile  | 131 ms                                                 | 137 ms: 1.05x slower                                                      |
| Geometric mean | (ref)                                                  | 1.01x slower                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-a4c1908 |
|---------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads         | 2.11 sec                                               | 1.87 sec: 1.13x faster                                                    |
| xml_etree_generate  | 87.0 ms                                                | 81.9 ms: 1.06x faster                                                     |
| xml_etree_parse     | 156 ms                                                 | 148 ms: 1.06x faster                                                      |
| xml_etree_process   | 60.4 ms                                                | 57.6 ms: 1.05x faster                                                     |
| xml_etree_iterparse | 102 ms                                                 | 98.4 ms: 1.04x faster                                                     |
| json_loads          | 27.0 us                                                | 27.6 us: 1.02x slower                                                     |
| pickle_pure_python  | 300 us                                                 | 308 us: 1.03x slower                                                      |
| Geometric mean      | (ref)                                                  | 1.03x faster                                                              |

Benchmark hidden because not significant (2): json_dumps, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-a4c1908 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.5 ms: 1.00x faster                                                     |
| python_startup_no_site | 6.99 ms                                                | 7.13 ms: 1.02x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-a4c1908 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 10.0 ms: 1.11x faster                                                     |
| django_template | 34.4 ms                                                | 34.9 ms: 1.01x slower                                                     |
| genshi_text     | 22.9 ms                                                | 25.9 ms: 1.13x slower                                                     |
| genshi_xml      | 50.3 ms                                                | 58.7 ms: 1.17x slower                                                     |
| Geometric mean  | (ref)                                                  | 1.05x slower                                                              |

All benchmarks:
===============

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-a4c1908 |
|---------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| deepcopy_memo             | 38.0 us                                                | 27.1 us: 1.40x faster                                                     |
| richards                  | 48.1 ms                                                | 35.9 ms: 1.34x faster                                                     |
| richards_super            | 54.4 ms                                                | 40.8 ms: 1.33x faster                                                     |
| deepcopy                  | 352 us                                                 | 265 us: 1.33x faster                                                      |
| async_tree_memoization_tg | 465 ms                                                 | 379 ms: 1.23x faster                                                      |
| scimark_fft               | 369 ms                                                 | 311 ms: 1.19x faster                                                      |
| deepcopy_reduce           | 3.17 us                                                | 2.68 us: 1.18x faster                                                     |
| scimark_sparse_mat_mult   | 5.03 ms                                                | 4.31 ms: 1.17x faster                                                     |
| float                     | 78.5 ms                                                | 69.5 ms: 1.13x faster                                                     |
| tomli_loads               | 2.11 sec                                               | 1.87 sec: 1.13x faster                                                    |
| spectral_norm             | 115 ms                                                 | 104 ms: 1.11x faster                                                      |
| mako                      | 11.1 ms                                                | 10.0 ms: 1.11x faster                                                     |
| crypto_pyaes              | 73.0 ms                                                | 66.6 ms: 1.10x faster                                                     |
| async_tree_none           | 354 ms                                                 | 327 ms: 1.08x faster                                                      |
| mdp                       | 2.74 sec                                               | 2.54 sec: 1.08x faster                                                    |
| async_tree_memoization    | 442 ms                                                 | 411 ms: 1.08x faster                                                      |
| telco                     | 8.45 ms                                                | 7.88 ms: 1.07x faster                                                     |
| nbody                     | 85.7 ms                                                | 80.5 ms: 1.06x faster                                                     |
| async_tree_none_tg        | 320 ms                                                 | 301 ms: 1.06x faster                                                      |
| pathlib                   | 17.1 ms                                                | 16.0 ms: 1.06x faster                                                     |
| scimark_monte_carlo       | 66.3 ms                                                | 62.4 ms: 1.06x faster                                                     |
| xml_etree_generate        | 87.0 ms                                                | 81.9 ms: 1.06x faster                                                     |
| fannkuch                  | 381 ms                                                 | 359 ms: 1.06x faster                                                      |
| xml_etree_parse           | 156 ms                                                 | 148 ms: 1.06x faster                                                      |
| pyflate                   | 460 ms                                                 | 437 ms: 1.05x faster                                                      |
| xml_etree_process         | 60.4 ms                                                | 57.6 ms: 1.05x faster                                                     |
| logging_simple            | 5.66 us                                                | 5.45 us: 1.04x faster                                                     |
| xml_etree_iterparse       | 102 ms                                                 | 98.4 ms: 1.04x faster                                                     |
| regex_effbot              | 3.88 ms                                                | 3.75 ms: 1.04x faster                                                     |
| logging_format            | 6.25 us                                                | 6.04 us: 1.04x faster                                                     |
| html5lib                  | 64.5 ms                                                | 63.6 ms: 1.01x faster                                                     |
| chaos                     | 58.4 ms                                                | 57.8 ms: 1.01x faster                                                     |
| meteor_contest            | 108 ms                                                 | 107 ms: 1.01x faster                                                      |
| python_startup            | 10.6 ms                                                | 10.5 ms: 1.00x faster                                                     |
| pidigits                  | 186 ms                                                 | 186 ms: 1.00x faster                                                      |
| regex_v8                  | 25.3 ms                                                | 25.4 ms: 1.00x slower                                                     |
| bpe_tokeniser             | 4.69 sec                                               | 4.72 sec: 1.01x slower                                                    |
| tornado_http              | 91.5 ms                                                | 92.2 ms: 1.01x slower                                                     |
| pprint_pformat            | 1.51 sec                                               | 1.53 sec: 1.01x slower                                                    |
| gc_traversal              | 3.81 ms                                                | 3.85 ms: 1.01x slower                                                     |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.81 sec: 1.01x slower                                                    |
| django_template           | 34.4 ms                                                | 34.9 ms: 1.01x slower                                                     |
| bench_thread_pool         | 815 us                                                 | 827 us: 1.01x slower                                                      |
| thrift                    | 796 us                                                 | 812 us: 1.02x slower                                                      |
| comprehensions            | 16.4 us                                                | 16.7 us: 1.02x slower                                                     |
| sqlglot_parse             | 1.27 ms                                                | 1.29 ms: 1.02x slower                                                     |
| python_startup_no_site    | 6.99 ms                                                | 7.13 ms: 1.02x slower                                                     |
| json_loads                | 27.0 us                                                | 27.6 us: 1.02x slower                                                     |
| go                        | 142 ms                                                 | 145 ms: 1.02x slower                                                      |
| async_tree_io_tg          | 825 ms                                                 | 846 ms: 1.02x slower                                                      |
| pickle_pure_python        | 300 us                                                 | 308 us: 1.03x slower                                                      |
| scimark_lu                | 115 ms                                                 | 119 ms: 1.03x slower                                                      |
| coroutines                | 22.5 ms                                                | 23.3 ms: 1.03x slower                                                     |
| generators                | 28.8 ms                                                | 29.8 ms: 1.03x slower                                                     |
| dulwich_log               | 63.0 ms                                                | 65.2 ms: 1.04x slower                                                     |
| asyncio_tcp               | 488 ms                                                 | 507 ms: 1.04x slower                                                      |
| regex_dna                 | 220 ms                                                 | 228 ms: 1.04x slower                                                      |
| 2to3                      | 265 ms                                                 | 275 ms: 1.04x slower                                                      |
| sqlglot_normalize         | 107 ms                                                 | 112 ms: 1.04x slower                                                      |
| sqlglot_transpile         | 1.57 ms                                                | 1.64 ms: 1.04x slower                                                     |
| sqlglot_optimize          | 53.9 ms                                                | 56.2 ms: 1.04x slower                                                     |
| raytrace                  | 262 ms                                                 | 273 ms: 1.04x slower                                                      |
| async_generators          | 433 ms                                                 | 452 ms: 1.04x slower                                                      |
| scimark_sor               | 122 ms                                                 | 128 ms: 1.05x slower                                                      |
| regex_compile             | 131 ms                                                 | 137 ms: 1.05x slower                                                      |
| sympy_str                 | 274 ms                                                 | 289 ms: 1.06x slower                                                      |
| typing_runtime_protocols  | 159 us                                                 | 169 us: 1.06x slower                                                      |
| dask                      | 338 ms                                                 | 361 ms: 1.07x slower                                                      |
| sympy_expand              | 462 ms                                                 | 494 ms: 1.07x slower                                                      |
| nqueens                   | 80.6 ms                                                | 86.5 ms: 1.07x slower                                                     |
| sympy_integrate           | 19.9 ms                                                | 21.7 ms: 1.09x slower                                                     |
| deltablue                 | 3.15 ms                                                | 3.45 ms: 1.10x slower                                                     |
| hexiom                    | 6.13 ms                                                | 6.73 ms: 1.10x slower                                                     |
| coverage                  | 83.7 ms                                                | 92.2 ms: 1.10x slower                                                     |
| create_gc_cycles          | 1.61 ms                                                | 1.78 ms: 1.10x slower                                                     |
| sympy_sum                 | 150 ms                                                 | 166 ms: 1.11x slower                                                      |
| pylint                    | 313 ms                                                 | 351 ms: 1.12x slower                                                      |
| docutils                  | 2.58 sec                                               | 2.92 sec: 1.13x slower                                                    |
| genshi_text               | 22.9 ms                                                | 25.9 ms: 1.13x slower                                                     |
| genshi_xml                | 50.3 ms                                                | 58.7 ms: 1.17x slower                                                     |
| Geometric mean            | (ref)                                                  | 1.01x faster                                                              |

Benchmark hidden because not significant (11): async_tree_cpu_io_mixed, logging_silent, pprint_safe_repr, json, json_dumps, pycparser, asyncio_websockets, bench_mp_pool, unpickle_pure_python, async_tree_cpu_io_mixed_tg, async_tree_io
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 71.63% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.07x