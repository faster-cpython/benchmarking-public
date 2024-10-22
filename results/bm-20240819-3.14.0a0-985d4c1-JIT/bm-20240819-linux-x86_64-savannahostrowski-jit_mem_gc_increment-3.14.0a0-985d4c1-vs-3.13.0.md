# Results vs. 3.13.0

- fork: savannahostrowski
- ref: jit_mem_gc_increment
- machine: linux-x86_64
- commit hash: 985d4c1
- commit date: 2024-08-19
- overall geometric mean: 1.01x faster
- HPT reliability: 65.19%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240819-linux-x86_64-savannahostrowski-jit_mem_gc_increment-3.14.0a0-985d4c1 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 283 ms: 1.07x slower                                                             |
| docutils       | 2.58 sec                                               | 2.98 sec: 1.15x slower                                                           |
| html5lib       | 64.5 ms                                                | 66.8 ms: 1.03x slower                                                            |
| tornado_http   | 91.5 ms                                                | 93.1 ms: 1.02x slower                                                            |
| Geometric mean | (ref)                                                  | 1.07x slower                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240819-linux-x86_64-savannahostrowski-jit_mem_gc_increment-3.14.0a0-985d4c1 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 465 ms                                                 | 392 ms: 1.19x faster                                                             |
| async_tree_none            | 354 ms                                                 | 326 ms: 1.09x faster                                                             |
| async_tree_none_tg         | 320 ms                                                 | 298 ms: 1.07x faster                                                             |
| async_tree_memoization     | 442 ms                                                 | 419 ms: 1.05x faster                                                             |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 532 ms: 1.02x faster                                                             |
| asyncio_tcp                | 488 ms                                                 | 494 ms: 1.01x slower                                                             |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.82 sec: 1.01x slower                                                           |
| coroutines                 | 22.5 ms                                                | 23.0 ms: 1.02x slower                                                            |
| async_tree_io_tg           | 825 ms                                                 | 865 ms: 1.05x slower                                                             |
| async_generators           | 433 ms                                                 | 458 ms: 1.06x slower                                                             |
| async_tree_io              | 843 ms                                                 | 903 ms: 1.07x slower                                                             |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                                     |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240819-linux-x86_64-savannahostrowski-jit_mem_gc_increment-3.14.0a0-985d4c1 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 72.0 ms: 1.09x faster                                                            |
| nbody          | 85.7 ms                                                | 81.8 ms: 1.05x faster                                                            |
| pidigits       | 186 ms                                                 | 188 ms: 1.01x slower                                                             |
| Geometric mean | (ref)                                                  | 1.04x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240819-linux-x86_64-savannahostrowski-jit_mem_gc_increment-3.14.0a0-985d4c1 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.77 ms: 1.03x faster                                                            |
| regex_v8       | 25.3 ms                                                | 24.8 ms: 1.02x faster                                                            |
| regex_dna      | 220 ms                                                 | 222 ms: 1.01x slower                                                             |
| regex_compile  | 131 ms                                                 | 142 ms: 1.08x slower                                                             |
| Geometric mean | (ref)                                                  | 1.01x slower                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240819-linux-x86_64-savannahostrowski-jit_mem_gc_increment-3.14.0a0-985d4c1 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| tomli_loads          | 2.11 sec                                               | 1.91 sec: 1.11x faster                                                           |
| xml_etree_parse      | 156 ms                                                 | 147 ms: 1.06x faster                                                             |
| xml_etree_iterparse  | 102 ms                                                 | 98.9 ms: 1.03x faster                                                            |
| xml_etree_process    | 60.4 ms                                                | 59.3 ms: 1.02x faster                                                            |
| xml_etree_generate   | 87.0 ms                                                | 85.9 ms: 1.01x faster                                                            |
| unpickle_pure_python | 213 us                                                 | 212 us: 1.00x faster                                                             |
| json_dumps           | 10.4 ms                                                | 10.5 ms: 1.01x slower                                                            |
| json_loads           | 27.0 us                                                | 28.8 us: 1.07x slower                                                            |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                                     |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240819-linux-x86_64-savannahostrowski-jit_mem_gc_increment-3.14.0a0-985d4c1 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.5 ms: 1.00x faster                                                            |
| python_startup_no_site | 6.99 ms                                                | 7.14 ms: 1.02x slower                                                            |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240819-linux-x86_64-savannahostrowski-jit_mem_gc_increment-3.14.0a0-985d4c1 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.84 ms: 1.13x faster                                                            |
| django_template | 34.4 ms                                                | 35.9 ms: 1.04x slower                                                            |
| genshi_text     | 22.9 ms                                                | 25.8 ms: 1.13x slower                                                            |
| genshi_xml      | 50.3 ms                                                | 61.1 ms: 1.21x slower                                                            |
| Geometric mean  | (ref)                                                  | 1.06x slower                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240819-linux-x86_64-savannahostrowski-jit_mem_gc_increment-3.14.0a0-985d4c1 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| deepcopy_memo              | 38.0 us                                                | 26.5 us: 1.44x faster                                                            |
| deepcopy                   | 352 us                                                 | 265 us: 1.33x faster                                                             |
| richards                   | 48.1 ms                                                | 39.6 ms: 1.22x faster                                                            |
| richards_super             | 54.4 ms                                                | 45.0 ms: 1.21x faster                                                            |
| scimark_fft                | 369 ms                                                 | 311 ms: 1.19x faster                                                             |
| async_tree_memoization_tg  | 465 ms                                                 | 392 ms: 1.19x faster                                                             |
| deepcopy_reduce            | 3.17 us                                                | 2.68 us: 1.18x faster                                                            |
| spectral_norm              | 115 ms                                                 | 102 ms: 1.13x faster                                                             |
| mako                       | 11.1 ms                                                | 9.84 ms: 1.13x faster                                                            |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.52 ms: 1.11x faster                                                            |
| tomli_loads                | 2.11 sec                                               | 1.91 sec: 1.11x faster                                                           |
| crypto_pyaes               | 73.0 ms                                                | 66.5 ms: 1.10x faster                                                            |
| float                      | 78.5 ms                                                | 72.0 ms: 1.09x faster                                                            |
| async_tree_none            | 354 ms                                                 | 326 ms: 1.09x faster                                                             |
| telco                      | 8.45 ms                                                | 7.80 ms: 1.08x faster                                                            |
| async_tree_none_tg         | 320 ms                                                 | 298 ms: 1.07x faster                                                             |
| scimark_lu                 | 115 ms                                                 | 107 ms: 1.07x faster                                                             |
| gc_traversal               | 3.81 ms                                                | 3.58 ms: 1.06x faster                                                            |
| xml_etree_parse            | 156 ms                                                 | 147 ms: 1.06x faster                                                             |
| pathlib                    | 17.1 ms                                                | 16.1 ms: 1.06x faster                                                            |
| async_tree_memoization     | 442 ms                                                 | 419 ms: 1.05x faster                                                             |
| scimark_monte_carlo        | 66.3 ms                                                | 62.8 ms: 1.05x faster                                                            |
| nbody                      | 85.7 ms                                                | 81.8 ms: 1.05x faster                                                            |
| scimark_sor                | 122 ms                                                 | 117 ms: 1.05x faster                                                             |
| pyflate                    | 460 ms                                                 | 443 ms: 1.04x faster                                                             |
| xml_etree_iterparse        | 102 ms                                                 | 98.9 ms: 1.03x faster                                                            |
| regex_effbot               | 3.88 ms                                                | 3.77 ms: 1.03x faster                                                            |
| logging_silent             | 102 ns                                                 | 99.2 ns: 1.03x faster                                                            |
| logging_format             | 6.25 us                                                | 6.09 us: 1.03x faster                                                            |
| pprint_safe_repr           | 744 ms                                                 | 726 ms: 1.02x faster                                                             |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 532 ms: 1.02x faster                                                             |
| regex_v8                   | 25.3 ms                                                | 24.8 ms: 1.02x faster                                                            |
| xml_etree_process          | 60.4 ms                                                | 59.3 ms: 1.02x faster                                                            |
| logging_simple             | 5.66 us                                                | 5.57 us: 1.02x faster                                                            |
| fannkuch                   | 381 ms                                                 | 375 ms: 1.02x faster                                                             |
| xml_etree_generate         | 87.0 ms                                                | 85.9 ms: 1.01x faster                                                            |
| thrift                     | 796 us                                                 | 790 us: 1.01x faster                                                             |
| meteor_contest             | 108 ms                                                 | 107 ms: 1.01x faster                                                             |
| unpickle_pure_python       | 213 us                                                 | 212 us: 1.00x faster                                                             |
| mdp                        | 2.74 sec                                               | 2.73 sec: 1.00x faster                                                           |
| python_startup             | 10.6 ms                                                | 10.5 ms: 1.00x faster                                                            |
| bench_thread_pool          | 815 us                                                 | 819 us: 1.01x slower                                                             |
| pidigits                   | 186 ms                                                 | 188 ms: 1.01x slower                                                             |
| chaos                      | 58.4 ms                                                | 58.9 ms: 1.01x slower                                                            |
| json_dumps                 | 10.4 ms                                                | 10.5 ms: 1.01x slower                                                            |
| regex_dna                  | 220 ms                                                 | 222 ms: 1.01x slower                                                             |
| asyncio_tcp                | 488 ms                                                 | 494 ms: 1.01x slower                                                             |
| raytrace                   | 262 ms                                                 | 265 ms: 1.01x slower                                                             |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.82 sec: 1.01x slower                                                           |
| tornado_http               | 91.5 ms                                                | 93.1 ms: 1.02x slower                                                            |
| go                         | 142 ms                                                 | 144 ms: 1.02x slower                                                             |
| coroutines                 | 22.5 ms                                                | 23.0 ms: 1.02x slower                                                            |
| coverage                   | 83.7 ms                                                | 85.5 ms: 1.02x slower                                                            |
| python_startup_no_site     | 6.99 ms                                                | 7.14 ms: 1.02x slower                                                            |
| comprehensions             | 16.4 us                                                | 16.8 us: 1.02x slower                                                            |
| json                       | 5.20 ms                                                | 5.35 ms: 1.03x slower                                                            |
| html5lib                   | 64.5 ms                                                | 66.8 ms: 1.03x slower                                                            |
| bpe_tokeniser              | 4.69 sec                                               | 4.86 sec: 1.04x slower                                                           |
| sqlglot_parse              | 1.27 ms                                                | 1.32 ms: 1.04x slower                                                            |
| sqlglot_normalize          | 107 ms                                                 | 112 ms: 1.04x slower                                                             |
| django_template            | 34.4 ms                                                | 35.9 ms: 1.04x slower                                                            |
| async_tree_io_tg           | 825 ms                                                 | 865 ms: 1.05x slower                                                             |
| async_generators           | 433 ms                                                 | 458 ms: 1.06x slower                                                             |
| sqlglot_transpile          | 1.57 ms                                                | 1.66 ms: 1.06x slower                                                            |
| create_gc_cycles           | 1.61 ms                                                | 1.71 ms: 1.06x slower                                                            |
| nqueens                    | 80.6 ms                                                | 86.1 ms: 1.07x slower                                                            |
| json_loads                 | 27.0 us                                                | 28.8 us: 1.07x slower                                                            |
| 2to3                       | 265 ms                                                 | 283 ms: 1.07x slower                                                             |
| async_tree_io              | 843 ms                                                 | 903 ms: 1.07x slower                                                             |
| typing_runtime_protocols   | 159 us                                                 | 172 us: 1.08x slower                                                             |
| sqlglot_optimize           | 53.9 ms                                                | 58.3 ms: 1.08x slower                                                            |
| regex_compile              | 131 ms                                                 | 142 ms: 1.08x slower                                                             |
| sympy_str                  | 274 ms                                                 | 302 ms: 1.10x slower                                                             |
| sympy_expand               | 462 ms                                                 | 511 ms: 1.11x slower                                                             |
| hexiom                     | 6.13 ms                                                | 6.81 ms: 1.11x slower                                                            |
| genshi_text                | 22.9 ms                                                | 25.8 ms: 1.13x slower                                                            |
| docutils                   | 2.58 sec                                               | 2.98 sec: 1.15x slower                                                           |
| sympy_integrate            | 19.9 ms                                                | 23.0 ms: 1.16x slower                                                            |
| generators                 | 28.8 ms                                                | 33.4 ms: 1.16x slower                                                            |
| sympy_sum                  | 150 ms                                                 | 174 ms: 1.16x slower                                                             |
| pylint                     | 313 ms                                                 | 367 ms: 1.17x slower                                                             |
| genshi_xml                 | 50.3 ms                                                | 61.1 ms: 1.21x slower                                                            |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                                     |

Benchmark hidden because not significant (7): async_tree_cpu_io_mixed, deltablue, pickle_pure_python, bench_mp_pool, asyncio_websockets, pprint_pformat, pycparser
Ignored benchmarks (15) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 65.19% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.07x