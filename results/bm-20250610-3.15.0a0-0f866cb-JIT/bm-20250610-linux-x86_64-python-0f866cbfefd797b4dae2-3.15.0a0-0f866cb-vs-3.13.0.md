# Results vs. 3.13.0

- fork: python
- ref: 0f866cbfefd797b4dae2
- machine: linux-x86_64
- commit hash: 0f866cb
- commit date: 2025-06-10
- overall geometric mean: 1.052x faster
- HPT reliability: 98.98%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250610-linux-x86_64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 261 ms: 1.02x faster                                                  |
| docutils       | 2.58 sec                                               | 2.64 sec: 1.02x slower                                                |
| html5lib       | 63.4 ms                                                | 61.5 ms: 1.03x faster                                                 |
| sphinx         | 1.03 sec                                               | 1.02 sec: 1.02x faster                                                |
| Geometric mean | (ref)                                                  | 1.01x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250610-linux-x86_64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 316 ms: 1.47x faster                                                  |
| async_tree_io_tg           | 861 ms                                                 | 614 ms: 1.40x faster                                                  |
| async_tree_io              | 838 ms                                                 | 598 ms: 1.40x faster                                                  |
| async_tree_memoization     | 437 ms                                                 | 314 ms: 1.39x faster                                                  |
| async_tree_none            | 350 ms                                                 | 262 ms: 1.34x faster                                                  |
| async_tree_none_tg         | 319 ms                                                 | 249 ms: 1.28x faster                                                  |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 491 ms: 1.17x faster                                                  |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 485 ms: 1.12x faster                                                  |
| async_generators           | 433 ms                                                 | 435 ms: 1.00x slower                                                  |
| coroutines                 | 22.2 ms                                                | 25.4 ms: 1.14x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.21x faster                                                          |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250610-linux-x86_64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 65.7 ms: 1.20x faster                                                 |
| pidigits       | 186 ms                                                 | 190 ms: 1.02x slower                                                  |
| nbody          | 87.7 ms                                                | 90.9 ms: 1.04x slower                                                 |
| Geometric mean | (ref)                                                  | 1.04x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250610-linux-x86_64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_v8       | 26.9 ms                                                | 21.5 ms: 1.25x faster                                                 |
| regex_effbot   | 3.77 ms                                                | 3.20 ms: 1.18x faster                                                 |
| regex_dna      | 220 ms                                                 | 196 ms: 1.12x faster                                                  |
| regex_compile  | 132 ms                                                 | 129 ms: 1.02x faster                                                  |
| Geometric mean | (ref)                                                  | 1.14x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250610-linux-x86_64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.90 sec: 1.11x faster                                                |
| xml_etree_parse      | 154 ms                                                 | 141 ms: 1.09x faster                                                  |
| xml_etree_process    | 60.5 ms                                                | 56.4 ms: 1.07x faster                                                 |
| xml_etree_generate   | 86.8 ms                                                | 81.3 ms: 1.07x faster                                                 |
| unpickle_pure_python | 213 us                                                 | 202 us: 1.06x faster                                                  |
| xml_etree_iterparse  | 101 ms                                                 | 98.4 ms: 1.03x faster                                                 |
| json_loads           | 27.2 us                                                | 28.7 us: 1.06x slower                                                 |
| pickle_pure_python   | 302 us                                                 | 323 us: 1.07x slower                                                  |
| json_dumps           | 10.1 ms                                                | 11.0 ms: 1.09x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250610-linux-x86_64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 12.2 ms: 1.04x faster                                                 |
| python_startup_no_site | 7.00 ms                                                | 6.95 ms: 1.01x faster                                                 |
| Geometric mean         | (ref)                                                  | 1.02x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250610-linux-x86_64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.3 ms: 1.06x faster                                                 |
| mako            | 10.7 ms                                                | 10.5 ms: 1.02x faster                                                 |
| genshi_xml      | 50.5 ms                                                | 50.0 ms: 1.01x faster                                                 |
| django_template | 31.7 ms                                                | 32.5 ms: 1.03x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250610-linux-x86_64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.24 sec: 2.04x faster                                                |
| async_tree_memoization_tg  | 463 ms                                                 | 316 ms: 1.47x faster                                                  |
| async_tree_io_tg           | 861 ms                                                 | 614 ms: 1.40x faster                                                  |
| async_tree_io              | 838 ms                                                 | 598 ms: 1.40x faster                                                  |
| async_tree_memoization     | 437 ms                                                 | 314 ms: 1.39x faster                                                  |
| richards                   | 47.5 ms                                                | 34.3 ms: 1.39x faster                                                 |
| deepcopy                   | 354 us                                                 | 258 us: 1.38x faster                                                  |
| richards_super             | 53.7 ms                                                | 39.9 ms: 1.35x faster                                                 |
| async_tree_none            | 350 ms                                                 | 262 ms: 1.34x faster                                                  |
| deepcopy_memo              | 38.4 us                                                | 29.8 us: 1.29x faster                                                 |
| async_tree_none_tg         | 319 ms                                                 | 249 ms: 1.28x faster                                                  |
| regex_v8                   | 26.9 ms                                                | 21.5 ms: 1.25x faster                                                 |
| deepcopy_reduce            | 3.24 us                                                | 2.70 us: 1.20x faster                                                 |
| float                      | 78.7 ms                                                | 65.7 ms: 1.20x faster                                                 |
| regex_effbot               | 3.77 ms                                                | 3.20 ms: 1.18x faster                                                 |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 491 ms: 1.17x faster                                                  |
| go                         | 141 ms                                                 | 124 ms: 1.13x faster                                                  |
| pyflate                    | 470 ms                                                 | 414 ms: 1.13x faster                                                  |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 485 ms: 1.12x faster                                                  |
| regex_dna                  | 220 ms                                                 | 196 ms: 1.12x faster                                                  |
| spectral_norm              | 113 ms                                                 | 101 ms: 1.12x faster                                                  |
| tomli_loads                | 2.12 sec                                               | 1.90 sec: 1.11x faster                                                |
| scimark_fft                | 367 ms                                                 | 330 ms: 1.11x faster                                                  |
| pylint                     | 312 ms                                                 | 283 ms: 1.10x faster                                                  |
| xml_etree_parse            | 154 ms                                                 | 141 ms: 1.09x faster                                                  |
| telco                      | 8.40 ms                                                | 7.73 ms: 1.09x faster                                                 |
| dulwich_log                | 64.6 ms                                                | 60.0 ms: 1.08x faster                                                 |
| xml_etree_process          | 60.5 ms                                                | 56.4 ms: 1.07x faster                                                 |
| xml_etree_generate         | 86.8 ms                                                | 81.3 ms: 1.07x faster                                                 |
| pycparser                  | 1.20 sec                                               | 1.13 sec: 1.07x faster                                                |
| genshi_text                | 22.6 ms                                                | 21.3 ms: 1.06x faster                                                 |
| unpickle_pure_python       | 213 us                                                 | 202 us: 1.06x faster                                                  |
| bpe_tokeniser              | 4.69 sec                                               | 4.45 sec: 1.05x faster                                                |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.84 ms: 1.04x faster                                                 |
| sqlite_synth               | 2.90 us                                                | 2.79 us: 1.04x faster                                                 |
| python_startup             | 12.7 ms                                                | 12.2 ms: 1.04x faster                                                 |
| k_core                     | 2.37 sec                                               | 2.29 sec: 1.03x faster                                                |
| html5lib                   | 63.4 ms                                                | 61.5 ms: 1.03x faster                                                 |
| xml_etree_iterparse        | 101 ms                                                 | 98.4 ms: 1.03x faster                                                 |
| gc_traversal               | 4.90 ms                                                | 4.78 ms: 1.02x faster                                                 |
| sympy_integrate            | 19.8 ms                                                | 19.4 ms: 1.02x faster                                                 |
| regex_compile              | 132 ms                                                 | 129 ms: 1.02x faster                                                  |
| 2to3                       | 266 ms                                                 | 261 ms: 1.02x faster                                                  |
| mako                       | 10.7 ms                                                | 10.5 ms: 1.02x faster                                                 |
| sphinx                     | 1.03 sec                                               | 1.02 sec: 1.02x faster                                                |
| thrift                     | 800 us                                                 | 787 us: 1.02x faster                                                  |
| pathlib                    | 17.4 ms                                                | 17.1 ms: 1.01x faster                                                 |
| genshi_xml                 | 50.5 ms                                                | 50.0 ms: 1.01x faster                                                 |
| deltablue                  | 3.19 ms                                                | 3.17 ms: 1.01x faster                                                 |
| python_startup_no_site     | 7.00 ms                                                | 6.95 ms: 1.01x faster                                                 |
| async_generators           | 433 ms                                                 | 435 ms: 1.00x slower                                                  |
| scimark_sor                | 122 ms                                                 | 123 ms: 1.01x slower                                                  |
| crypto_pyaes               | 74.7 ms                                                | 75.6 ms: 1.01x slower                                                 |
| connected_components       | 447 ms                                                 | 455 ms: 1.02x slower                                                  |
| pidigits                   | 186 ms                                                 | 190 ms: 1.02x slower                                                  |
| docutils                   | 2.58 sec                                               | 2.64 sec: 1.02x slower                                                |
| nqueens                    | 80.9 ms                                                | 82.9 ms: 1.02x slower                                                 |
| shortest_path              | 487 ms                                                 | 499 ms: 1.03x slower                                                  |
| sympy_expand               | 456 ms                                                 | 469 ms: 1.03x slower                                                  |
| django_template            | 31.7 ms                                                | 32.5 ms: 1.03x slower                                                 |
| comprehensions             | 16.5 us                                                | 17.1 us: 1.04x slower                                                 |
| nbody                      | 87.7 ms                                                | 90.9 ms: 1.04x slower                                                 |
| fannkuch                   | 394 ms                                                 | 412 ms: 1.05x slower                                                  |
| scimark_lu                 | 114 ms                                                 | 120 ms: 1.05x slower                                                  |
| coverage                   | 82.8 ms                                                | 87.2 ms: 1.05x slower                                                 |
| json_loads                 | 27.2 us                                                | 28.7 us: 1.06x slower                                                 |
| create_gc_cycles           | 2.45 ms                                                | 2.59 ms: 1.06x slower                                                 |
| typing_runtime_protocols   | 160 us                                                 | 170 us: 1.06x slower                                                  |
| raytrace                   | 262 ms                                                 | 278 ms: 1.06x slower                                                  |
| hexiom                     | 6.08 ms                                                | 6.47 ms: 1.07x slower                                                 |
| pickle_pure_python         | 302 us                                                 | 323 us: 1.07x slower                                                  |
| logging_simple             | 5.65 us                                                | 6.09 us: 1.08x slower                                                 |
| chaos                      | 58.0 ms                                                | 62.5 ms: 1.08x slower                                                 |
| logging_format             | 6.23 us                                                | 6.72 us: 1.08x slower                                                 |
| generators                 | 28.8 ms                                                | 31.1 ms: 1.08x slower                                                 |
| json_dumps                 | 10.1 ms                                                | 11.0 ms: 1.09x slower                                                 |
| coroutines                 | 22.2 ms                                                | 25.4 ms: 1.14x slower                                                 |
| many_optionals             | 857 us                                                 | 984 us: 1.15x slower                                                  |
| pprint_pformat             | 1.48 sec                                               | 1.70 sec: 1.15x slower                                                |
| pprint_safe_repr           | 727 ms                                                 | 840 ms: 1.16x slower                                                  |
| subparsers                 | 15.5 ms                                                | 23.7 ms: 1.53x slower                                                 |
| logging_silent             | 101 ns                                                 | 475 ns: 4.70x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                          |

Benchmark hidden because not significant (7): djangocms, json, meteor_contest, sympy_sum, asyncio_websockets, sympy_str, scimark_monte_carlo
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250610-3.15.0a0-0f866cb-JIT/bm-20250610-linux-x86_64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.052x faster

# HPT report

- Reliability score: 98.98% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.07x