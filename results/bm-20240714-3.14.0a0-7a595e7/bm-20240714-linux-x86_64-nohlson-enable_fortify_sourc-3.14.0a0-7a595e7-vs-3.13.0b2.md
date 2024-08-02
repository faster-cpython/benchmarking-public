# Results vs. 3.13.0b2

- fork: nohlson
- ref: enable_fortify_sourc
- machine: linux-x86_64
- commit hash: 7a595e7
- commit date: 2024-07-14
- overall geometric mean: 1.05x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240714-linux-x86_64-nohlson-enable_fortify_sourc-3.14.0a0-7a595e7 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 263 ms: 1.04x faster                                                   |
| docutils       | 2.83 sec                                                   | 2.69 sec: 1.05x faster                                                 |
| html5lib       | 67.2 ms                                                    | 64.9 ms: 1.04x faster                                                  |
| tornado_http   | 94.6 ms                                                    | 89.8 ms: 1.05x faster                                                  |
| Geometric mean | (ref)                                                      | 1.05x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240714-linux-x86_64-nohlson-enable_fortify_sourc-3.14.0a0-7a595e7 |
|----------------------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 444 ms                                                     | 377 ms: 1.18x faster                                                   |
| async_tree_none            | 378 ms                                                     | 326 ms: 1.16x faster                                                   |
| async_tree_none_tg         | 336 ms                                                     | 294 ms: 1.15x faster                                                   |
| async_tree_memoization     | 463 ms                                                     | 408 ms: 1.14x faster                                                   |
| async_tree_io              | 939 ms                                                     | 849 ms: 1.11x faster                                                   |
| async_tree_io_tg           | 936 ms                                                     | 848 ms: 1.10x faster                                                   |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 541 ms: 1.09x faster                                                   |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 566 ms: 1.08x faster                                                   |
| Geometric mean             | (ref)                                                      | 1.12x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240714-linux-x86_64-nohlson-enable_fortify_sourc-3.14.0a0-7a595e7 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| pidigits       | 191 ms                                                     | 188 ms: 1.02x faster                                                   |
| float          | 78.9 ms                                                    | 78.1 ms: 1.01x faster                                                  |
| nbody          | 88.3 ms                                                    | 91.4 ms: 1.03x slower                                                  |
| Geometric mean | (ref)                                                      | 1.00x slower                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240714-linux-x86_64-nohlson-enable_fortify_sourc-3.14.0a0-7a595e7 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_v8       | 25.1 ms                                                    | 23.9 ms: 1.05x faster                                                  |
| regex_compile  | 137 ms                                                     | 131 ms: 1.04x faster                                                   |
| regex_dna      | 221 ms                                                     | 217 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                      | 1.03x faster                                                           |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240714-linux-x86_64-nohlson-enable_fortify_sourc-3.14.0a0-7a595e7 |
|----------------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| json_loads           | 28.9 us                                                    | 27.4 us: 1.05x faster                                                  |
| unpickle_pure_python | 218 us                                                     | 211 us: 1.03x faster                                                   |
| xml_etree_parse      | 162 ms                                                     | 158 ms: 1.03x faster                                                   |
| xml_etree_process    | 61.2 ms                                                    | 59.6 ms: 1.03x faster                                                  |
| xml_etree_iterparse  | 107 ms                                                     | 105 ms: 1.03x faster                                                   |
| xml_etree_generate   | 87.4 ms                                                    | 85.9 ms: 1.02x faster                                                  |
| json_dumps           | 10.7 ms                                                    | 10.5 ms: 1.02x faster                                                  |
| pickle_pure_python   | 305 us                                                     | 303 us: 1.01x faster                                                   |
| Geometric mean       | (ref)                                                      | 1.02x faster                                                           |

Benchmark hidden because not significant (1): tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240714-linux-x86_64-nohlson-enable_fortify_sourc-3.14.0a0-7a595e7 |
|------------------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                                  |
| python_startup_no_site | 7.11 ms                                                    | 7.09 ms: 1.00x faster                                                  |
| Geometric mean         | (ref)                                                      | 1.01x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240714-linux-x86_64-nohlson-enable_fortify_sourc-3.14.0a0-7a595e7 |
|-----------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_xml      | 51.6 ms                                                    | 50.2 ms: 1.03x faster                                                  |
| genshi_text     | 23.7 ms                                                    | 23.1 ms: 1.03x faster                                                  |
| django_template | 34.8 ms                                                    | 34.3 ms: 1.02x faster                                                  |
| mako            | 11.2 ms                                                    | 11.5 ms: 1.03x slower                                                  |
| Geometric mean  | (ref)                                                      | 1.01x faster                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240714-linux-x86_64-nohlson-enable_fortify_sourc-3.14.0a0-7a595e7 |
|----------------------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| deepcopy                   | 367 us                                                     | 262 us: 1.40x faster                                                   |
| deepcopy_memo              | 39.7 us                                                    | 30.0 us: 1.32x faster                                                  |
| deepcopy_reduce            | 3.35 us                                                    | 2.65 us: 1.26x faster                                                  |
| async_tree_memoization_tg  | 444 ms                                                     | 377 ms: 1.18x faster                                                   |
| async_tree_none            | 378 ms                                                     | 326 ms: 1.16x faster                                                   |
| async_tree_none_tg         | 336 ms                                                     | 294 ms: 1.15x faster                                                   |
| async_tree_memoization     | 463 ms                                                     | 408 ms: 1.14x faster                                                   |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.72 ms: 1.12x faster                                                  |
| pathlib                    | 17.3 ms                                                    | 15.6 ms: 1.11x faster                                                  |
| async_tree_io              | 939 ms                                                     | 849 ms: 1.11x faster                                                   |
| async_tree_io_tg           | 936 ms                                                     | 848 ms: 1.10x faster                                                   |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 541 ms: 1.09x faster                                                   |
| mdp                        | 2.79 sec                                                   | 2.57 sec: 1.08x faster                                                 |
| richards_super             | 57.4 ms                                                    | 53.1 ms: 1.08x faster                                                  |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 566 ms: 1.08x faster                                                   |
| richards                   | 50.9 ms                                                    | 47.2 ms: 1.08x faster                                                  |
| scimark_lu                 | 122 ms                                                     | 113 ms: 1.08x faster                                                   |
| gc_traversal               | 3.98 ms                                                    | 3.69 ms: 1.08x faster                                                  |
| crypto_pyaes               | 77.5 ms                                                    | 72.9 ms: 1.06x faster                                                  |
| logging_format             | 6.47 us                                                    | 6.09 us: 1.06x faster                                                  |
| scimark_fft                | 392 ms                                                     | 370 ms: 1.06x faster                                                   |
| dulwich_log                | 67.2 ms                                                    | 63.7 ms: 1.06x faster                                                  |
| tornado_http               | 94.6 ms                                                    | 89.8 ms: 1.05x faster                                                  |
| json_loads                 | 28.9 us                                                    | 27.4 us: 1.05x faster                                                  |
| bench_thread_pool          | 834 us                                                     | 792 us: 1.05x faster                                                   |
| docutils                   | 2.83 sec                                                   | 2.69 sec: 1.05x faster                                                 |
| regex_v8                   | 25.1 ms                                                    | 23.9 ms: 1.05x faster                                                  |
| regex_compile              | 137 ms                                                     | 131 ms: 1.04x faster                                                   |
| sympy_sum                  | 156 ms                                                     | 149 ms: 1.04x faster                                                   |
| logging_simple             | 5.74 us                                                    | 5.51 us: 1.04x faster                                                  |
| json                       | 5.31 ms                                                    | 5.10 ms: 1.04x faster                                                  |
| 2to3                       | 274 ms                                                     | 263 ms: 1.04x faster                                                   |
| sympy_str                  | 282 ms                                                     | 272 ms: 1.04x faster                                                   |
| sqlglot_optimize           | 55.5 ms                                                    | 53.5 ms: 1.04x faster                                                  |
| nqueens                    | 81.4 ms                                                    | 78.5 ms: 1.04x faster                                                  |
| create_gc_cycles           | 1.82 ms                                                    | 1.75 ms: 1.04x faster                                                  |
| sympy_integrate            | 20.5 ms                                                    | 19.8 ms: 1.04x faster                                                  |
| pyflate                    | 484 ms                                                     | 467 ms: 1.04x faster                                                   |
| html5lib                   | 67.2 ms                                                    | 64.9 ms: 1.04x faster                                                  |
| thrift                     | 823 us                                                     | 796 us: 1.03x faster                                                   |
| spectral_norm              | 116 ms                                                     | 112 ms: 1.03x faster                                                   |
| asyncio_tcp                | 508 ms                                                     | 492 ms: 1.03x faster                                                   |
| async_generators           | 442 ms                                                     | 428 ms: 1.03x faster                                                   |
| unpickle_pure_python       | 218 us                                                     | 211 us: 1.03x faster                                                   |
| dask                       | 369 ms                                                     | 359 ms: 1.03x faster                                                   |
| sqlglot_normalize          | 110 ms                                                     | 107 ms: 1.03x faster                                                   |
| pycparser                  | 1.16 sec                                                   | 1.13 sec: 1.03x faster                                                 |
| go                         | 145 ms                                                     | 140 ms: 1.03x faster                                                   |
| genshi_xml                 | 51.6 ms                                                    | 50.2 ms: 1.03x faster                                                  |
| xml_etree_parse            | 162 ms                                                     | 158 ms: 1.03x faster                                                   |
| sqlglot_transpile          | 1.63 ms                                                    | 1.59 ms: 1.03x faster                                                  |
| xml_etree_process          | 61.2 ms                                                    | 59.6 ms: 1.03x faster                                                  |
| xml_etree_iterparse        | 107 ms                                                     | 105 ms: 1.03x faster                                                   |
| sympy_expand               | 473 ms                                                     | 461 ms: 1.03x faster                                                   |
| genshi_text                | 23.7 ms                                                    | 23.1 ms: 1.03x faster                                                  |
| chaos                      | 61.3 ms                                                    | 59.9 ms: 1.02x faster                                                  |
| bpe_tokeniser              | 5.02 sec                                                   | 4.91 sec: 1.02x faster                                                 |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.80 sec: 1.02x faster                                                 |
| regex_dna                  | 221 ms                                                     | 217 ms: 1.02x faster                                                   |
| pprint_pformat             | 1.56 sec                                                   | 1.52 sec: 1.02x faster                                                 |
| meteor_contest             | 110 ms                                                     | 108 ms: 1.02x faster                                                   |
| python_startup             | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                                  |
| pprint_safe_repr           | 758 ms                                                     | 745 ms: 1.02x faster                                                   |
| pidigits                   | 191 ms                                                     | 188 ms: 1.02x faster                                                   |
| sqlglot_parse              | 1.32 ms                                                    | 1.30 ms: 1.02x faster                                                  |
| xml_etree_generate         | 87.4 ms                                                    | 85.9 ms: 1.02x faster                                                  |
| json_dumps                 | 10.7 ms                                                    | 10.5 ms: 1.02x faster                                                  |
| typing_runtime_protocols   | 165 us                                                     | 162 us: 1.02x faster                                                   |
| asyncio_websockets         | 567 ms                                                     | 558 ms: 1.02x faster                                                   |
| scimark_sor                | 127 ms                                                     | 126 ms: 1.02x faster                                                   |
| django_template            | 34.8 ms                                                    | 34.3 ms: 1.02x faster                                                  |
| comprehensions             | 16.6 us                                                    | 16.4 us: 1.01x faster                                                  |
| generators                 | 29.6 ms                                                    | 29.3 ms: 1.01x faster                                                  |
| float                      | 78.9 ms                                                    | 78.1 ms: 1.01x faster                                                  |
| hexiom                     | 6.30 ms                                                    | 6.24 ms: 1.01x faster                                                  |
| telco                      | 8.41 ms                                                    | 8.34 ms: 1.01x faster                                                  |
| pickle_pure_python         | 305 us                                                     | 303 us: 1.01x faster                                                   |
| coroutines                 | 23.2 ms                                                    | 23.0 ms: 1.01x faster                                                  |
| scimark_monte_carlo        | 69.2 ms                                                    | 68.8 ms: 1.01x faster                                                  |
| python_startup_no_site     | 7.11 ms                                                    | 7.09 ms: 1.00x faster                                                  |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                                  |
| raytrace                   | 267 ms                                                     | 269 ms: 1.01x slower                                                   |
| deltablue                  | 3.25 ms                                                    | 3.29 ms: 1.01x slower                                                  |
| mako                       | 11.2 ms                                                    | 11.5 ms: 1.03x slower                                                  |
| logging_silent             | 105 ns                                                     | 108 ns: 1.03x slower                                                   |
| nbody                      | 88.3 ms                                                    | 91.4 ms: 1.03x slower                                                  |
| Geometric mean             | (ref)                                                      | 1.05x faster                                                           |

Benchmark hidden because not significant (5): pylint, fannkuch, tomli_loads, coverage, regex_effbot
Ignored benchmarks (12) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.00x