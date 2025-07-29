# Results vs. base

- fork: brandtbucher
- ref: macos_10_15
- machine: darwin-arm64
- commit hash: 6d7efa0
- commit date: 2025-07-29
- overall geometric mean: 1.002x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250729-darwin-arm64-python-0b4e13c2658c5a267fc5-3.15.0a0-0b4e13c | bm-20250729-darwin-arm64-brandtbucher-macos_10_15-3.15.0a0-6d7efa0 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 170 ms                                                                | 170 ms: 1.00x slower                                               |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                       |

Benchmark hidden because not significant (3): docutils, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20250729-darwin-arm64-python-0b4e13c2658c5a267fc5-3.15.0a0-0b4e13c | bm-20250729-darwin-arm64-brandtbucher-macos_10_15-3.15.0a0-6d7efa0 |
|------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| coroutines       | 16.7 ms                                                               | 16.3 ms: 1.03x faster                                              |
| async_tree_eager | 64.4 ms                                                               | 64.6 ms: 1.00x slower                                              |
| Geometric mean   | (ref)                                                                 | 1.00x faster                                                       |

Benchmark hidden because not significant (17): async_tree_eager_tg, async_tree_eager_memoization_tg, async_tree_eager_cpu_io_mixed_tg, asyncio_websockets, async_generators, async_tree_memoization, async_tree_eager_io_tg, async_tree_io_tg, async_tree_eager_memoization, async_tree_eager_cpu_io_mixed, async_tree_eager_io, async_tree_none_tg, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_memoization_tg, async_tree_none, async_tree_io

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): nbody, pidigits, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250729-darwin-arm64-python-0b4e13c2658c5a267fc5-3.15.0a0-0b4e13c | bm-20250729-darwin-arm64-brandtbucher-macos_10_15-3.15.0a0-6d7efa0 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_v8       | 15.3 ms                                                               | 15.2 ms: 1.00x faster                                              |
| regex_effbot   | 2.14 ms                                                               | 2.15 ms: 1.00x slower                                              |
| regex_compile  | 72.4 ms                                                               | 73.0 ms: 1.01x slower                                              |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                       |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20250729-darwin-arm64-python-0b4e13c2658c5a267fc5-3.15.0a0-0b4e13c | bm-20250729-darwin-arm64-brandtbucher-macos_10_15-3.15.0a0-6d7efa0 |
|--------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| xml_etree_parse    | 100 ms                                                                | 97.6 ms: 1.03x faster                                              |
| pickle_pure_python | 208 us                                                                | 206 us: 1.01x faster                                               |
| json_loads         | 17.4 us                                                               | 17.5 us: 1.01x slower                                              |
| xml_etree_generate | 49.2 ms                                                               | 49.5 ms: 1.01x slower                                              |
| xml_etree_process  | 34.5 ms                                                               | 34.7 ms: 1.01x slower                                              |
| json_dumps         | 6.54 ms                                                               | 6.61 ms: 1.01x slower                                              |
| Geometric mean     | (ref)                                                                 | 1.00x slower                                                       |

Benchmark hidden because not significant (3): xml_etree_iterparse, unpickle_pure_python, tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250729-darwin-arm64-python-0b4e13c2658c5a267fc5-3.15.0a0-0b4e13c | bm-20250729-darwin-arm64-brandtbucher-macos_10_15-3.15.0a0-6d7efa0 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup         | 17.3 ms                                                               | 16.5 ms: 1.05x faster                                              |
| python_startup_no_site | 12.7 ms                                                               | 12.2 ms: 1.04x faster                                              |
| Geometric mean         | (ref)                                                                 | 1.04x faster                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250729-darwin-arm64-python-0b4e13c2658c5a267fc5-3.15.0a0-0b4e13c | bm-20250729-darwin-arm64-brandtbucher-macos_10_15-3.15.0a0-6d7efa0 |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| django_template | 23.2 ms                                                               | 23.2 ms: 1.00x slower                                              |
| mako            | 6.47 ms                                                               | 6.51 ms: 1.01x slower                                              |
| genshi_xml      | 32.6 ms                                                               | 33.6 ms: 1.03x slower                                              |
| genshi_text     | 15.1 ms                                                               | 15.6 ms: 1.03x slower                                              |
| Geometric mean  | (ref)                                                                 | 1.02x slower                                                       |

All benchmarks:
===============

| Benchmark               | bm-20250729-darwin-arm64-python-0b4e13c2658c5a267fc5-3.15.0a0-0b4e13c | bm-20250729-darwin-arm64-brandtbucher-macos_10_15-3.15.0a0-6d7efa0 |
|-------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup          | 17.3 ms                                                               | 16.5 ms: 1.05x faster                                              |
| python_startup_no_site  | 12.7 ms                                                               | 12.2 ms: 1.04x faster                                              |
| coroutines              | 16.7 ms                                                               | 16.3 ms: 1.03x faster                                              |
| xml_etree_parse         | 100 ms                                                                | 97.6 ms: 1.03x faster                                              |
| comprehensions          | 11.4 us                                                               | 11.3 us: 1.01x faster                                              |
| pickle_pure_python      | 208 us                                                                | 206 us: 1.01x faster                                               |
| bpe_tokeniser           | 2.93 sec                                                              | 2.91 sec: 1.01x faster                                             |
| sqlglot_v2_parse        | 786 us                                                                | 780 us: 1.01x faster                                               |
| json                    | 3.05 ms                                                               | 3.03 ms: 1.01x faster                                              |
| many_optionals          | 596 us                                                                | 593 us: 1.01x faster                                               |
| sqlite_synth            | 1.58 us                                                               | 1.57 us: 1.00x faster                                              |
| sqlglot_v2_optimize     | 33.6 ms                                                               | 33.5 ms: 1.00x faster                                              |
| scimark_sparse_mat_mult | 3.38 ms                                                               | 3.37 ms: 1.00x faster                                              |
| shortest_path           | 350 ms                                                                | 349 ms: 1.00x faster                                               |
| regex_v8                | 15.3 ms                                                               | 15.2 ms: 1.00x faster                                              |
| subparsers              | 25.2 ms                                                               | 25.2 ms: 1.00x faster                                              |
| hexiom                  | 4.57 ms                                                               | 4.58 ms: 1.00x slower                                              |
| regex_effbot            | 2.14 ms                                                               | 2.15 ms: 1.00x slower                                              |
| scimark_lu              | 75.4 ms                                                               | 75.5 ms: 1.00x slower                                              |
| sqlglot_v2_transpile    | 954 us                                                                | 957 us: 1.00x slower                                               |
| async_tree_eager        | 64.4 ms                                                               | 64.6 ms: 1.00x slower                                              |
| django_template         | 23.2 ms                                                               | 23.2 ms: 1.00x slower                                              |
| sympy_sum               | 76.9 ms                                                               | 77.1 ms: 1.00x slower                                              |
| nqueens                 | 61.5 ms                                                               | 61.7 ms: 1.00x slower                                              |
| 2to3                    | 170 ms                                                                | 170 ms: 1.00x slower                                               |
| logging_format          | 3.64 us                                                               | 3.66 us: 1.00x slower                                              |
| deepcopy                | 173 us                                                                | 173 us: 1.00x slower                                               |
| sympy_expand            | 248 ms                                                                | 249 ms: 1.01x slower                                               |
| chaos                   | 38.7 ms                                                               | 38.9 ms: 1.01x slower                                              |
| dulwich_log             | 25.4 ms                                                               | 25.5 ms: 1.01x slower                                              |
| sympy_str               | 146 ms                                                                | 147 ms: 1.01x slower                                               |
| fannkuch                | 247 ms                                                                | 248 ms: 1.01x slower                                               |
| json_loads              | 17.4 us                                                               | 17.5 us: 1.01x slower                                              |
| xml_etree_generate      | 49.2 ms                                                               | 49.5 ms: 1.01x slower                                              |
| mako                    | 6.47 ms                                                               | 6.51 ms: 1.01x slower                                              |
| deepcopy_reduce         | 1.77 us                                                               | 1.78 us: 1.01x slower                                              |
| xml_etree_process       | 34.5 ms                                                               | 34.7 ms: 1.01x slower                                              |
| regex_compile           | 72.4 ms                                                               | 73.0 ms: 1.01x slower                                              |
| logging_simple          | 3.34 us                                                               | 3.37 us: 1.01x slower                                              |
| deepcopy_memo           | 21.7 us                                                               | 22.0 us: 1.01x slower                                              |
| json_dumps              | 6.54 ms                                                               | 6.61 ms: 1.01x slower                                              |
| go                      | 86.1 ms                                                               | 87.2 ms: 1.01x slower                                              |
| logging_silent          | 74.1 ns                                                               | 75.0 ns: 1.01x slower                                              |
| generators              | 24.3 ms                                                               | 24.6 ms: 1.01x slower                                              |
| spectral_norm           | 62.9 ms                                                               | 63.8 ms: 1.01x slower                                              |
| telco                   | 4.37 ms                                                               | 4.43 ms: 1.01x slower                                              |
| meteor_contest          | 73.0 ms                                                               | 74.1 ms: 1.01x slower                                              |
| deltablue               | 2.48 ms                                                               | 2.52 ms: 1.02x slower                                              |
| scimark_monte_carlo     | 45.3 ms                                                               | 46.2 ms: 1.02x slower                                              |
| gc_traversal            | 3.18 ms                                                               | 3.25 ms: 1.02x slower                                              |
| richards                | 33.6 ms                                                               | 34.3 ms: 1.02x slower                                              |
| richards_super          | 37.5 ms                                                               | 38.4 ms: 1.03x slower                                              |
| raytrace                | 173 ms                                                                | 178 ms: 1.03x slower                                               |
| genshi_xml              | 32.6 ms                                                               | 33.6 ms: 1.03x slower                                              |
| genshi_text             | 15.1 ms                                                               | 15.6 ms: 1.03x slower                                              |
| Geometric mean          | (ref)                                                                 | 1.00x slower                                                       |

Benchmark hidden because not significant (46): async_tree_eager_tg, xml_etree_iterparse, async_tree_eager_memoization_tg, nbody, thrift, crypto_pyaes, scimark_fft, async_tree_eager_cpu_io_mixed_tg, sympy_integrate, sqlglot_v2_normalize, coverage, k_core, asyncio_websockets, create_gc_cycles, regex_dna, async_generators, mdp, pidigits, async_tree_memoization, async_tree_eager_io_tg, float, connected_components, pyflate, dask, async_tree_io_tg, scimark_sor, async_tree_eager_memoization, docutils, async_tree_eager_cpu_io_mixed, async_tree_eager_io, async_tree_none_tg, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, html5lib, pprint_safe_repr, pylint, sphinx, unpickle_pure_python, async_tree_memoization_tg, typing_runtime_protocols, async_tree_none, pprint_pformat, async_tree_io, tomli_loads, pathlib, pycparser

- Geometric mean (including insignificant results): 1.002x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x