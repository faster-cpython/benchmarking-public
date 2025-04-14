# Results vs. 3.13.0

- fork: python
- ref: 52b5eb95b770fa00ebbd
- machine: linux-x86_64
- commit hash: 52b5eb9
- commit date: 2025-03-26
- overall geometric mean: 1.040x faster
- HPT reliability: 99.96%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250326-linux-x86_64-python-52b5eb95b770fa00ebbd-3.14.0a6+-52b5eb9 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 258 ms: 1.03x faster                                                   |
| docutils       | 2.58 sec                                               | 2.63 sec: 1.02x slower                                                 |
| html5lib       | 63.4 ms                                                | 61.9 ms: 1.02x faster                                                  |
| Geometric mean | (ref)                                                  | 1.01x faster                                                           |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250326-linux-x86_64-python-52b5eb95b770fa00ebbd-3.14.0a6+-52b5eb9 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 309 ms: 1.50x faster                                                   |
| async_tree_io_tg           | 861 ms                                                 | 610 ms: 1.41x faster                                                   |
| async_tree_memoization     | 437 ms                                                 | 311 ms: 1.40x faster                                                   |
| async_tree_io              | 838 ms                                                 | 612 ms: 1.37x faster                                                   |
| async_tree_none            | 350 ms                                                 | 257 ms: 1.36x faster                                                   |
| async_tree_none_tg         | 319 ms                                                 | 246 ms: 1.30x faster                                                   |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 487 ms: 1.18x faster                                                   |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 470 ms: 1.16x faster                                                   |
| async_generators           | 433 ms                                                 | 389 ms: 1.11x faster                                                   |
| coroutines                 | 22.2 ms                                                | 23.5 ms: 1.06x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.24x faster                                                           |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250326-linux-x86_64-python-52b5eb95b770fa00ebbd-3.14.0a6+-52b5eb9 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 70.5 ms: 1.12x faster                                                  |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                   |
| nbody          | 87.7 ms                                                | 97.3 ms: 1.11x slower                                                  |
| Geometric mean | (ref)                                                  | 1.00x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250326-linux-x86_64-python-52b5eb95b770fa00ebbd-3.14.0a6+-52b5eb9 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_v8       | 26.9 ms                                                | 23.0 ms: 1.17x faster                                                  |
| regex_effbot   | 3.77 ms                                                | 3.47 ms: 1.09x faster                                                  |
| regex_compile  | 132 ms                                                 | 127 ms: 1.04x faster                                                   |
| regex_dna      | 220 ms                                                 | 224 ms: 1.02x slower                                                   |
| Geometric mean | (ref)                                                  | 1.07x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250326-linux-x86_64-python-52b5eb95b770fa00ebbd-3.14.0a6+-52b5eb9 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 142 ms: 1.09x faster                                                   |
| tomli_loads          | 2.12 sec                                               | 1.97 sec: 1.08x faster                                                 |
| xml_etree_iterparse  | 101 ms                                                 | 99.0 ms: 1.02x faster                                                  |
| xml_etree_process    | 60.5 ms                                                | 59.3 ms: 1.02x faster                                                  |
| xml_etree_generate   | 86.8 ms                                                | 85.2 ms: 1.02x faster                                                  |
| unpickle_pure_python | 213 us                                                 | 218 us: 1.02x slower                                                   |
| pickle_pure_python   | 302 us                                                 | 319 us: 1.06x slower                                                   |
| json_loads           | 27.2 us                                                | 30.0 us: 1.10x slower                                                  |
| json_dumps           | 10.1 ms                                                | 11.7 ms: 1.16x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250326-linux-x86_64-python-52b5eb95b770fa00ebbd-3.14.0a6+-52b5eb9 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 13.1 ms: 1.03x slower                                                  |
| python_startup_no_site | 7.00 ms                                                | 8.19 ms: 1.17x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.10x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250326-linux-x86_64-python-52b5eb95b770fa00ebbd-3.14.0a6+-52b5eb9 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.4 ms: 1.06x faster                                                  |
| genshi_xml      | 50.5 ms                                                | 50.0 ms: 1.01x faster                                                  |
| django_template | 31.7 ms                                                | 32.0 ms: 1.01x slower                                                  |
| mako            | 10.7 ms                                                | 11.3 ms: 1.06x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.00x slower                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250326-linux-x86_64-python-52b5eb95b770fa00ebbd-3.14.0a6+-52b5eb9 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 309 ms: 1.50x faster                                                   |
| async_tree_io_tg           | 861 ms                                                 | 610 ms: 1.41x faster                                                   |
| async_tree_memoization     | 437 ms                                                 | 311 ms: 1.40x faster                                                   |
| deepcopy                   | 354 us                                                 | 259 us: 1.37x faster                                                   |
| async_tree_io              | 838 ms                                                 | 612 ms: 1.37x faster                                                   |
| async_tree_none            | 350 ms                                                 | 257 ms: 1.36x faster                                                   |
| deepcopy_memo              | 38.4 us                                                | 29.3 us: 1.31x faster                                                  |
| async_tree_none_tg         | 319 ms                                                 | 246 ms: 1.30x faster                                                   |
| deepcopy_reduce            | 3.24 us                                                | 2.69 us: 1.20x faster                                                  |
| go                         | 141 ms                                                 | 117 ms: 1.20x faster                                                   |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 487 ms: 1.18x faster                                                   |
| regex_v8                   | 26.9 ms                                                | 23.0 ms: 1.17x faster                                                  |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 470 ms: 1.16x faster                                                   |
| spectral_norm              | 113 ms                                                 | 99.0 ms: 1.14x faster                                                  |
| pylint                     | 312 ms                                                 | 276 ms: 1.13x faster                                                   |
| float                      | 78.7 ms                                                | 70.5 ms: 1.12x faster                                                  |
| async_generators           | 433 ms                                                 | 389 ms: 1.11x faster                                                   |
| dulwich_log                | 64.6 ms                                                | 58.1 ms: 1.11x faster                                                  |
| xml_etree_parse            | 154 ms                                                 | 142 ms: 1.09x faster                                                   |
| regex_effbot               | 3.77 ms                                                | 3.47 ms: 1.09x faster                                                  |
| tomli_loads                | 2.12 sec                                               | 1.97 sec: 1.08x faster                                                 |
| richards                   | 47.5 ms                                                | 44.5 ms: 1.07x faster                                                  |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.72 ms: 1.07x faster                                                  |
| pyflate                    | 470 ms                                                 | 442 ms: 1.06x faster                                                   |
| telco                      | 8.40 ms                                                | 7.93 ms: 1.06x faster                                                  |
| genshi_text                | 22.6 ms                                                | 21.4 ms: 1.06x faster                                                  |
| sqlite_synth               | 2.90 us                                                | 2.75 us: 1.05x faster                                                  |
| richards_super             | 53.7 ms                                                | 51.0 ms: 1.05x faster                                                  |
| k_core                     | 2.37 sec                                               | 2.26 sec: 1.05x faster                                                 |
| regex_compile              | 132 ms                                                 | 127 ms: 1.04x faster                                                   |
| pathlib                    | 17.4 ms                                                | 16.7 ms: 1.04x faster                                                  |
| thrift                     | 800 us                                                 | 772 us: 1.04x faster                                                   |
| scimark_fft                | 367 ms                                                 | 355 ms: 1.03x faster                                                   |
| 2to3                       | 266 ms                                                 | 258 ms: 1.03x faster                                                   |
| mdp                        | 2.54 sec                                               | 2.48 sec: 1.02x faster                                                 |
| html5lib                   | 63.4 ms                                                | 61.9 ms: 1.02x faster                                                  |
| xml_etree_iterparse        | 101 ms                                                 | 99.0 ms: 1.02x faster                                                  |
| pycparser                  | 1.20 sec                                               | 1.18 sec: 1.02x faster                                                 |
| bpe_tokeniser              | 4.69 sec                                               | 4.60 sec: 1.02x faster                                                 |
| scimark_sor                | 122 ms                                                 | 120 ms: 1.02x faster                                                   |
| xml_etree_process          | 60.5 ms                                                | 59.3 ms: 1.02x faster                                                  |
| xml_etree_generate         | 86.8 ms                                                | 85.2 ms: 1.02x faster                                                  |
| sqlalchemy_declarative     | 133 ms                                                 | 131 ms: 1.02x faster                                                   |
| logging_simple             | 5.65 us                                                | 5.56 us: 1.02x faster                                                  |
| sympy_str                  | 273 ms                                                 | 268 ms: 1.02x faster                                                   |
| sympy_integrate            | 19.8 ms                                                | 19.5 ms: 1.01x faster                                                  |
| meteor_contest             | 108 ms                                                 | 107 ms: 1.01x faster                                                   |
| logging_format             | 6.23 us                                                | 6.16 us: 1.01x faster                                                  |
| sympy_sum                  | 150 ms                                                 | 149 ms: 1.01x faster                                                   |
| gc_traversal               | 4.90 ms                                                | 4.84 ms: 1.01x faster                                                  |
| deltablue                  | 3.19 ms                                                | 3.16 ms: 1.01x faster                                                  |
| logging_silent             | 101 ns                                                 | 99.9 ns: 1.01x faster                                                  |
| sqlalchemy_imperative      | 16.9 ms                                                | 16.7 ms: 1.01x faster                                                  |
| genshi_xml                 | 50.5 ms                                                | 50.0 ms: 1.01x faster                                                  |
| generators                 | 28.8 ms                                                | 28.6 ms: 1.01x faster                                                  |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                                   |
| crypto_pyaes               | 74.7 ms                                                | 74.5 ms: 1.00x faster                                                  |
| pprint_pformat             | 1.48 sec                                               | 1.49 sec: 1.01x slower                                                 |
| typing_runtime_protocols   | 160 us                                                 | 161 us: 1.01x slower                                                   |
| django_template            | 31.7 ms                                                | 32.0 ms: 1.01x slower                                                  |
| chaos                      | 58.0 ms                                                | 58.8 ms: 1.01x slower                                                  |
| raytrace                   | 262 ms                                                 | 265 ms: 1.02x slower                                                   |
| shortest_path              | 487 ms                                                 | 494 ms: 1.02x slower                                                   |
| docutils                   | 2.58 sec                                               | 2.63 sec: 1.02x slower                                                 |
| scimark_monte_carlo        | 66.8 ms                                                | 68.0 ms: 1.02x slower                                                  |
| create_gc_cycles           | 2.45 ms                                                | 2.50 ms: 1.02x slower                                                  |
| regex_dna                  | 220 ms                                                 | 224 ms: 1.02x slower                                                   |
| nqueens                    | 80.9 ms                                                | 82.7 ms: 1.02x slower                                                  |
| scimark_lu                 | 114 ms                                                 | 117 ms: 1.02x slower                                                   |
| comprehensions             | 16.5 us                                                | 16.9 us: 1.02x slower                                                  |
| unpickle_pure_python       | 213 us                                                 | 218 us: 1.02x slower                                                   |
| hexiom                     | 6.08 ms                                                | 6.25 ms: 1.03x slower                                                  |
| python_startup             | 12.7 ms                                                | 13.1 ms: 1.03x slower                                                  |
| pickle_pure_python         | 302 us                                                 | 319 us: 1.06x slower                                                   |
| coroutines                 | 22.2 ms                                                | 23.5 ms: 1.06x slower                                                  |
| mako                       | 10.7 ms                                                | 11.3 ms: 1.06x slower                                                  |
| fannkuch                   | 394 ms                                                 | 418 ms: 1.06x slower                                                   |
| bench_thread_pool          | 818 us                                                 | 870 us: 1.06x slower                                                   |
| json_loads                 | 27.2 us                                                | 30.0 us: 1.10x slower                                                  |
| many_optionals             | 857 us                                                 | 951 us: 1.11x slower                                                   |
| coverage                   | 82.8 ms                                                | 91.9 ms: 1.11x slower                                                  |
| nbody                      | 87.7 ms                                                | 97.3 ms: 1.11x slower                                                  |
| json_dumps                 | 10.1 ms                                                | 11.7 ms: 1.16x slower                                                  |
| python_startup_no_site     | 7.00 ms                                                | 8.19 ms: 1.17x slower                                                  |
| subparsers                 | 15.5 ms                                                | 20.8 ms: 1.35x slower                                                  |
| bench_mp_pool              | 24.0 ms                                                | 82.9 ms: 3.46x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                           |

Benchmark hidden because not significant (6): sphinx, json, pprint_safe_repr, asyncio_websockets, sympy_expand, connected_components
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250326-3.14.0a6+-52b5eb9/bm-20250326-linux-x86_64-python-52b5eb95b770fa00ebbd-3.14.0a6+-52b5eb9.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.040x faster

# HPT report

- Reliability score: 99.96% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.03x