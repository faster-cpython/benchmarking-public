# Results vs. 3.13.0

- fork: brandtbucher
- ref: jit_up_10_12
- machine: linux-x86_64
- commit hash: 0f33ad5
- commit date: 2025-06-29
- overall geometric mean: 1.061x faster
- HPT reliability: 99.97%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250629-linux-x86_64-brandtbucher-jit_up_10_12-3.15.0a0-0f33ad5 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 261 ms: 1.02x faster                                                |
| docutils       | 2.58 sec                                               | 2.64 sec: 1.02x slower                                              |
| html5lib       | 63.4 ms                                                | 61.8 ms: 1.03x faster                                               |
| sphinx         | 1.03 sec                                               | 1.02 sec: 1.02x faster                                              |
| Geometric mean | (ref)                                                  | 1.01x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250629-linux-x86_64-brandtbucher-jit_up_10_12-3.15.0a0-0f33ad5 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 313 ms: 1.48x faster                                                |
| async_tree_io              | 838 ms                                                 | 603 ms: 1.39x faster                                                |
| async_tree_memoization     | 437 ms                                                 | 317 ms: 1.38x faster                                                |
| async_tree_io_tg           | 861 ms                                                 | 633 ms: 1.36x faster                                                |
| async_tree_none            | 350 ms                                                 | 264 ms: 1.33x faster                                                |
| async_tree_none_tg         | 319 ms                                                 | 252 ms: 1.27x faster                                                |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 498 ms: 1.15x faster                                                |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 486 ms: 1.12x faster                                                |
| coroutines                 | 22.2 ms                                                | 24.6 ms: 1.11x slower                                               |
| Geometric mean             | (ref)                                                  | 1.20x faster                                                        |

Benchmark hidden because not significant (2): async_generators, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250629-linux-x86_64-brandtbucher-jit_up_10_12-3.15.0a0-0f33ad5 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 65.8 ms: 1.19x faster                                               |
| pidigits       | 186 ms                                                 | 188 ms: 1.01x slower                                                |
| nbody          | 87.7 ms                                                | 97.0 ms: 1.11x slower                                               |
| Geometric mean | (ref)                                                  | 1.02x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250629-linux-x86_64-brandtbucher-jit_up_10_12-3.15.0a0-0f33ad5 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_v8       | 26.9 ms                                                | 23.0 ms: 1.17x faster                                               |
| regex_effbot   | 3.77 ms                                                | 3.32 ms: 1.13x faster                                               |
| regex_compile  | 132 ms                                                 | 127 ms: 1.04x faster                                                |
| regex_dna      | 220 ms                                                 | 215 ms: 1.02x faster                                                |
| Geometric mean | (ref)                                                  | 1.09x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250629-linux-x86_64-brandtbucher-jit_up_10_12-3.15.0a0-0f33ad5 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.83 sec: 1.16x faster                                              |
| unpickle_pure_python | 213 us                                                 | 192 us: 1.11x faster                                                |
| xml_etree_parse      | 154 ms                                                 | 140 ms: 1.10x faster                                                |
| xml_etree_generate   | 86.8 ms                                                | 79.5 ms: 1.09x faster                                               |
| xml_etree_process    | 60.5 ms                                                | 55.4 ms: 1.09x faster                                               |
| xml_etree_iterparse  | 101 ms                                                 | 98.1 ms: 1.03x faster                                               |
| json_loads           | 27.2 us                                                | 28.0 us: 1.03x slower                                               |
| pickle_pure_python   | 302 us                                                 | 322 us: 1.06x slower                                                |
| json_dumps           | 10.1 ms                                                | 11.1 ms: 1.10x slower                                               |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250629-linux-x86_64-brandtbucher-jit_up_10_12-3.15.0a0-0f33ad5 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 12.2 ms: 1.04x faster                                               |
| python_startup_no_site | 7.00 ms                                                | 6.93 ms: 1.01x faster                                               |
| Geometric mean         | (ref)                                                  | 1.03x faster                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250629-linux-x86_64-brandtbucher-jit_up_10_12-3.15.0a0-0f33ad5 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.7 ms: 1.04x faster                                               |
| mako            | 10.7 ms                                                | 10.5 ms: 1.02x faster                                               |
| django_template | 31.7 ms                                                | 33.0 ms: 1.04x slower                                               |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                        |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250629-linux-x86_64-brandtbucher-jit_up_10_12-3.15.0a0-0f33ad5 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.24 sec: 2.06x faster                                              |
| async_tree_memoization_tg  | 463 ms                                                 | 313 ms: 1.48x faster                                                |
| async_tree_io              | 838 ms                                                 | 603 ms: 1.39x faster                                                |
| richards                   | 47.5 ms                                                | 34.3 ms: 1.39x faster                                               |
| async_tree_memoization     | 437 ms                                                 | 317 ms: 1.38x faster                                                |
| richards_super             | 53.7 ms                                                | 39.4 ms: 1.36x faster                                               |
| async_tree_io_tg           | 861 ms                                                 | 633 ms: 1.36x faster                                                |
| deepcopy                   | 354 us                                                 | 262 us: 1.35x faster                                                |
| async_tree_none            | 350 ms                                                 | 264 ms: 1.33x faster                                                |
| deepcopy_memo              | 38.4 us                                                | 29.8 us: 1.29x faster                                               |
| async_tree_none_tg         | 319 ms                                                 | 252 ms: 1.27x faster                                                |
| spectral_norm              | 113 ms                                                 | 92.0 ms: 1.23x faster                                               |
| go                         | 141 ms                                                 | 117 ms: 1.20x faster                                                |
| float                      | 78.7 ms                                                | 65.8 ms: 1.19x faster                                               |
| deepcopy_reduce            | 3.24 us                                                | 2.74 us: 1.18x faster                                               |
| regex_v8                   | 26.9 ms                                                | 23.0 ms: 1.17x faster                                               |
| scimark_fft                | 367 ms                                                 | 315 ms: 1.16x faster                                                |
| tomli_loads                | 2.12 sec                                               | 1.83 sec: 1.16x faster                                              |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 498 ms: 1.15x faster                                                |
| pyflate                    | 470 ms                                                 | 414 ms: 1.13x faster                                                |
| regex_effbot               | 3.77 ms                                                | 3.32 ms: 1.13x faster                                               |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 486 ms: 1.12x faster                                                |
| unpickle_pure_python       | 213 us                                                 | 192 us: 1.11x faster                                                |
| telco                      | 8.40 ms                                                | 7.58 ms: 1.11x faster                                               |
| xml_etree_parse            | 154 ms                                                 | 140 ms: 1.10x faster                                                |
| pylint                     | 312 ms                                                 | 284 ms: 1.10x faster                                                |
| xml_etree_generate         | 86.8 ms                                                | 79.5 ms: 1.09x faster                                               |
| xml_etree_process          | 60.5 ms                                                | 55.4 ms: 1.09x faster                                               |
| dulwich_log                | 64.6 ms                                                | 59.6 ms: 1.08x faster                                               |
| bpe_tokeniser              | 4.69 sec                                               | 4.34 sec: 1.08x faster                                              |
| thrift                     | 800 us                                                 | 766 us: 1.04x faster                                                |
| crypto_pyaes               | 74.7 ms                                                | 71.6 ms: 1.04x faster                                               |
| deltablue                  | 3.19 ms                                                | 3.06 ms: 1.04x faster                                               |
| genshi_text                | 22.6 ms                                                | 21.7 ms: 1.04x faster                                               |
| sqlite_synth               | 2.90 us                                                | 2.79 us: 1.04x faster                                               |
| python_startup             | 12.7 ms                                                | 12.2 ms: 1.04x faster                                               |
| k_core                     | 2.37 sec                                               | 2.28 sec: 1.04x faster                                              |
| pycparser                  | 1.20 sec                                               | 1.15 sec: 1.04x faster                                              |
| regex_compile              | 132 ms                                                 | 127 ms: 1.04x faster                                                |
| xml_etree_iterparse        | 101 ms                                                 | 98.1 ms: 1.03x faster                                               |
| meteor_contest             | 108 ms                                                 | 105 ms: 1.03x faster                                                |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.89 ms: 1.03x faster                                               |
| json                       | 5.32 ms                                                | 5.19 ms: 1.03x faster                                               |
| pathlib                    | 17.4 ms                                                | 16.9 ms: 1.03x faster                                               |
| html5lib                   | 63.4 ms                                                | 61.8 ms: 1.03x faster                                               |
| regex_dna                  | 220 ms                                                 | 215 ms: 1.02x faster                                                |
| scimark_sor                | 122 ms                                                 | 119 ms: 1.02x faster                                                |
| 2to3                       | 266 ms                                                 | 261 ms: 1.02x faster                                                |
| sphinx                     | 1.03 sec                                               | 1.02 sec: 1.02x faster                                              |
| mako                       | 10.7 ms                                                | 10.5 ms: 1.02x faster                                               |
| scimark_monte_carlo        | 66.8 ms                                                | 65.9 ms: 1.01x faster                                               |
| sympy_integrate            | 19.8 ms                                                | 19.6 ms: 1.01x faster                                               |
| python_startup_no_site     | 7.00 ms                                                | 6.93 ms: 1.01x faster                                               |
| fannkuch                   | 394 ms                                                 | 395 ms: 1.00x slower                                                |
| sympy_sum                  | 150 ms                                                 | 151 ms: 1.00x slower                                                |
| gc_traversal               | 4.90 ms                                                | 4.93 ms: 1.01x slower                                               |
| shortest_path              | 487 ms                                                 | 491 ms: 1.01x slower                                                |
| pidigits                   | 186 ms                                                 | 188 ms: 1.01x slower                                                |
| comprehensions             | 16.5 us                                                | 16.7 us: 1.01x slower                                               |
| logging_format             | 6.23 us                                                | 6.36 us: 1.02x slower                                               |
| docutils                   | 2.58 sec                                               | 2.64 sec: 1.02x slower                                              |
| nqueens                    | 80.9 ms                                                | 82.9 ms: 1.02x slower                                               |
| pprint_pformat             | 1.48 sec                                               | 1.52 sec: 1.03x slower                                              |
| sympy_expand               | 456 ms                                                 | 470 ms: 1.03x slower                                                |
| json_loads                 | 27.2 us                                                | 28.0 us: 1.03x slower                                               |
| hexiom                     | 6.08 ms                                                | 6.27 ms: 1.03x slower                                               |
| scimark_lu                 | 114 ms                                                 | 119 ms: 1.04x slower                                                |
| pprint_safe_repr           | 727 ms                                                 | 754 ms: 1.04x slower                                                |
| django_template            | 31.7 ms                                                | 33.0 ms: 1.04x slower                                               |
| generators                 | 28.8 ms                                                | 30.0 ms: 1.04x slower                                               |
| typing_runtime_protocols   | 160 us                                                 | 168 us: 1.05x slower                                                |
| create_gc_cycles           | 2.45 ms                                                | 2.58 ms: 1.05x slower                                               |
| raytrace                   | 262 ms                                                 | 276 ms: 1.06x slower                                                |
| coverage                   | 82.8 ms                                                | 87.6 ms: 1.06x slower                                               |
| chaos                      | 58.0 ms                                                | 61.6 ms: 1.06x slower                                               |
| pickle_pure_python         | 302 us                                                 | 322 us: 1.06x slower                                                |
| json_dumps                 | 10.1 ms                                                | 11.1 ms: 1.10x slower                                               |
| connected_components       | 447 ms                                                 | 493 ms: 1.10x slower                                                |
| nbody                      | 87.7 ms                                                | 97.0 ms: 1.11x slower                                               |
| coroutines                 | 22.2 ms                                                | 24.6 ms: 1.11x slower                                               |
| many_optionals             | 857 us                                                 | 982 us: 1.15x slower                                                |
| subparsers                 | 15.5 ms                                                | 23.6 ms: 1.53x slower                                               |
| Geometric mean             | (ref)                                                  | 1.06x faster                                                        |

Benchmark hidden because not significant (7): genshi_xml, sympy_str, async_generators, asyncio_websockets, logging_simple, logging_silent, djangocms
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250629-3.15.0a0-0f33ad5-JIT/bm-20250629-linux-x86_64-brandtbucher-jit_up_10_12-3.15.0a0-0f33ad5.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.061x faster

# HPT report

- Reliability score: 99.97% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.07x