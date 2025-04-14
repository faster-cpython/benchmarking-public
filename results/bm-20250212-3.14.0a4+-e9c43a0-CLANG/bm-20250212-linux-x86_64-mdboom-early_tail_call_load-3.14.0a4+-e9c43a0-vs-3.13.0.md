# Results vs. 3.13.0

- fork: mdboom
- ref: early_tail_call_load
- machine: linux-x86_64
- commit hash: e9c43a0
- commit date: 2025-02-12
- overall geometric mean: 1.086x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250212-linux-x86_64-mdboom-early_tail_call_load-3.14.0a4+-e9c43a0 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 244 ms: 1.09x faster                                                   |
| docutils       | 2.58 sec                                               | 2.51 sec: 1.03x faster                                                 |
| html5lib       | 63.4 ms                                                | 55.3 ms: 1.15x faster                                                  |
| sphinx         | 1.03 sec                                               | 964 ms: 1.07x faster                                                   |
| Geometric mean | (ref)                                                  | 1.08x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250212-linux-x86_64-mdboom-early_tail_call_load-3.14.0a4+-e9c43a0 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 313 ms: 1.48x faster                                                   |
| async_tree_memoization     | 437 ms                                                 | 311 ms: 1.41x faster                                                   |
| async_tree_io              | 838 ms                                                 | 599 ms: 1.40x faster                                                   |
| async_tree_io_tg           | 861 ms                                                 | 616 ms: 1.40x faster                                                   |
| async_tree_none            | 350 ms                                                 | 252 ms: 1.39x faster                                                   |
| async_tree_none_tg         | 319 ms                                                 | 244 ms: 1.31x faster                                                   |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 487 ms: 1.18x faster                                                   |
| async_generators           | 433 ms                                                 | 378 ms: 1.15x faster                                                   |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 478 ms: 1.14x faster                                                   |
| coroutines                 | 22.2 ms                                                | 21.0 ms: 1.06x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.25x faster                                                           |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250212-linux-x86_64-mdboom-early_tail_call_load-3.14.0a4+-e9c43a0 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 64.1 ms: 1.23x faster                                                  |
| nbody          | 87.7 ms                                                | 80.5 ms: 1.09x faster                                                  |
| pidigits       | 186 ms                                                 | 202 ms: 1.08x slower                                                   |
| Geometric mean | (ref)                                                  | 1.07x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250212-linux-x86_64-mdboom-early_tail_call_load-3.14.0a4+-e9c43a0 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.13 ms: 1.21x faster                                                  |
| regex_dna      | 220 ms                                                 | 198 ms: 1.11x faster                                                   |
| regex_compile  | 132 ms                                                 | 119 ms: 1.11x faster                                                   |
| regex_v8       | 26.9 ms                                                | 24.9 ms: 1.08x faster                                                  |
| Geometric mean | (ref)                                                  | 1.13x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250212-linux-x86_64-mdboom-early_tail_call_load-3.14.0a4+-e9c43a0 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.86 sec: 1.14x faster                                                 |
| xml_etree_process    | 60.5 ms                                                | 56.9 ms: 1.06x faster                                                  |
| xml_etree_generate   | 86.8 ms                                                | 83.8 ms: 1.04x faster                                                  |
| unpickle_pure_python | 213 us                                                 | 206 us: 1.04x faster                                                   |
| pickle_pure_python   | 302 us                                                 | 299 us: 1.01x faster                                                   |
| xml_etree_parse      | 154 ms                                                 | 159 ms: 1.03x slower                                                   |
| json_loads           | 27.2 us                                                | 30.8 us: 1.13x slower                                                  |
| json_dumps           | 10.1 ms                                                | 12.5 ms: 1.24x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                           |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250212-linux-x86_64-mdboom-early_tail_call_load-3.14.0a4+-e9c43a0 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 12.6 ms: 1.01x faster                                                  |
| python_startup_no_site | 7.00 ms                                                | 6.95 ms: 1.01x faster                                                  |
| Geometric mean         | (ref)                                                  | 1.01x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250212-linux-x86_64-mdboom-early_tail_call_load-3.14.0a4+-e9c43a0 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 20.7 ms: 1.09x faster                                                  |
| genshi_xml      | 50.5 ms                                                | 47.5 ms: 1.06x faster                                                  |
| django_template | 31.7 ms                                                | 30.1 ms: 1.05x faster                                                  |
| mako            | 10.7 ms                                                | 11.3 ms: 1.06x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.04x faster                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250212-linux-x86_64-mdboom-early_tail_call_load-3.14.0a4+-e9c43a0 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 313 ms: 1.48x faster                                                   |
| deepcopy                   | 354 us                                                 | 240 us: 1.47x faster                                                   |
| async_tree_memoization     | 437 ms                                                 | 311 ms: 1.41x faster                                                   |
| async_tree_io              | 838 ms                                                 | 599 ms: 1.40x faster                                                   |
| async_tree_io_tg           | 861 ms                                                 | 616 ms: 1.40x faster                                                   |
| async_tree_none            | 350 ms                                                 | 252 ms: 1.39x faster                                                   |
| deepcopy_memo              | 38.4 us                                                | 28.2 us: 1.36x faster                                                  |
| spectral_norm              | 113 ms                                                 | 84.1 ms: 1.35x faster                                                  |
| scimark_fft                | 367 ms                                                 | 279 ms: 1.32x faster                                                   |
| go                         | 141 ms                                                 | 107 ms: 1.31x faster                                                   |
| async_tree_none_tg         | 319 ms                                                 | 244 ms: 1.31x faster                                                   |
| deepcopy_reduce            | 3.24 us                                                | 2.52 us: 1.29x faster                                                  |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.07 ms: 1.23x faster                                                  |
| logging_silent             | 101 ns                                                 | 82.3 ns: 1.23x faster                                                  |
| float                      | 78.7 ms                                                | 64.1 ms: 1.23x faster                                                  |
| richards                   | 47.5 ms                                                | 39.3 ms: 1.21x faster                                                  |
| regex_effbot               | 3.77 ms                                                | 3.13 ms: 1.21x faster                                                  |
| pathlib                    | 17.4 ms                                                | 14.4 ms: 1.20x faster                                                  |
| pyflate                    | 470 ms                                                 | 394 ms: 1.19x faster                                                   |
| pylint                     | 312 ms                                                 | 262 ms: 1.19x faster                                                   |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 487 ms: 1.18x faster                                                   |
| richards_super             | 53.7 ms                                                | 45.8 ms: 1.17x faster                                                  |
| telco                      | 8.40 ms                                                | 7.18 ms: 1.17x faster                                                  |
| scimark_sor                | 122 ms                                                 | 106 ms: 1.16x faster                                                   |
| async_generators           | 433 ms                                                 | 378 ms: 1.15x faster                                                   |
| html5lib                   | 63.4 ms                                                | 55.3 ms: 1.15x faster                                                  |
| tomli_loads                | 2.12 sec                                               | 1.86 sec: 1.14x faster                                                 |
| scimark_monte_carlo        | 66.8 ms                                                | 58.7 ms: 1.14x faster                                                  |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 478 ms: 1.14x faster                                                   |
| crypto_pyaes               | 74.7 ms                                                | 66.5 ms: 1.12x faster                                                  |
| deltablue                  | 3.19 ms                                                | 2.85 ms: 1.12x faster                                                  |
| regex_dna                  | 220 ms                                                 | 198 ms: 1.11x faster                                                   |
| sqlalchemy_imperative      | 16.9 ms                                                | 15.2 ms: 1.11x faster                                                  |
| regex_compile              | 132 ms                                                 | 119 ms: 1.11x faster                                                   |
| comprehensions             | 16.5 us                                                | 14.9 us: 1.11x faster                                                  |
| sqlglot_parse              | 1.26 ms                                                | 1.14 ms: 1.11x faster                                                  |
| chaos                      | 58.0 ms                                                | 52.7 ms: 1.10x faster                                                  |
| bpe_tokeniser              | 4.69 sec                                               | 4.26 sec: 1.10x faster                                                 |
| pycparser                  | 1.20 sec                                               | 1.09 sec: 1.10x faster                                                 |
| sqlalchemy_declarative     | 133 ms                                                 | 121 ms: 1.10x faster                                                   |
| sqlglot_transpile          | 1.57 ms                                                | 1.44 ms: 1.09x faster                                                  |
| genshi_text                | 22.6 ms                                                | 20.7 ms: 1.09x faster                                                  |
| 2to3                       | 266 ms                                                 | 244 ms: 1.09x faster                                                   |
| thrift                     | 800 us                                                 | 733 us: 1.09x faster                                                   |
| nbody                      | 87.7 ms                                                | 80.5 ms: 1.09x faster                                                  |
| typing_runtime_protocols   | 160 us                                                 | 147 us: 1.09x faster                                                   |
| sympy_str                  | 273 ms                                                 | 251 ms: 1.09x faster                                                   |
| sympy_sum                  | 150 ms                                                 | 139 ms: 1.08x faster                                                   |
| scimark_lu                 | 114 ms                                                 | 106 ms: 1.08x faster                                                   |
| nqueens                    | 80.9 ms                                                | 74.8 ms: 1.08x faster                                                  |
| regex_v8                   | 26.9 ms                                                | 24.9 ms: 1.08x faster                                                  |
| dulwich_log                | 64.6 ms                                                | 60.1 ms: 1.07x faster                                                  |
| sqlite_synth               | 2.90 us                                                | 2.70 us: 1.07x faster                                                  |
| logging_simple             | 5.65 us                                                | 5.28 us: 1.07x faster                                                  |
| sphinx                     | 1.03 sec                                               | 964 ms: 1.07x faster                                                   |
| logging_format             | 6.23 us                                                | 5.83 us: 1.07x faster                                                  |
| sympy_integrate            | 19.8 ms                                                | 18.6 ms: 1.07x faster                                                  |
| hexiom                     | 6.08 ms                                                | 5.70 ms: 1.07x faster                                                  |
| sympy_expand               | 456 ms                                                 | 428 ms: 1.07x faster                                                   |
| xml_etree_process          | 60.5 ms                                                | 56.9 ms: 1.06x faster                                                  |
| genshi_xml                 | 50.5 ms                                                | 47.5 ms: 1.06x faster                                                  |
| coroutines                 | 22.2 ms                                                | 21.0 ms: 1.06x faster                                                  |
| django_template            | 31.7 ms                                                | 30.1 ms: 1.05x faster                                                  |
| raytrace                   | 262 ms                                                 | 249 ms: 1.05x faster                                                   |
| sqlglot_optimize           | 53.4 ms                                                | 50.8 ms: 1.05x faster                                                  |
| k_core                     | 2.37 sec                                               | 2.28 sec: 1.04x faster                                                 |
| generators                 | 28.8 ms                                                | 27.7 ms: 1.04x faster                                                  |
| xml_etree_generate         | 86.8 ms                                                | 83.8 ms: 1.04x faster                                                  |
| unpickle_pure_python       | 213 us                                                 | 206 us: 1.04x faster                                                   |
| docutils                   | 2.58 sec                                               | 2.51 sec: 1.03x faster                                                 |
| coverage                   | 82.8 ms                                                | 80.6 ms: 1.03x faster                                                  |
| fannkuch                   | 394 ms                                                 | 384 ms: 1.02x faster                                                   |
| pprint_pformat             | 1.48 sec                                               | 1.45 sec: 1.02x faster                                                 |
| pprint_safe_repr           | 727 ms                                                 | 713 ms: 1.02x faster                                                   |
| pickle_pure_python         | 302 us                                                 | 299 us: 1.01x faster                                                   |
| meteor_contest             | 108 ms                                                 | 107 ms: 1.01x faster                                                   |
| python_startup             | 12.7 ms                                                | 12.6 ms: 1.01x faster                                                  |
| python_startup_no_site     | 7.00 ms                                                | 6.95 ms: 1.01x faster                                                  |
| bench_thread_pool          | 818 us                                                 | 813 us: 1.01x faster                                                   |
| connected_components       | 447 ms                                                 | 453 ms: 1.01x slower                                                   |
| json                       | 5.32 ms                                                | 5.43 ms: 1.02x slower                                                  |
| mdp                        | 2.54 sec                                               | 2.61 sec: 1.02x slower                                                 |
| gc_traversal               | 4.90 ms                                                | 5.04 ms: 1.03x slower                                                  |
| xml_etree_parse            | 154 ms                                                 | 159 ms: 1.03x slower                                                   |
| create_gc_cycles           | 2.45 ms                                                | 2.54 ms: 1.04x slower                                                  |
| many_optionals             | 857 us                                                 | 894 us: 1.04x slower                                                   |
| mako                       | 10.7 ms                                                | 11.3 ms: 1.06x slower                                                  |
| pidigits                   | 186 ms                                                 | 202 ms: 1.08x slower                                                   |
| json_loads                 | 27.2 us                                                | 30.8 us: 1.13x slower                                                  |
| json_dumps                 | 10.1 ms                                                | 12.5 ms: 1.24x slower                                                  |
| subparsers                 | 15.5 ms                                                | 19.8 ms: 1.28x slower                                                  |
| sqlglot_normalize          | 108 ms                                                 | 265 ms: 2.45x slower                                                   |
| bench_mp_pool              | 24.0 ms                                                | 79.0 ms: 3.30x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.07x faster                                                           |

Benchmark hidden because not significant (3): xml_etree_iterparse, asyncio_websockets, shortest_path
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.086x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: 1.03x