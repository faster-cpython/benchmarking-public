# Results vs. base

- fork: brandtbucher
- ref: jit_nops
- machine: windows-amd64
- commit hash: 75922b6
- commit date: 2025-06-27
- overall geometric mean: 1.002x faster
- HPT reliability: 95.77%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

Benchmark hidden because not significant (4): 2to3, docutils, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark              | bm-20250628-pythonperf1-amd64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250627-pythonperf1-amd64-brandtbucher-jit_nops-3.15.0a0-75922b6 |
|------------------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| asyncio_websockets     | 162 ms                                                                     | 157 ms: 1.04x faster                                                 |
| async_tree_io_tg       | 393 ms                                                                     | 387 ms: 1.02x faster                                                 |
| async_tree_memoization | 209 ms                                                                     | 207 ms: 1.01x faster                                                 |
| coroutines             | 15.0 ms                                                                    | 15.2 ms: 1.02x slower                                                |
| async_generators       | 242 ms                                                                     | 250 ms: 1.03x slower                                                 |
| Geometric mean         | (ref)                                                                      | 1.00x faster                                                         |

Benchmark hidden because not significant (6): async_tree_io, async_tree_cpu_io_mixed_tg, async_tree_none_tg, async_tree_none, async_tree_memoization_tg, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250628-pythonperf1-amd64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250627-pythonperf1-amd64-brandtbucher-jit_nops-3.15.0a0-75922b6 |
|----------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| pidigits       | 146 ms                                                                     | 145 ms: 1.00x faster                                                 |
| nbody          | 53.5 ms                                                                    | 54.3 ms: 1.02x slower                                                |
| float          | 44.6 ms                                                                    | 45.5 ms: 1.02x slower                                                |
| Geometric mean | (ref)                                                                      | 1.01x slower                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250628-pythonperf1-amd64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250627-pythonperf1-amd64-brandtbucher-jit_nops-3.15.0a0-75922b6 |
|----------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_effbot   | 1.61 ms                                                                    | 1.54 ms: 1.04x faster                                                |
| regex_dna      | 120 ms                                                                     | 115 ms: 1.04x faster                                                 |
| regex_compile  | 79.8 ms                                                                    | 78.8 ms: 1.01x faster                                                |
| Geometric mean | (ref)                                                                      | 1.03x faster                                                         |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250628-pythonperf1-amd64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250627-pythonperf1-amd64-brandtbucher-jit_nops-3.15.0a0-75922b6 |
|----------------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| xml_etree_parse      | 90.4 ms                                                                    | 88.4 ms: 1.02x faster                                                |
| unpickle_pure_python | 108 us                                                                     | 107 us: 1.01x faster                                                 |
| json_loads           | 14.5 us                                                                    | 14.4 us: 1.01x faster                                                |
| pickle_pure_python   | 204 us                                                                     | 209 us: 1.02x slower                                                 |
| xml_etree_process    | 34.6 ms                                                                    | 35.9 ms: 1.03x slower                                                |
| json_dumps           | 6.28 ms                                                                    | 6.55 ms: 1.04x slower                                                |
| Geometric mean       | (ref)                                                                      | 1.01x slower                                                         |

Benchmark hidden because not significant (3): xml_etree_iterparse, tomli_loads, xml_etree_generate

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250628-pythonperf1-amd64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250627-pythonperf1-amd64-brandtbucher-jit_nops-3.15.0a0-75922b6 |
|-----------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| genshi_xml      | 35.3 ms                                                                    | 34.3 ms: 1.03x faster                                                |
| mako            | 5.54 ms                                                                    | 5.38 ms: 1.03x faster                                                |
| genshi_text     | 15.8 ms                                                                    | 15.6 ms: 1.01x faster                                                |
| django_template | 24.1 ms                                                                    | 24.3 ms: 1.01x slower                                                |
| Geometric mean  | (ref)                                                                      | 1.01x faster                                                         |

All benchmarks:
===============

| Benchmark                | bm-20250628-pythonperf1-amd64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250627-pythonperf1-amd64-brandtbucher-jit_nops-3.15.0a0-75922b6 |
|--------------------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_effbot             | 1.61 ms                                                                    | 1.54 ms: 1.04x faster                                                |
| regex_dna                | 120 ms                                                                     | 115 ms: 1.04x faster                                                 |
| shortest_path            | 374 ms                                                                     | 361 ms: 1.04x faster                                                 |
| asyncio_websockets       | 162 ms                                                                     | 157 ms: 1.04x faster                                                 |
| raytrace                 | 186 ms                                                                     | 180 ms: 1.03x faster                                                 |
| genshi_xml               | 35.3 ms                                                                    | 34.3 ms: 1.03x faster                                                |
| mako                     | 5.54 ms                                                                    | 5.38 ms: 1.03x faster                                                |
| deepcopy                 | 173 us                                                                     | 169 us: 1.03x faster                                                 |
| scimark_lu               | 62.4 ms                                                                    | 60.9 ms: 1.02x faster                                                |
| scimark_sor              | 83.0 ms                                                                    | 81.1 ms: 1.02x faster                                                |
| xml_etree_parse          | 90.4 ms                                                                    | 88.4 ms: 1.02x faster                                                |
| richards                 | 27.7 ms                                                                    | 27.1 ms: 1.02x faster                                                |
| deltablue                | 2.27 ms                                                                    | 2.23 ms: 1.02x faster                                                |
| thrift                   | 500 us                                                                     | 490 us: 1.02x faster                                                 |
| typing_runtime_protocols | 106 us                                                                     | 104 us: 1.02x faster                                                 |
| async_tree_io_tg         | 393 ms                                                                     | 387 ms: 1.02x faster                                                 |
| regex_compile            | 79.8 ms                                                                    | 78.8 ms: 1.01x faster                                                |
| richards_super           | 31.2 ms                                                                    | 30.9 ms: 1.01x faster                                                |
| genshi_text              | 15.8 ms                                                                    | 15.6 ms: 1.01x faster                                                |
| go                       | 79.3 ms                                                                    | 78.6 ms: 1.01x faster                                                |
| unpickle_pure_python     | 108 us                                                                     | 107 us: 1.01x faster                                                 |
| sqlglot_v2_normalize     | 70.9 ms                                                                    | 70.3 ms: 1.01x faster                                                |
| async_tree_memoization   | 209 ms                                                                     | 207 ms: 1.01x faster                                                 |
| comprehensions           | 10.6 us                                                                    | 10.6 us: 1.01x faster                                                |
| coverage                 | 51.0 ms                                                                    | 50.6 ms: 1.01x faster                                                |
| json_loads               | 14.5 us                                                                    | 14.4 us: 1.01x faster                                                |
| nqueens                  | 60.3 ms                                                                    | 60.0 ms: 1.00x faster                                                |
| pidigits                 | 146 ms                                                                     | 145 ms: 1.00x faster                                                 |
| pyflate                  | 257 ms                                                                     | 258 ms: 1.01x slower                                                 |
| generators               | 19.4 ms                                                                    | 19.6 ms: 1.01x slower                                                |
| scimark_sparse_mat_mult  | 2.27 ms                                                                    | 2.29 ms: 1.01x slower                                                |
| bpe_tokeniser            | 2.54 sec                                                                   | 2.57 sec: 1.01x slower                                               |
| chaos                    | 41.2 ms                                                                    | 41.6 ms: 1.01x slower                                                |
| django_template          | 24.1 ms                                                                    | 24.3 ms: 1.01x slower                                                |
| pathlib                  | 31.6 ms                                                                    | 32.0 ms: 1.01x slower                                                |
| fannkuch                 | 224 ms                                                                     | 227 ms: 1.01x slower                                                 |
| nbody                    | 53.5 ms                                                                    | 54.3 ms: 1.02x slower                                                |
| logging_format           | 6.56 us                                                                    | 6.66 us: 1.02x slower                                                |
| coroutines               | 15.0 ms                                                                    | 15.2 ms: 1.02x slower                                                |
| float                    | 44.6 ms                                                                    | 45.5 ms: 1.02x slower                                                |
| meteor_contest           | 71.2 ms                                                                    | 72.6 ms: 1.02x slower                                                |
| sqlite_synth             | 1.55 us                                                                    | 1.58 us: 1.02x slower                                                |
| pickle_pure_python       | 204 us                                                                     | 209 us: 1.02x slower                                                 |
| pprint_pformat           | 915 ms                                                                     | 936 ms: 1.02x slower                                                 |
| spectral_norm            | 64.2 ms                                                                    | 65.9 ms: 1.03x slower                                                |
| async_generators         | 242 ms                                                                     | 250 ms: 1.03x slower                                                 |
| xml_etree_process        | 34.6 ms                                                                    | 35.9 ms: 1.03x slower                                                |
| json                     | 2.94 ms                                                                    | 3.05 ms: 1.04x slower                                                |
| json_dumps               | 6.28 ms                                                                    | 6.55 ms: 1.04x slower                                                |
| Geometric mean           | (ref)                                                                      | 1.00x faster                                                         |

Benchmark hidden because not significant (43): regex_v8, pylint, async_tree_io, sphinx, python_startup, async_tree_cpu_io_mixed_tg, async_tree_none_tg, 2to3, xml_etree_iterparse, python_startup_no_site, sympy_str, sympy_expand, many_optionals, hexiom, async_tree_none, deepcopy_reduce, html5lib, mdp, subparsers, crypto_pyaes, tomli_loads, pycparser, docutils, k_core, scimark_monte_carlo, scimark_fft, dulwich_log, connected_components, sympy_sum, sympy_integrate, logging_silent, logging_simple, sqlglot_v2_parse, async_tree_memoization_tg, gc_traversal, async_tree_cpu_io_mixed, sqlglot_v2_optimize, xml_etree_generate, sqlglot_v2_transpile, create_gc_cycles, deepcopy_memo, telco, pprint_safe_repr

- Geometric mean (including insignificant results): 1.002x faster

# HPT report

- Reliability score: 95.77% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown