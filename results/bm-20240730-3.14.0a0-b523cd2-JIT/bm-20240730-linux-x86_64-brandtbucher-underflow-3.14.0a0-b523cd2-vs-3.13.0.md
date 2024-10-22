# Results vs. 3.13.0

- fork: brandtbucher
- ref: underflow
- machine: linux-x86_64
- commit hash: b523cd2
- commit date: 2024-07-30
- overall geometric mean: 1.00x faster
- HPT reliability: 70.22%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240730-linux-x86_64-brandtbucher-underflow-3.14.0a0-b523cd2 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 278 ms: 1.05x slower                                             |
| docutils       | 2.58 sec                                               | 3.09 sec: 1.19x slower                                           |
| html5lib       | 64.5 ms                                                | 69.7 ms: 1.08x slower                                            |
| tornado_http   | 91.5 ms                                                | 103 ms: 1.13x slower                                             |
| Geometric mean | (ref)                                                  | 1.11x slower                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240730-linux-x86_64-brandtbucher-underflow-3.14.0a0-b523cd2 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_memoization_tg  | 465 ms                                                 | 396 ms: 1.17x faster                                             |
| async_tree_none            | 354 ms                                                 | 331 ms: 1.07x faster                                             |
| async_tree_none_tg         | 320 ms                                                 | 304 ms: 1.05x faster                                             |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 533 ms: 1.02x faster                                             |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 565 ms: 1.02x faster                                             |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.01x slower                                           |
| coroutines                 | 22.5 ms                                                | 22.7 ms: 1.01x slower                                            |
| asyncio_tcp                | 488 ms                                                 | 509 ms: 1.04x slower                                             |
| async_generators           | 433 ms                                                 | 453 ms: 1.05x slower                                             |
| async_tree_io_tg           | 825 ms                                                 | 879 ms: 1.06x slower                                             |
| async_tree_io              | 843 ms                                                 | 915 ms: 1.09x slower                                             |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                     |

Benchmark hidden because not significant (2): async_tree_memoization, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240730-linux-x86_64-brandtbucher-underflow-3.14.0a0-b523cd2 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| float          | 78.5 ms                                                | 71.5 ms: 1.10x faster                                            |
| nbody          | 85.7 ms                                                | 81.3 ms: 1.05x faster                                            |
| pidigits       | 186 ms                                                 | 187 ms: 1.01x slower                                             |
| Geometric mean | (ref)                                                  | 1.05x faster                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240730-linux-x86_64-brandtbucher-underflow-3.14.0a0-b523cd2 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.66 ms: 1.06x faster                                            |
| regex_dna      | 220 ms                                                 | 221 ms: 1.01x slower                                             |
| regex_v8       | 25.3 ms                                                | 25.9 ms: 1.02x slower                                            |
| regex_compile  | 131 ms                                                 | 140 ms: 1.07x slower                                             |
| Geometric mean | (ref)                                                  | 1.01x slower                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240730-linux-x86_64-brandtbucher-underflow-3.14.0a0-b523cd2 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| xml_etree_generate   | 87.0 ms                                                | 78.9 ms: 1.10x faster                                            |
| unpickle_pure_python | 213 us                                                 | 197 us: 1.08x faster                                             |
| xml_etree_process    | 60.4 ms                                                | 56.0 ms: 1.08x faster                                            |
| tomli_loads          | 2.11 sec                                               | 1.98 sec: 1.07x faster                                           |
| xml_etree_parse      | 156 ms                                                 | 148 ms: 1.05x faster                                             |
| xml_etree_iterparse  | 102 ms                                                 | 98.4 ms: 1.04x faster                                            |
| pickle_pure_python   | 300 us                                                 | 304 us: 1.01x slower                                             |
| json_loads           | 27.0 us                                                | 28.4 us: 1.05x slower                                            |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                     |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240730-linux-x86_64-brandtbucher-underflow-3.14.0a0-b523cd2 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.7 ms: 1.01x slower                                            |
| python_startup_no_site | 6.99 ms                                                | 7.22 ms: 1.03x slower                                            |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240730-linux-x86_64-brandtbucher-underflow-3.14.0a0-b523cd2 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.78 ms: 1.14x faster                                            |
| genshi_text     | 22.9 ms                                                | 23.4 ms: 1.02x slower                                            |
| django_template | 34.4 ms                                                | 36.2 ms: 1.05x slower                                            |
| genshi_xml      | 50.3 ms                                                | 59.9 ms: 1.19x slower                                            |
| Geometric mean  | (ref)                                                  | 1.03x slower                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240730-linux-x86_64-brandtbucher-underflow-3.14.0a0-b523cd2 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| deepcopy_memo              | 38.0 us                                                | 28.4 us: 1.34x faster                                            |
| deepcopy                   | 352 us                                                 | 263 us: 1.34x faster                                             |
| richards                   | 48.1 ms                                                | 38.1 ms: 1.26x faster                                            |
| scimark_fft                | 369 ms                                                 | 300 ms: 1.23x faster                                             |
| richards_super             | 54.4 ms                                                | 44.4 ms: 1.22x faster                                            |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.20 ms: 1.20x faster                                            |
| deepcopy_reduce            | 3.17 us                                                | 2.69 us: 1.18x faster                                            |
| async_tree_memoization_tg  | 465 ms                                                 | 396 ms: 1.17x faster                                             |
| spectral_norm              | 115 ms                                                 | 99.8 ms: 1.15x faster                                            |
| scimark_monte_carlo        | 66.3 ms                                                | 57.8 ms: 1.15x faster                                            |
| mako                       | 11.1 ms                                                | 9.78 ms: 1.14x faster                                            |
| xml_etree_generate         | 87.0 ms                                                | 78.9 ms: 1.10x faster                                            |
| float                      | 78.5 ms                                                | 71.5 ms: 1.10x faster                                            |
| telco                      | 8.45 ms                                                | 7.73 ms: 1.09x faster                                            |
| crypto_pyaes               | 73.0 ms                                                | 66.9 ms: 1.09x faster                                            |
| unpickle_pure_python       | 213 us                                                 | 197 us: 1.08x faster                                             |
| gc_traversal               | 3.81 ms                                                | 3.53 ms: 1.08x faster                                            |
| xml_etree_process          | 60.4 ms                                                | 56.0 ms: 1.08x faster                                            |
| async_tree_none            | 354 ms                                                 | 331 ms: 1.07x faster                                             |
| tomli_loads                | 2.11 sec                                               | 1.98 sec: 1.07x faster                                           |
| pathlib                    | 17.1 ms                                                | 16.0 ms: 1.07x faster                                            |
| regex_effbot               | 3.88 ms                                                | 3.66 ms: 1.06x faster                                            |
| pyflate                    | 460 ms                                                 | 436 ms: 1.06x faster                                             |
| nbody                      | 85.7 ms                                                | 81.3 ms: 1.05x faster                                            |
| async_tree_none_tg         | 320 ms                                                 | 304 ms: 1.05x faster                                             |
| xml_etree_parse            | 156 ms                                                 | 148 ms: 1.05x faster                                             |
| bpe_tokeniser              | 4.69 sec                                               | 4.50 sec: 1.04x faster                                           |
| pprint_safe_repr           | 744 ms                                                 | 716 ms: 1.04x faster                                             |
| fannkuch                   | 381 ms                                                 | 367 ms: 1.04x faster                                             |
| xml_etree_iterparse        | 102 ms                                                 | 98.4 ms: 1.04x faster                                            |
| meteor_contest             | 108 ms                                                 | 105 ms: 1.02x faster                                             |
| pprint_pformat             | 1.51 sec                                               | 1.48 sec: 1.02x faster                                           |
| pycparser                  | 1.19 sec                                               | 1.17 sec: 1.02x faster                                           |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 533 ms: 1.02x faster                                             |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 565 ms: 1.02x faster                                             |
| chaos                      | 58.4 ms                                                | 57.9 ms: 1.01x faster                                            |
| pidigits                   | 186 ms                                                 | 187 ms: 1.01x slower                                             |
| regex_dna                  | 220 ms                                                 | 221 ms: 1.01x slower                                             |
| mdp                        | 2.74 sec                                               | 2.77 sec: 1.01x slower                                           |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.01x slower                                           |
| coroutines                 | 22.5 ms                                                | 22.7 ms: 1.01x slower                                            |
| python_startup             | 10.6 ms                                                | 10.7 ms: 1.01x slower                                            |
| pickle_pure_python         | 300 us                                                 | 304 us: 1.01x slower                                             |
| bench_thread_pool          | 815 us                                                 | 827 us: 1.02x slower                                             |
| go                         | 142 ms                                                 | 144 ms: 1.02x slower                                             |
| genshi_text                | 22.9 ms                                                | 23.4 ms: 1.02x slower                                            |
| regex_v8                   | 25.3 ms                                                | 25.9 ms: 1.02x slower                                            |
| raytrace                   | 262 ms                                                 | 268 ms: 1.03x slower                                             |
| nqueens                    | 80.6 ms                                                | 83.0 ms: 1.03x slower                                            |
| python_startup_no_site     | 6.99 ms                                                | 7.22 ms: 1.03x slower                                            |
| scimark_sor                | 122 ms                                                 | 127 ms: 1.04x slower                                             |
| asyncio_tcp                | 488 ms                                                 | 509 ms: 1.04x slower                                             |
| async_generators           | 433 ms                                                 | 453 ms: 1.05x slower                                             |
| sqlglot_optimize           | 53.9 ms                                                | 56.6 ms: 1.05x slower                                            |
| 2to3                       | 265 ms                                                 | 278 ms: 1.05x slower                                             |
| django_template            | 34.4 ms                                                | 36.2 ms: 1.05x slower                                            |
| json_loads                 | 27.0 us                                                | 28.4 us: 1.05x slower                                            |
| scimark_lu                 | 115 ms                                                 | 122 ms: 1.06x slower                                             |
| async_tree_io_tg           | 825 ms                                                 | 879 ms: 1.06x slower                                             |
| regex_compile              | 131 ms                                                 | 140 ms: 1.07x slower                                             |
| typing_runtime_protocols   | 159 us                                                 | 172 us: 1.08x slower                                             |
| html5lib                   | 64.5 ms                                                | 69.7 ms: 1.08x slower                                            |
| async_tree_io              | 843 ms                                                 | 915 ms: 1.09x slower                                             |
| create_gc_cycles           | 1.61 ms                                                | 1.75 ms: 1.09x slower                                            |
| coverage                   | 83.7 ms                                                | 91.0 ms: 1.09x slower                                            |
| sqlglot_normalize          | 107 ms                                                 | 117 ms: 1.09x slower                                             |
| hexiom                     | 6.13 ms                                                | 6.78 ms: 1.11x slower                                            |
| dask                       | 338 ms                                                 | 379 ms: 1.12x slower                                             |
| sqlglot_parse              | 1.27 ms                                                | 1.42 ms: 1.13x slower                                            |
| sqlglot_transpile          | 1.57 ms                                                | 1.77 ms: 1.13x slower                                            |
| tornado_http               | 91.5 ms                                                | 103 ms: 1.13x slower                                             |
| generators                 | 28.8 ms                                                | 33.3 ms: 1.16x slower                                            |
| sympy_expand               | 462 ms                                                 | 538 ms: 1.17x slower                                             |
| sympy_str                  | 274 ms                                                 | 323 ms: 1.18x slower                                             |
| genshi_xml                 | 50.3 ms                                                | 59.9 ms: 1.19x slower                                            |
| docutils                   | 2.58 sec                                               | 3.09 sec: 1.19x slower                                           |
| sympy_integrate            | 19.9 ms                                                | 24.2 ms: 1.21x slower                                            |
| sympy_sum                  | 150 ms                                                 | 183 ms: 1.22x slower                                             |
| deltablue                  | 3.15 ms                                                | 3.86 ms: 1.23x slower                                            |
| pylint                     | 313 ms                                                 | 390 ms: 1.25x slower                                             |
| Geometric mean             | (ref)                                                  | 1.00x faster                                                     |

Benchmark hidden because not significant (10): async_tree_memoization, thrift, logging_silent, comprehensions, asyncio_websockets, bench_mp_pool, logging_format, logging_simple, json_dumps, json
Ignored benchmarks (14) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 70.22% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.09x