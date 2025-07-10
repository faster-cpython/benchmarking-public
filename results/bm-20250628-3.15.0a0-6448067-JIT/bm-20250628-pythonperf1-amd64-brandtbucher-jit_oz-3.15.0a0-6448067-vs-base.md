# Results vs. base

- fork: brandtbucher
- ref: jit_oz
- machine: windows-amd64
- commit hash: 6448067
- commit date: 2025-06-28
- overall geometric mean: 1.004x slower
- HPT reliability: 88.90%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250628-pythonperf1-amd64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250628-pythonperf1-amd64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|----------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 219 ms                                                                     | 218 ms: 1.01x faster                                               |
| docutils       | 1.66 sec                                                                   | 1.64 sec: 1.01x faster                                             |
| html5lib       | 38.8 ms                                                                    | 37.9 ms: 1.02x faster                                              |
| Geometric mean | (ref)                                                                      | 1.01x faster                                                       |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark          | bm-20250628-pythonperf1-amd64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250628-pythonperf1-amd64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|--------------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_io_tg   | 386 ms                                                                     | 392 ms: 1.02x slower                                               |
| async_tree_none_tg | 166 ms                                                                     | 169 ms: 1.02x slower                                               |
| async_generators   | 243 ms                                                                     | 248 ms: 1.02x slower                                               |
| Geometric mean     | (ref)                                                                      | 1.01x slower                                                       |

Benchmark hidden because not significant (8): asyncio_websockets, async_tree_io, coroutines, async_tree_cpu_io_mixed, async_tree_none, async_tree_memoization, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250628-pythonperf1-amd64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250628-pythonperf1-amd64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|----------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------:|
| pidigits       | 145 ms                                                                     | 147 ms: 1.01x slower                                               |
| nbody          | 54.9 ms                                                                    | 56.2 ms: 1.02x slower                                              |
| Geometric mean | (ref)                                                                      | 1.01x slower                                                       |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250628-pythonperf1-amd64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250628-pythonperf1-amd64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|----------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_v8       | 14.1 ms                                                                    | 13.4 ms: 1.06x faster                                              |
| regex_effbot   | 1.59 ms                                                                    | 1.54 ms: 1.04x faster                                              |
| regex_dna      | 119 ms                                                                     | 117 ms: 1.02x faster                                               |
| regex_compile  | 78.7 ms                                                                    | 78.5 ms: 1.00x faster                                              |
| Geometric mean | (ref)                                                                      | 1.03x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250628-pythonperf1-amd64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250628-pythonperf1-amd64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|----------------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------:|
| xml_etree_generate   | 51.3 ms                                                                    | 50.3 ms: 1.02x faster                                              |
| xml_etree_iterparse  | 61.2 ms                                                                    | 62.3 ms: 1.02x slower                                              |
| unpickle_pure_python | 108 us                                                                     | 110 us: 1.02x slower                                               |
| pickle_pure_python   | 203 us                                                                     | 207 us: 1.02x slower                                               |
| json_loads           | 14.3 us                                                                    | 14.7 us: 1.03x slower                                              |
| tomli_loads          | 1.12 sec                                                                   | 1.24 sec: 1.10x slower                                             |
| Geometric mean       | (ref)                                                                      | 1.02x slower                                                       |

Benchmark hidden because not significant (3): xml_etree_process, json_dumps, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20250628-pythonperf1-amd64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250628-pythonperf1-amd64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|----------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup | 25.6 ms                                                                    | 26.0 ms: 1.01x slower                                              |
| Geometric mean | (ref)                                                                      | 1.00x slower                                                       |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250628-pythonperf1-amd64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250628-pythonperf1-amd64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|----------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------:|
| genshi_xml     | 34.8 ms                                                                    | 34.0 ms: 1.02x faster                                              |
| genshi_text    | 15.4 ms                                                                    | 15.5 ms: 1.01x slower                                              |
| mako           | 5.37 ms                                                                    | 5.57 ms: 1.04x slower                                              |
| Geometric mean | (ref)                                                                      | 1.01x slower                                                       |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                | bm-20250628-pythonperf1-amd64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250628-pythonperf1-amd64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|--------------------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------:|
| scimark_lu               | 63.1 ms                                                                    | 58.6 ms: 1.08x faster                                              |
| regex_v8                 | 14.1 ms                                                                    | 13.4 ms: 1.06x faster                                              |
| meteor_contest           | 74.0 ms                                                                    | 71.0 ms: 1.04x faster                                              |
| regex_effbot             | 1.59 ms                                                                    | 1.54 ms: 1.04x faster                                              |
| deepcopy_memo            | 18.2 us                                                                    | 17.6 us: 1.04x faster                                              |
| html5lib                 | 38.8 ms                                                                    | 37.9 ms: 1.02x faster                                              |
| pycparser                | 706 ms                                                                     | 691 ms: 1.02x faster                                               |
| genshi_xml               | 34.8 ms                                                                    | 34.0 ms: 1.02x faster                                              |
| regex_dna                | 119 ms                                                                     | 117 ms: 1.02x faster                                               |
| xml_etree_generate       | 51.3 ms                                                                    | 50.3 ms: 1.02x faster                                              |
| telco                    | 4.44 ms                                                                    | 4.36 ms: 1.02x faster                                              |
| gc_traversal             | 2.12 ms                                                                    | 2.09 ms: 1.02x faster                                              |
| dulwich_log              | 40.9 ms                                                                    | 40.3 ms: 1.01x faster                                              |
| scimark_sparse_mat_mult  | 2.25 ms                                                                    | 2.23 ms: 1.01x faster                                              |
| richards_super           | 31.0 ms                                                                    | 30.7 ms: 1.01x faster                                              |
| richards                 | 27.3 ms                                                                    | 27.0 ms: 1.01x faster                                              |
| docutils                 | 1.66 sec                                                                   | 1.64 sec: 1.01x faster                                             |
| logging_silent           | 55.3 ns                                                                    | 54.8 ns: 1.01x faster                                              |
| mdp                      | 802 ms                                                                     | 795 ms: 1.01x faster                                               |
| 2to3                     | 219 ms                                                                     | 218 ms: 1.01x faster                                               |
| hexiom                   | 4.20 ms                                                                    | 4.17 ms: 1.01x faster                                              |
| connected_components     | 325 ms                                                                     | 323 ms: 1.01x faster                                               |
| sympy_expand             | 293 ms                                                                     | 292 ms: 1.00x faster                                               |
| go                       | 78.1 ms                                                                    | 77.8 ms: 1.00x faster                                              |
| regex_compile            | 78.7 ms                                                                    | 78.5 ms: 1.00x faster                                              |
| crypto_pyaes             | 46.4 ms                                                                    | 46.7 ms: 1.01x slower                                              |
| spectral_norm            | 64.0 ms                                                                    | 64.5 ms: 1.01x slower                                              |
| many_optionals           | 443 us                                                                     | 447 us: 1.01x slower                                               |
| scimark_sor              | 78.5 ms                                                                    | 79.2 ms: 1.01x slower                                              |
| genshi_text              | 15.4 ms                                                                    | 15.5 ms: 1.01x slower                                              |
| sqlglot_v2_optimize      | 34.0 ms                                                                    | 34.3 ms: 1.01x slower                                              |
| generators               | 19.3 ms                                                                    | 19.5 ms: 1.01x slower                                              |
| python_startup           | 25.6 ms                                                                    | 26.0 ms: 1.01x slower                                              |
| typing_runtime_protocols | 103 us                                                                     | 105 us: 1.01x slower                                               |
| pidigits                 | 145 ms                                                                     | 147 ms: 1.01x slower                                               |
| async_tree_io_tg         | 386 ms                                                                     | 392 ms: 1.02x slower                                               |
| sqlglot_v2_parse         | 781 us                                                                     | 794 us: 1.02x slower                                               |
| xml_etree_iterparse      | 61.2 ms                                                                    | 62.3 ms: 1.02x slower                                              |
| sqlglot_v2_transpile     | 980 us                                                                     | 997 us: 1.02x slower                                               |
| coverage                 | 48.8 ms                                                                    | 49.7 ms: 1.02x slower                                              |
| unpickle_pure_python     | 108 us                                                                     | 110 us: 1.02x slower                                               |
| pyflate                  | 253 ms                                                                     | 258 ms: 1.02x slower                                               |
| async_tree_none_tg       | 166 ms                                                                     | 169 ms: 1.02x slower                                               |
| pickle_pure_python       | 203 us                                                                     | 207 us: 1.02x slower                                               |
| async_generators         | 243 ms                                                                     | 248 ms: 1.02x slower                                               |
| nbody                    | 54.9 ms                                                                    | 56.2 ms: 1.02x slower                                              |
| pprint_pformat           | 919 ms                                                                     | 941 ms: 1.02x slower                                               |
| bpe_tokeniser            | 2.65 sec                                                                   | 2.71 sec: 1.03x slower                                             |
| pprint_safe_repr         | 448 ms                                                                     | 460 ms: 1.03x slower                                               |
| nqueens                  | 59.2 ms                                                                    | 60.8 ms: 1.03x slower                                              |
| json_loads               | 14.3 us                                                                    | 14.7 us: 1.03x slower                                              |
| comprehensions           | 10.6 us                                                                    | 11.0 us: 1.04x slower                                              |
| mako                     | 5.37 ms                                                                    | 5.57 ms: 1.04x slower                                              |
| fannkuch                 | 229 ms                                                                     | 242 ms: 1.06x slower                                               |
| scimark_fft              | 151 ms                                                                     | 161 ms: 1.07x slower                                               |
| json                     | 2.97 ms                                                                    | 3.26 ms: 1.10x slower                                              |
| tomli_loads              | 1.12 sec                                                                   | 1.24 sec: 1.10x slower                                             |
| Geometric mean           | (ref)                                                                      | 1.00x slower                                                       |

Benchmark hidden because not significant (35): deltablue, xml_etree_process, logging_simple, python_startup_no_site, asyncio_websockets, async_tree_io, coroutines, thrift, pylint, sphinx, deepcopy, k_core, pathlib, shortest_path, subparsers, float, raytrace, sympy_integrate, sympy_sum, sympy_str, sqlite_synth, async_tree_cpu_io_mixed, async_tree_none, scimark_monte_carlo, json_dumps, django_template, xml_etree_parse, logging_format, create_gc_cycles, chaos, sqlglot_v2_normalize, async_tree_memoization, async_tree_cpu_io_mixed_tg, deepcopy_reduce, async_tree_memoization_tg

- Geometric mean (including insignificant results): 1.004x slower

# HPT report

- Reliability score: 88.90% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown