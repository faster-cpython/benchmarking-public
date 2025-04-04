# Results vs. 3.13.0

- fork: brandtbucher
- ref: negative_subscr
- machine: linux-x86_64
- commit hash: 6a93886
- commit date: 2025-04-03
- overall geometric mean: 1.055x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250403-linux-x86_64-brandtbucher-negative_subscr-3.14.0a6+-6a93886 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 249 ms: 1.07x faster                                                    |
| docutils       | 2.58 sec                                               | 2.60 sec: 1.00x slower                                                  |
| html5lib       | 63.4 ms                                                | 60.6 ms: 1.05x faster                                                   |
| sphinx         | 1.03 sec                                               | 1.01 sec: 1.02x faster                                                  |
| Geometric mean | (ref)                                                  | 1.03x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250403-linux-x86_64-brandtbucher-negative_subscr-3.14.0a6+-6a93886 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 317 ms: 1.46x faster                                                    |
| async_tree_io_tg           | 861 ms                                                 | 614 ms: 1.40x faster                                                    |
| async_tree_memoization     | 437 ms                                                 | 314 ms: 1.39x faster                                                    |
| async_tree_io              | 838 ms                                                 | 616 ms: 1.36x faster                                                    |
| async_tree_none            | 350 ms                                                 | 262 ms: 1.34x faster                                                    |
| async_tree_none_tg         | 319 ms                                                 | 251 ms: 1.27x faster                                                    |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 490 ms: 1.17x faster                                                    |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 477 ms: 1.14x faster                                                    |
| async_generators           | 433 ms                                                 | 398 ms: 1.09x faster                                                    |
| coroutines                 | 22.2 ms                                                | 23.4 ms: 1.05x slower                                                   |
| Geometric mean             | (ref)                                                  | 1.22x faster                                                            |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250403-linux-x86_64-brandtbucher-negative_subscr-3.14.0a6+-6a93886 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 69.1 ms: 1.14x faster                                                   |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                    |
| nbody          | 87.7 ms                                                | 93.9 ms: 1.07x slower                                                   |
| Geometric mean | (ref)                                                  | 1.02x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250403-linux-x86_64-brandtbucher-negative_subscr-3.14.0a6+-6a93886 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 26.9 ms                                                | 23.0 ms: 1.17x faster                                                   |
| regex_effbot   | 3.77 ms                                                | 3.31 ms: 1.14x faster                                                   |
| regex_compile  | 132 ms                                                 | 126 ms: 1.05x faster                                                    |
| Geometric mean | (ref)                                                  | 1.09x faster                                                            |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250403-linux-x86_64-brandtbucher-negative_subscr-3.14.0a6+-6a93886 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.92 sec: 1.10x faster                                                  |
| xml_etree_parse      | 154 ms                                                 | 141 ms: 1.09x faster                                                    |
| xml_etree_generate   | 86.8 ms                                                | 83.6 ms: 1.04x faster                                                   |
| xml_etree_process    | 60.5 ms                                                | 58.5 ms: 1.03x faster                                                   |
| xml_etree_iterparse  | 101 ms                                                 | 99.1 ms: 1.02x faster                                                   |
| unpickle_pure_python | 213 us                                                 | 214 us: 1.01x slower                                                    |
| pickle_pure_python   | 302 us                                                 | 319 us: 1.06x slower                                                    |
| json_loads           | 27.2 us                                                | 29.8 us: 1.10x slower                                                   |
| json_dumps           | 10.1 ms                                                | 11.4 ms: 1.13x slower                                                   |
| Geometric mean       | (ref)                                                  | 1.00x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250403-linux-x86_64-brandtbucher-negative_subscr-3.14.0a6+-6a93886 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 13.1 ms: 1.04x slower                                                   |
| python_startup_no_site | 7.00 ms                                                | 8.18 ms: 1.17x slower                                                   |
| Geometric mean         | (ref)                                                  | 1.10x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250403-linux-x86_64-brandtbucher-negative_subscr-3.14.0a6+-6a93886 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.5 ms: 1.05x faster                                                   |
| genshi_xml      | 50.5 ms                                                | 49.0 ms: 1.03x faster                                                   |
| django_template | 31.7 ms                                                | 31.9 ms: 1.01x slower                                                   |
| mako            | 10.7 ms                                                | 11.4 ms: 1.07x slower                                                   |
| Geometric mean  | (ref)                                                  | 1.00x faster                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250403-linux-x86_64-brandtbucher-negative_subscr-3.14.0a6+-6a93886 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.22 sec: 2.08x faster                                                  |
| async_tree_memoization_tg  | 463 ms                                                 | 317 ms: 1.46x faster                                                    |
| deepcopy                   | 354 us                                                 | 251 us: 1.41x faster                                                    |
| async_tree_io_tg           | 861 ms                                                 | 614 ms: 1.40x faster                                                    |
| async_tree_memoization     | 437 ms                                                 | 314 ms: 1.39x faster                                                    |
| async_tree_io              | 838 ms                                                 | 616 ms: 1.36x faster                                                    |
| async_tree_none            | 350 ms                                                 | 262 ms: 1.34x faster                                                    |
| deepcopy_memo              | 38.4 us                                                | 28.9 us: 1.33x faster                                                   |
| async_tree_none_tg         | 319 ms                                                 | 251 ms: 1.27x faster                                                    |
| go                         | 141 ms                                                 | 112 ms: 1.25x faster                                                    |
| deepcopy_reduce            | 3.24 us                                                | 2.61 us: 1.24x faster                                                   |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 490 ms: 1.17x faster                                                    |
| regex_v8                   | 26.9 ms                                                | 23.0 ms: 1.17x faster                                                   |
| spectral_norm              | 113 ms                                                 | 98.7 ms: 1.15x faster                                                   |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 477 ms: 1.14x faster                                                    |
| float                      | 78.7 ms                                                | 69.1 ms: 1.14x faster                                                   |
| regex_effbot               | 3.77 ms                                                | 3.31 ms: 1.14x faster                                                   |
| pylint                     | 312 ms                                                 | 279 ms: 1.12x faster                                                    |
| richards                   | 47.5 ms                                                | 42.9 ms: 1.11x faster                                                   |
| dulwich_log                | 64.6 ms                                                | 58.6 ms: 1.10x faster                                                   |
| tomli_loads                | 2.12 sec                                               | 1.92 sec: 1.10x faster                                                  |
| richards_super             | 53.7 ms                                                | 49.2 ms: 1.09x faster                                                   |
| xml_etree_parse            | 154 ms                                                 | 141 ms: 1.09x faster                                                    |
| async_generators           | 433 ms                                                 | 398 ms: 1.09x faster                                                    |
| scimark_fft                | 367 ms                                                 | 339 ms: 1.08x faster                                                    |
| telco                      | 8.40 ms                                                | 7.87 ms: 1.07x faster                                                   |
| 2to3                       | 266 ms                                                 | 249 ms: 1.07x faster                                                    |
| scimark_sor                | 122 ms                                                 | 116 ms: 1.05x faster                                                    |
| sqlite_synth               | 2.90 us                                                | 2.75 us: 1.05x faster                                                   |
| pathlib                    | 17.4 ms                                                | 16.5 ms: 1.05x faster                                                   |
| regex_compile              | 132 ms                                                 | 126 ms: 1.05x faster                                                    |
| genshi_text                | 22.6 ms                                                | 21.5 ms: 1.05x faster                                                   |
| html5lib                   | 63.4 ms                                                | 60.6 ms: 1.05x faster                                                   |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.81 ms: 1.05x faster                                                   |
| xml_etree_generate         | 86.8 ms                                                | 83.6 ms: 1.04x faster                                                   |
| pycparser                  | 1.20 sec                                               | 1.16 sec: 1.04x faster                                                  |
| pyflate                    | 470 ms                                                 | 453 ms: 1.04x faster                                                    |
| bpe_tokeniser              | 4.69 sec                                               | 4.53 sec: 1.04x faster                                                  |
| k_core                     | 2.37 sec                                               | 2.29 sec: 1.04x faster                                                  |
| xml_etree_process          | 60.5 ms                                                | 58.5 ms: 1.03x faster                                                   |
| sympy_integrate            | 19.8 ms                                                | 19.2 ms: 1.03x faster                                                   |
| genshi_xml                 | 50.5 ms                                                | 49.0 ms: 1.03x faster                                                   |
| logging_silent             | 101 ns                                                 | 98.3 ns: 1.03x faster                                                   |
| meteor_contest             | 108 ms                                                 | 106 ms: 1.02x faster                                                    |
| logging_simple             | 5.65 us                                                | 5.53 us: 1.02x faster                                                   |
| crypto_pyaes               | 74.7 ms                                                | 73.1 ms: 1.02x faster                                                   |
| xml_etree_iterparse        | 101 ms                                                 | 99.1 ms: 1.02x faster                                                   |
| chaos                      | 58.0 ms                                                | 56.8 ms: 1.02x faster                                                   |
| sphinx                     | 1.03 sec                                               | 1.01 sec: 1.02x faster                                                  |
| sympy_str                  | 273 ms                                                 | 268 ms: 1.02x faster                                                    |
| scimark_monte_carlo        | 66.8 ms                                                | 65.8 ms: 1.01x faster                                                   |
| logging_format             | 6.23 us                                                | 6.15 us: 1.01x faster                                                   |
| raytrace                   | 262 ms                                                 | 259 ms: 1.01x faster                                                    |
| sqlalchemy_declarative     | 133 ms                                                 | 131 ms: 1.01x faster                                                    |
| pprint_safe_repr           | 727 ms                                                 | 722 ms: 1.01x faster                                                    |
| pprint_pformat             | 1.48 sec                                               | 1.47 sec: 1.01x faster                                                  |
| sympy_sum                  | 150 ms                                                 | 150 ms: 1.00x faster                                                    |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                                    |
| docutils                   | 2.58 sec                                               | 2.60 sec: 1.00x slower                                                  |
| sympy_expand               | 456 ms                                                 | 458 ms: 1.00x slower                                                    |
| unpickle_pure_python       | 213 us                                                 | 214 us: 1.01x slower                                                    |
| django_template            | 31.7 ms                                                | 31.9 ms: 1.01x slower                                                   |
| sqlalchemy_imperative      | 16.9 ms                                                | 17.1 ms: 1.01x slower                                                   |
| comprehensions             | 16.5 us                                                | 16.6 us: 1.01x slower                                                   |
| nqueens                    | 80.9 ms                                                | 81.9 ms: 1.01x slower                                                   |
| shortest_path              | 487 ms                                                 | 493 ms: 1.01x slower                                                    |
| create_gc_cycles           | 2.45 ms                                                | 2.48 ms: 1.01x slower                                                   |
| scimark_lu                 | 114 ms                                                 | 116 ms: 1.01x slower                                                    |
| typing_runtime_protocols   | 160 us                                                 | 163 us: 1.02x slower                                                    |
| hexiom                     | 6.08 ms                                                | 6.24 ms: 1.03x slower                                                   |
| coverage                   | 82.8 ms                                                | 85.6 ms: 1.03x slower                                                   |
| gc_traversal               | 4.90 ms                                                | 5.07 ms: 1.03x slower                                                   |
| python_startup             | 12.7 ms                                                | 13.1 ms: 1.04x slower                                                   |
| deltablue                  | 3.19 ms                                                | 3.34 ms: 1.05x slower                                                   |
| fannkuch                   | 394 ms                                                 | 413 ms: 1.05x slower                                                    |
| coroutines                 | 22.2 ms                                                | 23.4 ms: 1.05x slower                                                   |
| pickle_pure_python         | 302 us                                                 | 319 us: 1.06x slower                                                    |
| mako                       | 10.7 ms                                                | 11.4 ms: 1.07x slower                                                   |
| generators                 | 28.8 ms                                                | 30.7 ms: 1.07x slower                                                   |
| nbody                      | 87.7 ms                                                | 93.9 ms: 1.07x slower                                                   |
| bench_thread_pool          | 818 us                                                 | 883 us: 1.08x slower                                                    |
| many_optionals             | 857 us                                                 | 931 us: 1.09x slower                                                    |
| json_loads                 | 27.2 us                                                | 29.8 us: 1.10x slower                                                   |
| json_dumps                 | 10.1 ms                                                | 11.4 ms: 1.13x slower                                                   |
| python_startup_no_site     | 7.00 ms                                                | 8.18 ms: 1.17x slower                                                   |
| subparsers                 | 15.5 ms                                                | 20.7 ms: 1.34x slower                                                   |
| bench_mp_pool              | 24.0 ms                                                | 83.2 ms: 3.47x slower                                                   |
| Geometric mean             | (ref)                                                  | 1.04x faster                                                            |

Benchmark hidden because not significant (4): regex_dna, asyncio_websockets, connected_components, json
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (4) of results/bm-20250403-3.14.0a6+-6a93886/bm-20250403-linux-x86_64-brandtbucher-negative_subscr-3.14.0a6+-6a93886.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.055x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.04x