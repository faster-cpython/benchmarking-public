# Results vs. 3.13.0

- fork: brandtbucher
- ref: jit_up_12_9
- machine: linux-x86_64
- commit hash: 4df91f6
- commit date: 2025-03-27
- overall geometric mean: 1.037x faster
- HPT reliability: 95.68%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250327-linux-x86_64-brandtbucher-jit_up_12_9-3.14.0a6+-4df91f6 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 265 ms: 1.00x faster                                                |
| docutils       | 2.58 sec                                               | 2.72 sec: 1.05x slower                                              |
| html5lib       | 63.4 ms                                                | 62.3 ms: 1.02x faster                                               |
| Geometric mean | (ref)                                                  | 1.01x slower                                                        |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250327-linux-x86_64-brandtbucher-jit_up_12_9-3.14.0a6+-4df91f6 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 316 ms: 1.47x faster                                                |
| async_tree_io_tg           | 861 ms                                                 | 618 ms: 1.39x faster                                                |
| async_tree_memoization     | 437 ms                                                 | 317 ms: 1.38x faster                                                |
| async_tree_io              | 838 ms                                                 | 622 ms: 1.35x faster                                                |
| async_tree_none            | 350 ms                                                 | 265 ms: 1.32x faster                                                |
| async_tree_none_tg         | 319 ms                                                 | 253 ms: 1.26x faster                                                |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 491 ms: 1.17x faster                                                |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 475 ms: 1.14x faster                                                |
| async_generators           | 433 ms                                                 | 417 ms: 1.04x faster                                                |
| asyncio_websockets         | 551 ms                                                 | 553 ms: 1.00x slower                                                |
| coroutines                 | 22.2 ms                                                | 24.6 ms: 1.11x slower                                               |
| Geometric mean             | (ref)                                                  | 1.21x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250327-linux-x86_64-brandtbucher-jit_up_12_9-3.14.0a6+-4df91f6 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 65.1 ms: 1.21x faster                                               |
| nbody          | 87.7 ms                                                | 86.8 ms: 1.01x faster                                               |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                |
| Geometric mean | (ref)                                                  | 1.07x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250327-linux-x86_64-brandtbucher-jit_up_12_9-3.14.0a6+-4df91f6 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_v8       | 26.9 ms                                                | 23.1 ms: 1.16x faster                                               |
| regex_effbot   | 3.77 ms                                                | 3.51 ms: 1.07x faster                                               |
| regex_compile  | 132 ms                                                 | 128 ms: 1.03x faster                                                |
| Geometric mean | (ref)                                                  | 1.06x faster                                                        |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250327-linux-x86_64-brandtbucher-jit_up_12_9-3.14.0a6+-4df91f6 |
|---------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| tomli_loads         | 2.12 sec                                               | 1.87 sec: 1.13x faster                                              |
| xml_etree_parse     | 154 ms                                                 | 139 ms: 1.11x faster                                                |
| xml_etree_generate  | 86.8 ms                                                | 81.0 ms: 1.07x faster                                               |
| xml_etree_process   | 60.5 ms                                                | 57.1 ms: 1.06x faster                                               |
| xml_etree_iterparse | 101 ms                                                 | 97.5 ms: 1.04x faster                                               |
| pickle_pure_python  | 302 us                                                 | 330 us: 1.09x slower                                                |
| json_loads          | 27.2 us                                                | 30.0 us: 1.11x slower                                               |
| json_dumps          | 10.1 ms                                                | 11.6 ms: 1.14x slower                                               |
| Geometric mean      | (ref)                                                  | 1.01x faster                                                        |

Benchmark hidden because not significant (1): unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250327-linux-x86_64-brandtbucher-jit_up_12_9-3.14.0a6+-4df91f6 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 13.1 ms: 1.04x slower                                               |
| python_startup_no_site | 7.00 ms                                                | 8.19 ms: 1.17x slower                                               |
| Geometric mean         | (ref)                                                  | 1.10x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250327-linux-x86_64-brandtbucher-jit_up_12_9-3.14.0a6+-4df91f6 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.5 ms: 1.05x faster                                               |
| genshi_xml      | 50.5 ms                                                | 50.1 ms: 1.01x faster                                               |
| django_template | 31.7 ms                                                | 32.0 ms: 1.01x slower                                               |
| mako            | 10.7 ms                                                | 11.0 ms: 1.03x slower                                               |
| Geometric mean  | (ref)                                                  | 1.00x faster                                                        |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250327-linux-x86_64-brandtbucher-jit_up_12_9-3.14.0a6+-4df91f6 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 316 ms: 1.47x faster                                                |
| async_tree_io_tg           | 861 ms                                                 | 618 ms: 1.39x faster                                                |
| async_tree_memoization     | 437 ms                                                 | 317 ms: 1.38x faster                                                |
| deepcopy                   | 354 us                                                 | 260 us: 1.36x faster                                                |
| async_tree_io              | 838 ms                                                 | 622 ms: 1.35x faster                                                |
| deepcopy_memo              | 38.4 us                                                | 29.0 us: 1.32x faster                                               |
| async_tree_none            | 350 ms                                                 | 265 ms: 1.32x faster                                                |
| richards_super             | 53.7 ms                                                | 41.9 ms: 1.28x faster                                               |
| richards                   | 47.5 ms                                                | 37.5 ms: 1.27x faster                                               |
| async_tree_none_tg         | 319 ms                                                 | 253 ms: 1.26x faster                                                |
| float                      | 78.7 ms                                                | 65.1 ms: 1.21x faster                                               |
| deepcopy_reduce            | 3.24 us                                                | 2.73 us: 1.19x faster                                               |
| spectral_norm              | 113 ms                                                 | 95.5 ms: 1.19x faster                                               |
| scimark_fft                | 367 ms                                                 | 310 ms: 1.18x faster                                                |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 491 ms: 1.17x faster                                                |
| regex_v8                   | 26.9 ms                                                | 23.1 ms: 1.16x faster                                               |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 475 ms: 1.14x faster                                                |
| tomli_loads                | 2.12 sec                                               | 1.87 sec: 1.13x faster                                              |
| pylint                     | 312 ms                                                 | 281 ms: 1.11x faster                                                |
| xml_etree_parse            | 154 ms                                                 | 139 ms: 1.11x faster                                                |
| go                         | 141 ms                                                 | 129 ms: 1.09x faster                                                |
| sqlite_synth               | 2.90 us                                                | 2.70 us: 1.07x faster                                               |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.68 ms: 1.07x faster                                               |
| regex_effbot               | 3.77 ms                                                | 3.51 ms: 1.07x faster                                               |
| xml_etree_generate         | 86.8 ms                                                | 81.0 ms: 1.07x faster                                               |
| dulwich_log                | 64.6 ms                                                | 60.7 ms: 1.06x faster                                               |
| xml_etree_process          | 60.5 ms                                                | 57.1 ms: 1.06x faster                                               |
| telco                      | 8.40 ms                                                | 7.95 ms: 1.06x faster                                               |
| genshi_text                | 22.6 ms                                                | 21.5 ms: 1.05x faster                                               |
| pyflate                    | 470 ms                                                 | 448 ms: 1.05x faster                                                |
| deltablue                  | 3.19 ms                                                | 3.06 ms: 1.04x faster                                               |
| pathlib                    | 17.4 ms                                                | 16.7 ms: 1.04x faster                                               |
| xml_etree_iterparse        | 101 ms                                                 | 97.5 ms: 1.04x faster                                               |
| async_generators           | 433 ms                                                 | 417 ms: 1.04x faster                                                |
| scimark_sor                | 122 ms                                                 | 119 ms: 1.03x faster                                                |
| regex_compile              | 132 ms                                                 | 128 ms: 1.03x faster                                                |
| thrift                     | 800 us                                                 | 781 us: 1.02x faster                                                |
| k_core                     | 2.37 sec                                               | 2.33 sec: 1.02x faster                                              |
| gc_traversal               | 4.90 ms                                                | 4.81 ms: 1.02x faster                                               |
| html5lib                   | 63.4 ms                                                | 62.3 ms: 1.02x faster                                               |
| bpe_tokeniser              | 4.69 sec                                               | 4.61 sec: 1.02x faster                                              |
| logging_silent             | 101 ns                                                 | 99.5 ns: 1.02x faster                                               |
| nbody                      | 87.7 ms                                                | 86.8 ms: 1.01x faster                                               |
| genshi_xml                 | 50.5 ms                                                | 50.1 ms: 1.01x faster                                               |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                                |
| generators                 | 28.8 ms                                                | 28.6 ms: 1.00x faster                                               |
| 2to3                       | 266 ms                                                 | 265 ms: 1.00x faster                                                |
| asyncio_websockets         | 551 ms                                                 | 553 ms: 1.00x slower                                                |
| sqlalchemy_declarative     | 133 ms                                                 | 134 ms: 1.01x slower                                                |
| shortest_path              | 487 ms                                                 | 491 ms: 1.01x slower                                                |
| django_template            | 31.7 ms                                                | 32.0 ms: 1.01x slower                                               |
| sympy_str                  | 273 ms                                                 | 276 ms: 1.01x slower                                                |
| create_gc_cycles           | 2.45 ms                                                | 2.48 ms: 1.01x slower                                               |
| sympy_integrate            | 19.8 ms                                                | 20.1 ms: 1.02x slower                                               |
| connected_components       | 447 ms                                                 | 455 ms: 1.02x slower                                                |
| raytrace                   | 262 ms                                                 | 268 ms: 1.02x slower                                                |
| sympy_sum                  | 150 ms                                                 | 154 ms: 1.02x slower                                                |
| coverage                   | 82.8 ms                                                | 85.0 ms: 1.03x slower                                               |
| sqlalchemy_imperative      | 16.9 ms                                                | 17.4 ms: 1.03x slower                                               |
| scimark_lu                 | 114 ms                                                 | 117 ms: 1.03x slower                                                |
| scimark_monte_carlo        | 66.8 ms                                                | 68.8 ms: 1.03x slower                                               |
| mako                       | 10.7 ms                                                | 11.0 ms: 1.03x slower                                               |
| python_startup             | 12.7 ms                                                | 13.1 ms: 1.04x slower                                               |
| chaos                      | 58.0 ms                                                | 60.1 ms: 1.04x slower                                               |
| sympy_expand               | 456 ms                                                 | 474 ms: 1.04x slower                                                |
| typing_runtime_protocols   | 160 us                                                 | 168 us: 1.05x slower                                                |
| docutils                   | 2.58 sec                                               | 2.72 sec: 1.05x slower                                              |
| crypto_pyaes               | 74.7 ms                                                | 79.0 ms: 1.06x slower                                               |
| pprint_pformat             | 1.48 sec                                               | 1.57 sec: 1.06x slower                                              |
| pprint_safe_repr           | 727 ms                                                 | 773 ms: 1.06x slower                                                |
| fannkuch                   | 394 ms                                                 | 422 ms: 1.07x slower                                                |
| nqueens                    | 80.9 ms                                                | 87.1 ms: 1.08x slower                                               |
| bench_thread_pool          | 818 us                                                 | 883 us: 1.08x slower                                                |
| pickle_pure_python         | 302 us                                                 | 330 us: 1.09x slower                                                |
| coroutines                 | 22.2 ms                                                | 24.6 ms: 1.11x slower                                               |
| json_loads                 | 27.2 us                                                | 30.0 us: 1.11x slower                                               |
| hexiom                     | 6.08 ms                                                | 6.83 ms: 1.12x slower                                               |
| comprehensions             | 16.5 us                                                | 18.7 us: 1.14x slower                                               |
| many_optionals             | 857 us                                                 | 980 us: 1.14x slower                                                |
| json_dumps                 | 10.1 ms                                                | 11.6 ms: 1.14x slower                                               |
| python_startup_no_site     | 7.00 ms                                                | 8.19 ms: 1.17x slower                                               |
| subparsers                 | 15.5 ms                                                | 21.0 ms: 1.36x slower                                               |
| bench_mp_pool              | 24.0 ms                                                | 82.8 ms: 3.45x slower                                               |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                        |

Benchmark hidden because not significant (9): mdp, meteor_contest, logging_simple, regex_dna, pycparser, json, logging_format, unpickle_pure_python, sphinx
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250327-3.14.0a6+-4df91f6-JIT/bm-20250327-linux-x86_64-brandtbucher-jit_up_12_9-3.14.0a6+-4df91f6.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.037x faster

# HPT report

- Reliability score: 95.68% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.05x