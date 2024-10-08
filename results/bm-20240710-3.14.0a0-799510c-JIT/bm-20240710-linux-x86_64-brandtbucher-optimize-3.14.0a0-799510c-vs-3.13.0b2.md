# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: optimize
- machine: linux-x86_64
- commit hash: 799510c
- commit date: 2024-07-10
- overall geometric mean: 1.02x slower
- HPT reliability: 97.87%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240710-linux-x86_64-brandtbucher-optimize-3.14.0a0-799510c |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 271 ms: 1.01x faster                                            |
| docutils       | 2.83 sec                                                   | 6.74 sec: 2.38x slower                                          |
| html5lib       | 67.2 ms                                                    | 77.0 ms: 1.15x slower                                           |
| tornado_http   | 94.6 ms                                                    | 97.9 ms: 1.03x slower                                           |
| Geometric mean | (ref)                                                      | 1.29x slower                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240710-linux-x86_64-brandtbucher-optimize-3.14.0a0-799510c |
|----------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_memoization_tg  | 444 ms                                                     | 382 ms: 1.16x faster                                            |
| async_tree_none            | 378 ms                                                     | 329 ms: 1.15x faster                                            |
| async_tree_memoization     | 463 ms                                                     | 412 ms: 1.12x faster                                            |
| async_tree_none_tg         | 336 ms                                                     | 305 ms: 1.10x faster                                            |
| async_tree_io_tg           | 936 ms                                                     | 863 ms: 1.09x faster                                            |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 573 ms: 1.07x faster                                            |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 552 ms: 1.06x faster                                            |
| async_tree_io              | 939 ms                                                     | 896 ms: 1.05x faster                                            |
| Geometric mean             | (ref)                                                      | 1.10x faster                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240710-linux-x86_64-brandtbucher-optimize-3.14.0a0-799510c |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------:|
| nbody          | 88.3 ms                                                    | 77.4 ms: 1.14x faster                                           |
| float          | 78.9 ms                                                    | 70.9 ms: 1.11x faster                                           |
| pidigits       | 191 ms                                                     | 186 ms: 1.03x faster                                            |
| Geometric mean | (ref)                                                      | 1.09x faster                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240710-linux-x86_64-brandtbucher-optimize-3.14.0a0-799510c |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_compile  | 137 ms                                                     | 130 ms: 1.05x faster                                            |
| regex_dna      | 221 ms                                                     | 223 ms: 1.01x slower                                            |
| regex_v8       | 25.1 ms                                                    | 25.6 ms: 1.02x slower                                           |
| regex_effbot   | 3.67 ms                                                    | 3.88 ms: 1.06x slower                                           |
| Geometric mean | (ref)                                                      | 1.01x slower                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240710-linux-x86_64-brandtbucher-optimize-3.14.0a0-799510c |
|---------------------|:----------------------------------------------------------:|:---------------------------------------------------------------:|
| xml_etree_parse     | 162 ms                                                     | 148 ms: 1.09x faster                                            |
| tomli_loads         | 2.12 sec                                                   | 1.94 sec: 1.09x faster                                          |
| json_loads          | 28.9 us                                                    | 27.4 us: 1.06x faster                                           |
| xml_etree_process   | 61.2 ms                                                    | 58.1 ms: 1.05x faster                                           |
| xml_etree_iterparse | 107 ms                                                     | 102 ms: 1.05x faster                                            |
| json_dumps          | 10.7 ms                                                    | 10.4 ms: 1.03x faster                                           |
| xml_etree_generate  | 87.4 ms                                                    | 84.8 ms: 1.03x faster                                           |
| pickle_pure_python  | 305 us                                                     | 303 us: 1.01x faster                                            |
| Geometric mean      | (ref)                                                      | 1.05x faster                                                    |

Benchmark hidden because not significant (1): unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240710-linux-x86_64-brandtbucher-optimize-3.14.0a0-799510c |
|------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.6 ms: 1.02x faster                                           |
| python_startup_no_site | 7.11 ms                                                    | 7.12 ms: 1.00x slower                                           |
| Geometric mean         | (ref)                                                      | 1.01x faster                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240710-linux-x86_64-brandtbucher-optimize-3.14.0a0-799510c |
|-----------------|:----------------------------------------------------------:|:---------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.87 ms: 1.14x faster                                           |
| genshi_text     | 23.7 ms                                                    | 27.0 ms: 1.14x slower                                           |
| django_template | 34.8 ms                                                    | 40.3 ms: 1.16x slower                                           |
| genshi_xml      | 51.6 ms                                                    | 62.2 ms: 1.20x slower                                           |
| Geometric mean  | (ref)                                                      | 1.09x slower                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240710-linux-x86_64-brandtbucher-optimize-3.14.0a0-799510c |
|----------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------:|
| deepcopy_memo              | 39.7 us                                                    | 27.2 us: 1.46x faster                                           |
| deepcopy                   | 367 us                                                     | 261 us: 1.41x faster                                            |
| richards                   | 50.9 ms                                                    | 38.5 ms: 1.32x faster                                           |
| richards_super             | 57.4 ms                                                    | 44.6 ms: 1.29x faster                                           |
| deepcopy_reduce            | 3.35 us                                                    | 2.64 us: 1.27x faster                                           |
| scimark_fft                | 392 ms                                                     | 316 ms: 1.24x faster                                            |
| spectral_norm              | 116 ms                                                     | 98.0 ms: 1.18x faster                                           |
| crypto_pyaes               | 77.5 ms                                                    | 66.6 ms: 1.16x faster                                           |
| async_tree_memoization_tg  | 444 ms                                                     | 382 ms: 1.16x faster                                            |
| async_tree_none            | 378 ms                                                     | 329 ms: 1.15x faster                                            |
| nbody                      | 88.3 ms                                                    | 77.4 ms: 1.14x faster                                           |
| mako                       | 11.2 ms                                                    | 9.87 ms: 1.14x faster                                           |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.67 ms: 1.13x faster                                           |
| async_tree_memoization     | 463 ms                                                     | 412 ms: 1.12x faster                                            |
| float                      | 78.9 ms                                                    | 70.9 ms: 1.11x faster                                           |
| async_tree_none_tg         | 336 ms                                                     | 305 ms: 1.10x faster                                            |
| chaos                      | 61.3 ms                                                    | 56.0 ms: 1.10x faster                                           |
| xml_etree_parse            | 162 ms                                                     | 148 ms: 1.09x faster                                            |
| tomli_loads                | 2.12 sec                                                   | 1.94 sec: 1.09x faster                                          |
| async_tree_io_tg           | 936 ms                                                     | 863 ms: 1.09x faster                                            |
| scimark_monte_carlo        | 69.2 ms                                                    | 64.1 ms: 1.08x faster                                           |
| pathlib                    | 17.3 ms                                                    | 16.1 ms: 1.08x faster                                           |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 573 ms: 1.07x faster                                            |
| fannkuch                   | 402 ms                                                     | 377 ms: 1.07x faster                                            |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 552 ms: 1.06x faster                                            |
| telco                      | 8.41 ms                                                    | 7.90 ms: 1.06x faster                                           |
| pprint_pformat             | 1.56 sec                                                   | 1.47 sec: 1.06x faster                                          |
| pprint_safe_repr           | 758 ms                                                     | 716 ms: 1.06x faster                                            |
| logging_format             | 6.47 us                                                    | 6.11 us: 1.06x faster                                           |
| json_loads                 | 28.9 us                                                    | 27.4 us: 1.06x faster                                           |
| bpe_tokeniser              | 5.02 sec                                                   | 4.76 sec: 1.05x faster                                          |
| regex_compile              | 137 ms                                                     | 130 ms: 1.05x faster                                            |
| xml_etree_process          | 61.2 ms                                                    | 58.1 ms: 1.05x faster                                           |
| xml_etree_iterparse        | 107 ms                                                     | 102 ms: 1.05x faster                                            |
| async_tree_io              | 939 ms                                                     | 896 ms: 1.05x faster                                            |
| gc_traversal               | 3.98 ms                                                    | 3.80 ms: 1.05x faster                                           |
| pyflate                    | 484 ms                                                     | 463 ms: 1.05x faster                                            |
| json                       | 5.31 ms                                                    | 5.08 ms: 1.04x faster                                           |
| create_gc_cycles           | 1.82 ms                                                    | 1.75 ms: 1.04x faster                                           |
| logging_simple             | 5.74 us                                                    | 5.54 us: 1.04x faster                                           |
| json_dumps                 | 10.7 ms                                                    | 10.4 ms: 1.03x faster                                           |
| go                         | 145 ms                                                     | 140 ms: 1.03x faster                                            |
| xml_etree_generate         | 87.4 ms                                                    | 84.8 ms: 1.03x faster                                           |
| mdp                        | 2.79 sec                                                   | 2.70 sec: 1.03x faster                                          |
| pidigits                   | 191 ms                                                     | 186 ms: 1.03x faster                                            |
| sqlglot_parse              | 1.32 ms                                                    | 1.28 ms: 1.03x faster                                           |
| meteor_contest             | 110 ms                                                     | 107 ms: 1.03x faster                                            |
| dulwich_log                | 67.2 ms                                                    | 65.4 ms: 1.03x faster                                           |
| logging_silent             | 105 ns                                                     | 102 ns: 1.02x faster                                            |
| thrift                     | 823 us                                                     | 806 us: 1.02x faster                                            |
| asyncio_websockets         | 567 ms                                                     | 556 ms: 1.02x faster                                            |
| python_startup             | 10.8 ms                                                    | 10.6 ms: 1.02x faster                                           |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.81 sec: 1.02x faster                                          |
| 2to3                       | 274 ms                                                     | 271 ms: 1.01x faster                                            |
| scimark_sor                | 127 ms                                                     | 126 ms: 1.01x faster                                            |
| pickle_pure_python         | 305 us                                                     | 303 us: 1.01x faster                                            |
| comprehensions             | 16.6 us                                                    | 16.6 us: 1.00x faster                                           |
| python_startup_no_site     | 7.11 ms                                                    | 7.12 ms: 1.00x slower                                           |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                           |
| sqlglot_transpile          | 1.63 ms                                                    | 1.65 ms: 1.01x slower                                           |
| regex_dna                  | 221 ms                                                     | 223 ms: 1.01x slower                                            |
| typing_runtime_protocols   | 165 us                                                     | 167 us: 1.01x slower                                            |
| asyncio_tcp                | 508 ms                                                     | 516 ms: 1.02x slower                                            |
| regex_v8                   | 25.1 ms                                                    | 25.6 ms: 1.02x slower                                           |
| bench_thread_pool          | 834 us                                                     | 853 us: 1.02x slower                                            |
| tornado_http               | 94.6 ms                                                    | 97.9 ms: 1.03x slower                                           |
| sqlglot_normalize          | 110 ms                                                     | 114 ms: 1.03x slower                                            |
| hexiom                     | 6.30 ms                                                    | 6.52 ms: 1.04x slower                                           |
| dask                       | 369 ms                                                     | 383 ms: 1.04x slower                                            |
| sympy_expand               | 473 ms                                                     | 493 ms: 1.04x slower                                            |
| deltablue                  | 3.25 ms                                                    | 3.43 ms: 1.05x slower                                           |
| regex_effbot               | 3.67 ms                                                    | 3.88 ms: 1.06x slower                                           |
| sympy_str                  | 282 ms                                                     | 302 ms: 1.07x slower                                            |
| sympy_sum                  | 156 ms                                                     | 168 ms: 1.08x slower                                            |
| sqlglot_optimize           | 55.5 ms                                                    | 60.0 ms: 1.08x slower                                           |
| genshi_text                | 23.7 ms                                                    | 27.0 ms: 1.14x slower                                           |
| html5lib                   | 67.2 ms                                                    | 77.0 ms: 1.15x slower                                           |
| nqueens                    | 81.4 ms                                                    | 94.1 ms: 1.16x slower                                           |
| django_template            | 34.8 ms                                                    | 40.3 ms: 1.16x slower                                           |
| async_generators           | 442 ms                                                     | 514 ms: 1.16x slower                                            |
| coroutines                 | 23.2 ms                                                    | 27.5 ms: 1.19x slower                                           |
| genshi_xml                 | 51.6 ms                                                    | 62.2 ms: 1.20x slower                                           |
| sympy_integrate            | 20.5 ms                                                    | 25.3 ms: 1.24x slower                                           |
| pylint                     | 317 ms                                                     | 425 ms: 1.34x slower                                            |
| generators                 | 29.6 ms                                                    | 47.6 ms: 1.61x slower                                           |
| docutils                   | 2.83 sec                                                   | 6.74 sec: 2.38x slower                                          |
| raytrace                   | 267 ms                                                     | 4.85 sec: 18.19x slower                                         |
| Geometric mean             | (ref)                                                      | 1.02x slower                                                    |

Benchmark hidden because not significant (4): scimark_lu, unpickle_pure_python, coverage, pycparser
Ignored benchmarks (12) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 97.87% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.07x