# Results vs. base

- fork: faster-cpython
- ref: check_periodic_at_en
- machine: linux-x86_64
- commit hash: 021fc09
- commit date: 2025-07-25
- overall geometric mean: 1.001x faster
- HPT reliability: 89.01%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250724-pythonperf2-x86_64-python-ae4d27eba7c746463c62-3.15.0a0-ae4d27e | bm-20250725-pythonperf2-x86_64-faster%2dcpython-check_periodic_at_en-3.15.0a0-021fc09 |
|----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| docutils       | 2.91 sec                                                                    | 2.92 sec: 1.00x slower                                                                |
| Geometric mean | (ref)                                                                       | 1.00x slower                                                                          |

Benchmark hidden because not significant (3): 2to3, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20250724-pythonperf2-x86_64-python-ae4d27eba7c746463c62-3.15.0a0-ae4d27e | bm-20250725-pythonperf2-x86_64-faster%2dcpython-check_periodic_at_en-3.15.0a0-021fc09 |
|------------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| async_generators | 452 ms                                                                      | 417 ms: 1.08x faster                                                                  |
| async_tree_io_tg | 636 ms                                                                      | 630 ms: 1.01x faster                                                                  |
| coroutines       | 22.4 ms                                                                     | 22.4 ms: 1.00x faster                                                                 |
| Geometric mean   | (ref)                                                                       | 1.01x faster                                                                          |

Benchmark hidden because not significant (8): async_tree_none, async_tree_io, async_tree_memoization_tg, asyncio_websockets, async_tree_none_tg, async_tree_memoization, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250724-pythonperf2-x86_64-python-ae4d27eba7c746463c62-3.15.0a0-ae4d27e | bm-20250725-pythonperf2-x86_64-faster%2dcpython-check_periodic_at_en-3.15.0a0-021fc09 |
|----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| nbody          | 99.4 ms                                                                     | 97.5 ms: 1.02x faster                                                                 |
| pidigits       | 256 ms                                                                      | 255 ms: 1.00x faster                                                                  |
| Geometric mean | (ref)                                                                       | 1.01x faster                                                                          |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250724-pythonperf2-x86_64-python-ae4d27eba7c746463c62-3.15.0a0-ae4d27e | bm-20250725-pythonperf2-x86_64-faster%2dcpython-check_periodic_at_en-3.15.0a0-021fc09 |
|----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| regex_v8       | 24.4 ms                                                                     | 23.6 ms: 1.03x faster                                                                 |
| regex_compile  | 133 ms                                                                      | 133 ms: 1.00x faster                                                                  |
| regex_effbot   | 3.59 ms                                                                     | 3.73 ms: 1.04x slower                                                                 |
| Geometric mean | (ref)                                                                       | 1.00x slower                                                                          |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250724-pythonperf2-x86_64-python-ae4d27eba7c746463c62-3.15.0a0-ae4d27e | bm-20250725-pythonperf2-x86_64-faster%2dcpython-check_periodic_at_en-3.15.0a0-021fc09 |
|----------------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| xml_etree_parse      | 145 ms                                                                      | 136 ms: 1.07x faster                                                                  |
| xml_etree_iterparse  | 99.1 ms                                                                     | 96.8 ms: 1.02x faster                                                                 |
| xml_etree_process    | 56.0 ms                                                                     | 55.3 ms: 1.01x faster                                                                 |
| tomli_loads          | 1.91 sec                                                                    | 1.89 sec: 1.01x faster                                                                |
| pickle_pure_python   | 331 us                                                                      | 335 us: 1.01x slower                                                                  |
| unpickle_pure_python | 193 us                                                                      | 195 us: 1.01x slower                                                                  |
| json_dumps           | 11.2 ms                                                                     | 11.4 ms: 1.02x slower                                                                 |
| json_loads           | 25.0 us                                                                     | 26.8 us: 1.07x slower                                                                 |
| Geometric mean       | (ref)                                                                       | 1.00x slower                                                                          |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250724-pythonperf2-x86_64-python-ae4d27eba7c746463c62-3.15.0a0-ae4d27e | bm-20250725-pythonperf2-x86_64-faster%2dcpython-check_periodic_at_en-3.15.0a0-021fc09 |
|------------------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| python_startup_no_site | 8.84 ms                                                                     | 8.82 ms: 1.00x faster                                                                 |
| python_startup         | 15.4 ms                                                                     | 15.4 ms: 1.00x faster                                                                 |
| Geometric mean         | (ref)                                                                       | 1.00x faster                                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250724-pythonperf2-x86_64-python-ae4d27eba7c746463c62-3.15.0a0-ae4d27e | bm-20250725-pythonperf2-x86_64-faster%2dcpython-check_periodic_at_en-3.15.0a0-021fc09 |
|-----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| django_template | 35.2 ms                                                                     | 34.7 ms: 1.01x faster                                                                 |
| genshi_xml      | 54.3 ms                                                                     | 54.7 ms: 1.01x slower                                                                 |
| mako            | 9.65 ms                                                                     | 9.95 ms: 1.03x slower                                                                 |
| Geometric mean  | (ref)                                                                       | 1.01x slower                                                                          |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                | bm-20250724-pythonperf2-x86_64-python-ae4d27eba7c746463c62-3.15.0a0-ae4d27e | bm-20250725-pythonperf2-x86_64-faster%2dcpython-check_periodic_at_en-3.15.0a0-021fc09 |
|--------------------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| async_generators         | 452 ms                                                                      | 417 ms: 1.08x faster                                                                  |
| xml_etree_parse          | 145 ms                                                                      | 136 ms: 1.07x faster                                                                  |
| generators               | 30.1 ms                                                                     | 28.4 ms: 1.06x faster                                                                 |
| spectral_norm            | 80.4 ms                                                                     | 77.6 ms: 1.04x faster                                                                 |
| regex_v8                 | 24.4 ms                                                                     | 23.6 ms: 1.03x faster                                                                 |
| scimark_sparse_mat_mult  | 5.09 ms                                                                     | 4.96 ms: 1.03x faster                                                                 |
| go                       | 129 ms                                                                      | 125 ms: 1.03x faster                                                                  |
| xml_etree_iterparse      | 99.1 ms                                                                     | 96.8 ms: 1.02x faster                                                                 |
| richards                 | 35.1 ms                                                                     | 34.3 ms: 1.02x faster                                                                 |
| richards_super           | 40.7 ms                                                                     | 39.9 ms: 1.02x faster                                                                 |
| fannkuch                 | 366 ms                                                                      | 359 ms: 1.02x faster                                                                  |
| nbody                    | 99.4 ms                                                                     | 97.5 ms: 1.02x faster                                                                 |
| django_template          | 35.2 ms                                                                     | 34.7 ms: 1.01x faster                                                                 |
| chaos                    | 59.6 ms                                                                     | 58.9 ms: 1.01x faster                                                                 |
| xml_etree_process        | 56.0 ms                                                                     | 55.3 ms: 1.01x faster                                                                 |
| mdp                      | 1.29 sec                                                                    | 1.27 sec: 1.01x faster                                                                |
| scimark_sor              | 102 ms                                                                      | 101 ms: 1.01x faster                                                                  |
| tomli_loads              | 1.91 sec                                                                    | 1.89 sec: 1.01x faster                                                                |
| async_tree_io_tg         | 636 ms                                                                      | 630 ms: 1.01x faster                                                                  |
| scimark_fft              | 301 ms                                                                      | 298 ms: 1.01x faster                                                                  |
| comprehensions           | 17.3 us                                                                     | 17.2 us: 1.01x faster                                                                 |
| pathlib                  | 17.0 ms                                                                     | 16.8 ms: 1.01x faster                                                                 |
| deepcopy_reduce          | 2.99 us                                                                     | 2.97 us: 1.01x faster                                                                 |
| deepcopy                 | 279 us                                                                      | 277 us: 1.01x faster                                                                  |
| hexiom                   | 6.20 ms                                                                     | 6.17 ms: 1.00x faster                                                                 |
| python_startup_no_site   | 8.84 ms                                                                     | 8.82 ms: 1.00x faster                                                                 |
| python_startup           | 15.4 ms                                                                     | 15.4 ms: 1.00x faster                                                                 |
| pidigits                 | 256 ms                                                                      | 255 ms: 1.00x faster                                                                  |
| coroutines               | 22.4 ms                                                                     | 22.4 ms: 1.00x faster                                                                 |
| regex_compile            | 133 ms                                                                      | 133 ms: 1.00x faster                                                                  |
| sqlglot_v2_optimize      | 57.4 ms                                                                     | 57.3 ms: 1.00x faster                                                                 |
| crypto_pyaes             | 77.3 ms                                                                     | 77.5 ms: 1.00x slower                                                                 |
| deepcopy_memo            | 27.9 us                                                                     | 28.0 us: 1.00x slower                                                                 |
| docutils                 | 2.91 sec                                                                    | 2.92 sec: 1.00x slower                                                                |
| connected_components     | 402 ms                                                                      | 404 ms: 1.01x slower                                                                  |
| many_optionals           | 1.23 ms                                                                     | 1.23 ms: 1.01x slower                                                                 |
| genshi_xml               | 54.3 ms                                                                     | 54.7 ms: 1.01x slower                                                                 |
| typing_runtime_protocols | 169 us                                                                      | 170 us: 1.01x slower                                                                  |
| shortest_path            | 437 ms                                                                      | 440 ms: 1.01x slower                                                                  |
| meteor_contest           | 121 ms                                                                      | 122 ms: 1.01x slower                                                                  |
| logging_simple           | 5.96 us                                                                     | 6.01 us: 1.01x slower                                                                 |
| sqlglot_v2_parse         | 1.31 ms                                                                     | 1.32 ms: 1.01x slower                                                                 |
| deltablue                | 2.84 ms                                                                     | 2.87 ms: 1.01x slower                                                                 |
| bpe_tokeniser            | 4.52 sec                                                                    | 4.57 sec: 1.01x slower                                                                |
| subparsers               | 42.6 ms                                                                     | 43.0 ms: 1.01x slower                                                                 |
| dulwich_log              | 58.5 ms                                                                     | 59.1 ms: 1.01x slower                                                                 |
| sympy_sum                | 151 ms                                                                      | 152 ms: 1.01x slower                                                                  |
| pickle_pure_python       | 331 us                                                                      | 335 us: 1.01x slower                                                                  |
| unpickle_pure_python     | 193 us                                                                      | 195 us: 1.01x slower                                                                  |
| pprint_safe_repr         | 736 ms                                                                      | 745 ms: 1.01x slower                                                                  |
| pprint_pformat           | 1.49 sec                                                                    | 1.51 sec: 1.01x slower                                                                |
| create_gc_cycles         | 2.88 ms                                                                     | 2.93 ms: 1.02x slower                                                                 |
| pycparser                | 1.24 sec                                                                    | 1.26 sec: 1.02x slower                                                                |
| telco                    | 159 ms                                                                      | 162 ms: 1.02x slower                                                                  |
| json_dumps               | 11.2 ms                                                                     | 11.4 ms: 1.02x slower                                                                 |
| gc_traversal             | 6.54 ms                                                                     | 6.74 ms: 1.03x slower                                                                 |
| mako                     | 9.65 ms                                                                     | 9.95 ms: 1.03x slower                                                                 |
| regex_effbot             | 3.59 ms                                                                     | 3.73 ms: 1.04x slower                                                                 |
| coverage                 | 79.0 ms                                                                     | 82.3 ms: 1.04x slower                                                                 |
| json_loads               | 25.0 us                                                                     | 26.8 us: 1.07x slower                                                                 |
| Geometric mean           | (ref)                                                                       | 1.00x faster                                                                          |

Benchmark hidden because not significant (33): scimark_monte_carlo, async_tree_none, async_tree_io, async_tree_memoization_tg, asyncio_websockets, logging_silent, async_tree_none_tg, raytrace, sqlite_synth, async_tree_memoization, async_tree_cpu_io_mixed, nqueens, logging_format, sqlglot_v2_normalize, sympy_integrate, html5lib, djangocms, json, async_tree_cpu_io_mixed_tg, pyflate, regex_dna, float, sphinx, 2to3, sympy_str, sympy_expand, pylint, sqlglot_v2_transpile, k_core, genshi_text, scimark_lu, xml_etree_generate, thrift

- Geometric mean (including insignificant results): 1.001x faster

# HPT report

- Reliability score: 89.01% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x