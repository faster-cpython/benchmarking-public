# Results vs. base

- fork: faster-cpython
- ref: remove_most_conditio
- machine: linux-x86_64
- commit hash: 584015a
- commit date: 2025-01-23
- overall geometric mean: 1.008x slower
- HPT reliability: 99.87%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250123-pythonperf2-x86_64-python-a10f99375e7912df863c-3.14.0a4+-a10f993 | bm-20250123-pythonperf2-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-584015a |
|----------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                                       | 283 ms: 1.01x slower                                                                   |
| docutils       | 2.86 sec                                                                     | 2.92 sec: 1.02x slower                                                                 |
| sphinx         | 1.10 sec                                                                     | 1.13 sec: 1.03x slower                                                                 |
| Geometric mean | (ref)                                                                        | 1.01x slower                                                                           |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250123-pythonperf2-x86_64-python-a10f99375e7912df863c-3.14.0a4+-a10f993 | bm-20250123-pythonperf2-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-584015a |
|----------------------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| async_generators           | 413 ms                                                                       | 400 ms: 1.03x faster                                                                   |
| coroutines                 | 21.0 ms                                                                      | 20.6 ms: 1.02x faster                                                                  |
| async_tree_cpu_io_mixed_tg | 509 ms                                                                       | 505 ms: 1.01x faster                                                                   |
| async_tree_memoization_tg  | 335 ms                                                                       | 336 ms: 1.00x slower                                                                   |
| async_tree_cpu_io_mixed    | 514 ms                                                                       | 517 ms: 1.01x slower                                                                   |
| async_tree_none_tg         | 277 ms                                                                       | 279 ms: 1.01x slower                                                                   |
| async_tree_none            | 285 ms                                                                       | 288 ms: 1.01x slower                                                                   |
| async_tree_memoization     | 347 ms                                                                       | 351 ms: 1.01x slower                                                                   |
| async_tree_io              | 643 ms                                                                       | 653 ms: 1.02x slower                                                                   |
| Geometric mean             | (ref)                                                                        | 1.00x faster                                                                           |

Benchmark hidden because not significant (2): async_tree_io_tg, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250123-pythonperf2-x86_64-python-a10f99375e7912df863c-3.14.0a4+-a10f993 | bm-20250123-pythonperf2-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-584015a |
|----------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| pidigits       | 254 ms                                                                       | 253 ms: 1.00x faster                                                                   |
| Geometric mean | (ref)                                                                        | 1.00x faster                                                                           |

Benchmark hidden because not significant (2): float, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250123-pythonperf2-x86_64-python-a10f99375e7912df863c-3.14.0a4+-a10f993 | bm-20250123-pythonperf2-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-584015a |
|----------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| regex_v8       | 25.6 ms                                                                      | 25.3 ms: 1.01x faster                                                                  |
| regex_effbot   | 3.14 ms                                                                      | 3.12 ms: 1.00x faster                                                                  |
| regex_compile  | 133 ms                                                                       | 134 ms: 1.01x slower                                                                   |
| regex_dna      | 240 ms                                                                       | 244 ms: 1.02x slower                                                                   |
| Geometric mean | (ref)                                                                        | 1.00x slower                                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250123-pythonperf2-x86_64-python-a10f99375e7912df863c-3.14.0a4+-a10f993 | bm-20250123-pythonperf2-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-584015a |
|----------------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| pickle_pure_python   | 328 us                                                                       | 323 us: 1.02x faster                                                                   |
| unpickle_pure_python | 210 us                                                                       | 208 us: 1.01x faster                                                                   |
| xml_etree_generate   | 84.9 ms                                                                      | 84.1 ms: 1.01x faster                                                                  |
| json_loads           | 25.4 us                                                                      | 25.2 us: 1.01x faster                                                                  |
| tomli_loads          | 2.06 sec                                                                     | 2.05 sec: 1.01x faster                                                                 |
| json_dumps           | 11.6 ms                                                                      | 11.7 ms: 1.00x slower                                                                  |
| Geometric mean       | (ref)                                                                        | 1.00x faster                                                                           |

Benchmark hidden because not significant (3): xml_etree_parse, xml_etree_process, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250123-pythonperf2-x86_64-python-a10f99375e7912df863c-3.14.0a4+-a10f993 | bm-20250123-pythonperf2-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-584015a |
|------------------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| python_startup_no_site | 8.97 ms                                                                      | 8.98 ms: 1.00x slower                                                                  |
| python_startup         | 16.0 ms                                                                      | 16.0 ms: 1.00x slower                                                                  |
| Geometric mean         | (ref)                                                                        | 1.00x slower                                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250123-pythonperf2-x86_64-python-a10f99375e7912df863c-3.14.0a4+-a10f993 | bm-20250123-pythonperf2-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-584015a |
|-----------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| genshi_xml      | 51.7 ms                                                                      | 52.3 ms: 1.01x slower                                                                  |
| mako            | 10.8 ms                                                                      | 10.9 ms: 1.01x slower                                                                  |
| django_template | 35.9 ms                                                                      | 37.0 ms: 1.03x slower                                                                  |
| Geometric mean  | (ref)                                                                        | 1.01x slower                                                                           |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20250123-pythonperf2-x86_64-python-a10f99375e7912df863c-3.14.0a4+-a10f993 | bm-20250123-pythonperf2-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-584015a |
|----------------------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| telco                      | 8.01 ms                                                                      | 7.66 ms: 1.05x faster                                                                  |
| async_generators           | 413 ms                                                                       | 400 ms: 1.03x faster                                                                   |
| bench_thread_pool          | 961 us                                                                       | 933 us: 1.03x faster                                                                   |
| generators                 | 29.0 ms                                                                      | 28.2 ms: 1.03x faster                                                                  |
| hexiom                     | 6.02 ms                                                                      | 5.91 ms: 1.02x faster                                                                  |
| pickle_pure_python         | 328 us                                                                       | 323 us: 1.02x faster                                                                   |
| coroutines                 | 21.0 ms                                                                      | 20.6 ms: 1.02x faster                                                                  |
| chaos                      | 59.7 ms                                                                      | 58.8 ms: 1.02x faster                                                                  |
| typing_runtime_protocols   | 171 us                                                                       | 168 us: 1.02x faster                                                                   |
| nqueens                    | 90.0 ms                                                                      | 88.8 ms: 1.01x faster                                                                  |
| dulwich_log                | 66.5 ms                                                                      | 65.7 ms: 1.01x faster                                                                  |
| pyflate                    | 443 ms                                                                       | 438 ms: 1.01x faster                                                                   |
| regex_v8                   | 25.6 ms                                                                      | 25.3 ms: 1.01x faster                                                                  |
| unpickle_pure_python       | 210 us                                                                       | 208 us: 1.01x faster                                                                   |
| xml_etree_generate         | 84.9 ms                                                                      | 84.1 ms: 1.01x faster                                                                  |
| json_loads                 | 25.4 us                                                                      | 25.2 us: 1.01x faster                                                                  |
| async_tree_cpu_io_mixed_tg | 509 ms                                                                       | 505 ms: 1.01x faster                                                                   |
| sqlite_synth               | 2.82 us                                                                      | 2.80 us: 1.01x faster                                                                  |
| scimark_sor                | 110 ms                                                                       | 110 ms: 1.01x faster                                                                   |
| tomli_loads                | 2.06 sec                                                                     | 2.05 sec: 1.01x faster                                                                 |
| scimark_monte_carlo        | 63.2 ms                                                                      | 62.8 ms: 1.01x faster                                                                  |
| deepcopy                   | 282 us                                                                       | 280 us: 1.01x faster                                                                   |
| sqlalchemy_declarative     | 144 ms                                                                       | 143 ms: 1.01x faster                                                                   |
| mdp                        | 2.44 sec                                                                     | 2.43 sec: 1.00x faster                                                                 |
| regex_effbot               | 3.14 ms                                                                      | 3.12 ms: 1.00x faster                                                                  |
| pidigits                   | 254 ms                                                                       | 253 ms: 1.00x faster                                                                   |
| pprint_pformat             | 1.57 sec                                                                     | 1.57 sec: 1.00x faster                                                                 |
| meteor_contest             | 126 ms                                                                       | 126 ms: 1.00x slower                                                                   |
| python_startup_no_site     | 8.97 ms                                                                      | 8.98 ms: 1.00x slower                                                                  |
| python_startup             | 16.0 ms                                                                      | 16.0 ms: 1.00x slower                                                                  |
| deepcopy_reduce            | 2.89 us                                                                      | 2.90 us: 1.00x slower                                                                  |
| sqlglot_transpile          | 1.71 ms                                                                      | 1.71 ms: 1.00x slower                                                                  |
| pathlib                    | 15.8 ms                                                                      | 15.8 ms: 1.00x slower                                                                  |
| json_dumps                 | 11.6 ms                                                                      | 11.7 ms: 1.00x slower                                                                  |
| async_tree_memoization_tg  | 335 ms                                                                       | 336 ms: 1.00x slower                                                                   |
| async_tree_cpu_io_mixed    | 514 ms                                                                       | 517 ms: 1.01x slower                                                                   |
| logging_silent             | 96.9 ns                                                                      | 97.4 ns: 1.01x slower                                                                  |
| pprint_safe_repr           | 778 ms                                                                       | 782 ms: 1.01x slower                                                                   |
| sympy_integrate            | 23.0 ms                                                                      | 23.1 ms: 1.01x slower                                                                  |
| sympy_expand               | 488 ms                                                                       | 490 ms: 1.01x slower                                                                   |
| async_tree_none_tg         | 277 ms                                                                       | 279 ms: 1.01x slower                                                                   |
| bpe_tokeniser              | 4.66 sec                                                                     | 4.69 sec: 1.01x slower                                                                 |
| sympy_sum                  | 151 ms                                                                       | 152 ms: 1.01x slower                                                                   |
| scimark_lu                 | 93.5 ms                                                                      | 94.3 ms: 1.01x slower                                                                  |
| sqlglot_parse              | 1.31 ms                                                                      | 1.33 ms: 1.01x slower                                                                  |
| regex_compile              | 133 ms                                                                       | 134 ms: 1.01x slower                                                                   |
| spectral_norm              | 83.5 ms                                                                      | 84.3 ms: 1.01x slower                                                                  |
| sqlglot_optimize           | 56.9 ms                                                                      | 57.5 ms: 1.01x slower                                                                  |
| async_tree_none            | 285 ms                                                                       | 288 ms: 1.01x slower                                                                   |
| 2to3                       | 280 ms                                                                       | 283 ms: 1.01x slower                                                                   |
| genshi_xml                 | 51.7 ms                                                                      | 52.3 ms: 1.01x slower                                                                  |
| mako                       | 10.8 ms                                                                      | 10.9 ms: 1.01x slower                                                                  |
| async_tree_memoization     | 347 ms                                                                       | 351 ms: 1.01x slower                                                                   |
| comprehensions             | 17.5 us                                                                      | 17.7 us: 1.01x slower                                                                  |
| deepcopy_memo              | 30.0 us                                                                      | 30.4 us: 1.02x slower                                                                  |
| logging_format             | 6.76 us                                                                      | 6.86 us: 1.02x slower                                                                  |
| regex_dna                  | 240 ms                                                                       | 244 ms: 1.02x slower                                                                   |
| scimark_sparse_mat_mult    | 4.58 ms                                                                      | 4.66 ms: 1.02x slower                                                                  |
| async_tree_io              | 643 ms                                                                       | 653 ms: 1.02x slower                                                                   |
| connected_components       | 411 ms                                                                       | 418 ms: 1.02x slower                                                                   |
| shortest_path              | 438 ms                                                                       | 446 ms: 1.02x slower                                                                   |
| many_optionals             | 1.00 ms                                                                      | 1.02 ms: 1.02x slower                                                                  |
| pylint                     | 316 ms                                                                       | 322 ms: 1.02x slower                                                                   |
| pycparser                  | 1.22 sec                                                                     | 1.24 sec: 1.02x slower                                                                 |
| sqlglot_normalize          | 114 ms                                                                       | 116 ms: 1.02x slower                                                                   |
| docutils                   | 2.86 sec                                                                     | 2.92 sec: 1.02x slower                                                                 |
| fannkuch                   | 358 ms                                                                       | 366 ms: 1.02x slower                                                                   |
| sphinx                     | 1.10 sec                                                                     | 1.13 sec: 1.03x slower                                                                 |
| raytrace                   | 265 ms                                                                       | 272 ms: 1.03x slower                                                                   |
| thrift                     | 857 us                                                                       | 880 us: 1.03x slower                                                                   |
| coverage                   | 75.6 ms                                                                      | 77.7 ms: 1.03x slower                                                                  |
| django_template            | 35.9 ms                                                                      | 37.0 ms: 1.03x slower                                                                  |
| subparsers                 | 22.4 ms                                                                      | 23.1 ms: 1.03x slower                                                                  |
| go                         | 125 ms                                                                       | 130 ms: 1.04x slower                                                                   |
| gc_traversal               | 6.17 ms                                                                      | 6.41 ms: 1.04x slower                                                                  |
| deltablue                  | 3.28 ms                                                                      | 3.43 ms: 1.05x slower                                                                  |
| richards_super             | 52.8 ms                                                                      | 62.3 ms: 1.18x slower                                                                  |
| richards                   | 46.2 ms                                                                      | 55.3 ms: 1.20x slower                                                                  |
| bench_mp_pool              | 994 ms                                                                       | 2.02 sec: 2.03x slower                                                                 |
| Geometric mean             | (ref)                                                                        | 1.01x slower                                                                           |

Benchmark hidden because not significant (17): html5lib, float, genshi_text, sqlalchemy_imperative, async_tree_io_tg, xml_etree_parse, asyncio_websockets, scimark_fft, json, create_gc_cycles, xml_etree_process, xml_etree_iterparse, sympy_str, crypto_pyaes, nbody, k_core, logging_simple

- Geometric mean (including insignificant results): 1.008x slower

# HPT report

- Reliability score: 99.87% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x