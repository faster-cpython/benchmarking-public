# Results vs. 3.13.0

- fork: brandtbucher
- ref: no_progress_needed
- machine: linux-x86_64
- commit hash: 639e7c2
- commit date: 2024-07-16
- overall geometric mean: 1.02x faster
- HPT reliability: 54.80%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240716-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-639e7c2 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 276 ms: 1.04x slower                                                      |
| docutils       | 2.58 sec                                               | 2.92 sec: 1.13x slower                                                    |
| html5lib       | 64.5 ms                                                | 66.4 ms: 1.03x slower                                                     |
| tornado_http   | 91.5 ms                                                | 92.2 ms: 1.01x slower                                                     |
| Geometric mean | (ref)                                                  | 1.05x slower                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240716-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-639e7c2 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 465 ms                                                 | 375 ms: 1.24x faster                                                      |
| async_tree_none            | 354 ms                                                 | 323 ms: 1.10x faster                                                      |
| async_tree_memoization     | 442 ms                                                 | 406 ms: 1.09x faster                                                      |
| async_tree_none_tg         | 320 ms                                                 | 299 ms: 1.07x faster                                                      |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 559 ms: 1.03x faster                                                      |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 536 ms: 1.01x faster                                                      |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.80 sec: 1.01x slower                                                    |
| coroutines                 | 22.5 ms                                                | 22.7 ms: 1.01x slower                                                     |
| asyncio_tcp                | 488 ms                                                 | 503 ms: 1.03x slower                                                      |
| async_generators           | 433 ms                                                 | 458 ms: 1.06x slower                                                      |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                              |

Benchmark hidden because not significant (3): async_tree_io, asyncio_websockets, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240716-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-639e7c2 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 69.9 ms: 1.12x faster                                                     |
| nbody          | 85.7 ms                                                | 80.8 ms: 1.06x faster                                                     |
| Geometric mean | (ref)                                                  | 1.06x faster                                                              |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240716-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-639e7c2 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.64 ms: 1.07x faster                                                     |
| regex_v8       | 25.3 ms                                                | 23.9 ms: 1.06x faster                                                     |
| regex_dna      | 220 ms                                                 | 230 ms: 1.05x slower                                                      |
| regex_compile  | 131 ms                                                 | 138 ms: 1.05x slower                                                      |
| Geometric mean | (ref)                                                  | 1.01x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240716-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-639e7c2 |
|---------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads         | 2.11 sec                                               | 1.90 sec: 1.11x faster                                                    |
| xml_etree_generate  | 87.0 ms                                                | 81.0 ms: 1.07x faster                                                     |
| xml_etree_process   | 60.4 ms                                                | 57.2 ms: 1.06x faster                                                     |
| xml_etree_parse     | 156 ms                                                 | 150 ms: 1.04x faster                                                      |
| xml_etree_iterparse | 102 ms                                                 | 99.1 ms: 1.03x faster                                                     |
| json_loads          | 27.0 us                                                | 27.8 us: 1.03x slower                                                     |
| Geometric mean      | (ref)                                                  | 1.03x faster                                                              |

Benchmark hidden because not significant (3): json_dumps, unpickle_pure_python, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240716-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-639e7c2 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.6 ms: 1.00x faster                                                     |
| python_startup_no_site | 6.99 ms                                                | 7.15 ms: 1.02x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240716-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-639e7c2 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.73 ms: 1.14x faster                                                     |
| django_template | 34.4 ms                                                | 35.1 ms: 1.02x slower                                                     |
| genshi_text     | 22.9 ms                                                | 25.1 ms: 1.10x slower                                                     |
| genshi_xml      | 50.3 ms                                                | 57.3 ms: 1.14x slower                                                     |
| Geometric mean  | (ref)                                                  | 1.03x slower                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240716-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-639e7c2 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| deepcopy_memo              | 38.0 us                                                | 27.3 us: 1.39x faster                                                     |
| richards                   | 48.1 ms                                                | 35.7 ms: 1.35x faster                                                     |
| deepcopy                   | 352 us                                                 | 263 us: 1.34x faster                                                      |
| richards_super             | 54.4 ms                                                | 40.9 ms: 1.33x faster                                                     |
| async_tree_memoization_tg  | 465 ms                                                 | 375 ms: 1.24x faster                                                      |
| deepcopy_reduce            | 3.17 us                                                | 2.63 us: 1.20x faster                                                     |
| scimark_fft                | 369 ms                                                 | 309 ms: 1.19x faster                                                      |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.29 ms: 1.17x faster                                                     |
| mako                       | 11.1 ms                                                | 9.73 ms: 1.14x faster                                                     |
| spectral_norm              | 115 ms                                                 | 102 ms: 1.12x faster                                                      |
| float                      | 78.5 ms                                                | 69.9 ms: 1.12x faster                                                     |
| tomli_loads                | 2.11 sec                                               | 1.90 sec: 1.11x faster                                                    |
| async_tree_none            | 354 ms                                                 | 323 ms: 1.10x faster                                                      |
| async_tree_memoization     | 442 ms                                                 | 406 ms: 1.09x faster                                                      |
| crypto_pyaes               | 73.0 ms                                                | 67.3 ms: 1.08x faster                                                     |
| xml_etree_generate         | 87.0 ms                                                | 81.0 ms: 1.07x faster                                                     |
| gc_traversal               | 3.81 ms                                                | 3.55 ms: 1.07x faster                                                     |
| async_tree_none_tg         | 320 ms                                                 | 299 ms: 1.07x faster                                                      |
| regex_effbot               | 3.88 ms                                                | 3.64 ms: 1.07x faster                                                     |
| nbody                      | 85.7 ms                                                | 80.8 ms: 1.06x faster                                                     |
| regex_v8                   | 25.3 ms                                                | 23.9 ms: 1.06x faster                                                     |
| pathlib                    | 17.1 ms                                                | 16.1 ms: 1.06x faster                                                     |
| xml_etree_process          | 60.4 ms                                                | 57.2 ms: 1.06x faster                                                     |
| telco                      | 8.45 ms                                                | 8.03 ms: 1.05x faster                                                     |
| scimark_monte_carlo        | 66.3 ms                                                | 63.0 ms: 1.05x faster                                                     |
| pycparser                  | 1.19 sec                                               | 1.14 sec: 1.05x faster                                                    |
| fannkuch                   | 381 ms                                                 | 364 ms: 1.05x faster                                                      |
| xml_etree_parse            | 156 ms                                                 | 150 ms: 1.04x faster                                                      |
| xml_etree_iterparse        | 102 ms                                                 | 99.1 ms: 1.03x faster                                                     |
| logging_simple             | 5.66 us                                                | 5.51 us: 1.03x faster                                                     |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 559 ms: 1.03x faster                                                      |
| logging_format             | 6.25 us                                                | 6.10 us: 1.03x faster                                                     |
| pyflate                    | 460 ms                                                 | 454 ms: 1.01x faster                                                      |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 536 ms: 1.01x faster                                                      |
| pprint_safe_repr           | 744 ms                                                 | 735 ms: 1.01x faster                                                      |
| json                       | 5.20 ms                                                | 5.13 ms: 1.01x faster                                                     |
| chaos                      | 58.4 ms                                                | 57.7 ms: 1.01x faster                                                     |
| python_startup             | 10.6 ms                                                | 10.6 ms: 1.00x faster                                                     |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.80 sec: 1.01x slower                                                    |
| coroutines                 | 22.5 ms                                                | 22.7 ms: 1.01x slower                                                     |
| tornado_http               | 91.5 ms                                                | 92.2 ms: 1.01x slower                                                     |
| mdp                        | 2.74 sec                                               | 2.77 sec: 1.01x slower                                                    |
| bench_thread_pool          | 815 us                                                 | 825 us: 1.01x slower                                                      |
| bpe_tokeniser              | 4.69 sec                                               | 4.76 sec: 1.01x slower                                                    |
| meteor_contest             | 108 ms                                                 | 109 ms: 1.02x slower                                                      |
| go                         | 142 ms                                                 | 144 ms: 1.02x slower                                                      |
| scimark_lu                 | 115 ms                                                 | 117 ms: 1.02x slower                                                      |
| sqlglot_parse              | 1.27 ms                                                | 1.29 ms: 1.02x slower                                                     |
| django_template            | 34.4 ms                                                | 35.1 ms: 1.02x slower                                                     |
| comprehensions             | 16.4 us                                                | 16.7 us: 1.02x slower                                                     |
| logging_silent             | 102 ns                                                 | 104 ns: 1.02x slower                                                      |
| python_startup_no_site     | 6.99 ms                                                | 7.15 ms: 1.02x slower                                                     |
| scimark_sor                | 122 ms                                                 | 126 ms: 1.03x slower                                                      |
| generators                 | 28.8 ms                                                | 29.6 ms: 1.03x slower                                                     |
| html5lib                   | 64.5 ms                                                | 66.4 ms: 1.03x slower                                                     |
| asyncio_tcp                | 488 ms                                                 | 503 ms: 1.03x slower                                                      |
| raytrace                   | 262 ms                                                 | 269 ms: 1.03x slower                                                      |
| json_loads                 | 27.0 us                                                | 27.8 us: 1.03x slower                                                     |
| sqlglot_normalize          | 107 ms                                                 | 111 ms: 1.04x slower                                                      |
| sqlglot_transpile          | 1.57 ms                                                | 1.64 ms: 1.04x slower                                                     |
| 2to3                       | 265 ms                                                 | 276 ms: 1.04x slower                                                      |
| dulwich_log                | 63.0 ms                                                | 65.9 ms: 1.05x slower                                                     |
| regex_dna                  | 220 ms                                                 | 230 ms: 1.05x slower                                                      |
| sqlglot_optimize           | 53.9 ms                                                | 56.8 ms: 1.05x slower                                                     |
| regex_compile              | 131 ms                                                 | 138 ms: 1.05x slower                                                      |
| sympy_str                  | 274 ms                                                 | 289 ms: 1.06x slower                                                      |
| async_generators           | 433 ms                                                 | 458 ms: 1.06x slower                                                      |
| dask                       | 338 ms                                                 | 359 ms: 1.06x slower                                                      |
| typing_runtime_protocols   | 159 us                                                 | 170 us: 1.07x slower                                                      |
| sympy_expand               | 462 ms                                                 | 495 ms: 1.07x slower                                                      |
| nqueens                    | 80.6 ms                                                | 86.8 ms: 1.08x slower                                                     |
| create_gc_cycles           | 1.61 ms                                                | 1.74 ms: 1.08x slower                                                     |
| deltablue                  | 3.15 ms                                                | 3.43 ms: 1.09x slower                                                     |
| sympy_integrate            | 19.9 ms                                                | 21.8 ms: 1.10x slower                                                     |
| genshi_text                | 22.9 ms                                                | 25.1 ms: 1.10x slower                                                     |
| hexiom                     | 6.13 ms                                                | 6.77 ms: 1.10x slower                                                     |
| sympy_sum                  | 150 ms                                                 | 166 ms: 1.11x slower                                                      |
| pylint                     | 313 ms                                                 | 352 ms: 1.13x slower                                                      |
| docutils                   | 2.58 sec                                               | 2.92 sec: 1.13x slower                                                    |
| coverage                   | 83.7 ms                                                | 94.8 ms: 1.13x slower                                                     |
| genshi_xml                 | 50.3 ms                                                | 57.3 ms: 1.14x slower                                                     |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                              |

Benchmark hidden because not significant (10): async_tree_io, json_dumps, pidigits, bench_mp_pool, unpickle_pure_python, thrift, asyncio_websockets, pickle_pure_python, pprint_pformat, async_tree_io_tg
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 54.80% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.07x