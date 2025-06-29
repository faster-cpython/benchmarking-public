# Results vs. 3.13.0

- fork: brandtbucher
- ref: jit_up_11_12
- machine: linux-x86_64
- commit hash: e1a3f48
- commit date: 2025-06-29
- overall geometric mean: 1.065x faster
- HPT reliability: 99.98%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250629-linux-x86_64-brandtbucher-jit_up_11_12-3.15.0a0-e1a3f48 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 258 ms: 1.03x faster                                                |
| docutils       | 2.58 sec                                               | 2.64 sec: 1.02x slower                                              |
| html5lib       | 63.4 ms                                                | 62.2 ms: 1.02x faster                                               |
| sphinx         | 1.03 sec                                               | 1.01 sec: 1.02x faster                                              |
| Geometric mean | (ref)                                                  | 1.01x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250629-linux-x86_64-brandtbucher-jit_up_11_12-3.15.0a0-e1a3f48 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 312 ms: 1.48x faster                                                |
| async_tree_memoization     | 437 ms                                                 | 314 ms: 1.39x faster                                                |
| async_tree_io              | 838 ms                                                 | 607 ms: 1.38x faster                                                |
| async_tree_io_tg           | 861 ms                                                 | 626 ms: 1.37x faster                                                |
| async_tree_none            | 350 ms                                                 | 262 ms: 1.34x faster                                                |
| async_tree_none_tg         | 319 ms                                                 | 248 ms: 1.29x faster                                                |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 500 ms: 1.15x faster                                                |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 491 ms: 1.11x faster                                                |
| async_generators           | 433 ms                                                 | 432 ms: 1.00x faster                                                |
| asyncio_websockets         | 551 ms                                                 | 553 ms: 1.00x slower                                                |
| coroutines                 | 22.2 ms                                                | 25.1 ms: 1.13x slower                                               |
| Geometric mean             | (ref)                                                  | 1.20x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250629-linux-x86_64-brandtbucher-jit_up_11_12-3.15.0a0-e1a3f48 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 66.0 ms: 1.19x faster                                               |
| pidigits       | 186 ms                                                 | 189 ms: 1.01x slower                                                |
| nbody          | 87.7 ms                                                | 96.1 ms: 1.10x slower                                               |
| Geometric mean | (ref)                                                  | 1.02x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250629-linux-x86_64-brandtbucher-jit_up_11_12-3.15.0a0-e1a3f48 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_v8       | 26.9 ms                                                | 22.3 ms: 1.20x faster                                               |
| regex_effbot   | 3.77 ms                                                | 3.23 ms: 1.16x faster                                               |
| regex_dna      | 220 ms                                                 | 200 ms: 1.10x faster                                                |
| regex_compile  | 132 ms                                                 | 127 ms: 1.04x faster                                                |
| Geometric mean | (ref)                                                  | 1.13x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250629-linux-x86_64-brandtbucher-jit_up_11_12-3.15.0a0-e1a3f48 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.81 sec: 1.17x faster                                              |
| unpickle_pure_python | 213 us                                                 | 190 us: 1.12x faster                                                |
| xml_etree_parse      | 154 ms                                                 | 140 ms: 1.10x faster                                                |
| xml_etree_generate   | 86.8 ms                                                | 81.2 ms: 1.07x faster                                               |
| xml_etree_process    | 60.5 ms                                                | 56.6 ms: 1.07x faster                                               |
| xml_etree_iterparse  | 101 ms                                                 | 98.5 ms: 1.03x faster                                               |
| json_loads           | 27.2 us                                                | 28.4 us: 1.04x slower                                               |
| pickle_pure_python   | 302 us                                                 | 324 us: 1.07x slower                                                |
| json_dumps           | 10.1 ms                                                | 11.0 ms: 1.09x slower                                               |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250629-linux-x86_64-brandtbucher-jit_up_11_12-3.15.0a0-e1a3f48 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 12.2 ms: 1.04x faster                                               |
| python_startup_no_site | 7.00 ms                                                | 6.94 ms: 1.01x faster                                               |
| Geometric mean         | (ref)                                                  | 1.02x faster                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250629-linux-x86_64-brandtbucher-jit_up_11_12-3.15.0a0-e1a3f48 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.8 ms: 1.04x faster                                               |
| django_template | 31.7 ms                                                | 32.8 ms: 1.04x slower                                               |
| Geometric mean  | (ref)                                                  | 1.00x slower                                                        |

Benchmark hidden because not significant (2): mako, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250629-linux-x86_64-brandtbucher-jit_up_11_12-3.15.0a0-e1a3f48 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.22 sec: 2.08x faster                                              |
| async_tree_memoization_tg  | 463 ms                                                 | 312 ms: 1.48x faster                                                |
| async_tree_memoization     | 437 ms                                                 | 314 ms: 1.39x faster                                                |
| async_tree_io              | 838 ms                                                 | 607 ms: 1.38x faster                                                |
| async_tree_io_tg           | 861 ms                                                 | 626 ms: 1.37x faster                                                |
| richards                   | 47.5 ms                                                | 34.7 ms: 1.37x faster                                               |
| deepcopy                   | 354 us                                                 | 259 us: 1.37x faster                                                |
| richards_super             | 53.7 ms                                                | 39.8 ms: 1.35x faster                                               |
| async_tree_none            | 350 ms                                                 | 262 ms: 1.34x faster                                                |
| deepcopy_memo              | 38.4 us                                                | 29.4 us: 1.30x faster                                               |
| async_tree_none_tg         | 319 ms                                                 | 248 ms: 1.29x faster                                                |
| spectral_norm              | 113 ms                                                 | 91.7 ms: 1.24x faster                                               |
| go                         | 141 ms                                                 | 115 ms: 1.22x faster                                                |
| regex_v8                   | 26.9 ms                                                | 22.3 ms: 1.20x faster                                               |
| float                      | 78.7 ms                                                | 66.0 ms: 1.19x faster                                               |
| deepcopy_reduce            | 3.24 us                                                | 2.75 us: 1.18x faster                                               |
| scimark_fft                | 367 ms                                                 | 312 ms: 1.18x faster                                                |
| tomli_loads                | 2.12 sec                                               | 1.81 sec: 1.17x faster                                              |
| regex_effbot               | 3.77 ms                                                | 3.23 ms: 1.16x faster                                               |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 500 ms: 1.15x faster                                                |
| unpickle_pure_python       | 213 us                                                 | 190 us: 1.12x faster                                                |
| pyflate                    | 470 ms                                                 | 420 ms: 1.12x faster                                                |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 491 ms: 1.11x faster                                                |
| xml_etree_parse            | 154 ms                                                 | 140 ms: 1.10x faster                                                |
| regex_dna                  | 220 ms                                                 | 200 ms: 1.10x faster                                                |
| pylint                     | 312 ms                                                 | 284 ms: 1.10x faster                                                |
| bpe_tokeniser              | 4.69 sec                                               | 4.34 sec: 1.08x faster                                              |
| dulwich_log                | 64.6 ms                                                | 59.9 ms: 1.08x faster                                               |
| pycparser                  | 1.20 sec                                               | 1.11 sec: 1.08x faster                                              |
| telco                      | 8.40 ms                                                | 7.82 ms: 1.07x faster                                               |
| xml_etree_generate         | 86.8 ms                                                | 81.2 ms: 1.07x faster                                               |
| xml_etree_process          | 60.5 ms                                                | 56.6 ms: 1.07x faster                                               |
| deltablue                  | 3.19 ms                                                | 3.02 ms: 1.06x faster                                               |
| crypto_pyaes               | 74.7 ms                                                | 71.7 ms: 1.04x faster                                               |
| scimark_sor                | 122 ms                                                 | 117 ms: 1.04x faster                                                |
| python_startup             | 12.7 ms                                                | 12.2 ms: 1.04x faster                                               |
| regex_compile              | 132 ms                                                 | 127 ms: 1.04x faster                                                |
| sqlite_synth               | 2.90 us                                                | 2.79 us: 1.04x faster                                               |
| genshi_text                | 22.6 ms                                                | 21.8 ms: 1.04x faster                                               |
| k_core                     | 2.37 sec                                               | 2.29 sec: 1.04x faster                                              |
| 2to3                       | 266 ms                                                 | 258 ms: 1.03x faster                                                |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.88 ms: 1.03x faster                                               |
| pathlib                    | 17.4 ms                                                | 16.9 ms: 1.03x faster                                               |
| xml_etree_iterparse        | 101 ms                                                 | 98.5 ms: 1.03x faster                                               |
| pprint_safe_repr           | 727 ms                                                 | 708 ms: 1.03x faster                                                |
| thrift                     | 800 us                                                 | 779 us: 1.03x faster                                                |
| gc_traversal               | 4.90 ms                                                | 4.78 ms: 1.03x faster                                               |
| scimark_monte_carlo        | 66.8 ms                                                | 65.3 ms: 1.02x faster                                               |
| meteor_contest             | 108 ms                                                 | 106 ms: 1.02x faster                                                |
| sympy_integrate            | 19.8 ms                                                | 19.4 ms: 1.02x faster                                               |
| html5lib                   | 63.4 ms                                                | 62.2 ms: 1.02x faster                                               |
| sphinx                     | 1.03 sec                                               | 1.01 sec: 1.02x faster                                              |
| pprint_pformat             | 1.48 sec                                               | 1.45 sec: 1.02x faster                                              |
| json                       | 5.32 ms                                                | 5.23 ms: 1.02x faster                                               |
| python_startup_no_site     | 7.00 ms                                                | 6.94 ms: 1.01x faster                                               |
| logging_simple             | 5.65 us                                                | 5.62 us: 1.01x faster                                               |
| async_generators           | 433 ms                                                 | 432 ms: 1.00x faster                                                |
| asyncio_websockets         | 551 ms                                                 | 553 ms: 1.00x slower                                                |
| pidigits                   | 186 ms                                                 | 189 ms: 1.01x slower                                                |
| nqueens                    | 80.9 ms                                                | 82.1 ms: 1.01x slower                                               |
| logging_silent             | 101 ns                                                 | 103 ns: 1.02x slower                                                |
| hexiom                     | 6.08 ms                                                | 6.21 ms: 1.02x slower                                               |
| sympy_expand               | 456 ms                                                 | 466 ms: 1.02x slower                                                |
| docutils                   | 2.58 sec                                               | 2.64 sec: 1.02x slower                                              |
| shortest_path              | 487 ms                                                 | 498 ms: 1.02x slower                                                |
| raytrace                   | 262 ms                                                 | 270 ms: 1.03x slower                                                |
| connected_components       | 447 ms                                                 | 463 ms: 1.04x slower                                                |
| django_template            | 31.7 ms                                                | 32.8 ms: 1.04x slower                                               |
| typing_runtime_protocols   | 160 us                                                 | 167 us: 1.04x slower                                                |
| scimark_lu                 | 114 ms                                                 | 119 ms: 1.04x slower                                                |
| json_loads                 | 27.2 us                                                | 28.4 us: 1.04x slower                                               |
| chaos                      | 58.0 ms                                                | 61.0 ms: 1.05x slower                                               |
| create_gc_cycles           | 2.45 ms                                                | 2.59 ms: 1.06x slower                                               |
| coverage                   | 82.8 ms                                                | 88.2 ms: 1.06x slower                                               |
| pickle_pure_python         | 302 us                                                 | 324 us: 1.07x slower                                                |
| json_dumps                 | 10.1 ms                                                | 11.0 ms: 1.09x slower                                               |
| generators                 | 28.8 ms                                                | 31.3 ms: 1.09x slower                                               |
| nbody                      | 87.7 ms                                                | 96.1 ms: 1.10x slower                                               |
| coroutines                 | 22.2 ms                                                | 25.1 ms: 1.13x slower                                               |
| many_optionals             | 857 us                                                 | 981 us: 1.14x slower                                                |
| subparsers                 | 15.5 ms                                                | 23.8 ms: 1.54x slower                                               |
| Geometric mean             | (ref)                                                  | 1.06x faster                                                        |

Benchmark hidden because not significant (8): mako, sympy_str, comprehensions, sympy_sum, genshi_xml, logging_format, fannkuch, djangocms
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250629-3.15.0a0-e1a3f48-JIT/bm-20250629-linux-x86_64-brandtbucher-jit_up_11_12-3.15.0a0-e1a3f48.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.065x faster

# HPT report

- Reliability score: 99.98% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.07x