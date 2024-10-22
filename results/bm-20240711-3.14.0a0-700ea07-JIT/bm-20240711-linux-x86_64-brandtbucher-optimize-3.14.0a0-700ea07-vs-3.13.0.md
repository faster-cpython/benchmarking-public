# Results vs. 3.13.0

- fork: brandtbucher
- ref: optimize
- machine: linux-x86_64
- commit hash: 700ea07
- commit date: 2024-07-11
- overall geometric mean: 1.02x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240711-linux-x86_64-brandtbucher-optimize-3.14.0a0-700ea07 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 270 ms: 1.02x slower                                            |
| docutils       | 2.58 sec                                               | 2.96 sec: 1.15x slower                                          |
| html5lib       | 64.5 ms                                                | 67.9 ms: 1.05x slower                                           |
| tornado_http   | 91.5 ms                                                | 91.9 ms: 1.00x slower                                           |
| Geometric mean | (ref)                                                  | 1.05x slower                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240711-linux-x86_64-brandtbucher-optimize-3.14.0a0-700ea07 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_memoization_tg  | 465 ms                                                 | 383 ms: 1.21x faster                                            |
| async_tree_memoization     | 442 ms                                                 | 411 ms: 1.08x faster                                            |
| async_tree_none            | 354 ms                                                 | 329 ms: 1.08x faster                                            |
| async_tree_none_tg         | 320 ms                                                 | 307 ms: 1.04x faster                                            |
| asyncio_tcp                | 488 ms                                                 | 490 ms: 1.00x slower                                            |
| asyncio_websockets         | 555 ms                                                 | 558 ms: 1.00x slower                                            |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.80 sec: 1.01x slower                                          |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 549 ms: 1.01x slower                                            |
| async_tree_io_tg           | 825 ms                                                 | 859 ms: 1.04x slower                                            |
| async_generators           | 433 ms                                                 | 461 ms: 1.06x slower                                            |
| coroutines                 | 22.5 ms                                                | 24.0 ms: 1.07x slower                                           |
| async_tree_io              | 843 ms                                                 | 909 ms: 1.08x slower                                            |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                    |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240711-linux-x86_64-brandtbucher-optimize-3.14.0a0-700ea07 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| pidigits       | 186 ms                                                 | 187 ms: 1.00x slower                                            |
| nbody          | 85.7 ms                                                | 92.2 ms: 1.08x slower                                           |
| Geometric mean | (ref)                                                  | 1.03x slower                                                    |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240711-linux-x86_64-brandtbucher-optimize-3.14.0a0-700ea07 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.64 ms: 1.07x faster                                           |
| regex_v8       | 25.3 ms                                                | 24.1 ms: 1.05x faster                                           |
| regex_compile  | 131 ms                                                 | 135 ms: 1.03x slower                                            |
| regex_dna      | 220 ms                                                 | 228 ms: 1.04x slower                                            |
| Geometric mean | (ref)                                                  | 1.01x faster                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240711-linux-x86_64-brandtbucher-optimize-3.14.0a0-700ea07 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| pickle_pure_python   | 300 us                                                 | 304 us: 1.01x slower                                            |
| xml_etree_parse      | 156 ms                                                 | 159 ms: 1.02x slower                                            |
| json_loads           | 27.0 us                                                | 27.6 us: 1.02x slower                                           |
| unpickle_pure_python | 213 us                                                 | 220 us: 1.03x slower                                            |
| tomli_loads          | 2.11 sec                                               | 2.24 sec: 1.06x slower                                          |
| xml_etree_iterparse  | 102 ms                                                 | 108 ms: 1.06x slower                                            |
| Geometric mean       | (ref)                                                  | 1.02x slower                                                    |

Benchmark hidden because not significant (3): json_dumps, xml_etree_generate, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240711-linux-x86_64-brandtbucher-optimize-3.14.0a0-700ea07 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.5 ms: 1.00x faster                                           |
| python_startup_no_site | 6.99 ms                                                | 7.06 ms: 1.01x slower                                           |
| Geometric mean         | (ref)                                                  | 1.00x slower                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240711-linux-x86_64-brandtbucher-optimize-3.14.0a0-700ea07 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| mako           | 11.1 ms                                                | 11.5 ms: 1.03x slower                                           |
| genshi_text    | 22.9 ms                                                | 25.7 ms: 1.12x slower                                           |
| genshi_xml     | 50.3 ms                                                | 57.1 ms: 1.13x slower                                           |
| Geometric mean | (ref)                                                  | 1.07x slower                                                    |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240711-linux-x86_64-brandtbucher-optimize-3.14.0a0-700ea07 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| deepcopy                   | 352 us                                                 | 269 us: 1.31x faster                                            |
| deepcopy_memo              | 38.0 us                                                | 31.1 us: 1.22x faster                                           |
| async_tree_memoization_tg  | 465 ms                                                 | 383 ms: 1.21x faster                                            |
| deepcopy_reduce            | 3.17 us                                                | 2.65 us: 1.19x faster                                           |
| async_tree_memoization     | 442 ms                                                 | 411 ms: 1.08x faster                                            |
| async_tree_none            | 354 ms                                                 | 329 ms: 1.08x faster                                            |
| pathlib                    | 17.1 ms                                                | 16.0 ms: 1.07x faster                                           |
| regex_effbot               | 3.88 ms                                                | 3.64 ms: 1.07x faster                                           |
| regex_v8                   | 25.3 ms                                                | 24.1 ms: 1.05x faster                                           |
| async_tree_none_tg         | 320 ms                                                 | 307 ms: 1.04x faster                                            |
| logging_simple             | 5.66 us                                                | 5.46 us: 1.04x faster                                           |
| logging_format             | 6.25 us                                                | 6.06 us: 1.03x faster                                           |
| richards                   | 48.1 ms                                                | 47.0 ms: 1.02x faster                                           |
| gc_traversal               | 3.81 ms                                                | 3.73 ms: 1.02x faster                                           |
| telco                      | 8.45 ms                                                | 8.30 ms: 1.02x faster                                           |
| richards_super             | 54.4 ms                                                | 53.5 ms: 1.02x faster                                           |
| spectral_norm              | 115 ms                                                 | 113 ms: 1.02x faster                                            |
| pycparser                  | 1.19 sec                                               | 1.18 sec: 1.01x faster                                          |
| thrift                     | 796 us                                                 | 791 us: 1.01x faster                                            |
| python_startup             | 10.6 ms                                                | 10.5 ms: 1.00x faster                                           |
| pidigits                   | 186 ms                                                 | 187 ms: 1.00x slower                                            |
| asyncio_tcp                | 488 ms                                                 | 490 ms: 1.00x slower                                            |
| tornado_http               | 91.5 ms                                                | 91.9 ms: 1.00x slower                                           |
| asyncio_websockets         | 555 ms                                                 | 558 ms: 1.00x slower                                            |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.80 sec: 1.01x slower                                          |
| scimark_lu                 | 115 ms                                                 | 116 ms: 1.01x slower                                            |
| bench_thread_pool          | 815 us                                                 | 821 us: 1.01x slower                                            |
| pprint_pformat             | 1.51 sec                                               | 1.52 sec: 1.01x slower                                          |
| mdp                        | 2.74 sec                                               | 2.77 sec: 1.01x slower                                          |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 549 ms: 1.01x slower                                            |
| sympy_expand               | 462 ms                                                 | 466 ms: 1.01x slower                                            |
| python_startup_no_site     | 6.99 ms                                                | 7.06 ms: 1.01x slower                                           |
| pickle_pure_python         | 300 us                                                 | 304 us: 1.01x slower                                            |
| raytrace                   | 262 ms                                                 | 265 ms: 1.01x slower                                            |
| xml_etree_parse            | 156 ms                                                 | 159 ms: 1.02x slower                                            |
| 2to3                       | 265 ms                                                 | 270 ms: 1.02x slower                                            |
| scimark_sor                | 122 ms                                                 | 125 ms: 1.02x slower                                            |
| go                         | 142 ms                                                 | 145 ms: 1.02x slower                                            |
| sympy_str                  | 274 ms                                                 | 280 ms: 1.02x slower                                            |
| json_loads                 | 27.0 us                                                | 27.6 us: 1.02x slower                                           |
| regex_compile              | 131 ms                                                 | 135 ms: 1.03x slower                                            |
| sqlglot_normalize          | 107 ms                                                 | 110 ms: 1.03x slower                                            |
| sqlglot_transpile          | 1.57 ms                                                | 1.62 ms: 1.03x slower                                           |
| sqlglot_parse              | 1.27 ms                                                | 1.30 ms: 1.03x slower                                           |
| unpickle_pure_python       | 213 us                                                 | 220 us: 1.03x slower                                            |
| chaos                      | 58.4 ms                                                | 60.2 ms: 1.03x slower                                           |
| meteor_contest             | 108 ms                                                 | 111 ms: 1.03x slower                                            |
| dulwich_log                | 63.0 ms                                                | 64.9 ms: 1.03x slower                                           |
| mako                       | 11.1 ms                                                | 11.5 ms: 1.03x slower                                           |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 5.20 ms: 1.03x slower                                           |
| logging_silent             | 102 ns                                                 | 106 ns: 1.03x slower                                            |
| typing_runtime_protocols   | 159 us                                                 | 165 us: 1.04x slower                                            |
| regex_dna                  | 220 ms                                                 | 228 ms: 1.04x slower                                            |
| bpe_tokeniser              | 4.69 sec                                               | 4.87 sec: 1.04x slower                                          |
| async_tree_io_tg           | 825 ms                                                 | 859 ms: 1.04x slower                                            |
| deltablue                  | 3.15 ms                                                | 3.28 ms: 1.04x slower                                           |
| sympy_integrate            | 19.9 ms                                                | 20.8 ms: 1.05x slower                                           |
| scimark_monte_carlo        | 66.3 ms                                                | 69.4 ms: 1.05x slower                                           |
| sympy_sum                  | 150 ms                                                 | 157 ms: 1.05x slower                                            |
| html5lib                   | 64.5 ms                                                | 67.9 ms: 1.05x slower                                           |
| pyflate                    | 460 ms                                                 | 485 ms: 1.06x slower                                            |
| tomli_loads                | 2.11 sec                                               | 2.24 sec: 1.06x slower                                          |
| xml_etree_iterparse        | 102 ms                                                 | 108 ms: 1.06x slower                                            |
| async_generators           | 433 ms                                                 | 461 ms: 1.06x slower                                            |
| coroutines                 | 22.5 ms                                                | 24.0 ms: 1.07x slower                                           |
| dask                       | 338 ms                                                 | 361 ms: 1.07x slower                                            |
| nbody                      | 85.7 ms                                                | 92.2 ms: 1.08x slower                                           |
| sqlglot_optimize           | 53.9 ms                                                | 58.0 ms: 1.08x slower                                           |
| async_tree_io              | 843 ms                                                 | 909 ms: 1.08x slower                                            |
| create_gc_cycles           | 1.61 ms                                                | 1.74 ms: 1.08x slower                                           |
| fannkuch                   | 381 ms                                                 | 414 ms: 1.09x slower                                            |
| comprehensions             | 16.4 us                                                | 18.0 us: 1.10x slower                                           |
| coverage                   | 83.7 ms                                                | 92.7 ms: 1.11x slower                                           |
| pylint                     | 313 ms                                                 | 347 ms: 1.11x slower                                            |
| nqueens                    | 80.6 ms                                                | 90.6 ms: 1.12x slower                                           |
| genshi_text                | 22.9 ms                                                | 25.7 ms: 1.12x slower                                           |
| genshi_xml                 | 50.3 ms                                                | 57.1 ms: 1.13x slower                                           |
| docutils                   | 2.58 sec                                               | 2.96 sec: 1.15x slower                                          |
| hexiom                     | 6.13 ms                                                | 7.05 ms: 1.15x slower                                           |
| generators                 | 28.8 ms                                                | 45.8 ms: 1.59x slower                                           |
| Geometric mean             | (ref)                                                  | 1.02x slower                                                    |

Benchmark hidden because not significant (11): async_tree_cpu_io_mixed, json_dumps, xml_etree_generate, crypto_pyaes, bench_mp_pool, scimark_fft, django_template, float, json, pprint_safe_repr, xml_etree_process
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.03x