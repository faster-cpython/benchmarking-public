# Results vs. base

- fork: savannahostrowski
- ref: jit_inv_mem_1m
- machine: linux-x86_64
- commit hash: 062c54f
- commit date: 2024-09-23
- overall geometric mean: 1.00x slower
- HPT reliability: 87.34%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240917-linux-x86_64-python-33eeccf6d4f16e483b4c-3.14.0a0-33eeccf | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_mem_1m-3.14.0a0-062c54f |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 276 ms                                                                | 277 ms: 1.00x slower                                                       |
| docutils       | 2.96 sec                                                              | 2.93 sec: 1.01x faster                                                     |
| html5lib       | 65.1 ms                                                               | 64.3 ms: 1.01x faster                                                      |
| tornado_http   | 94.4 ms                                                               | 95.0 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20240917-linux-x86_64-python-33eeccf6d4f16e483b4c-3.14.0a0-33eeccf | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_mem_1m-3.14.0a0-062c54f |
|------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| coroutines       | 23.6 ms                                                               | 22.9 ms: 1.03x faster                                                      |
| asyncio_tcp_ssl  | 1.81 sec                                                              | 1.80 sec: 1.01x faster                                                     |
| async_generators | 451 ms                                                                | 459 ms: 1.02x slower                                                       |
| Geometric mean   | (ref)                                                                 | 1.00x faster                                                               |

Benchmark hidden because not significant (10): async_tree_none, async_tree_memoization, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, asyncio_websockets, asyncio_tcp, async_tree_io_tg, async_tree_none_tg, async_tree_io, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240917-linux-x86_64-python-33eeccf6d4f16e483b4c-3.14.0a0-33eeccf | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_mem_1m-3.14.0a0-062c54f |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 69.9 ms                                                               | 69.6 ms: 1.00x faster                                                      |
| nbody          | 79.7 ms                                                               | 84.1 ms: 1.06x slower                                                      |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240917-linux-x86_64-python-33eeccf6d4f16e483b4c-3.14.0a0-33eeccf | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_mem_1m-3.14.0a0-062c54f |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 224 ms                                                                | 216 ms: 1.04x faster                                                       |
| regex_effbot   | 3.82 ms                                                               | 3.80 ms: 1.01x faster                                                      |
| regex_compile  | 142 ms                                                                | 143 ms: 1.00x slower                                                       |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240917-linux-x86_64-python-33eeccf6d4f16e483b4c-3.14.0a0-33eeccf | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_mem_1m-3.14.0a0-062c54f |
|----------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| unpickle_list        | 5.40 us                                                               | 5.29 us: 1.02x faster                                                      |
| json_dumps           | 10.1 ms                                                               | 9.93 ms: 1.02x faster                                                      |
| unpickle             | 14.8 us                                                               | 14.5 us: 1.02x faster                                                      |
| xml_etree_process    | 54.1 ms                                                               | 54.5 ms: 1.01x slower                                                      |
| unpickle_pure_python | 215 us                                                                | 217 us: 1.01x slower                                                       |
| pickle_dict          | 34.1 us                                                               | 34.5 us: 1.01x slower                                                      |
| pickle               | 11.4 us                                                               | 11.5 us: 1.01x slower                                                      |
| json_loads           | 26.9 us                                                               | 27.6 us: 1.03x slower                                                      |
| Geometric mean       | (ref)                                                                 | 1.00x slower                                                               |

Benchmark hidden because not significant (6): pickle_pure_python, tomli_loads, xml_etree_parse, xml_etree_generate, xml_etree_iterparse, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240917-linux-x86_64-python-33eeccf6d4f16e483b4c-3.14.0a0-33eeccf | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_mem_1m-3.14.0a0-062c54f |
|------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 7.09 ms                                                               | 7.05 ms: 1.01x faster                                                      |
| python_startup         | 10.6 ms                                                               | 10.5 ms: 1.00x faster                                                      |
| Geometric mean         | (ref)                                                                 | 1.00x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240917-linux-x86_64-python-33eeccf6d4f16e483b4c-3.14.0a0-33eeccf | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_mem_1m-3.14.0a0-062c54f |
|-----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_text     | 25.5 ms                                                               | 24.9 ms: 1.02x faster                                                      |
| genshi_xml      | 59.6 ms                                                               | 58.7 ms: 1.02x faster                                                      |
| mako            | 10.0 ms                                                               | 9.87 ms: 1.02x faster                                                      |
| django_template | 36.1 ms                                                               | 36.7 ms: 1.02x slower                                                      |
| Geometric mean  | (ref)                                                                 | 1.01x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20240917-linux-x86_64-python-33eeccf6d4f16e483b4c-3.14.0a0-33eeccf | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_mem_1m-3.14.0a0-062c54f |
|--------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| unpack_sequence          | 112 ns                                                                | 105 ns: 1.07x faster                                                       |
| gc_traversal             | 3.90 ms                                                               | 3.66 ms: 1.06x faster                                                      |
| regex_dna                | 224 ms                                                                | 216 ms: 1.04x faster                                                       |
| pprint_pformat           | 1.57 sec                                                              | 1.52 sec: 1.03x faster                                                     |
| scimark_sparse_mat_mult  | 4.39 ms                                                               | 4.26 ms: 1.03x faster                                                      |
| mdp                      | 2.66 sec                                                              | 2.59 sec: 1.03x faster                                                     |
| coroutines               | 23.6 ms                                                               | 22.9 ms: 1.03x faster                                                      |
| genshi_text              | 25.5 ms                                                               | 24.9 ms: 1.02x faster                                                      |
| pathlib                  | 16.2 ms                                                               | 15.9 ms: 1.02x faster                                                      |
| unpickle_list            | 5.40 us                                                               | 5.29 us: 1.02x faster                                                      |
| json_dumps               | 10.1 ms                                                               | 9.93 ms: 1.02x faster                                                      |
| unpickle                 | 14.8 us                                                               | 14.5 us: 1.02x faster                                                      |
| genshi_xml               | 59.6 ms                                                               | 58.7 ms: 1.02x faster                                                      |
| mako                     | 10.0 ms                                                               | 9.87 ms: 1.02x faster                                                      |
| html5lib                 | 65.1 ms                                                               | 64.3 ms: 1.01x faster                                                      |
| create_gc_cycles         | 1.76 ms                                                               | 1.74 ms: 1.01x faster                                                      |
| docutils                 | 2.96 sec                                                              | 2.93 sec: 1.01x faster                                                     |
| logging_silent           | 104 ns                                                                | 103 ns: 1.01x faster                                                       |
| sqlglot_parse            | 1.34 ms                                                               | 1.33 ms: 1.01x faster                                                      |
| regex_effbot             | 3.82 ms                                                               | 3.80 ms: 1.01x faster                                                      |
| asyncio_tcp_ssl          | 1.81 sec                                                              | 1.80 sec: 1.01x faster                                                     |
| python_startup_no_site   | 7.09 ms                                                               | 7.05 ms: 1.01x faster                                                      |
| python_startup           | 10.6 ms                                                               | 10.5 ms: 1.00x faster                                                      |
| float                    | 69.9 ms                                                               | 69.6 ms: 1.00x faster                                                      |
| 2to3                     | 276 ms                                                                | 277 ms: 1.00x slower                                                       |
| regex_compile            | 142 ms                                                                | 143 ms: 1.00x slower                                                       |
| bpe_tokeniser            | 4.45 sec                                                              | 4.48 sec: 1.01x slower                                                     |
| tornado_http             | 94.4 ms                                                               | 95.0 ms: 1.01x slower                                                      |
| xml_etree_process        | 54.1 ms                                                               | 54.5 ms: 1.01x slower                                                      |
| crypto_pyaes             | 66.2 ms                                                               | 66.7 ms: 1.01x slower                                                      |
| dulwich_log              | 67.6 ms                                                               | 68.2 ms: 1.01x slower                                                      |
| meteor_contest           | 106 ms                                                                | 107 ms: 1.01x slower                                                       |
| logging_format           | 6.10 us                                                               | 6.15 us: 1.01x slower                                                      |
| unpickle_pure_python     | 215 us                                                                | 217 us: 1.01x slower                                                       |
| telco                    | 8.01 ms                                                               | 8.08 ms: 1.01x slower                                                      |
| comprehensions           | 16.7 us                                                               | 16.9 us: 1.01x slower                                                      |
| sqlglot_optimize         | 58.0 ms                                                               | 58.6 ms: 1.01x slower                                                      |
| sympy_integrate          | 22.8 ms                                                               | 23.0 ms: 1.01x slower                                                      |
| sympy_sum                | 172 ms                                                                | 174 ms: 1.01x slower                                                       |
| pyflate                  | 448 ms                                                                | 454 ms: 1.01x slower                                                       |
| pickle_dict              | 34.1 us                                                               | 34.5 us: 1.01x slower                                                      |
| hexiom                   | 6.88 ms                                                               | 6.97 ms: 1.01x slower                                                      |
| typing_runtime_protocols | 164 us                                                                | 166 us: 1.01x slower                                                       |
| scimark_lu               | 109 ms                                                                | 111 ms: 1.01x slower                                                       |
| pickle                   | 11.4 us                                                               | 11.5 us: 1.01x slower                                                      |
| scimark_sor              | 116 ms                                                                | 118 ms: 1.01x slower                                                       |
| fannkuch                 | 373 ms                                                                | 379 ms: 1.02x slower                                                       |
| django_template          | 36.1 ms                                                               | 36.7 ms: 1.02x slower                                                      |
| async_generators         | 451 ms                                                                | 459 ms: 1.02x slower                                                       |
| pycparser                | 1.16 sec                                                              | 1.18 sec: 1.02x slower                                                     |
| sympy_str                | 299 ms                                                                | 305 ms: 1.02x slower                                                       |
| sympy_expand             | 503 ms                                                                | 514 ms: 1.02x slower                                                       |
| richards_super           | 45.7 ms                                                               | 46.7 ms: 1.02x slower                                                      |
| go                       | 130 ms                                                                | 134 ms: 1.02x slower                                                       |
| richards                 | 39.7 ms                                                               | 40.7 ms: 1.03x slower                                                      |
| spectral_norm            | 102 ms                                                                | 105 ms: 1.03x slower                                                       |
| json_loads               | 26.9 us                                                               | 27.6 us: 1.03x slower                                                      |
| json                     | 5.02 ms                                                               | 5.21 ms: 1.04x slower                                                      |
| nbody                    | 79.7 ms                                                               | 84.1 ms: 1.06x slower                                                      |
| nqueens                  | 83.9 ms                                                               | 89.0 ms: 1.06x slower                                                      |
| generators               | 32.7 ms                                                               | 34.9 ms: 1.07x slower                                                      |
| Geometric mean           | (ref)                                                                 | 1.00x slower                                                               |

Benchmark hidden because not significant (36): pprint_safe_repr, async_tree_none, pickle_pure_python, async_tree_memoization, async_tree_cpu_io_mixed, tomli_loads, async_tree_cpu_io_mixed_tg, scimark_monte_carlo, coverage, asyncio_websockets, sqlite_synth, asyncio_tcp, xml_etree_parse, bench_mp_pool, deepcopy, pidigits, raytrace, scimark_fft, xml_etree_generate, chaos, regex_v8, thrift, xml_etree_iterparse, async_tree_io_tg, sqlglot_normalize, async_tree_none_tg, async_tree_io, sqlglot_transpile, pickle_list, bench_thread_pool, logging_simple, deepcopy_memo, deepcopy_reduce, deltablue, async_tree_memoization_tg, pylint

# HPT report

- Reliability score: 87.34% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.99x