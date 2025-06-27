# Results vs. 3.13.0

- fork: python
- ref: 8fdbbf8b18f1405abe67
- machine: linux-x86_64
- commit hash: 8fdbbf8
- commit date: 2025-06-07
- overall geometric mean: 1.048x faster
- HPT reliability: 99.15%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 259 ms: 1.02x faster                                                  |
| docutils       | 2.58 sec                                               | 2.65 sec: 1.03x slower                                                |
| html5lib       | 63.4 ms                                                | 62.7 ms: 1.01x faster                                                 |
| Geometric mean | (ref)                                                  | 1.01x faster                                                          |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 314 ms: 1.48x faster                                                  |
| async_tree_io_tg           | 861 ms                                                 | 613 ms: 1.40x faster                                                  |
| async_tree_memoization     | 437 ms                                                 | 312 ms: 1.40x faster                                                  |
| async_tree_io              | 838 ms                                                 | 599 ms: 1.40x faster                                                  |
| async_tree_none            | 350 ms                                                 | 261 ms: 1.34x faster                                                  |
| async_tree_none_tg         | 319 ms                                                 | 249 ms: 1.28x faster                                                  |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 489 ms: 1.17x faster                                                  |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 482 ms: 1.13x faster                                                  |
| async_generators           | 433 ms                                                 | 437 ms: 1.01x slower                                                  |
| coroutines                 | 22.2 ms                                                | 25.5 ms: 1.15x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.21x faster                                                          |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 64.1 ms: 1.23x faster                                                 |
| pidigits       | 186 ms                                                 | 187 ms: 1.00x slower                                                  |
| nbody          | 87.7 ms                                                | 91.9 ms: 1.05x slower                                                 |
| Geometric mean | (ref)                                                  | 1.05x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_v8       | 26.9 ms                                                | 23.3 ms: 1.15x faster                                                 |
| regex_effbot   | 3.77 ms                                                | 3.36 ms: 1.12x faster                                                 |
| regex_compile  | 132 ms                                                 | 128 ms: 1.03x faster                                                  |
| regex_dna      | 220 ms                                                 | 215 ms: 1.02x faster                                                  |
| Geometric mean | (ref)                                                  | 1.08x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.91 sec: 1.11x faster                                                |
| xml_etree_parse      | 154 ms                                                 | 140 ms: 1.10x faster                                                  |
| xml_etree_process    | 60.5 ms                                                | 56.0 ms: 1.08x faster                                                 |
| xml_etree_generate   | 86.8 ms                                                | 80.8 ms: 1.07x faster                                                 |
| unpickle_pure_python | 213 us                                                 | 203 us: 1.05x faster                                                  |
| xml_etree_iterparse  | 101 ms                                                 | 97.8 ms: 1.04x faster                                                 |
| json_loads           | 27.2 us                                                | 28.8 us: 1.06x slower                                                 |
| pickle_pure_python   | 302 us                                                 | 322 us: 1.06x slower                                                  |
| json_dumps           | 10.1 ms                                                | 11.0 ms: 1.08x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 12.2 ms: 1.04x faster                                                 |
| python_startup_no_site | 7.00 ms                                                | 6.94 ms: 1.01x faster                                                 |
| Geometric mean         | (ref)                                                  | 1.02x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.4 ms: 1.06x faster                                                 |
| genshi_xml      | 50.5 ms                                                | 50.2 ms: 1.01x faster                                                 |
| django_template | 31.7 ms                                                | 32.4 ms: 1.02x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                          |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.24 sec: 2.04x faster                                                |
| async_tree_memoization_tg  | 463 ms                                                 | 314 ms: 1.48x faster                                                  |
| async_tree_io_tg           | 861 ms                                                 | 613 ms: 1.40x faster                                                  |
| async_tree_memoization     | 437 ms                                                 | 312 ms: 1.40x faster                                                  |
| async_tree_io              | 838 ms                                                 | 599 ms: 1.40x faster                                                  |
| richards                   | 47.5 ms                                                | 34.1 ms: 1.40x faster                                                 |
| deepcopy                   | 354 us                                                 | 256 us: 1.39x faster                                                  |
| richards_super             | 53.7 ms                                                | 39.8 ms: 1.35x faster                                                 |
| async_tree_none            | 350 ms                                                 | 261 ms: 1.34x faster                                                  |
| deepcopy_memo              | 38.4 us                                                | 29.9 us: 1.28x faster                                                 |
| async_tree_none_tg         | 319 ms                                                 | 249 ms: 1.28x faster                                                  |
| float                      | 78.7 ms                                                | 64.1 ms: 1.23x faster                                                 |
| deepcopy_reduce            | 3.24 us                                                | 2.66 us: 1.22x faster                                                 |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 489 ms: 1.17x faster                                                  |
| regex_v8                   | 26.9 ms                                                | 23.3 ms: 1.15x faster                                                 |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 482 ms: 1.13x faster                                                  |
| pyflate                    | 470 ms                                                 | 417 ms: 1.13x faster                                                  |
| go                         | 141 ms                                                 | 125 ms: 1.12x faster                                                  |
| regex_effbot               | 3.77 ms                                                | 3.36 ms: 1.12x faster                                                 |
| tomli_loads                | 2.12 sec                                               | 1.91 sec: 1.11x faster                                                |
| xml_etree_parse            | 154 ms                                                 | 140 ms: 1.10x faster                                                  |
| pylint                     | 312 ms                                                 | 283 ms: 1.10x faster                                                  |
| scimark_fft                | 367 ms                                                 | 336 ms: 1.09x faster                                                  |
| dulwich_log                | 64.6 ms                                                | 59.4 ms: 1.09x faster                                                 |
| xml_etree_process          | 60.5 ms                                                | 56.0 ms: 1.08x faster                                                 |
| spectral_norm              | 113 ms                                                 | 105 ms: 1.08x faster                                                  |
| xml_etree_generate         | 86.8 ms                                                | 80.8 ms: 1.07x faster                                                 |
| telco                      | 8.40 ms                                                | 7.82 ms: 1.07x faster                                                 |
| genshi_text                | 22.6 ms                                                | 21.4 ms: 1.06x faster                                                 |
| bpe_tokeniser              | 4.69 sec                                               | 4.43 sec: 1.06x faster                                                |
| thrift                     | 800 us                                                 | 764 us: 1.05x faster                                                  |
| unpickle_pure_python       | 213 us                                                 | 203 us: 1.05x faster                                                  |
| python_startup             | 12.7 ms                                                | 12.2 ms: 1.04x faster                                                 |
| k_core                     | 2.37 sec                                               | 2.28 sec: 1.04x faster                                                |
| sqlite_synth               | 2.90 us                                                | 2.80 us: 1.04x faster                                                 |
| xml_etree_iterparse        | 101 ms                                                 | 97.8 ms: 1.04x faster                                                 |
| pycparser                  | 1.20 sec                                               | 1.16 sec: 1.03x faster                                                |
| regex_compile              | 132 ms                                                 | 128 ms: 1.03x faster                                                  |
| sympy_integrate            | 19.8 ms                                                | 19.3 ms: 1.03x faster                                                 |
| 2to3                       | 266 ms                                                 | 259 ms: 1.02x faster                                                  |
| regex_dna                  | 220 ms                                                 | 215 ms: 1.02x faster                                                  |
| deltablue                  | 3.19 ms                                                | 3.13 ms: 1.02x faster                                                 |
| meteor_contest             | 108 ms                                                 | 107 ms: 1.01x faster                                                  |
| html5lib                   | 63.4 ms                                                | 62.7 ms: 1.01x faster                                                 |
| python_startup_no_site     | 7.00 ms                                                | 6.94 ms: 1.01x faster                                                 |
| sympy_str                  | 273 ms                                                 | 271 ms: 1.01x faster                                                  |
| genshi_xml                 | 50.5 ms                                                | 50.2 ms: 1.01x faster                                                 |
| scimark_sor                | 122 ms                                                 | 121 ms: 1.01x faster                                                  |
| sympy_sum                  | 150 ms                                                 | 150 ms: 1.00x faster                                                  |
| pidigits                   | 186 ms                                                 | 187 ms: 1.00x slower                                                  |
| async_generators           | 433 ms                                                 | 437 ms: 1.01x slower                                                  |
| gc_traversal               | 4.90 ms                                                | 4.94 ms: 1.01x slower                                                 |
| shortest_path              | 487 ms                                                 | 492 ms: 1.01x slower                                                  |
| crypto_pyaes               | 74.7 ms                                                | 75.7 ms: 1.01x slower                                                 |
| sympy_expand               | 456 ms                                                 | 465 ms: 1.02x slower                                                  |
| scimark_monte_carlo        | 66.8 ms                                                | 68.1 ms: 1.02x slower                                                 |
| scimark_lu                 | 114 ms                                                 | 117 ms: 1.02x slower                                                  |
| django_template            | 31.7 ms                                                | 32.4 ms: 1.02x slower                                                 |
| connected_components       | 447 ms                                                 | 458 ms: 1.02x slower                                                  |
| docutils                   | 2.58 sec                                               | 2.65 sec: 1.03x slower                                                |
| nqueens                    | 80.9 ms                                                | 83.7 ms: 1.03x slower                                                 |
| comprehensions             | 16.5 us                                                | 17.2 us: 1.04x slower                                                 |
| nbody                      | 87.7 ms                                                | 91.9 ms: 1.05x slower                                                 |
| typing_runtime_protocols   | 160 us                                                 | 169 us: 1.05x slower                                                  |
| raytrace                   | 262 ms                                                 | 276 ms: 1.05x slower                                                  |
| create_gc_cycles           | 2.45 ms                                                | 2.58 ms: 1.06x slower                                                 |
| coverage                   | 82.8 ms                                                | 87.5 ms: 1.06x slower                                                 |
| json_loads                 | 27.2 us                                                | 28.8 us: 1.06x slower                                                 |
| fannkuch                   | 394 ms                                                 | 418 ms: 1.06x slower                                                  |
| pickle_pure_python         | 302 us                                                 | 322 us: 1.06x slower                                                  |
| hexiom                     | 6.08 ms                                                | 6.47 ms: 1.07x slower                                                 |
| chaos                      | 58.0 ms                                                | 62.3 ms: 1.07x slower                                                 |
| json_dumps                 | 10.1 ms                                                | 11.0 ms: 1.08x slower                                                 |
| logging_simple             | 5.65 us                                                | 6.14 us: 1.09x slower                                                 |
| logging_format             | 6.23 us                                                | 6.77 us: 1.09x slower                                                 |
| generators                 | 28.8 ms                                                | 31.5 ms: 1.09x slower                                                 |
| pprint_safe_repr           | 727 ms                                                 | 830 ms: 1.14x slower                                                  |
| pprint_pformat             | 1.48 sec                                               | 1.69 sec: 1.15x slower                                                |
| coroutines                 | 22.2 ms                                                | 25.5 ms: 1.15x slower                                                 |
| many_optionals             | 857 us                                                 | 982 us: 1.15x slower                                                  |
| subparsers                 | 15.5 ms                                                | 23.5 ms: 1.52x slower                                                 |
| logging_silent             | 101 ns                                                 | 479 ns: 4.74x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                          |

Benchmark hidden because not significant (7): sphinx, json, pathlib, scimark_sparse_mat_mult, mako, asyncio_websockets, djangocms
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250607-3.15.0a0-8fdbbf8-JIT/bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.048x faster

# HPT report

- Reliability score: 99.15% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.07x