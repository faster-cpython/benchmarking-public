# Results vs. 3.13.0

- fork: brandtbucher
- ref: jit_up_12_8
- machine: linux-x86_64
- commit hash: 23be3e4
- commit date: 2025-06-30
- overall geometric mean: 1.061x faster
- HPT reliability: 99.96%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250630-linux-x86_64-brandtbucher-jit_up_12_8-3.15.0a0-23be3e4 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 261 ms: 1.02x faster                                               |
| docutils       | 2.58 sec                                               | 2.66 sec: 1.03x slower                                             |
| html5lib       | 63.4 ms                                                | 62.3 ms: 1.02x faster                                              |
| Geometric mean | (ref)                                                  | 1.00x faster                                                       |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250630-linux-x86_64-brandtbucher-jit_up_12_8-3.15.0a0-23be3e4 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 318 ms: 1.45x faster                                               |
| async_tree_memoization     | 437 ms                                                 | 315 ms: 1.39x faster                                               |
| async_tree_io              | 838 ms                                                 | 606 ms: 1.38x faster                                               |
| async_tree_io_tg           | 861 ms                                                 | 629 ms: 1.37x faster                                               |
| async_tree_none            | 350 ms                                                 | 262 ms: 1.34x faster                                               |
| async_tree_none_tg         | 319 ms                                                 | 252 ms: 1.27x faster                                               |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 501 ms: 1.14x faster                                               |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 495 ms: 1.10x faster                                               |
| asyncio_websockets         | 551 ms                                                 | 555 ms: 1.01x slower                                               |
| async_generators           | 433 ms                                                 | 437 ms: 1.01x slower                                               |
| coroutines                 | 22.2 ms                                                | 24.9 ms: 1.12x slower                                              |
| Geometric mean             | (ref)                                                  | 1.20x faster                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250630-linux-x86_64-brandtbucher-jit_up_12_8-3.15.0a0-23be3e4 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 66.2 ms: 1.19x faster                                              |
| pidigits       | 186 ms                                                 | 189 ms: 1.01x slower                                               |
| nbody          | 87.7 ms                                                | 101 ms: 1.15x slower                                               |
| Geometric mean | (ref)                                                  | 1.01x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250630-linux-x86_64-brandtbucher-jit_up_12_8-3.15.0a0-23be3e4 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_v8       | 26.9 ms                                                | 23.0 ms: 1.17x faster                                              |
| regex_effbot   | 3.77 ms                                                | 3.45 ms: 1.09x faster                                              |
| regex_dna      | 220 ms                                                 | 208 ms: 1.06x faster                                               |
| regex_compile  | 132 ms                                                 | 127 ms: 1.04x faster                                               |
| Geometric mean | (ref)                                                  | 1.09x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250630-linux-x86_64-brandtbucher-jit_up_12_8-3.15.0a0-23be3e4 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.83 sec: 1.16x faster                                             |
| unpickle_pure_python | 213 us                                                 | 190 us: 1.12x faster                                               |
| xml_etree_parse      | 154 ms                                                 | 140 ms: 1.10x faster                                               |
| xml_etree_generate   | 86.8 ms                                                | 80.0 ms: 1.09x faster                                              |
| xml_etree_process    | 60.5 ms                                                | 55.7 ms: 1.09x faster                                              |
| xml_etree_iterparse  | 101 ms                                                 | 98.4 ms: 1.03x faster                                              |
| json_loads           | 27.2 us                                                | 28.7 us: 1.06x slower                                              |
| pickle_pure_python   | 302 us                                                 | 322 us: 1.06x slower                                               |
| json_dumps           | 10.1 ms                                                | 11.2 ms: 1.11x slower                                              |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250630-linux-x86_64-brandtbucher-jit_up_12_8-3.15.0a0-23be3e4 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 12.2 ms: 1.04x faster                                              |
| python_startup_no_site | 7.00 ms                                                | 6.96 ms: 1.01x faster                                              |
| Geometric mean         | (ref)                                                  | 1.02x faster                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250630-linux-x86_64-brandtbucher-jit_up_12_8-3.15.0a0-23be3e4 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 22.0 ms: 1.03x faster                                              |
| mako            | 10.7 ms                                                | 10.4 ms: 1.02x faster                                              |
| genshi_xml      | 50.5 ms                                                | 50.8 ms: 1.01x slower                                              |
| django_template | 31.7 ms                                                | 32.6 ms: 1.03x slower                                              |
| Geometric mean  | (ref)                                                  | 1.00x faster                                                       |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250630-linux-x86_64-brandtbucher-jit_up_12_8-3.15.0a0-23be3e4 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.23 sec: 2.07x faster                                             |
| async_tree_memoization_tg  | 463 ms                                                 | 318 ms: 1.45x faster                                               |
| richards_super             | 53.7 ms                                                | 38.0 ms: 1.42x faster                                              |
| richards                   | 47.5 ms                                                | 33.7 ms: 1.41x faster                                              |
| async_tree_memoization     | 437 ms                                                 | 315 ms: 1.39x faster                                               |
| async_tree_io              | 838 ms                                                 | 606 ms: 1.38x faster                                               |
| async_tree_io_tg           | 861 ms                                                 | 629 ms: 1.37x faster                                               |
| deepcopy                   | 354 us                                                 | 261 us: 1.36x faster                                               |
| async_tree_none            | 350 ms                                                 | 262 ms: 1.34x faster                                               |
| deepcopy_memo              | 38.4 us                                                | 29.7 us: 1.29x faster                                              |
| async_tree_none_tg         | 319 ms                                                 | 252 ms: 1.27x faster                                               |
| spectral_norm              | 113 ms                                                 | 91.0 ms: 1.24x faster                                              |
| go                         | 141 ms                                                 | 115 ms: 1.23x faster                                               |
| deepcopy_reduce            | 3.24 us                                                | 2.70 us: 1.20x faster                                              |
| float                      | 78.7 ms                                                | 66.2 ms: 1.19x faster                                              |
| scimark_fft                | 367 ms                                                 | 311 ms: 1.18x faster                                               |
| regex_v8                   | 26.9 ms                                                | 23.0 ms: 1.17x faster                                              |
| tomli_loads                | 2.12 sec                                               | 1.83 sec: 1.16x faster                                             |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 501 ms: 1.14x faster                                               |
| pyflate                    | 470 ms                                                 | 413 ms: 1.14x faster                                               |
| unpickle_pure_python       | 213 us                                                 | 190 us: 1.12x faster                                               |
| xml_etree_parse            | 154 ms                                                 | 140 ms: 1.10x faster                                               |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 495 ms: 1.10x faster                                               |
| pylint                     | 312 ms                                                 | 284 ms: 1.10x faster                                               |
| telco                      | 8.40 ms                                                | 7.68 ms: 1.09x faster                                              |
| regex_effbot               | 3.77 ms                                                | 3.45 ms: 1.09x faster                                              |
| xml_etree_generate         | 86.8 ms                                                | 80.0 ms: 1.09x faster                                              |
| xml_etree_process          | 60.5 ms                                                | 55.7 ms: 1.09x faster                                              |
| dulwich_log                | 64.6 ms                                                | 59.7 ms: 1.08x faster                                              |
| pycparser                  | 1.20 sec                                               | 1.11 sec: 1.08x faster                                             |
| bpe_tokeniser              | 4.69 sec                                               | 4.38 sec: 1.07x faster                                             |
| regex_dna                  | 220 ms                                                 | 208 ms: 1.06x faster                                               |
| deltablue                  | 3.19 ms                                                | 3.03 ms: 1.05x faster                                              |
| sqlite_synth               | 2.90 us                                                | 2.78 us: 1.04x faster                                              |
| pprint_safe_repr           | 727 ms                                                 | 697 ms: 1.04x faster                                               |
| regex_compile              | 132 ms                                                 | 127 ms: 1.04x faster                                               |
| k_core                     | 2.37 sec                                               | 2.28 sec: 1.04x faster                                             |
| python_startup             | 12.7 ms                                                | 12.2 ms: 1.04x faster                                              |
| scimark_sor                | 122 ms                                                 | 118 ms: 1.03x faster                                               |
| xml_etree_iterparse        | 101 ms                                                 | 98.4 ms: 1.03x faster                                              |
| genshi_text                | 22.6 ms                                                | 22.0 ms: 1.03x faster                                              |
| pathlib                    | 17.4 ms                                                | 16.9 ms: 1.03x faster                                              |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.90 ms: 1.03x faster                                              |
| scimark_monte_carlo        | 66.8 ms                                                | 65.2 ms: 1.03x faster                                              |
| mako                       | 10.7 ms                                                | 10.4 ms: 1.02x faster                                              |
| meteor_contest             | 108 ms                                                 | 106 ms: 1.02x faster                                               |
| 2to3                       | 266 ms                                                 | 261 ms: 1.02x faster                                               |
| pprint_pformat             | 1.48 sec                                               | 1.45 sec: 1.02x faster                                             |
| thrift                     | 800 us                                                 | 784 us: 1.02x faster                                               |
| html5lib                   | 63.4 ms                                                | 62.3 ms: 1.02x faster                                              |
| sympy_integrate            | 19.8 ms                                                | 19.5 ms: 1.02x faster                                              |
| comprehensions             | 16.5 us                                                | 16.3 us: 1.01x faster                                              |
| python_startup_no_site     | 7.00 ms                                                | 6.96 ms: 1.01x faster                                              |
| genshi_xml                 | 50.5 ms                                                | 50.8 ms: 1.01x slower                                              |
| asyncio_websockets         | 551 ms                                                 | 555 ms: 1.01x slower                                               |
| fannkuch                   | 394 ms                                                 | 396 ms: 1.01x slower                                               |
| shortest_path              | 487 ms                                                 | 491 ms: 1.01x slower                                               |
| async_generators           | 433 ms                                                 | 437 ms: 1.01x slower                                               |
| logging_simple             | 5.65 us                                                | 5.70 us: 1.01x slower                                              |
| gc_traversal               | 4.90 ms                                                | 4.95 ms: 1.01x slower                                              |
| crypto_pyaes               | 74.7 ms                                                | 75.6 ms: 1.01x slower                                              |
| pidigits                   | 186 ms                                                 | 189 ms: 1.01x slower                                               |
| logging_format             | 6.23 us                                                | 6.32 us: 1.01x slower                                              |
| connected_components       | 447 ms                                                 | 455 ms: 1.02x slower                                               |
| sympy_expand               | 456 ms                                                 | 468 ms: 1.03x slower                                               |
| hexiom                     | 6.08 ms                                                | 6.24 ms: 1.03x slower                                              |
| nqueens                    | 80.9 ms                                                | 83.0 ms: 1.03x slower                                              |
| docutils                   | 2.58 sec                                               | 2.66 sec: 1.03x slower                                             |
| raytrace                   | 262 ms                                                 | 269 ms: 1.03x slower                                               |
| django_template            | 31.7 ms                                                | 32.6 ms: 1.03x slower                                              |
| logging_silent             | 101 ns                                                 | 105 ns: 1.04x slower                                               |
| typing_runtime_protocols   | 160 us                                                 | 168 us: 1.05x slower                                               |
| chaos                      | 58.0 ms                                                | 61.2 ms: 1.06x slower                                              |
| scimark_lu                 | 114 ms                                                 | 121 ms: 1.06x slower                                               |
| json_loads                 | 27.2 us                                                | 28.7 us: 1.06x slower                                              |
| coverage                   | 82.8 ms                                                | 87.8 ms: 1.06x slower                                              |
| create_gc_cycles           | 2.45 ms                                                | 2.60 ms: 1.06x slower                                              |
| pickle_pure_python         | 302 us                                                 | 322 us: 1.06x slower                                               |
| generators                 | 28.8 ms                                                | 31.4 ms: 1.09x slower                                              |
| json_dumps                 | 10.1 ms                                                | 11.2 ms: 1.11x slower                                              |
| coroutines                 | 22.2 ms                                                | 24.9 ms: 1.12x slower                                              |
| many_optionals             | 857 us                                                 | 981 us: 1.15x slower                                               |
| nbody                      | 87.7 ms                                                | 101 ms: 1.15x slower                                               |
| subparsers                 | 15.5 ms                                                | 23.8 ms: 1.54x slower                                              |
| Geometric mean             | (ref)                                                  | 1.06x faster                                                       |

Benchmark hidden because not significant (5): sphinx, json, sympy_sum, sympy_str, djangocms
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250630-3.15.0a0-23be3e4-JIT/bm-20250630-linux-x86_64-brandtbucher-jit_up_12_8-3.15.0a0-23be3e4.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.061x faster

# HPT report

- Reliability score: 99.96% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.07x