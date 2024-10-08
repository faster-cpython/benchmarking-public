# Results vs. 3.13.0b2

- fork: faster-cpython
- ref: fix_122821
- machine: linux-x86_64
- commit hash: 87e2bf8
- commit date: 2024-08-12
- overall geometric mean: 1.04x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240812-linux-x86_64-faster%2dcpython-fix_122821-3.14.0a0-87e2bf8 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 263 ms: 1.04x faster                                                  |
| docutils       | 2.83 sec                                                   | 2.73 sec: 1.03x faster                                                |
| html5lib       | 67.2 ms                                                    | 65.0 ms: 1.03x faster                                                 |
| tornado_http   | 94.6 ms                                                    | 90.8 ms: 1.04x faster                                                 |
| Geometric mean | (ref)                                                      | 1.04x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240812-linux-x86_64-faster%2dcpython-fix_122821-3.14.0a0-87e2bf8 |
|----------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 322 ms: 1.17x faster                                                  |
| async_tree_memoization_tg  | 444 ms                                                     | 389 ms: 1.14x faster                                                  |
| async_tree_none_tg         | 336 ms                                                     | 298 ms: 1.13x faster                                                  |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 530 ms: 1.11x faster                                                  |
| async_tree_memoization     | 463 ms                                                     | 421 ms: 1.10x faster                                                  |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 563 ms: 1.09x faster                                                  |
| async_tree_io_tg           | 936 ms                                                     | 877 ms: 1.07x faster                                                  |
| async_tree_io              | 939 ms                                                     | 897 ms: 1.05x faster                                                  |
| Geometric mean             | (ref)                                                      | 1.11x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240812-linux-x86_64-faster%2dcpython-fix_122821-3.14.0a0-87e2bf8 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 191 ms                                                     | 188 ms: 1.02x faster                                                  |
| nbody          | 88.3 ms                                                    | 87.7 ms: 1.01x faster                                                 |
| Geometric mean | (ref)                                                      | 1.01x faster                                                          |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240812-linux-x86_64-faster%2dcpython-fix_122821-3.14.0a0-87e2bf8 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                     | 132 ms: 1.04x faster                                                  |
| regex_dna      | 221 ms                                                     | 227 ms: 1.03x slower                                                  |
| regex_v8       | 25.1 ms                                                    | 26.2 ms: 1.04x slower                                                 |
| regex_effbot   | 3.67 ms                                                    | 3.87 ms: 1.05x slower                                                 |
| Geometric mean | (ref)                                                      | 1.02x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240812-linux-x86_64-faster%2dcpython-fix_122821-3.14.0a0-87e2bf8 |
|----------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_parse      | 162 ms                                                     | 156 ms: 1.04x faster                                                  |
| json_dumps           | 10.7 ms                                                    | 10.4 ms: 1.03x faster                                                 |
| xml_etree_process    | 61.2 ms                                                    | 59.5 ms: 1.03x faster                                                 |
| xml_etree_iterparse  | 107 ms                                                     | 104 ms: 1.03x faster                                                  |
| json_loads           | 28.9 us                                                    | 28.2 us: 1.03x faster                                                 |
| unpickle_pure_python | 218 us                                                     | 214 us: 1.02x faster                                                  |
| xml_etree_generate   | 87.4 ms                                                    | 85.9 ms: 1.02x faster                                                 |
| Geometric mean       | (ref)                                                      | 1.02x faster                                                          |

Benchmark hidden because not significant (2): tomli_loads, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240812-linux-x86_64-faster%2dcpython-fix_122821-3.14.0a0-87e2bf8 |
|------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.5 ms: 1.03x faster                                                 |
| python_startup_no_site | 7.11 ms                                                    | 7.05 ms: 1.01x faster                                                 |
| Geometric mean         | (ref)                                                      | 1.02x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240812-linux-x86_64-faster%2dcpython-fix_122821-3.14.0a0-87e2bf8 |
|-----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 11.0 ms: 1.02x faster                                                 |
| django_template | 34.8 ms                                                    | 34.3 ms: 1.01x faster                                                 |
| genshi_text     | 23.7 ms                                                    | 23.8 ms: 1.00x slower                                                 |
| genshi_xml      | 51.6 ms                                                    | 52.8 ms: 1.02x slower                                                 |
| Geometric mean  | (ref)                                                      | 1.00x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240812-linux-x86_64-faster%2dcpython-fix_122821-3.14.0a0-87e2bf8 |
|----------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy                   | 367 us                                                     | 266 us: 1.38x faster                                                  |
| deepcopy_memo              | 39.7 us                                                    | 30.1 us: 1.32x faster                                                 |
| deepcopy_reduce            | 3.35 us                                                    | 2.77 us: 1.21x faster                                                 |
| async_tree_none            | 378 ms                                                     | 322 ms: 1.17x faster                                                  |
| async_tree_memoization_tg  | 444 ms                                                     | 389 ms: 1.14x faster                                                  |
| async_tree_none_tg         | 336 ms                                                     | 298 ms: 1.13x faster                                                  |
| gc_traversal               | 3.98 ms                                                    | 3.54 ms: 1.12x faster                                                 |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 530 ms: 1.11x faster                                                  |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.76 ms: 1.11x faster                                                 |
| async_tree_memoization     | 463 ms                                                     | 421 ms: 1.10x faster                                                  |
| richards_super             | 57.4 ms                                                    | 52.3 ms: 1.10x faster                                                 |
| richards                   | 50.9 ms                                                    | 46.4 ms: 1.10x faster                                                 |
| pathlib                    | 17.3 ms                                                    | 15.8 ms: 1.09x faster                                                 |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 563 ms: 1.09x faster                                                  |
| scimark_fft                | 392 ms                                                     | 367 ms: 1.07x faster                                                  |
| scimark_lu                 | 122 ms                                                     | 114 ms: 1.07x faster                                                  |
| async_tree_io_tg           | 936 ms                                                     | 877 ms: 1.07x faster                                                  |
| crypto_pyaes               | 77.5 ms                                                    | 72.9 ms: 1.06x faster                                                 |
| create_gc_cycles           | 1.82 ms                                                    | 1.71 ms: 1.06x faster                                                 |
| generators                 | 29.6 ms                                                    | 28.0 ms: 1.06x faster                                                 |
| logging_silent             | 105 ns                                                     | 99.2 ns: 1.06x faster                                                 |
| bench_thread_pool          | 834 us                                                     | 791 us: 1.05x faster                                                  |
| async_tree_io              | 939 ms                                                     | 897 ms: 1.05x faster                                                  |
| thrift                     | 823 us                                                     | 787 us: 1.05x faster                                                  |
| 2to3                       | 274 ms                                                     | 263 ms: 1.04x faster                                                  |
| chaos                      | 61.3 ms                                                    | 58.8 ms: 1.04x faster                                                 |
| tornado_http               | 94.6 ms                                                    | 90.8 ms: 1.04x faster                                                 |
| json                       | 5.31 ms                                                    | 5.09 ms: 1.04x faster                                                 |
| sympy_str                  | 282 ms                                                     | 272 ms: 1.04x faster                                                  |
| bpe_tokeniser              | 5.02 sec                                                   | 4.85 sec: 1.04x faster                                                |
| xml_etree_parse            | 162 ms                                                     | 156 ms: 1.04x faster                                                  |
| regex_compile              | 137 ms                                                     | 132 ms: 1.04x faster                                                  |
| html5lib                   | 67.2 ms                                                    | 65.0 ms: 1.03x faster                                                 |
| docutils                   | 2.83 sec                                                   | 2.73 sec: 1.03x faster                                                |
| logging_format             | 6.47 us                                                    | 6.26 us: 1.03x faster                                                 |
| sympy_integrate            | 20.5 ms                                                    | 19.8 ms: 1.03x faster                                                 |
| raytrace                   | 267 ms                                                     | 258 ms: 1.03x faster                                                  |
| coroutines                 | 23.2 ms                                                    | 22.5 ms: 1.03x faster                                                 |
| asyncio_tcp                | 508 ms                                                     | 492 ms: 1.03x faster                                                  |
| sqlglot_optimize           | 55.5 ms                                                    | 53.8 ms: 1.03x faster                                                 |
| hexiom                     | 6.30 ms                                                    | 6.10 ms: 1.03x faster                                                 |
| sympy_sum                  | 156 ms                                                     | 151 ms: 1.03x faster                                                  |
| json_dumps                 | 10.7 ms                                                    | 10.4 ms: 1.03x faster                                                 |
| sqlglot_transpile          | 1.63 ms                                                    | 1.59 ms: 1.03x faster                                                 |
| mdp                        | 2.79 sec                                                   | 2.71 sec: 1.03x faster                                                |
| sympy_expand               | 473 ms                                                     | 459 ms: 1.03x faster                                                  |
| xml_etree_process          | 61.2 ms                                                    | 59.5 ms: 1.03x faster                                                 |
| xml_etree_iterparse        | 107 ms                                                     | 104 ms: 1.03x faster                                                  |
| go                         | 145 ms                                                     | 141 ms: 1.03x faster                                                  |
| python_startup             | 10.8 ms                                                    | 10.5 ms: 1.03x faster                                                 |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.79 sec: 1.03x faster                                                |
| json_loads                 | 28.9 us                                                    | 28.2 us: 1.03x faster                                                 |
| logging_simple             | 5.74 us                                                    | 5.60 us: 1.03x faster                                                 |
| coverage                   | 93.1 ms                                                    | 90.8 ms: 1.03x faster                                                 |
| sqlglot_parse              | 1.32 ms                                                    | 1.29 ms: 1.02x faster                                                 |
| meteor_contest             | 110 ms                                                     | 107 ms: 1.02x faster                                                  |
| mako                       | 11.2 ms                                                    | 11.0 ms: 1.02x faster                                                 |
| nqueens                    | 81.4 ms                                                    | 79.7 ms: 1.02x faster                                                 |
| sqlglot_normalize          | 110 ms                                                     | 108 ms: 1.02x faster                                                  |
| unpickle_pure_python       | 218 us                                                     | 214 us: 1.02x faster                                                  |
| scimark_sor                | 127 ms                                                     | 125 ms: 1.02x faster                                                  |
| pidigits                   | 191 ms                                                     | 188 ms: 1.02x faster                                                  |
| telco                      | 8.41 ms                                                    | 8.26 ms: 1.02x faster                                                 |
| xml_etree_generate         | 87.4 ms                                                    | 85.9 ms: 1.02x faster                                                 |
| django_template            | 34.8 ms                                                    | 34.3 ms: 1.01x faster                                                 |
| pyflate                    | 484 ms                                                     | 478 ms: 1.01x faster                                                  |
| scimark_monte_carlo        | 69.2 ms                                                    | 68.3 ms: 1.01x faster                                                 |
| asyncio_websockets         | 567 ms                                                     | 560 ms: 1.01x faster                                                  |
| spectral_norm              | 116 ms                                                     | 115 ms: 1.01x faster                                                  |
| pprint_safe_repr           | 758 ms                                                     | 751 ms: 1.01x faster                                                  |
| python_startup_no_site     | 7.11 ms                                                    | 7.05 ms: 1.01x faster                                                 |
| nbody                      | 88.3 ms                                                    | 87.7 ms: 1.01x faster                                                 |
| fannkuch                   | 402 ms                                                     | 400 ms: 1.01x faster                                                  |
| pprint_pformat             | 1.56 sec                                                   | 1.55 sec: 1.00x faster                                                |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.00x slower                                                 |
| genshi_text                | 23.7 ms                                                    | 23.8 ms: 1.00x slower                                                 |
| deltablue                  | 3.25 ms                                                    | 3.28 ms: 1.01x slower                                                 |
| comprehensions             | 16.6 us                                                    | 16.8 us: 1.01x slower                                                 |
| pycparser                  | 1.16 sec                                                   | 1.18 sec: 1.02x slower                                                |
| genshi_xml                 | 51.6 ms                                                    | 52.8 ms: 1.02x slower                                                 |
| regex_dna                  | 221 ms                                                     | 227 ms: 1.03x slower                                                  |
| regex_v8                   | 25.1 ms                                                    | 26.2 ms: 1.04x slower                                                 |
| regex_effbot               | 3.67 ms                                                    | 3.87 ms: 1.05x slower                                                 |
| Geometric mean             | (ref)                                                      | 1.04x faster                                                          |

Benchmark hidden because not significant (6): tomli_loads, typing_runtime_protocols, pickle_pure_python, float, pylint, async_generators
Ignored benchmarks (14) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.00x