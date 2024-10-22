# Results vs. 3.13.0

- fork: savannahostrowski
- ref: jit_mem_invalidate_3
- machine: linux-x86_64
- commit hash: e6fcb4b
- commit date: 2024-08-20
- overall geometric mean: 1.01x faster
- HPT reliability: 73.30%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240820-linux-x86_64-savannahostrowski-jit_mem_invalidate_3-3.14.0a0-e6fcb4b |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 280 ms: 1.06x slower                                                             |
| docutils       | 2.58 sec                                               | 2.97 sec: 1.15x slower                                                           |
| html5lib       | 64.5 ms                                                | 66.2 ms: 1.03x slower                                                            |
| tornado_http   | 91.5 ms                                                | 93.6 ms: 1.02x slower                                                            |
| Geometric mean | (ref)                                                  | 1.06x slower                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240820-linux-x86_64-savannahostrowski-jit_mem_invalidate_3-3.14.0a0-e6fcb4b |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 465 ms                                                 | 394 ms: 1.18x faster                                                             |
| async_tree_none            | 354 ms                                                 | 324 ms: 1.09x faster                                                             |
| async_tree_none_tg         | 320 ms                                                 | 300 ms: 1.07x faster                                                             |
| async_tree_memoization     | 442 ms                                                 | 422 ms: 1.05x faster                                                             |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 528 ms: 1.03x faster                                                             |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 561 ms: 1.02x faster                                                             |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.80 sec: 1.00x slower                                                           |
| coroutines                 | 22.5 ms                                                | 22.8 ms: 1.01x slower                                                            |
| asyncio_tcp                | 488 ms                                                 | 496 ms: 1.02x slower                                                             |
| async_tree_io_tg           | 825 ms                                                 | 868 ms: 1.05x slower                                                             |
| async_tree_io              | 843 ms                                                 | 899 ms: 1.07x slower                                                             |
| async_generators           | 433 ms                                                 | 463 ms: 1.07x slower                                                             |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                                     |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240820-linux-x86_64-savannahostrowski-jit_mem_invalidate_3-3.14.0a0-e6fcb4b |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 72.1 ms: 1.09x faster                                                            |
| nbody          | 85.7 ms                                                | 81.7 ms: 1.05x faster                                                            |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                             |
| Geometric mean | (ref)                                                  | 1.05x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240820-linux-x86_64-savannahostrowski-jit_mem_invalidate_3-3.14.0a0-e6fcb4b |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.64 ms: 1.07x faster                                                            |
| regex_v8       | 25.3 ms                                                | 24.2 ms: 1.05x faster                                                            |
| regex_dna      | 220 ms                                                 | 219 ms: 1.00x faster                                                             |
| regex_compile  | 131 ms                                                 | 143 ms: 1.09x slower                                                             |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240820-linux-x86_64-savannahostrowski-jit_mem_invalidate_3-3.14.0a0-e6fcb4b |
|---------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| tomli_loads         | 2.11 sec                                               | 1.89 sec: 1.12x faster                                                           |
| xml_etree_parse     | 156 ms                                                 | 148 ms: 1.06x faster                                                             |
| xml_etree_generate  | 87.0 ms                                                | 82.4 ms: 1.06x faster                                                            |
| xml_etree_iterparse | 102 ms                                                 | 98.9 ms: 1.03x faster                                                            |
| xml_etree_process   | 60.4 ms                                                | 59.1 ms: 1.02x faster                                                            |
| json_dumps          | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                            |
| json_loads          | 27.0 us                                                | 28.4 us: 1.05x slower                                                            |
| Geometric mean      | (ref)                                                  | 1.03x faster                                                                     |

Benchmark hidden because not significant (2): unpickle_pure_python, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240820-linux-x86_64-savannahostrowski-jit_mem_invalidate_3-3.14.0a0-e6fcb4b |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.5 ms: 1.00x faster                                                            |
| python_startup_no_site | 6.99 ms                                                | 7.15 ms: 1.02x slower                                                            |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240820-linux-x86_64-savannahostrowski-jit_mem_invalidate_3-3.14.0a0-e6fcb4b |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 10.0 ms: 1.11x faster                                                            |
| django_template | 34.4 ms                                                | 36.0 ms: 1.05x slower                                                            |
| genshi_text     | 22.9 ms                                                | 26.8 ms: 1.17x slower                                                            |
| genshi_xml      | 50.3 ms                                                | 60.9 ms: 1.21x slower                                                            |
| Geometric mean  | (ref)                                                  | 1.08x slower                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240820-linux-x86_64-savannahostrowski-jit_mem_invalidate_3-3.14.0a0-e6fcb4b |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| deepcopy_memo              | 38.0 us                                                | 26.6 us: 1.43x faster                                                            |
| deepcopy                   | 352 us                                                 | 266 us: 1.33x faster                                                             |
| richards                   | 48.1 ms                                                | 39.0 ms: 1.23x faster                                                            |
| richards_super             | 54.4 ms                                                | 45.1 ms: 1.21x faster                                                            |
| scimark_fft                | 369 ms                                                 | 306 ms: 1.20x faster                                                             |
| deepcopy_reduce            | 3.17 us                                                | 2.66 us: 1.19x faster                                                            |
| spectral_norm              | 115 ms                                                 | 97.4 ms: 1.18x faster                                                            |
| async_tree_memoization_tg  | 465 ms                                                 | 394 ms: 1.18x faster                                                             |
| tomli_loads                | 2.11 sec                                               | 1.89 sec: 1.12x faster                                                           |
| crypto_pyaes               | 73.0 ms                                                | 65.3 ms: 1.12x faster                                                            |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.50 ms: 1.12x faster                                                            |
| mako                       | 11.1 ms                                                | 10.0 ms: 1.11x faster                                                            |
| async_tree_none            | 354 ms                                                 | 324 ms: 1.09x faster                                                             |
| float                      | 78.5 ms                                                | 72.1 ms: 1.09x faster                                                            |
| telco                      | 8.45 ms                                                | 7.84 ms: 1.08x faster                                                            |
| scimark_sor                | 122 ms                                                 | 114 ms: 1.07x faster                                                             |
| pathlib                    | 17.1 ms                                                | 16.0 ms: 1.07x faster                                                            |
| regex_effbot               | 3.88 ms                                                | 3.64 ms: 1.07x faster                                                            |
| async_tree_none_tg         | 320 ms                                                 | 300 ms: 1.07x faster                                                             |
| pyflate                    | 460 ms                                                 | 432 ms: 1.06x faster                                                             |
| scimark_monte_carlo        | 66.3 ms                                                | 62.5 ms: 1.06x faster                                                            |
| xml_etree_parse            | 156 ms                                                 | 148 ms: 1.06x faster                                                             |
| xml_etree_generate         | 87.0 ms                                                | 82.4 ms: 1.06x faster                                                            |
| scimark_lu                 | 115 ms                                                 | 109 ms: 1.06x faster                                                             |
| mdp                        | 2.74 sec                                               | 2.60 sec: 1.05x faster                                                           |
| nbody                      | 85.7 ms                                                | 81.7 ms: 1.05x faster                                                            |
| async_tree_memoization     | 442 ms                                                 | 422 ms: 1.05x faster                                                             |
| regex_v8                   | 25.3 ms                                                | 24.2 ms: 1.05x faster                                                            |
| logging_format             | 6.25 us                                                | 6.01 us: 1.04x faster                                                            |
| logging_simple             | 5.66 us                                                | 5.46 us: 1.04x faster                                                            |
| gc_traversal               | 3.81 ms                                                | 3.67 ms: 1.04x faster                                                            |
| fannkuch                   | 381 ms                                                 | 368 ms: 1.03x faster                                                             |
| xml_etree_iterparse        | 102 ms                                                 | 98.9 ms: 1.03x faster                                                            |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 528 ms: 1.03x faster                                                             |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 561 ms: 1.02x faster                                                             |
| bpe_tokeniser              | 4.69 sec                                               | 4.59 sec: 1.02x faster                                                           |
| xml_etree_process          | 60.4 ms                                                | 59.1 ms: 1.02x faster                                                            |
| logging_silent             | 102 ns                                                 | 100.0 ns: 1.02x faster                                                           |
| pprint_safe_repr           | 744 ms                                                 | 730 ms: 1.02x faster                                                             |
| json_dumps                 | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                            |
| meteor_contest             | 108 ms                                                 | 106 ms: 1.01x faster                                                             |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                                             |
| regex_dna                  | 220 ms                                                 | 219 ms: 1.00x faster                                                             |
| python_startup             | 10.6 ms                                                | 10.5 ms: 1.00x faster                                                            |
| bench_thread_pool          | 815 us                                                 | 817 us: 1.00x slower                                                             |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.80 sec: 1.00x slower                                                           |
| deltablue                  | 3.15 ms                                                | 3.18 ms: 1.01x slower                                                            |
| comprehensions             | 16.4 us                                                | 16.6 us: 1.01x slower                                                            |
| coroutines                 | 22.5 ms                                                | 22.8 ms: 1.01x slower                                                            |
| asyncio_tcp                | 488 ms                                                 | 496 ms: 1.02x slower                                                             |
| raytrace                   | 262 ms                                                 | 267 ms: 1.02x slower                                                             |
| pycparser                  | 1.19 sec                                               | 1.22 sec: 1.02x slower                                                           |
| tornado_http               | 91.5 ms                                                | 93.6 ms: 1.02x slower                                                            |
| python_startup_no_site     | 6.99 ms                                                | 7.15 ms: 1.02x slower                                                            |
| html5lib                   | 64.5 ms                                                | 66.2 ms: 1.03x slower                                                            |
| go                         | 142 ms                                                 | 145 ms: 1.03x slower                                                             |
| coverage                   | 83.7 ms                                                | 86.0 ms: 1.03x slower                                                            |
| json                       | 5.20 ms                                                | 5.40 ms: 1.04x slower                                                            |
| sqlglot_parse              | 1.27 ms                                                | 1.32 ms: 1.04x slower                                                            |
| sqlglot_normalize          | 107 ms                                                 | 112 ms: 1.05x slower                                                             |
| django_template            | 34.4 ms                                                | 36.0 ms: 1.05x slower                                                            |
| async_tree_io_tg           | 825 ms                                                 | 868 ms: 1.05x slower                                                             |
| json_loads                 | 27.0 us                                                | 28.4 us: 1.05x slower                                                            |
| 2to3                       | 265 ms                                                 | 280 ms: 1.06x slower                                                             |
| async_tree_io              | 843 ms                                                 | 899 ms: 1.07x slower                                                             |
| create_gc_cycles           | 1.61 ms                                                | 1.72 ms: 1.07x slower                                                            |
| sqlglot_transpile          | 1.57 ms                                                | 1.68 ms: 1.07x slower                                                            |
| sqlglot_optimize           | 53.9 ms                                                | 57.7 ms: 1.07x slower                                                            |
| async_generators           | 433 ms                                                 | 463 ms: 1.07x slower                                                             |
| nqueens                    | 80.6 ms                                                | 86.3 ms: 1.07x slower                                                            |
| typing_runtime_protocols   | 159 us                                                 | 171 us: 1.07x slower                                                             |
| regex_compile              | 131 ms                                                 | 143 ms: 1.09x slower                                                             |
| sympy_str                  | 274 ms                                                 | 300 ms: 1.10x slower                                                             |
| sympy_expand               | 462 ms                                                 | 508 ms: 1.10x slower                                                             |
| hexiom                     | 6.13 ms                                                | 6.84 ms: 1.12x slower                                                            |
| sympy_integrate            | 19.9 ms                                                | 22.8 ms: 1.15x slower                                                            |
| docutils                   | 2.58 sec                                               | 2.97 sec: 1.15x slower                                                           |
| sympy_sum                  | 150 ms                                                 | 173 ms: 1.15x slower                                                             |
| generators                 | 28.8 ms                                                | 33.5 ms: 1.16x slower                                                            |
| genshi_text                | 22.9 ms                                                | 26.8 ms: 1.17x slower                                                            |
| pylint                     | 313 ms                                                 | 368 ms: 1.18x slower                                                             |
| genshi_xml                 | 50.3 ms                                                | 60.9 ms: 1.21x slower                                                            |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                                     |

Benchmark hidden because not significant (7): thrift, chaos, pprint_pformat, asyncio_websockets, bench_mp_pool, unpickle_pure_python, pickle_pure_python
Ignored benchmarks (15) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 73.30% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.07x