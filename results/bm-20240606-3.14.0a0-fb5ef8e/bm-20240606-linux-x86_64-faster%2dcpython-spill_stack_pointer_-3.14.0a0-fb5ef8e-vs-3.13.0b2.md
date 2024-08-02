# Results vs. 3.13.0b2

- fork: faster-cpython
- ref: spill_stack_pointer_
- machine: linux-x86_64
- commit hash: fb5ef8e
- commit date: 2024-06-06
- overall geometric mean: 1.00x faster
- HPT reliability: 73.28%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240606-linux-x86_64-faster%2dcpython-spill_stack_pointer_-3.14.0a0-fb5ef8e |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 271 ms: 1.01x faster                                                            |
| docutils       | 2.83 sec                                                   | 2.80 sec: 1.01x faster                                                          |
| html5lib       | 67.2 ms                                                    | 67.7 ms: 1.01x slower                                                           |
| tornado_http   | 94.6 ms                                                    | 94.9 ms: 1.00x slower                                                           |
| Geometric mean | (ref)                                                      | 1.00x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark          | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240606-linux-x86_64-faster%2dcpython-spill_stack_pointer_-3.14.0a0-fb5ef8e |
|--------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none    | 378 ms                                                     | 391 ms: 1.03x slower                                                            |
| async_tree_none_tg | 336 ms                                                     | 350 ms: 1.04x slower                                                            |
| Geometric mean     | (ref)                                                      | 1.02x slower                                                                    |

Benchmark hidden because not significant (6): async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, async_tree_cpu_io_mixed, async_tree_io_tg, async_tree_io, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240606-linux-x86_64-faster%2dcpython-spill_stack_pointer_-3.14.0a0-fb5ef8e |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 191 ms                                                     | 189 ms: 1.01x faster                                                            |
| float          | 78.9 ms                                                    | 79.3 ms: 1.01x slower                                                           |
| nbody          | 88.3 ms                                                    | 92.1 ms: 1.04x slower                                                           |
| Geometric mean | (ref)                                                      | 1.01x slower                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240606-linux-x86_64-faster%2dcpython-spill_stack_pointer_-3.14.0a0-fb5ef8e |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_v8       | 25.1 ms                                                    | 24.8 ms: 1.01x faster                                                           |
| regex_compile  | 137 ms                                                     | 136 ms: 1.01x faster                                                            |
| regex_dna      | 221 ms                                                     | 223 ms: 1.01x slower                                                            |
| Geometric mean | (ref)                                                      | 1.00x faster                                                                    |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240606-linux-x86_64-faster%2dcpython-spill_stack_pointer_-3.14.0a0-fb5ef8e |
|----------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_parse      | 162 ms                                                     | 158 ms: 1.02x faster                                                            |
| json_dumps           | 10.7 ms                                                    | 10.6 ms: 1.02x faster                                                           |
| xml_etree_process    | 61.2 ms                                                    | 60.3 ms: 1.01x faster                                                           |
| pickle_list          | 5.11 us                                                    | 5.04 us: 1.01x faster                                                           |
| pickle_pure_python   | 305 us                                                     | 302 us: 1.01x faster                                                            |
| xml_etree_generate   | 87.4 ms                                                    | 87.0 ms: 1.00x faster                                                           |
| unpickle_list        | 5.34 us                                                    | 5.40 us: 1.01x slower                                                           |
| unpickle             | 15.1 us                                                    | 15.3 us: 1.01x slower                                                           |
| pickle_dict          | 34.8 us                                                    | 35.3 us: 1.02x slower                                                           |
| pickle               | 11.5 us                                                    | 11.7 us: 1.02x slower                                                           |
| unpickle_pure_python | 218 us                                                     | 223 us: 1.02x slower                                                            |
| tomli_loads          | 2.12 sec                                                   | 2.19 sec: 1.03x slower                                                          |
| Geometric mean       | (ref)                                                      | 1.00x slower                                                                    |

Benchmark hidden because not significant (2): xml_etree_iterparse, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240606-linux-x86_64-faster%2dcpython-spill_stack_pointer_-3.14.0a0-fb5ef8e |
|------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.6 ms: 1.01x faster                                                           |
| python_startup_no_site | 7.11 ms                                                    | 7.13 ms: 1.00x slower                                                           |
| Geometric mean         | (ref)                                                      | 1.00x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240606-linux-x86_64-faster%2dcpython-spill_stack_pointer_-3.14.0a0-fb5ef8e |
|-----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 10.9 ms: 1.03x faster                                                           |
| genshi_xml      | 51.6 ms                                                    | 50.5 ms: 1.02x faster                                                           |
| django_template | 34.8 ms                                                    | 36.1 ms: 1.04x slower                                                           |
| Geometric mean  | (ref)                                                      | 1.00x faster                                                                    |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240606-linux-x86_64-faster%2dcpython-spill_stack_pointer_-3.14.0a0-fb5ef8e |
|--------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pathlib                  | 17.3 ms                                                    | 16.1 ms: 1.08x faster                                                           |
| generators               | 29.6 ms                                                    | 27.9 ms: 1.06x faster                                                           |
| richards_super           | 57.4 ms                                                    | 54.0 ms: 1.06x faster                                                           |
| richards                 | 50.9 ms                                                    | 48.3 ms: 1.05x faster                                                           |
| scimark_lu               | 122 ms                                                     | 116 ms: 1.05x faster                                                            |
| scimark_fft              | 392 ms                                                     | 379 ms: 1.04x faster                                                            |
| mdp                      | 2.79 sec                                                   | 2.71 sec: 1.03x faster                                                          |
| mako                     | 11.2 ms                                                    | 10.9 ms: 1.03x faster                                                           |
| hexiom                   | 6.30 ms                                                    | 6.16 ms: 1.02x faster                                                           |
| genshi_xml               | 51.6 ms                                                    | 50.5 ms: 1.02x faster                                                           |
| xml_etree_parse          | 162 ms                                                     | 158 ms: 1.02x faster                                                            |
| dulwich_log              | 67.2 ms                                                    | 65.8 ms: 1.02x faster                                                           |
| pprint_pformat           | 1.56 sec                                                   | 1.53 sec: 1.02x faster                                                          |
| scimark_sparse_mat_mult  | 5.27 ms                                                    | 5.17 ms: 1.02x faster                                                           |
| pprint_safe_repr         | 758 ms                                                     | 745 ms: 1.02x faster                                                            |
| deepcopy_reduce          | 3.35 us                                                    | 3.30 us: 1.02x faster                                                           |
| json_dumps               | 10.7 ms                                                    | 10.6 ms: 1.02x faster                                                           |
| xml_etree_process        | 61.2 ms                                                    | 60.3 ms: 1.01x faster                                                           |
| crypto_pyaes             | 77.5 ms                                                    | 76.4 ms: 1.01x faster                                                           |
| pickle_list              | 5.11 us                                                    | 5.04 us: 1.01x faster                                                           |
| thrift                   | 823 us                                                     | 812 us: 1.01x faster                                                            |
| scimark_sor              | 127 ms                                                     | 126 ms: 1.01x faster                                                            |
| python_startup           | 10.8 ms                                                    | 10.6 ms: 1.01x faster                                                           |
| pickle_pure_python       | 305 us                                                     | 302 us: 1.01x faster                                                            |
| regex_v8                 | 25.1 ms                                                    | 24.8 ms: 1.01x faster                                                           |
| pidigits                 | 191 ms                                                     | 189 ms: 1.01x faster                                                            |
| docutils                 | 2.83 sec                                                   | 2.80 sec: 1.01x faster                                                          |
| create_gc_cycles         | 1.82 ms                                                    | 1.80 ms: 1.01x faster                                                           |
| 2to3                     | 274 ms                                                     | 271 ms: 1.01x faster                                                            |
| chaos                    | 61.3 ms                                                    | 60.8 ms: 1.01x faster                                                           |
| raytrace                 | 267 ms                                                     | 264 ms: 1.01x faster                                                            |
| scimark_monte_carlo      | 69.2 ms                                                    | 68.5 ms: 1.01x faster                                                           |
| regex_compile            | 137 ms                                                     | 136 ms: 1.01x faster                                                            |
| logging_silent           | 105 ns                                                     | 104 ns: 1.01x faster                                                            |
| sqlite_synth             | 2.99 us                                                    | 2.97 us: 1.01x faster                                                           |
| fannkuch                 | 402 ms                                                     | 399 ms: 1.01x faster                                                            |
| bench_thread_pool        | 834 us                                                     | 828 us: 1.01x faster                                                            |
| deepcopy_memo            | 39.7 us                                                    | 39.5 us: 1.01x faster                                                           |
| asyncio_websockets       | 567 ms                                                     | 564 ms: 1.01x faster                                                            |
| xml_etree_generate       | 87.4 ms                                                    | 87.0 ms: 1.00x faster                                                           |
| deepcopy                 | 367 us                                                     | 366 us: 1.00x faster                                                            |
| tornado_http             | 94.6 ms                                                    | 94.9 ms: 1.00x slower                                                           |
| asyncio_tcp_ssl          | 1.84 sec                                                   | 1.85 sec: 1.00x slower                                                          |
| python_startup_no_site   | 7.11 ms                                                    | 7.13 ms: 1.00x slower                                                           |
| pyflate                  | 484 ms                                                     | 486 ms: 1.00x slower                                                            |
| sympy_sum                | 156 ms                                                     | 157 ms: 1.00x slower                                                            |
| gc_traversal             | 3.98 ms                                                    | 4.00 ms: 1.00x slower                                                           |
| float                    | 78.9 ms                                                    | 79.3 ms: 1.01x slower                                                           |
| sqlglot_normalize        | 110 ms                                                     | 111 ms: 1.01x slower                                                            |
| meteor_contest           | 110 ms                                                     | 110 ms: 1.01x slower                                                            |
| html5lib                 | 67.2 ms                                                    | 67.7 ms: 1.01x slower                                                           |
| sympy_expand             | 473 ms                                                     | 476 ms: 1.01x slower                                                            |
| regex_dna                | 221 ms                                                     | 223 ms: 1.01x slower                                                            |
| telco                    | 8.41 ms                                                    | 8.50 ms: 1.01x slower                                                           |
| unpickle_list            | 5.34 us                                                    | 5.40 us: 1.01x slower                                                           |
| unpickle                 | 15.1 us                                                    | 15.3 us: 1.01x slower                                                           |
| coverage                 | 93.1 ms                                                    | 94.2 ms: 1.01x slower                                                           |
| logging_format           | 6.47 us                                                    | 6.55 us: 1.01x slower                                                           |
| sqlglot_parse            | 1.32 ms                                                    | 1.34 ms: 1.01x slower                                                           |
| json                     | 5.31 ms                                                    | 5.39 ms: 1.02x slower                                                           |
| pickle_dict              | 34.8 us                                                    | 35.3 us: 1.02x slower                                                           |
| comprehensions           | 16.6 us                                                    | 16.9 us: 1.02x slower                                                           |
| pickle                   | 11.5 us                                                    | 11.7 us: 1.02x slower                                                           |
| unpickle_pure_python     | 218 us                                                     | 223 us: 1.02x slower                                                            |
| typing_runtime_protocols | 165 us                                                     | 168 us: 1.02x slower                                                            |
| logging_simple           | 5.74 us                                                    | 5.89 us: 1.02x slower                                                           |
| tomli_loads              | 2.12 sec                                                   | 2.19 sec: 1.03x slower                                                          |
| async_tree_none          | 378 ms                                                     | 391 ms: 1.03x slower                                                            |
| django_template          | 34.8 ms                                                    | 36.1 ms: 1.04x slower                                                           |
| async_generators         | 442 ms                                                     | 458 ms: 1.04x slower                                                            |
| async_tree_none_tg       | 336 ms                                                     | 350 ms: 1.04x slower                                                            |
| nbody                    | 88.3 ms                                                    | 92.1 ms: 1.04x slower                                                           |
| Geometric mean           | (ref)                                                      | 1.00x faster                                                                    |

Benchmark hidden because not significant (24): xml_etree_iterparse, async_tree_cpu_io_mixed_tg, coroutines, genshi_text, pylint, json_loads, sqlglot_optimize, nqueens, spectral_norm, regex_effbot, sympy_str, deltablue, sympy_integrate, sqlglot_transpile, go, bench_mp_pool, asyncio_tcp, dask, pycparser, async_tree_memoization_tg, async_tree_cpu_io_mixed, async_tree_io_tg, async_tree_io, async_tree_memoization
Ignored benchmarks (7) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, bpe_tokeniser, chameleon, djangocms, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 73.28% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x