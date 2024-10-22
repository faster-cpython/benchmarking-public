# Results vs. 3.13.0

- fork: encukou
- ref: intern_ūnus
- machine: linux-x86_64
- commit hash: a5da0a6
- commit date: 2024-07-26
- overall geometric mean: 1.02x faster
- HPT reliability: 81.26%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240726-linux-x86_64-encukou-intern_ūnus-3.14.0a0-a5da0a6 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 262 ms: 1.01x faster                                          |
| docutils       | 2.58 sec                                               | 2.73 sec: 1.06x slower                                        |
| html5lib       | 64.5 ms                                                | 65.9 ms: 1.02x slower                                         |
| tornado_http   | 91.5 ms                                                | 89.9 ms: 1.02x faster                                         |
| Geometric mean | (ref)                                                  | 1.01x slower                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240726-linux-x86_64-encukou-intern_ūnus-3.14.0a0-a5da0a6 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| async_tree_memoization_tg  | 465 ms                                                 | 391 ms: 1.19x faster                                          |
| async_tree_none            | 354 ms                                                 | 324 ms: 1.09x faster                                          |
| async_tree_none_tg         | 320 ms                                                 | 299 ms: 1.07x faster                                          |
| async_tree_memoization     | 442 ms                                                 | 413 ms: 1.07x faster                                          |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 534 ms: 1.02x faster                                          |
| asyncio_tcp                | 488 ms                                                 | 481 ms: 1.01x faster                                          |
| async_generators           | 433 ms                                                 | 431 ms: 1.00x faster                                          |
| asyncio_websockets         | 555 ms                                                 | 558 ms: 1.00x slower                                          |
| coroutines                 | 22.5 ms                                                | 22.9 ms: 1.02x slower                                         |
| async_tree_io_tg           | 825 ms                                                 | 861 ms: 1.04x slower                                          |
| async_tree_io              | 843 ms                                                 | 902 ms: 1.07x slower                                          |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                  |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed, asyncio_tcp_ssl

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240726-linux-x86_64-encukou-intern_ūnus-3.14.0a0-a5da0a6 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| float          | 78.5 ms                                                | 77.4 ms: 1.01x faster                                         |
| nbody          | 85.7 ms                                                | 84.6 ms: 1.01x faster                                         |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x slower                                          |
| Geometric mean | (ref)                                                  | 1.01x faster                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240726-linux-x86_64-encukou-intern_ūnus-3.14.0a0-a5da0a6 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.78 ms: 1.03x faster                                         |
| regex_compile  | 131 ms                                                 | 132 ms: 1.01x slower                                          |
| regex_dna      | 220 ms                                                 | 224 ms: 1.02x slower                                          |
| Geometric mean | (ref)                                                  | 1.00x faster                                                  |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240726-linux-x86_64-encukou-intern_ūnus-3.14.0a0-a5da0a6 |
|---------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| xml_etree_process   | 60.4 ms                                                | 58.5 ms: 1.03x faster                                         |
| xml_etree_generate  | 87.0 ms                                                | 84.7 ms: 1.03x faster                                         |
| tomli_loads         | 2.11 sec                                               | 2.09 sec: 1.01x faster                                        |
| pickle_pure_python  | 300 us                                                 | 299 us: 1.01x faster                                          |
| xml_etree_iterparse | 102 ms                                                 | 104 ms: 1.02x slower                                          |
| json_loads          | 27.0 us                                                | 27.7 us: 1.03x slower                                         |
| Geometric mean      | (ref)                                                  | 1.00x faster                                                  |

Benchmark hidden because not significant (3): unpickle_pure_python, json_dumps, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240726-linux-x86_64-encukou-intern_ūnus-3.14.0a0-a5da0a6 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.5 ms: 1.01x faster                                         |
| python_startup_no_site | 6.99 ms                                                | 7.05 ms: 1.01x slower                                         |
| Geometric mean         | (ref)                                                  | 1.00x slower                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240726-linux-x86_64-encukou-intern_ūnus-3.14.0a0-a5da0a6 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| genshi_text     | 22.9 ms                                                | 22.3 ms: 1.03x faster                                         |
| django_template | 34.4 ms                                                | 33.8 ms: 1.02x faster                                         |
| genshi_xml      | 50.3 ms                                                | 50.0 ms: 1.01x faster                                         |
| mako            | 11.1 ms                                                | 11.4 ms: 1.03x slower                                         |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                  |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240726-linux-x86_64-encukou-intern_ūnus-3.14.0a0-a5da0a6 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| deepcopy                   | 352 us                                                 | 261 us: 1.35x faster                                          |
| deepcopy_memo              | 38.0 us                                                | 29.5 us: 1.29x faster                                         |
| deepcopy_reduce            | 3.17 us                                                | 2.63 us: 1.21x faster                                         |
| async_tree_memoization_tg  | 465 ms                                                 | 391 ms: 1.19x faster                                          |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.51 ms: 1.11x faster                                         |
| async_tree_none            | 354 ms                                                 | 324 ms: 1.09x faster                                          |
| gc_traversal               | 3.81 ms                                                | 3.49 ms: 1.09x faster                                         |
| mdp                        | 2.74 sec                                               | 2.52 sec: 1.09x faster                                        |
| pathlib                    | 17.1 ms                                                | 15.9 ms: 1.07x faster                                         |
| async_tree_none_tg         | 320 ms                                                 | 299 ms: 1.07x faster                                          |
| async_tree_memoization     | 442 ms                                                 | 413 ms: 1.07x faster                                          |
| richards                   | 48.1 ms                                                | 45.3 ms: 1.06x faster                                         |
| richards_super             | 54.4 ms                                                | 51.2 ms: 1.06x faster                                         |
| logging_silent             | 102 ns                                                 | 97.5 ns: 1.05x faster                                         |
| scimark_fft                | 369 ms                                                 | 355 ms: 1.04x faster                                          |
| telco                      | 8.45 ms                                                | 8.15 ms: 1.04x faster                                         |
| bench_thread_pool          | 815 us                                                 | 786 us: 1.04x faster                                          |
| logging_simple             | 5.66 us                                                | 5.49 us: 1.03x faster                                         |
| xml_etree_process          | 60.4 ms                                                | 58.5 ms: 1.03x faster                                         |
| logging_format             | 6.25 us                                                | 6.08 us: 1.03x faster                                         |
| generators                 | 28.8 ms                                                | 28.0 ms: 1.03x faster                                         |
| scimark_lu                 | 115 ms                                                 | 112 ms: 1.03x faster                                          |
| regex_effbot               | 3.88 ms                                                | 3.78 ms: 1.03x faster                                         |
| xml_etree_generate         | 87.0 ms                                                | 84.7 ms: 1.03x faster                                         |
| genshi_text                | 22.9 ms                                                | 22.3 ms: 1.03x faster                                         |
| raytrace                   | 262 ms                                                 | 255 ms: 1.02x faster                                          |
| json                       | 5.20 ms                                                | 5.09 ms: 1.02x faster                                         |
| spectral_norm              | 115 ms                                                 | 113 ms: 1.02x faster                                          |
| django_template            | 34.4 ms                                                | 33.8 ms: 1.02x faster                                         |
| tornado_http               | 91.5 ms                                                | 89.9 ms: 1.02x faster                                         |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 534 ms: 1.02x faster                                          |
| thrift                     | 796 us                                                 | 783 us: 1.02x faster                                          |
| asyncio_tcp                | 488 ms                                                 | 481 ms: 1.01x faster                                          |
| sqlglot_optimize           | 53.9 ms                                                | 53.2 ms: 1.01x faster                                         |
| float                      | 78.5 ms                                                | 77.4 ms: 1.01x faster                                         |
| nbody                      | 85.7 ms                                                | 84.6 ms: 1.01x faster                                         |
| tomli_loads                | 2.11 sec                                               | 2.09 sec: 1.01x faster                                        |
| go                         | 142 ms                                                 | 140 ms: 1.01x faster                                          |
| sympy_str                  | 274 ms                                                 | 271 ms: 1.01x faster                                          |
| pycparser                  | 1.19 sec                                               | 1.18 sec: 1.01x faster                                        |
| 2to3                       | 265 ms                                                 | 262 ms: 1.01x faster                                          |
| sympy_integrate            | 19.9 ms                                                | 19.7 ms: 1.01x faster                                         |
| sqlglot_normalize          | 107 ms                                                 | 106 ms: 1.01x faster                                          |
| python_startup             | 10.6 ms                                                | 10.5 ms: 1.01x faster                                         |
| deltablue                  | 3.15 ms                                                | 3.12 ms: 1.01x faster                                         |
| genshi_xml                 | 50.3 ms                                                | 50.0 ms: 1.01x faster                                         |
| pickle_pure_python         | 300 us                                                 | 299 us: 1.01x faster                                          |
| meteor_contest             | 108 ms                                                 | 107 ms: 1.00x faster                                          |
| async_generators           | 433 ms                                                 | 431 ms: 1.00x faster                                          |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x slower                                          |
| hexiom                     | 6.13 ms                                                | 6.14 ms: 1.00x slower                                         |
| asyncio_websockets         | 555 ms                                                 | 558 ms: 1.00x slower                                          |
| regex_compile              | 131 ms                                                 | 132 ms: 1.01x slower                                          |
| chaos                      | 58.4 ms                                                | 58.9 ms: 1.01x slower                                         |
| python_startup_no_site     | 6.99 ms                                                | 7.05 ms: 1.01x slower                                         |
| pprint_pformat             | 1.51 sec                                               | 1.53 sec: 1.01x slower                                        |
| xml_etree_iterparse        | 102 ms                                                 | 104 ms: 1.02x slower                                          |
| coroutines                 | 22.5 ms                                                | 22.9 ms: 1.02x slower                                         |
| nqueens                    | 80.6 ms                                                | 82.2 ms: 1.02x slower                                         |
| regex_dna                  | 220 ms                                                 | 224 ms: 1.02x slower                                          |
| pyflate                    | 460 ms                                                 | 469 ms: 1.02x slower                                          |
| html5lib                   | 64.5 ms                                                | 65.9 ms: 1.02x slower                                         |
| mako                       | 11.1 ms                                                | 11.4 ms: 1.03x slower                                         |
| json_loads                 | 27.0 us                                                | 27.7 us: 1.03x slower                                         |
| crypto_pyaes               | 73.0 ms                                                | 75.1 ms: 1.03x slower                                         |
| bpe_tokeniser              | 4.69 sec                                               | 4.84 sec: 1.03x slower                                        |
| scimark_sor                | 122 ms                                                 | 127 ms: 1.04x slower                                          |
| async_tree_io_tg           | 825 ms                                                 | 861 ms: 1.04x slower                                          |
| dask                       | 338 ms                                                 | 353 ms: 1.04x slower                                          |
| typing_runtime_protocols   | 159 us                                                 | 167 us: 1.05x slower                                          |
| docutils                   | 2.58 sec                                               | 2.73 sec: 1.06x slower                                        |
| create_gc_cycles           | 1.61 ms                                                | 1.72 ms: 1.07x slower                                         |
| coverage                   | 83.7 ms                                                | 89.3 ms: 1.07x slower                                         |
| fannkuch                   | 381 ms                                                 | 407 ms: 1.07x slower                                          |
| async_tree_io              | 843 ms                                                 | 902 ms: 1.07x slower                                          |
| scimark_monte_carlo        | 66.3 ms                                                | 71.4 ms: 1.08x slower                                         |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                  |

Benchmark hidden because not significant (14): async_tree_cpu_io_mixed, sympy_expand, unpickle_pure_python, regex_v8, asyncio_tcp_ssl, json_dumps, bench_mp_pool, comprehensions, pprint_safe_repr, sympy_sum, sqlglot_transpile, sqlglot_parse, xml_etree_parse, pylint
Ignored benchmarks (14) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 81.26% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x