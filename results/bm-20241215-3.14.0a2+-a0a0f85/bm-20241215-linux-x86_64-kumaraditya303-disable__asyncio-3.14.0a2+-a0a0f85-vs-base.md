# Results vs. base

- fork: kumaraditya303
- ref: disable__asyncio
- machine: linux-x86_64
- commit hash: a0a0f85
- commit date: 2024-12-15
- overall geometric mean: 1.045x slower
- HPT reliability: 58.73%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.19x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241213-linux-x86_64-python-11ff3286b7e821bf439b-3.14.0a2+-11ff328 | bm-20241215-linux-x86_64-kumaraditya303-disable__asyncio-3.14.0a2+-a0a0f85 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| docutils       | 2.60 sec                                                               | 2.59 sec: 1.01x faster                                                     |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                               |

Benchmark hidden because not significant (3): 2to3, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241213-linux-x86_64-python-11ff3286b7e821bf439b-3.14.0a2+-11ff328 | bm-20241215-linux-x86_64-kumaraditya303-disable__asyncio-3.14.0a2+-a0a0f85 |
|----------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| coroutines                 | 23.4 ms                                                                | 23.1 ms: 1.01x faster                                                      |
| async_generators           | 426 ms                                                                 | 423 ms: 1.01x faster                                                       |
| async_tree_cpu_io_mixed_tg | 478 ms                                                                 | 746 ms: 1.56x slower                                                       |
| async_tree_io_tg           | 620 ms                                                                 | 1.00 sec: 1.61x slower                                                     |
| async_tree_cpu_io_mixed    | 493 ms                                                                 | 796 ms: 1.62x slower                                                       |
| async_tree_io              | 631 ms                                                                 | 1.03 sec: 1.63x slower                                                     |
| async_tree_memoization_tg  | 314 ms                                                                 | 580 ms: 1.85x slower                                                       |
| async_tree_memoization     | 338 ms                                                                 | 632 ms: 1.87x slower                                                       |
| async_tree_none            | 272 ms                                                                 | 522 ms: 1.92x slower                                                       |
| async_tree_none_tg         | 252 ms                                                                 | 489 ms: 1.94x slower                                                       |
| Geometric mean             | (ref)                                                                  | 1.50x slower                                                               |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241213-linux-x86_64-python-11ff3286b7e821bf439b-3.14.0a2+-11ff328 | bm-20241215-linux-x86_64-kumaraditya303-disable__asyncio-3.14.0a2+-a0a0f85 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 77.8 ms                                                                | 77.0 ms: 1.01x faster                                                      |
| nbody          | 92.4 ms                                                                | 91.8 ms: 1.01x faster                                                      |
| pidigits       | 187 ms                                                                 | 187 ms: 1.00x faster                                                       |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241213-linux-x86_64-python-11ff3286b7e821bf439b-3.14.0a2+-11ff328 | bm-20241215-linux-x86_64-kumaraditya303-disable__asyncio-3.14.0a2+-a0a0f85 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 25.8 ms                                                                | 25.4 ms: 1.02x faster                                                      |
| regex_compile  | 129 ms                                                                 | 129 ms: 1.01x faster                                                       |
| regex_dna      | 217 ms                                                                 | 216 ms: 1.00x faster                                                       |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                               |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241213-linux-x86_64-python-11ff3286b7e821bf439b-3.14.0a2+-11ff328 | bm-20241215-linux-x86_64-kumaraditya303-disable__asyncio-3.14.0a2+-a0a0f85 |
|----------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_process    | 60.3 ms                                                                | 59.8 ms: 1.01x faster                                                      |
| json_dumps           | 11.4 ms                                                                | 11.5 ms: 1.01x slower                                                      |
| xml_etree_parse      | 139 ms                                                                 | 140 ms: 1.01x slower                                                       |
| unpickle_pure_python | 217 us                                                                 | 219 us: 1.01x slower                                                       |
| json_loads           | 26.6 us                                                                | 26.8 us: 1.01x slower                                                      |
| Geometric mean       | (ref)                                                                  | 1.00x slower                                                               |

Benchmark hidden because not significant (4): xml_etree_generate, xml_etree_iterparse, pickle_pure_python, tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241213-linux-x86_64-python-11ff3286b7e821bf439b-3.14.0a2+-11ff328 | bm-20241215-linux-x86_64-kumaraditya303-disable__asyncio-3.14.0a2+-a0a0f85 |
|------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 7.05 ms                                                                | 7.05 ms: 1.00x slower                                                      |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                               |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241213-linux-x86_64-python-11ff3286b7e821bf439b-3.14.0a2+-11ff328 | bm-20241215-linux-x86_64-kumaraditya303-disable__asyncio-3.14.0a2+-a0a0f85 |
|-----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_xml      | 50.4 ms                                                                | 49.5 ms: 1.02x faster                                                      |
| genshi_text     | 22.2 ms                                                                | 22.1 ms: 1.01x faster                                                      |
| mako            | 11.3 ms                                                                | 11.4 ms: 1.01x slower                                                      |
| django_template | 31.6 ms                                                                | 32.1 ms: 1.02x slower                                                      |
| Geometric mean  | (ref)                                                                  | 1.00x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241213-linux-x86_64-python-11ff3286b7e821bf439b-3.14.0a2+-11ff328 | bm-20241215-linux-x86_64-kumaraditya303-disable__asyncio-3.14.0a2+-a0a0f85 |
|----------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pyflate                    | 494 ms                                                                 | 462 ms: 1.07x faster                                                       |
| logging_silent             | 110 ns                                                                 | 106 ns: 1.04x faster                                                       |
| djangocms                  | 22.3 us                                                                | 21.5 us: 1.03x faster                                                      |
| fannkuch                   | 401 ms                                                                 | 393 ms: 1.02x faster                                                       |
| genshi_xml                 | 50.4 ms                                                                | 49.5 ms: 1.02x faster                                                      |
| nqueens                    | 80.4 ms                                                                | 79.0 ms: 1.02x faster                                                      |
| scimark_fft                | 374 ms                                                                 | 368 ms: 1.02x faster                                                       |
| regex_v8                   | 25.8 ms                                                                | 25.4 ms: 1.02x faster                                                      |
| sqlite_synth               | 2.89 us                                                                | 2.85 us: 1.01x faster                                                      |
| coroutines                 | 23.4 ms                                                                | 23.1 ms: 1.01x faster                                                      |
| float                      | 77.8 ms                                                                | 77.0 ms: 1.01x faster                                                      |
| sympy_sum                  | 149 ms                                                                 | 147 ms: 1.01x faster                                                       |
| thrift                     | 763 us                                                                 | 756 us: 1.01x faster                                                       |
| meteor_contest             | 107 ms                                                                 | 106 ms: 1.01x faster                                                       |
| xml_etree_process          | 60.3 ms                                                                | 59.8 ms: 1.01x faster                                                      |
| generators                 | 27.4 ms                                                                | 27.2 ms: 1.01x faster                                                      |
| deltablue                  | 3.30 ms                                                                | 3.28 ms: 1.01x faster                                                      |
| nbody                      | 92.4 ms                                                                | 91.8 ms: 1.01x faster                                                      |
| scimark_monte_carlo        | 68.9 ms                                                                | 68.4 ms: 1.01x faster                                                      |
| async_generators           | 426 ms                                                                 | 423 ms: 1.01x faster                                                       |
| sqlalchemy_imperative      | 16.3 ms                                                                | 16.2 ms: 1.01x faster                                                      |
| docutils                   | 2.60 sec                                                               | 2.59 sec: 1.01x faster                                                     |
| logging_simple             | 5.59 us                                                                | 5.56 us: 1.01x faster                                                      |
| regex_compile              | 129 ms                                                                 | 129 ms: 1.01x faster                                                       |
| genshi_text                | 22.2 ms                                                                | 22.1 ms: 1.01x faster                                                      |
| bpe_tokeniser              | 4.53 sec                                                               | 4.51 sec: 1.01x faster                                                     |
| many_optionals             | 954 us                                                                 | 949 us: 1.01x faster                                                       |
| regex_dna                  | 217 ms                                                                 | 216 ms: 1.00x faster                                                       |
| pidigits                   | 187 ms                                                                 | 187 ms: 1.00x faster                                                       |
| python_startup_no_site     | 7.05 ms                                                                | 7.05 ms: 1.00x slower                                                      |
| sqlglot_optimize           | 52.7 ms                                                                | 52.8 ms: 1.00x slower                                                      |
| pprint_pformat             | 1.48 sec                                                               | 1.49 sec: 1.01x slower                                                     |
| deepcopy_reduce            | 2.68 us                                                                | 2.69 us: 1.01x slower                                                      |
| subparsers                 | 20.8 ms                                                                | 21.0 ms: 1.01x slower                                                      |
| json_dumps                 | 11.4 ms                                                                | 11.5 ms: 1.01x slower                                                      |
| create_gc_cycles           | 2.46 ms                                                                | 2.48 ms: 1.01x slower                                                      |
| chaos                      | 61.0 ms                                                                | 61.5 ms: 1.01x slower                                                      |
| xml_etree_parse            | 139 ms                                                                 | 140 ms: 1.01x slower                                                       |
| unpickle_pure_python       | 217 us                                                                 | 219 us: 1.01x slower                                                       |
| json_loads                 | 26.6 us                                                                | 26.8 us: 1.01x slower                                                      |
| telco                      | 7.76 ms                                                                | 7.83 ms: 1.01x slower                                                      |
| crypto_pyaes               | 72.1 ms                                                                | 72.7 ms: 1.01x slower                                                      |
| pprint_safe_repr           | 721 ms                                                                 | 728 ms: 1.01x slower                                                       |
| hexiom                     | 6.14 ms                                                                | 6.20 ms: 1.01x slower                                                      |
| comprehensions             | 16.8 us                                                                | 17.0 us: 1.01x slower                                                      |
| go                         | 120 ms                                                                 | 122 ms: 1.01x slower                                                       |
| raytrace                   | 271 ms                                                                 | 274 ms: 1.01x slower                                                       |
| coverage                   | 82.7 ms                                                                | 83.8 ms: 1.01x slower                                                      |
| mako                       | 11.3 ms                                                                | 11.4 ms: 1.01x slower                                                      |
| gc_traversal               | 4.94 ms                                                                | 5.02 ms: 1.02x slower                                                      |
| django_template            | 31.6 ms                                                                | 32.1 ms: 1.02x slower                                                      |
| scimark_lu                 | 115 ms                                                                 | 117 ms: 1.02x slower                                                       |
| scimark_sparse_mat_mult    | 4.82 ms                                                                | 5.03 ms: 1.04x slower                                                      |
| mdp                        | 2.49 sec                                                               | 2.64 sec: 1.06x slower                                                     |
| async_tree_cpu_io_mixed_tg | 478 ms                                                                 | 746 ms: 1.56x slower                                                       |
| async_tree_io_tg           | 620 ms                                                                 | 1.00 sec: 1.61x slower                                                     |
| async_tree_cpu_io_mixed    | 493 ms                                                                 | 796 ms: 1.62x slower                                                       |
| async_tree_io              | 631 ms                                                                 | 1.03 sec: 1.63x slower                                                     |
| async_tree_memoization_tg  | 314 ms                                                                 | 580 ms: 1.85x slower                                                       |
| async_tree_memoization     | 338 ms                                                                 | 632 ms: 1.87x slower                                                       |
| async_tree_none            | 272 ms                                                                 | 522 ms: 1.92x slower                                                       |
| async_tree_none_tg         | 252 ms                                                                 | 489 ms: 1.94x slower                                                       |
| Geometric mean             | (ref)                                                                  | 1.05x slower                                                               |

Benchmark hidden because not significant (36): mypy2, connected_components, shortest_path, sphinx, pylint, sympy_expand, spectral_norm, typing_runtime_protocols, sqlglot_transpile, sympy_str, scimark_sor, bench_mp_pool, k_core, logging_format, pathlib, deepcopy, regex_effbot, html5lib, sqlalchemy_declarative, richards_super, pycparser, deepcopy_memo, xml_etree_generate, python_startup, 2to3, sympy_integrate, sqlglot_parse, bench_thread_pool, xml_etree_iterparse, dulwich_log, pickle_pure_python, asyncio_websockets, sqlglot_normalize, richards, tomli_loads, json

- Geometric mean (including insignificant results): 1.045x slower

# HPT report

- Reliability score: 58.73% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.19x