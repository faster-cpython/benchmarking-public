# Results vs. 3.13.0

- fork: brandtbucher
- ref: jit_up_12_9
- machine: linux-x86_64
- commit hash: ad5f858
- commit date: 2025-06-29
- overall geometric mean: 1.063x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250629-linux-x86_64-brandtbucher-jit_up_12_9-3.15.0a0-ad5f858 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 260 ms: 1.02x faster                                               |
| docutils       | 2.58 sec                                               | 2.65 sec: 1.03x slower                                             |
| html5lib       | 63.4 ms                                                | 62.1 ms: 1.02x faster                                              |
| sphinx         | 1.03 sec                                               | 1.02 sec: 1.02x faster                                             |
| Geometric mean | (ref)                                                  | 1.01x faster                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250629-linux-x86_64-brandtbucher-jit_up_12_9-3.15.0a0-ad5f858 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 315 ms: 1.47x faster                                               |
| async_tree_io_tg           | 861 ms                                                 | 612 ms: 1.41x faster                                               |
| async_tree_io              | 838 ms                                                 | 600 ms: 1.40x faster                                               |
| async_tree_memoization     | 437 ms                                                 | 317 ms: 1.38x faster                                               |
| async_tree_none            | 350 ms                                                 | 261 ms: 1.34x faster                                               |
| async_tree_none_tg         | 319 ms                                                 | 251 ms: 1.27x faster                                               |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 494 ms: 1.16x faster                                               |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 487 ms: 1.12x faster                                               |
| async_generators           | 433 ms                                                 | 426 ms: 1.02x faster                                               |
| asyncio_websockets         | 551 ms                                                 | 554 ms: 1.00x slower                                               |
| coroutines                 | 22.2 ms                                                | 25.0 ms: 1.12x slower                                              |
| Geometric mean             | (ref)                                                  | 1.21x faster                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250629-linux-x86_64-brandtbucher-jit_up_12_9-3.15.0a0-ad5f858 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 66.3 ms: 1.19x faster                                              |
| pidigits       | 186 ms                                                 | 189 ms: 1.01x slower                                               |
| nbody          | 87.7 ms                                                | 96.3 ms: 1.10x slower                                              |
| Geometric mean | (ref)                                                  | 1.02x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250629-linux-x86_64-brandtbucher-jit_up_12_9-3.15.0a0-ad5f858 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_v8       | 26.9 ms                                                | 23.9 ms: 1.13x faster                                              |
| regex_effbot   | 3.77 ms                                                | 3.42 ms: 1.10x faster                                              |
| regex_compile  | 132 ms                                                 | 127 ms: 1.04x faster                                               |
| regex_dna      | 220 ms                                                 | 216 ms: 1.02x faster                                               |
| Geometric mean | (ref)                                                  | 1.07x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250629-linux-x86_64-brandtbucher-jit_up_12_9-3.15.0a0-ad5f858 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.85 sec: 1.14x faster                                             |
| unpickle_pure_python | 213 us                                                 | 190 us: 1.12x faster                                               |
| xml_etree_parse      | 154 ms                                                 | 141 ms: 1.10x faster                                               |
| xml_etree_process    | 60.5 ms                                                | 55.4 ms: 1.09x faster                                              |
| xml_etree_generate   | 86.8 ms                                                | 80.0 ms: 1.09x faster                                              |
| xml_etree_iterparse  | 101 ms                                                 | 98.8 ms: 1.02x faster                                              |
| json_loads           | 27.2 us                                                | 28.1 us: 1.03x slower                                              |
| pickle_pure_python   | 302 us                                                 | 320 us: 1.06x slower                                               |
| json_dumps           | 10.1 ms                                                | 11.0 ms: 1.09x slower                                              |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250629-linux-x86_64-brandtbucher-jit_up_12_9-3.15.0a0-ad5f858 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 12.1 ms: 1.04x faster                                              |
| python_startup_no_site | 7.00 ms                                                | 6.90 ms: 1.01x faster                                              |
| Geometric mean         | (ref)                                                  | 1.03x faster                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250629-linux-x86_64-brandtbucher-jit_up_12_9-3.15.0a0-ad5f858 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.9 ms: 1.03x faster                                              |
| mako            | 10.7 ms                                                | 10.5 ms: 1.01x faster                                              |
| django_template | 31.7 ms                                                | 32.5 ms: 1.03x slower                                              |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                       |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250629-linux-x86_64-brandtbucher-jit_up_12_9-3.15.0a0-ad5f858 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.23 sec: 2.07x faster                                             |
| richards                   | 47.5 ms                                                | 31.9 ms: 1.49x faster                                              |
| richards_super             | 53.7 ms                                                | 36.3 ms: 1.48x faster                                              |
| async_tree_memoization_tg  | 463 ms                                                 | 315 ms: 1.47x faster                                               |
| async_tree_io_tg           | 861 ms                                                 | 612 ms: 1.41x faster                                               |
| async_tree_io              | 838 ms                                                 | 600 ms: 1.40x faster                                               |
| async_tree_memoization     | 437 ms                                                 | 317 ms: 1.38x faster                                               |
| deepcopy                   | 354 us                                                 | 259 us: 1.37x faster                                               |
| async_tree_none            | 350 ms                                                 | 261 ms: 1.34x faster                                               |
| deepcopy_memo              | 38.4 us                                                | 29.9 us: 1.28x faster                                              |
| async_tree_none_tg         | 319 ms                                                 | 251 ms: 1.27x faster                                               |
| go                         | 141 ms                                                 | 114 ms: 1.23x faster                                               |
| spectral_norm              | 113 ms                                                 | 93.1 ms: 1.22x faster                                              |
| deepcopy_reduce            | 3.24 us                                                | 2.70 us: 1.20x faster                                              |
| float                      | 78.7 ms                                                | 66.3 ms: 1.19x faster                                              |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 494 ms: 1.16x faster                                               |
| scimark_fft                | 367 ms                                                 | 319 ms: 1.15x faster                                               |
| tomli_loads                | 2.12 sec                                               | 1.85 sec: 1.14x faster                                             |
| regex_v8                   | 26.9 ms                                                | 23.9 ms: 1.13x faster                                              |
| unpickle_pure_python       | 213 us                                                 | 190 us: 1.12x faster                                               |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 487 ms: 1.12x faster                                               |
| pyflate                    | 470 ms                                                 | 421 ms: 1.12x faster                                               |
| pylint                     | 312 ms                                                 | 282 ms: 1.11x faster                                               |
| regex_effbot               | 3.77 ms                                                | 3.42 ms: 1.10x faster                                              |
| xml_etree_parse            | 154 ms                                                 | 141 ms: 1.10x faster                                               |
| xml_etree_process          | 60.5 ms                                                | 55.4 ms: 1.09x faster                                              |
| dulwich_log                | 64.6 ms                                                | 59.4 ms: 1.09x faster                                              |
| xml_etree_generate         | 86.8 ms                                                | 80.0 ms: 1.09x faster                                              |
| telco                      | 8.40 ms                                                | 7.78 ms: 1.08x faster                                              |
| bpe_tokeniser              | 4.69 sec                                               | 4.38 sec: 1.07x faster                                             |
| deltablue                  | 3.19 ms                                                | 3.03 ms: 1.05x faster                                              |
| python_startup             | 12.7 ms                                                | 12.1 ms: 1.04x faster                                              |
| sqlite_synth               | 2.90 us                                                | 2.78 us: 1.04x faster                                              |
| pycparser                  | 1.20 sec                                               | 1.15 sec: 1.04x faster                                             |
| regex_compile              | 132 ms                                                 | 127 ms: 1.04x faster                                               |
| scimark_sor                | 122 ms                                                 | 117 ms: 1.04x faster                                               |
| k_core                     | 2.37 sec                                               | 2.29 sec: 1.04x faster                                             |
| genshi_text                | 22.6 ms                                                | 21.9 ms: 1.03x faster                                              |
| pprint_pformat             | 1.48 sec                                               | 1.44 sec: 1.03x faster                                             |
| pprint_safe_repr           | 727 ms                                                 | 708 ms: 1.03x faster                                               |
| xml_etree_iterparse        | 101 ms                                                 | 98.8 ms: 1.02x faster                                              |
| sympy_integrate            | 19.8 ms                                                | 19.4 ms: 1.02x faster                                              |
| 2to3                       | 266 ms                                                 | 260 ms: 1.02x faster                                               |
| meteor_contest             | 108 ms                                                 | 106 ms: 1.02x faster                                               |
| thrift                     | 800 us                                                 | 783 us: 1.02x faster                                               |
| html5lib                   | 63.4 ms                                                | 62.1 ms: 1.02x faster                                              |
| regex_dna                  | 220 ms                                                 | 216 ms: 1.02x faster                                               |
| scimark_monte_carlo        | 66.8 ms                                                | 65.7 ms: 1.02x faster                                              |
| async_generators           | 433 ms                                                 | 426 ms: 1.02x faster                                               |
| json                       | 5.32 ms                                                | 5.24 ms: 1.02x faster                                              |
| sphinx                     | 1.03 sec                                               | 1.02 sec: 1.02x faster                                             |
| pathlib                    | 17.4 ms                                                | 17.1 ms: 1.02x faster                                              |
| python_startup_no_site     | 7.00 ms                                                | 6.90 ms: 1.01x faster                                              |
| mako                       | 10.7 ms                                                | 10.5 ms: 1.01x faster                                              |
| sympy_sum                  | 150 ms                                                 | 149 ms: 1.01x faster                                               |
| gc_traversal               | 4.90 ms                                                | 4.88 ms: 1.00x faster                                              |
| asyncio_websockets         | 551 ms                                                 | 554 ms: 1.00x slower                                               |
| fannkuch                   | 394 ms                                                 | 396 ms: 1.01x slower                                               |
| shortest_path              | 487 ms                                                 | 491 ms: 1.01x slower                                               |
| crypto_pyaes               | 74.7 ms                                                | 75.5 ms: 1.01x slower                                              |
| pidigits                   | 186 ms                                                 | 189 ms: 1.01x slower                                               |
| logging_format             | 6.23 us                                                | 6.35 us: 1.02x slower                                              |
| hexiom                     | 6.08 ms                                                | 6.21 ms: 1.02x slower                                              |
| nqueens                    | 80.9 ms                                                | 82.9 ms: 1.02x slower                                              |
| docutils                   | 2.58 sec                                               | 2.65 sec: 1.03x slower                                             |
| connected_components       | 447 ms                                                 | 459 ms: 1.03x slower                                               |
| sympy_expand               | 456 ms                                                 | 469 ms: 1.03x slower                                               |
| django_template            | 31.7 ms                                                | 32.5 ms: 1.03x slower                                              |
| json_loads                 | 27.2 us                                                | 28.1 us: 1.03x slower                                              |
| raytrace                   | 262 ms                                                 | 272 ms: 1.04x slower                                               |
| scimark_lu                 | 114 ms                                                 | 119 ms: 1.04x slower                                               |
| logging_silent             | 101 ns                                                 | 105 ns: 1.04x slower                                               |
| typing_runtime_protocols   | 160 us                                                 | 168 us: 1.05x slower                                               |
| create_gc_cycles           | 2.45 ms                                                | 2.58 ms: 1.05x slower                                              |
| pickle_pure_python         | 302 us                                                 | 320 us: 1.06x slower                                               |
| coverage                   | 82.8 ms                                                | 87.9 ms: 1.06x slower                                              |
| chaos                      | 58.0 ms                                                | 61.9 ms: 1.07x slower                                              |
| json_dumps                 | 10.1 ms                                                | 11.0 ms: 1.09x slower                                              |
| nbody                      | 87.7 ms                                                | 96.3 ms: 1.10x slower                                              |
| generators                 | 28.8 ms                                                | 31.7 ms: 1.10x slower                                              |
| coroutines                 | 22.2 ms                                                | 25.0 ms: 1.12x slower                                              |
| many_optionals             | 857 us                                                 | 977 us: 1.14x slower                                               |
| subparsers                 | 15.5 ms                                                | 23.6 ms: 1.52x slower                                              |
| Geometric mean             | (ref)                                                  | 1.06x faster                                                       |

Benchmark hidden because not significant (6): scimark_sparse_mat_mult, sympy_str, genshi_xml, logging_simple, comprehensions, djangocms
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250629-3.15.0a0-ad5f858-JIT/bm-20250629-linux-x86_64-brandtbucher-jit_up_12_9-3.15.0a0-ad5f858.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.063x faster

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.07x