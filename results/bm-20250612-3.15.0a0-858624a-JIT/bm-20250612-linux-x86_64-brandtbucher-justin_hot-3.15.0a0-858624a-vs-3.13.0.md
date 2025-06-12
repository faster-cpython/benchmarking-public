# Results vs. 3.13.0

- fork: brandtbucher
- ref: justin_hot
- machine: linux-x86_64
- commit hash: 858624a
- commit date: 2025-06-12
- overall geometric mean: 1.026x slower
- HPT reliability: 99.31%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250612-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-858624a |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 260 ms: 1.02x faster                                              |
| docutils       | 2.58 sec                                               | 2.65 sec: 1.02x slower                                            |
| html5lib       | 63.4 ms                                                | 62.3 ms: 1.02x faster                                             |
| Geometric mean | (ref)                                                  | 1.01x faster                                                      |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250612-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-858624a |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 315 ms: 1.47x faster                                              |
| async_tree_io              | 838 ms                                                 | 597 ms: 1.40x faster                                              |
| async_tree_memoization     | 437 ms                                                 | 312 ms: 1.40x faster                                              |
| async_tree_io_tg           | 861 ms                                                 | 617 ms: 1.39x faster                                              |
| async_tree_none            | 350 ms                                                 | 260 ms: 1.35x faster                                              |
| async_tree_none_tg         | 319 ms                                                 | 248 ms: 1.29x faster                                              |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 498 ms: 1.15x faster                                              |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 490 ms: 1.11x faster                                              |
| async_generators           | 433 ms                                                 | 431 ms: 1.01x faster                                              |
| coroutines                 | 22.2 ms                                                | 25.1 ms: 1.13x slower                                             |
| Geometric mean             | (ref)                                                  | 1.21x faster                                                      |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250612-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-858624a |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| float          | 78.7 ms                                                | 65.2 ms: 1.21x faster                                             |
| pidigits       | 186 ms                                                 | 187 ms: 1.00x slower                                              |
| nbody          | 87.7 ms                                                | 93.5 ms: 1.07x slower                                             |
| Geometric mean | (ref)                                                  | 1.04x faster                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250612-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-858624a |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_v8       | 26.9 ms                                                | 23.7 ms: 1.14x faster                                             |
| regex_effbot   | 3.77 ms                                                | 3.45 ms: 1.09x faster                                             |
| regex_compile  | 132 ms                                                 | 128 ms: 1.03x faster                                              |
| Geometric mean | (ref)                                                  | 1.07x faster                                                      |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250612-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-858624a |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.87 sec: 1.13x faster                                            |
| xml_etree_process    | 60.5 ms                                                | 54.7 ms: 1.11x faster                                             |
| xml_etree_parse      | 154 ms                                                 | 140 ms: 1.10x faster                                              |
| xml_etree_generate   | 86.8 ms                                                | 79.0 ms: 1.10x faster                                             |
| unpickle_pure_python | 213 us                                                 | 194 us: 1.10x faster                                              |
| xml_etree_iterparse  | 101 ms                                                 | 98.2 ms: 1.03x faster                                             |
| json_loads           | 27.2 us                                                | 28.1 us: 1.03x slower                                             |
| pickle_pure_python   | 302 us                                                 | 321 us: 1.06x slower                                              |
| json_dumps           | 10.1 ms                                                | 11.3 ms: 1.11x slower                                             |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250612-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-858624a |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 12.2 ms: 1.04x faster                                             |
| python_startup_no_site | 7.00 ms                                                | 6.93 ms: 1.01x faster                                             |
| Geometric mean         | (ref)                                                  | 1.03x faster                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250612-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-858624a |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.4 ms: 1.06x faster                                             |
| genshi_xml      | 50.5 ms                                                | 49.9 ms: 1.01x faster                                             |
| mako            | 10.7 ms                                                | 10.6 ms: 1.01x faster                                             |
| django_template | 31.7 ms                                                | 32.4 ms: 1.02x slower                                             |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                      |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250612-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-858624a |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.24 sec: 2.06x faster                                            |
| async_tree_memoization_tg  | 463 ms                                                 | 315 ms: 1.47x faster                                              |
| richards                   | 47.5 ms                                                | 32.9 ms: 1.44x faster                                             |
| async_tree_io              | 838 ms                                                 | 597 ms: 1.40x faster                                              |
| richards_super             | 53.7 ms                                                | 38.3 ms: 1.40x faster                                             |
| async_tree_memoization     | 437 ms                                                 | 312 ms: 1.40x faster                                              |
| async_tree_io_tg           | 861 ms                                                 | 617 ms: 1.39x faster                                              |
| deepcopy                   | 354 us                                                 | 258 us: 1.37x faster                                              |
| async_tree_none            | 350 ms                                                 | 260 ms: 1.35x faster                                              |
| deepcopy_memo              | 38.4 us                                                | 29.6 us: 1.30x faster                                             |
| async_tree_none_tg         | 319 ms                                                 | 248 ms: 1.29x faster                                              |
| float                      | 78.7 ms                                                | 65.2 ms: 1.21x faster                                             |
| deepcopy_reduce            | 3.24 us                                                | 2.69 us: 1.20x faster                                             |
| go                         | 141 ms                                                 | 117 ms: 1.20x faster                                              |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 498 ms: 1.15x faster                                              |
| regex_v8                   | 26.9 ms                                                | 23.7 ms: 1.14x faster                                             |
| tomli_loads                | 2.12 sec                                               | 1.87 sec: 1.13x faster                                            |
| pyflate                    | 470 ms                                                 | 416 ms: 1.13x faster                                              |
| scimark_fft                | 367 ms                                                 | 330 ms: 1.11x faster                                              |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 490 ms: 1.11x faster                                              |
| xml_etree_process          | 60.5 ms                                                | 54.7 ms: 1.11x faster                                             |
| pylint                     | 312 ms                                                 | 283 ms: 1.10x faster                                              |
| xml_etree_parse            | 154 ms                                                 | 140 ms: 1.10x faster                                              |
| xml_etree_generate         | 86.8 ms                                                | 79.0 ms: 1.10x faster                                             |
| unpickle_pure_python       | 213 us                                                 | 194 us: 1.10x faster                                              |
| spectral_norm              | 113 ms                                                 | 103 ms: 1.10x faster                                              |
| regex_effbot               | 3.77 ms                                                | 3.45 ms: 1.09x faster                                             |
| telco                      | 8.40 ms                                                | 7.76 ms: 1.08x faster                                             |
| bpe_tokeniser              | 4.69 sec                                               | 4.37 sec: 1.07x faster                                            |
| genshi_text                | 22.6 ms                                                | 21.4 ms: 1.06x faster                                             |
| dulwich_log                | 64.6 ms                                                | 61.5 ms: 1.05x faster                                             |
| deltablue                  | 3.19 ms                                                | 3.06 ms: 1.05x faster                                             |
| python_startup             | 12.7 ms                                                | 12.2 ms: 1.04x faster                                             |
| regex_compile              | 132 ms                                                 | 128 ms: 1.03x faster                                              |
| k_core                     | 2.37 sec                                               | 2.29 sec: 1.03x faster                                            |
| xml_etree_iterparse        | 101 ms                                                 | 98.2 ms: 1.03x faster                                             |
| sqlite_synth               | 2.90 us                                                | 2.82 us: 1.03x faster                                             |
| sympy_integrate            | 19.8 ms                                                | 19.3 ms: 1.03x faster                                             |
| pathlib                    | 17.4 ms                                                | 17.0 ms: 1.02x faster                                             |
| scimark_monte_carlo        | 66.8 ms                                                | 65.3 ms: 1.02x faster                                             |
| 2to3                       | 266 ms                                                 | 260 ms: 1.02x faster                                              |
| pycparser                  | 1.20 sec                                               | 1.17 sec: 1.02x faster                                            |
| json                       | 5.32 ms                                                | 5.21 ms: 1.02x faster                                             |
| html5lib                   | 63.4 ms                                                | 62.3 ms: 1.02x faster                                             |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.95 ms: 1.02x faster                                             |
| scimark_sor                | 122 ms                                                 | 121 ms: 1.01x faster                                              |
| genshi_xml                 | 50.5 ms                                                | 49.9 ms: 1.01x faster                                             |
| meteor_contest             | 108 ms                                                 | 107 ms: 1.01x faster                                              |
| mako                       | 10.7 ms                                                | 10.6 ms: 1.01x faster                                             |
| python_startup_no_site     | 7.00 ms                                                | 6.93 ms: 1.01x faster                                             |
| sympy_sum                  | 150 ms                                                 | 149 ms: 1.01x faster                                              |
| async_generators           | 433 ms                                                 | 431 ms: 1.01x faster                                              |
| pidigits                   | 186 ms                                                 | 187 ms: 1.00x slower                                              |
| crypto_pyaes               | 74.7 ms                                                | 74.9 ms: 1.00x slower                                             |
| shortest_path              | 487 ms                                                 | 495 ms: 1.02x slower                                              |
| django_template            | 31.7 ms                                                | 32.4 ms: 1.02x slower                                             |
| docutils                   | 2.58 sec                                               | 2.65 sec: 1.02x slower                                            |
| nqueens                    | 80.9 ms                                                | 82.9 ms: 1.02x slower                                             |
| fannkuch                   | 394 ms                                                 | 404 ms: 1.03x slower                                              |
| connected_components       | 447 ms                                                 | 459 ms: 1.03x slower                                              |
| sympy_expand               | 456 ms                                                 | 469 ms: 1.03x slower                                              |
| hexiom                     | 6.08 ms                                                | 6.27 ms: 1.03x slower                                             |
| json_loads                 | 27.2 us                                                | 28.1 us: 1.03x slower                                             |
| typing_runtime_protocols   | 160 us                                                 | 168 us: 1.05x slower                                              |
| raytrace                   | 262 ms                                                 | 274 ms: 1.05x slower                                              |
| gc_traversal               | 4.90 ms                                                | 5.14 ms: 1.05x slower                                             |
| generators                 | 28.8 ms                                                | 30.4 ms: 1.06x slower                                             |
| create_gc_cycles           | 2.45 ms                                                | 2.59 ms: 1.06x slower                                             |
| scimark_lu                 | 114 ms                                                 | 121 ms: 1.06x slower                                              |
| pickle_pure_python         | 302 us                                                 | 321 us: 1.06x slower                                              |
| nbody                      | 87.7 ms                                                | 93.5 ms: 1.07x slower                                             |
| chaos                      | 58.0 ms                                                | 62.6 ms: 1.08x slower                                             |
| logging_format             | 6.23 us                                                | 6.79 us: 1.09x slower                                             |
| pprint_pformat             | 1.48 sec                                               | 1.61 sec: 1.09x slower                                            |
| pprint_safe_repr           | 727 ms                                                 | 800 ms: 1.10x slower                                              |
| logging_simple             | 5.65 us                                                | 6.24 us: 1.10x slower                                             |
| json_dumps                 | 10.1 ms                                                | 11.3 ms: 1.11x slower                                             |
| coroutines                 | 22.2 ms                                                | 25.1 ms: 1.13x slower                                             |
| many_optionals             | 857 us                                                 | 979 us: 1.14x slower                                              |
| subparsers                 | 15.5 ms                                                | 23.6 ms: 1.53x slower                                             |
| logging_silent             | 101 ns                                                 | 475 ns: 4.70x slower                                              |
| coverage                   | 82.8 ms                                                | 425 ms: 5.13x slower                                              |
| thrift                     | 800 us                                                 | 148 ms: 185.36x slower                                            |
| Geometric mean             | (ref)                                                  | 1.04x slower                                                      |

Benchmark hidden because not significant (5): sphinx, regex_dna, sympy_str, comprehensions, asyncio_websockets
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250612-3.15.0a0-858624a-JIT/bm-20250612-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-858624a.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.026x slower

# HPT report

- Reliability score: 99.31% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.07x