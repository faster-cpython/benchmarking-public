# Results vs. base

- fork: brandtbucher
- ref: jit_has_space
- machine: linux-x86_64
- commit hash: 0c7e399
- commit date: 2025-03-25
- overall geometric mean: 1.001x slower
- HPT reliability: 99.87%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250325-linux-x86_64-brandtbucher-jit_has_space-3.14.0a6+-0c7e399 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 263 ms                                                                 | 264 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                          |

Benchmark hidden because not significant (3): docutils, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250325-linux-x86_64-brandtbucher-jit_has_space-3.14.0a6+-0c7e399 |
|-------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none_tg      | 255 ms                                                                 | 253 ms: 1.01x faster                                                  |
| async_generators        | 418 ms                                                                 | 415 ms: 1.01x faster                                                  |
| async_tree_cpu_io_mixed | 492 ms                                                                 | 499 ms: 1.01x slower                                                  |
| Geometric mean          | (ref)                                                                  | 1.00x faster                                                          |

Benchmark hidden because not significant (8): async_tree_memoization_tg, async_tree_memoization, async_tree_io_tg, asyncio_websockets, async_tree_cpu_io_mixed_tg, async_tree_none, coroutines, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250325-linux-x86_64-brandtbucher-jit_has_space-3.14.0a6+-0c7e399 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 89.4 ms                                                                | 87.5 ms: 1.02x faster                                                 |
| pidigits       | 186 ms                                                                 | 186 ms: 1.00x slower                                                  |
| float          | 64.9 ms                                                                | 65.3 ms: 1.01x slower                                                 |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250325-linux-x86_64-brandtbucher-jit_has_space-3.14.0a6+-0c7e399 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_v8       | 23.5 ms                                                                | 22.7 ms: 1.04x faster                                                 |
| regex_dna      | 217 ms                                                                 | 213 ms: 1.02x faster                                                  |
| regex_effbot   | 3.16 ms                                                                | 3.14 ms: 1.01x faster                                                 |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                          |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250325-linux-x86_64-brandtbucher-jit_has_space-3.14.0a6+-0c7e399 |
|---------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python  | 325 us                                                                 | 322 us: 1.01x faster                                                  |
| json_loads          | 30.1 us                                                                | 29.9 us: 1.01x faster                                                 |
| xml_etree_iterparse | 97.6 ms                                                                | 98.4 ms: 1.01x slower                                                 |
| Geometric mean      | (ref)                                                                  | 1.00x faster                                                          |

Benchmark hidden because not significant (6): xml_etree_process, xml_etree_generate, json_dumps, xml_etree_parse, unpickle_pure_python, tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250325-linux-x86_64-brandtbucher-jit_has_space-3.14.0a6+-0c7e399 |
|------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 13.1 ms                                                                | 13.1 ms: 1.00x faster                                                 |
| python_startup_no_site | 8.19 ms                                                                | 8.18 ms: 1.00x faster                                                 |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250325-linux-x86_64-brandtbucher-jit_has_space-3.14.0a6+-0c7e399 |
|-----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 11.0 ms                                                                | 10.9 ms: 1.01x faster                                                 |
| django_template | 32.0 ms                                                                | 31.8 ms: 1.01x faster                                                 |
| genshi_xml      | 49.8 ms                                                                | 50.3 ms: 1.01x slower                                                 |
| Geometric mean  | (ref)                                                                  | 1.00x faster                                                          |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark               | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250325-linux-x86_64-brandtbucher-jit_has_space-3.14.0a6+-0c7e399 |
|-------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| gc_traversal            | 5.05 ms                                                                | 4.85 ms: 1.04x faster                                                 |
| regex_v8                | 23.5 ms                                                                | 22.7 ms: 1.04x faster                                                 |
| nbody                   | 89.4 ms                                                                | 87.5 ms: 1.02x faster                                                 |
| telco                   | 7.93 ms                                                                | 7.79 ms: 1.02x faster                                                 |
| regex_dna               | 217 ms                                                                 | 213 ms: 1.02x faster                                                  |
| mako                    | 11.0 ms                                                                | 10.9 ms: 1.01x faster                                                 |
| pickle_pure_python      | 325 us                                                                 | 322 us: 1.01x faster                                                  |
| async_tree_none_tg      | 255 ms                                                                 | 253 ms: 1.01x faster                                                  |
| bench_mp_pool           | 83.3 ms                                                                | 82.7 ms: 1.01x faster                                                 |
| pathlib                 | 16.8 ms                                                                | 16.6 ms: 1.01x faster                                                 |
| async_generators        | 418 ms                                                                 | 415 ms: 1.01x faster                                                  |
| json_loads              | 30.1 us                                                                | 29.9 us: 1.01x faster                                                 |
| regex_effbot            | 3.16 ms                                                                | 3.14 ms: 1.01x faster                                                 |
| hexiom                  | 6.86 ms                                                                | 6.81 ms: 1.01x faster                                                 |
| django_template         | 32.0 ms                                                                | 31.8 ms: 1.01x faster                                                 |
| scimark_lu              | 118 ms                                                                 | 117 ms: 1.01x faster                                                  |
| python_startup          | 13.1 ms                                                                | 13.1 ms: 1.00x faster                                                 |
| python_startup_no_site  | 8.19 ms                                                                | 8.18 ms: 1.00x faster                                                 |
| pidigits                | 186 ms                                                                 | 186 ms: 1.00x slower                                                  |
| create_gc_cycles        | 2.48 ms                                                                | 2.49 ms: 1.00x slower                                                 |
| sqlalchemy_declarative  | 133 ms                                                                 | 133 ms: 1.00x slower                                                  |
| scimark_sor             | 119 ms                                                                 | 119 ms: 1.00x slower                                                  |
| sympy_expand            | 475 ms                                                                 | 477 ms: 1.00x slower                                                  |
| sympy_integrate         | 20.0 ms                                                                | 20.1 ms: 1.01x slower                                                 |
| scimark_fft             | 312 ms                                                                 | 313 ms: 1.01x slower                                                  |
| 2to3                    | 263 ms                                                                 | 264 ms: 1.01x slower                                                  |
| sympy_str               | 274 ms                                                                 | 276 ms: 1.01x slower                                                  |
| float                   | 64.9 ms                                                                | 65.3 ms: 1.01x slower                                                 |
| shortest_path           | 494 ms                                                                 | 498 ms: 1.01x slower                                                  |
| meteor_contest          | 108 ms                                                                 | 109 ms: 1.01x slower                                                  |
| logging_simple          | 5.59 us                                                                | 5.63 us: 1.01x slower                                                 |
| xml_etree_iterparse     | 97.6 ms                                                                | 98.4 ms: 1.01x slower                                                 |
| mdp                     | 2.48 sec                                                               | 2.50 sec: 1.01x slower                                                |
| deltablue               | 3.06 ms                                                                | 3.08 ms: 1.01x slower                                                 |
| sympy_sum               | 152 ms                                                                 | 153 ms: 1.01x slower                                                  |
| raytrace                | 269 ms                                                                 | 271 ms: 1.01x slower                                                  |
| connected_components    | 454 ms                                                                 | 458 ms: 1.01x slower                                                  |
| genshi_xml              | 49.8 ms                                                                | 50.3 ms: 1.01x slower                                                 |
| sqlglot_v2_normalize    | 107 ms                                                                 | 109 ms: 1.01x slower                                                  |
| bpe_tokeniser           | 4.57 sec                                                               | 4.63 sec: 1.01x slower                                                |
| logging_format          | 6.16 us                                                                | 6.24 us: 1.01x slower                                                 |
| async_tree_cpu_io_mixed | 492 ms                                                                 | 499 ms: 1.01x slower                                                  |
| coverage                | 85.5 ms                                                                | 86.7 ms: 1.01x slower                                                 |
| richards                | 35.8 ms                                                                | 36.4 ms: 1.02x slower                                                 |
| deepcopy_reduce         | 2.66 us                                                                | 2.71 us: 1.02x slower                                                 |
| logging_silent          | 95.7 ns                                                                | 98.2 ns: 1.03x slower                                                 |
| scimark_sparse_mat_mult | 4.61 ms                                                                | 4.75 ms: 1.03x slower                                                 |
| pyflate                 | 432 ms                                                                 | 450 ms: 1.04x slower                                                  |
| Geometric mean          | (ref)                                                                  | 1.00x slower                                                          |

Benchmark hidden because not significant (48): thrift, async_tree_memoization_tg, async_tree_memoization, comprehensions, xml_etree_process, pprint_safe_repr, k_core, async_tree_io_tg, generators, chaos, xml_etree_generate, deepcopy, bench_thread_pool, crypto_pyaes, asyncio_websockets, docutils, async_tree_cpu_io_mixed_tg, deepcopy_memo, fannkuch, spectral_norm, html5lib, json_dumps, genshi_text, sqlite_synth, subparsers, pprint_pformat, scimark_monte_carlo, xml_etree_parse, async_tree_none, many_optionals, regex_compile, sqlglot_v2_transpile, sphinx, nqueens, dulwich_log, unpickle_pure_python, sqlglot_v2_optimize, pylint, sqlalchemy_imperative, coroutines, sqlglot_v2_parse, tomli_loads, go, richards_super, json, async_tree_io, typing_runtime_protocols, pycparser

- Geometric mean (including insignificant results): 1.001x slower

# HPT report

- Reliability score: 99.87% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x