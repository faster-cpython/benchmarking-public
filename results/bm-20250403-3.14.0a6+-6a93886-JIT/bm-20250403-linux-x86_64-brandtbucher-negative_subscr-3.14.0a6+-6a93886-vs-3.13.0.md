# Results vs. 3.13.0

- fork: brandtbucher
- ref: negative_subscr
- machine: linux-x86_64
- commit hash: 6a93886
- commit date: 2025-04-03
- overall geometric mean: 1.062x faster
- HPT reliability: 99.91%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250403-linux-x86_64-brandtbucher-negative_subscr-3.14.0a6+-6a93886 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 254 ms: 1.05x faster                                                    |
| docutils       | 2.58 sec                                               | 2.67 sec: 1.03x slower                                                  |
| html5lib       | 63.4 ms                                                | 61.0 ms: 1.04x faster                                                   |
| Geometric mean | (ref)                                                  | 1.01x faster                                                            |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250403-linux-x86_64-brandtbucher-negative_subscr-3.14.0a6+-6a93886 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 314 ms: 1.47x faster                                                    |
| async_tree_memoization     | 437 ms                                                 | 311 ms: 1.41x faster                                                    |
| async_tree_io_tg           | 861 ms                                                 | 616 ms: 1.40x faster                                                    |
| async_tree_io              | 838 ms                                                 | 615 ms: 1.36x faster                                                    |
| async_tree_none            | 350 ms                                                 | 259 ms: 1.35x faster                                                    |
| async_tree_none_tg         | 319 ms                                                 | 247 ms: 1.29x faster                                                    |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 488 ms: 1.17x faster                                                    |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 473 ms: 1.15x faster                                                    |
| async_generators           | 433 ms                                                 | 410 ms: 1.06x faster                                                    |
| asyncio_websockets         | 551 ms                                                 | 554 ms: 1.00x slower                                                    |
| coroutines                 | 22.2 ms                                                | 23.7 ms: 1.07x slower                                                   |
| Geometric mean             | (ref)                                                  | 1.22x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250403-linux-x86_64-brandtbucher-negative_subscr-3.14.0a6+-6a93886 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 62.0 ms: 1.27x faster                                                   |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                    |
| nbody          | 87.7 ms                                                | 89.7 ms: 1.02x slower                                                   |
| Geometric mean | (ref)                                                  | 1.08x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250403-linux-x86_64-brandtbucher-negative_subscr-3.14.0a6+-6a93886 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.26 ms: 1.15x faster                                                   |
| regex_v8       | 26.9 ms                                                | 24.0 ms: 1.12x faster                                                   |
| regex_compile  | 132 ms                                                 | 126 ms: 1.05x faster                                                    |
| regex_dna      | 220 ms                                                 | 210 ms: 1.05x faster                                                    |
| Geometric mean | (ref)                                                  | 1.09x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250403-linux-x86_64-brandtbucher-negative_subscr-3.14.0a6+-6a93886 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.84 sec: 1.15x faster                                                  |
| xml_etree_parse      | 154 ms                                                 | 139 ms: 1.11x faster                                                    |
| xml_etree_generate   | 86.8 ms                                                | 79.4 ms: 1.09x faster                                                   |
| xml_etree_process    | 60.5 ms                                                | 56.4 ms: 1.07x faster                                                   |
| unpickle_pure_python | 213 us                                                 | 206 us: 1.03x faster                                                    |
| xml_etree_iterparse  | 101 ms                                                 | 98.0 ms: 1.03x faster                                                   |
| pickle_pure_python   | 302 us                                                 | 317 us: 1.05x slower                                                    |
| json_loads           | 27.2 us                                                | 29.8 us: 1.10x slower                                                   |
| json_dumps           | 10.1 ms                                                | 11.5 ms: 1.14x slower                                                   |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250403-linux-x86_64-brandtbucher-negative_subscr-3.14.0a6+-6a93886 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 13.2 ms: 1.04x slower                                                   |
| python_startup_no_site | 7.00 ms                                                | 8.23 ms: 1.18x slower                                                   |
| Geometric mean         | (ref)                                                  | 1.11x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250403-linux-x86_64-brandtbucher-negative_subscr-3.14.0a6+-6a93886 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.1 ms: 1.07x faster                                                   |
| genshi_xml      | 50.5 ms                                                | 48.8 ms: 1.04x faster                                                   |
| django_template | 31.7 ms                                                | 32.2 ms: 1.02x slower                                                   |
| mako            | 10.7 ms                                                | 11.0 ms: 1.03x slower                                                   |
| Geometric mean  | (ref)                                                  | 1.02x faster                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250403-linux-x86_64-brandtbucher-negative_subscr-3.14.0a6+-6a93886 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.22 sec: 2.09x faster                                                  |
| async_tree_memoization_tg  | 463 ms                                                 | 314 ms: 1.47x faster                                                    |
| async_tree_memoization     | 437 ms                                                 | 311 ms: 1.41x faster                                                    |
| deepcopy                   | 354 us                                                 | 252 us: 1.40x faster                                                    |
| async_tree_io_tg           | 861 ms                                                 | 616 ms: 1.40x faster                                                    |
| richards                   | 47.5 ms                                                | 34.7 ms: 1.37x faster                                                   |
| async_tree_io              | 838 ms                                                 | 615 ms: 1.36x faster                                                    |
| async_tree_none            | 350 ms                                                 | 259 ms: 1.35x faster                                                    |
| richards_super             | 53.7 ms                                                | 39.8 ms: 1.35x faster                                                   |
| deepcopy_memo              | 38.4 us                                                | 29.0 us: 1.32x faster                                                   |
| async_tree_none_tg         | 319 ms                                                 | 247 ms: 1.29x faster                                                    |
| float                      | 78.7 ms                                                | 62.0 ms: 1.27x faster                                                   |
| deepcopy_reduce            | 3.24 us                                                | 2.62 us: 1.24x faster                                                   |
| scimark_fft                | 367 ms                                                 | 307 ms: 1.19x faster                                                    |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 488 ms: 1.17x faster                                                    |
| spectral_norm              | 113 ms                                                 | 96.9 ms: 1.17x faster                                                   |
| regex_effbot               | 3.77 ms                                                | 3.26 ms: 1.15x faster                                                   |
| tomli_loads                | 2.12 sec                                               | 1.84 sec: 1.15x faster                                                  |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 473 ms: 1.15x faster                                                    |
| go                         | 141 ms                                                 | 124 ms: 1.13x faster                                                    |
| pyflate                    | 470 ms                                                 | 416 ms: 1.13x faster                                                    |
| regex_v8                   | 26.9 ms                                                | 24.0 ms: 1.12x faster                                                   |
| pylint                     | 312 ms                                                 | 281 ms: 1.11x faster                                                    |
| xml_etree_parse            | 154 ms                                                 | 139 ms: 1.11x faster                                                    |
| xml_etree_generate         | 86.8 ms                                                | 79.4 ms: 1.09x faster                                                   |
| telco                      | 8.40 ms                                                | 7.82 ms: 1.07x faster                                                   |
| xml_etree_process          | 60.5 ms                                                | 56.4 ms: 1.07x faster                                                   |
| genshi_text                | 22.6 ms                                                | 21.1 ms: 1.07x faster                                                   |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.70 ms: 1.07x faster                                                   |
| dulwich_log                | 64.6 ms                                                | 60.5 ms: 1.07x faster                                                   |
| logging_silent             | 101 ns                                                 | 94.9 ns: 1.06x faster                                                   |
| sqlite_synth               | 2.90 us                                                | 2.74 us: 1.06x faster                                                   |
| async_generators           | 433 ms                                                 | 410 ms: 1.06x faster                                                    |
| deltablue                  | 3.19 ms                                                | 3.03 ms: 1.05x faster                                                   |
| pycparser                  | 1.20 sec                                               | 1.14 sec: 1.05x faster                                                  |
| scimark_sor                | 122 ms                                                 | 117 ms: 1.05x faster                                                    |
| regex_compile              | 132 ms                                                 | 126 ms: 1.05x faster                                                    |
| regex_dna                  | 220 ms                                                 | 210 ms: 1.05x faster                                                    |
| 2to3                       | 266 ms                                                 | 254 ms: 1.05x faster                                                    |
| html5lib                   | 63.4 ms                                                | 61.0 ms: 1.04x faster                                                   |
| bpe_tokeniser              | 4.69 sec                                               | 4.52 sec: 1.04x faster                                                  |
| genshi_xml                 | 50.5 ms                                                | 48.8 ms: 1.04x faster                                                   |
| unpickle_pure_python       | 213 us                                                 | 206 us: 1.03x faster                                                    |
| xml_etree_iterparse        | 101 ms                                                 | 98.0 ms: 1.03x faster                                                   |
| pathlib                    | 17.4 ms                                                | 16.8 ms: 1.03x faster                                                   |
| k_core                     | 2.37 sec                                               | 2.30 sec: 1.03x faster                                                  |
| logging_simple             | 5.65 us                                                | 5.56 us: 1.02x faster                                                   |
| scimark_monte_carlo        | 66.8 ms                                                | 65.8 ms: 1.02x faster                                                   |
| sympy_integrate            | 19.8 ms                                                | 19.6 ms: 1.01x faster                                                   |
| chaos                      | 58.0 ms                                                | 57.7 ms: 1.01x faster                                                   |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                                    |
| gc_traversal               | 4.90 ms                                                | 4.89 ms: 1.00x faster                                                   |
| sympy_sum                  | 150 ms                                                 | 151 ms: 1.00x slower                                                    |
| asyncio_websockets         | 551 ms                                                 | 554 ms: 1.00x slower                                                    |
| crypto_pyaes               | 74.7 ms                                                | 75.0 ms: 1.00x slower                                                   |
| raytrace                   | 262 ms                                                 | 264 ms: 1.01x slower                                                    |
| nqueens                    | 80.9 ms                                                | 81.6 ms: 1.01x slower                                                   |
| django_template            | 31.7 ms                                                | 32.2 ms: 1.02x slower                                                   |
| sqlalchemy_imperative      | 16.9 ms                                                | 17.2 ms: 1.02x slower                                                   |
| create_gc_cycles           | 2.45 ms                                                | 2.50 ms: 1.02x slower                                                   |
| nbody                      | 87.7 ms                                                | 89.7 ms: 1.02x slower                                                   |
| fannkuch                   | 394 ms                                                 | 403 ms: 1.02x slower                                                    |
| mako                       | 10.7 ms                                                | 11.0 ms: 1.03x slower                                                   |
| scimark_lu                 | 114 ms                                                 | 117 ms: 1.03x slower                                                    |
| coverage                   | 82.8 ms                                                | 85.1 ms: 1.03x slower                                                   |
| generators                 | 28.8 ms                                                | 29.6 ms: 1.03x slower                                                   |
| docutils                   | 2.58 sec                                               | 2.67 sec: 1.03x slower                                                  |
| sympy_expand               | 456 ms                                                 | 472 ms: 1.03x slower                                                    |
| python_startup             | 12.7 ms                                                | 13.2 ms: 1.04x slower                                                   |
| typing_runtime_protocols   | 160 us                                                 | 167 us: 1.04x slower                                                    |
| pprint_safe_repr           | 727 ms                                                 | 761 ms: 1.05x slower                                                    |
| pickle_pure_python         | 302 us                                                 | 317 us: 1.05x slower                                                    |
| pprint_pformat             | 1.48 sec                                               | 1.56 sec: 1.05x slower                                                  |
| coroutines                 | 22.2 ms                                                | 23.7 ms: 1.07x slower                                                   |
| bench_thread_pool          | 818 us                                                 | 887 us: 1.09x slower                                                    |
| json_loads                 | 27.2 us                                                | 29.8 us: 1.10x slower                                                   |
| comprehensions             | 16.5 us                                                | 18.2 us: 1.10x slower                                                   |
| many_optionals             | 857 us                                                 | 949 us: 1.11x slower                                                    |
| hexiom                     | 6.08 ms                                                | 6.76 ms: 1.11x slower                                                   |
| json_dumps                 | 10.1 ms                                                | 11.5 ms: 1.14x slower                                                   |
| python_startup_no_site     | 7.00 ms                                                | 8.23 ms: 1.18x slower                                                   |
| subparsers                 | 15.5 ms                                                | 20.9 ms: 1.35x slower                                                   |
| bench_mp_pool              | 24.0 ms                                                | 83.4 ms: 3.48x slower                                                   |
| Geometric mean             | (ref)                                                  | 1.05x faster                                                            |

Benchmark hidden because not significant (8): sphinx, json, sympy_str, logging_format, sqlalchemy_declarative, meteor_contest, shortest_path, connected_components
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (4) of results/bm-20250403-3.14.0a6+-6a93886-JIT/bm-20250403-linux-x86_64-brandtbucher-negative_subscr-3.14.0a6+-6a93886.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.062x faster

# HPT report

- Reliability score: 99.91% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.05x