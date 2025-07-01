# Results vs. 3.13.0

- fork: brandtbucher
- ref: jit_up_11_8
- machine: linux-x86_64
- commit hash: 10bb0c5
- commit date: 2025-06-30
- overall geometric mean: 1.063x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250630-linux-x86_64-brandtbucher-jit_up_11_8-3.15.0a0-10bb0c5 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 261 ms: 1.02x faster                                               |
| docutils       | 2.58 sec                                               | 2.64 sec: 1.02x slower                                             |
| html5lib       | 63.4 ms                                                | 62.4 ms: 1.01x faster                                              |
| sphinx         | 1.03 sec                                               | 1.02 sec: 1.01x faster                                             |
| Geometric mean | (ref)                                                  | 1.01x faster                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250630-linux-x86_64-brandtbucher-jit_up_11_8-3.15.0a0-10bb0c5 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 311 ms: 1.49x faster                                               |
| async_tree_memoization     | 437 ms                                                 | 312 ms: 1.40x faster                                               |
| async_tree_io              | 838 ms                                                 | 601 ms: 1.40x faster                                               |
| async_tree_io_tg           | 861 ms                                                 | 639 ms: 1.35x faster                                               |
| async_tree_none            | 350 ms                                                 | 262 ms: 1.34x faster                                               |
| async_tree_none_tg         | 319 ms                                                 | 249 ms: 1.28x faster                                               |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 493 ms: 1.16x faster                                               |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 485 ms: 1.12x faster                                               |
| async_generators           | 433 ms                                                 | 428 ms: 1.01x faster                                               |
| coroutines                 | 22.2 ms                                                | 25.3 ms: 1.14x slower                                              |
| Geometric mean             | (ref)                                                  | 1.20x faster                                                       |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250630-linux-x86_64-brandtbucher-jit_up_11_8-3.15.0a0-10bb0c5 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 65.4 ms: 1.20x faster                                              |
| pidigits       | 186 ms                                                 | 188 ms: 1.01x slower                                               |
| nbody          | 87.7 ms                                                | 93.1 ms: 1.06x slower                                              |
| Geometric mean | (ref)                                                  | 1.04x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250630-linux-x86_64-brandtbucher-jit_up_11_8-3.15.0a0-10bb0c5 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_v8       | 26.9 ms                                                | 22.8 ms: 1.18x faster                                              |
| regex_effbot   | 3.77 ms                                                | 3.42 ms: 1.10x faster                                              |
| regex_dna      | 220 ms                                                 | 208 ms: 1.06x faster                                               |
| regex_compile  | 132 ms                                                 | 127 ms: 1.04x faster                                               |
| Geometric mean | (ref)                                                  | 1.09x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250630-linux-x86_64-brandtbucher-jit_up_11_8-3.15.0a0-10bb0c5 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.80 sec: 1.18x faster                                             |
| unpickle_pure_python | 213 us                                                 | 192 us: 1.11x faster                                               |
| xml_etree_parse      | 154 ms                                                 | 141 ms: 1.09x faster                                               |
| xml_etree_process    | 60.5 ms                                                | 56.3 ms: 1.07x faster                                              |
| xml_etree_generate   | 86.8 ms                                                | 80.9 ms: 1.07x faster                                              |
| xml_etree_iterparse  | 101 ms                                                 | 98.2 ms: 1.03x faster                                              |
| json_loads           | 27.2 us                                                | 28.7 us: 1.06x slower                                              |
| pickle_pure_python   | 302 us                                                 | 324 us: 1.07x slower                                               |
| json_dumps           | 10.1 ms                                                | 11.1 ms: 1.10x slower                                              |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250630-linux-x86_64-brandtbucher-jit_up_11_8-3.15.0a0-10bb0c5 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 12.2 ms: 1.04x faster                                              |
| python_startup_no_site | 7.00 ms                                                | 6.94 ms: 1.01x faster                                              |
| Geometric mean         | (ref)                                                  | 1.02x faster                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250630-linux-x86_64-brandtbucher-jit_up_11_8-3.15.0a0-10bb0c5 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.2 ms: 1.06x faster                                              |
| mako            | 10.7 ms                                                | 10.5 ms: 1.02x faster                                              |
| genshi_xml      | 50.5 ms                                                | 49.7 ms: 1.02x faster                                              |
| django_template | 31.7 ms                                                | 33.1 ms: 1.04x slower                                              |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                       |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250630-linux-x86_64-brandtbucher-jit_up_11_8-3.15.0a0-10bb0c5 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.24 sec: 2.06x faster                                             |
| async_tree_memoization_tg  | 463 ms                                                 | 311 ms: 1.49x faster                                               |
| async_tree_memoization     | 437 ms                                                 | 312 ms: 1.40x faster                                               |
| async_tree_io              | 838 ms                                                 | 601 ms: 1.40x faster                                               |
| deepcopy                   | 354 us                                                 | 260 us: 1.37x faster                                               |
| async_tree_io_tg           | 861 ms                                                 | 639 ms: 1.35x faster                                               |
| async_tree_none            | 350 ms                                                 | 262 ms: 1.34x faster                                               |
| richards_super             | 53.7 ms                                                | 40.7 ms: 1.32x faster                                              |
| richards                   | 47.5 ms                                                | 36.2 ms: 1.31x faster                                              |
| deepcopy_memo              | 38.4 us                                                | 29.6 us: 1.30x faster                                              |
| async_tree_none_tg         | 319 ms                                                 | 249 ms: 1.28x faster                                               |
| spectral_norm              | 113 ms                                                 | 90.1 ms: 1.26x faster                                              |
| deepcopy_reduce            | 3.24 us                                                | 2.68 us: 1.21x faster                                              |
| float                      | 78.7 ms                                                | 65.4 ms: 1.20x faster                                              |
| go                         | 141 ms                                                 | 117 ms: 1.20x faster                                               |
| scimark_fft                | 367 ms                                                 | 307 ms: 1.19x faster                                               |
| regex_v8                   | 26.9 ms                                                | 22.8 ms: 1.18x faster                                              |
| tomli_loads                | 2.12 sec                                               | 1.80 sec: 1.18x faster                                             |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 493 ms: 1.16x faster                                               |
| pyflate                    | 470 ms                                                 | 410 ms: 1.14x faster                                               |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 485 ms: 1.12x faster                                               |
| unpickle_pure_python       | 213 us                                                 | 192 us: 1.11x faster                                               |
| pylint                     | 312 ms                                                 | 283 ms: 1.10x faster                                               |
| regex_effbot               | 3.77 ms                                                | 3.42 ms: 1.10x faster                                              |
| xml_etree_parse            | 154 ms                                                 | 141 ms: 1.09x faster                                               |
| telco                      | 8.40 ms                                                | 7.70 ms: 1.09x faster                                              |
| dulwich_log                | 64.6 ms                                                | 59.3 ms: 1.09x faster                                              |
| xml_etree_process          | 60.5 ms                                                | 56.3 ms: 1.07x faster                                              |
| xml_etree_generate         | 86.8 ms                                                | 80.9 ms: 1.07x faster                                              |
| bpe_tokeniser              | 4.69 sec                                               | 4.38 sec: 1.07x faster                                             |
| genshi_text                | 22.6 ms                                                | 21.2 ms: 1.06x faster                                              |
| regex_dna                  | 220 ms                                                 | 208 ms: 1.06x faster                                               |
| crypto_pyaes               | 74.7 ms                                                | 70.8 ms: 1.05x faster                                              |
| sqlite_synth               | 2.90 us                                                | 2.77 us: 1.05x faster                                              |
| thrift                     | 800 us                                                 | 766 us: 1.04x faster                                               |
| deltablue                  | 3.19 ms                                                | 3.06 ms: 1.04x faster                                              |
| regex_compile              | 132 ms                                                 | 127 ms: 1.04x faster                                               |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.84 ms: 1.04x faster                                              |
| pycparser                  | 1.20 sec                                               | 1.16 sec: 1.04x faster                                             |
| python_startup             | 12.7 ms                                                | 12.2 ms: 1.04x faster                                              |
| k_core                     | 2.37 sec                                               | 2.29 sec: 1.03x faster                                             |
| xml_etree_iterparse        | 101 ms                                                 | 98.2 ms: 1.03x faster                                              |
| scimark_monte_carlo        | 66.8 ms                                                | 65.0 ms: 1.03x faster                                              |
| scimark_sor                | 122 ms                                                 | 119 ms: 1.03x faster                                               |
| meteor_contest             | 108 ms                                                 | 106 ms: 1.02x faster                                               |
| 2to3                       | 266 ms                                                 | 261 ms: 1.02x faster                                               |
| pathlib                    | 17.4 ms                                                | 17.0 ms: 1.02x faster                                              |
| mako                       | 10.7 ms                                                | 10.5 ms: 1.02x faster                                              |
| sympy_integrate            | 19.8 ms                                                | 19.5 ms: 1.02x faster                                              |
| genshi_xml                 | 50.5 ms                                                | 49.7 ms: 1.02x faster                                              |
| html5lib                   | 63.4 ms                                                | 62.4 ms: 1.01x faster                                              |
| sphinx                     | 1.03 sec                                               | 1.02 sec: 1.01x faster                                             |
| async_generators           | 433 ms                                                 | 428 ms: 1.01x faster                                               |
| comprehensions             | 16.5 us                                                | 16.3 us: 1.01x faster                                              |
| python_startup_no_site     | 7.00 ms                                                | 6.94 ms: 1.01x faster                                              |
| fannkuch                   | 394 ms                                                 | 395 ms: 1.00x slower                                               |
| sympy_sum                  | 150 ms                                                 | 152 ms: 1.01x slower                                               |
| pidigits                   | 186 ms                                                 | 188 ms: 1.01x slower                                               |
| shortest_path              | 487 ms                                                 | 493 ms: 1.01x slower                                               |
| hexiom                     | 6.08 ms                                                | 6.16 ms: 1.01x slower                                              |
| gc_traversal               | 4.90 ms                                                | 4.98 ms: 1.02x slower                                              |
| docutils                   | 2.58 sec                                               | 2.64 sec: 1.02x slower                                             |
| sympy_expand               | 456 ms                                                 | 466 ms: 1.02x slower                                               |
| scimark_lu                 | 114 ms                                                 | 117 ms: 1.03x slower                                               |
| connected_components       | 447 ms                                                 | 461 ms: 1.03x slower                                               |
| raytrace                   | 262 ms                                                 | 271 ms: 1.03x slower                                               |
| logging_silent             | 101 ns                                                 | 105 ns: 1.04x slower                                               |
| typing_runtime_protocols   | 160 us                                                 | 167 us: 1.04x slower                                               |
| django_template            | 31.7 ms                                                | 33.1 ms: 1.04x slower                                              |
| json_loads                 | 27.2 us                                                | 28.7 us: 1.06x slower                                              |
| create_gc_cycles           | 2.45 ms                                                | 2.59 ms: 1.06x slower                                              |
| coverage                   | 82.8 ms                                                | 87.9 ms: 1.06x slower                                              |
| nbody                      | 87.7 ms                                                | 93.1 ms: 1.06x slower                                              |
| chaos                      | 58.0 ms                                                | 61.6 ms: 1.06x slower                                              |
| pickle_pure_python         | 302 us                                                 | 324 us: 1.07x slower                                               |
| json_dumps                 | 10.1 ms                                                | 11.1 ms: 1.10x slower                                              |
| generators                 | 28.8 ms                                                | 31.6 ms: 1.10x slower                                              |
| coroutines                 | 22.2 ms                                                | 25.3 ms: 1.14x slower                                              |
| many_optionals             | 857 us                                                 | 988 us: 1.15x slower                                               |
| subparsers                 | 15.5 ms                                                | 23.7 ms: 1.53x slower                                              |
| Geometric mean             | (ref)                                                  | 1.06x faster                                                       |

Benchmark hidden because not significant (9): sympy_str, nqueens, logging_simple, logging_format, asyncio_websockets, djangocms, pprint_safe_repr, json, pprint_pformat
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250630-3.15.0a0-10bb0c5-JIT/bm-20250630-linux-x86_64-brandtbucher-jit_up_11_8-3.15.0a0-10bb0c5.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.063x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.07x