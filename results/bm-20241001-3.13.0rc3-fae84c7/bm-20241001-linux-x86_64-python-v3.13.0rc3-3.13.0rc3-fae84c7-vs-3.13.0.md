# Results vs. 3.13.0

- fork: python
- ref: v3.13.0rc3
- machine: linux-x86_64
- commit hash: fae84c7
- commit date: 2024-10-01
- overall geometric mean: 1.00x slower
- HPT reliability: 98.42%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241001-linux-x86_64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 264 ms: 1.00x faster                                         |
| docutils       | 2.58 sec                                               | 2.56 sec: 1.01x faster                                       |
| html5lib       | 64.5 ms                                                | 63.1 ms: 1.02x faster                                        |
| tornado_http   | 91.5 ms                                                | 91.2 ms: 1.00x faster                                        |
| Geometric mean | (ref)                                                  | 1.01x faster                                                 |

Benchmark hidden because not significant (1): chameleon

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241001-linux-x86_64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| coroutines                 | 22.5 ms                                                | 22.1 ms: 1.02x faster                                        |
| async_tree_none            | 354 ms                                                 | 349 ms: 1.01x faster                                         |
| async_tree_memoization_tg  | 465 ms                                                 | 459 ms: 1.01x faster                                         |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.77 sec: 1.01x faster                                       |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 539 ms: 1.01x faster                                         |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 569 ms: 1.01x faster                                         |
| asyncio_tcp                | 488 ms                                                 | 484 ms: 1.01x faster                                         |
| async_generators           | 433 ms                                                 | 435 ms: 1.01x slower                                         |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                 |

Benchmark hidden because not significant (5): async_tree_io_tg, async_tree_memoization, async_tree_io, async_tree_none_tg, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241001-linux-x86_64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| float          | 78.5 ms                                                | 79.0 ms: 1.01x slower                                        |
| nbody          | 85.7 ms                                                | 88.4 ms: 1.03x slower                                        |
| Geometric mean | (ref)                                                  | 1.01x slower                                                 |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241001-linux-x86_64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.51 ms: 1.11x faster                                        |
| regex_v8       | 25.3 ms                                                | 23.7 ms: 1.07x faster                                        |
| regex_dna      | 220 ms                                                 | 208 ms: 1.06x faster                                         |
| Geometric mean | (ref)                                                  | 1.06x faster                                                 |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241001-linux-x86_64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| unpickle_pure_python | 213 us                                                 | 211 us: 1.01x faster                                         |
| xml_etree_generate   | 87.0 ms                                                | 86.1 ms: 1.01x faster                                        |
| xml_etree_process    | 60.4 ms                                                | 59.8 ms: 1.01x faster                                        |
| xml_etree_parse      | 156 ms                                                 | 155 ms: 1.01x faster                                         |
| pickle_list          | 5.01 us                                                | 4.98 us: 1.01x faster                                        |
| pickle_pure_python   | 300 us                                                 | 302 us: 1.01x slower                                         |
| xml_etree_iterparse  | 102 ms                                                 | 103 ms: 1.01x slower                                         |
| json_dumps           | 10.4 ms                                                | 10.5 ms: 1.01x slower                                        |
| json_loads           | 27.0 us                                                | 27.3 us: 1.01x slower                                        |
| pickle               | 11.6 us                                                | 11.8 us: 1.02x slower                                        |
| unpickle             | 14.9 us                                                | 15.2 us: 1.02x slower                                        |
| pickle_dict          | 33.2 us                                                | 35.4 us: 1.07x slower                                        |
| unpickle_list        | 4.96 us                                                | 5.36 us: 1.08x slower                                        |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                 |

Benchmark hidden because not significant (1): tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241001-linux-x86_64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup_no_site | 6.99 ms                                                | 6.95 ms: 1.00x faster                                        |
| python_startup         | 10.6 ms                                                | 10.5 ms: 1.00x faster                                        |
| Geometric mean         | (ref)                                                  | 1.00x faster                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241001-linux-x86_64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| django_template | 34.4 ms                                                | 33.7 ms: 1.02x faster                                        |
| mako            | 11.1 ms                                                | 11.0 ms: 1.01x faster                                        |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                 |

Benchmark hidden because not significant (2): genshi_xml, genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241001-linux-x86_64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| regex_effbot               | 3.88 ms                                                | 3.51 ms: 1.11x faster                                        |
| regex_v8                   | 25.3 ms                                                | 23.7 ms: 1.07x faster                                        |
| regex_dna                  | 220 ms                                                 | 208 ms: 1.06x faster                                         |
| pycparser                  | 1.19 sec                                               | 1.15 sec: 1.03x faster                                       |
| html5lib                   | 64.5 ms                                                | 63.1 ms: 1.02x faster                                        |
| django_template            | 34.4 ms                                                | 33.7 ms: 1.02x faster                                        |
| coroutines                 | 22.5 ms                                                | 22.1 ms: 1.02x faster                                        |
| spectral_norm              | 115 ms                                                 | 113 ms: 1.02x faster                                         |
| djangocms                  | 31.9 us                                                | 31.3 us: 1.02x faster                                        |
| aiohttp                    | 1.14 ms                                                | 1.13 ms: 1.01x faster                                        |
| async_tree_none            | 354 ms                                                 | 349 ms: 1.01x faster                                         |
| async_tree_memoization_tg  | 465 ms                                                 | 459 ms: 1.01x faster                                         |
| comprehensions             | 16.4 us                                                | 16.2 us: 1.01x faster                                        |
| unpickle_pure_python       | 213 us                                                 | 211 us: 1.01x faster                                         |
| richards_super             | 54.4 ms                                                | 53.8 ms: 1.01x faster                                        |
| xml_etree_generate         | 87.0 ms                                                | 86.1 ms: 1.01x faster                                        |
| xml_etree_process          | 60.4 ms                                                | 59.8 ms: 1.01x faster                                        |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.77 sec: 1.01x faster                                       |
| docutils                   | 2.58 sec                                               | 2.56 sec: 1.01x faster                                       |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 539 ms: 1.01x faster                                         |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 569 ms: 1.01x faster                                         |
| asyncio_tcp                | 488 ms                                                 | 484 ms: 1.01x faster                                         |
| scimark_lu                 | 115 ms                                                 | 114 ms: 1.01x faster                                         |
| richards                   | 48.1 ms                                                | 47.8 ms: 1.01x faster                                        |
| xml_etree_parse            | 156 ms                                                 | 155 ms: 1.01x faster                                         |
| mako                       | 11.1 ms                                                | 11.0 ms: 1.01x faster                                        |
| gc_traversal               | 3.81 ms                                                | 3.78 ms: 1.01x faster                                        |
| pickle_list                | 5.01 us                                                | 4.98 us: 1.01x faster                                        |
| gunicorn                   | 1.23 ms                                                | 1.22 ms: 1.01x faster                                        |
| hexiom                     | 6.13 ms                                                | 6.10 ms: 1.00x faster                                        |
| python_startup_no_site     | 6.99 ms                                                | 6.95 ms: 1.00x faster                                        |
| mdp                        | 2.74 sec                                               | 2.73 sec: 1.00x faster                                       |
| sympy_integrate            | 19.9 ms                                                | 19.8 ms: 1.00x faster                                        |
| python_startup             | 10.6 ms                                                | 10.5 ms: 1.00x faster                                        |
| tornado_http               | 91.5 ms                                                | 91.2 ms: 1.00x faster                                        |
| sqlglot_normalize          | 107 ms                                                 | 107 ms: 1.00x faster                                         |
| sqlglot_transpile          | 1.57 ms                                                | 1.57 ms: 1.00x faster                                        |
| bench_thread_pool          | 815 us                                                 | 813 us: 1.00x faster                                         |
| 2to3                       | 265 ms                                                 | 264 ms: 1.00x faster                                         |
| dulwich_log                | 63.0 ms                                                | 63.2 ms: 1.00x slower                                        |
| sympy_sum                  | 150 ms                                                 | 150 ms: 1.01x slower                                         |
| coverage                   | 83.7 ms                                                | 84.2 ms: 1.01x slower                                        |
| async_generators           | 433 ms                                                 | 435 ms: 1.01x slower                                         |
| generators                 | 28.8 ms                                                | 29.0 ms: 1.01x slower                                        |
| raytrace                   | 262 ms                                                 | 263 ms: 1.01x slower                                         |
| pickle_pure_python         | 300 us                                                 | 302 us: 1.01x slower                                         |
| logging_format             | 6.25 us                                                | 6.29 us: 1.01x slower                                        |
| float                      | 78.5 ms                                                | 79.0 ms: 1.01x slower                                        |
| bpe_tokeniser              | 4.69 sec                                               | 4.72 sec: 1.01x slower                                       |
| logging_simple             | 5.66 us                                                | 5.71 us: 1.01x slower                                        |
| nqueens                    | 80.6 ms                                                | 81.2 ms: 1.01x slower                                        |
| telco                      | 8.45 ms                                                | 8.52 ms: 1.01x slower                                        |
| pathlib                    | 17.1 ms                                                | 17.2 ms: 1.01x slower                                        |
| xml_etree_iterparse        | 102 ms                                                 | 103 ms: 1.01x slower                                         |
| json_dumps                 | 10.4 ms                                                | 10.5 ms: 1.01x slower                                        |
| json_loads                 | 27.0 us                                                | 27.3 us: 1.01x slower                                        |
| create_gc_cycles           | 1.61 ms                                                | 1.63 ms: 1.01x slower                                        |
| chaos                      | 58.4 ms                                                | 59.2 ms: 1.01x slower                                        |
| deltablue                  | 3.15 ms                                                | 3.19 ms: 1.01x slower                                        |
| deepcopy_memo              | 38.0 us                                                | 38.6 us: 1.01x slower                                        |
| crypto_pyaes               | 73.0 ms                                                | 74.0 ms: 1.02x slower                                        |
| pyflate                    | 460 ms                                                 | 468 ms: 1.02x slower                                         |
| pickle                     | 11.6 us                                                | 11.8 us: 1.02x slower                                        |
| scimark_sor                | 122 ms                                                 | 125 ms: 1.02x slower                                         |
| deepcopy                   | 352 us                                                 | 360 us: 1.02x slower                                         |
| unpickle                   | 14.9 us                                                | 15.2 us: 1.02x slower                                        |
| scimark_monte_carlo        | 66.3 ms                                                | 67.8 ms: 1.02x slower                                        |
| deepcopy_reduce            | 3.17 us                                                | 3.26 us: 1.03x slower                                        |
| nbody                      | 85.7 ms                                                | 88.4 ms: 1.03x slower                                        |
| typing_runtime_protocols   | 159 us                                                 | 165 us: 1.04x slower                                         |
| fannkuch                   | 381 ms                                                 | 394 ms: 1.04x slower                                         |
| pickle_dict                | 33.2 us                                                | 35.4 us: 1.07x slower                                        |
| unpickle_list              | 4.96 us                                                | 5.36 us: 1.08x slower                                        |
| unpack_sequence            | 42.4 ns                                                | 48.1 ns: 1.13x slower                                        |
| Geometric mean             | (ref)                                                  | 1.00x slower                                                 |

Benchmark hidden because not significant (30): async_tree_io_tg, async_tree_memoization, async_tree_io, async_tree_none_tg, mypy2, pylint, logging_silent, thrift, pprint_safe_repr, sympy_expand, dask, asyncio_websockets, genshi_xml, sympy_str, go, scimark_fft, pprint_pformat, sqlglot_parse, sqlglot_optimize, pidigits, bench_mp_pool, chameleon, meteor_contest, sqlite_synth, scimark_sparse_mat_mult, regex_compile, json, flaskblogging, tomli_loads, genshi_text

# HPT report

- Reliability score: 98.42% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x