# Results vs. 3.13.0

- fork: python
- ref: 1a9d4a1fb3d4beda7c7e
- machine: linux-x86_64
- commit hash: 1a9d4a1
- commit date: 2025-04-01
- overall geometric mean: 1.058x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250401-linux-x86_64-python-1a9d4a1fb3d4beda7c7e-3.14.0a6+-1a9d4a1 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 252 ms: 1.06x faster                                                   |
| docutils       | 2.58 sec                                               | 2.60 sec: 1.01x slower                                                 |
| html5lib       | 63.4 ms                                                | 60.6 ms: 1.05x faster                                                  |
| sphinx         | 1.03 sec                                               | 1.02 sec: 1.01x faster                                                 |
| Geometric mean | (ref)                                                  | 1.03x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250401-linux-x86_64-python-1a9d4a1fb3d4beda7c7e-3.14.0a6+-1a9d4a1 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 314 ms: 1.48x faster                                                   |
| async_tree_io_tg           | 861 ms                                                 | 614 ms: 1.40x faster                                                   |
| async_tree_memoization     | 437 ms                                                 | 313 ms: 1.40x faster                                                   |
| async_tree_io              | 838 ms                                                 | 615 ms: 1.36x faster                                                   |
| async_tree_none            | 350 ms                                                 | 259 ms: 1.35x faster                                                   |
| async_tree_none_tg         | 319 ms                                                 | 248 ms: 1.29x faster                                                   |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 491 ms: 1.17x faster                                                   |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 477 ms: 1.14x faster                                                   |
| async_generators           | 433 ms                                                 | 394 ms: 1.10x faster                                                   |
| coroutines                 | 22.2 ms                                                | 23.3 ms: 1.05x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.23x faster                                                           |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250401-linux-x86_64-python-1a9d4a1fb3d4beda7c7e-3.14.0a6+-1a9d4a1 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 68.6 ms: 1.15x faster                                                  |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                   |
| nbody          | 87.7 ms                                                | 93.8 ms: 1.07x slower                                                  |
| Geometric mean | (ref)                                                  | 1.02x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250401-linux-x86_64-python-1a9d4a1fb3d4beda7c7e-3.14.0a6+-1a9d4a1 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_v8       | 26.9 ms                                                | 23.1 ms: 1.16x faster                                                  |
| regex_effbot   | 3.77 ms                                                | 3.29 ms: 1.14x faster                                                  |
| regex_compile  | 132 ms                                                 | 125 ms: 1.05x faster                                                   |
| Geometric mean | (ref)                                                  | 1.09x faster                                                           |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250401-linux-x86_64-python-1a9d4a1fb3d4beda7c7e-3.14.0a6+-1a9d4a1 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.94 sec: 1.09x faster                                                 |
| xml_etree_parse      | 154 ms                                                 | 144 ms: 1.07x faster                                                   |
| xml_etree_generate   | 86.8 ms                                                | 84.1 ms: 1.03x faster                                                  |
| xml_etree_process    | 60.5 ms                                                | 58.7 ms: 1.03x faster                                                  |
| xml_etree_iterparse  | 101 ms                                                 | 98.8 ms: 1.03x faster                                                  |
| unpickle_pure_python | 213 us                                                 | 218 us: 1.02x slower                                                   |
| pickle_pure_python   | 302 us                                                 | 313 us: 1.04x slower                                                   |
| json_loads           | 27.2 us                                                | 29.8 us: 1.10x slower                                                  |
| json_dumps           | 10.1 ms                                                | 11.4 ms: 1.12x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.00x slower                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250401-linux-x86_64-python-1a9d4a1fb3d4beda7c7e-3.14.0a6+-1a9d4a1 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 13.1 ms: 1.04x slower                                                  |
| python_startup_no_site | 7.00 ms                                                | 8.18 ms: 1.17x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.10x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250401-linux-x86_64-python-1a9d4a1fb3d4beda7c7e-3.14.0a6+-1a9d4a1 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.5 ms: 1.05x faster                                                  |
| genshi_xml      | 50.5 ms                                                | 49.2 ms: 1.03x faster                                                  |
| django_template | 31.7 ms                                                | 31.3 ms: 1.01x faster                                                  |
| mako            | 10.7 ms                                                | 11.3 ms: 1.06x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250401-linux-x86_64-python-1a9d4a1fb3d4beda7c7e-3.14.0a6+-1a9d4a1 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.22 sec: 2.09x faster                                                 |
| async_tree_memoization_tg  | 463 ms                                                 | 314 ms: 1.48x faster                                                   |
| deepcopy                   | 354 us                                                 | 251 us: 1.41x faster                                                   |
| async_tree_io_tg           | 861 ms                                                 | 614 ms: 1.40x faster                                                   |
| async_tree_memoization     | 437 ms                                                 | 313 ms: 1.40x faster                                                   |
| async_tree_io              | 838 ms                                                 | 615 ms: 1.36x faster                                                   |
| async_tree_none            | 350 ms                                                 | 259 ms: 1.35x faster                                                   |
| deepcopy_memo              | 38.4 us                                                | 28.9 us: 1.33x faster                                                  |
| async_tree_none_tg         | 319 ms                                                 | 248 ms: 1.29x faster                                                   |
| go                         | 141 ms                                                 | 111 ms: 1.26x faster                                                   |
| deepcopy_reduce            | 3.24 us                                                | 2.72 us: 1.19x faster                                                  |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 491 ms: 1.17x faster                                                   |
| regex_v8                   | 26.9 ms                                                | 23.1 ms: 1.16x faster                                                  |
| float                      | 78.7 ms                                                | 68.6 ms: 1.15x faster                                                  |
| spectral_norm              | 113 ms                                                 | 98.9 ms: 1.14x faster                                                  |
| regex_effbot               | 3.77 ms                                                | 3.29 ms: 1.14x faster                                                  |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 477 ms: 1.14x faster                                                   |
| pylint                     | 312 ms                                                 | 277 ms: 1.13x faster                                                   |
| async_generators           | 433 ms                                                 | 394 ms: 1.10x faster                                                   |
| richards                   | 47.5 ms                                                | 43.3 ms: 1.10x faster                                                  |
| dulwich_log                | 64.6 ms                                                | 58.9 ms: 1.10x faster                                                  |
| tomli_loads                | 2.12 sec                                               | 1.94 sec: 1.09x faster                                                 |
| richards_super             | 53.7 ms                                                | 49.4 ms: 1.09x faster                                                  |
| scimark_fft                | 367 ms                                                 | 340 ms: 1.08x faster                                                   |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.66 ms: 1.08x faster                                                  |
| telco                      | 8.40 ms                                                | 7.80 ms: 1.08x faster                                                  |
| xml_etree_parse            | 154 ms                                                 | 144 ms: 1.07x faster                                                   |
| pathlib                    | 17.4 ms                                                | 16.4 ms: 1.06x faster                                                  |
| 2to3                       | 266 ms                                                 | 252 ms: 1.06x faster                                                   |
| pyflate                    | 470 ms                                                 | 444 ms: 1.06x faster                                                   |
| scimark_sor                | 122 ms                                                 | 116 ms: 1.05x faster                                                   |
| regex_compile              | 132 ms                                                 | 125 ms: 1.05x faster                                                   |
| genshi_text                | 22.6 ms                                                | 21.5 ms: 1.05x faster                                                  |
| logging_silent             | 101 ns                                                 | 96.5 ns: 1.05x faster                                                  |
| html5lib                   | 63.4 ms                                                | 60.6 ms: 1.05x faster                                                  |
| k_core                     | 2.37 sec                                               | 2.27 sec: 1.05x faster                                                 |
| bpe_tokeniser              | 4.69 sec                                               | 4.49 sec: 1.04x faster                                                 |
| pycparser                  | 1.20 sec                                               | 1.15 sec: 1.04x faster                                                 |
| scimark_monte_carlo        | 66.8 ms                                                | 64.3 ms: 1.04x faster                                                  |
| sqlite_synth               | 2.90 us                                                | 2.80 us: 1.04x faster                                                  |
| xml_etree_generate         | 86.8 ms                                                | 84.1 ms: 1.03x faster                                                  |
| chaos                      | 58.0 ms                                                | 56.3 ms: 1.03x faster                                                  |
| sympy_integrate            | 19.8 ms                                                | 19.2 ms: 1.03x faster                                                  |
| xml_etree_process          | 60.5 ms                                                | 58.7 ms: 1.03x faster                                                  |
| crypto_pyaes               | 74.7 ms                                                | 72.6 ms: 1.03x faster                                                  |
| meteor_contest             | 108 ms                                                 | 106 ms: 1.03x faster                                                   |
| genshi_xml                 | 50.5 ms                                                | 49.2 ms: 1.03x faster                                                  |
| xml_etree_iterparse        | 101 ms                                                 | 98.8 ms: 1.03x faster                                                  |
| raytrace                   | 262 ms                                                 | 256 ms: 1.02x faster                                                   |
| sympy_str                  | 273 ms                                                 | 268 ms: 1.02x faster                                                   |
| logging_format             | 6.23 us                                                | 6.13 us: 1.02x faster                                                  |
| sphinx                     | 1.03 sec                                               | 1.02 sec: 1.01x faster                                                 |
| scimark_lu                 | 114 ms                                                 | 113 ms: 1.01x faster                                                   |
| sqlalchemy_declarative     | 133 ms                                                 | 131 ms: 1.01x faster                                                   |
| sympy_sum                  | 150 ms                                                 | 149 ms: 1.01x faster                                                   |
| django_template            | 31.7 ms                                                | 31.3 ms: 1.01x faster                                                  |
| logging_simple             | 5.65 us                                                | 5.61 us: 1.01x faster                                                  |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                                   |
| comprehensions             | 16.5 us                                                | 16.5 us: 1.00x slower                                                  |
| docutils                   | 2.58 sec                                               | 2.60 sec: 1.01x slower                                                 |
| pprint_pformat             | 1.48 sec                                               | 1.49 sec: 1.01x slower                                                 |
| sympy_expand               | 456 ms                                                 | 459 ms: 1.01x slower                                                   |
| connected_components       | 447 ms                                                 | 451 ms: 1.01x slower                                                   |
| create_gc_cycles           | 2.45 ms                                                | 2.48 ms: 1.01x slower                                                  |
| shortest_path              | 487 ms                                                 | 494 ms: 1.02x slower                                                   |
| hexiom                     | 6.08 ms                                                | 6.18 ms: 1.02x slower                                                  |
| nqueens                    | 80.9 ms                                                | 82.3 ms: 1.02x slower                                                  |
| gc_traversal               | 4.90 ms                                                | 4.98 ms: 1.02x slower                                                  |
| coverage                   | 82.8 ms                                                | 84.6 ms: 1.02x slower                                                  |
| typing_runtime_protocols   | 160 us                                                 | 164 us: 1.02x slower                                                   |
| unpickle_pure_python       | 213 us                                                 | 218 us: 1.02x slower                                                   |
| pickle_pure_python         | 302 us                                                 | 313 us: 1.04x slower                                                   |
| python_startup             | 12.7 ms                                                | 13.1 ms: 1.04x slower                                                  |
| fannkuch                   | 394 ms                                                 | 413 ms: 1.05x slower                                                   |
| coroutines                 | 22.2 ms                                                | 23.3 ms: 1.05x slower                                                  |
| deltablue                  | 3.19 ms                                                | 3.37 ms: 1.06x slower                                                  |
| mako                       | 10.7 ms                                                | 11.3 ms: 1.06x slower                                                  |
| nbody                      | 87.7 ms                                                | 93.8 ms: 1.07x slower                                                  |
| bench_thread_pool          | 818 us                                                 | 878 us: 1.07x slower                                                   |
| generators                 | 28.8 ms                                                | 30.9 ms: 1.08x slower                                                  |
| many_optionals             | 857 us                                                 | 928 us: 1.08x slower                                                   |
| json_loads                 | 27.2 us                                                | 29.8 us: 1.10x slower                                                  |
| json_dumps                 | 10.1 ms                                                | 11.4 ms: 1.12x slower                                                  |
| python_startup_no_site     | 7.00 ms                                                | 8.18 ms: 1.17x slower                                                  |
| subparsers                 | 15.5 ms                                                | 20.7 ms: 1.34x slower                                                  |
| bench_mp_pool              | 24.0 ms                                                | 83.3 ms: 3.47x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.04x faster                                                           |

Benchmark hidden because not significant (5): pprint_safe_repr, json, regex_dna, asyncio_websockets, sqlalchemy_imperative
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (4) of results/bm-20250401-3.14.0a6+-1a9d4a1/bm-20250401-linux-x86_64-python-1a9d4a1fb3d4beda7c7e-3.14.0a6+-1a9d4a1.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.058x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.04x