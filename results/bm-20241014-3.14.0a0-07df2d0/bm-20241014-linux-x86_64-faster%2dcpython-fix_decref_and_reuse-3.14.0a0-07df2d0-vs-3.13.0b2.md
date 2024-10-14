# Results vs. 3.13.0b2

- fork: faster-cpython
- ref: fix_decref_and_reuse
- machine: linux-x86_64
- commit hash: 07df2d0
- commit date: 2024-10-14
- overall geometric mean: 1.03x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241014-linux-x86_64-faster%2dcpython-fix_decref_and_reuse-3.14.0a0-07df2d0 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 255 ms: 1.08x faster                                                            |
| docutils       | 2.83 sec                                                   | 2.62 sec: 1.08x faster                                                          |
| html5lib       | 67.2 ms                                                    | 62.1 ms: 1.08x faster                                                           |
| tornado_http   | 94.6 ms                                                    | 90.4 ms: 1.05x faster                                                           |
| Geometric mean | (ref)                                                      | 1.07x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241014-linux-x86_64-faster%2dcpython-fix_decref_and_reuse-3.14.0a0-07df2d0 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 191 ms                                                     | 188 ms: 1.02x faster                                                            |
| float          | 78.9 ms                                                    | 78.3 ms: 1.01x faster                                                           |
| nbody          | 88.3 ms                                                    | 94.2 ms: 1.07x slower                                                           |
| Geometric mean | (ref)                                                      | 1.01x slower                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241014-linux-x86_64-faster%2dcpython-fix_decref_and_reuse-3.14.0a0-07df2d0 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                     | 129 ms: 1.06x faster                                                            |
| regex_effbot   | 3.67 ms                                                    | 3.63 ms: 1.01x faster                                                           |
| regex_v8       | 25.1 ms                                                    | 25.0 ms: 1.00x faster                                                           |
| Geometric mean | (ref)                                                      | 1.02x faster                                                                    |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241014-linux-x86_64-faster%2dcpython-fix_decref_and_reuse-3.14.0a0-07df2d0 |
|----------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| json_loads           | 28.9 us                                                    | 26.8 us: 1.08x faster                                                           |
| xml_etree_parse      | 162 ms                                                     | 157 ms: 1.03x faster                                                            |
| xml_etree_process    | 61.2 ms                                                    | 59.8 ms: 1.02x faster                                                           |
| xml_etree_iterparse  | 107 ms                                                     | 105 ms: 1.02x faster                                                            |
| unpickle             | 15.1 us                                                    | 14.9 us: 1.02x faster                                                           |
| xml_etree_generate   | 87.4 ms                                                    | 86.3 ms: 1.01x faster                                                           |
| pickle_dict          | 34.8 us                                                    | 35.0 us: 1.01x slower                                                           |
| unpickle_list        | 5.34 us                                                    | 5.43 us: 1.02x slower                                                           |
| unpickle_pure_python | 218 us                                                     | 222 us: 1.02x slower                                                            |
| pickle_pure_python   | 305 us                                                     | 313 us: 1.02x slower                                                            |
| pickle               | 11.5 us                                                    | 11.9 us: 1.03x slower                                                           |
| json_dumps           | 10.7 ms                                                    | 11.2 ms: 1.05x slower                                                           |
| Geometric mean       | (ref)                                                      | 1.00x faster                                                                    |

Benchmark hidden because not significant (2): pickle_list, tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241014-linux-x86_64-faster%2dcpython-fix_decref_and_reuse-3.14.0a0-07df2d0 |
|------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.6 ms: 1.02x faster                                                           |
| python_startup_no_site | 7.11 ms                                                    | 7.02 ms: 1.01x faster                                                           |
| Geometric mean         | (ref)                                                      | 1.02x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241014-linux-x86_64-faster%2dcpython-fix_decref_and_reuse-3.14.0a0-07df2d0 |
|-----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_text     | 23.7 ms                                                    | 23.0 ms: 1.03x faster                                                           |
| django_template | 34.8 ms                                                    | 34.1 ms: 1.02x faster                                                           |
| genshi_xml      | 51.6 ms                                                    | 51.9 ms: 1.01x slower                                                           |
| mako            | 11.2 ms                                                    | 11.4 ms: 1.02x slower                                                           |
| Geometric mean  | (ref)                                                      | 1.01x faster                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241014-linux-x86_64-faster%2dcpython-fix_decref_and_reuse-3.14.0a0-07df2d0 |
|--------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| deepcopy                 | 367 us                                                     | 261 us: 1.41x faster                                                            |
| deepcopy_memo            | 39.7 us                                                    | 31.2 us: 1.27x faster                                                           |
| deepcopy_reduce          | 3.35 us                                                    | 2.68 us: 1.25x faster                                                           |
| go                       | 145 ms                                                     | 122 ms: 1.19x faster                                                            |
| scimark_sparse_mat_mult  | 5.27 ms                                                    | 4.76 ms: 1.11x faster                                                           |
| mdp                      | 2.79 sec                                                   | 2.53 sec: 1.10x faster                                                          |
| coverage                 | 93.1 ms                                                    | 85.0 ms: 1.09x faster                                                           |
| html5lib                 | 67.2 ms                                                    | 62.1 ms: 1.08x faster                                                           |
| richards_super           | 57.4 ms                                                    | 53.0 ms: 1.08x faster                                                           |
| docutils                 | 2.83 sec                                                   | 2.62 sec: 1.08x faster                                                          |
| pathlib                  | 17.3 ms                                                    | 16.1 ms: 1.08x faster                                                           |
| json_loads               | 28.9 us                                                    | 26.8 us: 1.08x faster                                                           |
| richards                 | 50.9 ms                                                    | 47.3 ms: 1.08x faster                                                           |
| 2to3                     | 274 ms                                                     | 255 ms: 1.08x faster                                                            |
| scimark_fft              | 392 ms                                                     | 367 ms: 1.07x faster                                                            |
| bpe_tokeniser            | 5.02 sec                                                   | 4.71 sec: 1.07x faster                                                          |
| sympy_sum                | 156 ms                                                     | 147 ms: 1.06x faster                                                            |
| generators               | 29.6 ms                                                    | 28.0 ms: 1.06x faster                                                           |
| asyncio_tcp              | 508 ms                                                     | 480 ms: 1.06x faster                                                            |
| regex_compile            | 137 ms                                                     | 129 ms: 1.06x faster                                                            |
| thrift                   | 823 us                                                     | 779 us: 1.06x faster                                                            |
| sympy_str                | 282 ms                                                     | 268 ms: 1.06x faster                                                            |
| telco                    | 8.41 ms                                                    | 8.00 ms: 1.05x faster                                                           |
| scimark_lu               | 122 ms                                                     | 116 ms: 1.05x faster                                                            |
| pyflate                  | 484 ms                                                     | 462 ms: 1.05x faster                                                            |
| sqlite_synth             | 2.99 us                                                    | 2.85 us: 1.05x faster                                                           |
| dulwich_log              | 67.2 ms                                                    | 64.2 ms: 1.05x faster                                                           |
| tornado_http             | 94.6 ms                                                    | 90.4 ms: 1.05x faster                                                           |
| crypto_pyaes             | 77.5 ms                                                    | 74.1 ms: 1.05x faster                                                           |
| json                     | 5.31 ms                                                    | 5.09 ms: 1.04x faster                                                           |
| sqlglot_optimize         | 55.5 ms                                                    | 53.4 ms: 1.04x faster                                                           |
| pprint_pformat           | 1.56 sec                                                   | 1.49 sec: 1.04x faster                                                          |
| pprint_safe_repr         | 758 ms                                                     | 729 ms: 1.04x faster                                                            |
| sympy_expand             | 473 ms                                                     | 455 ms: 1.04x faster                                                            |
| sqlglot_normalize        | 110 ms                                                     | 106 ms: 1.03x faster                                                            |
| sympy_integrate          | 20.5 ms                                                    | 19.8 ms: 1.03x faster                                                           |
| logging_format           | 6.47 us                                                    | 6.26 us: 1.03x faster                                                           |
| meteor_contest           | 110 ms                                                     | 106 ms: 1.03x faster                                                            |
| typing_runtime_protocols | 165 us                                                     | 160 us: 1.03x faster                                                            |
| xml_etree_parse          | 162 ms                                                     | 157 ms: 1.03x faster                                                            |
| genshi_text              | 23.7 ms                                                    | 23.0 ms: 1.03x faster                                                           |
| asyncio_tcp_ssl          | 1.84 sec                                                   | 1.79 sec: 1.03x faster                                                          |
| pycparser                | 1.16 sec                                                   | 1.13 sec: 1.03x faster                                                          |
| sqlglot_transpile        | 1.63 ms                                                    | 1.59 ms: 1.03x faster                                                           |
| xml_etree_process        | 61.2 ms                                                    | 59.8 ms: 1.02x faster                                                           |
| xml_etree_iterparse      | 107 ms                                                     | 105 ms: 1.02x faster                                                            |
| gc_traversal             | 3.98 ms                                                    | 3.89 ms: 1.02x faster                                                           |
| logging_simple           | 5.74 us                                                    | 5.62 us: 1.02x faster                                                           |
| asyncio_websockets       | 567 ms                                                     | 555 ms: 1.02x faster                                                            |
| sqlglot_parse            | 1.32 ms                                                    | 1.29 ms: 1.02x faster                                                           |
| django_template          | 34.8 ms                                                    | 34.1 ms: 1.02x faster                                                           |
| create_gc_cycles         | 1.82 ms                                                    | 1.78 ms: 1.02x faster                                                           |
| python_startup           | 10.8 ms                                                    | 10.6 ms: 1.02x faster                                                           |
| spectral_norm            | 116 ms                                                     | 114 ms: 1.02x faster                                                            |
| pidigits                 | 191 ms                                                     | 188 ms: 1.02x faster                                                            |
| unpickle                 | 15.1 us                                                    | 14.9 us: 1.02x faster                                                           |
| xml_etree_generate       | 87.4 ms                                                    | 86.3 ms: 1.01x faster                                                           |
| python_startup_no_site   | 7.11 ms                                                    | 7.02 ms: 1.01x faster                                                           |
| regex_effbot             | 3.67 ms                                                    | 3.63 ms: 1.01x faster                                                           |
| async_generators         | 442 ms                                                     | 438 ms: 1.01x faster                                                            |
| float                    | 78.9 ms                                                    | 78.3 ms: 1.01x faster                                                           |
| chaos                    | 61.3 ms                                                    | 61.0 ms: 1.01x faster                                                           |
| scimark_sor              | 127 ms                                                     | 127 ms: 1.00x faster                                                            |
| regex_v8                 | 25.1 ms                                                    | 25.0 ms: 1.00x faster                                                           |
| genshi_xml               | 51.6 ms                                                    | 51.9 ms: 1.01x slower                                                           |
| bench_thread_pool        | 834 us                                                     | 838 us: 1.01x slower                                                            |
| pickle_dict              | 34.8 us                                                    | 35.0 us: 1.01x slower                                                           |
| coroutines               | 23.2 ms                                                    | 23.4 ms: 1.01x slower                                                           |
| comprehensions           | 16.6 us                                                    | 16.8 us: 1.01x slower                                                           |
| hexiom                   | 6.30 ms                                                    | 6.38 ms: 1.01x slower                                                           |
| unpickle_list            | 5.34 us                                                    | 5.43 us: 1.02x slower                                                           |
| raytrace                 | 267 ms                                                     | 271 ms: 1.02x slower                                                            |
| mako                     | 11.2 ms                                                    | 11.4 ms: 1.02x slower                                                           |
| deltablue                | 3.25 ms                                                    | 3.31 ms: 1.02x slower                                                           |
| unpickle_pure_python     | 218 us                                                     | 222 us: 1.02x slower                                                            |
| fannkuch                 | 402 ms                                                     | 411 ms: 1.02x slower                                                            |
| pickle_pure_python       | 305 us                                                     | 313 us: 1.02x slower                                                            |
| pickle                   | 11.5 us                                                    | 11.9 us: 1.03x slower                                                           |
| logging_silent           | 105 ns                                                     | 109 ns: 1.04x slower                                                            |
| json_dumps               | 10.7 ms                                                    | 11.2 ms: 1.05x slower                                                           |
| nbody                    | 88.3 ms                                                    | 94.2 ms: 1.07x slower                                                           |
| bench_mp_pool            | 23.9 ms                                                    | 56.2 ms: 2.35x slower                                                           |
| Geometric mean           | (ref)                                                      | 1.03x faster                                                                    |

Benchmark hidden because not significant (6): nqueens, regex_dna, pylint, pickle_list, tomli_loads, scimark_monte_carlo
Ignored benchmarks (15) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_io_tg, async_tree_memoization, async_tree_memoization_tg, async_tree_none, async_tree_none_tg, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20241014-3.14.0a0-07df2d0/bm-20241014-linux-x86_64-faster%2dcpython-fix_decref_and_reuse-3.14.0a0-07df2d0.json: unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.01x