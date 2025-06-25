# Results vs. 3.13.0

- fork: python
- ref: fea5ccc55d8486300beb
- machine: linux-x86_64
- commit hash: fea5ccc
- commit date: 2025-06-24
- overall geometric mean: 1.054x faster
- HPT reliability: 99.51%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250624-linux-x86_64-python-fea5ccc55d8486300beb-3.15.0a0-fea5ccc |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 260 ms: 1.02x faster                                                  |
| docutils       | 2.58 sec                                               | 2.63 sec: 1.02x slower                                                |
| html5lib       | 63.4 ms                                                | 62.0 ms: 1.02x faster                                                 |
| sphinx         | 1.03 sec                                               | 1.01 sec: 1.02x faster                                                |
| Geometric mean | (ref)                                                  | 1.01x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250624-linux-x86_64-python-fea5ccc55d8486300beb-3.15.0a0-fea5ccc |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 317 ms: 1.46x faster                                                  |
| async_tree_io_tg           | 861 ms                                                 | 616 ms: 1.40x faster                                                  |
| async_tree_memoization     | 437 ms                                                 | 314 ms: 1.39x faster                                                  |
| async_tree_io              | 838 ms                                                 | 603 ms: 1.39x faster                                                  |
| async_tree_none            | 350 ms                                                 | 261 ms: 1.34x faster                                                  |
| async_tree_none_tg         | 319 ms                                                 | 251 ms: 1.27x faster                                                  |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 502 ms: 1.14x faster                                                  |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 492 ms: 1.11x faster                                                  |
| coroutines                 | 22.2 ms                                                | 24.9 ms: 1.12x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.20x faster                                                          |

Benchmark hidden because not significant (2): async_generators, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250624-linux-x86_64-python-fea5ccc55d8486300beb-3.15.0a0-fea5ccc |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 66.2 ms: 1.19x faster                                                 |
| pidigits       | 186 ms                                                 | 188 ms: 1.01x slower                                                  |
| nbody          | 87.7 ms                                                | 97.5 ms: 1.11x slower                                                 |
| Geometric mean | (ref)                                                  | 1.02x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250624-linux-x86_64-python-fea5ccc55d8486300beb-3.15.0a0-fea5ccc |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_v8       | 26.9 ms                                                | 22.1 ms: 1.22x faster                                                 |
| regex_effbot   | 3.77 ms                                                | 3.17 ms: 1.19x faster                                                 |
| regex_dna      | 220 ms                                                 | 200 ms: 1.10x faster                                                  |
| regex_compile  | 132 ms                                                 | 128 ms: 1.03x faster                                                  |
| Geometric mean | (ref)                                                  | 1.13x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250624-linux-x86_64-python-fea5ccc55d8486300beb-3.15.0a0-fea5ccc |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.82 sec: 1.16x faster                                                |
| xml_etree_parse      | 154 ms                                                 | 140 ms: 1.10x faster                                                  |
| xml_etree_generate   | 86.8 ms                                                | 80.3 ms: 1.08x faster                                                 |
| xml_etree_process    | 60.5 ms                                                | 56.2 ms: 1.08x faster                                                 |
| unpickle_pure_python | 213 us                                                 | 202 us: 1.06x faster                                                  |
| xml_etree_iterparse  | 101 ms                                                 | 98.7 ms: 1.03x faster                                                 |
| json_loads           | 27.2 us                                                | 28.1 us: 1.03x slower                                                 |
| pickle_pure_python   | 302 us                                                 | 323 us: 1.07x slower                                                  |
| json_dumps           | 10.1 ms                                                | 11.1 ms: 1.09x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250624-linux-x86_64-python-fea5ccc55d8486300beb-3.15.0a0-fea5ccc |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 12.2 ms: 1.04x faster                                                 |
| python_startup_no_site | 7.00 ms                                                | 6.95 ms: 1.01x faster                                                 |
| Geometric mean         | (ref)                                                  | 1.02x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250624-linux-x86_64-python-fea5ccc55d8486300beb-3.15.0a0-fea5ccc |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.7 ms: 1.04x faster                                                 |
| genshi_xml      | 50.5 ms                                                | 51.4 ms: 1.02x slower                                                 |
| mako            | 10.7 ms                                                | 11.0 ms: 1.03x slower                                                 |
| django_template | 31.7 ms                                                | 32.6 ms: 1.03x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.01x slower                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250624-linux-x86_64-python-fea5ccc55d8486300beb-3.15.0a0-fea5ccc |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.24 sec: 2.04x faster                                                |
| async_tree_memoization_tg  | 463 ms                                                 | 317 ms: 1.46x faster                                                  |
| richards                   | 47.5 ms                                                | 33.2 ms: 1.43x faster                                                 |
| async_tree_io_tg           | 861 ms                                                 | 616 ms: 1.40x faster                                                  |
| async_tree_memoization     | 437 ms                                                 | 314 ms: 1.39x faster                                                  |
| async_tree_io              | 838 ms                                                 | 603 ms: 1.39x faster                                                  |
| richards_super             | 53.7 ms                                                | 39.2 ms: 1.37x faster                                                 |
| deepcopy                   | 354 us                                                 | 260 us: 1.36x faster                                                  |
| async_tree_none            | 350 ms                                                 | 261 ms: 1.34x faster                                                  |
| deepcopy_memo              | 38.4 us                                                | 29.3 us: 1.31x faster                                                 |
| async_tree_none_tg         | 319 ms                                                 | 251 ms: 1.27x faster                                                  |
| regex_v8                   | 26.9 ms                                                | 22.1 ms: 1.22x faster                                                 |
| spectral_norm              | 113 ms                                                 | 94.8 ms: 1.19x faster                                                 |
| float                      | 78.7 ms                                                | 66.2 ms: 1.19x faster                                                 |
| regex_effbot               | 3.77 ms                                                | 3.17 ms: 1.19x faster                                                 |
| scimark_fft                | 367 ms                                                 | 314 ms: 1.17x faster                                                  |
| deepcopy_reduce            | 3.24 us                                                | 2.78 us: 1.17x faster                                                 |
| go                         | 141 ms                                                 | 121 ms: 1.16x faster                                                  |
| tomli_loads                | 2.12 sec                                               | 1.82 sec: 1.16x faster                                                |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 502 ms: 1.14x faster                                                  |
| pyflate                    | 470 ms                                                 | 420 ms: 1.12x faster                                                  |
| pylint                     | 312 ms                                                 | 282 ms: 1.11x faster                                                  |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 492 ms: 1.11x faster                                                  |
| xml_etree_parse            | 154 ms                                                 | 140 ms: 1.10x faster                                                  |
| regex_dna                  | 220 ms                                                 | 200 ms: 1.10x faster                                                  |
| dulwich_log                | 64.6 ms                                                | 59.4 ms: 1.09x faster                                                 |
| telco                      | 8.40 ms                                                | 7.73 ms: 1.09x faster                                                 |
| xml_etree_generate         | 86.8 ms                                                | 80.3 ms: 1.08x faster                                                 |
| xml_etree_process          | 60.5 ms                                                | 56.2 ms: 1.08x faster                                                 |
| pycparser                  | 1.20 sec                                               | 1.12 sec: 1.07x faster                                                |
| bpe_tokeniser              | 4.69 sec                                               | 4.42 sec: 1.06x faster                                                |
| unpickle_pure_python       | 213 us                                                 | 202 us: 1.06x faster                                                  |
| k_core                     | 2.37 sec                                               | 2.28 sec: 1.04x faster                                                |
| genshi_text                | 22.6 ms                                                | 21.7 ms: 1.04x faster                                                 |
| python_startup             | 12.7 ms                                                | 12.2 ms: 1.04x faster                                                 |
| sqlite_synth               | 2.90 us                                                | 2.80 us: 1.04x faster                                                 |
| thrift                     | 800 us                                                 | 774 us: 1.03x faster                                                  |
| regex_compile              | 132 ms                                                 | 128 ms: 1.03x faster                                                  |
| deltablue                  | 3.19 ms                                                | 3.10 ms: 1.03x faster                                                 |
| scimark_sor                | 122 ms                                                 | 119 ms: 1.03x faster                                                  |
| xml_etree_iterparse        | 101 ms                                                 | 98.7 ms: 1.03x faster                                                 |
| sympy_integrate            | 19.8 ms                                                | 19.3 ms: 1.02x faster                                                 |
| 2to3                       | 266 ms                                                 | 260 ms: 1.02x faster                                                  |
| meteor_contest             | 108 ms                                                 | 106 ms: 1.02x faster                                                  |
| html5lib                   | 63.4 ms                                                | 62.0 ms: 1.02x faster                                                 |
| pathlib                    | 17.4 ms                                                | 17.0 ms: 1.02x faster                                                 |
| djangocms                  | 22.3 us                                                | 21.8 us: 1.02x faster                                                 |
| sphinx                     | 1.03 sec                                               | 1.01 sec: 1.02x faster                                                |
| scimark_monte_carlo        | 66.8 ms                                                | 66.0 ms: 1.01x faster                                                 |
| python_startup_no_site     | 7.00 ms                                                | 6.95 ms: 1.01x faster                                                 |
| sympy_sum                  | 150 ms                                                 | 150 ms: 1.01x faster                                                  |
| gc_traversal               | 4.90 ms                                                | 4.93 ms: 1.01x slower                                                 |
| pidigits                   | 186 ms                                                 | 188 ms: 1.01x slower                                                  |
| genshi_xml                 | 50.5 ms                                                | 51.4 ms: 1.02x slower                                                 |
| connected_components       | 447 ms                                                 | 455 ms: 1.02x slower                                                  |
| docutils                   | 2.58 sec                                               | 2.63 sec: 1.02x slower                                                |
| fannkuch                   | 394 ms                                                 | 403 ms: 1.02x slower                                                  |
| mako                       | 10.7 ms                                                | 11.0 ms: 1.03x slower                                                 |
| crypto_pyaes               | 74.7 ms                                                | 76.8 ms: 1.03x slower                                                 |
| django_template            | 31.7 ms                                                | 32.6 ms: 1.03x slower                                                 |
| scimark_lu                 | 114 ms                                                 | 118 ms: 1.03x slower                                                  |
| sympy_expand               | 456 ms                                                 | 470 ms: 1.03x slower                                                  |
| json_loads                 | 27.2 us                                                | 28.1 us: 1.03x slower                                                 |
| typing_runtime_protocols   | 160 us                                                 | 166 us: 1.04x slower                                                  |
| shortest_path              | 487 ms                                                 | 504 ms: 1.04x slower                                                  |
| nqueens                    | 80.9 ms                                                | 83.9 ms: 1.04x slower                                                 |
| comprehensions             | 16.5 us                                                | 17.2 us: 1.04x slower                                                 |
| generators                 | 28.8 ms                                                | 30.3 ms: 1.05x slower                                                 |
| raytrace                   | 262 ms                                                 | 275 ms: 1.05x slower                                                  |
| coverage                   | 82.8 ms                                                | 87.5 ms: 1.06x slower                                                 |
| create_gc_cycles           | 2.45 ms                                                | 2.59 ms: 1.06x slower                                                 |
| chaos                      | 58.0 ms                                                | 61.6 ms: 1.06x slower                                                 |
| hexiom                     | 6.08 ms                                                | 6.49 ms: 1.07x slower                                                 |
| pickle_pure_python         | 302 us                                                 | 323 us: 1.07x slower                                                  |
| logging_simple             | 5.65 us                                                | 6.16 us: 1.09x slower                                                 |
| json_dumps                 | 10.1 ms                                                | 11.1 ms: 1.09x slower                                                 |
| logging_format             | 6.23 us                                                | 6.83 us: 1.10x slower                                                 |
| nbody                      | 87.7 ms                                                | 97.5 ms: 1.11x slower                                                 |
| coroutines                 | 22.2 ms                                                | 24.9 ms: 1.12x slower                                                 |
| pprint_safe_repr           | 727 ms                                                 | 822 ms: 1.13x slower                                                  |
| many_optionals             | 857 us                                                 | 978 us: 1.14x slower                                                  |
| pprint_pformat             | 1.48 sec                                               | 1.70 sec: 1.15x slower                                                |
| subparsers                 | 15.5 ms                                                | 23.9 ms: 1.55x slower                                                 |
| logging_silent             | 101 ns                                                 | 479 ns: 4.75x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.04x faster                                                          |

Benchmark hidden because not significant (5): json, sympy_str, scimark_sparse_mat_mult, async_generators, asyncio_websockets
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250624-3.15.0a0-fea5ccc-JIT/bm-20250624-linux-x86_64-python-fea5ccc55d8486300beb-3.15.0a0-fea5ccc.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.054x faster

# HPT report

- Reliability score: 99.51% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.07x