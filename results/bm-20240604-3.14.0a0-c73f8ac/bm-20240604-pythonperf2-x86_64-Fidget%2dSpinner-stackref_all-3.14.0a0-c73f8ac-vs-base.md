# Results vs. base

- fork: Fidget-Spinner
- ref: stackref_all
- machine: linux-x86_64
- commit hash: c73f8ac
- commit date: 2024-06-04
- overall geometric mean: 1.01x slower
- HPT reliability: 99.99%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240603-pythonperf2-x86_64-python-31a4fb3c74a028443634-3.14.0a0-31a4fb3 | bm-20240604-pythonperf2-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-c73f8ac |
|----------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 303 ms                                                                      | 308 ms: 1.02x slower                                                          |
| docutils       | 3.11 sec                                                                    | 3.14 sec: 1.01x slower                                                        |
| html5lib       | 72.1 ms                                                                     | 74.6 ms: 1.03x slower                                                         |
| Geometric mean | (ref)                                                                       | 1.01x slower                                                                  |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (8): async_tree_none_tg, async_tree_none, async_tree_io_tg, async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_cpu_io_mixed, async_tree_memoization_tg, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240603-pythonperf2-x86_64-python-31a4fb3c74a028443634-3.14.0a0-31a4fb3 | bm-20240604-pythonperf2-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-c73f8ac |
|----------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| pidigits       | 250 ms                                                                      | 251 ms: 1.00x slower                                                          |
| float          | 74.2 ms                                                                     | 75.0 ms: 1.01x slower                                                         |
| nbody          | 82.8 ms                                                                     | 84.3 ms: 1.02x slower                                                         |
| Geometric mean | (ref)                                                                       | 1.01x slower                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240603-pythonperf2-x86_64-python-31a4fb3c74a028443634-3.14.0a0-31a4fb3 | bm-20240604-pythonperf2-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-c73f8ac |
|----------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_dna      | 252 ms                                                                      | 245 ms: 1.03x faster                                                          |
| regex_v8       | 26.1 ms                                                                     | 25.6 ms: 1.02x faster                                                         |
| regex_effbot   | 3.46 ms                                                                     | 3.43 ms: 1.01x faster                                                         |
| regex_compile  | 138 ms                                                                      | 141 ms: 1.02x slower                                                          |
| Geometric mean | (ref)                                                                       | 1.01x faster                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240603-pythonperf2-x86_64-python-31a4fb3c74a028443634-3.14.0a0-31a4fb3 | bm-20240604-pythonperf2-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-c73f8ac |
|----------------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| pickle_list          | 4.51 us                                                                     | 4.42 us: 1.02x faster                                                         |
| xml_etree_parse      | 147 ms                                                                      | 144 ms: 1.02x faster                                                          |
| pickle_dict          | 32.2 us                                                                     | 31.6 us: 1.02x faster                                                         |
| pickle               | 10.7 us                                                                     | 10.5 us: 1.01x faster                                                         |
| json_dumps           | 10.8 ms                                                                     | 10.7 ms: 1.01x faster                                                         |
| xml_etree_generate   | 82.0 ms                                                                     | 81.5 ms: 1.01x faster                                                         |
| xml_etree_process    | 58.6 ms                                                                     | 58.3 ms: 1.01x faster                                                         |
| tomli_loads          | 2.07 sec                                                                    | 2.10 sec: 1.01x slower                                                        |
| unpickle_pure_python | 219 us                                                                      | 224 us: 1.03x slower                                                          |
| unpickle             | 15.2 us                                                                     | 15.7 us: 1.03x slower                                                         |
| pickle_pure_python   | 314 us                                                                      | 326 us: 1.04x slower                                                          |
| Geometric mean       | (ref)                                                                       | 1.00x slower                                                                  |

Benchmark hidden because not significant (3): unpickle_list, xml_etree_iterparse, json_loads

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240603-pythonperf2-x86_64-python-31a4fb3c74a028443634-3.14.0a0-31a4fb3 | bm-20240604-pythonperf2-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-c73f8ac |
|-----------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mako            | 9.15 ms                                                                     | 9.27 ms: 1.01x slower                                                         |
| genshi_text     | 27.8 ms                                                                     | 28.8 ms: 1.04x slower                                                         |
| django_template | 41.1 ms                                                                     | 43.0 ms: 1.05x slower                                                         |
| genshi_xml      | 62.0 ms                                                                     | 67.0 ms: 1.08x slower                                                         |
| Geometric mean  | (ref)                                                                       | 1.04x slower                                                                  |

All benchmarks:
===============

| Benchmark                | bm-20240603-pythonperf2-x86_64-python-31a4fb3c74a028443634-3.14.0a0-31a4fb3 | bm-20240604-pythonperf2-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-c73f8ac |
|--------------------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| gc_traversal             | 4.91 ms                                                                     | 4.47 ms: 1.10x faster                                                         |
| raytrace                 | 294 ms                                                                      | 285 ms: 1.03x faster                                                          |
| regex_dna                | 252 ms                                                                      | 245 ms: 1.03x faster                                                          |
| pickle_list              | 4.51 us                                                                     | 4.42 us: 1.02x faster                                                         |
| xml_etree_parse          | 147 ms                                                                      | 144 ms: 1.02x faster                                                          |
| typing_runtime_protocols | 189 us                                                                      | 185 us: 1.02x faster                                                          |
| pickle_dict              | 32.2 us                                                                     | 31.6 us: 1.02x faster                                                         |
| create_gc_cycles         | 1.95 ms                                                                     | 1.91 ms: 1.02x faster                                                         |
| regex_v8                 | 26.1 ms                                                                     | 25.6 ms: 1.02x faster                                                         |
| coverage                 | 81.6 ms                                                                     | 80.3 ms: 1.02x faster                                                         |
| logging_silent           | 110 ns                                                                      | 109 ns: 1.01x faster                                                          |
| pickle                   | 10.7 us                                                                     | 10.5 us: 1.01x faster                                                         |
| regex_effbot             | 3.46 ms                                                                     | 3.43 ms: 1.01x faster                                                         |
| json_dumps               | 10.8 ms                                                                     | 10.7 ms: 1.01x faster                                                         |
| meteor_contest           | 130 ms                                                                      | 129 ms: 1.01x faster                                                          |
| xml_etree_generate       | 82.0 ms                                                                     | 81.5 ms: 1.01x faster                                                         |
| xml_etree_process        | 58.6 ms                                                                     | 58.3 ms: 1.01x faster                                                         |
| generators               | 34.5 ms                                                                     | 34.3 ms: 1.00x faster                                                         |
| pidigits                 | 250 ms                                                                      | 251 ms: 1.00x slower                                                          |
| telco                    | 8.23 ms                                                                     | 8.27 ms: 1.01x slower                                                         |
| sqlglot_parse            | 1.41 ms                                                                     | 1.42 ms: 1.01x slower                                                         |
| chaos                    | 65.6 ms                                                                     | 66.0 ms: 1.01x slower                                                         |
| asyncio_tcp              | 379 ms                                                                      | 381 ms: 1.01x slower                                                          |
| mdp                      | 2.56 sec                                                                    | 2.59 sec: 1.01x slower                                                        |
| dulwich_log              | 65.7 ms                                                                     | 66.3 ms: 1.01x slower                                                         |
| docutils                 | 3.11 sec                                                                    | 3.14 sec: 1.01x slower                                                        |
| float                    | 74.2 ms                                                                     | 75.0 ms: 1.01x slower                                                         |
| sqlglot_transpile        | 1.82 ms                                                                     | 1.84 ms: 1.01x slower                                                         |
| pathlib                  | 16.2 ms                                                                     | 16.5 ms: 1.01x slower                                                         |
| tomli_loads              | 2.07 sec                                                                    | 2.10 sec: 1.01x slower                                                        |
| mako                     | 9.15 ms                                                                     | 9.27 ms: 1.01x slower                                                         |
| sympy_expand             | 531 ms                                                                      | 538 ms: 1.01x slower                                                          |
| sqlglot_normalize        | 128 ms                                                                      | 129 ms: 1.01x slower                                                          |
| pprint_pformat           | 1.61 sec                                                                    | 1.63 sec: 1.01x slower                                                        |
| async_generators         | 386 ms                                                                      | 392 ms: 1.01x slower                                                          |
| sympy_integrate          | 25.5 ms                                                                     | 25.8 ms: 1.01x slower                                                         |
| 2to3                     | 303 ms                                                                      | 308 ms: 1.02x slower                                                          |
| pyflate                  | 447 ms                                                                      | 454 ms: 1.02x slower                                                          |
| nbody                    | 82.8 ms                                                                     | 84.3 ms: 1.02x slower                                                         |
| sympy_sum                | 165 ms                                                                      | 168 ms: 1.02x slower                                                          |
| sqlglot_optimize         | 63.0 ms                                                                     | 64.2 ms: 1.02x slower                                                         |
| sympy_str                | 311 ms                                                                      | 316 ms: 1.02x slower                                                          |
| regex_compile            | 138 ms                                                                      | 141 ms: 1.02x slower                                                          |
| scimark_sor              | 131 ms                                                                      | 134 ms: 1.02x slower                                                          |
| unpickle_pure_python     | 219 us                                                                      | 224 us: 1.03x slower                                                          |
| crypto_pyaes             | 70.5 ms                                                                     | 72.4 ms: 1.03x slower                                                         |
| scimark_monte_carlo      | 67.3 ms                                                                     | 69.1 ms: 1.03x slower                                                         |
| scimark_lu               | 119 ms                                                                      | 122 ms: 1.03x slower                                                          |
| richards_super           | 51.8 ms                                                                     | 53.3 ms: 1.03x slower                                                         |
| coroutines               | 21.3 ms                                                                     | 22.0 ms: 1.03x slower                                                         |
| unpickle                 | 15.2 us                                                                     | 15.7 us: 1.03x slower                                                         |
| deepcopy_reduce          | 3.61 us                                                                     | 3.73 us: 1.03x slower                                                         |
| pycparser                | 1.23 sec                                                                    | 1.27 sec: 1.03x slower                                                        |
| go                       | 158 ms                                                                      | 163 ms: 1.03x slower                                                          |
| richards                 | 44.2 ms                                                                     | 45.7 ms: 1.03x slower                                                         |
| nqueens                  | 95.4 ms                                                                     | 98.7 ms: 1.03x slower                                                         |
| deepcopy                 | 409 us                                                                      | 423 us: 1.03x slower                                                          |
| fannkuch                 | 343 ms                                                                      | 355 ms: 1.03x slower                                                          |
| html5lib                 | 72.1 ms                                                                     | 74.6 ms: 1.03x slower                                                         |
| deepcopy_memo            | 36.3 us                                                                     | 37.6 us: 1.04x slower                                                         |
| pickle_pure_python       | 314 us                                                                      | 326 us: 1.04x slower                                                          |
| genshi_text              | 27.8 ms                                                                     | 28.8 ms: 1.04x slower                                                         |
| comprehensions           | 17.7 us                                                                     | 18.4 us: 1.04x slower                                                         |
| hexiom                   | 6.66 ms                                                                     | 6.96 ms: 1.04x slower                                                         |
| django_template          | 41.1 ms                                                                     | 43.0 ms: 1.05x slower                                                         |
| scimark_sparse_mat_mult  | 4.00 ms                                                                     | 4.20 ms: 1.05x slower                                                         |
| genshi_xml               | 62.0 ms                                                                     | 67.0 ms: 1.08x slower                                                         |
| Geometric mean           | (ref)                                                                       | 1.01x slower                                                                  |

Benchmark hidden because not significant (29): async_tree_none_tg, async_tree_none, async_tree_io_tg, pprint_safe_repr, async_tree_cpu_io_mixed_tg, async_tree_io, spectral_norm, scimark_fft, unpickle_list, asyncio_tcp_ssl, python_startup, xml_etree_iterparse, python_startup_no_site, tornado_http, async_tree_cpu_io_mixed, async_tree_memoization_tg, logging_simple, deltablue, json_loads, async_tree_memoization, asyncio_websockets, json, thrift, sqlite_synth, logging_format, bench_mp_pool, dask, bench_thread_pool, pylint

# HPT report

- Reliability score: 99.99% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x