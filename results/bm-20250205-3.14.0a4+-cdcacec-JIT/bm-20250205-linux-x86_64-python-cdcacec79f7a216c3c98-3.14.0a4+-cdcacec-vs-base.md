# Results vs. base

- fork: python
- ref: cdcacec79f7a216c3c98
- machine: linux-x86_64
- commit hash: cdcacec
- commit date: 2025-02-05
- overall geometric mean: 1.018x slower
- HPT reliability: 99.95%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250205-3.14.0a4+-cdcacec/bm-20250205-linux-x86_64-python-cdcacec79f7a216c3c98-3.14.0a4+-cdcacec.json | results/bm-20250205-3.14.0a4+-cdcacec-JIT/bm-20250205-linux-x86_64-python-cdcacec79f7a216c3c98-3.14.0a4+-cdcacec.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 252 ms                                                                                                            | 261 ms: 1.03x slower                                                                                                  |
| docutils       | 2.58 sec                                                                                                          | 2.68 sec: 1.04x slower                                                                                                |
| html5lib       | 59.8 ms                                                                                                           | 64.1 ms: 1.07x slower                                                                                                 |
| sphinx         | 994 ms                                                                                                            | 1.04 sec: 1.04x slower                                                                                                |
| Geometric mean | (ref)                                                                                                             | 1.05x slower                                                                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark              | results/bm-20250205-3.14.0a4+-cdcacec/bm-20250205-linux-x86_64-python-cdcacec79f7a216c3c98-3.14.0a4+-cdcacec.json | results/bm-20250205-3.14.0a4+-cdcacec-JIT/bm-20250205-linux-x86_64-python-cdcacec79f7a216c3c98-3.14.0a4+-cdcacec.json |
|------------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| coroutines             | 23.3 ms                                                                                                           | 22.7 ms: 1.03x faster                                                                                                 |
| async_tree_io          | 618 ms                                                                                                            | 627 ms: 1.01x slower                                                                                                  |
| async_tree_none        | 264 ms                                                                                                            | 268 ms: 1.02x slower                                                                                                  |
| async_tree_memoization | 322 ms                                                                                                            | 329 ms: 1.02x slower                                                                                                  |
| async_generators       | 383 ms                                                                                                            | 411 ms: 1.07x slower                                                                                                  |
| Geometric mean         | (ref)                                                                                                             | 1.01x slower                                                                                                          |

Benchmark hidden because not significant (6): async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, asyncio_websockets, async_tree_none_tg, async_tree_cpu_io_mixed, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250205-3.14.0a4+-cdcacec/bm-20250205-linux-x86_64-python-cdcacec79f7a216c3c98-3.14.0a4+-cdcacec.json | results/bm-20250205-3.14.0a4+-cdcacec-JIT/bm-20250205-linux-x86_64-python-cdcacec79f7a216c3c98-3.14.0a4+-cdcacec.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| float          | 70.5 ms                                                                                                           | 67.1 ms: 1.05x faster                                                                                                 |
| pidigits       | 186 ms                                                                                                            | 186 ms: 1.00x faster                                                                                                  |
| nbody          | 92.7 ms                                                                                                           | 93.6 ms: 1.01x slower                                                                                                 |
| Geometric mean | (ref)                                                                                                             | 1.01x faster                                                                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250205-3.14.0a4+-cdcacec/bm-20250205-linux-x86_64-python-cdcacec79f7a216c3c98-3.14.0a4+-cdcacec.json | results/bm-20250205-3.14.0a4+-cdcacec-JIT/bm-20250205-linux-x86_64-python-cdcacec79f7a216c3c98-3.14.0a4+-cdcacec.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| regex_v8       | 25.4 ms                                                                                                           | 24.1 ms: 1.05x faster                                                                                                 |
| regex_compile  | 126 ms                                                                                                            | 129 ms: 1.02x slower                                                                                                  |
| regex_dna      | 210 ms                                                                                                            | 215 ms: 1.02x slower                                                                                                  |
| Geometric mean | (ref)                                                                                                             | 1.00x faster                                                                                                          |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20250205-3.14.0a4+-cdcacec/bm-20250205-linux-x86_64-python-cdcacec79f7a216c3c98-3.14.0a4+-cdcacec.json | results/bm-20250205-3.14.0a4+-cdcacec-JIT/bm-20250205-linux-x86_64-python-cdcacec79f7a216c3c98-3.14.0a4+-cdcacec.json |
|----------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| unpickle_pure_python | 216 us                                                                                                            | 201 us: 1.07x faster                                                                                                  |
| tomli_loads          | 1.94 sec                                                                                                          | 1.84 sec: 1.06x faster                                                                                                |
| json_dumps           | 11.9 ms                                                                                                           | 11.3 ms: 1.05x faster                                                                                                 |
| xml_etree_process    | 58.4 ms                                                                                                           | 56.7 ms: 1.03x faster                                                                                                 |
| xml_etree_iterparse  | 97.1 ms                                                                                                           | 95.9 ms: 1.01x faster                                                                                                 |
| pickle_pure_python   | 317 us                                                                                                            | 314 us: 1.01x faster                                                                                                  |
| xml_etree_parse      | 139 ms                                                                                                            | 138 ms: 1.01x faster                                                                                                  |
| json_loads           | 28.5 us                                                                                                           | 29.1 us: 1.02x slower                                                                                                 |
| Geometric mean       | (ref)                                                                                                             | 1.02x faster                                                                                                          |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20250205-3.14.0a4+-cdcacec/bm-20250205-linux-x86_64-python-cdcacec79f7a216c3c98-3.14.0a4+-cdcacec.json | results/bm-20250205-3.14.0a4+-cdcacec-JIT/bm-20250205-linux-x86_64-python-cdcacec79f7a216c3c98-3.14.0a4+-cdcacec.json |
|------------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| python_startup         | 12.8 ms                                                                                                           | 12.8 ms: 1.00x faster                                                                                                 |
| python_startup_no_site | 7.05 ms                                                                                                           | 7.04 ms: 1.00x faster                                                                                                 |
| Geometric mean         | (ref)                                                                                                             | 1.00x faster                                                                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20250205-3.14.0a4+-cdcacec/bm-20250205-linux-x86_64-python-cdcacec79f7a216c3c98-3.14.0a4+-cdcacec.json | results/bm-20250205-3.14.0a4+-cdcacec-JIT/bm-20250205-linux-x86_64-python-cdcacec79f7a216c3c98-3.14.0a4+-cdcacec.json |
|-----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| mako            | 11.0 ms                                                                                                           | 9.86 ms: 1.12x faster                                                                                                 |
| django_template | 31.4 ms                                                                                                           | 33.0 ms: 1.05x slower                                                                                                 |
| genshi_text     | 21.1 ms                                                                                                           | 23.1 ms: 1.09x slower                                                                                                 |
| genshi_xml      | 47.8 ms                                                                                                           | 57.0 ms: 1.19x slower                                                                                                 |
| Geometric mean  | (ref)                                                                                                             | 1.05x slower                                                                                                          |

All benchmarks:
===============

| Benchmark                | results/bm-20250205-3.14.0a4+-cdcacec/bm-20250205-linux-x86_64-python-cdcacec79f7a216c3c98-3.14.0a4+-cdcacec.json | results/bm-20250205-3.14.0a4+-cdcacec-JIT/bm-20250205-linux-x86_64-python-cdcacec79f7a216c3c98-3.14.0a4+-cdcacec.json |
|--------------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| mako                     | 11.0 ms                                                                                                           | 9.86 ms: 1.12x faster                                                                                                 |
| scimark_fft              | 341 ms                                                                                                            | 315 ms: 1.08x faster                                                                                                  |
| unpickle_pure_python     | 216 us                                                                                                            | 201 us: 1.07x faster                                                                                                  |
| scimark_sor              | 121 ms                                                                                                            | 114 ms: 1.06x faster                                                                                                  |
| scimark_monte_carlo      | 67.4 ms                                                                                                           | 63.5 ms: 1.06x faster                                                                                                 |
| tomli_loads              | 1.94 sec                                                                                                          | 1.84 sec: 1.06x faster                                                                                                |
| regex_v8                 | 25.4 ms                                                                                                           | 24.1 ms: 1.05x faster                                                                                                 |
| json_dumps               | 11.9 ms                                                                                                           | 11.3 ms: 1.05x faster                                                                                                 |
| float                    | 70.5 ms                                                                                                           | 67.1 ms: 1.05x faster                                                                                                 |
| telco                    | 7.81 ms                                                                                                           | 7.53 ms: 1.04x faster                                                                                                 |
| coroutines               | 23.3 ms                                                                                                           | 22.7 ms: 1.03x faster                                                                                                 |
| xml_etree_process        | 58.4 ms                                                                                                           | 56.7 ms: 1.03x faster                                                                                                 |
| gc_traversal             | 5.03 ms                                                                                                           | 4.89 ms: 1.03x faster                                                                                                 |
| fannkuch                 | 396 ms                                                                                                            | 386 ms: 1.03x faster                                                                                                  |
| sqlite_synth             | 2.77 us                                                                                                           | 2.71 us: 1.02x faster                                                                                                 |
| bpe_tokeniser            | 4.42 sec                                                                                                          | 4.37 sec: 1.01x faster                                                                                                |
| coverage                 | 91.8 ms                                                                                                           | 90.6 ms: 1.01x faster                                                                                                 |
| xml_etree_iterparse      | 97.1 ms                                                                                                           | 95.9 ms: 1.01x faster                                                                                                 |
| create_gc_cycles         | 2.48 ms                                                                                                           | 2.45 ms: 1.01x faster                                                                                                 |
| pickle_pure_python       | 317 us                                                                                                            | 314 us: 1.01x faster                                                                                                  |
| pyflate                  | 452 ms                                                                                                            | 448 ms: 1.01x faster                                                                                                  |
| bench_mp_pool            | 81.0 ms                                                                                                           | 80.4 ms: 1.01x faster                                                                                                 |
| xml_etree_parse          | 139 ms                                                                                                            | 138 ms: 1.01x faster                                                                                                  |
| crypto_pyaes             | 70.2 ms                                                                                                           | 69.9 ms: 1.00x faster                                                                                                 |
| python_startup           | 12.8 ms                                                                                                           | 12.8 ms: 1.00x faster                                                                                                 |
| python_startup_no_site   | 7.05 ms                                                                                                           | 7.04 ms: 1.00x faster                                                                                                 |
| pidigits                 | 186 ms                                                                                                            | 186 ms: 1.00x faster                                                                                                  |
| meteor_contest           | 106 ms                                                                                                            | 106 ms: 1.00x slower                                                                                                  |
| scimark_lu               | 115 ms                                                                                                            | 115 ms: 1.01x slower                                                                                                  |
| nbody                    | 92.7 ms                                                                                                           | 93.6 ms: 1.01x slower                                                                                                 |
| thrift                   | 766 us                                                                                                            | 773 us: 1.01x slower                                                                                                  |
| subparsers               | 20.5 ms                                                                                                           | 20.7 ms: 1.01x slower                                                                                                 |
| deepcopy_memo            | 30.0 us                                                                                                           | 30.3 us: 1.01x slower                                                                                                 |
| async_tree_io            | 618 ms                                                                                                            | 627 ms: 1.01x slower                                                                                                  |
| sqlglot_parse            | 1.26 ms                                                                                                           | 1.28 ms: 1.02x slower                                                                                                 |
| async_tree_none          | 264 ms                                                                                                            | 268 ms: 1.02x slower                                                                                                  |
| connected_components     | 434 ms                                                                                                            | 441 ms: 1.02x slower                                                                                                  |
| k_core                   | 2.26 sec                                                                                                          | 2.30 sec: 1.02x slower                                                                                                |
| json_loads               | 28.5 us                                                                                                           | 29.1 us: 1.02x slower                                                                                                 |
| regex_compile            | 126 ms                                                                                                            | 129 ms: 1.02x slower                                                                                                  |
| sqlalchemy_imperative    | 16.4 ms                                                                                                           | 16.8 ms: 1.02x slower                                                                                                 |
| async_tree_memoization   | 322 ms                                                                                                            | 329 ms: 1.02x slower                                                                                                  |
| pycparser                | 1.16 sec                                                                                                          | 1.18 sec: 1.02x slower                                                                                                |
| regex_dna                | 210 ms                                                                                                            | 215 ms: 1.02x slower                                                                                                  |
| sqlalchemy_declarative   | 128 ms                                                                                                            | 131 ms: 1.02x slower                                                                                                  |
| sqlglot_transpile        | 1.56 ms                                                                                                           | 1.60 ms: 1.02x slower                                                                                                 |
| many_optionals           | 932 us                                                                                                            | 958 us: 1.03x slower                                                                                                  |
| shortest_path            | 471 ms                                                                                                            | 484 ms: 1.03x slower                                                                                                  |
| typing_runtime_protocols | 157 us                                                                                                            | 162 us: 1.03x slower                                                                                                  |
| logging_format           | 6.12 us                                                                                                           | 6.32 us: 1.03x slower                                                                                                 |
| 2to3                     | 252 ms                                                                                                            | 261 ms: 1.03x slower                                                                                                  |
| sympy_expand             | 454 ms                                                                                                            | 469 ms: 1.03x slower                                                                                                  |
| docutils                 | 2.58 sec                                                                                                          | 2.68 sec: 1.04x slower                                                                                                |
| bench_thread_pool        | 864 us                                                                                                            | 897 us: 1.04x slower                                                                                                  |
| logging_silent           | 107 ns                                                                                                            | 112 ns: 1.04x slower                                                                                                  |
| chaos                    | 57.6 ms                                                                                                           | 60.0 ms: 1.04x slower                                                                                                 |
| mdp                      | 2.46 sec                                                                                                          | 2.56 sec: 1.04x slower                                                                                                |
| sphinx                   | 994 ms                                                                                                            | 1.04 sec: 1.04x slower                                                                                                |
| comprehensions           | 16.3 us                                                                                                           | 17.1 us: 1.05x slower                                                                                                 |
| dulwich_log              | 64.0 ms                                                                                                           | 66.9 ms: 1.05x slower                                                                                                 |
| deepcopy_reduce          | 2.68 us                                                                                                           | 2.81 us: 1.05x slower                                                                                                 |
| sqlglot_optimize         | 51.8 ms                                                                                                           | 54.3 ms: 1.05x slower                                                                                                 |
| pylint                   | 273 ms                                                                                                            | 286 ms: 1.05x slower                                                                                                  |
| django_template          | 31.4 ms                                                                                                           | 33.0 ms: 1.05x slower                                                                                                 |
| sqlglot_normalize        | 103 ms                                                                                                            | 108 ms: 1.05x slower                                                                                                  |
| logging_simple           | 5.48 us                                                                                                           | 5.77 us: 1.05x slower                                                                                                 |
| go                       | 119 ms                                                                                                            | 126 ms: 1.05x slower                                                                                                  |
| sympy_str                | 265 ms                                                                                                            | 280 ms: 1.06x slower                                                                                                  |
| sympy_sum                | 147 ms                                                                                                            | 155 ms: 1.06x slower                                                                                                  |
| sympy_integrate          | 19.5 ms                                                                                                           | 20.7 ms: 1.06x slower                                                                                                 |
| deepcopy                 | 255 us                                                                                                            | 272 us: 1.06x slower                                                                                                  |
| html5lib                 | 59.8 ms                                                                                                           | 64.1 ms: 1.07x slower                                                                                                 |
| async_generators         | 383 ms                                                                                                            | 411 ms: 1.07x slower                                                                                                  |
| deltablue                | 3.22 ms                                                                                                           | 3.48 ms: 1.08x slower                                                                                                 |
| pprint_pformat           | 1.45 sec                                                                                                          | 1.56 sec: 1.08x slower                                                                                                |
| pprint_safe_repr         | 707 ms                                                                                                            | 763 ms: 1.08x slower                                                                                                  |
| raytrace                 | 269 ms                                                                                                            | 292 ms: 1.09x slower                                                                                                  |
| genshi_text              | 21.1 ms                                                                                                           | 23.1 ms: 1.09x slower                                                                                                 |
| nqueens                  | 79.6 ms                                                                                                           | 90.5 ms: 1.14x slower                                                                                                 |
| hexiom                   | 6.27 ms                                                                                                           | 7.43 ms: 1.18x slower                                                                                                 |
| genshi_xml               | 47.8 ms                                                                                                           | 57.0 ms: 1.19x slower                                                                                                 |
| generators               | 27.6 ms                                                                                                           | 37.5 ms: 1.36x slower                                                                                                 |
| Geometric mean           | (ref)                                                                                                             | 1.02x slower                                                                                                          |

Benchmark hidden because not significant (14): async_tree_memoization_tg, scimark_sparse_mat_mult, async_tree_cpu_io_mixed_tg, richards, richards_super, asyncio_websockets, regex_effbot, async_tree_none_tg, json, spectral_norm, async_tree_cpu_io_mixed, xml_etree_generate, pathlib, async_tree_io_tg

- Geometric mean (including insignificant results): 1.018x slower

# HPT report

- Reliability score: 99.95% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.02x