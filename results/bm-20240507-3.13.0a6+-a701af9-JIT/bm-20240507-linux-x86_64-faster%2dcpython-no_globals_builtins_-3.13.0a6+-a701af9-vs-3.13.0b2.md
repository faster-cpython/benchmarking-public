# Results vs. 3.13.0b2

- fork: faster-cpython
- ref: no_globals_builtins_
- machine: linux-x86_64
- commit hash: a701af9
- commit date: 2024-05-07
- overall geometric mean: 1.03x slower
- HPT reliability: 86.58%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240507-linux-x86_64-faster%2dcpython-no_globals_builtins_-3.13.0a6+-a701af9 |
|----------------|:----------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 281 ms: 1.02x slower                                                             |
| chameleon      | 7.22 ms                                                    | 7.11 ms: 1.02x faster                                                            |
| docutils       | 2.83 sec                                                   | 3.00 sec: 1.06x slower                                                           |
| html5lib       | 67.2 ms                                                    | 68.7 ms: 1.02x slower                                                            |
| tornado_http   | 94.6 ms                                                    | 97.5 ms: 1.03x slower                                                            |
| Geometric mean | (ref)                                                      | 1.02x slower                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240507-linux-x86_64-faster%2dcpython-no_globals_builtins_-3.13.0a6+-a701af9 |
|-------------------------|:----------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_none_tg      | 336 ms                                                     | 348 ms: 1.04x slower                                                             |
| async_tree_cpu_io_mixed | 611 ms                                                     | 633 ms: 1.04x slower                                                             |
| async_tree_memoization  | 463 ms                                                     | 486 ms: 1.05x slower                                                             |
| async_tree_io_tg        | 936 ms                                                     | 1.03 sec: 1.10x slower                                                           |
| Geometric mean          | (ref)                                                      | 1.03x slower                                                                     |

Benchmark hidden because not significant (4): async_tree_none, async_tree_io, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240507-linux-x86_64-faster%2dcpython-no_globals_builtins_-3.13.0a6+-a701af9 |
|----------------|:----------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 71.7 ms: 1.10x faster                                                            |
| nbody          | 88.3 ms                                                    | 81.2 ms: 1.09x faster                                                            |
| pidigits       | 191 ms                                                     | 188 ms: 1.02x faster                                                             |
| Geometric mean | (ref)                                                      | 1.07x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240507-linux-x86_64-faster%2dcpython-no_globals_builtins_-3.13.0a6+-a701af9 |
|----------------|:----------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                    | 3.73 ms: 1.02x slower                                                            |
| regex_v8       | 25.1 ms                                                    | 25.7 ms: 1.02x slower                                                            |
| regex_compile  | 137 ms                                                     | 140 ms: 1.02x slower                                                             |
| regex_dna      | 221 ms                                                     | 228 ms: 1.03x slower                                                             |
| Geometric mean | (ref)                                                      | 1.02x slower                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240507-linux-x86_64-faster%2dcpython-no_globals_builtins_-3.13.0a6+-a701af9 |
|----------------------|:----------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                                   | 1.98 sec: 1.07x faster                                                           |
| xml_etree_iterparse  | 107 ms                                                     | 101 ms: 1.06x faster                                                             |
| xml_etree_parse      | 162 ms                                                     | 154 ms: 1.05x faster                                                             |
| pickle_dict          | 34.8 us                                                    | 33.1 us: 1.05x faster                                                            |
| json_dumps           | 10.7 ms                                                    | 10.3 ms: 1.05x faster                                                            |
| xml_etree_generate   | 87.4 ms                                                    | 83.7 ms: 1.04x faster                                                            |
| xml_etree_process    | 61.2 ms                                                    | 58.9 ms: 1.04x faster                                                            |
| pickle_pure_python   | 305 us                                                     | 301 us: 1.01x faster                                                             |
| pickle_list          | 5.11 us                                                    | 5.05 us: 1.01x faster                                                            |
| unpickle_list        | 5.34 us                                                    | 5.30 us: 1.01x faster                                                            |
| unpickle_pure_python | 218 us                                                     | 222 us: 1.02x slower                                                             |
| unpickle             | 15.1 us                                                    | 15.7 us: 1.04x slower                                                            |
| pickle               | 11.5 us                                                    | 12.0 us: 1.05x slower                                                            |
| Geometric mean       | (ref)                                                      | 1.02x faster                                                                     |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240507-linux-x86_64-faster%2dcpython-no_globals_builtins_-3.13.0a6+-a701af9 |
|------------------------|:----------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 11.2 ms: 1.04x slower                                                            |
| python_startup_no_site | 7.11 ms                                                    | 7.65 ms: 1.08x slower                                                            |
| Geometric mean         | (ref)                                                      | 1.06x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240507-linux-x86_64-faster%2dcpython-no_globals_builtins_-3.13.0a6+-a701af9 |
|-----------------|:----------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.60 ms: 1.17x faster                                                            |
| django_template | 34.8 ms                                                    | 36.9 ms: 1.06x slower                                                            |
| genshi_text     | 23.7 ms                                                    | 25.1 ms: 1.06x slower                                                            |
| genshi_xml      | 51.6 ms                                                    | 59.0 ms: 1.14x slower                                                            |
| Geometric mean  | (ref)                                                      | 1.02x slower                                                                     |

All benchmarks:
===============

| Benchmark                | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240507-linux-x86_64-faster%2dcpython-no_globals_builtins_-3.13.0a6+-a701af9 |
|--------------------------|:----------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| scimark_fft              | 392 ms                                                     | 316 ms: 1.24x faster                                                             |
| richards                 | 50.9 ms                                                    | 43.1 ms: 1.18x faster                                                            |
| mako                     | 11.2 ms                                                    | 9.60 ms: 1.17x faster                                                            |
| richards_super           | 57.4 ms                                                    | 49.5 ms: 1.16x faster                                                            |
| spectral_norm            | 116 ms                                                     | 100 ms: 1.16x faster                                                             |
| scimark_sparse_mat_mult  | 5.27 ms                                                    | 4.57 ms: 1.15x faster                                                            |
| crypto_pyaes             | 77.5 ms                                                    | 68.2 ms: 1.14x faster                                                            |
| float                    | 78.9 ms                                                    | 71.7 ms: 1.10x faster                                                            |
| fannkuch                 | 402 ms                                                     | 369 ms: 1.09x faster                                                             |
| nbody                    | 88.3 ms                                                    | 81.2 ms: 1.09x faster                                                            |
| coverage                 | 93.1 ms                                                    | 86.3 ms: 1.08x faster                                                            |
| scimark_monte_carlo      | 69.2 ms                                                    | 64.2 ms: 1.08x faster                                                            |
| tomli_loads              | 2.12 sec                                                   | 1.98 sec: 1.07x faster                                                           |
| pyflate                  | 484 ms                                                     | 453 ms: 1.07x faster                                                             |
| deepcopy_memo            | 39.7 us                                                    | 37.2 us: 1.07x faster                                                            |
| mdp                      | 2.79 sec                                                   | 2.61 sec: 1.07x faster                                                           |
| xml_etree_iterparse      | 107 ms                                                     | 101 ms: 1.06x faster                                                             |
| xml_etree_parse          | 162 ms                                                     | 154 ms: 1.05x faster                                                             |
| sqlite_synth             | 2.99 us                                                    | 2.84 us: 1.05x faster                                                            |
| pickle_dict              | 34.8 us                                                    | 33.1 us: 1.05x faster                                                            |
| json_dumps               | 10.7 ms                                                    | 10.3 ms: 1.05x faster                                                            |
| xml_etree_generate       | 87.4 ms                                                    | 83.7 ms: 1.04x faster                                                            |
| pprint_safe_repr         | 758 ms                                                     | 727 ms: 1.04x faster                                                             |
| xml_etree_process        | 61.2 ms                                                    | 58.9 ms: 1.04x faster                                                            |
| deepcopy_reduce          | 3.35 us                                                    | 3.23 us: 1.04x faster                                                            |
| gc_traversal             | 3.98 ms                                                    | 3.84 ms: 1.03x faster                                                            |
| chaos                    | 61.3 ms                                                    | 59.3 ms: 1.03x faster                                                            |
| pprint_pformat           | 1.56 sec                                                   | 1.52 sec: 1.03x faster                                                           |
| pidigits                 | 191 ms                                                     | 188 ms: 1.02x faster                                                             |
| thrift                   | 823 us                                                     | 809 us: 1.02x faster                                                             |
| chameleon                | 7.22 ms                                                    | 7.11 ms: 1.02x faster                                                            |
| pickle_pure_python       | 305 us                                                     | 301 us: 1.01x faster                                                             |
| logging_format           | 6.47 us                                                    | 6.40 us: 1.01x faster                                                            |
| pickle_list              | 5.11 us                                                    | 5.05 us: 1.01x faster                                                            |
| sqlglot_parse            | 1.32 ms                                                    | 1.31 ms: 1.01x faster                                                            |
| unpickle_list            | 5.34 us                                                    | 5.30 us: 1.01x faster                                                            |
| coroutines               | 23.2 ms                                                    | 23.1 ms: 1.01x faster                                                            |
| create_gc_cycles         | 1.82 ms                                                    | 1.82 ms: 1.00x slower                                                            |
| asyncio_websockets       | 567 ms                                                     | 570 ms: 1.01x slower                                                             |
| meteor_contest           | 110 ms                                                     | 110 ms: 1.01x slower                                                             |
| asyncio_tcp_ssl          | 1.84 sec                                                   | 1.86 sec: 1.01x slower                                                           |
| deepcopy                 | 367 us                                                     | 370 us: 1.01x slower                                                             |
| logging_silent           | 105 ns                                                     | 106 ns: 1.01x slower                                                             |
| logging_simple           | 5.74 us                                                    | 5.81 us: 1.01x slower                                                            |
| comprehensions           | 16.6 us                                                    | 16.8 us: 1.01x slower                                                            |
| regex_effbot             | 3.67 ms                                                    | 3.73 ms: 1.02x slower                                                            |
| pathlib                  | 17.3 ms                                                    | 17.6 ms: 1.02x slower                                                            |
| unpickle_pure_python     | 218 us                                                     | 222 us: 1.02x slower                                                             |
| scimark_sor              | 127 ms                                                     | 130 ms: 1.02x slower                                                             |
| html5lib                 | 67.2 ms                                                    | 68.7 ms: 1.02x slower                                                            |
| asyncio_tcp              | 508 ms                                                     | 519 ms: 1.02x slower                                                             |
| regex_v8                 | 25.1 ms                                                    | 25.7 ms: 1.02x slower                                                            |
| scimark_lu               | 122 ms                                                     | 124 ms: 1.02x slower                                                             |
| generators               | 29.6 ms                                                    | 30.3 ms: 1.02x slower                                                            |
| 2to3                     | 274 ms                                                     | 281 ms: 1.02x slower                                                             |
| regex_compile            | 137 ms                                                     | 140 ms: 1.02x slower                                                             |
| sqlglot_optimize         | 55.5 ms                                                    | 56.9 ms: 1.02x slower                                                            |
| go                       | 145 ms                                                     | 148 ms: 1.03x slower                                                             |
| dask                     | 369 ms                                                     | 380 ms: 1.03x slower                                                             |
| regex_dna                | 221 ms                                                     | 228 ms: 1.03x slower                                                             |
| tornado_http             | 94.6 ms                                                    | 97.5 ms: 1.03x slower                                                            |
| djangocms                | 31.5 us                                                    | 32.5 us: 1.03x slower                                                            |
| flaskblogging            | 9.01 ms                                                    | 9.31 ms: 1.03x slower                                                            |
| async_tree_none_tg       | 336 ms                                                     | 348 ms: 1.04x slower                                                             |
| async_tree_cpu_io_mixed  | 611 ms                                                     | 633 ms: 1.04x slower                                                             |
| python_startup           | 10.8 ms                                                    | 11.2 ms: 1.04x slower                                                            |
| unpickle                 | 15.1 us                                                    | 15.7 us: 1.04x slower                                                            |
| bench_thread_pool        | 834 us                                                     | 869 us: 1.04x slower                                                             |
| sqlglot_normalize        | 110 ms                                                     | 115 ms: 1.04x slower                                                             |
| dulwich_log              | 67.2 ms                                                    | 70.1 ms: 1.04x slower                                                            |
| hexiom                   | 6.30 ms                                                    | 6.58 ms: 1.04x slower                                                            |
| pycparser                | 1.16 sec                                                   | 1.21 sec: 1.05x slower                                                           |
| raytrace                 | 267 ms                                                     | 279 ms: 1.05x slower                                                             |
| pickle                   | 11.5 us                                                    | 12.0 us: 1.05x slower                                                            |
| async_tree_memoization   | 463 ms                                                     | 486 ms: 1.05x slower                                                             |
| async_generators         | 442 ms                                                     | 465 ms: 1.05x slower                                                             |
| gunicorn                 | 1.28 ms                                                    | 1.35 ms: 1.06x slower                                                            |
| typing_runtime_protocols | 165 us                                                     | 174 us: 1.06x slower                                                             |
| django_template          | 34.8 ms                                                    | 36.9 ms: 1.06x slower                                                            |
| docutils                 | 2.83 sec                                                   | 3.00 sec: 1.06x slower                                                           |
| aiohttp                  | 1.18 ms                                                    | 1.25 ms: 1.06x slower                                                            |
| genshi_text              | 23.7 ms                                                    | 25.1 ms: 1.06x slower                                                            |
| sympy_str                | 282 ms                                                     | 300 ms: 1.06x slower                                                             |
| nqueens                  | 81.4 ms                                                    | 86.7 ms: 1.06x slower                                                            |
| python_startup_no_site   | 7.11 ms                                                    | 7.65 ms: 1.08x slower                                                            |
| sympy_expand             | 473 ms                                                     | 511 ms: 1.08x slower                                                             |
| async_tree_io_tg         | 936 ms                                                     | 1.03 sec: 1.10x slower                                                           |
| mypy2                    | 742 ms                                                     | 820 ms: 1.11x slower                                                             |
| sympy_integrate          | 20.5 ms                                                    | 22.7 ms: 1.11x slower                                                            |
| sympy_sum                | 156 ms                                                     | 173 ms: 1.11x slower                                                             |
| pylint                   | 317 ms                                                     | 357 ms: 1.13x slower                                                             |
| genshi_xml               | 51.6 ms                                                    | 59.0 ms: 1.14x slower                                                            |
| deltablue                | 3.25 ms                                                    | 3.76 ms: 1.16x slower                                                            |
| telco                    | 8.41 ms                                                    | 172 ms: 20.39x slower                                                            |
| Geometric mean           | (ref)                                                      | 1.03x slower                                                                     |

Benchmark hidden because not significant (8): async_tree_none, json, json_loads, sqlglot_transpile, bench_mp_pool, async_tree_io, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg
Ignored benchmarks (1) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: bpe_tokeniser

# HPT report

- Reliability score: 86.58% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.08x