# Results vs. base

- fork: Fidget-Spinner
- ref: tail_call
- machine: linux-x86_64
- commit hash: df5d01c
- commit date: 2025-01-16
- overall geometric mean: 1.062x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250116-pythonperf2-x86_64-python-313b96eb8b8d0ad3bac5-3.14.0a4+-313b96e | bm-20250116-pythonperf2-x86_64-Fidget%2dSpinner-tail_call-3.14.0a4+-df5d01c |
|----------------|:----------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                                       | 274 ms: 1.02x faster                                                        |
| html5lib       | 67.1 ms                                                                      | 66.0 ms: 1.02x faster                                                       |
| sphinx         | 1.10 sec                                                                     | 1.09 sec: 1.01x faster                                                      |
| Geometric mean | (ref)                                                                        | 1.01x faster                                                                |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250116-pythonperf2-x86_64-python-313b96eb8b8d0ad3bac5-3.14.0a4+-313b96e | bm-20250116-pythonperf2-x86_64-Fidget%2dSpinner-tail_call-3.14.0a4+-df5d01c |
|----------------------------|:----------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none_tg         | 267 ms                                                                       | 257 ms: 1.04x faster                                                        |
| async_tree_none            | 282 ms                                                                       | 271 ms: 1.04x faster                                                        |
| async_tree_memoization     | 346 ms                                                                       | 334 ms: 1.04x faster                                                        |
| async_tree_io              | 629 ms                                                                       | 610 ms: 1.03x faster                                                        |
| async_tree_memoization_tg  | 324 ms                                                                       | 315 ms: 1.03x faster                                                        |
| async_tree_io_tg           | 630 ms                                                                       | 613 ms: 1.03x faster                                                        |
| async_tree_cpu_io_mixed    | 545 ms                                                                       | 532 ms: 1.03x faster                                                        |
| async_tree_cpu_io_mixed_tg | 528 ms                                                                       | 517 ms: 1.02x faster                                                        |
| async_generators           | 414 ms                                                                       | 421 ms: 1.02x slower                                                        |
| Geometric mean             | (ref)                                                                        | 1.02x faster                                                                |

Benchmark hidden because not significant (2): asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250116-pythonperf2-x86_64-python-313b96eb8b8d0ad3bac5-3.14.0a4+-313b96e | bm-20250116-pythonperf2-x86_64-Fidget%2dSpinner-tail_call-3.14.0a4+-df5d01c |
|----------------|:----------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 75.1 ms                                                                      | 66.9 ms: 1.12x faster                                                       |
| nbody          | 105 ms                                                                       | 101 ms: 1.04x faster                                                        |
| Geometric mean | (ref)                                                                        | 1.05x faster                                                                |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250116-pythonperf2-x86_64-python-313b96eb8b8d0ad3bac5-3.14.0a4+-313b96e | bm-20250116-pythonperf2-x86_64-Fidget%2dSpinner-tail_call-3.14.0a4+-df5d01c |
|----------------|:----------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                                       | 134 ms: 1.08x faster                                                        |
| regex_effbot   | 3.03 ms                                                                      | 2.98 ms: 1.02x faster                                                       |
| regex_v8       | 26.4 ms                                                                      | 26.5 ms: 1.00x slower                                                       |
| regex_dna      | 222 ms                                                                       | 226 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                                        | 1.02x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250116-pythonperf2-x86_64-python-313b96eb8b8d0ad3bac5-3.14.0a4+-313b96e | bm-20250116-pythonperf2-x86_64-Fidget%2dSpinner-tail_call-3.14.0a4+-df5d01c |
|----------------------|:----------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.48 sec                                                                     | 1.99 sec: 1.25x faster                                                      |
| unpickle_pure_python | 239 us                                                                       | 202 us: 1.18x faster                                                        |
| pickle_pure_python   | 353 us                                                                       | 311 us: 1.13x faster                                                        |
| xml_etree_process    | 61.0 ms                                                                      | 55.6 ms: 1.10x faster                                                       |
| xml_etree_generate   | 85.3 ms                                                                      | 79.0 ms: 1.08x faster                                                       |
| xml_etree_iterparse  | 106 ms                                                                       | 102 ms: 1.05x faster                                                        |
| json_dumps           | 11.9 ms                                                                      | 11.6 ms: 1.03x faster                                                       |
| json_loads           | 25.6 us                                                                      | 25.2 us: 1.02x faster                                                       |
| xml_etree_parse      | 163 ms                                                                       | 162 ms: 1.01x faster                                                        |
| Geometric mean       | (ref)                                                                        | 1.09x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250116-pythonperf2-x86_64-python-313b96eb8b8d0ad3bac5-3.14.0a4+-313b96e | bm-20250116-pythonperf2-x86_64-Fidget%2dSpinner-tail_call-3.14.0a4+-df5d01c |
|------------------------|:----------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 9.05 ms                                                                      | 9.02 ms: 1.00x faster                                                       |
| python_startup         | 16.0 ms                                                                      | 16.0 ms: 1.00x faster                                                       |
| Geometric mean         | (ref)                                                                        | 1.00x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250116-pythonperf2-x86_64-python-313b96eb8b8d0ad3bac5-3.14.0a4+-313b96e | bm-20250116-pythonperf2-x86_64-Fidget%2dSpinner-tail_call-3.14.0a4+-df5d01c |
|-----------------|:----------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 25.0 ms                                                                      | 22.0 ms: 1.14x faster                                                       |
| mako            | 12.0 ms                                                                      | 10.9 ms: 1.10x faster                                                       |
| genshi_xml      | 54.9 ms                                                                      | 52.6 ms: 1.04x faster                                                       |
| django_template | 35.2 ms                                                                      | 34.0 ms: 1.04x faster                                                       |
| Geometric mean  | (ref)                                                                        | 1.08x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20250116-pythonperf2-x86_64-python-313b96eb8b8d0ad3bac5-3.14.0a4+-313b96e | bm-20250116-pythonperf2-x86_64-Fidget%2dSpinner-tail_call-3.14.0a4+-df5d01c |
|----------------------------|:----------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| scimark_sor                | 126 ms                                                                       | 95.1 ms: 1.33x faster                                                       |
| scimark_monte_carlo        | 71.2 ms                                                                      | 54.8 ms: 1.30x faster                                                       |
| tomli_loads                | 2.48 sec                                                                     | 1.99 sec: 1.25x faster                                                      |
| deepcopy_memo              | 33.4 us                                                                      | 27.0 us: 1.24x faster                                                       |
| hexiom                     | 6.84 ms                                                                      | 5.65 ms: 1.21x faster                                                       |
| scimark_fft                | 311 ms                                                                       | 258 ms: 1.21x faster                                                        |
| logging_silent             | 99.8 ns                                                                      | 82.8 ns: 1.21x faster                                                       |
| scimark_lu                 | 99.1 ms                                                                      | 82.5 ms: 1.20x faster                                                       |
| fannkuch                   | 431 ms                                                                       | 359 ms: 1.20x faster                                                        |
| unpickle_pure_python       | 239 us                                                                       | 202 us: 1.18x faster                                                        |
| go                         | 137 ms                                                                       | 117 ms: 1.17x faster                                                        |
| spectral_norm              | 94.4 ms                                                                      | 80.7 ms: 1.17x faster                                                       |
| scimark_sparse_mat_mult    | 4.54 ms                                                                      | 3.88 ms: 1.17x faster                                                       |
| pyflate                    | 473 ms                                                                       | 405 ms: 1.17x faster                                                        |
| generators                 | 33.1 ms                                                                      | 28.5 ms: 1.16x faster                                                       |
| comprehensions             | 18.1 us                                                                      | 15.8 us: 1.15x faster                                                       |
| pprint_safe_repr           | 874 ms                                                                       | 767 ms: 1.14x faster                                                        |
| genshi_text                | 25.0 ms                                                                      | 22.0 ms: 1.14x faster                                                       |
| pickle_pure_python         | 353 us                                                                       | 311 us: 1.13x faster                                                        |
| pprint_pformat             | 1.77 sec                                                                     | 1.57 sec: 1.13x faster                                                      |
| float                      | 75.1 ms                                                                      | 66.9 ms: 1.12x faster                                                       |
| sqlglot_parse              | 1.41 ms                                                                      | 1.26 ms: 1.12x faster                                                       |
| richards                   | 46.8 ms                                                                      | 42.1 ms: 1.11x faster                                                       |
| chaos                      | 63.9 ms                                                                      | 58.1 ms: 1.10x faster                                                       |
| nqueens                    | 95.5 ms                                                                      | 86.9 ms: 1.10x faster                                                       |
| xml_etree_process          | 61.0 ms                                                                      | 55.6 ms: 1.10x faster                                                       |
| mako                       | 12.0 ms                                                                      | 10.9 ms: 1.10x faster                                                       |
| deepcopy                   | 286 us                                                                       | 263 us: 1.09x faster                                                        |
| richards_super             | 52.3 ms                                                                      | 48.4 ms: 1.08x faster                                                       |
| xml_etree_generate         | 85.3 ms                                                                      | 79.0 ms: 1.08x faster                                                       |
| sqlglot_transpile          | 1.78 ms                                                                      | 1.65 ms: 1.08x faster                                                       |
| regex_compile              | 144 ms                                                                       | 134 ms: 1.08x faster                                                        |
| bpe_tokeniser              | 4.86 sec                                                                     | 4.56 sec: 1.07x faster                                                      |
| deepcopy_reduce            | 2.93 us                                                                      | 2.75 us: 1.06x faster                                                       |
| crypto_pyaes               | 79.6 ms                                                                      | 75.1 ms: 1.06x faster                                                       |
| deltablue                  | 3.28 ms                                                                      | 3.12 ms: 1.05x faster                                                       |
| raytrace                   | 267 ms                                                                       | 254 ms: 1.05x faster                                                        |
| pycparser                  | 1.27 sec                                                                     | 1.21 sec: 1.05x faster                                                      |
| meteor_contest             | 134 ms                                                                       | 128 ms: 1.05x faster                                                        |
| xml_etree_iterparse        | 106 ms                                                                       | 102 ms: 1.05x faster                                                        |
| nbody                      | 105 ms                                                                       | 101 ms: 1.04x faster                                                        |
| genshi_xml                 | 54.9 ms                                                                      | 52.6 ms: 1.04x faster                                                       |
| async_tree_none_tg         | 267 ms                                                                       | 257 ms: 1.04x faster                                                        |
| async_tree_none            | 282 ms                                                                       | 271 ms: 1.04x faster                                                        |
| telco                      | 7.84 ms                                                                      | 7.54 ms: 1.04x faster                                                       |
| django_template            | 35.2 ms                                                                      | 34.0 ms: 1.04x faster                                                       |
| async_tree_memoization     | 346 ms                                                                       | 334 ms: 1.04x faster                                                        |
| thrift                     | 853 us                                                                       | 827 us: 1.03x faster                                                        |
| async_tree_io              | 629 ms                                                                       | 610 ms: 1.03x faster                                                        |
| async_tree_memoization_tg  | 324 ms                                                                       | 315 ms: 1.03x faster                                                        |
| typing_runtime_protocols   | 169 us                                                                       | 165 us: 1.03x faster                                                        |
| async_tree_io_tg           | 630 ms                                                                       | 613 ms: 1.03x faster                                                        |
| bench_thread_pool          | 926 us                                                                       | 901 us: 1.03x faster                                                        |
| json_dumps                 | 11.9 ms                                                                      | 11.6 ms: 1.03x faster                                                       |
| sympy_str                  | 289 ms                                                                       | 282 ms: 1.03x faster                                                        |
| dulwich_log                | 66.6 ms                                                                      | 64.9 ms: 1.03x faster                                                       |
| async_tree_cpu_io_mixed    | 545 ms                                                                       | 532 ms: 1.03x faster                                                        |
| sqlglot_optimize           | 58.7 ms                                                                      | 57.3 ms: 1.02x faster                                                       |
| sqlglot_normalize          | 118 ms                                                                       | 115 ms: 1.02x faster                                                        |
| 2to3                       | 280 ms                                                                       | 274 ms: 1.02x faster                                                        |
| sqlalchemy_imperative      | 17.9 ms                                                                      | 17.5 ms: 1.02x faster                                                       |
| async_tree_cpu_io_mixed_tg | 528 ms                                                                       | 517 ms: 1.02x faster                                                        |
| regex_effbot               | 3.03 ms                                                                      | 2.98 ms: 1.02x faster                                                       |
| sympy_sum                  | 150 ms                                                                       | 148 ms: 1.02x faster                                                        |
| html5lib                   | 67.1 ms                                                                      | 66.0 ms: 1.02x faster                                                       |
| json_loads                 | 25.6 us                                                                      | 25.2 us: 1.02x faster                                                       |
| sqlite_synth               | 2.82 us                                                                      | 2.79 us: 1.01x faster                                                       |
| sphinx                     | 1.10 sec                                                                     | 1.09 sec: 1.01x faster                                                      |
| shortest_path              | 452 ms                                                                       | 446 ms: 1.01x faster                                                        |
| sqlalchemy_declarative     | 145 ms                                                                       | 143 ms: 1.01x faster                                                        |
| mdp                        | 2.63 sec                                                                     | 2.60 sec: 1.01x faster                                                      |
| sympy_expand               | 487 ms                                                                       | 483 ms: 1.01x faster                                                        |
| pathlib                    | 15.7 ms                                                                      | 15.6 ms: 1.01x faster                                                       |
| connected_components       | 429 ms                                                                       | 426 ms: 1.01x faster                                                        |
| logging_simple             | 6.09 us                                                                      | 6.05 us: 1.01x faster                                                       |
| logging_format             | 6.75 us                                                                      | 6.71 us: 1.01x faster                                                       |
| xml_etree_parse            | 163 ms                                                                       | 162 ms: 1.01x faster                                                        |
| python_startup_no_site     | 9.05 ms                                                                      | 9.02 ms: 1.00x faster                                                       |
| sympy_integrate            | 22.6 ms                                                                      | 22.5 ms: 1.00x faster                                                       |
| python_startup             | 16.0 ms                                                                      | 16.0 ms: 1.00x faster                                                       |
| regex_v8                   | 26.4 ms                                                                      | 26.5 ms: 1.00x slower                                                       |
| coverage                   | 72.7 ms                                                                      | 73.2 ms: 1.01x slower                                                       |
| subparsers                 | 22.5 ms                                                                      | 22.8 ms: 1.01x slower                                                       |
| gc_traversal               | 5.64 ms                                                                      | 5.72 ms: 1.01x slower                                                       |
| async_generators           | 414 ms                                                                       | 421 ms: 1.02x slower                                                        |
| many_optionals             | 1.01 ms                                                                      | 1.02 ms: 1.02x slower                                                       |
| regex_dna                  | 222 ms                                                                       | 226 ms: 1.02x slower                                                        |
| Geometric mean             | (ref)                                                                        | 1.06x faster                                                                |

Benchmark hidden because not significant (9): asyncio_websockets, k_core, pidigits, create_gc_cycles, docutils, json, coroutines, pylint, bench_mp_pool

- Geometric mean (including insignificant results): 1.062x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.01x