# Results vs. 3.13.0b2

- fork: savannahostrowski
- ref: jit_mem_invalidate_1
- machine: linux-x86_64
- commit hash: 071a1a4
- commit date: 2024-08-20
- overall geometric mean: 1.05x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240820-linux-x86_64-savannahostrowski-jit_mem_invalidate_1-3.14.0a0-071a1a4 |
|----------------|:----------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 280 ms: 1.02x slower                                                             |
| docutils       | 2.83 sec                                                   | 2.97 sec: 1.05x slower                                                           |
| tornado_http   | 94.6 ms                                                    | 93.2 ms: 1.02x faster                                                            |
| Geometric mean | (ref)                                                      | 1.01x slower                                                                     |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240820-linux-x86_64-savannahostrowski-jit_mem_invalidate_1-3.14.0a0-071a1a4 |
|----------------------------|:----------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 321 ms: 1.18x faster                                                             |
| async_tree_memoization_tg  | 444 ms                                                     | 393 ms: 1.13x faster                                                             |
| async_tree_none_tg         | 336 ms                                                     | 299 ms: 1.13x faster                                                             |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 529 ms: 1.11x faster                                                             |
| async_tree_io_tg           | 936 ms                                                     | 861 ms: 1.09x faster                                                             |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 562 ms: 1.09x faster                                                             |
| async_tree_memoization     | 463 ms                                                     | 427 ms: 1.09x faster                                                             |
| async_tree_io              | 939 ms                                                     | 900 ms: 1.04x faster                                                             |
| Geometric mean             | (ref)                                                      | 1.11x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240820-linux-x86_64-savannahostrowski-jit_mem_invalidate_1-3.14.0a0-071a1a4 |
|----------------|:----------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 88.3 ms                                                    | 79.9 ms: 1.10x faster                                                            |
| float          | 78.9 ms                                                    | 72.1 ms: 1.09x faster                                                            |
| pidigits       | 191 ms                                                     | 186 ms: 1.03x faster                                                             |
| Geometric mean | (ref)                                                      | 1.08x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240820-linux-x86_64-savannahostrowski-jit_mem_invalidate_1-3.14.0a0-071a1a4 |
|----------------|:----------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                    | 3.56 ms: 1.03x faster                                                            |
| regex_v8       | 25.1 ms                                                    | 24.4 ms: 1.03x faster                                                            |
| regex_dna      | 221 ms                                                     | 218 ms: 1.02x faster                                                             |
| regex_compile  | 137 ms                                                     | 141 ms: 1.03x slower                                                             |
| Geometric mean | (ref)                                                      | 1.01x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240820-linux-x86_64-savannahostrowski-jit_mem_invalidate_1-3.14.0a0-071a1a4 |
|----------------------|:----------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                                   | 1.88 sec: 1.13x faster                                                           |
| xml_etree_iterparse  | 107 ms                                                     | 98.4 ms: 1.09x faster                                                            |
| xml_etree_parse      | 162 ms                                                     | 148 ms: 1.09x faster                                                             |
| xml_etree_generate   | 87.4 ms                                                    | 82.6 ms: 1.06x faster                                                            |
| xml_etree_process    | 61.2 ms                                                    | 58.0 ms: 1.05x faster                                                            |
| unpickle_pure_python | 218 us                                                     | 212 us: 1.03x faster                                                             |
| json_dumps           | 10.7 ms                                                    | 10.4 ms: 1.03x faster                                                            |
| pickle_pure_python   | 305 us                                                     | 302 us: 1.01x faster                                                             |
| json_loads           | 28.9 us                                                    | 28.7 us: 1.01x faster                                                            |
| Geometric mean       | (ref)                                                      | 1.05x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240820-linux-x86_64-savannahostrowski-jit_mem_invalidate_1-3.14.0a0-071a1a4 |
|------------------------|:----------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                                            |
| python_startup_no_site | 7.11 ms                                                    | 7.13 ms: 1.00x slower                                                            |
| Geometric mean         | (ref)                                                      | 1.01x faster                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240820-linux-x86_64-savannahostrowski-jit_mem_invalidate_1-3.14.0a0-071a1a4 |
|-----------------|:----------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.88 ms: 1.14x faster                                                            |
| django_template | 34.8 ms                                                    | 36.2 ms: 1.04x slower                                                            |
| genshi_text     | 23.7 ms                                                    | 26.2 ms: 1.11x slower                                                            |
| genshi_xml      | 51.6 ms                                                    | 62.0 ms: 1.20x slower                                                            |
| Geometric mean  | (ref)                                                      | 1.05x slower                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240820-linux-x86_64-savannahostrowski-jit_mem_invalidate_1-3.14.0a0-071a1a4 |
|----------------------------|:----------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| deepcopy_memo              | 39.7 us                                                    | 26.3 us: 1.51x faster                                                            |
| deepcopy                   | 367 us                                                     | 262 us: 1.40x faster                                                             |
| richards                   | 50.9 ms                                                    | 39.1 ms: 1.30x faster                                                            |
| scimark_fft                | 392 ms                                                     | 308 ms: 1.28x faster                                                             |
| deepcopy_reduce            | 3.35 us                                                    | 2.64 us: 1.27x faster                                                            |
| richards_super             | 57.4 ms                                                    | 45.4 ms: 1.26x faster                                                            |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.46 ms: 1.18x faster                                                            |
| async_tree_none            | 378 ms                                                     | 321 ms: 1.18x faster                                                             |
| crypto_pyaes               | 77.5 ms                                                    | 65.7 ms: 1.18x faster                                                            |
| spectral_norm              | 116 ms                                                     | 100 ms: 1.16x faster                                                             |
| mako                       | 11.2 ms                                                    | 9.88 ms: 1.14x faster                                                            |
| tomli_loads                | 2.12 sec                                                   | 1.88 sec: 1.13x faster                                                           |
| async_tree_memoization_tg  | 444 ms                                                     | 393 ms: 1.13x faster                                                             |
| async_tree_none_tg         | 336 ms                                                     | 299 ms: 1.13x faster                                                             |
| pyflate                    | 484 ms                                                     | 434 ms: 1.12x faster                                                             |
| scimark_lu                 | 122 ms                                                     | 109 ms: 1.12x faster                                                             |
| scimark_monte_carlo        | 69.2 ms                                                    | 62.1 ms: 1.11x faster                                                            |
| bpe_tokeniser              | 5.02 sec                                                   | 4.52 sec: 1.11x faster                                                           |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 529 ms: 1.11x faster                                                             |
| scimark_sor                | 127 ms                                                     | 115 ms: 1.11x faster                                                             |
| nbody                      | 88.3 ms                                                    | 79.9 ms: 1.10x faster                                                            |
| float                      | 78.9 ms                                                    | 72.1 ms: 1.09x faster                                                            |
| xml_etree_iterparse        | 107 ms                                                     | 98.4 ms: 1.09x faster                                                            |
| xml_etree_parse            | 162 ms                                                     | 148 ms: 1.09x faster                                                             |
| async_tree_io_tg           | 936 ms                                                     | 861 ms: 1.09x faster                                                             |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 562 ms: 1.09x faster                                                             |
| pathlib                    | 17.3 ms                                                    | 16.0 ms: 1.09x faster                                                            |
| async_tree_memoization     | 463 ms                                                     | 427 ms: 1.09x faster                                                             |
| telco                      | 8.41 ms                                                    | 7.76 ms: 1.08x faster                                                            |
| coverage                   | 93.1 ms                                                    | 86.0 ms: 1.08x faster                                                            |
| logging_format             | 6.47 us                                                    | 6.03 us: 1.07x faster                                                            |
| fannkuch                   | 402 ms                                                     | 377 ms: 1.07x faster                                                             |
| logging_silent             | 105 ns                                                     | 98.5 ns: 1.06x faster                                                            |
| gc_traversal               | 3.98 ms                                                    | 3.75 ms: 1.06x faster                                                            |
| logging_simple             | 5.74 us                                                    | 5.41 us: 1.06x faster                                                            |
| xml_etree_generate         | 87.4 ms                                                    | 82.6 ms: 1.06x faster                                                            |
| xml_etree_process          | 61.2 ms                                                    | 58.0 ms: 1.05x faster                                                            |
| thrift                     | 823 us                                                     | 785 us: 1.05x faster                                                             |
| create_gc_cycles           | 1.82 ms                                                    | 1.73 ms: 1.05x faster                                                            |
| async_tree_io              | 939 ms                                                     | 900 ms: 1.04x faster                                                             |
| pprint_pformat             | 1.56 sec                                                   | 1.50 sec: 1.04x faster                                                           |
| mdp                        | 2.79 sec                                                   | 2.68 sec: 1.04x faster                                                           |
| meteor_contest             | 110 ms                                                     | 106 ms: 1.04x faster                                                             |
| deltablue                  | 3.25 ms                                                    | 3.14 ms: 1.04x faster                                                            |
| pprint_safe_repr           | 758 ms                                                     | 733 ms: 1.03x faster                                                             |
| chaos                      | 61.3 ms                                                    | 59.4 ms: 1.03x faster                                                            |
| regex_effbot               | 3.67 ms                                                    | 3.56 ms: 1.03x faster                                                            |
| regex_v8                   | 25.1 ms                                                    | 24.4 ms: 1.03x faster                                                            |
| unpickle_pure_python       | 218 us                                                     | 212 us: 1.03x faster                                                             |
| json_dumps                 | 10.7 ms                                                    | 10.4 ms: 1.03x faster                                                            |
| pidigits                   | 191 ms                                                     | 186 ms: 1.03x faster                                                             |
| asyncio_tcp                | 508 ms                                                     | 495 ms: 1.03x faster                                                             |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.79 sec: 1.03x faster                                                           |
| python_startup             | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                                            |
| bench_thread_pool          | 834 us                                                     | 816 us: 1.02x faster                                                             |
| regex_dna                  | 221 ms                                                     | 218 ms: 1.02x faster                                                             |
| tornado_http               | 94.6 ms                                                    | 93.2 ms: 1.02x faster                                                            |
| asyncio_websockets         | 567 ms                                                     | 559 ms: 1.01x faster                                                             |
| pickle_pure_python         | 305 us                                                     | 302 us: 1.01x faster                                                             |
| coroutines                 | 23.2 ms                                                    | 23.0 ms: 1.01x faster                                                            |
| json_loads                 | 28.9 us                                                    | 28.7 us: 1.01x faster                                                            |
| raytrace                   | 267 ms                                                     | 266 ms: 1.00x faster                                                             |
| python_startup_no_site     | 7.11 ms                                                    | 7.13 ms: 1.00x slower                                                            |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                                            |
| json                       | 5.31 ms                                                    | 5.34 ms: 1.01x slower                                                            |
| 2to3                       | 274 ms                                                     | 280 ms: 1.02x slower                                                             |
| sqlglot_transpile          | 1.63 ms                                                    | 1.67 ms: 1.02x slower                                                            |
| sqlglot_normalize          | 110 ms                                                     | 113 ms: 1.03x slower                                                             |
| async_generators           | 442 ms                                                     | 456 ms: 1.03x slower                                                             |
| regex_compile              | 137 ms                                                     | 141 ms: 1.03x slower                                                             |
| typing_runtime_protocols   | 165 us                                                     | 171 us: 1.04x slower                                                             |
| django_template            | 34.8 ms                                                    | 36.2 ms: 1.04x slower                                                            |
| sqlglot_optimize           | 55.5 ms                                                    | 57.8 ms: 1.04x slower                                                            |
| nqueens                    | 81.4 ms                                                    | 85.2 ms: 1.05x slower                                                            |
| docutils                   | 2.83 sec                                                   | 2.97 sec: 1.05x slower                                                           |
| sympy_str                  | 282 ms                                                     | 304 ms: 1.08x slower                                                             |
| sympy_expand               | 473 ms                                                     | 510 ms: 1.08x slower                                                             |
| hexiom                     | 6.30 ms                                                    | 6.90 ms: 1.10x slower                                                            |
| genshi_text                | 23.7 ms                                                    | 26.2 ms: 1.11x slower                                                            |
| sympy_integrate            | 20.5 ms                                                    | 23.1 ms: 1.13x slower                                                            |
| generators                 | 29.6 ms                                                    | 33.6 ms: 1.13x slower                                                            |
| sympy_sum                  | 156 ms                                                     | 177 ms: 1.14x slower                                                             |
| pylint                     | 317 ms                                                     | 367 ms: 1.16x slower                                                             |
| genshi_xml                 | 51.6 ms                                                    | 62.0 ms: 1.20x slower                                                            |
| Geometric mean             | (ref)                                                      | 1.05x faster                                                                     |

Benchmark hidden because not significant (5): sqlglot_parse, go, html5lib, comprehensions, pycparser
Ignored benchmarks (14) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.07x