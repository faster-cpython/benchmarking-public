# Results vs. 3.13.0

- fork: brandtbucher
- ref: jit_up_7_12
- machine: linux-x86_64
- commit hash: 459e94c
- commit date: 2025-07-01
- overall geometric mean: 1.063x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250701-linux-x86_64-brandtbucher-jit_up_7_12-3.15.0a0-459e94c |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 262 ms: 1.01x faster                                               |
| docutils       | 2.58 sec                                               | 2.66 sec: 1.03x slower                                             |
| html5lib       | 63.4 ms                                                | 61.7 ms: 1.03x faster                                              |
| Geometric mean | (ref)                                                  | 1.01x faster                                                       |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250701-linux-x86_64-brandtbucher-jit_up_7_12-3.15.0a0-459e94c |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 317 ms: 1.46x faster                                               |
| async_tree_io              | 838 ms                                                 | 606 ms: 1.38x faster                                               |
| async_tree_memoization     | 437 ms                                                 | 316 ms: 1.38x faster                                               |
| async_tree_io_tg           | 861 ms                                                 | 639 ms: 1.35x faster                                               |
| async_tree_none            | 350 ms                                                 | 268 ms: 1.31x faster                                               |
| async_tree_none_tg         | 319 ms                                                 | 253 ms: 1.26x faster                                               |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 507 ms: 1.13x faster                                               |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 500 ms: 1.09x faster                                               |
| async_generators           | 433 ms                                                 | 431 ms: 1.01x faster                                               |
| asyncio_websockets         | 551 ms                                                 | 554 ms: 1.00x slower                                               |
| coroutines                 | 22.2 ms                                                | 25.6 ms: 1.15x slower                                              |
| Geometric mean             | (ref)                                                  | 1.19x faster                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250701-linux-x86_64-brandtbucher-jit_up_7_12-3.15.0a0-459e94c |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 66.0 ms: 1.19x faster                                              |
| pidigits       | 186 ms                                                 | 193 ms: 1.03x slower                                               |
| nbody          | 87.7 ms                                                | 92.3 ms: 1.05x slower                                              |
| Geometric mean | (ref)                                                  | 1.03x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250701-linux-x86_64-brandtbucher-jit_up_7_12-3.15.0a0-459e94c |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_v8       | 26.9 ms                                                | 24.0 ms: 1.12x faster                                              |
| regex_effbot   | 3.77 ms                                                | 3.41 ms: 1.10x faster                                              |
| regex_compile  | 132 ms                                                 | 127 ms: 1.04x faster                                               |
| regex_dna      | 220 ms                                                 | 216 ms: 1.02x faster                                               |
| Geometric mean | (ref)                                                  | 1.07x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250701-linux-x86_64-brandtbucher-jit_up_7_12-3.15.0a0-459e94c |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.82 sec: 1.16x faster                                             |
| unpickle_pure_python | 213 us                                                 | 193 us: 1.11x faster                                               |
| xml_etree_parse      | 154 ms                                                 | 140 ms: 1.10x faster                                               |
| xml_etree_generate   | 86.8 ms                                                | 79.6 ms: 1.09x faster                                              |
| xml_etree_process    | 60.5 ms                                                | 55.6 ms: 1.09x faster                                              |
| xml_etree_iterparse  | 101 ms                                                 | 98.3 ms: 1.03x faster                                              |
| json_loads           | 27.2 us                                                | 28.2 us: 1.04x slower                                              |
| pickle_pure_python   | 302 us                                                 | 321 us: 1.06x slower                                               |
| json_dumps           | 10.1 ms                                                | 11.1 ms: 1.10x slower                                              |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250701-linux-x86_64-brandtbucher-jit_up_7_12-3.15.0a0-459e94c |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 12.2 ms: 1.04x faster                                              |
| python_startup_no_site | 7.00 ms                                                | 6.96 ms: 1.01x faster                                              |
| Geometric mean         | (ref)                                                  | 1.02x faster                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250701-linux-x86_64-brandtbucher-jit_up_7_12-3.15.0a0-459e94c |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.6 ms: 1.05x faster                                              |
| mako            | 10.7 ms                                                | 10.5 ms: 1.02x faster                                              |
| django_template | 31.7 ms                                                | 33.2 ms: 1.05x slower                                              |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                       |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250701-linux-x86_64-brandtbucher-jit_up_7_12-3.15.0a0-459e94c |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.23 sec: 2.07x faster                                             |
| richards                   | 47.5 ms                                                | 31.0 ms: 1.54x faster                                              |
| richards_super             | 53.7 ms                                                | 35.9 ms: 1.50x faster                                              |
| async_tree_memoization_tg  | 463 ms                                                 | 317 ms: 1.46x faster                                               |
| async_tree_io              | 838 ms                                                 | 606 ms: 1.38x faster                                               |
| async_tree_memoization     | 437 ms                                                 | 316 ms: 1.38x faster                                               |
| deepcopy                   | 354 us                                                 | 258 us: 1.37x faster                                               |
| async_tree_io_tg           | 861 ms                                                 | 639 ms: 1.35x faster                                               |
| async_tree_none            | 350 ms                                                 | 268 ms: 1.31x faster                                               |
| deepcopy_memo              | 38.4 us                                                | 29.8 us: 1.29x faster                                              |
| async_tree_none_tg         | 319 ms                                                 | 253 ms: 1.26x faster                                               |
| spectral_norm              | 113 ms                                                 | 91.5 ms: 1.24x faster                                              |
| go                         | 141 ms                                                 | 116 ms: 1.21x faster                                               |
| float                      | 78.7 ms                                                | 66.0 ms: 1.19x faster                                              |
| scimark_fft                | 367 ms                                                 | 311 ms: 1.18x faster                                               |
| deepcopy_reduce            | 3.24 us                                                | 2.79 us: 1.16x faster                                              |
| pyflate                    | 470 ms                                                 | 404 ms: 1.16x faster                                               |
| tomli_loads                | 2.12 sec                                               | 1.82 sec: 1.16x faster                                             |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 507 ms: 1.13x faster                                               |
| regex_v8                   | 26.9 ms                                                | 24.0 ms: 1.12x faster                                              |
| unpickle_pure_python       | 213 us                                                 | 193 us: 1.11x faster                                               |
| regex_effbot               | 3.77 ms                                                | 3.41 ms: 1.10x faster                                              |
| xml_etree_parse            | 154 ms                                                 | 140 ms: 1.10x faster                                               |
| xml_etree_generate         | 86.8 ms                                                | 79.6 ms: 1.09x faster                                              |
| pylint                     | 312 ms                                                 | 287 ms: 1.09x faster                                               |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 500 ms: 1.09x faster                                               |
| telco                      | 8.40 ms                                                | 7.73 ms: 1.09x faster                                              |
| xml_etree_process          | 60.5 ms                                                | 55.6 ms: 1.09x faster                                              |
| dulwich_log                | 64.6 ms                                                | 59.6 ms: 1.08x faster                                              |
| bpe_tokeniser              | 4.69 sec                                               | 4.34 sec: 1.08x faster                                             |
| deltablue                  | 3.19 ms                                                | 3.03 ms: 1.05x faster                                              |
| genshi_text                | 22.6 ms                                                | 21.6 ms: 1.05x faster                                              |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.80 ms: 1.05x faster                                              |
| pycparser                  | 1.20 sec                                               | 1.15 sec: 1.04x faster                                             |
| sqlite_synth               | 2.90 us                                                | 2.79 us: 1.04x faster                                              |
| regex_compile              | 132 ms                                                 | 127 ms: 1.04x faster                                               |
| k_core                     | 2.37 sec                                               | 2.28 sec: 1.04x faster                                             |
| meteor_contest             | 108 ms                                                 | 105 ms: 1.04x faster                                               |
| python_startup             | 12.7 ms                                                | 12.2 ms: 1.04x faster                                              |
| thrift                     | 800 us                                                 | 773 us: 1.03x faster                                               |
| scimark_sor                | 122 ms                                                 | 118 ms: 1.03x faster                                               |
| xml_etree_iterparse        | 101 ms                                                 | 98.3 ms: 1.03x faster                                              |
| html5lib                   | 63.4 ms                                                | 61.7 ms: 1.03x faster                                              |
| scimark_monte_carlo        | 66.8 ms                                                | 65.3 ms: 1.02x faster                                              |
| json                       | 5.32 ms                                                | 5.22 ms: 1.02x faster                                              |
| regex_dna                  | 220 ms                                                 | 216 ms: 1.02x faster                                               |
| pprint_pformat             | 1.48 sec                                               | 1.45 sec: 1.02x faster                                             |
| mako                       | 10.7 ms                                                | 10.5 ms: 1.02x faster                                              |
| 2to3                       | 266 ms                                                 | 262 ms: 1.01x faster                                               |
| crypto_pyaes               | 74.7 ms                                                | 73.7 ms: 1.01x faster                                              |
| sympy_integrate            | 19.8 ms                                                | 19.6 ms: 1.01x faster                                              |
| logging_format             | 6.23 us                                                | 6.17 us: 1.01x faster                                              |
| logging_simple             | 5.65 us                                                | 5.60 us: 1.01x faster                                              |
| async_generators           | 433 ms                                                 | 431 ms: 1.01x faster                                               |
| python_startup_no_site     | 7.00 ms                                                | 6.96 ms: 1.01x faster                                              |
| fannkuch                   | 394 ms                                                 | 392 ms: 1.00x faster                                               |
| asyncio_websockets         | 551 ms                                                 | 554 ms: 1.00x slower                                               |
| gc_traversal               | 4.90 ms                                                | 4.92 ms: 1.00x slower                                              |
| hexiom                     | 6.08 ms                                                | 6.13 ms: 1.01x slower                                              |
| sympy_sum                  | 150 ms                                                 | 152 ms: 1.01x slower                                               |
| shortest_path              | 487 ms                                                 | 492 ms: 1.01x slower                                               |
| sympy_expand               | 456 ms                                                 | 465 ms: 1.02x slower                                               |
| nqueens                    | 80.9 ms                                                | 82.5 ms: 1.02x slower                                              |
| connected_components       | 447 ms                                                 | 458 ms: 1.02x slower                                               |
| djangocms                  | 22.3 us                                                | 22.9 us: 1.03x slower                                              |
| logging_silent             | 101 ns                                                 | 104 ns: 1.03x slower                                               |
| docutils                   | 2.58 sec                                               | 2.66 sec: 1.03x slower                                             |
| pidigits                   | 186 ms                                                 | 193 ms: 1.03x slower                                               |
| scimark_lu                 | 114 ms                                                 | 119 ms: 1.04x slower                                               |
| json_loads                 | 27.2 us                                                | 28.2 us: 1.04x slower                                              |
| generators                 | 28.8 ms                                                | 30.0 ms: 1.04x slower                                              |
| raytrace                   | 262 ms                                                 | 273 ms: 1.04x slower                                               |
| django_template            | 31.7 ms                                                | 33.2 ms: 1.05x slower                                              |
| nbody                      | 87.7 ms                                                | 92.3 ms: 1.05x slower                                              |
| typing_runtime_protocols   | 160 us                                                 | 169 us: 1.05x slower                                               |
| chaos                      | 58.0 ms                                                | 61.5 ms: 1.06x slower                                              |
| pickle_pure_python         | 302 us                                                 | 321 us: 1.06x slower                                               |
| coverage                   | 82.8 ms                                                | 88.0 ms: 1.06x slower                                              |
| create_gc_cycles           | 2.45 ms                                                | 2.61 ms: 1.06x slower                                              |
| json_dumps                 | 10.1 ms                                                | 11.1 ms: 1.10x slower                                              |
| coroutines                 | 22.2 ms                                                | 25.6 ms: 1.15x slower                                              |
| many_optionals             | 857 us                                                 | 988 us: 1.15x slower                                               |
| subparsers                 | 15.5 ms                                                | 23.8 ms: 1.54x slower                                              |
| Geometric mean             | (ref)                                                  | 1.06x faster                                                       |

Benchmark hidden because not significant (6): sphinx, genshi_xml, pathlib, sympy_str, comprehensions, pprint_safe_repr
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250701-3.15.0a0-459e94c-JIT/bm-20250701-linux-x86_64-brandtbucher-jit_up_7_12-3.15.0a0-459e94c.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.063x faster

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.09x