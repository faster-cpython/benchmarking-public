# Results vs. 3.13.0

- fork: python
- ref: 04eb5c8db1e24cabd0cb
- machine: linux-x86_64
- commit hash: 04eb5c8
- commit date: 2024-07-27
- overall geometric mean: 1.01x faster
- HPT reliability: 53.20%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 264 ms: 1.00x faster                                                  |
| docutils       | 2.58 sec                                               | 2.74 sec: 1.06x slower                                                |
| html5lib       | 64.5 ms                                                | 65.6 ms: 1.02x slower                                                 |
| tornado_http   | 91.5 ms                                                | 90.9 ms: 1.01x faster                                                 |
| Geometric mean | (ref)                                                  | 1.02x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg  | 465 ms                                                 | 391 ms: 1.19x faster                                                  |
| async_tree_none            | 354 ms                                                 | 323 ms: 1.10x faster                                                  |
| async_tree_memoization     | 442 ms                                                 | 409 ms: 1.08x faster                                                  |
| async_tree_none_tg         | 320 ms                                                 | 299 ms: 1.07x faster                                                  |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 530 ms: 1.03x faster                                                  |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 562 ms: 1.02x faster                                                  |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.79 sec: 1.00x faster                                                |
| asyncio_websockets         | 555 ms                                                 | 560 ms: 1.01x slower                                                  |
| async_generators           | 433 ms                                                 | 437 ms: 1.01x slower                                                  |
| async_tree_io_tg           | 825 ms                                                 | 860 ms: 1.04x slower                                                  |
| async_tree_io              | 843 ms                                                 | 893 ms: 1.06x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                          |

Benchmark hidden because not significant (2): asyncio_tcp, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 78.1 ms: 1.00x faster                                                 |
| pidigits       | 186 ms                                                 | 187 ms: 1.01x slower                                                  |
| nbody          | 85.7 ms                                                | 89.0 ms: 1.04x slower                                                 |
| Geometric mean | (ref)                                                  | 1.01x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.67 ms: 1.06x faster                                                 |
| regex_v8       | 25.3 ms                                                | 24.6 ms: 1.03x faster                                                 |
| regex_dna      | 220 ms                                                 | 226 ms: 1.03x slower                                                  |
| Geometric mean | (ref)                                                  | 1.01x faster                                                          |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.11 sec                                               | 2.03 sec: 1.04x faster                                                |
| xml_etree_parse      | 156 ms                                                 | 154 ms: 1.01x faster                                                  |
| unpickle_pure_python | 213 us                                                 | 212 us: 1.01x faster                                                  |
| pickle_pure_python   | 300 us                                                 | 306 us: 1.02x slower                                                  |
| json_loads           | 27.0 us                                                | 27.6 us: 1.02x slower                                                 |
| xml_etree_iterparse  | 102 ms                                                 | 105 ms: 1.03x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.00x slower                                                          |

Benchmark hidden because not significant (3): xml_etree_process, json_dumps, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.5 ms: 1.00x faster                                                 |
| python_startup_no_site | 6.99 ms                                                | 7.10 ms: 1.02x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako           | 11.1 ms                                                | 11.0 ms: 1.01x faster                                                 |
| genshi_text    | 22.9 ms                                                | 23.7 ms: 1.04x slower                                                 |
| genshi_xml     | 50.3 ms                                                | 52.4 ms: 1.04x slower                                                 |
| Geometric mean | (ref)                                                  | 1.02x slower                                                          |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy                   | 352 us                                                 | 267 us: 1.32x faster                                                  |
| deepcopy_memo              | 38.0 us                                                | 29.4 us: 1.29x faster                                                 |
| async_tree_memoization_tg  | 465 ms                                                 | 391 ms: 1.19x faster                                                  |
| deepcopy_reduce            | 3.17 us                                                | 2.76 us: 1.15x faster                                                 |
| async_tree_none            | 354 ms                                                 | 323 ms: 1.10x faster                                                  |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.62 ms: 1.09x faster                                                 |
| mdp                        | 2.74 sec                                               | 2.52 sec: 1.09x faster                                                |
| pathlib                    | 17.1 ms                                                | 15.7 ms: 1.08x faster                                                 |
| async_tree_memoization     | 442 ms                                                 | 409 ms: 1.08x faster                                                  |
| async_tree_none_tg         | 320 ms                                                 | 299 ms: 1.07x faster                                                  |
| regex_effbot               | 3.88 ms                                                | 3.67 ms: 1.06x faster                                                 |
| pycparser                  | 1.19 sec                                               | 1.13 sec: 1.05x faster                                                |
| richards_super             | 54.4 ms                                                | 51.8 ms: 1.05x faster                                                 |
| scimark_fft                | 369 ms                                                 | 351 ms: 1.05x faster                                                  |
| richards                   | 48.1 ms                                                | 45.9 ms: 1.05x faster                                                 |
| telco                      | 8.45 ms                                                | 8.10 ms: 1.04x faster                                                 |
| tomli_loads                | 2.11 sec                                               | 2.03 sec: 1.04x faster                                                |
| bench_thread_pool          | 815 us                                                 | 789 us: 1.03x faster                                                  |
| logging_simple             | 5.66 us                                                | 5.49 us: 1.03x faster                                                 |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 530 ms: 1.03x faster                                                  |
| regex_v8                   | 25.3 ms                                                | 24.6 ms: 1.03x faster                                                 |
| thrift                     | 796 us                                                 | 777 us: 1.02x faster                                                  |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 562 ms: 1.02x faster                                                  |
| go                         | 142 ms                                                 | 139 ms: 1.02x faster                                                  |
| scimark_lu                 | 115 ms                                                 | 113 ms: 1.02x faster                                                  |
| gc_traversal               | 3.81 ms                                                | 3.75 ms: 1.02x faster                                                 |
| spectral_norm              | 115 ms                                                 | 113 ms: 1.01x faster                                                  |
| logging_format             | 6.25 us                                                | 6.17 us: 1.01x faster                                                 |
| sqlglot_optimize           | 53.9 ms                                                | 53.2 ms: 1.01x faster                                                 |
| xml_etree_parse            | 156 ms                                                 | 154 ms: 1.01x faster                                                  |
| generators                 | 28.8 ms                                                | 28.5 ms: 1.01x faster                                                 |
| nqueens                    | 80.6 ms                                                | 79.8 ms: 1.01x faster                                                 |
| sqlglot_normalize          | 107 ms                                                 | 106 ms: 1.01x faster                                                  |
| mako                       | 11.1 ms                                                | 11.0 ms: 1.01x faster                                                 |
| tornado_http               | 91.5 ms                                                | 90.9 ms: 1.01x faster                                                 |
| unpickle_pure_python       | 213 us                                                 | 212 us: 1.01x faster                                                  |
| float                      | 78.5 ms                                                | 78.1 ms: 1.00x faster                                                 |
| sympy_integrate            | 19.9 ms                                                | 19.8 ms: 1.00x faster                                                 |
| 2to3                       | 265 ms                                                 | 264 ms: 1.00x faster                                                  |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.79 sec: 1.00x faster                                                |
| python_startup             | 10.6 ms                                                | 10.5 ms: 1.00x faster                                                 |
| pprint_safe_repr           | 744 ms                                                 | 748 ms: 1.01x slower                                                  |
| pidigits                   | 186 ms                                                 | 187 ms: 1.01x slower                                                  |
| asyncio_websockets         | 555 ms                                                 | 560 ms: 1.01x slower                                                  |
| crypto_pyaes               | 73.0 ms                                                | 73.6 ms: 1.01x slower                                                 |
| async_generators           | 433 ms                                                 | 437 ms: 1.01x slower                                                  |
| comprehensions             | 16.4 us                                                | 16.6 us: 1.01x slower                                                 |
| hexiom                     | 6.13 ms                                                | 6.22 ms: 1.01x slower                                                 |
| chaos                      | 58.4 ms                                                | 59.3 ms: 1.01x slower                                                 |
| sympy_sum                  | 150 ms                                                 | 152 ms: 1.02x slower                                                  |
| python_startup_no_site     | 6.99 ms                                                | 7.10 ms: 1.02x slower                                                 |
| pprint_pformat             | 1.51 sec                                               | 1.54 sec: 1.02x slower                                                |
| html5lib                   | 64.5 ms                                                | 65.6 ms: 1.02x slower                                                 |
| coverage                   | 83.7 ms                                                | 85.4 ms: 1.02x slower                                                 |
| pickle_pure_python         | 300 us                                                 | 306 us: 1.02x slower                                                  |
| logging_silent             | 102 ns                                                 | 104 ns: 1.02x slower                                                  |
| pyflate                    | 460 ms                                                 | 470 ms: 1.02x slower                                                  |
| json_loads                 | 27.0 us                                                | 27.6 us: 1.02x slower                                                 |
| xml_etree_iterparse        | 102 ms                                                 | 105 ms: 1.03x slower                                                  |
| scimark_sor                | 122 ms                                                 | 126 ms: 1.03x slower                                                  |
| regex_dna                  | 220 ms                                                 | 226 ms: 1.03x slower                                                  |
| deltablue                  | 3.15 ms                                                | 3.24 ms: 1.03x slower                                                 |
| scimark_monte_carlo        | 66.3 ms                                                | 68.6 ms: 1.04x slower                                                 |
| bpe_tokeniser              | 4.69 sec                                               | 4.86 sec: 1.04x slower                                                |
| genshi_text                | 22.9 ms                                                | 23.7 ms: 1.04x slower                                                 |
| nbody                      | 85.7 ms                                                | 89.0 ms: 1.04x slower                                                 |
| genshi_xml                 | 50.3 ms                                                | 52.4 ms: 1.04x slower                                                 |
| async_tree_io_tg           | 825 ms                                                 | 860 ms: 1.04x slower                                                  |
| typing_runtime_protocols   | 159 us                                                 | 166 us: 1.05x slower                                                  |
| dask                       | 338 ms                                                 | 355 ms: 1.05x slower                                                  |
| docutils                   | 2.58 sec                                               | 2.74 sec: 1.06x slower                                                |
| async_tree_io              | 843 ms                                                 | 893 ms: 1.06x slower                                                  |
| fannkuch                   | 381 ms                                                 | 405 ms: 1.06x slower                                                  |
| create_gc_cycles           | 1.61 ms                                                | 1.74 ms: 1.08x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                          |

Benchmark hidden because not significant (16): json, xml_etree_process, json_dumps, asyncio_tcp, regex_compile, raytrace, sqlglot_parse, bench_mp_pool, xml_etree_generate, sympy_str, meteor_contest, coroutines, django_template, sqlglot_transpile, sympy_expand, pylint
Ignored benchmarks (14) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 53.20% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x