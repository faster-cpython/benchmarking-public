# Results vs. 3.10.4

- fork: faster-cpython
- ref: virtual_iterators
- machine: darwin-arm64
- commit hash: a4b740d
- commit date: 2025-04-16
- overall geometric mean: 1.233x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x faster
- Memory change: 1.15x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250416-darwin-arm64-faster%2dcpython-virtual_iterators-3.14.0a7+-a4b740d |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 218 ms: 1.08x slower                                                          |
| docutils       | 1.74 sec                                               | 1.59 sec: 1.09x faster                                                        |
| html5lib       | 43.5 ms                                                | 36.3 ms: 1.20x faster                                                         |
| sphinx         | 729 ms                                                 | 620 ms: 1.18x faster                                                          |
| Geometric mean | (ref)                                                  | 1.09x faster                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250416-darwin-arm64-faster%2dcpython-virtual_iterators-3.14.0a7+-a4b740d |
|-------------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 75.2 ms: 5.21x faster                                                         |
| async_tree_eager_memoization  | 483 ms                                                 | 152 ms: 3.18x faster                                                          |
| async_tree_eager_io           | 1.01 sec                                               | 405 ms: 2.51x faster                                                          |
| async_tree_io                 | 1.02 sec                                               | 424 ms: 2.40x faster                                                          |
| async_tree_memoization        | 481 ms                                                 | 221 ms: 2.18x faster                                                          |
| async_tree_none               | 391 ms                                                 | 185 ms: 2.12x faster                                                          |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 370 ms: 1.81x faster                                                          |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 431 ms: 1.55x faster                                                          |
| coroutines                    | 20.5 ms                                                | 20.3 ms: 1.01x faster                                                         |
| asyncio_websockets            | 242 ms                                                 | 245 ms: 1.01x slower                                                          |
| async_generators              | 233 ms                                                 | 272 ms: 1.17x slower                                                          |
| Geometric mean                | (ref)                                                  | 1.89x faster                                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250416-darwin-arm64-faster%2dcpython-virtual_iterators-3.14.0a7+-a4b740d |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| float          | 72.4 ms                                                | 56.4 ms: 1.28x faster                                                         |
| nbody          | 92.5 ms                                                | 87.0 ms: 1.06x faster                                                         |
| pidigits       | 280 ms                                                 | 284 ms: 1.01x slower                                                          |
| Geometric mean | (ref)                                                  | 1.11x faster                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250416-darwin-arm64-faster%2dcpython-virtual_iterators-3.14.0a7+-a4b740d |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_dna      | 175 ms                                                 | 141 ms: 1.24x faster                                                          |
| regex_v8       | 19.1 ms                                                | 15.8 ms: 1.21x faster                                                         |
| regex_compile  | 95.6 ms                                                | 82.8 ms: 1.15x faster                                                         |
| regex_effbot   | 2.34 ms                                                | 2.30 ms: 1.02x faster                                                         |
| Geometric mean | (ref)                                                  | 1.15x faster                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250416-darwin-arm64-faster%2dcpython-virtual_iterators-3.14.0a7+-a4b740d |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| tomli_loads          | 1.72 sec                                               | 1.48 sec: 1.16x faster                                                        |
| pickle_pure_python   | 285 us                                                 | 247 us: 1.15x faster                                                          |
| unpickle_pure_python | 198 us                                                 | 181 us: 1.09x faster                                                          |
| json_dumps           | 8.31 ms                                                | 7.78 ms: 1.07x faster                                                         |
| xml_etree_parse      | 109 ms                                                 | 107 ms: 1.02x faster                                                          |
| xml_etree_iterparse  | 74.5 ms                                                | 76.3 ms: 1.02x slower                                                         |
| xml_etree_process    | 44.6 ms                                                | 46.0 ms: 1.03x slower                                                         |
| json_loads           | 16.6 us                                                | 17.8 us: 1.07x slower                                                         |
| xml_etree_generate   | 53.9 ms                                                | 62.2 ms: 1.15x slower                                                         |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250416-darwin-arm64-faster%2dcpython-virtual_iterators-3.14.0a7+-a4b740d |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup         | 19.6 ms                                                | 19.0 ms: 1.03x faster                                                         |
| python_startup_no_site | 12.8 ms                                                | 14.7 ms: 1.15x slower                                                         |
| Geometric mean         | (ref)                                                  | 1.05x slower                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250416-darwin-arm64-faster%2dcpython-virtual_iterators-3.14.0a7+-a4b740d |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mako            | 9.81 ms                                                | 8.88 ms: 1.10x faster                                                         |
| genshi_xml      | 35.1 ms                                                | 37.4 ms: 1.06x slower                                                         |
| genshi_text     | 17.7 ms                                                | 19.4 ms: 1.10x slower                                                         |
| django_template | 24.4 ms                                                | 26.9 ms: 1.11x slower                                                         |
| Geometric mean  | (ref)                                                  | 1.04x slower                                                                  |

All benchmarks:
===============

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250416-darwin-arm64-faster%2dcpython-virtual_iterators-3.14.0a7+-a4b740d |
|-------------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 75.2 ms: 5.21x faster                                                         |
| async_tree_eager_memoization  | 483 ms                                                 | 152 ms: 3.18x faster                                                          |
| typing_runtime_protocols      | 326 us                                                 | 105 us: 3.11x faster                                                          |
| subparsers                    | 39.8 ms                                                | 13.6 ms: 2.94x faster                                                         |
| async_tree_eager_io           | 1.01 sec                                               | 405 ms: 2.51x faster                                                          |
| async_tree_io                 | 1.02 sec                                               | 424 ms: 2.40x faster                                                          |
| async_tree_memoization        | 481 ms                                                 | 221 ms: 2.18x faster                                                          |
| async_tree_none               | 391 ms                                                 | 185 ms: 2.12x faster                                                          |
| mdp                           | 1.65 sec                                               | 849 ms: 1.94x faster                                                          |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 370 ms: 1.81x faster                                                          |
| deltablue                     | 4.99 ms                                                | 2.80 ms: 1.78x faster                                                         |
| raytrace                      | 327 ms                                                 | 202 ms: 1.61x faster                                                          |
| deepcopy                      | 276 us                                                 | 177 us: 1.55x faster                                                          |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 431 ms: 1.55x faster                                                          |
| go                            | 163 ms                                                 | 106 ms: 1.54x faster                                                          |
| deepcopy_memo                 | 34.7 us                                                | 23.1 us: 1.51x faster                                                         |
| logging_silent                | 117 ns                                                 | 78.0 ns: 1.50x faster                                                         |
| scimark_sor                   | 140 ms                                                 | 93.7 ms: 1.49x faster                                                         |
| chaos                         | 67.7 ms                                                | 49.2 ms: 1.38x faster                                                         |
| richards_super                | 61.0 ms                                                | 45.4 ms: 1.34x faster                                                         |
| richards                      | 52.3 ms                                                | 39.0 ms: 1.34x faster                                                         |
| dulwich_log                   | 35.6 ms                                                | 26.8 ms: 1.33x faster                                                         |
| comprehensions                | 17.3 us                                                | 13.1 us: 1.32x faster                                                         |
| pyflate                       | 448 ms                                                 | 338 ms: 1.32x faster                                                          |
| scimark_monte_carlo           | 72.4 ms                                                | 54.9 ms: 1.32x faster                                                         |
| k_core                        | 2.01 sec                                               | 1.54 sec: 1.31x faster                                                        |
| float                         | 72.4 ms                                                | 56.4 ms: 1.28x faster                                                         |
| spectral_norm                 | 95.3 ms                                                | 75.6 ms: 1.26x faster                                                         |
| regex_dna                     | 175 ms                                                 | 141 ms: 1.24x faster                                                          |
| deepcopy_reduce               | 2.32 us                                                | 1.90 us: 1.22x faster                                                         |
| hexiom                        | 6.25 ms                                                | 5.12 ms: 1.22x faster                                                         |
| sqlalchemy_imperative         | 9.07 ms                                                | 7.48 ms: 1.21x faster                                                         |
| scimark_lu                    | 103 ms                                                 | 84.6 ms: 1.21x faster                                                         |
| regex_v8                      | 19.1 ms                                                | 15.8 ms: 1.21x faster                                                         |
| html5lib                      | 43.5 ms                                                | 36.3 ms: 1.20x faster                                                         |
| crypto_pyaes                  | 73.3 ms                                                | 61.3 ms: 1.20x faster                                                         |
| pycparser                     | 887 ms                                                 | 750 ms: 1.18x faster                                                          |
| sphinx                        | 729 ms                                                 | 620 ms: 1.18x faster                                                          |
| sqlalchemy_declarative        | 75.7 ms                                                | 64.4 ms: 1.18x faster                                                         |
| logging_format                | 5.03 us                                                | 4.29 us: 1.17x faster                                                         |
| tomli_loads                   | 1.72 sec                                               | 1.48 sec: 1.16x faster                                                        |
| regex_compile                 | 95.6 ms                                                | 82.8 ms: 1.15x faster                                                         |
| logging_simple                | 4.59 us                                                | 3.98 us: 1.15x faster                                                         |
| pickle_pure_python            | 285 us                                                 | 247 us: 1.15x faster                                                          |
| pprint_pformat                | 1.33 sec                                               | 1.17 sec: 1.13x faster                                                        |
| pprint_safe_repr              | 648 ms                                                 | 578 ms: 1.12x faster                                                          |
| mako                          | 9.81 ms                                                | 8.88 ms: 1.10x faster                                                         |
| unpickle_pure_python          | 198 us                                                 | 181 us: 1.09x faster                                                          |
| docutils                      | 1.74 sec                                               | 1.59 sec: 1.09x faster                                                        |
| scimark_sparse_mat_mult       | 3.42 ms                                                | 3.18 ms: 1.07x faster                                                         |
| scimark_fft                   | 225 ms                                                 | 211 ms: 1.07x faster                                                          |
| json_dumps                    | 8.31 ms                                                | 7.78 ms: 1.07x faster                                                         |
| nbody                         | 92.5 ms                                                | 87.0 ms: 1.06x faster                                                         |
| pathlib                       | 25.7 ms                                                | 24.3 ms: 1.06x faster                                                         |
| bpe_tokeniser                 | 3.44 sec                                               | 3.32 sec: 1.04x faster                                                        |
| python_startup                | 19.6 ms                                                | 19.0 ms: 1.03x faster                                                         |
| xml_etree_parse               | 109 ms                                                 | 107 ms: 1.02x faster                                                          |
| meteor_contest                | 77.8 ms                                                | 76.1 ms: 1.02x faster                                                         |
| regex_effbot                  | 2.34 ms                                                | 2.30 ms: 1.02x faster                                                         |
| many_optionals                | 486 us                                                 | 478 us: 1.02x faster                                                          |
| coroutines                    | 20.5 ms                                                | 20.3 ms: 1.01x faster                                                         |
| bench_thread_pool             | 545 us                                                 | 542 us: 1.01x faster                                                          |
| connected_components          | 318 ms                                                 | 317 ms: 1.00x faster                                                          |
| pidigits                      | 280 ms                                                 | 284 ms: 1.01x slower                                                          |
| asyncio_websockets            | 242 ms                                                 | 245 ms: 1.01x slower                                                          |
| xml_etree_iterparse           | 74.5 ms                                                | 76.3 ms: 1.02x slower                                                         |
| xml_etree_process             | 44.6 ms                                                | 46.0 ms: 1.03x slower                                                         |
| shortest_path                 | 328 ms                                                 | 341 ms: 1.04x slower                                                          |
| fannkuch                      | 303 ms                                                 | 315 ms: 1.04x slower                                                          |
| genshi_xml                    | 35.1 ms                                                | 37.4 ms: 1.06x slower                                                         |
| sqlite_synth                  | 1.48 us                                                | 1.59 us: 1.07x slower                                                         |
| json_loads                    | 16.6 us                                                | 17.8 us: 1.07x slower                                                         |
| 2to3                          | 201 ms                                                 | 218 ms: 1.08x slower                                                          |
| genshi_text                   | 17.7 ms                                                | 19.4 ms: 1.10x slower                                                         |
| django_template               | 24.4 ms                                                | 26.9 ms: 1.11x slower                                                         |
| create_gc_cycles              | 1.16 ms                                                | 1.29 ms: 1.11x slower                                                         |
| nqueens                       | 63.8 ms                                                | 73.0 ms: 1.14x slower                                                         |
| python_startup_no_site        | 12.8 ms                                                | 14.7 ms: 1.15x slower                                                         |
| xml_etree_generate            | 53.9 ms                                                | 62.2 ms: 1.15x slower                                                         |
| gc_traversal                  | 2.71 ms                                                | 3.13 ms: 1.16x slower                                                         |
| async_generators              | 233 ms                                                 | 272 ms: 1.17x slower                                                          |
| bench_mp_pool                 | 56.0 ms                                                | 66.3 ms: 1.18x slower                                                         |
| coverage                      | 41.2 ms                                                | 48.8 ms: 1.19x slower                                                         |
| telco                         | 3.49 ms                                                | 4.90 ms: 1.40x slower                                                         |
| Geometric mean                | (ref)                                                  | 1.23x faster                                                                  |

Benchmark hidden because not significant (2): json, generators
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: chameleon, dask, djangocms, gevent_hub, pylint, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift, tornado_http
Ignored benchmarks (12) of results/bm-20250416-3.14.0a7+-a4b740d/bm-20250416-darwin-arm64-faster%2dcpython-virtual_iterators-3.14.0a7+-a4b740d.json: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.233x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.12x
- 95% likely to have a speedup of 1.11x
- 99% likely to have a speedup of 1.08x

# Memory
- memory change: 1.15x