# Results vs. base

- fork: mdboom
- ref: remove_redundant_typ
- machine: linux-x86_64
- commit hash: b0f5f3a
- commit date: 2024-09-23
- overall geometric mean: 1.003x faster
- HPT reliability: 89.29%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240924-pythonperf2-x86_64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 | bm-20240923-pythonperf2-x86_64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 284 ms                                                                      | 283 ms: 1.00x faster                                                        |
| docutils       | 2.90 sec                                                                    | 2.91 sec: 1.00x slower                                                      |
| html5lib       | 71.4 ms                                                                     | 71.8 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                                       | 1.00x slower                                                                |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark      | bm-20240924-pythonperf2-x86_64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 | bm-20240923-pythonperf2-x86_64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| asyncio_tcp    | 369 ms                                                                      | 374 ms: 1.01x slower                                                        |
| coroutines     | 21.6 ms                                                                     | 22.1 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                                       | 1.00x slower                                                                |

Benchmark hidden because not significant (11): async_tree_none, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, async_tree_memoization, async_tree_io, asyncio_tcp_ssl, async_generators, async_tree_cpu_io_mixed, asyncio_websockets, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240924-pythonperf2-x86_64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 | bm-20240923-pythonperf2-x86_64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 79.6 ms                                                                     | 78.7 ms: 1.01x faster                                                       |
| pidigits       | 253 ms                                                                      | 252 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                                       | 1.00x faster                                                                |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240924-pythonperf2-x86_64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 | bm-20240923-pythonperf2-x86_64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 248 ms                                                                      | 235 ms: 1.06x faster                                                        |
| regex_effbot   | 3.58 ms                                                                     | 3.51 ms: 1.02x faster                                                       |
| regex_v8       | 25.5 ms                                                                     | 25.2 ms: 1.01x faster                                                       |
| regex_compile  | 139 ms                                                                      | 138 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                                       | 1.02x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240924-pythonperf2-x86_64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 | bm-20240923-pythonperf2-x86_64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_iterparse  | 103 ms                                                                      | 100 ms: 1.03x faster                                                        |
| pickle_pure_python   | 321 us                                                                      | 315 us: 1.02x faster                                                        |
| tomli_loads          | 2.64 sec                                                                    | 2.59 sec: 1.02x faster                                                      |
| xml_etree_process    | 59.9 ms                                                                     | 59.1 ms: 1.01x faster                                                       |
| unpickle             | 15.1 us                                                                     | 15.0 us: 1.01x faster                                                       |
| xml_etree_parse      | 142 ms                                                                      | 141 ms: 1.01x faster                                                        |
| xml_etree_generate   | 84.8 ms                                                                     | 85.4 ms: 1.01x slower                                                       |
| json_dumps           | 10.8 ms                                                                     | 11.0 ms: 1.02x slower                                                       |
| unpickle_list        | 4.57 us                                                                     | 4.73 us: 1.03x slower                                                       |
| pickle               | 10.2 us                                                                     | 10.7 us: 1.05x slower                                                       |
| unpickle_pure_python | 213 us                                                                      | 224 us: 1.05x slower                                                        |
| pickle_list          | 4.30 us                                                                     | 4.64 us: 1.08x slower                                                       |
| pickle_dict          | 30.0 us                                                                     | 32.7 us: 1.09x slower                                                       |
| Geometric mean       | (ref)                                                                       | 1.02x slower                                                                |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240924-pythonperf2-x86_64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 | bm-20240923-pythonperf2-x86_64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|-----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 24.6 ms                                                                     | 24.1 ms: 1.02x faster                                                       |
| genshi_xml      | 54.4 ms                                                                     | 53.6 ms: 1.02x faster                                                       |
| django_template | 40.8 ms                                                                     | 40.3 ms: 1.01x faster                                                       |
| Geometric mean  | (ref)                                                                       | 1.01x faster                                                                |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark               | bm-20240924-pythonperf2-x86_64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 | bm-20240923-pythonperf2-x86_64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|-------------------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpack_sequence         | 60.1 ns                                                                     | 48.1 ns: 1.25x faster                                                       |
| regex_dna               | 248 ms                                                                      | 235 ms: 1.06x faster                                                        |
| raytrace                | 283 ms                                                                      | 268 ms: 1.05x faster                                                        |
| create_gc_cycles        | 2.01 ms                                                                     | 1.91 ms: 1.05x faster                                                       |
| logging_format          | 7.21 us                                                                     | 6.93 us: 1.04x faster                                                       |
| coverage                | 82.6 ms                                                                     | 80.2 ms: 1.03x faster                                                       |
| generators              | 29.7 ms                                                                     | 28.9 ms: 1.03x faster                                                       |
| xml_etree_iterparse     | 103 ms                                                                      | 100 ms: 1.03x faster                                                        |
| hexiom                  | 6.33 ms                                                                     | 6.19 ms: 1.02x faster                                                       |
| telco                   | 8.29 ms                                                                     | 8.11 ms: 1.02x faster                                                       |
| genshi_text             | 24.6 ms                                                                     | 24.1 ms: 1.02x faster                                                       |
| pickle_pure_python      | 321 us                                                                      | 315 us: 1.02x faster                                                        |
| regex_effbot            | 3.58 ms                                                                     | 3.51 ms: 1.02x faster                                                       |
| logging_simple          | 6.50 us                                                                     | 6.37 us: 1.02x faster                                                       |
| tomli_loads             | 2.64 sec                                                                    | 2.59 sec: 1.02x faster                                                      |
| go                      | 138 ms                                                                      | 136 ms: 1.02x faster                                                        |
| genshi_xml              | 54.4 ms                                                                     | 53.6 ms: 1.02x faster                                                       |
| xml_etree_process       | 59.9 ms                                                                     | 59.1 ms: 1.01x faster                                                       |
| django_template         | 40.8 ms                                                                     | 40.3 ms: 1.01x faster                                                       |
| float                   | 79.6 ms                                                                     | 78.7 ms: 1.01x faster                                                       |
| regex_v8                | 25.5 ms                                                                     | 25.2 ms: 1.01x faster                                                       |
| dulwich_log             | 66.9 ms                                                                     | 66.1 ms: 1.01x faster                                                       |
| deepcopy_reduce         | 2.89 us                                                                     | 2.86 us: 1.01x faster                                                       |
| deepcopy                | 286 us                                                                      | 284 us: 1.01x faster                                                        |
| unpickle                | 15.1 us                                                                     | 15.0 us: 1.01x faster                                                       |
| fannkuch                | 361 ms                                                                      | 359 ms: 1.01x faster                                                        |
| meteor_contest          | 128 ms                                                                      | 128 ms: 1.01x faster                                                        |
| deltablue               | 3.40 ms                                                                     | 3.38 ms: 1.01x faster                                                       |
| pidigits                | 253 ms                                                                      | 252 ms: 1.01x faster                                                        |
| sqlglot_optimize        | 58.3 ms                                                                     | 57.9 ms: 1.01x faster                                                       |
| regex_compile           | 139 ms                                                                      | 138 ms: 1.01x faster                                                        |
| xml_etree_parse         | 142 ms                                                                      | 141 ms: 1.01x faster                                                        |
| sympy_str               | 290 ms                                                                      | 289 ms: 1.00x faster                                                        |
| 2to3                    | 284 ms                                                                      | 283 ms: 1.00x faster                                                        |
| bpe_tokeniser           | 4.89 sec                                                                    | 4.90 sec: 1.00x slower                                                      |
| sympy_integrate         | 22.8 ms                                                                     | 22.9 ms: 1.00x slower                                                       |
| docutils                | 2.90 sec                                                                    | 2.91 sec: 1.00x slower                                                      |
| mdp                     | 2.49 sec                                                                    | 2.50 sec: 1.00x slower                                                      |
| pyflate                 | 487 ms                                                                      | 489 ms: 1.00x slower                                                        |
| json                    | 5.26 ms                                                                     | 5.29 ms: 1.01x slower                                                       |
| html5lib                | 71.4 ms                                                                     | 71.8 ms: 1.01x slower                                                       |
| xml_etree_generate      | 84.8 ms                                                                     | 85.4 ms: 1.01x slower                                                       |
| nqueens                 | 87.6 ms                                                                     | 88.3 ms: 1.01x slower                                                       |
| chaos                   | 62.0 ms                                                                     | 62.6 ms: 1.01x slower                                                       |
| pathlib                 | 15.7 ms                                                                     | 15.8 ms: 1.01x slower                                                       |
| pycparser               | 1.23 sec                                                                    | 1.25 sec: 1.01x slower                                                      |
| sqlite_synth            | 2.73 us                                                                     | 2.76 us: 1.01x slower                                                       |
| richards                | 49.7 ms                                                                     | 50.2 ms: 1.01x slower                                                       |
| pprint_pformat          | 1.64 sec                                                                    | 1.66 sec: 1.01x slower                                                      |
| thrift                  | 863 us                                                                      | 874 us: 1.01x slower                                                        |
| asyncio_tcp             | 369 ms                                                                      | 374 ms: 1.01x slower                                                        |
| scimark_sor             | 115 ms                                                                      | 117 ms: 1.01x slower                                                        |
| json_dumps              | 10.8 ms                                                                     | 11.0 ms: 1.02x slower                                                       |
| scimark_monte_carlo     | 66.0 ms                                                                     | 67.2 ms: 1.02x slower                                                       |
| gc_traversal            | 4.78 ms                                                                     | 4.87 ms: 1.02x slower                                                       |
| scimark_fft             | 298 ms                                                                      | 304 ms: 1.02x slower                                                        |
| logging_silent          | 97.9 ns                                                                     | 100 ns: 1.02x slower                                                        |
| coroutines              | 21.6 ms                                                                     | 22.1 ms: 1.02x slower                                                       |
| crypto_pyaes            | 71.9 ms                                                                     | 73.6 ms: 1.02x slower                                                       |
| scimark_sparse_mat_mult | 4.16 ms                                                                     | 4.26 ms: 1.02x slower                                                       |
| unpickle_list           | 4.57 us                                                                     | 4.73 us: 1.03x slower                                                       |
| bench_mp_pool           | 4.62 ms                                                                     | 4.80 ms: 1.04x slower                                                       |
| pickle                  | 10.2 us                                                                     | 10.7 us: 1.05x slower                                                       |
| unpickle_pure_python    | 213 us                                                                      | 224 us: 1.05x slower                                                        |
| pickle_list             | 4.30 us                                                                     | 4.64 us: 1.08x slower                                                       |
| pickle_dict             | 30.0 us                                                                     | 32.7 us: 1.09x slower                                                       |
| Geometric mean          | (ref)                                                                       | 1.00x faster                                                                |

Benchmark hidden because not significant (31): async_tree_none, sqlglot_parse, async_tree_io_tg, async_tree_memoization_tg, mako, typing_runtime_protocols, async_tree_none_tg, sympy_sum, async_tree_memoization, tornado_http, scimark_lu, pprint_safe_repr, python_startup, comprehensions, deepcopy_memo, pylint, sqlglot_transpile, async_tree_io, asyncio_tcp_ssl, json_loads, async_generators, richards_super, python_startup_no_site, spectral_norm, async_tree_cpu_io_mixed, sympy_expand, sqlglot_normalize, asyncio_websockets, bench_thread_pool, nbody, async_tree_cpu_io_mixed_tg

- Geometric mean (including insignificant results): 1.003x faster
# HPT report

- Reliability score: 89.29% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x