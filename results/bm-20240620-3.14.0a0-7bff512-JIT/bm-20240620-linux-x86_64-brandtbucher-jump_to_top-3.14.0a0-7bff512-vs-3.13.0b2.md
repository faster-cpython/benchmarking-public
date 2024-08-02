# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: jump_to_top
- machine: linux-x86_64
- commit hash: 7bff512
- commit date: 2024-06-20
- overall geometric mean: 1.03x faster
- HPT reliability: 99.81%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240620-linux-x86_64-brandtbucher-jump_to_top-3.14.0a0-7bff512 |
|----------------|:----------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 273 ms: 1.01x faster                                               |
| html5lib       | 67.2 ms                                                    | 66.7 ms: 1.01x faster                                              |
| tornado_http   | 94.6 ms                                                    | 93.3 ms: 1.01x faster                                              |
| Geometric mean | (ref)                                                      | 1.01x faster                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240620-linux-x86_64-brandtbucher-jump_to_top-3.14.0a0-7bff512 |
|----------------------------|:----------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 366 ms: 1.04x faster                                               |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 570 ms: 1.03x faster                                               |
| async_tree_io_tg           | 936 ms                                                     | 986 ms: 1.05x slower                                               |
| Geometric mean             | (ref)                                                      | 1.00x slower                                                       |

Benchmark hidden because not significant (5): async_tree_io, async_tree_none_tg, async_tree_cpu_io_mixed, async_tree_memoization_tg, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240620-linux-x86_64-brandtbucher-jump_to_top-3.14.0a0-7bff512 |
|----------------|:----------------------------------------------------------:|:------------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 70.2 ms: 1.12x faster                                              |
| nbody          | 88.3 ms                                                    | 79.2 ms: 1.11x faster                                              |
| pidigits       | 191 ms                                                     | 185 ms: 1.03x faster                                               |
| Geometric mean | (ref)                                                      | 1.09x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240620-linux-x86_64-brandtbucher-jump_to_top-3.14.0a0-7bff512 |
|----------------|:----------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                     | 135 ms: 1.01x faster                                               |
| regex_dna      | 221 ms                                                     | 227 ms: 1.03x slower                                               |
| regex_effbot   | 3.67 ms                                                    | 3.85 ms: 1.05x slower                                              |
| regex_v8       | 25.1 ms                                                    | 26.8 ms: 1.07x slower                                              |
| Geometric mean | (ref)                                                      | 1.03x slower                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240620-linux-x86_64-brandtbucher-jump_to_top-3.14.0a0-7bff512 |
|---------------------|:----------------------------------------------------------:|:------------------------------------------------------------------:|
| tomli_loads         | 2.12 sec                                                   | 1.91 sec: 1.11x faster                                             |
| xml_etree_parse     | 162 ms                                                     | 147 ms: 1.10x faster                                               |
| xml_etree_generate  | 87.4 ms                                                    | 80.4 ms: 1.09x faster                                              |
| xml_etree_iterparse | 107 ms                                                     | 99.5 ms: 1.08x faster                                              |
| xml_etree_process   | 61.2 ms                                                    | 57.6 ms: 1.06x faster                                              |
| pickle_pure_python  | 305 us                                                     | 290 us: 1.05x faster                                               |
| unpickle            | 15.1 us                                                    | 14.4 us: 1.05x faster                                              |
| json_dumps          | 10.7 ms                                                    | 10.5 ms: 1.02x faster                                              |
| unpickle_list       | 5.34 us                                                    | 5.28 us: 1.01x faster                                              |
| pickle_dict         | 34.8 us                                                    | 35.5 us: 1.02x slower                                              |
| pickle              | 11.5 us                                                    | 11.9 us: 1.04x slower                                              |
| pickle_list         | 5.11 us                                                    | 5.31 us: 1.04x slower                                              |
| Geometric mean      | (ref)                                                      | 1.03x faster                                                       |

Benchmark hidden because not significant (2): json_loads, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240620-linux-x86_64-brandtbucher-jump_to_top-3.14.0a0-7bff512 |
|------------------------|:----------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.8 ms: 1.01x slower                                              |
| python_startup_no_site | 7.11 ms                                                    | 7.39 ms: 1.04x slower                                              |
| Geometric mean         | (ref)                                                      | 1.02x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240620-linux-x86_64-brandtbucher-jump_to_top-3.14.0a0-7bff512 |
|-----------------|:----------------------------------------------------------:|:------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.63 ms: 1.17x faster                                              |
| genshi_text     | 23.7 ms                                                    | 24.5 ms: 1.04x slower                                              |
| django_template | 34.8 ms                                                    | 36.6 ms: 1.05x slower                                              |
| genshi_xml      | 51.6 ms                                                    | 56.5 ms: 1.09x slower                                              |
| Geometric mean  | (ref)                                                      | 1.01x slower                                                       |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240620-linux-x86_64-brandtbucher-jump_to_top-3.14.0a0-7bff512 |
|----------------------------|:----------------------------------------------------------:|:------------------------------------------------------------------:|
| deepcopy_memo              | 39.7 us                                                    | 28.6 us: 1.39x faster                                              |
| deepcopy                   | 367 us                                                     | 275 us: 1.33x faster                                               |
| scimark_fft                | 392 ms                                                     | 317 ms: 1.24x faster                                               |
| richards                   | 50.9 ms                                                    | 41.9 ms: 1.22x faster                                              |
| richards_super             | 57.4 ms                                                    | 48.0 ms: 1.20x faster                                              |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.41 ms: 1.19x faster                                              |
| deepcopy_reduce            | 3.35 us                                                    | 2.83 us: 1.18x faster                                              |
| mako                       | 11.2 ms                                                    | 9.63 ms: 1.17x faster                                              |
| crypto_pyaes               | 77.5 ms                                                    | 67.0 ms: 1.16x faster                                              |
| fannkuch                   | 402 ms                                                     | 353 ms: 1.14x faster                                               |
| float                      | 78.9 ms                                                    | 70.2 ms: 1.12x faster                                              |
| scimark_monte_carlo        | 69.2 ms                                                    | 61.6 ms: 1.12x faster                                              |
| nbody                      | 88.3 ms                                                    | 79.2 ms: 1.11x faster                                              |
| spectral_norm              | 116 ms                                                     | 104 ms: 1.11x faster                                               |
| gc_traversal               | 3.98 ms                                                    | 3.59 ms: 1.11x faster                                              |
| tomli_loads                | 2.12 sec                                                   | 1.91 sec: 1.11x faster                                             |
| mdp                        | 2.79 sec                                                   | 2.53 sec: 1.10x faster                                             |
| xml_etree_parse            | 162 ms                                                     | 147 ms: 1.10x faster                                               |
| xml_etree_generate         | 87.4 ms                                                    | 80.4 ms: 1.09x faster                                              |
| pyflate                    | 484 ms                                                     | 447 ms: 1.08x faster                                               |
| xml_etree_iterparse        | 107 ms                                                     | 99.5 ms: 1.08x faster                                              |
| logging_format             | 6.47 us                                                    | 5.99 us: 1.08x faster                                              |
| pathlib                    | 17.3 ms                                                    | 16.1 ms: 1.07x faster                                              |
| sqlite_synth               | 2.99 us                                                    | 2.80 us: 1.07x faster                                              |
| telco                      | 8.41 ms                                                    | 7.87 ms: 1.07x faster                                              |
| pprint_safe_repr           | 758 ms                                                     | 710 ms: 1.07x faster                                               |
| xml_etree_process          | 61.2 ms                                                    | 57.6 ms: 1.06x faster                                              |
| pickle_pure_python         | 305 us                                                     | 290 us: 1.05x faster                                               |
| logging_simple             | 5.74 us                                                    | 5.46 us: 1.05x faster                                              |
| pprint_pformat             | 1.56 sec                                                   | 1.48 sec: 1.05x faster                                             |
| unpickle                   | 15.1 us                                                    | 14.4 us: 1.05x faster                                              |
| create_gc_cycles           | 1.82 ms                                                    | 1.74 ms: 1.04x faster                                              |
| asyncio_tcp                | 508 ms                                                     | 490 ms: 1.04x faster                                               |
| bpe_tokeniser              | 5.02 sec                                                   | 4.84 sec: 1.04x faster                                             |
| chaos                      | 61.3 ms                                                    | 59.2 ms: 1.04x faster                                              |
| async_tree_none            | 378 ms                                                     | 366 ms: 1.04x faster                                               |
| pidigits                   | 191 ms                                                     | 185 ms: 1.03x faster                                               |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 570 ms: 1.03x faster                                               |
| meteor_contest             | 110 ms                                                     | 107 ms: 1.03x faster                                               |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.79 sec: 1.03x faster                                             |
| thrift                     | 823 us                                                     | 804 us: 1.02x faster                                               |
| json_dumps                 | 10.7 ms                                                    | 10.5 ms: 1.02x faster                                              |
| sqlglot_parse              | 1.32 ms                                                    | 1.29 ms: 1.02x faster                                              |
| asyncio_websockets         | 567 ms                                                     | 556 ms: 1.02x faster                                               |
| dask                       | 369 ms                                                     | 363 ms: 1.02x faster                                               |
| sqlglot_transpile          | 1.63 ms                                                    | 1.61 ms: 1.02x faster                                              |
| regex_compile              | 137 ms                                                     | 135 ms: 1.01x faster                                               |
| pycparser                  | 1.16 sec                                                   | 1.14 sec: 1.01x faster                                             |
| tornado_http               | 94.6 ms                                                    | 93.3 ms: 1.01x faster                                              |
| comprehensions             | 16.6 us                                                    | 16.4 us: 1.01x faster                                              |
| unpickle_list              | 5.34 us                                                    | 5.28 us: 1.01x faster                                              |
| html5lib                   | 67.2 ms                                                    | 66.7 ms: 1.01x faster                                              |
| bench_thread_pool          | 834 us                                                     | 827 us: 1.01x faster                                               |
| 2to3                       | 274 ms                                                     | 273 ms: 1.01x faster                                               |
| go                         | 145 ms                                                     | 145 ms: 1.01x slower                                               |
| python_startup             | 10.8 ms                                                    | 10.8 ms: 1.01x slower                                              |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                              |
| coverage                   | 93.1 ms                                                    | 94.1 ms: 1.01x slower                                              |
| scimark_lu                 | 122 ms                                                     | 123 ms: 1.01x slower                                               |
| typing_runtime_protocols   | 165 us                                                     | 167 us: 1.02x slower                                               |
| raytrace                   | 267 ms                                                     | 271 ms: 1.02x slower                                               |
| logging_silent             | 105 ns                                                     | 107 ns: 1.02x slower                                               |
| sqlglot_normalize          | 110 ms                                                     | 112 ms: 1.02x slower                                               |
| pickle_dict                | 34.8 us                                                    | 35.5 us: 1.02x slower                                              |
| scimark_sor                | 127 ms                                                     | 131 ms: 1.03x slower                                               |
| regex_dna                  | 221 ms                                                     | 227 ms: 1.03x slower                                               |
| hexiom                     | 6.30 ms                                                    | 6.51 ms: 1.03x slower                                              |
| pickle                     | 11.5 us                                                    | 11.9 us: 1.04x slower                                              |
| genshi_text                | 23.7 ms                                                    | 24.5 ms: 1.04x slower                                              |
| python_startup_no_site     | 7.11 ms                                                    | 7.39 ms: 1.04x slower                                              |
| pickle_list                | 5.11 us                                                    | 5.31 us: 1.04x slower                                              |
| sympy_str                  | 282 ms                                                     | 294 ms: 1.04x slower                                               |
| coroutines                 | 23.2 ms                                                    | 24.2 ms: 1.04x slower                                              |
| async_generators           | 442 ms                                                     | 462 ms: 1.04x slower                                               |
| regex_effbot               | 3.67 ms                                                    | 3.85 ms: 1.05x slower                                              |
| nqueens                    | 81.4 ms                                                    | 85.4 ms: 1.05x slower                                              |
| django_template            | 34.8 ms                                                    | 36.6 ms: 1.05x slower                                              |
| async_tree_io_tg           | 936 ms                                                     | 986 ms: 1.05x slower                                               |
| sympy_expand               | 473 ms                                                     | 499 ms: 1.06x slower                                               |
| sympy_sum                  | 156 ms                                                     | 165 ms: 1.06x slower                                               |
| regex_v8                   | 25.1 ms                                                    | 26.8 ms: 1.07x slower                                              |
| pylint                     | 317 ms                                                     | 341 ms: 1.07x slower                                               |
| sympy_integrate            | 20.5 ms                                                    | 22.0 ms: 1.07x slower                                              |
| deltablue                  | 3.25 ms                                                    | 3.52 ms: 1.08x slower                                              |
| genshi_xml                 | 51.6 ms                                                    | 56.5 ms: 1.09x slower                                              |
| Geometric mean             | (ref)                                                      | 1.03x faster                                                       |

Benchmark hidden because not significant (11): async_tree_io, async_tree_none_tg, json_loads, generators, json, dulwich_log, async_tree_cpu_io_mixed, unpickle_pure_python, sqlglot_optimize, async_tree_memoization_tg, async_tree_memoization
Ignored benchmarks (7) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, djangocms, docutils, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 99.81% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.09x