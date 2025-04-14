# Results vs. base

- fork: Fidget-Spinner
- ref: method_jit_bench
- machine: linux-x86_64
- commit hash: d456718
- commit date: 2025-03-18
- overall geometric mean: 1.011x slower
- HPT reliability: 88.40%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250318-linux-x86_64-python-b2ed7a6d6aae9860110f-3.14.0a6+-b2ed7a6 | bm-20250318-linux-x86_64-Fidget%2dSpinner-method_jit_bench-3.14.0a6+-d456718 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| docutils       | 2.68 sec                                                               | 2.63 sec: 1.02x faster                                                       |
| html5lib       | 61.6 ms                                                                | 62.4 ms: 1.01x slower                                                        |
| sphinx         | 1.03 sec                                                               | 1.01 sec: 1.01x faster                                                       |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20250318-linux-x86_64-python-b2ed7a6d6aae9860110f-3.14.0a6+-b2ed7a6 | bm-20250318-linux-x86_64-Fidget%2dSpinner-method_jit_bench-3.14.0a6+-d456718 |
|-------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_generators        | 420 ms                                                                 | 393 ms: 1.07x faster                                                         |
| async_tree_none_tg      | 253 ms                                                                 | 250 ms: 1.01x faster                                                         |
| async_tree_memoization  | 319 ms                                                                 | 316 ms: 1.01x faster                                                         |
| async_tree_cpu_io_mixed | 491 ms                                                                 | 488 ms: 1.01x faster                                                         |
| coroutines              | 23.2 ms                                                                | 24.0 ms: 1.04x slower                                                        |
| Geometric mean          | (ref)                                                                  | 1.01x faster                                                                 |

Benchmark hidden because not significant (6): async_tree_memoization_tg, async_tree_io, async_tree_io_tg, async_tree_none, async_tree_cpu_io_mixed_tg, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250318-linux-x86_64-python-b2ed7a6d6aae9860110f-3.14.0a6+-b2ed7a6 | bm-20250318-linux-x86_64-Fidget%2dSpinner-method_jit_bench-3.14.0a6+-d456718 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pidigits       | 186 ms                                                                 | 187 ms: 1.01x slower                                                         |
| float          | 65.5 ms                                                                | 69.2 ms: 1.06x slower                                                        |
| nbody          | 88.5 ms                                                                | 96.7 ms: 1.09x slower                                                        |
| Geometric mean | (ref)                                                                  | 1.05x slower                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250318-linux-x86_64-python-b2ed7a6d6aae9860110f-3.14.0a6+-b2ed7a6 | bm-20250318-linux-x86_64-Fidget%2dSpinner-method_jit_bench-3.14.0a6+-d456718 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.49 ms                                                                | 3.18 ms: 1.10x faster                                                        |
| regex_dna      | 225 ms                                                                 | 217 ms: 1.04x faster                                                         |
| regex_v8       | 23.9 ms                                                                | 23.1 ms: 1.04x faster                                                        |
| regex_compile  | 128 ms                                                                 | 135 ms: 1.06x slower                                                         |
| Geometric mean | (ref)                                                                  | 1.03x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250318-linux-x86_64-python-b2ed7a6d6aae9860110f-3.14.0a6+-b2ed7a6 | bm-20250318-linux-x86_64-Fidget%2dSpinner-method_jit_bench-3.14.0a6+-d456718 |
|----------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pickle_pure_python   | 326 us                                                                 | 322 us: 1.01x faster                                                         |
| json_loads           | 29.8 us                                                                | 29.5 us: 1.01x faster                                                        |
| xml_etree_iterparse  | 97.5 ms                                                                | 98.2 ms: 1.01x slower                                                        |
| xml_etree_parse      | 138 ms                                                                 | 141 ms: 1.02x slower                                                         |
| unpickle_pure_python | 212 us                                                                 | 219 us: 1.03x slower                                                         |
| xml_etree_process    | 55.8 ms                                                                | 58.3 ms: 1.04x slower                                                        |
| xml_etree_generate   | 79.5 ms                                                                | 83.7 ms: 1.05x slower                                                        |
| tomli_loads          | 1.87 sec                                                               | 2.09 sec: 1.12x slower                                                       |
| Geometric mean       | (ref)                                                                  | 1.03x slower                                                                 |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250318-linux-x86_64-python-b2ed7a6d6aae9860110f-3.14.0a6+-b2ed7a6 | bm-20250318-linux-x86_64-Fidget%2dSpinner-method_jit_bench-3.14.0a6+-d456718 |
|------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 13.2 ms                                                                | 13.2 ms: 1.00x slower                                                        |
| python_startup_no_site | 8.23 ms                                                                | 8.29 ms: 1.01x slower                                                        |
| Geometric mean         | (ref)                                                                  | 1.01x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250318-linux-x86_64-python-b2ed7a6d6aae9860110f-3.14.0a6+-b2ed7a6 | bm-20250318-linux-x86_64-Fidget%2dSpinner-method_jit_bench-3.14.0a6+-d456718 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_text    | 21.3 ms                                                                | 21.9 ms: 1.03x slower                                                        |
| mako           | 10.9 ms                                                                | 11.7 ms: 1.07x slower                                                        |
| Geometric mean | (ref)                                                                  | 1.02x slower                                                                 |

Benchmark hidden because not significant (2): genshi_xml, django_template

All benchmarks:
===============

| Benchmark                | bm-20250318-linux-x86_64-python-b2ed7a6d6aae9860110f-3.14.0a6+-b2ed7a6 | bm-20250318-linux-x86_64-Fidget%2dSpinner-method_jit_bench-3.14.0a6+-d456718 |
|--------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| comprehensions           | 18.8 us                                                                | 16.8 us: 1.12x faster                                                        |
| regex_effbot             | 3.49 ms                                                                | 3.18 ms: 1.10x faster                                                        |
| hexiom                   | 6.77 ms                                                                | 6.19 ms: 1.09x faster                                                        |
| async_generators         | 420 ms                                                                 | 393 ms: 1.07x faster                                                         |
| go                       | 128 ms                                                                 | 120 ms: 1.06x faster                                                         |
| crypto_pyaes             | 79.2 ms                                                                | 75.7 ms: 1.05x faster                                                        |
| pprint_pformat           | 1.57 sec                                                               | 1.51 sec: 1.04x faster                                                       |
| regex_dna                | 225 ms                                                                 | 217 ms: 1.04x faster                                                         |
| scimark_lu               | 120 ms                                                                 | 116 ms: 1.04x faster                                                         |
| regex_v8                 | 23.9 ms                                                                | 23.1 ms: 1.04x faster                                                        |
| sqlalchemy_imperative    | 17.4 ms                                                                | 16.8 ms: 1.04x faster                                                        |
| pycparser                | 1.17 sec                                                               | 1.14 sec: 1.03x faster                                                       |
| typing_runtime_protocols | 168 us                                                                 | 163 us: 1.03x faster                                                         |
| fannkuch                 | 426 ms                                                                 | 413 ms: 1.03x faster                                                         |
| dulwich_log              | 60.7 ms                                                                | 59.2 ms: 1.03x faster                                                        |
| pprint_safe_repr         | 757 ms                                                                 | 739 ms: 1.02x faster                                                         |
| sympy_expand             | 475 ms                                                                 | 464 ms: 1.02x faster                                                         |
| scimark_sor              | 119 ms                                                                 | 117 ms: 1.02x faster                                                         |
| nqueens                  | 85.6 ms                                                                | 83.8 ms: 1.02x faster                                                        |
| generators               | 28.4 ms                                                                | 27.8 ms: 1.02x faster                                                        |
| meteor_contest           | 110 ms                                                                 | 108 ms: 1.02x faster                                                         |
| docutils                 | 2.68 sec                                                               | 2.63 sec: 1.02x faster                                                       |
| logging_format           | 6.26 us                                                                | 6.15 us: 1.02x faster                                                        |
| sympy_sum                | 154 ms                                                                 | 151 ms: 1.02x faster                                                         |
| sqlglot_v2_normalize     | 108 ms                                                                 | 106 ms: 1.02x faster                                                         |
| scimark_monte_carlo      | 68.4 ms                                                                | 67.4 ms: 1.01x faster                                                        |
| async_tree_none_tg       | 253 ms                                                                 | 250 ms: 1.01x faster                                                         |
| sphinx                   | 1.03 sec                                                               | 1.01 sec: 1.01x faster                                                       |
| sympy_str                | 277 ms                                                                 | 273 ms: 1.01x faster                                                         |
| pyflate                  | 452 ms                                                                 | 446 ms: 1.01x faster                                                         |
| many_optionals           | 968 us                                                                 | 956 us: 1.01x faster                                                         |
| bench_thread_pool        | 885 us                                                                 | 875 us: 1.01x faster                                                         |
| pickle_pure_python       | 326 us                                                                 | 322 us: 1.01x faster                                                         |
| async_tree_memoization   | 319 ms                                                                 | 316 ms: 1.01x faster                                                         |
| json_loads               | 29.8 us                                                                | 29.5 us: 1.01x faster                                                        |
| connected_components     | 456 ms                                                                 | 452 ms: 1.01x faster                                                         |
| chaos                    | 60.4 ms                                                                | 59.9 ms: 1.01x faster                                                        |
| async_tree_cpu_io_mixed  | 491 ms                                                                 | 488 ms: 1.01x faster                                                         |
| subparsers               | 21.1 ms                                                                | 21.0 ms: 1.01x faster                                                        |
| gc_traversal             | 4.85 ms                                                                | 4.83 ms: 1.00x faster                                                        |
| sympy_integrate          | 20.3 ms                                                                | 20.2 ms: 1.00x faster                                                        |
| sqlglot_v2_optimize      | 53.8 ms                                                                | 53.9 ms: 1.00x slower                                                        |
| python_startup           | 13.2 ms                                                                | 13.2 ms: 1.00x slower                                                        |
| create_gc_cycles         | 2.48 ms                                                                | 2.50 ms: 1.01x slower                                                        |
| xml_etree_iterparse      | 97.5 ms                                                                | 98.2 ms: 1.01x slower                                                        |
| pidigits                 | 186 ms                                                                 | 187 ms: 1.01x slower                                                         |
| python_startup_no_site   | 8.23 ms                                                                | 8.29 ms: 1.01x slower                                                        |
| bpe_tokeniser            | 4.59 sec                                                               | 4.63 sec: 1.01x slower                                                       |
| deepcopy_memo            | 29.1 us                                                                | 29.4 us: 1.01x slower                                                        |
| logging_silent           | 95.7 ns                                                                | 96.8 ns: 1.01x slower                                                        |
| html5lib                 | 61.6 ms                                                                | 62.4 ms: 1.01x slower                                                        |
| json                     | 5.28 ms                                                                | 5.35 ms: 1.01x slower                                                        |
| telco                    | 7.84 ms                                                                | 7.95 ms: 1.01x slower                                                        |
| sqlalchemy_declarative   | 133 ms                                                                 | 135 ms: 1.02x slower                                                         |
| xml_etree_parse          | 138 ms                                                                 | 141 ms: 1.02x slower                                                         |
| deepcopy                 | 259 us                                                                 | 264 us: 1.02x slower                                                         |
| deepcopy_reduce          | 2.71 us                                                                | 2.76 us: 1.02x slower                                                        |
| pathlib                  | 16.5 ms                                                                | 16.8 ms: 1.02x slower                                                        |
| sqlite_synth             | 2.73 us                                                                | 2.79 us: 1.02x slower                                                        |
| raytrace                 | 271 ms                                                                 | 278 ms: 1.03x slower                                                         |
| mdp                      | 2.47 sec                                                               | 2.54 sec: 1.03x slower                                                       |
| bench_mp_pool            | 83.4 ms                                                                | 85.8 ms: 1.03x slower                                                        |
| scimark_sparse_mat_mult  | 4.67 ms                                                                | 4.81 ms: 1.03x slower                                                        |
| unpickle_pure_python     | 212 us                                                                 | 219 us: 1.03x slower                                                         |
| genshi_text              | 21.3 ms                                                                | 21.9 ms: 1.03x slower                                                        |
| coroutines               | 23.2 ms                                                                | 24.0 ms: 1.04x slower                                                        |
| xml_etree_process        | 55.8 ms                                                                | 58.3 ms: 1.04x slower                                                        |
| spectral_norm            | 94.4 ms                                                                | 99.2 ms: 1.05x slower                                                        |
| xml_etree_generate       | 79.5 ms                                                                | 83.7 ms: 1.05x slower                                                        |
| float                    | 65.5 ms                                                                | 69.2 ms: 1.06x slower                                                        |
| regex_compile            | 128 ms                                                                 | 135 ms: 1.06x slower                                                         |
| mako                     | 10.9 ms                                                                | 11.7 ms: 1.07x slower                                                        |
| nbody                    | 88.5 ms                                                                | 96.7 ms: 1.09x slower                                                        |
| scimark_fft              | 313 ms                                                                 | 343 ms: 1.10x slower                                                         |
| coverage                 | 83.7 ms                                                                | 93.3 ms: 1.11x slower                                                        |
| tomli_loads              | 1.87 sec                                                               | 2.09 sec: 1.12x slower                                                       |
| deltablue                | 3.05 ms                                                                | 3.63 ms: 1.19x slower                                                        |
| richards_super           | 41.5 ms                                                                | 49.5 ms: 1.19x slower                                                        |
| sqlglot_v2_transpile     | 1.61 ms                                                                | 1.95 ms: 1.21x slower                                                        |
| richards                 | 35.6 ms                                                                | 43.4 ms: 1.22x slower                                                        |
| sqlglot_v2_parse         | 1.29 ms                                                                | 1.64 ms: 1.27x slower                                                        |
| Geometric mean           | (ref)                                                                  | 1.01x slower                                                                 |

Benchmark hidden because not significant (14): async_tree_memoization_tg, async_tree_io, async_tree_io_tg, k_core, logging_simple, async_tree_none, async_tree_cpu_io_mixed_tg, asyncio_websockets, json_dumps, thrift, genshi_xml, django_template, pylint, shortest_path
Ignored benchmarks (1) of results/bm-20250318-3.14.0a6+-b2ed7a6-JIT/bm-20250318-linux-x86_64-python-b2ed7a6d6aae9860110f-3.14.0a6+-b2ed7a6.json: 2to3

- Geometric mean (including insignificant results): 1.011x slower

# HPT report

- Reliability score: 88.40% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x