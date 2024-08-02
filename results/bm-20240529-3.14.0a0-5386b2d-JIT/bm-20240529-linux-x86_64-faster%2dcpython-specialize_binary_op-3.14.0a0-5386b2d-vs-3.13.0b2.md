# Results vs. 3.13.0b2

- fork: faster-cpython
- ref: specialize_binary_op
- machine: linux-x86_64
- commit hash: 5386b2d
- commit date: 2024-05-29
- overall geometric mean: 1.00x faster
- HPT reliability: 68.26%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240529-linux-x86_64-faster%2dcpython-specialize_binary_op-3.14.0a0-5386b2d |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 279 ms: 1.02x slower                                                            |
| docutils       | 2.83 sec                                                   | 2.92 sec: 1.03x slower                                                          |
| html5lib       | 67.2 ms                                                    | 66.9 ms: 1.00x faster                                                           |
| tornado_http   | 94.6 ms                                                    | 96.6 ms: 1.02x slower                                                           |
| Geometric mean | (ref)                                                      | 1.02x slower                                                                    |

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (8): async_tree_none_tg, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, async_tree_memoization, async_tree_io_tg, async_tree_cpu_io_mixed, async_tree_none, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240529-linux-x86_64-faster%2dcpython-specialize_binary_op-3.14.0a0-5386b2d |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 71.7 ms: 1.10x faster                                                           |
| nbody          | 88.3 ms                                                    | 80.8 ms: 1.09x faster                                                           |
| pidigits       | 191 ms                                                     | 189 ms: 1.01x faster                                                            |
| Geometric mean | (ref)                                                      | 1.07x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240529-linux-x86_64-faster%2dcpython-specialize_binary_op-3.14.0a0-5386b2d |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_v8       | 25.1 ms                                                    | 24.1 ms: 1.04x faster                                                           |
| regex_dna      | 221 ms                                                     | 229 ms: 1.03x slower                                                            |
| Geometric mean | (ref)                                                      | 1.00x faster                                                                    |

Benchmark hidden because not significant (2): regex_compile, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240529-linux-x86_64-faster%2dcpython-specialize_binary_op-3.14.0a0-5386b2d |
|----------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_parse      | 162 ms                                                     | 150 ms: 1.08x faster                                                            |
| xml_etree_iterparse  | 107 ms                                                     | 100 ms: 1.07x faster                                                            |
| xml_etree_generate   | 87.4 ms                                                    | 82.0 ms: 1.07x faster                                                           |
| xml_etree_process    | 61.2 ms                                                    | 58.2 ms: 1.05x faster                                                           |
| json_dumps           | 10.7 ms                                                    | 10.4 ms: 1.03x faster                                                           |
| unpickle             | 15.1 us                                                    | 14.7 us: 1.03x faster                                                           |
| pickle_pure_python   | 305 us                                                     | 300 us: 1.02x faster                                                            |
| tomli_loads          | 2.12 sec                                                   | 2.09 sec: 1.02x faster                                                          |
| json_loads           | 28.9 us                                                    | 28.7 us: 1.01x faster                                                           |
| unpickle_pure_python | 218 us                                                     | 222 us: 1.02x slower                                                            |
| unpickle_list        | 5.34 us                                                    | 5.48 us: 1.03x slower                                                           |
| pickle_list          | 5.11 us                                                    | 5.26 us: 1.03x slower                                                           |
| pickle_dict          | 34.8 us                                                    | 36.0 us: 1.03x slower                                                           |
| pickle               | 11.5 us                                                    | 12.1 us: 1.05x slower                                                           |
| Geometric mean       | (ref)                                                      | 1.01x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240529-linux-x86_64-faster%2dcpython-specialize_binary_op-3.14.0a0-5386b2d |
|------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 11.1 ms: 1.03x slower                                                           |
| python_startup_no_site | 7.11 ms                                                    | 7.59 ms: 1.07x slower                                                           |
| Geometric mean         | (ref)                                                      | 1.05x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240529-linux-x86_64-faster%2dcpython-specialize_binary_op-3.14.0a0-5386b2d |
|-----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 10.2 ms: 1.11x faster                                                           |
| django_template | 34.8 ms                                                    | 36.1 ms: 1.04x slower                                                           |
| genshi_text     | 23.7 ms                                                    | 25.4 ms: 1.07x slower                                                           |
| genshi_xml      | 51.6 ms                                                    | 58.2 ms: 1.13x slower                                                           |
| Geometric mean  | (ref)                                                      | 1.03x slower                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240529-linux-x86_64-faster%2dcpython-specialize_binary_op-3.14.0a0-5386b2d |
|--------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| richards                 | 50.9 ms                                                    | 41.7 ms: 1.22x faster                                                           |
| richards_super           | 57.4 ms                                                    | 47.9 ms: 1.20x faster                                                           |
| scimark_fft              | 392 ms                                                     | 335 ms: 1.17x faster                                                            |
| crypto_pyaes             | 77.5 ms                                                    | 67.6 ms: 1.15x faster                                                           |
| fannkuch                 | 402 ms                                                     | 356 ms: 1.13x faster                                                            |
| scimark_monte_carlo      | 69.2 ms                                                    | 62.5 ms: 1.11x faster                                                           |
| mako                     | 11.2 ms                                                    | 10.2 ms: 1.11x faster                                                           |
| float                    | 78.9 ms                                                    | 71.7 ms: 1.10x faster                                                           |
| scimark_sparse_mat_mult  | 5.27 ms                                                    | 4.82 ms: 1.09x faster                                                           |
| nbody                    | 88.3 ms                                                    | 80.8 ms: 1.09x faster                                                           |
| xml_etree_parse          | 162 ms                                                     | 150 ms: 1.08x faster                                                            |
| pyflate                  | 484 ms                                                     | 448 ms: 1.08x faster                                                            |
| pprint_pformat           | 1.56 sec                                                   | 1.45 sec: 1.08x faster                                                          |
| pprint_safe_repr         | 758 ms                                                     | 705 ms: 1.07x faster                                                            |
| xml_etree_iterparse      | 107 ms                                                     | 100 ms: 1.07x faster                                                            |
| xml_etree_generate       | 87.4 ms                                                    | 82.0 ms: 1.07x faster                                                           |
| xml_etree_process        | 61.2 ms                                                    | 58.2 ms: 1.05x faster                                                           |
| pathlib                  | 17.3 ms                                                    | 16.6 ms: 1.05x faster                                                           |
| regex_v8                 | 25.1 ms                                                    | 24.1 ms: 1.04x faster                                                           |
| logging_format           | 6.47 us                                                    | 6.20 us: 1.04x faster                                                           |
| chaos                    | 61.3 ms                                                    | 58.9 ms: 1.04x faster                                                           |
| coroutines               | 23.2 ms                                                    | 22.5 ms: 1.03x faster                                                           |
| telco                    | 8.41 ms                                                    | 8.16 ms: 1.03x faster                                                           |
| sqlite_synth             | 2.99 us                                                    | 2.90 us: 1.03x faster                                                           |
| json_dumps               | 10.7 ms                                                    | 10.4 ms: 1.03x faster                                                           |
| unpickle                 | 15.1 us                                                    | 14.7 us: 1.03x faster                                                           |
| pickle_pure_python       | 305 us                                                     | 300 us: 1.02x faster                                                            |
| logging_simple           | 5.74 us                                                    | 5.65 us: 1.02x faster                                                           |
| tomli_loads              | 2.12 sec                                                   | 2.09 sec: 1.02x faster                                                          |
| mdp                      | 2.79 sec                                                   | 2.74 sec: 1.02x faster                                                          |
| pidigits                 | 191 ms                                                     | 189 ms: 1.01x faster                                                            |
| create_gc_cycles         | 1.82 ms                                                    | 1.80 ms: 1.01x faster                                                           |
| meteor_contest           | 110 ms                                                     | 109 ms: 1.01x faster                                                            |
| thrift                   | 823 us                                                     | 817 us: 1.01x faster                                                            |
| json_loads               | 28.9 us                                                    | 28.7 us: 1.01x faster                                                           |
| html5lib                 | 67.2 ms                                                    | 66.9 ms: 1.00x faster                                                           |
| bench_mp_pool            | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                                           |
| coverage                 | 93.1 ms                                                    | 93.8 ms: 1.01x slower                                                           |
| asyncio_tcp_ssl          | 1.84 sec                                                   | 1.86 sec: 1.01x slower                                                          |
| spectral_norm            | 116 ms                                                     | 118 ms: 1.01x slower                                                            |
| gc_traversal             | 3.98 ms                                                    | 4.04 ms: 1.02x slower                                                           |
| 2to3                     | 274 ms                                                     | 279 ms: 1.02x slower                                                            |
| sqlglot_parse            | 1.32 ms                                                    | 1.34 ms: 1.02x slower                                                           |
| deepcopy                 | 367 us                                                     | 374 us: 1.02x slower                                                            |
| asyncio_tcp              | 508 ms                                                     | 518 ms: 1.02x slower                                                            |
| unpickle_pure_python     | 218 us                                                     | 222 us: 1.02x slower                                                            |
| sqlglot_transpile        | 1.63 ms                                                    | 1.67 ms: 1.02x slower                                                           |
| generators               | 29.6 ms                                                    | 30.3 ms: 1.02x slower                                                           |
| tornado_http             | 94.6 ms                                                    | 96.6 ms: 1.02x slower                                                           |
| dask                     | 369 ms                                                     | 378 ms: 1.02x slower                                                            |
| go                       | 145 ms                                                     | 148 ms: 1.02x slower                                                            |
| unpickle_list            | 5.34 us                                                    | 5.48 us: 1.03x slower                                                           |
| python_startup           | 10.8 ms                                                    | 11.1 ms: 1.03x slower                                                           |
| sqlglot_optimize         | 55.5 ms                                                    | 57.1 ms: 1.03x slower                                                           |
| pickle_list              | 5.11 us                                                    | 5.26 us: 1.03x slower                                                           |
| logging_silent           | 105 ns                                                     | 108 ns: 1.03x slower                                                            |
| dulwich_log              | 67.2 ms                                                    | 69.3 ms: 1.03x slower                                                           |
| docutils                 | 2.83 sec                                                   | 2.92 sec: 1.03x slower                                                          |
| pickle_dict              | 34.8 us                                                    | 36.0 us: 1.03x slower                                                           |
| regex_dna                | 221 ms                                                     | 229 ms: 1.03x slower                                                            |
| sqlglot_normalize        | 110 ms                                                     | 114 ms: 1.03x slower                                                            |
| typing_runtime_protocols | 165 us                                                     | 171 us: 1.04x slower                                                            |
| django_template          | 34.8 ms                                                    | 36.1 ms: 1.04x slower                                                           |
| bench_thread_pool        | 834 us                                                     | 870 us: 1.04x slower                                                            |
| scimark_lu               | 122 ms                                                     | 128 ms: 1.05x slower                                                            |
| pickle                   | 11.5 us                                                    | 12.1 us: 1.05x slower                                                           |
| async_generators         | 442 ms                                                     | 468 ms: 1.06x slower                                                            |
| hexiom                   | 6.30 ms                                                    | 6.67 ms: 1.06x slower                                                           |
| sympy_str                | 282 ms                                                     | 301 ms: 1.07x slower                                                            |
| nqueens                  | 81.4 ms                                                    | 86.7 ms: 1.07x slower                                                           |
| scimark_sor              | 127 ms                                                     | 136 ms: 1.07x slower                                                            |
| raytrace                 | 267 ms                                                     | 284 ms: 1.07x slower                                                            |
| python_startup_no_site   | 7.11 ms                                                    | 7.59 ms: 1.07x slower                                                           |
| genshi_text              | 23.7 ms                                                    | 25.4 ms: 1.07x slower                                                           |
| sympy_expand             | 473 ms                                                     | 509 ms: 1.08x slower                                                            |
| sympy_integrate          | 20.5 ms                                                    | 22.5 ms: 1.10x slower                                                           |
| pylint                   | 317 ms                                                     | 352 ms: 1.11x slower                                                            |
| sympy_sum                | 156 ms                                                     | 173 ms: 1.11x slower                                                            |
| genshi_xml               | 51.6 ms                                                    | 58.2 ms: 1.13x slower                                                           |
| deltablue                | 3.25 ms                                                    | 3.80 ms: 1.17x slower                                                           |
| Geometric mean           | (ref)                                                      | 1.00x faster                                                                    |

Benchmark hidden because not significant (16): async_tree_none_tg, async_tree_cpu_io_mixed_tg, json, comprehensions, asyncio_websockets, async_tree_memoization_tg, regex_compile, async_tree_memoization, regex_effbot, deepcopy_memo, pycparser, async_tree_io_tg, async_tree_cpu_io_mixed, deepcopy_reduce, async_tree_none, async_tree_io
Ignored benchmarks (7) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, bpe_tokeniser, chameleon, djangocms, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 68.26% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.08x