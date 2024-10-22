# Results vs. 3.13.0

- fork: brandtbucher
- ref: stitch_executors
- machine: linux-x86_64
- commit hash: 5d0917d
- commit date: 2024-08-07
- overall geometric mean: 1.01x faster
- HPT reliability: 66.03%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240807-linux-x86_64-brandtbucher-stitch_executors-3.14.0a0-5d0917d |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 273 ms: 1.03x slower                                                    |
| docutils       | 2.58 sec                                               | 2.96 sec: 1.14x slower                                                  |
| html5lib       | 64.5 ms                                                | 65.8 ms: 1.02x slower                                                   |
| tornado_http   | 91.5 ms                                                | 95.6 ms: 1.04x slower                                                   |
| Geometric mean | (ref)                                                  | 1.06x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240807-linux-x86_64-brandtbucher-stitch_executors-3.14.0a0-5d0917d |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 465 ms                                                 | 393 ms: 1.18x faster                                                    |
| async_tree_none            | 354 ms                                                 | 328 ms: 1.08x faster                                                    |
| async_tree_none_tg         | 320 ms                                                 | 300 ms: 1.07x faster                                                    |
| async_tree_memoization     | 442 ms                                                 | 422 ms: 1.05x faster                                                    |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 534 ms: 1.02x faster                                                    |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.01x slower                                                  |
| asyncio_tcp                | 488 ms                                                 | 502 ms: 1.03x slower                                                    |
| async_tree_io_tg           | 825 ms                                                 | 868 ms: 1.05x slower                                                    |
| async_generators           | 433 ms                                                 | 458 ms: 1.06x slower                                                    |
| async_tree_io              | 843 ms                                                 | 911 ms: 1.08x slower                                                    |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                            |

Benchmark hidden because not significant (3): async_tree_cpu_io_mixed, asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240807-linux-x86_64-brandtbucher-stitch_executors-3.14.0a0-5d0917d |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 71.8 ms: 1.09x faster                                                   |
| nbody          | 85.7 ms                                                | 79.7 ms: 1.08x faster                                                   |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                    |
| Geometric mean | (ref)                                                  | 1.06x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240807-linux-x86_64-brandtbucher-stitch_executors-3.14.0a0-5d0917d |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.87 ms: 1.00x faster                                                   |
| regex_v8       | 25.3 ms                                                | 25.7 ms: 1.02x slower                                                   |
| regex_compile  | 131 ms                                                 | 135 ms: 1.03x slower                                                    |
| regex_dna      | 220 ms                                                 | 232 ms: 1.05x slower                                                    |
| Geometric mean | (ref)                                                  | 1.02x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240807-linux-x86_64-brandtbucher-stitch_executors-3.14.0a0-5d0917d |
|---------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_generate  | 87.0 ms                                                | 79.8 ms: 1.09x faster                                                   |
| tomli_loads         | 2.11 sec                                               | 1.95 sec: 1.09x faster                                                  |
| xml_etree_process   | 60.4 ms                                                | 56.6 ms: 1.07x faster                                                   |
| xml_etree_parse     | 156 ms                                                 | 148 ms: 1.05x faster                                                    |
| xml_etree_iterparse | 102 ms                                                 | 99.7 ms: 1.02x faster                                                   |
| json_dumps          | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                   |
| json_loads          | 27.0 us                                                | 27.7 us: 1.03x slower                                                   |
| Geometric mean      | (ref)                                                  | 1.03x faster                                                            |

Benchmark hidden because not significant (2): pickle_pure_python, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240807-linux-x86_64-brandtbucher-stitch_executors-3.14.0a0-5d0917d |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.6 ms: 1.01x slower                                                   |
| python_startup_no_site | 6.99 ms                                                | 7.20 ms: 1.03x slower                                                   |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240807-linux-x86_64-brandtbucher-stitch_executors-3.14.0a0-5d0917d |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.69 ms: 1.15x faster                                                   |
| django_template | 34.4 ms                                                | 36.2 ms: 1.05x slower                                                   |
| genshi_text     | 22.9 ms                                                | 25.0 ms: 1.09x slower                                                   |
| genshi_xml      | 50.3 ms                                                | 56.1 ms: 1.12x slower                                                   |
| Geometric mean  | (ref)                                                  | 1.03x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240807-linux-x86_64-brandtbucher-stitch_executors-3.14.0a0-5d0917d |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy_memo              | 38.0 us                                                | 28.3 us: 1.34x faster                                                   |
| deepcopy                   | 352 us                                                 | 270 us: 1.30x faster                                                    |
| scimark_fft                | 369 ms                                                 | 300 ms: 1.23x faster                                                    |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.14 ms: 1.21x faster                                                   |
| async_tree_memoization_tg  | 465 ms                                                 | 393 ms: 1.18x faster                                                    |
| richards                   | 48.1 ms                                                | 41.5 ms: 1.16x faster                                                   |
| richards_super             | 54.4 ms                                                | 47.5 ms: 1.15x faster                                                   |
| mako                       | 11.1 ms                                                | 9.69 ms: 1.15x faster                                                   |
| deepcopy_reduce            | 3.17 us                                                | 2.77 us: 1.14x faster                                                   |
| spectral_norm              | 115 ms                                                 | 101 ms: 1.14x faster                                                    |
| crypto_pyaes               | 73.0 ms                                                | 66.1 ms: 1.10x faster                                                   |
| float                      | 78.5 ms                                                | 71.8 ms: 1.09x faster                                                   |
| xml_etree_generate         | 87.0 ms                                                | 79.8 ms: 1.09x faster                                                   |
| scimark_monte_carlo        | 66.3 ms                                                | 60.9 ms: 1.09x faster                                                   |
| scimark_lu                 | 115 ms                                                 | 106 ms: 1.09x faster                                                    |
| tomli_loads                | 2.11 sec                                               | 1.95 sec: 1.09x faster                                                  |
| async_tree_none            | 354 ms                                                 | 328 ms: 1.08x faster                                                    |
| nbody                      | 85.7 ms                                                | 79.7 ms: 1.08x faster                                                   |
| telco                      | 8.45 ms                                                | 7.87 ms: 1.07x faster                                                   |
| mdp                        | 2.74 sec                                               | 2.56 sec: 1.07x faster                                                  |
| pathlib                    | 17.1 ms                                                | 16.0 ms: 1.07x faster                                                   |
| xml_etree_process          | 60.4 ms                                                | 56.6 ms: 1.07x faster                                                   |
| async_tree_none_tg         | 320 ms                                                 | 300 ms: 1.07x faster                                                    |
| scimark_sor                | 122 ms                                                 | 115 ms: 1.06x faster                                                    |
| xml_etree_parse            | 156 ms                                                 | 148 ms: 1.05x faster                                                    |
| async_tree_memoization     | 442 ms                                                 | 422 ms: 1.05x faster                                                    |
| pprint_pformat             | 1.51 sec                                               | 1.45 sec: 1.04x faster                                                  |
| bpe_tokeniser              | 4.69 sec                                               | 4.51 sec: 1.04x faster                                                  |
| pprint_safe_repr           | 744 ms                                                 | 718 ms: 1.04x faster                                                    |
| logging_format             | 6.25 us                                                | 6.07 us: 1.03x faster                                                   |
| fannkuch                   | 381 ms                                                 | 370 ms: 1.03x faster                                                    |
| pyflate                    | 460 ms                                                 | 448 ms: 1.03x faster                                                    |
| meteor_contest             | 108 ms                                                 | 105 ms: 1.03x faster                                                    |
| logging_simple             | 5.66 us                                                | 5.53 us: 1.02x faster                                                   |
| xml_etree_iterparse        | 102 ms                                                 | 99.7 ms: 1.02x faster                                                   |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 534 ms: 1.02x faster                                                    |
| gc_traversal               | 3.81 ms                                                | 3.75 ms: 1.02x faster                                                   |
| chaos                      | 58.4 ms                                                | 57.7 ms: 1.01x faster                                                   |
| json_dumps                 | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                   |
| regex_effbot               | 3.88 ms                                                | 3.87 ms: 1.00x faster                                                   |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                                    |
| sqlglot_parse              | 1.27 ms                                                | 1.27 ms: 1.00x slower                                                   |
| python_startup             | 10.6 ms                                                | 10.6 ms: 1.01x slower                                                   |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.01x slower                                                  |
| comprehensions             | 16.4 us                                                | 16.6 us: 1.01x slower                                                   |
| bench_thread_pool          | 815 us                                                 | 829 us: 1.02x slower                                                    |
| regex_v8                   | 25.3 ms                                                | 25.7 ms: 1.02x slower                                                   |
| sqlglot_transpile          | 1.57 ms                                                | 1.60 ms: 1.02x slower                                                   |
| html5lib                   | 64.5 ms                                                | 65.8 ms: 1.02x slower                                                   |
| raytrace                   | 262 ms                                                 | 267 ms: 1.02x slower                                                    |
| go                         | 142 ms                                                 | 145 ms: 1.02x slower                                                    |
| regex_compile              | 131 ms                                                 | 135 ms: 1.03x slower                                                    |
| json_loads                 | 27.0 us                                                | 27.7 us: 1.03x slower                                                   |
| asyncio_tcp                | 488 ms                                                 | 502 ms: 1.03x slower                                                    |
| python_startup_no_site     | 6.99 ms                                                | 7.20 ms: 1.03x slower                                                   |
| 2to3                       | 265 ms                                                 | 273 ms: 1.03x slower                                                    |
| nqueens                    | 80.6 ms                                                | 83.9 ms: 1.04x slower                                                   |
| tornado_http               | 91.5 ms                                                | 95.6 ms: 1.04x slower                                                   |
| sqlglot_normalize          | 107 ms                                                 | 112 ms: 1.05x slower                                                    |
| sqlglot_optimize           | 53.9 ms                                                | 56.4 ms: 1.05x slower                                                   |
| django_template            | 34.4 ms                                                | 36.2 ms: 1.05x slower                                                   |
| hexiom                     | 6.13 ms                                                | 6.44 ms: 1.05x slower                                                   |
| async_tree_io_tg           | 825 ms                                                 | 868 ms: 1.05x slower                                                    |
| regex_dna                  | 220 ms                                                 | 232 ms: 1.05x slower                                                    |
| async_generators           | 433 ms                                                 | 458 ms: 1.06x slower                                                    |
| async_tree_io              | 843 ms                                                 | 911 ms: 1.08x slower                                                    |
| coverage                   | 83.7 ms                                                | 90.8 ms: 1.08x slower                                                   |
| typing_runtime_protocols   | 159 us                                                 | 173 us: 1.09x slower                                                    |
| genshi_text                | 22.9 ms                                                | 25.0 ms: 1.09x slower                                                   |
| create_gc_cycles           | 1.61 ms                                                | 1.77 ms: 1.10x slower                                                   |
| sympy_str                  | 274 ms                                                 | 305 ms: 1.11x slower                                                    |
| genshi_xml                 | 50.3 ms                                                | 56.1 ms: 1.12x slower                                                   |
| sympy_expand               | 462 ms                                                 | 517 ms: 1.12x slower                                                    |
| deltablue                  | 3.15 ms                                                | 3.56 ms: 1.13x slower                                                   |
| generators                 | 28.8 ms                                                | 32.9 ms: 1.14x slower                                                   |
| pylint                     | 313 ms                                                 | 358 ms: 1.14x slower                                                    |
| docutils                   | 2.58 sec                                               | 2.96 sec: 1.14x slower                                                  |
| sympy_integrate            | 19.9 ms                                                | 22.8 ms: 1.14x slower                                                   |
| sympy_sum                  | 150 ms                                                 | 174 ms: 1.16x slower                                                    |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                            |

Benchmark hidden because not significant (10): async_tree_cpu_io_mixed, pickle_pure_python, pycparser, bench_mp_pool, unpickle_pure_python, json, asyncio_websockets, coroutines, logging_silent, thrift
Ignored benchmarks (15) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 66.03% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.08x