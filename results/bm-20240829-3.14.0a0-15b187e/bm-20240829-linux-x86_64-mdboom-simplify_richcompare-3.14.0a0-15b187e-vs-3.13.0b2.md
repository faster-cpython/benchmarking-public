# Results vs. 3.13.0b2

- fork: mdboom
- ref: simplify_richcompare
- machine: linux-x86_64
- commit hash: 15b187e
- commit date: 2024-08-29
- overall geometric mean: 1.05x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 256 ms: 1.07x faster                                                  |
| docutils       | 2.83 sec                                                   | 2.67 sec: 1.06x faster                                                |
| html5lib       | 67.2 ms                                                    | 64.0 ms: 1.05x faster                                                 |
| tornado_http   | 94.6 ms                                                    | 89.9 ms: 1.05x faster                                                 |
| Geometric mean | (ref)                                                      | 1.06x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization     | 463 ms                                                     | 389 ms: 1.19x faster                                                  |
| async_tree_none            | 378 ms                                                     | 322 ms: 1.18x faster                                                  |
| async_tree_memoization_tg  | 444 ms                                                     | 399 ms: 1.11x faster                                                  |
| async_tree_none_tg         | 336 ms                                                     | 306 ms: 1.10x faster                                                  |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 557 ms: 1.10x faster                                                  |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 538 ms: 1.09x faster                                                  |
| async_tree_io_tg           | 936 ms                                                     | 887 ms: 1.06x faster                                                  |
| Geometric mean             | (ref)                                                      | 1.10x faster                                                          |

Benchmark hidden because not significant (1): async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 191 ms                                                     | 186 ms: 1.03x faster                                                  |
| float          | 78.9 ms                                                    | 78.3 ms: 1.01x faster                                                 |
| nbody          | 88.3 ms                                                    | 89.8 ms: 1.02x slower                                                 |
| Geometric mean | (ref)                                                      | 1.01x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                     | 129 ms: 1.06x faster                                                  |
| regex_dna      | 221 ms                                                     | 224 ms: 1.01x slower                                                  |
| regex_effbot   | 3.67 ms                                                    | 3.77 ms: 1.03x slower                                                 |
| regex_v8       | 25.1 ms                                                    | 26.1 ms: 1.04x slower                                                 |
| Geometric mean | (ref)                                                      | 1.00x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_parse      | 162 ms                                                     | 154 ms: 1.05x faster                                                  |
| xml_etree_process    | 61.2 ms                                                    | 58.7 ms: 1.04x faster                                                 |
| xml_etree_generate   | 87.4 ms                                                    | 84.6 ms: 1.03x faster                                                 |
| xml_etree_iterparse  | 107 ms                                                     | 104 ms: 1.03x faster                                                  |
| json_dumps           | 10.7 ms                                                    | 10.4 ms: 1.03x faster                                                 |
| tomli_loads          | 2.12 sec                                                   | 2.08 sec: 1.02x faster                                                |
| unpickle_pure_python | 218 us                                                     | 214 us: 1.02x faster                                                  |
| pickle_pure_python   | 305 us                                                     | 301 us: 1.02x faster                                                  |
| json_loads           | 28.9 us                                                    | 28.6 us: 1.01x faster                                                 |
| Geometric mean       | (ref)                                                      | 1.03x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                                 |
| python_startup_no_site | 7.11 ms                                                    | 7.07 ms: 1.01x faster                                                 |
| Geometric mean         | (ref)                                                      | 1.01x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|-----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 23.7 ms                                                    | 21.8 ms: 1.09x faster                                                 |
| genshi_xml      | 51.6 ms                                                    | 49.1 ms: 1.05x faster                                                 |
| django_template | 34.8 ms                                                    | 33.8 ms: 1.03x faster                                                 |
| mako            | 11.2 ms                                                    | 11.5 ms: 1.02x slower                                                 |
| Geometric mean  | (ref)                                                      | 1.04x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy                   | 367 us                                                     | 260 us: 1.41x faster                                                  |
| deepcopy_memo              | 39.7 us                                                    | 30.1 us: 1.32x faster                                                 |
| deepcopy_reduce            | 3.35 us                                                    | 2.67 us: 1.25x faster                                                 |
| go                         | 145 ms                                                     | 119 ms: 1.22x faster                                                  |
| async_tree_memoization     | 463 ms                                                     | 389 ms: 1.19x faster                                                  |
| async_tree_none            | 378 ms                                                     | 322 ms: 1.18x faster                                                  |
| async_tree_memoization_tg  | 444 ms                                                     | 399 ms: 1.11x faster                                                  |
| mdp                        | 2.79 sec                                                   | 2.50 sec: 1.11x faster                                                |
| richards                   | 50.9 ms                                                    | 45.9 ms: 1.11x faster                                                 |
| richards_super             | 57.4 ms                                                    | 51.9 ms: 1.11x faster                                                 |
| pathlib                    | 17.3 ms                                                    | 15.7 ms: 1.10x faster                                                 |
| async_tree_none_tg         | 336 ms                                                     | 306 ms: 1.10x faster                                                  |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 557 ms: 1.10x faster                                                  |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 538 ms: 1.09x faster                                                  |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.83 ms: 1.09x faster                                                 |
| genshi_text                | 23.7 ms                                                    | 21.8 ms: 1.09x faster                                                 |
| crypto_pyaes               | 77.5 ms                                                    | 71.4 ms: 1.08x faster                                                 |
| coverage                   | 93.1 ms                                                    | 86.2 ms: 1.08x faster                                                 |
| asyncio_tcp                | 508 ms                                                     | 473 ms: 1.07x faster                                                  |
| 2to3                       | 274 ms                                                     | 256 ms: 1.07x faster                                                  |
| thrift                     | 823 us                                                     | 767 us: 1.07x faster                                                  |
| gc_traversal               | 3.98 ms                                                    | 3.71 ms: 1.07x faster                                                 |
| scimark_lu                 | 122 ms                                                     | 114 ms: 1.07x faster                                                  |
| generators                 | 29.6 ms                                                    | 27.8 ms: 1.07x faster                                                 |
| sympy_sum                  | 156 ms                                                     | 146 ms: 1.06x faster                                                  |
| scimark_fft                | 392 ms                                                     | 369 ms: 1.06x faster                                                  |
| bench_thread_pool          | 834 us                                                     | 784 us: 1.06x faster                                                  |
| regex_compile              | 137 ms                                                     | 129 ms: 1.06x faster                                                  |
| pprint_pformat             | 1.56 sec                                                   | 1.47 sec: 1.06x faster                                                |
| docutils                   | 2.83 sec                                                   | 2.67 sec: 1.06x faster                                                |
| pprint_safe_repr           | 758 ms                                                     | 716 ms: 1.06x faster                                                  |
| async_tree_io_tg           | 936 ms                                                     | 887 ms: 1.06x faster                                                  |
| sympy_integrate            | 20.5 ms                                                    | 19.4 ms: 1.05x faster                                                 |
| tornado_http               | 94.6 ms                                                    | 89.9 ms: 1.05x faster                                                 |
| genshi_xml                 | 51.6 ms                                                    | 49.1 ms: 1.05x faster                                                 |
| sympy_str                  | 282 ms                                                     | 269 ms: 1.05x faster                                                  |
| html5lib                   | 67.2 ms                                                    | 64.0 ms: 1.05x faster                                                 |
| chaos                      | 61.3 ms                                                    | 58.6 ms: 1.05x faster                                                 |
| xml_etree_parse            | 162 ms                                                     | 154 ms: 1.05x faster                                                  |
| logging_format             | 6.47 us                                                    | 6.18 us: 1.05x faster                                                 |
| xml_etree_process          | 61.2 ms                                                    | 58.7 ms: 1.04x faster                                                 |
| bpe_tokeniser              | 5.02 sec                                                   | 4.83 sec: 1.04x faster                                                |
| typing_runtime_protocols   | 165 us                                                     | 159 us: 1.04x faster                                                  |
| sympy_expand               | 473 ms                                                     | 455 ms: 1.04x faster                                                  |
| sqlglot_transpile          | 1.63 ms                                                    | 1.57 ms: 1.04x faster                                                 |
| meteor_contest             | 110 ms                                                     | 106 ms: 1.04x faster                                                  |
| scimark_monte_carlo        | 69.2 ms                                                    | 66.7 ms: 1.04x faster                                                 |
| create_gc_cycles           | 1.82 ms                                                    | 1.75 ms: 1.04x faster                                                 |
| logging_silent             | 105 ns                                                     | 101 ns: 1.03x faster                                                  |
| logging_simple             | 5.74 us                                                    | 5.55 us: 1.03x faster                                                 |
| sqlglot_optimize           | 55.5 ms                                                    | 53.7 ms: 1.03x faster                                                 |
| xml_etree_generate         | 87.4 ms                                                    | 84.6 ms: 1.03x faster                                                 |
| spectral_norm              | 116 ms                                                     | 113 ms: 1.03x faster                                                  |
| xml_etree_iterparse        | 107 ms                                                     | 104 ms: 1.03x faster                                                  |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.79 sec: 1.03x faster                                                |
| json_dumps                 | 10.7 ms                                                    | 10.4 ms: 1.03x faster                                                 |
| hexiom                     | 6.30 ms                                                    | 6.11 ms: 1.03x faster                                                 |
| sqlglot_parse              | 1.32 ms                                                    | 1.28 ms: 1.03x faster                                                 |
| django_template            | 34.8 ms                                                    | 33.8 ms: 1.03x faster                                                 |
| pidigits                   | 191 ms                                                     | 186 ms: 1.03x faster                                                  |
| python_startup             | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                                 |
| pyflate                    | 484 ms                                                     | 474 ms: 1.02x faster                                                  |
| tomli_loads                | 2.12 sec                                                   | 2.08 sec: 1.02x faster                                                |
| raytrace                   | 267 ms                                                     | 262 ms: 1.02x faster                                                  |
| unpickle_pure_python       | 218 us                                                     | 214 us: 1.02x faster                                                  |
| deltablue                  | 3.25 ms                                                    | 3.20 ms: 1.02x faster                                                 |
| sqlglot_normalize          | 110 ms                                                     | 108 ms: 1.02x faster                                                  |
| asyncio_websockets         | 567 ms                                                     | 558 ms: 1.02x faster                                                  |
| pickle_pure_python         | 305 us                                                     | 301 us: 1.02x faster                                                  |
| nqueens                    | 81.4 ms                                                    | 80.4 ms: 1.01x faster                                                 |
| telco                      | 8.41 ms                                                    | 8.32 ms: 1.01x faster                                                 |
| json_loads                 | 28.9 us                                                    | 28.6 us: 1.01x faster                                                 |
| scimark_sor                | 127 ms                                                     | 126 ms: 1.01x faster                                                  |
| float                      | 78.9 ms                                                    | 78.3 ms: 1.01x faster                                                 |
| async_generators           | 442 ms                                                     | 439 ms: 1.01x faster                                                  |
| comprehensions             | 16.6 us                                                    | 16.5 us: 1.01x faster                                                 |
| python_startup_no_site     | 7.11 ms                                                    | 7.07 ms: 1.01x faster                                                 |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                                 |
| regex_dna                  | 221 ms                                                     | 224 ms: 1.01x slower                                                  |
| nbody                      | 88.3 ms                                                    | 89.8 ms: 1.02x slower                                                 |
| pycparser                  | 1.16 sec                                                   | 1.18 sec: 1.02x slower                                                |
| mako                       | 11.2 ms                                                    | 11.5 ms: 1.02x slower                                                 |
| regex_effbot               | 3.67 ms                                                    | 3.77 ms: 1.03x slower                                                 |
| coroutines                 | 23.2 ms                                                    | 23.8 ms: 1.03x slower                                                 |
| regex_v8                   | 25.1 ms                                                    | 26.1 ms: 1.04x slower                                                 |
| Geometric mean             | (ref)                                                      | 1.05x faster                                                          |

Benchmark hidden because not significant (4): async_tree_io, fannkuch, json, pylint
Ignored benchmarks (14) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.01x