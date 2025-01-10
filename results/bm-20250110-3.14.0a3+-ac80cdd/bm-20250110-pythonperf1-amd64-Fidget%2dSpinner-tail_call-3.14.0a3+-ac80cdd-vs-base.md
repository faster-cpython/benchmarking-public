# Results vs. base

- fork: Fidget-Spinner
- ref: tail_call
- machine: windows-amd64
- commit hash: ac80cdd
- commit date: 2025-01-10
- overall geometric mean: 1.012x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250105-pythonperf1-amd64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250110-pythonperf1-amd64-Fidget%2dSpinner-tail_call-3.14.0a3+-ac80cdd |
|----------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 228 ms                                                                      | 231 ms: 1.01x slower                                                       |
| docutils       | 1.69 sec                                                                    | 1.71 sec: 1.01x slower                                                     |
| html5lib       | 39.8 ms                                                                     | 41.1 ms: 1.03x slower                                                      |
| sphinx         | 651 ms                                                                      | 662 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                                       | 1.02x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250105-pythonperf1-amd64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250110-pythonperf1-amd64-Fidget%2dSpinner-tail_call-3.14.0a3+-ac80cdd |
|----------------------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| coroutines                 | 14.0 ms                                                                     | 13.5 ms: 1.04x faster                                                      |
| async_generators           | 241 ms                                                                      | 236 ms: 1.02x faster                                                       |
| asyncio_websockets         | 315 ms                                                                      | 310 ms: 1.01x faster                                                       |
| async_tree_io              | 417 ms                                                                      | 421 ms: 1.01x slower                                                       |
| async_tree_cpu_io_mixed_tg | 345 ms                                                                      | 350 ms: 1.01x slower                                                       |
| async_tree_cpu_io_mixed    | 347 ms                                                                      | 354 ms: 1.02x slower                                                       |
| async_tree_none            | 184 ms                                                                      | 189 ms: 1.02x slower                                                       |
| async_tree_io_tg           | 399 ms                                                                      | 412 ms: 1.03x slower                                                       |
| async_tree_memoization_tg  | 209 ms                                                                      | 216 ms: 1.03x slower                                                       |
| async_tree_none_tg         | 168 ms                                                                      | 177 ms: 1.05x slower                                                       |
| async_tree_memoization     | 221 ms                                                                      | 233 ms: 1.05x slower                                                       |
| Geometric mean             | (ref)                                                                       | 1.01x slower                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250105-pythonperf1-amd64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250110-pythonperf1-amd64-Fidget%2dSpinner-tail_call-3.14.0a3+-ac80cdd |
|----------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 78.7 ms                                                                     | 79.7 ms: 1.01x slower                                                      |
| float          | 52.2 ms                                                                     | 53.0 ms: 1.02x slower                                                      |
| Geometric mean | (ref)                                                                       | 1.01x slower                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250105-pythonperf1-amd64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250110-pythonperf1-amd64-Fidget%2dSpinner-tail_call-3.14.0a3+-ac80cdd |
|----------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 88.1 ms                                                                     | 89.7 ms: 1.02x slower                                                      |
| regex_effbot   | 1.41 ms                                                                     | 1.48 ms: 1.05x slower                                                      |
| regex_dna      | 114 ms                                                                      | 122 ms: 1.07x slower                                                       |
| regex_v8       | 19.3 ms                                                                     | 24.6 ms: 1.28x slower                                                      |
| Geometric mean | (ref)                                                                       | 1.10x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250105-pythonperf1-amd64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250110-pythonperf1-amd64-Fidget%2dSpinner-tail_call-3.14.0a3+-ac80cdd |
|----------------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| unpickle_pure_python | 157 us                                                                      | 153 us: 1.02x faster                                                       |
| xml_etree_generate   | 58.8 ms                                                                     | 58.1 ms: 1.01x faster                                                      |
| xml_etree_parse      | 90.9 ms                                                                     | 89.9 ms: 1.01x faster                                                      |
| xml_etree_process    | 41.8 ms                                                                     | 41.5 ms: 1.01x faster                                                      |
| xml_etree_iterparse  | 64.2 ms                                                                     | 63.8 ms: 1.01x faster                                                      |
| tomli_loads          | 1.45 sec                                                                    | 1.47 sec: 1.01x slower                                                     |
| json_dumps           | 6.71 ms                                                                     | 6.81 ms: 1.02x slower                                                      |
| pickle_pure_python   | 229 us                                                                      | 234 us: 1.02x slower                                                       |
| Geometric mean       | (ref)                                                                       | 1.00x slower                                                               |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250105-pythonperf1-amd64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250110-pythonperf1-amd64-Fidget%2dSpinner-tail_call-3.14.0a3+-ac80cdd |
|------------------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                                     | 24.6 ms: 1.01x slower                                                      |
| python_startup_no_site | 17.9 ms                                                                     | 18.1 ms: 1.01x slower                                                      |
| Geometric mean         | (ref)                                                                       | 1.01x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250105-pythonperf1-amd64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250110-pythonperf1-amd64-Fidget%2dSpinner-tail_call-3.14.0a3+-ac80cdd |
|-----------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_text     | 16.6 ms                                                                     | 16.8 ms: 1.01x slower                                                      |
| genshi_xml      | 34.7 ms                                                                     | 35.3 ms: 1.02x slower                                                      |
| django_template | 25.1 ms                                                                     | 25.7 ms: 1.02x slower                                                      |
| Geometric mean  | (ref)                                                                       | 1.01x slower                                                               |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20250105-pythonperf1-amd64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250110-pythonperf1-amd64-Fidget%2dSpinner-tail_call-3.14.0a3+-ac80cdd |
|----------------------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mdp                        | 1.53 sec                                                                    | 1.47 sec: 1.04x faster                                                     |
| coroutines                 | 14.0 ms                                                                     | 13.5 ms: 1.04x faster                                                      |
| spectral_norm              | 67.2 ms                                                                     | 65.1 ms: 1.03x faster                                                      |
| scimark_fft                | 199 ms                                                                      | 193 ms: 1.03x faster                                                       |
| telco                      | 4.93 ms                                                                     | 4.81 ms: 1.03x faster                                                      |
| scimark_sparse_mat_mult    | 2.71 ms                                                                     | 2.64 ms: 1.02x faster                                                      |
| unpickle_pure_python       | 157 us                                                                      | 153 us: 1.02x faster                                                       |
| async_generators           | 241 ms                                                                      | 236 ms: 1.02x faster                                                       |
| json                       | 3.09 ms                                                                     | 3.04 ms: 1.02x faster                                                      |
| fannkuch                   | 281 ms                                                                      | 277 ms: 1.02x faster                                                       |
| asyncio_websockets         | 315 ms                                                                      | 310 ms: 1.01x faster                                                       |
| xml_etree_generate         | 58.8 ms                                                                     | 58.1 ms: 1.01x faster                                                      |
| xml_etree_parse            | 90.9 ms                                                                     | 89.9 ms: 1.01x faster                                                      |
| sqlglot_transpile          | 1.14 ms                                                                     | 1.12 ms: 1.01x faster                                                      |
| xml_etree_process          | 41.8 ms                                                                     | 41.5 ms: 1.01x faster                                                      |
| xml_etree_iterparse        | 64.2 ms                                                                     | 63.8 ms: 1.01x faster                                                      |
| sqlite_synth               | 1.62 us                                                                     | 1.61 us: 1.01x faster                                                      |
| scimark_lu                 | 64.7 ms                                                                     | 64.8 ms: 1.00x slower                                                      |
| sympy_expand               | 309 ms                                                                      | 310 ms: 1.00x slower                                                       |
| sqlglot_normalize          | 196 ms                                                                      | 197 ms: 1.00x slower                                                       |
| bench_mp_pool              | 88.9 ms                                                                     | 89.4 ms: 1.01x slower                                                      |
| sympy_str                  | 180 ms                                                                      | 181 ms: 1.01x slower                                                       |
| crypto_pyaes               | 49.6 ms                                                                     | 50.0 ms: 1.01x slower                                                      |
| sympy_integrate            | 13.5 ms                                                                     | 13.7 ms: 1.01x slower                                                      |
| python_startup             | 24.4 ms                                                                     | 24.6 ms: 1.01x slower                                                      |
| docutils                   | 1.69 sec                                                                    | 1.71 sec: 1.01x slower                                                     |
| sqlglot_optimize           | 35.8 ms                                                                     | 36.2 ms: 1.01x slower                                                      |
| async_tree_io              | 417 ms                                                                      | 421 ms: 1.01x slower                                                       |
| python_startup_no_site     | 17.9 ms                                                                     | 18.1 ms: 1.01x slower                                                      |
| genshi_text                | 16.6 ms                                                                     | 16.8 ms: 1.01x slower                                                      |
| 2to3                       | 228 ms                                                                      | 231 ms: 1.01x slower                                                       |
| nbody                      | 78.7 ms                                                                     | 79.7 ms: 1.01x slower                                                      |
| async_tree_cpu_io_mixed_tg | 345 ms                                                                      | 350 ms: 1.01x slower                                                       |
| sympy_sum                  | 90.5 ms                                                                     | 91.7 ms: 1.01x slower                                                      |
| tomli_loads                | 1.45 sec                                                                    | 1.47 sec: 1.01x slower                                                     |
| float                      | 52.2 ms                                                                     | 53.0 ms: 1.02x slower                                                      |
| json_dumps                 | 6.71 ms                                                                     | 6.81 ms: 1.02x slower                                                      |
| thrift                     | 522 us                                                                      | 530 us: 1.02x slower                                                       |
| deepcopy_reduce            | 1.89 us                                                                     | 1.92 us: 1.02x slower                                                      |
| sphinx                     | 651 ms                                                                      | 662 ms: 1.02x slower                                                       |
| regex_compile              | 88.1 ms                                                                     | 89.7 ms: 1.02x slower                                                      |
| genshi_xml                 | 34.7 ms                                                                     | 35.3 ms: 1.02x slower                                                      |
| hexiom                     | 4.61 ms                                                                     | 4.69 ms: 1.02x slower                                                      |
| deepcopy_memo              | 21.5 us                                                                     | 21.9 us: 1.02x slower                                                      |
| pprint_safe_repr           | 541 ms                                                                      | 552 ms: 1.02x slower                                                       |
| async_tree_cpu_io_mixed    | 347 ms                                                                      | 354 ms: 1.02x slower                                                       |
| meteor_contest             | 77.3 ms                                                                     | 78.9 ms: 1.02x slower                                                      |
| generators                 | 21.1 ms                                                                     | 21.6 ms: 1.02x slower                                                      |
| pickle_pure_python         | 229 us                                                                      | 234 us: 1.02x slower                                                       |
| scimark_sor                | 90.8 ms                                                                     | 92.9 ms: 1.02x slower                                                      |
| dulwich_log                | 42.5 ms                                                                     | 43.4 ms: 1.02x slower                                                      |
| async_tree_none            | 184 ms                                                                      | 189 ms: 1.02x slower                                                       |
| django_template            | 25.1 ms                                                                     | 25.7 ms: 1.02x slower                                                      |
| pprint_pformat             | 1.10 sec                                                                    | 1.13 sec: 1.02x slower                                                     |
| many_optionals             | 437 us                                                                      | 451 us: 1.03x slower                                                       |
| async_tree_io_tg           | 399 ms                                                                      | 412 ms: 1.03x slower                                                       |
| async_tree_memoization_tg  | 209 ms                                                                      | 216 ms: 1.03x slower                                                       |
| logging_silent             | 66.8 ns                                                                     | 69.1 ns: 1.03x slower                                                      |
| html5lib                   | 39.8 ms                                                                     | 41.1 ms: 1.03x slower                                                      |
| chaos                      | 44.0 ms                                                                     | 45.6 ms: 1.04x slower                                                      |
| go                         | 90.9 ms                                                                     | 94.3 ms: 1.04x slower                                                      |
| subparsers                 | 16.2 ms                                                                     | 16.8 ms: 1.04x slower                                                      |
| richards_super             | 35.5 ms                                                                     | 36.9 ms: 1.04x slower                                                      |
| logging_format             | 6.77 us                                                                     | 7.07 us: 1.04x slower                                                      |
| scimark_monte_carlo        | 47.9 ms                                                                     | 50.0 ms: 1.05x slower                                                      |
| regex_effbot               | 1.41 ms                                                                     | 1.48 ms: 1.05x slower                                                      |
| richards                   | 31.5 ms                                                                     | 33.1 ms: 1.05x slower                                                      |
| async_tree_none_tg         | 168 ms                                                                      | 177 ms: 1.05x slower                                                       |
| deltablue                  | 2.28 ms                                                                     | 2.40 ms: 1.05x slower                                                      |
| async_tree_memoization     | 221 ms                                                                      | 233 ms: 1.05x slower                                                       |
| logging_simple             | 6.30 us                                                                     | 6.65 us: 1.06x slower                                                      |
| regex_dna                  | 114 ms                                                                      | 122 ms: 1.07x slower                                                       |
| raytrace                   | 195 ms                                                                      | 211 ms: 1.08x slower                                                       |
| regex_v8                   | 19.3 ms                                                                     | 24.6 ms: 1.28x slower                                                      |
| Geometric mean             | (ref)                                                                       | 1.01x slower                                                               |

Benchmark hidden because not significant (20): mako, gc_traversal, pyflate, typing_runtime_protocols, k_core, shortest_path, coverage, comprehensions, pidigits, pathlib, sqlglot_parse, connected_components, nqueens, bpe_tokeniser, create_gc_cycles, pylint, deepcopy, bench_thread_pool, pycparser, json_loads

- Geometric mean (including insignificant results): 1.012x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown