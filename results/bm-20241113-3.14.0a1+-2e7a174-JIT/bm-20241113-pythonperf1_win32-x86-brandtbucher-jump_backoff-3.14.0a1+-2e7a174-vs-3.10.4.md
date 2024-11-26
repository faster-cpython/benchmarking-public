# Results vs. 3.10.4

- fork: brandtbucher
- ref: jump_backoff
- machine: windows-x86
- commit hash: 2e7a174
- commit date: 2024-11-13
- overall geometric mean: 1.046x faster
- HPT reliability: 54.26%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241113-pythonperf1_win32-x86-brandtbucher-jump_backoff-3.14.0a1+-2e7a174 |
|----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 267 ms: 1.01x slower                                                          |
| docutils       | 1.95 sec                                                        | 2.08 sec: 1.07x slower                                                        |
| html5lib       | 52.1 ms                                                         | 48.9 ms: 1.07x faster                                                         |
| Geometric mean | (ref)                                                           | 1.00x slower                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241113-pythonperf1_win32-x86-brandtbucher-jump_backoff-3.14.0a1+-2e7a174 |
|-------------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 487 ms: 1.89x faster                                                          |
| async_tree_io           | 940 ms                                                          | 559 ms: 1.68x faster                                                          |
| async_tree_none         | 394 ms                                                          | 244 ms: 1.61x faster                                                          |
| async_tree_memoization  | 467 ms                                                          | 298 ms: 1.57x faster                                                          |
| Geometric mean          | (ref)                                                           | 1.68x faster                                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241113-pythonperf1_win32-x86-brandtbucher-jump_backoff-3.14.0a1+-2e7a174 |
|----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 203 ms: 2.48x faster                                                          |
| float          | 69.6 ms                                                         | 55.6 ms: 1.25x faster                                                         |
| nbody          | 79.1 ms                                                         | 100 ms: 1.27x slower                                                          |
| Geometric mean | (ref)                                                           | 1.35x faster                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241113-pythonperf1_win32-x86-brandtbucher-jump_backoff-3.14.0a1+-2e7a174 |
|----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_dna      | 131 ms                                                          | 116 ms: 1.13x faster                                                          |
| regex_v8       | 15.8 ms                                                         | 16.1 ms: 1.02x slower                                                         |
| regex_effbot   | 1.66 ms                                                         | 1.83 ms: 1.10x slower                                                         |
| Geometric mean | (ref)                                                           | 1.00x faster                                                                  |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241113-pythonperf1_win32-x86-brandtbucher-jump_backoff-3.14.0a1+-2e7a174 |
|----------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 8.79 ms: 1.12x faster                                                         |
| json_loads           | 22.4 us                                                         | 20.7 us: 1.08x faster                                                         |
| xml_etree_parse      | 120 ms                                                          | 112 ms: 1.07x faster                                                          |
| xml_etree_iterparse  | 70.8 ms                                                         | 68.0 ms: 1.04x faster                                                         |
| tomli_loads          | 1.91 sec                                                        | 1.85 sec: 1.03x faster                                                        |
| pickle_pure_python   | 280 us                                                          | 302 us: 1.08x slower                                                          |
| unpickle_pure_python | 189 us                                                          | 208 us: 1.10x slower                                                          |
| xml_etree_process    | 48.1 ms                                                         | 53.9 ms: 1.12x slower                                                         |
| xml_etree_generate   | 61.6 ms                                                         | 73.3 ms: 1.19x slower                                                         |
| Geometric mean       | (ref)                                                           | 1.01x slower                                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241113-pythonperf1_win32-x86-brandtbucher-jump_backoff-3.14.0a1+-2e7a174 |
|------------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 19.2 ms: 1.06x slower                                                         |
| python_startup         | 22.9 ms                                                         | 25.5 ms: 1.11x slower                                                         |
| Geometric mean         | (ref)                                                           | 1.09x slower                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241113-pythonperf1_win32-x86-brandtbucher-jump_backoff-3.14.0a1+-2e7a174 |
|----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mako           | 9.10 ms                                                         | 7.37 ms: 1.23x faster                                                         |
| genshi_xml     | 46.6 ms                                                         | 56.5 ms: 1.21x slower                                                         |
| genshi_text    | 21.0 ms                                                         | 25.8 ms: 1.23x slower                                                         |
| Geometric mean | (ref)                                                           | 1.05x slower                                                                  |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241113-pythonperf1_win32-x86-brandtbucher-jump_backoff-3.14.0a1+-2e7a174 |
|--------------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| pidigits                 | 502 ms                                                          | 203 ms: 2.48x faster                                                          |
| typing_runtime_protocols | 396 us                                                          | 168 us: 2.36x faster                                                          |
| sqlglot_normalize        | 230 ms                                                          | 110 ms: 2.09x faster                                                          |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 487 ms: 1.89x faster                                                          |
| async_tree_io            | 940 ms                                                          | 559 ms: 1.68x faster                                                          |
| async_tree_none          | 394 ms                                                          | 244 ms: 1.61x faster                                                          |
| async_tree_memoization   | 467 ms                                                          | 298 ms: 1.57x faster                                                          |
| pylint                   | 384 ms                                                          | 258 ms: 1.49x faster                                                          |
| deepcopy_memo            | 29.6 us                                                         | 23.1 us: 1.28x faster                                                         |
| float                    | 69.6 ms                                                         | 55.6 ms: 1.25x faster                                                         |
| deltablue                | 4.04 ms                                                         | 3.23 ms: 1.25x faster                                                         |
| mako                     | 9.10 ms                                                         | 7.37 ms: 1.23x faster                                                         |
| crypto_pyaes             | 81.3 ms                                                         | 65.9 ms: 1.23x faster                                                         |
| dulwich_log              | 58.5 ms                                                         | 49.5 ms: 1.18x faster                                                         |
| scimark_lu               | 89.8 ms                                                         | 75.9 ms: 1.18x faster                                                         |
| thrift                   | 902 us                                                          | 776 us: 1.16x faster                                                          |
| go                       | 146 ms                                                          | 125 ms: 1.16x faster                                                          |
| sqlite_synth             | 2.29 us                                                         | 2.01 us: 1.14x faster                                                         |
| chaos                    | 74.4 ms                                                         | 65.3 ms: 1.14x faster                                                         |
| logging_silent           | 97.9 ns                                                         | 86.0 ns: 1.14x faster                                                         |
| scimark_sor              | 115 ms                                                          | 101 ms: 1.14x faster                                                          |
| pycparser                | 1.04 sec                                                        | 922 ms: 1.13x faster                                                          |
| regex_dna                | 131 ms                                                          | 116 ms: 1.13x faster                                                          |
| sqlglot_parse            | 1.33 ms                                                         | 1.18 ms: 1.12x faster                                                         |
| deepcopy                 | 310 us                                                          | 277 us: 1.12x faster                                                          |
| json_dumps               | 9.82 ms                                                         | 8.79 ms: 1.12x faster                                                         |
| json                     | 4.76 ms                                                         | 4.39 ms: 1.08x faster                                                         |
| json_loads               | 22.4 us                                                         | 20.7 us: 1.08x faster                                                         |
| bench_thread_pool        | 1.12 ms                                                         | 1.03 ms: 1.08x faster                                                         |
| sqlglot_transpile        | 1.58 ms                                                         | 1.47 ms: 1.07x faster                                                         |
| coroutines               | 17.9 ms                                                         | 16.7 ms: 1.07x faster                                                         |
| xml_etree_parse          | 120 ms                                                          | 112 ms: 1.07x faster                                                          |
| html5lib                 | 52.1 ms                                                         | 48.9 ms: 1.07x faster                                                         |
| sympy_sum                | 122 ms                                                          | 117 ms: 1.05x faster                                                          |
| pyflate                  | 422 ms                                                          | 404 ms: 1.04x faster                                                          |
| xml_etree_iterparse      | 70.8 ms                                                         | 68.0 ms: 1.04x faster                                                         |
| tomli_loads              | 1.91 sec                                                        | 1.85 sec: 1.03x faster                                                        |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 3.19 ms: 1.02x faster                                                         |
| richards_super           | 49.9 ms                                                         | 49.4 ms: 1.01x faster                                                         |
| 2to3                     | 265 ms                                                          | 267 ms: 1.01x slower                                                          |
| raytrace                 | 303 ms                                                          | 308 ms: 1.02x slower                                                          |
| pathlib                  | 81.2 ms                                                         | 82.6 ms: 1.02x slower                                                         |
| comprehensions           | 17.7 us                                                         | 18.2 us: 1.02x slower                                                         |
| regex_v8                 | 15.8 ms                                                         | 16.1 ms: 1.02x slower                                                         |
| deepcopy_reduce          | 2.68 us                                                         | 2.82 us: 1.05x slower                                                         |
| spectral_norm            | 80.2 ms                                                         | 84.3 ms: 1.05x slower                                                         |
| sympy_integrate          | 16.6 ms                                                         | 17.6 ms: 1.06x slower                                                         |
| python_startup_no_site   | 18.1 ms                                                         | 19.2 ms: 1.06x slower                                                         |
| sympy_str                | 229 ms                                                          | 243 ms: 1.06x slower                                                          |
| fannkuch                 | 317 ms                                                          | 338 ms: 1.06x slower                                                          |
| docutils                 | 1.95 sec                                                        | 2.08 sec: 1.07x slower                                                        |
| mdp                      | 1.83 sec                                                        | 1.95 sec: 1.07x slower                                                        |
| richards                 | 40.3 ms                                                         | 43.1 ms: 1.07x slower                                                         |
| pickle_pure_python       | 280 us                                                          | 302 us: 1.08x slower                                                          |
| sympy_expand             | 391 ms                                                          | 424 ms: 1.08x slower                                                          |
| unpickle_pure_python     | 189 us                                                          | 208 us: 1.10x slower                                                          |
| regex_effbot             | 1.66 ms                                                         | 1.83 ms: 1.10x slower                                                         |
| coverage                 | 46.6 ms                                                         | 51.7 ms: 1.11x slower                                                         |
| python_startup           | 22.9 ms                                                         | 25.5 ms: 1.11x slower                                                         |
| pprint_pformat           | 1.37 sec                                                        | 1.52 sec: 1.11x slower                                                        |
| xml_etree_process        | 48.1 ms                                                         | 53.9 ms: 1.12x slower                                                         |
| nqueens                  | 87.1 ms                                                         | 97.8 ms: 1.12x slower                                                         |
| meteor_contest           | 80.0 ms                                                         | 89.8 ms: 1.12x slower                                                         |
| pprint_safe_repr         | 658 ms                                                          | 740 ms: 1.12x slower                                                          |
| generators               | 31.6 ms                                                         | 35.6 ms: 1.13x slower                                                         |
| scimark_fft              | 216 ms                                                          | 244 ms: 1.13x slower                                                          |
| logging_format           | 7.91 us                                                         | 9.04 us: 1.14x slower                                                         |
| logging_simple           | 7.29 us                                                         | 8.39 us: 1.15x slower                                                         |
| sqlglot_optimize         | 44.7 ms                                                         | 51.5 ms: 1.15x slower                                                         |
| hexiom                   | 6.13 ms                                                         | 7.21 ms: 1.18x slower                                                         |
| xml_etree_generate       | 61.6 ms                                                         | 73.3 ms: 1.19x slower                                                         |
| genshi_xml               | 46.6 ms                                                         | 56.5 ms: 1.21x slower                                                         |
| genshi_text              | 21.0 ms                                                         | 25.8 ms: 1.23x slower                                                         |
| nbody                    | 79.1 ms                                                         | 100 ms: 1.27x slower                                                          |
| bench_mp_pool            | 66.4 ms                                                         | 86.3 ms: 1.30x slower                                                         |
| async_generators         | 241 ms                                                          | 324 ms: 1.34x slower                                                          |
| gc_traversal             | 1.28 ms                                                         | 1.78 ms: 1.39x slower                                                         |
| telco                    | 4.83 ms                                                         | 7.18 ms: 1.49x slower                                                         |
| create_gc_cycles         | 694 us                                                          | 1.16 ms: 1.67x slower                                                         |
| Geometric mean           | (ref)                                                           | 1.04x faster                                                                  |

Benchmark hidden because not significant (3): regex_compile, django_template, scimark_monte_carlo
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (10) of results/bm-20241113-3.14.0a1+-2e7a174-JIT/bm-20241113-pythonperf1_win32-x86-brandtbucher-jump_backoff-3.14.0a1+-2e7a174.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, shortest_path, sphinx

- Geometric mean (including insignificant results): 1.046x faster
# HPT report

- Reliability score: 54.26% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown