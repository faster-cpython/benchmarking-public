# Results vs. base

- fork: faster-cpython
- ref: tier_2_tos_caching
- machine: linux-x86_64
- commit hash: 53a50eb
- commit date: 2025-07-21
- overall geometric mean: 1.004x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250721-pythonperf2-x86_64-python-9c7b2af73dee2b997936-3.15.0a0-9c7b2af | bm-20250721-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-53a50eb |
|----------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| docutils       | 2.92 sec                                                                    | 2.94 sec: 1.01x slower                                                              |
| html5lib       | 67.5 ms                                                                     | 66.3 ms: 1.02x faster                                                               |
| sphinx         | 1.09 sec                                                                    | 1.10 sec: 1.01x slower                                                              |
| Geometric mean | (ref)                                                                       | 1.00x slower                                                                        |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark          | bm-20250721-pythonperf2-x86_64-python-9c7b2af73dee2b997936-3.15.0a0-9c7b2af | bm-20250721-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-53a50eb |
|--------------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| asyncio_websockets | 381 ms                                                                      | 383 ms: 1.01x slower                                                                |
| async_tree_none_tg | 272 ms                                                                      | 274 ms: 1.01x slower                                                                |
| coroutines         | 22.3 ms                                                                     | 22.6 ms: 1.02x slower                                                               |
| Geometric mean     | (ref)                                                                       | 1.00x slower                                                                        |

Benchmark hidden because not significant (8): async_generators, async_tree_io, async_tree_cpu_io_mixed, async_tree_none, async_tree_io_tg, async_tree_memoization, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250721-pythonperf2-x86_64-python-9c7b2af73dee2b997936-3.15.0a0-9c7b2af | bm-20250721-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-53a50eb |
|----------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| nbody          | 98.4 ms                                                                     | 88.8 ms: 1.11x faster                                                               |
| float          | 64.2 ms                                                                     | 61.5 ms: 1.04x faster                                                               |
| pidigits       | 256 ms                                                                      | 256 ms: 1.00x faster                                                                |
| Geometric mean | (ref)                                                                       | 1.05x faster                                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250721-pythonperf2-x86_64-python-9c7b2af73dee2b997936-3.15.0a0-9c7b2af | bm-20250721-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-53a50eb |
|----------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| regex_effbot   | 3.71 ms                                                                     | 3.58 ms: 1.04x faster                                                               |
| regex_dna      | 228 ms                                                                      | 227 ms: 1.00x faster                                                                |
| regex_compile  | 132 ms                                                                      | 133 ms: 1.01x slower                                                                |
| regex_v8       | 22.9 ms                                                                     | 24.5 ms: 1.07x slower                                                               |
| Geometric mean | (ref)                                                                       | 1.01x slower                                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250721-pythonperf2-x86_64-python-9c7b2af73dee2b997936-3.15.0a0-9c7b2af | bm-20250721-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-53a50eb |
|----------------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| xml_etree_iterparse  | 96.9 ms                                                                     | 96.4 ms: 1.01x faster                                                               |
| xml_etree_parse      | 138 ms                                                                      | 137 ms: 1.01x faster                                                                |
| tomli_loads          | 1.92 sec                                                                    | 1.94 sec: 1.01x slower                                                              |
| pickle_pure_python   | 334 us                                                                      | 338 us: 1.01x slower                                                                |
| json_loads           | 24.9 us                                                                     | 25.3 us: 1.01x slower                                                               |
| xml_etree_generate   | 81.6 ms                                                                     | 83.2 ms: 1.02x slower                                                               |
| xml_etree_process    | 56.6 ms                                                                     | 58.2 ms: 1.03x slower                                                               |
| unpickle_pure_python | 197 us                                                                      | 204 us: 1.04x slower                                                                |
| Geometric mean       | (ref)                                                                       | 1.01x slower                                                                        |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250721-pythonperf2-x86_64-python-9c7b2af73dee2b997936-3.15.0a0-9c7b2af | bm-20250721-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-53a50eb |
|------------------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| python_startup         | 15.3 ms                                                                     | 15.2 ms: 1.00x faster                                                               |
| python_startup_no_site | 8.72 ms                                                                     | 8.70 ms: 1.00x faster                                                               |
| Geometric mean         | (ref)                                                                       | 1.00x faster                                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250721-pythonperf2-x86_64-python-9c7b2af73dee2b997936-3.15.0a0-9c7b2af | bm-20250721-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-53a50eb |
|-----------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| django_template | 35.5 ms                                                                     | 35.2 ms: 1.01x faster                                                               |
| genshi_text     | 23.0 ms                                                                     | 23.3 ms: 1.01x slower                                                               |
| mako            | 9.65 ms                                                                     | 10.4 ms: 1.08x slower                                                               |
| Geometric mean  | (ref)                                                                       | 1.02x slower                                                                        |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark               | bm-20250721-pythonperf2-x86_64-python-9c7b2af73dee2b997936-3.15.0a0-9c7b2af | bm-20250721-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-53a50eb |
|-------------------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| nbody                   | 98.4 ms                                                                     | 88.8 ms: 1.11x faster                                                               |
| float                   | 64.2 ms                                                                     | 61.5 ms: 1.04x faster                                                               |
| coverage                | 81.7 ms                                                                     | 78.7 ms: 1.04x faster                                                               |
| regex_effbot            | 3.71 ms                                                                     | 3.58 ms: 1.04x faster                                                               |
| create_gc_cycles        | 2.91 ms                                                                     | 2.85 ms: 1.02x faster                                                               |
| go                      | 128 ms                                                                      | 126 ms: 1.02x faster                                                                |
| html5lib                | 67.5 ms                                                                     | 66.3 ms: 1.02x faster                                                               |
| pycparser               | 1.26 sec                                                                    | 1.24 sec: 1.01x faster                                                              |
| json                    | 5.40 ms                                                                     | 5.34 ms: 1.01x faster                                                               |
| deepcopy                | 280 us                                                                      | 278 us: 1.01x faster                                                                |
| gc_traversal            | 6.53 ms                                                                     | 6.47 ms: 1.01x faster                                                               |
| django_template         | 35.5 ms                                                                     | 35.2 ms: 1.01x faster                                                               |
| xml_etree_iterparse     | 96.9 ms                                                                     | 96.4 ms: 1.01x faster                                                               |
| nqueens                 | 93.2 ms                                                                     | 92.6 ms: 1.01x faster                                                               |
| logging_silent          | 93.8 ns                                                                     | 93.3 ns: 1.01x faster                                                               |
| xml_etree_parse         | 138 ms                                                                      | 137 ms: 1.01x faster                                                                |
| subparsers              | 42.9 ms                                                                     | 42.7 ms: 1.00x faster                                                               |
| regex_dna               | 228 ms                                                                      | 227 ms: 1.00x faster                                                                |
| python_startup          | 15.3 ms                                                                     | 15.2 ms: 1.00x faster                                                               |
| python_startup_no_site  | 8.72 ms                                                                     | 8.70 ms: 1.00x faster                                                               |
| shortest_path           | 442 ms                                                                      | 442 ms: 1.00x faster                                                                |
| pidigits                | 256 ms                                                                      | 256 ms: 1.00x faster                                                                |
| deepcopy_memo           | 28.3 us                                                                     | 28.4 us: 1.00x slower                                                               |
| chaos                   | 59.9 ms                                                                     | 60.1 ms: 1.00x slower                                                               |
| spectral_norm           | 79.2 ms                                                                     | 79.4 ms: 1.00x slower                                                               |
| sqlite_synth            | 2.80 us                                                                     | 2.81 us: 1.00x slower                                                               |
| mdp                     | 1.28 sec                                                                    | 1.29 sec: 1.00x slower                                                              |
| fannkuch                | 369 ms                                                                      | 370 ms: 1.00x slower                                                                |
| sympy_expand            | 498 ms                                                                      | 500 ms: 1.00x slower                                                                |
| raytrace                | 291 ms                                                                      | 292 ms: 1.00x slower                                                                |
| pyflate                 | 421 ms                                                                      | 423 ms: 1.00x slower                                                                |
| sympy_str               | 291 ms                                                                      | 292 ms: 1.01x slower                                                                |
| deltablue               | 2.90 ms                                                                     | 2.92 ms: 1.01x slower                                                               |
| telco                   | 159 ms                                                                      | 160 ms: 1.01x slower                                                                |
| asyncio_websockets      | 381 ms                                                                      | 383 ms: 1.01x slower                                                                |
| regex_compile           | 132 ms                                                                      | 133 ms: 1.01x slower                                                                |
| sympy_sum               | 151 ms                                                                      | 153 ms: 1.01x slower                                                                |
| async_tree_none_tg      | 272 ms                                                                      | 274 ms: 1.01x slower                                                                |
| bpe_tokeniser           | 4.56 sec                                                                    | 4.60 sec: 1.01x slower                                                              |
| docutils                | 2.92 sec                                                                    | 2.94 sec: 1.01x slower                                                              |
| genshi_text             | 23.0 ms                                                                     | 23.3 ms: 1.01x slower                                                               |
| tomli_loads             | 1.92 sec                                                                    | 1.94 sec: 1.01x slower                                                              |
| sqlglot_v2_normalize    | 114 ms                                                                      | 115 ms: 1.01x slower                                                                |
| sqlglot_v2_optimize     | 57.4 ms                                                                     | 58.0 ms: 1.01x slower                                                               |
| scimark_fft             | 300 ms                                                                      | 303 ms: 1.01x slower                                                                |
| pickle_pure_python      | 334 us                                                                      | 338 us: 1.01x slower                                                                |
| sphinx                  | 1.09 sec                                                                    | 1.10 sec: 1.01x slower                                                              |
| hexiom                  | 6.20 ms                                                                     | 6.28 ms: 1.01x slower                                                               |
| json_loads              | 24.9 us                                                                     | 25.3 us: 1.01x slower                                                               |
| scimark_lu              | 95.0 ms                                                                     | 96.4 ms: 1.01x slower                                                               |
| pprint_safe_repr        | 741 ms                                                                      | 753 ms: 1.02x slower                                                                |
| coroutines              | 22.3 ms                                                                     | 22.6 ms: 1.02x slower                                                               |
| pprint_pformat          | 1.50 sec                                                                    | 1.53 sec: 1.02x slower                                                              |
| meteor_contest          | 121 ms                                                                      | 123 ms: 1.02x slower                                                                |
| richards_super          | 40.8 ms                                                                     | 41.6 ms: 1.02x slower                                                               |
| scimark_sparse_mat_mult | 4.81 ms                                                                     | 4.91 ms: 1.02x slower                                                               |
| xml_etree_generate      | 81.6 ms                                                                     | 83.2 ms: 1.02x slower                                                               |
| dulwich_log             | 58.4 ms                                                                     | 59.7 ms: 1.02x slower                                                               |
| crypto_pyaes            | 77.3 ms                                                                     | 79.0 ms: 1.02x slower                                                               |
| scimark_monte_carlo     | 62.5 ms                                                                     | 64.0 ms: 1.02x slower                                                               |
| comprehensions          | 17.3 us                                                                     | 17.8 us: 1.02x slower                                                               |
| logging_format          | 6.69 us                                                                     | 6.87 us: 1.03x slower                                                               |
| xml_etree_process       | 56.6 ms                                                                     | 58.2 ms: 1.03x slower                                                               |
| unpickle_pure_python    | 197 us                                                                      | 204 us: 1.04x slower                                                                |
| logging_simple          | 6.06 us                                                                     | 6.32 us: 1.04x slower                                                               |
| scimark_sor             | 103 ms                                                                      | 108 ms: 1.05x slower                                                                |
| regex_v8                | 22.9 ms                                                                     | 24.5 ms: 1.07x slower                                                               |
| mako                    | 9.65 ms                                                                     | 10.4 ms: 1.08x slower                                                               |
| Geometric mean          | (ref)                                                                       | 1.00x slower                                                                        |

Benchmark hidden because not significant (25): typing_runtime_protocols, thrift, async_generators, sqlglot_v2_parse, pylint, async_tree_io, many_optionals, djangocms, 2to3, async_tree_cpu_io_mixed, sympy_integrate, async_tree_none, k_core, async_tree_io_tg, connected_components, pathlib, generators, sqlglot_v2_transpile, genshi_xml, deepcopy_reduce, async_tree_memoization, json_dumps, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, richards

- Geometric mean (including insignificant results): 1.004x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.01x