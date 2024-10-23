# Results vs. 3.13.0

- fork: nick-arm
- ref: codecache
- machine: linux-x86_64
- commit hash: 0be1ef3
- commit date: 2024-10-21
- overall geometric mean: 1.02x slower
- HPT reliability: 55.50%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.20x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-linux-x86_64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 276 ms: 1.04x slower                                            |
| docutils       | 2.58 sec                                               | 2.91 sec: 1.12x slower                                          |
| html5lib       | 64.5 ms                                                | 67.1 ms: 1.04x slower                                           |
| tornado_http   | 91.5 ms                                                | 94.8 ms: 1.04x slower                                           |
| Geometric mean | (ref)                                                  | 1.06x slower                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-linux-x86_64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_memoization_tg  | 465 ms                                                 | 377 ms: 1.23x faster                                            |
| async_tree_memoization     | 442 ms                                                 | 418 ms: 1.06x faster                                            |
| async_tree_none            | 354 ms                                                 | 339 ms: 1.05x faster                                            |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 556 ms: 1.02x slower                                            |
| coroutines                 | 22.5 ms                                                | 23.7 ms: 1.05x slower                                           |
| async_generators           | 433 ms                                                 | 457 ms: 1.06x slower                                            |
| async_tree_io_tg           | 825 ms                                                 | 976 ms: 1.18x slower                                            |
| Geometric mean             | (ref)                                                  | 1.00x faster                                                    |

Benchmark hidden because not significant (4): async_tree_cpu_io_mixed, asyncio_websockets, async_tree_none_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-linux-x86_64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| nbody          | 85.7 ms                                                | 82.3 ms: 1.04x faster                                           |
| float          | 78.5 ms                                                | 75.6 ms: 1.04x faster                                           |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                            |
| Geometric mean | (ref)                                                  | 1.03x faster                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-linux-x86_64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.72 ms: 1.04x faster                                           |
| regex_dna      | 220 ms                                                 | 214 ms: 1.03x faster                                            |
| regex_v8       | 25.3 ms                                                | 24.7 ms: 1.02x faster                                           |
| regex_compile  | 131 ms                                                 | 139 ms: 1.06x slower                                            |
| Geometric mean | (ref)                                                  | 1.01x faster                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-linux-x86_64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| xml_etree_generate   | 87.0 ms                                                | 78.2 ms: 1.11x faster                                           |
| tomli_loads          | 2.11 sec                                               | 1.90 sec: 1.11x faster                                          |
| xml_etree_process    | 60.4 ms                                                | 54.8 ms: 1.10x faster                                           |
| xml_etree_parse      | 156 ms                                                 | 148 ms: 1.05x faster                                            |
| json_loads           | 27.0 us                                                | 26.8 us: 1.01x faster                                           |
| unpickle_pure_python | 213 us                                                 | 215 us: 1.01x slower                                            |
| pickle_pure_python   | 300 us                                                 | 311 us: 1.03x slower                                            |
| json_dumps           | 10.4 ms                                                | 10.8 ms: 1.04x slower                                           |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                    |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-linux-x86_64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup_no_site | 6.99 ms                                                | 7.07 ms: 1.01x slower                                           |
| python_startup         | 10.6 ms                                                | 11.8 ms: 1.12x slower                                           |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-linux-x86_64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 10.2 ms: 1.09x faster                                           |
| django_template | 34.4 ms                                                | 35.8 ms: 1.04x slower                                           |
| genshi_text     | 22.9 ms                                                | 25.8 ms: 1.13x slower                                           |
| genshi_xml      | 50.3 ms                                                | 60.4 ms: 1.20x slower                                           |
| Geometric mean  | (ref)                                                  | 1.07x slower                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-linux-x86_64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| deepcopy                   | 352 us                                                 | 266 us: 1.33x faster                                            |
| deepcopy_memo              | 38.0 us                                                | 29.1 us: 1.30x faster                                           |
| async_tree_memoization_tg  | 465 ms                                                 | 377 ms: 1.23x faster                                            |
| richards                   | 48.1 ms                                                | 40.8 ms: 1.18x faster                                           |
| scimark_fft                | 369 ms                                                 | 315 ms: 1.17x faster                                            |
| deepcopy_reduce            | 3.17 us                                                | 2.73 us: 1.16x faster                                           |
| richards_super             | 54.4 ms                                                | 47.6 ms: 1.14x faster                                           |
| telco                      | 8.45 ms                                                | 7.58 ms: 1.11x faster                                           |
| xml_etree_generate         | 87.0 ms                                                | 78.2 ms: 1.11x faster                                           |
| tomli_loads                | 2.11 sec                                               | 1.90 sec: 1.11x faster                                          |
| xml_etree_process          | 60.4 ms                                                | 54.8 ms: 1.10x faster                                           |
| mako                       | 11.1 ms                                                | 10.2 ms: 1.09x faster                                           |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.63 ms: 1.09x faster                                           |
| mdp                        | 2.74 sec                                               | 2.54 sec: 1.08x faster                                          |
| pprint_safe_repr           | 744 ms                                                 | 696 ms: 1.07x faster                                            |
| pathlib                    | 17.1 ms                                                | 16.0 ms: 1.07x faster                                           |
| crypto_pyaes               | 73.0 ms                                                | 68.6 ms: 1.06x faster                                           |
| go                         | 142 ms                                                 | 133 ms: 1.06x faster                                            |
| async_tree_memoization     | 442 ms                                                 | 418 ms: 1.06x faster                                            |
| logging_silent             | 102 ns                                                 | 97.1 ns: 1.05x faster                                           |
| xml_etree_parse            | 156 ms                                                 | 148 ms: 1.05x faster                                            |
| bpe_tokeniser              | 4.69 sec                                               | 4.46 sec: 1.05x faster                                          |
| pycparser                  | 1.19 sec                                               | 1.14 sec: 1.05x faster                                          |
| async_tree_none            | 354 ms                                                 | 339 ms: 1.05x faster                                            |
| regex_effbot               | 3.88 ms                                                | 3.72 ms: 1.04x faster                                           |
| nbody                      | 85.7 ms                                                | 82.3 ms: 1.04x faster                                           |
| json                       | 5.20 ms                                                | 5.00 ms: 1.04x faster                                           |
| float                      | 78.5 ms                                                | 75.6 ms: 1.04x faster                                           |
| pprint_pformat             | 1.51 sec                                               | 1.46 sec: 1.03x faster                                          |
| scimark_monte_carlo        | 66.3 ms                                                | 64.3 ms: 1.03x faster                                           |
| scimark_sor                | 122 ms                                                 | 119 ms: 1.03x faster                                            |
| pyflate                    | 460 ms                                                 | 447 ms: 1.03x faster                                            |
| regex_dna                  | 220 ms                                                 | 214 ms: 1.03x faster                                            |
| logging_format             | 6.25 us                                                | 6.10 us: 1.03x faster                                           |
| regex_v8                   | 25.3 ms                                                | 24.7 ms: 1.02x faster                                           |
| thrift                     | 796 us                                                 | 779 us: 1.02x faster                                            |
| scimark_lu                 | 115 ms                                                 | 113 ms: 1.02x faster                                            |
| logging_simple             | 5.66 us                                                | 5.57 us: 1.02x faster                                           |
| meteor_contest             | 108 ms                                                 | 107 ms: 1.01x faster                                            |
| json_loads                 | 27.0 us                                                | 26.8 us: 1.01x faster                                           |
| spectral_norm              | 115 ms                                                 | 115 ms: 1.00x faster                                            |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                            |
| coverage                   | 83.7 ms                                                | 84.4 ms: 1.01x slower                                           |
| unpickle_pure_python       | 213 us                                                 | 215 us: 1.01x slower                                            |
| chaos                      | 58.4 ms                                                | 59.1 ms: 1.01x slower                                           |
| python_startup_no_site     | 6.99 ms                                                | 7.07 ms: 1.01x slower                                           |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 556 ms: 1.02x slower                                            |
| comprehensions             | 16.4 us                                                | 17.0 us: 1.03x slower                                           |
| pickle_pure_python         | 300 us                                                 | 311 us: 1.03x slower                                            |
| typing_runtime_protocols   | 159 us                                                 | 165 us: 1.04x slower                                            |
| tornado_http               | 91.5 ms                                                | 94.8 ms: 1.04x slower                                           |
| deltablue                  | 3.15 ms                                                | 3.27 ms: 1.04x slower                                           |
| json_dumps                 | 10.4 ms                                                | 10.8 ms: 1.04x slower                                           |
| html5lib                   | 64.5 ms                                                | 67.1 ms: 1.04x slower                                           |
| django_template            | 34.4 ms                                                | 35.8 ms: 1.04x slower                                           |
| 2to3                       | 265 ms                                                 | 276 ms: 1.04x slower                                            |
| raytrace                   | 262 ms                                                 | 273 ms: 1.04x slower                                            |
| coroutines                 | 22.5 ms                                                | 23.7 ms: 1.05x slower                                           |
| sqlglot_normalize          | 107 ms                                                 | 113 ms: 1.05x slower                                            |
| regex_compile              | 131 ms                                                 | 139 ms: 1.06x slower                                            |
| async_generators           | 433 ms                                                 | 457 ms: 1.06x slower                                            |
| sqlglot_parse              | 1.27 ms                                                | 1.34 ms: 1.06x slower                                           |
| dulwich_log                | 63.0 ms                                                | 66.9 ms: 1.06x slower                                           |
| sqlglot_transpile          | 1.57 ms                                                | 1.70 ms: 1.08x slower                                           |
| sympy_expand               | 462 ms                                                 | 498 ms: 1.08x slower                                            |
| bench_thread_pool          | 815 us                                                 | 881 us: 1.08x slower                                            |
| nqueens                    | 80.6 ms                                                | 87.6 ms: 1.09x slower                                           |
| sympy_str                  | 274 ms                                                 | 299 ms: 1.09x slower                                            |
| sqlglot_optimize           | 53.9 ms                                                | 59.3 ms: 1.10x slower                                           |
| python_startup             | 10.6 ms                                                | 11.8 ms: 1.12x slower                                           |
| docutils                   | 2.58 sec                                               | 2.91 sec: 1.12x slower                                          |
| genshi_text                | 22.9 ms                                                | 25.8 ms: 1.13x slower                                           |
| hexiom                     | 6.13 ms                                                | 7.01 ms: 1.14x slower                                           |
| gc_traversal               | 3.81 ms                                                | 4.37 ms: 1.15x slower                                           |
| sympy_sum                  | 150 ms                                                 | 175 ms: 1.17x slower                                            |
| sympy_integrate            | 19.9 ms                                                | 23.3 ms: 1.17x slower                                           |
| async_tree_io_tg           | 825 ms                                                 | 976 ms: 1.18x slower                                            |
| pylint                     | 313 ms                                                 | 374 ms: 1.19x slower                                            |
| genshi_xml                 | 50.3 ms                                                | 60.4 ms: 1.20x slower                                           |
| generators                 | 28.8 ms                                                | 35.5 ms: 1.23x slower                                           |
| create_gc_cycles           | 1.61 ms                                                | 2.66 ms: 1.65x slower                                           |
| bench_mp_pool              | 24.0 ms                                                | 83.8 ms: 3.49x slower                                           |
| Geometric mean             | (ref)                                                  | 1.02x slower                                                    |

Benchmark hidden because not significant (6): xml_etree_iterparse, async_tree_cpu_io_mixed, asyncio_websockets, fannkuch, async_tree_none_tg, async_tree_io
Ignored benchmarks (16) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (1) of results/bm-20241021-3.14.0a1+-0be1ef3-JIT/bm-20241021-linux-x86_64-nick%2darm-codecache-3.14.0a1+-0be1ef3.json: sphinx

# HPT report

- Reliability score: 55.50% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.20x