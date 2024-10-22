# Results vs. 3.13.0

- fork: brandtbucher
- ref: underflow
- machine: linux-x86_64
- commit hash: 8c45870
- commit date: 2024-08-12
- overall geometric mean: 1.00x faster
- HPT reliability: 66.19%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240812-linux-x86_64-brandtbucher-underflow-3.14.0a0-8c45870 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 280 ms: 1.06x slower                                             |
| docutils       | 2.58 sec                                               | 3.29 sec: 1.27x slower                                           |
| html5lib       | 64.5 ms                                                | 68.6 ms: 1.06x slower                                            |
| tornado_http   | 91.5 ms                                                | 96.9 ms: 1.06x slower                                            |
| Geometric mean | (ref)                                                  | 1.11x slower                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240812-linux-x86_64-brandtbucher-underflow-3.14.0a0-8c45870 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_memoization_tg  | 465 ms                                                 | 395 ms: 1.18x faster                                             |
| async_tree_none            | 354 ms                                                 | 324 ms: 1.09x faster                                             |
| async_tree_none_tg         | 320 ms                                                 | 302 ms: 1.06x faster                                             |
| async_tree_memoization     | 442 ms                                                 | 425 ms: 1.04x faster                                             |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 532 ms: 1.02x faster                                             |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.82 sec: 1.01x slower                                           |
| coroutines                 | 22.5 ms                                                | 23.1 ms: 1.02x slower                                            |
| async_generators           | 433 ms                                                 | 452 ms: 1.04x slower                                             |
| asyncio_tcp                | 488 ms                                                 | 512 ms: 1.05x slower                                             |
| async_tree_io_tg           | 825 ms                                                 | 878 ms: 1.06x slower                                             |
| async_tree_io              | 843 ms                                                 | 902 ms: 1.07x slower                                             |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                     |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240812-linux-x86_64-brandtbucher-underflow-3.14.0a0-8c45870 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| float          | 78.5 ms                                                | 70.7 ms: 1.11x faster                                            |
| nbody          | 85.7 ms                                                | 82.3 ms: 1.04x faster                                            |
| pidigits       | 186 ms                                                 | 188 ms: 1.01x slower                                             |
| Geometric mean | (ref)                                                  | 1.05x faster                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240812-linux-x86_64-brandtbucher-underflow-3.14.0a0-8c45870 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.68 ms: 1.05x faster                                            |
| regex_dna      | 220 ms                                                 | 210 ms: 1.05x faster                                             |
| regex_v8       | 25.3 ms                                                | 24.6 ms: 1.03x faster                                            |
| regex_compile  | 131 ms                                                 | 146 ms: 1.11x slower                                             |
| Geometric mean | (ref)                                                  | 1.00x faster                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240812-linux-x86_64-brandtbucher-underflow-3.14.0a0-8c45870 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| unpickle_pure_python | 213 us                                                 | 194 us: 1.10x faster                                             |
| xml_etree_generate   | 87.0 ms                                                | 80.7 ms: 1.08x faster                                            |
| xml_etree_process    | 60.4 ms                                                | 56.3 ms: 1.07x faster                                            |
| xml_etree_parse      | 156 ms                                                 | 148 ms: 1.06x faster                                             |
| xml_etree_iterparse  | 102 ms                                                 | 98.7 ms: 1.03x faster                                            |
| tomli_loads          | 2.11 sec                                               | 2.09 sec: 1.01x faster                                           |
| pickle_pure_python   | 300 us                                                 | 304 us: 1.01x slower                                             |
| json_loads           | 27.0 us                                                | 28.0 us: 1.04x slower                                            |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                     |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240812-linux-x86_64-brandtbucher-underflow-3.14.0a0-8c45870 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.6 ms: 1.00x slower                                            |
| python_startup_no_site | 6.99 ms                                                | 7.17 ms: 1.03x slower                                            |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240812-linux-x86_64-brandtbucher-underflow-3.14.0a0-8c45870 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.74 ms: 1.14x faster                                            |
| genshi_text     | 22.9 ms                                                | 23.8 ms: 1.04x slower                                            |
| django_template | 34.4 ms                                                | 36.8 ms: 1.07x slower                                            |
| genshi_xml      | 50.3 ms                                                | 63.5 ms: 1.26x slower                                            |
| Geometric mean  | (ref)                                                  | 1.05x slower                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240812-linux-x86_64-brandtbucher-underflow-3.14.0a0-8c45870 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| deepcopy_memo              | 38.0 us                                                | 26.3 us: 1.45x faster                                            |
| deepcopy                   | 352 us                                                 | 260 us: 1.36x faster                                             |
| richards_super             | 54.4 ms                                                | 43.4 ms: 1.26x faster                                            |
| richards                   | 48.1 ms                                                | 38.4 ms: 1.25x faster                                            |
| scimark_fft                | 369 ms                                                 | 307 ms: 1.20x faster                                             |
| deepcopy_reduce            | 3.17 us                                                | 2.69 us: 1.18x faster                                            |
| async_tree_memoization_tg  | 465 ms                                                 | 395 ms: 1.18x faster                                             |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.32 ms: 1.16x faster                                            |
| mako                       | 11.1 ms                                                | 9.74 ms: 1.14x faster                                            |
| scimark_monte_carlo        | 66.3 ms                                                | 58.2 ms: 1.14x faster                                            |
| spectral_norm              | 115 ms                                                 | 103 ms: 1.12x faster                                             |
| float                      | 78.5 ms                                                | 70.7 ms: 1.11x faster                                            |
| crypto_pyaes               | 73.0 ms                                                | 66.1 ms: 1.10x faster                                            |
| unpickle_pure_python       | 213 us                                                 | 194 us: 1.10x faster                                             |
| telco                      | 8.45 ms                                                | 7.68 ms: 1.10x faster                                            |
| async_tree_none            | 354 ms                                                 | 324 ms: 1.09x faster                                             |
| xml_etree_generate         | 87.0 ms                                                | 80.7 ms: 1.08x faster                                            |
| xml_etree_process          | 60.4 ms                                                | 56.3 ms: 1.07x faster                                            |
| async_tree_none_tg         | 320 ms                                                 | 302 ms: 1.06x faster                                             |
| pathlib                    | 17.1 ms                                                | 16.1 ms: 1.06x faster                                            |
| xml_etree_parse            | 156 ms                                                 | 148 ms: 1.06x faster                                             |
| regex_effbot               | 3.88 ms                                                | 3.68 ms: 1.05x faster                                            |
| logging_silent             | 102 ns                                                 | 97.0 ns: 1.05x faster                                            |
| scimark_lu                 | 115 ms                                                 | 110 ms: 1.05x faster                                             |
| regex_dna                  | 220 ms                                                 | 210 ms: 1.05x faster                                             |
| nbody                      | 85.7 ms                                                | 82.3 ms: 1.04x faster                                            |
| async_tree_memoization     | 442 ms                                                 | 425 ms: 1.04x faster                                             |
| pyflate                    | 460 ms                                                 | 442 ms: 1.04x faster                                             |
| fannkuch                   | 381 ms                                                 | 367 ms: 1.04x faster                                             |
| xml_etree_iterparse        | 102 ms                                                 | 98.7 ms: 1.03x faster                                            |
| bpe_tokeniser              | 4.69 sec                                               | 4.55 sec: 1.03x faster                                           |
| regex_v8                   | 25.3 ms                                                | 24.6 ms: 1.03x faster                                            |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 532 ms: 1.02x faster                                             |
| json                       | 5.20 ms                                                | 5.10 ms: 1.02x faster                                            |
| scimark_sor                | 122 ms                                                 | 121 ms: 1.02x faster                                             |
| gc_traversal               | 3.81 ms                                                | 3.76 ms: 1.01x faster                                            |
| meteor_contest             | 108 ms                                                 | 106 ms: 1.01x faster                                             |
| tomli_loads                | 2.11 sec                                               | 2.09 sec: 1.01x faster                                           |
| python_startup             | 10.6 ms                                                | 10.6 ms: 1.00x slower                                            |
| comprehensions             | 16.4 us                                                | 16.5 us: 1.01x slower                                            |
| deltablue                  | 3.15 ms                                                | 3.17 ms: 1.01x slower                                            |
| bench_thread_pool          | 815 us                                                 | 821 us: 1.01x slower                                             |
| chaos                      | 58.4 ms                                                | 58.9 ms: 1.01x slower                                            |
| logging_format             | 6.25 us                                                | 6.31 us: 1.01x slower                                            |
| pidigits                   | 186 ms                                                 | 188 ms: 1.01x slower                                             |
| pickle_pure_python         | 300 us                                                 | 304 us: 1.01x slower                                             |
| raytrace                   | 262 ms                                                 | 265 ms: 1.01x slower                                             |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.82 sec: 1.01x slower                                           |
| coroutines                 | 22.5 ms                                                | 23.1 ms: 1.02x slower                                            |
| python_startup_no_site     | 6.99 ms                                                | 7.17 ms: 1.03x slower                                            |
| go                         | 142 ms                                                 | 146 ms: 1.03x slower                                             |
| pprint_pformat             | 1.51 sec                                               | 1.56 sec: 1.03x slower                                           |
| nqueens                    | 80.6 ms                                                | 83.1 ms: 1.03x slower                                            |
| json_loads                 | 27.0 us                                                | 28.0 us: 1.04x slower                                            |
| pycparser                  | 1.19 sec                                               | 1.24 sec: 1.04x slower                                           |
| genshi_text                | 22.9 ms                                                | 23.8 ms: 1.04x slower                                            |
| async_generators           | 433 ms                                                 | 452 ms: 1.04x slower                                             |
| asyncio_tcp                | 488 ms                                                 | 512 ms: 1.05x slower                                             |
| 2to3                       | 265 ms                                                 | 280 ms: 1.06x slower                                             |
| tornado_http               | 91.5 ms                                                | 96.9 ms: 1.06x slower                                            |
| html5lib                   | 64.5 ms                                                | 68.6 ms: 1.06x slower                                            |
| async_tree_io_tg           | 825 ms                                                 | 878 ms: 1.06x slower                                             |
| django_template            | 34.4 ms                                                | 36.8 ms: 1.07x slower                                            |
| async_tree_io              | 843 ms                                                 | 902 ms: 1.07x slower                                             |
| typing_runtime_protocols   | 159 us                                                 | 171 us: 1.08x slower                                             |
| coverage                   | 83.7 ms                                                | 90.9 ms: 1.09x slower                                            |
| sqlglot_normalize          | 107 ms                                                 | 117 ms: 1.09x slower                                             |
| sqlglot_transpile          | 1.57 ms                                                | 1.72 ms: 1.09x slower                                            |
| create_gc_cycles           | 1.61 ms                                                | 1.78 ms: 1.10x slower                                            |
| sqlglot_optimize           | 53.9 ms                                                | 59.9 ms: 1.11x slower                                            |
| hexiom                     | 6.13 ms                                                | 6.80 ms: 1.11x slower                                            |
| regex_compile              | 131 ms                                                 | 146 ms: 1.11x slower                                             |
| sqlglot_parse              | 1.27 ms                                                | 1.44 ms: 1.14x slower                                            |
| sympy_expand               | 462 ms                                                 | 531 ms: 1.15x slower                                             |
| generators                 | 28.8 ms                                                | 33.5 ms: 1.16x slower                                            |
| sympy_str                  | 274 ms                                                 | 318 ms: 1.16x slower                                             |
| sympy_integrate            | 19.9 ms                                                | 24.4 ms: 1.23x slower                                            |
| sympy_sum                  | 150 ms                                                 | 187 ms: 1.25x slower                                             |
| genshi_xml                 | 50.3 ms                                                | 63.5 ms: 1.26x slower                                            |
| docutils                   | 2.58 sec                                               | 3.29 sec: 1.27x slower                                           |
| pylint                     | 313 ms                                                 | 408 ms: 1.30x slower                                             |
| Geometric mean             | (ref)                                                  | 1.00x faster                                                     |

Benchmark hidden because not significant (8): async_tree_cpu_io_mixed, json_dumps, mdp, asyncio_websockets, bench_mp_pool, thrift, logging_simple, pprint_safe_repr
Ignored benchmarks (15) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 66.19% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.09x