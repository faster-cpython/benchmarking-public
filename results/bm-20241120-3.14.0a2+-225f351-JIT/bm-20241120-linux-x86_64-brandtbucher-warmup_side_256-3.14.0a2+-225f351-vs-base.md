# Results vs. base

- fork: brandtbucher
- ref: warmup_side_256
- machine: linux-x86_64
- commit hash: 225f351
- commit date: 2024-11-20
- overall geometric mean: 1.002x slower
- HPT reliability: 95.95%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241120-linux-x86_64-python-0af4ec30bd2e3a523503-3.14.0a2+-0af4ec3 | bm-20241120-linux-x86_64-brandtbucher-warmup_side_256-3.14.0a2+-225f351 |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 262 ms                                                                 | 262 ms: 1.00x slower                                                    |
| docutils       | 2.83 sec                                                               | 2.79 sec: 1.01x faster                                                  |
| html5lib       | 66.8 ms                                                                | 67.6 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                            |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20241120-linux-x86_64-python-0af4ec30bd2e3a523503-3.14.0a2+-0af4ec3 | bm-20241120-linux-x86_64-brandtbucher-warmup_side_256-3.14.0a2+-225f351 |
|------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| coroutines       | 23.4 ms                                                                | 23.1 ms: 1.01x faster                                                   |
| async_generators | 456 ms                                                                 | 453 ms: 1.01x faster                                                    |
| Geometric mean   | (ref)                                                                  | 1.00x slower                                                            |

Benchmark hidden because not significant (9): async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, asyncio_websockets, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, async_tree_none, async_tree_io, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241120-linux-x86_64-python-0af4ec30bd2e3a523503-3.14.0a2+-0af4ec3 | bm-20241120-linux-x86_64-brandtbucher-warmup_side_256-3.14.0a2+-225f351 |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pidigits       | 186 ms                                                                 | 187 ms: 1.00x slower                                                    |
| nbody          | 82.5 ms                                                                | 83.1 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                            |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241120-linux-x86_64-python-0af4ec30bd2e3a523503-3.14.0a2+-0af4ec3 | bm-20241120-linux-x86_64-brandtbucher-warmup_side_256-3.14.0a2+-225f351 |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 3.47 ms                                                                | 3.34 ms: 1.04x faster                                                   |
| regex_dna      | 223 ms                                                                 | 220 ms: 1.01x faster                                                    |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                            |

Benchmark hidden because not significant (2): regex_compile, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241120-linux-x86_64-python-0af4ec30bd2e3a523503-3.14.0a2+-0af4ec3 | bm-20241120-linux-x86_64-brandtbucher-warmup_side_256-3.14.0a2+-225f351 |
|----------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_generate   | 83.0 ms                                                                | 79.0 ms: 1.05x faster                                                   |
| xml_etree_process    | 57.5 ms                                                                | 55.5 ms: 1.04x faster                                                   |
| unpickle_pure_python | 193 us                                                                 | 194 us: 1.00x slower                                                    |
| json_loads           | 26.3 us                                                                | 26.4 us: 1.00x slower                                                   |
| xml_etree_iterparse  | 101 ms                                                                 | 102 ms: 1.01x slower                                                    |
| pickle_pure_python   | 319 us                                                                 | 321 us: 1.01x slower                                                    |
| Geometric mean       | (ref)                                                                  | 1.01x faster                                                            |

Benchmark hidden because not significant (3): json_dumps, tomli_loads, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241120-linux-x86_64-python-0af4ec30bd2e3a523503-3.14.0a2+-0af4ec3 | bm-20241120-linux-x86_64-brandtbucher-warmup_side_256-3.14.0a2+-225f351 |
|------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 12.8 ms                                                                | 12.9 ms: 1.00x slower                                                   |
| python_startup_no_site | 7.05 ms                                                                | 7.06 ms: 1.00x slower                                                   |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241120-linux-x86_64-python-0af4ec30bd2e3a523503-3.14.0a2+-0af4ec3 | bm-20241120-linux-x86_64-brandtbucher-warmup_side_256-3.14.0a2+-225f351 |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako           | 10.1 ms                                                                | 10.0 ms: 1.01x faster                                                   |
| genshi_text    | 25.0 ms                                                                | 25.5 ms: 1.02x slower                                                   |
| genshi_xml     | 57.1 ms                                                                | 59.1 ms: 1.03x slower                                                   |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                            |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark               | bm-20241120-linux-x86_64-python-0af4ec30bd2e3a523503-3.14.0a2+-0af4ec3 | bm-20241120-linux-x86_64-brandtbucher-warmup_side_256-3.14.0a2+-225f351 |
|-------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_generate      | 83.0 ms                                                                | 79.0 ms: 1.05x faster                                                   |
| regex_effbot            | 3.47 ms                                                                | 3.34 ms: 1.04x faster                                                   |
| xml_etree_process       | 57.5 ms                                                                | 55.5 ms: 1.04x faster                                                   |
| pylint                  | 284 ms                                                                 | 278 ms: 1.02x faster                                                    |
| logging_format          | 6.17 us                                                                | 6.07 us: 1.02x faster                                                   |
| scimark_monte_carlo     | 65.3 ms                                                                | 64.3 ms: 1.02x faster                                                   |
| regex_dna               | 223 ms                                                                 | 220 ms: 1.01x faster                                                    |
| coroutines              | 23.4 ms                                                                | 23.1 ms: 1.01x faster                                                   |
| docutils                | 2.83 sec                                                               | 2.79 sec: 1.01x faster                                                  |
| scimark_sparse_mat_mult | 4.67 ms                                                                | 4.62 ms: 1.01x faster                                                   |
| pathlib                 | 16.4 ms                                                                | 16.2 ms: 1.01x faster                                                   |
| shortest_path           | 485 ms                                                                 | 480 ms: 1.01x faster                                                    |
| logging_simple          | 5.55 us                                                                | 5.49 us: 1.01x faster                                                   |
| deepcopy_reduce         | 2.69 us                                                                | 2.66 us: 1.01x faster                                                   |
| connected_components    | 440 ms                                                                 | 435 ms: 1.01x faster                                                    |
| dulwich_log             | 68.0 ms                                                                | 67.5 ms: 1.01x faster                                                   |
| sympy_str               | 287 ms                                                                 | 285 ms: 1.01x faster                                                    |
| async_generators        | 456 ms                                                                 | 453 ms: 1.01x faster                                                    |
| pprint_pformat          | 1.46 sec                                                               | 1.45 sec: 1.01x faster                                                  |
| sqlalchemy_declarative  | 131 ms                                                                 | 130 ms: 1.01x faster                                                    |
| mako                    | 10.1 ms                                                                | 10.0 ms: 1.01x faster                                                   |
| pidigits                | 186 ms                                                                 | 187 ms: 1.00x slower                                                    |
| gc_traversal            | 4.35 ms                                                                | 4.36 ms: 1.00x slower                                                   |
| 2to3                    | 262 ms                                                                 | 262 ms: 1.00x slower                                                    |
| python_startup          | 12.8 ms                                                                | 12.9 ms: 1.00x slower                                                   |
| python_startup_no_site  | 7.05 ms                                                                | 7.06 ms: 1.00x slower                                                   |
| create_gc_cycles        | 2.64 ms                                                                | 2.65 ms: 1.00x slower                                                   |
| unpickle_pure_python    | 193 us                                                                 | 194 us: 1.00x slower                                                    |
| json_loads              | 26.3 us                                                                | 26.4 us: 1.00x slower                                                   |
| xml_etree_iterparse     | 101 ms                                                                 | 102 ms: 1.01x slower                                                    |
| pickle_pure_python      | 319 us                                                                 | 321 us: 1.01x slower                                                    |
| scimark_fft             | 317 ms                                                                 | 319 ms: 1.01x slower                                                    |
| sqlglot_optimize        | 55.5 ms                                                                | 55.9 ms: 1.01x slower                                                   |
| nbody                   | 82.5 ms                                                                | 83.1 ms: 1.01x slower                                                   |
| logging_silent          | 99.4 ns                                                                | 100 ns: 1.01x slower                                                    |
| subparsers              | 21.0 ms                                                                | 21.1 ms: 1.01x slower                                                   |
| thrift                  | 776 us                                                                 | 782 us: 1.01x slower                                                    |
| spectral_norm           | 112 ms                                                                 | 113 ms: 1.01x slower                                                    |
| go                      | 134 ms                                                                 | 135 ms: 1.01x slower                                                    |
| sqlalchemy_imperative   | 17.2 ms                                                                | 17.4 ms: 1.01x slower                                                   |
| crypto_pyaes            | 67.6 ms                                                                | 68.4 ms: 1.01x slower                                                   |
| html5lib                | 66.8 ms                                                                | 67.6 ms: 1.01x slower                                                   |
| sympy_expand            | 482 ms                                                                 | 488 ms: 1.01x slower                                                    |
| generators              | 35.2 ms                                                                | 35.8 ms: 1.01x slower                                                   |
| chaos                   | 58.9 ms                                                                | 59.8 ms: 1.02x slower                                                   |
| comprehensions          | 17.6 us                                                                | 17.9 us: 1.02x slower                                                   |
| fannkuch                | 389 ms                                                                 | 396 ms: 1.02x slower                                                    |
| genshi_text             | 25.0 ms                                                                | 25.5 ms: 1.02x slower                                                   |
| raytrace                | 280 ms                                                                 | 287 ms: 1.02x slower                                                    |
| genshi_xml              | 57.1 ms                                                                | 59.1 ms: 1.03x slower                                                   |
| mdp                     | 2.59 sec                                                               | 2.77 sec: 1.07x slower                                                  |
| richards                | 36.9 ms                                                                | 39.6 ms: 1.07x slower                                                   |
| richards_super          | 42.5 ms                                                                | 46.7 ms: 1.10x slower                                                   |
| Geometric mean          | (ref)                                                                  | 1.00x slower                                                            |

Benchmark hidden because not significant (44): json, async_tree_cpu_io_mixed_tg, nqueens, sphinx, pyflate, sqlglot_normalize, deepcopy, sympy_sum, telco, coverage, pprint_safe_repr, async_tree_cpu_io_mixed, regex_compile, json_dumps, many_optionals, djangocms, sympy_integrate, bench_thread_pool, sqlglot_transpile, meteor_contest, deltablue, bpe_tokeniser, typing_runtime_protocols, bench_mp_pool, hexiom, asyncio_websockets, sqlite_synth, tomli_loads, scimark_lu, k_core, sqlglot_parse, scimark_sor, regex_v8, xml_etree_parse, pycparser, async_tree_io_tg, django_template, async_tree_memoization_tg, float, async_tree_none_tg, deepcopy_memo, async_tree_none, async_tree_io, async_tree_memoization

- Geometric mean (including insignificant results): 1.002x slower
# HPT report

- Reliability score: 95.95% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x