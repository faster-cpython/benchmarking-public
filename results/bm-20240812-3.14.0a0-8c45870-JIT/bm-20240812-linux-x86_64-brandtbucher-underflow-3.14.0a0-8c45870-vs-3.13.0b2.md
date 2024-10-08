# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: underflow
- machine: linux-x86_64
- commit hash: 8c45870
- commit date: 2024-08-12
- overall geometric mean: 1.04x faster
- HPT reliability: 99.50%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240812-linux-x86_64-brandtbucher-underflow-3.14.0a0-8c45870 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 280 ms: 1.02x slower                                             |
| docutils       | 2.83 sec                                                   | 3.29 sec: 1.16x slower                                           |
| html5lib       | 67.2 ms                                                    | 68.6 ms: 1.02x slower                                            |
| tornado_http   | 94.6 ms                                                    | 96.9 ms: 1.02x slower                                            |
| Geometric mean | (ref)                                                      | 1.06x slower                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240812-linux-x86_64-brandtbucher-underflow-3.14.0a0-8c45870 |
|----------------------------|:----------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 324 ms: 1.17x faster                                             |
| async_tree_memoization_tg  | 444 ms                                                     | 395 ms: 1.12x faster                                             |
| async_tree_none_tg         | 336 ms                                                     | 302 ms: 1.11x faster                                             |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 532 ms: 1.10x faster                                             |
| async_tree_memoization     | 463 ms                                                     | 425 ms: 1.09x faster                                             |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 566 ms: 1.08x faster                                             |
| async_tree_io_tg           | 936 ms                                                     | 878 ms: 1.07x faster                                             |
| async_tree_io              | 939 ms                                                     | 902 ms: 1.04x faster                                             |
| Geometric mean             | (ref)                                                      | 1.10x faster                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240812-linux-x86_64-brandtbucher-underflow-3.14.0a0-8c45870 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 70.7 ms: 1.12x faster                                            |
| nbody          | 88.3 ms                                                    | 82.3 ms: 1.07x faster                                            |
| pidigits       | 191 ms                                                     | 188 ms: 1.02x faster                                             |
| Geometric mean | (ref)                                                      | 1.07x faster                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240812-linux-x86_64-brandtbucher-underflow-3.14.0a0-8c45870 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_dna      | 221 ms                                                     | 210 ms: 1.05x faster                                             |
| regex_v8       | 25.1 ms                                                    | 24.6 ms: 1.02x faster                                            |
| regex_effbot   | 3.67 ms                                                    | 3.68 ms: 1.00x slower                                            |
| regex_compile  | 137 ms                                                     | 146 ms: 1.07x slower                                             |
| Geometric mean | (ref)                                                      | 1.00x faster                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240812-linux-x86_64-brandtbucher-underflow-3.14.0a0-8c45870 |
|----------------------|:----------------------------------------------------------:|:----------------------------------------------------------------:|
| unpickle_pure_python | 218 us                                                     | 194 us: 1.13x faster                                             |
| xml_etree_parse      | 162 ms                                                     | 148 ms: 1.10x faster                                             |
| xml_etree_iterparse  | 107 ms                                                     | 98.7 ms: 1.09x faster                                            |
| xml_etree_process    | 61.2 ms                                                    | 56.3 ms: 1.09x faster                                            |
| xml_etree_generate   | 87.4 ms                                                    | 80.7 ms: 1.08x faster                                            |
| json_loads           | 28.9 us                                                    | 28.0 us: 1.03x faster                                            |
| json_dumps           | 10.7 ms                                                    | 10.4 ms: 1.03x faster                                            |
| tomli_loads          | 2.12 sec                                                   | 2.09 sec: 1.02x faster                                           |
| pickle_pure_python   | 305 us                                                     | 304 us: 1.01x faster                                             |
| Geometric mean       | (ref)                                                      | 1.06x faster                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240812-linux-x86_64-brandtbucher-underflow-3.14.0a0-8c45870 |
|------------------------|:----------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.6 ms: 1.02x faster                                            |
| python_startup_no_site | 7.11 ms                                                    | 7.17 ms: 1.01x slower                                            |
| Geometric mean         | (ref)                                                      | 1.00x faster                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240812-linux-x86_64-brandtbucher-underflow-3.14.0a0-8c45870 |
|-----------------|:----------------------------------------------------------:|:----------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.74 ms: 1.15x faster                                            |
| django_template | 34.8 ms                                                    | 36.8 ms: 1.06x slower                                            |
| genshi_xml      | 51.6 ms                                                    | 63.5 ms: 1.23x slower                                            |
| Geometric mean  | (ref)                                                      | 1.03x slower                                                     |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240812-linux-x86_64-brandtbucher-underflow-3.14.0a0-8c45870 |
|----------------------------|:----------------------------------------------------------:|:----------------------------------------------------------------:|
| deepcopy_memo              | 39.7 us                                                    | 26.3 us: 1.51x faster                                            |
| deepcopy                   | 367 us                                                     | 260 us: 1.41x faster                                             |
| richards                   | 50.9 ms                                                    | 38.4 ms: 1.33x faster                                            |
| richards_super             | 57.4 ms                                                    | 43.4 ms: 1.32x faster                                            |
| scimark_fft                | 392 ms                                                     | 307 ms: 1.28x faster                                             |
| deepcopy_reduce            | 3.35 us                                                    | 2.69 us: 1.25x faster                                            |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.32 ms: 1.22x faster                                            |
| scimark_monte_carlo        | 69.2 ms                                                    | 58.2 ms: 1.19x faster                                            |
| crypto_pyaes               | 77.5 ms                                                    | 66.1 ms: 1.17x faster                                            |
| async_tree_none            | 378 ms                                                     | 324 ms: 1.17x faster                                             |
| mako                       | 11.2 ms                                                    | 9.74 ms: 1.15x faster                                            |
| spectral_norm              | 116 ms                                                     | 103 ms: 1.13x faster                                             |
| unpickle_pure_python       | 218 us                                                     | 194 us: 1.13x faster                                             |
| async_tree_memoization_tg  | 444 ms                                                     | 395 ms: 1.12x faster                                             |
| float                      | 78.9 ms                                                    | 70.7 ms: 1.12x faster                                            |
| async_tree_none_tg         | 336 ms                                                     | 302 ms: 1.11x faster                                             |
| scimark_lu                 | 122 ms                                                     | 110 ms: 1.11x faster                                             |
| bpe_tokeniser              | 5.02 sec                                                   | 4.55 sec: 1.10x faster                                           |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 532 ms: 1.10x faster                                             |
| fannkuch                   | 402 ms                                                     | 367 ms: 1.10x faster                                             |
| telco                      | 8.41 ms                                                    | 7.68 ms: 1.10x faster                                            |
| xml_etree_parse            | 162 ms                                                     | 148 ms: 1.10x faster                                             |
| pyflate                    | 484 ms                                                     | 442 ms: 1.09x faster                                             |
| async_tree_memoization     | 463 ms                                                     | 425 ms: 1.09x faster                                             |
| xml_etree_iterparse        | 107 ms                                                     | 98.7 ms: 1.09x faster                                            |
| xml_etree_process          | 61.2 ms                                                    | 56.3 ms: 1.09x faster                                            |
| xml_etree_generate         | 87.4 ms                                                    | 80.7 ms: 1.08x faster                                            |
| logging_silent             | 105 ns                                                     | 97.0 ns: 1.08x faster                                            |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 566 ms: 1.08x faster                                             |
| pathlib                    | 17.3 ms                                                    | 16.1 ms: 1.08x faster                                            |
| nbody                      | 88.3 ms                                                    | 82.3 ms: 1.07x faster                                            |
| async_tree_io_tg           | 936 ms                                                     | 878 ms: 1.07x faster                                             |
| gc_traversal               | 3.98 ms                                                    | 3.76 ms: 1.06x faster                                            |
| scimark_sor                | 127 ms                                                     | 121 ms: 1.06x faster                                             |
| regex_dna                  | 221 ms                                                     | 210 ms: 1.05x faster                                             |
| async_tree_io              | 939 ms                                                     | 902 ms: 1.04x faster                                             |
| chaos                      | 61.3 ms                                                    | 58.9 ms: 1.04x faster                                            |
| json                       | 5.31 ms                                                    | 5.10 ms: 1.04x faster                                            |
| meteor_contest             | 110 ms                                                     | 106 ms: 1.03x faster                                             |
| thrift                     | 823 us                                                     | 797 us: 1.03x faster                                             |
| json_loads                 | 28.9 us                                                    | 28.0 us: 1.03x faster                                            |
| json_dumps                 | 10.7 ms                                                    | 10.4 ms: 1.03x faster                                            |
| deltablue                  | 3.25 ms                                                    | 3.17 ms: 1.03x faster                                            |
| logging_format             | 6.47 us                                                    | 6.31 us: 1.02x faster                                            |
| coverage                   | 93.1 ms                                                    | 90.9 ms: 1.02x faster                                            |
| create_gc_cycles           | 1.82 ms                                                    | 1.78 ms: 1.02x faster                                            |
| regex_v8                   | 25.1 ms                                                    | 24.6 ms: 1.02x faster                                            |
| asyncio_websockets         | 567 ms                                                     | 555 ms: 1.02x faster                                             |
| mdp                        | 2.79 sec                                                   | 2.74 sec: 1.02x faster                                           |
| pidigits                   | 191 ms                                                     | 188 ms: 1.02x faster                                             |
| tomli_loads                | 2.12 sec                                                   | 2.09 sec: 1.02x faster                                           |
| python_startup             | 10.8 ms                                                    | 10.6 ms: 1.02x faster                                            |
| pprint_safe_repr           | 758 ms                                                     | 746 ms: 1.02x faster                                             |
| bench_thread_pool          | 834 us                                                     | 821 us: 1.02x faster                                             |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.82 sec: 1.01x faster                                           |
| logging_simple             | 5.74 us                                                    | 5.68 us: 1.01x faster                                            |
| raytrace                   | 267 ms                                                     | 265 ms: 1.01x faster                                             |
| comprehensions             | 16.6 us                                                    | 16.5 us: 1.01x faster                                            |
| pickle_pure_python         | 305 us                                                     | 304 us: 1.01x faster                                             |
| coroutines                 | 23.2 ms                                                    | 23.1 ms: 1.00x faster                                            |
| regex_effbot               | 3.67 ms                                                    | 3.68 ms: 1.00x slower                                            |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.00x slower                                            |
| go                         | 145 ms                                                     | 146 ms: 1.01x slower                                             |
| asyncio_tcp                | 508 ms                                                     | 512 ms: 1.01x slower                                             |
| python_startup_no_site     | 7.11 ms                                                    | 7.17 ms: 1.01x slower                                            |
| html5lib                   | 67.2 ms                                                    | 68.6 ms: 1.02x slower                                            |
| nqueens                    | 81.4 ms                                                    | 83.1 ms: 1.02x slower                                            |
| 2to3                       | 274 ms                                                     | 280 ms: 1.02x slower                                             |
| async_generators           | 442 ms                                                     | 452 ms: 1.02x slower                                             |
| tornado_http               | 94.6 ms                                                    | 96.9 ms: 1.02x slower                                            |
| typing_runtime_protocols   | 165 us                                                     | 171 us: 1.04x slower                                             |
| sqlglot_transpile          | 1.63 ms                                                    | 1.72 ms: 1.05x slower                                            |
| django_template            | 34.8 ms                                                    | 36.8 ms: 1.06x slower                                            |
| sqlglot_normalize          | 110 ms                                                     | 117 ms: 1.06x slower                                             |
| regex_compile              | 137 ms                                                     | 146 ms: 1.07x slower                                             |
| pycparser                  | 1.16 sec                                                   | 1.24 sec: 1.07x slower                                           |
| sqlglot_optimize           | 55.5 ms                                                    | 59.9 ms: 1.08x slower                                            |
| hexiom                     | 6.30 ms                                                    | 6.80 ms: 1.08x slower                                            |
| sqlglot_parse              | 1.32 ms                                                    | 1.44 ms: 1.09x slower                                            |
| sympy_expand               | 473 ms                                                     | 531 ms: 1.12x slower                                             |
| sympy_str                  | 282 ms                                                     | 318 ms: 1.13x slower                                             |
| generators                 | 29.6 ms                                                    | 33.5 ms: 1.13x slower                                            |
| docutils                   | 2.83 sec                                                   | 3.29 sec: 1.16x slower                                           |
| sympy_integrate            | 20.5 ms                                                    | 24.4 ms: 1.19x slower                                            |
| sympy_sum                  | 156 ms                                                     | 187 ms: 1.20x slower                                             |
| genshi_xml                 | 51.6 ms                                                    | 63.5 ms: 1.23x slower                                            |
| pylint                     | 317 ms                                                     | 408 ms: 1.29x slower                                             |
| Geometric mean             | (ref)                                                      | 1.04x faster                                                     |

Benchmark hidden because not significant (2): pprint_pformat, genshi_text
Ignored benchmarks (14) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 99.50% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.08x