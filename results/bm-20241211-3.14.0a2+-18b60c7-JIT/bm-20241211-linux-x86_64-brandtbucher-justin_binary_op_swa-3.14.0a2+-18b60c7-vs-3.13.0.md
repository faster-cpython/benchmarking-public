# Results vs. 3.13.0

- fork: brandtbucher
- ref: justin_binary_op_swa
- machine: linux-x86_64
- commit hash: 18b60c7
- commit date: 2024-12-11
- overall geometric mean: 1.028x faster
- HPT reliability: 97.57%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241211-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a2+-18b60c7 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 258 ms: 1.03x faster                                                         |
| docutils       | 2.58 sec                                               | 2.67 sec: 1.03x slower                                                       |
| sphinx         | 1.03 sec                                               | 1.05 sec: 1.01x slower                                                       |
| Geometric mean | (ref)                                                  | 1.00x slower                                                                 |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241211-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a2+-18b60c7 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 318 ms: 1.45x faster                                                         |
| async_tree_io_tg           | 861 ms                                                 | 619 ms: 1.39x faster                                                         |
| async_tree_io              | 838 ms                                                 | 625 ms: 1.34x faster                                                         |
| async_tree_none            | 350 ms                                                 | 272 ms: 1.29x faster                                                         |
| async_tree_memoization     | 437 ms                                                 | 343 ms: 1.27x faster                                                         |
| async_tree_none_tg         | 319 ms                                                 | 256 ms: 1.25x faster                                                         |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 502 ms: 1.14x faster                                                         |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 487 ms: 1.12x faster                                                         |
| asyncio_websockets         | 551 ms                                                 | 554 ms: 1.00x slower                                                         |
| async_generators           | 433 ms                                                 | 445 ms: 1.03x slower                                                         |
| coroutines                 | 22.2 ms                                                | 23.3 ms: 1.05x slower                                                        |
| Geometric mean             | (ref)                                                  | 1.19x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241211-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a2+-18b60c7 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 77.2 ms: 1.02x faster                                                        |
| pidigits       | 186 ms                                                 | 187 ms: 1.00x slower                                                         |
| nbody          | 87.7 ms                                                | 93.8 ms: 1.07x slower                                                        |
| Geometric mean | (ref)                                                  | 1.02x slower                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241211-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a2+-18b60c7 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.19 ms: 1.18x faster                                                        |
| regex_v8       | 26.9 ms                                                | 24.6 ms: 1.09x faster                                                        |
| regex_dna      | 220 ms                                                 | 211 ms: 1.04x faster                                                         |
| regex_compile  | 132 ms                                                 | 130 ms: 1.02x faster                                                         |
| Geometric mean | (ref)                                                  | 1.08x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241211-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a2+-18b60c7 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 138 ms: 1.12x faster                                                         |
| xml_etree_process    | 60.5 ms                                                | 54.6 ms: 1.11x faster                                                        |
| unpickle_pure_python | 213 us                                                 | 194 us: 1.10x faster                                                         |
| tomli_loads          | 2.12 sec                                               | 1.96 sec: 1.08x faster                                                       |
| xml_etree_generate   | 86.8 ms                                                | 81.2 ms: 1.07x faster                                                        |
| xml_etree_iterparse  | 101 ms                                                 | 95.0 ms: 1.07x faster                                                        |
| json_loads           | 27.2 us                                                | 25.9 us: 1.05x faster                                                        |
| pickle_pure_python   | 302 us                                                 | 320 us: 1.06x slower                                                         |
| json_dumps           | 10.1 ms                                                | 11.1 ms: 1.10x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241211-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a2+-18b60c7 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 7.00 ms                                                | 7.08 ms: 1.01x slower                                                        |
| python_startup         | 12.7 ms                                                | 12.8 ms: 1.01x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241211-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a2+-18b60c7 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 10.7 ms                                                | 10.2 ms: 1.04x faster                                                        |
| genshi_text     | 22.6 ms                                                | 23.9 ms: 1.06x slower                                                        |
| django_template | 31.7 ms                                                | 33.9 ms: 1.07x slower                                                        |
| genshi_xml      | 50.5 ms                                                | 56.3 ms: 1.11x slower                                                        |
| Geometric mean  | (ref)                                                  | 1.05x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241211-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a2+-18b60c7 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 318 ms: 1.45x faster                                                         |
| async_tree_io_tg           | 861 ms                                                 | 619 ms: 1.39x faster                                                         |
| async_tree_io              | 838 ms                                                 | 625 ms: 1.34x faster                                                         |
| deepcopy                   | 354 us                                                 | 267 us: 1.33x faster                                                         |
| deepcopy_memo              | 38.4 us                                                | 29.2 us: 1.32x faster                                                        |
| richards                   | 47.5 ms                                                | 36.9 ms: 1.29x faster                                                        |
| async_tree_none            | 350 ms                                                 | 272 ms: 1.29x faster                                                         |
| async_tree_memoization     | 437 ms                                                 | 343 ms: 1.27x faster                                                         |
| async_tree_none_tg         | 319 ms                                                 | 256 ms: 1.25x faster                                                         |
| richards_super             | 53.7 ms                                                | 43.8 ms: 1.23x faster                                                        |
| deepcopy_reduce            | 3.24 us                                                | 2.70 us: 1.20x faster                                                        |
| regex_effbot               | 3.77 ms                                                | 3.19 ms: 1.18x faster                                                        |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 502 ms: 1.14x faster                                                         |
| xml_etree_parse            | 154 ms                                                 | 138 ms: 1.12x faster                                                         |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 487 ms: 1.12x faster                                                         |
| json                       | 5.32 ms                                                | 4.80 ms: 1.11x faster                                                        |
| xml_etree_process          | 60.5 ms                                                | 54.6 ms: 1.11x faster                                                        |
| telco                      | 8.40 ms                                                | 7.66 ms: 1.10x faster                                                        |
| unpickle_pure_python       | 213 us                                                 | 194 us: 1.10x faster                                                         |
| regex_v8                   | 26.9 ms                                                | 24.6 ms: 1.09x faster                                                        |
| tomli_loads                | 2.12 sec                                               | 1.96 sec: 1.08x faster                                                       |
| pylint                     | 312 ms                                                 | 290 ms: 1.07x faster                                                         |
| xml_etree_generate         | 86.8 ms                                                | 81.2 ms: 1.07x faster                                                        |
| scimark_fft                | 367 ms                                                 | 343 ms: 1.07x faster                                                         |
| pathlib                    | 17.4 ms                                                | 16.3 ms: 1.07x faster                                                        |
| xml_etree_iterparse        | 101 ms                                                 | 95.0 ms: 1.07x faster                                                        |
| bpe_tokeniser              | 4.69 sec                                               | 4.40 sec: 1.07x faster                                                       |
| crypto_pyaes               | 74.7 ms                                                | 70.8 ms: 1.06x faster                                                        |
| json_loads                 | 27.2 us                                                | 25.9 us: 1.05x faster                                                        |
| go                         | 141 ms                                                 | 134 ms: 1.05x faster                                                         |
| mako                       | 10.7 ms                                                | 10.2 ms: 1.04x faster                                                        |
| sqlite_synth               | 2.90 us                                                | 2.79 us: 1.04x faster                                                        |
| regex_dna                  | 220 ms                                                 | 211 ms: 1.04x faster                                                         |
| scimark_sor                | 122 ms                                                 | 118 ms: 1.03x faster                                                         |
| 2to3                       | 266 ms                                                 | 258 ms: 1.03x faster                                                         |
| thrift                     | 800 us                                                 | 777 us: 1.03x faster                                                         |
| scimark_lu                 | 114 ms                                                 | 111 ms: 1.03x faster                                                         |
| k_core                     | 2.37 sec                                               | 2.31 sec: 1.03x faster                                                       |
| connected_components       | 447 ms                                                 | 436 ms: 1.03x faster                                                         |
| sqlalchemy_declarative     | 133 ms                                                 | 130 ms: 1.03x faster                                                         |
| fannkuch                   | 394 ms                                                 | 386 ms: 1.02x faster                                                         |
| pprint_safe_repr           | 727 ms                                                 | 712 ms: 1.02x faster                                                         |
| float                      | 78.7 ms                                                | 77.2 ms: 1.02x faster                                                        |
| scimark_monte_carlo        | 66.8 ms                                                | 65.6 ms: 1.02x faster                                                        |
| pyflate                    | 470 ms                                                 | 462 ms: 1.02x faster                                                         |
| regex_compile              | 132 ms                                                 | 130 ms: 1.02x faster                                                         |
| shortest_path              | 487 ms                                                 | 479 ms: 1.02x faster                                                         |
| sqlalchemy_imperative      | 16.9 ms                                                | 16.8 ms: 1.01x faster                                                        |
| logging_format             | 6.23 us                                                | 6.19 us: 1.01x faster                                                        |
| pidigits                   | 186 ms                                                 | 187 ms: 1.00x slower                                                         |
| asyncio_websockets         | 551 ms                                                 | 554 ms: 1.00x slower                                                         |
| create_gc_cycles           | 2.45 ms                                                | 2.47 ms: 1.01x slower                                                        |
| mdp                        | 2.54 sec                                               | 2.57 sec: 1.01x slower                                                       |
| python_startup_no_site     | 7.00 ms                                                | 7.08 ms: 1.01x slower                                                        |
| gc_traversal               | 4.90 ms                                                | 4.95 ms: 1.01x slower                                                        |
| python_startup             | 12.7 ms                                                | 12.8 ms: 1.01x slower                                                        |
| sphinx                     | 1.03 sec                                               | 1.05 sec: 1.01x slower                                                       |
| coverage                   | 82.8 ms                                                | 84.3 ms: 1.02x slower                                                        |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 5.13 ms: 1.02x slower                                                        |
| djangocms                  | 22.3 us                                                | 22.8 us: 1.02x slower                                                        |
| sqlglot_normalize          | 108 ms                                                 | 111 ms: 1.03x slower                                                         |
| async_generators           | 433 ms                                                 | 445 ms: 1.03x slower                                                         |
| docutils                   | 2.58 sec                                               | 2.67 sec: 1.03x slower                                                       |
| sympy_str                  | 273 ms                                                 | 283 ms: 1.04x slower                                                         |
| sqlglot_optimize           | 53.4 ms                                                | 55.4 ms: 1.04x slower                                                        |
| sympy_sum                  | 150 ms                                                 | 156 ms: 1.04x slower                                                         |
| spectral_norm              | 113 ms                                                 | 118 ms: 1.04x slower                                                         |
| sympy_expand               | 456 ms                                                 | 476 ms: 1.04x slower                                                         |
| dulwich_log                | 64.6 ms                                                | 67.6 ms: 1.05x slower                                                        |
| comprehensions             | 16.5 us                                                | 17.3 us: 1.05x slower                                                        |
| sqlglot_transpile          | 1.57 ms                                                | 1.65 ms: 1.05x slower                                                        |
| sympy_integrate            | 19.8 ms                                                | 20.8 ms: 1.05x slower                                                        |
| coroutines                 | 22.2 ms                                                | 23.3 ms: 1.05x slower                                                        |
| sqlglot_parse              | 1.26 ms                                                | 1.33 ms: 1.05x slower                                                        |
| genshi_text                | 22.6 ms                                                | 23.9 ms: 1.06x slower                                                        |
| pickle_pure_python         | 302 us                                                 | 320 us: 1.06x slower                                                         |
| typing_runtime_protocols   | 160 us                                                 | 170 us: 1.06x slower                                                         |
| nbody                      | 87.7 ms                                                | 93.8 ms: 1.07x slower                                                        |
| django_template            | 31.7 ms                                                | 33.9 ms: 1.07x slower                                                        |
| bench_thread_pool          | 818 us                                                 | 878 us: 1.07x slower                                                         |
| chaos                      | 58.0 ms                                                | 63.7 ms: 1.10x slower                                                        |
| json_dumps                 | 10.1 ms                                                | 11.1 ms: 1.10x slower                                                        |
| raytrace                   | 262 ms                                                 | 291 ms: 1.11x slower                                                         |
| genshi_xml                 | 50.5 ms                                                | 56.3 ms: 1.11x slower                                                        |
| nqueens                    | 80.9 ms                                                | 91.1 ms: 1.13x slower                                                        |
| many_optionals             | 857 us                                                 | 971 us: 1.13x slower                                                         |
| hexiom                     | 6.08 ms                                                | 7.07 ms: 1.16x slower                                                        |
| generators                 | 28.8 ms                                                | 36.3 ms: 1.26x slower                                                        |
| subparsers                 | 15.5 ms                                                | 20.7 ms: 1.34x slower                                                        |
| bench_mp_pool              | 24.0 ms                                                | 81.3 ms: 3.39x slower                                                        |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                                 |

Benchmark hidden because not significant (7): pycparser, pprint_pformat, html5lib, deltablue, meteor_contest, logging_silent, logging_simple
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (1) of results/bm-20241211-3.14.0a2+-18b60c7-JIT/bm-20241211-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a2+-18b60c7.json: mypy2

- Geometric mean (including insignificant results): 1.028x faster

# HPT report

- Reliability score: 97.57% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.04x