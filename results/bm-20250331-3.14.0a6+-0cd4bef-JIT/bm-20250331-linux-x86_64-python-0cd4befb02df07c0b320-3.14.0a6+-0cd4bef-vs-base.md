# Results vs. base

- fork: python
- ref: 0cd4befb02df07c0b320
- machine: linux-x86_64
- commit hash: 0cd4bef
- commit date: 2025-03-31
- overall geometric mean: 1.004x faster
- HPT reliability: 99.88%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250331-3.14.0a6+-0cd4bef/bm-20250331-linux-x86_64-python-0cd4befb02df07c0b320-3.14.0a6+-0cd4bef.json | results/bm-20250331-3.14.0a6+-0cd4bef-JIT/bm-20250331-linux-x86_64-python-0cd4befb02df07c0b320-3.14.0a6+-0cd4bef.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 254 ms                                                                                                            | 262 ms: 1.03x slower                                                                                                  |
| docutils       | 2.60 sec                                                                                                          | 2.69 sec: 1.03x slower                                                                                                |
| sphinx         | 1.01 sec                                                                                                          | 1.03 sec: 1.02x slower                                                                                                |
| Geometric mean | (ref)                                                                                                             | 1.02x slower                                                                                                          |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20250331-3.14.0a6+-0cd4bef/bm-20250331-linux-x86_64-python-0cd4befb02df07c0b320-3.14.0a6+-0cd4bef.json | results/bm-20250331-3.14.0a6+-0cd4bef-JIT/bm-20250331-linux-x86_64-python-0cd4befb02df07c0b320-3.14.0a6+-0cd4bef.json |
|----------------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| async_tree_none_tg         | 249 ms                                                                                                            | 253 ms: 1.01x slower                                                                                                  |
| async_tree_cpu_io_mixed_tg | 474 ms                                                                                                            | 483 ms: 1.02x slower                                                                                                  |
| async_tree_cpu_io_mixed    | 483 ms                                                                                                            | 495 ms: 1.02x slower                                                                                                  |
| async_generators           | 389 ms                                                                                                            | 416 ms: 1.07x slower                                                                                                  |
| Geometric mean             | (ref)                                                                                                             | 1.01x slower                                                                                                          |

Benchmark hidden because not significant (7): async_tree_memoization, asyncio_websockets, coroutines, async_tree_io_tg, async_tree_io, async_tree_memoization_tg, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250331-3.14.0a6+-0cd4bef/bm-20250331-linux-x86_64-python-0cd4befb02df07c0b320-3.14.0a6+-0cd4bef.json | results/bm-20250331-3.14.0a6+-0cd4bef-JIT/bm-20250331-linux-x86_64-python-0cd4befb02df07c0b320-3.14.0a6+-0cd4bef.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| nbody          | 96.4 ms                                                                                                           | 85.6 ms: 1.13x faster                                                                                                 |
| float          | 69.3 ms                                                                                                           | 63.9 ms: 1.08x faster                                                                                                 |
| pidigits       | 187 ms                                                                                                            | 186 ms: 1.01x faster                                                                                                  |
| Geometric mean | (ref)                                                                                                             | 1.07x faster                                                                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250331-3.14.0a6+-0cd4bef/bm-20250331-linux-x86_64-python-0cd4befb02df07c0b320-3.14.0a6+-0cd4bef.json | results/bm-20250331-3.14.0a6+-0cd4bef-JIT/bm-20250331-linux-x86_64-python-0cd4befb02df07c0b320-3.14.0a6+-0cd4bef.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| regex_effbot   | 3.80 ms                                                                                                           | 3.37 ms: 1.13x faster                                                                                                 |
| regex_compile  | 127 ms                                                                                                            | 127 ms: 1.00x slower                                                                                                  |
| regex_dna      | 215 ms                                                                                                            | 218 ms: 1.01x slower                                                                                                  |
| Geometric mean | (ref)                                                                                                             | 1.03x faster                                                                                                          |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20250331-3.14.0a6+-0cd4bef/bm-20250331-linux-x86_64-python-0cd4befb02df07c0b320-3.14.0a6+-0cd4bef.json | results/bm-20250331-3.14.0a6+-0cd4bef-JIT/bm-20250331-linux-x86_64-python-0cd4befb02df07c0b320-3.14.0a6+-0cd4bef.json |
|----------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| xml_etree_generate   | 85.0 ms                                                                                                           | 79.8 ms: 1.06x faster                                                                                                 |
| tomli_loads          | 1.95 sec                                                                                                          | 1.85 sec: 1.06x faster                                                                                                |
| xml_etree_process    | 58.9 ms                                                                                                           | 56.2 ms: 1.05x faster                                                                                                 |
| unpickle_pure_python | 219 us                                                                                                            | 212 us: 1.03x faster                                                                                                  |
| xml_etree_iterparse  | 99.1 ms                                                                                                           | 97.4 ms: 1.02x faster                                                                                                 |
| json_loads           | 29.9 us                                                                                                           | 29.7 us: 1.01x faster                                                                                                 |
| pickle_pure_python   | 321 us                                                                                                            | 323 us: 1.01x slower                                                                                                  |
| Geometric mean       | (ref)                                                                                                             | 1.02x faster                                                                                                          |

Benchmark hidden because not significant (2): xml_etree_parse, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20250331-3.14.0a6+-0cd4bef/bm-20250331-linux-x86_64-python-0cd4befb02df07c0b320-3.14.0a6+-0cd4bef.json | results/bm-20250331-3.14.0a6+-0cd4bef-JIT/bm-20250331-linux-x86_64-python-0cd4befb02df07c0b320-3.14.0a6+-0cd4bef.json |
|------------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| python_startup_no_site | 8.16 ms                                                                                                           | 8.22 ms: 1.01x slower                                                                                                 |
| python_startup         | 13.1 ms                                                                                                           | 13.2 ms: 1.01x slower                                                                                                 |
| Geometric mean         | (ref)                                                                                                             | 1.01x slower                                                                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20250331-3.14.0a6+-0cd4bef/bm-20250331-linux-x86_64-python-0cd4befb02df07c0b320-3.14.0a6+-0cd4bef.json | results/bm-20250331-3.14.0a6+-0cd4bef-JIT/bm-20250331-linux-x86_64-python-0cd4befb02df07c0b320-3.14.0a6+-0cd4bef.json |
|-----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| mako            | 11.4 ms                                                                                                           | 11.0 ms: 1.03x faster                                                                                                 |
| genshi_text     | 21.5 ms                                                                                                           | 21.1 ms: 1.02x faster                                                                                                 |
| genshi_xml      | 49.6 ms                                                                                                           | 50.1 ms: 1.01x slower                                                                                                 |
| django_template | 31.9 ms                                                                                                           | 32.3 ms: 1.01x slower                                                                                                 |
| Geometric mean  | (ref)                                                                                                             | 1.01x faster                                                                                                          |

All benchmarks:
===============

| Benchmark                  | results/bm-20250331-3.14.0a6+-0cd4bef/bm-20250331-linux-x86_64-python-0cd4befb02df07c0b320-3.14.0a6+-0cd4bef.json | results/bm-20250331-3.14.0a6+-0cd4bef-JIT/bm-20250331-linux-x86_64-python-0cd4befb02df07c0b320-3.14.0a6+-0cd4bef.json |
|----------------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| richards                   | 44.9 ms                                                                                                           | 35.5 ms: 1.27x faster                                                                                                 |
| richards_super             | 50.6 ms                                                                                                           | 40.6 ms: 1.25x faster                                                                                                 |
| scimark_fft                | 355 ms                                                                                                            | 307 ms: 1.16x faster                                                                                                  |
| regex_effbot               | 3.80 ms                                                                                                           | 3.37 ms: 1.13x faster                                                                                                 |
| nbody                      | 96.4 ms                                                                                                           | 85.6 ms: 1.13x faster                                                                                                 |
| scimark_sparse_mat_mult    | 4.86 ms                                                                                                           | 4.49 ms: 1.08x faster                                                                                                 |
| float                      | 69.3 ms                                                                                                           | 63.9 ms: 1.08x faster                                                                                                 |
| xml_etree_generate         | 85.0 ms                                                                                                           | 79.8 ms: 1.06x faster                                                                                                 |
| tomli_loads                | 1.95 sec                                                                                                          | 1.85 sec: 1.06x faster                                                                                                |
| xml_etree_process          | 58.9 ms                                                                                                           | 56.2 ms: 1.05x faster                                                                                                 |
| pyflate                    | 449 ms                                                                                                            | 429 ms: 1.05x faster                                                                                                  |
| fannkuch                   | 426 ms                                                                                                            | 408 ms: 1.04x faster                                                                                                  |
| deltablue                  | 3.15 ms                                                                                                           | 3.03 ms: 1.04x faster                                                                                                 |
| mako                       | 11.4 ms                                                                                                           | 11.0 ms: 1.03x faster                                                                                                 |
| unpickle_pure_python       | 219 us                                                                                                            | 212 us: 1.03x faster                                                                                                  |
| sqlite_synth               | 2.81 us                                                                                                           | 2.72 us: 1.03x faster                                                                                                 |
| spectral_norm              | 96.3 ms                                                                                                           | 94.0 ms: 1.02x faster                                                                                                 |
| genshi_text                | 21.5 ms                                                                                                           | 21.1 ms: 1.02x faster                                                                                                 |
| xml_etree_iterparse        | 99.1 ms                                                                                                           | 97.4 ms: 1.02x faster                                                                                                 |
| generators                 | 28.6 ms                                                                                                           | 28.1 ms: 1.02x faster                                                                                                 |
| json                       | 5.35 ms                                                                                                           | 5.28 ms: 1.01x faster                                                                                                 |
| logging_silent             | 98.9 ns                                                                                                           | 97.8 ns: 1.01x faster                                                                                                 |
| deepcopy_reduce            | 2.70 us                                                                                                           | 2.67 us: 1.01x faster                                                                                                 |
| deepcopy                   | 258 us                                                                                                            | 255 us: 1.01x faster                                                                                                  |
| bpe_tokeniser              | 4.58 sec                                                                                                          | 4.54 sec: 1.01x faster                                                                                                |
| deepcopy_memo              | 30.0 us                                                                                                           | 29.8 us: 1.01x faster                                                                                                 |
| pidigits                   | 187 ms                                                                                                            | 186 ms: 1.01x faster                                                                                                  |
| json_loads                 | 29.9 us                                                                                                           | 29.7 us: 1.01x faster                                                                                                 |
| create_gc_cycles           | 2.50 ms                                                                                                           | 2.49 ms: 1.00x faster                                                                                                 |
| regex_compile              | 127 ms                                                                                                            | 127 ms: 1.00x slower                                                                                                  |
| raytrace                   | 266 ms                                                                                                            | 267 ms: 1.01x slower                                                                                                  |
| nqueens                    | 82.6 ms                                                                                                           | 83.1 ms: 1.01x slower                                                                                                 |
| python_startup_no_site     | 8.16 ms                                                                                                           | 8.22 ms: 1.01x slower                                                                                                 |
| bench_mp_pool              | 82.5 ms                                                                                                           | 83.1 ms: 1.01x slower                                                                                                 |
| python_startup             | 13.1 ms                                                                                                           | 13.2 ms: 1.01x slower                                                                                                 |
| gc_traversal               | 5.02 ms                                                                                                           | 5.06 ms: 1.01x slower                                                                                                 |
| pickle_pure_python         | 321 us                                                                                                            | 323 us: 1.01x slower                                                                                                  |
| crypto_pyaes               | 73.8 ms                                                                                                           | 74.5 ms: 1.01x slower                                                                                                 |
| logging_format             | 6.21 us                                                                                                           | 6.28 us: 1.01x slower                                                                                                 |
| genshi_xml                 | 49.6 ms                                                                                                           | 50.1 ms: 1.01x slower                                                                                                 |
| scimark_lu                 | 115 ms                                                                                                            | 116 ms: 1.01x slower                                                                                                  |
| mdp                        | 1.24 sec                                                                                                          | 1.25 sec: 1.01x slower                                                                                                |
| regex_dna                  | 215 ms                                                                                                            | 218 ms: 1.01x slower                                                                                                  |
| connected_components       | 447 ms                                                                                                            | 453 ms: 1.01x slower                                                                                                  |
| django_template            | 31.9 ms                                                                                                           | 32.3 ms: 1.01x slower                                                                                                 |
| coverage                   | 84.3 ms                                                                                                           | 85.4 ms: 1.01x slower                                                                                                 |
| async_tree_none_tg         | 249 ms                                                                                                            | 253 ms: 1.01x slower                                                                                                  |
| subparsers                 | 20.8 ms                                                                                                           | 21.1 ms: 1.01x slower                                                                                                 |
| pycparser                  | 1.17 sec                                                                                                          | 1.19 sec: 1.01x slower                                                                                                |
| bench_thread_pool          | 872 us                                                                                                            | 885 us: 1.02x slower                                                                                                  |
| sphinx                     | 1.01 sec                                                                                                          | 1.03 sec: 1.02x slower                                                                                                |
| sqlalchemy_declarative     | 130 ms                                                                                                            | 133 ms: 1.02x slower                                                                                                  |
| meteor_contest             | 105 ms                                                                                                            | 107 ms: 1.02x slower                                                                                                  |
| scimark_sor                | 119 ms                                                                                                            | 121 ms: 1.02x slower                                                                                                  |
| sympy_sum                  | 148 ms                                                                                                            | 151 ms: 1.02x slower                                                                                                  |
| async_tree_cpu_io_mixed_tg | 474 ms                                                                                                            | 483 ms: 1.02x slower                                                                                                  |
| k_core                     | 2.27 sec                                                                                                          | 2.32 sec: 1.02x slower                                                                                                |
| sympy_integrate            | 19.2 ms                                                                                                           | 19.6 ms: 1.02x slower                                                                                                 |
| sympy_str                  | 268 ms                                                                                                            | 274 ms: 1.02x slower                                                                                                  |
| sqlglot_v2_parse           | 1.25 ms                                                                                                           | 1.27 ms: 1.02x slower                                                                                                 |
| pathlib                    | 16.3 ms                                                                                                           | 16.7 ms: 1.02x slower                                                                                                 |
| sqlglot_v2_transpile       | 1.56 ms                                                                                                           | 1.60 ms: 1.02x slower                                                                                                 |
| many_optionals             | 947 us                                                                                                            | 971 us: 1.02x slower                                                                                                  |
| async_tree_cpu_io_mixed    | 483 ms                                                                                                            | 495 ms: 1.02x slower                                                                                                  |
| chaos                      | 58.1 ms                                                                                                           | 59.5 ms: 1.03x slower                                                                                                 |
| sqlglot_v2_optimize        | 53.1 ms                                                                                                           | 54.4 ms: 1.03x slower                                                                                                 |
| sqlglot_v2_normalize       | 107 ms                                                                                                            | 110 ms: 1.03x slower                                                                                                  |
| sympy_expand               | 461 ms                                                                                                            | 475 ms: 1.03x slower                                                                                                  |
| sqlalchemy_imperative      | 16.6 ms                                                                                                           | 17.2 ms: 1.03x slower                                                                                                 |
| 2to3                       | 254 ms                                                                                                            | 262 ms: 1.03x slower                                                                                                  |
| docutils                   | 2.60 sec                                                                                                          | 2.69 sec: 1.03x slower                                                                                                |
| dulwich_log                | 58.4 ms                                                                                                           | 60.5 ms: 1.03x slower                                                                                                 |
| typing_runtime_protocols   | 161 us                                                                                                            | 170 us: 1.05x slower                                                                                                  |
| pprint_pformat             | 1.48 sec                                                                                                          | 1.57 sec: 1.06x slower                                                                                                |
| pprint_safe_repr           | 726 ms                                                                                                            | 773 ms: 1.06x slower                                                                                                  |
| async_generators           | 389 ms                                                                                                            | 416 ms: 1.07x slower                                                                                                  |
| hexiom                     | 6.25 ms                                                                                                           | 6.81 ms: 1.09x slower                                                                                                 |
| go                         | 115 ms                                                                                                            | 126 ms: 1.10x slower                                                                                                  |
| comprehensions             | 16.7 us                                                                                                           | 18.5 us: 1.11x slower                                                                                                 |
| Geometric mean             | (ref)                                                                                                             | 1.00x faster                                                                                                          |

Benchmark hidden because not significant (16): logging_simple, async_tree_memoization, scimark_monte_carlo, asyncio_websockets, shortest_path, regex_v8, coroutines, async_tree_io_tg, xml_etree_parse, json_dumps, telco, async_tree_io, async_tree_memoization_tg, html5lib, async_tree_none, pylint

- Geometric mean (including insignificant results): 1.004x faster

# HPT report

- Reliability score: 99.88% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.01x