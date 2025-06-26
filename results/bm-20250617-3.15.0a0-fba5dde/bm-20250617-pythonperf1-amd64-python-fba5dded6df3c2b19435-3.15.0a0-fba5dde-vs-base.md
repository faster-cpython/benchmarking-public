# Results vs. base

- fork: python
- ref: fba5dded6df3c2b19435
- machine: windows-amd64
- commit hash: fba5dde
- commit date: 2025-06-17
- overall geometric mean: 1.010x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250617-pythonperf1-amd64-python-8dd8b5c2f0785675b928-3.15.0a0-8dd8b5c | bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 222 ms                                                                     | 220 ms: 1.01x faster                                                       |
| docutils       | 1.62 sec                                                                   | 1.61 sec: 1.01x faster                                                     |
| html5lib       | 39.0 ms                                                                    | 38.1 ms: 1.02x faster                                                      |
| Geometric mean | (ref)                                                                      | 1.01x faster                                                               |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20250617-pythonperf1-amd64-python-8dd8b5c2f0785675b928-3.15.0a0-8dd8b5c | bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|---------------------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none           | 174 ms                                                                     | 167 ms: 1.04x faster                                                       |
| async_tree_io_tg          | 395 ms                                                                     | 385 ms: 1.02x faster                                                       |
| async_tree_none_tg        | 170 ms                                                                     | 166 ms: 1.02x faster                                                       |
| async_tree_memoization    | 209 ms                                                                     | 206 ms: 1.01x faster                                                       |
| async_tree_memoization_tg | 211 ms                                                                     | 208 ms: 1.01x faster                                                       |
| async_tree_cpu_io_mixed   | 330 ms                                                                     | 328 ms: 1.01x faster                                                       |
| Geometric mean            | (ref)                                                                      | 1.01x faster                                                               |

Benchmark hidden because not significant (5): async_tree_io, async_generators, async_tree_cpu_io_mixed_tg, coroutines, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250617-pythonperf1-amd64-python-8dd8b5c2f0785675b928-3.15.0a0-8dd8b5c | bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 44.1 ms                                                                    | 43.2 ms: 1.02x faster                                                      |
| nbody          | 61.8 ms                                                                    | 60.5 ms: 1.02x faster                                                      |
| Geometric mean | (ref)                                                                      | 1.02x faster                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250617-pythonperf1-amd64-python-8dd8b5c2f0785675b928-3.15.0a0-8dd8b5c | bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 1.61 ms                                                                    | 1.51 ms: 1.06x faster                                                      |
| Geometric mean | (ref)                                                                      | 1.02x faster                                                               |

Benchmark hidden because not significant (3): regex_v8, regex_compile, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250617-pythonperf1-amd64-python-8dd8b5c2f0785675b928-3.15.0a0-8dd8b5c | bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_process    | 39.3 ms                                                                    | 38.5 ms: 1.02x faster                                                      |
| unpickle_pure_python | 133 us                                                                     | 131 us: 1.02x faster                                                       |
| xml_etree_generate   | 56.2 ms                                                                    | 55.4 ms: 1.01x faster                                                      |
| json_dumps           | 6.24 ms                                                                    | 6.16 ms: 1.01x faster                                                      |
| tomli_loads          | 1.37 sec                                                                   | 1.35 sec: 1.01x faster                                                     |
| pickle_pure_python   | 207 us                                                                     | 206 us: 1.01x faster                                                       |
| json_loads           | 14.2 us                                                                    | 14.3 us: 1.01x slower                                                      |
| Geometric mean       | (ref)                                                                      | 1.01x faster                                                               |

Benchmark hidden because not significant (2): xml_etree_parse, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250617-pythonperf1-amd64-python-8dd8b5c2f0785675b928-3.15.0a0-8dd8b5c | bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|-----------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.73 ms                                                                    | 6.57 ms: 1.02x faster                                                      |
| django_template | 24.1 ms                                                                    | 23.6 ms: 1.02x faster                                                      |
| genshi_text     | 15.4 ms                                                                    | 15.1 ms: 1.02x faster                                                      |
| Geometric mean  | (ref)                                                                      | 1.02x faster                                                               |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                 | bm-20250617-pythonperf1-amd64-python-8dd8b5c2f0785675b928-3.15.0a0-8dd8b5c | bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|---------------------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| logging_silent            | 342 ns                                                                     | 318 ns: 1.07x faster                                                       |
| regex_effbot              | 1.61 ms                                                                    | 1.51 ms: 1.06x faster                                                      |
| shortest_path             | 381 ms                                                                     | 362 ms: 1.05x faster                                                       |
| async_tree_none           | 174 ms                                                                     | 167 ms: 1.04x faster                                                       |
| fannkuch                  | 257 ms                                                                     | 247 ms: 1.04x faster                                                       |
| spectral_norm             | 62.1 ms                                                                    | 59.7 ms: 1.04x faster                                                      |
| hexiom                    | 4.02 ms                                                                    | 3.91 ms: 1.03x faster                                                      |
| pyflate                   | 289 ms                                                                     | 281 ms: 1.03x faster                                                       |
| bpe_tokeniser             | 2.97 sec                                                                   | 2.90 sec: 1.02x faster                                                     |
| deepcopy_reduce           | 1.86 us                                                                    | 1.81 us: 1.02x faster                                                      |
| mako                      | 6.73 ms                                                                    | 6.57 ms: 1.02x faster                                                      |
| html5lib                  | 39.0 ms                                                                    | 38.1 ms: 1.02x faster                                                      |
| async_tree_io_tg          | 395 ms                                                                     | 385 ms: 1.02x faster                                                       |
| float                     | 44.1 ms                                                                    | 43.2 ms: 1.02x faster                                                      |
| django_template           | 24.1 ms                                                                    | 23.6 ms: 1.02x faster                                                      |
| create_gc_cycles          | 1.34 ms                                                                    | 1.31 ms: 1.02x faster                                                      |
| generators                | 19.8 ms                                                                    | 19.4 ms: 1.02x faster                                                      |
| nbody                     | 61.8 ms                                                                    | 60.5 ms: 1.02x faster                                                      |
| xml_etree_process         | 39.3 ms                                                                    | 38.5 ms: 1.02x faster                                                      |
| pprint_pformat            | 1.09 sec                                                                   | 1.07 sec: 1.02x faster                                                     |
| async_tree_none_tg        | 170 ms                                                                     | 166 ms: 1.02x faster                                                       |
| unpickle_pure_python      | 133 us                                                                     | 131 us: 1.02x faster                                                       |
| genshi_text               | 15.4 ms                                                                    | 15.1 ms: 1.02x faster                                                      |
| scimark_sparse_mat_mult   | 2.52 ms                                                                    | 2.48 ms: 1.02x faster                                                      |
| chaos                     | 39.9 ms                                                                    | 39.3 ms: 1.02x faster                                                      |
| comprehensions            | 10.8 us                                                                    | 10.6 us: 1.02x faster                                                      |
| pycparser                 | 710 ms                                                                     | 699 ms: 1.02x faster                                                       |
| async_tree_memoization    | 209 ms                                                                     | 206 ms: 1.01x faster                                                       |
| scimark_monte_carlo       | 40.6 ms                                                                    | 40.0 ms: 1.01x faster                                                      |
| xml_etree_generate        | 56.2 ms                                                                    | 55.4 ms: 1.01x faster                                                      |
| deltablue                 | 2.17 ms                                                                    | 2.14 ms: 1.01x faster                                                      |
| thrift                    | 500 us                                                                     | 493 us: 1.01x faster                                                       |
| json_dumps                | 6.24 ms                                                                    | 6.16 ms: 1.01x faster                                                      |
| pprint_safe_repr          | 537 ms                                                                     | 530 ms: 1.01x faster                                                       |
| deepcopy                  | 170 us                                                                     | 168 us: 1.01x faster                                                       |
| go                        | 74.9 ms                                                                    | 74.0 ms: 1.01x faster                                                      |
| async_tree_memoization_tg | 211 ms                                                                     | 208 ms: 1.01x faster                                                       |
| pathlib                   | 32.1 ms                                                                    | 31.8 ms: 1.01x faster                                                      |
| tomli_loads               | 1.37 sec                                                                   | 1.35 sec: 1.01x faster                                                     |
| 2to3                      | 222 ms                                                                     | 220 ms: 1.01x faster                                                       |
| scimark_sor               | 75.0 ms                                                                    | 74.3 ms: 1.01x faster                                                      |
| meteor_contest            | 72.5 ms                                                                    | 71.8 ms: 1.01x faster                                                      |
| crypto_pyaes              | 47.1 ms                                                                    | 46.7 ms: 1.01x faster                                                      |
| richards_super            | 30.5 ms                                                                    | 30.2 ms: 1.01x faster                                                      |
| sympy_integrate           | 12.4 ms                                                                    | 12.3 ms: 1.01x faster                                                      |
| docutils                  | 1.62 sec                                                                   | 1.61 sec: 1.01x faster                                                     |
| telco                     | 4.55 ms                                                                    | 4.52 ms: 1.01x faster                                                      |
| richards                  | 26.8 ms                                                                    | 26.6 ms: 1.01x faster                                                      |
| sqlglot_v2_optimize       | 33.7 ms                                                                    | 33.5 ms: 1.01x faster                                                      |
| mdp                       | 800 ms                                                                     | 794 ms: 1.01x faster                                                       |
| subparsers                | 17.0 ms                                                                    | 16.8 ms: 1.01x faster                                                      |
| nqueens                   | 60.9 ms                                                                    | 60.5 ms: 1.01x faster                                                      |
| pickle_pure_python        | 207 us                                                                     | 206 us: 1.01x faster                                                       |
| logging_format            | 6.77 us                                                                    | 6.73 us: 1.01x faster                                                      |
| sqlite_synth              | 1.59 us                                                                    | 1.58 us: 1.01x faster                                                      |
| async_tree_cpu_io_mixed   | 330 ms                                                                     | 328 ms: 1.01x faster                                                       |
| scimark_lu                | 58.0 ms                                                                    | 57.7 ms: 1.00x faster                                                      |
| logging_simple            | 6.28 us                                                                    | 6.32 us: 1.01x slower                                                      |
| json_loads                | 14.2 us                                                                    | 14.3 us: 1.01x slower                                                      |
| deepcopy_memo             | 17.6 us                                                                    | 17.8 us: 1.01x slower                                                      |
| json                      | 2.97 ms                                                                    | 3.01 ms: 1.01x slower                                                      |
| raytrace                  | 177 ms                                                                     | 180 ms: 1.01x slower                                                       |
| coverage                  | 49.0 ms                                                                    | 50.6 ms: 1.03x slower                                                      |
| Geometric mean            | (ref)                                                                      | 1.01x faster                                                               |

Benchmark hidden because not significant (29): async_tree_io, python_startup_no_site, genshi_xml, sqlglot_v2_parse, sphinx, python_startup, pylint, sqlglot_v2_normalize, connected_components, regex_v8, sqlglot_v2_transpile, pidigits, gc_traversal, regex_compile, dulwich_log, many_optionals, async_generators, sympy_str, xml_etree_parse, async_tree_cpu_io_mixed_tg, regex_dna, sympy_expand, xml_etree_iterparse, coroutines, typing_runtime_protocols, asyncio_websockets, scimark_fft, sympy_sum, k_core

- Geometric mean (including insignificant results): 1.010x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown