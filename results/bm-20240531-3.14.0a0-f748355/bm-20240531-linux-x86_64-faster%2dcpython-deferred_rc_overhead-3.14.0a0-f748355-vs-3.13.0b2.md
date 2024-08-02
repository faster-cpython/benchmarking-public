# Results vs. 3.13.0b2

- fork: faster-cpython
- ref: deferred_rc_overhead
- machine: linux-x86_64
- commit hash: f748355
- commit date: 2024-05-31
- overall geometric mean: 1.01x faster
- HPT reliability: 99.94%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240531-linux-x86_64-faster%2dcpython-deferred_rc_overhead-3.14.0a0-f748355 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 270 ms: 1.01x faster                                                            |
| docutils       | 2.83 sec                                                   | 2.79 sec: 1.01x faster                                                          |
| tornado_http   | 94.6 ms                                                    | 93.9 ms: 1.01x faster                                                           |
| Geometric mean | (ref)                                                      | 1.01x faster                                                                    |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark          | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240531-linux-x86_64-faster%2dcpython-deferred_rc_overhead-3.14.0a0-f748355 |
|--------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none_tg | 336 ms                                                     | 350 ms: 1.04x slower                                                            |
| Geometric mean     | (ref)                                                      | 1.01x slower                                                                    |

Benchmark hidden because not significant (7): async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_io, async_tree_memoization, async_tree_cpu_io_mixed, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240531-linux-x86_64-faster%2dcpython-deferred_rc_overhead-3.14.0a0-f748355 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 191 ms                                                     | 189 ms: 1.01x faster                                                            |
| float          | 78.9 ms                                                    | 79.5 ms: 1.01x slower                                                           |
| nbody          | 88.3 ms                                                    | 89.1 ms: 1.01x slower                                                           |
| Geometric mean | (ref)                                                      | 1.00x slower                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240531-linux-x86_64-faster%2dcpython-deferred_rc_overhead-3.14.0a0-f748355 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                     | 134 ms: 1.02x faster                                                            |
| regex_effbot   | 3.67 ms                                                    | 3.62 ms: 1.01x faster                                                           |
| regex_dna      | 221 ms                                                     | 228 ms: 1.03x slower                                                            |
| regex_v8       | 25.1 ms                                                    | 26.0 ms: 1.03x slower                                                           |
| Geometric mean | (ref)                                                      | 1.01x slower                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240531-linux-x86_64-faster%2dcpython-deferred_rc_overhead-3.14.0a0-f748355 |
|---------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_process   | 61.2 ms                                                    | 60.3 ms: 1.01x faster                                                           |
| json_dumps          | 10.7 ms                                                    | 10.6 ms: 1.01x faster                                                           |
| xml_etree_iterparse | 107 ms                                                     | 106 ms: 1.01x faster                                                            |
| pickle_pure_python  | 305 us                                                     | 303 us: 1.01x faster                                                            |
| xml_etree_generate  | 87.4 ms                                                    | 87.1 ms: 1.00x faster                                                           |
| unpickle_list       | 5.34 us                                                    | 5.41 us: 1.01x slower                                                           |
| tomli_loads         | 2.12 sec                                                   | 2.18 sec: 1.03x slower                                                          |
| pickle_dict         | 34.8 us                                                    | 35.9 us: 1.03x slower                                                           |
| pickle_list         | 5.11 us                                                    | 5.30 us: 1.04x slower                                                           |
| pickle              | 11.5 us                                                    | 12.0 us: 1.05x slower                                                           |
| Geometric mean      | (ref)                                                      | 1.01x slower                                                                    |

Benchmark hidden because not significant (4): xml_etree_parse, json_loads, unpickle_pure_python, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240531-linux-x86_64-faster%2dcpython-deferred_rc_overhead-3.14.0a0-f748355 |
|------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                                           |
| python_startup_no_site | 7.11 ms                                                    | 7.07 ms: 1.01x faster                                                           |
| Geometric mean         | (ref)                                                      | 1.01x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240531-linux-x86_64-faster%2dcpython-deferred_rc_overhead-3.14.0a0-f748355 |
|-----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_xml      | 51.6 ms                                                    | 50.6 ms: 1.02x faster                                                           |
| genshi_text     | 23.7 ms                                                    | 23.3 ms: 1.02x faster                                                           |
| django_template | 34.8 ms                                                    | 35.3 ms: 1.01x slower                                                           |
| mako            | 11.2 ms                                                    | 11.7 ms: 1.04x slower                                                           |
| Geometric mean  | (ref)                                                      | 1.00x slower                                                                    |

All benchmarks:
===============

| Benchmark               | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240531-linux-x86_64-faster%2dcpython-deferred_rc_overhead-3.14.0a0-f748355 |
|-------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| gc_traversal            | 3.98 ms                                                    | 3.59 ms: 1.11x faster                                                           |
| mdp                     | 2.79 sec                                                   | 2.58 sec: 1.08x faster                                                          |
| logging_silent          | 105 ns                                                     | 97.2 ns: 1.08x faster                                                           |
| generators              | 29.6 ms                                                    | 27.8 ms: 1.07x faster                                                           |
| pathlib                 | 17.3 ms                                                    | 16.2 ms: 1.07x faster                                                           |
| scimark_fft             | 392 ms                                                     | 374 ms: 1.05x faster                                                            |
| scimark_lu              | 122 ms                                                     | 116 ms: 1.05x faster                                                            |
| richards_super          | 57.4 ms                                                    | 55.2 ms: 1.04x faster                                                           |
| richards                | 50.9 ms                                                    | 49.1 ms: 1.04x faster                                                           |
| pyflate                 | 484 ms                                                     | 467 ms: 1.04x faster                                                            |
| thrift                  | 823 us                                                     | 801 us: 1.03x faster                                                            |
| coroutines              | 23.2 ms                                                    | 22.6 ms: 1.03x faster                                                           |
| logging_format          | 6.47 us                                                    | 6.31 us: 1.02x faster                                                           |
| scimark_sparse_mat_mult | 5.27 ms                                                    | 5.15 ms: 1.02x faster                                                           |
| genshi_xml              | 51.6 ms                                                    | 50.6 ms: 1.02x faster                                                           |
| crypto_pyaes            | 77.5 ms                                                    | 75.9 ms: 1.02x faster                                                           |
| dulwich_log             | 67.2 ms                                                    | 65.8 ms: 1.02x faster                                                           |
| regex_compile           | 137 ms                                                     | 134 ms: 1.02x faster                                                            |
| python_startup          | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                                           |
| create_gc_cycles        | 1.82 ms                                                    | 1.78 ms: 1.02x faster                                                           |
| genshi_text             | 23.7 ms                                                    | 23.3 ms: 1.02x faster                                                           |
| scimark_sor             | 127 ms                                                     | 126 ms: 1.02x faster                                                            |
| regex_effbot            | 3.67 ms                                                    | 3.62 ms: 1.01x faster                                                           |
| xml_etree_process       | 61.2 ms                                                    | 60.3 ms: 1.01x faster                                                           |
| hexiom                  | 6.30 ms                                                    | 6.21 ms: 1.01x faster                                                           |
| docutils                | 2.83 sec                                                   | 2.79 sec: 1.01x faster                                                          |
| 2to3                    | 274 ms                                                     | 270 ms: 1.01x faster                                                            |
| sqlite_synth            | 2.99 us                                                    | 2.95 us: 1.01x faster                                                           |
| pidigits                | 191 ms                                                     | 189 ms: 1.01x faster                                                            |
| logging_simple          | 5.74 us                                                    | 5.68 us: 1.01x faster                                                           |
| deepcopy_memo           | 39.7 us                                                    | 39.3 us: 1.01x faster                                                           |
| deepcopy_reduce         | 3.35 us                                                    | 3.31 us: 1.01x faster                                                           |
| json_dumps              | 10.7 ms                                                    | 10.6 ms: 1.01x faster                                                           |
| sqlglot_transpile       | 1.63 ms                                                    | 1.62 ms: 1.01x faster                                                           |
| pprint_pformat          | 1.56 sec                                                   | 1.54 sec: 1.01x faster                                                          |
| xml_etree_iterparse     | 107 ms                                                     | 106 ms: 1.01x faster                                                            |
| coverage                | 93.1 ms                                                    | 92.3 ms: 1.01x faster                                                           |
| pickle_pure_python      | 305 us                                                     | 303 us: 1.01x faster                                                            |
| sympy_expand            | 473 ms                                                     | 469 ms: 1.01x faster                                                            |
| pprint_safe_repr        | 758 ms                                                     | 752 ms: 1.01x faster                                                            |
| tornado_http            | 94.6 ms                                                    | 93.9 ms: 1.01x faster                                                           |
| chaos                   | 61.3 ms                                                    | 60.9 ms: 1.01x faster                                                           |
| sqlglot_optimize        | 55.5 ms                                                    | 55.1 ms: 1.01x faster                                                           |
| sympy_sum               | 156 ms                                                     | 155 ms: 1.01x faster                                                            |
| raytrace                | 267 ms                                                     | 265 ms: 1.01x faster                                                            |
| asyncio_tcp             | 508 ms                                                     | 505 ms: 1.01x faster                                                            |
| sympy_integrate         | 20.5 ms                                                    | 20.4 ms: 1.01x faster                                                           |
| python_startup_no_site  | 7.11 ms                                                    | 7.07 ms: 1.01x faster                                                           |
| bench_thread_pool       | 834 us                                                     | 830 us: 1.00x faster                                                            |
| xml_etree_generate      | 87.4 ms                                                    | 87.1 ms: 1.00x faster                                                           |
| asyncio_tcp_ssl         | 1.84 sec                                                   | 1.84 sec: 1.00x faster                                                          |
| deepcopy                | 367 us                                                     | 366 us: 1.00x faster                                                            |
| float                   | 78.9 ms                                                    | 79.5 ms: 1.01x slower                                                           |
| nbody                   | 88.3 ms                                                    | 89.1 ms: 1.01x slower                                                           |
| go                      | 145 ms                                                     | 146 ms: 1.01x slower                                                            |
| fannkuch                | 402 ms                                                     | 406 ms: 1.01x slower                                                            |
| async_generators        | 442 ms                                                     | 447 ms: 1.01x slower                                                            |
| nqueens                 | 81.4 ms                                                    | 82.4 ms: 1.01x slower                                                           |
| scimark_monte_carlo     | 69.2 ms                                                    | 70.1 ms: 1.01x slower                                                           |
| unpickle_list           | 5.34 us                                                    | 5.41 us: 1.01x slower                                                           |
| comprehensions          | 16.6 us                                                    | 16.8 us: 1.01x slower                                                           |
| django_template         | 34.8 ms                                                    | 35.3 ms: 1.01x slower                                                           |
| tomli_loads             | 2.12 sec                                                   | 2.18 sec: 1.03x slower                                                          |
| regex_dna               | 221 ms                                                     | 228 ms: 1.03x slower                                                            |
| pickle_dict             | 34.8 us                                                    | 35.9 us: 1.03x slower                                                           |
| regex_v8                | 25.1 ms                                                    | 26.0 ms: 1.03x slower                                                           |
| mako                    | 11.2 ms                                                    | 11.7 ms: 1.04x slower                                                           |
| pickle_list             | 5.11 us                                                    | 5.30 us: 1.04x slower                                                           |
| async_tree_none_tg      | 336 ms                                                     | 350 ms: 1.04x slower                                                            |
| pycparser               | 1.16 sec                                                   | 1.21 sec: 1.05x slower                                                          |
| pickle                  | 11.5 us                                                    | 12.0 us: 1.05x slower                                                           |
| Geometric mean          | (ref)                                                      | 1.01x faster                                                                    |

Benchmark hidden because not significant (24): xml_etree_parse, sympy_str, async_tree_cpu_io_mixed_tg, json_loads, pylint, async_tree_io_tg, sqlglot_normalize, sqlglot_parse, asyncio_websockets, spectral_norm, json, bench_mp_pool, unpickle_pure_python, html5lib, typing_runtime_protocols, telco, deltablue, async_tree_memoization_tg, meteor_contest, async_tree_io, async_tree_memoization, async_tree_cpu_io_mixed, async_tree_none, unpickle
Ignored benchmarks (8) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, bpe_tokeniser, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 99.94% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x