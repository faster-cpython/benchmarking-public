# Results vs. 3.13.0b2

- fork: python
- ref: db6f5e193315a3bbfa7b
- machine: linux-x86_64
- commit hash: db6f5e1
- commit date: 2024-08-13
- overall geometric mean: 1.41x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.24x slower
- Memory change: 1.15x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240813-linux-x86_64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 395 ms: 1.44x slower                                                  |
| docutils       | 2.83 sec                                                   | 3.34 sec: 1.18x slower                                                |
| html5lib       | 67.2 ms                                                    | 98.3 ms: 1.46x slower                                                 |
| tornado_http   | 94.6 ms                                                    | 138 ms: 1.46x slower                                                  |
| Geometric mean | (ref)                                                      | 1.38x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240813-linux-x86_64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1 |
|----------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io_tg           | 936 ms                                                     | 840 ms: 1.11x faster                                                  |
| async_tree_io              | 939 ms                                                     | 906 ms: 1.04x faster                                                  |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 602 ms: 1.02x slower                                                  |
| async_tree_memoization_tg  | 444 ms                                                     | 456 ms: 1.03x slower                                                  |
| async_tree_none_tg         | 336 ms                                                     | 350 ms: 1.04x slower                                                  |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 662 ms: 1.08x slower                                                  |
| async_tree_none            | 378 ms                                                     | 412 ms: 1.09x slower                                                  |
| async_tree_memoization     | 463 ms                                                     | 517 ms: 1.12x slower                                                  |
| Geometric mean             | (ref)                                                      | 1.03x slower                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240813-linux-x86_64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 191 ms                                                     | 184 ms: 1.04x faster                                                  |
| float          | 78.9 ms                                                    | 142 ms: 1.80x slower                                                  |
| nbody          | 88.3 ms                                                    | 222 ms: 2.52x slower                                                  |
| Geometric mean | (ref)                                                      | 1.63x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240813-linux-x86_64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                    | 3.51 ms: 1.05x faster                                                 |
| regex_dna      | 221 ms                                                     | 218 ms: 1.02x faster                                                  |
| regex_v8       | 25.1 ms                                                    | 26.0 ms: 1.04x slower                                                 |
| regex_compile  | 137 ms                                                     | 217 ms: 1.59x slower                                                  |
| Geometric mean | (ref)                                                      | 1.12x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240813-linux-x86_64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1 |
|----------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_parse      | 162 ms                                                     | 149 ms: 1.08x faster                                                  |
| xml_etree_iterparse  | 107 ms                                                     | 113 ms: 1.05x slower                                                  |
| json_loads           | 28.9 us                                                    | 32.4 us: 1.12x slower                                                 |
| json_dumps           | 10.7 ms                                                    | 13.5 ms: 1.26x slower                                                 |
| xml_etree_generate   | 87.4 ms                                                    | 110 ms: 1.26x slower                                                  |
| xml_etree_process    | 61.2 ms                                                    | 88.8 ms: 1.45x slower                                                 |
| tomli_loads          | 2.12 sec                                                   | 3.26 sec: 1.54x slower                                                |
| pickle_pure_python   | 305 us                                                     | 572 us: 1.87x slower                                                  |
| unpickle_pure_python | 218 us                                                     | 411 us: 1.88x slower                                                  |
| Geometric mean       | (ref)                                                      | 1.34x slower                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240813-linux-x86_64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1 |
|------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 13.7 ms: 1.28x slower                                                 |
| python_startup_no_site | 7.11 ms                                                    | 9.31 ms: 1.31x slower                                                 |
| Geometric mean         | (ref)                                                      | 1.29x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240813-linux-x86_64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1 |
|-----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_xml      | 51.6 ms                                                    | 82.1 ms: 1.59x slower                                                 |
| genshi_text     | 23.7 ms                                                    | 39.6 ms: 1.67x slower                                                 |
| django_template | 34.8 ms                                                    | 59.2 ms: 1.70x slower                                                 |
| mako            | 11.2 ms                                                    | 21.0 ms: 1.86x slower                                                 |
| Geometric mean  | (ref)                                                      | 1.70x slower                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240813-linux-x86_64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1 |
|----------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| gc_traversal               | 3.98 ms                                                    | 3.02 ms: 1.32x faster                                                 |
| create_gc_cycles           | 1.82 ms                                                    | 1.38 ms: 1.32x faster                                                 |
| async_tree_io_tg           | 936 ms                                                     | 840 ms: 1.11x faster                                                  |
| xml_etree_parse            | 162 ms                                                     | 149 ms: 1.08x faster                                                  |
| regex_effbot               | 3.67 ms                                                    | 3.51 ms: 1.05x faster                                                 |
| pidigits                   | 191 ms                                                     | 184 ms: 1.04x faster                                                  |
| async_tree_io              | 939 ms                                                     | 906 ms: 1.04x faster                                                  |
| asyncio_websockets         | 567 ms                                                     | 553 ms: 1.03x faster                                                  |
| regex_dna                  | 221 ms                                                     | 218 ms: 1.02x faster                                                  |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 602 ms: 1.02x slower                                                  |
| async_tree_memoization_tg  | 444 ms                                                     | 456 ms: 1.03x slower                                                  |
| regex_v8                   | 25.1 ms                                                    | 26.0 ms: 1.04x slower                                                 |
| async_tree_none_tg         | 336 ms                                                     | 350 ms: 1.04x slower                                                  |
| xml_etree_iterparse        | 107 ms                                                     | 113 ms: 1.05x slower                                                  |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 662 ms: 1.08x slower                                                  |
| async_tree_none            | 378 ms                                                     | 412 ms: 1.09x slower                                                  |
| asyncio_tcp                | 508 ms                                                     | 561 ms: 1.10x slower                                                  |
| pathlib                    | 17.3 ms                                                    | 19.2 ms: 1.11x slower                                                 |
| async_tree_memoization     | 463 ms                                                     | 517 ms: 1.12x slower                                                  |
| json_loads                 | 28.9 us                                                    | 32.4 us: 1.12x slower                                                 |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 2.07 sec: 1.12x slower                                                |
| deepcopy                   | 367 us                                                     | 417 us: 1.14x slower                                                  |
| json                       | 5.31 ms                                                    | 6.04 ms: 1.14x slower                                                 |
| mdp                        | 2.79 sec                                                   | 3.21 sec: 1.15x slower                                                |
| docutils                   | 2.83 sec                                                   | 3.34 sec: 1.18x slower                                                |
| coverage                   | 93.1 ms                                                    | 111 ms: 1.19x slower                                                  |
| scimark_fft                | 392 ms                                                     | 484 ms: 1.23x slower                                                  |
| telco                      | 8.41 ms                                                    | 10.4 ms: 1.23x slower                                                 |
| pylint                     | 317 ms                                                     | 395 ms: 1.25x slower                                                  |
| json_dumps                 | 10.7 ms                                                    | 13.5 ms: 1.26x slower                                                 |
| generators                 | 29.6 ms                                                    | 37.4 ms: 1.26x slower                                                 |
| xml_etree_generate         | 87.4 ms                                                    | 110 ms: 1.26x slower                                                  |
| async_generators           | 442 ms                                                     | 559 ms: 1.27x slower                                                  |
| python_startup             | 10.8 ms                                                    | 13.7 ms: 1.28x slower                                                 |
| deepcopy_reduce            | 3.35 us                                                    | 4.28 us: 1.28x slower                                                 |
| meteor_contest             | 110 ms                                                     | 143 ms: 1.30x slower                                                  |
| bpe_tokeniser              | 5.02 sec                                                   | 6.57 sec: 1.31x slower                                                |
| python_startup_no_site     | 7.11 ms                                                    | 9.31 ms: 1.31x slower                                                 |
| deepcopy_memo              | 39.7 us                                                    | 52.2 us: 1.31x slower                                                 |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 6.95 ms: 1.32x slower                                                 |
| coroutines                 | 23.2 ms                                                    | 32.1 ms: 1.39x slower                                                 |
| pycparser                  | 1.16 sec                                                   | 1.63 sec: 1.40x slower                                                |
| sympy_integrate            | 20.5 ms                                                    | 28.8 ms: 1.40x slower                                                 |
| 2to3                       | 274 ms                                                     | 395 ms: 1.44x slower                                                  |
| xml_etree_process          | 61.2 ms                                                    | 88.8 ms: 1.45x slower                                                 |
| nqueens                    | 81.4 ms                                                    | 119 ms: 1.46x slower                                                  |
| tornado_http               | 94.6 ms                                                    | 138 ms: 1.46x slower                                                  |
| crypto_pyaes               | 77.5 ms                                                    | 113 ms: 1.46x slower                                                  |
| html5lib                   | 67.2 ms                                                    | 98.3 ms: 1.46x slower                                                 |
| thrift                     | 823 us                                                     | 1.22 ms: 1.49x slower                                                 |
| sympy_str                  | 282 ms                                                     | 425 ms: 1.50x slower                                                  |
| typing_runtime_protocols   | 165 us                                                     | 249 us: 1.51x slower                                                  |
| tomli_loads                | 2.12 sec                                                   | 3.26 sec: 1.54x slower                                                |
| richards                   | 50.9 ms                                                    | 78.3 ms: 1.54x slower                                                 |
| sqlglot_optimize           | 55.5 ms                                                    | 85.9 ms: 1.55x slower                                                 |
| sqlglot_normalize          | 110 ms                                                     | 171 ms: 1.55x slower                                                  |
| fannkuch                   | 402 ms                                                     | 625 ms: 1.55x slower                                                  |
| sympy_expand               | 473 ms                                                     | 748 ms: 1.58x slower                                                  |
| regex_compile              | 137 ms                                                     | 217 ms: 1.59x slower                                                  |
| genshi_xml                 | 51.6 ms                                                    | 82.1 ms: 1.59x slower                                                 |
| pyflate                    | 484 ms                                                     | 773 ms: 1.60x slower                                                  |
| spectral_norm              | 116 ms                                                     | 189 ms: 1.63x slower                                                  |
| sympy_sum                  | 156 ms                                                     | 256 ms: 1.64x slower                                                  |
| richards_super             | 57.4 ms                                                    | 95.4 ms: 1.66x slower                                                 |
| genshi_text                | 23.7 ms                                                    | 39.6 ms: 1.67x slower                                                 |
| pprint_safe_repr           | 758 ms                                                     | 1.27 sec: 1.68x slower                                                |
| pprint_pformat             | 1.56 sec                                                   | 2.64 sec: 1.70x slower                                                |
| django_template            | 34.8 ms                                                    | 59.2 ms: 1.70x slower                                                 |
| comprehensions             | 16.6 us                                                    | 28.8 us: 1.73x slower                                                 |
| logging_format             | 6.47 us                                                    | 11.6 us: 1.79x slower                                                 |
| logging_simple             | 5.74 us                                                    | 10.3 us: 1.79x slower                                                 |
| float                      | 78.9 ms                                                    | 142 ms: 1.80x slower                                                  |
| scimark_monte_carlo        | 69.2 ms                                                    | 124 ms: 1.80x slower                                                  |
| logging_silent             | 105 ns                                                     | 191 ns: 1.82x slower                                                  |
| mako                       | 11.2 ms                                                    | 21.0 ms: 1.86x slower                                                 |
| pickle_pure_python         | 305 us                                                     | 572 us: 1.87x slower                                                  |
| unpickle_pure_python       | 218 us                                                     | 411 us: 1.88x slower                                                  |
| sqlglot_transpile          | 1.63 ms                                                    | 3.08 ms: 1.89x slower                                                 |
| hexiom                     | 6.30 ms                                                    | 12.0 ms: 1.91x slower                                                 |
| scimark_lu                 | 122 ms                                                     | 240 ms: 1.98x slower                                                  |
| sqlglot_parse              | 1.32 ms                                                    | 2.63 ms: 1.99x slower                                                 |
| chaos                      | 61.3 ms                                                    | 125 ms: 2.04x slower                                                  |
| scimark_sor                | 127 ms                                                     | 266 ms: 2.09x slower                                                  |
| go                         | 145 ms                                                     | 306 ms: 2.12x slower                                                  |
| raytrace                   | 267 ms                                                     | 598 ms: 2.24x slower                                                  |
| nbody                      | 88.3 ms                                                    | 222 ms: 2.52x slower                                                  |
| deltablue                  | 3.25 ms                                                    | 8.34 ms: 2.56x slower                                                 |
| bench_thread_pool          | 834 us                                                     | 3.11 ms: 3.73x slower                                                 |
| Geometric mean             | (ref)                                                      | 1.41x slower                                                          |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (14) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.29x
- 95% likely to have a slowdown of 1.27x
- 99% likely to have a slowdown of 1.24x

# Memory
- memory change: 1.15x