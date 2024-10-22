# Results vs. base

- fork: mdboom
- ref: cmq_mdboom
- machine: linux-x86_64
- commit hash: 8ca892b
- commit date: 2024-09-26
- overall geometric mean: 1.00x faster
- HPT reliability: 93.58%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240924-linux-x86_64-python-b4d0d7de0f6d938128bf-3.14.0a0-b4d0d7d | bm-20240926-linux-x86_64-mdboom-cmq_mdboom-3.14.0a0-8ca892b |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------:|
| 2to3           | 255 ms                                                                | 253 ms: 1.01x faster                                        |
| docutils       | 2.64 sec                                                              | 2.66 sec: 1.01x slower                                      |
| html5lib       | 63.2 ms                                                               | 63.9 ms: 1.01x slower                                       |
| tornado_http   | 90.7 ms                                                               | 90.4 ms: 1.00x faster                                       |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark          | bm-20240924-linux-x86_64-python-b4d0d7de0f6d938128bf-3.14.0a0-b4d0d7d | bm-20240926-linux-x86_64-mdboom-cmq_mdboom-3.14.0a0-8ca892b |
|--------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------:|
| asyncio_tcp_ssl    | 1.79 sec                                                              | 1.79 sec: 1.00x faster                                      |
| async_generators   | 433 ms                                                                | 434 ms: 1.00x slower                                        |
| asyncio_websockets | 554 ms                                                                | 560 ms: 1.01x slower                                        |
| coroutines         | 23.1 ms                                                               | 23.4 ms: 1.01x slower                                       |
| Geometric mean     | (ref)                                                                 | 1.00x faster                                                |

Benchmark hidden because not significant (9): async_tree_none_tg, async_tree_io_tg, async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_memoization, async_tree_memoization_tg, asyncio_tcp, async_tree_cpu_io_mixed, async_tree_none

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): float, pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240924-linux-x86_64-python-b4d0d7de0f6d938128bf-3.14.0a0-b4d0d7d | bm-20240926-linux-x86_64-mdboom-cmq_mdboom-3.14.0a0-8ca892b |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------:|
| regex_v8       | 25.3 ms                                                               | 24.2 ms: 1.04x faster                                       |
| regex_compile  | 129 ms                                                                | 127 ms: 1.01x faster                                        |
| regex_dna      | 219 ms                                                                | 229 ms: 1.05x slower                                        |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240924-linux-x86_64-python-b4d0d7de0f6d938128bf-3.14.0a0-b4d0d7d | bm-20240926-linux-x86_64-mdboom-cmq_mdboom-3.14.0a0-8ca892b |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------:|
| pickle_dict          | 35.9 us                                                               | 33.9 us: 1.06x faster                                       |
| xml_etree_process    | 59.4 ms                                                               | 58.4 ms: 1.02x faster                                       |
| pickle_list          | 5.18 us                                                               | 5.09 us: 1.02x faster                                       |
| unpickle_pure_python | 216 us                                                                | 214 us: 1.01x faster                                        |
| json_loads           | 27.0 us                                                               | 26.8 us: 1.01x faster                                       |
| xml_etree_generate   | 85.1 ms                                                               | 84.8 ms: 1.00x faster                                       |
| json_dumps           | 10.3 ms                                                               | 10.4 ms: 1.01x slower                                       |
| unpickle_list        | 5.15 us                                                               | 5.24 us: 1.02x slower                                       |
| Geometric mean       | (ref)                                                                 | 1.01x faster                                                |

Benchmark hidden because not significant (6): unpickle, xml_etree_parse, xml_etree_iterparse, pickle, tomli_loads, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240924-linux-x86_64-python-b4d0d7de0f6d938128bf-3.14.0a0-b4d0d7d | bm-20240926-linux-x86_64-mdboom-cmq_mdboom-3.14.0a0-8ca892b |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------:|
| python_startup         | 10.5 ms                                                               | 10.5 ms: 1.00x faster                                       |
| python_startup_no_site | 7.00 ms                                                               | 6.98 ms: 1.00x faster                                       |
| Geometric mean         | (ref)                                                                 | 1.00x faster                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240924-linux-x86_64-python-b4d0d7de0f6d938128bf-3.14.0a0-b4d0d7d | bm-20240926-linux-x86_64-mdboom-cmq_mdboom-3.14.0a0-8ca892b |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------:|
| django_template | 34.7 ms                                                               | 34.0 ms: 1.02x faster                                       |
| genshi_text     | 22.1 ms                                                               | 21.8 ms: 1.02x faster                                       |
| Geometric mean  | (ref)                                                                 | 1.01x faster                                                |

Benchmark hidden because not significant (2): genshi_xml, mako

All benchmarks:
===============

| Benchmark               | bm-20240924-linux-x86_64-python-b4d0d7de0f6d938128bf-3.14.0a0-b4d0d7d | bm-20240926-linux-x86_64-mdboom-cmq_mdboom-3.14.0a0-8ca892b |
|-------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------:|
| pickle_dict             | 35.9 us                                                               | 33.9 us: 1.06x faster                                       |
| pycparser               | 1.17 sec                                                              | 1.12 sec: 1.04x faster                                      |
| regex_v8                | 25.3 ms                                                               | 24.2 ms: 1.04x faster                                       |
| json                    | 5.07 ms                                                               | 4.90 ms: 1.03x faster                                       |
| scimark_fft             | 367 ms                                                                | 358 ms: 1.03x faster                                        |
| go                      | 120 ms                                                                | 117 ms: 1.03x faster                                        |
| django_template         | 34.7 ms                                                               | 34.0 ms: 1.02x faster                                       |
| deepcopy_memo           | 30.2 us                                                               | 29.7 us: 1.02x faster                                       |
| chaos                   | 58.8 ms                                                               | 57.7 ms: 1.02x faster                                       |
| xml_etree_process       | 59.4 ms                                                               | 58.4 ms: 1.02x faster                                       |
| pickle_list             | 5.18 us                                                               | 5.09 us: 1.02x faster                                       |
| scimark_sparse_mat_mult | 4.87 ms                                                               | 4.79 ms: 1.02x faster                                       |
| genshi_text             | 22.1 ms                                                               | 21.8 ms: 1.02x faster                                       |
| scimark_lu              | 114 ms                                                                | 112 ms: 1.02x faster                                        |
| regex_compile           | 129 ms                                                                | 127 ms: 1.01x faster                                        |
| scimark_sor             | 125 ms                                                                | 124 ms: 1.01x faster                                        |
| sqlite_synth            | 2.84 us                                                               | 2.81 us: 1.01x faster                                       |
| dulwich_log             | 65.0 ms                                                               | 64.3 ms: 1.01x faster                                       |
| deltablue               | 3.28 ms                                                               | 3.24 ms: 1.01x faster                                       |
| logging_format          | 6.23 us                                                               | 6.17 us: 1.01x faster                                       |
| create_gc_cycles        | 1.73 ms                                                               | 1.71 ms: 1.01x faster                                       |
| bpe_tokeniser           | 4.81 sec                                                              | 4.77 sec: 1.01x faster                                      |
| unpickle_pure_python    | 216 us                                                                | 214 us: 1.01x faster                                        |
| sqlglot_parse           | 1.29 ms                                                               | 1.28 ms: 1.01x faster                                       |
| 2to3                    | 255 ms                                                                | 253 ms: 1.01x faster                                        |
| logging_simple          | 5.59 us                                                               | 5.55 us: 1.01x faster                                       |
| scimark_monte_carlo     | 67.6 ms                                                               | 67.2 ms: 1.01x faster                                       |
| json_loads              | 27.0 us                                                               | 26.8 us: 1.01x faster                                       |
| richards_super          | 52.5 ms                                                               | 52.2 ms: 1.01x faster                                       |
| raytrace                | 264 ms                                                                | 262 ms: 1.01x faster                                        |
| sqlglot_normalize       | 106 ms                                                                | 106 ms: 1.01x faster                                        |
| bench_thread_pool       | 794 us                                                                | 789 us: 1.01x faster                                        |
| python_startup          | 10.5 ms                                                               | 10.5 ms: 1.00x faster                                       |
| tornado_http            | 90.7 ms                                                               | 90.4 ms: 1.00x faster                                       |
| python_startup_no_site  | 7.00 ms                                                               | 6.98 ms: 1.00x faster                                       |
| xml_etree_generate      | 85.1 ms                                                               | 84.8 ms: 1.00x faster                                       |
| sqlglot_transpile       | 1.58 ms                                                               | 1.57 ms: 1.00x faster                                       |
| hexiom                  | 6.22 ms                                                               | 6.20 ms: 1.00x faster                                       |
| asyncio_tcp_ssl         | 1.79 sec                                                              | 1.79 sec: 1.00x faster                                      |
| sympy_integrate         | 19.6 ms                                                               | 19.5 ms: 1.00x faster                                       |
| async_generators        | 433 ms                                                                | 434 ms: 1.00x slower                                        |
| pprint_safe_repr        | 717 ms                                                                | 721 ms: 1.01x slower                                        |
| json_dumps              | 10.3 ms                                                               | 10.4 ms: 1.01x slower                                       |
| meteor_contest          | 106 ms                                                                | 106 ms: 1.01x slower                                        |
| spectral_norm           | 113 ms                                                                | 114 ms: 1.01x slower                                        |
| docutils                | 2.64 sec                                                              | 2.66 sec: 1.01x slower                                      |
| asyncio_websockets      | 554 ms                                                                | 560 ms: 1.01x slower                                        |
| thrift                  | 766 us                                                                | 774 us: 1.01x slower                                        |
| html5lib                | 63.2 ms                                                               | 63.9 ms: 1.01x slower                                       |
| deepcopy_reduce         | 2.66 us                                                               | 2.69 us: 1.01x slower                                       |
| coroutines              | 23.1 ms                                                               | 23.4 ms: 1.01x slower                                       |
| unpickle_list           | 5.15 us                                                               | 5.24 us: 1.02x slower                                       |
| nqueens                 | 78.8 ms                                                               | 80.4 ms: 1.02x slower                                       |
| fannkuch                | 397 ms                                                                | 405 ms: 1.02x slower                                        |
| gc_traversal            | 3.84 ms                                                               | 3.92 ms: 1.02x slower                                       |
| mdp                     | 2.51 sec                                                              | 2.57 sec: 1.02x slower                                      |
| crypto_pyaes            | 70.9 ms                                                               | 72.7 ms: 1.03x slower                                       |
| pyflate                 | 462 ms                                                                | 476 ms: 1.03x slower                                        |
| regex_dna               | 219 ms                                                                | 229 ms: 1.05x slower                                        |
| coverage                | 85.1 ms                                                               | 89.8 ms: 1.06x slower                                       |
| unpack_sequence         | 49.7 ns                                                               | 53.2 ns: 1.07x slower                                       |
| Geometric mean          | (ref)                                                                 | 1.00x faster                                                |

Benchmark hidden because not significant (36): unpickle, async_tree_none_tg, async_tree_io_tg, async_tree_cpu_io_mixed_tg, xml_etree_parse, typing_runtime_protocols, xml_etree_iterparse, async_tree_io, async_tree_memoization, logging_silent, sympy_str, pathlib, comprehensions, generators, async_tree_memoization_tg, pprint_pformat, regex_effbot, genshi_xml, pickle, float, asyncio_tcp, telco, deepcopy, pidigits, richards, async_tree_cpu_io_mixed, nbody, sqlglot_optimize, sympy_expand, tomli_loads, sympy_sum, bench_mp_pool, mako, pylint, pickle_pure_python, async_tree_none

# HPT report

- Reliability score: 93.58% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x