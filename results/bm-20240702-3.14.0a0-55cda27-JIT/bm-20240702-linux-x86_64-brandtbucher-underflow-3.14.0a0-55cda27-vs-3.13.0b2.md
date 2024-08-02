# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: underflow
- machine: linux-x86_64
- commit hash: 55cda27
- commit date: 2024-07-02
- overall geometric mean: 1.02x faster
- HPT reliability: 96.79%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240702-linux-x86_64-brandtbucher-underflow-3.14.0a0-55cda27 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 284 ms: 1.04x slower                                             |
| docutils       | 2.83 sec                                                   | 3.03 sec: 1.07x slower                                           |
| html5lib       | 67.2 ms                                                    | 68.4 ms: 1.02x slower                                            |
| tornado_http   | 94.6 ms                                                    | 97.4 ms: 1.03x slower                                            |
| Geometric mean | (ref)                                                      | 1.04x slower                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240702-linux-x86_64-brandtbucher-underflow-3.14.0a0-55cda27 |
|----------------------------|:----------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_memoization_tg  | 444 ms                                                     | 381 ms: 1.17x faster                                             |
| async_tree_none            | 378 ms                                                     | 326 ms: 1.16x faster                                             |
| async_tree_memoization     | 463 ms                                                     | 411 ms: 1.13x faster                                             |
| async_tree_none_tg         | 336 ms                                                     | 299 ms: 1.13x faster                                             |
| async_tree_io_tg           | 936 ms                                                     | 842 ms: 1.11x faster                                             |
| async_tree_io              | 939 ms                                                     | 863 ms: 1.09x faster                                             |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 543 ms: 1.08x faster                                             |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 567 ms: 1.08x faster                                             |
| Geometric mean             | (ref)                                                      | 1.12x faster                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240702-linux-x86_64-brandtbucher-underflow-3.14.0a0-55cda27 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 69.6 ms: 1.13x faster                                            |
| nbody          | 88.3 ms                                                    | 79.1 ms: 1.12x faster                                            |
| pidigits       | 191 ms                                                     | 186 ms: 1.03x faster                                             |
| Geometric mean | (ref)                                                      | 1.09x faster                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240702-linux-x86_64-brandtbucher-underflow-3.14.0a0-55cda27 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_compile  | 137 ms                                                     | 139 ms: 1.01x slower                                             |
| regex_v8       | 25.1 ms                                                    | 26.0 ms: 1.04x slower                                            |
| Geometric mean | (ref)                                                      | 1.01x slower                                                     |

Benchmark hidden because not significant (2): regex_dna, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240702-linux-x86_64-brandtbucher-underflow-3.14.0a0-55cda27 |
|----------------------|:----------------------------------------------------------:|:----------------------------------------------------------------:|
| xml_etree_parse      | 162 ms                                                     | 148 ms: 1.09x faster                                             |
| xml_etree_iterparse  | 107 ms                                                     | 99.7 ms: 1.08x faster                                            |
| unpickle_pure_python | 218 us                                                     | 204 us: 1.07x faster                                             |
| xml_etree_generate   | 87.4 ms                                                    | 82.0 ms: 1.07x faster                                            |
| xml_etree_process    | 61.2 ms                                                    | 57.9 ms: 1.06x faster                                            |
| tomli_loads          | 2.12 sec                                                   | 2.04 sec: 1.04x faster                                           |
| json_loads           | 28.9 us                                                    | 27.8 us: 1.04x faster                                            |
| json_dumps           | 10.7 ms                                                    | 10.4 ms: 1.03x faster                                            |
| pickle_pure_python   | 305 us                                                     | 300 us: 1.02x faster                                             |
| Geometric mean       | (ref)                                                      | 1.05x faster                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240702-linux-x86_64-brandtbucher-underflow-3.14.0a0-55cda27 |
|------------------------|:----------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.5 ms: 1.03x faster                                            |
| python_startup_no_site | 7.11 ms                                                    | 7.08 ms: 1.00x faster                                            |
| Geometric mean         | (ref)                                                      | 1.02x faster                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240702-linux-x86_64-brandtbucher-underflow-3.14.0a0-55cda27 |
|-----------------|:----------------------------------------------------------:|:----------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.61 ms: 1.17x faster                                            |
| genshi_text     | 23.7 ms                                                    | 24.4 ms: 1.03x slower                                            |
| django_template | 34.8 ms                                                    | 36.9 ms: 1.06x slower                                            |
| genshi_xml      | 51.6 ms                                                    | 62.7 ms: 1.21x slower                                            |
| Geometric mean  | (ref)                                                      | 1.03x slower                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240702-linux-x86_64-brandtbucher-underflow-3.14.0a0-55cda27 |
|----------------------------|:----------------------------------------------------------:|:----------------------------------------------------------------:|
| deepcopy_memo              | 39.7 us                                                    | 28.4 us: 1.40x faster                                            |
| deepcopy                   | 367 us                                                     | 274 us: 1.34x faster                                             |
| scimark_fft                | 392 ms                                                     | 305 ms: 1.29x faster                                             |
| deepcopy_reduce            | 3.35 us                                                    | 2.77 us: 1.21x faster                                            |
| scimark_monte_carlo        | 69.2 ms                                                    | 57.3 ms: 1.21x faster                                            |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.37 ms: 1.21x faster                                            |
| mako                       | 11.2 ms                                                    | 9.61 ms: 1.17x faster                                            |
| async_tree_memoization_tg  | 444 ms                                                     | 381 ms: 1.17x faster                                             |
| async_tree_none            | 378 ms                                                     | 326 ms: 1.16x faster                                             |
| crypto_pyaes               | 77.5 ms                                                    | 66.8 ms: 1.16x faster                                            |
| richards                   | 50.9 ms                                                    | 44.2 ms: 1.15x faster                                            |
| richards_super             | 57.4 ms                                                    | 50.1 ms: 1.15x faster                                            |
| float                      | 78.9 ms                                                    | 69.6 ms: 1.13x faster                                            |
| async_tree_memoization     | 463 ms                                                     | 411 ms: 1.13x faster                                             |
| async_tree_none_tg         | 336 ms                                                     | 299 ms: 1.13x faster                                             |
| spectral_norm              | 116 ms                                                     | 103 ms: 1.12x faster                                             |
| pyflate                    | 484 ms                                                     | 432 ms: 1.12x faster                                             |
| nbody                      | 88.3 ms                                                    | 79.1 ms: 1.12x faster                                            |
| fannkuch                   | 402 ms                                                     | 360 ms: 1.12x faster                                             |
| async_tree_io_tg           | 936 ms                                                     | 842 ms: 1.11x faster                                             |
| mdp                        | 2.79 sec                                                   | 2.55 sec: 1.09x faster                                           |
| xml_etree_parse            | 162 ms                                                     | 148 ms: 1.09x faster                                             |
| async_tree_io              | 939 ms                                                     | 863 ms: 1.09x faster                                             |
| pathlib                    | 17.3 ms                                                    | 15.9 ms: 1.09x faster                                            |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 543 ms: 1.08x faster                                             |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 567 ms: 1.08x faster                                             |
| xml_etree_iterparse        | 107 ms                                                     | 99.7 ms: 1.08x faster                                            |
| logging_silent             | 105 ns                                                     | 97.6 ns: 1.07x faster                                            |
| unpickle_pure_python       | 218 us                                                     | 204 us: 1.07x faster                                             |
| xml_etree_generate         | 87.4 ms                                                    | 82.0 ms: 1.07x faster                                            |
| xml_etree_process          | 61.2 ms                                                    | 57.9 ms: 1.06x faster                                            |
| logging_format             | 6.47 us                                                    | 6.17 us: 1.05x faster                                            |
| telco                      | 8.41 ms                                                    | 8.07 ms: 1.04x faster                                            |
| json                       | 5.31 ms                                                    | 5.09 ms: 1.04x faster                                            |
| gc_traversal               | 3.98 ms                                                    | 3.81 ms: 1.04x faster                                            |
| bpe_tokeniser              | 5.02 sec                                                   | 4.82 sec: 1.04x faster                                           |
| tomli_loads                | 2.12 sec                                                   | 2.04 sec: 1.04x faster                                           |
| json_loads                 | 28.9 us                                                    | 27.8 us: 1.04x faster                                            |
| create_gc_cycles           | 1.82 ms                                                    | 1.75 ms: 1.04x faster                                            |
| logging_simple             | 5.74 us                                                    | 5.55 us: 1.03x faster                                            |
| json_dumps                 | 10.7 ms                                                    | 10.4 ms: 1.03x faster                                            |
| thrift                     | 823 us                                                     | 799 us: 1.03x faster                                             |
| pidigits                   | 191 ms                                                     | 186 ms: 1.03x faster                                             |
| python_startup             | 10.8 ms                                                    | 10.5 ms: 1.03x faster                                            |
| meteor_contest             | 110 ms                                                     | 107 ms: 1.03x faster                                             |
| sqlglot_parse              | 1.32 ms                                                    | 1.29 ms: 1.03x faster                                            |
| pprint_safe_repr           | 758 ms                                                     | 744 ms: 1.02x faster                                             |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.81 sec: 1.02x faster                                           |
| pickle_pure_python         | 305 us                                                     | 300 us: 1.02x faster                                             |
| asyncio_websockets         | 567 ms                                                     | 558 ms: 1.01x faster                                             |
| chaos                      | 61.3 ms                                                    | 60.5 ms: 1.01x faster                                            |
| comprehensions             | 16.6 us                                                    | 16.5 us: 1.01x faster                                            |
| python_startup_no_site     | 7.11 ms                                                    | 7.08 ms: 1.00x faster                                            |
| bench_thread_pool          | 834 us                                                     | 836 us: 1.00x slower                                             |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                            |
| sqlglot_transpile          | 1.63 ms                                                    | 1.65 ms: 1.01x slower                                            |
| raytrace                   | 267 ms                                                     | 270 ms: 1.01x slower                                             |
| regex_compile              | 137 ms                                                     | 139 ms: 1.01x slower                                             |
| html5lib                   | 67.2 ms                                                    | 68.4 ms: 1.02x slower                                            |
| pprint_pformat             | 1.56 sec                                                   | 1.59 sec: 1.02x slower                                           |
| tornado_http               | 94.6 ms                                                    | 97.4 ms: 1.03x slower                                            |
| genshi_text                | 23.7 ms                                                    | 24.4 ms: 1.03x slower                                            |
| scimark_lu                 | 122 ms                                                     | 126 ms: 1.03x slower                                             |
| sqlglot_optimize           | 55.5 ms                                                    | 57.5 ms: 1.04x slower                                            |
| regex_v8                   | 25.1 ms                                                    | 26.0 ms: 1.04x slower                                            |
| 2to3                       | 274 ms                                                     | 284 ms: 1.04x slower                                             |
| scimark_sor                | 127 ms                                                     | 132 ms: 1.04x slower                                             |
| async_generators           | 442 ms                                                     | 459 ms: 1.04x slower                                             |
| pycparser                  | 1.16 sec                                                   | 1.21 sec: 1.04x slower                                           |
| hexiom                     | 6.30 ms                                                    | 6.58 ms: 1.04x slower                                            |
| typing_runtime_protocols   | 165 us                                                     | 172 us: 1.05x slower                                             |
| django_template            | 34.8 ms                                                    | 36.9 ms: 1.06x slower                                            |
| nqueens                    | 81.4 ms                                                    | 86.7 ms: 1.07x slower                                            |
| docutils                   | 2.83 sec                                                   | 3.03 sec: 1.07x slower                                           |
| dulwich_log                | 67.2 ms                                                    | 72.3 ms: 1.08x slower                                            |
| sqlglot_normalize          | 110 ms                                                     | 119 ms: 1.08x slower                                             |
| sympy_expand               | 473 ms                                                     | 517 ms: 1.09x slower                                             |
| sympy_str                  | 282 ms                                                     | 310 ms: 1.10x slower                                             |
| sympy_integrate            | 20.5 ms                                                    | 23.2 ms: 1.13x slower                                            |
| sympy_sum                  | 156 ms                                                     | 179 ms: 1.15x slower                                             |
| genshi_xml                 | 51.6 ms                                                    | 62.7 ms: 1.21x slower                                            |
| pylint                     | 317 ms                                                     | 398 ms: 1.26x slower                                             |
| deltablue                  | 3.25 ms                                                    | 4.10 ms: 1.26x slower                                            |
| generators                 | 29.6 ms                                                    | 51.2 ms: 1.73x slower                                            |
| Geometric mean             | (ref)                                                      | 1.02x faster                                                     |

Benchmark hidden because not significant (7): asyncio_tcp, go, dask, regex_dna, coroutines, regex_effbot, coverage
Ignored benchmarks (12) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 96.79% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.07x