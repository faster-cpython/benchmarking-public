# Results vs. base

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 406dc71
- commit date: 2025-08-03
- overall geometric mean: 1.029x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250803-pythonperf2-x86_64-python-13e21b2fd6343ba8309e-3.15.0a0-13e21b2 | bm-20250803-pythonperf2-x86_64-python-main-3.15.0a0-406dc71 |
|----------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------:|
| 2to3           | 320 ms                                                                      | 325 ms: 1.02x slower                                        |
| docutils       | 3.10 sec                                                                    | 3.14 sec: 1.01x slower                                      |
| html5lib       | 68.6 ms                                                                     | 70.2 ms: 1.02x slower                                       |
| Geometric mean | (ref)                                                                       | 1.01x slower                                                |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250803-pythonperf2-x86_64-python-13e21b2fd6343ba8309e-3.15.0a0-13e21b2 | bm-20250803-pythonperf2-x86_64-python-main-3.15.0a0-406dc71 |
|----------------------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------:|
| async_generators           | 454 ms                                                                      | 456 ms: 1.00x slower                                        |
| async_tree_cpu_io_mixed_tg | 523 ms                                                                      | 527 ms: 1.01x slower                                        |
| async_tree_io_tg           | 662 ms                                                                      | 671 ms: 1.01x slower                                        |
| async_tree_cpu_io_mixed    | 524 ms                                                                      | 531 ms: 1.01x slower                                        |
| async_tree_io              | 657 ms                                                                      | 667 ms: 1.01x slower                                        |
| async_tree_none_tg         | 285 ms                                                                      | 290 ms: 1.02x slower                                        |
| async_tree_memoization_tg  | 347 ms                                                                      | 354 ms: 1.02x slower                                        |
| async_tree_memoization     | 354 ms                                                                      | 362 ms: 1.02x slower                                        |
| async_tree_none            | 300 ms                                                                      | 306 ms: 1.02x slower                                        |
| Geometric mean             | (ref)                                                                       | 1.01x slower                                                |

Benchmark hidden because not significant (2): asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250803-pythonperf2-x86_64-python-13e21b2fd6343ba8309e-3.15.0a0-13e21b2 | bm-20250803-pythonperf2-x86_64-python-main-3.15.0a0-406dc71 |
|----------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------:|
| float          | 95.8 ms                                                                     | 107 ms: 1.11x slower                                        |
| nbody          | 162 ms                                                                      | 184 ms: 1.14x slower                                        |
| Geometric mean | (ref)                                                                       | 1.08x slower                                                |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250803-pythonperf2-x86_64-python-13e21b2fd6343ba8309e-3.15.0a0-13e21b2 | bm-20250803-pythonperf2-x86_64-python-main-3.15.0a0-406dc71 |
|----------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------:|
| regex_v8       | 24.2 ms                                                                     | 23.9 ms: 1.01x faster                                       |
| regex_dna      | 221 ms                                                                      | 223 ms: 1.01x slower                                        |
| regex_compile  | 155 ms                                                                      | 159 ms: 1.03x slower                                        |
| regex_effbot   | 3.43 ms                                                                     | 3.64 ms: 1.06x slower                                       |
| Geometric mean | (ref)                                                                       | 1.02x slower                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250803-pythonperf2-x86_64-python-13e21b2fd6343ba8309e-3.15.0a0-13e21b2 | bm-20250803-pythonperf2-x86_64-python-main-3.15.0a0-406dc71 |
|----------------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------:|
| json_loads           | 26.6 us                                                                     | 25.2 us: 1.06x faster                                       |
| xml_etree_parse      | 143 ms                                                                      | 142 ms: 1.01x faster                                        |
| xml_etree_iterparse  | 108 ms                                                                      | 110 ms: 1.02x slower                                        |
| pickle_pure_python   | 396 us                                                                      | 410 us: 1.04x slower                                        |
| xml_etree_generate   | 102 ms                                                                      | 109 ms: 1.07x slower                                        |
| xml_etree_process    | 70.9 ms                                                                     | 76.1 ms: 1.07x slower                                       |
| tomli_loads          | 2.83 sec                                                                    | 3.08 sec: 1.09x slower                                      |
| unpickle_pure_python | 340 us                                                                      | 388 us: 1.14x slower                                        |
| Geometric mean       | (ref)                                                                       | 1.04x slower                                                |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250803-pythonperf2-x86_64-python-13e21b2fd6343ba8309e-3.15.0a0-13e21b2 | bm-20250803-pythonperf2-x86_64-python-main-3.15.0a0-406dc71 |
|------------------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------:|
| python_startup_no_site | 8.87 ms                                                                     | 8.81 ms: 1.01x faster                                       |
| python_startup         | 15.4 ms                                                                     | 15.4 ms: 1.01x faster                                       |
| Geometric mean         | (ref)                                                                       | 1.01x faster                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250803-pythonperf2-x86_64-python-13e21b2fd6343ba8309e-3.15.0a0-13e21b2 | bm-20250803-pythonperf2-x86_64-python-main-3.15.0a0-406dc71 |
|-----------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------:|
| genshi_text     | 24.0 ms                                                                     | 23.7 ms: 1.01x faster                                       |
| django_template | 35.0 ms                                                                     | 35.3 ms: 1.01x slower                                       |
| genshi_xml      | 57.0 ms                                                                     | 57.7 ms: 1.01x slower                                       |
| mako            | 15.2 ms                                                                     | 16.9 ms: 1.11x slower                                       |
| Geometric mean  | (ref)                                                                       | 1.03x slower                                                |

All benchmarks:
===============

| Benchmark                  | bm-20250803-pythonperf2-x86_64-python-13e21b2fd6343ba8309e-3.15.0a0-13e21b2 | bm-20250803-pythonperf2-x86_64-python-main-3.15.0a0-406dc71 |
|----------------------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------:|
| json_loads                 | 26.6 us                                                                     | 25.2 us: 1.06x faster                                       |
| deepcopy_memo              | 28.9 us                                                                     | 27.6 us: 1.05x faster                                       |
| scimark_lu                 | 95.2 ms                                                                     | 92.5 ms: 1.03x faster                                       |
| json                       | 5.48 ms                                                                     | 5.33 ms: 1.03x faster                                       |
| scimark_sor                | 105 ms                                                                      | 102 ms: 1.02x faster                                        |
| coverage                   | 79.3 ms                                                                     | 77.8 ms: 1.02x faster                                       |
| genshi_text                | 24.0 ms                                                                     | 23.7 ms: 1.01x faster                                       |
| regex_v8                   | 24.2 ms                                                                     | 23.9 ms: 1.01x faster                                       |
| telco                      | 161 ms                                                                      | 159 ms: 1.01x faster                                        |
| dulwich_log                | 61.4 ms                                                                     | 60.9 ms: 1.01x faster                                       |
| python_startup_no_site     | 8.87 ms                                                                     | 8.81 ms: 1.01x faster                                       |
| python_startup             | 15.4 ms                                                                     | 15.4 ms: 1.01x faster                                       |
| xml_etree_parse            | 143 ms                                                                      | 142 ms: 1.01x faster                                        |
| deepcopy                   | 280 us                                                                      | 279 us: 1.00x faster                                        |
| pathlib                    | 16.7 ms                                                                     | 16.7 ms: 1.00x faster                                       |
| logging_silent             | 91.4 ns                                                                     | 91.7 ns: 1.00x slower                                       |
| sympy_integrate            | 23.7 ms                                                                     | 23.7 ms: 1.00x slower                                       |
| async_generators           | 454 ms                                                                      | 456 ms: 1.00x slower                                        |
| deepcopy_reduce            | 2.93 us                                                                     | 2.95 us: 1.00x slower                                       |
| sympy_expand               | 550 ms                                                                      | 552 ms: 1.00x slower                                        |
| subparsers                 | 43.0 ms                                                                     | 43.2 ms: 1.01x slower                                       |
| many_optionals             | 1.27 ms                                                                     | 1.28 ms: 1.01x slower                                       |
| sqlglot_v2_normalize       | 122 ms                                                                      | 123 ms: 1.01x slower                                        |
| regex_dna                  | 221 ms                                                                      | 223 ms: 1.01x slower                                        |
| generators                 | 29.7 ms                                                                     | 29.9 ms: 1.01x slower                                       |
| async_tree_cpu_io_mixed_tg | 523 ms                                                                      | 527 ms: 1.01x slower                                        |
| sympy_str                  | 312 ms                                                                      | 315 ms: 1.01x slower                                        |
| gc_traversal               | 6.70 ms                                                                     | 6.77 ms: 1.01x slower                                       |
| sqlglot_v2_optimize        | 63.7 ms                                                                     | 64.4 ms: 1.01x slower                                       |
| django_template            | 35.0 ms                                                                     | 35.3 ms: 1.01x slower                                       |
| mdp                        | 1.45 sec                                                                    | 1.46 sec: 1.01x slower                                      |
| genshi_xml                 | 57.0 ms                                                                     | 57.7 ms: 1.01x slower                                       |
| docutils                   | 3.10 sec                                                                    | 3.14 sec: 1.01x slower                                      |
| async_tree_io_tg           | 662 ms                                                                      | 671 ms: 1.01x slower                                        |
| async_tree_cpu_io_mixed    | 524 ms                                                                      | 531 ms: 1.01x slower                                        |
| async_tree_io              | 657 ms                                                                      | 667 ms: 1.01x slower                                        |
| k_core                     | 2.26 sec                                                                    | 2.29 sec: 1.02x slower                                      |
| 2to3                       | 320 ms                                                                      | 325 ms: 1.02x slower                                        |
| logging_format             | 6.58 us                                                                     | 6.69 us: 1.02x slower                                       |
| shortest_path              | 492 ms                                                                      | 501 ms: 1.02x slower                                        |
| async_tree_none_tg         | 285 ms                                                                      | 290 ms: 1.02x slower                                        |
| sqlite_synth               | 2.96 us                                                                     | 3.01 us: 1.02x slower                                       |
| async_tree_memoization_tg  | 347 ms                                                                      | 354 ms: 1.02x slower                                        |
| async_tree_memoization     | 354 ms                                                                      | 362 ms: 1.02x slower                                        |
| async_tree_none            | 300 ms                                                                      | 306 ms: 1.02x slower                                        |
| html5lib                   | 68.6 ms                                                                     | 70.2 ms: 1.02x slower                                       |
| xml_etree_iterparse        | 108 ms                                                                      | 110 ms: 1.02x slower                                        |
| regex_compile              | 155 ms                                                                      | 159 ms: 1.03x slower                                        |
| connected_components       | 474 ms                                                                      | 487 ms: 1.03x slower                                        |
| logging_simple             | 5.93 us                                                                     | 6.10 us: 1.03x slower                                       |
| nqueens                    | 100 ms                                                                      | 103 ms: 1.03x slower                                        |
| typing_runtime_protocols   | 195 us                                                                      | 201 us: 1.03x slower                                        |
| pycparser                  | 1.47 sec                                                                    | 1.52 sec: 1.03x slower                                      |
| chaos                      | 61.3 ms                                                                     | 63.4 ms: 1.04x slower                                       |
| pickle_pure_python         | 396 us                                                                      | 410 us: 1.04x slower                                        |
| sqlglot_v2_transpile       | 2.04 ms                                                                     | 2.13 ms: 1.04x slower                                       |
| crypto_pyaes               | 99.9 ms                                                                     | 105 ms: 1.05x slower                                        |
| richards                   | 50.6 ms                                                                     | 53.3 ms: 1.05x slower                                       |
| sqlglot_v2_parse           | 1.65 ms                                                                     | 1.74 ms: 1.05x slower                                       |
| meteor_contest             | 151 ms                                                                      | 160 ms: 1.06x slower                                        |
| regex_effbot               | 3.43 ms                                                                     | 3.64 ms: 1.06x slower                                       |
| pprint_pformat             | 2.12 sec                                                                    | 2.26 sec: 1.06x slower                                      |
| scimark_fft                | 434 ms                                                                      | 462 ms: 1.07x slower                                        |
| pprint_safe_repr           | 1.05 sec                                                                    | 1.11 sec: 1.07x slower                                      |
| xml_etree_generate         | 102 ms                                                                      | 109 ms: 1.07x slower                                        |
| raytrace                   | 319 ms                                                                      | 341 ms: 1.07x slower                                        |
| xml_etree_process          | 70.9 ms                                                                     | 76.1 ms: 1.07x slower                                       |
| richards_super             | 55.5 ms                                                                     | 59.7 ms: 1.08x slower                                       |
| pyflate                    | 582 ms                                                                      | 632 ms: 1.08x slower                                        |
| tomli_loads                | 2.83 sec                                                                    | 3.08 sec: 1.09x slower                                      |
| bpe_tokeniser              | 5.95 sec                                                                    | 6.48 sec: 1.09x slower                                      |
| scimark_monte_carlo        | 81.4 ms                                                                     | 88.9 ms: 1.09x slower                                       |
| hexiom                     | 9.71 ms                                                                     | 10.6 ms: 1.09x slower                                       |
| go                         | 204 ms                                                                      | 224 ms: 1.10x slower                                        |
| scimark_sparse_mat_mult    | 7.57 ms                                                                     | 8.35 ms: 1.10x slower                                       |
| fannkuch                   | 550 ms                                                                      | 607 ms: 1.11x slower                                        |
| mako                       | 15.2 ms                                                                     | 16.9 ms: 1.11x slower                                       |
| float                      | 95.8 ms                                                                     | 107 ms: 1.11x slower                                        |
| comprehensions             | 27.4 us                                                                     | 30.6 us: 1.12x slower                                       |
| deltablue                  | 5.34 ms                                                                     | 5.97 ms: 1.12x slower                                       |
| spectral_norm              | 148 ms                                                                      | 168 ms: 1.14x slower                                        |
| unpickle_pure_python       | 340 us                                                                      | 388 us: 1.14x slower                                        |
| nbody                      | 162 ms                                                                      | 184 ms: 1.14x slower                                        |
| Geometric mean             | (ref)                                                                       | 1.03x slower                                                |

Benchmark hidden because not significant (10): asyncio_websockets, thrift, json_dumps, sphinx, pylint, sympy_sum, djangocms, pidigits, create_gc_cycles, coroutines

- Geometric mean (including insignificant results): 1.029x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 1.00x