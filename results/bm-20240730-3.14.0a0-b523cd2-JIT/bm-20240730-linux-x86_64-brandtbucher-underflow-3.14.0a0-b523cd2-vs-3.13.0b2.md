# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: underflow
- machine: linux-x86_64
- commit hash: b523cd2
- commit date: 2024-07-30
- overall geometric mean: 1.04x faster
- HPT reliability: 99.23%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240730-linux-x86_64-brandtbucher-underflow-3.14.0a0-b523cd2 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 278 ms: 1.02x slower                                             |
| docutils       | 2.83 sec                                                   | 3.09 sec: 1.09x slower                                           |
| html5lib       | 67.2 ms                                                    | 69.7 ms: 1.04x slower                                            |
| tornado_http   | 94.6 ms                                                    | 103 ms: 1.09x slower                                             |
| Geometric mean | (ref)                                                      | 1.06x slower                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240730-linux-x86_64-brandtbucher-underflow-3.14.0a0-b523cd2 |
|----------------------------|:----------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 331 ms: 1.14x faster                                             |
| async_tree_memoization_tg  | 444 ms                                                     | 396 ms: 1.12x faster                                             |
| async_tree_none_tg         | 336 ms                                                     | 304 ms: 1.10x faster                                             |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 533 ms: 1.10x faster                                             |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 565 ms: 1.08x faster                                             |
| async_tree_memoization     | 463 ms                                                     | 431 ms: 1.08x faster                                             |
| async_tree_io_tg           | 936 ms                                                     | 879 ms: 1.07x faster                                             |
| Geometric mean             | (ref)                                                      | 1.09x faster                                                     |

Benchmark hidden because not significant (1): async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240730-linux-x86_64-brandtbucher-underflow-3.14.0a0-b523cd2 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 71.5 ms: 1.10x faster                                            |
| nbody          | 88.3 ms                                                    | 81.3 ms: 1.09x faster                                            |
| pidigits       | 191 ms                                                     | 187 ms: 1.02x faster                                             |
| Geometric mean | (ref)                                                      | 1.07x faster                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240730-linux-x86_64-brandtbucher-underflow-3.14.0a0-b523cd2 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_compile  | 137 ms                                                     | 140 ms: 1.02x slower                                             |
| regex_v8       | 25.1 ms                                                    | 25.9 ms: 1.03x slower                                            |
| Geometric mean | (ref)                                                      | 1.01x slower                                                     |

Benchmark hidden because not significant (2): regex_effbot, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240730-linux-x86_64-brandtbucher-underflow-3.14.0a0-b523cd2 |
|----------------------|:----------------------------------------------------------:|:----------------------------------------------------------------:|
| unpickle_pure_python | 218 us                                                     | 197 us: 1.11x faster                                             |
| xml_etree_generate   | 87.4 ms                                                    | 78.9 ms: 1.11x faster                                            |
| xml_etree_process    | 61.2 ms                                                    | 56.0 ms: 1.09x faster                                            |
| xml_etree_iterparse  | 107 ms                                                     | 98.4 ms: 1.09x faster                                            |
| xml_etree_parse      | 162 ms                                                     | 148 ms: 1.09x faster                                             |
| tomli_loads          | 2.12 sec                                                   | 1.98 sec: 1.07x faster                                           |
| json_dumps           | 10.7 ms                                                    | 10.4 ms: 1.03x faster                                            |
| json_loads           | 28.9 us                                                    | 28.4 us: 1.02x faster                                            |
| Geometric mean       | (ref)                                                      | 1.07x faster                                                     |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240730-linux-x86_64-brandtbucher-underflow-3.14.0a0-b523cd2 |
|------------------------|:----------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.7 ms: 1.01x faster                                            |
| python_startup_no_site | 7.11 ms                                                    | 7.22 ms: 1.02x slower                                            |
| Geometric mean         | (ref)                                                      | 1.00x slower                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240730-linux-x86_64-brandtbucher-underflow-3.14.0a0-b523cd2 |
|-----------------|:----------------------------------------------------------:|:----------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.78 ms: 1.15x faster                                            |
| genshi_text     | 23.7 ms                                                    | 23.4 ms: 1.01x faster                                            |
| django_template | 34.8 ms                                                    | 36.2 ms: 1.04x slower                                            |
| genshi_xml      | 51.6 ms                                                    | 59.9 ms: 1.16x slower                                            |
| Geometric mean  | (ref)                                                      | 1.01x slower                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240730-linux-x86_64-brandtbucher-underflow-3.14.0a0-b523cd2 |
|----------------------------|:----------------------------------------------------------:|:----------------------------------------------------------------:|
| deepcopy_memo              | 39.7 us                                                    | 28.4 us: 1.40x faster                                            |
| deepcopy                   | 367 us                                                     | 263 us: 1.39x faster                                             |
| richards                   | 50.9 ms                                                    | 38.1 ms: 1.34x faster                                            |
| scimark_fft                | 392 ms                                                     | 300 ms: 1.31x faster                                             |
| richards_super             | 57.4 ms                                                    | 44.4 ms: 1.29x faster                                            |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.20 ms: 1.25x faster                                            |
| deepcopy_reduce            | 3.35 us                                                    | 2.69 us: 1.25x faster                                            |
| scimark_monte_carlo        | 69.2 ms                                                    | 57.8 ms: 1.20x faster                                            |
| spectral_norm              | 116 ms                                                     | 99.8 ms: 1.16x faster                                            |
| crypto_pyaes               | 77.5 ms                                                    | 66.9 ms: 1.16x faster                                            |
| mako                       | 11.2 ms                                                    | 9.78 ms: 1.15x faster                                            |
| async_tree_none            | 378 ms                                                     | 331 ms: 1.14x faster                                             |
| gc_traversal               | 3.98 ms                                                    | 3.53 ms: 1.13x faster                                            |
| async_tree_memoization_tg  | 444 ms                                                     | 396 ms: 1.12x faster                                             |
| bpe_tokeniser              | 5.02 sec                                                   | 4.50 sec: 1.12x faster                                           |
| pyflate                    | 484 ms                                                     | 436 ms: 1.11x faster                                             |
| unpickle_pure_python       | 218 us                                                     | 197 us: 1.11x faster                                             |
| xml_etree_generate         | 87.4 ms                                                    | 78.9 ms: 1.11x faster                                            |
| async_tree_none_tg         | 336 ms                                                     | 304 ms: 1.10x faster                                             |
| float                      | 78.9 ms                                                    | 71.5 ms: 1.10x faster                                            |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 533 ms: 1.10x faster                                             |
| fannkuch                   | 402 ms                                                     | 367 ms: 1.09x faster                                             |
| xml_etree_process          | 61.2 ms                                                    | 56.0 ms: 1.09x faster                                            |
| xml_etree_iterparse        | 107 ms                                                     | 98.4 ms: 1.09x faster                                            |
| xml_etree_parse            | 162 ms                                                     | 148 ms: 1.09x faster                                             |
| telco                      | 8.41 ms                                                    | 7.73 ms: 1.09x faster                                            |
| nbody                      | 88.3 ms                                                    | 81.3 ms: 1.09x faster                                            |
| pathlib                    | 17.3 ms                                                    | 16.0 ms: 1.08x faster                                            |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 565 ms: 1.08x faster                                             |
| async_tree_memoization     | 463 ms                                                     | 431 ms: 1.08x faster                                             |
| tomli_loads                | 2.12 sec                                                   | 1.98 sec: 1.07x faster                                           |
| async_tree_io_tg           | 936 ms                                                     | 879 ms: 1.07x faster                                             |
| chaos                      | 61.3 ms                                                    | 57.9 ms: 1.06x faster                                            |
| pprint_safe_repr           | 758 ms                                                     | 716 ms: 1.06x faster                                             |
| pprint_pformat             | 1.56 sec                                                   | 1.48 sec: 1.05x faster                                           |
| meteor_contest             | 110 ms                                                     | 105 ms: 1.05x faster                                             |
| thrift                     | 823 us                                                     | 792 us: 1.04x faster                                             |
| create_gc_cycles           | 1.82 ms                                                    | 1.75 ms: 1.04x faster                                            |
| logging_format             | 6.47 us                                                    | 6.26 us: 1.03x faster                                            |
| logging_silent             | 105 ns                                                     | 102 ns: 1.03x faster                                             |
| json_dumps                 | 10.7 ms                                                    | 10.4 ms: 1.03x faster                                            |
| coverage                   | 93.1 ms                                                    | 91.0 ms: 1.02x faster                                            |
| pidigits                   | 191 ms                                                     | 187 ms: 1.02x faster                                             |
| asyncio_websockets         | 567 ms                                                     | 555 ms: 1.02x faster                                             |
| coroutines                 | 23.2 ms                                                    | 22.7 ms: 1.02x faster                                            |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.81 sec: 1.02x faster                                           |
| json_loads                 | 28.9 us                                                    | 28.4 us: 1.02x faster                                            |
| json                       | 5.31 ms                                                    | 5.23 ms: 1.02x faster                                            |
| comprehensions             | 16.6 us                                                    | 16.4 us: 1.01x faster                                            |
| genshi_text                | 23.7 ms                                                    | 23.4 ms: 1.01x faster                                            |
| logging_simple             | 5.74 us                                                    | 5.67 us: 1.01x faster                                            |
| bench_thread_pool          | 834 us                                                     | 827 us: 1.01x faster                                             |
| mdp                        | 2.79 sec                                                   | 2.77 sec: 1.01x faster                                           |
| python_startup             | 10.8 ms                                                    | 10.7 ms: 1.01x faster                                            |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                            |
| raytrace                   | 267 ms                                                     | 268 ms: 1.01x slower                                             |
| 2to3                       | 274 ms                                                     | 278 ms: 1.02x slower                                             |
| python_startup_no_site     | 7.11 ms                                                    | 7.22 ms: 1.02x slower                                            |
| nqueens                    | 81.4 ms                                                    | 83.0 ms: 1.02x slower                                            |
| sqlglot_optimize           | 55.5 ms                                                    | 56.6 ms: 1.02x slower                                            |
| async_generators           | 442 ms                                                     | 453 ms: 1.02x slower                                             |
| regex_compile              | 137 ms                                                     | 140 ms: 1.02x slower                                             |
| dask                       | 369 ms                                                     | 379 ms: 1.03x slower                                             |
| regex_v8                   | 25.1 ms                                                    | 25.9 ms: 1.03x slower                                            |
| html5lib                   | 67.2 ms                                                    | 69.7 ms: 1.04x slower                                            |
| django_template            | 34.8 ms                                                    | 36.2 ms: 1.04x slower                                            |
| typing_runtime_protocols   | 165 us                                                     | 172 us: 1.04x slower                                             |
| sqlglot_normalize          | 110 ms                                                     | 117 ms: 1.06x slower                                             |
| hexiom                     | 6.30 ms                                                    | 6.78 ms: 1.08x slower                                            |
| sqlglot_parse              | 1.32 ms                                                    | 1.42 ms: 1.08x slower                                            |
| sqlglot_transpile          | 1.63 ms                                                    | 1.77 ms: 1.09x slower                                            |
| docutils                   | 2.83 sec                                                   | 3.09 sec: 1.09x slower                                           |
| tornado_http               | 94.6 ms                                                    | 103 ms: 1.09x slower                                             |
| generators                 | 29.6 ms                                                    | 33.3 ms: 1.12x slower                                            |
| sympy_expand               | 473 ms                                                     | 538 ms: 1.14x slower                                             |
| sympy_str                  | 282 ms                                                     | 323 ms: 1.14x slower                                             |
| genshi_xml                 | 51.6 ms                                                    | 59.9 ms: 1.16x slower                                            |
| sympy_sum                  | 156 ms                                                     | 183 ms: 1.17x slower                                             |
| sympy_integrate            | 20.5 ms                                                    | 24.2 ms: 1.18x slower                                            |
| deltablue                  | 3.25 ms                                                    | 3.86 ms: 1.19x slower                                            |
| pylint                     | 317 ms                                                     | 390 ms: 1.23x slower                                             |
| Geometric mean             | (ref)                                                      | 1.04x faster                                                     |

Benchmark hidden because not significant (9): async_tree_io, pickle_pure_python, scimark_sor, regex_effbot, go, asyncio_tcp, regex_dna, scimark_lu, pycparser
Ignored benchmarks (13) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 99.23% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.09x