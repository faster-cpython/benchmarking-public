# Results vs. base

- fork: faster-cpython
- ref: never_inline_decref
- machine: linux-x86_64
- commit hash: 2ab3a06
- commit date: 2025-06-27
- overall geometric mean: 1.013x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250626-pythonperf2-x86_64-python-a4625d597f9fc2d083fb-3.15.0a0-a4625d5 | bm-20250627-pythonperf2-x86_64-faster%2dcpython-never_inline_decref-3.15.0a0-2ab3a06 |
|----------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                                      | 282 ms: 1.01x slower                                                                 |
| docutils       | 2.83 sec                                                                    | 2.86 sec: 1.01x slower                                                               |
| html5lib       | 67.3 ms                                                                     | 66.6 ms: 1.01x faster                                                                |
| sphinx         | 1.08 sec                                                                    | 1.09 sec: 1.02x slower                                                               |
| Geometric mean | (ref)                                                                       | 1.01x slower                                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250626-pythonperf2-x86_64-python-a4625d597f9fc2d083fb-3.15.0a0-a4625d5 | bm-20250627-pythonperf2-x86_64-faster%2dcpython-never_inline_decref-3.15.0a0-2ab3a06 |
|----------------------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| asyncio_websockets         | 388 ms                                                                      | 385 ms: 1.01x faster                                                                 |
| async_tree_cpu_io_mixed    | 504 ms                                                                      | 508 ms: 1.01x slower                                                                 |
| async_tree_io              | 631 ms                                                                      | 636 ms: 1.01x slower                                                                 |
| async_tree_cpu_io_mixed_tg | 508 ms                                                                      | 514 ms: 1.01x slower                                                                 |
| async_tree_io_tg           | 631 ms                                                                      | 641 ms: 1.02x slower                                                                 |
| async_tree_none_tg         | 271 ms                                                                      | 276 ms: 1.02x slower                                                                 |
| async_tree_memoization_tg  | 331 ms                                                                      | 337 ms: 1.02x slower                                                                 |
| coroutines                 | 21.9 ms                                                                     | 22.8 ms: 1.04x slower                                                                |
| Geometric mean             | (ref)                                                                       | 1.01x slower                                                                         |

Benchmark hidden because not significant (3): async_generators, async_tree_memoization, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250626-pythonperf2-x86_64-python-a4625d597f9fc2d083fb-3.15.0a0-a4625d5 | bm-20250627-pythonperf2-x86_64-faster%2dcpython-never_inline_decref-3.15.0a0-2ab3a06 |
|----------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| pidigits       | 260 ms                                                                      | 258 ms: 1.00x faster                                                                 |
| nbody          | 92.3 ms                                                                     | 94.5 ms: 1.02x slower                                                                |
| Geometric mean | (ref)                                                                       | 1.01x slower                                                                         |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250626-pythonperf2-x86_64-python-a4625d597f9fc2d083fb-3.15.0a0-a4625d5 | bm-20250627-pythonperf2-x86_64-faster%2dcpython-never_inline_decref-3.15.0a0-2ab3a06 |
|----------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_compile  | 133 ms                                                                      | 133 ms: 1.00x slower                                                                 |
| regex_dna      | 221 ms                                                                      | 225 ms: 1.02x slower                                                                 |
| regex_v8       | 23.1 ms                                                                     | 24.2 ms: 1.05x slower                                                                |
| regex_effbot   | 3.49 ms                                                                     | 3.75 ms: 1.07x slower                                                                |
| Geometric mean | (ref)                                                                       | 1.04x slower                                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250626-pythonperf2-x86_64-python-a4625d597f9fc2d083fb-3.15.0a0-a4625d5 | bm-20250627-pythonperf2-x86_64-faster%2dcpython-never_inline_decref-3.15.0a0-2ab3a06 |
|----------------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| tomli_loads          | 2.05 sec                                                                    | 2.04 sec: 1.01x faster                                                               |
| json_loads           | 25.5 us                                                                     | 25.4 us: 1.00x faster                                                                |
| xml_etree_process    | 58.2 ms                                                                     | 59.2 ms: 1.02x slower                                                                |
| xml_etree_generate   | 83.4 ms                                                                     | 84.9 ms: 1.02x slower                                                                |
| pickle_pure_python   | 330 us                                                                      | 340 us: 1.03x slower                                                                 |
| json_dumps           | 11.1 ms                                                                     | 11.6 ms: 1.04x slower                                                                |
| xml_etree_iterparse  | 97.4 ms                                                                     | 102 ms: 1.04x slower                                                                 |
| xml_etree_parse      | 140 ms                                                                      | 146 ms: 1.04x slower                                                                 |
| unpickle_pure_python | 206 us                                                                      | 217 us: 1.05x slower                                                                 |
| Geometric mean       | (ref)                                                                       | 1.03x slower                                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250626-pythonperf2-x86_64-python-a4625d597f9fc2d083fb-3.15.0a0-a4625d5 | bm-20250627-pythonperf2-x86_64-faster%2dcpython-never_inline_decref-3.15.0a0-2ab3a06 |
|------------------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| python_startup_no_site | 8.80 ms                                                                     | 8.83 ms: 1.00x slower                                                                |
| python_startup         | 15.3 ms                                                                     | 15.4 ms: 1.00x slower                                                                |
| Geometric mean         | (ref)                                                                       | 1.00x slower                                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250626-pythonperf2-x86_64-python-a4625d597f9fc2d083fb-3.15.0a0-a4625d5 | bm-20250627-pythonperf2-x86_64-faster%2dcpython-never_inline_decref-3.15.0a0-2ab3a06 |
|-----------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| mako            | 10.8 ms                                                                     | 10.7 ms: 1.01x faster                                                                |
| genshi_text     | 22.8 ms                                                                     | 23.0 ms: 1.01x slower                                                                |
| django_template | 35.3 ms                                                                     | 35.9 ms: 1.02x slower                                                                |
| genshi_xml      | 52.1 ms                                                                     | 53.8 ms: 1.03x slower                                                                |
| Geometric mean  | (ref)                                                                       | 1.01x slower                                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20250626-pythonperf2-x86_64-python-a4625d597f9fc2d083fb-3.15.0a0-a4625d5 | bm-20250627-pythonperf2-x86_64-faster%2dcpython-never_inline_decref-3.15.0a0-2ab3a06 |
|----------------------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| pycparser                  | 1.27 sec                                                                    | 1.22 sec: 1.04x faster                                                               |
| crypto_pyaes               | 77.9 ms                                                                     | 76.0 ms: 1.02x faster                                                                |
| generators                 | 30.1 ms                                                                     | 29.7 ms: 1.01x faster                                                                |
| thrift                     | 846 us                                                                      | 835 us: 1.01x faster                                                                 |
| asyncio_websockets         | 388 ms                                                                      | 385 ms: 1.01x faster                                                                 |
| html5lib                   | 67.3 ms                                                                     | 66.6 ms: 1.01x faster                                                                |
| logging_format             | 6.64 us                                                                     | 6.58 us: 1.01x faster                                                                |
| mako                       | 10.8 ms                                                                     | 10.7 ms: 1.01x faster                                                                |
| spectral_norm              | 86.3 ms                                                                     | 85.7 ms: 1.01x faster                                                                |
| richards_super             | 51.7 ms                                                                     | 51.4 ms: 1.01x faster                                                                |
| logging_silent             | 93.8 ns                                                                     | 93.3 ns: 1.01x faster                                                                |
| logging_simple             | 6.01 us                                                                     | 5.98 us: 1.01x faster                                                                |
| tomli_loads                | 2.05 sec                                                                    | 2.04 sec: 1.01x faster                                                               |
| json_loads                 | 25.5 us                                                                     | 25.4 us: 1.00x faster                                                                |
| pidigits                   | 260 ms                                                                      | 258 ms: 1.00x faster                                                                 |
| mdp                        | 1.29 sec                                                                    | 1.29 sec: 1.00x faster                                                               |
| shortest_path              | 452 ms                                                                      | 450 ms: 1.00x faster                                                                 |
| connected_components       | 421 ms                                                                      | 420 ms: 1.00x faster                                                                 |
| regex_compile              | 133 ms                                                                      | 133 ms: 1.00x slower                                                                 |
| python_startup_no_site     | 8.80 ms                                                                     | 8.83 ms: 1.00x slower                                                                |
| python_startup             | 15.3 ms                                                                     | 15.4 ms: 1.00x slower                                                                |
| comprehensions             | 16.3 us                                                                     | 16.4 us: 1.01x slower                                                                |
| genshi_text                | 22.8 ms                                                                     | 23.0 ms: 1.01x slower                                                                |
| deltablue                  | 3.18 ms                                                                     | 3.20 ms: 1.01x slower                                                                |
| 2to3                       | 280 ms                                                                      | 282 ms: 1.01x slower                                                                 |
| async_tree_cpu_io_mixed    | 504 ms                                                                      | 508 ms: 1.01x slower                                                                 |
| subparsers                 | 24.8 ms                                                                     | 25.0 ms: 1.01x slower                                                                |
| async_tree_io              | 631 ms                                                                      | 636 ms: 1.01x slower                                                                 |
| deepcopy                   | 273 us                                                                      | 276 us: 1.01x slower                                                                 |
| many_optionals             | 1.03 ms                                                                     | 1.04 ms: 1.01x slower                                                                |
| docutils                   | 2.83 sec                                                                    | 2.86 sec: 1.01x slower                                                               |
| meteor_contest             | 119 ms                                                                      | 121 ms: 1.01x slower                                                                 |
| async_tree_cpu_io_mixed_tg | 508 ms                                                                      | 514 ms: 1.01x slower                                                                 |
| pathlib                    | 16.9 ms                                                                     | 17.1 ms: 1.01x slower                                                                |
| chaos                      | 58.8 ms                                                                     | 59.7 ms: 1.01x slower                                                                |
| sympy_integrate            | 21.9 ms                                                                     | 22.2 ms: 1.01x slower                                                                |
| dulwich_log                | 59.6 ms                                                                     | 60.5 ms: 1.01x slower                                                                |
| async_tree_io_tg           | 631 ms                                                                      | 641 ms: 1.02x slower                                                                 |
| django_template            | 35.3 ms                                                                     | 35.9 ms: 1.02x slower                                                                |
| sqlglot_v2_optimize        | 55.8 ms                                                                     | 56.7 ms: 1.02x slower                                                                |
| sphinx                     | 1.08 sec                                                                    | 1.09 sec: 1.02x slower                                                               |
| xml_etree_process          | 58.2 ms                                                                     | 59.2 ms: 1.02x slower                                                                |
| bpe_tokeniser              | 4.69 sec                                                                    | 4.77 sec: 1.02x slower                                                               |
| pprint_pformat             | 1.58 sec                                                                    | 1.61 sec: 1.02x slower                                                               |
| async_tree_none_tg         | 271 ms                                                                      | 276 ms: 1.02x slower                                                                 |
| async_tree_memoization_tg  | 331 ms                                                                      | 337 ms: 1.02x slower                                                                 |
| pprint_safe_repr           | 779 ms                                                                      | 793 ms: 1.02x slower                                                                 |
| create_gc_cycles           | 2.83 ms                                                                     | 2.88 ms: 1.02x slower                                                                |
| fannkuch                   | 363 ms                                                                      | 370 ms: 1.02x slower                                                                 |
| xml_etree_generate         | 83.4 ms                                                                     | 84.9 ms: 1.02x slower                                                                |
| deepcopy_reduce            | 2.94 us                                                                     | 3.00 us: 1.02x slower                                                                |
| scimark_fft                | 307 ms                                                                      | 314 ms: 1.02x slower                                                                 |
| regex_dna                  | 221 ms                                                                      | 225 ms: 1.02x slower                                                                 |
| scimark_sor                | 104 ms                                                                      | 107 ms: 1.02x slower                                                                 |
| sqlite_synth               | 2.84 us                                                                     | 2.91 us: 1.02x slower                                                                |
| sympy_sum                  | 149 ms                                                                      | 153 ms: 1.02x slower                                                                 |
| sqlglot_v2_transpile       | 1.68 ms                                                                     | 1.72 ms: 1.02x slower                                                                |
| nbody                      | 92.3 ms                                                                     | 94.5 ms: 1.02x slower                                                                |
| sympy_str                  | 284 ms                                                                      | 291 ms: 1.02x slower                                                                 |
| sympy_expand               | 483 ms                                                                      | 496 ms: 1.03x slower                                                                 |
| sqlglot_v2_parse           | 1.30 ms                                                                     | 1.34 ms: 1.03x slower                                                                |
| sqlglot_v2_normalize       | 111 ms                                                                      | 114 ms: 1.03x slower                                                                 |
| pickle_pure_python         | 330 us                                                                      | 340 us: 1.03x slower                                                                 |
| pyflate                    | 402 ms                                                                      | 415 ms: 1.03x slower                                                                 |
| genshi_xml                 | 52.1 ms                                                                     | 53.8 ms: 1.03x slower                                                                |
| scimark_sparse_mat_mult    | 4.77 ms                                                                     | 4.93 ms: 1.03x slower                                                                |
| scimark_lu                 | 95.0 ms                                                                     | 98.5 ms: 1.04x slower                                                                |
| json_dumps                 | 11.1 ms                                                                     | 11.6 ms: 1.04x slower                                                                |
| coroutines                 | 21.9 ms                                                                     | 22.8 ms: 1.04x slower                                                                |
| gc_traversal               | 6.47 ms                                                                     | 6.73 ms: 1.04x slower                                                                |
| xml_etree_iterparse        | 97.4 ms                                                                     | 102 ms: 1.04x slower                                                                 |
| xml_etree_parse            | 140 ms                                                                      | 146 ms: 1.04x slower                                                                 |
| scimark_monte_carlo        | 60.6 ms                                                                     | 63.4 ms: 1.05x slower                                                                |
| regex_v8                   | 23.1 ms                                                                     | 24.2 ms: 1.05x slower                                                                |
| unpickle_pure_python       | 206 us                                                                      | 217 us: 1.05x slower                                                                 |
| coverage                   | 82.8 ms                                                                     | 87.9 ms: 1.06x slower                                                                |
| regex_effbot               | 3.49 ms                                                                     | 3.75 ms: 1.07x slower                                                                |
| telco                      | 7.64 ms                                                                     | 8.28 ms: 1.08x slower                                                                |
| Geometric mean             | (ref)                                                                       | 1.01x slower                                                                         |

Benchmark hidden because not significant (15): djangocms, float, async_generators, async_tree_memoization, nqueens, hexiom, richards, raytrace, deepcopy_memo, go, async_tree_none, json, typing_runtime_protocols, k_core, pylint

- Geometric mean (including insignificant results): 1.013x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.99x