# Results vs. base

- fork: brandtbucher
- ref: jit_up_12_11
- machine: linux-x86_64
- commit hash: 9ee2a07
- commit date: 2025-03-26
- overall geometric mean: 1.002x slower
- HPT reliability: 78.76%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250326-linux-x86_64-brandtbucher-jit_up_12_11-3.14.0a6+-9ee2a07 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 263 ms                                                                 | 264 ms: 1.01x slower                                                 |
| html5lib       | 63.2 ms                                                                | 62.3 ms: 1.02x faster                                                |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                         |

Benchmark hidden because not significant (2): docutils, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250326-linux-x86_64-brandtbucher-jit_up_12_11-3.14.0a6+-9ee2a07 |
|-------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| coroutines              | 24.1 ms                                                                | 23.3 ms: 1.03x faster                                                |
| async_tree_none_tg      | 255 ms                                                                 | 253 ms: 1.01x faster                                                 |
| async_generators        | 418 ms                                                                 | 415 ms: 1.01x faster                                                 |
| async_tree_cpu_io_mixed | 492 ms                                                                 | 494 ms: 1.00x slower                                                 |
| Geometric mean          | (ref)                                                                  | 1.01x faster                                                         |

Benchmark hidden because not significant (7): async_tree_memoization_tg, async_tree_io, async_tree_memoization, async_tree_cpu_io_mixed_tg, asyncio_websockets, async_tree_none, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250326-linux-x86_64-brandtbucher-jit_up_12_11-3.14.0a6+-9ee2a07 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| nbody          | 89.4 ms                                                                | 87.9 ms: 1.02x faster                                                |
| float          | 64.9 ms                                                                | 65.4 ms: 1.01x slower                                                |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                         |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250326-linux-x86_64-brandtbucher-jit_up_12_11-3.14.0a6+-9ee2a07 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 128 ms                                                                 | 128 ms: 1.00x slower                                                 |
| regex_v8       | 23.5 ms                                                                | 23.9 ms: 1.02x slower                                                |
| regex_dna      | 217 ms                                                                 | 226 ms: 1.05x slower                                                 |
| regex_effbot   | 3.16 ms                                                                | 3.48 ms: 1.10x slower                                                |
| Geometric mean | (ref)                                                                  | 1.04x slower                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250326-linux-x86_64-brandtbucher-jit_up_12_11-3.14.0a6+-9ee2a07 |
|----------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| pickle_pure_python   | 325 us                                                                 | 321 us: 1.01x faster                                                 |
| unpickle_pure_python | 214 us                                                                 | 212 us: 1.01x faster                                                 |
| xml_etree_parse      | 140 ms                                                                 | 139 ms: 1.01x faster                                                 |
| xml_etree_iterparse  | 97.6 ms                                                                | 97.2 ms: 1.00x faster                                                |
| tomli_loads          | 1.87 sec                                                               | 1.88 sec: 1.01x slower                                               |
| Geometric mean       | (ref)                                                                  | 1.00x faster                                                         |

Benchmark hidden because not significant (4): json_loads, xml_etree_generate, xml_etree_process, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250326-linux-x86_64-brandtbucher-jit_up_12_11-3.14.0a6+-9ee2a07 |
|------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 13.1 ms                                                                | 13.1 ms: 1.00x faster                                                |
| python_startup_no_site | 8.19 ms                                                                | 8.18 ms: 1.00x faster                                                |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250326-linux-x86_64-brandtbucher-jit_up_12_11-3.14.0a6+-9ee2a07 |
|-----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| genshi_text     | 21.4 ms                                                                | 21.3 ms: 1.01x faster                                                |
| mako            | 11.0 ms                                                                | 11.0 ms: 1.01x faster                                                |
| genshi_xml      | 49.8 ms                                                                | 50.4 ms: 1.01x slower                                                |
| django_template | 32.0 ms                                                                | 32.4 ms: 1.01x slower                                                |
| Geometric mean  | (ref)                                                                  | 1.00x slower                                                         |

All benchmarks:
===============

| Benchmark               | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250326-linux-x86_64-brandtbucher-jit_up_12_11-3.14.0a6+-9ee2a07 |
|-------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| gc_traversal            | 5.05 ms                                                                | 4.80 ms: 1.05x faster                                                |
| spectral_norm           | 97.1 ms                                                                | 93.0 ms: 1.04x faster                                                |
| coroutines              | 24.1 ms                                                                | 23.3 ms: 1.03x faster                                                |
| telco                   | 7.93 ms                                                                | 7.77 ms: 1.02x faster                                                |
| nbody                   | 89.4 ms                                                                | 87.9 ms: 1.02x faster                                                |
| scimark_monte_carlo     | 68.6 ms                                                                | 67.6 ms: 1.02x faster                                                |
| html5lib                | 63.2 ms                                                                | 62.3 ms: 1.02x faster                                                |
| pickle_pure_python      | 325 us                                                                 | 321 us: 1.01x faster                                                 |
| richards_super          | 41.1 ms                                                                | 40.6 ms: 1.01x faster                                                |
| generators              | 29.2 ms                                                                | 28.9 ms: 1.01x faster                                                |
| fannkuch                | 423 ms                                                                 | 419 ms: 1.01x faster                                                 |
| async_tree_none_tg      | 255 ms                                                                 | 253 ms: 1.01x faster                                                 |
| unpickle_pure_python    | 214 us                                                                 | 212 us: 1.01x faster                                                 |
| nqueens                 | 84.9 ms                                                                | 84.1 ms: 1.01x faster                                                |
| bench_mp_pool           | 83.3 ms                                                                | 82.7 ms: 1.01x faster                                                |
| logging_simple          | 5.59 us                                                                | 5.54 us: 1.01x faster                                                |
| chaos                   | 60.3 ms                                                                | 59.9 ms: 1.01x faster                                                |
| genshi_text             | 21.4 ms                                                                | 21.3 ms: 1.01x faster                                                |
| async_generators        | 418 ms                                                                 | 415 ms: 1.01x faster                                                 |
| xml_etree_parse         | 140 ms                                                                 | 139 ms: 1.01x faster                                                 |
| shortest_path           | 494 ms                                                                 | 491 ms: 1.01x faster                                                 |
| create_gc_cycles        | 2.48 ms                                                                | 2.47 ms: 1.01x faster                                                |
| mako                    | 11.0 ms                                                                | 11.0 ms: 1.01x faster                                                |
| deltablue               | 3.06 ms                                                                | 3.05 ms: 1.00x faster                                                |
| xml_etree_iterparse     | 97.6 ms                                                                | 97.2 ms: 1.00x faster                                                |
| python_startup          | 13.1 ms                                                                | 13.1 ms: 1.00x faster                                                |
| python_startup_no_site  | 8.19 ms                                                                | 8.18 ms: 1.00x faster                                                |
| deepcopy_memo           | 29.0 us                                                                | 29.0 us: 1.00x slower                                                |
| sympy_integrate         | 20.0 ms                                                                | 20.1 ms: 1.00x slower                                                |
| sqlglot_v2_parse        | 1.29 ms                                                                | 1.29 ms: 1.00x slower                                                |
| bpe_tokeniser           | 4.57 sec                                                               | 4.59 sec: 1.00x slower                                               |
| async_tree_cpu_io_mixed | 492 ms                                                                 | 494 ms: 1.00x slower                                                 |
| regex_compile           | 128 ms                                                                 | 128 ms: 1.00x slower                                                 |
| sqlalchemy_declarative  | 133 ms                                                                 | 133 ms: 1.00x slower                                                 |
| 2to3                    | 263 ms                                                                 | 264 ms: 1.01x slower                                                 |
| sympy_str               | 274 ms                                                                 | 276 ms: 1.01x slower                                                 |
| hexiom                  | 6.86 ms                                                                | 6.90 ms: 1.01x slower                                                |
| float                   | 64.9 ms                                                                | 65.4 ms: 1.01x slower                                                |
| tomli_loads             | 1.87 sec                                                               | 1.88 sec: 1.01x slower                                               |
| sqlglot_v2_optimize     | 54.1 ms                                                                | 54.5 ms: 1.01x slower                                                |
| sqlalchemy_imperative   | 17.1 ms                                                                | 17.2 ms: 1.01x slower                                                |
| logging_format          | 6.16 us                                                                | 6.22 us: 1.01x slower                                                |
| sqlglot_v2_normalize    | 107 ms                                                                 | 109 ms: 1.01x slower                                                 |
| thrift                  | 783 us                                                                 | 792 us: 1.01x slower                                                 |
| scimark_sor             | 119 ms                                                                 | 120 ms: 1.01x slower                                                 |
| genshi_xml              | 49.8 ms                                                                | 50.4 ms: 1.01x slower                                                |
| django_template         | 32.0 ms                                                                | 32.4 ms: 1.01x slower                                                |
| meteor_contest          | 108 ms                                                                 | 110 ms: 1.01x slower                                                 |
| mdp                     | 2.48 sec                                                               | 2.51 sec: 1.01x slower                                               |
| pprint_pformat          | 1.55 sec                                                               | 1.57 sec: 1.02x slower                                               |
| regex_v8                | 23.5 ms                                                                | 23.9 ms: 1.02x slower                                                |
| pyflate                 | 432 ms                                                                 | 443 ms: 1.03x slower                                                 |
| pprint_safe_repr        | 756 ms                                                                 | 777 ms: 1.03x slower                                                 |
| logging_silent          | 95.7 ns                                                                | 98.4 ns: 1.03x slower                                                |
| deepcopy_reduce         | 2.66 us                                                                | 2.75 us: 1.03x slower                                                |
| go                      | 128 ms                                                                 | 133 ms: 1.04x slower                                                 |
| regex_dna               | 217 ms                                                                 | 226 ms: 1.05x slower                                                 |
| pycparser               | 1.13 sec                                                               | 1.18 sec: 1.05x slower                                               |
| regex_effbot            | 3.16 ms                                                                | 3.48 ms: 1.10x slower                                                |
| Geometric mean          | (ref)                                                                  | 1.00x slower                                                         |

Benchmark hidden because not significant (37): async_tree_memoization_tg, async_tree_io, json_loads, async_tree_memoization, async_tree_cpu_io_mixed_tg, xml_etree_generate, raytrace, sqlite_synth, xml_etree_process, json_dumps, k_core, comprehensions, asyncio_websockets, scimark_lu, json, sympy_expand, many_optionals, pidigits, docutils, sqlglot_v2_transpile, bench_thread_pool, scimark_fft, connected_components, coverage, async_tree_none, pathlib, async_tree_io_tg, dulwich_log, pylint, deepcopy, crypto_pyaes, sympy_sum, subparsers, richards, scimark_sparse_mat_mult, sphinx, typing_runtime_protocols

- Geometric mean (including insignificant results): 1.002x slower

# HPT report

- Reliability score: 78.76% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x