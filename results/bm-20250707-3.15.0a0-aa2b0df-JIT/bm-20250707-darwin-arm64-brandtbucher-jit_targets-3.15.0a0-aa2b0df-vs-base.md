# Results vs. base

- fork: brandtbucher
- ref: jit_targets
- machine: darwin-arm64
- commit hash: aa2b0df
- commit date: 2025-07-07
- overall geometric mean: 1.000x slower
- HPT reliability: 89.49%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.98x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250707-darwin-arm64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 | bm-20250707-darwin-arm64-brandtbucher-jit_targets-3.15.0a0-aa2b0df |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| docutils       | 1.47 sec                                                              | 1.47 sec: 1.00x slower                                             |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                       |

Benchmark hidden because not significant (3): 2to3, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20250707-darwin-arm64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 | bm-20250707-darwin-arm64-brandtbucher-jit_targets-3.15.0a0-aa2b0df |
|------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| coroutines       | 17.2 ms                                                               | 17.1 ms: 1.00x faster                                              |
| async_generators | 277 ms                                                                | 280 ms: 1.01x slower                                               |
| Geometric mean   | (ref)                                                                 | 1.00x slower                                                       |

Benchmark hidden because not significant (17): async_tree_memoization, asyncio_websockets, async_tree_eager_cpu_io_mixed, async_tree_none, async_tree_eager_cpu_io_mixed_tg, async_tree_eager, async_tree_cpu_io_mixed_tg, async_tree_none_tg, async_tree_memoization_tg, async_tree_cpu_io_mixed, async_tree_eager_memoization_tg, async_tree_eager_memoization, async_tree_eager_tg, async_tree_eager_io_tg, async_tree_eager_io, async_tree_io_tg, async_tree_io

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): nbody, pidigits, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250707-darwin-arm64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 | bm-20250707-darwin-arm64-brandtbucher-jit_targets-3.15.0a0-aa2b0df |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_effbot   | 2.40 ms                                                               | 2.34 ms: 1.03x faster                                              |
| regex_v8       | 16.2 ms                                                               | 16.0 ms: 1.01x faster                                              |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                       |

Benchmark hidden because not significant (2): regex_dna, regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20250707-darwin-arm64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 | bm-20250707-darwin-arm64-brandtbucher-jit_targets-3.15.0a0-aa2b0df |
|--------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| xml_etree_generate | 50.7 ms                                                               | 50.3 ms: 1.01x faster                                              |
| xml_etree_process  | 35.9 ms                                                               | 35.7 ms: 1.01x faster                                              |
| tomli_loads        | 1.25 sec                                                              | 1.24 sec: 1.01x faster                                             |
| pickle_pure_python | 210 us                                                                | 209 us: 1.00x faster                                               |
| json_loads         | 16.5 us                                                               | 16.4 us: 1.00x faster                                              |
| json_dumps         | 6.59 ms                                                               | 6.63 ms: 1.01x slower                                              |
| xml_etree_parse    | 98.8 ms                                                               | 101 ms: 1.02x slower                                               |
| Geometric mean     | (ref)                                                                 | 1.00x slower                                                       |

Benchmark hidden because not significant (2): xml_etree_iterparse, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250707-darwin-arm64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 | bm-20250707-darwin-arm64-brandtbucher-jit_targets-3.15.0a0-aa2b0df |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup_no_site | 14.4 ms                                                               | 14.3 ms: 1.01x faster                                              |
| python_startup         | 18.9 ms                                                               | 18.8 ms: 1.01x faster                                              |
| Geometric mean         | (ref)                                                                 | 1.01x faster                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250707-darwin-arm64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 | bm-20250707-darwin-arm64-brandtbucher-jit_targets-3.15.0a0-aa2b0df |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| genshi_xml     | 31.3 ms                                                               | 31.6 ms: 1.01x slower                                              |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                       |

Benchmark hidden because not significant (3): django_template, genshi_text, mako

All benchmarks:
===============

| Benchmark                | bm-20250707-darwin-arm64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 | bm-20250707-darwin-arm64-brandtbucher-jit_targets-3.15.0a0-aa2b0df |
|--------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_effbot             | 2.40 ms                                                               | 2.34 ms: 1.03x faster                                              |
| python_startup_no_site   | 14.4 ms                                                               | 14.3 ms: 1.01x faster                                              |
| typing_runtime_protocols | 98.2 us                                                               | 97.3 us: 1.01x faster                                              |
| regex_v8                 | 16.2 ms                                                               | 16.0 ms: 1.01x faster                                              |
| scimark_lu               | 82.7 ms                                                               | 82.1 ms: 1.01x faster                                              |
| xml_etree_generate       | 50.7 ms                                                               | 50.3 ms: 1.01x faster                                              |
| xml_etree_process        | 35.9 ms                                                               | 35.7 ms: 1.01x faster                                              |
| deepcopy                 | 157 us                                                                | 156 us: 1.01x faster                                               |
| tomli_loads              | 1.25 sec                                                              | 1.24 sec: 1.01x faster                                             |
| sqlglot_v2_optimize      | 34.2 ms                                                               | 34.1 ms: 1.01x faster                                              |
| python_startup           | 18.9 ms                                                               | 18.8 ms: 1.01x faster                                              |
| json                     | 2.89 ms                                                               | 2.88 ms: 1.01x faster                                              |
| sqlglot_v2_normalize     | 68.8 ms                                                               | 68.4 ms: 1.01x faster                                              |
| scimark_fft              | 199 ms                                                                | 198 ms: 1.00x faster                                               |
| pickle_pure_python       | 210 us                                                                | 209 us: 1.00x faster                                               |
| coroutines               | 17.2 ms                                                               | 17.1 ms: 1.00x faster                                              |
| mdp                      | 757 ms                                                                | 755 ms: 1.00x faster                                               |
| json_loads               | 16.5 us                                                               | 16.4 us: 1.00x faster                                              |
| scimark_sparse_mat_mult  | 3.54 ms                                                               | 3.54 ms: 1.00x faster                                              |
| richards_super           | 40.4 ms                                                               | 40.5 ms: 1.00x slower                                              |
| bpe_tokeniser            | 3.08 sec                                                              | 3.08 sec: 1.00x slower                                             |
| crypto_pyaes             | 55.7 ms                                                               | 55.8 ms: 1.00x slower                                              |
| docutils                 | 1.47 sec                                                              | 1.47 sec: 1.00x slower                                             |
| logging_format           | 3.71 us                                                               | 3.72 us: 1.00x slower                                              |
| scimark_sor              | 88.7 ms                                                               | 89.0 ms: 1.00x slower                                              |
| spectral_norm            | 67.0 ms                                                               | 67.2 ms: 1.00x slower                                              |
| thrift                   | 444 us                                                                | 445 us: 1.00x slower                                               |
| gc_traversal             | 3.19 ms                                                               | 3.20 ms: 1.00x slower                                              |
| telco                    | 4.57 ms                                                               | 4.60 ms: 1.01x slower                                              |
| json_dumps               | 6.59 ms                                                               | 6.63 ms: 1.01x slower                                              |
| pprint_pformat           | 1.06 sec                                                              | 1.07 sec: 1.01x slower                                             |
| comprehensions           | 12.1 us                                                               | 12.2 us: 1.01x slower                                              |
| async_generators         | 277 ms                                                                | 280 ms: 1.01x slower                                               |
| genshi_xml               | 31.3 ms                                                               | 31.6 ms: 1.01x slower                                              |
| pprint_safe_repr         | 527 ms                                                                | 532 ms: 1.01x slower                                               |
| create_gc_cycles         | 1.36 ms                                                               | 1.37 ms: 1.01x slower                                              |
| sqlite_synth             | 1.58 us                                                               | 1.59 us: 1.01x slower                                              |
| coverage                 | 48.0 ms                                                               | 48.7 ms: 1.01x slower                                              |
| fannkuch                 | 300 ms                                                                | 306 ms: 1.02x slower                                               |
| meteor_contest           | 76.3 ms                                                               | 77.8 ms: 1.02x slower                                              |
| xml_etree_parse          | 98.8 ms                                                               | 101 ms: 1.02x slower                                               |
| Geometric mean           | (ref)                                                                 | 1.00x slower                                                       |

Benchmark hidden because not significant (60): pathlib, pylint, sympy_sum, html5lib, dulwich_log, sphinx, deepcopy_reduce, django_template, logging_silent, sympy_integrate, genshi_text, sympy_expand, richards, async_tree_memoization, asyncio_websockets, async_tree_eager_cpu_io_mixed, async_tree_none, async_tree_eager_cpu_io_mixed_tg, go, async_tree_eager, dask, nbody, hexiom, xml_etree_iterparse, mako, k_core, sqlglot_v2_transpile, regex_dna, async_tree_cpu_io_mixed_tg, connected_components, regex_compile, chaos, raytrace, async_tree_none_tg, scimark_monte_carlo, many_optionals, async_tree_memoization_tg, async_tree_cpu_io_mixed, logging_simple, nqueens, subparsers, unpickle_pure_python, deepcopy_memo, pidigits, generators, sympy_str, async_tree_eager_memoization_tg, deltablue, async_tree_eager_memoization, 2to3, async_tree_eager_tg, async_tree_eager_io_tg, async_tree_eager_io, sqlglot_v2_parse, pyflate, pycparser, float, async_tree_io_tg, async_tree_io, shortest_path

- Geometric mean (including insignificant results): 1.000x slower

# HPT report

- Reliability score: 89.49% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.98x