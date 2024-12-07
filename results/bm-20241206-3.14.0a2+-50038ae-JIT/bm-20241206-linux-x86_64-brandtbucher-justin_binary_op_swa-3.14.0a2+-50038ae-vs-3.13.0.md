# Results vs. 3.13.0

- fork: brandtbucher
- ref: justin_binary_op_swa
- machine: linux-x86_64
- commit hash: 50038ae
- commit date: 2024-12-06
- overall geometric mean: 1.023x faster
- HPT reliability: 97.36%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241206-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a2+-50038ae |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 259 ms: 1.03x faster                                                         |
| docutils       | 2.58 sec                                               | 2.68 sec: 1.04x slower                                                       |
| html5lib       | 63.4 ms                                                | 65.6 ms: 1.04x slower                                                        |
| sphinx         | 1.03 sec                                               | 1.05 sec: 1.02x slower                                                       |
| Geometric mean | (ref)                                                  | 1.02x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241206-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a2+-50038ae |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 319 ms: 1.45x faster                                                         |
| async_tree_io_tg           | 861 ms                                                 | 619 ms: 1.39x faster                                                         |
| async_tree_io              | 838 ms                                                 | 620 ms: 1.35x faster                                                         |
| async_tree_none            | 350 ms                                                 | 272 ms: 1.29x faster                                                         |
| async_tree_memoization     | 437 ms                                                 | 343 ms: 1.27x faster                                                         |
| async_tree_none_tg         | 319 ms                                                 | 256 ms: 1.25x faster                                                         |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 507 ms: 1.13x faster                                                         |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 491 ms: 1.11x faster                                                         |
| asyncio_websockets         | 551 ms                                                 | 553 ms: 1.00x slower                                                         |
| async_generators           | 433 ms                                                 | 451 ms: 1.04x slower                                                         |
| coroutines                 | 22.2 ms                                                | 23.9 ms: 1.08x slower                                                        |
| Geometric mean             | (ref)                                                  | 1.18x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241206-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a2+-50038ae |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 76.8 ms: 1.02x faster                                                        |
| pidigits       | 186 ms                                                 | 187 ms: 1.00x slower                                                         |
| nbody          | 87.7 ms                                                | 94.2 ms: 1.07x slower                                                        |
| Geometric mean | (ref)                                                  | 1.02x slower                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241206-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a2+-50038ae |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.47 ms: 1.08x faster                                                        |
| regex_v8       | 26.9 ms                                                | 25.2 ms: 1.07x faster                                                        |
| regex_dna      | 220 ms                                                 | 217 ms: 1.01x faster                                                         |
| regex_compile  | 132 ms                                                 | 130 ms: 1.01x faster                                                         |
| Geometric mean | (ref)                                                  | 1.04x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241206-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a2+-50038ae |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 138 ms: 1.12x faster                                                         |
| xml_etree_process    | 60.5 ms                                                | 54.9 ms: 1.10x faster                                                        |
| unpickle_pure_python | 213 us                                                 | 197 us: 1.08x faster                                                         |
| tomli_loads          | 2.12 sec                                               | 1.96 sec: 1.08x faster                                                       |
| xml_etree_generate   | 86.8 ms                                                | 80.5 ms: 1.08x faster                                                        |
| xml_etree_iterparse  | 101 ms                                                 | 94.7 ms: 1.07x faster                                                        |
| json_loads           | 27.2 us                                                | 26.1 us: 1.04x faster                                                        |
| pickle_pure_python   | 302 us                                                 | 322 us: 1.07x slower                                                         |
| json_dumps           | 10.1 ms                                                | 11.1 ms: 1.10x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241206-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a2+-50038ae |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 7.00 ms                                                | 7.03 ms: 1.00x slower                                                        |
| python_startup         | 12.7 ms                                                | 12.7 ms: 1.01x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.00x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241206-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a2+-50038ae |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 10.7 ms                                                | 10.1 ms: 1.06x faster                                                        |
| django_template | 31.7 ms                                                | 33.9 ms: 1.07x slower                                                        |
| genshi_text     | 22.6 ms                                                | 24.4 ms: 1.08x slower                                                        |
| genshi_xml      | 50.5 ms                                                | 56.5 ms: 1.12x slower                                                        |
| Geometric mean  | (ref)                                                  | 1.05x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241206-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a2+-50038ae |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 319 ms: 1.45x faster                                                         |
| async_tree_io_tg           | 861 ms                                                 | 619 ms: 1.39x faster                                                         |
| async_tree_io              | 838 ms                                                 | 620 ms: 1.35x faster                                                         |
| deepcopy                   | 354 us                                                 | 269 us: 1.32x faster                                                         |
| deepcopy_memo              | 38.4 us                                                | 29.2 us: 1.31x faster                                                        |
| async_tree_none            | 350 ms                                                 | 272 ms: 1.29x faster                                                         |
| async_tree_memoization     | 437 ms                                                 | 343 ms: 1.27x faster                                                         |
| richards                   | 47.5 ms                                                | 38.0 ms: 1.25x faster                                                        |
| async_tree_none_tg         | 319 ms                                                 | 256 ms: 1.25x faster                                                         |
| richards_super             | 53.7 ms                                                | 44.1 ms: 1.22x faster                                                        |
| deepcopy_reduce            | 3.24 us                                                | 2.72 us: 1.19x faster                                                        |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 507 ms: 1.13x faster                                                         |
| xml_etree_parse            | 154 ms                                                 | 138 ms: 1.12x faster                                                         |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 491 ms: 1.11x faster                                                         |
| xml_etree_process          | 60.5 ms                                                | 54.9 ms: 1.10x faster                                                        |
| telco                      | 8.40 ms                                                | 7.64 ms: 1.10x faster                                                        |
| json                       | 5.32 ms                                                | 4.89 ms: 1.09x faster                                                        |
| pylint                     | 312 ms                                                 | 287 ms: 1.09x faster                                                         |
| regex_effbot               | 3.77 ms                                                | 3.47 ms: 1.08x faster                                                        |
| unpickle_pure_python       | 213 us                                                 | 197 us: 1.08x faster                                                         |
| tomli_loads                | 2.12 sec                                               | 1.96 sec: 1.08x faster                                                       |
| xml_etree_generate         | 86.8 ms                                                | 80.5 ms: 1.08x faster                                                        |
| scimark_fft                | 367 ms                                                 | 341 ms: 1.07x faster                                                         |
| xml_etree_iterparse        | 101 ms                                                 | 94.7 ms: 1.07x faster                                                        |
| regex_v8                   | 26.9 ms                                                | 25.2 ms: 1.07x faster                                                        |
| mako                       | 10.7 ms                                                | 10.1 ms: 1.06x faster                                                        |
| pathlib                    | 17.4 ms                                                | 16.4 ms: 1.06x faster                                                        |
| crypto_pyaes               | 74.7 ms                                                | 70.8 ms: 1.05x faster                                                        |
| bpe_tokeniser              | 4.69 sec                                               | 4.46 sec: 1.05x faster                                                       |
| json_loads                 | 27.2 us                                                | 26.1 us: 1.04x faster                                                        |
| go                         | 141 ms                                                 | 135 ms: 1.04x faster                                                         |
| pycparser                  | 1.20 sec                                               | 1.15 sec: 1.04x faster                                                       |
| sqlalchemy_declarative     | 133 ms                                                 | 129 ms: 1.03x faster                                                         |
| sqlite_synth               | 2.90 us                                                | 2.82 us: 1.03x faster                                                        |
| 2to3                       | 266 ms                                                 | 259 ms: 1.03x faster                                                         |
| thrift                     | 800 us                                                 | 779 us: 1.03x faster                                                         |
| connected_components       | 447 ms                                                 | 437 ms: 1.02x faster                                                         |
| k_core                     | 2.37 sec                                               | 2.31 sec: 1.02x faster                                                       |
| float                      | 78.7 ms                                                | 76.8 ms: 1.02x faster                                                        |
| gc_traversal               | 4.90 ms                                                | 4.80 ms: 1.02x faster                                                        |
| pprint_safe_repr           | 727 ms                                                 | 713 ms: 1.02x faster                                                         |
| pyflate                    | 470 ms                                                 | 461 ms: 1.02x faster                                                         |
| sqlalchemy_imperative      | 16.9 ms                                                | 16.6 ms: 1.02x faster                                                        |
| shortest_path              | 487 ms                                                 | 479 ms: 1.02x faster                                                         |
| regex_dna                  | 220 ms                                                 | 217 ms: 1.01x faster                                                         |
| scimark_monte_carlo        | 66.8 ms                                                | 65.9 ms: 1.01x faster                                                        |
| regex_compile              | 132 ms                                                 | 130 ms: 1.01x faster                                                         |
| scimark_lu                 | 114 ms                                                 | 114 ms: 1.01x faster                                                         |
| asyncio_websockets         | 551 ms                                                 | 553 ms: 1.00x slower                                                         |
| python_startup_no_site     | 7.00 ms                                                | 7.03 ms: 1.00x slower                                                        |
| pidigits                   | 186 ms                                                 | 187 ms: 1.00x slower                                                         |
| python_startup             | 12.7 ms                                                | 12.7 ms: 1.01x slower                                                        |
| create_gc_cycles           | 2.45 ms                                                | 2.46 ms: 1.01x slower                                                        |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 5.07 ms: 1.01x slower                                                        |
| meteor_contest             | 108 ms                                                 | 109 ms: 1.01x slower                                                         |
| mdp                        | 2.54 sec                                               | 2.57 sec: 1.01x slower                                                       |
| sqlglot_normalize          | 108 ms                                                 | 110 ms: 1.02x slower                                                         |
| sphinx                     | 1.03 sec                                               | 1.05 sec: 1.02x slower                                                       |
| logging_format             | 6.23 us                                                | 6.41 us: 1.03x slower                                                        |
| sympy_sum                  | 150 ms                                                 | 156 ms: 1.03x slower                                                         |
| html5lib                   | 63.4 ms                                                | 65.6 ms: 1.04x slower                                                        |
| sympy_str                  | 273 ms                                                 | 283 ms: 1.04x slower                                                         |
| docutils                   | 2.58 sec                                               | 2.68 sec: 1.04x slower                                                       |
| sqlglot_optimize           | 53.4 ms                                                | 55.4 ms: 1.04x slower                                                        |
| sympy_expand               | 456 ms                                                 | 474 ms: 1.04x slower                                                         |
| async_generators           | 433 ms                                                 | 451 ms: 1.04x slower                                                         |
| coverage                   | 82.8 ms                                                | 86.3 ms: 1.04x slower                                                        |
| sqlglot_transpile          | 1.57 ms                                                | 1.64 ms: 1.04x slower                                                        |
| sympy_integrate            | 19.8 ms                                                | 20.7 ms: 1.04x slower                                                        |
| logging_simple             | 5.65 us                                                | 5.92 us: 1.05x slower                                                        |
| comprehensions             | 16.5 us                                                | 17.3 us: 1.05x slower                                                        |
| sqlglot_parse              | 1.26 ms                                                | 1.33 ms: 1.05x slower                                                        |
| dulwich_log                | 64.6 ms                                                | 68.2 ms: 1.06x slower                                                        |
| typing_runtime_protocols   | 160 us                                                 | 170 us: 1.06x slower                                                         |
| pickle_pure_python         | 302 us                                                 | 322 us: 1.07x slower                                                         |
| bench_thread_pool          | 818 us                                                 | 875 us: 1.07x slower                                                         |
| django_template            | 31.7 ms                                                | 33.9 ms: 1.07x slower                                                        |
| spectral_norm              | 113 ms                                                 | 121 ms: 1.07x slower                                                         |
| nbody                      | 87.7 ms                                                | 94.2 ms: 1.07x slower                                                        |
| coroutines                 | 22.2 ms                                                | 23.9 ms: 1.08x slower                                                        |
| genshi_text                | 22.6 ms                                                | 24.4 ms: 1.08x slower                                                        |
| chaos                      | 58.0 ms                                                | 63.4 ms: 1.09x slower                                                        |
| json_dumps                 | 10.1 ms                                                | 11.1 ms: 1.10x slower                                                        |
| genshi_xml                 | 50.5 ms                                                | 56.5 ms: 1.12x slower                                                        |
| nqueens                    | 80.9 ms                                                | 91.4 ms: 1.13x slower                                                        |
| raytrace                   | 262 ms                                                 | 298 ms: 1.14x slower                                                         |
| many_optionals             | 857 us                                                 | 981 us: 1.14x slower                                                         |
| hexiom                     | 6.08 ms                                                | 7.13 ms: 1.17x slower                                                        |
| generators                 | 28.8 ms                                                | 36.4 ms: 1.26x slower                                                        |
| subparsers                 | 15.5 ms                                                | 20.8 ms: 1.34x slower                                                        |
| bench_mp_pool              | 24.0 ms                                                | 80.9 ms: 3.37x slower                                                        |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                                 |

Benchmark hidden because not significant (6): djangocms, scimark_sor, logging_silent, pprint_pformat, deltablue, fannkuch
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.023x faster

# HPT report

- Reliability score: 97.36% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.04x