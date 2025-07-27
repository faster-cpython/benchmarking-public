# Results vs. base

- fork: python
- ref: a852c7bdd48979218a0c
- machine: windows-amd64
- commit hash: a852c7b
- commit date: 2025-07-26
- overall geometric mean: 1.033x faster
- HPT reliability: 99.98%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250726-3.15.0a0-a852c7b/bm-20250726-pythonperf1-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b.json | results/bm-20250726-3.15.0a0-a852c7b-JIT/bm-20250726-pythonperf1-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| docutils       | 1.64 sec                                                                                                             | 1.69 sec: 1.03x slower                                                                                                   |
| html5lib       | 39.3 ms                                                                                                              | 38.3 ms: 1.02x faster                                                                                                    |
| Geometric mean | (ref)                                                                                                                | 1.00x slower                                                                                                             |

Benchmark hidden because not significant (2): 2to3, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | results/bm-20250726-3.15.0a0-a852c7b/bm-20250726-pythonperf1-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b.json | results/bm-20250726-3.15.0a0-a852c7b-JIT/bm-20250726-pythonperf1-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b.json |
|-------------------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| async_tree_io_tg        | 402 ms                                                                                                               | 390 ms: 1.03x faster                                                                                                     |
| async_tree_memoization  | 214 ms                                                                                                               | 207 ms: 1.03x faster                                                                                                     |
| async_tree_io           | 405 ms                                                                                                               | 394 ms: 1.03x faster                                                                                                     |
| async_tree_cpu_io_mixed | 335 ms                                                                                                               | 339 ms: 1.01x slower                                                                                                     |
| asyncio_tcp_ssl         | 1.30 sec                                                                                                             | 1.39 sec: 1.08x slower                                                                                                   |
| async_generators        | 230 ms                                                                                                               | 249 ms: 1.08x slower                                                                                                     |
| asyncio_tcp             | 447 ms                                                                                                               | 497 ms: 1.11x slower                                                                                                     |
| Geometric mean          | (ref)                                                                                                                | 1.01x slower                                                                                                             |

Benchmark hidden because not significant (6): async_tree_none_tg, async_tree_memoization_tg, coroutines, async_tree_none, async_tree_cpu_io_mixed_tg, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250726-3.15.0a0-a852c7b/bm-20250726-pythonperf1-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b.json | results/bm-20250726-3.15.0a0-a852c7b-JIT/bm-20250726-pythonperf1-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| nbody          | 65.3 ms                                                                                                              | 56.5 ms: 1.16x faster                                                                                                    |
| Geometric mean | (ref)                                                                                                                | 1.05x faster                                                                                                             |

Benchmark hidden because not significant (2): pidigits, float

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250726-3.15.0a0-a852c7b/bm-20250726-pythonperf1-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b.json | results/bm-20250726-3.15.0a0-a852c7b-JIT/bm-20250726-pythonperf1-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| regex_compile  | 82.8 ms                                                                                                              | 79.2 ms: 1.05x faster                                                                                                    |
| Geometric mean | (ref)                                                                                                                | 1.02x faster                                                                                                             |

Benchmark hidden because not significant (3): regex_v8, regex_effbot, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20250726-3.15.0a0-a852c7b/bm-20250726-pythonperf1-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b.json | results/bm-20250726-3.15.0a0-a852c7b-JIT/bm-20250726-pythonperf1-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b.json |
|----------------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| unpickle_pure_python | 140 us                                                                                                               | 106 us: 1.32x faster                                                                                                     |
| tomli_loads          | 1.45 sec                                                                                                             | 1.12 sec: 1.30x faster                                                                                                   |
| xml_etree_generate   | 59.1 ms                                                                                                              | 51.3 ms: 1.15x faster                                                                                                    |
| xml_etree_process    | 40.8 ms                                                                                                              | 36.6 ms: 1.11x faster                                                                                                    |
| unpickle_list        | 2.99 us                                                                                                              | 2.76 us: 1.08x faster                                                                                                    |
| pickle_pure_python   | 219 us                                                                                                               | 205 us: 1.07x faster                                                                                                     |
| xml_etree_iterparse  | 66.4 ms                                                                                                              | 65.2 ms: 1.02x faster                                                                                                    |
| json_dumps           | 6.24 ms                                                                                                              | 6.42 ms: 1.03x slower                                                                                                    |
| xml_etree_parse      | 90.0 ms                                                                                                              | 94.8 ms: 1.05x slower                                                                                                    |
| pickle_dict          | 19.7 us                                                                                                              | 20.8 us: 1.06x slower                                                                                                    |
| pickle_list          | 3.24 us                                                                                                              | 3.43 us: 1.06x slower                                                                                                    |
| Geometric mean       | (ref)                                                                                                                | 1.05x faster                                                                                                             |

Benchmark hidden because not significant (3): pickle, json_loads, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20250726-3.15.0a0-a852c7b/bm-20250726-pythonperf1-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b.json | results/bm-20250726-3.15.0a0-a852c7b-JIT/bm-20250726-pythonperf1-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b.json |
|------------------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| python_startup         | 27.0 ms                                                                                                              | 26.2 ms: 1.03x faster                                                                                                    |
| python_startup_no_site | 20.1 ms                                                                                                              | 19.7 ms: 1.02x faster                                                                                                    |
| Geometric mean         | (ref)                                                                                                                | 1.02x faster                                                                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20250726-3.15.0a0-a852c7b/bm-20250726-pythonperf1-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b.json | results/bm-20250726-3.15.0a0-a852c7b-JIT/bm-20250726-pythonperf1-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b.json |
|-----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| mako            | 6.82 ms                                                                                                              | 5.42 ms: 1.26x faster                                                                                                    |
| genshi_text     | 15.7 ms                                                                                                              | 15.4 ms: 1.02x faster                                                                                                    |
| django_template | 25.2 ms                                                                                                              | 24.8 ms: 1.01x faster                                                                                                    |
| genshi_xml      | 34.5 ms                                                                                                              | 35.4 ms: 1.03x slower                                                                                                    |
| Geometric mean  | (ref)                                                                                                                | 1.06x faster                                                                                                             |

All benchmarks:
===============

| Benchmark               | results/bm-20250726-3.15.0a0-a852c7b/bm-20250726-pythonperf1-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b.json | results/bm-20250726-3.15.0a0-a852c7b-JIT/bm-20250726-pythonperf1-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b.json |
|-------------------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| unpickle_pure_python    | 140 us                                                                                                               | 106 us: 1.32x faster                                                                                                     |
| tomli_loads             | 1.45 sec                                                                                                             | 1.12 sec: 1.30x faster                                                                                                   |
| fannkuch                | 264 ms                                                                                                               | 207 ms: 1.28x faster                                                                                                     |
| mako                    | 6.82 ms                                                                                                              | 5.42 ms: 1.26x faster                                                                                                    |
| bpe_tokeniser           | 3.00 sec                                                                                                             | 2.53 sec: 1.19x faster                                                                                                   |
| pyflate                 | 295 ms                                                                                                               | 249 ms: 1.18x faster                                                                                                     |
| scimark_fft             | 183 ms                                                                                                               | 156 ms: 1.17x faster                                                                                                     |
| pprint_safe_repr        | 515 ms                                                                                                               | 443 ms: 1.16x faster                                                                                                     |
| nbody                   | 65.3 ms                                                                                                              | 56.5 ms: 1.16x faster                                                                                                    |
| xml_etree_generate      | 59.1 ms                                                                                                              | 51.3 ms: 1.15x faster                                                                                                    |
| pprint_pformat          | 1.03 sec                                                                                                             | 896 ms: 1.14x faster                                                                                                     |
| scimark_sparse_mat_mult | 2.58 ms                                                                                                              | 2.31 ms: 1.12x faster                                                                                                    |
| xml_etree_process       | 40.8 ms                                                                                                              | 36.6 ms: 1.11x faster                                                                                                    |
| telco                   | 4.69 ms                                                                                                              | 4.27 ms: 1.10x faster                                                                                                    |
| unpickle_list           | 2.99 us                                                                                                              | 2.76 us: 1.08x faster                                                                                                    |
| crypto_pyaes            | 49.4 ms                                                                                                              | 45.9 ms: 1.08x faster                                                                                                    |
| sqlglot_v2_parse        | 836 us                                                                                                               | 776 us: 1.08x faster                                                                                                     |
| pickle_pure_python      | 219 us                                                                                                               | 205 us: 1.07x faster                                                                                                     |
| richards                | 28.7 ms                                                                                                              | 27.1 ms: 1.06x faster                                                                                                    |
| nqueens                 | 65.2 ms                                                                                                              | 61.7 ms: 1.06x faster                                                                                                    |
| raytrace                | 187 ms                                                                                                               | 178 ms: 1.05x faster                                                                                                     |
| k_core                  | 1.71 sec                                                                                                             | 1.63 sec: 1.05x faster                                                                                                   |
| hexiom                  | 4.23 ms                                                                                                              | 4.05 ms: 1.05x faster                                                                                                    |
| regex_compile           | 82.8 ms                                                                                                              | 79.2 ms: 1.05x faster                                                                                                    |
| chaos                   | 42.3 ms                                                                                                              | 40.5 ms: 1.04x faster                                                                                                    |
| sqlglot_v2_transpile    | 1.03 ms                                                                                                              | 984 us: 1.04x faster                                                                                                     |
| pycparser               | 723 ms                                                                                                               | 696 ms: 1.04x faster                                                                                                     |
| connected_components    | 336 ms                                                                                                               | 324 ms: 1.04x faster                                                                                                     |
| richards_super          | 31.5 ms                                                                                                              | 30.5 ms: 1.03x faster                                                                                                    |
| async_tree_io_tg        | 402 ms                                                                                                               | 390 ms: 1.03x faster                                                                                                     |
| async_tree_memoization  | 214 ms                                                                                                               | 207 ms: 1.03x faster                                                                                                     |
| go                      | 77.4 ms                                                                                                              | 75.1 ms: 1.03x faster                                                                                                    |
| comprehensions          | 11.0 us                                                                                                              | 10.7 us: 1.03x faster                                                                                                    |
| python_startup          | 27.0 ms                                                                                                              | 26.2 ms: 1.03x faster                                                                                                    |
| logging_silent          | 57.6 ns                                                                                                              | 56.1 ns: 1.03x faster                                                                                                    |
| async_tree_io           | 405 ms                                                                                                               | 394 ms: 1.03x faster                                                                                                     |
| scimark_sor             | 77.3 ms                                                                                                              | 75.3 ms: 1.03x faster                                                                                                    |
| deepcopy_memo           | 18.7 us                                                                                                              | 18.2 us: 1.03x faster                                                                                                    |
| thrift                  | 523 us                                                                                                               | 510 us: 1.03x faster                                                                                                     |
| html5lib                | 39.3 ms                                                                                                              | 38.3 ms: 1.02x faster                                                                                                    |
| genshi_text             | 15.7 ms                                                                                                              | 15.4 ms: 1.02x faster                                                                                                    |
| sqlite_synth            | 1.58 us                                                                                                              | 1.55 us: 1.02x faster                                                                                                    |
| xml_etree_iterparse     | 66.4 ms                                                                                                              | 65.2 ms: 1.02x faster                                                                                                    |
| coverage                | 51.9 ms                                                                                                              | 51.1 ms: 1.02x faster                                                                                                    |
| python_startup_no_site  | 20.1 ms                                                                                                              | 19.7 ms: 1.02x faster                                                                                                    |
| deltablue               | 2.29 ms                                                                                                              | 2.26 ms: 1.01x faster                                                                                                    |
| django_template         | 25.2 ms                                                                                                              | 24.8 ms: 1.01x faster                                                                                                    |
| shortest_path           | 362 ms                                                                                                               | 357 ms: 1.01x faster                                                                                                     |
| scimark_monte_carlo     | 40.9 ms                                                                                                              | 40.5 ms: 1.01x faster                                                                                                    |
| bench_mp_pool           | 96.6 ms                                                                                                              | 95.8 ms: 1.01x faster                                                                                                    |
| sqlglot_v2_optimize     | 34.1 ms                                                                                                              | 34.5 ms: 1.01x slower                                                                                                    |
| async_tree_cpu_io_mixed | 335 ms                                                                                                               | 339 ms: 1.01x slower                                                                                                     |
| dulwich_log             | 40.8 ms                                                                                                              | 41.6 ms: 1.02x slower                                                                                                    |
| create_gc_cycles        | 1.30 ms                                                                                                              | 1.33 ms: 1.02x slower                                                                                                    |
| sympy_sum               | 88.3 ms                                                                                                              | 90.2 ms: 1.02x slower                                                                                                    |
| genshi_xml              | 34.5 ms                                                                                                              | 35.4 ms: 1.03x slower                                                                                                    |
| pathlib                 | 32.6 ms                                                                                                              | 33.4 ms: 1.03x slower                                                                                                    |
| json_dumps              | 6.24 ms                                                                                                              | 6.42 ms: 1.03x slower                                                                                                    |
| sympy_expand            | 287 ms                                                                                                               | 296 ms: 1.03x slower                                                                                                     |
| subparsers              | 30.2 ms                                                                                                              | 31.1 ms: 1.03x slower                                                                                                    |
| docutils                | 1.64 sec                                                                                                             | 1.69 sec: 1.03x slower                                                                                                   |
| gc_traversal            | 2.11 ms                                                                                                              | 2.18 ms: 1.03x slower                                                                                                    |
| many_optionals          | 573 us                                                                                                               | 594 us: 1.04x slower                                                                                                     |
| generators              | 19.4 ms                                                                                                              | 20.2 ms: 1.04x slower                                                                                                    |
| spectral_norm           | 61.6 ms                                                                                                              | 64.3 ms: 1.05x slower                                                                                                    |
| logging_format          | 6.58 us                                                                                                              | 6.89 us: 1.05x slower                                                                                                    |
| sympy_integrate         | 12.5 ms                                                                                                              | 13.1 ms: 1.05x slower                                                                                                    |
| xml_etree_parse         | 90.0 ms                                                                                                              | 94.8 ms: 1.05x slower                                                                                                    |
| pickle_dict             | 19.7 us                                                                                                              | 20.8 us: 1.06x slower                                                                                                    |
| logging_simple          | 6.18 us                                                                                                              | 6.53 us: 1.06x slower                                                                                                    |
| pickle_list             | 3.24 us                                                                                                              | 3.43 us: 1.06x slower                                                                                                    |
| asyncio_tcp_ssl         | 1.30 sec                                                                                                             | 1.39 sec: 1.08x slower                                                                                                   |
| async_generators        | 230 ms                                                                                                               | 249 ms: 1.08x slower                                                                                                     |
| asyncio_tcp             | 447 ms                                                                                                               | 497 ms: 1.11x slower                                                                                                     |
| Geometric mean          | (ref)                                                                                                                | 1.03x faster                                                                                                             |

Benchmark hidden because not significant (28): regex_v8, deepcopy_reduce, async_tree_none_tg, async_tree_memoization_tg, coroutines, async_tree_none, bench_thread_pool, pidigits, deepcopy, async_tree_cpu_io_mixed_tg, scimark_lu, unpack_sequence, typing_runtime_protocols, sqlglot_v2_normalize, 2to3, pylint, regex_effbot, json, regex_dna, pickle, float, mdp, meteor_contest, json_loads, sphinx, unpickle, asyncio_websockets, sympy_str

- Geometric mean (including insignificant results): 1.033x faster

# HPT report

- Reliability score: 99.98% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown