# Results vs. 3.13.0

- fork: savannahostrowski
- ref: jit_invalidate_500k
- machine: linux-x86_64
- commit hash: 61a6174
- commit date: 2024-09-25
- overall geometric mean: 1.00x slower
- HPT reliability: 73.82%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240925-linux-x86_64-savannahostrowski-jit_invalidate_500k-3.14.0a0-61a6174 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 276 ms: 1.04x slower                                                            |
| docutils       | 2.58 sec                                               | 2.93 sec: 1.13x slower                                                          |
| html5lib       | 64.5 ms                                                | 62.0 ms: 1.04x faster                                                           |
| tornado_http   | 91.5 ms                                                | 94.6 ms: 1.03x slower                                                           |
| Geometric mean | (ref)                                                  | 1.04x slower                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240925-linux-x86_64-savannahostrowski-jit_invalidate_500k-3.14.0a0-61a6174 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 465 ms                                                 | 387 ms: 1.20x faster                                                            |
| async_tree_memoization     | 442 ms                                                 | 398 ms: 1.11x faster                                                            |
| async_tree_none            | 354 ms                                                 | 320 ms: 1.11x faster                                                            |
| async_tree_none_tg         | 320 ms                                                 | 309 ms: 1.04x faster                                                            |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 564 ms: 1.02x faster                                                            |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.01x slower                                                          |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 551 ms: 1.01x slower                                                            |
| coroutines                 | 22.5 ms                                                | 22.9 ms: 1.02x slower                                                           |
| asyncio_tcp                | 488 ms                                                 | 497 ms: 1.02x slower                                                            |
| async_tree_io              | 843 ms                                                 | 887 ms: 1.05x slower                                                            |
| async_tree_io_tg           | 825 ms                                                 | 876 ms: 1.06x slower                                                            |
| async_generators           | 433 ms                                                 | 460 ms: 1.06x slower                                                            |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                                    |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240925-linux-x86_64-savannahostrowski-jit_invalidate_500k-3.14.0a0-61a6174 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 69.8 ms: 1.12x faster                                                           |
| nbody          | 85.7 ms                                                | 81.4 ms: 1.05x faster                                                           |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                            |
| Geometric mean | (ref)                                                  | 1.06x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240925-linux-x86_64-savannahostrowski-jit_invalidate_500k-3.14.0a0-61a6174 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.70 ms: 1.05x faster                                                           |
| regex_dna      | 220 ms                                                 | 212 ms: 1.04x faster                                                            |
| regex_v8       | 25.3 ms                                                | 24.8 ms: 1.02x faster                                                           |
| regex_compile  | 131 ms                                                 | 142 ms: 1.09x slower                                                            |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240925-linux-x86_64-savannahostrowski-jit_invalidate_500k-3.14.0a0-61a6174 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_generate   | 87.0 ms                                                | 77.3 ms: 1.13x faster                                                           |
| xml_etree_process    | 60.4 ms                                                | 54.8 ms: 1.10x faster                                                           |
| tomli_loads          | 2.11 sec                                               | 1.92 sec: 1.10x faster                                                          |
| xml_etree_parse      | 156 ms                                                 | 146 ms: 1.07x faster                                                            |
| json_dumps           | 10.4 ms                                                | 9.81 ms: 1.06x faster                                                           |
| xml_etree_iterparse  | 102 ms                                                 | 98.7 ms: 1.03x faster                                                           |
| pickle               | 11.6 us                                                | 11.7 us: 1.01x slower                                                           |
| json_loads           | 27.0 us                                                | 27.2 us: 1.01x slower                                                           |
| pickle_pure_python   | 300 us                                                 | 303 us: 1.01x slower                                                            |
| unpickle_pure_python | 213 us                                                 | 216 us: 1.01x slower                                                            |
| pickle_list          | 5.01 us                                                | 5.11 us: 1.02x slower                                                           |
| pickle_dict          | 33.2 us                                                | 35.0 us: 1.05x slower                                                           |
| unpickle_list        | 4.96 us                                                | 5.27 us: 1.06x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                                    |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240925-linux-x86_64-savannahostrowski-jit_invalidate_500k-3.14.0a0-61a6174 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.5 ms: 1.00x faster                                                           |
| python_startup_no_site | 6.99 ms                                                | 7.06 ms: 1.01x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.00x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240925-linux-x86_64-savannahostrowski-jit_invalidate_500k-3.14.0a0-61a6174 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.74 ms: 1.14x faster                                                           |
| django_template | 34.4 ms                                                | 36.0 ms: 1.05x slower                                                           |
| genshi_text     | 22.9 ms                                                | 24.8 ms: 1.09x slower                                                           |
| genshi_xml      | 50.3 ms                                                | 58.3 ms: 1.16x slower                                                           |
| Geometric mean  | (ref)                                                  | 1.04x slower                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240925-linux-x86_64-savannahostrowski-jit_invalidate_500k-3.14.0a0-61a6174 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| deepcopy_memo              | 38.0 us                                                | 27.4 us: 1.39x faster                                                           |
| deepcopy                   | 352 us                                                 | 266 us: 1.33x faster                                                            |
| async_tree_memoization_tg  | 465 ms                                                 | 387 ms: 1.20x faster                                                            |
| deepcopy_reduce            | 3.17 us                                                | 2.67 us: 1.19x faster                                                           |
| scimark_fft                | 369 ms                                                 | 312 ms: 1.18x faster                                                            |
| richards                   | 48.1 ms                                                | 41.1 ms: 1.17x faster                                                           |
| richards_super             | 54.4 ms                                                | 46.9 ms: 1.16x faster                                                           |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.40 ms: 1.14x faster                                                           |
| mako                       | 11.1 ms                                                | 9.74 ms: 1.14x faster                                                           |
| xml_etree_generate         | 87.0 ms                                                | 77.3 ms: 1.13x faster                                                           |
| float                      | 78.5 ms                                                | 69.8 ms: 1.12x faster                                                           |
| async_tree_memoization     | 442 ms                                                 | 398 ms: 1.11x faster                                                            |
| spectral_norm              | 115 ms                                                 | 104 ms: 1.11x faster                                                            |
| async_tree_none            | 354 ms                                                 | 320 ms: 1.11x faster                                                            |
| xml_etree_process          | 60.4 ms                                                | 54.8 ms: 1.10x faster                                                           |
| tomli_loads                | 2.11 sec                                               | 1.92 sec: 1.10x faster                                                          |
| crypto_pyaes               | 73.0 ms                                                | 67.5 ms: 1.08x faster                                                           |
| mdp                        | 2.74 sec                                               | 2.54 sec: 1.08x faster                                                          |
| pathlib                    | 17.1 ms                                                | 15.9 ms: 1.07x faster                                                           |
| xml_etree_parse            | 156 ms                                                 | 146 ms: 1.07x faster                                                            |
| go                         | 142 ms                                                 | 133 ms: 1.07x faster                                                            |
| telco                      | 8.45 ms                                                | 7.96 ms: 1.06x faster                                                           |
| json_dumps                 | 10.4 ms                                                | 9.81 ms: 1.06x faster                                                           |
| bpe_tokeniser              | 4.69 sec                                               | 4.45 sec: 1.05x faster                                                          |
| nbody                      | 85.7 ms                                                | 81.4 ms: 1.05x faster                                                           |
| scimark_monte_carlo        | 66.3 ms                                                | 63.2 ms: 1.05x faster                                                           |
| regex_effbot               | 3.88 ms                                                | 3.70 ms: 1.05x faster                                                           |
| scimark_sor                | 122 ms                                                 | 117 ms: 1.05x faster                                                            |
| pyflate                    | 460 ms                                                 | 439 ms: 1.05x faster                                                            |
| html5lib                   | 64.5 ms                                                | 62.0 ms: 1.04x faster                                                           |
| scimark_lu                 | 115 ms                                                 | 111 ms: 1.04x faster                                                            |
| regex_dna                  | 220 ms                                                 | 212 ms: 1.04x faster                                                            |
| sqlite_synth               | 2.85 us                                                | 2.75 us: 1.04x faster                                                           |
| async_tree_none_tg         | 320 ms                                                 | 309 ms: 1.04x faster                                                            |
| xml_etree_iterparse        | 102 ms                                                 | 98.7 ms: 1.03x faster                                                           |
| regex_v8                   | 25.3 ms                                                | 24.8 ms: 1.02x faster                                                           |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 564 ms: 1.02x faster                                                            |
| logging_format             | 6.25 us                                                | 6.15 us: 1.02x faster                                                           |
| pycparser                  | 1.19 sec                                               | 1.18 sec: 1.01x faster                                                          |
| thrift                     | 796 us                                                 | 788 us: 1.01x faster                                                            |
| fannkuch                   | 381 ms                                                 | 377 ms: 1.01x faster                                                            |
| gc_traversal               | 3.81 ms                                                | 3.77 ms: 1.01x faster                                                           |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                                            |
| python_startup             | 10.6 ms                                                | 10.5 ms: 1.00x faster                                                           |
| pickle                     | 11.6 us                                                | 11.7 us: 1.01x slower                                                           |
| json_loads                 | 27.0 us                                                | 27.2 us: 1.01x slower                                                           |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.01x slower                                                          |
| pickle_pure_python         | 300 us                                                 | 303 us: 1.01x slower                                                            |
| logging_silent             | 102 ns                                                 | 103 ns: 1.01x slower                                                            |
| python_startup_no_site     | 6.99 ms                                                | 7.06 ms: 1.01x slower                                                           |
| chaos                      | 58.4 ms                                                | 59.1 ms: 1.01x slower                                                           |
| unpickle_pure_python       | 213 us                                                 | 216 us: 1.01x slower                                                            |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 551 ms: 1.01x slower                                                            |
| coroutines                 | 22.5 ms                                                | 22.9 ms: 1.02x slower                                                           |
| deltablue                  | 3.15 ms                                                | 3.20 ms: 1.02x slower                                                           |
| asyncio_tcp                | 488 ms                                                 | 497 ms: 1.02x slower                                                            |
| coverage                   | 83.7 ms                                                | 85.4 ms: 1.02x slower                                                           |
| pickle_list                | 5.01 us                                                | 5.11 us: 1.02x slower                                                           |
| typing_runtime_protocols   | 159 us                                                 | 164 us: 1.03x slower                                                            |
| pprint_pformat             | 1.51 sec                                               | 1.56 sec: 1.03x slower                                                          |
| tornado_http               | 91.5 ms                                                | 94.6 ms: 1.03x slower                                                           |
| bench_thread_pool          | 815 us                                                 | 844 us: 1.04x slower                                                            |
| comprehensions             | 16.4 us                                                | 17.0 us: 1.04x slower                                                           |
| 2to3                       | 265 ms                                                 | 276 ms: 1.04x slower                                                            |
| sqlglot_normalize          | 107 ms                                                 | 112 ms: 1.04x slower                                                            |
| django_template            | 34.4 ms                                                | 36.0 ms: 1.05x slower                                                           |
| async_tree_io              | 843 ms                                                 | 887 ms: 1.05x slower                                                            |
| pickle_dict                | 33.2 us                                                | 35.0 us: 1.05x slower                                                           |
| sqlglot_parse              | 1.27 ms                                                | 1.33 ms: 1.06x slower                                                           |
| raytrace                   | 262 ms                                                 | 276 ms: 1.06x slower                                                            |
| unpickle_list              | 4.96 us                                                | 5.27 us: 1.06x slower                                                           |
| async_tree_io_tg           | 825 ms                                                 | 876 ms: 1.06x slower                                                            |
| async_generators           | 433 ms                                                 | 460 ms: 1.06x slower                                                            |
| sqlglot_transpile          | 1.57 ms                                                | 1.69 ms: 1.07x slower                                                           |
| sqlglot_optimize           | 53.9 ms                                                | 58.4 ms: 1.08x slower                                                           |
| regex_compile              | 131 ms                                                 | 142 ms: 1.09x slower                                                            |
| create_gc_cycles           | 1.61 ms                                                | 1.75 ms: 1.09x slower                                                           |
| genshi_text                | 22.9 ms                                                | 24.8 ms: 1.09x slower                                                           |
| dulwich_log                | 63.0 ms                                                | 68.6 ms: 1.09x slower                                                           |
| sympy_str                  | 274 ms                                                 | 300 ms: 1.10x slower                                                            |
| sympy_expand               | 462 ms                                                 | 506 ms: 1.10x slower                                                            |
| nqueens                    | 80.6 ms                                                | 88.5 ms: 1.10x slower                                                           |
| docutils                   | 2.58 sec                                               | 2.93 sec: 1.13x slower                                                          |
| hexiom                     | 6.13 ms                                                | 6.97 ms: 1.14x slower                                                           |
| sympy_integrate            | 19.9 ms                                                | 22.9 ms: 1.15x slower                                                           |
| genshi_xml                 | 50.3 ms                                                | 58.3 ms: 1.16x slower                                                           |
| sympy_sum                  | 150 ms                                                 | 174 ms: 1.16x slower                                                            |
| generators                 | 28.8 ms                                                | 34.9 ms: 1.21x slower                                                           |
| pylint                     | 313 ms                                                 | 381 ms: 1.22x slower                                                            |
| unpack_sequence            | 42.4 ns                                                | 112 ns: 2.64x slower                                                            |
| Geometric mean             | (ref)                                                  | 1.00x slower                                                                    |

Benchmark hidden because not significant (7): json, unpickle, logging_simple, pprint_safe_repr, asyncio_websockets, bench_mp_pool, meteor_contest
Ignored benchmarks (7) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 73.82% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.07x