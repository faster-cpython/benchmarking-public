# Results vs. 3.13.0

- fork: savannahostrowski
- ref: jit_mem_invalidate_1
- machine: linux-x86_64
- commit hash: 071a1a4
- commit date: 2024-08-20
- overall geometric mean: 1.01x faster
- HPT reliability: 79.18%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240820-linux-x86_64-savannahostrowski-jit_mem_invalidate_1-3.14.0a0-071a1a4 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 280 ms: 1.06x slower                                                             |
| docutils       | 2.58 sec                                               | 2.97 sec: 1.15x slower                                                           |
| html5lib       | 64.5 ms                                                | 67.2 ms: 1.04x slower                                                            |
| tornado_http   | 91.5 ms                                                | 93.2 ms: 1.02x slower                                                            |
| Geometric mean | (ref)                                                  | 1.07x slower                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240820-linux-x86_64-savannahostrowski-jit_mem_invalidate_1-3.14.0a0-071a1a4 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 465 ms                                                 | 393 ms: 1.18x faster                                                             |
| async_tree_none            | 354 ms                                                 | 321 ms: 1.10x faster                                                             |
| async_tree_none_tg         | 320 ms                                                 | 299 ms: 1.07x faster                                                             |
| async_tree_memoization     | 442 ms                                                 | 427 ms: 1.04x faster                                                             |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 529 ms: 1.03x faster                                                             |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 562 ms: 1.02x faster                                                             |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.79 sec: 1.00x slower                                                           |
| asyncio_websockets         | 555 ms                                                 | 559 ms: 1.01x slower                                                             |
| asyncio_tcp                | 488 ms                                                 | 495 ms: 1.01x slower                                                             |
| coroutines                 | 22.5 ms                                                | 23.0 ms: 1.02x slower                                                            |
| async_tree_io_tg           | 825 ms                                                 | 861 ms: 1.04x slower                                                             |
| async_generators           | 433 ms                                                 | 456 ms: 1.05x slower                                                             |
| async_tree_io              | 843 ms                                                 | 900 ms: 1.07x slower                                                             |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240820-linux-x86_64-savannahostrowski-jit_mem_invalidate_1-3.14.0a0-071a1a4 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 72.1 ms: 1.09x faster                                                            |
| nbody          | 85.7 ms                                                | 79.9 ms: 1.07x faster                                                            |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                             |
| Geometric mean | (ref)                                                  | 1.05x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240820-linux-x86_64-savannahostrowski-jit_mem_invalidate_1-3.14.0a0-071a1a4 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.56 ms: 1.09x faster                                                            |
| regex_v8       | 25.3 ms                                                | 24.4 ms: 1.04x faster                                                            |
| regex_dna      | 220 ms                                                 | 218 ms: 1.01x faster                                                             |
| regex_compile  | 131 ms                                                 | 141 ms: 1.08x slower                                                             |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240820-linux-x86_64-savannahostrowski-jit_mem_invalidate_1-3.14.0a0-071a1a4 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| tomli_loads          | 2.11 sec                                               | 1.88 sec: 1.12x faster                                                           |
| xml_etree_generate   | 87.0 ms                                                | 82.6 ms: 1.05x faster                                                            |
| xml_etree_parse      | 156 ms                                                 | 148 ms: 1.05x faster                                                             |
| xml_etree_process    | 60.4 ms                                                | 58.0 ms: 1.04x faster                                                            |
| xml_etree_iterparse  | 102 ms                                                 | 98.4 ms: 1.04x faster                                                            |
| unpickle_pure_python | 213 us                                                 | 212 us: 1.01x faster                                                             |
| pickle_pure_python   | 300 us                                                 | 302 us: 1.01x slower                                                             |
| json_loads           | 27.0 us                                                | 28.7 us: 1.06x slower                                                            |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                                     |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240820-linux-x86_64-savannahostrowski-jit_mem_invalidate_1-3.14.0a0-071a1a4 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.5 ms: 1.01x faster                                                            |
| python_startup_no_site | 6.99 ms                                                | 7.13 ms: 1.02x slower                                                            |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240820-linux-x86_64-savannahostrowski-jit_mem_invalidate_1-3.14.0a0-071a1a4 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.88 ms: 1.12x faster                                                            |
| django_template | 34.4 ms                                                | 36.2 ms: 1.05x slower                                                            |
| genshi_text     | 22.9 ms                                                | 26.2 ms: 1.14x slower                                                            |
| genshi_xml      | 50.3 ms                                                | 62.0 ms: 1.23x slower                                                            |
| Geometric mean  | (ref)                                                  | 1.07x slower                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240820-linux-x86_64-savannahostrowski-jit_mem_invalidate_1-3.14.0a0-071a1a4 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| deepcopy_memo              | 38.0 us                                                | 26.3 us: 1.45x faster                                                            |
| deepcopy                   | 352 us                                                 | 262 us: 1.35x faster                                                             |
| richards                   | 48.1 ms                                                | 39.1 ms: 1.23x faster                                                            |
| deepcopy_reduce            | 3.17 us                                                | 2.64 us: 1.20x faster                                                            |
| richards_super             | 54.4 ms                                                | 45.4 ms: 1.20x faster                                                            |
| scimark_fft                | 369 ms                                                 | 308 ms: 1.20x faster                                                             |
| async_tree_memoization_tg  | 465 ms                                                 | 393 ms: 1.18x faster                                                             |
| spectral_norm              | 115 ms                                                 | 100 ms: 1.15x faster                                                             |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.46 ms: 1.13x faster                                                            |
| tomli_loads                | 2.11 sec                                               | 1.88 sec: 1.12x faster                                                           |
| mako                       | 11.1 ms                                                | 9.88 ms: 1.12x faster                                                            |
| crypto_pyaes               | 73.0 ms                                                | 65.7 ms: 1.11x faster                                                            |
| async_tree_none            | 354 ms                                                 | 321 ms: 1.10x faster                                                             |
| regex_effbot               | 3.88 ms                                                | 3.56 ms: 1.09x faster                                                            |
| telco                      | 8.45 ms                                                | 7.76 ms: 1.09x faster                                                            |
| float                      | 78.5 ms                                                | 72.1 ms: 1.09x faster                                                            |
| nbody                      | 85.7 ms                                                | 79.9 ms: 1.07x faster                                                            |
| async_tree_none_tg         | 320 ms                                                 | 299 ms: 1.07x faster                                                             |
| pathlib                    | 17.1 ms                                                | 16.0 ms: 1.07x faster                                                            |
| scimark_monte_carlo        | 66.3 ms                                                | 62.1 ms: 1.07x faster                                                            |
| scimark_sor                | 122 ms                                                 | 115 ms: 1.06x faster                                                             |
| pyflate                    | 460 ms                                                 | 434 ms: 1.06x faster                                                             |
| scimark_lu                 | 115 ms                                                 | 109 ms: 1.05x faster                                                             |
| xml_etree_generate         | 87.0 ms                                                | 82.6 ms: 1.05x faster                                                            |
| xml_etree_parse            | 156 ms                                                 | 148 ms: 1.05x faster                                                             |
| logging_simple             | 5.66 us                                                | 5.41 us: 1.05x faster                                                            |
| xml_etree_process          | 60.4 ms                                                | 58.0 ms: 1.04x faster                                                            |
| bpe_tokeniser              | 4.69 sec                                               | 4.52 sec: 1.04x faster                                                           |
| xml_etree_iterparse        | 102 ms                                                 | 98.4 ms: 1.04x faster                                                            |
| async_tree_memoization     | 442 ms                                                 | 427 ms: 1.04x faster                                                             |
| logging_format             | 6.25 us                                                | 6.03 us: 1.04x faster                                                            |
| logging_silent             | 102 ns                                                 | 98.5 ns: 1.04x faster                                                            |
| regex_v8                   | 25.3 ms                                                | 24.4 ms: 1.04x faster                                                            |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 529 ms: 1.03x faster                                                             |
| pycparser                  | 1.19 sec                                               | 1.17 sec: 1.02x faster                                                           |
| mdp                        | 2.74 sec                                               | 2.68 sec: 1.02x faster                                                           |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 562 ms: 1.02x faster                                                             |
| meteor_contest             | 108 ms                                                 | 106 ms: 1.02x faster                                                             |
| gc_traversal               | 3.81 ms                                                | 3.75 ms: 1.02x faster                                                            |
| pprint_safe_repr           | 744 ms                                                 | 733 ms: 1.02x faster                                                             |
| thrift                     | 796 us                                                 | 785 us: 1.01x faster                                                             |
| fannkuch                   | 381 ms                                                 | 377 ms: 1.01x faster                                                             |
| regex_dna                  | 220 ms                                                 | 218 ms: 1.01x faster                                                             |
| pprint_pformat             | 1.51 sec                                               | 1.50 sec: 1.01x faster                                                           |
| unpickle_pure_python       | 213 us                                                 | 212 us: 1.01x faster                                                             |
| python_startup             | 10.6 ms                                                | 10.5 ms: 1.01x faster                                                            |
| deltablue                  | 3.15 ms                                                | 3.14 ms: 1.00x faster                                                            |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                                             |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.79 sec: 1.00x slower                                                           |
| asyncio_websockets         | 555 ms                                                 | 559 ms: 1.01x slower                                                             |
| pickle_pure_python         | 300 us                                                 | 302 us: 1.01x slower                                                             |
| asyncio_tcp                | 488 ms                                                 | 495 ms: 1.01x slower                                                             |
| comprehensions             | 16.4 us                                                | 16.7 us: 1.02x slower                                                            |
| raytrace                   | 262 ms                                                 | 266 ms: 1.02x slower                                                             |
| tornado_http               | 91.5 ms                                                | 93.2 ms: 1.02x slower                                                            |
| python_startup_no_site     | 6.99 ms                                                | 7.13 ms: 1.02x slower                                                            |
| go                         | 142 ms                                                 | 144 ms: 1.02x slower                                                             |
| coroutines                 | 22.5 ms                                                | 23.0 ms: 1.02x slower                                                            |
| coverage                   | 83.7 ms                                                | 86.0 ms: 1.03x slower                                                            |
| json                       | 5.20 ms                                                | 5.34 ms: 1.03x slower                                                            |
| sqlglot_parse              | 1.27 ms                                                | 1.31 ms: 1.04x slower                                                            |
| html5lib                   | 64.5 ms                                                | 67.2 ms: 1.04x slower                                                            |
| async_tree_io_tg           | 825 ms                                                 | 861 ms: 1.04x slower                                                             |
| django_template            | 34.4 ms                                                | 36.2 ms: 1.05x slower                                                            |
| async_generators           | 433 ms                                                 | 456 ms: 1.05x slower                                                             |
| 2to3                       | 265 ms                                                 | 280 ms: 1.06x slower                                                             |
| sqlglot_normalize          | 107 ms                                                 | 113 ms: 1.06x slower                                                             |
| nqueens                    | 80.6 ms                                                | 85.2 ms: 1.06x slower                                                            |
| sqlglot_transpile          | 1.57 ms                                                | 1.67 ms: 1.06x slower                                                            |
| json_loads                 | 27.0 us                                                | 28.7 us: 1.06x slower                                                            |
| async_tree_io              | 843 ms                                                 | 900 ms: 1.07x slower                                                             |
| sqlglot_optimize           | 53.9 ms                                                | 57.8 ms: 1.07x slower                                                            |
| typing_runtime_protocols   | 159 us                                                 | 171 us: 1.08x slower                                                             |
| create_gc_cycles           | 1.61 ms                                                | 1.73 ms: 1.08x slower                                                            |
| regex_compile              | 131 ms                                                 | 141 ms: 1.08x slower                                                             |
| sympy_expand               | 462 ms                                                 | 510 ms: 1.11x slower                                                             |
| sympy_str                  | 274 ms                                                 | 304 ms: 1.11x slower                                                             |
| hexiom                     | 6.13 ms                                                | 6.90 ms: 1.13x slower                                                            |
| genshi_text                | 22.9 ms                                                | 26.2 ms: 1.14x slower                                                            |
| docutils                   | 2.58 sec                                               | 2.97 sec: 1.15x slower                                                           |
| sympy_integrate            | 19.9 ms                                                | 23.1 ms: 1.16x slower                                                            |
| generators                 | 28.8 ms                                                | 33.6 ms: 1.17x slower                                                            |
| pylint                     | 313 ms                                                 | 367 ms: 1.17x slower                                                             |
| sympy_sum                  | 150 ms                                                 | 177 ms: 1.18x slower                                                             |
| genshi_xml                 | 50.3 ms                                                | 62.0 ms: 1.23x slower                                                            |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                                     |

Benchmark hidden because not significant (4): bench_mp_pool, bench_thread_pool, json_dumps, chaos
Ignored benchmarks (15) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 79.18% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.08x