# Results vs. 3.13.0

- fork: brandtbucher
- ref: no_progress_needed
- machine: linux-x86_64
- commit hash: 62e781e
- commit date: 2024-07-29
- overall geometric mean: 1.01x faster
- HPT reliability: 51.78%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240729-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-62e781e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 282 ms: 1.06x slower                                                      |
| docutils       | 2.58 sec                                               | 2.99 sec: 1.16x slower                                                    |
| html5lib       | 64.5 ms                                                | 67.3 ms: 1.04x slower                                                     |
| tornado_http   | 91.5 ms                                                | 92.8 ms: 1.01x slower                                                     |
| Geometric mean | (ref)                                                  | 1.07x slower                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240729-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-62e781e |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 465 ms                                                 | 393 ms: 1.18x faster                                                      |
| async_tree_none            | 354 ms                                                 | 325 ms: 1.09x faster                                                      |
| async_tree_none_tg         | 320 ms                                                 | 298 ms: 1.07x faster                                                      |
| async_tree_memoization     | 442 ms                                                 | 427 ms: 1.04x faster                                                      |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 527 ms: 1.03x faster                                                      |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 559 ms: 1.03x faster                                                      |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.01x slower                                                    |
| asyncio_tcp                | 488 ms                                                 | 506 ms: 1.04x slower                                                      |
| async_tree_io_tg           | 825 ms                                                 | 867 ms: 1.05x slower                                                      |
| async_generators           | 433 ms                                                 | 458 ms: 1.06x slower                                                      |
| async_tree_io              | 843 ms                                                 | 907 ms: 1.08x slower                                                      |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                              |

Benchmark hidden because not significant (2): asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240729-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-62e781e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 70.5 ms: 1.11x faster                                                     |
| nbody          | 85.7 ms                                                | 80.0 ms: 1.07x faster                                                     |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                      |
| Geometric mean | (ref)                                                  | 1.06x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240729-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-62e781e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.79 ms: 1.02x faster                                                     |
| regex_v8       | 25.3 ms                                                | 25.5 ms: 1.01x slower                                                     |
| regex_dna      | 220 ms                                                 | 229 ms: 1.04x slower                                                      |
| regex_compile  | 131 ms                                                 | 143 ms: 1.09x slower                                                      |
| Geometric mean | (ref)                                                  | 1.03x slower                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240729-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-62e781e |
|---------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads         | 2.11 sec                                               | 1.91 sec: 1.11x faster                                                    |
| xml_etree_generate  | 87.0 ms                                                | 79.8 ms: 1.09x faster                                                     |
| xml_etree_process   | 60.4 ms                                                | 56.2 ms: 1.07x faster                                                     |
| xml_etree_parse     | 156 ms                                                 | 146 ms: 1.07x faster                                                      |
| xml_etree_iterparse | 102 ms                                                 | 99.4 ms: 1.03x faster                                                     |
| json_dumps          | 10.4 ms                                                | 10.5 ms: 1.01x slower                                                     |
| pickle_pure_python  | 300 us                                                 | 303 us: 1.01x slower                                                      |
| json_loads          | 27.0 us                                                | 28.3 us: 1.05x slower                                                     |
| Geometric mean      | (ref)                                                  | 1.03x faster                                                              |

Benchmark hidden because not significant (1): unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240729-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-62e781e |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.5 ms: 1.01x faster                                                     |
| python_startup_no_site | 6.99 ms                                                | 7.11 ms: 1.02x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.00x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240729-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-62e781e |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.77 ms: 1.14x faster                                                     |
| django_template | 34.4 ms                                                | 35.6 ms: 1.03x slower                                                     |
| genshi_xml      | 50.3 ms                                                | 52.8 ms: 1.05x slower                                                     |
| genshi_text     | 22.9 ms                                                | 24.2 ms: 1.06x slower                                                     |
| Geometric mean  | (ref)                                                  | 1.00x slower                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240729-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-62e781e |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| deepcopy_memo              | 38.0 us                                                | 26.9 us: 1.42x faster                                                     |
| deepcopy                   | 352 us                                                 | 268 us: 1.32x faster                                                      |
| scimark_fft                | 369 ms                                                 | 304 ms: 1.21x faster                                                      |
| async_tree_memoization_tg  | 465 ms                                                 | 393 ms: 1.18x faster                                                      |
| deepcopy_reduce            | 3.17 us                                                | 2.68 us: 1.18x faster                                                     |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.27 ms: 1.18x faster                                                     |
| richards                   | 48.1 ms                                                | 42.3 ms: 1.14x faster                                                     |
| mako                       | 11.1 ms                                                | 9.77 ms: 1.14x faster                                                     |
| spectral_norm              | 115 ms                                                 | 102 ms: 1.13x faster                                                      |
| richards_super             | 54.4 ms                                                | 48.7 ms: 1.12x faster                                                     |
| float                      | 78.5 ms                                                | 70.5 ms: 1.11x faster                                                     |
| tomli_loads                | 2.11 sec                                               | 1.91 sec: 1.11x faster                                                    |
| crypto_pyaes               | 73.0 ms                                                | 65.9 ms: 1.11x faster                                                     |
| async_tree_none            | 354 ms                                                 | 325 ms: 1.09x faster                                                      |
| xml_etree_generate         | 87.0 ms                                                | 79.8 ms: 1.09x faster                                                     |
| telco                      | 8.45 ms                                                | 7.76 ms: 1.09x faster                                                     |
| xml_etree_process          | 60.4 ms                                                | 56.2 ms: 1.07x faster                                                     |
| async_tree_none_tg         | 320 ms                                                 | 298 ms: 1.07x faster                                                      |
| nbody                      | 85.7 ms                                                | 80.0 ms: 1.07x faster                                                     |
| xml_etree_parse            | 156 ms                                                 | 146 ms: 1.07x faster                                                      |
| gc_traversal               | 3.81 ms                                                | 3.56 ms: 1.07x faster                                                     |
| mdp                        | 2.74 sec                                               | 2.56 sec: 1.07x faster                                                    |
| scimark_monte_carlo        | 66.3 ms                                                | 62.3 ms: 1.06x faster                                                     |
| pathlib                    | 17.1 ms                                                | 16.0 ms: 1.06x faster                                                     |
| logging_format             | 6.25 us                                                | 5.96 us: 1.05x faster                                                     |
| logging_simple             | 5.66 us                                                | 5.43 us: 1.04x faster                                                     |
| pyflate                    | 460 ms                                                 | 440 ms: 1.04x faster                                                      |
| deltablue                  | 3.15 ms                                                | 3.02 ms: 1.04x faster                                                     |
| logging_silent             | 102 ns                                                 | 98.4 ns: 1.04x faster                                                     |
| async_tree_memoization     | 442 ms                                                 | 427 ms: 1.04x faster                                                      |
| bpe_tokeniser              | 4.69 sec                                               | 4.53 sec: 1.04x faster                                                    |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 527 ms: 1.03x faster                                                      |
| xml_etree_iterparse        | 102 ms                                                 | 99.4 ms: 1.03x faster                                                     |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 559 ms: 1.03x faster                                                      |
| regex_effbot               | 3.88 ms                                                | 3.79 ms: 1.02x faster                                                     |
| pprint_safe_repr           | 744 ms                                                 | 728 ms: 1.02x faster                                                      |
| fannkuch                   | 381 ms                                                 | 375 ms: 1.01x faster                                                      |
| json                       | 5.20 ms                                                | 5.13 ms: 1.01x faster                                                     |
| thrift                     | 796 us                                                 | 787 us: 1.01x faster                                                      |
| meteor_contest             | 108 ms                                                 | 106 ms: 1.01x faster                                                      |
| chaos                      | 58.4 ms                                                | 57.9 ms: 1.01x faster                                                     |
| python_startup             | 10.6 ms                                                | 10.5 ms: 1.01x faster                                                     |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                                      |
| bench_mp_pool              | 24.0 ms                                                | 24.0 ms: 1.00x slower                                                     |
| bench_thread_pool          | 815 us                                                 | 818 us: 1.00x slower                                                      |
| scimark_sor                | 122 ms                                                 | 123 ms: 1.01x slower                                                      |
| json_dumps                 | 10.4 ms                                                | 10.5 ms: 1.01x slower                                                     |
| regex_v8                   | 25.3 ms                                                | 25.5 ms: 1.01x slower                                                     |
| pickle_pure_python         | 300 us                                                 | 303 us: 1.01x slower                                                      |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.01x slower                                                    |
| tornado_http               | 91.5 ms                                                | 92.8 ms: 1.01x slower                                                     |
| pycparser                  | 1.19 sec                                               | 1.22 sec: 1.02x slower                                                    |
| python_startup_no_site     | 6.99 ms                                                | 7.11 ms: 1.02x slower                                                     |
| raytrace                   | 262 ms                                                 | 267 ms: 1.02x slower                                                      |
| comprehensions             | 16.4 us                                                | 16.7 us: 1.02x slower                                                     |
| scimark_lu                 | 115 ms                                                 | 118 ms: 1.02x slower                                                      |
| go                         | 142 ms                                                 | 146 ms: 1.03x slower                                                      |
| django_template            | 34.4 ms                                                | 35.6 ms: 1.03x slower                                                     |
| asyncio_tcp                | 488 ms                                                 | 506 ms: 1.04x slower                                                      |
| regex_dna                  | 220 ms                                                 | 229 ms: 1.04x slower                                                      |
| html5lib                   | 64.5 ms                                                | 67.3 ms: 1.04x slower                                                     |
| sqlglot_parse              | 1.27 ms                                                | 1.32 ms: 1.05x slower                                                     |
| typing_runtime_protocols   | 159 us                                                 | 167 us: 1.05x slower                                                      |
| json_loads                 | 27.0 us                                                | 28.3 us: 1.05x slower                                                     |
| genshi_xml                 | 50.3 ms                                                | 52.8 ms: 1.05x slower                                                     |
| async_tree_io_tg           | 825 ms                                                 | 867 ms: 1.05x slower                                                      |
| genshi_text                | 22.9 ms                                                | 24.2 ms: 1.06x slower                                                     |
| sqlglot_normalize          | 107 ms                                                 | 113 ms: 1.06x slower                                                      |
| async_generators           | 433 ms                                                 | 458 ms: 1.06x slower                                                      |
| nqueens                    | 80.6 ms                                                | 85.4 ms: 1.06x slower                                                     |
| 2to3                       | 265 ms                                                 | 282 ms: 1.06x slower                                                      |
| sqlglot_transpile          | 1.57 ms                                                | 1.68 ms: 1.07x slower                                                     |
| dask                       | 338 ms                                                 | 363 ms: 1.08x slower                                                      |
| async_tree_io              | 843 ms                                                 | 907 ms: 1.08x slower                                                      |
| create_gc_cycles           | 1.61 ms                                                | 1.74 ms: 1.08x slower                                                     |
| coverage                   | 83.7 ms                                                | 90.4 ms: 1.08x slower                                                     |
| sqlglot_optimize           | 53.9 ms                                                | 58.3 ms: 1.08x slower                                                     |
| regex_compile              | 131 ms                                                 | 143 ms: 1.09x slower                                                      |
| sympy_expand               | 462 ms                                                 | 511 ms: 1.11x slower                                                      |
| sympy_str                  | 274 ms                                                 | 306 ms: 1.12x slower                                                      |
| generators                 | 28.8 ms                                                | 32.8 ms: 1.14x slower                                                     |
| docutils                   | 2.58 sec                                               | 2.99 sec: 1.16x slower                                                    |
| sympy_integrate            | 19.9 ms                                                | 23.0 ms: 1.16x slower                                                     |
| pylint                     | 313 ms                                                 | 368 ms: 1.18x slower                                                      |
| sympy_sum                  | 150 ms                                                 | 176 ms: 1.18x slower                                                      |
| hexiom                     | 6.13 ms                                                | 7.68 ms: 1.25x slower                                                     |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                              |

Benchmark hidden because not significant (4): unpickle_pure_python, pprint_pformat, asyncio_websockets, coroutines
Ignored benchmarks (14) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 51.78% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.09x