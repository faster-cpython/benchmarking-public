# Results vs. base

- fork: brandtbucher
- ref: jit_build_and_iter
- machine: linux-x86_64
- commit hash: 488d5b8
- commit date: 2025-03-27
- overall geometric mean: 1.003x slower
- HPT reliability: 96.08%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250327-linux-x86_64-brandtbucher-jit_build_and_iter-3.14.0a6+-488d5b8 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 263 ms                                                                 | 264 ms: 1.00x slower                                                       |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                               |

Benchmark hidden because not significant (3): docutils, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark              | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250327-linux-x86_64-brandtbucher-jit_build_and_iter-3.14.0a6+-488d5b8 |
|------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| coroutines             | 24.1 ms                                                                | 23.3 ms: 1.03x faster                                                      |
| async_generators       | 418 ms                                                                 | 412 ms: 1.01x faster                                                       |
| async_tree_memoization | 319 ms                                                                 | 316 ms: 1.01x faster                                                       |
| Geometric mean         | (ref)                                                                  | 1.01x faster                                                               |

Benchmark hidden because not significant (8): async_tree_memoization_tg, async_tree_none_tg, async_tree_cpu_io_mixed_tg, async_tree_none, async_tree_io_tg, async_tree_cpu_io_mixed, async_tree_io, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250327-linux-x86_64-brandtbucher-jit_build_and_iter-3.14.0a6+-488d5b8 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 89.4 ms                                                                | 88.4 ms: 1.01x faster                                                      |
| float          | 64.9 ms                                                                | 65.7 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250327-linux-x86_64-brandtbucher-jit_build_and_iter-3.14.0a6+-488d5b8 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 128 ms                                                                 | 129 ms: 1.01x slower                                                       |
| regex_v8       | 23.5 ms                                                                | 23.7 ms: 1.01x slower                                                      |
| regex_effbot   | 3.16 ms                                                                | 3.20 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                               |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250327-linux-x86_64-brandtbucher-jit_build_and_iter-3.14.0a6+-488d5b8 |
|----------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_loads           | 30.1 us                                                                | 29.7 us: 1.01x faster                                                      |
| xml_etree_process    | 57.1 ms                                                                | 56.6 ms: 1.01x faster                                                      |
| xml_etree_parse      | 140 ms                                                                 | 139 ms: 1.01x faster                                                       |
| json_dumps           | 11.6 ms                                                                | 11.6 ms: 1.01x slower                                                      |
| unpickle_pure_python | 214 us                                                                 | 216 us: 1.01x slower                                                       |
| Geometric mean       | (ref)                                                                  | 1.00x faster                                                               |

Benchmark hidden because not significant (4): xml_etree_generate, pickle_pure_python, tomli_loads, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250327-linux-x86_64-brandtbucher-jit_build_and_iter-3.14.0a6+-488d5b8 |
|------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 13.1 ms                                                                | 13.2 ms: 1.01x slower                                                      |
| python_startup_no_site | 8.19 ms                                                                | 8.24 ms: 1.01x slower                                                      |
| Geometric mean         | (ref)                                                                  | 1.01x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250327-linux-x86_64-brandtbucher-jit_build_and_iter-3.14.0a6+-488d5b8 |
|-----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 11.0 ms                                                                | 11.0 ms: 1.00x faster                                                      |
| django_template | 32.0 ms                                                                | 32.2 ms: 1.01x slower                                                      |
| Geometric mean  | (ref)                                                                  | 1.00x faster                                                               |

Benchmark hidden because not significant (2): genshi_text, genshi_xml

All benchmarks:
===============

| Benchmark               | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250327-linux-x86_64-brandtbucher-jit_build_and_iter-3.14.0a6+-488d5b8 |
|-------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| gc_traversal            | 5.05 ms                                                                | 4.83 ms: 1.04x faster                                                      |
| coroutines              | 24.1 ms                                                                | 23.3 ms: 1.03x faster                                                      |
| generators              | 29.2 ms                                                                | 28.6 ms: 1.02x faster                                                      |
| spectral_norm           | 97.1 ms                                                                | 95.2 ms: 1.02x faster                                                      |
| telco                   | 7.93 ms                                                                | 7.82 ms: 1.01x faster                                                      |
| async_generators        | 418 ms                                                                 | 412 ms: 1.01x faster                                                       |
| json_loads              | 30.1 us                                                                | 29.7 us: 1.01x faster                                                      |
| pyflate                 | 432 ms                                                                 | 427 ms: 1.01x faster                                                       |
| comprehensions          | 19.0 us                                                                | 18.8 us: 1.01x faster                                                      |
| nbody                   | 89.4 ms                                                                | 88.4 ms: 1.01x faster                                                      |
| xml_etree_process       | 57.1 ms                                                                | 56.6 ms: 1.01x faster                                                      |
| thrift                  | 783 us                                                                 | 776 us: 1.01x faster                                                       |
| chaos                   | 60.3 ms                                                                | 59.8 ms: 1.01x faster                                                      |
| async_tree_memoization  | 319 ms                                                                 | 316 ms: 1.01x faster                                                       |
| fannkuch                | 423 ms                                                                 | 420 ms: 1.01x faster                                                       |
| xml_etree_parse         | 140 ms                                                                 | 139 ms: 1.01x faster                                                       |
| mako                    | 11.0 ms                                                                | 11.0 ms: 1.00x faster                                                      |
| create_gc_cycles        | 2.48 ms                                                                | 2.49 ms: 1.00x slower                                                      |
| 2to3                    | 263 ms                                                                 | 264 ms: 1.00x slower                                                       |
| sympy_integrate         | 20.0 ms                                                                | 20.1 ms: 1.00x slower                                                      |
| sympy_str               | 274 ms                                                                 | 275 ms: 1.00x slower                                                       |
| deltablue               | 3.06 ms                                                                | 3.07 ms: 1.00x slower                                                      |
| dulwich_log             | 60.6 ms                                                                | 60.9 ms: 1.00x slower                                                      |
| mdp                     | 2.48 sec                                                               | 2.49 sec: 1.01x slower                                                     |
| sqlglot_v2_parse        | 1.29 ms                                                                | 1.30 ms: 1.01x slower                                                      |
| regex_compile           | 128 ms                                                                 | 129 ms: 1.01x slower                                                       |
| python_startup          | 13.1 ms                                                                | 13.2 ms: 1.01x slower                                                      |
| go                      | 128 ms                                                                 | 129 ms: 1.01x slower                                                       |
| pathlib                 | 16.8 ms                                                                | 16.9 ms: 1.01x slower                                                      |
| python_startup_no_site  | 8.19 ms                                                                | 8.24 ms: 1.01x slower                                                      |
| json_dumps              | 11.6 ms                                                                | 11.6 ms: 1.01x slower                                                      |
| django_template         | 32.0 ms                                                                | 32.2 ms: 1.01x slower                                                      |
| sqlglot_v2_optimize     | 54.1 ms                                                                | 54.5 ms: 1.01x slower                                                      |
| sqlalchemy_declarative  | 133 ms                                                                 | 134 ms: 1.01x slower                                                       |
| scimark_fft             | 312 ms                                                                 | 314 ms: 1.01x slower                                                       |
| sqlglot_v2_normalize    | 107 ms                                                                 | 108 ms: 1.01x slower                                                       |
| unpickle_pure_python    | 214 us                                                                 | 216 us: 1.01x slower                                                       |
| deepcopy_memo           | 29.0 us                                                                | 29.2 us: 1.01x slower                                                      |
| meteor_contest          | 108 ms                                                                 | 109 ms: 1.01x slower                                                       |
| sympy_sum               | 152 ms                                                                 | 153 ms: 1.01x slower                                                       |
| regex_v8                | 23.5 ms                                                                | 23.7 ms: 1.01x slower                                                      |
| logging_simple          | 5.59 us                                                                | 5.65 us: 1.01x slower                                                      |
| float                   | 64.9 ms                                                                | 65.7 ms: 1.01x slower                                                      |
| bpe_tokeniser           | 4.57 sec                                                               | 4.62 sec: 1.01x slower                                                     |
| regex_effbot            | 3.16 ms                                                                | 3.20 ms: 1.01x slower                                                      |
| richards                | 35.8 ms                                                                | 36.2 ms: 1.01x slower                                                      |
| crypto_pyaes            | 78.3 ms                                                                | 79.3 ms: 1.01x slower                                                      |
| subparsers              | 21.0 ms                                                                | 21.3 ms: 1.01x slower                                                      |
| deepcopy                | 260 us                                                                 | 263 us: 1.01x slower                                                       |
| scimark_sparse_mat_mult | 4.61 ms                                                                | 4.67 ms: 1.01x slower                                                      |
| sqlalchemy_imperative   | 17.1 ms                                                                | 17.3 ms: 1.01x slower                                                      |
| raytrace                | 269 ms                                                                 | 273 ms: 1.02x slower                                                       |
| connected_components    | 454 ms                                                                 | 461 ms: 1.02x slower                                                       |
| deepcopy_reduce         | 2.66 us                                                                | 2.71 us: 1.02x slower                                                      |
| shortest_path           | 494 ms                                                                 | 503 ms: 1.02x slower                                                       |
| pycparser               | 1.13 sec                                                               | 1.15 sec: 1.02x slower                                                     |
| logging_format          | 6.16 us                                                                | 6.27 us: 1.02x slower                                                      |
| scimark_sor             | 119 ms                                                                 | 121 ms: 1.02x slower                                                       |
| coverage                | 85.5 ms                                                                | 88.9 ms: 1.04x slower                                                      |
| logging_silent          | 95.7 ns                                                                | 100 ns: 1.05x slower                                                       |
| pprint_pformat          | 1.55 sec                                                               | 1.64 sec: 1.06x slower                                                     |
| pprint_safe_repr        | 756 ms                                                                 | 804 ms: 1.06x slower                                                       |
| Geometric mean          | (ref)                                                                  | 1.00x slower                                                               |

Benchmark hidden because not significant (34): async_tree_memoization_tg, async_tree_none_tg, async_tree_cpu_io_mixed_tg, scimark_monte_carlo, nqueens, async_tree_none, genshi_text, async_tree_io_tg, genshi_xml, typing_runtime_protocols, xml_etree_generate, scimark_lu, async_tree_cpu_io_mixed, pidigits, regex_dna, json, pickle_pure_python, bench_thread_pool, k_core, async_tree_io, docutils, asyncio_websockets, many_optionals, tomli_loads, bench_mp_pool, sympy_expand, pylint, hexiom, xml_etree_iterparse, sqlite_synth, sqlglot_v2_transpile, html5lib, sphinx, richards_super

- Geometric mean (including insignificant results): 1.003x slower

# HPT report

- Reliability score: 96.08% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x