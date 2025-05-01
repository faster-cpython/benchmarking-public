# Results vs. base

- fork: methane
- ref: optimize_json_encode
- machine: linux-x86_64
- commit hash: d026be3
- commit date: 2025-04-30
- overall geometric mean: 1.001x slower
- HPT reliability: 99.95%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250430-linux-x86_64-python-4e294f6feb3193854d23-3.14.0a7+-4e294f6 | bm-20250430-linux-x86_64-methane-optimize_json_encode-3.14.0a7+-d026be3 |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 253 ms                                                                 | 252 ms: 1.00x faster                                                    |
| docutils       | 2.60 sec                                                               | 2.62 sec: 1.01x slower                                                  |
| html5lib       | 61.2 ms                                                                | 62.2 ms: 1.02x slower                                                   |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                            |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20250430-linux-x86_64-python-4e294f6feb3193854d23-3.14.0a7+-4e294f6 | bm-20250430-linux-x86_64-methane-optimize_json_encode-3.14.0a7+-d026be3 |
|-------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_eager_io_tg  | 612 ms                                                                 | 616 ms: 1.01x slower                                                    |
| async_tree_cpu_io_mixed | 498 ms                                                                 | 503 ms: 1.01x slower                                                    |
| async_tree_io           | 593 ms                                                                 | 601 ms: 1.01x slower                                                    |
| async_tree_memoization  | 312 ms                                                                 | 316 ms: 1.01x slower                                                    |
| async_generators        | 394 ms                                                                 | 401 ms: 1.02x slower                                                    |
| async_tree_none         | 259 ms                                                                 | 266 ms: 1.02x slower                                                    |
| Geometric mean          | (ref)                                                                  | 1.01x slower                                                            |

Benchmark hidden because not significant (13): async_tree_eager_cpu_io_mixed, coroutines, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_eager_memoization_tg, async_tree_eager_cpu_io_mixed_tg, asyncio_websockets, async_tree_eager, async_tree_eager_memoization, async_tree_none_tg, async_tree_eager_tg, async_tree_eager_io, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250430-linux-x86_64-python-4e294f6feb3193854d23-3.14.0a7+-4e294f6 | bm-20250430-linux-x86_64-methane-optimize_json_encode-3.14.0a7+-d026be3 |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pidigits       | 192 ms                                                                 | 195 ms: 1.02x slower                                                    |
| float          | 68.3 ms                                                                | 69.5 ms: 1.02x slower                                                   |
| nbody          | 96.1 ms                                                                | 101 ms: 1.05x slower                                                    |
| Geometric mean | (ref)                                                                  | 1.03x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250430-linux-x86_64-python-4e294f6feb3193854d23-3.14.0a7+-4e294f6 | bm-20250430-linux-x86_64-methane-optimize_json_encode-3.14.0a7+-d026be3 |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 125 ms                                                                 | 126 ms: 1.01x slower                                                    |
| regex_effbot   | 3.18 ms                                                                | 3.25 ms: 1.02x slower                                                   |
| regex_dna      | 202 ms                                                                 | 209 ms: 1.03x slower                                                    |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                            |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250430-linux-x86_64-python-4e294f6feb3193854d23-3.14.0a7+-4e294f6 | bm-20250430-linux-x86_64-methane-optimize_json_encode-3.14.0a7+-d026be3 |
|----------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| json_dumps           | 11.7 ms                                                                | 10.2 ms: 1.15x faster                                                   |
| unpickle_pure_python | 219 us                                                                 | 216 us: 1.01x faster                                                    |
| json_loads           | 30.2 us                                                                | 30.0 us: 1.01x faster                                                   |
| xml_etree_process    | 60.5 ms                                                                | 60.8 ms: 1.00x slower                                                   |
| xml_etree_iterparse  | 99.0 ms                                                                | 100 ms: 1.01x slower                                                    |
| tomli_loads          | 1.95 sec                                                               | 1.98 sec: 1.02x slower                                                  |
| xml_etree_generate   | 86.2 ms                                                                | 87.6 ms: 1.02x slower                                                   |
| Geometric mean       | (ref)                                                                  | 1.01x faster                                                            |

Benchmark hidden because not significant (2): pickle_pure_python, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250430-linux-x86_64-python-4e294f6feb3193854d23-3.14.0a7+-4e294f6 | bm-20250430-linux-x86_64-methane-optimize_json_encode-3.14.0a7+-d026be3 |
|------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 6.92 ms                                                                | 6.87 ms: 1.01x faster                                                   |
| python_startup         | 13.1 ms                                                                | 13.0 ms: 1.01x faster                                                   |
| Geometric mean         | (ref)                                                                  | 1.01x faster                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250430-linux-x86_64-python-4e294f6feb3193854d23-3.14.0a7+-4e294f6 | bm-20250430-linux-x86_64-methane-optimize_json_encode-3.14.0a7+-d026be3 |
|-----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_text     | 21.3 ms                                                                | 20.9 ms: 1.02x faster                                                   |
| genshi_xml      | 49.7 ms                                                                | 48.9 ms: 1.02x faster                                                   |
| mako            | 11.6 ms                                                                | 11.7 ms: 1.01x slower                                                   |
| django_template | 31.7 ms                                                                | 32.3 ms: 1.02x slower                                                   |
| Geometric mean  | (ref)                                                                  | 1.00x faster                                                            |

All benchmarks:
===============

| Benchmark               | bm-20250430-linux-x86_64-python-4e294f6feb3193854d23-3.14.0a7+-4e294f6 | bm-20250430-linux-x86_64-methane-optimize_json_encode-3.14.0a7+-d026be3 |
|-------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| json_dumps              | 11.7 ms                                                                | 10.2 ms: 1.15x faster                                                   |
| gc_traversal            | 4.83 ms                                                                | 4.62 ms: 1.05x faster                                                   |
| genshi_text             | 21.3 ms                                                                | 20.9 ms: 1.02x faster                                                   |
| generators              | 30.1 ms                                                                | 29.6 ms: 1.02x faster                                                   |
| genshi_xml              | 49.7 ms                                                                | 48.9 ms: 1.02x faster                                                   |
| logging_silent          | 98.1 ns                                                                | 96.6 ns: 1.02x faster                                                   |
| pyflate                 | 447 ms                                                                 | 440 ms: 1.02x faster                                                    |
| logging_simple          | 5.63 us                                                                | 5.55 us: 1.01x faster                                                   |
| unpickle_pure_python    | 219 us                                                                 | 216 us: 1.01x faster                                                    |
| deepcopy_memo           | 28.8 us                                                                | 28.5 us: 1.01x faster                                                   |
| pathlib                 | 16.8 ms                                                                | 16.6 ms: 1.01x faster                                                   |
| connected_components    | 457 ms                                                                 | 452 ms: 1.01x faster                                                    |
| logging_format          | 6.25 us                                                                | 6.19 us: 1.01x faster                                                   |
| telco                   | 7.82 ms                                                                | 7.76 ms: 1.01x faster                                                   |
| richards                | 43.5 ms                                                                | 43.2 ms: 1.01x faster                                                   |
| bpe_tokeniser           | 4.49 sec                                                               | 4.45 sec: 1.01x faster                                                  |
| chaos                   | 57.1 ms                                                                | 56.6 ms: 1.01x faster                                                   |
| deepcopy                | 253 us                                                                 | 251 us: 1.01x faster                                                    |
| json_loads              | 30.2 us                                                                | 30.0 us: 1.01x faster                                                   |
| python_startup_no_site  | 6.92 ms                                                                | 6.87 ms: 1.01x faster                                                   |
| subparsers              | 21.2 ms                                                                | 21.1 ms: 1.01x faster                                                   |
| hexiom                  | 6.22 ms                                                                | 6.18 ms: 1.01x faster                                                   |
| go                      | 112 ms                                                                 | 112 ms: 1.01x faster                                                    |
| python_startup          | 13.1 ms                                                                | 13.0 ms: 1.01x faster                                                   |
| fannkuch                | 415 ms                                                                 | 413 ms: 1.01x faster                                                    |
| 2to3                    | 253 ms                                                                 | 252 ms: 1.00x faster                                                    |
| nqueens                 | 81.0 ms                                                                | 80.6 ms: 1.00x faster                                                   |
| create_gc_cycles        | 2.49 ms                                                                | 2.48 ms: 1.00x faster                                                   |
| many_optionals          | 931 us                                                                 | 933 us: 1.00x slower                                                    |
| sqlalchemy_imperative   | 17.0 ms                                                                | 17.0 ms: 1.00x slower                                                   |
| sqlglot_v2_transpile    | 1.53 ms                                                                | 1.54 ms: 1.00x slower                                                   |
| sqlalchemy_declarative  | 132 ms                                                                 | 132 ms: 1.00x slower                                                    |
| xml_etree_process       | 60.5 ms                                                                | 60.8 ms: 1.00x slower                                                   |
| bench_thread_pool       | 883 us                                                                 | 887 us: 1.00x slower                                                    |
| dulwich_log             | 59.2 ms                                                                | 59.5 ms: 1.00x slower                                                   |
| sympy_integrate         | 19.0 ms                                                                | 19.1 ms: 1.00x slower                                                   |
| sympy_sum               | 148 ms                                                                 | 148 ms: 1.00x slower                                                    |
| mdp                     | 1.22 sec                                                               | 1.23 sec: 1.00x slower                                                  |
| regex_compile           | 125 ms                                                                 | 126 ms: 1.01x slower                                                    |
| raytrace                | 262 ms                                                                 | 263 ms: 1.01x slower                                                    |
| sqlglot_v2_parse        | 1.22 ms                                                                | 1.23 ms: 1.01x slower                                                   |
| deepcopy_reduce         | 2.69 us                                                                | 2.71 us: 1.01x slower                                                   |
| sympy_str               | 266 ms                                                                 | 267 ms: 1.01x slower                                                    |
| docutils                | 2.60 sec                                                               | 2.62 sec: 1.01x slower                                                  |
| deltablue               | 3.34 ms                                                                | 3.36 ms: 1.01x slower                                                   |
| crypto_pyaes            | 72.3 ms                                                                | 72.8 ms: 1.01x slower                                                   |
| async_tree_eager_io_tg  | 612 ms                                                                 | 616 ms: 1.01x slower                                                    |
| json                    | 5.57 ms                                                                | 5.62 ms: 1.01x slower                                                   |
| mako                    | 11.6 ms                                                                | 11.7 ms: 1.01x slower                                                   |
| scimark_sor             | 118 ms                                                                 | 119 ms: 1.01x slower                                                    |
| scimark_fft             | 355 ms                                                                 | 358 ms: 1.01x slower                                                    |
| async_tree_cpu_io_mixed | 498 ms                                                                 | 503 ms: 1.01x slower                                                    |
| xml_etree_iterparse     | 99.0 ms                                                                | 100 ms: 1.01x slower                                                    |
| scimark_sparse_mat_mult | 4.88 ms                                                                | 4.94 ms: 1.01x slower                                                   |
| async_tree_io           | 593 ms                                                                 | 601 ms: 1.01x slower                                                    |
| async_tree_memoization  | 312 ms                                                                 | 316 ms: 1.01x slower                                                    |
| sqlite_synth            | 2.80 us                                                                | 2.84 us: 1.02x slower                                                   |
| pidigits                | 192 ms                                                                 | 195 ms: 1.02x slower                                                    |
| tomli_loads             | 1.95 sec                                                               | 1.98 sec: 1.02x slower                                                  |
| html5lib                | 61.2 ms                                                                | 62.2 ms: 1.02x slower                                                   |
| xml_etree_generate      | 86.2 ms                                                                | 87.6 ms: 1.02x slower                                                   |
| django_template         | 31.7 ms                                                                | 32.3 ms: 1.02x slower                                                   |
| float                   | 68.3 ms                                                                | 69.5 ms: 1.02x slower                                                   |
| async_generators        | 394 ms                                                                 | 401 ms: 1.02x slower                                                    |
| scimark_monte_carlo     | 66.4 ms                                                                | 67.7 ms: 1.02x slower                                                   |
| regex_effbot            | 3.18 ms                                                                | 3.25 ms: 1.02x slower                                                   |
| async_tree_none         | 259 ms                                                                 | 266 ms: 1.02x slower                                                    |
| regex_dna               | 202 ms                                                                 | 209 ms: 1.03x slower                                                    |
| spectral_norm           | 99.7 ms                                                                | 105 ms: 1.05x slower                                                    |
| nbody                   | 96.1 ms                                                                | 101 ms: 1.05x slower                                                    |
| Geometric mean          | (ref)                                                                  | 1.00x slower                                                            |

Benchmark hidden because not significant (33): k_core, async_tree_eager_cpu_io_mixed, pycparser, coroutines, regex_v8, bench_mp_pool, pickle_pure_python, meteor_contest, sqlglot_v2_optimize, coverage, richards_super, async_tree_memoization_tg, typing_runtime_protocols, shortest_path, comprehensions, pylint, sqlglot_v2_normalize, async_tree_cpu_io_mixed_tg, pprint_pformat, async_tree_eager_memoization_tg, async_tree_eager_cpu_io_mixed_tg, asyncio_websockets, async_tree_eager, pprint_safe_repr, scimark_lu, xml_etree_parse, sympy_expand, async_tree_eager_memoization, sphinx, async_tree_none_tg, async_tree_eager_tg, async_tree_eager_io, async_tree_io_tg

- Geometric mean (including insignificant results): 1.001x slower

# HPT report

- Reliability score: 99.95% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x