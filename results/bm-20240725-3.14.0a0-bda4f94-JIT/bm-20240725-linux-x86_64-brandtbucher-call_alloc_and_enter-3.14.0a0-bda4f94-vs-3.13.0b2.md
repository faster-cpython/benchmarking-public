# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: call_alloc_and_enter
- machine: linux-x86_64
- commit hash: bda4f94
- commit date: 2024-07-25
- overall geometric mean: 1.05x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240725-linux-x86_64-brandtbucher-call_alloc_and_enter-3.14.0a0-bda4f94 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 271 ms: 1.01x faster                                                        |
| docutils       | 2.83 sec                                                   | 2.89 sec: 1.02x slower                                                      |
| html5lib       | 67.2 ms                                                    | 65.8 ms: 1.02x faster                                                       |
| tornado_http   | 94.6 ms                                                    | 92.3 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                      | 1.01x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240725-linux-x86_64-brandtbucher-call_alloc_and_enter-3.14.0a0-bda4f94 |
|----------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization     | 463 ms                                                     | 399 ms: 1.16x faster                                                        |
| async_tree_none            | 378 ms                                                     | 327 ms: 1.16x faster                                                        |
| async_tree_memoization_tg  | 444 ms                                                     | 388 ms: 1.14x faster                                                        |
| async_tree_none_tg         | 336 ms                                                     | 298 ms: 1.13x faster                                                        |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 525 ms: 1.12x faster                                                        |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 562 ms: 1.09x faster                                                        |
| async_tree_io_tg           | 936 ms                                                     | 864 ms: 1.08x faster                                                        |
| async_tree_io              | 939 ms                                                     | 898 ms: 1.05x faster                                                        |
| Geometric mean             | (ref)                                                      | 1.12x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240725-linux-x86_64-brandtbucher-call_alloc_and_enter-3.14.0a0-bda4f94 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 70.6 ms: 1.12x faster                                                       |
| nbody          | 88.3 ms                                                    | 79.9 ms: 1.10x faster                                                       |
| pidigits       | 191 ms                                                     | 185 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                      | 1.08x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240725-linux-x86_64-brandtbucher-call_alloc_and_enter-3.14.0a0-bda4f94 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 25.1 ms                                                    | 24.0 ms: 1.05x faster                                                       |
| regex_compile  | 137 ms                                                     | 132 ms: 1.03x faster                                                        |
| regex_dna      | 221 ms                                                     | 231 ms: 1.05x slower                                                        |
| Geometric mean | (ref)                                                      | 1.01x faster                                                                |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240725-linux-x86_64-brandtbucher-call_alloc_and_enter-3.14.0a0-bda4f94 |
|----------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                                   | 1.93 sec: 1.10x faster                                                      |
| xml_etree_generate   | 87.4 ms                                                    | 79.7 ms: 1.10x faster                                                       |
| xml_etree_process    | 61.2 ms                                                    | 55.9 ms: 1.09x faster                                                       |
| xml_etree_parse      | 162 ms                                                     | 148 ms: 1.09x faster                                                        |
| xml_etree_iterparse  | 107 ms                                                     | 98.5 ms: 1.09x faster                                                       |
| json_loads           | 28.9 us                                                    | 27.6 us: 1.05x faster                                                       |
| pickle_pure_python   | 305 us                                                     | 297 us: 1.03x faster                                                        |
| json_dumps           | 10.7 ms                                                    | 10.4 ms: 1.03x faster                                                       |
| unpickle_pure_python | 218 us                                                     | 215 us: 1.01x faster                                                        |
| Geometric mean       | (ref)                                                      | 1.06x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240725-linux-x86_64-brandtbucher-call_alloc_and_enter-3.14.0a0-bda4f94 |
|------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.6 ms: 1.02x faster                                                       |
| python_startup_no_site | 7.11 ms                                                    | 7.15 ms: 1.01x slower                                                       |
| Geometric mean         | (ref)                                                      | 1.01x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240725-linux-x86_64-brandtbucher-call_alloc_and_enter-3.14.0a0-bda4f94 |
|-----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.85 ms: 1.14x faster                                                       |
| django_template | 34.8 ms                                                    | 35.5 ms: 1.02x slower                                                       |
| genshi_text     | 23.7 ms                                                    | 24.8 ms: 1.05x slower                                                       |
| genshi_xml      | 51.6 ms                                                    | 59.0 ms: 1.14x slower                                                       |
| Geometric mean  | (ref)                                                      | 1.02x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240725-linux-x86_64-brandtbucher-call_alloc_and_enter-3.14.0a0-bda4f94 |
|----------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy_memo              | 39.7 us                                                    | 28.6 us: 1.39x faster                                                       |
| deepcopy                   | 367 us                                                     | 269 us: 1.37x faster                                                        |
| scimark_fft                | 392 ms                                                     | 312 ms: 1.26x faster                                                        |
| richards                   | 50.9 ms                                                    | 40.5 ms: 1.26x faster                                                       |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.29 ms: 1.23x faster                                                       |
| richards_super             | 57.4 ms                                                    | 46.9 ms: 1.22x faster                                                       |
| deepcopy_reduce            | 3.35 us                                                    | 2.77 us: 1.21x faster                                                       |
| crypto_pyaes               | 77.5 ms                                                    | 66.3 ms: 1.17x faster                                                       |
| async_tree_memoization     | 463 ms                                                     | 399 ms: 1.16x faster                                                        |
| spectral_norm              | 116 ms                                                     | 100 ms: 1.16x faster                                                        |
| async_tree_none            | 378 ms                                                     | 327 ms: 1.16x faster                                                        |
| async_tree_memoization_tg  | 444 ms                                                     | 388 ms: 1.14x faster                                                        |
| mako                       | 11.2 ms                                                    | 9.85 ms: 1.14x faster                                                       |
| scimark_monte_carlo        | 69.2 ms                                                    | 60.7 ms: 1.14x faster                                                       |
| async_tree_none_tg         | 336 ms                                                     | 298 ms: 1.13x faster                                                        |
| bpe_tokeniser              | 5.02 sec                                                   | 4.49 sec: 1.12x faster                                                      |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 525 ms: 1.12x faster                                                        |
| float                      | 78.9 ms                                                    | 70.6 ms: 1.12x faster                                                       |
| pyflate                    | 484 ms                                                     | 433 ms: 1.12x faster                                                        |
| gc_traversal               | 3.98 ms                                                    | 3.56 ms: 1.12x faster                                                       |
| nbody                      | 88.3 ms                                                    | 79.9 ms: 1.10x faster                                                       |
| tomli_loads                | 2.12 sec                                                   | 1.93 sec: 1.10x faster                                                      |
| xml_etree_generate         | 87.4 ms                                                    | 79.7 ms: 1.10x faster                                                       |
| xml_etree_process          | 61.2 ms                                                    | 55.9 ms: 1.09x faster                                                       |
| xml_etree_parse            | 162 ms                                                     | 148 ms: 1.09x faster                                                        |
| pathlib                    | 17.3 ms                                                    | 15.9 ms: 1.09x faster                                                       |
| xml_etree_iterparse        | 107 ms                                                     | 98.5 ms: 1.09x faster                                                       |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 562 ms: 1.09x faster                                                        |
| async_tree_io_tg           | 936 ms                                                     | 864 ms: 1.08x faster                                                        |
| telco                      | 8.41 ms                                                    | 7.83 ms: 1.08x faster                                                       |
| pprint_pformat             | 1.56 sec                                                   | 1.45 sec: 1.07x faster                                                      |
| fannkuch                   | 402 ms                                                     | 377 ms: 1.07x faster                                                        |
| logging_format             | 6.47 us                                                    | 6.09 us: 1.06x faster                                                       |
| pprint_safe_repr           | 758 ms                                                     | 716 ms: 1.06x faster                                                        |
| thrift                     | 823 us                                                     | 782 us: 1.05x faster                                                        |
| chaos                      | 61.3 ms                                                    | 58.4 ms: 1.05x faster                                                       |
| regex_v8                   | 25.1 ms                                                    | 24.0 ms: 1.05x faster                                                       |
| json_loads                 | 28.9 us                                                    | 27.6 us: 1.05x faster                                                       |
| async_tree_io              | 939 ms                                                     | 898 ms: 1.05x faster                                                        |
| asyncio_tcp                | 508 ms                                                     | 486 ms: 1.05x faster                                                        |
| create_gc_cycles           | 1.82 ms                                                    | 1.74 ms: 1.04x faster                                                       |
| sqlglot_parse              | 1.32 ms                                                    | 1.27 ms: 1.04x faster                                                       |
| meteor_contest             | 110 ms                                                     | 106 ms: 1.04x faster                                                        |
| logging_simple             | 5.74 us                                                    | 5.53 us: 1.04x faster                                                       |
| generators                 | 29.6 ms                                                    | 28.6 ms: 1.04x faster                                                       |
| pycparser                  | 1.16 sec                                                   | 1.12 sec: 1.04x faster                                                      |
| coroutines                 | 23.2 ms                                                    | 22.4 ms: 1.03x faster                                                       |
| regex_compile              | 137 ms                                                     | 132 ms: 1.03x faster                                                        |
| pidigits                   | 191 ms                                                     | 185 ms: 1.03x faster                                                        |
| json                       | 5.31 ms                                                    | 5.14 ms: 1.03x faster                                                       |
| sqlglot_transpile          | 1.63 ms                                                    | 1.59 ms: 1.03x faster                                                       |
| pickle_pure_python         | 305 us                                                     | 297 us: 1.03x faster                                                        |
| json_dumps                 | 10.7 ms                                                    | 10.4 ms: 1.03x faster                                                       |
| mdp                        | 2.79 sec                                                   | 2.71 sec: 1.03x faster                                                      |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.79 sec: 1.03x faster                                                      |
| tornado_http               | 94.6 ms                                                    | 92.3 ms: 1.02x faster                                                       |
| html5lib                   | 67.2 ms                                                    | 65.8 ms: 1.02x faster                                                       |
| python_startup             | 10.8 ms                                                    | 10.6 ms: 1.02x faster                                                       |
| asyncio_websockets         | 567 ms                                                     | 557 ms: 1.02x faster                                                        |
| coverage                   | 93.1 ms                                                    | 91.6 ms: 1.02x faster                                                       |
| unpickle_pure_python       | 218 us                                                     | 215 us: 1.01x faster                                                        |
| 2to3                       | 274 ms                                                     | 271 ms: 1.01x faster                                                        |
| bench_thread_pool          | 834 us                                                     | 824 us: 1.01x faster                                                        |
| comprehensions             | 16.6 us                                                    | 16.5 us: 1.01x faster                                                       |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                                       |
| scimark_sor                | 127 ms                                                     | 128 ms: 1.01x slower                                                        |
| python_startup_no_site     | 7.11 ms                                                    | 7.15 ms: 1.01x slower                                                       |
| sqlglot_optimize           | 55.5 ms                                                    | 55.9 ms: 1.01x slower                                                       |
| sqlglot_normalize          | 110 ms                                                     | 112 ms: 1.02x slower                                                        |
| typing_runtime_protocols   | 165 us                                                     | 168 us: 1.02x slower                                                        |
| django_template            | 34.8 ms                                                    | 35.5 ms: 1.02x slower                                                       |
| logging_silent             | 105 ns                                                     | 107 ns: 1.02x slower                                                        |
| docutils                   | 2.83 sec                                                   | 2.89 sec: 1.02x slower                                                      |
| async_generators           | 442 ms                                                     | 455 ms: 1.03x slower                                                        |
| hexiom                     | 6.30 ms                                                    | 6.53 ms: 1.04x slower                                                       |
| sympy_str                  | 282 ms                                                     | 294 ms: 1.04x slower                                                        |
| regex_dna                  | 221 ms                                                     | 231 ms: 1.05x slower                                                        |
| genshi_text                | 23.7 ms                                                    | 24.8 ms: 1.05x slower                                                       |
| scimark_lu                 | 122 ms                                                     | 127 ms: 1.05x slower                                                        |
| nqueens                    | 81.4 ms                                                    | 86.0 ms: 1.06x slower                                                       |
| sympy_expand               | 473 ms                                                     | 499 ms: 1.06x slower                                                        |
| deltablue                  | 3.25 ms                                                    | 3.51 ms: 1.08x slower                                                       |
| sympy_integrate            | 20.5 ms                                                    | 22.2 ms: 1.08x slower                                                       |
| sympy_sum                  | 156 ms                                                     | 169 ms: 1.08x slower                                                        |
| pylint                     | 317 ms                                                     | 347 ms: 1.09x slower                                                        |
| genshi_xml                 | 51.6 ms                                                    | 59.0 ms: 1.14x slower                                                       |
| Geometric mean             | (ref)                                                      | 1.05x faster                                                                |

Benchmark hidden because not significant (4): dask, go, regex_effbot, raytrace
Ignored benchmarks (13) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.07x