# Results vs. base

- fork: faster-cpython
- ref: tstate_in_dealloc
- machine: linux-x86_64
- commit hash: 49ac4ce
- commit date: 2025-04-09
- overall geometric mean: 1.013x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250408-linux-x86_64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a | bm-20250409-linux-x86_64-faster%2dcpython-tstate_in_dealloc-3.14.0a7+-49ac4ce |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 250 ms                                                                 | 252 ms: 1.01x slower                                                          |
| docutils       | 2.59 sec                                                               | 2.61 sec: 1.01x slower                                                        |
| html5lib       | 60.8 ms                                                                | 62.2 ms: 1.02x slower                                                         |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                                  |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250408-linux-x86_64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a | bm-20250409-linux-x86_64-faster%2dcpython-tstate_in_dealloc-3.14.0a7+-49ac4ce |
|----------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_none_tg         | 246 ms                                                                 | 248 ms: 1.01x slower                                                          |
| async_tree_memoization     | 309 ms                                                                 | 313 ms: 1.01x slower                                                          |
| async_tree_cpu_io_mixed_tg | 474 ms                                                                 | 483 ms: 1.02x slower                                                          |
| async_tree_cpu_io_mixed    | 479 ms                                                                 | 489 ms: 1.02x slower                                                          |
| coroutines                 | 23.3 ms                                                                | 23.9 ms: 1.03x slower                                                         |
| async_tree_none            | 255 ms                                                                 | 262 ms: 1.03x slower                                                          |
| async_generators           | 384 ms                                                                 | 407 ms: 1.06x slower                                                          |
| Geometric mean             | (ref)                                                                  | 1.02x slower                                                                  |

Benchmark hidden because not significant (4): asyncio_websockets, async_tree_io_tg, async_tree_io, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250408-linux-x86_64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a | bm-20250409-linux-x86_64-faster%2dcpython-tstate_in_dealloc-3.14.0a7+-49ac4ce |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| pidigits       | 186 ms                                                                 | 186 ms: 1.00x faster                                                          |
| float          | 66.1 ms                                                                | 70.3 ms: 1.06x slower                                                         |
| nbody          | 87.8 ms                                                                | 97.1 ms: 1.10x slower                                                         |
| Geometric mean | (ref)                                                                  | 1.05x slower                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250408-linux-x86_64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a | bm-20250409-linux-x86_64-faster%2dcpython-tstate_in_dealloc-3.14.0a7+-49ac4ce |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_effbot   | 3.27 ms                                                                | 3.10 ms: 1.05x faster                                                         |
| regex_dna      | 214 ms                                                                 | 209 ms: 1.03x faster                                                          |
| regex_compile  | 123 ms                                                                 | 125 ms: 1.02x slower                                                          |
| regex_v8       | 22.9 ms                                                                | 23.9 ms: 1.04x slower                                                         |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250408-linux-x86_64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a | bm-20250409-linux-x86_64-faster%2dcpython-tstate_in_dealloc-3.14.0a7+-49ac4ce |
|----------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| json_dumps           | 11.6 ms                                                                | 11.5 ms: 1.01x faster                                                         |
| xml_etree_iterparse  | 98.1 ms                                                                | 97.7 ms: 1.00x faster                                                         |
| unpickle_pure_python | 214 us                                                                 | 214 us: 1.00x faster                                                          |
| pickle_pure_python   | 312 us                                                                 | 313 us: 1.00x slower                                                          |
| xml_etree_process    | 57.7 ms                                                                | 58.1 ms: 1.01x slower                                                         |
| xml_etree_generate   | 82.9 ms                                                                | 83.5 ms: 1.01x slower                                                         |
| json_loads           | 29.8 us                                                                | 30.5 us: 1.02x slower                                                         |
| tomli_loads          | 1.94 sec                                                               | 2.00 sec: 1.03x slower                                                        |
| Geometric mean       | (ref)                                                                  | 1.01x slower                                                                  |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250408-linux-x86_64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a | bm-20250409-linux-x86_64-faster%2dcpython-tstate_in_dealloc-3.14.0a7+-49ac4ce |
|------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup         | 13.2 ms                                                                | 13.2 ms: 1.00x slower                                                         |
| python_startup_no_site | 8.20 ms                                                                | 8.24 ms: 1.00x slower                                                         |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250408-linux-x86_64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a | bm-20250409-linux-x86_64-faster%2dcpython-tstate_in_dealloc-3.14.0a7+-49ac4ce |
|-----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| django_template | 31.9 ms                                                                | 31.4 ms: 1.01x faster                                                         |
| mako            | 11.2 ms                                                                | 11.3 ms: 1.00x slower                                                         |
| genshi_text     | 20.6 ms                                                                | 20.9 ms: 1.01x slower                                                         |
| genshi_xml      | 48.6 ms                                                                | 49.5 ms: 1.02x slower                                                         |
| Geometric mean  | (ref)                                                                  | 1.01x slower                                                                  |

All benchmarks:
===============

| Benchmark                  | bm-20250408-linux-x86_64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a | bm-20250409-linux-x86_64-faster%2dcpython-tstate_in_dealloc-3.14.0a7+-49ac4ce |
|----------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_effbot               | 3.27 ms                                                                | 3.10 ms: 1.05x faster                                                         |
| pyflate                    | 438 ms                                                                 | 425 ms: 1.03x faster                                                          |
| regex_dna                  | 214 ms                                                                 | 209 ms: 1.03x faster                                                          |
| pycparser                  | 1.14 sec                                                               | 1.12 sec: 1.02x faster                                                        |
| logging_silent             | 97.1 ns                                                                | 95.5 ns: 1.02x faster                                                         |
| django_template            | 31.9 ms                                                                | 31.4 ms: 1.01x faster                                                         |
| deltablue                  | 3.32 ms                                                                | 3.28 ms: 1.01x faster                                                         |
| richards_super             | 49.2 ms                                                                | 48.7 ms: 1.01x faster                                                         |
| hexiom                     | 6.11 ms                                                                | 6.05 ms: 1.01x faster                                                         |
| sqlglot_v2_parse           | 1.21 ms                                                                | 1.20 ms: 1.01x faster                                                         |
| gc_traversal               | 4.82 ms                                                                | 4.79 ms: 1.01x faster                                                         |
| json_dumps                 | 11.6 ms                                                                | 11.5 ms: 1.01x faster                                                         |
| richards                   | 42.6 ms                                                                | 42.4 ms: 1.01x faster                                                         |
| xml_etree_iterparse        | 98.1 ms                                                                | 97.7 ms: 1.00x faster                                                         |
| sqlglot_v2_transpile       | 1.52 ms                                                                | 1.51 ms: 1.00x faster                                                         |
| unpickle_pure_python       | 214 us                                                                 | 214 us: 1.00x faster                                                          |
| pidigits                   | 186 ms                                                                 | 186 ms: 1.00x faster                                                          |
| sympy_integrate            | 19.0 ms                                                                | 19.1 ms: 1.00x slower                                                         |
| sqlalchemy_imperative      | 16.8 ms                                                                | 16.8 ms: 1.00x slower                                                         |
| python_startup             | 13.2 ms                                                                | 13.2 ms: 1.00x slower                                                         |
| meteor_contest             | 106 ms                                                                 | 106 ms: 1.00x slower                                                          |
| pickle_pure_python         | 312 us                                                                 | 313 us: 1.00x slower                                                          |
| python_startup_no_site     | 8.20 ms                                                                | 8.24 ms: 1.00x slower                                                         |
| bench_mp_pool              | 82.0 ms                                                                | 82.3 ms: 1.00x slower                                                         |
| mako                       | 11.2 ms                                                                | 11.3 ms: 1.00x slower                                                         |
| mdp                        | 1.23 sec                                                               | 1.23 sec: 1.00x slower                                                        |
| xml_etree_process          | 57.7 ms                                                                | 58.1 ms: 1.01x slower                                                         |
| sqlglot_v2_normalize       | 106 ms                                                                 | 106 ms: 1.01x slower                                                          |
| comprehensions             | 16.6 us                                                                | 16.7 us: 1.01x slower                                                         |
| xml_etree_generate         | 82.9 ms                                                                | 83.5 ms: 1.01x slower                                                         |
| generators                 | 29.6 ms                                                                | 29.9 ms: 1.01x slower                                                         |
| docutils                   | 2.59 sec                                                               | 2.61 sec: 1.01x slower                                                        |
| bench_thread_pool          | 874 us                                                                 | 882 us: 1.01x slower                                                          |
| 2to3                       | 250 ms                                                                 | 252 ms: 1.01x slower                                                          |
| sympy_sum                  | 148 ms                                                                 | 149 ms: 1.01x slower                                                          |
| sqlglot_v2_optimize        | 52.0 ms                                                                | 52.5 ms: 1.01x slower                                                         |
| async_tree_none_tg         | 246 ms                                                                 | 248 ms: 1.01x slower                                                          |
| sqlalchemy_declarative     | 131 ms                                                                 | 133 ms: 1.01x slower                                                          |
| many_optionals             | 922 us                                                                 | 932 us: 1.01x slower                                                          |
| sympy_str                  | 266 ms                                                                 | 269 ms: 1.01x slower                                                          |
| deepcopy_memo              | 28.5 us                                                                | 28.9 us: 1.01x slower                                                         |
| async_tree_memoization     | 309 ms                                                                 | 313 ms: 1.01x slower                                                          |
| go                         | 109 ms                                                                 | 110 ms: 1.01x slower                                                          |
| bpe_tokeniser              | 4.51 sec                                                               | 4.57 sec: 1.01x slower                                                        |
| pprint_pformat             | 1.44 sec                                                               | 1.46 sec: 1.01x slower                                                        |
| logging_simple             | 5.56 us                                                                | 5.63 us: 1.01x slower                                                         |
| sympy_expand               | 453 ms                                                                 | 459 ms: 1.01x slower                                                          |
| genshi_text                | 20.6 ms                                                                | 20.9 ms: 1.01x slower                                                         |
| subparsers                 | 20.5 ms                                                                | 20.8 ms: 1.01x slower                                                         |
| regex_compile              | 123 ms                                                                 | 125 ms: 1.02x slower                                                          |
| sqlite_synth               | 2.79 us                                                                | 2.84 us: 1.02x slower                                                         |
| pprint_safe_repr           | 704 ms                                                                 | 717 ms: 1.02x slower                                                          |
| logging_format             | 6.10 us                                                                | 6.22 us: 1.02x slower                                                         |
| async_tree_cpu_io_mixed_tg | 474 ms                                                                 | 483 ms: 1.02x slower                                                          |
| genshi_xml                 | 48.6 ms                                                                | 49.5 ms: 1.02x slower                                                         |
| async_tree_cpu_io_mixed    | 479 ms                                                                 | 489 ms: 1.02x slower                                                          |
| scimark_sor                | 115 ms                                                                 | 118 ms: 1.02x slower                                                          |
| json_loads                 | 29.8 us                                                                | 30.5 us: 1.02x slower                                                         |
| pathlib                    | 16.5 ms                                                                | 16.9 ms: 1.02x slower                                                         |
| html5lib                   | 60.8 ms                                                                | 62.2 ms: 1.02x slower                                                         |
| json                       | 5.41 ms                                                                | 5.54 ms: 1.02x slower                                                         |
| nqueens                    | 79.6 ms                                                                | 81.6 ms: 1.02x slower                                                         |
| dulwich_log                | 58.6 ms                                                                | 60.1 ms: 1.03x slower                                                         |
| coroutines                 | 23.3 ms                                                                | 23.9 ms: 1.03x slower                                                         |
| async_tree_none            | 255 ms                                                                 | 262 ms: 1.03x slower                                                          |
| deepcopy                   | 244 us                                                                 | 251 us: 1.03x slower                                                          |
| tomli_loads                | 1.94 sec                                                               | 2.00 sec: 1.03x slower                                                        |
| telco                      | 7.72 ms                                                                | 7.98 ms: 1.03x slower                                                         |
| regex_v8                   | 22.9 ms                                                                | 23.9 ms: 1.04x slower                                                         |
| raytrace                   | 252 ms                                                                 | 265 ms: 1.05x slower                                                          |
| deepcopy_reduce            | 2.55 us                                                                | 2.69 us: 1.05x slower                                                         |
| crypto_pyaes               | 71.3 ms                                                                | 75.4 ms: 1.06x slower                                                         |
| scimark_monte_carlo        | 63.8 ms                                                                | 67.5 ms: 1.06x slower                                                         |
| async_generators           | 384 ms                                                                 | 407 ms: 1.06x slower                                                          |
| chaos                      | 54.3 ms                                                                | 57.7 ms: 1.06x slower                                                         |
| float                      | 66.1 ms                                                                | 70.3 ms: 1.06x slower                                                         |
| scimark_fft                | 341 ms                                                                 | 366 ms: 1.07x slower                                                          |
| spectral_norm              | 98.3 ms                                                                | 107 ms: 1.09x slower                                                          |
| scimark_sparse_mat_mult    | 4.63 ms                                                                | 5.10 ms: 1.10x slower                                                         |
| nbody                      | 87.8 ms                                                                | 97.1 ms: 1.10x slower                                                         |
| Geometric mean             | (ref)                                                                  | 1.01x slower                                                                  |

Benchmark hidden because not significant (15): k_core, shortest_path, asyncio_websockets, create_gc_cycles, coverage, connected_components, fannkuch, scimark_lu, typing_runtime_protocols, xml_etree_parse, async_tree_io_tg, sphinx, pylint, async_tree_io, async_tree_memoization_tg

- Geometric mean (including insignificant results): 1.013x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x