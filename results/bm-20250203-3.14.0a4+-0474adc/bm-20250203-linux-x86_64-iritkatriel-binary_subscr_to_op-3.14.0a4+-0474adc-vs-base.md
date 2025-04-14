# Results vs. base

- fork: iritkatriel
- ref: binary_subscr_to_op
- machine: linux-x86_64
- commit hash: 0474adc
- commit date: 2025-02-03
- overall geometric mean: 1.007x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250130-linux-x86_64-python-5ab9604683a58e613c6e-3.14.0a4+-5ab9604 | bm-20250203-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-0474adc |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 253 ms                                                                 | 252 ms: 1.00x faster                                                       |
| docutils       | 2.59 sec                                                               | 2.57 sec: 1.01x faster                                                     |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                               |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20250130-linux-x86_64-python-5ab9604683a58e613c6e-3.14.0a4+-5ab9604 | bm-20250203-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-0474adc |
|------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_generators | 389 ms                                                                 | 382 ms: 1.02x faster                                                       |
| coroutines       | 23.4 ms                                                                | 23.6 ms: 1.01x slower                                                      |
| Geometric mean   | (ref)                                                                  | 1.00x faster                                                               |

Benchmark hidden because not significant (9): async_tree_cpu_io_mixed, async_tree_memoization, async_tree_io, async_tree_io_tg, asyncio_websockets, async_tree_cpu_io_mixed_tg, async_tree_none, async_tree_none_tg, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250130-linux-x86_64-python-5ab9604683a58e613c6e-3.14.0a4+-5ab9604 | bm-20250203-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-0474adc |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 99.4 ms                                                                | 93.7 ms: 1.06x faster                                                      |
| float          | 72.6 ms                                                                | 70.1 ms: 1.03x faster                                                      |
| pidigits       | 186 ms                                                                 | 187 ms: 1.00x slower                                                       |
| Geometric mean | (ref)                                                                  | 1.03x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250130-linux-x86_64-python-5ab9604683a58e613c6e-3.14.0a4+-5ab9604 | bm-20250203-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-0474adc |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 3.35 ms                                                                | 3.27 ms: 1.03x faster                                                      |
| regex_v8       | 25.5 ms                                                                | 24.9 ms: 1.02x faster                                                      |
| regex_dna      | 212 ms                                                                 | 209 ms: 1.01x faster                                                       |
| regex_compile  | 126 ms                                                                 | 125 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                                  | 1.02x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250130-linux-x86_64-python-5ab9604683a58e613c6e-3.14.0a4+-5ab9604 | bm-20250203-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-0474adc |
|----------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 11.8 ms                                                                | 11.6 ms: 1.02x faster                                                      |
| xml_etree_process    | 59.9 ms                                                                | 58.7 ms: 1.02x faster                                                      |
| tomli_loads          | 1.95 sec                                                               | 1.92 sec: 1.02x faster                                                     |
| pickle_pure_python   | 324 us                                                                 | 318 us: 1.02x faster                                                       |
| xml_etree_generate   | 84.9 ms                                                                | 83.5 ms: 1.02x faster                                                      |
| unpickle_pure_python | 220 us                                                                 | 217 us: 1.01x faster                                                       |
| json_loads           | 28.7 us                                                                | 28.9 us: 1.01x slower                                                      |
| xml_etree_parse      | 138 ms                                                                 | 140 ms: 1.01x slower                                                       |
| Geometric mean       | (ref)                                                                  | 1.01x faster                                                               |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250130-linux-x86_64-python-5ab9604683a58e613c6e-3.14.0a4+-5ab9604 | bm-20250203-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-0474adc |
|------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 7.02 ms                                                                | 7.06 ms: 1.01x slower                                                      |
| python_startup         | 12.8 ms                                                                | 12.9 ms: 1.01x slower                                                      |
| Geometric mean         | (ref)                                                                  | 1.01x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250130-linux-x86_64-python-5ab9604683a58e613c6e-3.14.0a4+-5ab9604 | bm-20250203-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-0474adc |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako           | 11.3 ms                                                                | 10.9 ms: 1.03x faster                                                      |
| genshi_text    | 21.7 ms                                                                | 21.3 ms: 1.02x faster                                                      |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                               |

Benchmark hidden because not significant (2): django_template, genshi_xml

All benchmarks:
===============

| Benchmark               | bm-20250130-linux-x86_64-python-5ab9604683a58e613c6e-3.14.0a4+-5ab9604 | bm-20250203-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-0474adc |
|-------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody                   | 99.4 ms                                                                | 93.7 ms: 1.06x faster                                                      |
| deepcopy_memo           | 31.7 us                                                                | 30.1 us: 1.05x faster                                                      |
| logging_silent          | 112 ns                                                                 | 107 ns: 1.05x faster                                                       |
| scimark_sparse_mat_mult | 4.80 ms                                                                | 4.59 ms: 1.05x faster                                                      |
| float                   | 72.6 ms                                                                | 70.1 ms: 1.03x faster                                                      |
| scimark_fft             | 351 ms                                                                 | 340 ms: 1.03x faster                                                       |
| spectral_norm           | 97.6 ms                                                                | 94.6 ms: 1.03x faster                                                      |
| deepcopy_reduce         | 2.76 us                                                                | 2.68 us: 1.03x faster                                                      |
| mako                    | 11.3 ms                                                                | 10.9 ms: 1.03x faster                                                      |
| pprint_safe_repr        | 738 ms                                                                 | 719 ms: 1.03x faster                                                       |
| regex_effbot            | 3.35 ms                                                                | 3.27 ms: 1.03x faster                                                      |
| deepcopy                | 259 us                                                                 | 253 us: 1.02x faster                                                       |
| comprehensions          | 16.7 us                                                                | 16.3 us: 1.02x faster                                                      |
| regex_v8                | 25.5 ms                                                                | 24.9 ms: 1.02x faster                                                      |
| json_dumps              | 11.8 ms                                                                | 11.6 ms: 1.02x faster                                                      |
| chaos                   | 59.6 ms                                                                | 58.3 ms: 1.02x faster                                                      |
| xml_etree_process       | 59.9 ms                                                                | 58.7 ms: 1.02x faster                                                      |
| raytrace                | 278 ms                                                                 | 272 ms: 1.02x faster                                                       |
| richards                | 45.2 ms                                                                | 44.4 ms: 1.02x faster                                                      |
| tomli_loads             | 1.95 sec                                                               | 1.92 sec: 1.02x faster                                                     |
| async_generators        | 389 ms                                                                 | 382 ms: 1.02x faster                                                       |
| k_core                  | 2.28 sec                                                               | 2.24 sec: 1.02x faster                                                     |
| genshi_text             | 21.7 ms                                                                | 21.3 ms: 1.02x faster                                                      |
| pickle_pure_python      | 324 us                                                                 | 318 us: 1.02x faster                                                       |
| xml_etree_generate      | 84.9 ms                                                                | 83.5 ms: 1.02x faster                                                      |
| richards_super          | 51.4 ms                                                                | 50.6 ms: 1.02x faster                                                      |
| sqlglot_parse           | 1.28 ms                                                                | 1.26 ms: 1.02x faster                                                      |
| pprint_pformat          | 1.50 sec                                                               | 1.48 sec: 1.02x faster                                                     |
| unpickle_pure_python    | 220 us                                                                 | 217 us: 1.01x faster                                                       |
| coverage                | 91.2 ms                                                                | 89.9 ms: 1.01x faster                                                      |
| subparsers              | 20.7 ms                                                                | 20.4 ms: 1.01x faster                                                      |
| go                      | 119 ms                                                                 | 118 ms: 1.01x faster                                                       |
| scimark_lu              | 117 ms                                                                 | 115 ms: 1.01x faster                                                       |
| regex_dna               | 212 ms                                                                 | 209 ms: 1.01x faster                                                       |
| sqlglot_transpile       | 1.59 ms                                                                | 1.57 ms: 1.01x faster                                                      |
| bpe_tokeniser           | 4.43 sec                                                               | 4.38 sec: 1.01x faster                                                     |
| logging_simple          | 5.54 us                                                                | 5.47 us: 1.01x faster                                                      |
| sqlglot_normalize       | 104 ms                                                                 | 103 ms: 1.01x faster                                                       |
| shortest_path           | 475 ms                                                                 | 471 ms: 1.01x faster                                                       |
| regex_compile           | 126 ms                                                                 | 125 ms: 1.01x faster                                                       |
| sqlglot_optimize        | 52.1 ms                                                                | 51.7 ms: 1.01x faster                                                      |
| sympy_integrate         | 19.7 ms                                                                | 19.6 ms: 1.01x faster                                                      |
| docutils                | 2.59 sec                                                               | 2.57 sec: 1.01x faster                                                     |
| hexiom                  | 6.28 ms                                                                | 6.24 ms: 1.01x faster                                                      |
| crypto_pyaes            | 70.4 ms                                                                | 70.0 ms: 1.01x faster                                                      |
| mdp                     | 2.46 sec                                                               | 2.45 sec: 1.01x faster                                                     |
| scimark_sor             | 122 ms                                                                 | 122 ms: 1.01x faster                                                       |
| sqlalchemy_declarative  | 128 ms                                                                 | 128 ms: 1.00x faster                                                       |
| 2to3                    | 253 ms                                                                 | 252 ms: 1.00x faster                                                       |
| pidigits                | 186 ms                                                                 | 187 ms: 1.00x slower                                                       |
| create_gc_cycles        | 2.47 ms                                                                | 2.48 ms: 1.00x slower                                                      |
| python_startup_no_site  | 7.02 ms                                                                | 7.06 ms: 1.01x slower                                                      |
| json_loads              | 28.7 us                                                                | 28.9 us: 1.01x slower                                                      |
| coroutines              | 23.4 ms                                                                | 23.6 ms: 1.01x slower                                                      |
| deltablue               | 3.26 ms                                                                | 3.28 ms: 1.01x slower                                                      |
| bench_mp_pool           | 80.5 ms                                                                | 81.0 ms: 1.01x slower                                                      |
| json                    | 5.11 ms                                                                | 5.15 ms: 1.01x slower                                                      |
| python_startup          | 12.8 ms                                                                | 12.9 ms: 1.01x slower                                                      |
| scimark_monte_carlo     | 67.7 ms                                                                | 68.3 ms: 1.01x slower                                                      |
| xml_etree_parse         | 138 ms                                                                 | 140 ms: 1.01x slower                                                       |
| generators              | 27.6 ms                                                                | 27.9 ms: 1.01x slower                                                      |
| meteor_contest          | 105 ms                                                                 | 106 ms: 1.01x slower                                                       |
| nqueens                 | 79.0 ms                                                                | 79.9 ms: 1.01x slower                                                      |
| pathlib                 | 15.6 ms                                                                | 15.7 ms: 1.01x slower                                                      |
| fannkuch                | 401 ms                                                                 | 408 ms: 1.02x slower                                                       |
| gc_traversal            | 4.89 ms                                                                | 5.03 ms: 1.03x slower                                                      |
| pyflate                 | 437 ms                                                                 | 467 ms: 1.07x slower                                                       |
| Geometric mean          | (ref)                                                                  | 1.01x faster                                                               |

Benchmark hidden because not significant (29): connected_components, pylint, async_tree_cpu_io_mixed, logging_format, typing_runtime_protocols, sympy_expand, async_tree_memoization, telco, pycparser, django_template, async_tree_io, dulwich_log, html5lib, genshi_xml, sympy_str, async_tree_io_tg, xml_etree_iterparse, bench_thread_pool, sphinx, asyncio_websockets, thrift, async_tree_cpu_io_mixed_tg, sqlalchemy_imperative, many_optionals, sympy_sum, async_tree_none, async_tree_none_tg, async_tree_memoization_tg, sqlite_synth

- Geometric mean (including insignificant results): 1.007x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x