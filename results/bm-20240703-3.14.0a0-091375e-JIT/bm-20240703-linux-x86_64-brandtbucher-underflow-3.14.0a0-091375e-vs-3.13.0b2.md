# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: underflow
- machine: linux-x86_64
- commit hash: 091375e
- commit date: 2024-07-03
- overall geometric mean: 1.03x faster
- HPT reliability: 99.70%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240703-linux-x86_64-brandtbucher-underflow-3.14.0a0-091375e |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 279 ms: 1.02x slower                                             |
| docutils       | 2.83 sec                                                   | 3.01 sec: 1.07x slower                                           |
| html5lib       | 67.2 ms                                                    | 68.3 ms: 1.02x slower                                            |
| tornado_http   | 94.6 ms                                                    | 97.7 ms: 1.03x slower                                            |
| Geometric mean | (ref)                                                      | 1.03x slower                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240703-linux-x86_64-brandtbucher-underflow-3.14.0a0-091375e |
|----------------------------|:----------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_memoization_tg  | 444 ms                                                     | 379 ms: 1.17x faster                                             |
| async_tree_none            | 378 ms                                                     | 326 ms: 1.16x faster                                             |
| async_tree_none_tg         | 336 ms                                                     | 299 ms: 1.13x faster                                             |
| async_tree_memoization     | 463 ms                                                     | 412 ms: 1.12x faster                                             |
| async_tree_io_tg           | 936 ms                                                     | 845 ms: 1.11x faster                                             |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 543 ms: 1.08x faster                                             |
| async_tree_io              | 939 ms                                                     | 870 ms: 1.08x faster                                             |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 571 ms: 1.07x faster                                             |
| Geometric mean             | (ref)                                                      | 1.11x faster                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240703-linux-x86_64-brandtbucher-underflow-3.14.0a0-091375e |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 70.2 ms: 1.12x faster                                            |
| nbody          | 88.3 ms                                                    | 79.9 ms: 1.11x faster                                            |
| pidigits       | 191 ms                                                     | 186 ms: 1.03x faster                                             |
| Geometric mean | (ref)                                                      | 1.09x faster                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240703-linux-x86_64-brandtbucher-underflow-3.14.0a0-091375e |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_v8       | 25.1 ms                                                    | 24.3 ms: 1.03x faster                                            |
| regex_effbot   | 3.67 ms                                                    | 3.60 ms: 1.02x faster                                            |
| regex_compile  | 137 ms                                                     | 138 ms: 1.01x slower                                             |
| regex_dna      | 221 ms                                                     | 230 ms: 1.04x slower                                             |
| Geometric mean | (ref)                                                      | 1.00x faster                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240703-linux-x86_64-brandtbucher-underflow-3.14.0a0-091375e |
|----------------------|:----------------------------------------------------------:|:----------------------------------------------------------------:|
| xml_etree_parse      | 162 ms                                                     | 146 ms: 1.11x faster                                             |
| unpickle_pure_python | 218 us                                                     | 200 us: 1.09x faster                                             |
| xml_etree_iterparse  | 107 ms                                                     | 99.3 ms: 1.08x faster                                            |
| xml_etree_generate   | 87.4 ms                                                    | 80.9 ms: 1.08x faster                                            |
| xml_etree_process    | 61.2 ms                                                    | 57.5 ms: 1.06x faster                                            |
| json_loads           | 28.9 us                                                    | 27.3 us: 1.06x faster                                            |
| tomli_loads          | 2.12 sec                                                   | 2.03 sec: 1.05x faster                                           |
| json_dumps           | 10.7 ms                                                    | 10.4 ms: 1.03x faster                                            |
| pickle_pure_python   | 305 us                                                     | 297 us: 1.03x faster                                             |
| Geometric mean       | (ref)                                                      | 1.07x faster                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240703-linux-x86_64-brandtbucher-underflow-3.14.0a0-091375e |
|------------------------|:----------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                            |
| python_startup_no_site | 7.11 ms                                                    | 7.13 ms: 1.00x slower                                            |
| Geometric mean         | (ref)                                                      | 1.01x faster                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240703-linux-x86_64-brandtbucher-underflow-3.14.0a0-091375e |
|-----------------|:----------------------------------------------------------:|:----------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.86 ms: 1.14x faster                                            |
| genshi_text     | 23.7 ms                                                    | 24.1 ms: 1.02x slower                                            |
| django_template | 34.8 ms                                                    | 36.6 ms: 1.05x slower                                            |
| genshi_xml      | 51.6 ms                                                    | 62.6 ms: 1.21x slower                                            |
| Geometric mean  | (ref)                                                      | 1.03x slower                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240703-linux-x86_64-brandtbucher-underflow-3.14.0a0-091375e |
|----------------------------|:----------------------------------------------------------:|:----------------------------------------------------------------:|
| deepcopy_memo              | 39.7 us                                                    | 28.4 us: 1.40x faster                                            |
| deepcopy                   | 367 us                                                     | 274 us: 1.34x faster                                             |
| scimark_fft                | 392 ms                                                     | 312 ms: 1.26x faster                                             |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.30 ms: 1.23x faster                                            |
| deepcopy_reduce            | 3.35 us                                                    | 2.73 us: 1.22x faster                                            |
| scimark_monte_carlo        | 69.2 ms                                                    | 57.4 ms: 1.20x faster                                            |
| async_tree_memoization_tg  | 444 ms                                                     | 379 ms: 1.17x faster                                             |
| async_tree_none            | 378 ms                                                     | 326 ms: 1.16x faster                                             |
| crypto_pyaes               | 77.5 ms                                                    | 66.9 ms: 1.16x faster                                            |
| richards_super             | 57.4 ms                                                    | 49.7 ms: 1.16x faster                                            |
| richards                   | 50.9 ms                                                    | 44.6 ms: 1.14x faster                                            |
| mako                       | 11.2 ms                                                    | 9.86 ms: 1.14x faster                                            |
| pyflate                    | 484 ms                                                     | 427 ms: 1.13x faster                                             |
| async_tree_none_tg         | 336 ms                                                     | 299 ms: 1.13x faster                                             |
| async_tree_memoization     | 463 ms                                                     | 412 ms: 1.12x faster                                             |
| float                      | 78.9 ms                                                    | 70.2 ms: 1.12x faster                                            |
| spectral_norm              | 116 ms                                                     | 104 ms: 1.12x faster                                             |
| fannkuch                   | 402 ms                                                     | 362 ms: 1.11x faster                                             |
| async_tree_io_tg           | 936 ms                                                     | 845 ms: 1.11x faster                                             |
| xml_etree_parse            | 162 ms                                                     | 146 ms: 1.11x faster                                             |
| nbody                      | 88.3 ms                                                    | 79.9 ms: 1.11x faster                                            |
| mdp                        | 2.79 sec                                                   | 2.55 sec: 1.09x faster                                           |
| unpickle_pure_python       | 218 us                                                     | 200 us: 1.09x faster                                             |
| xml_etree_iterparse        | 107 ms                                                     | 99.3 ms: 1.08x faster                                            |
| xml_etree_generate         | 87.4 ms                                                    | 80.9 ms: 1.08x faster                                            |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 543 ms: 1.08x faster                                             |
| async_tree_io              | 939 ms                                                     | 870 ms: 1.08x faster                                             |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 571 ms: 1.07x faster                                             |
| pathlib                    | 17.3 ms                                                    | 16.2 ms: 1.07x faster                                            |
| xml_etree_process          | 61.2 ms                                                    | 57.5 ms: 1.06x faster                                            |
| logging_silent             | 105 ns                                                     | 98.4 ns: 1.06x faster                                            |
| json_loads                 | 28.9 us                                                    | 27.3 us: 1.06x faster                                            |
| telco                      | 8.41 ms                                                    | 7.97 ms: 1.06x faster                                            |
| bpe_tokeniser              | 5.02 sec                                                   | 4.78 sec: 1.05x faster                                           |
| tomli_loads                | 2.12 sec                                                   | 2.03 sec: 1.05x faster                                           |
| meteor_contest             | 110 ms                                                     | 106 ms: 1.04x faster                                             |
| json                       | 5.31 ms                                                    | 5.13 ms: 1.03x faster                                            |
| regex_v8                   | 25.1 ms                                                    | 24.3 ms: 1.03x faster                                            |
| gc_traversal               | 3.98 ms                                                    | 3.85 ms: 1.03x faster                                            |
| logging_format             | 6.47 us                                                    | 6.27 us: 1.03x faster                                            |
| json_dumps                 | 10.7 ms                                                    | 10.4 ms: 1.03x faster                                            |
| pidigits                   | 191 ms                                                     | 186 ms: 1.03x faster                                             |
| create_gc_cycles           | 1.82 ms                                                    | 1.76 ms: 1.03x faster                                            |
| logging_simple             | 5.74 us                                                    | 5.59 us: 1.03x faster                                            |
| pickle_pure_python         | 305 us                                                     | 297 us: 1.03x faster                                             |
| sqlglot_parse              | 1.32 ms                                                    | 1.29 ms: 1.03x faster                                            |
| chaos                      | 61.3 ms                                                    | 59.8 ms: 1.03x faster                                            |
| pprint_safe_repr           | 758 ms                                                     | 739 ms: 1.03x faster                                             |
| thrift                     | 823 us                                                     | 802 us: 1.03x faster                                             |
| python_startup             | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                            |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.81 sec: 1.02x faster                                           |
| regex_effbot               | 3.67 ms                                                    | 3.60 ms: 1.02x faster                                            |
| asyncio_websockets         | 567 ms                                                     | 559 ms: 1.01x faster                                             |
| go                         | 145 ms                                                     | 143 ms: 1.01x faster                                             |
| coverage                   | 93.1 ms                                                    | 92.4 ms: 1.01x faster                                            |
| coroutines                 | 23.2 ms                                                    | 23.0 ms: 1.01x faster                                            |
| bench_thread_pool          | 834 us                                                     | 837 us: 1.00x slower                                             |
| python_startup_no_site     | 7.11 ms                                                    | 7.13 ms: 1.00x slower                                            |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                            |
| sqlglot_transpile          | 1.63 ms                                                    | 1.64 ms: 1.01x slower                                            |
| regex_compile              | 137 ms                                                     | 138 ms: 1.01x slower                                             |
| html5lib                   | 67.2 ms                                                    | 68.3 ms: 1.02x slower                                            |
| 2to3                       | 274 ms                                                     | 279 ms: 1.02x slower                                             |
| genshi_text                | 23.7 ms                                                    | 24.1 ms: 1.02x slower                                            |
| scimark_lu                 | 122 ms                                                     | 124 ms: 1.02x slower                                             |
| tornado_http               | 94.6 ms                                                    | 97.7 ms: 1.03x slower                                            |
| scimark_sor                | 127 ms                                                     | 132 ms: 1.03x slower                                             |
| sqlglot_optimize           | 55.5 ms                                                    | 57.6 ms: 1.04x slower                                            |
| regex_dna                  | 221 ms                                                     | 230 ms: 1.04x slower                                             |
| async_generators           | 442 ms                                                     | 460 ms: 1.04x slower                                             |
| typing_runtime_protocols   | 165 us                                                     | 172 us: 1.04x slower                                             |
| hexiom                     | 6.30 ms                                                    | 6.59 ms: 1.05x slower                                            |
| nqueens                    | 81.4 ms                                                    | 85.4 ms: 1.05x slower                                            |
| django_template            | 34.8 ms                                                    | 36.6 ms: 1.05x slower                                            |
| docutils                   | 2.83 sec                                                   | 3.01 sec: 1.07x slower                                           |
| dulwich_log                | 67.2 ms                                                    | 71.8 ms: 1.07x slower                                            |
| sqlglot_normalize          | 110 ms                                                     | 119 ms: 1.08x slower                                             |
| sympy_str                  | 282 ms                                                     | 309 ms: 1.09x slower                                             |
| sympy_expand               | 473 ms                                                     | 517 ms: 1.09x slower                                             |
| sympy_integrate            | 20.5 ms                                                    | 23.2 ms: 1.13x slower                                            |
| sympy_sum                  | 156 ms                                                     | 178 ms: 1.14x slower                                             |
| genshi_xml                 | 51.6 ms                                                    | 62.6 ms: 1.21x slower                                            |
| pylint                     | 317 ms                                                     | 397 ms: 1.25x slower                                             |
| deltablue                  | 3.25 ms                                                    | 4.10 ms: 1.26x slower                                            |
| generators                 | 29.6 ms                                                    | 48.4 ms: 1.63x slower                                            |
| Geometric mean             | (ref)                                                      | 1.03x faster                                                     |

Benchmark hidden because not significant (6): dask, asyncio_tcp, comprehensions, pycparser, pprint_pformat, raytrace
Ignored benchmarks (12) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 99.70% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.07x