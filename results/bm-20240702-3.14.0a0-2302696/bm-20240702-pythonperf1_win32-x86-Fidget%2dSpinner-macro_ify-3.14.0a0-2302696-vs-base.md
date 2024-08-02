# Results vs. base

- fork: Fidget-Spinner
- ref: macro_ify
- machine: windows-x86
- commit hash: 2302696
- commit date: 2024-07-02
- overall geometric mean: 1.07x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240702-pythonperf1_win32-x86-python-6343486eb60ac5a9e154-3.14.0a0-6343486 | bm-20240702-pythonperf1_win32-x86-Fidget%2dSpinner-macro_ify-3.14.0a0-2302696 |
|----------------|:------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                                         | 253 ms: 1.05x faster                                                          |
| docutils       | 1.96 sec                                                                       | 1.89 sec: 1.04x faster                                                        |
| html5lib       | 50.7 ms                                                                        | 49.9 ms: 1.02x faster                                                         |
| tornado_http   | 98.5 ms                                                                        | 95.2 ms: 1.04x faster                                                         |
| Geometric mean | (ref)                                                                          | 1.03x faster                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240702-pythonperf1_win32-x86-python-6343486eb60ac5a9e154-3.14.0a0-6343486 | bm-20240702-pythonperf1_win32-x86-Fidget%2dSpinner-macro_ify-3.14.0a0-2302696 |
|----------------------------|:------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_none_tg         | 213 ms                                                                         | 190 ms: 1.12x faster                                                          |
| async_tree_memoization_tg  | 265 ms                                                                         | 242 ms: 1.10x faster                                                          |
| async_tree_io_tg           | 541 ms                                                                         | 495 ms: 1.09x faster                                                          |
| async_tree_none            | 242 ms                                                                         | 223 ms: 1.09x faster                                                          |
| async_tree_memoization     | 294 ms                                                                         | 272 ms: 1.08x faster                                                          |
| async_tree_io              | 581 ms                                                                         | 539 ms: 1.08x faster                                                          |
| async_tree_cpu_io_mixed    | 487 ms                                                                         | 470 ms: 1.04x faster                                                          |
| async_tree_cpu_io_mixed_tg | 465 ms                                                                         | 459 ms: 1.01x faster                                                          |
| Geometric mean             | (ref)                                                                          | 1.08x faster                                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240702-pythonperf1_win32-x86-python-6343486eb60ac5a9e154-3.14.0a0-6343486 | bm-20240702-pythonperf1_win32-x86-Fidget%2dSpinner-macro_ify-3.14.0a0-2302696 |
|----------------|:------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| nbody          | 105 ms                                                                         | 93.6 ms: 1.12x faster                                                         |
| float          | 66.0 ms                                                                        | 60.9 ms: 1.08x faster                                                         |
| Geometric mean | (ref)                                                                          | 1.07x faster                                                                  |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240702-pythonperf1_win32-x86-python-6343486eb60ac5a9e154-3.14.0a0-6343486 | bm-20240702-pythonperf1_win32-x86-Fidget%2dSpinner-macro_ify-3.14.0a0-2302696 |
|----------------|:------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                                         | 106 ms: 1.10x faster                                                          |
| regex_v8       | 16.1 ms                                                                        | 16.3 ms: 1.01x slower                                                         |
| regex_dna      | 122 ms                                                                         | 124 ms: 1.01x slower                                                          |
| regex_effbot   | 1.88 ms                                                                        | 1.92 ms: 1.02x slower                                                         |
| Geometric mean | (ref)                                                                          | 1.01x faster                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240702-pythonperf1_win32-x86-python-6343486eb60ac5a9e154-3.14.0a0-6343486 | bm-20240702-pythonperf1_win32-x86-Fidget%2dSpinner-macro_ify-3.14.0a0-2302696 |
|----------------------|:------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| pickle_pure_python   | 286 us                                                                         | 245 us: 1.17x faster                                                          |
| unpickle_pure_python | 198 us                                                                         | 171 us: 1.16x faster                                                          |
| tomli_loads          | 2.05 sec                                                                       | 1.82 sec: 1.13x faster                                                        |
| xml_etree_generate   | 72.2 ms                                                                        | 66.0 ms: 1.09x faster                                                         |
| json_dumps           | 7.91 ms                                                                        | 7.29 ms: 1.08x faster                                                         |
| xml_etree_process    | 52.7 ms                                                                        | 48.6 ms: 1.08x faster                                                         |
| xml_etree_iterparse  | 70.1 ms                                                                        | 67.1 ms: 1.04x faster                                                         |
| json_loads           | 20.7 us                                                                        | 20.5 us: 1.01x faster                                                         |
| Geometric mean       | (ref)                                                                          | 1.08x faster                                                                  |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240702-pythonperf1_win32-x86-python-6343486eb60ac5a9e154-3.14.0a0-6343486 | bm-20240702-pythonperf1_win32-x86-Fidget%2dSpinner-macro_ify-3.14.0a0-2302696 |
|-----------------|:------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| genshi_xml      | 54.5 ms                                                                        | 47.6 ms: 1.15x faster                                                         |
| mako            | 9.07 ms                                                                        | 8.10 ms: 1.12x faster                                                         |
| genshi_text     | 24.5 ms                                                                        | 22.0 ms: 1.11x faster                                                         |
| django_template | 36.5 ms                                                                        | 34.0 ms: 1.07x faster                                                         |
| Geometric mean  | (ref)                                                                          | 1.11x faster                                                                  |

All benchmarks:
===============

| Benchmark                  | bm-20240702-pythonperf1_win32-x86-python-6343486eb60ac5a9e154-3.14.0a0-6343486 | bm-20240702-pythonperf1_win32-x86-Fidget%2dSpinner-macro_ify-3.14.0a0-2302696 |
|----------------------------|:------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| scimark_fft                | 263 ms                                                                         | 217 ms: 1.21x faster                                                          |
| deepcopy_memo              | 26.2 us                                                                        | 21.6 us: 1.21x faster                                                         |
| pickle_pure_python         | 286 us                                                                         | 245 us: 1.17x faster                                                          |
| richards                   | 41.2 ms                                                                        | 35.4 ms: 1.16x faster                                                         |
| unpickle_pure_python       | 198 us                                                                         | 171 us: 1.16x faster                                                          |
| scimark_sparse_mat_mult    | 3.60 ms                                                                        | 3.12 ms: 1.15x faster                                                         |
| genshi_xml                 | 54.5 ms                                                                        | 47.6 ms: 1.15x faster                                                         |
| richards_super             | 45.9 ms                                                                        | 40.1 ms: 1.14x faster                                                         |
| chaos                      | 61.3 ms                                                                        | 53.7 ms: 1.14x faster                                                         |
| tomli_loads                | 2.05 sec                                                                       | 1.82 sec: 1.13x faster                                                        |
| go                         | 129 ms                                                                         | 115 ms: 1.13x faster                                                          |
| deepcopy_reduce            | 2.89 us                                                                        | 2.57 us: 1.12x faster                                                         |
| scimark_monte_carlo        | 59.6 ms                                                                        | 53.1 ms: 1.12x faster                                                         |
| deepcopy                   | 280 us                                                                         | 249 us: 1.12x faster                                                          |
| hexiom                     | 5.71 ms                                                                        | 5.09 ms: 1.12x faster                                                         |
| mako                       | 9.07 ms                                                                        | 8.10 ms: 1.12x faster                                                         |
| scimark_sor                | 109 ms                                                                         | 97.2 ms: 1.12x faster                                                         |
| async_tree_none_tg         | 213 ms                                                                         | 190 ms: 1.12x faster                                                          |
| nbody                      | 105 ms                                                                         | 93.6 ms: 1.12x faster                                                         |
| genshi_text                | 24.5 ms                                                                        | 22.0 ms: 1.11x faster                                                         |
| crypto_pyaes               | 64.3 ms                                                                        | 58.2 ms: 1.11x faster                                                         |
| regex_compile              | 117 ms                                                                         | 106 ms: 1.10x faster                                                          |
| pycparser                  | 923 ms                                                                         | 838 ms: 1.10x faster                                                          |
| sqlglot_transpile          | 1.44 ms                                                                        | 1.31 ms: 1.10x faster                                                         |
| sqlglot_parse              | 1.17 ms                                                                        | 1.07 ms: 1.10x faster                                                         |
| async_tree_memoization_tg  | 265 ms                                                                         | 242 ms: 1.10x faster                                                          |
| async_generators           | 320 ms                                                                         | 292 ms: 1.09x faster                                                          |
| xml_etree_generate         | 72.2 ms                                                                        | 66.0 ms: 1.09x faster                                                         |
| async_tree_io_tg           | 541 ms                                                                         | 495 ms: 1.09x faster                                                          |
| raytrace                   | 247 ms                                                                         | 226 ms: 1.09x faster                                                          |
| comprehensions             | 15.3 us                                                                        | 14.0 us: 1.09x faster                                                         |
| logging_silent             | 82.0 ns                                                                        | 75.1 ns: 1.09x faster                                                         |
| scimark_lu                 | 75.0 ms                                                                        | 68.7 ms: 1.09x faster                                                         |
| pyflate                    | 372 ms                                                                         | 342 ms: 1.09x faster                                                          |
| deltablue                  | 2.87 ms                                                                        | 2.64 ms: 1.09x faster                                                         |
| pprint_safe_repr           | 710 ms                                                                         | 653 ms: 1.09x faster                                                          |
| async_tree_none            | 242 ms                                                                         | 223 ms: 1.09x faster                                                          |
| json_dumps                 | 7.91 ms                                                                        | 7.29 ms: 1.08x faster                                                         |
| async_tree_memoization     | 294 ms                                                                         | 272 ms: 1.08x faster                                                          |
| float                      | 66.0 ms                                                                        | 60.9 ms: 1.08x faster                                                         |
| xml_etree_process          | 52.7 ms                                                                        | 48.6 ms: 1.08x faster                                                         |
| pprint_pformat             | 1.46 sec                                                                       | 1.35 sec: 1.08x faster                                                        |
| typing_runtime_protocols   | 165 us                                                                         | 153 us: 1.08x faster                                                          |
| async_tree_io              | 581 ms                                                                         | 539 ms: 1.08x faster                                                          |
| telco                      | 6.68 ms                                                                        | 6.23 ms: 1.07x faster                                                         |
| django_template            | 36.5 ms                                                                        | 34.0 ms: 1.07x faster                                                         |
| sympy_sum                  | 116 ms                                                                         | 109 ms: 1.07x faster                                                          |
| sympy_str                  | 231 ms                                                                         | 218 ms: 1.06x faster                                                          |
| sympy_integrate            | 16.3 ms                                                                        | 15.4 ms: 1.06x faster                                                         |
| fannkuch                   | 340 ms                                                                         | 320 ms: 1.06x faster                                                          |
| sympy_expand               | 405 ms                                                                         | 382 ms: 1.06x faster                                                          |
| logging_format             | 9.26 us                                                                        | 8.75 us: 1.06x faster                                                         |
| generators                 | 28.8 ms                                                                        | 27.3 ms: 1.05x faster                                                         |
| logging_simple             | 8.47 us                                                                        | 8.04 us: 1.05x faster                                                         |
| 2to3                       | 265 ms                                                                         | 253 ms: 1.05x faster                                                          |
| spectral_norm              | 80.1 ms                                                                        | 76.4 ms: 1.05x faster                                                         |
| sqlglot_normalize          | 238 ms                                                                         | 228 ms: 1.05x faster                                                          |
| pylint                     | 238 ms                                                                         | 227 ms: 1.05x faster                                                          |
| xml_etree_iterparse        | 70.1 ms                                                                        | 67.1 ms: 1.04x faster                                                         |
| sqlglot_optimize           | 45.8 ms                                                                        | 44.0 ms: 1.04x faster                                                         |
| coverage                   | 53.6 ms                                                                        | 51.5 ms: 1.04x faster                                                         |
| meteor_contest             | 82.8 ms                                                                        | 79.4 ms: 1.04x faster                                                         |
| coroutines                 | 18.0 ms                                                                        | 17.3 ms: 1.04x faster                                                         |
| mdp                        | 1.74 sec                                                                       | 1.67 sec: 1.04x faster                                                        |
| docutils                   | 1.96 sec                                                                       | 1.89 sec: 1.04x faster                                                        |
| async_tree_cpu_io_mixed    | 487 ms                                                                         | 470 ms: 1.04x faster                                                          |
| tornado_http               | 98.5 ms                                                                        | 95.2 ms: 1.04x faster                                                         |
| thrift                     | 788 us                                                                         | 763 us: 1.03x faster                                                          |
| json                       | 4.37 ms                                                                        | 4.24 ms: 1.03x faster                                                         |
| html5lib                   | 50.7 ms                                                                        | 49.9 ms: 1.02x faster                                                         |
| async_tree_cpu_io_mixed_tg | 465 ms                                                                         | 459 ms: 1.01x faster                                                          |
| nqueens                    | 78.8 ms                                                                        | 77.8 ms: 1.01x faster                                                         |
| bench_mp_pool              | 71.4 ms                                                                        | 70.5 ms: 1.01x faster                                                         |
| json_loads                 | 20.7 us                                                                        | 20.5 us: 1.01x faster                                                         |
| regex_v8                   | 16.1 ms                                                                        | 16.3 ms: 1.01x slower                                                         |
| regex_dna                  | 122 ms                                                                         | 124 ms: 1.01x slower                                                          |
| regex_effbot               | 1.88 ms                                                                        | 1.92 ms: 1.02x slower                                                         |
| Geometric mean             | (ref)                                                                          | 1.07x faster                                                                  |

Benchmark hidden because not significant (10): asyncio_tcp, bench_thread_pool, python_startup_no_site, create_gc_cycles, pidigits, pathlib, asyncio_tcp_ssl, python_startup, xml_etree_parse, gc_traversal

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: unknown