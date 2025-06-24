# Results vs. base

- fork: brandtbucher
- ref: justin_hot
- machine: windows-amd64
- commit hash: a987be7
- commit date: 2025-06-23
- overall geometric mean: 1.007x faster
- HPT reliability: 97.44%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250610-pythonperf1-amd64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb | bm-20250623-pythonperf1-amd64-brandtbucher-justin_hot-3.15.0a0-a987be7 |
|----------------|:--------------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 221 ms                                                                     | 219 ms: 1.01x faster                                                   |
| sphinx         | 648 ms                                                                     | 640 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                                      | 1.00x faster                                                           |

Benchmark hidden because not significant (2): docutils, html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20250610-pythonperf1-amd64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb | bm-20250623-pythonperf1-amd64-brandtbucher-justin_hot-3.15.0a0-a987be7 |
|-------------------------|:--------------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| coroutines              | 14.5 ms                                                                    | 14.0 ms: 1.03x faster                                                  |
| async_generators        | 245 ms                                                                     | 247 ms: 1.01x slower                                                   |
| async_tree_cpu_io_mixed | 328 ms                                                                     | 330 ms: 1.01x slower                                                   |
| async_tree_io_tg        | 389 ms                                                                     | 392 ms: 1.01x slower                                                   |
| Geometric mean          | (ref)                                                                      | 1.00x faster                                                           |

Benchmark hidden because not significant (7): async_tree_memoization_tg, async_tree_io, async_tree_cpu_io_mixed_tg, async_tree_memoization, async_tree_none_tg, async_tree_none, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250610-pythonperf1-amd64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb | bm-20250623-pythonperf1-amd64-brandtbucher-justin_hot-3.15.0a0-a987be7 |
|----------------|:--------------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 59.7 ms                                                                    | 55.3 ms: 1.08x faster                                                  |
| float          | 44.1 ms                                                                    | 44.7 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                                      | 1.02x faster                                                           |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250610-pythonperf1-amd64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb | bm-20250623-pythonperf1-amd64-brandtbucher-justin_hot-3.15.0a0-a987be7 |
|----------------|:--------------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 79.2 ms                                                                    | 78.3 ms: 1.01x faster                                                  |
| regex_v8       | 14.1 ms                                                                    | 13.9 ms: 1.01x faster                                                  |
| regex_effbot   | 1.60 ms                                                                    | 1.59 ms: 1.00x faster                                                  |
| regex_dna      | 118 ms                                                                     | 119 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                                      | 1.00x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250610-pythonperf1-amd64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb | bm-20250623-pythonperf1-amd64-brandtbucher-justin_hot-3.15.0a0-a987be7 |
|----------------------|:--------------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| unpickle_pure_python | 115 us                                                                     | 109 us: 1.05x faster                                                   |
| xml_etree_process    | 36.4 ms                                                                    | 35.5 ms: 1.03x faster                                                  |
| json_dumps           | 6.30 ms                                                                    | 6.16 ms: 1.02x faster                                                  |
| xml_etree_generate   | 51.4 ms                                                                    | 50.3 ms: 1.02x faster                                                  |
| pickle_pure_python   | 205 us                                                                     | 202 us: 1.02x faster                                                   |
| json_loads           | 14.5 us                                                                    | 14.3 us: 1.01x faster                                                  |
| tomli_loads          | 1.15 sec                                                                   | 1.15 sec: 1.01x faster                                                 |
| Geometric mean       | (ref)                                                                      | 1.02x faster                                                           |

Benchmark hidden because not significant (2): xml_etree_parse, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250610-pythonperf1-amd64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb | bm-20250623-pythonperf1-amd64-brandtbucher-justin_hot-3.15.0a0-a987be7 |
|-----------------|:--------------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 5.63 ms                                                                    | 5.40 ms: 1.04x faster                                                  |
| genshi_text     | 15.7 ms                                                                    | 15.3 ms: 1.03x faster                                                  |
| genshi_xml      | 34.1 ms                                                                    | 34.3 ms: 1.01x slower                                                  |
| django_template | 23.7 ms                                                                    | 24.1 ms: 1.02x slower                                                  |
| Geometric mean  | (ref)                                                                      | 1.01x faster                                                           |

All benchmarks:
===============

| Benchmark               | bm-20250610-pythonperf1-amd64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb | bm-20250623-pythonperf1-amd64-brandtbucher-justin_hot-3.15.0a0-a987be7 |
|-------------------------|:--------------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody                   | 59.7 ms                                                                    | 55.3 ms: 1.08x faster                                                  |
| fannkuch                | 232 ms                                                                     | 215 ms: 1.08x faster                                                   |
| coverage                | 50.8 ms                                                                    | 48.3 ms: 1.05x faster                                                  |
| unpickle_pure_python    | 115 us                                                                     | 109 us: 1.05x faster                                                   |
| mako                    | 5.63 ms                                                                    | 5.40 ms: 1.04x faster                                                  |
| meteor_contest          | 74.9 ms                                                                    | 72.1 ms: 1.04x faster                                                  |
| go                      | 78.1 ms                                                                    | 75.5 ms: 1.03x faster                                                  |
| coroutines              | 14.5 ms                                                                    | 14.0 ms: 1.03x faster                                                  |
| scimark_sparse_mat_mult | 2.30 ms                                                                    | 2.23 ms: 1.03x faster                                                  |
| genshi_text             | 15.7 ms                                                                    | 15.3 ms: 1.03x faster                                                  |
| deepcopy_memo           | 18.3 us                                                                    | 17.8 us: 1.03x faster                                                  |
| xml_etree_process       | 36.4 ms                                                                    | 35.5 ms: 1.03x faster                                                  |
| pprint_pformat          | 1.04 sec                                                                   | 1.01 sec: 1.03x faster                                                 |
| sqlglot_v2_parse        | 797 us                                                                     | 777 us: 1.03x faster                                                   |
| comprehensions          | 10.9 us                                                                    | 10.6 us: 1.03x faster                                                  |
| crypto_pyaes            | 47.0 ms                                                                    | 45.9 ms: 1.03x faster                                                  |
| json_dumps              | 6.30 ms                                                                    | 6.16 ms: 1.02x faster                                                  |
| json                    | 3.08 ms                                                                    | 3.01 ms: 1.02x faster                                                  |
| xml_etree_generate      | 51.4 ms                                                                    | 50.3 ms: 1.02x faster                                                  |
| sqlglot_v2_transpile    | 1.01 ms                                                                    | 990 us: 1.02x faster                                                   |
| hexiom                  | 4.12 ms                                                                    | 4.05 ms: 1.02x faster                                                  |
| logging_format          | 6.71 us                                                                    | 6.59 us: 1.02x faster                                                  |
| pickle_pure_python      | 205 us                                                                     | 202 us: 1.02x faster                                                   |
| richards_super          | 31.0 ms                                                                    | 30.5 ms: 1.02x faster                                                  |
| gc_traversal            | 2.16 ms                                                                    | 2.12 ms: 1.02x faster                                                  |
| deepcopy_reduce         | 1.81 us                                                                    | 1.78 us: 1.02x faster                                                  |
| richards                | 27.3 ms                                                                    | 26.9 ms: 1.01x faster                                                  |
| sphinx                  | 648 ms                                                                     | 640 ms: 1.01x faster                                                   |
| regex_compile           | 79.2 ms                                                                    | 78.3 ms: 1.01x faster                                                  |
| regex_v8                | 14.1 ms                                                                    | 13.9 ms: 1.01x faster                                                  |
| json_loads              | 14.5 us                                                                    | 14.3 us: 1.01x faster                                                  |
| bpe_tokeniser           | 2.62 sec                                                                   | 2.60 sec: 1.01x faster                                                 |
| logging_simple          | 6.26 us                                                                    | 6.21 us: 1.01x faster                                                  |
| deltablue               | 2.23 ms                                                                    | 2.22 ms: 1.01x faster                                                  |
| dulwich_log             | 41.2 ms                                                                    | 40.9 ms: 1.01x faster                                                  |
| 2to3                    | 221 ms                                                                     | 219 ms: 1.01x faster                                                   |
| scimark_fft             | 158 ms                                                                     | 157 ms: 1.01x faster                                                   |
| create_gc_cycles        | 1.34 ms                                                                    | 1.33 ms: 1.01x faster                                                  |
| tomli_loads             | 1.15 sec                                                                   | 1.15 sec: 1.01x faster                                                 |
| scimark_sor             | 76.3 ms                                                                    | 75.9 ms: 1.01x faster                                                  |
| regex_effbot            | 1.60 ms                                                                    | 1.59 ms: 1.00x faster                                                  |
| spectral_norm           | 59.6 ms                                                                    | 59.9 ms: 1.00x slower                                                  |
| sqlglot_v2_optimize     | 34.4 ms                                                                    | 34.5 ms: 1.00x slower                                                  |
| generators              | 19.6 ms                                                                    | 19.7 ms: 1.01x slower                                                  |
| genshi_xml              | 34.1 ms                                                                    | 34.3 ms: 1.01x slower                                                  |
| async_generators        | 245 ms                                                                     | 247 ms: 1.01x slower                                                   |
| async_tree_cpu_io_mixed | 328 ms                                                                     | 330 ms: 1.01x slower                                                   |
| async_tree_io_tg        | 389 ms                                                                     | 392 ms: 1.01x slower                                                   |
| sympy_sum               | 86.4 ms                                                                    | 87.1 ms: 1.01x slower                                                  |
| regex_dna               | 118 ms                                                                     | 119 ms: 1.01x slower                                                   |
| sqlglot_v2_normalize    | 70.2 ms                                                                    | 70.9 ms: 1.01x slower                                                  |
| chaos                   | 39.9 ms                                                                    | 40.4 ms: 1.01x slower                                                  |
| float                   | 44.1 ms                                                                    | 44.7 ms: 1.01x slower                                                  |
| subparsers              | 16.9 ms                                                                    | 17.2 ms: 1.02x slower                                                  |
| shortest_path           | 356 ms                                                                     | 362 ms: 1.02x slower                                                   |
| django_template         | 23.7 ms                                                                    | 24.1 ms: 1.02x slower                                                  |
| nqueens                 | 59.1 ms                                                                    | 60.1 ms: 1.02x slower                                                  |
| thrift                  | 487 us                                                                     | 497 us: 1.02x slower                                                   |
| raytrace                | 177 ms                                                                     | 182 ms: 1.03x slower                                                   |
| scimark_monte_carlo     | 40.0 ms                                                                    | 41.2 ms: 1.03x slower                                                  |
| scimark_lu              | 58.4 ms                                                                    | 62.8 ms: 1.08x slower                                                  |
| Geometric mean          | (ref)                                                                      | 1.01x faster                                                           |

Benchmark hidden because not significant (31): pyflate, async_tree_memoization_tg, pylint, python_startup_no_site, pycparser, pathlib, async_tree_io, sqlite_synth, telco, k_core, sympy_expand, docutils, sympy_integrate, sympy_str, many_optionals, connected_components, xml_etree_parse, typing_runtime_protocols, async_tree_cpu_io_mixed_tg, async_tree_memoization, logging_silent, pidigits, python_startup, deepcopy, async_tree_none_tg, html5lib, async_tree_none, mdp, xml_etree_iterparse, pprint_safe_repr, asyncio_websockets

- Geometric mean (including insignificant results): 1.007x faster

# HPT report

- Reliability score: 97.44% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown