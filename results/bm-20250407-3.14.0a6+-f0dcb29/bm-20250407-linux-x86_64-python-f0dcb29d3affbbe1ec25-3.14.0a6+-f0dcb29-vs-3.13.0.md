# Results vs. 3.13.0

- fork: python
- ref: f0dcb29d3affbbe1ec25
- machine: linux-x86_64
- commit hash: f0dcb29
- commit date: 2025-04-07
- overall geometric mean: 1.061x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250407-linux-x86_64-python-f0dcb29d3affbbe1ec25-3.14.0a6+-f0dcb29 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 251 ms: 1.06x faster                                                   |
| docutils       | 2.58 sec                                               | 2.58 sec: 1.00x faster                                                 |
| html5lib       | 63.4 ms                                                | 60.5 ms: 1.05x faster                                                  |
| sphinx         | 1.03 sec                                               | 1.01 sec: 1.02x faster                                                 |
| Geometric mean | (ref)                                                  | 1.03x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250407-linux-x86_64-python-f0dcb29d3affbbe1ec25-3.14.0a6+-f0dcb29 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 313 ms: 1.48x faster                                                   |
| async_tree_io_tg           | 861 ms                                                 | 611 ms: 1.41x faster                                                   |
| async_tree_memoization     | 437 ms                                                 | 310 ms: 1.41x faster                                                   |
| async_tree_none            | 350 ms                                                 | 255 ms: 1.38x faster                                                   |
| async_tree_io              | 838 ms                                                 | 612 ms: 1.37x faster                                                   |
| async_tree_none_tg         | 319 ms                                                 | 246 ms: 1.30x faster                                                   |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 478 ms: 1.20x faster                                                   |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 473 ms: 1.15x faster                                                   |
| async_generators           | 433 ms                                                 | 388 ms: 1.12x faster                                                   |
| coroutines                 | 22.2 ms                                                | 24.4 ms: 1.10x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.23x faster                                                           |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250407-linux-x86_64-python-f0dcb29d3affbbe1ec25-3.14.0a6+-f0dcb29 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 67.5 ms: 1.17x faster                                                  |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                   |
| nbody          | 87.7 ms                                                | 93.2 ms: 1.06x slower                                                  |
| Geometric mean | (ref)                                                  | 1.03x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250407-linux-x86_64-python-f0dcb29d3affbbe1ec25-3.14.0a6+-f0dcb29 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_v8       | 26.9 ms                                                | 21.6 ms: 1.24x faster                                                  |
| regex_effbot   | 3.77 ms                                                | 3.26 ms: 1.15x faster                                                  |
| regex_compile  | 132 ms                                                 | 124 ms: 1.07x faster                                                   |
| regex_dna      | 220 ms                                                 | 214 ms: 1.03x faster                                                   |
| Geometric mean | (ref)                                                  | 1.12x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250407-linux-x86_64-python-f0dcb29d3affbbe1ec25-3.14.0a6+-f0dcb29 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 140 ms: 1.10x faster                                                   |
| tomli_loads          | 2.12 sec                                               | 1.93 sec: 1.10x faster                                                 |
| xml_etree_process    | 60.5 ms                                                | 58.6 ms: 1.03x faster                                                  |
| xml_etree_generate   | 86.8 ms                                                | 84.3 ms: 1.03x faster                                                  |
| xml_etree_iterparse  | 101 ms                                                 | 98.4 ms: 1.03x faster                                                  |
| unpickle_pure_python | 213 us                                                 | 215 us: 1.01x slower                                                   |
| pickle_pure_python   | 302 us                                                 | 313 us: 1.04x slower                                                   |
| json_loads           | 27.2 us                                                | 29.8 us: 1.10x slower                                                  |
| json_dumps           | 10.1 ms                                                | 11.6 ms: 1.14x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.00x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250407-linux-x86_64-python-f0dcb29d3affbbe1ec25-3.14.0a6+-f0dcb29 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 13.2 ms: 1.04x slower                                                  |
| python_startup_no_site | 7.00 ms                                                | 8.21 ms: 1.17x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.11x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250407-linux-x86_64-python-f0dcb29d3affbbe1ec25-3.14.0a6+-f0dcb29 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 20.7 ms: 1.09x faster                                                  |
| genshi_xml      | 50.5 ms                                                | 49.8 ms: 1.01x faster                                                  |
| django_template | 31.7 ms                                                | 31.9 ms: 1.01x slower                                                  |
| mako            | 10.7 ms                                                | 11.2 ms: 1.05x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250407-linux-x86_64-python-f0dcb29d3affbbe1ec25-3.14.0a6+-f0dcb29 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.24 sec: 2.05x faster                                                 |
| async_tree_memoization_tg  | 463 ms                                                 | 313 ms: 1.48x faster                                                   |
| deepcopy                   | 354 us                                                 | 247 us: 1.44x faster                                                   |
| async_tree_io_tg           | 861 ms                                                 | 611 ms: 1.41x faster                                                   |
| async_tree_memoization     | 437 ms                                                 | 310 ms: 1.41x faster                                                   |
| async_tree_none            | 350 ms                                                 | 255 ms: 1.38x faster                                                   |
| async_tree_io              | 838 ms                                                 | 612 ms: 1.37x faster                                                   |
| deepcopy_memo              | 38.4 us                                                | 28.8 us: 1.33x faster                                                  |
| async_tree_none_tg         | 319 ms                                                 | 246 ms: 1.30x faster                                                   |
| go                         | 141 ms                                                 | 111 ms: 1.26x faster                                                   |
| regex_v8                   | 26.9 ms                                                | 21.6 ms: 1.24x faster                                                  |
| deepcopy_reduce            | 3.24 us                                                | 2.62 us: 1.23x faster                                                  |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 478 ms: 1.20x faster                                                   |
| float                      | 78.7 ms                                                | 67.5 ms: 1.17x faster                                                  |
| regex_effbot               | 3.77 ms                                                | 3.26 ms: 1.15x faster                                                  |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 473 ms: 1.15x faster                                                   |
| pylint                     | 312 ms                                                 | 277 ms: 1.13x faster                                                   |
| spectral_norm              | 113 ms                                                 | 101 ms: 1.12x faster                                                   |
| async_generators           | 433 ms                                                 | 388 ms: 1.12x faster                                                   |
| richards                   | 47.5 ms                                                | 43.1 ms: 1.10x faster                                                  |
| xml_etree_parse            | 154 ms                                                 | 140 ms: 1.10x faster                                                   |
| dulwich_log                | 64.6 ms                                                | 58.8 ms: 1.10x faster                                                  |
| tomli_loads                | 2.12 sec                                               | 1.93 sec: 1.10x faster                                                 |
| richards_super             | 53.7 ms                                                | 49.1 ms: 1.09x faster                                                  |
| genshi_text                | 22.6 ms                                                | 20.7 ms: 1.09x faster                                                  |
| telco                      | 8.40 ms                                                | 7.72 ms: 1.09x faster                                                  |
| scimark_fft                | 367 ms                                                 | 342 ms: 1.07x faster                                                   |
| regex_compile              | 132 ms                                                 | 124 ms: 1.07x faster                                                   |
| pyflate                    | 470 ms                                                 | 442 ms: 1.06x faster                                                   |
| 2to3                       | 266 ms                                                 | 251 ms: 1.06x faster                                                   |
| pathlib                    | 17.4 ms                                                | 16.5 ms: 1.06x faster                                                  |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.77 ms: 1.05x faster                                                  |
| pycparser                  | 1.20 sec                                               | 1.14 sec: 1.05x faster                                                 |
| html5lib                   | 63.4 ms                                                | 60.5 ms: 1.05x faster                                                  |
| chaos                      | 58.0 ms                                                | 55.8 ms: 1.04x faster                                                  |
| logging_silent             | 101 ns                                                 | 97.3 ns: 1.04x faster                                                  |
| sympy_integrate            | 19.8 ms                                                | 19.1 ms: 1.04x faster                                                  |
| logging_simple             | 5.65 us                                                | 5.45 us: 1.04x faster                                                  |
| gc_traversal               | 4.90 ms                                                | 4.73 ms: 1.04x faster                                                  |
| k_core                     | 2.37 sec                                               | 2.29 sec: 1.03x faster                                                 |
| sqlite_synth               | 2.90 us                                                | 2.81 us: 1.03x faster                                                  |
| bpe_tokeniser              | 4.69 sec                                               | 4.54 sec: 1.03x faster                                                 |
| xml_etree_process          | 60.5 ms                                                | 58.6 ms: 1.03x faster                                                  |
| xml_etree_generate         | 86.8 ms                                                | 84.3 ms: 1.03x faster                                                  |
| regex_dna                  | 220 ms                                                 | 214 ms: 1.03x faster                                                   |
| xml_etree_iterparse        | 101 ms                                                 | 98.4 ms: 1.03x faster                                                  |
| crypto_pyaes               | 74.7 ms                                                | 72.9 ms: 1.03x faster                                                  |
| sphinx                     | 1.03 sec                                               | 1.01 sec: 1.02x faster                                                 |
| logging_format             | 6.23 us                                                | 6.08 us: 1.02x faster                                                  |
| meteor_contest             | 108 ms                                                 | 106 ms: 1.02x faster                                                   |
| scimark_sor                | 122 ms                                                 | 120 ms: 1.02x faster                                                   |
| sympy_str                  | 273 ms                                                 | 268 ms: 1.02x faster                                                   |
| genshi_xml                 | 50.5 ms                                                | 49.8 ms: 1.01x faster                                                  |
| pprint_safe_repr           | 727 ms                                                 | 718 ms: 1.01x faster                                                   |
| sqlalchemy_declarative     | 133 ms                                                 | 131 ms: 1.01x faster                                                   |
| pprint_pformat             | 1.48 sec                                               | 1.47 sec: 1.01x faster                                                 |
| sqlalchemy_imperative      | 16.9 ms                                                | 16.8 ms: 1.01x faster                                                  |
| raytrace                   | 262 ms                                                 | 260 ms: 1.01x faster                                                   |
| sympy_sum                  | 150 ms                                                 | 150 ms: 1.00x faster                                                   |
| docutils                   | 2.58 sec                                               | 2.58 sec: 1.00x faster                                                 |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                                   |
| create_gc_cycles           | 2.45 ms                                                | 2.46 ms: 1.01x slower                                                  |
| nqueens                    | 80.9 ms                                                | 81.4 ms: 1.01x slower                                                  |
| connected_components       | 447 ms                                                 | 450 ms: 1.01x slower                                                   |
| django_template            | 31.7 ms                                                | 31.9 ms: 1.01x slower                                                  |
| scimark_lu                 | 114 ms                                                 | 115 ms: 1.01x slower                                                   |
| hexiom                     | 6.08 ms                                                | 6.14 ms: 1.01x slower                                                  |
| unpickle_pure_python       | 213 us                                                 | 215 us: 1.01x slower                                                   |
| typing_runtime_protocols   | 160 us                                                 | 164 us: 1.02x slower                                                   |
| comprehensions             | 16.5 us                                                | 16.9 us: 1.03x slower                                                  |
| generators                 | 28.8 ms                                                | 29.5 ms: 1.03x slower                                                  |
| pickle_pure_python         | 302 us                                                 | 313 us: 1.04x slower                                                   |
| coverage                   | 82.8 ms                                                | 86.3 ms: 1.04x slower                                                  |
| python_startup             | 12.7 ms                                                | 13.2 ms: 1.04x slower                                                  |
| fannkuch                   | 394 ms                                                 | 411 ms: 1.04x slower                                                   |
| mako                       | 10.7 ms                                                | 11.2 ms: 1.05x slower                                                  |
| deltablue                  | 3.19 ms                                                | 3.37 ms: 1.05x slower                                                  |
| nbody                      | 87.7 ms                                                | 93.2 ms: 1.06x slower                                                  |
| bench_thread_pool          | 818 us                                                 | 879 us: 1.08x slower                                                   |
| many_optionals             | 857 us                                                 | 926 us: 1.08x slower                                                   |
| coroutines                 | 22.2 ms                                                | 24.4 ms: 1.10x slower                                                  |
| json_loads                 | 27.2 us                                                | 29.8 us: 1.10x slower                                                  |
| json_dumps                 | 10.1 ms                                                | 11.6 ms: 1.14x slower                                                  |
| python_startup_no_site     | 7.00 ms                                                | 8.21 ms: 1.17x slower                                                  |
| subparsers                 | 15.5 ms                                                | 20.7 ms: 1.34x slower                                                  |
| bench_mp_pool              | 24.0 ms                                                | 82.2 ms: 3.43x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.05x faster                                                           |

Benchmark hidden because not significant (5): asyncio_websockets, scimark_monte_carlo, sympy_expand, shortest_path, json
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (4) of results/bm-20250407-3.14.0a6+-f0dcb29/bm-20250407-linux-x86_64-python-f0dcb29d3affbbe1ec25-3.14.0a6+-f0dcb29.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.061x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.03x