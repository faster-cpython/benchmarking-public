# Results vs. 3.13.0

- fork: faster-cpython
- ref: experimental_gc_fix
- machine: linux-x86_64
- commit hash: 9d28e99
- commit date: 2024-09-27
- overall geometric mean: 1.02x slower
- HPT reliability: 99.65%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-9d28e99 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 272 ms: 1.02x slower                                                           |
| docutils       | 2.58 sec                                               | 2.77 sec: 1.07x slower                                                         |
| html5lib       | 64.5 ms                                                | 68.1 ms: 1.05x slower                                                          |
| Geometric mean | (ref)                                                  | 1.04x slower                                                                   |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-9d28e99 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| asyncio_tcp                | 488 ms                                                 | 480 ms: 1.02x faster                                                           |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.78 sec: 1.01x faster                                                         |
| coroutines                 | 22.5 ms                                                | 23.6 ms: 1.05x slower                                                          |
| async_generators           | 433 ms                                                 | 459 ms: 1.06x slower                                                           |
| async_tree_memoization_tg  | 465 ms                                                 | 498 ms: 1.07x slower                                                           |
| async_tree_memoization     | 442 ms                                                 | 489 ms: 1.11x slower                                                           |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 638 ms: 1.11x slower                                                           |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 635 ms: 1.17x slower                                                           |
| async_tree_io_tg           | 825 ms                                                 | 966 ms: 1.17x slower                                                           |
| async_tree_io              | 843 ms                                                 | 995 ms: 1.18x slower                                                           |
| async_tree_none            | 354 ms                                                 | 424 ms: 1.20x slower                                                           |
| async_tree_none_tg         | 320 ms                                                 | 390 ms: 1.22x slower                                                           |
| Geometric mean             | (ref)                                                  | 1.10x slower                                                                   |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-9d28e99 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 186 ms                                                 | 187 ms: 1.01x slower                                                           |
| nbody          | 85.7 ms                                                | 87.7 ms: 1.02x slower                                                          |
| float          | 78.5 ms                                                | 97.0 ms: 1.24x slower                                                          |
| Geometric mean | (ref)                                                  | 1.08x slower                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-9d28e99 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.67 ms: 1.06x faster                                                          |
| regex_v8       | 25.3 ms                                                | 24.5 ms: 1.03x faster                                                          |
| regex_compile  | 131 ms                                                 | 128 ms: 1.02x faster                                                           |
| regex_dna      | 220 ms                                                 | 223 ms: 1.01x slower                                                           |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-9d28e99 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| unpickle             | 14.9 us                                                | 14.5 us: 1.02x faster                                                          |
| tomli_loads          | 2.11 sec                                               | 2.09 sec: 1.01x faster                                                         |
| json_loads           | 27.0 us                                                | 27.1 us: 1.00x slower                                                          |
| unpickle_pure_python | 213 us                                                 | 215 us: 1.01x slower                                                           |
| pickle               | 11.6 us                                                | 11.7 us: 1.01x slower                                                          |
| pickle_pure_python   | 300 us                                                 | 305 us: 1.02x slower                                                           |
| pickle_dict          | 33.2 us                                                | 34.8 us: 1.05x slower                                                          |
| unpickle_list        | 4.96 us                                                | 5.22 us: 1.05x slower                                                          |
| xml_etree_generate   | 87.0 ms                                                | 93.0 ms: 1.07x slower                                                          |
| pickle_list          | 5.01 us                                                | 5.36 us: 1.07x slower                                                          |
| xml_etree_process    | 60.4 ms                                                | 65.1 ms: 1.08x slower                                                          |
| xml_etree_parse      | 156 ms                                                 | 184 ms: 1.18x slower                                                           |
| xml_etree_iterparse  | 102 ms                                                 | 150 ms: 1.47x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.06x slower                                                                   |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-9d28e99 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 6.99 ms                                                | 7.00 ms: 1.00x slower                                                          |
| python_startup         | 10.6 ms                                                | 10.6 ms: 1.01x slower                                                          |
| Geometric mean         | (ref)                                                  | 1.00x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-9d28e99 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| genshi_text     | 22.9 ms                                                | 22.3 ms: 1.03x faster                                                          |
| mako            | 11.1 ms                                                | 11.3 ms: 1.02x slower                                                          |
| django_template | 34.4 ms                                                | 35.2 ms: 1.02x slower                                                          |
| genshi_xml      | 50.3 ms                                                | 54.4 ms: 1.08x slower                                                          |
| Geometric mean  | (ref)                                                  | 1.02x slower                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-9d28e99 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| deepcopy                   | 352 us                                                 | 261 us: 1.35x faster                                                           |
| deepcopy_memo              | 38.0 us                                                | 30.6 us: 1.24x faster                                                          |
| go                         | 142 ms                                                 | 119 ms: 1.19x faster                                                           |
| pylint                     | 313 ms                                                 | 266 ms: 1.18x faster                                                           |
| deepcopy_reduce            | 3.17 us                                                | 2.71 us: 1.17x faster                                                          |
| pathlib                    | 17.1 ms                                                | 16.1 ms: 1.06x faster                                                          |
| regex_effbot               | 3.88 ms                                                | 3.67 ms: 1.06x faster                                                          |
| richards_super             | 54.4 ms                                                | 52.4 ms: 1.04x faster                                                          |
| pprint_safe_repr           | 744 ms                                                 | 717 ms: 1.04x faster                                                           |
| richards                   | 48.1 ms                                                | 46.4 ms: 1.04x faster                                                          |
| bench_thread_pool          | 815 us                                                 | 790 us: 1.03x faster                                                           |
| spectral_norm              | 115 ms                                                 | 112 ms: 1.03x faster                                                           |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.88 ms: 1.03x faster                                                          |
| pprint_pformat             | 1.51 sec                                               | 1.47 sec: 1.03x faster                                                         |
| regex_v8                   | 25.3 ms                                                | 24.5 ms: 1.03x faster                                                          |
| genshi_text                | 22.9 ms                                                | 22.3 ms: 1.03x faster                                                          |
| thrift                     | 796 us                                                 | 776 us: 1.03x faster                                                           |
| unpickle                   | 14.9 us                                                | 14.5 us: 1.02x faster                                                          |
| regex_compile              | 131 ms                                                 | 128 ms: 1.02x faster                                                           |
| asyncio_tcp                | 488 ms                                                 | 480 ms: 1.02x faster                                                           |
| generators                 | 28.8 ms                                                | 28.3 ms: 1.02x faster                                                          |
| sympy_str                  | 274 ms                                                 | 269 ms: 1.02x faster                                                           |
| sympy_sum                  | 150 ms                                                 | 147 ms: 1.01x faster                                                           |
| typing_runtime_protocols   | 159 us                                                 | 157 us: 1.01x faster                                                           |
| json                       | 5.20 ms                                                | 5.13 ms: 1.01x faster                                                          |
| sympy_integrate            | 19.9 ms                                                | 19.6 ms: 1.01x faster                                                          |
| nqueens                    | 80.6 ms                                                | 79.6 ms: 1.01x faster                                                          |
| gc_traversal               | 3.81 ms                                                | 3.77 ms: 1.01x faster                                                          |
| sqlite_synth               | 2.85 us                                                | 2.82 us: 1.01x faster                                                          |
| tomli_loads                | 2.11 sec                                               | 2.09 sec: 1.01x faster                                                         |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.78 sec: 1.01x faster                                                         |
| mdp                        | 2.74 sec                                               | 2.73 sec: 1.01x faster                                                         |
| sqlglot_normalize          | 107 ms                                                 | 107 ms: 1.01x faster                                                           |
| python_startup_no_site     | 6.99 ms                                                | 7.00 ms: 1.00x slower                                                          |
| json_loads                 | 27.0 us                                                | 27.1 us: 1.00x slower                                                          |
| meteor_contest             | 108 ms                                                 | 108 ms: 1.00x slower                                                           |
| python_startup             | 10.6 ms                                                | 10.6 ms: 1.01x slower                                                          |
| scimark_lu                 | 115 ms                                                 | 116 ms: 1.01x slower                                                           |
| pidigits                   | 186 ms                                                 | 187 ms: 1.01x slower                                                           |
| crypto_pyaes               | 73.0 ms                                                | 73.4 ms: 1.01x slower                                                          |
| sqlglot_optimize           | 53.9 ms                                                | 54.3 ms: 1.01x slower                                                          |
| unpickle_pure_python       | 213 us                                                 | 215 us: 1.01x slower                                                           |
| raytrace                   | 262 ms                                                 | 264 ms: 1.01x slower                                                           |
| comprehensions             | 16.4 us                                                | 16.6 us: 1.01x slower                                                          |
| pickle                     | 11.6 us                                                | 11.7 us: 1.01x slower                                                          |
| regex_dna                  | 220 ms                                                 | 223 ms: 1.01x slower                                                           |
| logging_format             | 6.25 us                                                | 6.34 us: 1.01x slower                                                          |
| chaos                      | 58.4 ms                                                | 59.2 ms: 1.01x slower                                                          |
| pickle_pure_python         | 300 us                                                 | 305 us: 1.02x slower                                                           |
| mako                       | 11.1 ms                                                | 11.3 ms: 1.02x slower                                                          |
| scimark_sor                | 122 ms                                                 | 125 ms: 1.02x slower                                                           |
| pycparser                  | 1.19 sec                                               | 1.22 sec: 1.02x slower                                                         |
| django_template            | 34.4 ms                                                | 35.2 ms: 1.02x slower                                                          |
| nbody                      | 85.7 ms                                                | 87.7 ms: 1.02x slower                                                          |
| 2to3                       | 265 ms                                                 | 272 ms: 1.02x slower                                                           |
| scimark_monte_carlo        | 66.3 ms                                                | 68.0 ms: 1.03x slower                                                          |
| dulwich_log                | 63.0 ms                                                | 64.8 ms: 1.03x slower                                                          |
| logging_silent             | 102 ns                                                 | 105 ns: 1.03x slower                                                           |
| hexiom                     | 6.13 ms                                                | 6.31 ms: 1.03x slower                                                          |
| pyflate                    | 460 ms                                                 | 474 ms: 1.03x slower                                                           |
| coverage                   | 83.7 ms                                                | 86.6 ms: 1.03x slower                                                          |
| create_gc_cycles           | 1.61 ms                                                | 1.68 ms: 1.04x slower                                                          |
| coroutines                 | 22.5 ms                                                | 23.6 ms: 1.05x slower                                                          |
| pickle_dict                | 33.2 us                                                | 34.8 us: 1.05x slower                                                          |
| unpickle_list              | 4.96 us                                                | 5.22 us: 1.05x slower                                                          |
| html5lib                   | 64.5 ms                                                | 68.1 ms: 1.05x slower                                                          |
| async_generators           | 433 ms                                                 | 459 ms: 1.06x slower                                                           |
| fannkuch                   | 381 ms                                                 | 405 ms: 1.06x slower                                                           |
| sqlglot_transpile          | 1.57 ms                                                | 1.67 ms: 1.06x slower                                                          |
| xml_etree_generate         | 87.0 ms                                                | 93.0 ms: 1.07x slower                                                          |
| pickle_list                | 5.01 us                                                | 5.36 us: 1.07x slower                                                          |
| async_tree_memoization_tg  | 465 ms                                                 | 498 ms: 1.07x slower                                                           |
| docutils                   | 2.58 sec                                               | 2.77 sec: 1.07x slower                                                         |
| xml_etree_process          | 60.4 ms                                                | 65.1 ms: 1.08x slower                                                          |
| genshi_xml                 | 50.3 ms                                                | 54.4 ms: 1.08x slower                                                          |
| async_tree_memoization     | 442 ms                                                 | 489 ms: 1.11x slower                                                           |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 638 ms: 1.11x slower                                                           |
| sqlglot_parse              | 1.27 ms                                                | 1.41 ms: 1.11x slower                                                          |
| deltablue                  | 3.15 ms                                                | 3.55 ms: 1.13x slower                                                          |
| unpack_sequence            | 42.4 ns                                                | 49.5 ns: 1.17x slower                                                          |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 635 ms: 1.17x slower                                                           |
| async_tree_io_tg           | 825 ms                                                 | 966 ms: 1.17x slower                                                           |
| async_tree_io              | 843 ms                                                 | 995 ms: 1.18x slower                                                           |
| xml_etree_parse            | 156 ms                                                 | 184 ms: 1.18x slower                                                           |
| async_tree_none            | 354 ms                                                 | 424 ms: 1.20x slower                                                           |
| bpe_tokeniser              | 4.69 sec                                               | 5.67 sec: 1.21x slower                                                         |
| async_tree_none_tg         | 320 ms                                                 | 390 ms: 1.22x slower                                                           |
| float                      | 78.5 ms                                                | 97.0 ms: 1.24x slower                                                          |
| xml_etree_iterparse        | 102 ms                                                 | 150 ms: 1.47x slower                                                           |
| Geometric mean             | (ref)                                                  | 1.02x slower                                                                   |

Benchmark hidden because not significant (8): sympy_expand, telco, scimark_fft, asyncio_websockets, bench_mp_pool, tornado_http, json_dumps, logging_simple
Ignored benchmarks (7) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 99.65% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x