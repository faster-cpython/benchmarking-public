# Results vs. base

- fork: brandtbucher
- ref: jit_off
- machine: linux-x86_64
- commit hash: 1f40ea4
- commit date: 2025-01-08
- overall geometric mean: 1.002x slower
- HPT reliability: 96.67%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250106-pythonperf2-x86_64-python-7363476b6405e3d288a6-3.14.0a3+-7363476 | bm-20250108-pythonperf2-x86_64-brandtbucher-jit_off-3.14.0a3+-1f40ea4 |
|----------------|:----------------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 279 ms                                                                       | 282 ms: 1.01x slower                                                  |
| docutils       | 2.88 sec                                                                     | 2.90 sec: 1.01x slower                                                |
| Geometric mean | (ref)                                                                        | 1.01x slower                                                          |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark          | bm-20250106-pythonperf2-x86_64-python-7363476b6405e3d288a6-3.14.0a3+-7363476 | bm-20250108-pythonperf2-x86_64-brandtbucher-jit_off-3.14.0a3+-1f40ea4 |
|--------------------|:----------------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io_tg   | 634 ms                                                                       | 623 ms: 1.02x faster                                                  |
| asyncio_websockets | 392 ms                                                                       | 385 ms: 1.02x faster                                                  |
| coroutines         | 20.9 ms                                                                      | 20.8 ms: 1.00x faster                                                 |
| Geometric mean     | (ref)                                                                        | 1.00x faster                                                          |

Benchmark hidden because not significant (8): async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_memoization_tg, async_tree_io, async_generators, async_tree_memoization, async_tree_none_tg, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250106-pythonperf2-x86_64-python-7363476b6405e3d288a6-3.14.0a3+-7363476 | bm-20250108-pythonperf2-x86_64-brandtbucher-jit_off-3.14.0a3+-1f40ea4 |
|----------------|:----------------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 72.2 ms                                                                      | 73.0 ms: 1.01x slower                                                 |
| nbody          | 86.6 ms                                                                      | 89.3 ms: 1.03x slower                                                 |
| Geometric mean | (ref)                                                                        | 1.01x slower                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250106-pythonperf2-x86_64-python-7363476b6405e3d288a6-3.14.0a3+-7363476 | bm-20250108-pythonperf2-x86_64-brandtbucher-jit_off-3.14.0a3+-1f40ea4 |
|----------------|:----------------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_dna      | 234 ms                                                                       | 233 ms: 1.01x faster                                                  |
| regex_compile  | 134 ms                                                                       | 135 ms: 1.01x slower                                                  |
| regex_effbot   | 3.11 ms                                                                      | 3.15 ms: 1.01x slower                                                 |
| regex_v8       | 24.9 ms                                                                      | 25.8 ms: 1.03x slower                                                 |
| Geometric mean | (ref)                                                                        | 1.01x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250106-pythonperf2-x86_64-python-7363476b6405e3d288a6-3.14.0a3+-7363476 | bm-20250108-pythonperf2-x86_64-brandtbucher-jit_off-3.14.0a3+-1f40ea4 |
|----------------------|:----------------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| json_loads           | 24.6 us                                                                      | 24.0 us: 1.03x faster                                                 |
| xml_etree_generate   | 83.5 ms                                                                      | 82.2 ms: 1.02x faster                                                 |
| tomli_loads          | 2.03 sec                                                                     | 2.05 sec: 1.01x slower                                                |
| pickle_pure_python   | 325 us                                                                       | 328 us: 1.01x slower                                                  |
| xml_etree_iterparse  | 95.1 ms                                                                      | 96.4 ms: 1.01x slower                                                 |
| json_dumps           | 11.4 ms                                                                      | 11.5 ms: 1.01x slower                                                 |
| unpickle_pure_python | 203 us                                                                       | 207 us: 1.02x slower                                                  |
| Geometric mean       | (ref)                                                                        | 1.00x slower                                                          |

Benchmark hidden because not significant (2): xml_etree_parse, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250106-pythonperf2-x86_64-python-7363476b6405e3d288a6-3.14.0a3+-7363476 | bm-20250108-pythonperf2-x86_64-brandtbucher-jit_off-3.14.0a3+-1f40ea4 |
|------------------------|:----------------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 8.99 ms                                                                      | 9.03 ms: 1.00x slower                                                 |
| python_startup         | 16.0 ms                                                                      | 16.1 ms: 1.00x slower                                                 |
| Geometric mean         | (ref)                                                                        | 1.00x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250106-pythonperf2-x86_64-python-7363476b6405e3d288a6-3.14.0a3+-7363476 | bm-20250108-pythonperf2-x86_64-brandtbucher-jit_off-3.14.0a3+-1f40ea4 |
|-----------------|:----------------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_xml      | 53.0 ms                                                                      | 51.8 ms: 1.02x faster                                                 |
| django_template | 35.9 ms                                                                      | 35.7 ms: 1.01x faster                                                 |
| Geometric mean  | (ref)                                                                        | 1.01x faster                                                          |

Benchmark hidden because not significant (2): genshi_text, mako

All benchmarks:
===============

| Benchmark               | bm-20250106-pythonperf2-x86_64-python-7363476b6405e3d288a6-3.14.0a3+-7363476 | bm-20250108-pythonperf2-x86_64-brandtbucher-jit_off-3.14.0a3+-1f40ea4 |
|-------------------------|:----------------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| scimark_sor             | 115 ms                                                                       | 110 ms: 1.04x faster                                                  |
| coverage                | 80.4 ms                                                                      | 77.7 ms: 1.03x faster                                                 |
| nqueens                 | 92.5 ms                                                                      | 90.1 ms: 1.03x faster                                                 |
| json_loads              | 24.6 us                                                                      | 24.0 us: 1.03x faster                                                 |
| genshi_xml              | 53.0 ms                                                                      | 51.8 ms: 1.02x faster                                                 |
| async_tree_io_tg        | 634 ms                                                                       | 623 ms: 1.02x faster                                                  |
| mdp                     | 2.51 sec                                                                     | 2.47 sec: 1.02x faster                                                |
| xml_etree_generate      | 83.5 ms                                                                      | 82.2 ms: 1.02x faster                                                 |
| asyncio_websockets      | 392 ms                                                                       | 385 ms: 1.02x faster                                                  |
| meteor_contest          | 126 ms                                                                       | 125 ms: 1.01x faster                                                  |
| comprehensions          | 17.8 us                                                                      | 17.6 us: 1.01x faster                                                 |
| deepcopy_memo           | 29.6 us                                                                      | 29.4 us: 1.01x faster                                                 |
| pycparser               | 1.24 sec                                                                     | 1.23 sec: 1.01x faster                                                |
| richards                | 46.8 ms                                                                      | 46.4 ms: 1.01x faster                                                 |
| pprint_safe_repr        | 776 ms                                                                       | 770 ms: 1.01x faster                                                  |
| django_template         | 35.9 ms                                                                      | 35.7 ms: 1.01x faster                                                 |
| regex_dna               | 234 ms                                                                       | 233 ms: 1.01x faster                                                  |
| pprint_pformat          | 1.58 sec                                                                     | 1.57 sec: 1.01x faster                                                |
| bpe_tokeniser           | 4.71 sec                                                                     | 4.69 sec: 1.01x faster                                                |
| connected_components    | 417 ms                                                                       | 415 ms: 1.00x faster                                                  |
| scimark_sparse_mat_mult | 4.61 ms                                                                      | 4.59 ms: 1.00x faster                                                 |
| coroutines              | 20.9 ms                                                                      | 20.8 ms: 1.00x faster                                                 |
| spectral_norm           | 87.2 ms                                                                      | 87.5 ms: 1.00x slower                                                 |
| python_startup_no_site  | 8.99 ms                                                                      | 9.03 ms: 1.00x slower                                                 |
| crypto_pyaes            | 73.0 ms                                                                      | 73.3 ms: 1.00x slower                                                 |
| python_startup          | 16.0 ms                                                                      | 16.1 ms: 1.00x slower                                                 |
| scimark_monte_carlo     | 62.1 ms                                                                      | 62.4 ms: 1.01x slower                                                 |
| sympy_integrate         | 23.1 ms                                                                      | 23.2 ms: 1.01x slower                                                 |
| subparsers              | 22.7 ms                                                                      | 22.8 ms: 1.01x slower                                                 |
| docutils                | 2.88 sec                                                                     | 2.90 sec: 1.01x slower                                                |
| hexiom                  | 6.05 ms                                                                      | 6.09 ms: 1.01x slower                                                 |
| sqlalchemy_declarative  | 142 ms                                                                       | 143 ms: 1.01x slower                                                  |
| chaos                   | 62.6 ms                                                                      | 63.0 ms: 1.01x slower                                                 |
| tomli_loads             | 2.03 sec                                                                     | 2.05 sec: 1.01x slower                                                |
| pickle_pure_python      | 325 us                                                                       | 328 us: 1.01x slower                                                  |
| sqlglot_parse           | 1.32 ms                                                                      | 1.33 ms: 1.01x slower                                                 |
| regex_compile           | 134 ms                                                                       | 135 ms: 1.01x slower                                                  |
| sqlglot_transpile       | 1.71 ms                                                                      | 1.72 ms: 1.01x slower                                                 |
| sympy_sum               | 151 ms                                                                       | 152 ms: 1.01x slower                                                  |
| sqlalchemy_imperative   | 17.8 ms                                                                      | 18.0 ms: 1.01x slower                                                 |
| sqlglot_optimize        | 57.1 ms                                                                      | 57.6 ms: 1.01x slower                                                 |
| 2to3                    | 279 ms                                                                       | 282 ms: 1.01x slower                                                  |
| go                      | 127 ms                                                                       | 128 ms: 1.01x slower                                                  |
| scimark_fft             | 301 ms                                                                       | 304 ms: 1.01x slower                                                  |
| deepcopy_reduce         | 2.93 us                                                                      | 2.96 us: 1.01x slower                                                 |
| float                   | 72.2 ms                                                                      | 73.0 ms: 1.01x slower                                                 |
| regex_effbot            | 3.11 ms                                                                      | 3.15 ms: 1.01x slower                                                 |
| richards_super          | 52.5 ms                                                                      | 53.1 ms: 1.01x slower                                                 |
| deltablue               | 3.36 ms                                                                      | 3.40 ms: 1.01x slower                                                 |
| sympy_str               | 289 ms                                                                       | 293 ms: 1.01x slower                                                  |
| xml_etree_iterparse     | 95.1 ms                                                                      | 96.4 ms: 1.01x slower                                                 |
| pathlib                 | 15.8 ms                                                                      | 16.1 ms: 1.01x slower                                                 |
| many_optionals          | 1.02 ms                                                                      | 1.03 ms: 1.01x slower                                                 |
| json_dumps              | 11.4 ms                                                                      | 11.5 ms: 1.01x slower                                                 |
| sympy_expand            | 494 ms                                                                       | 502 ms: 1.01x slower                                                  |
| fannkuch                | 352 ms                                                                       | 358 ms: 1.02x slower                                                  |
| gc_traversal            | 6.14 ms                                                                      | 6.25 ms: 1.02x slower                                                 |
| unpickle_pure_python    | 203 us                                                                       | 207 us: 1.02x slower                                                  |
| logging_format          | 6.77 us                                                                      | 6.96 us: 1.03x slower                                                 |
| nbody                   | 86.6 ms                                                                      | 89.3 ms: 1.03x slower                                                 |
| logging_simple          | 6.17 us                                                                      | 6.37 us: 1.03x slower                                                 |
| regex_v8                | 24.9 ms                                                                      | 25.8 ms: 1.03x slower                                                 |
| Geometric mean          | (ref)                                                                        | 1.00x slower                                                          |

Benchmark hidden because not significant (34): bench_mp_pool, create_gc_cycles, sqlite_synth, scimark_lu, thrift, xml_etree_parse, async_tree_cpu_io_mixed_tg, telco, k_core, deepcopy, xml_etree_process, genshi_text, async_tree_cpu_io_mixed, raytrace, async_tree_memoization_tg, logging_silent, async_tree_io, async_generators, shortest_path, dulwich_log, sqlglot_normalize, mako, bench_thread_pool, pidigits, generators, pyflate, async_tree_memoization, html5lib, typing_runtime_protocols, async_tree_none_tg, async_tree_none, json, sphinx, pylint

- Geometric mean (including insignificant results): 1.002x slower

# HPT report

- Reliability score: 96.67% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x