# Results vs. base

- fork: python
- ref: ed81971e6b26c34445f0
- machine: windows-amd64
- commit hash: ed81971
- commit date: 2024-11-16
- overall geometric mean: 1.002x slower
- HPT reliability: 56.63%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241116-pythonperf1-amd64-python-2313f8421080ceb3343c-3.14.0a1+-2313f84 | bm-20241116-pythonperf1-amd64-python-ed81971e6b26c34445f0-3.14.0a1+-ed81971 |
|----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| html5lib       | 40.0 ms                                                                     | 40.2 ms: 1.00x slower                                                       |
| Geometric mean | (ref)                                                                       | 1.00x slower                                                                |

Benchmark hidden because not significant (3): 2to3, docutils, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark          | bm-20241116-pythonperf1-amd64-python-2313f8421080ceb3343c-3.14.0a1+-2313f84 | bm-20241116-pythonperf1-amd64-python-ed81971e6b26c34445f0-3.14.0a1+-ed81971 |
|--------------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_generators   | 243 ms                                                                      | 245 ms: 1.01x slower                                                        |
| asyncio_websockets | 303 ms                                                                      | 321 ms: 1.06x slower                                                        |
| Geometric mean     | (ref)                                                                       | 1.01x slower                                                                |

Benchmark hidden because not significant (9): async_tree_io, async_tree_memoization, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, async_tree_cpu_io_mixed_tg, coroutines, async_tree_cpu_io_mixed, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241116-pythonperf1-amd64-python-2313f8421080ceb3343c-3.14.0a1+-2313f84 | bm-20241116-pythonperf1-amd64-python-ed81971e6b26c34445f0-3.14.0a1+-ed81971 |
|----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 148 ms                                                                      | 145 ms: 1.02x faster                                                        |
| float          | 56.0 ms                                                                     | 56.4 ms: 1.01x slower                                                       |
| nbody          | 79.9 ms                                                                     | 82.8 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                                       | 1.01x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241116-pythonperf1-amd64-python-2313f8421080ceb3343c-3.14.0a1+-2313f84 | bm-20241116-pythonperf1-amd64-python-ed81971e6b26c34445f0-3.14.0a1+-ed81971 |
|----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 91.8 ms                                                                     | 91.2 ms: 1.01x faster                                                       |
| regex_v8       | 14.7 ms                                                                     | 15.2 ms: 1.03x slower                                                       |
| regex_dna      | 116 ms                                                                      | 124 ms: 1.06x slower                                                        |
| Geometric mean | (ref)                                                                       | 1.02x slower                                                                |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20241116-pythonperf1-amd64-python-2313f8421080ceb3343c-3.14.0a1+-2313f84 | bm-20241116-pythonperf1-amd64-python-ed81971e6b26c34445f0-3.14.0a1+-ed81971 |
|--------------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads        | 1.60 sec                                                                    | 1.58 sec: 1.01x faster                                                      |
| json_loads         | 14.6 us                                                                     | 14.4 us: 1.01x faster                                                       |
| pickle_pure_python | 229 us                                                                      | 227 us: 1.01x faster                                                        |
| xml_etree_parse    | 96.0 ms                                                                     | 96.8 ms: 1.01x slower                                                       |
| xml_etree_generate | 58.6 ms                                                                     | 59.2 ms: 1.01x slower                                                       |
| Geometric mean     | (ref)                                                                       | 1.00x faster                                                                |

Benchmark hidden because not significant (4): xml_etree_iterparse, xml_etree_process, json_dumps, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241116-pythonperf1-amd64-python-2313f8421080ceb3343c-3.14.0a1+-2313f84 | bm-20241116-pythonperf1-amd64-python-ed81971e6b26c34445f0-3.14.0a1+-ed81971 |
|------------------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 23.4 ms                                                                     | 24.0 ms: 1.03x slower                                                       |
| python_startup_no_site | 17.2 ms                                                                     | 17.9 ms: 1.04x slower                                                       |
| Geometric mean         | (ref)                                                                       | 1.03x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241116-pythonperf1-amd64-python-2313f8421080ceb3343c-3.14.0a1+-2313f84 | bm-20241116-pythonperf1-amd64-python-ed81971e6b26c34445f0-3.14.0a1+-ed81971 |
|-----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 7.07 ms                                                                     | 6.95 ms: 1.02x faster                                                       |
| django_template | 25.0 ms                                                                     | 25.4 ms: 1.01x slower                                                       |
| genshi_xml      | 36.5 ms                                                                     | 37.2 ms: 1.02x slower                                                       |
| genshi_text     | 16.9 ms                                                                     | 17.4 ms: 1.03x slower                                                       |
| Geometric mean  | (ref)                                                                       | 1.01x slower                                                                |

All benchmarks:
===============

| Benchmark                | bm-20241116-pythonperf1-amd64-python-2313f8421080ceb3343c-3.14.0a1+-2313f84 | bm-20241116-pythonperf1-amd64-python-ed81971e6b26c34445f0-3.14.0a1+-ed81971 |
|--------------------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| coverage                 | 48.3 ms                                                                     | 46.3 ms: 1.04x faster                                                       |
| typing_runtime_protocols | 116 us                                                                      | 112 us: 1.04x faster                                                        |
| scimark_fft              | 205 ms                                                                      | 200 ms: 1.03x faster                                                        |
| generators               | 22.5 ms                                                                     | 21.9 ms: 1.03x faster                                                       |
| richards                 | 33.2 ms                                                                     | 32.5 ms: 1.02x faster                                                       |
| pathlib                  | 76.0 ms                                                                     | 74.5 ms: 1.02x faster                                                       |
| pprint_safe_repr         | 569 ms                                                                      | 558 ms: 1.02x faster                                                        |
| richards_super           | 37.1 ms                                                                     | 36.4 ms: 1.02x faster                                                       |
| mako                     | 7.07 ms                                                                     | 6.95 ms: 1.02x faster                                                       |
| raytrace                 | 201 ms                                                                      | 197 ms: 1.02x faster                                                        |
| shortest_path            | 362 ms                                                                      | 357 ms: 1.02x faster                                                        |
| pidigits                 | 148 ms                                                                      | 145 ms: 1.02x faster                                                        |
| tomli_loads              | 1.60 sec                                                                    | 1.58 sec: 1.01x faster                                                      |
| chaos                    | 44.0 ms                                                                     | 43.4 ms: 1.01x faster                                                       |
| json_loads               | 14.6 us                                                                     | 14.4 us: 1.01x faster                                                       |
| scimark_sor              | 92.5 ms                                                                     | 91.2 ms: 1.01x faster                                                       |
| deltablue                | 2.32 ms                                                                     | 2.29 ms: 1.01x faster                                                       |
| nqueens                  | 64.1 ms                                                                     | 63.3 ms: 1.01x faster                                                       |
| gc_traversal             | 1.93 ms                                                                     | 1.91 ms: 1.01x faster                                                       |
| pprint_pformat           | 1.13 sec                                                                    | 1.12 sec: 1.01x faster                                                      |
| crypto_pyaes             | 48.5 ms                                                                     | 48.1 ms: 1.01x faster                                                       |
| fannkuch                 | 280 ms                                                                      | 278 ms: 1.01x faster                                                        |
| pickle_pure_python       | 229 us                                                                      | 227 us: 1.01x faster                                                        |
| connected_components     | 328 ms                                                                      | 326 ms: 1.01x faster                                                        |
| sympy_sum                | 90.4 ms                                                                     | 89.7 ms: 1.01x faster                                                       |
| regex_compile            | 91.8 ms                                                                     | 91.2 ms: 1.01x faster                                                       |
| scimark_monte_carlo      | 48.0 ms                                                                     | 47.7 ms: 1.01x faster                                                       |
| pyflate                  | 323 ms                                                                      | 321 ms: 1.01x faster                                                        |
| telco                    | 4.83 ms                                                                     | 4.81 ms: 1.01x faster                                                       |
| sqlglot_optimize         | 37.3 ms                                                                     | 37.1 ms: 1.01x faster                                                       |
| go                       | 90.5 ms                                                                     | 90.2 ms: 1.00x faster                                                       |
| bpe_tokeniser            | 3.09 sec                                                                    | 3.08 sec: 1.00x faster                                                      |
| html5lib                 | 40.0 ms                                                                     | 40.2 ms: 1.00x slower                                                       |
| deepcopy_memo            | 21.2 us                                                                     | 21.3 us: 1.01x slower                                                       |
| logging_format           | 6.78 us                                                                     | 6.82 us: 1.01x slower                                                       |
| float                    | 56.0 ms                                                                     | 56.4 ms: 1.01x slower                                                       |
| logging_simple           | 6.34 us                                                                     | 6.39 us: 1.01x slower                                                       |
| xml_etree_parse          | 96.0 ms                                                                     | 96.8 ms: 1.01x slower                                                       |
| async_generators         | 243 ms                                                                      | 245 ms: 1.01x slower                                                        |
| logging_silent           | 64.9 ns                                                                     | 65.5 ns: 1.01x slower                                                       |
| xml_etree_generate       | 58.6 ms                                                                     | 59.2 ms: 1.01x slower                                                       |
| pycparser                | 732 ms                                                                      | 741 ms: 1.01x slower                                                        |
| meteor_contest           | 78.2 ms                                                                     | 79.3 ms: 1.01x slower                                                       |
| django_template          | 25.0 ms                                                                     | 25.4 ms: 1.01x slower                                                       |
| deepcopy                 | 191 us                                                                      | 194 us: 1.02x slower                                                        |
| deepcopy_reduce          | 1.95 us                                                                     | 1.98 us: 1.02x slower                                                       |
| comprehensions           | 12.2 us                                                                     | 12.4 us: 1.02x slower                                                       |
| genshi_xml               | 36.5 ms                                                                     | 37.2 ms: 1.02x slower                                                       |
| dulwich_log              | 42.0 ms                                                                     | 42.9 ms: 1.02x slower                                                       |
| python_startup           | 23.4 ms                                                                     | 24.0 ms: 1.03x slower                                                       |
| genshi_text              | 16.9 ms                                                                     | 17.4 ms: 1.03x slower                                                       |
| regex_v8                 | 14.7 ms                                                                     | 15.2 ms: 1.03x slower                                                       |
| subparsers               | 16.4 ms                                                                     | 17.0 ms: 1.03x slower                                                       |
| scimark_sparse_mat_mult  | 2.72 ms                                                                     | 2.81 ms: 1.04x slower                                                       |
| nbody                    | 79.9 ms                                                                     | 82.8 ms: 1.04x slower                                                       |
| spectral_norm            | 65.4 ms                                                                     | 67.8 ms: 1.04x slower                                                       |
| mdp                      | 1.45 sec                                                                    | 1.50 sec: 1.04x slower                                                      |
| python_startup_no_site   | 17.2 ms                                                                     | 17.9 ms: 1.04x slower                                                       |
| asyncio_websockets       | 303 ms                                                                      | 321 ms: 1.06x slower                                                        |
| regex_dna                | 116 ms                                                                      | 124 ms: 1.06x slower                                                        |
| Geometric mean           | (ref)                                                                       | 1.00x slower                                                                |

Benchmark hidden because not significant (34): async_tree_io, pylint, async_tree_memoization, async_tree_io_tg, sympy_integrate, 2to3, xml_etree_iterparse, sqlglot_transpile, sympy_str, async_tree_memoization_tg, xml_etree_process, async_tree_none_tg, create_gc_cycles, sympy_expand, bench_thread_pool, thrift, sqlite_synth, hexiom, sqlglot_normalize, scimark_lu, sqlglot_parse, many_optionals, docutils, bench_mp_pool, regex_effbot, sphinx, async_tree_cpu_io_mixed_tg, json_dumps, coroutines, unpickle_pure_python, json, async_tree_cpu_io_mixed, k_core, async_tree_none

- Geometric mean (including insignificant results): 1.002x slower
# HPT report

- Reliability score: 56.63% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown