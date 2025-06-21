# Results vs. 3.13.0

- fork: brandtbucher
- ref: justin_hot
- machine: linux-x86_64
- commit hash: 4cfabf5
- commit date: 2025-06-20
- overall geometric mean: 1.049x faster
- HPT reliability: 99.64%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250620-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-4cfabf5 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 260 ms: 1.02x faster                                              |
| docutils       | 2.58 sec                                               | 2.64 sec: 1.02x slower                                            |
| html5lib       | 63.4 ms                                                | 61.9 ms: 1.02x faster                                             |
| Geometric mean | (ref)                                                  | 1.01x faster                                                      |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250620-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-4cfabf5 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 318 ms: 1.46x faster                                              |
| async_tree_io              | 838 ms                                                 | 604 ms: 1.39x faster                                              |
| async_tree_io_tg           | 861 ms                                                 | 622 ms: 1.38x faster                                              |
| async_tree_memoization     | 437 ms                                                 | 319 ms: 1.37x faster                                              |
| async_tree_none            | 350 ms                                                 | 265 ms: 1.32x faster                                              |
| async_tree_none_tg         | 319 ms                                                 | 251 ms: 1.27x faster                                              |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 500 ms: 1.15x faster                                              |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 492 ms: 1.10x faster                                              |
| coroutines                 | 22.2 ms                                                | 25.3 ms: 1.14x slower                                             |
| Geometric mean             | (ref)                                                  | 1.20x faster                                                      |

Benchmark hidden because not significant (2): async_generators, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250620-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-4cfabf5 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| float          | 78.7 ms                                                | 64.9 ms: 1.21x faster                                             |
| pidigits       | 186 ms                                                 | 187 ms: 1.00x slower                                              |
| nbody          | 87.7 ms                                                | 92.2 ms: 1.05x slower                                             |
| Geometric mean | (ref)                                                  | 1.05x faster                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250620-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-4cfabf5 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_v8       | 26.9 ms                                                | 22.8 ms: 1.18x faster                                             |
| regex_effbot   | 3.77 ms                                                | 3.31 ms: 1.14x faster                                             |
| regex_dna      | 220 ms                                                 | 197 ms: 1.12x faster                                              |
| regex_compile  | 132 ms                                                 | 127 ms: 1.04x faster                                              |
| Geometric mean | (ref)                                                  | 1.12x faster                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250620-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-4cfabf5 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.90 sec: 1.11x faster                                            |
| xml_etree_parse      | 154 ms                                                 | 141 ms: 1.10x faster                                              |
| xml_etree_generate   | 86.8 ms                                                | 80.1 ms: 1.08x faster                                             |
| xml_etree_process    | 60.5 ms                                                | 56.0 ms: 1.08x faster                                             |
| unpickle_pure_python | 213 us                                                 | 199 us: 1.07x faster                                              |
| xml_etree_iterparse  | 101 ms                                                 | 100 ms: 1.01x faster                                              |
| json_loads           | 27.2 us                                                | 28.6 us: 1.05x slower                                             |
| pickle_pure_python   | 302 us                                                 | 329 us: 1.09x slower                                              |
| json_dumps           | 10.1 ms                                                | 11.3 ms: 1.12x slower                                             |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250620-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-4cfabf5 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 12.2 ms: 1.04x faster                                             |
| python_startup_no_site | 7.00 ms                                                | 6.95 ms: 1.01x faster                                             |
| Geometric mean         | (ref)                                                  | 1.02x faster                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250620-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-4cfabf5 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.7 ms: 1.04x faster                                             |
| genshi_xml      | 50.5 ms                                                | 50.0 ms: 1.01x faster                                             |
| mako            | 10.7 ms                                                | 10.6 ms: 1.01x faster                                             |
| django_template | 31.7 ms                                                | 32.8 ms: 1.04x slower                                             |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                      |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250620-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-4cfabf5 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.27 sec: 2.00x faster                                            |
| async_tree_memoization_tg  | 463 ms                                                 | 318 ms: 1.46x faster                                              |
| richards                   | 47.5 ms                                                | 34.1 ms: 1.39x faster                                             |
| async_tree_io              | 838 ms                                                 | 604 ms: 1.39x faster                                              |
| async_tree_io_tg           | 861 ms                                                 | 622 ms: 1.38x faster                                              |
| deepcopy                   | 354 us                                                 | 258 us: 1.37x faster                                              |
| async_tree_memoization     | 437 ms                                                 | 319 ms: 1.37x faster                                              |
| richards_super             | 53.7 ms                                                | 39.4 ms: 1.36x faster                                             |
| async_tree_none            | 350 ms                                                 | 265 ms: 1.32x faster                                              |
| deepcopy_memo              | 38.4 us                                                | 29.9 us: 1.28x faster                                             |
| async_tree_none_tg         | 319 ms                                                 | 251 ms: 1.27x faster                                              |
| float                      | 78.7 ms                                                | 64.9 ms: 1.21x faster                                             |
| deepcopy_reduce            | 3.24 us                                                | 2.73 us: 1.19x faster                                             |
| regex_v8                   | 26.9 ms                                                | 22.8 ms: 1.18x faster                                             |
| go                         | 141 ms                                                 | 122 ms: 1.16x faster                                              |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 500 ms: 1.15x faster                                              |
| regex_effbot               | 3.77 ms                                                | 3.31 ms: 1.14x faster                                             |
| regex_dna                  | 220 ms                                                 | 197 ms: 1.12x faster                                              |
| tomli_loads                | 2.12 sec                                               | 1.90 sec: 1.11x faster                                            |
| pyflate                    | 470 ms                                                 | 422 ms: 1.11x faster                                              |
| scimark_fft                | 367 ms                                                 | 330 ms: 1.11x faster                                              |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 492 ms: 1.10x faster                                              |
| pylint                     | 312 ms                                                 | 284 ms: 1.10x faster                                              |
| xml_etree_parse            | 154 ms                                                 | 141 ms: 1.10x faster                                              |
| telco                      | 8.40 ms                                                | 7.67 ms: 1.10x faster                                             |
| spectral_norm              | 113 ms                                                 | 104 ms: 1.09x faster                                              |
| dulwich_log                | 64.6 ms                                                | 59.5 ms: 1.08x faster                                             |
| xml_etree_generate         | 86.8 ms                                                | 80.1 ms: 1.08x faster                                             |
| xml_etree_process          | 60.5 ms                                                | 56.0 ms: 1.08x faster                                             |
| unpickle_pure_python       | 213 us                                                 | 199 us: 1.07x faster                                              |
| bpe_tokeniser              | 4.69 sec                                               | 4.41 sec: 1.06x faster                                            |
| pycparser                  | 1.20 sec                                               | 1.14 sec: 1.05x faster                                            |
| genshi_text                | 22.6 ms                                                | 21.7 ms: 1.04x faster                                             |
| python_startup             | 12.7 ms                                                | 12.2 ms: 1.04x faster                                             |
| sqlite_synth               | 2.90 us                                                | 2.80 us: 1.04x faster                                             |
| regex_compile              | 132 ms                                                 | 127 ms: 1.04x faster                                              |
| gc_traversal               | 4.90 ms                                                | 4.75 ms: 1.03x faster                                             |
| k_core                     | 2.37 sec                                               | 2.31 sec: 1.03x faster                                            |
| pathlib                    | 17.4 ms                                                | 16.9 ms: 1.03x faster                                             |
| deltablue                  | 3.19 ms                                                | 3.12 ms: 1.02x faster                                             |
| html5lib                   | 63.4 ms                                                | 61.9 ms: 1.02x faster                                             |
| 2to3                       | 266 ms                                                 | 260 ms: 1.02x faster                                              |
| sympy_integrate            | 19.8 ms                                                | 19.5 ms: 1.02x faster                                             |
| thrift                     | 800 us                                                 | 787 us: 1.02x faster                                              |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.95 ms: 1.02x faster                                             |
| meteor_contest             | 108 ms                                                 | 107 ms: 1.01x faster                                              |
| xml_etree_iterparse        | 101 ms                                                 | 100 ms: 1.01x faster                                              |
| genshi_xml                 | 50.5 ms                                                | 50.0 ms: 1.01x faster                                             |
| python_startup_no_site     | 7.00 ms                                                | 6.95 ms: 1.01x faster                                             |
| mako                       | 10.7 ms                                                | 10.6 ms: 1.01x faster                                             |
| sympy_sum                  | 150 ms                                                 | 150 ms: 1.00x faster                                              |
| pidigits                   | 186 ms                                                 | 187 ms: 1.00x slower                                              |
| crypto_pyaes               | 74.7 ms                                                | 74.9 ms: 1.00x slower                                             |
| scimark_sor                | 122 ms                                                 | 123 ms: 1.01x slower                                              |
| shortest_path              | 487 ms                                                 | 492 ms: 1.01x slower                                              |
| docutils                   | 2.58 sec                                               | 2.64 sec: 1.02x slower                                            |
| sympy_expand               | 456 ms                                                 | 466 ms: 1.02x slower                                              |
| djangocms                  | 22.3 us                                                | 22.8 us: 1.02x slower                                             |
| nqueens                    | 80.9 ms                                                | 82.9 ms: 1.02x slower                                             |
| connected_components       | 447 ms                                                 | 458 ms: 1.03x slower                                              |
| django_template            | 31.7 ms                                                | 32.8 ms: 1.04x slower                                             |
| comprehensions             | 16.5 us                                                | 17.1 us: 1.04x slower                                             |
| fannkuch                   | 394 ms                                                 | 409 ms: 1.04x slower                                              |
| scimark_lu                 | 114 ms                                                 | 119 ms: 1.04x slower                                              |
| raytrace                   | 262 ms                                                 | 274 ms: 1.05x slower                                              |
| nbody                      | 87.7 ms                                                | 92.2 ms: 1.05x slower                                             |
| json_loads                 | 27.2 us                                                | 28.6 us: 1.05x slower                                             |
| create_gc_cycles           | 2.45 ms                                                | 2.59 ms: 1.06x slower                                             |
| coverage                   | 82.8 ms                                                | 87.6 ms: 1.06x slower                                             |
| typing_runtime_protocols   | 160 us                                                 | 170 us: 1.06x slower                                              |
| hexiom                     | 6.08 ms                                                | 6.44 ms: 1.06x slower                                             |
| generators                 | 28.8 ms                                                | 30.9 ms: 1.08x slower                                             |
| chaos                      | 58.0 ms                                                | 62.4 ms: 1.08x slower                                             |
| pickle_pure_python         | 302 us                                                 | 329 us: 1.09x slower                                              |
| logging_format             | 6.23 us                                                | 6.83 us: 1.10x slower                                             |
| logging_simple             | 5.65 us                                                | 6.25 us: 1.11x slower                                             |
| json_dumps                 | 10.1 ms                                                | 11.3 ms: 1.12x slower                                             |
| pprint_pformat             | 1.48 sec                                               | 1.66 sec: 1.13x slower                                            |
| coroutines                 | 22.2 ms                                                | 25.3 ms: 1.14x slower                                             |
| pprint_safe_repr           | 727 ms                                                 | 835 ms: 1.15x slower                                              |
| many_optionals             | 857 us                                                 | 987 us: 1.15x slower                                              |
| subparsers                 | 15.5 ms                                                | 23.6 ms: 1.53x slower                                             |
| logging_silent             | 101 ns                                                 | 472 ns: 4.67x slower                                              |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                      |

Benchmark hidden because not significant (6): sphinx, json, async_generators, scimark_monte_carlo, asyncio_websockets, sympy_str
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250620-3.15.0a0-4cfabf5-JIT/bm-20250620-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-4cfabf5.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.049x faster

# HPT report

- Reliability score: 99.64% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.07x