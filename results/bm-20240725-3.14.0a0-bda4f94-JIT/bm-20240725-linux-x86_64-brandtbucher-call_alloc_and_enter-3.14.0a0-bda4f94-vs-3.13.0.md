# Results vs. 3.13.0

- fork: brandtbucher
- ref: call_alloc_and_enter
- machine: linux-x86_64
- commit hash: bda4f94
- commit date: 2024-07-25
- overall geometric mean: 1.02x faster
- HPT reliability: 82.67%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240725-linux-x86_64-brandtbucher-call_alloc_and_enter-3.14.0a0-bda4f94 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 271 ms: 1.02x slower                                                        |
| docutils       | 2.58 sec                                               | 2.89 sec: 1.12x slower                                                      |
| html5lib       | 64.5 ms                                                | 65.8 ms: 1.02x slower                                                       |
| tornado_http   | 91.5 ms                                                | 92.3 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                  | 1.04x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240725-linux-x86_64-brandtbucher-call_alloc_and_enter-3.14.0a0-bda4f94 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 465 ms                                                 | 388 ms: 1.20x faster                                                        |
| async_tree_memoization     | 442 ms                                                 | 399 ms: 1.11x faster                                                        |
| async_tree_none            | 354 ms                                                 | 327 ms: 1.08x faster                                                        |
| async_tree_none_tg         | 320 ms                                                 | 298 ms: 1.08x faster                                                        |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 525 ms: 1.03x faster                                                        |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 562 ms: 1.02x faster                                                        |
| asyncio_tcp                | 488 ms                                                 | 486 ms: 1.00x faster                                                        |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.79 sec: 1.00x slower                                                      |
| async_tree_io_tg           | 825 ms                                                 | 864 ms: 1.05x slower                                                        |
| async_generators           | 433 ms                                                 | 455 ms: 1.05x slower                                                        |
| async_tree_io              | 843 ms                                                 | 898 ms: 1.07x slower                                                        |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                                |

Benchmark hidden because not significant (2): coroutines, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240725-linux-x86_64-brandtbucher-call_alloc_and_enter-3.14.0a0-bda4f94 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 70.6 ms: 1.11x faster                                                       |
| nbody          | 85.7 ms                                                | 79.9 ms: 1.07x faster                                                       |
| pidigits       | 186 ms                                                 | 185 ms: 1.00x faster                                                        |
| Geometric mean | (ref)                                                  | 1.06x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240725-linux-x86_64-brandtbucher-call_alloc_and_enter-3.14.0a0-bda4f94 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.67 ms: 1.06x faster                                                       |
| regex_v8       | 25.3 ms                                                | 24.0 ms: 1.05x faster                                                       |
| regex_compile  | 131 ms                                                 | 132 ms: 1.01x slower                                                        |
| regex_dna      | 220 ms                                                 | 231 ms: 1.05x slower                                                        |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240725-linux-x86_64-brandtbucher-call_alloc_and_enter-3.14.0a0-bda4f94 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.11 sec                                               | 1.93 sec: 1.10x faster                                                      |
| xml_etree_generate   | 87.0 ms                                                | 79.7 ms: 1.09x faster                                                       |
| xml_etree_process    | 60.4 ms                                                | 55.9 ms: 1.08x faster                                                       |
| xml_etree_parse      | 156 ms                                                 | 148 ms: 1.05x faster                                                        |
| xml_etree_iterparse  | 102 ms                                                 | 98.5 ms: 1.04x faster                                                       |
| pickle_pure_python   | 300 us                                                 | 297 us: 1.01x faster                                                        |
| unpickle_pure_python | 213 us                                                 | 215 us: 1.01x slower                                                        |
| json_loads           | 27.0 us                                                | 27.6 us: 1.02x slower                                                       |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                                |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240725-linux-x86_64-brandtbucher-call_alloc_and_enter-3.14.0a0-bda4f94 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.6 ms: 1.00x faster                                                       |
| python_startup_no_site | 6.99 ms                                                | 7.15 ms: 1.02x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240725-linux-x86_64-brandtbucher-call_alloc_and_enter-3.14.0a0-bda4f94 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.85 ms: 1.13x faster                                                       |
| django_template | 34.4 ms                                                | 35.5 ms: 1.03x slower                                                       |
| genshi_text     | 22.9 ms                                                | 24.8 ms: 1.08x slower                                                       |
| genshi_xml      | 50.3 ms                                                | 59.0 ms: 1.17x slower                                                       |
| Geometric mean  | (ref)                                                  | 1.04x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240725-linux-x86_64-brandtbucher-call_alloc_and_enter-3.14.0a0-bda4f94 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy_memo              | 38.0 us                                                | 28.6 us: 1.33x faster                                                       |
| deepcopy                   | 352 us                                                 | 269 us: 1.31x faster                                                        |
| async_tree_memoization_tg  | 465 ms                                                 | 388 ms: 1.20x faster                                                        |
| richards                   | 48.1 ms                                                | 40.5 ms: 1.19x faster                                                       |
| scimark_fft                | 369 ms                                                 | 312 ms: 1.18x faster                                                        |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.29 ms: 1.17x faster                                                       |
| richards_super             | 54.4 ms                                                | 46.9 ms: 1.16x faster                                                       |
| spectral_norm              | 115 ms                                                 | 100 ms: 1.15x faster                                                        |
| deepcopy_reduce            | 3.17 us                                                | 2.77 us: 1.14x faster                                                       |
| mako                       | 11.1 ms                                                | 9.85 ms: 1.13x faster                                                       |
| float                      | 78.5 ms                                                | 70.6 ms: 1.11x faster                                                       |
| async_tree_memoization     | 442 ms                                                 | 399 ms: 1.11x faster                                                        |
| crypto_pyaes               | 73.0 ms                                                | 66.3 ms: 1.10x faster                                                       |
| tomli_loads                | 2.11 sec                                               | 1.93 sec: 1.10x faster                                                      |
| scimark_monte_carlo        | 66.3 ms                                                | 60.7 ms: 1.09x faster                                                       |
| xml_etree_generate         | 87.0 ms                                                | 79.7 ms: 1.09x faster                                                       |
| async_tree_none            | 354 ms                                                 | 327 ms: 1.08x faster                                                        |
| telco                      | 8.45 ms                                                | 7.83 ms: 1.08x faster                                                       |
| xml_etree_process          | 60.4 ms                                                | 55.9 ms: 1.08x faster                                                       |
| async_tree_none_tg         | 320 ms                                                 | 298 ms: 1.08x faster                                                        |
| pathlib                    | 17.1 ms                                                | 15.9 ms: 1.08x faster                                                       |
| nbody                      | 85.7 ms                                                | 79.9 ms: 1.07x faster                                                       |
| gc_traversal               | 3.81 ms                                                | 3.56 ms: 1.07x faster                                                       |
| pycparser                  | 1.19 sec                                               | 1.12 sec: 1.07x faster                                                      |
| pyflate                    | 460 ms                                                 | 433 ms: 1.06x faster                                                        |
| regex_effbot               | 3.88 ms                                                | 3.67 ms: 1.06x faster                                                       |
| regex_v8                   | 25.3 ms                                                | 24.0 ms: 1.05x faster                                                       |
| xml_etree_parse            | 156 ms                                                 | 148 ms: 1.05x faster                                                        |
| bpe_tokeniser              | 4.69 sec                                               | 4.49 sec: 1.05x faster                                                      |
| pprint_safe_repr           | 744 ms                                                 | 716 ms: 1.04x faster                                                        |
| pprint_pformat             | 1.51 sec                                               | 1.45 sec: 1.04x faster                                                      |
| xml_etree_iterparse        | 102 ms                                                 | 98.5 ms: 1.04x faster                                                       |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 525 ms: 1.03x faster                                                        |
| logging_format             | 6.25 us                                                | 6.09 us: 1.03x faster                                                       |
| logging_simple             | 5.66 us                                                | 5.53 us: 1.02x faster                                                       |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 562 ms: 1.02x faster                                                        |
| meteor_contest             | 108 ms                                                 | 106 ms: 1.02x faster                                                        |
| thrift                     | 796 us                                                 | 782 us: 1.02x faster                                                        |
| fannkuch                   | 381 ms                                                 | 377 ms: 1.01x faster                                                        |
| json                       | 5.20 ms                                                | 5.14 ms: 1.01x faster                                                       |
| mdp                        | 2.74 sec                                               | 2.71 sec: 1.01x faster                                                      |
| pickle_pure_python         | 300 us                                                 | 297 us: 1.01x faster                                                        |
| generators                 | 28.8 ms                                                | 28.6 ms: 1.01x faster                                                       |
| pidigits                   | 186 ms                                                 | 185 ms: 1.00x faster                                                        |
| asyncio_tcp                | 488 ms                                                 | 486 ms: 1.00x faster                                                        |
| python_startup             | 10.6 ms                                                | 10.6 ms: 1.00x faster                                                       |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.79 sec: 1.00x slower                                                      |
| comprehensions             | 16.4 us                                                | 16.5 us: 1.01x slower                                                       |
| unpickle_pure_python       | 213 us                                                 | 215 us: 1.01x slower                                                        |
| sqlglot_transpile          | 1.57 ms                                                | 1.59 ms: 1.01x slower                                                       |
| tornado_http               | 91.5 ms                                                | 92.3 ms: 1.01x slower                                                       |
| regex_compile              | 131 ms                                                 | 132 ms: 1.01x slower                                                        |
| bench_thread_pool          | 815 us                                                 | 824 us: 1.01x slower                                                        |
| go                         | 142 ms                                                 | 144 ms: 1.02x slower                                                        |
| html5lib                   | 64.5 ms                                                | 65.8 ms: 1.02x slower                                                       |
| raytrace                   | 262 ms                                                 | 267 ms: 1.02x slower                                                        |
| 2to3                       | 265 ms                                                 | 271 ms: 1.02x slower                                                        |
| json_loads                 | 27.0 us                                                | 27.6 us: 1.02x slower                                                       |
| python_startup_no_site     | 6.99 ms                                                | 7.15 ms: 1.02x slower                                                       |
| django_template            | 34.4 ms                                                | 35.5 ms: 1.03x slower                                                       |
| sqlglot_optimize           | 53.9 ms                                                | 55.9 ms: 1.04x slower                                                       |
| sqlglot_normalize          | 107 ms                                                 | 112 ms: 1.04x slower                                                        |
| async_tree_io_tg           | 825 ms                                                 | 864 ms: 1.05x slower                                                        |
| logging_silent             | 102 ns                                                 | 107 ns: 1.05x slower                                                        |
| scimark_sor                | 122 ms                                                 | 128 ms: 1.05x slower                                                        |
| async_generators           | 433 ms                                                 | 455 ms: 1.05x slower                                                        |
| regex_dna                  | 220 ms                                                 | 231 ms: 1.05x slower                                                        |
| typing_runtime_protocols   | 159 us                                                 | 168 us: 1.05x slower                                                        |
| async_tree_io              | 843 ms                                                 | 898 ms: 1.07x slower                                                        |
| hexiom                     | 6.13 ms                                                | 6.53 ms: 1.07x slower                                                       |
| nqueens                    | 80.6 ms                                                | 86.0 ms: 1.07x slower                                                       |
| sympy_str                  | 274 ms                                                 | 294 ms: 1.07x slower                                                        |
| sympy_expand               | 462 ms                                                 | 499 ms: 1.08x slower                                                        |
| create_gc_cycles           | 1.61 ms                                                | 1.74 ms: 1.08x slower                                                       |
| genshi_text                | 22.9 ms                                                | 24.8 ms: 1.08x slower                                                       |
| dask                       | 338 ms                                                 | 366 ms: 1.08x slower                                                        |
| coverage                   | 83.7 ms                                                | 91.6 ms: 1.09x slower                                                       |
| scimark_lu                 | 115 ms                                                 | 127 ms: 1.11x slower                                                        |
| pylint                     | 313 ms                                                 | 347 ms: 1.11x slower                                                        |
| deltablue                  | 3.15 ms                                                | 3.51 ms: 1.11x slower                                                       |
| sympy_integrate            | 19.9 ms                                                | 22.2 ms: 1.11x slower                                                       |
| docutils                   | 2.58 sec                                               | 2.89 sec: 1.12x slower                                                      |
| sympy_sum                  | 150 ms                                                 | 169 ms: 1.13x slower                                                        |
| genshi_xml                 | 50.3 ms                                                | 59.0 ms: 1.17x slower                                                       |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                                |

Benchmark hidden because not significant (6): coroutines, chaos, bench_mp_pool, sqlglot_parse, json_dumps, asyncio_websockets
Ignored benchmarks (14) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 82.67% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.08x