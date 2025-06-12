# Results vs. 3.13.0

- fork: brandtbucher
- ref: justin_hot
- machine: linux-x86_64
- commit hash: 5606078
- commit date: 2025-06-11
- overall geometric mean: 1.023x slower
- HPT reliability: 99.60%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250611-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-5606078 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 259 ms: 1.03x faster                                              |
| docutils       | 2.58 sec                                               | 2.64 sec: 1.02x slower                                            |
| html5lib       | 63.4 ms                                                | 62.3 ms: 1.02x faster                                             |
| Geometric mean | (ref)                                                  | 1.01x faster                                                      |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250611-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-5606078 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 317 ms: 1.46x faster                                              |
| async_tree_io              | 838 ms                                                 | 600 ms: 1.40x faster                                              |
| async_tree_memoization     | 437 ms                                                 | 314 ms: 1.39x faster                                              |
| async_tree_io_tg           | 861 ms                                                 | 619 ms: 1.39x faster                                              |
| async_tree_none            | 350 ms                                                 | 263 ms: 1.33x faster                                              |
| async_tree_none_tg         | 319 ms                                                 | 251 ms: 1.27x faster                                              |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 490 ms: 1.17x faster                                              |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 485 ms: 1.12x faster                                              |
| async_generators           | 433 ms                                                 | 425 ms: 1.02x faster                                              |
| coroutines                 | 22.2 ms                                                | 24.7 ms: 1.11x slower                                             |
| Geometric mean             | (ref)                                                  | 1.21x faster                                                      |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250611-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-5606078 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| float          | 78.7 ms                                                | 65.0 ms: 1.21x faster                                             |
| pidigits       | 186 ms                                                 | 187 ms: 1.00x slower                                              |
| nbody          | 87.7 ms                                                | 90.2 ms: 1.03x slower                                             |
| Geometric mean | (ref)                                                  | 1.05x faster                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250611-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-5606078 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_v8       | 26.9 ms                                                | 23.5 ms: 1.14x faster                                             |
| regex_effbot   | 3.77 ms                                                | 3.43 ms: 1.10x faster                                             |
| regex_compile  | 132 ms                                                 | 127 ms: 1.04x faster                                              |
| regex_dna      | 220 ms                                                 | 215 ms: 1.02x faster                                              |
| Geometric mean | (ref)                                                  | 1.07x faster                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250611-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-5606078 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.86 sec: 1.14x faster                                            |
| xml_etree_parse      | 154 ms                                                 | 139 ms: 1.11x faster                                              |
| xml_etree_process    | 60.5 ms                                                | 55.4 ms: 1.09x faster                                             |
| unpickle_pure_python | 213 us                                                 | 196 us: 1.09x faster                                              |
| xml_etree_generate   | 86.8 ms                                                | 80.2 ms: 1.08x faster                                             |
| xml_etree_iterparse  | 101 ms                                                 | 98.0 ms: 1.03x faster                                             |
| json_loads           | 27.2 us                                                | 27.8 us: 1.02x slower                                             |
| pickle_pure_python   | 302 us                                                 | 322 us: 1.06x slower                                              |
| json_dumps           | 10.1 ms                                                | 11.0 ms: 1.08x slower                                             |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250611-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-5606078 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 12.1 ms: 1.04x faster                                             |
| python_startup_no_site | 7.00 ms                                                | 6.91 ms: 1.01x faster                                             |
| Geometric mean         | (ref)                                                  | 1.03x faster                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250611-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-5606078 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.0 ms: 1.08x faster                                             |
| genshi_xml      | 50.5 ms                                                | 49.8 ms: 1.01x faster                                             |
| mako            | 10.7 ms                                                | 10.5 ms: 1.01x faster                                             |
| django_template | 31.7 ms                                                | 32.6 ms: 1.03x slower                                             |
| Geometric mean  | (ref)                                                  | 1.02x faster                                                      |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250611-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-5606078 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.26 sec: 2.02x faster                                            |
| async_tree_memoization_tg  | 463 ms                                                 | 317 ms: 1.46x faster                                              |
| richards                   | 47.5 ms                                                | 32.6 ms: 1.46x faster                                             |
| richards_super             | 53.7 ms                                                | 38.0 ms: 1.41x faster                                             |
| async_tree_io              | 838 ms                                                 | 600 ms: 1.40x faster                                              |
| async_tree_memoization     | 437 ms                                                 | 314 ms: 1.39x faster                                              |
| async_tree_io_tg           | 861 ms                                                 | 619 ms: 1.39x faster                                              |
| deepcopy                   | 354 us                                                 | 262 us: 1.35x faster                                              |
| async_tree_none            | 350 ms                                                 | 263 ms: 1.33x faster                                              |
| deepcopy_memo              | 38.4 us                                                | 29.7 us: 1.29x faster                                             |
| async_tree_none_tg         | 319 ms                                                 | 251 ms: 1.27x faster                                              |
| float                      | 78.7 ms                                                | 65.0 ms: 1.21x faster                                             |
| go                         | 141 ms                                                 | 116 ms: 1.21x faster                                              |
| deepcopy_reduce            | 3.24 us                                                | 2.75 us: 1.18x faster                                             |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 490 ms: 1.17x faster                                              |
| spectral_norm              | 113 ms                                                 | 98.9 ms: 1.14x faster                                             |
| regex_v8                   | 26.9 ms                                                | 23.5 ms: 1.14x faster                                             |
| pyflate                    | 470 ms                                                 | 412 ms: 1.14x faster                                              |
| tomli_loads                | 2.12 sec                                               | 1.86 sec: 1.14x faster                                            |
| scimark_fft                | 367 ms                                                 | 323 ms: 1.14x faster                                              |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 485 ms: 1.12x faster                                              |
| xml_etree_parse            | 154 ms                                                 | 139 ms: 1.11x faster                                              |
| pylint                     | 312 ms                                                 | 283 ms: 1.10x faster                                              |
| regex_effbot               | 3.77 ms                                                | 3.43 ms: 1.10x faster                                             |
| xml_etree_process          | 60.5 ms                                                | 55.4 ms: 1.09x faster                                             |
| unpickle_pure_python       | 213 us                                                 | 196 us: 1.09x faster                                              |
| xml_etree_generate         | 86.8 ms                                                | 80.2 ms: 1.08x faster                                             |
| telco                      | 8.40 ms                                                | 7.78 ms: 1.08x faster                                             |
| genshi_text                | 22.6 ms                                                | 21.0 ms: 1.08x faster                                             |
| bpe_tokeniser              | 4.69 sec                                               | 4.36 sec: 1.07x faster                                            |
| dulwich_log                | 64.6 ms                                                | 61.8 ms: 1.05x faster                                             |
| json                       | 5.32 ms                                                | 5.10 ms: 1.04x faster                                             |
| python_startup             | 12.7 ms                                                | 12.1 ms: 1.04x faster                                             |
| deltablue                  | 3.19 ms                                                | 3.07 ms: 1.04x faster                                             |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.83 ms: 1.04x faster                                             |
| regex_compile              | 132 ms                                                 | 127 ms: 1.04x faster                                              |
| pycparser                  | 1.20 sec                                               | 1.16 sec: 1.04x faster                                            |
| xml_etree_iterparse        | 101 ms                                                 | 98.0 ms: 1.03x faster                                             |
| sqlite_synth               | 2.90 us                                                | 2.81 us: 1.03x faster                                             |
| 2to3                       | 266 ms                                                 | 259 ms: 1.03x faster                                              |
| k_core                     | 2.37 sec                                               | 2.31 sec: 1.03x faster                                            |
| regex_dna                  | 220 ms                                                 | 215 ms: 1.02x faster                                              |
| sympy_integrate            | 19.8 ms                                                | 19.4 ms: 1.02x faster                                             |
| pathlib                    | 17.4 ms                                                | 17.0 ms: 1.02x faster                                             |
| async_generators           | 433 ms                                                 | 425 ms: 1.02x faster                                              |
| scimark_monte_carlo        | 66.8 ms                                                | 65.6 ms: 1.02x faster                                             |
| scimark_sor                | 122 ms                                                 | 120 ms: 1.02x faster                                              |
| html5lib                   | 63.4 ms                                                | 62.3 ms: 1.02x faster                                             |
| python_startup_no_site     | 7.00 ms                                                | 6.91 ms: 1.01x faster                                             |
| genshi_xml                 | 50.5 ms                                                | 49.8 ms: 1.01x faster                                             |
| mako                       | 10.7 ms                                                | 10.5 ms: 1.01x faster                                             |
| crypto_pyaes               | 74.7 ms                                                | 74.0 ms: 1.01x faster                                             |
| meteor_contest             | 108 ms                                                 | 107 ms: 1.01x faster                                              |
| pidigits                   | 186 ms                                                 | 187 ms: 1.00x slower                                              |
| sympy_sum                  | 150 ms                                                 | 151 ms: 1.00x slower                                              |
| comprehensions             | 16.5 us                                                | 16.7 us: 1.01x slower                                             |
| fannkuch                   | 394 ms                                                 | 401 ms: 1.02x slower                                              |
| json_loads                 | 27.2 us                                                | 27.8 us: 1.02x slower                                             |
| docutils                   | 2.58 sec                                               | 2.64 sec: 1.02x slower                                            |
| connected_components       | 447 ms                                                 | 459 ms: 1.03x slower                                              |
| sympy_expand               | 456 ms                                                 | 469 ms: 1.03x slower                                              |
| gc_traversal               | 4.90 ms                                                | 5.03 ms: 1.03x slower                                             |
| shortest_path              | 487 ms                                                 | 500 ms: 1.03x slower                                              |
| nbody                      | 87.7 ms                                                | 90.2 ms: 1.03x slower                                             |
| django_template            | 31.7 ms                                                | 32.6 ms: 1.03x slower                                             |
| hexiom                     | 6.08 ms                                                | 6.32 ms: 1.04x slower                                             |
| nqueens                    | 80.9 ms                                                | 84.2 ms: 1.04x slower                                             |
| generators                 | 28.8 ms                                                | 30.0 ms: 1.04x slower                                             |
| raytrace                   | 262 ms                                                 | 274 ms: 1.05x slower                                              |
| typing_runtime_protocols   | 160 us                                                 | 168 us: 1.05x slower                                              |
| create_gc_cycles           | 2.45 ms                                                | 2.58 ms: 1.05x slower                                             |
| chaos                      | 58.0 ms                                                | 61.7 ms: 1.06x slower                                             |
| pickle_pure_python         | 302 us                                                 | 322 us: 1.06x slower                                              |
| scimark_lu                 | 114 ms                                                 | 122 ms: 1.07x slower                                              |
| pprint_safe_repr           | 727 ms                                                 | 785 ms: 1.08x slower                                              |
| json_dumps                 | 10.1 ms                                                | 11.0 ms: 1.08x slower                                             |
| logging_simple             | 5.65 us                                                | 6.15 us: 1.09x slower                                             |
| logging_format             | 6.23 us                                                | 6.82 us: 1.10x slower                                             |
| pprint_pformat             | 1.48 sec                                               | 1.63 sec: 1.10x slower                                            |
| coroutines                 | 22.2 ms                                                | 24.7 ms: 1.11x slower                                             |
| many_optionals             | 857 us                                                 | 978 us: 1.14x slower                                              |
| subparsers                 | 15.5 ms                                                | 23.5 ms: 1.52x slower                                             |
| logging_silent             | 101 ns                                                 | 475 ns: 4.70x slower                                              |
| coverage                   | 82.8 ms                                                | 428 ms: 5.17x slower                                              |
| thrift                     | 800 us                                                 | 148 ms: 185.30x slower                                            |
| Geometric mean             | (ref)                                                  | 1.04x slower                                                      |

Benchmark hidden because not significant (3): sphinx, sympy_str, asyncio_websockets
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250611-3.15.0a0-5606078-JIT/bm-20250611-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-5606078.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.023x slower

# HPT report

- Reliability score: 99.60% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.07x