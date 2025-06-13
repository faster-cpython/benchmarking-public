# Results vs. 3.13.0

- fork: Fidget-Spinner
- ref: pylong_compactadd
- machine: linux-x86_64
- commit hash: 4019a15
- commit date: 2025-06-14
- overall geometric mean: 1.033x slower
- HPT reliability: 99.84%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250614-linux-x86_64-Fidget%2dSpinner-pylong_compactadd-3.15.0a0-4019a15 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 254 ms: 1.05x faster                                                         |
| docutils       | 2.58 sec                                               | 2.57 sec: 1.01x faster                                                       |
| html5lib       | 63.4 ms                                                | 61.7 ms: 1.03x faster                                                        |
| sphinx         | 1.03 sec                                               | 1.00 sec: 1.03x faster                                                       |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250614-linux-x86_64-Fidget%2dSpinner-pylong_compactadd-3.15.0a0-4019a15 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 310 ms: 1.49x faster                                                         |
| async_tree_io              | 838 ms                                                 | 599 ms: 1.40x faster                                                         |
| async_tree_memoization     | 437 ms                                                 | 313 ms: 1.40x faster                                                         |
| async_tree_io_tg           | 861 ms                                                 | 633 ms: 1.36x faster                                                         |
| async_tree_none            | 350 ms                                                 | 261 ms: 1.34x faster                                                         |
| async_tree_none_tg         | 319 ms                                                 | 247 ms: 1.29x faster                                                         |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 487 ms: 1.18x faster                                                         |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 478 ms: 1.14x faster                                                         |
| async_generators           | 433 ms                                                 | 418 ms: 1.04x faster                                                         |
| coroutines                 | 22.2 ms                                                | 24.5 ms: 1.10x slower                                                        |
| Geometric mean             | (ref)                                                  | 1.22x faster                                                                 |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250614-linux-x86_64-Fidget%2dSpinner-pylong_compactadd-3.15.0a0-4019a15 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 72.4 ms: 1.09x faster                                                        |
| pidigits       | 186 ms                                                 | 189 ms: 1.01x slower                                                         |
| nbody          | 87.7 ms                                                | 97.5 ms: 1.11x slower                                                        |
| Geometric mean | (ref)                                                  | 1.01x slower                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250614-linux-x86_64-Fidget%2dSpinner-pylong_compactadd-3.15.0a0-4019a15 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.06 ms: 1.23x faster                                                        |
| regex_v8       | 26.9 ms                                                | 22.1 ms: 1.22x faster                                                        |
| regex_dna      | 220 ms                                                 | 183 ms: 1.20x faster                                                         |
| regex_compile  | 132 ms                                                 | 127 ms: 1.04x faster                                                         |
| Geometric mean | (ref)                                                  | 1.17x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250614-linux-x86_64-Fidget%2dSpinner-pylong_compactadd-3.15.0a0-4019a15 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 143 ms: 1.08x faster                                                         |
| tomli_loads          | 2.12 sec                                               | 2.01 sec: 1.05x faster                                                       |
| xml_etree_iterparse  | 101 ms                                                 | 98.5 ms: 1.03x faster                                                        |
| xml_etree_generate   | 86.8 ms                                                | 85.5 ms: 1.02x faster                                                        |
| xml_etree_process    | 60.5 ms                                                | 60.0 ms: 1.01x faster                                                        |
| unpickle_pure_python | 213 us                                                 | 217 us: 1.02x slower                                                         |
| json_loads           | 27.2 us                                                | 28.2 us: 1.04x slower                                                        |
| pickle_pure_python   | 302 us                                                 | 320 us: 1.06x slower                                                         |
| json_dumps           | 10.1 ms                                                | 11.0 ms: 1.09x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.00x slower                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250614-linux-x86_64-Fidget%2dSpinner-pylong_compactadd-3.15.0a0-4019a15 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 12.1 ms: 1.04x faster                                                        |
| python_startup_no_site | 7.00 ms                                                | 6.90 ms: 1.01x faster                                                        |
| Geometric mean         | (ref)                                                  | 1.03x faster                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250614-linux-x86_64-Fidget%2dSpinner-pylong_compactadd-3.15.0a0-4019a15 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.1 ms: 1.07x faster                                                        |
| genshi_xml      | 50.5 ms                                                | 49.2 ms: 1.03x faster                                                        |
| django_template | 31.7 ms                                                | 32.6 ms: 1.03x slower                                                        |
| mako            | 10.7 ms                                                | 11.8 ms: 1.10x slower                                                        |
| Geometric mean  | (ref)                                                  | 1.01x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250614-linux-x86_64-Fidget%2dSpinner-pylong_compactadd-3.15.0a0-4019a15 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.22 sec: 2.08x faster                                                       |
| async_tree_memoization_tg  | 463 ms                                                 | 310 ms: 1.49x faster                                                         |
| async_tree_io              | 838 ms                                                 | 599 ms: 1.40x faster                                                         |
| deepcopy                   | 354 us                                                 | 254 us: 1.40x faster                                                         |
| async_tree_memoization     | 437 ms                                                 | 313 ms: 1.40x faster                                                         |
| async_tree_io_tg           | 861 ms                                                 | 633 ms: 1.36x faster                                                         |
| async_tree_none            | 350 ms                                                 | 261 ms: 1.34x faster                                                         |
| deepcopy_memo              | 38.4 us                                                | 29.2 us: 1.32x faster                                                        |
| async_tree_none_tg         | 319 ms                                                 | 247 ms: 1.29x faster                                                         |
| go                         | 141 ms                                                 | 111 ms: 1.27x faster                                                         |
| regex_effbot               | 3.77 ms                                                | 3.06 ms: 1.23x faster                                                        |
| regex_v8                   | 26.9 ms                                                | 22.1 ms: 1.22x faster                                                        |
| deepcopy_reduce            | 3.24 us                                                | 2.69 us: 1.20x faster                                                        |
| regex_dna                  | 220 ms                                                 | 183 ms: 1.20x faster                                                         |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 487 ms: 1.18x faster                                                         |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 478 ms: 1.14x faster                                                         |
| pylint                     | 312 ms                                                 | 279 ms: 1.12x faster                                                         |
| pyflate                    | 470 ms                                                 | 427 ms: 1.10x faster                                                         |
| richards                   | 47.5 ms                                                | 43.3 ms: 1.10x faster                                                        |
| dulwich_log                | 64.6 ms                                                | 59.2 ms: 1.09x faster                                                        |
| richards_super             | 53.7 ms                                                | 49.3 ms: 1.09x faster                                                        |
| spectral_norm              | 113 ms                                                 | 104 ms: 1.09x faster                                                         |
| float                      | 78.7 ms                                                | 72.4 ms: 1.09x faster                                                        |
| xml_etree_parse            | 154 ms                                                 | 143 ms: 1.08x faster                                                         |
| genshi_text                | 22.6 ms                                                | 21.1 ms: 1.07x faster                                                        |
| pycparser                  | 1.20 sec                                               | 1.12 sec: 1.07x faster                                                       |
| scimark_sor                | 122 ms                                                 | 116 ms: 1.06x faster                                                         |
| tomli_loads                | 2.12 sec                                               | 2.01 sec: 1.05x faster                                                       |
| telco                      | 8.40 ms                                                | 7.99 ms: 1.05x faster                                                        |
| 2to3                       | 266 ms                                                 | 254 ms: 1.05x faster                                                         |
| python_startup             | 12.7 ms                                                | 12.1 ms: 1.04x faster                                                        |
| sympy_integrate            | 19.8 ms                                                | 19.0 ms: 1.04x faster                                                        |
| bpe_tokeniser              | 4.69 sec                                               | 4.50 sec: 1.04x faster                                                       |
| regex_compile              | 132 ms                                                 | 127 ms: 1.04x faster                                                         |
| async_generators           | 433 ms                                                 | 418 ms: 1.04x faster                                                         |
| comprehensions             | 16.5 us                                                | 15.9 us: 1.04x faster                                                        |
| k_core                     | 2.37 sec                                               | 2.29 sec: 1.03x faster                                                       |
| sphinx                     | 1.03 sec                                               | 1.00 sec: 1.03x faster                                                       |
| xml_etree_iterparse        | 101 ms                                                 | 98.5 ms: 1.03x faster                                                        |
| html5lib                   | 63.4 ms                                                | 61.7 ms: 1.03x faster                                                        |
| genshi_xml                 | 50.5 ms                                                | 49.2 ms: 1.03x faster                                                        |
| sympy_str                  | 273 ms                                                 | 267 ms: 1.02x faster                                                         |
| pathlib                    | 17.4 ms                                                | 17.0 ms: 1.02x faster                                                        |
| meteor_contest             | 108 ms                                                 | 107 ms: 1.02x faster                                                         |
| xml_etree_generate         | 86.8 ms                                                | 85.5 ms: 1.02x faster                                                        |
| python_startup_no_site     | 7.00 ms                                                | 6.90 ms: 1.01x faster                                                        |
| sympy_sum                  | 150 ms                                                 | 149 ms: 1.01x faster                                                         |
| json                       | 5.32 ms                                                | 5.27 ms: 1.01x faster                                                        |
| sympy_expand               | 456 ms                                                 | 452 ms: 1.01x faster                                                         |
| sqlite_synth               | 2.90 us                                                | 2.88 us: 1.01x faster                                                        |
| xml_etree_process          | 60.5 ms                                                | 60.0 ms: 1.01x faster                                                        |
| hexiom                     | 6.08 ms                                                | 6.03 ms: 1.01x faster                                                        |
| docutils                   | 2.58 sec                                               | 2.57 sec: 1.01x faster                                                       |
| gc_traversal               | 4.90 ms                                                | 4.90 ms: 1.00x slower                                                        |
| nqueens                    | 80.9 ms                                                | 81.3 ms: 1.01x slower                                                        |
| scimark_monte_carlo        | 66.8 ms                                                | 67.2 ms: 1.01x slower                                                        |
| crypto_pyaes               | 74.7 ms                                                | 75.6 ms: 1.01x slower                                                        |
| pidigits                   | 186 ms                                                 | 189 ms: 1.01x slower                                                         |
| unpickle_pure_python       | 213 us                                                 | 217 us: 1.02x slower                                                         |
| django_template            | 31.7 ms                                                | 32.6 ms: 1.03x slower                                                        |
| shortest_path              | 487 ms                                                 | 503 ms: 1.03x slower                                                         |
| json_loads                 | 27.2 us                                                | 28.2 us: 1.04x slower                                                        |
| raytrace                   | 262 ms                                                 | 273 ms: 1.04x slower                                                         |
| scimark_lu                 | 114 ms                                                 | 119 ms: 1.04x slower                                                         |
| fannkuch                   | 394 ms                                                 | 412 ms: 1.05x slower                                                         |
| typing_runtime_protocols   | 160 us                                                 | 168 us: 1.05x slower                                                         |
| chaos                      | 58.0 ms                                                | 61.1 ms: 1.05x slower                                                        |
| generators                 | 28.8 ms                                                | 30.3 ms: 1.05x slower                                                        |
| create_gc_cycles           | 2.45 ms                                                | 2.58 ms: 1.05x slower                                                        |
| pickle_pure_python         | 302 us                                                 | 320 us: 1.06x slower                                                         |
| connected_components       | 447 ms                                                 | 475 ms: 1.06x slower                                                         |
| logging_simple             | 5.65 us                                                | 6.13 us: 1.08x slower                                                        |
| json_dumps                 | 10.1 ms                                                | 11.0 ms: 1.09x slower                                                        |
| deltablue                  | 3.19 ms                                                | 3.50 ms: 1.10x slower                                                        |
| mako                       | 10.7 ms                                                | 11.8 ms: 1.10x slower                                                        |
| coroutines                 | 22.2 ms                                                | 24.5 ms: 1.10x slower                                                        |
| nbody                      | 87.7 ms                                                | 97.5 ms: 1.11x slower                                                        |
| logging_format             | 6.23 us                                                | 6.94 us: 1.11x slower                                                        |
| many_optionals             | 857 us                                                 | 958 us: 1.12x slower                                                         |
| pprint_safe_repr           | 727 ms                                                 | 813 ms: 1.12x slower                                                         |
| pprint_pformat             | 1.48 sec                                               | 1.66 sec: 1.13x slower                                                       |
| subparsers                 | 15.5 ms                                                | 23.5 ms: 1.52x slower                                                        |
| logging_silent             | 101 ns                                                 | 473 ns: 4.69x slower                                                         |
| coverage                   | 82.8 ms                                                | 423 ms: 5.10x slower                                                         |
| thrift                     | 800 us                                                 | 147 ms: 184.31x slower                                                       |
| Geometric mean             | (ref)                                                  | 1.05x slower                                                                 |

Benchmark hidden because not significant (3): scimark_sparse_mat_mult, scimark_fft, asyncio_websockets
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250614-3.15.0a0-4019a15/bm-20250614-linux-x86_64-Fidget%2dSpinner-pylong_compactadd-3.15.0a0-4019a15.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.033x slower

# HPT report

- Reliability score: 99.84% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.06x