# Results vs. 3.13.0b2

- fork: faster-cpython
- ref: specialize_binary_op
- machine: linux-x86_64
- commit hash: 881df50
- commit date: 2024-05-23
- overall geometric mean: 1.00x faster
- HPT reliability: 86.75%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240523-linux-x86_64-faster%2dcpython-specialize_binary_op-3.14.0a0-881df50 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 279 ms: 1.02x slower                                                            |
| chameleon      | 7.22 ms                                                    | 7.12 ms: 1.01x faster                                                           |
| docutils       | 2.83 sec                                                   | 2.96 sec: 1.05x slower                                                          |
| tornado_http   | 94.6 ms                                                    | 97.1 ms: 1.03x slower                                                           |
| Geometric mean | (ref)                                                      | 1.02x slower                                                                    |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (8): async_tree_none_tg, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, async_tree_memoization, async_tree_cpu_io_mixed, async_tree_io_tg, async_tree_none, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240523-linux-x86_64-faster%2dcpython-specialize_binary_op-3.14.0a0-881df50 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 88.3 ms                                                    | 81.0 ms: 1.09x faster                                                           |
| float          | 78.9 ms                                                    | 72.5 ms: 1.09x faster                                                           |
| pidigits       | 191 ms                                                     | 189 ms: 1.01x faster                                                            |
| Geometric mean | (ref)                                                      | 1.06x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240523-linux-x86_64-faster%2dcpython-specialize_binary_op-3.14.0a0-881df50 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                     | 136 ms: 1.00x faster                                                            |
| regex_dna      | 221 ms                                                     | 233 ms: 1.05x slower                                                            |
| regex_effbot   | 3.67 ms                                                    | 3.87 ms: 1.05x slower                                                           |
| regex_v8       | 25.1 ms                                                    | 26.5 ms: 1.06x slower                                                           |
| Geometric mean | (ref)                                                      | 1.04x slower                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240523-linux-x86_64-faster%2dcpython-specialize_binary_op-3.14.0a0-881df50 |
|----------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_parse      | 162 ms                                                     | 149 ms: 1.08x faster                                                            |
| xml_etree_iterparse  | 107 ms                                                     | 101 ms: 1.07x faster                                                            |
| xml_etree_generate   | 87.4 ms                                                    | 82.5 ms: 1.06x faster                                                           |
| xml_etree_process    | 61.2 ms                                                    | 57.9 ms: 1.06x faster                                                           |
| json_dumps           | 10.7 ms                                                    | 10.5 ms: 1.03x faster                                                           |
| unpickle_list        | 5.34 us                                                    | 5.31 us: 1.01x faster                                                           |
| pickle_list          | 5.11 us                                                    | 5.15 us: 1.01x slower                                                           |
| unpickle_pure_python | 218 us                                                     | 222 us: 1.02x slower                                                            |
| pickle_dict          | 34.8 us                                                    | 35.6 us: 1.02x slower                                                           |
| pickle               | 11.5 us                                                    | 12.0 us: 1.04x slower                                                           |
| Geometric mean       | (ref)                                                      | 1.02x faster                                                                    |

Benchmark hidden because not significant (4): pickle_pure_python, tomli_loads, json_loads, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240523-linux-x86_64-faster%2dcpython-specialize_binary_op-3.14.0a0-881df50 |
|------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.9 ms: 1.01x slower                                                           |
| python_startup_no_site | 7.11 ms                                                    | 7.59 ms: 1.07x slower                                                           |
| Geometric mean         | (ref)                                                      | 1.04x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240523-linux-x86_64-faster%2dcpython-specialize_binary_op-3.14.0a0-881df50 |
|-----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 10.1 ms: 1.11x faster                                                           |
| django_template | 34.8 ms                                                    | 36.7 ms: 1.05x slower                                                           |
| genshi_text     | 23.7 ms                                                    | 25.6 ms: 1.08x slower                                                           |
| genshi_xml      | 51.6 ms                                                    | 58.5 ms: 1.13x slower                                                           |
| Geometric mean  | (ref)                                                      | 1.04x slower                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240523-linux-x86_64-faster%2dcpython-specialize_binary_op-3.14.0a0-881df50 |
|--------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| richards                 | 50.9 ms                                                    | 42.2 ms: 1.21x faster                                                           |
| richards_super           | 57.4 ms                                                    | 48.2 ms: 1.19x faster                                                           |
| scimark_fft              | 392 ms                                                     | 334 ms: 1.17x faster                                                            |
| crypto_pyaes             | 77.5 ms                                                    | 66.6 ms: 1.16x faster                                                           |
| fannkuch                 | 402 ms                                                     | 360 ms: 1.12x faster                                                            |
| mako                     | 11.2 ms                                                    | 10.1 ms: 1.11x faster                                                           |
| scimark_monte_carlo      | 69.2 ms                                                    | 62.3 ms: 1.11x faster                                                           |
| scimark_sparse_mat_mult  | 5.27 ms                                                    | 4.82 ms: 1.09x faster                                                           |
| nbody                    | 88.3 ms                                                    | 81.0 ms: 1.09x faster                                                           |
| float                    | 78.9 ms                                                    | 72.5 ms: 1.09x faster                                                           |
| xml_etree_parse          | 162 ms                                                     | 149 ms: 1.08x faster                                                            |
| pyflate                  | 484 ms                                                     | 450 ms: 1.08x faster                                                            |
| pprint_safe_repr         | 758 ms                                                     | 708 ms: 1.07x faster                                                            |
| pprint_pformat           | 1.56 sec                                                   | 1.45 sec: 1.07x faster                                                          |
| xml_etree_iterparse      | 107 ms                                                     | 101 ms: 1.07x faster                                                            |
| chaos                    | 61.3 ms                                                    | 57.7 ms: 1.06x faster                                                           |
| xml_etree_generate       | 87.4 ms                                                    | 82.5 ms: 1.06x faster                                                           |
| mdp                      | 2.79 sec                                                   | 2.64 sec: 1.06x faster                                                          |
| xml_etree_process        | 61.2 ms                                                    | 57.9 ms: 1.06x faster                                                           |
| pathlib                  | 17.3 ms                                                    | 16.4 ms: 1.06x faster                                                           |
| logging_format           | 6.47 us                                                    | 6.24 us: 1.04x faster                                                           |
| sqlite_synth             | 2.99 us                                                    | 2.89 us: 1.03x faster                                                           |
| deepcopy_memo            | 39.7 us                                                    | 38.5 us: 1.03x faster                                                           |
| json_dumps               | 10.7 ms                                                    | 10.5 ms: 1.03x faster                                                           |
| meteor_contest           | 110 ms                                                     | 108 ms: 1.02x faster                                                            |
| chameleon                | 7.22 ms                                                    | 7.12 ms: 1.01x faster                                                           |
| logging_simple           | 5.74 us                                                    | 5.68 us: 1.01x faster                                                           |
| pidigits                 | 191 ms                                                     | 189 ms: 1.01x faster                                                            |
| json                     | 5.31 ms                                                    | 5.25 ms: 1.01x faster                                                           |
| telco                    | 8.41 ms                                                    | 8.34 ms: 1.01x faster                                                           |
| comprehensions           | 16.6 us                                                    | 16.5 us: 1.01x faster                                                           |
| unpickle_list            | 5.34 us                                                    | 5.31 us: 1.01x faster                                                           |
| regex_compile            | 137 ms                                                     | 136 ms: 1.00x faster                                                            |
| asyncio_websockets       | 567 ms                                                     | 570 ms: 1.01x slower                                                            |
| bench_mp_pool            | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                                           |
| deepcopy                 | 367 us                                                     | 370 us: 1.01x slower                                                            |
| coverage                 | 93.1 ms                                                    | 93.8 ms: 1.01x slower                                                           |
| pickle_list              | 5.11 us                                                    | 5.15 us: 1.01x slower                                                           |
| asyncio_tcp_ssl          | 1.84 sec                                                   | 1.86 sec: 1.01x slower                                                          |
| python_startup           | 10.8 ms                                                    | 10.9 ms: 1.01x slower                                                           |
| 2to3                     | 274 ms                                                     | 279 ms: 1.02x slower                                                            |
| unpickle_pure_python     | 218 us                                                     | 222 us: 1.02x slower                                                            |
| logging_silent           | 105 ns                                                     | 107 ns: 1.02x slower                                                            |
| sqlglot_transpile        | 1.63 ms                                                    | 1.67 ms: 1.02x slower                                                           |
| asyncio_tcp              | 508 ms                                                     | 519 ms: 1.02x slower                                                            |
| sqlglot_optimize         | 55.5 ms                                                    | 56.8 ms: 1.02x slower                                                           |
| pickle_dict              | 34.8 us                                                    | 35.6 us: 1.02x slower                                                           |
| gc_traversal             | 3.98 ms                                                    | 4.08 ms: 1.03x slower                                                           |
| flaskblogging            | 9.01 ms                                                    | 9.25 ms: 1.03x slower                                                           |
| tornado_http             | 94.6 ms                                                    | 97.1 ms: 1.03x slower                                                           |
| dask                     | 369 ms                                                     | 380 ms: 1.03x slower                                                            |
| scimark_lu               | 122 ms                                                     | 125 ms: 1.03x slower                                                            |
| dulwich_log              | 67.2 ms                                                    | 69.4 ms: 1.03x slower                                                           |
| sqlglot_normalize        | 110 ms                                                     | 114 ms: 1.03x slower                                                            |
| bench_thread_pool        | 834 us                                                     | 865 us: 1.04x slower                                                            |
| typing_runtime_protocols | 165 us                                                     | 171 us: 1.04x slower                                                            |
| pycparser                | 1.16 sec                                                   | 1.21 sec: 1.04x slower                                                          |
| pickle                   | 11.5 us                                                    | 12.0 us: 1.04x slower                                                           |
| go                       | 145 ms                                                     | 151 ms: 1.04x slower                                                            |
| docutils                 | 2.83 sec                                                   | 2.96 sec: 1.05x slower                                                          |
| async_generators         | 442 ms                                                     | 463 ms: 1.05x slower                                                            |
| hexiom                   | 6.30 ms                                                    | 6.60 ms: 1.05x slower                                                           |
| generators               | 29.6 ms                                                    | 31.2 ms: 1.05x slower                                                           |
| scimark_sor              | 127 ms                                                     | 134 ms: 1.05x slower                                                            |
| regex_dna                | 221 ms                                                     | 233 ms: 1.05x slower                                                            |
| django_template          | 34.8 ms                                                    | 36.7 ms: 1.05x slower                                                           |
| regex_effbot             | 3.67 ms                                                    | 3.87 ms: 1.05x slower                                                           |
| raytrace                 | 267 ms                                                     | 281 ms: 1.06x slower                                                            |
| regex_v8                 | 25.1 ms                                                    | 26.5 ms: 1.06x slower                                                           |
| sympy_str                | 282 ms                                                     | 301 ms: 1.07x slower                                                            |
| python_startup_no_site   | 7.11 ms                                                    | 7.59 ms: 1.07x slower                                                           |
| nqueens                  | 81.4 ms                                                    | 87.2 ms: 1.07x slower                                                           |
| genshi_text              | 23.7 ms                                                    | 25.6 ms: 1.08x slower                                                           |
| sympy_expand             | 473 ms                                                     | 514 ms: 1.09x slower                                                            |
| sympy_integrate          | 20.5 ms                                                    | 22.4 ms: 1.09x slower                                                           |
| sympy_sum                | 156 ms                                                     | 171 ms: 1.10x slower                                                            |
| pylint                   | 317 ms                                                     | 353 ms: 1.11x slower                                                            |
| genshi_xml               | 51.6 ms                                                    | 58.5 ms: 1.13x slower                                                           |
| deltablue                | 3.25 ms                                                    | 3.79 ms: 1.16x slower                                                           |
| Geometric mean           | (ref)                                                      | 1.00x faster                                                                    |

Benchmark hidden because not significant (19): pickle_pure_python, async_tree_none_tg, async_tree_cpu_io_mixed_tg, tomli_loads, async_tree_memoization_tg, spectral_norm, json_loads, async_tree_memoization, sqlglot_parse, create_gc_cycles, thrift, html5lib, unpickle, deepcopy_reduce, coroutines, async_tree_cpu_io_mixed, async_tree_io_tg, async_tree_none, async_tree_io
Ignored benchmarks (5) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, bpe_tokeniser, djangocms, gunicorn, mypy2

# HPT report

- Reliability score: 86.75% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.08x