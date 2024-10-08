# Results vs. 3.13.0b2

- fork: savannahostrowski
- ref: jit_mem_invalidate_3
- machine: linux-x86_64
- commit hash: e6fcb4b
- commit date: 2024-08-20
- overall geometric mean: 1.05x faster
- HPT reliability: 99.97%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240820-linux-x86_64-savannahostrowski-jit_mem_invalidate_3-3.14.0a0-e6fcb4b |
|----------------|:----------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 280 ms: 1.02x slower                                                             |
| docutils       | 2.83 sec                                                   | 2.97 sec: 1.05x slower                                                           |
| html5lib       | 67.2 ms                                                    | 66.2 ms: 1.02x faster                                                            |
| tornado_http   | 94.6 ms                                                    | 93.6 ms: 1.01x faster                                                            |
| Geometric mean | (ref)                                                      | 1.01x slower                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240820-linux-x86_64-savannahostrowski-jit_mem_invalidate_3-3.14.0a0-e6fcb4b |
|----------------------------|:----------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 324 ms: 1.17x faster                                                             |
| async_tree_memoization_tg  | 444 ms                                                     | 394 ms: 1.13x faster                                                             |
| async_tree_none_tg         | 336 ms                                                     | 300 ms: 1.12x faster                                                             |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 528 ms: 1.11x faster                                                             |
| async_tree_memoization     | 463 ms                                                     | 422 ms: 1.10x faster                                                             |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 561 ms: 1.09x faster                                                             |
| async_tree_io_tg           | 936 ms                                                     | 868 ms: 1.08x faster                                                             |
| async_tree_io              | 939 ms                                                     | 899 ms: 1.04x faster                                                             |
| Geometric mean             | (ref)                                                      | 1.10x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240820-linux-x86_64-savannahostrowski-jit_mem_invalidate_3-3.14.0a0-e6fcb4b |
|----------------|:----------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 72.1 ms: 1.09x faster                                                            |
| nbody          | 88.3 ms                                                    | 81.7 ms: 1.08x faster                                                            |
| pidigits       | 191 ms                                                     | 186 ms: 1.03x faster                                                             |
| Geometric mean | (ref)                                                      | 1.07x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240820-linux-x86_64-savannahostrowski-jit_mem_invalidate_3-3.14.0a0-e6fcb4b |
|----------------|:----------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_v8       | 25.1 ms                                                    | 24.2 ms: 1.04x faster                                                            |
| regex_dna      | 221 ms                                                     | 219 ms: 1.01x faster                                                             |
| regex_effbot   | 3.67 ms                                                    | 3.64 ms: 1.01x faster                                                            |
| regex_compile  | 137 ms                                                     | 143 ms: 1.05x slower                                                             |
| Geometric mean | (ref)                                                      | 1.00x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240820-linux-x86_64-savannahostrowski-jit_mem_invalidate_3-3.14.0a0-e6fcb4b |
|----------------------|:----------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                                   | 1.89 sec: 1.12x faster                                                           |
| xml_etree_parse      | 162 ms                                                     | 148 ms: 1.10x faster                                                             |
| xml_etree_iterparse  | 107 ms                                                     | 98.9 ms: 1.09x faster                                                            |
| xml_etree_generate   | 87.4 ms                                                    | 82.4 ms: 1.06x faster                                                            |
| json_dumps           | 10.7 ms                                                    | 10.3 ms: 1.05x faster                                                            |
| xml_etree_process    | 61.2 ms                                                    | 59.1 ms: 1.03x faster                                                            |
| unpickle_pure_python | 218 us                                                     | 213 us: 1.02x faster                                                             |
| json_loads           | 28.9 us                                                    | 28.4 us: 1.02x faster                                                            |
| Geometric mean       | (ref)                                                      | 1.05x faster                                                                     |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240820-linux-x86_64-savannahostrowski-jit_mem_invalidate_3-3.14.0a0-e6fcb4b |
|------------------------|:----------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                                            |
| python_startup_no_site | 7.11 ms                                                    | 7.15 ms: 1.01x slower                                                            |
| Geometric mean         | (ref)                                                      | 1.01x faster                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240820-linux-x86_64-savannahostrowski-jit_mem_invalidate_3-3.14.0a0-e6fcb4b |
|-----------------|:----------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 10.0 ms: 1.12x faster                                                            |
| django_template | 34.8 ms                                                    | 36.0 ms: 1.04x slower                                                            |
| genshi_text     | 23.7 ms                                                    | 26.8 ms: 1.13x slower                                                            |
| genshi_xml      | 51.6 ms                                                    | 60.9 ms: 1.18x slower                                                            |
| Geometric mean  | (ref)                                                      | 1.05x slower                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240820-linux-x86_64-savannahostrowski-jit_mem_invalidate_3-3.14.0a0-e6fcb4b |
|----------------------------|:----------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| deepcopy_memo              | 39.7 us                                                    | 26.6 us: 1.49x faster                                                            |
| deepcopy                   | 367 us                                                     | 266 us: 1.38x faster                                                             |
| richards                   | 50.9 ms                                                    | 39.0 ms: 1.31x faster                                                            |
| scimark_fft                | 392 ms                                                     | 306 ms: 1.28x faster                                                             |
| richards_super             | 57.4 ms                                                    | 45.1 ms: 1.27x faster                                                            |
| deepcopy_reduce            | 3.35 us                                                    | 2.66 us: 1.26x faster                                                            |
| spectral_norm              | 116 ms                                                     | 97.4 ms: 1.19x faster                                                            |
| crypto_pyaes               | 77.5 ms                                                    | 65.3 ms: 1.19x faster                                                            |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.50 ms: 1.17x faster                                                            |
| async_tree_none            | 378 ms                                                     | 324 ms: 1.17x faster                                                             |
| async_tree_memoization_tg  | 444 ms                                                     | 394 ms: 1.13x faster                                                             |
| tomli_loads                | 2.12 sec                                                   | 1.89 sec: 1.12x faster                                                           |
| async_tree_none_tg         | 336 ms                                                     | 300 ms: 1.12x faster                                                             |
| pyflate                    | 484 ms                                                     | 432 ms: 1.12x faster                                                             |
| mako                       | 11.2 ms                                                    | 10.0 ms: 1.12x faster                                                            |
| scimark_lu                 | 122 ms                                                     | 109 ms: 1.12x faster                                                             |
| scimark_sor                | 127 ms                                                     | 114 ms: 1.11x faster                                                             |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 528 ms: 1.11x faster                                                             |
| scimark_monte_carlo        | 69.2 ms                                                    | 62.5 ms: 1.11x faster                                                            |
| async_tree_memoization     | 463 ms                                                     | 422 ms: 1.10x faster                                                             |
| xml_etree_parse            | 162 ms                                                     | 148 ms: 1.10x faster                                                             |
| bpe_tokeniser              | 5.02 sec                                                   | 4.59 sec: 1.10x faster                                                           |
| float                      | 78.9 ms                                                    | 72.1 ms: 1.09x faster                                                            |
| fannkuch                   | 402 ms                                                     | 368 ms: 1.09x faster                                                             |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 561 ms: 1.09x faster                                                             |
| xml_etree_iterparse        | 107 ms                                                     | 98.9 ms: 1.09x faster                                                            |
| pathlib                    | 17.3 ms                                                    | 16.0 ms: 1.08x faster                                                            |
| gc_traversal               | 3.98 ms                                                    | 3.67 ms: 1.08x faster                                                            |
| coverage                   | 93.1 ms                                                    | 86.0 ms: 1.08x faster                                                            |
| nbody                      | 88.3 ms                                                    | 81.7 ms: 1.08x faster                                                            |
| async_tree_io_tg           | 936 ms                                                     | 868 ms: 1.08x faster                                                             |
| logging_format             | 6.47 us                                                    | 6.01 us: 1.08x faster                                                            |
| telco                      | 8.41 ms                                                    | 7.84 ms: 1.07x faster                                                            |
| mdp                        | 2.79 sec                                                   | 2.60 sec: 1.07x faster                                                           |
| xml_etree_generate         | 87.4 ms                                                    | 82.4 ms: 1.06x faster                                                            |
| create_gc_cycles           | 1.82 ms                                                    | 1.72 ms: 1.06x faster                                                            |
| chaos                      | 61.3 ms                                                    | 58.2 ms: 1.05x faster                                                            |
| logging_simple             | 5.74 us                                                    | 5.46 us: 1.05x faster                                                            |
| logging_silent             | 105 ns                                                     | 100.0 ns: 1.05x faster                                                           |
| json_dumps                 | 10.7 ms                                                    | 10.3 ms: 1.05x faster                                                            |
| async_tree_io              | 939 ms                                                     | 899 ms: 1.04x faster                                                             |
| pprint_safe_repr           | 758 ms                                                     | 730 ms: 1.04x faster                                                             |
| regex_v8                   | 25.1 ms                                                    | 24.2 ms: 1.04x faster                                                            |
| thrift                     | 823 us                                                     | 793 us: 1.04x faster                                                             |
| xml_etree_process          | 61.2 ms                                                    | 59.1 ms: 1.03x faster                                                            |
| meteor_contest             | 110 ms                                                     | 106 ms: 1.03x faster                                                             |
| pprint_pformat             | 1.56 sec                                                   | 1.51 sec: 1.03x faster                                                           |
| pidigits                   | 191 ms                                                     | 186 ms: 1.03x faster                                                             |
| asyncio_tcp                | 508 ms                                                     | 496 ms: 1.02x faster                                                             |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.80 sec: 1.02x faster                                                           |
| asyncio_websockets         | 567 ms                                                     | 554 ms: 1.02x faster                                                             |
| deltablue                  | 3.25 ms                                                    | 3.18 ms: 1.02x faster                                                            |
| unpickle_pure_python       | 218 us                                                     | 213 us: 1.02x faster                                                             |
| bench_thread_pool          | 834 us                                                     | 817 us: 1.02x faster                                                             |
| python_startup             | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                                            |
| coroutines                 | 23.2 ms                                                    | 22.8 ms: 1.02x faster                                                            |
| html5lib                   | 67.2 ms                                                    | 66.2 ms: 1.02x faster                                                            |
| json_loads                 | 28.9 us                                                    | 28.4 us: 1.02x faster                                                            |
| tornado_http               | 94.6 ms                                                    | 93.6 ms: 1.01x faster                                                            |
| regex_dna                  | 221 ms                                                     | 219 ms: 1.01x faster                                                             |
| regex_effbot               | 3.67 ms                                                    | 3.64 ms: 1.01x faster                                                            |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.00x slower                                                            |
| python_startup_no_site     | 7.11 ms                                                    | 7.15 ms: 1.01x slower                                                            |
| json                       | 5.31 ms                                                    | 5.40 ms: 1.02x slower                                                            |
| sqlglot_normalize          | 110 ms                                                     | 112 ms: 1.02x slower                                                             |
| 2to3                       | 274 ms                                                     | 280 ms: 1.02x slower                                                             |
| sqlglot_transpile          | 1.63 ms                                                    | 1.68 ms: 1.03x slower                                                            |
| django_template            | 34.8 ms                                                    | 36.0 ms: 1.04x slower                                                            |
| typing_runtime_protocols   | 165 us                                                     | 171 us: 1.04x slower                                                             |
| sqlglot_optimize           | 55.5 ms                                                    | 57.7 ms: 1.04x slower                                                            |
| regex_compile              | 137 ms                                                     | 143 ms: 1.05x slower                                                             |
| async_generators           | 442 ms                                                     | 463 ms: 1.05x slower                                                             |
| docutils                   | 2.83 sec                                                   | 2.97 sec: 1.05x slower                                                           |
| pycparser                  | 1.16 sec                                                   | 1.22 sec: 1.05x slower                                                           |
| nqueens                    | 81.4 ms                                                    | 86.3 ms: 1.06x slower                                                            |
| sympy_str                  | 282 ms                                                     | 300 ms: 1.06x slower                                                             |
| sympy_expand               | 473 ms                                                     | 508 ms: 1.07x slower                                                             |
| hexiom                     | 6.30 ms                                                    | 6.84 ms: 1.09x slower                                                            |
| sympy_sum                  | 156 ms                                                     | 173 ms: 1.11x slower                                                             |
| sympy_integrate            | 20.5 ms                                                    | 22.8 ms: 1.11x slower                                                            |
| generators                 | 29.6 ms                                                    | 33.5 ms: 1.13x slower                                                            |
| genshi_text                | 23.7 ms                                                    | 26.8 ms: 1.13x slower                                                            |
| pylint                     | 317 ms                                                     | 368 ms: 1.16x slower                                                             |
| genshi_xml                 | 51.6 ms                                                    | 60.9 ms: 1.18x slower                                                            |
| Geometric mean             | (ref)                                                      | 1.05x faster                                                                     |

Benchmark hidden because not significant (5): pickle_pure_python, comprehensions, raytrace, sqlglot_parse, go
Ignored benchmarks (14) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 99.97% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.07x