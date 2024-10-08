# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: exit_if
- machine: linux-x86_64
- commit hash: a0f1853
- commit date: 2024-08-12
- overall geometric mean: 1.05x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240812-linux-x86_64-brandtbucher-exit_if-3.14.0a0-a0f1853 |
|----------------|:----------------------------------------------------------:|:--------------------------------------------------------------:|
| docutils       | 2.83 sec                                                   | 2.99 sec: 1.06x slower                                         |
| html5lib       | 67.2 ms                                                    | 66.1 ms: 1.02x faster                                          |
| tornado_http   | 94.6 ms                                                    | 92.3 ms: 1.03x faster                                          |
| Geometric mean | (ref)                                                      | 1.00x slower                                                   |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240812-linux-x86_64-brandtbucher-exit_if-3.14.0a0-a0f1853 |
|----------------------------|:----------------------------------------------------------:|:--------------------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 329 ms: 1.15x faster                                           |
| async_tree_memoization_tg  | 444 ms                                                     | 391 ms: 1.13x faster                                           |
| async_tree_memoization     | 463 ms                                                     | 412 ms: 1.13x faster                                           |
| async_tree_none_tg         | 336 ms                                                     | 301 ms: 1.12x faster                                           |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 531 ms: 1.11x faster                                           |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 564 ms: 1.08x faster                                           |
| async_tree_io_tg           | 936 ms                                                     | 866 ms: 1.08x faster                                           |
| async_tree_io              | 939 ms                                                     | 910 ms: 1.03x faster                                           |
| Geometric mean             | (ref)                                                      | 1.10x faster                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240812-linux-x86_64-brandtbucher-exit_if-3.14.0a0-a0f1853 |
|----------------|:----------------------------------------------------------:|:--------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 70.3 ms: 1.12x faster                                          |
| nbody          | 88.3 ms                                                    | 80.0 ms: 1.10x faster                                          |
| pidigits       | 191 ms                                                     | 186 ms: 1.03x faster                                           |
| Geometric mean | (ref)                                                      | 1.08x faster                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240812-linux-x86_64-brandtbucher-exit_if-3.14.0a0-a0f1853 |
|----------------|:----------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_v8       | 25.1 ms                                                    | 24.4 ms: 1.03x faster                                          |
| regex_dna      | 221 ms                                                     | 217 ms: 1.02x faster                                           |
| regex_compile  | 137 ms                                                     | 136 ms: 1.00x faster                                           |
| regex_effbot   | 3.67 ms                                                    | 3.70 ms: 1.01x slower                                          |
| Geometric mean | (ref)                                                      | 1.01x faster                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240812-linux-x86_64-brandtbucher-exit_if-3.14.0a0-a0f1853 |
|----------------------|:----------------------------------------------------------:|:--------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                                   | 1.90 sec: 1.12x faster                                         |
| xml_etree_parse      | 162 ms                                                     | 146 ms: 1.11x faster                                           |
| xml_etree_iterparse  | 107 ms                                                     | 98.5 ms: 1.09x faster                                          |
| xml_etree_process    | 61.2 ms                                                    | 56.4 ms: 1.08x faster                                          |
| xml_etree_generate   | 87.4 ms                                                    | 80.6 ms: 1.08x faster                                          |
| json_dumps           | 10.7 ms                                                    | 10.2 ms: 1.05x faster                                          |
| json_loads           | 28.9 us                                                    | 27.7 us: 1.04x faster                                          |
| unpickle_pure_python | 218 us                                                     | 210 us: 1.04x faster                                           |
| pickle_pure_python   | 305 us                                                     | 300 us: 1.02x faster                                           |
| Geometric mean       | (ref)                                                      | 1.07x faster                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240812-linux-x86_64-brandtbucher-exit_if-3.14.0a0-a0f1853 |
|------------------------|:----------------------------------------------------------:|:--------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                          |
| python_startup_no_site | 7.11 ms                                                    | 7.13 ms: 1.00x slower                                          |
| Geometric mean         | (ref)                                                      | 1.01x faster                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240812-linux-x86_64-brandtbucher-exit_if-3.14.0a0-a0f1853 |
|-----------------|:----------------------------------------------------------:|:--------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.82 ms: 1.14x faster                                          |
| django_template | 34.8 ms                                                    | 35.2 ms: 1.01x slower                                          |
| genshi_text     | 23.7 ms                                                    | 24.7 ms: 1.04x slower                                          |
| genshi_xml      | 51.6 ms                                                    | 55.7 ms: 1.08x slower                                          |
| Geometric mean  | (ref)                                                      | 1.00x faster                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240812-linux-x86_64-brandtbucher-exit_if-3.14.0a0-a0f1853 |
|----------------------------|:----------------------------------------------------------:|:--------------------------------------------------------------:|
| deepcopy_memo              | 39.7 us                                                    | 26.3 us: 1.51x faster                                          |
| deepcopy                   | 367 us                                                     | 261 us: 1.41x faster                                           |
| richards                   | 50.9 ms                                                    | 40.0 ms: 1.27x faster                                          |
| scimark_fft                | 392 ms                                                     | 309 ms: 1.27x faster                                           |
| deepcopy_reduce            | 3.35 us                                                    | 2.65 us: 1.26x faster                                          |
| richards_super             | 57.4 ms                                                    | 46.1 ms: 1.24x faster                                          |
| crypto_pyaes               | 77.5 ms                                                    | 65.7 ms: 1.18x faster                                          |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.50 ms: 1.17x faster                                          |
| async_tree_none            | 378 ms                                                     | 329 ms: 1.15x faster                                           |
| mako                       | 11.2 ms                                                    | 9.82 ms: 1.14x faster                                          |
| spectral_norm              | 116 ms                                                     | 102 ms: 1.14x faster                                           |
| async_tree_memoization_tg  | 444 ms                                                     | 391 ms: 1.13x faster                                           |
| async_tree_memoization     | 463 ms                                                     | 412 ms: 1.13x faster                                           |
| float                      | 78.9 ms                                                    | 70.3 ms: 1.12x faster                                          |
| scimark_sor                | 127 ms                                                     | 114 ms: 1.12x faster                                           |
| bpe_tokeniser              | 5.02 sec                                                   | 4.49 sec: 1.12x faster                                         |
| scimark_lu                 | 122 ms                                                     | 109 ms: 1.12x faster                                           |
| scimark_monte_carlo        | 69.2 ms                                                    | 62.0 ms: 1.12x faster                                          |
| async_tree_none_tg         | 336 ms                                                     | 301 ms: 1.12x faster                                           |
| tomli_loads                | 2.12 sec                                                   | 1.90 sec: 1.12x faster                                         |
| xml_etree_parse            | 162 ms                                                     | 146 ms: 1.11x faster                                           |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 531 ms: 1.11x faster                                           |
| nbody                      | 88.3 ms                                                    | 80.0 ms: 1.10x faster                                          |
| fannkuch                   | 402 ms                                                     | 365 ms: 1.10x faster                                           |
| mdp                        | 2.79 sec                                                   | 2.55 sec: 1.09x faster                                         |
| xml_etree_iterparse        | 107 ms                                                     | 98.5 ms: 1.09x faster                                          |
| xml_etree_process          | 61.2 ms                                                    | 56.4 ms: 1.08x faster                                          |
| xml_etree_generate         | 87.4 ms                                                    | 80.6 ms: 1.08x faster                                          |
| logging_format             | 6.47 us                                                    | 5.97 us: 1.08x faster                                          |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 564 ms: 1.08x faster                                           |
| pathlib                    | 17.3 ms                                                    | 16.0 ms: 1.08x faster                                          |
| async_tree_io_tg           | 936 ms                                                     | 866 ms: 1.08x faster                                           |
| telco                      | 8.41 ms                                                    | 7.83 ms: 1.07x faster                                          |
| pyflate                    | 484 ms                                                     | 452 ms: 1.07x faster                                           |
| logging_silent             | 105 ns                                                     | 98.0 ns: 1.07x faster                                          |
| logging_simple             | 5.74 us                                                    | 5.42 us: 1.06x faster                                          |
| chaos                      | 61.3 ms                                                    | 58.0 ms: 1.06x faster                                          |
| gc_traversal               | 3.98 ms                                                    | 3.76 ms: 1.06x faster                                          |
| json_dumps                 | 10.7 ms                                                    | 10.2 ms: 1.05x faster                                          |
| meteor_contest             | 110 ms                                                     | 105 ms: 1.05x faster                                           |
| thrift                     | 823 us                                                     | 786 us: 1.05x faster                                           |
| deltablue                  | 3.25 ms                                                    | 3.11 ms: 1.04x faster                                          |
| json_loads                 | 28.9 us                                                    | 27.7 us: 1.04x faster                                          |
| unpickle_pure_python       | 218 us                                                     | 210 us: 1.04x faster                                           |
| json                       | 5.31 ms                                                    | 5.13 ms: 1.03x faster                                          |
| create_gc_cycles           | 1.82 ms                                                    | 1.76 ms: 1.03x faster                                          |
| async_tree_io              | 939 ms                                                     | 910 ms: 1.03x faster                                           |
| pidigits                   | 191 ms                                                     | 186 ms: 1.03x faster                                           |
| regex_v8                   | 25.1 ms                                                    | 24.4 ms: 1.03x faster                                          |
| bench_thread_pool          | 834 us                                                     | 813 us: 1.03x faster                                           |
| tornado_http               | 94.6 ms                                                    | 92.3 ms: 1.03x faster                                          |
| comprehensions             | 16.6 us                                                    | 16.2 us: 1.02x faster                                          |
| sqlglot_parse              | 1.32 ms                                                    | 1.29 ms: 1.02x faster                                          |
| python_startup             | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                          |
| regex_dna                  | 221 ms                                                     | 217 ms: 1.02x faster                                           |
| pickle_pure_python         | 305 us                                                     | 300 us: 1.02x faster                                           |
| asyncio_websockets         | 567 ms                                                     | 557 ms: 1.02x faster                                           |
| html5lib                   | 67.2 ms                                                    | 66.1 ms: 1.02x faster                                          |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.81 sec: 1.02x faster                                         |
| asyncio_tcp                | 508 ms                                                     | 501 ms: 1.01x faster                                           |
| coverage                   | 93.1 ms                                                    | 92.0 ms: 1.01x faster                                          |
| raytrace                   | 267 ms                                                     | 264 ms: 1.01x faster                                           |
| pprint_safe_repr           | 758 ms                                                     | 751 ms: 1.01x faster                                           |
| regex_compile              | 137 ms                                                     | 136 ms: 1.00x faster                                           |
| python_startup_no_site     | 7.11 ms                                                    | 7.13 ms: 1.00x slower                                          |
| coroutines                 | 23.2 ms                                                    | 23.3 ms: 1.01x slower                                          |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                          |
| regex_effbot               | 3.67 ms                                                    | 3.70 ms: 1.01x slower                                          |
| django_template            | 34.8 ms                                                    | 35.2 ms: 1.01x slower                                          |
| typing_runtime_protocols   | 165 us                                                     | 168 us: 1.02x slower                                           |
| sqlglot_normalize          | 110 ms                                                     | 113 ms: 1.02x slower                                           |
| pycparser                  | 1.16 sec                                                   | 1.19 sec: 1.03x slower                                         |
| sqlglot_optimize           | 55.5 ms                                                    | 57.3 ms: 1.03x slower                                          |
| async_generators           | 442 ms                                                     | 457 ms: 1.03x slower                                           |
| genshi_text                | 23.7 ms                                                    | 24.7 ms: 1.04x slower                                          |
| nqueens                    | 81.4 ms                                                    | 84.9 ms: 1.04x slower                                          |
| sympy_str                  | 282 ms                                                     | 298 ms: 1.06x slower                                           |
| docutils                   | 2.83 sec                                                   | 2.99 sec: 1.06x slower                                         |
| sympy_expand               | 473 ms                                                     | 504 ms: 1.07x slower                                           |
| hexiom                     | 6.30 ms                                                    | 6.73 ms: 1.07x slower                                          |
| genshi_xml                 | 51.6 ms                                                    | 55.7 ms: 1.08x slower                                          |
| sympy_integrate            | 20.5 ms                                                    | 22.7 ms: 1.11x slower                                          |
| generators                 | 29.6 ms                                                    | 33.2 ms: 1.12x slower                                          |
| sympy_sum                  | 156 ms                                                     | 175 ms: 1.12x slower                                           |
| pylint                     | 317 ms                                                     | 366 ms: 1.15x slower                                           |
| Geometric mean             | (ref)                                                      | 1.05x faster                                                   |

Benchmark hidden because not significant (4): go, 2to3, pprint_pformat, sqlglot_transpile
Ignored benchmarks (14) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.08x