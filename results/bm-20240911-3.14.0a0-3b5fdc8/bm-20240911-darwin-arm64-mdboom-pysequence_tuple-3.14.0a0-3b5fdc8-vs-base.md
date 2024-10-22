# Results vs. base

- fork: mdboom
- ref: pysequence_tuple
- machine: darwin-arm64
- commit hash: 3b5fdc8
- commit date: 2024-09-11
- overall geometric mean: 1.00x faster
- HPT reliability: 80.53%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240911-darwin-arm64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b | bm-20240911-darwin-arm64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 160 ms                                                                | 158 ms: 1.02x faster                                              |
| html5lib       | 30.1 ms                                                               | 30.3 ms: 1.01x slower                                             |
| Geometric mean | (ref)                                                                 | 1.03x faster                                                      |

Benchmark hidden because not significant (2): docutils, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark           | bm-20240911-darwin-arm64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b | bm-20240911-darwin-arm64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|---------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_io       | 585 ms                                                                | 581 ms: 1.01x faster                                              |
| async_generators    | 280 ms                                                                | 279 ms: 1.00x faster                                              |
| coroutines          | 16.0 ms                                                               | 16.1 ms: 1.00x slower                                             |
| async_tree_eager    | 60.7 ms                                                               | 61.1 ms: 1.01x slower                                             |
| async_tree_eager_tg | 42.1 ms                                                               | 42.5 ms: 1.01x slower                                             |
| Geometric mean      | (ref)                                                                 | 1.00x slower                                                      |

Benchmark hidden because not significant (16): async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_memoization_tg, async_tree_none, asyncio_websockets, async_tree_none_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_memoization, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_memoization, async_tree_eager_cpu_io_mixed, asyncio_tcp_ssl, asyncio_tcp, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240911-darwin-arm64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b | bm-20240911-darwin-arm64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| nbody          | 59.6 ms                                                               | 60.7 ms: 1.02x slower                                             |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                      |

Benchmark hidden because not significant (2): float, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240911-darwin-arm64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b | bm-20240911-darwin-arm64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_compile  | 67.1 ms                                                               | 67.2 ms: 1.00x slower                                             |
| regex_v8       | 16.4 ms                                                               | 16.6 ms: 1.01x slower                                             |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                      |

Benchmark hidden because not significant (2): regex_effbot, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240911-darwin-arm64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b | bm-20240911-darwin-arm64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| pickle_pure_python   | 184 us                                                                | 182 us: 1.01x faster                                              |
| unpickle_list        | 2.93 us                                                               | 2.91 us: 1.01x faster                                             |
| unpickle             | 9.27 us                                                               | 9.21 us: 1.01x faster                                             |
| json_dumps           | 6.44 ms                                                               | 6.41 ms: 1.00x faster                                             |
| unpickle_pure_python | 141 us                                                                | 141 us: 1.00x slower                                              |
| json_loads           | 17.1 us                                                               | 17.1 us: 1.00x slower                                             |
| xml_etree_process    | 37.2 ms                                                               | 37.4 ms: 1.01x slower                                             |
| xml_etree_parse      | 107 ms                                                                | 109 ms: 1.02x slower                                              |
| Geometric mean       | (ref)                                                                 | 1.00x faster                                                      |

Benchmark hidden because not significant (6): tomli_loads, xml_etree_iterparse, pickle_dict, pickle, xml_etree_generate, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240911-darwin-arm64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b | bm-20240911-darwin-arm64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup_no_site | 13.8 ms                                                               | 13.7 ms: 1.01x faster                                             |
| python_startup         | 16.8 ms                                                               | 17.0 ms: 1.01x slower                                             |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240911-darwin-arm64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b | bm-20240911-darwin-arm64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| mako            | 7.06 ms                                                               | 7.00 ms: 1.01x faster                                             |
| django_template | 19.7 ms                                                               | 19.6 ms: 1.01x faster                                             |
| genshi_xml      | 30.4 ms                                                               | 30.5 ms: 1.00x slower                                             |
| genshi_text     | 13.9 ms                                                               | 14.0 ms: 1.01x slower                                             |
| Geometric mean  | (ref)                                                                 | 1.00x faster                                                      |

All benchmarks:
===============

| Benchmark               | bm-20240911-darwin-arm64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b | bm-20240911-darwin-arm64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|-------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| richards_super          | 35.1 ms                                                               | 33.5 ms: 1.05x faster                                             |
| richards                | 31.4 ms                                                               | 30.3 ms: 1.04x faster                                             |
| 2to3                    | 160 ms                                                                | 158 ms: 1.02x faster                                              |
| pprint_pformat          | 933 ms                                                                | 919 ms: 1.02x faster                                              |
| logging_format          | 3.37 us                                                               | 3.32 us: 1.01x faster                                             |
| pprint_safe_repr        | 454 ms                                                                | 448 ms: 1.01x faster                                              |
| logging_simple          | 3.05 us                                                               | 3.01 us: 1.01x faster                                             |
| mdp                     | 1.43 sec                                                              | 1.42 sec: 1.01x faster                                            |
| pickle_pure_python      | 184 us                                                                | 182 us: 1.01x faster                                              |
| deltablue               | 2.14 ms                                                               | 2.13 ms: 1.01x faster                                             |
| mako                    | 7.06 ms                                                               | 7.00 ms: 1.01x faster                                             |
| async_tree_io           | 585 ms                                                                | 581 ms: 1.01x faster                                              |
| unpickle_list           | 2.93 us                                                               | 2.91 us: 1.01x faster                                             |
| deepcopy_reduce         | 1.52 us                                                               | 1.51 us: 1.01x faster                                             |
| django_template         | 19.7 ms                                                               | 19.6 ms: 1.01x faster                                             |
| thrift                  | 428 us                                                                | 425 us: 1.01x faster                                              |
| sqlglot_normalize       | 168 ms                                                                | 167 ms: 1.01x faster                                              |
| unpickle                | 9.27 us                                                               | 9.21 us: 1.01x faster                                             |
| fannkuch                | 262 ms                                                                | 260 ms: 1.01x faster                                              |
| bench_thread_pool       | 451 us                                                                | 449 us: 1.01x faster                                              |
| raytrace                | 149 ms                                                                | 148 ms: 1.01x faster                                              |
| python_startup_no_site  | 13.8 ms                                                               | 13.7 ms: 1.01x faster                                             |
| json_dumps              | 6.44 ms                                                               | 6.41 ms: 1.00x faster                                             |
| deepcopy                | 145 us                                                                | 145 us: 1.00x faster                                              |
| async_generators        | 280 ms                                                                | 279 ms: 1.00x faster                                              |
| sympy_expand            | 227 ms                                                                | 226 ms: 1.00x faster                                              |
| chaos                   | 35.0 ms                                                               | 34.9 ms: 1.00x faster                                             |
| deepcopy_memo           | 16.5 us                                                               | 16.5 us: 1.00x faster                                             |
| crypto_pyaes            | 50.3 ms                                                               | 50.2 ms: 1.00x faster                                             |
| dulwich_log             | 27.2 ms                                                               | 27.1 ms: 1.00x faster                                             |
| logging_silent          | 60.6 ns                                                               | 60.5 ns: 1.00x faster                                             |
| meteor_contest          | 71.6 ms                                                               | 71.5 ms: 1.00x faster                                             |
| regex_compile           | 67.1 ms                                                               | 67.2 ms: 1.00x slower                                             |
| coroutines              | 16.0 ms                                                               | 16.1 ms: 1.00x slower                                             |
| comprehensions          | 9.98 us                                                               | 10.0 us: 1.00x slower                                             |
| sqlite_synth            | 1.55 us                                                               | 1.56 us: 1.00x slower                                             |
| gc_traversal            | 2.45 ms                                                               | 2.45 ms: 1.00x slower                                             |
| unpickle_pure_python    | 141 us                                                                | 141 us: 1.00x slower                                              |
| generators              | 20.3 ms                                                               | 20.4 ms: 1.00x slower                                             |
| json_loads              | 17.1 us                                                               | 17.1 us: 1.00x slower                                             |
| genshi_xml              | 30.4 ms                                                               | 30.5 ms: 1.00x slower                                             |
| scimark_sor             | 92.8 ms                                                               | 93.2 ms: 1.00x slower                                             |
| scimark_monte_carlo     | 43.1 ms                                                               | 43.4 ms: 1.00x slower                                             |
| html5lib                | 30.1 ms                                                               | 30.3 ms: 1.01x slower                                             |
| xml_etree_process       | 37.2 ms                                                               | 37.4 ms: 1.01x slower                                             |
| spectral_norm           | 66.9 ms                                                               | 67.3 ms: 1.01x slower                                             |
| async_tree_eager        | 60.7 ms                                                               | 61.1 ms: 1.01x slower                                             |
| telco                   | 4.78 ms                                                               | 4.81 ms: 1.01x slower                                             |
| coverage                | 44.1 ms                                                               | 44.4 ms: 1.01x slower                                             |
| scimark_fft             | 185 ms                                                                | 186 ms: 1.01x slower                                              |
| pathlib                 | 23.7 ms                                                               | 23.8 ms: 1.01x slower                                             |
| async_tree_eager_tg     | 42.1 ms                                                               | 42.5 ms: 1.01x slower                                             |
| python_startup          | 16.8 ms                                                               | 17.0 ms: 1.01x slower                                             |
| genshi_text             | 13.9 ms                                                               | 14.0 ms: 1.01x slower                                             |
| hexiom                  | 4.06 ms                                                               | 4.11 ms: 1.01x slower                                             |
| regex_v8                | 16.4 ms                                                               | 16.6 ms: 1.01x slower                                             |
| scimark_sparse_mat_mult | 2.78 ms                                                               | 2.82 ms: 1.01x slower                                             |
| scimark_lu              | 66.6 ms                                                               | 67.7 ms: 1.02x slower                                             |
| nbody                   | 59.6 ms                                                               | 60.7 ms: 1.02x slower                                             |
| xml_etree_parse         | 107 ms                                                                | 109 ms: 1.02x slower                                              |
| unpack_sequence         | 26.6 ns                                                               | 27.4 ns: 1.03x slower                                             |
| Geometric mean          | (ref)                                                                 | 1.00x faster                                                      |

Benchmark hidden because not significant (44): tornado_http, pycparser, sympy_integrate, sympy_sum, tomli_loads, pylint, xml_etree_iterparse, json, async_tree_cpu_io_mixed_tg, pickle_dict, pickle, nqueens, async_tree_cpu_io_mixed, sympy_str, async_tree_memoization_tg, docutils, create_gc_cycles, bpe_tokeniser, sqlglot_parse, xml_etree_generate, async_tree_none, asyncio_websockets, regex_effbot, sqlglot_optimize, go, async_tree_none_tg, async_tree_eager_cpu_io_mixed_tg, float, pickle_list, bench_mp_pool, regex_dna, async_tree_eager_memoization, async_tree_eager_io, async_tree_eager_io_tg, pidigits, async_tree_eager_memoization_tg, typing_runtime_protocols, sqlglot_transpile, async_tree_memoization, async_tree_eager_cpu_io_mixed, pyflate, asyncio_tcp_ssl, asyncio_tcp, async_tree_io_tg

# HPT report

- Reliability score: 80.53% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x