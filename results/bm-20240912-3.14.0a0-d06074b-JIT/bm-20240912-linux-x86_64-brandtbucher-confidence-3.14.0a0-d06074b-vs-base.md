# Results vs. base

- fork: brandtbucher
- ref: confidence
- machine: linux-x86_64
- commit hash: d06074b
- commit date: 2024-09-12
- overall geometric mean: 1.01x faster
- HPT reliability: 99.97%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240912-linux-x86_64-brandtbucher-confidence-3.14.0a0-d06074b |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 276 ms                                                                | 273 ms: 1.01x faster                                              |
| tornado_http   | 94.6 ms                                                               | 94.9 ms: 1.00x slower                                             |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                      |

Benchmark hidden because not significant (2): docutils, html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240912-linux-x86_64-brandtbucher-confidence-3.14.0a0-d06074b |
|------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_generators | 461 ms                                                                | 455 ms: 1.01x faster                                              |
| coroutines       | 22.9 ms                                                               | 22.6 ms: 1.01x faster                                             |
| asyncio_tcp      | 498 ms                                                                | 494 ms: 1.01x faster                                              |
| asyncio_tcp_ssl  | 1.81 sec                                                              | 1.80 sec: 1.00x faster                                            |
| Geometric mean   | (ref)                                                                 | 1.01x faster                                                      |

Benchmark hidden because not significant (9): async_tree_none_tg, async_tree_memoization, async_tree_none, async_tree_memoization_tg, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, asyncio_websockets, async_tree_io, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240912-linux-x86_64-brandtbucher-confidence-3.14.0a0-d06074b |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| nbody          | 80.2 ms                                                               | 79.9 ms: 1.00x faster                                             |
| pidigits       | 185 ms                                                                | 185 ms: 1.00x faster                                              |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                      |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240912-linux-x86_64-brandtbucher-confidence-3.14.0a0-d06074b |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_v8       | 24.7 ms                                                               | 24.4 ms: 1.01x faster                                             |
| regex_compile  | 141 ms                                                                | 140 ms: 1.01x faster                                              |
| regex_effbot   | 3.80 ms                                                               | 3.82 ms: 1.01x slower                                             |
| regex_dna      | 216 ms                                                                | 221 ms: 1.03x slower                                              |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240912-linux-x86_64-brandtbucher-confidence-3.14.0a0-d06074b |
|---------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| xml_etree_generate  | 78.7 ms                                                               | 76.9 ms: 1.02x faster                                             |
| unpickle_list       | 5.17 us                                                               | 5.07 us: 1.02x faster                                             |
| xml_etree_process   | 55.6 ms                                                               | 54.6 ms: 1.02x faster                                             |
| xml_etree_iterparse | 97.9 ms                                                               | 98.3 ms: 1.00x slower                                             |
| pickle              | 11.6 us                                                               | 11.7 us: 1.01x slower                                             |
| pickle_dict         | 34.5 us                                                               | 34.9 us: 1.01x slower                                             |
| pickle_list         | 5.17 us                                                               | 5.24 us: 1.01x slower                                             |
| json_loads          | 26.7 us                                                               | 27.0 us: 1.01x slower                                             |
| Geometric mean      | (ref)                                                                 | 1.00x faster                                                      |

Benchmark hidden because not significant (6): unpickle, pickle_pure_python, json_dumps, unpickle_pure_python, xml_etree_parse, tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240912-linux-x86_64-brandtbucher-confidence-3.14.0a0-d06074b |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup         | 10.5 ms                                                               | 10.5 ms: 1.00x faster                                             |
| python_startup_no_site | 7.07 ms                                                               | 7.04 ms: 1.00x faster                                             |
| Geometric mean         | (ref)                                                                 | 1.00x faster                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240912-linux-x86_64-brandtbucher-confidence-3.14.0a0-d06074b |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| genshi_xml      | 60.0 ms                                                               | 56.4 ms: 1.06x faster                                             |
| genshi_text     | 25.4 ms                                                               | 24.8 ms: 1.03x faster                                             |
| mako            | 9.88 ms                                                               | 9.85 ms: 1.00x faster                                             |
| django_template | 35.3 ms                                                               | 35.9 ms: 1.01x slower                                             |
| Geometric mean  | (ref)                                                                 | 1.02x faster                                                      |

All benchmarks:
===============

| Benchmark                | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240912-linux-x86_64-brandtbucher-confidence-3.14.0a0-d06074b |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| pprint_pformat           | 1.60 sec                                                              | 1.47 sec: 1.09x faster                                            |
| genshi_xml               | 60.0 ms                                                               | 56.4 ms: 1.06x faster                                             |
| pprint_safe_repr         | 748 ms                                                                | 710 ms: 1.05x faster                                              |
| richards_super           | 45.6 ms                                                               | 43.3 ms: 1.05x faster                                             |
| pyflate                  | 448 ms                                                                | 430 ms: 1.04x faster                                              |
| genshi_text              | 25.4 ms                                                               | 24.8 ms: 1.03x faster                                             |
| logging_simple           | 5.75 us                                                               | 5.61 us: 1.02x faster                                             |
| scimark_sparse_mat_mult  | 4.21 ms                                                               | 4.11 ms: 1.02x faster                                             |
| xml_etree_generate       | 78.7 ms                                                               | 76.9 ms: 1.02x faster                                             |
| typing_runtime_protocols | 166 us                                                                | 162 us: 1.02x faster                                              |
| logging_format           | 6.24 us                                                               | 6.11 us: 1.02x faster                                             |
| unpickle_list            | 5.17 us                                                               | 5.07 us: 1.02x faster                                             |
| xml_etree_process        | 55.6 ms                                                               | 54.6 ms: 1.02x faster                                             |
| raytrace                 | 281 ms                                                                | 276 ms: 1.02x faster                                              |
| nqueens                  | 85.5 ms                                                               | 84.1 ms: 1.02x faster                                             |
| richards                 | 39.9 ms                                                               | 39.3 ms: 1.01x faster                                             |
| async_generators         | 461 ms                                                                | 455 ms: 1.01x faster                                              |
| deepcopy_reduce          | 2.68 us                                                               | 2.64 us: 1.01x faster                                             |
| unpack_sequence          | 112 ns                                                                | 111 ns: 1.01x faster                                              |
| coroutines               | 22.9 ms                                                               | 22.6 ms: 1.01x faster                                             |
| sympy_expand             | 506 ms                                                                | 500 ms: 1.01x faster                                              |
| 2to3                     | 276 ms                                                                | 273 ms: 1.01x faster                                              |
| regex_v8                 | 24.7 ms                                                               | 24.4 ms: 1.01x faster                                             |
| regex_compile            | 141 ms                                                                | 140 ms: 1.01x faster                                              |
| scimark_monte_carlo      | 63.0 ms                                                               | 62.3 ms: 1.01x faster                                             |
| meteor_contest           | 107 ms                                                                | 106 ms: 1.01x faster                                              |
| coverage                 | 85.2 ms                                                               | 84.4 ms: 1.01x faster                                             |
| sqlglot_parse            | 1.35 ms                                                               | 1.34 ms: 1.01x faster                                             |
| asyncio_tcp              | 498 ms                                                                | 494 ms: 1.01x faster                                              |
| deepcopy_memo            | 27.2 us                                                               | 27.0 us: 1.01x faster                                             |
| dulwich_log              | 67.8 ms                                                               | 67.3 ms: 1.01x faster                                             |
| scimark_sor              | 117 ms                                                                | 116 ms: 1.01x faster                                              |
| sqlglot_transpile        | 1.69 ms                                                               | 1.68 ms: 1.01x faster                                             |
| asyncio_tcp_ssl          | 1.81 sec                                                              | 1.80 sec: 1.00x faster                                            |
| python_startup           | 10.5 ms                                                               | 10.5 ms: 1.00x faster                                             |
| nbody                    | 80.2 ms                                                               | 79.9 ms: 1.00x faster                                             |
| sympy_sum                | 173 ms                                                                | 172 ms: 1.00x faster                                              |
| python_startup_no_site   | 7.07 ms                                                               | 7.04 ms: 1.00x faster                                             |
| bpe_tokeniser            | 4.44 sec                                                              | 4.43 sec: 1.00x faster                                            |
| mako                     | 9.88 ms                                                               | 9.85 ms: 1.00x faster                                             |
| pidigits                 | 185 ms                                                                | 185 ms: 1.00x faster                                              |
| tornado_http             | 94.6 ms                                                               | 94.9 ms: 1.00x slower                                             |
| scimark_lu               | 110 ms                                                                | 111 ms: 1.00x slower                                              |
| xml_etree_iterparse      | 97.9 ms                                                               | 98.3 ms: 1.00x slower                                             |
| create_gc_cycles         | 1.74 ms                                                               | 1.75 ms: 1.00x slower                                             |
| regex_effbot             | 3.80 ms                                                               | 3.82 ms: 1.01x slower                                             |
| pickle                   | 11.6 us                                                               | 11.7 us: 1.01x slower                                             |
| gc_traversal             | 3.94 ms                                                               | 3.98 ms: 1.01x slower                                             |
| pickle_dict              | 34.5 us                                                               | 34.9 us: 1.01x slower                                             |
| deltablue                | 3.21 ms                                                               | 3.24 ms: 1.01x slower                                             |
| pickle_list              | 5.17 us                                                               | 5.24 us: 1.01x slower                                             |
| sqlite_synth             | 2.74 us                                                               | 2.78 us: 1.01x slower                                             |
| json_loads               | 26.7 us                                                               | 27.0 us: 1.01x slower                                             |
| json                     | 4.94 ms                                                               | 5.01 ms: 1.01x slower                                             |
| django_template          | 35.3 ms                                                               | 35.9 ms: 1.01x slower                                             |
| chaos                    | 58.0 ms                                                               | 59.2 ms: 1.02x slower                                             |
| spectral_norm            | 98.4 ms                                                               | 101 ms: 1.02x slower                                              |
| regex_dna                | 216 ms                                                                | 221 ms: 1.03x slower                                              |
| Geometric mean           | (ref)                                                                 | 1.01x faster                                                      |

Benchmark hidden because not significant (39): async_tree_none_tg, async_tree_memoization, async_tree_none, async_tree_memoization_tg, async_tree_cpu_io_mixed, unpickle, telco, async_tree_cpu_io_mixed_tg, pickle_pure_python, sqlglot_normalize, json_dumps, sympy_integrate, pathlib, sympy_str, asyncio_websockets, thrift, pylint, float, sqlglot_optimize, bench_thread_pool, bench_mp_pool, fannkuch, mdp, generators, docutils, scimark_fft, html5lib, async_tree_io, go, hexiom, unpickle_pure_python, crypto_pyaes, xml_etree_parse, comprehensions, tomli_loads, deepcopy, logging_silent, async_tree_io_tg, pycparser

# HPT report

- Reliability score: 99.97% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x