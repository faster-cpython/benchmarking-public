# Results vs. 3.13.0b2

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 7b26c4d
- commit date: 2024-08-21
- overall geometric mean: 1.05x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240821-linux-x86_64-python-main-3.14.0a0-7b26c4d |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------:|
| 2to3           | 274 ms                                                     | 262 ms: 1.05x faster                                  |
| docutils       | 2.83 sec                                                   | 2.72 sec: 1.04x faster                                |
| html5lib       | 67.2 ms                                                    | 63.5 ms: 1.06x faster                                 |
| tornado_http   | 94.6 ms                                                    | 90.2 ms: 1.05x faster                                 |
| Geometric mean | (ref)                                                      | 1.05x faster                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240821-linux-x86_64-python-main-3.14.0a0-7b26c4d |
|----------------------------|:----------------------------------------------------------:|:-----------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 323 ms: 1.17x faster                                  |
| async_tree_memoization_tg  | 444 ms                                                     | 392 ms: 1.13x faster                                  |
| async_tree_none_tg         | 336 ms                                                     | 300 ms: 1.12x faster                                  |
| async_tree_memoization     | 463 ms                                                     | 413 ms: 1.12x faster                                  |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 529 ms: 1.11x faster                                  |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 560 ms: 1.09x faster                                  |
| async_tree_io_tg           | 936 ms                                                     | 867 ms: 1.08x faster                                  |
| async_tree_io              | 939 ms                                                     | 903 ms: 1.04x faster                                  |
| Geometric mean             | (ref)                                                      | 1.11x faster                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240821-linux-x86_64-python-main-3.14.0a0-7b26c4d |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------:|
| pidigits       | 191 ms                                                     | 187 ms: 1.02x faster                                  |
| float          | 78.9 ms                                                    | 78.3 ms: 1.01x faster                                 |
| nbody          | 88.3 ms                                                    | 87.7 ms: 1.01x faster                                 |
| Geometric mean | (ref)                                                      | 1.01x faster                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240821-linux-x86_64-python-main-3.14.0a0-7b26c4d |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------:|
| regex_compile  | 137 ms                                                     | 130 ms: 1.05x faster                                  |
| regex_effbot   | 3.67 ms                                                    | 3.59 ms: 1.02x faster                                 |
| regex_v8       | 25.1 ms                                                    | 24.9 ms: 1.01x faster                                 |
| regex_dna      | 221 ms                                                     | 223 ms: 1.01x slower                                  |
| Geometric mean | (ref)                                                      | 1.02x faster                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240821-linux-x86_64-python-main-3.14.0a0-7b26c4d |
|----------------------|:----------------------------------------------------------:|:-----------------------------------------------------:|
| xml_etree_parse      | 162 ms                                                     | 153 ms: 1.05x faster                                  |
| xml_etree_process    | 61.2 ms                                                    | 59.6 ms: 1.03x faster                                 |
| tomli_loads          | 2.12 sec                                                   | 2.07 sec: 1.02x faster                                |
| xml_etree_iterparse  | 107 ms                                                     | 105 ms: 1.02x faster                                  |
| json_dumps           | 10.7 ms                                                    | 10.5 ms: 1.02x faster                                 |
| xml_etree_generate   | 87.4 ms                                                    | 86.1 ms: 1.02x faster                                 |
| unpickle_pure_python | 218 us                                                     | 215 us: 1.02x faster                                  |
| json_loads           | 28.9 us                                                    | 28.4 us: 1.02x faster                                 |
| pickle_pure_python   | 305 us                                                     | 303 us: 1.01x faster                                  |
| Geometric mean       | (ref)                                                      | 1.02x faster                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240821-linux-x86_64-python-main-3.14.0a0-7b26c4d |
|------------------------|:----------------------------------------------------------:|:-----------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                 |
| python_startup_no_site | 7.11 ms                                                    | 7.09 ms: 1.00x faster                                 |
| Geometric mean         | (ref)                                                      | 1.01x faster                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240821-linux-x86_64-python-main-3.14.0a0-7b26c4d |
|-----------------|:----------------------------------------------------------:|:-----------------------------------------------------:|
| django_template | 34.8 ms                                                    | 33.8 ms: 1.03x faster                                 |
| genshi_text     | 23.7 ms                                                    | 23.5 ms: 1.01x faster                                 |
| genshi_xml      | 51.6 ms                                                    | 51.3 ms: 1.01x faster                                 |
| mako            | 11.2 ms                                                    | 11.3 ms: 1.00x slower                                 |
| Geometric mean  | (ref)                                                      | 1.01x faster                                          |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240821-linux-x86_64-python-main-3.14.0a0-7b26c4d |
|----------------------------|:----------------------------------------------------------:|:-----------------------------------------------------:|
| deepcopy                   | 367 us                                                     | 262 us: 1.40x faster                                  |
| deepcopy_memo              | 39.7 us                                                    | 30.2 us: 1.31x faster                                 |
| deepcopy_reduce            | 3.35 us                                                    | 2.69 us: 1.24x faster                                 |
| async_tree_none            | 378 ms                                                     | 323 ms: 1.17x faster                                  |
| async_tree_memoization_tg  | 444 ms                                                     | 392 ms: 1.13x faster                                  |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.67 ms: 1.13x faster                                 |
| async_tree_none_tg         | 336 ms                                                     | 300 ms: 1.12x faster                                  |
| async_tree_memoization     | 463 ms                                                     | 413 ms: 1.12x faster                                  |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 529 ms: 1.11x faster                                  |
| coverage                   | 93.1 ms                                                    | 83.8 ms: 1.11x faster                                 |
| richards                   | 50.9 ms                                                    | 46.6 ms: 1.09x faster                                 |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 560 ms: 1.09x faster                                  |
| thrift                     | 823 us                                                     | 754 us: 1.09x faster                                  |
| richards_super             | 57.4 ms                                                    | 52.8 ms: 1.09x faster                                 |
| scimark_fft                | 392 ms                                                     | 361 ms: 1.09x faster                                  |
| async_tree_io_tg           | 936 ms                                                     | 867 ms: 1.08x faster                                  |
| crypto_pyaes               | 77.5 ms                                                    | 71.9 ms: 1.08x faster                                 |
| mdp                        | 2.79 sec                                                   | 2.60 sec: 1.07x faster                                |
| logging_format             | 6.47 us                                                    | 6.06 us: 1.07x faster                                 |
| pathlib                    | 17.3 ms                                                    | 16.2 ms: 1.07x faster                                 |
| scimark_lu                 | 122 ms                                                     | 114 ms: 1.06x faster                                  |
| bench_thread_pool          | 834 us                                                     | 785 us: 1.06x faster                                  |
| generators                 | 29.6 ms                                                    | 27.9 ms: 1.06x faster                                 |
| html5lib                   | 67.2 ms                                                    | 63.5 ms: 1.06x faster                                 |
| asyncio_tcp                | 508 ms                                                     | 480 ms: 1.06x faster                                  |
| regex_compile              | 137 ms                                                     | 130 ms: 1.05x faster                                  |
| xml_etree_parse            | 162 ms                                                     | 153 ms: 1.05x faster                                  |
| logging_simple             | 5.74 us                                                    | 5.45 us: 1.05x faster                                 |
| tornado_http               | 94.6 ms                                                    | 90.2 ms: 1.05x faster                                 |
| spectral_norm              | 116 ms                                                     | 111 ms: 1.05x faster                                  |
| 2to3                       | 274 ms                                                     | 262 ms: 1.05x faster                                  |
| logging_silent             | 105 ns                                                     | 100 ns: 1.04x faster                                  |
| sympy_sum                  | 156 ms                                                     | 150 ms: 1.04x faster                                  |
| create_gc_cycles           | 1.82 ms                                                    | 1.74 ms: 1.04x faster                                 |
| sympy_str                  | 282 ms                                                     | 271 ms: 1.04x faster                                  |
| async_tree_io              | 939 ms                                                     | 903 ms: 1.04x faster                                  |
| sqlglot_transpile          | 1.63 ms                                                    | 1.57 ms: 1.04x faster                                 |
| bpe_tokeniser              | 5.02 sec                                                   | 4.84 sec: 1.04x faster                                |
| docutils                   | 2.83 sec                                                   | 2.72 sec: 1.04x faster                                |
| sympy_integrate            | 20.5 ms                                                    | 19.8 ms: 1.03x faster                                 |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.78 sec: 1.03x faster                                |
| chaos                      | 61.3 ms                                                    | 59.3 ms: 1.03x faster                                 |
| gc_traversal               | 3.98 ms                                                    | 3.85 ms: 1.03x faster                                 |
| sqlglot_optimize           | 55.5 ms                                                    | 53.7 ms: 1.03x faster                                 |
| sympy_expand               | 473 ms                                                     | 458 ms: 1.03x faster                                  |
| sqlglot_parse              | 1.32 ms                                                    | 1.28 ms: 1.03x faster                                 |
| deltablue                  | 3.25 ms                                                    | 3.16 ms: 1.03x faster                                 |
| django_template            | 34.8 ms                                                    | 33.8 ms: 1.03x faster                                 |
| telco                      | 8.41 ms                                                    | 8.18 ms: 1.03x faster                                 |
| hexiom                     | 6.30 ms                                                    | 6.13 ms: 1.03x faster                                 |
| xml_etree_process          | 61.2 ms                                                    | 59.6 ms: 1.03x faster                                 |
| meteor_contest             | 110 ms                                                     | 107 ms: 1.03x faster                                  |
| pyflate                    | 484 ms                                                     | 472 ms: 1.03x faster                                  |
| pprint_safe_repr           | 758 ms                                                     | 740 ms: 1.02x faster                                  |
| pidigits                   | 191 ms                                                     | 187 ms: 1.02x faster                                  |
| tomli_loads                | 2.12 sec                                                   | 2.07 sec: 1.02x faster                                |
| sqlglot_normalize          | 110 ms                                                     | 108 ms: 1.02x faster                                  |
| pprint_pformat             | 1.56 sec                                                   | 1.52 sec: 1.02x faster                                |
| regex_effbot               | 3.67 ms                                                    | 3.59 ms: 1.02x faster                                 |
| xml_etree_iterparse        | 107 ms                                                     | 105 ms: 1.02x faster                                  |
| pycparser                  | 1.16 sec                                                   | 1.14 sec: 1.02x faster                                |
| python_startup             | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                 |
| async_generators           | 442 ms                                                     | 433 ms: 1.02x faster                                  |
| json_dumps                 | 10.7 ms                                                    | 10.5 ms: 1.02x faster                                 |
| comprehensions             | 16.6 us                                                    | 16.3 us: 1.02x faster                                 |
| scimark_sor                | 127 ms                                                     | 125 ms: 1.02x faster                                  |
| nqueens                    | 81.4 ms                                                    | 80.1 ms: 1.02x faster                                 |
| xml_etree_generate         | 87.4 ms                                                    | 86.1 ms: 1.02x faster                                 |
| unpickle_pure_python       | 218 us                                                     | 215 us: 1.02x faster                                  |
| json_loads                 | 28.9 us                                                    | 28.4 us: 1.02x faster                                 |
| scimark_monte_carlo        | 69.2 ms                                                    | 68.3 ms: 1.01x faster                                 |
| raytrace                   | 267 ms                                                     | 263 ms: 1.01x faster                                  |
| asyncio_websockets         | 567 ms                                                     | 560 ms: 1.01x faster                                  |
| regex_v8                   | 25.1 ms                                                    | 24.9 ms: 1.01x faster                                 |
| float                      | 78.9 ms                                                    | 78.3 ms: 1.01x faster                                 |
| pickle_pure_python         | 305 us                                                     | 303 us: 1.01x faster                                  |
| genshi_text                | 23.7 ms                                                    | 23.5 ms: 1.01x faster                                 |
| nbody                      | 88.3 ms                                                    | 87.7 ms: 1.01x faster                                 |
| genshi_xml                 | 51.6 ms                                                    | 51.3 ms: 1.01x faster                                 |
| coroutines                 | 23.2 ms                                                    | 23.1 ms: 1.00x faster                                 |
| python_startup_no_site     | 7.11 ms                                                    | 7.09 ms: 1.00x faster                                 |
| mako                       | 11.2 ms                                                    | 11.3 ms: 1.00x slower                                 |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                 |
| regex_dna                  | 221 ms                                                     | 223 ms: 1.01x slower                                  |
| go                         | 145 ms                                                     | 146 ms: 1.01x slower                                  |
| Geometric mean             | (ref)                                                      | 1.05x faster                                          |

Benchmark hidden because not significant (4): typing_runtime_protocols, pylint, json, fannkuch
Ignored benchmarks (14) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.01x