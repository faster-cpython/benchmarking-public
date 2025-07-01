# Results vs. 3.13.0

- fork: brandtbucher
- ref: jit_up_12_6
- machine: linux-x86_64
- commit hash: a33098b
- commit date: 2025-06-30
- overall geometric mean: 1.068x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250630-linux-x86_64-brandtbucher-jit_up_12_6-3.15.0a0-a33098b |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 258 ms: 1.03x faster                                               |
| docutils       | 2.58 sec                                               | 2.64 sec: 1.02x slower                                             |
| html5lib       | 63.4 ms                                                | 62.7 ms: 1.01x faster                                              |
| sphinx         | 1.03 sec                                               | 1.02 sec: 1.02x faster                                             |
| Geometric mean | (ref)                                                  | 1.01x faster                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250630-linux-x86_64-brandtbucher-jit_up_12_6-3.15.0a0-a33098b |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 311 ms: 1.49x faster                                               |
| async_tree_io              | 838 ms                                                 | 602 ms: 1.39x faster                                               |
| async_tree_memoization     | 437 ms                                                 | 314 ms: 1.39x faster                                               |
| async_tree_io_tg           | 861 ms                                                 | 629 ms: 1.37x faster                                               |
| async_tree_none            | 350 ms                                                 | 261 ms: 1.34x faster                                               |
| async_tree_none_tg         | 319 ms                                                 | 248 ms: 1.29x faster                                               |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 505 ms: 1.13x faster                                               |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 496 ms: 1.09x faster                                               |
| async_generators           | 433 ms                                                 | 428 ms: 1.01x faster                                               |
| asyncio_websockets         | 551 ms                                                 | 555 ms: 1.01x slower                                               |
| coroutines                 | 22.2 ms                                                | 25.0 ms: 1.13x slower                                              |
| Geometric mean             | (ref)                                                  | 1.20x faster                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250630-linux-x86_64-brandtbucher-jit_up_12_6-3.15.0a0-a33098b |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 66.1 ms: 1.19x faster                                              |
| pidigits       | 186 ms                                                 | 193 ms: 1.03x slower                                               |
| nbody          | 87.7 ms                                                | 98.2 ms: 1.12x slower                                              |
| Geometric mean | (ref)                                                  | 1.01x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250630-linux-x86_64-brandtbucher-jit_up_12_6-3.15.0a0-a33098b |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_v8       | 26.9 ms                                                | 22.1 ms: 1.21x faster                                              |
| regex_effbot   | 3.77 ms                                                | 3.31 ms: 1.14x faster                                              |
| regex_dna      | 220 ms                                                 | 206 ms: 1.07x faster                                               |
| regex_compile  | 132 ms                                                 | 127 ms: 1.04x faster                                               |
| Geometric mean | (ref)                                                  | 1.11x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250630-linux-x86_64-brandtbucher-jit_up_12_6-3.15.0a0-a33098b |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.81 sec: 1.17x faster                                             |
| unpickle_pure_python | 213 us                                                 | 191 us: 1.11x faster                                               |
| xml_etree_parse      | 154 ms                                                 | 141 ms: 1.09x faster                                               |
| xml_etree_generate   | 86.8 ms                                                | 80.5 ms: 1.08x faster                                              |
| xml_etree_process    | 60.5 ms                                                | 56.4 ms: 1.07x faster                                              |
| xml_etree_iterparse  | 101 ms                                                 | 98.6 ms: 1.03x faster                                              |
| json_loads           | 27.2 us                                                | 28.0 us: 1.03x slower                                              |
| pickle_pure_python   | 302 us                                                 | 322 us: 1.07x slower                                               |
| json_dumps           | 10.1 ms                                                | 11.1 ms: 1.10x slower                                              |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250630-linux-x86_64-brandtbucher-jit_up_12_6-3.15.0a0-a33098b |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 12.2 ms: 1.04x faster                                              |
| python_startup_no_site | 7.00 ms                                                | 6.93 ms: 1.01x faster                                              |
| Geometric mean         | (ref)                                                  | 1.03x faster                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250630-linux-x86_64-brandtbucher-jit_up_12_6-3.15.0a0-a33098b |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.8 ms: 1.04x faster                                              |
| mako            | 10.7 ms                                                | 10.4 ms: 1.03x faster                                              |
| django_template | 31.7 ms                                                | 32.4 ms: 1.02x slower                                              |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                       |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250630-linux-x86_64-brandtbucher-jit_up_12_6-3.15.0a0-a33098b |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.24 sec: 2.06x faster                                             |
| richards                   | 47.5 ms                                                | 29.5 ms: 1.61x faster                                              |
| richards_super             | 53.7 ms                                                | 33.8 ms: 1.59x faster                                              |
| async_tree_memoization_tg  | 463 ms                                                 | 311 ms: 1.49x faster                                               |
| async_tree_io              | 838 ms                                                 | 602 ms: 1.39x faster                                               |
| async_tree_memoization     | 437 ms                                                 | 314 ms: 1.39x faster                                               |
| async_tree_io_tg           | 861 ms                                                 | 629 ms: 1.37x faster                                               |
| deepcopy                   | 354 us                                                 | 261 us: 1.36x faster                                               |
| async_tree_none            | 350 ms                                                 | 261 ms: 1.34x faster                                               |
| deepcopy_memo              | 38.4 us                                                | 29.6 us: 1.30x faster                                              |
| async_tree_none_tg         | 319 ms                                                 | 248 ms: 1.29x faster                                               |
| spectral_norm              | 113 ms                                                 | 91.7 ms: 1.23x faster                                              |
| go                         | 141 ms                                                 | 114 ms: 1.23x faster                                               |
| regex_v8                   | 26.9 ms                                                | 22.1 ms: 1.21x faster                                              |
| float                      | 78.7 ms                                                | 66.1 ms: 1.19x faster                                              |
| scimark_fft                | 367 ms                                                 | 313 ms: 1.17x faster                                               |
| tomli_loads                | 2.12 sec                                               | 1.81 sec: 1.17x faster                                             |
| deepcopy_reduce            | 3.24 us                                                | 2.81 us: 1.16x faster                                              |
| regex_effbot               | 3.77 ms                                                | 3.31 ms: 1.14x faster                                              |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 505 ms: 1.13x faster                                               |
| pyflate                    | 470 ms                                                 | 415 ms: 1.13x faster                                               |
| unpickle_pure_python       | 213 us                                                 | 191 us: 1.11x faster                                               |
| pylint                     | 312 ms                                                 | 283 ms: 1.10x faster                                               |
| telco                      | 8.40 ms                                                | 7.67 ms: 1.09x faster                                              |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 496 ms: 1.09x faster                                               |
| xml_etree_parse            | 154 ms                                                 | 141 ms: 1.09x faster                                               |
| dulwich_log                | 64.6 ms                                                | 59.6 ms: 1.08x faster                                              |
| xml_etree_generate         | 86.8 ms                                                | 80.5 ms: 1.08x faster                                              |
| bpe_tokeniser              | 4.69 sec                                               | 4.36 sec: 1.08x faster                                             |
| pycparser                  | 1.20 sec                                               | 1.12 sec: 1.07x faster                                             |
| xml_etree_process          | 60.5 ms                                                | 56.4 ms: 1.07x faster                                              |
| regex_dna                  | 220 ms                                                 | 206 ms: 1.07x faster                                               |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.77 ms: 1.06x faster                                              |
| deltablue                  | 3.19 ms                                                | 3.06 ms: 1.04x faster                                              |
| regex_compile              | 132 ms                                                 | 127 ms: 1.04x faster                                               |
| python_startup             | 12.7 ms                                                | 12.2 ms: 1.04x faster                                              |
| k_core                     | 2.37 sec                                               | 2.28 sec: 1.04x faster                                             |
| sqlite_synth               | 2.90 us                                                | 2.79 us: 1.04x faster                                              |
| genshi_text                | 22.6 ms                                                | 21.8 ms: 1.04x faster                                              |
| mako                       | 10.7 ms                                                | 10.4 ms: 1.03x faster                                              |
| gc_traversal               | 4.90 ms                                                | 4.75 ms: 1.03x faster                                              |
| 2to3                       | 266 ms                                                 | 258 ms: 1.03x faster                                               |
| thrift                     | 800 us                                                 | 778 us: 1.03x faster                                               |
| xml_etree_iterparse        | 101 ms                                                 | 98.6 ms: 1.03x faster                                              |
| scimark_sor                | 122 ms                                                 | 119 ms: 1.02x faster                                               |
| sympy_integrate            | 19.8 ms                                                | 19.4 ms: 1.02x faster                                              |
| pprint_safe_repr           | 727 ms                                                 | 712 ms: 1.02x faster                                               |
| pathlib                    | 17.4 ms                                                | 17.0 ms: 1.02x faster                                              |
| pprint_pformat             | 1.48 sec                                               | 1.45 sec: 1.02x faster                                             |
| json                       | 5.32 ms                                                | 5.24 ms: 1.02x faster                                              |
| meteor_contest             | 108 ms                                                 | 107 ms: 1.02x faster                                               |
| sphinx                     | 1.03 sec                                               | 1.02 sec: 1.02x faster                                             |
| scimark_monte_carlo        | 66.8 ms                                                | 66.0 ms: 1.01x faster                                              |
| async_generators           | 433 ms                                                 | 428 ms: 1.01x faster                                               |
| python_startup_no_site     | 7.00 ms                                                | 6.93 ms: 1.01x faster                                              |
| html5lib                   | 63.4 ms                                                | 62.7 ms: 1.01x faster                                              |
| comprehensions             | 16.5 us                                                | 16.3 us: 1.01x faster                                              |
| logging_simple             | 5.65 us                                                | 5.62 us: 1.01x faster                                              |
| sympy_sum                  | 150 ms                                                 | 150 ms: 1.01x faster                                               |
| asyncio_websockets         | 551 ms                                                 | 555 ms: 1.01x slower                                               |
| crypto_pyaes               | 74.7 ms                                                | 75.3 ms: 1.01x slower                                              |
| hexiom                     | 6.08 ms                                                | 6.13 ms: 1.01x slower                                              |
| logging_silent             | 101 ns                                                 | 102 ns: 1.01x slower                                               |
| shortest_path              | 487 ms                                                 | 493 ms: 1.01x slower                                               |
| connected_components       | 447 ms                                                 | 454 ms: 1.02x slower                                               |
| nqueens                    | 80.9 ms                                                | 82.4 ms: 1.02x slower                                              |
| docutils                   | 2.58 sec                                               | 2.64 sec: 1.02x slower                                             |
| sympy_expand               | 456 ms                                                 | 466 ms: 1.02x slower                                               |
| fannkuch                   | 394 ms                                                 | 403 ms: 1.02x slower                                               |
| django_template            | 31.7 ms                                                | 32.4 ms: 1.02x slower                                              |
| json_loads                 | 27.2 us                                                | 28.0 us: 1.03x slower                                              |
| pidigits                   | 186 ms                                                 | 193 ms: 1.03x slower                                               |
| raytrace                   | 262 ms                                                 | 271 ms: 1.04x slower                                               |
| scimark_lu                 | 114 ms                                                 | 119 ms: 1.04x slower                                               |
| generators                 | 28.8 ms                                                | 30.0 ms: 1.04x slower                                              |
| create_gc_cycles           | 2.45 ms                                                | 2.57 ms: 1.05x slower                                              |
| coverage                   | 82.8 ms                                                | 87.1 ms: 1.05x slower                                              |
| chaos                      | 58.0 ms                                                | 61.5 ms: 1.06x slower                                              |
| typing_runtime_protocols   | 160 us                                                 | 170 us: 1.06x slower                                               |
| pickle_pure_python         | 302 us                                                 | 322 us: 1.07x slower                                               |
| json_dumps                 | 10.1 ms                                                | 11.1 ms: 1.10x slower                                              |
| nbody                      | 87.7 ms                                                | 98.2 ms: 1.12x slower                                              |
| coroutines                 | 22.2 ms                                                | 25.0 ms: 1.13x slower                                              |
| many_optionals             | 857 us                                                 | 983 us: 1.15x slower                                               |
| subparsers                 | 15.5 ms                                                | 23.8 ms: 1.54x slower                                              |
| Geometric mean             | (ref)                                                  | 1.07x faster                                                       |

Benchmark hidden because not significant (4): sympy_str, genshi_xml, logging_format, djangocms
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250630-3.15.0a0-a33098b-JIT/bm-20250630-linux-x86_64-brandtbucher-jit_up_12_6-3.15.0a0-a33098b.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.068x faster

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.07x