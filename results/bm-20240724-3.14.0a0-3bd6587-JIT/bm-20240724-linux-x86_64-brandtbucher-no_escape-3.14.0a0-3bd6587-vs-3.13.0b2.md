# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: no_escape
- machine: linux-x86_64
- commit hash: 3bd6587
- commit date: 2024-07-24
- overall geometric mean: 1.05x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240724-linux-x86_64-brandtbucher-no_escape-3.14.0a0-3bd6587 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 271 ms: 1.01x faster                                             |
| docutils       | 2.83 sec                                                   | 2.89 sec: 1.02x slower                                           |
| html5lib       | 67.2 ms                                                    | 63.7 ms: 1.05x faster                                            |
| tornado_http   | 94.6 ms                                                    | 93.4 ms: 1.01x faster                                            |
| Geometric mean | (ref)                                                      | 1.01x faster                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240724-linux-x86_64-brandtbucher-no_escape-3.14.0a0-3bd6587 |
|----------------------------|:----------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 327 ms: 1.16x faster                                             |
| async_tree_memoization_tg  | 444 ms                                                     | 393 ms: 1.13x faster                                             |
| async_tree_none_tg         | 336 ms                                                     | 301 ms: 1.12x faster                                             |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 529 ms: 1.11x faster                                             |
| async_tree_memoization     | 463 ms                                                     | 426 ms: 1.09x faster                                             |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 564 ms: 1.08x faster                                             |
| async_tree_io_tg           | 936 ms                                                     | 868 ms: 1.08x faster                                             |
| async_tree_io              | 939 ms                                                     | 899 ms: 1.04x faster                                             |
| Geometric mean             | (ref)                                                      | 1.10x faster                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240724-linux-x86_64-brandtbucher-no_escape-3.14.0a0-3bd6587 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 70.7 ms: 1.12x faster                                            |
| nbody          | 88.3 ms                                                    | 81.3 ms: 1.09x faster                                            |
| pidigits       | 191 ms                                                     | 186 ms: 1.03x faster                                             |
| Geometric mean | (ref)                                                      | 1.08x faster                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240724-linux-x86_64-brandtbucher-no_escape-3.14.0a0-3bd6587 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_v8       | 25.1 ms                                                    | 24.0 ms: 1.05x faster                                            |
| regex_compile  | 137 ms                                                     | 135 ms: 1.02x faster                                             |
| regex_effbot   | 3.67 ms                                                    | 3.76 ms: 1.02x slower                                            |
| regex_dna      | 221 ms                                                     | 231 ms: 1.05x slower                                             |
| Geometric mean | (ref)                                                      | 1.00x slower                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240724-linux-x86_64-brandtbucher-no_escape-3.14.0a0-3bd6587 |
|----------------------|:----------------------------------------------------------:|:----------------------------------------------------------------:|
| xml_etree_parse      | 162 ms                                                     | 146 ms: 1.11x faster                                             |
| tomli_loads          | 2.12 sec                                                   | 1.91 sec: 1.11x faster                                           |
| xml_etree_iterparse  | 107 ms                                                     | 98.4 ms: 1.09x faster                                            |
| xml_etree_generate   | 87.4 ms                                                    | 80.2 ms: 1.09x faster                                            |
| xml_etree_process    | 61.2 ms                                                    | 56.2 ms: 1.09x faster                                            |
| json_loads           | 28.9 us                                                    | 27.8 us: 1.04x faster                                            |
| json_dumps           | 10.7 ms                                                    | 10.4 ms: 1.04x faster                                            |
| unpickle_pure_python | 218 us                                                     | 215 us: 1.02x faster                                             |
| pickle_pure_python   | 305 us                                                     | 302 us: 1.01x faster                                             |
| Geometric mean       | (ref)                                                      | 1.07x faster                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240724-linux-x86_64-brandtbucher-no_escape-3.14.0a0-3bd6587 |
|------------------------|:----------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.6 ms: 1.02x faster                                            |
| python_startup_no_site | 7.11 ms                                                    | 7.16 ms: 1.01x slower                                            |
| Geometric mean         | (ref)                                                      | 1.00x faster                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240724-linux-x86_64-brandtbucher-no_escape-3.14.0a0-3bd6587 |
|-----------------|:----------------------------------------------------------:|:----------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.72 ms: 1.16x faster                                            |
| genshi_text     | 23.7 ms                                                    | 24.5 ms: 1.03x slower                                            |
| django_template | 34.8 ms                                                    | 36.3 ms: 1.04x slower                                            |
| genshi_xml      | 51.6 ms                                                    | 58.3 ms: 1.13x slower                                            |
| Geometric mean  | (ref)                                                      | 1.01x slower                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240724-linux-x86_64-brandtbucher-no_escape-3.14.0a0-3bd6587 |
|----------------------------|:----------------------------------------------------------:|:----------------------------------------------------------------:|
| deepcopy_memo              | 39.7 us                                                    | 28.1 us: 1.42x faster                                            |
| deepcopy                   | 367 us                                                     | 275 us: 1.34x faster                                             |
| scimark_fft                | 392 ms                                                     | 308 ms: 1.27x faster                                             |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.22 ms: 1.25x faster                                            |
| richards                   | 50.9 ms                                                    | 41.5 ms: 1.23x faster                                            |
| deepcopy_reduce            | 3.35 us                                                    | 2.74 us: 1.22x faster                                            |
| richards_super             | 57.4 ms                                                    | 47.6 ms: 1.20x faster                                            |
| crypto_pyaes               | 77.5 ms                                                    | 66.5 ms: 1.16x faster                                            |
| async_tree_none            | 378 ms                                                     | 327 ms: 1.16x faster                                             |
| mako                       | 11.2 ms                                                    | 9.72 ms: 1.16x faster                                            |
| scimark_monte_carlo        | 69.2 ms                                                    | 59.9 ms: 1.15x faster                                            |
| spectral_norm              | 116 ms                                                     | 101 ms: 1.14x faster                                             |
| async_tree_memoization_tg  | 444 ms                                                     | 393 ms: 1.13x faster                                             |
| async_tree_none_tg         | 336 ms                                                     | 301 ms: 1.12x faster                                             |
| bpe_tokeniser              | 5.02 sec                                                   | 4.50 sec: 1.12x faster                                           |
| float                      | 78.9 ms                                                    | 70.7 ms: 1.12x faster                                            |
| xml_etree_parse            | 162 ms                                                     | 146 ms: 1.11x faster                                             |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 529 ms: 1.11x faster                                             |
| tomli_loads                | 2.12 sec                                                   | 1.91 sec: 1.11x faster                                           |
| pyflate                    | 484 ms                                                     | 440 ms: 1.10x faster                                             |
| fannkuch                   | 402 ms                                                     | 366 ms: 1.10x faster                                             |
| mdp                        | 2.79 sec                                                   | 2.54 sec: 1.10x faster                                           |
| xml_etree_iterparse        | 107 ms                                                     | 98.4 ms: 1.09x faster                                            |
| xml_etree_generate         | 87.4 ms                                                    | 80.2 ms: 1.09x faster                                            |
| xml_etree_process          | 61.2 ms                                                    | 56.2 ms: 1.09x faster                                            |
| async_tree_memoization     | 463 ms                                                     | 426 ms: 1.09x faster                                             |
| nbody                      | 88.3 ms                                                    | 81.3 ms: 1.09x faster                                            |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 564 ms: 1.08x faster                                             |
| async_tree_io_tg           | 936 ms                                                     | 868 ms: 1.08x faster                                             |
| telco                      | 8.41 ms                                                    | 7.81 ms: 1.08x faster                                            |
| pprint_safe_repr           | 758 ms                                                     | 704 ms: 1.08x faster                                             |
| pathlib                    | 17.3 ms                                                    | 16.2 ms: 1.07x faster                                            |
| pprint_pformat             | 1.56 sec                                                   | 1.46 sec: 1.06x faster                                           |
| logging_format             | 6.47 us                                                    | 6.13 us: 1.06x faster                                            |
| chaos                      | 61.3 ms                                                    | 58.1 ms: 1.06x faster                                            |
| html5lib                   | 67.2 ms                                                    | 63.7 ms: 1.05x faster                                            |
| gc_traversal               | 3.98 ms                                                    | 3.79 ms: 1.05x faster                                            |
| regex_v8                   | 25.1 ms                                                    | 24.0 ms: 1.05x faster                                            |
| async_tree_io              | 939 ms                                                     | 899 ms: 1.04x faster                                             |
| json_loads                 | 28.9 us                                                    | 27.8 us: 1.04x faster                                            |
| meteor_contest             | 110 ms                                                     | 106 ms: 1.04x faster                                             |
| json_dumps                 | 10.7 ms                                                    | 10.4 ms: 1.04x faster                                            |
| pycparser                  | 1.16 sec                                                   | 1.12 sec: 1.03x faster                                           |
| logging_simple             | 5.74 us                                                    | 5.55 us: 1.03x faster                                            |
| json                       | 5.31 ms                                                    | 5.14 ms: 1.03x faster                                            |
| thrift                     | 823 us                                                     | 797 us: 1.03x faster                                             |
| coroutines                 | 23.2 ms                                                    | 22.5 ms: 1.03x faster                                            |
| sqlglot_parse              | 1.32 ms                                                    | 1.28 ms: 1.03x faster                                            |
| generators                 | 29.6 ms                                                    | 28.8 ms: 1.03x faster                                            |
| pidigits                   | 191 ms                                                     | 186 ms: 1.03x faster                                             |
| create_gc_cycles           | 1.82 ms                                                    | 1.77 ms: 1.03x faster                                            |
| asyncio_websockets         | 567 ms                                                     | 555 ms: 1.02x faster                                             |
| logging_silent             | 105 ns                                                     | 103 ns: 1.02x faster                                             |
| sqlglot_transpile          | 1.63 ms                                                    | 1.60 ms: 1.02x faster                                            |
| unpickle_pure_python       | 218 us                                                     | 215 us: 1.02x faster                                             |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.81 sec: 1.02x faster                                           |
| python_startup             | 10.8 ms                                                    | 10.6 ms: 1.02x faster                                            |
| dask                       | 369 ms                                                     | 364 ms: 1.02x faster                                             |
| bench_thread_pool          | 834 us                                                     | 821 us: 1.02x faster                                             |
| regex_compile              | 137 ms                                                     | 135 ms: 1.02x faster                                             |
| tornado_http               | 94.6 ms                                                    | 93.4 ms: 1.01x faster                                            |
| pickle_pure_python         | 305 us                                                     | 302 us: 1.01x faster                                             |
| coverage                   | 93.1 ms                                                    | 92.0 ms: 1.01x faster                                            |
| 2to3                       | 274 ms                                                     | 271 ms: 1.01x faster                                             |
| comprehensions             | 16.6 us                                                    | 16.5 us: 1.01x faster                                            |
| asyncio_tcp                | 508 ms                                                     | 504 ms: 1.01x faster                                             |
| scimark_sor                | 127 ms                                                     | 128 ms: 1.00x slower                                             |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                            |
| sqlglot_optimize           | 55.5 ms                                                    | 56.0 ms: 1.01x slower                                            |
| python_startup_no_site     | 7.11 ms                                                    | 7.16 ms: 1.01x slower                                            |
| raytrace                   | 267 ms                                                     | 269 ms: 1.01x slower                                             |
| docutils                   | 2.83 sec                                                   | 2.89 sec: 1.02x slower                                           |
| regex_effbot               | 3.67 ms                                                    | 3.76 ms: 1.02x slower                                            |
| scimark_lu                 | 122 ms                                                     | 125 ms: 1.02x slower                                             |
| dulwich_log                | 67.2 ms                                                    | 68.9 ms: 1.03x slower                                            |
| sqlglot_normalize          | 110 ms                                                     | 113 ms: 1.03x slower                                             |
| typing_runtime_protocols   | 165 us                                                     | 169 us: 1.03x slower                                             |
| genshi_text                | 23.7 ms                                                    | 24.5 ms: 1.03x slower                                            |
| hexiom                     | 6.30 ms                                                    | 6.51 ms: 1.03x slower                                            |
| async_generators           | 442 ms                                                     | 459 ms: 1.04x slower                                             |
| nqueens                    | 81.4 ms                                                    | 84.8 ms: 1.04x slower                                            |
| django_template            | 34.8 ms                                                    | 36.3 ms: 1.04x slower                                            |
| regex_dna                  | 221 ms                                                     | 231 ms: 1.05x slower                                             |
| sympy_str                  | 282 ms                                                     | 296 ms: 1.05x slower                                             |
| sympy_expand               | 473 ms                                                     | 501 ms: 1.06x slower                                             |
| sympy_integrate            | 20.5 ms                                                    | 22.2 ms: 1.08x slower                                            |
| deltablue                  | 3.25 ms                                                    | 3.53 ms: 1.09x slower                                            |
| sympy_sum                  | 156 ms                                                     | 169 ms: 1.09x slower                                             |
| pylint                     | 317 ms                                                     | 351 ms: 1.11x slower                                             |
| genshi_xml                 | 51.6 ms                                                    | 58.3 ms: 1.13x slower                                            |
| Geometric mean             | (ref)                                                      | 1.05x faster                                                     |

Benchmark hidden because not significant (1): go
Ignored benchmarks (12) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.07x