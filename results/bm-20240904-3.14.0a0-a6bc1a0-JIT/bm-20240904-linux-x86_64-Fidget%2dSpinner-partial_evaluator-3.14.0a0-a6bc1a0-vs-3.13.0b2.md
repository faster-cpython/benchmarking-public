# Results vs. 3.13.0b2

- fork: Fidget-Spinner
- ref: partial_evaluator
- machine: linux-x86_64
- commit hash: a6bc1a0
- commit date: 2024-09-04
- overall geometric mean: 1.05x faster
- HPT reliability: 99.94%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240904-linux-x86_64-Fidget%2dSpinner-partial_evaluator-3.14.0a0-a6bc1a0 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 276 ms: 1.01x slower                                                         |
| docutils       | 2.83 sec                                                   | 2.95 sec: 1.04x slower                                                       |
| html5lib       | 67.2 ms                                                    | 62.4 ms: 1.08x faster                                                        |
| tornado_http   | 94.6 ms                                                    | 95.0 ms: 1.00x slower                                                        |
| Geometric mean | (ref)                                                      | 1.01x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240904-linux-x86_64-Fidget%2dSpinner-partial_evaluator-3.14.0a0-a6bc1a0 |
|----------------------------|:----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 331 ms: 1.14x faster                                                         |
| async_tree_memoization     | 463 ms                                                     | 414 ms: 1.12x faster                                                         |
| async_tree_memoization_tg  | 444 ms                                                     | 410 ms: 1.08x faster                                                         |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 568 ms: 1.08x faster                                                         |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 550 ms: 1.07x faster                                                         |
| async_tree_none_tg         | 336 ms                                                     | 316 ms: 1.07x faster                                                         |
| async_tree_io_tg           | 936 ms                                                     | 910 ms: 1.03x faster                                                         |
| Geometric mean             | (ref)                                                      | 1.07x faster                                                                 |

Benchmark hidden because not significant (1): async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240904-linux-x86_64-Fidget%2dSpinner-partial_evaluator-3.14.0a0-a6bc1a0 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 70.9 ms: 1.11x faster                                                        |
| nbody          | 88.3 ms                                                    | 80.0 ms: 1.10x faster                                                        |
| pidigits       | 191 ms                                                     | 188 ms: 1.02x faster                                                         |
| Geometric mean | (ref)                                                      | 1.08x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240904-linux-x86_64-Fidget%2dSpinner-partial_evaluator-3.14.0a0-a6bc1a0 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_dna      | 221 ms                                                     | 212 ms: 1.04x faster                                                         |
| regex_effbot   | 3.67 ms                                                    | 3.58 ms: 1.03x faster                                                        |
| regex_v8       | 25.1 ms                                                    | 24.7 ms: 1.02x faster                                                        |
| regex_compile  | 137 ms                                                     | 141 ms: 1.03x slower                                                         |
| Geometric mean | (ref)                                                      | 1.01x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240904-linux-x86_64-Fidget%2dSpinner-partial_evaluator-3.14.0a0-a6bc1a0 |
|----------------------|:----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_generate   | 87.4 ms                                                    | 77.4 ms: 1.13x faster                                                        |
| xml_etree_process    | 61.2 ms                                                    | 54.5 ms: 1.12x faster                                                        |
| xml_etree_parse      | 162 ms                                                     | 146 ms: 1.10x faster                                                         |
| tomli_loads          | 2.12 sec                                                   | 1.92 sec: 1.10x faster                                                       |
| xml_etree_iterparse  | 107 ms                                                     | 98.8 ms: 1.09x faster                                                        |
| json_dumps           | 10.7 ms                                                    | 10.3 ms: 1.04x faster                                                        |
| unpickle_pure_python | 218 us                                                     | 214 us: 1.02x faster                                                         |
| pickle_pure_python   | 305 us                                                     | 300 us: 1.02x faster                                                         |
| json_loads           | 28.9 us                                                    | 28.6 us: 1.01x faster                                                        |
| Geometric mean       | (ref)                                                      | 1.07x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240904-linux-x86_64-Fidget%2dSpinner-partial_evaluator-3.14.0a0-a6bc1a0 |
|------------------------|:----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.6 ms: 1.02x faster                                                        |
| python_startup_no_site | 7.11 ms                                                    | 7.21 ms: 1.01x slower                                                        |
| Geometric mean         | (ref)                                                      | 1.00x faster                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240904-linux-x86_64-Fidget%2dSpinner-partial_evaluator-3.14.0a0-a6bc1a0 |
|-----------------|:----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.72 ms: 1.16x faster                                                        |
| django_template | 34.8 ms                                                    | 35.9 ms: 1.03x slower                                                        |
| genshi_text     | 23.7 ms                                                    | 24.6 ms: 1.04x slower                                                        |
| genshi_xml      | 51.6 ms                                                    | 56.6 ms: 1.10x slower                                                        |
| Geometric mean  | (ref)                                                      | 1.00x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240904-linux-x86_64-Fidget%2dSpinner-partial_evaluator-3.14.0a0-a6bc1a0 |
|----------------------------|:----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| deepcopy_memo              | 39.7 us                                                    | 27.0 us: 1.47x faster                                                        |
| deepcopy                   | 367 us                                                     | 261 us: 1.40x faster                                                         |
| richards                   | 50.9 ms                                                    | 39.2 ms: 1.30x faster                                                        |
| richards_super             | 57.4 ms                                                    | 44.8 ms: 1.28x faster                                                        |
| scimark_fft                | 392 ms                                                     | 309 ms: 1.27x faster                                                         |
| deepcopy_reduce            | 3.35 us                                                    | 2.67 us: 1.25x faster                                                        |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.37 ms: 1.21x faster                                                        |
| crypto_pyaes               | 77.5 ms                                                    | 65.7 ms: 1.18x faster                                                        |
| mako                       | 11.2 ms                                                    | 9.72 ms: 1.16x faster                                                        |
| async_tree_none            | 378 ms                                                     | 331 ms: 1.14x faster                                                         |
| spectral_norm              | 116 ms                                                     | 103 ms: 1.13x faster                                                         |
| xml_etree_generate         | 87.4 ms                                                    | 77.4 ms: 1.13x faster                                                        |
| bpe_tokeniser              | 5.02 sec                                                   | 4.46 sec: 1.13x faster                                                       |
| xml_etree_process          | 61.2 ms                                                    | 54.5 ms: 1.12x faster                                                        |
| async_tree_memoization     | 463 ms                                                     | 414 ms: 1.12x faster                                                         |
| float                      | 78.9 ms                                                    | 70.9 ms: 1.11x faster                                                        |
| go                         | 145 ms                                                     | 130 ms: 1.11x faster                                                         |
| scimark_lu                 | 122 ms                                                     | 110 ms: 1.11x faster                                                         |
| xml_etree_parse            | 162 ms                                                     | 146 ms: 1.10x faster                                                         |
| tomli_loads                | 2.12 sec                                                   | 1.92 sec: 1.10x faster                                                       |
| nbody                      | 88.3 ms                                                    | 80.0 ms: 1.10x faster                                                        |
| pathlib                    | 17.3 ms                                                    | 15.7 ms: 1.10x faster                                                        |
| mdp                        | 2.79 sec                                                   | 2.54 sec: 1.10x faster                                                       |
| scimark_monte_carlo        | 69.2 ms                                                    | 63.2 ms: 1.09x faster                                                        |
| xml_etree_iterparse        | 107 ms                                                     | 98.8 ms: 1.09x faster                                                        |
| fannkuch                   | 402 ms                                                     | 371 ms: 1.08x faster                                                         |
| async_tree_memoization_tg  | 444 ms                                                     | 410 ms: 1.08x faster                                                         |
| scimark_sor                | 127 ms                                                     | 118 ms: 1.08x faster                                                         |
| coverage                   | 93.1 ms                                                    | 86.4 ms: 1.08x faster                                                        |
| html5lib                   | 67.2 ms                                                    | 62.4 ms: 1.08x faster                                                        |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 568 ms: 1.08x faster                                                         |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 550 ms: 1.07x faster                                                         |
| async_tree_none_tg         | 336 ms                                                     | 316 ms: 1.07x faster                                                         |
| telco                      | 8.41 ms                                                    | 7.91 ms: 1.06x faster                                                        |
| pyflate                    | 484 ms                                                     | 456 ms: 1.06x faster                                                         |
| gc_traversal               | 3.98 ms                                                    | 3.77 ms: 1.05x faster                                                        |
| logging_format             | 6.47 us                                                    | 6.14 us: 1.05x faster                                                        |
| thrift                     | 823 us                                                     | 782 us: 1.05x faster                                                         |
| regex_dna                  | 221 ms                                                     | 212 ms: 1.04x faster                                                         |
| pprint_safe_repr           | 758 ms                                                     | 729 ms: 1.04x faster                                                         |
| json_dumps                 | 10.7 ms                                                    | 10.3 ms: 1.04x faster                                                        |
| chaos                      | 61.3 ms                                                    | 59.1 ms: 1.04x faster                                                        |
| meteor_contest             | 110 ms                                                     | 106 ms: 1.03x faster                                                         |
| logging_silent             | 105 ns                                                     | 102 ns: 1.03x faster                                                         |
| async_tree_io_tg           | 936 ms                                                     | 910 ms: 1.03x faster                                                         |
| asyncio_tcp                | 508 ms                                                     | 494 ms: 1.03x faster                                                         |
| pprint_pformat             | 1.56 sec                                                   | 1.51 sec: 1.03x faster                                                       |
| regex_effbot               | 3.67 ms                                                    | 3.58 ms: 1.03x faster                                                        |
| logging_simple             | 5.74 us                                                    | 5.61 us: 1.02x faster                                                        |
| deltablue                  | 3.25 ms                                                    | 3.18 ms: 1.02x faster                                                        |
| asyncio_websockets         | 567 ms                                                     | 555 ms: 1.02x faster                                                         |
| pidigits                   | 191 ms                                                     | 188 ms: 1.02x faster                                                         |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.81 sec: 1.02x faster                                                       |
| unpickle_pure_python       | 218 us                                                     | 214 us: 1.02x faster                                                         |
| create_gc_cycles           | 1.82 ms                                                    | 1.78 ms: 1.02x faster                                                        |
| pickle_pure_python         | 305 us                                                     | 300 us: 1.02x faster                                                         |
| regex_v8                   | 25.1 ms                                                    | 24.7 ms: 1.02x faster                                                        |
| python_startup             | 10.8 ms                                                    | 10.6 ms: 1.02x faster                                                        |
| coroutines                 | 23.2 ms                                                    | 22.9 ms: 1.01x faster                                                        |
| json_loads                 | 28.9 us                                                    | 28.6 us: 1.01x faster                                                        |
| comprehensions             | 16.6 us                                                    | 16.5 us: 1.01x faster                                                        |
| bench_thread_pool          | 834 us                                                     | 831 us: 1.00x faster                                                         |
| tornado_http               | 94.6 ms                                                    | 95.0 ms: 1.00x slower                                                        |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                                        |
| sqlglot_parse              | 1.32 ms                                                    | 1.33 ms: 1.01x slower                                                        |
| 2to3                       | 274 ms                                                     | 276 ms: 1.01x slower                                                         |
| python_startup_no_site     | 7.11 ms                                                    | 7.21 ms: 1.01x slower                                                        |
| dulwich_log                | 67.2 ms                                                    | 68.4 ms: 1.02x slower                                                        |
| sqlglot_normalize          | 110 ms                                                     | 112 ms: 1.02x slower                                                         |
| raytrace                   | 267 ms                                                     | 272 ms: 1.02x slower                                                         |
| sqlglot_transpile          | 1.63 ms                                                    | 1.68 ms: 1.03x slower                                                        |
| django_template            | 34.8 ms                                                    | 35.9 ms: 1.03x slower                                                        |
| regex_compile              | 137 ms                                                     | 141 ms: 1.03x slower                                                         |
| genshi_text                | 23.7 ms                                                    | 24.6 ms: 1.04x slower                                                        |
| async_generators           | 442 ms                                                     | 459 ms: 1.04x slower                                                         |
| sqlglot_optimize           | 55.5 ms                                                    | 57.8 ms: 1.04x slower                                                        |
| docutils                   | 2.83 sec                                                   | 2.95 sec: 1.04x slower                                                       |
| nqueens                    | 81.4 ms                                                    | 85.3 ms: 1.05x slower                                                        |
| pycparser                  | 1.16 sec                                                   | 1.22 sec: 1.05x slower                                                       |
| sympy_str                  | 282 ms                                                     | 299 ms: 1.06x slower                                                         |
| sympy_expand               | 473 ms                                                     | 507 ms: 1.07x slower                                                         |
| genshi_xml                 | 51.6 ms                                                    | 56.6 ms: 1.10x slower                                                        |
| hexiom                     | 6.30 ms                                                    | 6.92 ms: 1.10x slower                                                        |
| sympy_sum                  | 156 ms                                                     | 172 ms: 1.11x slower                                                         |
| sympy_integrate            | 20.5 ms                                                    | 22.7 ms: 1.11x slower                                                        |
| generators                 | 29.6 ms                                                    | 32.9 ms: 1.11x slower                                                        |
| pylint                     | 317 ms                                                     | 372 ms: 1.17x slower                                                         |
| Geometric mean             | (ref)                                                      | 1.05x faster                                                                 |

Benchmark hidden because not significant (3): json, async_tree_io, typing_runtime_protocols
Ignored benchmarks (13) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 99.94% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.09x