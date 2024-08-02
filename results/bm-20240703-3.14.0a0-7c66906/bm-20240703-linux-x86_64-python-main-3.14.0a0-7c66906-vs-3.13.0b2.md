# Results vs. 3.13.0b2

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 7c66906
- commit date: 2024-07-03
- overall geometric mean: 1.05x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240703-linux-x86_64-python-main-3.14.0a0-7c66906 |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------:|
| 2to3           | 274 ms                                                     | 262 ms: 1.05x faster                                  |
| docutils       | 2.83 sec                                                   | 2.69 sec: 1.05x faster                                |
| html5lib       | 67.2 ms                                                    | 64.2 ms: 1.05x faster                                 |
| tornado_http   | 94.6 ms                                                    | 90.2 ms: 1.05x faster                                 |
| Geometric mean | (ref)                                                      | 1.05x faster                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240703-linux-x86_64-python-main-3.14.0a0-7c66906 |
|----------------------------|:----------------------------------------------------------:|:-----------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 321 ms: 1.18x faster                                  |
| async_tree_memoization_tg  | 444 ms                                                     | 378 ms: 1.17x faster                                  |
| async_tree_memoization     | 463 ms                                                     | 405 ms: 1.14x faster                                  |
| async_tree_io              | 939 ms                                                     | 827 ms: 1.13x faster                                  |
| async_tree_none_tg         | 336 ms                                                     | 298 ms: 1.13x faster                                  |
| async_tree_io_tg           | 936 ms                                                     | 842 ms: 1.11x faster                                  |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 541 ms: 1.09x faster                                  |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 566 ms: 1.08x faster                                  |
| Geometric mean             | (ref)                                                      | 1.13x faster                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240703-linux-x86_64-python-main-3.14.0a0-7c66906 |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------:|
| float          | 78.9 ms                                                    | 76.4 ms: 1.03x faster                                 |
| pidigits       | 191 ms                                                     | 187 ms: 1.02x faster                                  |
| nbody          | 88.3 ms                                                    | 86.5 ms: 1.02x faster                                 |
| Geometric mean | (ref)                                                      | 1.03x faster                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240703-linux-x86_64-python-main-3.14.0a0-7c66906 |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------:|
| regex_compile  | 137 ms                                                     | 129 ms: 1.06x faster                                  |
| regex_v8       | 25.1 ms                                                    | 25.7 ms: 1.02x slower                                 |
| regex_effbot   | 3.67 ms                                                    | 3.79 ms: 1.03x slower                                 |
| regex_dna      | 221 ms                                                     | 231 ms: 1.04x slower                                  |
| Geometric mean | (ref)                                                      | 1.01x slower                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240703-linux-x86_64-python-main-3.14.0a0-7c66906 |
|----------------------|:----------------------------------------------------------:|:-----------------------------------------------------:|
| json_loads           | 28.9 us                                                    | 27.8 us: 1.04x faster                                 |
| xml_etree_parse      | 162 ms                                                     | 156 ms: 1.04x faster                                  |
| unpickle_pure_python | 218 us                                                     | 211 us: 1.03x faster                                  |
| xml_etree_iterparse  | 107 ms                                                     | 104 ms: 1.03x faster                                  |
| xml_etree_process    | 61.2 ms                                                    | 59.2 ms: 1.03x faster                                 |
| xml_etree_generate   | 87.4 ms                                                    | 85.2 ms: 1.03x faster                                 |
| json_dumps           | 10.7 ms                                                    | 10.5 ms: 1.02x faster                                 |
| pickle_pure_python   | 305 us                                                     | 300 us: 1.02x faster                                  |
| Geometric mean       | (ref)                                                      | 1.03x faster                                          |

Benchmark hidden because not significant (1): tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240703-linux-x86_64-python-main-3.14.0a0-7c66906 |
|------------------------|:----------------------------------------------------------:|:-----------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.5 ms: 1.03x faster                                 |
| python_startup_no_site | 7.11 ms                                                    | 7.03 ms: 1.01x faster                                 |
| Geometric mean         | (ref)                                                      | 1.02x faster                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240703-linux-x86_64-python-main-3.14.0a0-7c66906 |
|-----------------|:----------------------------------------------------------:|:-----------------------------------------------------:|
| genshi_xml      | 51.6 ms                                                    | 49.2 ms: 1.05x faster                                 |
| django_template | 34.8 ms                                                    | 33.7 ms: 1.03x faster                                 |
| genshi_text     | 23.7 ms                                                    | 22.9 ms: 1.03x faster                                 |
| mako            | 11.2 ms                                                    | 10.9 ms: 1.03x faster                                 |
| Geometric mean  | (ref)                                                      | 1.04x faster                                          |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240703-linux-x86_64-python-main-3.14.0a0-7c66906 |
|----------------------------|:----------------------------------------------------------:|:-----------------------------------------------------:|
| deepcopy                   | 367 us                                                     | 258 us: 1.42x faster                                  |
| deepcopy_memo              | 39.7 us                                                    | 29.0 us: 1.37x faster                                 |
| deepcopy_reduce            | 3.35 us                                                    | 2.62 us: 1.28x faster                                 |
| async_tree_none            | 378 ms                                                     | 321 ms: 1.18x faster                                  |
| async_tree_memoization_tg  | 444 ms                                                     | 378 ms: 1.17x faster                                  |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.58 ms: 1.15x faster                                 |
| async_tree_memoization     | 463 ms                                                     | 405 ms: 1.14x faster                                  |
| async_tree_io              | 939 ms                                                     | 827 ms: 1.13x faster                                  |
| async_tree_none_tg         | 336 ms                                                     | 298 ms: 1.13x faster                                  |
| scimark_fft                | 392 ms                                                     | 350 ms: 1.12x faster                                  |
| async_tree_io_tg           | 936 ms                                                     | 842 ms: 1.11x faster                                  |
| richards                   | 50.9 ms                                                    | 45.9 ms: 1.11x faster                                 |
| richards_super             | 57.4 ms                                                    | 52.0 ms: 1.10x faster                                 |
| scimark_lu                 | 122 ms                                                     | 111 ms: 1.10x faster                                  |
| pathlib                    | 17.3 ms                                                    | 15.9 ms: 1.09x faster                                 |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 541 ms: 1.09x faster                                  |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 566 ms: 1.08x faster                                  |
| gc_traversal               | 3.98 ms                                                    | 3.68 ms: 1.08x faster                                 |
| spectral_norm              | 116 ms                                                     | 108 ms: 1.08x faster                                  |
| crypto_pyaes               | 77.5 ms                                                    | 72.7 ms: 1.06x faster                                 |
| chaos                      | 61.3 ms                                                    | 57.9 ms: 1.06x faster                                 |
| regex_compile              | 137 ms                                                     | 129 ms: 1.06x faster                                  |
| bench_thread_pool          | 834 us                                                     | 791 us: 1.05x faster                                  |
| docutils                   | 2.83 sec                                                   | 2.69 sec: 1.05x faster                                |
| create_gc_cycles           | 1.82 ms                                                    | 1.73 ms: 1.05x faster                                 |
| genshi_xml                 | 51.6 ms                                                    | 49.2 ms: 1.05x faster                                 |
| raytrace                   | 267 ms                                                     | 254 ms: 1.05x faster                                  |
| tornado_http               | 94.6 ms                                                    | 90.2 ms: 1.05x faster                                 |
| sympy_str                  | 282 ms                                                     | 269 ms: 1.05x faster                                  |
| sympy_integrate            | 20.5 ms                                                    | 19.6 ms: 1.05x faster                                 |
| html5lib                   | 67.2 ms                                                    | 64.2 ms: 1.05x faster                                 |
| 2to3                       | 274 ms                                                     | 262 ms: 1.05x faster                                  |
| dulwich_log                | 67.2 ms                                                    | 64.3 ms: 1.04x faster                                 |
| asyncio_tcp                | 508 ms                                                     | 487 ms: 1.04x faster                                  |
| nqueens                    | 81.4 ms                                                    | 78.1 ms: 1.04x faster                                 |
| scimark_monte_carlo        | 69.2 ms                                                    | 66.4 ms: 1.04x faster                                 |
| sympy_sum                  | 156 ms                                                     | 150 ms: 1.04x faster                                  |
| thrift                     | 823 us                                                     | 791 us: 1.04x faster                                  |
| sqlglot_optimize           | 55.5 ms                                                    | 53.4 ms: 1.04x faster                                 |
| json_loads                 | 28.9 us                                                    | 27.8 us: 1.04x faster                                 |
| xml_etree_parse            | 162 ms                                                     | 156 ms: 1.04x faster                                  |
| sqlglot_parse              | 1.32 ms                                                    | 1.27 ms: 1.04x faster                                 |
| meteor_contest             | 110 ms                                                     | 106 ms: 1.04x faster                                  |
| logging_format             | 6.47 us                                                    | 6.24 us: 1.04x faster                                 |
| dask                       | 369 ms                                                     | 357 ms: 1.04x faster                                  |
| pyflate                    | 484 ms                                                     | 467 ms: 1.04x faster                                  |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.78 sec: 1.04x faster                                |
| hexiom                     | 6.30 ms                                                    | 6.08 ms: 1.04x faster                                 |
| unpickle_pure_python       | 218 us                                                     | 211 us: 1.03x faster                                  |
| json                       | 5.31 ms                                                    | 5.13 ms: 1.03x faster                                 |
| xml_etree_iterparse        | 107 ms                                                     | 104 ms: 1.03x faster                                  |
| sqlglot_transpile          | 1.63 ms                                                    | 1.58 ms: 1.03x faster                                 |
| go                         | 145 ms                                                     | 140 ms: 1.03x faster                                  |
| xml_etree_process          | 61.2 ms                                                    | 59.2 ms: 1.03x faster                                 |
| django_template            | 34.8 ms                                                    | 33.7 ms: 1.03x faster                                 |
| sympy_expand               | 473 ms                                                     | 458 ms: 1.03x faster                                  |
| generators                 | 29.6 ms                                                    | 28.7 ms: 1.03x faster                                 |
| float                      | 78.9 ms                                                    | 76.4 ms: 1.03x faster                                 |
| pprint_pformat             | 1.56 sec                                                   | 1.51 sec: 1.03x faster                                |
| genshi_text                | 23.7 ms                                                    | 22.9 ms: 1.03x faster                                 |
| logging_silent             | 105 ns                                                     | 102 ns: 1.03x faster                                  |
| bpe_tokeniser              | 5.02 sec                                                   | 4.87 sec: 1.03x faster                                |
| logging_simple             | 5.74 us                                                    | 5.57 us: 1.03x faster                                 |
| mako                       | 11.2 ms                                                    | 10.9 ms: 1.03x faster                                 |
| python_startup             | 10.8 ms                                                    | 10.5 ms: 1.03x faster                                 |
| sqlglot_normalize          | 110 ms                                                     | 107 ms: 1.03x faster                                  |
| pprint_safe_repr           | 758 ms                                                     | 739 ms: 1.03x faster                                  |
| xml_etree_generate         | 87.4 ms                                                    | 85.2 ms: 1.03x faster                                 |
| deltablue                  | 3.25 ms                                                    | 3.17 ms: 1.02x faster                                 |
| telco                      | 8.41 ms                                                    | 8.22 ms: 1.02x faster                                 |
| pidigits                   | 191 ms                                                     | 187 ms: 1.02x faster                                  |
| scimark_sor                | 127 ms                                                     | 125 ms: 1.02x faster                                  |
| asyncio_websockets         | 567 ms                                                     | 555 ms: 1.02x faster                                  |
| nbody                      | 88.3 ms                                                    | 86.5 ms: 1.02x faster                                 |
| json_dumps                 | 10.7 ms                                                    | 10.5 ms: 1.02x faster                                 |
| pickle_pure_python         | 305 us                                                     | 300 us: 1.02x faster                                  |
| mdp                        | 2.79 sec                                                   | 2.74 sec: 1.02x faster                                |
| fannkuch                   | 402 ms                                                     | 397 ms: 1.01x faster                                  |
| comprehensions             | 16.6 us                                                    | 16.4 us: 1.01x faster                                 |
| typing_runtime_protocols   | 165 us                                                     | 163 us: 1.01x faster                                  |
| async_generators           | 442 ms                                                     | 437 ms: 1.01x faster                                  |
| python_startup_no_site     | 7.11 ms                                                    | 7.03 ms: 1.01x faster                                 |
| coroutines                 | 23.2 ms                                                    | 23.0 ms: 1.01x faster                                 |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                 |
| pycparser                  | 1.16 sec                                                   | 1.18 sec: 1.02x slower                                |
| regex_v8                   | 25.1 ms                                                    | 25.7 ms: 1.02x slower                                 |
| regex_effbot               | 3.67 ms                                                    | 3.79 ms: 1.03x slower                                 |
| regex_dna                  | 221 ms                                                     | 231 ms: 1.04x slower                                  |
| Geometric mean             | (ref)                                                      | 1.05x faster                                          |

Benchmark hidden because not significant (3): pylint, coverage, tomli_loads
Ignored benchmarks (12) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.00x