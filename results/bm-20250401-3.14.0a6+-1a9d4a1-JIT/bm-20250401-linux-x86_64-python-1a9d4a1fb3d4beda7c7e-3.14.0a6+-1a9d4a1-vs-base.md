# Results vs. base

- fork: python
- ref: 1a9d4a1fb3d4beda7c7e
- machine: linux-x86_64
- commit hash: 1a9d4a1
- commit date: 2025-04-01
- overall geometric mean: 1.003x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250401-3.14.0a6+-1a9d4a1/bm-20250401-linux-x86_64-python-1a9d4a1fb3d4beda7c7e-3.14.0a6+-1a9d4a1.json | results/bm-20250401-3.14.0a6+-1a9d4a1-JIT/bm-20250401-linux-x86_64-python-1a9d4a1fb3d4beda7c7e-3.14.0a6+-1a9d4a1.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 252 ms                                                                                                            | 257 ms: 1.02x slower                                                                                                  |
| docutils       | 2.60 sec                                                                                                          | 2.67 sec: 1.03x slower                                                                                                |
| html5lib       | 60.6 ms                                                                                                           | 61.9 ms: 1.02x slower                                                                                                 |
| sphinx         | 1.02 sec                                                                                                          | 1.03 sec: 1.01x slower                                                                                                |
| Geometric mean | (ref)                                                                                                             | 1.02x slower                                                                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | results/bm-20250401-3.14.0a6+-1a9d4a1/bm-20250401-linux-x86_64-python-1a9d4a1fb3d4beda7c7e-3.14.0a6+-1a9d4a1.json | results/bm-20250401-3.14.0a6+-1a9d4a1-JIT/bm-20250401-linux-x86_64-python-1a9d4a1fb3d4beda7c7e-3.14.0a6+-1a9d4a1.json |
|------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| coroutines       | 23.3 ms                                                                                                           | 23.5 ms: 1.00x slower                                                                                                 |
| async_generators | 394 ms                                                                                                            | 414 ms: 1.05x slower                                                                                                  |
| Geometric mean   | (ref)                                                                                                             | 1.01x slower                                                                                                          |

Benchmark hidden because not significant (9): async_tree_io, asyncio_websockets, async_tree_memoization, async_tree_cpu_io_mixed, async_tree_none, async_tree_memoization_tg, async_tree_io_tg, async_tree_none_tg, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250401-3.14.0a6+-1a9d4a1/bm-20250401-linux-x86_64-python-1a9d4a1fb3d4beda7c7e-3.14.0a6+-1a9d4a1.json | results/bm-20250401-3.14.0a6+-1a9d4a1-JIT/bm-20250401-linux-x86_64-python-1a9d4a1fb3d4beda7c7e-3.14.0a6+-1a9d4a1.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| float          | 68.6 ms                                                                                                           | 61.5 ms: 1.12x faster                                                                                                 |
| nbody          | 93.8 ms                                                                                                           | 86.4 ms: 1.09x faster                                                                                                 |
| pidigits       | 186 ms                                                                                                            | 186 ms: 1.00x slower                                                                                                  |
| Geometric mean | (ref)                                                                                                             | 1.06x faster                                                                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250401-3.14.0a6+-1a9d4a1/bm-20250401-linux-x86_64-python-1a9d4a1fb3d4beda7c7e-3.14.0a6+-1a9d4a1.json | results/bm-20250401-3.14.0a6+-1a9d4a1-JIT/bm-20250401-linux-x86_64-python-1a9d4a1fb3d4beda7c7e-3.14.0a6+-1a9d4a1.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| regex_dna      | 220 ms                                                                                                            | 221 ms: 1.00x slower                                                                                                  |
| regex_compile  | 125 ms                                                                                                            | 126 ms: 1.01x slower                                                                                                  |
| regex_effbot   | 3.29 ms                                                                                                           | 3.35 ms: 1.02x slower                                                                                                 |
| Geometric mean | (ref)                                                                                                             | 1.01x slower                                                                                                          |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20250401-3.14.0a6+-1a9d4a1/bm-20250401-linux-x86_64-python-1a9d4a1fb3d4beda7c7e-3.14.0a6+-1a9d4a1.json | results/bm-20250401-3.14.0a6+-1a9d4a1-JIT/bm-20250401-linux-x86_64-python-1a9d4a1fb3d4beda7c7e-3.14.0a6+-1a9d4a1.json |
|----------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| tomli_loads          | 1.94 sec                                                                                                          | 1.83 sec: 1.06x faster                                                                                                |
| xml_etree_generate   | 84.1 ms                                                                                                           | 79.4 ms: 1.06x faster                                                                                                 |
| unpickle_pure_python | 218 us                                                                                                            | 209 us: 1.04x faster                                                                                                  |
| xml_etree_process    | 58.7 ms                                                                                                           | 56.6 ms: 1.04x faster                                                                                                 |
| xml_etree_parse      | 144 ms                                                                                                            | 140 ms: 1.03x faster                                                                                                  |
| json_loads           | 29.8 us                                                                                                           | 29.6 us: 1.01x faster                                                                                                 |
| xml_etree_iterparse  | 98.8 ms                                                                                                           | 98.2 ms: 1.01x faster                                                                                                 |
| json_dumps           | 11.4 ms                                                                                                           | 11.5 ms: 1.01x slower                                                                                                 |
| pickle_pure_python   | 313 us                                                                                                            | 317 us: 1.01x slower                                                                                                  |
| Geometric mean       | (ref)                                                                                                             | 1.02x faster                                                                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20250401-3.14.0a6+-1a9d4a1/bm-20250401-linux-x86_64-python-1a9d4a1fb3d4beda7c7e-3.14.0a6+-1a9d4a1.json | results/bm-20250401-3.14.0a6+-1a9d4a1-JIT/bm-20250401-linux-x86_64-python-1a9d4a1fb3d4beda7c7e-3.14.0a6+-1a9d4a1.json |
|------------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| python_startup         | 13.1 ms                                                                                                           | 13.1 ms: 1.00x faster                                                                                                 |
| python_startup_no_site | 8.18 ms                                                                                                           | 8.19 ms: 1.00x slower                                                                                                 |
| Geometric mean         | (ref)                                                                                                             | 1.00x faster                                                                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20250401-3.14.0a6+-1a9d4a1/bm-20250401-linux-x86_64-python-1a9d4a1fb3d4beda7c7e-3.14.0a6+-1a9d4a1.json | results/bm-20250401-3.14.0a6+-1a9d4a1-JIT/bm-20250401-linux-x86_64-python-1a9d4a1fb3d4beda7c7e-3.14.0a6+-1a9d4a1.json |
|-----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| mako            | 11.3 ms                                                                                                           | 10.9 ms: 1.04x faster                                                                                                 |
| genshi_text     | 21.5 ms                                                                                                           | 21.2 ms: 1.01x faster                                                                                                 |
| genshi_xml      | 49.2 ms                                                                                                           | 49.9 ms: 1.02x slower                                                                                                 |
| django_template | 31.3 ms                                                                                                           | 32.6 ms: 1.04x slower                                                                                                 |
| Geometric mean  | (ref)                                                                                                             | 1.00x faster                                                                                                          |

All benchmarks:
===============

| Benchmark                | results/bm-20250401-3.14.0a6+-1a9d4a1/bm-20250401-linux-x86_64-python-1a9d4a1fb3d4beda7c7e-3.14.0a6+-1a9d4a1.json | results/bm-20250401-3.14.0a6+-1a9d4a1-JIT/bm-20250401-linux-x86_64-python-1a9d4a1fb3d4beda7c7e-3.14.0a6+-1a9d4a1.json |
|--------------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| richards_super           | 49.4 ms                                                                                                           | 39.7 ms: 1.24x faster                                                                                                 |
| richards                 | 43.3 ms                                                                                                           | 34.9 ms: 1.24x faster                                                                                                 |
| float                    | 68.6 ms                                                                                                           | 61.5 ms: 1.12x faster                                                                                                 |
| deltablue                | 3.37 ms                                                                                                           | 3.03 ms: 1.11x faster                                                                                                 |
| scimark_fft              | 340 ms                                                                                                            | 307 ms: 1.11x faster                                                                                                  |
| nbody                    | 93.8 ms                                                                                                           | 86.4 ms: 1.09x faster                                                                                                 |
| tomli_loads              | 1.94 sec                                                                                                          | 1.83 sec: 1.06x faster                                                                                                |
| xml_etree_generate       | 84.1 ms                                                                                                           | 79.4 ms: 1.06x faster                                                                                                 |
| generators               | 30.9 ms                                                                                                           | 29.5 ms: 1.05x faster                                                                                                 |
| mako                     | 11.3 ms                                                                                                           | 10.9 ms: 1.04x faster                                                                                                 |
| unpickle_pure_python     | 218 us                                                                                                            | 209 us: 1.04x faster                                                                                                  |
| xml_etree_process        | 58.7 ms                                                                                                           | 56.6 ms: 1.04x faster                                                                                                 |
| pyflate                  | 444 ms                                                                                                            | 429 ms: 1.04x faster                                                                                                  |
| gc_traversal             | 4.98 ms                                                                                                           | 4.82 ms: 1.03x faster                                                                                                 |
| deepcopy_reduce          | 2.72 us                                                                                                           | 2.64 us: 1.03x faster                                                                                                 |
| xml_etree_parse          | 144 ms                                                                                                            | 140 ms: 1.03x faster                                                                                                  |
| sqlite_synth             | 2.80 us                                                                                                           | 2.75 us: 1.02x faster                                                                                                 |
| genshi_text              | 21.5 ms                                                                                                           | 21.2 ms: 1.01x faster                                                                                                 |
| json                     | 5.33 ms                                                                                                           | 5.27 ms: 1.01x faster                                                                                                 |
| deepcopy_memo            | 28.9 us                                                                                                           | 28.6 us: 1.01x faster                                                                                                 |
| json_loads               | 29.8 us                                                                                                           | 29.6 us: 1.01x faster                                                                                                 |
| bench_mp_pool            | 83.3 ms                                                                                                           | 82.7 ms: 1.01x faster                                                                                                 |
| logging_simple           | 5.61 us                                                                                                           | 5.57 us: 1.01x faster                                                                                                 |
| logging_silent           | 96.5 ns                                                                                                           | 95.9 ns: 1.01x faster                                                                                                 |
| xml_etree_iterparse      | 98.8 ms                                                                                                           | 98.2 ms: 1.01x faster                                                                                                 |
| python_startup           | 13.1 ms                                                                                                           | 13.1 ms: 1.00x faster                                                                                                 |
| python_startup_no_site   | 8.18 ms                                                                                                           | 8.19 ms: 1.00x slower                                                                                                 |
| regex_dna                | 220 ms                                                                                                            | 221 ms: 1.00x slower                                                                                                  |
| pidigits                 | 186 ms                                                                                                            | 186 ms: 1.00x slower                                                                                                  |
| mdp                      | 1.22 sec                                                                                                          | 1.22 sec: 1.00x slower                                                                                                |
| coroutines               | 23.3 ms                                                                                                           | 23.5 ms: 1.00x slower                                                                                                 |
| fannkuch                 | 413 ms                                                                                                            | 415 ms: 1.01x slower                                                                                                  |
| regex_compile            | 125 ms                                                                                                            | 126 ms: 1.01x slower                                                                                                  |
| create_gc_cycles         | 2.48 ms                                                                                                           | 2.50 ms: 1.01x slower                                                                                                 |
| coverage                 | 84.6 ms                                                                                                           | 85.1 ms: 1.01x slower                                                                                                 |
| subparsers               | 20.7 ms                                                                                                           | 20.8 ms: 1.01x slower                                                                                                 |
| chaos                    | 56.3 ms                                                                                                           | 56.8 ms: 1.01x slower                                                                                                 |
| pathlib                  | 16.4 ms                                                                                                           | 16.6 ms: 1.01x slower                                                                                                 |
| raytrace                 | 256 ms                                                                                                            | 259 ms: 1.01x slower                                                                                                  |
| sympy_sum                | 149 ms                                                                                                            | 150 ms: 1.01x slower                                                                                                  |
| scimark_sor              | 116 ms                                                                                                            | 117 ms: 1.01x slower                                                                                                  |
| bpe_tokeniser            | 4.49 sec                                                                                                          | 4.55 sec: 1.01x slower                                                                                                |
| sqlglot_v2_normalize     | 107 ms                                                                                                            | 108 ms: 1.01x slower                                                                                                  |
| json_dumps               | 11.4 ms                                                                                                           | 11.5 ms: 1.01x slower                                                                                                 |
| sympy_str                | 268 ms                                                                                                            | 272 ms: 1.01x slower                                                                                                  |
| bench_thread_pool        | 878 us                                                                                                            | 890 us: 1.01x slower                                                                                                  |
| pickle_pure_python       | 313 us                                                                                                            | 317 us: 1.01x slower                                                                                                  |
| sphinx                   | 1.02 sec                                                                                                          | 1.03 sec: 1.01x slower                                                                                                |
| sqlalchemy_declarative   | 131 ms                                                                                                            | 133 ms: 1.01x slower                                                                                                  |
| spectral_norm            | 98.9 ms                                                                                                           | 100 ms: 1.01x slower                                                                                                  |
| genshi_xml               | 49.2 ms                                                                                                           | 49.9 ms: 1.02x slower                                                                                                 |
| sqlglot_v2_parse         | 1.23 ms                                                                                                           | 1.25 ms: 1.02x slower                                                                                                 |
| regex_effbot             | 3.29 ms                                                                                                           | 3.35 ms: 1.02x slower                                                                                                 |
| pycparser                | 1.15 sec                                                                                                          | 1.17 sec: 1.02x slower                                                                                                |
| sympy_integrate          | 19.2 ms                                                                                                           | 19.6 ms: 1.02x slower                                                                                                 |
| meteor_contest           | 106 ms                                                                                                            | 108 ms: 1.02x slower                                                                                                  |
| 2to3                     | 252 ms                                                                                                            | 257 ms: 1.02x slower                                                                                                  |
| dulwich_log              | 58.9 ms                                                                                                           | 60.2 ms: 1.02x slower                                                                                                 |
| sympy_expand             | 459 ms                                                                                                            | 469 ms: 1.02x slower                                                                                                  |
| sqlglot_v2_optimize      | 52.8 ms                                                                                                           | 54.0 ms: 1.02x slower                                                                                                 |
| many_optionals           | 928 us                                                                                                            | 948 us: 1.02x slower                                                                                                  |
| html5lib                 | 60.6 ms                                                                                                           | 61.9 ms: 1.02x slower                                                                                                 |
| sqlglot_v2_transpile     | 1.54 ms                                                                                                           | 1.58 ms: 1.02x slower                                                                                                 |
| crypto_pyaes             | 72.6 ms                                                                                                           | 74.4 ms: 1.02x slower                                                                                                 |
| scimark_lu               | 113 ms                                                                                                            | 116 ms: 1.03x slower                                                                                                  |
| scimark_monte_carlo      | 64.3 ms                                                                                                           | 66.0 ms: 1.03x slower                                                                                                 |
| docutils                 | 2.60 sec                                                                                                          | 2.67 sec: 1.03x slower                                                                                                |
| telco                    | 7.80 ms                                                                                                           | 8.02 ms: 1.03x slower                                                                                                 |
| nqueens                  | 82.3 ms                                                                                                           | 84.7 ms: 1.03x slower                                                                                                 |
| pprint_safe_repr         | 725 ms                                                                                                            | 750 ms: 1.03x slower                                                                                                  |
| pprint_pformat           | 1.49 sec                                                                                                          | 1.55 sec: 1.04x slower                                                                                                |
| django_template          | 31.3 ms                                                                                                           | 32.6 ms: 1.04x slower                                                                                                 |
| async_generators         | 394 ms                                                                                                            | 414 ms: 1.05x slower                                                                                                  |
| typing_runtime_protocols | 164 us                                                                                                            | 173 us: 1.06x slower                                                                                                  |
| hexiom                   | 6.18 ms                                                                                                           | 6.70 ms: 1.08x slower                                                                                                 |
| comprehensions           | 16.5 us                                                                                                           | 18.2 us: 1.10x slower                                                                                                 |
| go                       | 111 ms                                                                                                            | 123 ms: 1.11x slower                                                                                                  |
| Geometric mean           | (ref)                                                                                                             | 1.00x faster                                                                                                          |

Benchmark hidden because not significant (18): scimark_sparse_mat_mult, shortest_path, async_tree_io, asyncio_websockets, async_tree_memoization, async_tree_cpu_io_mixed, connected_components, async_tree_none, async_tree_memoization_tg, regex_v8, async_tree_io_tg, deepcopy, logging_format, async_tree_none_tg, async_tree_cpu_io_mixed_tg, sqlalchemy_imperative, k_core, pylint

- Geometric mean (including insignificant results): 1.003x faster

# HPT report

- Reliability score: 99.99% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.01x