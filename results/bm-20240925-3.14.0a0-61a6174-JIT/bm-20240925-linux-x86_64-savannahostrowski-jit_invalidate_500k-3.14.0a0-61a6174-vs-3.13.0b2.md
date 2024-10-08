# Results vs. 3.13.0b2

- fork: savannahostrowski
- ref: jit_invalidate_500k
- machine: linux-x86_64
- commit hash: 61a6174
- commit date: 2024-09-25
- overall geometric mean: 1.04x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240925-linux-x86_64-savannahostrowski-jit_invalidate_500k-3.14.0a0-61a6174 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 276 ms: 1.01x slower                                                            |
| docutils       | 2.83 sec                                                   | 2.93 sec: 1.04x slower                                                          |
| html5lib       | 67.2 ms                                                    | 62.0 ms: 1.08x faster                                                           |
| Geometric mean | (ref)                                                      | 1.01x faster                                                                    |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240925-linux-x86_64-savannahostrowski-jit_invalidate_500k-3.14.0a0-61a6174 |
|----------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 320 ms: 1.18x faster                                                            |
| async_tree_memoization     | 463 ms                                                     | 398 ms: 1.16x faster                                                            |
| async_tree_memoization_tg  | 444 ms                                                     | 387 ms: 1.15x faster                                                            |
| async_tree_none_tg         | 336 ms                                                     | 309 ms: 1.09x faster                                                            |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 564 ms: 1.08x faster                                                            |
| async_tree_io_tg           | 936 ms                                                     | 876 ms: 1.07x faster                                                            |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 551 ms: 1.07x faster                                                            |
| async_tree_io              | 939 ms                                                     | 887 ms: 1.06x faster                                                            |
| Geometric mean             | (ref)                                                      | 1.11x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240925-linux-x86_64-savannahostrowski-jit_invalidate_500k-3.14.0a0-61a6174 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 69.8 ms: 1.13x faster                                                           |
| nbody          | 88.3 ms                                                    | 81.4 ms: 1.08x faster                                                           |
| pidigits       | 191 ms                                                     | 186 ms: 1.03x faster                                                            |
| Geometric mean | (ref)                                                      | 1.08x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240925-linux-x86_64-savannahostrowski-jit_invalidate_500k-3.14.0a0-61a6174 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_dna      | 221 ms                                                     | 212 ms: 1.04x faster                                                            |
| regex_v8       | 25.1 ms                                                    | 24.8 ms: 1.01x faster                                                           |
| regex_effbot   | 3.67 ms                                                    | 3.70 ms: 1.01x slower                                                           |
| regex_compile  | 137 ms                                                     | 142 ms: 1.04x slower                                                            |
| Geometric mean | (ref)                                                      | 1.00x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240925-linux-x86_64-savannahostrowski-jit_invalidate_500k-3.14.0a0-61a6174 |
|----------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_generate   | 87.4 ms                                                    | 77.3 ms: 1.13x faster                                                           |
| xml_etree_process    | 61.2 ms                                                    | 54.8 ms: 1.12x faster                                                           |
| xml_etree_parse      | 162 ms                                                     | 146 ms: 1.11x faster                                                            |
| tomli_loads          | 2.12 sec                                                   | 1.92 sec: 1.10x faster                                                          |
| json_dumps           | 10.7 ms                                                    | 9.81 ms: 1.09x faster                                                           |
| xml_etree_iterparse  | 107 ms                                                     | 98.7 ms: 1.09x faster                                                           |
| json_loads           | 28.9 us                                                    | 27.2 us: 1.06x faster                                                           |
| unpickle             | 15.1 us                                                    | 14.8 us: 1.02x faster                                                           |
| unpickle_list        | 5.34 us                                                    | 5.27 us: 1.01x faster                                                           |
| unpickle_pure_python | 218 us                                                     | 216 us: 1.01x faster                                                            |
| pickle_pure_python   | 305 us                                                     | 303 us: 1.01x faster                                                            |
| pickle_dict          | 34.8 us                                                    | 35.0 us: 1.00x slower                                                           |
| pickle               | 11.5 us                                                    | 11.7 us: 1.02x slower                                                           |
| Geometric mean       | (ref)                                                      | 1.05x faster                                                                    |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240925-linux-x86_64-savannahostrowski-jit_invalidate_500k-3.14.0a0-61a6174 |
|------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                                           |
| python_startup_no_site | 7.11 ms                                                    | 7.06 ms: 1.01x faster                                                           |
| Geometric mean         | (ref)                                                      | 1.01x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240925-linux-x86_64-savannahostrowski-jit_invalidate_500k-3.14.0a0-61a6174 |
|-----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.74 ms: 1.15x faster                                                           |
| django_template | 34.8 ms                                                    | 36.0 ms: 1.03x slower                                                           |
| genshi_text     | 23.7 ms                                                    | 24.8 ms: 1.05x slower                                                           |
| genshi_xml      | 51.6 ms                                                    | 58.3 ms: 1.13x slower                                                           |
| Geometric mean  | (ref)                                                      | 1.02x slower                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240925-linux-x86_64-savannahostrowski-jit_invalidate_500k-3.14.0a0-61a6174 |
|----------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| deepcopy_memo              | 39.7 us                                                    | 27.4 us: 1.45x faster                                                           |
| deepcopy                   | 367 us                                                     | 266 us: 1.38x faster                                                            |
| scimark_fft                | 392 ms                                                     | 312 ms: 1.26x faster                                                            |
| deepcopy_reduce            | 3.35 us                                                    | 2.67 us: 1.26x faster                                                           |
| richards                   | 50.9 ms                                                    | 41.1 ms: 1.24x faster                                                           |
| richards_super             | 57.4 ms                                                    | 46.9 ms: 1.22x faster                                                           |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.40 ms: 1.20x faster                                                           |
| async_tree_none            | 378 ms                                                     | 320 ms: 1.18x faster                                                            |
| async_tree_memoization     | 463 ms                                                     | 398 ms: 1.16x faster                                                            |
| mako                       | 11.2 ms                                                    | 9.74 ms: 1.15x faster                                                           |
| async_tree_memoization_tg  | 444 ms                                                     | 387 ms: 1.15x faster                                                            |
| crypto_pyaes               | 77.5 ms                                                    | 67.5 ms: 1.15x faster                                                           |
| xml_etree_generate         | 87.4 ms                                                    | 77.3 ms: 1.13x faster                                                           |
| float                      | 78.9 ms                                                    | 69.8 ms: 1.13x faster                                                           |
| bpe_tokeniser              | 5.02 sec                                                   | 4.45 sec: 1.13x faster                                                          |
| spectral_norm              | 116 ms                                                     | 104 ms: 1.12x faster                                                            |
| xml_etree_process          | 61.2 ms                                                    | 54.8 ms: 1.12x faster                                                           |
| xml_etree_parse            | 162 ms                                                     | 146 ms: 1.11x faster                                                            |
| tomli_loads                | 2.12 sec                                                   | 1.92 sec: 1.10x faster                                                          |
| pyflate                    | 484 ms                                                     | 439 ms: 1.10x faster                                                            |
| scimark_lu                 | 122 ms                                                     | 111 ms: 1.10x faster                                                            |
| mdp                        | 2.79 sec                                                   | 2.54 sec: 1.10x faster                                                          |
| scimark_monte_carlo        | 69.2 ms                                                    | 63.2 ms: 1.10x faster                                                           |
| json_dumps                 | 10.7 ms                                                    | 9.81 ms: 1.09x faster                                                           |
| coverage                   | 93.1 ms                                                    | 85.4 ms: 1.09x faster                                                           |
| go                         | 145 ms                                                     | 133 ms: 1.09x faster                                                            |
| scimark_sor                | 127 ms                                                     | 117 ms: 1.09x faster                                                            |
| async_tree_none_tg         | 336 ms                                                     | 309 ms: 1.09x faster                                                            |
| pathlib                    | 17.3 ms                                                    | 15.9 ms: 1.09x faster                                                           |
| xml_etree_iterparse        | 107 ms                                                     | 98.7 ms: 1.09x faster                                                           |
| sqlite_synth               | 2.99 us                                                    | 2.75 us: 1.09x faster                                                           |
| nbody                      | 88.3 ms                                                    | 81.4 ms: 1.08x faster                                                           |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 564 ms: 1.08x faster                                                            |
| html5lib                   | 67.2 ms                                                    | 62.0 ms: 1.08x faster                                                           |
| async_tree_io_tg           | 936 ms                                                     | 876 ms: 1.07x faster                                                            |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 551 ms: 1.07x faster                                                            |
| fannkuch                   | 402 ms                                                     | 377 ms: 1.07x faster                                                            |
| json_loads                 | 28.9 us                                                    | 27.2 us: 1.06x faster                                                           |
| async_tree_io              | 939 ms                                                     | 887 ms: 1.06x faster                                                            |
| telco                      | 8.41 ms                                                    | 7.96 ms: 1.06x faster                                                           |
| gc_traversal               | 3.98 ms                                                    | 3.77 ms: 1.05x faster                                                           |
| logging_format             | 6.47 us                                                    | 6.15 us: 1.05x faster                                                           |
| regex_dna                  | 221 ms                                                     | 212 ms: 1.04x faster                                                            |
| thrift                     | 823 us                                                     | 788 us: 1.04x faster                                                            |
| create_gc_cycles           | 1.82 ms                                                    | 1.75 ms: 1.04x faster                                                           |
| chaos                      | 61.3 ms                                                    | 59.1 ms: 1.04x faster                                                           |
| pidigits                   | 191 ms                                                     | 186 ms: 1.03x faster                                                            |
| json                       | 5.31 ms                                                    | 5.17 ms: 1.03x faster                                                           |
| asyncio_tcp                | 508 ms                                                     | 497 ms: 1.02x faster                                                            |
| unpickle                   | 15.1 us                                                    | 14.8 us: 1.02x faster                                                           |
| python_startup             | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                                           |
| asyncio_websockets         | 567 ms                                                     | 555 ms: 1.02x faster                                                            |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.81 sec: 1.02x faster                                                          |
| pprint_safe_repr           | 758 ms                                                     | 744 ms: 1.02x faster                                                            |
| meteor_contest             | 110 ms                                                     | 108 ms: 1.02x faster                                                            |
| logging_simple             | 5.74 us                                                    | 5.65 us: 1.02x faster                                                           |
| deltablue                  | 3.25 ms                                                    | 3.20 ms: 1.02x faster                                                           |
| logging_silent             | 105 ns                                                     | 103 ns: 1.01x faster                                                            |
| unpickle_list              | 5.34 us                                                    | 5.27 us: 1.01x faster                                                           |
| regex_v8                   | 25.1 ms                                                    | 24.8 ms: 1.01x faster                                                           |
| coroutines                 | 23.2 ms                                                    | 22.9 ms: 1.01x faster                                                           |
| unpickle_pure_python       | 218 us                                                     | 216 us: 1.01x faster                                                            |
| pickle_pure_python         | 305 us                                                     | 303 us: 1.01x faster                                                            |
| python_startup_no_site     | 7.11 ms                                                    | 7.06 ms: 1.01x faster                                                           |
| pickle_dict                | 34.8 us                                                    | 35.0 us: 1.00x slower                                                           |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                                           |
| 2to3                       | 274 ms                                                     | 276 ms: 1.01x slower                                                            |
| regex_effbot               | 3.67 ms                                                    | 3.70 ms: 1.01x slower                                                           |
| sqlglot_parse              | 1.32 ms                                                    | 1.33 ms: 1.01x slower                                                           |
| bench_thread_pool          | 834 us                                                     | 844 us: 1.01x slower                                                            |
| pickle                     | 11.5 us                                                    | 11.7 us: 1.02x slower                                                           |
| sqlglot_normalize          | 110 ms                                                     | 112 ms: 1.02x slower                                                            |
| pycparser                  | 1.16 sec                                                   | 1.18 sec: 1.02x slower                                                          |
| dulwich_log                | 67.2 ms                                                    | 68.6 ms: 1.02x slower                                                           |
| comprehensions             | 16.6 us                                                    | 17.0 us: 1.03x slower                                                           |
| sqlglot_transpile          | 1.63 ms                                                    | 1.69 ms: 1.03x slower                                                           |
| django_template            | 34.8 ms                                                    | 36.0 ms: 1.03x slower                                                           |
| docutils                   | 2.83 sec                                                   | 2.93 sec: 1.04x slower                                                          |
| raytrace                   | 267 ms                                                     | 276 ms: 1.04x slower                                                            |
| regex_compile              | 137 ms                                                     | 142 ms: 1.04x slower                                                            |
| async_generators           | 442 ms                                                     | 460 ms: 1.04x slower                                                            |
| genshi_text                | 23.7 ms                                                    | 24.8 ms: 1.05x slower                                                           |
| sqlglot_optimize           | 55.5 ms                                                    | 58.4 ms: 1.05x slower                                                           |
| sympy_str                  | 282 ms                                                     | 300 ms: 1.06x slower                                                            |
| sympy_expand               | 473 ms                                                     | 506 ms: 1.07x slower                                                            |
| nqueens                    | 81.4 ms                                                    | 88.5 ms: 1.09x slower                                                           |
| hexiom                     | 6.30 ms                                                    | 6.97 ms: 1.11x slower                                                           |
| sympy_sum                  | 156 ms                                                     | 174 ms: 1.11x slower                                                            |
| sympy_integrate            | 20.5 ms                                                    | 22.9 ms: 1.12x slower                                                           |
| genshi_xml                 | 51.6 ms                                                    | 58.3 ms: 1.13x slower                                                           |
| generators                 | 29.6 ms                                                    | 34.9 ms: 1.18x slower                                                           |
| pylint                     | 317 ms                                                     | 381 ms: 1.20x slower                                                            |
| Geometric mean             | (ref)                                                      | 1.04x faster                                                                    |

Benchmark hidden because not significant (4): typing_runtime_protocols, tornado_http, pickle_list, pprint_pformat
Ignored benchmarks (7) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20240925-3.14.0a0-61a6174-JIT/bm-20240925-linux-x86_64-savannahostrowski-jit_invalidate_500k-3.14.0a0-61a6174.json: unpack_sequence

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.07x