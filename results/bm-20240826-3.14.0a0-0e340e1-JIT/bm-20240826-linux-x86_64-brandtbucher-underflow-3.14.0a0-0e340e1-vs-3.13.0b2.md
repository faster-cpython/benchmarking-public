# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: underflow
- machine: linux-x86_64
- commit hash: 0e340e1
- commit date: 2024-08-26
- overall geometric mean: 1.03x faster
- HPT reliability: 98.87%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240826-linux-x86_64-brandtbucher-underflow-3.14.0a0-0e340e1 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 283 ms: 1.03x slower                                             |
| docutils       | 2.83 sec                                                   | 3.34 sec: 1.18x slower                                           |
| html5lib       | 67.2 ms                                                    | 70.6 ms: 1.05x slower                                            |
| tornado_http   | 94.6 ms                                                    | 102 ms: 1.08x slower                                             |
| Geometric mean | (ref)                                                      | 1.09x slower                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240826-linux-x86_64-brandtbucher-underflow-3.14.0a0-0e340e1 |
|----------------------------|:----------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 326 ms: 1.16x faster                                             |
| async_tree_memoization     | 463 ms                                                     | 414 ms: 1.12x faster                                             |
| async_tree_memoization_tg  | 444 ms                                                     | 405 ms: 1.10x faster                                             |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 560 ms: 1.09x faster                                             |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 540 ms: 1.09x faster                                             |
| async_tree_none_tg         | 336 ms                                                     | 310 ms: 1.08x faster                                             |
| async_tree_io_tg           | 936 ms                                                     | 899 ms: 1.04x faster                                             |
| Geometric mean             | (ref)                                                      | 1.08x faster                                                     |

Benchmark hidden because not significant (1): async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240826-linux-x86_64-brandtbucher-underflow-3.14.0a0-0e340e1 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 71.0 ms: 1.11x faster                                            |
| nbody          | 88.3 ms                                                    | 79.6 ms: 1.11x faster                                            |
| pidigits       | 191 ms                                                     | 185 ms: 1.03x faster                                             |
| Geometric mean | (ref)                                                      | 1.08x faster                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240826-linux-x86_64-brandtbucher-underflow-3.14.0a0-0e340e1 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_v8       | 25.1 ms                                                    | 24.2 ms: 1.04x faster                                            |
| regex_dna      | 221 ms                                                     | 216 ms: 1.02x faster                                             |
| regex_effbot   | 3.67 ms                                                    | 3.60 ms: 1.02x faster                                            |
| regex_compile  | 137 ms                                                     | 150 ms: 1.10x slower                                             |
| Geometric mean | (ref)                                                      | 1.00x slower                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240826-linux-x86_64-brandtbucher-underflow-3.14.0a0-0e340e1 |
|----------------------|:----------------------------------------------------------:|:----------------------------------------------------------------:|
| xml_etree_generate   | 87.4 ms                                                    | 77.0 ms: 1.14x faster                                            |
| xml_etree_process    | 61.2 ms                                                    | 54.5 ms: 1.12x faster                                            |
| xml_etree_parse      | 162 ms                                                     | 146 ms: 1.11x faster                                             |
| unpickle_pure_python | 218 us                                                     | 198 us: 1.10x faster                                             |
| xml_etree_iterparse  | 107 ms                                                     | 98.8 ms: 1.09x faster                                            |
| json_dumps           | 10.7 ms                                                    | 9.99 ms: 1.07x faster                                            |
| tomli_loads          | 2.12 sec                                                   | 2.05 sec: 1.03x faster                                           |
| pickle_pure_python   | 305 us                                                     | 310 us: 1.02x slower                                             |
| json_loads           | 28.9 us                                                    | 29.6 us: 1.03x slower                                            |
| Geometric mean       | (ref)                                                      | 1.07x faster                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240826-linux-x86_64-brandtbucher-underflow-3.14.0a0-0e340e1 |
|------------------------|:----------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                            |
| python_startup_no_site | 7.11 ms                                                    | 7.16 ms: 1.01x slower                                            |
| Geometric mean         | (ref)                                                      | 1.01x faster                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240826-linux-x86_64-brandtbucher-underflow-3.14.0a0-0e340e1 |
|-----------------|:----------------------------------------------------------:|:----------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.61 ms: 1.17x faster                                            |
| genshi_text     | 23.7 ms                                                    | 24.3 ms: 1.03x slower                                            |
| django_template | 34.8 ms                                                    | 38.3 ms: 1.10x slower                                            |
| genshi_xml      | 51.6 ms                                                    | 65.0 ms: 1.26x slower                                            |
| Geometric mean  | (ref)                                                      | 1.05x slower                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240826-linux-x86_64-brandtbucher-underflow-3.14.0a0-0e340e1 |
|----------------------------|:----------------------------------------------------------:|:----------------------------------------------------------------:|
| deepcopy_memo              | 39.7 us                                                    | 26.6 us: 1.49x faster                                            |
| deepcopy                   | 367 us                                                     | 263 us: 1.39x faster                                             |
| richards                   | 50.9 ms                                                    | 38.1 ms: 1.34x faster                                            |
| richards_super             | 57.4 ms                                                    | 43.1 ms: 1.33x faster                                            |
| scimark_fft                | 392 ms                                                     | 310 ms: 1.27x faster                                             |
| deepcopy_reduce            | 3.35 us                                                    | 2.69 us: 1.24x faster                                            |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.44 ms: 1.19x faster                                            |
| crypto_pyaes               | 77.5 ms                                                    | 65.9 ms: 1.18x faster                                            |
| scimark_monte_carlo        | 69.2 ms                                                    | 59.1 ms: 1.17x faster                                            |
| mako                       | 11.2 ms                                                    | 9.61 ms: 1.17x faster                                            |
| async_tree_none            | 378 ms                                                     | 326 ms: 1.16x faster                                             |
| spectral_norm              | 116 ms                                                     | 101 ms: 1.15x faster                                             |
| xml_etree_generate         | 87.4 ms                                                    | 77.0 ms: 1.14x faster                                            |
| bpe_tokeniser              | 5.02 sec                                                   | 4.44 sec: 1.13x faster                                           |
| xml_etree_process          | 61.2 ms                                                    | 54.5 ms: 1.12x faster                                            |
| async_tree_memoization     | 463 ms                                                     | 414 ms: 1.12x faster                                             |
| float                      | 78.9 ms                                                    | 71.0 ms: 1.11x faster                                            |
| nbody                      | 88.3 ms                                                    | 79.6 ms: 1.11x faster                                            |
| xml_etree_parse            | 162 ms                                                     | 146 ms: 1.11x faster                                             |
| unpickle_pure_python       | 218 us                                                     | 198 us: 1.10x faster                                             |
| pyflate                    | 484 ms                                                     | 440 ms: 1.10x faster                                             |
| telco                      | 8.41 ms                                                    | 7.66 ms: 1.10x faster                                            |
| pathlib                    | 17.3 ms                                                    | 15.8 ms: 1.10x faster                                            |
| async_tree_memoization_tg  | 444 ms                                                     | 405 ms: 1.10x faster                                             |
| fannkuch                   | 402 ms                                                     | 367 ms: 1.09x faster                                             |
| mdp                        | 2.79 sec                                                   | 2.55 sec: 1.09x faster                                           |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 560 ms: 1.09x faster                                             |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 540 ms: 1.09x faster                                             |
| xml_etree_iterparse        | 107 ms                                                     | 98.8 ms: 1.09x faster                                            |
| async_tree_none_tg         | 336 ms                                                     | 310 ms: 1.08x faster                                             |
| json_dumps                 | 10.7 ms                                                    | 9.99 ms: 1.07x faster                                            |
| coverage                   | 93.1 ms                                                    | 86.9 ms: 1.07x faster                                            |
| scimark_lu                 | 122 ms                                                     | 114 ms: 1.06x faster                                             |
| chaos                      | 61.3 ms                                                    | 58.2 ms: 1.05x faster                                            |
| gc_traversal               | 3.98 ms                                                    | 3.78 ms: 1.05x faster                                            |
| pprint_safe_repr           | 758 ms                                                     | 723 ms: 1.05x faster                                             |
| pprint_pformat             | 1.56 sec                                                   | 1.49 sec: 1.04x faster                                           |
| meteor_contest             | 110 ms                                                     | 105 ms: 1.04x faster                                             |
| thrift                     | 823 us                                                     | 789 us: 1.04x faster                                             |
| async_tree_io_tg           | 936 ms                                                     | 899 ms: 1.04x faster                                             |
| regex_v8                   | 25.1 ms                                                    | 24.2 ms: 1.04x faster                                            |
| tomli_loads                | 2.12 sec                                                   | 2.05 sec: 1.03x faster                                           |
| pidigits                   | 191 ms                                                     | 185 ms: 1.03x faster                                             |
| logging_silent             | 105 ns                                                     | 101 ns: 1.03x faster                                             |
| scimark_sor                | 127 ms                                                     | 124 ms: 1.03x faster                                             |
| regex_dna                  | 221 ms                                                     | 216 ms: 1.02x faster                                             |
| coroutines                 | 23.2 ms                                                    | 22.7 ms: 1.02x faster                                            |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.80 sec: 1.02x faster                                           |
| regex_effbot               | 3.67 ms                                                    | 3.60 ms: 1.02x faster                                            |
| asyncio_websockets         | 567 ms                                                     | 556 ms: 1.02x faster                                             |
| python_startup             | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                            |
| create_gc_cycles           | 1.82 ms                                                    | 1.78 ms: 1.02x faster                                            |
| bench_thread_pool          | 834 us                                                     | 825 us: 1.01x faster                                             |
| json                       | 5.31 ms                                                    | 5.26 ms: 1.01x faster                                            |
| comprehensions             | 16.6 us                                                    | 16.7 us: 1.00x slower                                            |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                            |
| deltablue                  | 3.25 ms                                                    | 3.27 ms: 1.01x slower                                            |
| python_startup_no_site     | 7.11 ms                                                    | 7.16 ms: 1.01x slower                                            |
| asyncio_tcp                | 508 ms                                                     | 514 ms: 1.01x slower                                             |
| logging_simple             | 5.74 us                                                    | 5.84 us: 1.02x slower                                            |
| pickle_pure_python         | 305 us                                                     | 310 us: 1.02x slower                                             |
| genshi_text                | 23.7 ms                                                    | 24.3 ms: 1.03x slower                                            |
| json_loads                 | 28.9 us                                                    | 29.6 us: 1.03x slower                                            |
| nqueens                    | 81.4 ms                                                    | 83.7 ms: 1.03x slower                                            |
| async_generators           | 442 ms                                                     | 456 ms: 1.03x slower                                             |
| 2to3                       | 274 ms                                                     | 283 ms: 1.03x slower                                             |
| raytrace                   | 267 ms                                                     | 276 ms: 1.04x slower                                             |
| html5lib                   | 67.2 ms                                                    | 70.6 ms: 1.05x slower                                            |
| pycparser                  | 1.16 sec                                                   | 1.23 sec: 1.06x slower                                           |
| tornado_http               | 94.6 ms                                                    | 102 ms: 1.08x slower                                             |
| hexiom                     | 6.30 ms                                                    | 6.82 ms: 1.08x slower                                            |
| sqlglot_optimize           | 55.5 ms                                                    | 60.4 ms: 1.09x slower                                            |
| sqlglot_normalize          | 110 ms                                                     | 121 ms: 1.10x slower                                             |
| regex_compile              | 137 ms                                                     | 150 ms: 1.10x slower                                             |
| sqlglot_transpile          | 1.63 ms                                                    | 1.80 ms: 1.10x slower                                            |
| django_template            | 34.8 ms                                                    | 38.3 ms: 1.10x slower                                            |
| sympy_expand               | 473 ms                                                     | 536 ms: 1.13x slower                                             |
| generators                 | 29.6 ms                                                    | 33.7 ms: 1.14x slower                                            |
| sympy_str                  | 282 ms                                                     | 321 ms: 1.14x slower                                             |
| sqlglot_parse              | 1.32 ms                                                    | 1.51 ms: 1.15x slower                                            |
| go                         | 145 ms                                                     | 170 ms: 1.18x slower                                             |
| docutils                   | 2.83 sec                                                   | 3.34 sec: 1.18x slower                                           |
| sympy_integrate            | 20.5 ms                                                    | 25.0 ms: 1.22x slower                                            |
| sympy_sum                  | 156 ms                                                     | 192 ms: 1.23x slower                                             |
| genshi_xml                 | 51.6 ms                                                    | 65.0 ms: 1.26x slower                                            |
| pylint                     | 317 ms                                                     | 415 ms: 1.31x slower                                             |
| Geometric mean             | (ref)                                                      | 1.03x faster                                                     |

Benchmark hidden because not significant (3): typing_runtime_protocols, async_tree_io, logging_format
Ignored benchmarks (14) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 98.87% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.10x