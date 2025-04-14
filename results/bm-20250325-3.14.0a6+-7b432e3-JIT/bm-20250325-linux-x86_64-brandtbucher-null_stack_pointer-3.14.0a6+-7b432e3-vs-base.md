# Results vs. base

- fork: brandtbucher
- ref: null_stack_pointer
- machine: linux-x86_64
- commit hash: 7b432e3
- commit date: 2025-03-25
- overall geometric mean: 1.004x faster
- HPT reliability: 93.21%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250325-linux-x86_64-brandtbucher-null_stack_pointer-3.14.0a6+-7b432e3 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| docutils       | 2.69 sec                                                               | 2.67 sec: 1.01x faster                                                     |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                               |

Benchmark hidden because not significant (3): 2to3, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark              | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250325-linux-x86_64-brandtbucher-null_stack_pointer-3.14.0a6+-7b432e3 |
|------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| coroutines             | 24.1 ms                                                                | 23.1 ms: 1.04x faster                                                      |
| async_tree_none_tg     | 255 ms                                                                 | 252 ms: 1.01x faster                                                       |
| async_tree_memoization | 319 ms                                                                 | 315 ms: 1.01x faster                                                       |
| async_tree_none        | 266 ms                                                                 | 263 ms: 1.01x faster                                                       |
| async_generators       | 418 ms                                                                 | 414 ms: 1.01x faster                                                       |
| Geometric mean         | (ref)                                                                  | 1.01x faster                                                               |

Benchmark hidden because not significant (6): async_tree_memoization_tg, async_tree_io, async_tree_cpu_io_mixed_tg, asyncio_websockets, async_tree_io_tg, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250325-linux-x86_64-brandtbucher-null_stack_pointer-3.14.0a6+-7b432e3 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 89.4 ms                                                                | 88.1 ms: 1.02x faster                                                      |
| pidigits       | 186 ms                                                                 | 186 ms: 1.00x faster                                                       |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                               |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250325-linux-x86_64-brandtbucher-null_stack_pointer-3.14.0a6+-7b432e3 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 23.5 ms                                                                | 23.2 ms: 1.01x faster                                                      |
| regex_dna      | 217 ms                                                                 | 216 ms: 1.00x faster                                                       |
| regex_compile  | 128 ms                                                                 | 128 ms: 1.00x slower                                                       |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                               |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250325-linux-x86_64-brandtbucher-null_stack_pointer-3.14.0a6+-7b432e3 |
|----------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| unpickle_pure_python | 214 us                                                                 | 210 us: 1.02x faster                                                       |
| xml_etree_process    | 57.1 ms                                                                | 56.1 ms: 1.02x faster                                                      |
| pickle_pure_python   | 325 us                                                                 | 321 us: 1.01x faster                                                       |
| xml_etree_parse      | 140 ms                                                                 | 139 ms: 1.01x faster                                                       |
| xml_etree_generate   | 80.8 ms                                                                | 80.2 ms: 1.01x faster                                                      |
| Geometric mean       | (ref)                                                                  | 1.01x faster                                                               |

Benchmark hidden because not significant (4): json_loads, tomli_loads, json_dumps, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250325-linux-x86_64-brandtbucher-null_stack_pointer-3.14.0a6+-7b432e3 |
|------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 13.1 ms                                                                | 13.1 ms: 1.00x slower                                                      |
| python_startup_no_site | 8.19 ms                                                                | 8.22 ms: 1.00x slower                                                      |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250325-linux-x86_64-brandtbucher-null_stack_pointer-3.14.0a6+-7b432e3 |
|-----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 32.0 ms                                                                | 31.7 ms: 1.01x faster                                                      |
| genshi_xml      | 49.8 ms                                                                | 50.3 ms: 1.01x slower                                                      |
| Geometric mean  | (ref)                                                                  | 1.00x slower                                                               |

Benchmark hidden because not significant (2): genshi_text, mako

All benchmarks:
===============

| Benchmark                | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250325-linux-x86_64-brandtbucher-null_stack_pointer-3.14.0a6+-7b432e3 |
|--------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| spectral_norm            | 97.1 ms                                                                | 92.7 ms: 1.05x faster                                                      |
| gc_traversal             | 5.05 ms                                                                | 4.84 ms: 1.04x faster                                                      |
| coroutines               | 24.1 ms                                                                | 23.1 ms: 1.04x faster                                                      |
| scimark_lu               | 118 ms                                                                 | 114 ms: 1.03x faster                                                       |
| generators               | 29.2 ms                                                                | 28.4 ms: 1.03x faster                                                      |
| comprehensions           | 19.0 us                                                                | 18.5 us: 1.03x faster                                                      |
| thrift                   | 783 us                                                                 | 765 us: 1.02x faster                                                       |
| telco                    | 7.93 ms                                                                | 7.77 ms: 1.02x faster                                                      |
| richards_super           | 41.1 ms                                                                | 40.2 ms: 1.02x faster                                                      |
| unpickle_pure_python     | 214 us                                                                 | 210 us: 1.02x faster                                                       |
| xml_etree_process        | 57.1 ms                                                                | 56.1 ms: 1.02x faster                                                      |
| logging_simple           | 5.59 us                                                                | 5.49 us: 1.02x faster                                                      |
| nbody                    | 89.4 ms                                                                | 88.1 ms: 1.02x faster                                                      |
| async_tree_none_tg       | 255 ms                                                                 | 252 ms: 1.01x faster                                                       |
| scimark_fft              | 312 ms                                                                 | 307 ms: 1.01x faster                                                       |
| scimark_monte_carlo      | 68.6 ms                                                                | 67.7 ms: 1.01x faster                                                      |
| async_tree_memoization   | 319 ms                                                                 | 315 ms: 1.01x faster                                                       |
| chaos                    | 60.3 ms                                                                | 59.6 ms: 1.01x faster                                                      |
| pickle_pure_python       | 325 us                                                                 | 321 us: 1.01x faster                                                       |
| async_tree_none          | 266 ms                                                                 | 263 ms: 1.01x faster                                                       |
| deltablue                | 3.06 ms                                                                | 3.02 ms: 1.01x faster                                                      |
| regex_v8                 | 23.5 ms                                                                | 23.2 ms: 1.01x faster                                                      |
| django_template          | 32.0 ms                                                                | 31.7 ms: 1.01x faster                                                      |
| pathlib                  | 16.8 ms                                                                | 16.6 ms: 1.01x faster                                                      |
| xml_etree_parse          | 140 ms                                                                 | 139 ms: 1.01x faster                                                       |
| xml_etree_generate       | 80.8 ms                                                                | 80.2 ms: 1.01x faster                                                      |
| typing_runtime_protocols | 167 us                                                                 | 166 us: 1.01x faster                                                       |
| async_generators         | 418 ms                                                                 | 414 ms: 1.01x faster                                                       |
| richards                 | 35.8 ms                                                                | 35.5 ms: 1.01x faster                                                      |
| scimark_sparse_mat_mult  | 4.61 ms                                                                | 4.57 ms: 1.01x faster                                                      |
| logging_format           | 6.16 us                                                                | 6.12 us: 1.01x faster                                                      |
| docutils                 | 2.69 sec                                                               | 2.67 sec: 1.01x faster                                                     |
| hexiom                   | 6.86 ms                                                                | 6.82 ms: 1.01x faster                                                      |
| regex_dna                | 217 ms                                                                 | 216 ms: 1.00x faster                                                       |
| pidigits                 | 186 ms                                                                 | 186 ms: 1.00x faster                                                       |
| python_startup           | 13.1 ms                                                                | 13.1 ms: 1.00x slower                                                      |
| sqlalchemy_declarative   | 133 ms                                                                 | 133 ms: 1.00x slower                                                       |
| regex_compile            | 128 ms                                                                 | 128 ms: 1.00x slower                                                       |
| sympy_expand             | 475 ms                                                                 | 476 ms: 1.00x slower                                                       |
| python_startup_no_site   | 8.19 ms                                                                | 8.22 ms: 1.00x slower                                                      |
| mdp                      | 2.48 sec                                                               | 2.49 sec: 1.00x slower                                                     |
| sqlglot_v2_parse         | 1.29 ms                                                                | 1.30 ms: 1.01x slower                                                      |
| create_gc_cycles         | 2.48 ms                                                                | 2.50 ms: 1.01x slower                                                      |
| scimark_sor              | 119 ms                                                                 | 119 ms: 1.01x slower                                                       |
| sqlalchemy_imperative    | 17.1 ms                                                                | 17.2 ms: 1.01x slower                                                      |
| genshi_xml               | 49.8 ms                                                                | 50.3 ms: 1.01x slower                                                      |
| json                     | 5.29 ms                                                                | 5.34 ms: 1.01x slower                                                      |
| nqueens                  | 84.9 ms                                                                | 86.2 ms: 1.02x slower                                                      |
| deepcopy_memo            | 29.0 us                                                                | 29.5 us: 1.02x slower                                                      |
| pyflate                  | 432 ms                                                                 | 442 ms: 1.02x slower                                                       |
| logging_silent           | 95.7 ns                                                                | 98.2 ns: 1.03x slower                                                      |
| pprint_safe_repr         | 756 ms                                                                 | 783 ms: 1.04x slower                                                       |
| pprint_pformat           | 1.55 sec                                                               | 1.62 sec: 1.05x slower                                                     |
| Geometric mean           | (ref)                                                                  | 1.00x faster                                                               |

Benchmark hidden because not significant (43): async_tree_memoization_tg, json_loads, deepcopy, go, crypto_pyaes, async_tree_io, tomli_loads, json_dumps, sqlglot_v2_transpile, sqlglot_v2_optimize, pylint, async_tree_cpu_io_mixed_tg, asyncio_websockets, bench_mp_pool, sqlglot_v2_normalize, sympy_integrate, connected_components, async_tree_io_tg, dulwich_log, 2to3, regex_effbot, sphinx, shortest_path, many_optionals, meteor_contest, bench_thread_pool, sympy_sum, k_core, async_tree_cpu_io_mixed, raytrace, sympy_str, float, xml_etree_iterparse, subparsers, bpe_tokeniser, genshi_text, sqlite_synth, fannkuch, html5lib, pycparser, coverage, deepcopy_reduce, mako

- Geometric mean (including insignificant results): 1.004x faster

# HPT report

- Reliability score: 93.21% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x