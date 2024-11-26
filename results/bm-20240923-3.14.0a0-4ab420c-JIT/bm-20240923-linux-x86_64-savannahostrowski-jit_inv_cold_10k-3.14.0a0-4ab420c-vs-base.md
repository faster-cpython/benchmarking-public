# Results vs. base

- fork: savannahostrowski
- ref: jit_inv_cold_10k
- machine: linux-x86_64
- commit hash: 4ab420c
- commit date: 2024-09-23
- overall geometric mean: 1.019x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.97x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240917-linux-x86_64-python-33eeccf6d4f16e483b4c-3.14.0a0-33eeccf | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_cold_10k-3.14.0a0-4ab420c |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 276 ms                                                                | 285 ms: 1.03x slower                                                         |
| docutils       | 2.96 sec                                                              | 2.89 sec: 1.03x faster                                                       |
| html5lib       | 65.1 ms                                                               | 66.2 ms: 1.02x slower                                                        |
| tornado_http   | 94.4 ms                                                               | 96.0 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20240917-linux-x86_64-python-33eeccf6d4f16e483b4c-3.14.0a0-33eeccf | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_cold_10k-3.14.0a0-4ab420c |
|------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| asyncio_tcp      | 497 ms                                                                | 495 ms: 1.00x faster                                                         |
| asyncio_tcp_ssl  | 1.81 sec                                                              | 1.81 sec: 1.00x faster                                                       |
| async_generators | 451 ms                                                                | 456 ms: 1.01x slower                                                         |
| async_tree_io    | 856 ms                                                                | 886 ms: 1.03x slower                                                         |
| Geometric mean   | (ref)                                                                 | 1.00x slower                                                                 |

Benchmark hidden because not significant (9): async_tree_none_tg, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, coroutines, asyncio_websockets, async_tree_memoization, async_tree_memoization_tg, async_tree_io_tg, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240917-linux-x86_64-python-33eeccf6d4f16e483b4c-3.14.0a0-33eeccf | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_cold_10k-3.14.0a0-4ab420c |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pidigits       | 186 ms                                                                | 186 ms: 1.00x slower                                                         |
| float          | 69.9 ms                                                               | 71.4 ms: 1.02x slower                                                        |
| nbody          | 79.7 ms                                                               | 82.1 ms: 1.03x slower                                                        |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240917-linux-x86_64-python-33eeccf6d4f16e483b4c-3.14.0a0-33eeccf | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_cold_10k-3.14.0a0-4ab420c |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 142 ms                                                                | 139 ms: 1.02x faster                                                         |
| regex_effbot   | 3.82 ms                                                               | 3.78 ms: 1.01x faster                                                        |
| regex_v8       | 24.6 ms                                                               | 26.2 ms: 1.06x slower                                                        |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                                 |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240917-linux-x86_64-python-33eeccf6d4f16e483b4c-3.14.0a0-33eeccf | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_cold_10k-3.14.0a0-4ab420c |
|----------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| unpickle_list        | 5.40 us                                                               | 5.32 us: 1.01x faster                                                        |
| pickle_pure_python   | 307 us                                                                | 303 us: 1.01x faster                                                         |
| tomli_loads          | 1.95 sec                                                              | 1.93 sec: 1.01x faster                                                       |
| xml_etree_iterparse  | 98.2 ms                                                               | 99.7 ms: 1.01x slower                                                        |
| pickle_dict          | 34.1 us                                                               | 34.6 us: 1.02x slower                                                        |
| unpickle_pure_python | 215 us                                                                | 219 us: 1.02x slower                                                         |
| pickle_list          | 5.09 us                                                               | 5.18 us: 1.02x slower                                                        |
| json_loads           | 26.9 us                                                               | 27.4 us: 1.02x slower                                                        |
| xml_etree_parse      | 146 ms                                                                | 149 ms: 1.02x slower                                                         |
| pickle               | 11.4 us                                                               | 11.7 us: 1.03x slower                                                        |
| xml_etree_generate   | 77.8 ms                                                               | 80.7 ms: 1.04x slower                                                        |
| xml_etree_process    | 54.1 ms                                                               | 56.2 ms: 1.04x slower                                                        |
| Geometric mean       | (ref)                                                                 | 1.01x slower                                                                 |

Benchmark hidden because not significant (2): json_dumps, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240917-linux-x86_64-python-33eeccf6d4f16e483b4c-3.14.0a0-33eeccf | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_cold_10k-3.14.0a0-4ab420c |
|------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 7.09 ms                                                               | 7.05 ms: 1.01x faster                                                        |
| python_startup         | 10.6 ms                                                               | 10.5 ms: 1.00x faster                                                        |
| Geometric mean         | (ref)                                                                 | 1.01x faster                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240917-linux-x86_64-python-33eeccf6d4f16e483b4c-3.14.0a0-33eeccf | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_cold_10k-3.14.0a0-4ab420c |
|-----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_text     | 25.5 ms                                                               | 25.7 ms: 1.01x slower                                                        |
| genshi_xml      | 59.6 ms                                                               | 60.8 ms: 1.02x slower                                                        |
| django_template | 36.1 ms                                                               | 36.9 ms: 1.02x slower                                                        |
| Geometric mean  | (ref)                                                                 | 1.01x slower                                                                 |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                | bm-20240917-linux-x86_64-python-33eeccf6d4f16e483b4c-3.14.0a0-33eeccf | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_cold_10k-3.14.0a0-4ab420c |
|--------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mdp                      | 2.66 sec                                                              | 2.55 sec: 1.04x faster                                                       |
| gc_traversal             | 3.90 ms                                                               | 3.80 ms: 1.03x faster                                                        |
| docutils                 | 2.96 sec                                                              | 2.89 sec: 1.03x faster                                                       |
| create_gc_cycles         | 1.76 ms                                                               | 1.72 ms: 1.02x faster                                                        |
| regex_compile            | 142 ms                                                                | 139 ms: 1.02x faster                                                         |
| logging_silent           | 104 ns                                                                | 102 ns: 1.01x faster                                                         |
| unpickle_list            | 5.40 us                                                               | 5.32 us: 1.01x faster                                                        |
| pickle_pure_python       | 307 us                                                                | 303 us: 1.01x faster                                                         |
| regex_effbot             | 3.82 ms                                                               | 3.78 ms: 1.01x faster                                                        |
| tomli_loads              | 1.95 sec                                                              | 1.93 sec: 1.01x faster                                                       |
| python_startup_no_site   | 7.09 ms                                                               | 7.05 ms: 1.01x faster                                                        |
| python_startup           | 10.6 ms                                                               | 10.5 ms: 1.00x faster                                                        |
| asyncio_tcp              | 497 ms                                                                | 495 ms: 1.00x faster                                                         |
| unpack_sequence          | 112 ns                                                                | 112 ns: 1.00x faster                                                         |
| asyncio_tcp_ssl          | 1.81 sec                                                              | 1.81 sec: 1.00x faster                                                       |
| pidigits                 | 186 ms                                                                | 186 ms: 1.00x slower                                                         |
| scimark_sparse_mat_mult  | 4.39 ms                                                               | 4.40 ms: 1.00x slower                                                        |
| bench_thread_pool        | 837 us                                                                | 841 us: 1.00x slower                                                         |
| sqlglot_parse            | 1.34 ms                                                               | 1.35 ms: 1.01x slower                                                        |
| dulwich_log              | 67.6 ms                                                               | 68.1 ms: 1.01x slower                                                        |
| thrift                   | 781 us                                                                | 786 us: 1.01x slower                                                         |
| chaos                    | 58.8 ms                                                               | 59.3 ms: 1.01x slower                                                        |
| fannkuch                 | 373 ms                                                                | 376 ms: 1.01x slower                                                         |
| comprehensions           | 16.7 us                                                               | 16.8 us: 1.01x slower                                                        |
| scimark_sor              | 116 ms                                                                | 117 ms: 1.01x slower                                                         |
| typing_runtime_protocols | 164 us                                                                | 165 us: 1.01x slower                                                         |
| genshi_text              | 25.5 ms                                                               | 25.7 ms: 1.01x slower                                                        |
| async_generators         | 451 ms                                                                | 456 ms: 1.01x slower                                                         |
| json                     | 5.02 ms                                                               | 5.08 ms: 1.01x slower                                                        |
| logging_format           | 6.10 us                                                               | 6.18 us: 1.01x slower                                                        |
| xml_etree_iterparse      | 98.2 ms                                                               | 99.7 ms: 1.01x slower                                                        |
| pickle_dict              | 34.1 us                                                               | 34.6 us: 1.02x slower                                                        |
| tornado_http             | 94.4 ms                                                               | 96.0 ms: 1.02x slower                                                        |
| scimark_fft              | 312 ms                                                                | 317 ms: 1.02x slower                                                         |
| unpickle_pure_python     | 215 us                                                                | 219 us: 1.02x slower                                                         |
| pyflate                  | 448 ms                                                                | 456 ms: 1.02x slower                                                         |
| html5lib                 | 65.1 ms                                                               | 66.2 ms: 1.02x slower                                                        |
| pickle_list              | 5.09 us                                                               | 5.18 us: 1.02x slower                                                        |
| json_loads               | 26.9 us                                                               | 27.4 us: 1.02x slower                                                        |
| logging_simple           | 5.57 us                                                               | 5.68 us: 1.02x slower                                                        |
| genshi_xml               | 59.6 ms                                                               | 60.8 ms: 1.02x slower                                                        |
| django_template          | 36.1 ms                                                               | 36.9 ms: 1.02x slower                                                        |
| xml_etree_parse          | 146 ms                                                                | 149 ms: 1.02x slower                                                         |
| raytrace                 | 276 ms                                                                | 281 ms: 1.02x slower                                                         |
| coverage                 | 85.2 ms                                                               | 86.9 ms: 1.02x slower                                                        |
| float                    | 69.9 ms                                                               | 71.4 ms: 1.02x slower                                                        |
| deepcopy                 | 263 us                                                                | 269 us: 1.02x slower                                                         |
| crypto_pyaes             | 66.2 ms                                                               | 67.9 ms: 1.03x slower                                                        |
| richards_super           | 45.7 ms                                                               | 47.0 ms: 1.03x slower                                                        |
| sympy_str                | 299 ms                                                                | 308 ms: 1.03x slower                                                         |
| nbody                    | 79.7 ms                                                               | 82.1 ms: 1.03x slower                                                        |
| pickle                   | 11.4 us                                                               | 11.7 us: 1.03x slower                                                        |
| 2to3                     | 276 ms                                                                | 285 ms: 1.03x slower                                                         |
| async_tree_io            | 856 ms                                                                | 886 ms: 1.03x slower                                                         |
| sqlglot_normalize        | 113 ms                                                                | 117 ms: 1.04x slower                                                         |
| xml_etree_generate       | 77.8 ms                                                               | 80.7 ms: 1.04x slower                                                        |
| xml_etree_process        | 54.1 ms                                                               | 56.2 ms: 1.04x slower                                                        |
| go                       | 130 ms                                                                | 136 ms: 1.04x slower                                                         |
| nqueens                  | 83.9 ms                                                               | 87.7 ms: 1.04x slower                                                        |
| pycparser                | 1.16 sec                                                              | 1.23 sec: 1.06x slower                                                       |
| scimark_lu               | 109 ms                                                                | 115 ms: 1.06x slower                                                         |
| regex_v8                 | 24.6 ms                                                               | 26.2 ms: 1.06x slower                                                        |
| richards                 | 39.7 ms                                                               | 42.7 ms: 1.08x slower                                                        |
| generators               | 32.7 ms                                                               | 35.6 ms: 1.09x slower                                                        |
| spectral_norm            | 102 ms                                                                | 112 ms: 1.10x slower                                                         |
| bpe_tokeniser            | 4.45 sec                                                              | 4.90 sec: 1.10x slower                                                       |
| sqlglot_optimize         | 58.0 ms                                                               | 64.3 ms: 1.11x slower                                                        |
| hexiom                   | 6.88 ms                                                               | 7.80 ms: 1.13x slower                                                        |
| deltablue                | 3.21 ms                                                               | 3.65 ms: 1.14x slower                                                        |
| sympy_integrate          | 22.8 ms                                                               | 26.7 ms: 1.17x slower                                                        |
| Geometric mean           | (ref)                                                                 | 1.02x slower                                                                 |

Benchmark hidden because not significant (27): async_tree_none_tg, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, mako, pathlib, coroutines, sympy_sum, asyncio_websockets, pprint_pformat, regex_dna, sqlglot_transpile, async_tree_memoization, deepcopy_memo, sympy_expand, bench_mp_pool, meteor_contest, scimark_monte_carlo, deepcopy_reduce, telco, sqlite_synth, json_dumps, async_tree_memoization_tg, pprint_safe_repr, async_tree_io_tg, async_tree_none, unpickle, pylint

- Geometric mean (including insignificant results): 1.019x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.97x