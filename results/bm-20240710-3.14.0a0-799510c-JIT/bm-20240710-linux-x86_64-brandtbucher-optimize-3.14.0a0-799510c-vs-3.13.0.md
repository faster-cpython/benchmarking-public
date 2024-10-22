# Results vs. 3.13.0

- fork: brandtbucher
- ref: optimize
- machine: linux-x86_64
- commit hash: 799510c
- commit date: 2024-07-10
- overall geometric mean: 1.05x slower
- HPT reliability: 79.06%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240710-linux-x86_64-brandtbucher-optimize-3.14.0a0-799510c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 271 ms: 1.02x slower                                            |
| docutils       | 2.58 sec                                               | 6.74 sec: 2.61x slower                                          |
| html5lib       | 64.5 ms                                                | 77.0 ms: 1.19x slower                                           |
| tornado_http   | 91.5 ms                                                | 97.9 ms: 1.07x slower                                           |
| Geometric mean | (ref)                                                  | 1.36x slower                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240710-linux-x86_64-brandtbucher-optimize-3.14.0a0-799510c |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_memoization_tg  | 465 ms                                                 | 382 ms: 1.22x faster                                            |
| async_tree_none            | 354 ms                                                 | 329 ms: 1.08x faster                                            |
| async_tree_memoization     | 442 ms                                                 | 412 ms: 1.07x faster                                            |
| async_tree_none_tg         | 320 ms                                                 | 305 ms: 1.05x faster                                            |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.01x slower                                          |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 552 ms: 1.01x slower                                            |
| async_tree_io_tg           | 825 ms                                                 | 863 ms: 1.05x slower                                            |
| asyncio_tcp                | 488 ms                                                 | 516 ms: 1.06x slower                                            |
| async_tree_io              | 843 ms                                                 | 896 ms: 1.06x slower                                            |
| async_generators           | 433 ms                                                 | 514 ms: 1.19x slower                                            |
| coroutines                 | 22.5 ms                                                | 27.5 ms: 1.22x slower                                           |
| Geometric mean             | (ref)                                                  | 1.01x slower                                                    |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240710-linux-x86_64-brandtbucher-optimize-3.14.0a0-799510c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| nbody          | 85.7 ms                                                | 77.4 ms: 1.11x faster                                           |
| float          | 78.5 ms                                                | 70.9 ms: 1.11x faster                                           |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                            |
| Geometric mean | (ref)                                                  | 1.07x faster                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240710-linux-x86_64-brandtbucher-optimize-3.14.0a0-799510c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_compile  | 131 ms                                                 | 130 ms: 1.01x faster                                            |
| regex_v8       | 25.3 ms                                                | 25.6 ms: 1.01x slower                                           |
| regex_dna      | 220 ms                                                 | 223 ms: 1.02x slower                                            |
| Geometric mean | (ref)                                                  | 1.01x slower                                                    |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240710-linux-x86_64-brandtbucher-optimize-3.14.0a0-799510c |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| tomli_loads          | 2.11 sec                                               | 1.94 sec: 1.09x faster                                          |
| xml_etree_parse      | 156 ms                                                 | 148 ms: 1.05x faster                                            |
| xml_etree_process    | 60.4 ms                                                | 58.1 ms: 1.04x faster                                           |
| xml_etree_generate   | 87.0 ms                                                | 84.8 ms: 1.03x faster                                           |
| pickle_pure_python   | 300 us                                                 | 303 us: 1.01x slower                                            |
| json_loads           | 27.0 us                                                | 27.4 us: 1.01x slower                                           |
| unpickle_pure_python | 213 us                                                 | 218 us: 1.02x slower                                            |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                    |

Benchmark hidden because not significant (2): json_dumps, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240710-linux-x86_64-brandtbucher-optimize-3.14.0a0-799510c |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.6 ms: 1.00x faster                                           |
| python_startup_no_site | 6.99 ms                                                | 7.12 ms: 1.02x slower                                           |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240710-linux-x86_64-brandtbucher-optimize-3.14.0a0-799510c |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.87 ms: 1.12x faster                                           |
| django_template | 34.4 ms                                                | 40.3 ms: 1.17x slower                                           |
| genshi_text     | 22.9 ms                                                | 27.0 ms: 1.18x slower                                           |
| genshi_xml      | 50.3 ms                                                | 62.2 ms: 1.24x slower                                           |
| Geometric mean  | (ref)                                                  | 1.11x slower                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240710-linux-x86_64-brandtbucher-optimize-3.14.0a0-799510c |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| deepcopy_memo              | 38.0 us                                                | 27.2 us: 1.40x faster                                           |
| deepcopy                   | 352 us                                                 | 261 us: 1.35x faster                                            |
| richards                   | 48.1 ms                                                | 38.5 ms: 1.25x faster                                           |
| richards_super             | 54.4 ms                                                | 44.6 ms: 1.22x faster                                           |
| async_tree_memoization_tg  | 465 ms                                                 | 382 ms: 1.22x faster                                            |
| deepcopy_reduce            | 3.17 us                                                | 2.64 us: 1.20x faster                                           |
| spectral_norm              | 115 ms                                                 | 98.0 ms: 1.17x faster                                           |
| scimark_fft                | 369 ms                                                 | 316 ms: 1.17x faster                                            |
| mako                       | 11.1 ms                                                | 9.87 ms: 1.12x faster                                           |
| nbody                      | 85.7 ms                                                | 77.4 ms: 1.11x faster                                           |
| float                      | 78.5 ms                                                | 70.9 ms: 1.11x faster                                           |
| crypto_pyaes               | 73.0 ms                                                | 66.6 ms: 1.09x faster                                           |
| tomli_loads                | 2.11 sec                                               | 1.94 sec: 1.09x faster                                          |
| async_tree_none            | 354 ms                                                 | 329 ms: 1.08x faster                                            |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.67 ms: 1.08x faster                                           |
| async_tree_memoization     | 442 ms                                                 | 412 ms: 1.07x faster                                            |
| telco                      | 8.45 ms                                                | 7.90 ms: 1.07x faster                                           |
| pathlib                    | 17.1 ms                                                | 16.1 ms: 1.06x faster                                           |
| xml_etree_parse            | 156 ms                                                 | 148 ms: 1.05x faster                                            |
| async_tree_none_tg         | 320 ms                                                 | 305 ms: 1.05x faster                                            |
| chaos                      | 58.4 ms                                                | 56.0 ms: 1.04x faster                                           |
| pprint_safe_repr           | 744 ms                                                 | 716 ms: 1.04x faster                                            |
| xml_etree_process          | 60.4 ms                                                | 58.1 ms: 1.04x faster                                           |
| scimark_monte_carlo        | 66.3 ms                                                | 64.1 ms: 1.03x faster                                           |
| pprint_pformat             | 1.51 sec                                               | 1.47 sec: 1.03x faster                                          |
| xml_etree_generate         | 87.0 ms                                                | 84.8 ms: 1.03x faster                                           |
| pycparser                  | 1.19 sec                                               | 1.16 sec: 1.02x faster                                          |
| logging_simple             | 5.66 us                                                | 5.54 us: 1.02x faster                                           |
| json                       | 5.20 ms                                                | 5.08 ms: 1.02x faster                                           |
| logging_format             | 6.25 us                                                | 6.11 us: 1.02x faster                                           |
| mdp                        | 2.74 sec                                               | 2.70 sec: 1.01x faster                                          |
| go                         | 142 ms                                                 | 140 ms: 1.01x faster                                            |
| regex_compile              | 131 ms                                                 | 130 ms: 1.01x faster                                            |
| meteor_contest             | 108 ms                                                 | 107 ms: 1.01x faster                                            |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                            |
| gc_traversal               | 3.81 ms                                                | 3.80 ms: 1.00x faster                                           |
| python_startup             | 10.6 ms                                                | 10.6 ms: 1.00x faster                                           |
| pyflate                    | 460 ms                                                 | 463 ms: 1.01x slower                                            |
| comprehensions             | 16.4 us                                                | 16.6 us: 1.01x slower                                           |
| pickle_pure_python         | 300 us                                                 | 303 us: 1.01x slower                                            |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.01x slower                                          |
| thrift                     | 796 us                                                 | 806 us: 1.01x slower                                            |
| sqlglot_parse              | 1.27 ms                                                | 1.28 ms: 1.01x slower                                           |
| json_loads                 | 27.0 us                                                | 27.4 us: 1.01x slower                                           |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 552 ms: 1.01x slower                                            |
| regex_v8                   | 25.3 ms                                                | 25.6 ms: 1.01x slower                                           |
| bpe_tokeniser              | 4.69 sec                                               | 4.76 sec: 1.02x slower                                          |
| regex_dna                  | 220 ms                                                 | 223 ms: 1.02x slower                                            |
| unpickle_pure_python       | 213 us                                                 | 218 us: 1.02x slower                                            |
| python_startup_no_site     | 6.99 ms                                                | 7.12 ms: 1.02x slower                                           |
| 2to3                       | 265 ms                                                 | 271 ms: 1.02x slower                                            |
| scimark_sor                | 122 ms                                                 | 126 ms: 1.03x slower                                            |
| dulwich_log                | 63.0 ms                                                | 65.4 ms: 1.04x slower                                           |
| async_tree_io_tg           | 825 ms                                                 | 863 ms: 1.05x slower                                            |
| sqlglot_transpile          | 1.57 ms                                                | 1.65 ms: 1.05x slower                                           |
| bench_thread_pool          | 815 us                                                 | 853 us: 1.05x slower                                            |
| typing_runtime_protocols   | 159 us                                                 | 167 us: 1.05x slower                                            |
| scimark_lu                 | 115 ms                                                 | 121 ms: 1.05x slower                                            |
| asyncio_tcp                | 488 ms                                                 | 516 ms: 1.06x slower                                            |
| sqlglot_normalize          | 107 ms                                                 | 114 ms: 1.06x slower                                            |
| async_tree_io              | 843 ms                                                 | 896 ms: 1.06x slower                                            |
| hexiom                     | 6.13 ms                                                | 6.52 ms: 1.06x slower                                           |
| sympy_expand               | 462 ms                                                 | 493 ms: 1.07x slower                                            |
| tornado_http               | 91.5 ms                                                | 97.9 ms: 1.07x slower                                           |
| create_gc_cycles           | 1.61 ms                                                | 1.75 ms: 1.09x slower                                           |
| deltablue                  | 3.15 ms                                                | 3.43 ms: 1.09x slower                                           |
| sympy_str                  | 274 ms                                                 | 302 ms: 1.10x slower                                            |
| sqlglot_optimize           | 53.9 ms                                                | 60.0 ms: 1.11x slower                                           |
| coverage                   | 83.7 ms                                                | 93.3 ms: 1.11x slower                                           |
| sympy_sum                  | 150 ms                                                 | 168 ms: 1.12x slower                                            |
| dask                       | 338 ms                                                 | 383 ms: 1.13x slower                                            |
| nqueens                    | 80.6 ms                                                | 94.1 ms: 1.17x slower                                           |
| django_template            | 34.4 ms                                                | 40.3 ms: 1.17x slower                                           |
| genshi_text                | 22.9 ms                                                | 27.0 ms: 1.18x slower                                           |
| async_generators           | 433 ms                                                 | 514 ms: 1.19x slower                                            |
| html5lib                   | 64.5 ms                                                | 77.0 ms: 1.19x slower                                           |
| coroutines                 | 22.5 ms                                                | 27.5 ms: 1.22x slower                                           |
| genshi_xml                 | 50.3 ms                                                | 62.2 ms: 1.24x slower                                           |
| sympy_integrate            | 19.9 ms                                                | 25.3 ms: 1.27x slower                                           |
| pylint                     | 313 ms                                                 | 425 ms: 1.36x slower                                            |
| generators                 | 28.8 ms                                                | 47.6 ms: 1.65x slower                                           |
| docutils                   | 2.58 sec                                               | 6.74 sec: 2.61x slower                                          |
| raytrace                   | 262 ms                                                 | 4.85 sec: 18.54x slower                                         |
| Geometric mean             | (ref)                                                  | 1.05x slower                                                    |

Benchmark hidden because not significant (8): fannkuch, json_dumps, async_tree_cpu_io_mixed, regex_effbot, bench_mp_pool, asyncio_websockets, xml_etree_iterparse, logging_silent
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 79.06% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.09x