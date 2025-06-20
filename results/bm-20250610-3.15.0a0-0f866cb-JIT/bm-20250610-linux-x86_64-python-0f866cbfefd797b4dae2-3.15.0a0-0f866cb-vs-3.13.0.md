# Results vs. 3.13.0

- fork: python
- ref: 0f866cbfefd797b4dae2
- machine: linux-x86_64
- commit hash: 0f866cb
- commit date: 2025-06-10
- overall geometric mean: 1.051x faster
- HPT reliability: 99.32%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250610-linux-x86_64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 260 ms: 1.02x faster                                                  |
| docutils       | 2.58 sec                                               | 2.64 sec: 1.02x slower                                                |
| html5lib       | 63.4 ms                                                | 61.4 ms: 1.03x faster                                                 |
| sphinx         | 1.03 sec                                               | 1.02 sec: 1.02x faster                                                |
| Geometric mean | (ref)                                                  | 1.01x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250610-linux-x86_64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 314 ms: 1.47x faster                                                  |
| async_tree_io              | 838 ms                                                 | 598 ms: 1.40x faster                                                  |
| async_tree_io_tg           | 861 ms                                                 | 617 ms: 1.40x faster                                                  |
| async_tree_memoization     | 437 ms                                                 | 315 ms: 1.39x faster                                                  |
| async_tree_none            | 350 ms                                                 | 263 ms: 1.33x faster                                                  |
| async_tree_none_tg         | 319 ms                                                 | 249 ms: 1.28x faster                                                  |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 499 ms: 1.15x faster                                                  |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 490 ms: 1.11x faster                                                  |
| asyncio_websockets         | 551 ms                                                 | 553 ms: 1.00x slower                                                  |
| async_generators           | 433 ms                                                 | 441 ms: 1.02x slower                                                  |
| coroutines                 | 22.2 ms                                                | 25.1 ms: 1.13x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.20x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250610-linux-x86_64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 65.1 ms: 1.21x faster                                                 |
| pidigits       | 186 ms                                                 | 187 ms: 1.00x slower                                                  |
| nbody          | 87.7 ms                                                | 94.5 ms: 1.08x slower                                                 |
| Geometric mean | (ref)                                                  | 1.04x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250610-linux-x86_64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_v8       | 26.9 ms                                                | 22.4 ms: 1.20x faster                                                 |
| regex_effbot   | 3.77 ms                                                | 3.31 ms: 1.14x faster                                                 |
| regex_dna      | 220 ms                                                 | 200 ms: 1.10x faster                                                  |
| regex_compile  | 132 ms                                                 | 127 ms: 1.04x faster                                                  |
| Geometric mean | (ref)                                                  | 1.12x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250610-linux-x86_64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.90 sec: 1.11x faster                                                |
| xml_etree_parse      | 154 ms                                                 | 141 ms: 1.09x faster                                                  |
| xml_etree_generate   | 86.8 ms                                                | 80.0 ms: 1.09x faster                                                 |
| xml_etree_process    | 60.5 ms                                                | 56.0 ms: 1.08x faster                                                 |
| unpickle_pure_python | 213 us                                                 | 201 us: 1.06x faster                                                  |
| xml_etree_iterparse  | 101 ms                                                 | 98.5 ms: 1.03x faster                                                 |
| json_loads           | 27.2 us                                                | 28.4 us: 1.05x slower                                                 |
| pickle_pure_python   | 302 us                                                 | 322 us: 1.07x slower                                                  |
| json_dumps           | 10.1 ms                                                | 11.2 ms: 1.11x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250610-linux-x86_64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 12.2 ms: 1.04x faster                                                 |
| python_startup_no_site | 7.00 ms                                                | 6.96 ms: 1.01x faster                                                 |
| Geometric mean         | (ref)                                                  | 1.02x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250610-linux-x86_64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.1 ms: 1.07x faster                                                 |
| genshi_xml      | 50.5 ms                                                | 49.7 ms: 1.02x faster                                                 |
| mako            | 10.7 ms                                                | 10.6 ms: 1.01x faster                                                 |
| django_template | 31.7 ms                                                | 32.5 ms: 1.03x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.02x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250610-linux-x86_64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.24 sec: 2.04x faster                                                |
| async_tree_memoization_tg  | 463 ms                                                 | 314 ms: 1.47x faster                                                  |
| richards                   | 47.5 ms                                                | 33.9 ms: 1.40x faster                                                 |
| async_tree_io              | 838 ms                                                 | 598 ms: 1.40x faster                                                  |
| async_tree_io_tg           | 861 ms                                                 | 617 ms: 1.40x faster                                                  |
| async_tree_memoization     | 437 ms                                                 | 315 ms: 1.39x faster                                                  |
| deepcopy                   | 354 us                                                 | 258 us: 1.38x faster                                                  |
| richards_super             | 53.7 ms                                                | 39.9 ms: 1.35x faster                                                 |
| async_tree_none            | 350 ms                                                 | 263 ms: 1.33x faster                                                  |
| deepcopy_memo              | 38.4 us                                                | 29.5 us: 1.30x faster                                                 |
| async_tree_none_tg         | 319 ms                                                 | 249 ms: 1.28x faster                                                  |
| float                      | 78.7 ms                                                | 65.1 ms: 1.21x faster                                                 |
| deepcopy_reduce            | 3.24 us                                                | 2.69 us: 1.20x faster                                                 |
| regex_v8                   | 26.9 ms                                                | 22.4 ms: 1.20x faster                                                 |
| go                         | 141 ms                                                 | 122 ms: 1.15x faster                                                  |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 499 ms: 1.15x faster                                                  |
| pyflate                    | 470 ms                                                 | 412 ms: 1.14x faster                                                  |
| regex_effbot               | 3.77 ms                                                | 3.31 ms: 1.14x faster                                                 |
| spectral_norm              | 113 ms                                                 | 101 ms: 1.12x faster                                                  |
| tomli_loads                | 2.12 sec                                               | 1.90 sec: 1.11x faster                                                |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 490 ms: 1.11x faster                                                  |
| pylint                     | 312 ms                                                 | 283 ms: 1.10x faster                                                  |
| regex_dna                  | 220 ms                                                 | 200 ms: 1.10x faster                                                  |
| scimark_fft                | 367 ms                                                 | 335 ms: 1.10x faster                                                  |
| xml_etree_parse            | 154 ms                                                 | 141 ms: 1.09x faster                                                  |
| xml_etree_generate         | 86.8 ms                                                | 80.0 ms: 1.09x faster                                                 |
| xml_etree_process          | 60.5 ms                                                | 56.0 ms: 1.08x faster                                                 |
| pycparser                  | 1.20 sec                                               | 1.12 sec: 1.07x faster                                                |
| genshi_text                | 22.6 ms                                                | 21.1 ms: 1.07x faster                                                 |
| dulwich_log                | 64.6 ms                                                | 60.6 ms: 1.07x faster                                                 |
| unpickle_pure_python       | 213 us                                                 | 201 us: 1.06x faster                                                  |
| bpe_tokeniser              | 4.69 sec                                               | 4.42 sec: 1.06x faster                                                |
| telco                      | 8.40 ms                                                | 7.92 ms: 1.06x faster                                                 |
| regex_compile              | 132 ms                                                 | 127 ms: 1.04x faster                                                  |
| sqlite_synth               | 2.90 us                                                | 2.80 us: 1.04x faster                                                 |
| python_startup             | 12.7 ms                                                | 12.2 ms: 1.04x faster                                                 |
| html5lib                   | 63.4 ms                                                | 61.4 ms: 1.03x faster                                                 |
| pathlib                    | 17.4 ms                                                | 16.9 ms: 1.03x faster                                                 |
| xml_etree_iterparse        | 101 ms                                                 | 98.5 ms: 1.03x faster                                                 |
| deltablue                  | 3.19 ms                                                | 3.11 ms: 1.03x faster                                                 |
| k_core                     | 2.37 sec                                               | 2.31 sec: 1.03x faster                                                |
| 2to3                       | 266 ms                                                 | 260 ms: 1.02x faster                                                  |
| thrift                     | 800 us                                                 | 783 us: 1.02x faster                                                  |
| sympy_integrate            | 19.8 ms                                                | 19.4 ms: 1.02x faster                                                 |
| json                       | 5.32 ms                                                | 5.24 ms: 1.02x faster                                                 |
| sphinx                     | 1.03 sec                                               | 1.02 sec: 1.02x faster                                                |
| genshi_xml                 | 50.5 ms                                                | 49.7 ms: 1.02x faster                                                 |
| mako                       | 10.7 ms                                                | 10.6 ms: 1.01x faster                                                 |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 5.00 ms: 1.01x faster                                                 |
| python_startup_no_site     | 7.00 ms                                                | 6.96 ms: 1.01x faster                                                 |
| scimark_sor                | 122 ms                                                 | 122 ms: 1.00x faster                                                  |
| sympy_sum                  | 150 ms                                                 | 150 ms: 1.00x faster                                                  |
| pidigits                   | 186 ms                                                 | 187 ms: 1.00x slower                                                  |
| asyncio_websockets         | 551 ms                                                 | 553 ms: 1.00x slower                                                  |
| gc_traversal               | 4.90 ms                                                | 4.92 ms: 1.00x slower                                                 |
| scimark_monte_carlo        | 66.8 ms                                                | 67.5 ms: 1.01x slower                                                 |
| shortest_path              | 487 ms                                                 | 492 ms: 1.01x slower                                                  |
| crypto_pyaes               | 74.7 ms                                                | 75.8 ms: 1.02x slower                                                 |
| async_generators           | 433 ms                                                 | 441 ms: 1.02x slower                                                  |
| docutils                   | 2.58 sec                                               | 2.64 sec: 1.02x slower                                                |
| connected_components       | 447 ms                                                 | 458 ms: 1.02x slower                                                  |
| django_template            | 31.7 ms                                                | 32.5 ms: 1.03x slower                                                 |
| scimark_lu                 | 114 ms                                                 | 117 ms: 1.03x slower                                                  |
| sympy_expand               | 456 ms                                                 | 468 ms: 1.03x slower                                                  |
| nqueens                    | 80.9 ms                                                | 83.9 ms: 1.04x slower                                                 |
| comprehensions             | 16.5 us                                                | 17.1 us: 1.04x slower                                                 |
| fannkuch                   | 394 ms                                                 | 411 ms: 1.05x slower                                                  |
| json_loads                 | 27.2 us                                                | 28.4 us: 1.05x slower                                                 |
| raytrace                   | 262 ms                                                 | 275 ms: 1.05x slower                                                  |
| create_gc_cycles           | 2.45 ms                                                | 2.59 ms: 1.06x slower                                                 |
| coverage                   | 82.8 ms                                                | 87.7 ms: 1.06x slower                                                 |
| pickle_pure_python         | 302 us                                                 | 322 us: 1.07x slower                                                  |
| typing_runtime_protocols   | 160 us                                                 | 171 us: 1.07x slower                                                  |
| chaos                      | 58.0 ms                                                | 62.2 ms: 1.07x slower                                                 |
| hexiom                     | 6.08 ms                                                | 6.52 ms: 1.07x slower                                                 |
| logging_format             | 6.23 us                                                | 6.69 us: 1.07x slower                                                 |
| logging_simple             | 5.65 us                                                | 6.08 us: 1.08x slower                                                 |
| nbody                      | 87.7 ms                                                | 94.5 ms: 1.08x slower                                                 |
| generators                 | 28.8 ms                                                | 31.0 ms: 1.08x slower                                                 |
| json_dumps                 | 10.1 ms                                                | 11.2 ms: 1.11x slower                                                 |
| coroutines                 | 22.2 ms                                                | 25.1 ms: 1.13x slower                                                 |
| pprint_safe_repr           | 727 ms                                                 | 825 ms: 1.14x slower                                                  |
| pprint_pformat             | 1.48 sec                                               | 1.68 sec: 1.14x slower                                                |
| many_optionals             | 857 us                                                 | 984 us: 1.15x slower                                                  |
| subparsers                 | 15.5 ms                                                | 23.8 ms: 1.54x slower                                                 |
| logging_silent             | 101 ns                                                 | 470 ns: 4.65x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                          |

Benchmark hidden because not significant (3): meteor_contest, sympy_str, djangocms
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250610-3.15.0a0-0f866cb-JIT/bm-20250610-linux-x86_64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.051x faster

# HPT report

- Reliability score: 99.32% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.07x