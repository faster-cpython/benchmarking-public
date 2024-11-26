# Results vs. base

- fork: brandtbucher
- ref: jump_backoff
- machine: linux-aarch64
- commit hash: 5dd5806
- commit date: 2024-11-13
- overall geometric mean: 1.021x faster
- HPT reliability: 99.96%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.96x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241113-arminc-aarch64-python-c695e37a3f95c225ee08-3.14.0a1+-c695e37 | bm-20241113-arminc-aarch64-brandtbucher-jump_backoff-3.14.0a1+-5dd5806 |
|----------------|:------------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 398 ms                                                                   | 336 ms: 1.19x faster                                                   |
| docutils       | 3.79 sec                                                                 | 3.62 sec: 1.05x faster                                                 |
| sphinx         | 1.51 sec                                                                 | 1.45 sec: 1.04x faster                                                 |
| Geometric mean | (ref)                                                                    | 1.07x faster                                                           |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (11): coroutines, asyncio_websockets, async_tree_none, async_tree_cpu_io_mixed_tg, async_tree_none_tg, async_tree_cpu_io_mixed, async_tree_io_tg, async_generators, async_tree_memoization_tg, async_tree_io, async_tree_memoization

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): pidigits, float, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241113-arminc-aarch64-python-c695e37a3f95c225ee08-3.14.0a1+-c695e37 | bm-20241113-arminc-aarch64-brandtbucher-jump_backoff-3.14.0a1+-5dd5806 |
|----------------|:------------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 180 ms                                                                   | 162 ms: 1.11x faster                                                   |
| Geometric mean | (ref)                                                                    | 1.03x faster                                                           |

Benchmark hidden because not significant (3): regex_effbot, regex_v8, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241113-arminc-aarch64-python-c695e37a3f95c225ee08-3.14.0a1+-c695e37 | bm-20241113-arminc-aarch64-brandtbucher-jump_backoff-3.14.0a1+-5dd5806 |
|----------------------|:------------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| unpickle_pure_python | 270 us                                                                   | 257 us: 1.05x faster                                                   |
| Geometric mean       | (ref)                                                                    | 1.01x faster                                                           |

Benchmark hidden because not significant (8): json_dumps, xml_etree_generate, xml_etree_process, json_loads, xml_etree_parse, pickle_pure_python, tomli_loads, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

Benchmark hidden because not significant (4): django_template, genshi_xml, mako, genshi_text

All benchmarks:
===============

| Benchmark              | bm-20241113-arminc-aarch64-python-c695e37a3f95c225ee08-3.14.0a1+-c695e37 | bm-20241113-arminc-aarch64-brandtbucher-jump_backoff-3.14.0a1+-5dd5806 |
|------------------------|:------------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| sqlalchemy_declarative | 193 ms                                                                   | 155 ms: 1.25x faster                                                   |
| sympy_sum              | 212 ms                                                                   | 174 ms: 1.22x faster                                                   |
| pylint                 | 502 ms                                                                   | 419 ms: 1.20x faster                                                   |
| sympy_integrate        | 29.4 ms                                                                  | 24.8 ms: 1.19x faster                                                  |
| 2to3                   | 398 ms                                                                   | 336 ms: 1.19x faster                                                   |
| richards_super         | 73.8 ms                                                                  | 62.6 ms: 1.18x faster                                                  |
| sqlglot_optimize       | 84.7 ms                                                                  | 72.4 ms: 1.17x faster                                                  |
| richards               | 64.4 ms                                                                  | 56.8 ms: 1.13x faster                                                  |
| regex_compile          | 180 ms                                                                   | 162 ms: 1.11x faster                                                   |
| sqlglot_normalize      | 164 ms                                                                   | 149 ms: 1.10x faster                                                   |
| sqlglot_transpile      | 2.14 ms                                                                  | 2.00 ms: 1.07x faster                                                  |
| sqlglot_parse          | 1.71 ms                                                                  | 1.60 ms: 1.07x faster                                                  |
| sympy_str              | 356 ms                                                                   | 335 ms: 1.06x faster                                                   |
| unpickle_pure_python   | 270 us                                                                   | 257 us: 1.05x faster                                                   |
| pprint_pformat         | 2.66 sec                                                                 | 2.54 sec: 1.05x faster                                                 |
| docutils               | 3.79 sec                                                                 | 3.62 sec: 1.05x faster                                                 |
| sphinx                 | 1.51 sec                                                                 | 1.45 sec: 1.04x faster                                                 |
| create_gc_cycles       | 3.83 ms                                                                  | 3.68 ms: 1.04x faster                                                  |
| connected_components   | 567 ms                                                                   | 547 ms: 1.04x faster                                                   |
| pycparser              | 1.55 sec                                                                 | 1.51 sec: 1.03x faster                                                 |
| bpe_tokeniser          | 5.90 sec                                                                 | 5.94 sec: 1.01x slower                                                 |
| nqueens                | 123 ms                                                                   | 126 ms: 1.03x slower                                                   |
| fannkuch               | 502 ms                                                                   | 523 ms: 1.04x slower                                                   |
| pyflate                | 609 ms                                                                   | 661 ms: 1.09x slower                                                   |
| Geometric mean         | (ref)                                                                    | 1.03x faster                                                           |

Benchmark hidden because not significant (70): bench_mp_pool, sqlalchemy_imperative, django_template, scimark_lu, coroutines, deepcopy_reduce, chaos, regex_effbot, coverage, json_dumps, xml_etree_generate, generators, xml_etree_process, scimark_fft, genshi_xml, asyncio_websockets, mdp, pprint_safe_repr, bench_thread_pool, json_loads, shortest_path, mako, python_startup_no_site, typing_runtime_protocols, html5lib, dulwich_log, thrift, raytrace, hexiom, comprehensions, regex_v8, pidigits, xml_etree_parse, sympy_expand, async_tree_none, async_tree_cpu_io_mixed_tg, pathlib, pickle_pure_python, async_tree_none_tg, crypto_pyaes, sqlite_synth, async_tree_cpu_io_mixed, python_startup, async_tree_io_tg, gc_traversal, k_core, scimark_sparse_mat_mult, logging_silent, tomli_loads, deepcopy, deltablue, async_generators, telco, logging_format, async_tree_memoization_tg, genshi_text, scimark_monte_carlo, async_tree_io, async_tree_memoization, logging_simple, deepcopy_memo, float, json, spectral_norm, regex_dna, meteor_contest, xml_etree_iterparse, scimark_sor, go, nbody

- Geometric mean (including insignificant results): 1.021x faster
# HPT report

- Reliability score: 99.96% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.96x