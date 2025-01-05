# Results vs. base

- fork: python
- ref: 0cafa97932c6574734bb
- machine: linux-aarch64
- commit hash: 0cafa97
- commit date: 2025-01-04
- overall geometric mean: 1.052x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250104-3.14.0a3+-0cafa97/bm-20250104-arminc-aarch64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97.json | results/bm-20250104-3.14.0a3+-0cafa97-JIT/bm-20250104-arminc-aarch64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 307 ms                                                                                                              | 321 ms: 1.04x slower                                                                                                    |
| docutils       | 3.03 sec                                                                                                            | 3.27 sec: 1.08x slower                                                                                                  |
| html5lib       | 63.8 ms                                                                                                             | 69.8 ms: 1.09x slower                                                                                                   |
| sphinx         | 1.20 sec                                                                                                            | 1.25 sec: 1.04x slower                                                                                                  |
| Geometric mean | (ref)                                                                                                               | 1.07x slower                                                                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | results/bm-20250104-3.14.0a3+-0cafa97/bm-20250104-arminc-aarch64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97.json | results/bm-20250104-3.14.0a3+-0cafa97-JIT/bm-20250104-arminc-aarch64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97.json |
|------------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| async_generators | 486 ms                                                                                                              | 528 ms: 1.09x slower                                                                                                    |
| Geometric mean   | (ref)                                                                                                               | 1.01x slower                                                                                                            |

Benchmark hidden because not significant (10): async_tree_io, async_tree_none_tg, async_tree_io_tg, asyncio_websockets, async_tree_cpu_io_mixed_tg, async_tree_memoization, async_tree_memoization_tg, coroutines, async_tree_cpu_io_mixed, async_tree_none

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): nbody, float, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250104-3.14.0a3+-0cafa97/bm-20250104-arminc-aarch64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97.json | results/bm-20250104-3.14.0a3+-0cafa97-JIT/bm-20250104-arminc-aarch64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| regex_compile  | 130 ms                                                                                                              | 142 ms: 1.09x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                               | 1.01x slower                                                                                                            |

Benchmark hidden because not significant (3): regex_dna, regex_effbot, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark          | results/bm-20250104-3.14.0a3+-0cafa97/bm-20250104-arminc-aarch64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97.json | results/bm-20250104-3.14.0a3+-0cafa97-JIT/bm-20250104-arminc-aarch64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97.json |
|--------------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| pickle_pure_python | 401 us                                                                                                              | 384 us: 1.04x faster                                                                                                    |
| tomli_loads        | 2.64 sec                                                                                                            | 2.54 sec: 1.04x faster                                                                                                  |
| Geometric mean     | (ref)                                                                                                               | 1.03x faster                                                                                                            |

Benchmark hidden because not significant (7): xml_etree_generate, xml_etree_iterparse, xml_etree_parse, xml_etree_process, unpickle_pure_python, json_loads, json_dumps

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20250104-3.14.0a3+-0cafa97/bm-20250104-arminc-aarch64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97.json | results/bm-20250104-3.14.0a3+-0cafa97-JIT/bm-20250104-arminc-aarch64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97.json |
|-----------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| django_template | 41.4 ms                                                                                                             | 48.5 ms: 1.17x slower                                                                                                   |
| genshi_text     | 29.4 ms                                                                                                             | 35.4 ms: 1.21x slower                                                                                                   |
| genshi_xml      | 63.7 ms                                                                                                             | 81.5 ms: 1.28x slower                                                                                                   |
| Geometric mean  | (ref)                                                                                                               | 1.15x slower                                                                                                            |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark             | results/bm-20250104-3.14.0a3+-0cafa97/bm-20250104-arminc-aarch64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97.json | results/bm-20250104-3.14.0a3+-0cafa97-JIT/bm-20250104-arminc-aarch64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97.json |
|-----------------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| bench_mp_pool         | 4.34 sec                                                                                                            | 1.42 sec: 3.05x faster                                                                                                  |
| deepcopy_memo         | 41.1 us                                                                                                             | 38.4 us: 1.07x faster                                                                                                   |
| pickle_pure_python    | 401 us                                                                                                              | 384 us: 1.04x faster                                                                                                    |
| tomli_loads           | 2.64 sec                                                                                                            | 2.54 sec: 1.04x faster                                                                                                  |
| bpe_tokeniser         | 5.77 sec                                                                                                            | 5.83 sec: 1.01x slower                                                                                                  |
| bench_thread_pool     | 1.32 ms                                                                                                             | 1.36 ms: 1.03x slower                                                                                                   |
| 2to3                  | 307 ms                                                                                                              | 321 ms: 1.04x slower                                                                                                    |
| sphinx                | 1.20 sec                                                                                                            | 1.25 sec: 1.04x slower                                                                                                  |
| mdp                   | 3.45 sec                                                                                                            | 3.61 sec: 1.05x slower                                                                                                  |
| pathlib               | 21.7 ms                                                                                                             | 22.8 ms: 1.05x slower                                                                                                   |
| logging_silent        | 140 ns                                                                                                              | 147 ns: 1.05x slower                                                                                                    |
| sqlglot_transpile     | 1.80 ms                                                                                                             | 1.91 ms: 1.06x slower                                                                                                   |
| sympy_integrate       | 21.6 ms                                                                                                             | 23.2 ms: 1.07x slower                                                                                                   |
| meteor_contest        | 116 ms                                                                                                              | 125 ms: 1.07x slower                                                                                                    |
| docutils              | 3.03 sec                                                                                                            | 3.27 sec: 1.08x slower                                                                                                  |
| mypy2                 | 1.03 sec                                                                                                            | 1.11 sec: 1.08x slower                                                                                                  |
| sqlglot_normalize     | 134 ms                                                                                                              | 145 ms: 1.08x slower                                                                                                    |
| spectral_norm         | 132 ms                                                                                                              | 143 ms: 1.08x slower                                                                                                    |
| subparsers            | 25.6 ms                                                                                                             | 27.8 ms: 1.09x slower                                                                                                   |
| async_generators      | 486 ms                                                                                                              | 528 ms: 1.09x slower                                                                                                    |
| coverage              | 101 ms                                                                                                              | 111 ms: 1.09x slower                                                                                                    |
| scimark_lu            | 139 ms                                                                                                              | 152 ms: 1.09x slower                                                                                                    |
| regex_compile         | 130 ms                                                                                                              | 142 ms: 1.09x slower                                                                                                    |
| html5lib              | 63.8 ms                                                                                                             | 69.8 ms: 1.09x slower                                                                                                   |
| sympy_sum             | 148 ms                                                                                                              | 163 ms: 1.10x slower                                                                                                    |
| deepcopy_reduce       | 3.60 us                                                                                                             | 3.95 us: 1.10x slower                                                                                                   |
| sympy_expand          | 473 ms                                                                                                              | 519 ms: 1.10x slower                                                                                                    |
| crypto_pyaes          | 84.8 ms                                                                                                             | 93.4 ms: 1.10x slower                                                                                                   |
| sqlalchemy_imperative | 15.3 ms                                                                                                             | 17.2 ms: 1.12x slower                                                                                                   |
| sympy_str             | 275 ms                                                                                                              | 308 ms: 1.12x slower                                                                                                    |
| deltablue             | 4.01 ms                                                                                                             | 4.52 ms: 1.13x slower                                                                                                   |
| dulwich_log           | 62.0 ms                                                                                                             | 69.9 ms: 1.13x slower                                                                                                   |
| logging_simple        | 7.23 us                                                                                                             | 8.19 us: 1.13x slower                                                                                                   |
| logging_format        | 7.87 us                                                                                                             | 9.00 us: 1.14x slower                                                                                                   |
| pylint                | 306 ms                                                                                                              | 353 ms: 1.15x slower                                                                                                    |
| chaos                 | 74.2 ms                                                                                                             | 85.6 ms: 1.15x slower                                                                                                   |
| pycparser             | 1.29 sec                                                                                                            | 1.49 sec: 1.16x slower                                                                                                  |
| go                    | 150 ms                                                                                                              | 174 ms: 1.16x slower                                                                                                    |
| comprehensions        | 21.9 us                                                                                                             | 25.5 us: 1.16x slower                                                                                                   |
| raytrace              | 324 ms                                                                                                              | 378 ms: 1.16x slower                                                                                                    |
| django_template       | 41.4 ms                                                                                                             | 48.5 ms: 1.17x slower                                                                                                   |
| deepcopy              | 342 us                                                                                                              | 401 us: 1.17x slower                                                                                                    |
| genshi_text           | 29.4 ms                                                                                                             | 35.4 ms: 1.21x slower                                                                                                   |
| many_optionals        | 708 us                                                                                                              | 859 us: 1.21x slower                                                                                                    |
| nqueens               | 105 ms                                                                                                              | 131 ms: 1.25x slower                                                                                                    |
| genshi_xml            | 63.7 ms                                                                                                             | 81.5 ms: 1.28x slower                                                                                                   |
| pprint_safe_repr      | 966 ms                                                                                                              | 1.25 sec: 1.29x slower                                                                                                  |
| pprint_pformat        | 1.96 sec                                                                                                            | 2.58 sec: 1.31x slower                                                                                                  |
| hexiom                | 7.39 ms                                                                                                             | 9.81 ms: 1.33x slower                                                                                                   |
| generators            | 36.9 ms                                                                                                             | 51.0 ms: 1.38x slower                                                                                                   |
| Geometric mean        | (ref)                                                                                                               | 1.05x slower                                                                                                            |

Benchmark hidden because not significant (48): xml_etree_generate, nbody, regex_dna, mako, xml_etree_iterparse, float, xml_etree_parse, xml_etree_process, unpickle_pure_python, scimark_sor, async_tree_io, regex_effbot, json_loads, regex_v8, async_tree_none_tg, scimark_fft, python_startup_no_site, async_tree_io_tg, connected_components, asyncio_websockets, k_core, pyflate, json_dumps, async_tree_cpu_io_mixed_tg, async_tree_memoization, async_tree_memoization_tg, gc_traversal, shortest_path, djangocms, coroutines, python_startup, scimark_monte_carlo, async_tree_cpu_io_mixed, pidigits, async_tree_none, sqlglot_parse, thrift, create_gc_cycles, sqlite_synth, richards_super, json, telco, fannkuch, sqlalchemy_declarative, scimark_sparse_mat_mult, richards, sqlglot_optimize, typing_runtime_protocols

- Geometric mean (including insignificant results): 1.052x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 1.02x