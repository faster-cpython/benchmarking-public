# Results vs. base

- fork: brandtbucher
- ref: justin_compact_exits
- machine: linux-x86_64
- commit hash: 971feb9
- commit date: 2024-10-01
- overall geometric mean: 1.01x faster
- HPT reliability: 99.98%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240929-linux-x86_64-python-6f4d64b048133c60d407-3.14.0a0-6f4d64b | bm-20241001-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-971feb9 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                                | 277 ms: 1.01x faster                                                        |
| html5lib       | 65.5 ms                                                               | 62.7 ms: 1.04x faster                                                       |
| tornado_http   | 95.4 ms                                                               | 94.1 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                                 | 1.02x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20240929-linux-x86_64-python-6f4d64b048133c60d407-3.14.0a0-6f4d64b | bm-20241001-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-971feb9 |
|------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| asyncio_tcp      | 488 ms                                                                | 484 ms: 1.01x faster                                                        |
| coroutines       | 23.2 ms                                                               | 23.0 ms: 1.01x faster                                                       |
| asyncio_tcp_ssl  | 1.79 sec                                                              | 1.80 sec: 1.01x slower                                                      |
| async_generators | 453 ms                                                                | 461 ms: 1.02x slower                                                        |
| Geometric mean   | (ref)                                                                 | 1.00x slower                                                                |

Benchmark hidden because not significant (9): async_tree_memoization, async_tree_cpu_io_mixed, asyncio_websockets, async_tree_io, async_tree_io_tg, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_none_tg, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240929-linux-x86_64-python-6f4d64b048133c60d407-3.14.0a0-6f4d64b | bm-20241001-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-971feb9 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 72.0 ms                                                               | 71.4 ms: 1.01x faster                                                       |
| pidigits       | 186 ms                                                                | 185 ms: 1.00x faster                                                        |
| nbody          | 80.7 ms                                                               | 82.8 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240929-linux-x86_64-python-6f4d64b048133c60d407-3.14.0a0-6f4d64b | bm-20241001-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-971feb9 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 3.79 ms                                                               | 3.61 ms: 1.05x faster                                                       |
| regex_compile  | 145 ms                                                                | 140 ms: 1.04x faster                                                        |
| regex_dna      | 218 ms                                                                | 217 ms: 1.01x faster                                                        |
| regex_v8       | 24.6 ms                                                               | 25.1 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                                 | 1.02x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240929-linux-x86_64-python-6f4d64b048133c60d407-3.14.0a0-6f4d64b | bm-20241001-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-971feb9 |
|----------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle             | 15.3 us                                                               | 14.6 us: 1.04x faster                                                       |
| unpickle_list        | 5.44 us                                                               | 5.25 us: 1.03x faster                                                       |
| tomli_loads          | 1.93 sec                                                              | 1.88 sec: 1.02x faster                                                      |
| pickle_dict          | 34.7 us                                                               | 34.1 us: 1.02x faster                                                       |
| xml_etree_process    | 54.9 ms                                                               | 54.1 ms: 1.01x faster                                                       |
| xml_etree_generate   | 77.2 ms                                                               | 76.7 ms: 1.01x faster                                                       |
| unpickle_pure_python | 214 us                                                                | 213 us: 1.00x faster                                                        |
| pickle_pure_python   | 306 us                                                                | 307 us: 1.00x slower                                                        |
| json_loads           | 26.6 us                                                               | 26.8 us: 1.01x slower                                                       |
| xml_etree_iterparse  | 97.8 ms                                                               | 98.7 ms: 1.01x slower                                                       |
| pickle_list          | 4.92 us                                                               | 5.06 us: 1.03x slower                                                       |
| pickle               | 11.4 us                                                               | 11.8 us: 1.03x slower                                                       |
| Geometric mean       | (ref)                                                                 | 1.00x faster                                                                |

Benchmark hidden because not significant (2): json_dumps, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240929-linux-x86_64-python-6f4d64b048133c60d407-3.14.0a0-6f4d64b | bm-20241001-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-971feb9 |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 10.5 ms                                                               | 10.6 ms: 1.00x slower                                                       |
| python_startup_no_site | 7.07 ms                                                               | 7.09 ms: 1.00x slower                                                       |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240929-linux-x86_64-python-6f4d64b048133c60d407-3.14.0a0-6f4d64b | bm-20241001-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-971feb9 |
|-----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 36.3 ms                                                               | 35.4 ms: 1.02x faster                                                       |
| mako            | 9.80 ms                                                               | 9.79 ms: 1.00x faster                                                       |
| genshi_xml      | 57.3 ms                                                               | 57.7 ms: 1.01x slower                                                       |
| genshi_text     | 24.7 ms                                                               | 25.0 ms: 1.01x slower                                                       |
| Geometric mean  | (ref)                                                                 | 1.00x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20240929-linux-x86_64-python-6f4d64b048133c60d407-3.14.0a0-6f4d64b | bm-20241001-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-971feb9 |
|--------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| richards                 | 39.7 ms                                                               | 32.7 ms: 1.21x faster                                                       |
| richards_super           | 45.3 ms                                                               | 38.5 ms: 1.18x faster                                                       |
| pprint_safe_repr         | 738 ms                                                                | 691 ms: 1.07x faster                                                        |
| pprint_pformat           | 1.54 sec                                                              | 1.44 sec: 1.07x faster                                                      |
| unpack_sequence          | 110 ns                                                                | 105 ns: 1.05x faster                                                        |
| regex_effbot             | 3.79 ms                                                               | 3.61 ms: 1.05x faster                                                       |
| html5lib                 | 65.5 ms                                                               | 62.7 ms: 1.04x faster                                                       |
| unpickle                 | 15.3 us                                                               | 14.6 us: 1.04x faster                                                       |
| comprehensions           | 16.8 us                                                               | 16.2 us: 1.04x faster                                                       |
| regex_compile            | 145 ms                                                                | 140 ms: 1.04x faster                                                        |
| sympy_integrate          | 23.5 ms                                                               | 22.6 ms: 1.04x faster                                                       |
| hexiom                   | 6.93 ms                                                               | 6.67 ms: 1.04x faster                                                       |
| sympy_str                | 308 ms                                                                | 298 ms: 1.04x faster                                                        |
| unpickle_list            | 5.44 us                                                               | 5.25 us: 1.03x faster                                                       |
| sqlglot_parse            | 1.35 ms                                                               | 1.31 ms: 1.03x faster                                                       |
| scimark_sparse_mat_mult  | 4.55 ms                                                               | 4.40 ms: 1.03x faster                                                       |
| scimark_fft              | 317 ms                                                                | 307 ms: 1.03x faster                                                        |
| sqlglot_transpile        | 1.70 ms                                                               | 1.65 ms: 1.03x faster                                                       |
| deltablue                | 3.21 ms                                                               | 3.13 ms: 1.03x faster                                                       |
| go                       | 131 ms                                                                | 127 ms: 1.03x faster                                                        |
| sqlglot_normalize        | 116 ms                                                                | 113 ms: 1.03x faster                                                        |
| django_template          | 36.3 ms                                                               | 35.4 ms: 1.02x faster                                                       |
| tomli_loads              | 1.93 sec                                                              | 1.88 sec: 1.02x faster                                                      |
| deepcopy                 | 268 us                                                                | 261 us: 1.02x faster                                                        |
| sympy_expand             | 511 ms                                                                | 500 ms: 1.02x faster                                                        |
| pyflate                  | 450 ms                                                                | 441 ms: 1.02x faster                                                        |
| generators               | 34.8 ms                                                               | 34.1 ms: 1.02x faster                                                       |
| dulwich_log              | 69.0 ms                                                               | 67.6 ms: 1.02x faster                                                       |
| fannkuch                 | 372 ms                                                                | 366 ms: 1.02x faster                                                        |
| pickle_dict              | 34.7 us                                                               | 34.1 us: 1.02x faster                                                       |
| tornado_http             | 95.4 ms                                                               | 94.1 ms: 1.01x faster                                                       |
| crypto_pyaes             | 65.9 ms                                                               | 64.9 ms: 1.01x faster                                                       |
| meteor_contest           | 107 ms                                                                | 105 ms: 1.01x faster                                                        |
| xml_etree_process        | 54.9 ms                                                               | 54.1 ms: 1.01x faster                                                       |
| bpe_tokeniser            | 4.44 sec                                                              | 4.39 sec: 1.01x faster                                                      |
| typing_runtime_protocols | 166 us                                                                | 164 us: 1.01x faster                                                        |
| deepcopy_memo            | 27.1 us                                                               | 26.8 us: 1.01x faster                                                       |
| scimark_monte_carlo      | 62.9 ms                                                               | 62.2 ms: 1.01x faster                                                       |
| mdp                      | 2.56 sec                                                              | 2.53 sec: 1.01x faster                                                      |
| asyncio_tcp              | 488 ms                                                                | 484 ms: 1.01x faster                                                        |
| 2to3                     | 280 ms                                                                | 277 ms: 1.01x faster                                                        |
| float                    | 72.0 ms                                                               | 71.4 ms: 1.01x faster                                                       |
| regex_dna                | 218 ms                                                                | 217 ms: 1.01x faster                                                        |
| raytrace                 | 276 ms                                                                | 274 ms: 1.01x faster                                                        |
| coroutines               | 23.2 ms                                                               | 23.0 ms: 1.01x faster                                                       |
| xml_etree_generate       | 77.2 ms                                                               | 76.7 ms: 1.01x faster                                                       |
| unpickle_pure_python     | 214 us                                                                | 213 us: 1.00x faster                                                        |
| create_gc_cycles         | 1.74 ms                                                               | 1.73 ms: 1.00x faster                                                       |
| pidigits                 | 186 ms                                                                | 185 ms: 1.00x faster                                                        |
| mako                     | 9.80 ms                                                               | 9.79 ms: 1.00x faster                                                       |
| python_startup           | 10.5 ms                                                               | 10.6 ms: 1.00x slower                                                       |
| python_startup_no_site   | 7.07 ms                                                               | 7.09 ms: 1.00x slower                                                       |
| pickle_pure_python       | 306 us                                                                | 307 us: 1.00x slower                                                        |
| json_loads               | 26.6 us                                                               | 26.8 us: 1.01x slower                                                       |
| sqlite_synth             | 2.72 us                                                               | 2.74 us: 1.01x slower                                                       |
| genshi_xml               | 57.3 ms                                                               | 57.7 ms: 1.01x slower                                                       |
| asyncio_tcp_ssl          | 1.79 sec                                                              | 1.80 sec: 1.01x slower                                                      |
| xml_etree_iterparse      | 97.8 ms                                                               | 98.7 ms: 1.01x slower                                                       |
| telco                    | 7.55 ms                                                               | 7.63 ms: 1.01x slower                                                       |
| gc_traversal             | 3.84 ms                                                               | 3.88 ms: 1.01x slower                                                       |
| genshi_text              | 24.7 ms                                                               | 25.0 ms: 1.01x slower                                                       |
| logging_simple           | 5.54 us                                                               | 5.62 us: 1.01x slower                                                       |
| json                     | 5.02 ms                                                               | 5.10 ms: 1.02x slower                                                       |
| async_generators         | 453 ms                                                                | 461 ms: 1.02x slower                                                        |
| regex_v8                 | 24.6 ms                                                               | 25.1 ms: 1.02x slower                                                       |
| nbody                    | 80.7 ms                                                               | 82.8 ms: 1.03x slower                                                       |
| pickle_list              | 4.92 us                                                               | 5.06 us: 1.03x slower                                                       |
| pickle                   | 11.4 us                                                               | 11.8 us: 1.03x slower                                                       |
| nqueens                  | 85.1 ms                                                               | 89.6 ms: 1.05x slower                                                       |
| Geometric mean           | (ref)                                                                 | 1.01x faster                                                                |

Benchmark hidden because not significant (26): pylint, async_tree_memoization, scimark_sor, async_tree_cpu_io_mixed, pycparser, deepcopy_reduce, json_dumps, chaos, bench_mp_pool, spectral_norm, pathlib, logging_silent, thrift, logging_format, sympy_sum, asyncio_websockets, bench_thread_pool, coverage, async_tree_io, async_tree_io_tg, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, scimark_lu, xml_etree_parse, async_tree_none_tg, async_tree_none
Ignored benchmarks (2) of results/bm-20240929-3.14.0a0-6f4d64b-JIT/bm-20240929-linux-x86_64-python-6f4d64b048133c60d407-3.14.0a0-6f4d64b.json: docutils, sqlglot_optimize

# HPT report

- Reliability score: 99.98% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x