# Results vs. base

- fork: python
- ref: 16cd6cc86b3ba20074ae
- machine: linux-aarch64
- commit hash: 16cd6cc
- commit date: 2024-10-05
- overall geometric mean: 1.107x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x slower
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20241005-3.14.0a0-16cd6cc/bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc.json | results/bm-20241005-3.14.0a0-16cd6cc-JIT/bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 294 ms                                                                                                            | 383 ms: 1.30x slower                                                                                                  |
| docutils       | 3.01 sec                                                                                                          | 3.71 sec: 1.23x slower                                                                                                |
| html5lib       | 64.8 ms                                                                                                           | 71.0 ms: 1.10x slower                                                                                                 |
| tornado_http   | 129 ms                                                                                                            | 147 ms: 1.14x slower                                                                                                  |
| Geometric mean | (ref)                                                                                                             | 1.19x slower                                                                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20241005-3.14.0a0-16cd6cc/bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc.json | results/bm-20241005-3.14.0a0-16cd6cc-JIT/bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc.json |
|----------------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| coroutines                 | 28.5 ms                                                                                                           | 29.0 ms: 1.02x slower                                                                                                 |
| async_tree_memoization_tg  | 552 ms                                                                                                            | 561 ms: 1.02x slower                                                                                                  |
| async_tree_cpu_io_mixed_tg | 721 ms                                                                                                            | 739 ms: 1.02x slower                                                                                                  |
| async_tree_cpu_io_mixed    | 728 ms                                                                                                            | 753 ms: 1.03x slower                                                                                                  |
| asyncio_tcp_ssl            | 2.20 sec                                                                                                          | 2.27 sec: 1.03x slower                                                                                                |
| async_tree_none            | 424 ms                                                                                                            | 445 ms: 1.05x slower                                                                                                  |
| async_tree_memoization     | 555 ms                                                                                                            | 591 ms: 1.06x slower                                                                                                  |
| async_generators           | 476 ms                                                                                                            | 508 ms: 1.07x slower                                                                                                  |
| asyncio_tcp                | 559 ms                                                                                                            | 611 ms: 1.09x slower                                                                                                  |
| Geometric mean             | (ref)                                                                                                             | 1.03x slower                                                                                                          |

Benchmark hidden because not significant (4): async_tree_io, async_tree_io_tg, asyncio_websockets, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20241005-3.14.0a0-16cd6cc/bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc.json | results/bm-20241005-3.14.0a0-16cd6cc-JIT/bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| float          | 93.0 ms                                                                                                           | 90.0 ms: 1.03x faster                                                                                                 |
| Geometric mean | (ref)                                                                                                             | 1.01x faster                                                                                                          |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20241005-3.14.0a0-16cd6cc/bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc.json | results/bm-20241005-3.14.0a0-16cd6cc-JIT/bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| regex_dna      | 259 ms                                                                                                            | 262 ms: 1.01x slower                                                                                                  |
| regex_compile  | 126 ms                                                                                                            | 184 ms: 1.46x slower                                                                                                  |
| Geometric mean | (ref)                                                                                                             | 1.11x slower                                                                                                          |

Benchmark hidden because not significant (2): regex_effbot, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20241005-3.14.0a0-16cd6cc/bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc.json | results/bm-20241005-3.14.0a0-16cd6cc-JIT/bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc.json |
|----------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| unpickle_list        | 6.59 us                                                                                                           | 6.37 us: 1.03x faster                                                                                                 |
| unpickle             | 19.5 us                                                                                                           | 19.2 us: 1.01x faster                                                                                                 |
| json_dumps           | 13.2 ms                                                                                                           | 13.1 ms: 1.01x faster                                                                                                 |
| pickle_list          | 5.27 us                                                                                                           | 5.21 us: 1.01x faster                                                                                                 |
| pickle_dict          | 37.4 us                                                                                                           | 37.7 us: 1.01x slower                                                                                                 |
| unpickle_pure_python | 254 us                                                                                                            | 268 us: 1.06x slower                                                                                                  |
| pickle_pure_python   | 362 us                                                                                                            | 386 us: 1.07x slower                                                                                                  |
| Geometric mean       | (ref)                                                                                                             | 1.01x slower                                                                                                          |

Benchmark hidden because not significant (7): xml_etree_generate, json_loads, pickle, tomli_loads, xml_etree_parse, xml_etree_iterparse, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20241005-3.14.0a0-16cd6cc/bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc.json | results/bm-20241005-3.14.0a0-16cd6cc-JIT/bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc.json |
|------------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| python_startup_no_site | 8.61 ms                                                                                                           | 8.73 ms: 1.01x slower                                                                                                 |
| Geometric mean         | (ref)                                                                                                             | 1.01x slower                                                                                                          |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20241005-3.14.0a0-16cd6cc/bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc.json | results/bm-20241005-3.14.0a0-16cd6cc-JIT/bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc.json |
|-----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| mako            | 13.8 ms                                                                                                           | 13.0 ms: 1.06x faster                                                                                                 |
| django_template | 42.2 ms                                                                                                           | 51.8 ms: 1.23x slower                                                                                                 |
| genshi_text     | 27.5 ms                                                                                                           | 34.4 ms: 1.25x slower                                                                                                 |
| genshi_xml      | 60.6 ms                                                                                                           | 83.1 ms: 1.37x slower                                                                                                 |
| Geometric mean  | (ref)                                                                                                             | 1.19x slower                                                                                                          |

All benchmarks:
===============

| Benchmark                  | results/bm-20241005-3.14.0a0-16cd6cc/bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc.json | results/bm-20241005-3.14.0a0-16cd6cc-JIT/bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc.json |
|----------------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| bench_mp_pool              | 4.42 sec                                                                                                          | 2.07 sec: 2.14x faster                                                                                                |
| mako                       | 13.8 ms                                                                                                           | 13.0 ms: 1.06x faster                                                                                                 |
| unpickle_list              | 6.59 us                                                                                                           | 6.37 us: 1.03x faster                                                                                                 |
| scimark_sor                | 157 ms                                                                                                            | 152 ms: 1.03x faster                                                                                                  |
| float                      | 93.0 ms                                                                                                           | 90.0 ms: 1.03x faster                                                                                                 |
| unpickle                   | 19.5 us                                                                                                           | 19.2 us: 1.01x faster                                                                                                 |
| json_dumps                 | 13.2 ms                                                                                                           | 13.1 ms: 1.01x faster                                                                                                 |
| pickle_list                | 5.27 us                                                                                                           | 5.21 us: 1.01x faster                                                                                                 |
| pickle_dict                | 37.4 us                                                                                                           | 37.7 us: 1.01x slower                                                                                                 |
| regex_dna                  | 259 ms                                                                                                            | 262 ms: 1.01x slower                                                                                                  |
| python_startup_no_site     | 8.61 ms                                                                                                           | 8.73 ms: 1.01x slower                                                                                                 |
| coroutines                 | 28.5 ms                                                                                                           | 29.0 ms: 1.02x slower                                                                                                 |
| spectral_norm              | 142 ms                                                                                                            | 145 ms: 1.02x slower                                                                                                  |
| async_tree_memoization_tg  | 552 ms                                                                                                            | 561 ms: 1.02x slower                                                                                                  |
| bpe_tokeniser              | 5.85 sec                                                                                                          | 5.97 sec: 1.02x slower                                                                                                |
| async_tree_cpu_io_mixed_tg | 721 ms                                                                                                            | 739 ms: 1.02x slower                                                                                                  |
| sqlite_synth               | 3.81 us                                                                                                           | 3.91 us: 1.03x slower                                                                                                 |
| pathlib                    | 21.2 ms                                                                                                           | 21.8 ms: 1.03x slower                                                                                                 |
| telco                      | 9.45 ms                                                                                                           | 9.75 ms: 1.03x slower                                                                                                 |
| async_tree_cpu_io_mixed    | 728 ms                                                                                                            | 753 ms: 1.03x slower                                                                                                  |
| asyncio_tcp_ssl            | 2.20 sec                                                                                                          | 2.27 sec: 1.03x slower                                                                                                |
| scimark_fft                | 427 ms                                                                                                            | 446 ms: 1.04x slower                                                                                                  |
| mdp                        | 3.33 sec                                                                                                          | 3.48 sec: 1.04x slower                                                                                                |
| thrift                     | 920 us                                                                                                            | 960 us: 1.04x slower                                                                                                  |
| logging_format             | 7.72 us                                                                                                           | 8.11 us: 1.05x slower                                                                                                 |
| async_tree_none            | 424 ms                                                                                                            | 445 ms: 1.05x slower                                                                                                  |
| unpickle_pure_python       | 254 us                                                                                                            | 268 us: 1.06x slower                                                                                                  |
| bench_thread_pool          | 1.30 ms                                                                                                           | 1.37 ms: 1.06x slower                                                                                                 |
| logging_simple             | 7.11 us                                                                                                           | 7.54 us: 1.06x slower                                                                                                 |
| async_tree_memoization     | 555 ms                                                                                                            | 591 ms: 1.06x slower                                                                                                  |
| async_generators           | 476 ms                                                                                                            | 508 ms: 1.07x slower                                                                                                  |
| pickle_pure_python         | 362 us                                                                                                            | 386 us: 1.07x slower                                                                                                  |
| fannkuch                   | 468 ms                                                                                                            | 503 ms: 1.08x slower                                                                                                  |
| scimark_monte_carlo        | 82.8 ms                                                                                                           | 89.1 ms: 1.08x slower                                                                                                 |
| scimark_sparse_mat_mult    | 6.37 ms                                                                                                           | 6.87 ms: 1.08x slower                                                                                                 |
| asyncio_tcp                | 559 ms                                                                                                            | 611 ms: 1.09x slower                                                                                                  |
| crypto_pyaes               | 82.0 ms                                                                                                           | 89.9 ms: 1.10x slower                                                                                                 |
| html5lib                   | 64.8 ms                                                                                                           | 71.0 ms: 1.10x slower                                                                                                 |
| meteor_contest             | 112 ms                                                                                                            | 124 ms: 1.10x slower                                                                                                  |
| typing_runtime_protocols   | 193 us                                                                                                            | 213 us: 1.10x slower                                                                                                  |
| pyflate                    | 579 ms                                                                                                            | 640 ms: 1.11x slower                                                                                                  |
| deltablue                  | 3.92 ms                                                                                                           | 4.35 ms: 1.11x slower                                                                                                 |
| deepcopy_reduce            | 3.52 us                                                                                                           | 3.93 us: 1.11x slower                                                                                                 |
| scimark_lu                 | 133 ms                                                                                                            | 150 ms: 1.13x slower                                                                                                  |
| tornado_http               | 129 ms                                                                                                            | 147 ms: 1.14x slower                                                                                                  |
| raytrace                   | 305 ms                                                                                                            | 350 ms: 1.15x slower                                                                                                  |
| deepcopy                   | 335 us                                                                                                            | 400 us: 1.20x slower                                                                                                  |
| pycparser                  | 1.23 sec                                                                                                          | 1.48 sec: 1.20x slower                                                                                                |
| richards                   | 53.0 ms                                                                                                           | 63.8 ms: 1.20x slower                                                                                                 |
| comprehensions             | 20.6 us                                                                                                           | 24.9 us: 1.21x slower                                                                                                 |
| sqlglot_parse              | 1.43 ms                                                                                                           | 1.74 ms: 1.21x slower                                                                                                 |
| richards_super             | 59.3 ms                                                                                                           | 72.0 ms: 1.21x slower                                                                                                 |
| sqlglot_normalize          | 127 ms                                                                                                            | 156 ms: 1.22x slower                                                                                                  |
| django_template            | 42.2 ms                                                                                                           | 51.8 ms: 1.23x slower                                                                                                 |
| docutils                   | 3.01 sec                                                                                                          | 3.71 sec: 1.23x slower                                                                                                |
| genshi_text                | 27.5 ms                                                                                                           | 34.4 ms: 1.25x slower                                                                                                 |
| nqueens                    | 98.0 ms                                                                                                           | 124 ms: 1.27x slower                                                                                                  |
| sqlglot_transpile          | 1.73 ms                                                                                                           | 2.21 ms: 1.28x slower                                                                                                 |
| 2to3                       | 294 ms                                                                                                            | 383 ms: 1.30x slower                                                                                                  |
| chaos                      | 69.4 ms                                                                                                           | 90.5 ms: 1.30x slower                                                                                                 |
| sqlglot_optimize           | 62.9 ms                                                                                                           | 82.2 ms: 1.31x slower                                                                                                 |
| sympy_expand               | 457 ms                                                                                                            | 598 ms: 1.31x slower                                                                                                  |
| go                         | 138 ms                                                                                                            | 185 ms: 1.34x slower                                                                                                  |
| pprint_safe_repr           | 907 ms                                                                                                            | 1.23 sec: 1.36x slower                                                                                                |
| dulwich_log                | 58.6 ms                                                                                                           | 80.1 ms: 1.37x slower                                                                                                 |
| genshi_xml                 | 60.6 ms                                                                                                           | 83.1 ms: 1.37x slower                                                                                                 |
| pylint                     | 354 ms                                                                                                            | 486 ms: 1.37x slower                                                                                                  |
| pprint_pformat             | 1.89 sec                                                                                                          | 2.61 sec: 1.38x slower                                                                                                |
| sympy_str                  | 263 ms                                                                                                            | 366 ms: 1.39x slower                                                                                                  |
| sympy_integrate            | 20.9 ms                                                                                                           | 29.6 ms: 1.41x slower                                                                                                 |
| hexiom                     | 7.11 ms                                                                                                           | 10.1 ms: 1.42x slower                                                                                                 |
| regex_compile              | 126 ms                                                                                                            | 184 ms: 1.46x slower                                                                                                  |
| sympy_sum                  | 140 ms                                                                                                            | 218 ms: 1.56x slower                                                                                                  |
| generators                 | 34.7 ms                                                                                                           | 59.2 ms: 1.70x slower                                                                                                 |
| unpack_sequence            | 57.1 ns                                                                                                           | 144 ns: 2.53x slower                                                                                                  |
| Geometric mean             | (ref)                                                                                                             | 1.11x slower                                                                                                          |

Benchmark hidden because not significant (22): deepcopy_memo, async_tree_io, xml_etree_generate, pidigits, json_loads, async_tree_io_tg, pickle, python_startup, tomli_loads, regex_effbot, gc_traversal, asyncio_websockets, create_gc_cycles, logging_silent, json, regex_v8, xml_etree_parse, xml_etree_iterparse, nbody, coverage, xml_etree_process, async_tree_none_tg

- Geometric mean (including insignificant results): 1.107x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.05x
- 99% likely to have a slowdown of 1.04x

# Memory
- memory change: 1.06x