# Results vs. base

- fork: faster-cpython
- ref: virtual_iterators
- machine: linux-x86_64
- commit hash: a4b740d
- commit date: 2025-04-16
- overall geometric mean: 1.005x faster
- HPT reliability: 84.78%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250414-linux-x86_64-python-844596c09fc812a58ac1-3.14.0a7+-844596c | bm-20250416-linux-x86_64-faster%2dcpython-virtual_iterators-3.14.0a7+-a4b740d |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 250 ms                                                                 | 250 ms: 1.00x faster                                                          |
| docutils       | 2.59 sec                                                               | 2.56 sec: 1.01x faster                                                        |
| sphinx         | 1.00 sec                                                               | 993 ms: 1.01x faster                                                          |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                                  |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20250414-linux-x86_64-python-844596c09fc812a58ac1-3.14.0a7+-844596c | bm-20250416-linux-x86_64-faster%2dcpython-virtual_iterators-3.14.0a7+-a4b740d |
|-------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 475 ms                                                                 | 480 ms: 1.01x slower                                                          |
| async_tree_none_tg      | 247 ms                                                                 | 251 ms: 1.01x slower                                                          |
| coroutines              | 23.6 ms                                                                | 24.4 ms: 1.03x slower                                                         |
| Geometric mean          | (ref)                                                                  | 1.01x slower                                                                  |

Benchmark hidden because not significant (8): async_generators, asyncio_websockets, async_tree_none, async_tree_io, async_tree_memoization, async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250414-linux-x86_64-python-844596c09fc812a58ac1-3.14.0a7+-844596c | bm-20250416-linux-x86_64-faster%2dcpython-virtual_iterators-3.14.0a7+-a4b740d |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| nbody          | 100 ms                                                                 | 93.9 ms: 1.07x faster                                                         |
| pidigits       | 194 ms                                                                 | 187 ms: 1.04x faster                                                          |
| float          | 69.6 ms                                                                | 69.0 ms: 1.01x faster                                                         |
| Geometric mean | (ref)                                                                  | 1.04x faster                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250414-linux-x86_64-python-844596c09fc812a58ac1-3.14.0a7+-844596c | bm-20250416-linux-x86_64-faster%2dcpython-virtual_iterators-3.14.0a7+-a4b740d |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_v8       | 22.9 ms                                                                | 22.3 ms: 1.03x faster                                                         |
| regex_compile  | 126 ms                                                                 | 125 ms: 1.01x faster                                                          |
| regex_dna      | 198 ms                                                                 | 203 ms: 1.02x slower                                                          |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                                  |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250414-linux-x86_64-python-844596c09fc812a58ac1-3.14.0a7+-844596c | bm-20250416-linux-x86_64-faster%2dcpython-virtual_iterators-3.14.0a7+-a4b740d |
|----------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| xml_etree_generate   | 84.9 ms                                                                | 83.2 ms: 1.02x faster                                                         |
| xml_etree_process    | 58.8 ms                                                                | 57.8 ms: 1.02x faster                                                         |
| json_dumps           | 11.6 ms                                                                | 11.5 ms: 1.01x faster                                                         |
| unpickle_pure_python | 218 us                                                                 | 217 us: 1.01x faster                                                          |
| json_loads           | 29.7 us                                                                | 30.1 us: 1.01x slower                                                         |
| Geometric mean       | (ref)                                                                  | 1.00x faster                                                                  |

Benchmark hidden because not significant (4): xml_etree_iterparse, pickle_pure_python, tomli_loads, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20250414-linux-x86_64-python-844596c09fc812a58ac1-3.14.0a7+-844596c | bm-20250416-linux-x86_64-faster%2dcpython-virtual_iterators-3.14.0a7+-a4b740d |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup | 13.2 ms                                                                | 13.2 ms: 1.00x slower                                                         |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                                  |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250414-linux-x86_64-python-844596c09fc812a58ac1-3.14.0a7+-844596c | bm-20250416-linux-x86_64-faster%2dcpython-virtual_iterators-3.14.0a7+-a4b740d |
|-----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mako            | 11.5 ms                                                                | 11.3 ms: 1.02x faster                                                         |
| django_template | 31.6 ms                                                                | 31.0 ms: 1.02x faster                                                         |
| genshi_text     | 20.9 ms                                                                | 20.6 ms: 1.02x faster                                                         |
| Geometric mean  | (ref)                                                                  | 1.02x faster                                                                  |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                | bm-20250414-linux-x86_64-python-844596c09fc812a58ac1-3.14.0a7+-844596c | bm-20250416-linux-x86_64-faster%2dcpython-virtual_iterators-3.14.0a7+-a4b740d |
|--------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| nbody                    | 100 ms                                                                 | 93.9 ms: 1.07x faster                                                         |
| comprehensions           | 16.9 us                                                                | 15.9 us: 1.06x faster                                                         |
| generators               | 30.3 ms                                                                | 28.9 ms: 1.05x faster                                                         |
| pidigits                 | 194 ms                                                                 | 187 ms: 1.04x faster                                                          |
| typing_runtime_protocols | 164 us                                                                 | 159 us: 1.03x faster                                                          |
| regex_v8                 | 22.9 ms                                                                | 22.3 ms: 1.03x faster                                                         |
| telco                    | 7.82 ms                                                                | 7.64 ms: 1.02x faster                                                         |
| mako                     | 11.5 ms                                                                | 11.3 ms: 1.02x faster                                                         |
| sqlalchemy_declarative   | 133 ms                                                                 | 130 ms: 1.02x faster                                                          |
| xml_etree_generate       | 84.9 ms                                                                | 83.2 ms: 1.02x faster                                                         |
| pathlib                  | 17.2 ms                                                                | 16.8 ms: 1.02x faster                                                         |
| django_template          | 31.6 ms                                                                | 31.0 ms: 1.02x faster                                                         |
| coverage                 | 88.5 ms                                                                | 86.8 ms: 1.02x faster                                                         |
| genshi_text              | 20.9 ms                                                                | 20.6 ms: 1.02x faster                                                         |
| sqlglot_v2_normalize     | 105 ms                                                                 | 103 ms: 1.02x faster                                                          |
| scimark_sparse_mat_mult  | 5.05 ms                                                                | 4.96 ms: 1.02x faster                                                         |
| xml_etree_process        | 58.8 ms                                                                | 57.8 ms: 1.02x faster                                                         |
| scimark_lu               | 120 ms                                                                 | 118 ms: 1.02x faster                                                          |
| sqlglot_v2_optimize      | 52.1 ms                                                                | 51.3 ms: 1.02x faster                                                         |
| pycparser                | 1.12 sec                                                               | 1.10 sec: 1.01x faster                                                        |
| hexiom                   | 6.20 ms                                                                | 6.11 ms: 1.01x faster                                                         |
| logging_format           | 6.10 us                                                                | 6.02 us: 1.01x faster                                                         |
| pprint_safe_repr         | 710 ms                                                                 | 702 ms: 1.01x faster                                                          |
| subparsers               | 20.8 ms                                                                | 20.5 ms: 1.01x faster                                                         |
| sphinx                   | 1.00 sec                                                               | 993 ms: 1.01x faster                                                          |
| json_dumps               | 11.6 ms                                                                | 11.5 ms: 1.01x faster                                                         |
| pyflate                  | 435 ms                                                                 | 431 ms: 1.01x faster                                                          |
| deepcopy_reduce          | 2.68 us                                                                | 2.65 us: 1.01x faster                                                         |
| docutils                 | 2.59 sec                                                               | 2.56 sec: 1.01x faster                                                        |
| raytrace                 | 262 ms                                                                 | 260 ms: 1.01x faster                                                          |
| many_optionals           | 932 us                                                                 | 923 us: 1.01x faster                                                          |
| float                    | 69.6 ms                                                                | 69.0 ms: 1.01x faster                                                         |
| mdp                      | 1.21 sec                                                               | 1.20 sec: 1.01x faster                                                        |
| pprint_pformat           | 1.45 sec                                                               | 1.44 sec: 1.01x faster                                                        |
| regex_compile            | 126 ms                                                                 | 125 ms: 1.01x faster                                                          |
| bench_thread_pool        | 886 us                                                                 | 880 us: 1.01x faster                                                          |
| sqlalchemy_imperative    | 16.9 ms                                                                | 16.8 ms: 1.01x faster                                                         |
| unpickle_pure_python     | 218 us                                                                 | 217 us: 1.01x faster                                                          |
| meteor_contest           | 105 ms                                                                 | 104 ms: 1.00x faster                                                          |
| go                       | 109 ms                                                                 | 108 ms: 1.00x faster                                                          |
| dulwich_log              | 59.6 ms                                                                | 59.5 ms: 1.00x faster                                                         |
| 2to3                     | 250 ms                                                                 | 250 ms: 1.00x faster                                                          |
| python_startup           | 13.2 ms                                                                | 13.2 ms: 1.00x slower                                                         |
| nqueens                  | 80.0 ms                                                                | 80.1 ms: 1.00x slower                                                         |
| sqlglot_v2_transpile     | 1.54 ms                                                                | 1.55 ms: 1.00x slower                                                         |
| gc_traversal             | 5.01 ms                                                                | 5.05 ms: 1.01x slower                                                         |
| crypto_pyaes             | 73.2 ms                                                                | 73.8 ms: 1.01x slower                                                         |
| shortest_path            | 489 ms                                                                 | 493 ms: 1.01x slower                                                          |
| bpe_tokeniser            | 4.54 sec                                                               | 4.58 sec: 1.01x slower                                                        |
| async_tree_cpu_io_mixed  | 475 ms                                                                 | 480 ms: 1.01x slower                                                          |
| create_gc_cycles         | 2.46 ms                                                                | 2.49 ms: 1.01x slower                                                         |
| spectral_norm            | 102 ms                                                                 | 104 ms: 1.01x slower                                                          |
| chaos                    | 55.8 ms                                                                | 56.5 ms: 1.01x slower                                                         |
| async_tree_none_tg       | 247 ms                                                                 | 251 ms: 1.01x slower                                                          |
| json_loads               | 29.7 us                                                                | 30.1 us: 1.01x slower                                                         |
| fannkuch                 | 411 ms                                                                 | 417 ms: 1.02x slower                                                          |
| deltablue                | 3.32 ms                                                                | 3.39 ms: 1.02x slower                                                         |
| deepcopy_memo            | 28.2 us                                                                | 28.7 us: 1.02x slower                                                         |
| regex_dna                | 198 ms                                                                 | 203 ms: 1.02x slower                                                          |
| scimark_sor              | 116 ms                                                                 | 119 ms: 1.03x slower                                                          |
| coroutines               | 23.6 ms                                                                | 24.4 ms: 1.03x slower                                                         |
| Geometric mean           | (ref)                                                                  | 1.01x faster                                                                  |

Benchmark hidden because not significant (29): logging_silent, sqlite_synth, async_generators, regex_effbot, xml_etree_iterparse, bench_mp_pool, deepcopy, pickle_pure_python, logging_simple, richards, genshi_xml, json, richards_super, tomli_loads, asyncio_websockets, python_startup_no_site, async_tree_none, sqlglot_v2_parse, async_tree_io, async_tree_memoization, k_core, scimark_fft, html5lib, xml_etree_parse, scimark_monte_carlo, async_tree_cpu_io_mixed_tg, async_tree_io_tg, connected_components, async_tree_memoization_tg
Ignored benchmarks (5) of results/bm-20250414-3.14.0a7+-844596c/bm-20250414-linux-x86_64-python-844596c09fc812a58ac1-3.14.0a7+-844596c.json: pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum

- Geometric mean (including insignificant results): 1.005x faster

# HPT report

- Reliability score: 84.78% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x