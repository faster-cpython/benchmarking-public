# Results vs. 3.13.0

- fork: brandtbucher
- ref: keep_tracing
- machine: linux-x86_64
- commit hash: 8746972
- commit date: 2025-06-09
- overall geometric mean: 1.039x slower
- HPT reliability: 88.48%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250609-linux-x86_64-brandtbucher-keep_tracing-3.15.0a0-8746972 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 262 ms: 1.02x faster                                                |
| docutils       | 2.58 sec                                               | 2.65 sec: 1.02x slower                                              |
| html5lib       | 63.4 ms                                                | 62.3 ms: 1.02x faster                                               |
| Geometric mean | (ref)                                                  | 1.00x faster                                                        |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250609-linux-x86_64-brandtbucher-keep_tracing-3.15.0a0-8746972 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 318 ms: 1.46x faster                                                |
| async_tree_io_tg           | 861 ms                                                 | 616 ms: 1.40x faster                                                |
| async_tree_io              | 838 ms                                                 | 605 ms: 1.39x faster                                                |
| async_tree_memoization     | 437 ms                                                 | 315 ms: 1.39x faster                                                |
| async_tree_none            | 350 ms                                                 | 265 ms: 1.32x faster                                                |
| async_tree_none_tg         | 319 ms                                                 | 252 ms: 1.27x faster                                                |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 506 ms: 1.13x faster                                                |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 498 ms: 1.09x faster                                                |
| async_generators           | 433 ms                                                 | 424 ms: 1.02x faster                                                |
| asyncio_websockets         | 551 ms                                                 | 553 ms: 1.00x slower                                                |
| coroutines                 | 22.2 ms                                                | 25.2 ms: 1.14x slower                                               |
| Geometric mean             | (ref)                                                  | 1.20x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250609-linux-x86_64-brandtbucher-keep_tracing-3.15.0a0-8746972 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 65.4 ms: 1.20x faster                                               |
| pidigits       | 186 ms                                                 | 191 ms: 1.02x slower                                                |
| nbody          | 87.7 ms                                                | 90.4 ms: 1.03x slower                                               |
| Geometric mean | (ref)                                                  | 1.04x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250609-linux-x86_64-brandtbucher-keep_tracing-3.15.0a0-8746972 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_v8       | 26.9 ms                                                | 22.8 ms: 1.18x faster                                               |
| regex_effbot   | 3.77 ms                                                | 3.49 ms: 1.08x faster                                               |
| regex_compile  | 132 ms                                                 | 129 ms: 1.02x faster                                                |
| Geometric mean | (ref)                                                  | 1.07x faster                                                        |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250609-linux-x86_64-brandtbucher-keep_tracing-3.15.0a0-8746972 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.93 sec: 1.10x faster                                              |
| xml_etree_process    | 60.5 ms                                                | 56.0 ms: 1.08x faster                                               |
| xml_etree_generate   | 86.8 ms                                                | 80.5 ms: 1.08x faster                                               |
| xml_etree_parse      | 154 ms                                                 | 145 ms: 1.07x faster                                                |
| unpickle_pure_python | 213 us                                                 | 205 us: 1.04x faster                                                |
| json_loads           | 27.2 us                                                | 28.3 us: 1.04x slower                                               |
| pickle_pure_python   | 302 us                                                 | 330 us: 1.09x slower                                                |
| json_dumps           | 10.1 ms                                                | 11.2 ms: 1.11x slower                                               |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                        |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250609-linux-x86_64-brandtbucher-keep_tracing-3.15.0a0-8746972 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 12.2 ms: 1.04x faster                                               |
| python_startup_no_site | 7.00 ms                                                | 6.94 ms: 1.01x faster                                               |
| Geometric mean         | (ref)                                                  | 1.02x faster                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250609-linux-x86_64-brandtbucher-keep_tracing-3.15.0a0-8746972 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 22.0 ms: 1.03x faster                                               |
| mako            | 10.7 ms                                                | 10.8 ms: 1.01x slower                                               |
| genshi_xml      | 50.5 ms                                                | 51.1 ms: 1.01x slower                                               |
| django_template | 31.7 ms                                                | 32.8 ms: 1.04x slower                                               |
| Geometric mean  | (ref)                                                  | 1.01x slower                                                        |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250609-linux-x86_64-brandtbucher-keep_tracing-3.15.0a0-8746972 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.26 sec: 2.01x faster                                              |
| async_tree_memoization_tg  | 463 ms                                                 | 318 ms: 1.46x faster                                                |
| async_tree_io_tg           | 861 ms                                                 | 616 ms: 1.40x faster                                                |
| async_tree_io              | 838 ms                                                 | 605 ms: 1.39x faster                                                |
| async_tree_memoization     | 437 ms                                                 | 315 ms: 1.39x faster                                                |
| deepcopy                   | 354 us                                                 | 262 us: 1.35x faster                                                |
| async_tree_none            | 350 ms                                                 | 265 ms: 1.32x faster                                                |
| deepcopy_memo              | 38.4 us                                                | 29.8 us: 1.29x faster                                               |
| richards                   | 47.5 ms                                                | 37.0 ms: 1.29x faster                                               |
| richards_super             | 53.7 ms                                                | 42.4 ms: 1.27x faster                                               |
| async_tree_none_tg         | 319 ms                                                 | 252 ms: 1.27x faster                                                |
| float                      | 78.7 ms                                                | 65.4 ms: 1.20x faster                                               |
| regex_v8                   | 26.9 ms                                                | 22.8 ms: 1.18x faster                                               |
| deepcopy_reduce            | 3.24 us                                                | 2.82 us: 1.15x faster                                               |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 506 ms: 1.13x faster                                                |
| go                         | 141 ms                                                 | 126 ms: 1.12x faster                                                |
| pyflate                    | 470 ms                                                 | 425 ms: 1.11x faster                                                |
| tomli_loads                | 2.12 sec                                               | 1.93 sec: 1.10x faster                                              |
| pylint                     | 312 ms                                                 | 284 ms: 1.10x faster                                                |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 498 ms: 1.09x faster                                                |
| scimark_fft                | 367 ms                                                 | 339 ms: 1.08x faster                                                |
| regex_effbot               | 3.77 ms                                                | 3.49 ms: 1.08x faster                                               |
| xml_etree_process          | 60.5 ms                                                | 56.0 ms: 1.08x faster                                               |
| xml_etree_generate         | 86.8 ms                                                | 80.5 ms: 1.08x faster                                               |
| spectral_norm              | 113 ms                                                 | 106 ms: 1.07x faster                                                |
| xml_etree_parse            | 154 ms                                                 | 145 ms: 1.07x faster                                                |
| dulwich_log                | 64.6 ms                                                | 61.7 ms: 1.05x faster                                               |
| bpe_tokeniser              | 4.69 sec                                               | 4.49 sec: 1.05x faster                                              |
| telco                      | 8.40 ms                                                | 8.07 ms: 1.04x faster                                               |
| unpickle_pure_python       | 213 us                                                 | 205 us: 1.04x faster                                                |
| python_startup             | 12.7 ms                                                | 12.2 ms: 1.04x faster                                               |
| json                       | 5.32 ms                                                | 5.14 ms: 1.04x faster                                               |
| sqlite_synth               | 2.90 us                                                | 2.81 us: 1.03x faster                                               |
| k_core                     | 2.37 sec                                               | 2.31 sec: 1.03x faster                                              |
| genshi_text                | 22.6 ms                                                | 22.0 ms: 1.03x faster                                               |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.91 ms: 1.03x faster                                               |
| regex_compile              | 132 ms                                                 | 129 ms: 1.02x faster                                                |
| async_generators           | 433 ms                                                 | 424 ms: 1.02x faster                                                |
| pathlib                    | 17.4 ms                                                | 17.0 ms: 1.02x faster                                               |
| deltablue                  | 3.19 ms                                                | 3.14 ms: 1.02x faster                                               |
| pycparser                  | 1.20 sec                                               | 1.18 sec: 1.02x faster                                              |
| html5lib                   | 63.4 ms                                                | 62.3 ms: 1.02x faster                                               |
| 2to3                       | 266 ms                                                 | 262 ms: 1.02x faster                                                |
| sympy_integrate            | 19.8 ms                                                | 19.6 ms: 1.01x faster                                               |
| python_startup_no_site     | 7.00 ms                                                | 6.94 ms: 1.01x faster                                               |
| asyncio_websockets         | 551 ms                                                 | 553 ms: 1.00x slower                                                |
| mako                       | 10.7 ms                                                | 10.8 ms: 1.01x slower                                               |
| sympy_sum                  | 150 ms                                                 | 152 ms: 1.01x slower                                                |
| genshi_xml                 | 50.5 ms                                                | 51.1 ms: 1.01x slower                                               |
| scimark_monte_carlo        | 66.8 ms                                                | 67.8 ms: 1.01x slower                                               |
| comprehensions             | 16.5 us                                                | 16.8 us: 1.02x slower                                               |
| connected_components       | 447 ms                                                 | 457 ms: 1.02x slower                                                |
| scimark_lu                 | 114 ms                                                 | 117 ms: 1.02x slower                                                |
| docutils                   | 2.58 sec                                               | 2.65 sec: 1.02x slower                                              |
| pidigits                   | 186 ms                                                 | 191 ms: 1.02x slower                                                |
| nqueens                    | 80.9 ms                                                | 83.0 ms: 1.03x slower                                               |
| crypto_pyaes               | 74.7 ms                                                | 76.7 ms: 1.03x slower                                               |
| shortest_path              | 487 ms                                                 | 500 ms: 1.03x slower                                                |
| generators                 | 28.8 ms                                                | 29.7 ms: 1.03x slower                                               |
| nbody                      | 87.7 ms                                                | 90.4 ms: 1.03x slower                                               |
| sympy_expand               | 456 ms                                                 | 472 ms: 1.03x slower                                                |
| django_template            | 31.7 ms                                                | 32.8 ms: 1.04x slower                                               |
| json_loads                 | 27.2 us                                                | 28.3 us: 1.04x slower                                               |
| gc_traversal               | 4.90 ms                                                | 5.18 ms: 1.06x slower                                               |
| raytrace                   | 262 ms                                                 | 278 ms: 1.06x slower                                                |
| create_gc_cycles           | 2.45 ms                                                | 2.60 ms: 1.06x slower                                               |
| fannkuch                   | 394 ms                                                 | 418 ms: 1.06x slower                                                |
| typing_runtime_protocols   | 160 us                                                 | 172 us: 1.07x slower                                                |
| logging_simple             | 5.65 us                                                | 6.09 us: 1.08x slower                                               |
| chaos                      | 58.0 ms                                                | 62.9 ms: 1.08x slower                                               |
| logging_format             | 6.23 us                                                | 6.79 us: 1.09x slower                                               |
| pickle_pure_python         | 302 us                                                 | 330 us: 1.09x slower                                                |
| json_dumps                 | 10.1 ms                                                | 11.2 ms: 1.11x slower                                               |
| hexiom                     | 6.08 ms                                                | 6.74 ms: 1.11x slower                                               |
| pprint_pformat             | 1.48 sec                                               | 1.66 sec: 1.12x slower                                              |
| coroutines                 | 22.2 ms                                                | 25.2 ms: 1.14x slower                                               |
| pprint_safe_repr           | 727 ms                                                 | 831 ms: 1.14x slower                                                |
| many_optionals             | 857 us                                                 | 984 us: 1.15x slower                                                |
| subparsers                 | 15.5 ms                                                | 23.6 ms: 1.53x slower                                               |
| logging_silent             | 101 ns                                                 | 487 ns: 4.82x slower                                                |
| coverage                   | 82.8 ms                                                | 428 ms: 5.17x slower                                                |
| thrift                     | 800 us                                                 | 148 ms: 185.33x slower                                              |
| Geometric mean             | (ref)                                                  | 1.06x slower                                                        |

Benchmark hidden because not significant (6): sphinx, xml_etree_iterparse, regex_dna, meteor_contest, scimark_sor, sympy_str
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250609-3.15.0a0-8746972-JIT/bm-20250609-linux-x86_64-brandtbucher-keep_tracing-3.15.0a0-8746972.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.039x slower

# HPT report

- Reliability score: 88.48% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.07x