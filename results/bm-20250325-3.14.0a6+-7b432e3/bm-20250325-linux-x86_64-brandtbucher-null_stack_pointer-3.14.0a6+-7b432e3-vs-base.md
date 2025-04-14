# Results vs. base

- fork: brandtbucher
- ref: null_stack_pointer
- machine: linux-x86_64
- commit hash: 7b432e3
- commit date: 2025-03-25
- overall geometric mean: 1.007x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250325-linux-x86_64-brandtbucher-null_stack_pointer-3.14.0a6+-7b432e3 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 258 ms                                                                 | 256 ms: 1.01x faster                                                       |
| docutils       | 2.62 sec                                                               | 2.60 sec: 1.01x faster                                                     |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                               |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250325-linux-x86_64-brandtbucher-null_stack_pointer-3.14.0a6+-7b432e3 |
|-------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| coroutines              | 23.6 ms                                                                | 23.8 ms: 1.01x slower                                                      |
| async_tree_cpu_io_mixed | 486 ms                                                                 | 490 ms: 1.01x slower                                                       |
| Geometric mean          | (ref)                                                                  | 1.00x slower                                                               |

Benchmark hidden because not significant (9): async_tree_none_tg, async_generators, async_tree_none, asyncio_websockets, async_tree_memoization_tg, async_tree_io, async_tree_memoization, async_tree_cpu_io_mixed_tg, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250325-linux-x86_64-brandtbucher-null_stack_pointer-3.14.0a6+-7b432e3 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 99.1 ms                                                                | 96.6 ms: 1.03x faster                                                      |
| float          | 70.3 ms                                                                | 68.9 ms: 1.02x faster                                                      |
| pidigits       | 186 ms                                                                 | 186 ms: 1.00x slower                                                       |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250325-linux-x86_64-brandtbucher-null_stack_pointer-3.14.0a6+-7b432e3 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 227 ms                                                                 | 223 ms: 1.02x faster                                                       |
| regex_effbot   | 3.50 ms                                                                | 3.43 ms: 1.02x faster                                                      |
| regex_v8       | 24.3 ms                                                                | 24.2 ms: 1.00x faster                                                      |
| regex_compile  | 127 ms                                                                 | 126 ms: 1.00x faster                                                       |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250325-linux-x86_64-brandtbucher-null_stack_pointer-3.14.0a6+-7b432e3 |
|----------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 2.01 sec                                                               | 1.95 sec: 1.03x faster                                                     |
| xml_etree_iterparse  | 98.9 ms                                                                | 97.4 ms: 1.02x faster                                                      |
| pickle_pure_python   | 318 us                                                                 | 315 us: 1.01x faster                                                       |
| xml_etree_parse      | 141 ms                                                                 | 140 ms: 1.01x faster                                                       |
| unpickle_pure_python | 220 us                                                                 | 218 us: 1.01x faster                                                       |
| Geometric mean       | (ref)                                                                  | 1.01x faster                                                               |

Benchmark hidden because not significant (4): json_dumps, json_loads, xml_etree_generate, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250325-linux-x86_64-brandtbucher-null_stack_pointer-3.14.0a6+-7b432e3 |
|------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 13.1 ms                                                                | 13.1 ms: 1.00x slower                                                      |
| python_startup_no_site | 8.18 ms                                                                | 8.21 ms: 1.00x slower                                                      |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250325-linux-x86_64-brandtbucher-null_stack_pointer-3.14.0a6+-7b432e3 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako           | 11.4 ms                                                                | 11.0 ms: 1.03x faster                                                      |
| genshi_xml     | 48.8 ms                                                                | 48.4 ms: 1.01x faster                                                      |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                               |

Benchmark hidden because not significant (2): django_template, genshi_text

All benchmarks:
===============

| Benchmark                | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250325-linux-x86_64-brandtbucher-null_stack_pointer-3.14.0a6+-7b432e3 |
|--------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| gc_traversal             | 5.07 ms                                                                | 4.82 ms: 1.05x faster                                                      |
| deepcopy_reduce          | 2.71 us                                                                | 2.62 us: 1.04x faster                                                      |
| scimark_sparse_mat_mult  | 4.95 ms                                                                | 4.79 ms: 1.03x faster                                                      |
| mako                     | 11.4 ms                                                                | 11.0 ms: 1.03x faster                                                      |
| chaos                    | 60.3 ms                                                                | 58.4 ms: 1.03x faster                                                      |
| pyflate                  | 443 ms                                                                 | 429 ms: 1.03x faster                                                       |
| logging_format           | 6.34 us                                                                | 6.15 us: 1.03x faster                                                      |
| tomli_loads              | 2.01 sec                                                               | 1.95 sec: 1.03x faster                                                     |
| generators               | 28.7 ms                                                                | 27.9 ms: 1.03x faster                                                      |
| deepcopy_memo            | 30.1 us                                                                | 29.3 us: 1.03x faster                                                      |
| nbody                    | 99.1 ms                                                                | 96.6 ms: 1.03x faster                                                      |
| logging_simple           | 5.72 us                                                                | 5.59 us: 1.02x faster                                                      |
| scimark_fft              | 356 ms                                                                 | 348 ms: 1.02x faster                                                       |
| regex_dna                | 227 ms                                                                 | 223 ms: 1.02x faster                                                       |
| float                    | 70.3 ms                                                                | 68.9 ms: 1.02x faster                                                      |
| regex_effbot             | 3.50 ms                                                                | 3.43 ms: 1.02x faster                                                      |
| scimark_monte_carlo      | 68.7 ms                                                                | 67.4 ms: 1.02x faster                                                      |
| mdp                      | 2.53 sec                                                               | 2.48 sec: 1.02x faster                                                     |
| sqlglot_v2_parse         | 1.26 ms                                                                | 1.24 ms: 1.02x faster                                                      |
| sqlglot_v2_transpile     | 1.57 ms                                                                | 1.55 ms: 1.02x faster                                                      |
| richards                 | 43.7 ms                                                                | 42.9 ms: 1.02x faster                                                      |
| xml_etree_iterparse      | 98.9 ms                                                                | 97.4 ms: 1.02x faster                                                      |
| shortest_path            | 498 ms                                                                 | 491 ms: 1.01x faster                                                       |
| pathlib                  | 16.9 ms                                                                | 16.7 ms: 1.01x faster                                                      |
| fannkuch                 | 431 ms                                                                 | 425 ms: 1.01x faster                                                       |
| pprint_safe_repr         | 744 ms                                                                 | 734 ms: 1.01x faster                                                       |
| richards_super           | 50.0 ms                                                                | 49.4 ms: 1.01x faster                                                      |
| dulwich_log              | 59.0 ms                                                                | 58.3 ms: 1.01x faster                                                      |
| pprint_pformat           | 1.52 sec                                                               | 1.50 sec: 1.01x faster                                                     |
| sqlglot_v2_optimize      | 53.0 ms                                                                | 52.4 ms: 1.01x faster                                                      |
| connected_components     | 459 ms                                                                 | 454 ms: 1.01x faster                                                       |
| sqlalchemy_declarative   | 131 ms                                                                 | 129 ms: 1.01x faster                                                       |
| go                       | 114 ms                                                                 | 113 ms: 1.01x faster                                                       |
| raytrace                 | 266 ms                                                                 | 263 ms: 1.01x faster                                                       |
| genshi_xml               | 48.8 ms                                                                | 48.4 ms: 1.01x faster                                                      |
| pickle_pure_python       | 318 us                                                                 | 315 us: 1.01x faster                                                       |
| 2to3                     | 258 ms                                                                 | 256 ms: 1.01x faster                                                       |
| xml_etree_parse          | 141 ms                                                                 | 140 ms: 1.01x faster                                                       |
| sqlglot_v2_normalize     | 106 ms                                                                 | 105 ms: 1.01x faster                                                       |
| deepcopy                 | 262 us                                                                 | 260 us: 1.01x faster                                                       |
| create_gc_cycles         | 2.50 ms                                                                | 2.48 ms: 1.01x faster                                                      |
| unpickle_pure_python     | 220 us                                                                 | 218 us: 1.01x faster                                                       |
| sqlalchemy_imperative    | 16.8 ms                                                                | 16.7 ms: 1.01x faster                                                      |
| sympy_integrate          | 19.5 ms                                                                | 19.4 ms: 1.01x faster                                                      |
| docutils                 | 2.62 sec                                                               | 2.60 sec: 1.01x faster                                                     |
| meteor_contest           | 108 ms                                                                 | 107 ms: 1.01x faster                                                       |
| sympy_expand             | 459 ms                                                                 | 457 ms: 1.01x faster                                                       |
| sympy_str                | 268 ms                                                                 | 267 ms: 1.00x faster                                                       |
| regex_v8                 | 24.3 ms                                                                | 24.2 ms: 1.00x faster                                                      |
| regex_compile            | 127 ms                                                                 | 126 ms: 1.00x faster                                                       |
| crypto_pyaes             | 75.7 ms                                                                | 75.4 ms: 1.00x faster                                                      |
| bpe_tokeniser            | 4.59 sec                                                               | 4.58 sec: 1.00x faster                                                     |
| comprehensions           | 16.6 us                                                                | 16.5 us: 1.00x faster                                                      |
| pidigits                 | 186 ms                                                                 | 186 ms: 1.00x slower                                                       |
| python_startup           | 13.1 ms                                                                | 13.1 ms: 1.00x slower                                                      |
| python_startup_no_site   | 8.18 ms                                                                | 8.21 ms: 1.00x slower                                                      |
| bench_mp_pool            | 82.8 ms                                                                | 83.2 ms: 1.00x slower                                                      |
| coroutines               | 23.6 ms                                                                | 23.8 ms: 1.01x slower                                                      |
| json                     | 5.29 ms                                                                | 5.33 ms: 1.01x slower                                                      |
| async_tree_cpu_io_mixed  | 486 ms                                                                 | 490 ms: 1.01x slower                                                       |
| deltablue                | 3.07 ms                                                                | 3.09 ms: 1.01x slower                                                      |
| subparsers               | 20.8 ms                                                                | 21.1 ms: 1.01x slower                                                      |
| scimark_lu               | 116 ms                                                                 | 117 ms: 1.01x slower                                                       |
| hexiom                   | 6.20 ms                                                                | 6.29 ms: 1.01x slower                                                      |
| typing_runtime_protocols | 159 us                                                                 | 163 us: 1.02x slower                                                       |
| logging_silent           | 95.6 ns                                                                | 97.8 ns: 1.02x slower                                                      |
| Geometric mean           | (ref)                                                                  | 1.01x faster                                                               |

Benchmark hidden because not significant (30): k_core, async_tree_none_tg, scimark_sor, spectral_norm, pylint, sphinx, django_template, json_dumps, sqlite_synth, nqueens, sympy_sum, bench_thread_pool, async_generators, many_optionals, json_loads, async_tree_none, telco, asyncio_websockets, xml_etree_generate, genshi_text, async_tree_memoization_tg, xml_etree_process, html5lib, async_tree_io, async_tree_memoization, thrift, pycparser, async_tree_cpu_io_mixed_tg, async_tree_io_tg, coverage

- Geometric mean (including insignificant results): 1.007x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x