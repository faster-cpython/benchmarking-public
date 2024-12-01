# Results vs. 3.13.0

- fork: python
- ref: 328187cc4fcdd578db42
- machine: darwin-arm64
- commit hash: 328187c
- commit date: 2024-11-30
- overall geometric mean: 1.026x faster
- HPT reliability: 89.83%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241130-darwin-arm64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 187 ms                                                 | 203 ms: 1.08x slower                                                   |
| docutils       | 1.44 sec                                               | 1.52 sec: 1.06x slower                                                 |
| html5lib       | 36.6 ms                                                | 33.3 ms: 1.10x faster                                                  |
| sphinx         | 603 ms                                                 | 630 ms: 1.05x slower                                                   |
| Geometric mean | (ref)                                                  | 1.02x slower                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241130-darwin-arm64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| coroutines                       | 19.8 ms                                                | 17.5 ms: 1.13x faster                                                  |
| async_tree_memoization_tg        | 288 ms                                                 | 257 ms: 1.12x faster                                                   |
| async_tree_memoization           | 268 ms                                                 | 252 ms: 1.06x faster                                                   |
| async_tree_eager_tg              | 47.8 ms                                                | 45.4 ms: 1.05x faster                                                  |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 133 ms: 1.03x faster                                                   |
| async_tree_eager                 | 70.1 ms                                                | 67.9 ms: 1.03x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 165 ms: 1.02x faster                                                   |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 365 ms: 1.02x faster                                                   |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 345 ms: 1.01x faster                                                   |
| async_generators                 | 295 ms                                                 | 304 ms: 1.03x slower                                                   |
| async_tree_cpu_io_mixed          | 460 ms                                                 | 474 ms: 1.03x slower                                                   |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 476 ms: 1.06x slower                                                   |
| async_tree_io_tg                 | 497 ms                                                 | 593 ms: 1.19x slower                                                   |
| async_tree_io                    | 507 ms                                                 | 609 ms: 1.20x slower                                                   |
| async_tree_eager_io              | 514 ms                                                 | 714 ms: 1.39x slower                                                   |
| async_tree_eager_io_tg           | 477 ms                                                 | 705 ms: 1.48x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.04x slower                                                           |

Benchmark hidden because not significant (3): async_tree_none, asyncio_websockets, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241130-darwin-arm64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 74.0 ms                                                | 63.5 ms: 1.17x faster                                                  |
| float          | 56.0 ms                                                | 48.9 ms: 1.15x faster                                                  |
| Geometric mean | (ref)                                                  | 1.10x faster                                                           |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241130-darwin-arm64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.01 ms: 1.30x faster                                                  |
| regex_dna      | 149 ms                                                 | 135 ms: 1.10x faster                                                   |
| regex_compile  | 78.6 ms                                                | 71.9 ms: 1.09x faster                                                  |
| regex_v8       | 17.0 ms                                                | 16.0 ms: 1.06x faster                                                  |
| Geometric mean | (ref)                                                  | 1.14x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241130-darwin-arm64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| unpickle_pure_python | 164 us                                                 | 126 us: 1.31x faster                                                   |
| tomli_loads          | 1.57 sec                                               | 1.26 sec: 1.24x faster                                                 |
| xml_etree_process    | 41.0 ms                                                | 35.7 ms: 1.15x faster                                                  |
| xml_etree_generate   | 57.0 ms                                                | 50.7 ms: 1.12x faster                                                  |
| pickle_pure_python   | 214 us                                                 | 195 us: 1.10x faster                                                   |
| json_loads           | 17.0 us                                                | 16.5 us: 1.02x faster                                                  |
| xml_etree_iterparse  | 73.6 ms                                                | 74.5 ms: 1.01x slower                                                  |
| xml_etree_parse      | 107 ms                                                 | 110 ms: 1.02x slower                                                   |
| json_dumps           | 6.52 ms                                                | 7.21 ms: 1.11x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.08x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241130-darwin-arm64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 14.5 ms                                                | 15.7 ms: 1.08x slower                                                  |
| python_startup         | 18.9 ms                                                | 20.5 ms: 1.08x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.08x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241130-darwin-arm64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 7.68 ms                                                | 6.24 ms: 1.23x faster                                                  |
| genshi_text     | 16.9 ms                                                | 16.8 ms: 1.01x faster                                                  |
| django_template | 22.2 ms                                                | 23.0 ms: 1.03x slower                                                  |
| genshi_xml      | 34.4 ms                                                | 39.3 ms: 1.14x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                           |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241130-darwin-arm64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| deepcopy_memo                    | 27.4 us                                                | 17.5 us: 1.56x faster                                                  |
| deepcopy                         | 237 us                                                 | 161 us: 1.47x faster                                                   |
| deepcopy_reduce                  | 2.07 us                                                | 1.58 us: 1.31x faster                                                  |
| unpickle_pure_python             | 164 us                                                 | 126 us: 1.31x faster                                                   |
| regex_effbot                     | 2.63 ms                                                | 2.01 ms: 1.30x faster                                                  |
| tomli_loads                      | 1.57 sec                                               | 1.26 sec: 1.24x faster                                                 |
| mako                             | 7.68 ms                                                | 6.24 ms: 1.23x faster                                                  |
| scimark_sor                      | 105 ms                                                 | 87.8 ms: 1.20x faster                                                  |
| generators                       | 31.5 ms                                                | 26.8 ms: 1.18x faster                                                  |
| nbody                            | 74.0 ms                                                | 63.5 ms: 1.17x faster                                                  |
| xml_etree_process                | 41.0 ms                                                | 35.7 ms: 1.15x faster                                                  |
| float                            | 56.0 ms                                                | 48.9 ms: 1.15x faster                                                  |
| go                               | 115 ms                                                 | 101 ms: 1.14x faster                                                   |
| coroutines                       | 19.8 ms                                                | 17.5 ms: 1.13x faster                                                  |
| xml_etree_generate               | 57.0 ms                                                | 50.7 ms: 1.12x faster                                                  |
| async_tree_memoization_tg        | 288 ms                                                 | 257 ms: 1.12x faster                                                   |
| pylint                           | 180 ms                                                 | 161 ms: 1.12x faster                                                   |
| scimark_monte_carlo              | 50.4 ms                                                | 45.3 ms: 1.11x faster                                                  |
| pprint_safe_repr                 | 533 ms                                                 | 482 ms: 1.11x faster                                                   |
| scimark_lu                       | 76.7 ms                                                | 69.3 ms: 1.11x faster                                                  |
| pprint_pformat                   | 1.08 sec                                               | 982 ms: 1.10x faster                                                   |
| regex_dna                        | 149 ms                                                 | 135 ms: 1.10x faster                                                   |
| html5lib                         | 36.6 ms                                                | 33.3 ms: 1.10x faster                                                  |
| pickle_pure_python               | 214 us                                                 | 195 us: 1.10x faster                                                   |
| spectral_norm                    | 76.3 ms                                                | 69.6 ms: 1.10x faster                                                  |
| regex_compile                    | 78.6 ms                                                | 71.9 ms: 1.09x faster                                                  |
| scimark_fft                      | 201 ms                                                 | 186 ms: 1.08x faster                                                   |
| pyflate                          | 351 ms                                                 | 327 ms: 1.07x faster                                                   |
| bpe_tokeniser                    | 3.25 sec                                               | 3.05 sec: 1.07x faster                                                 |
| async_tree_memoization           | 268 ms                                                 | 252 ms: 1.06x faster                                                   |
| regex_v8                         | 17.0 ms                                                | 16.0 ms: 1.06x faster                                                  |
| json                             | 3.03 ms                                                | 2.85 ms: 1.06x faster                                                  |
| connected_components             | 319 ms                                                 | 301 ms: 1.06x faster                                                   |
| logging_simple                   | 3.60 us                                                | 3.40 us: 1.06x faster                                                  |
| thrift                           | 466 us                                                 | 442 us: 1.05x faster                                                   |
| async_tree_eager_tg              | 47.8 ms                                                | 45.4 ms: 1.05x faster                                                  |
| shortest_path                    | 347 ms                                                 | 330 ms: 1.05x faster                                                   |
| telco                            | 4.76 ms                                                | 4.54 ms: 1.05x faster                                                  |
| logging_format                   | 3.89 us                                                | 3.72 us: 1.05x faster                                                  |
| pycparser                        | 705 ms                                                 | 681 ms: 1.04x faster                                                   |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 133 ms: 1.03x faster                                                   |
| async_tree_eager                 | 70.1 ms                                                | 67.9 ms: 1.03x faster                                                  |
| pathlib                          | 23.4 ms                                                | 22.7 ms: 1.03x faster                                                  |
| richards                         | 35.2 ms                                                | 34.2 ms: 1.03x faster                                                  |
| bench_thread_pool                | 505 us                                                 | 492 us: 1.03x faster                                                   |
| json_loads                       | 17.0 us                                                | 16.5 us: 1.02x faster                                                  |
| deltablue                        | 2.68 ms                                                | 2.61 ms: 1.02x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 165 ms: 1.02x faster                                                   |
| coverage                         | 46.0 ms                                                | 44.9 ms: 1.02x faster                                                  |
| typing_runtime_protocols         | 101 us                                                 | 99.1 us: 1.02x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 365 ms: 1.02x faster                                                   |
| richards_super                   | 39.1 ms                                                | 38.4 ms: 1.02x faster                                                  |
| bench_mp_pool                    | 62.5 ms                                                | 61.9 ms: 1.01x faster                                                  |
| meteor_contest                   | 74.0 ms                                                | 73.3 ms: 1.01x faster                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 345 ms: 1.01x faster                                                   |
| genshi_text                      | 16.9 ms                                                | 16.8 ms: 1.01x faster                                                  |
| sympy_expand                     | 246 ms                                                 | 248 ms: 1.01x slower                                                   |
| sympy_str                        | 145 ms                                                 | 147 ms: 1.01x slower                                                   |
| crypto_pyaes                     | 54.2 ms                                                | 54.8 ms: 1.01x slower                                                  |
| sqlglot_optimize                 | 34.9 ms                                                | 35.3 ms: 1.01x slower                                                  |
| xml_etree_iterparse              | 73.6 ms                                                | 74.5 ms: 1.01x slower                                                  |
| sqlalchemy_declarative           | 58.9 ms                                                | 59.6 ms: 1.01x slower                                                  |
| raytrace                         | 181 ms                                                 | 183 ms: 1.01x slower                                                   |
| gc_traversal                     | 2.91 ms                                                | 2.96 ms: 1.02x slower                                                  |
| sympy_sum                        | 75.4 ms                                                | 76.9 ms: 1.02x slower                                                  |
| hexiom                           | 4.86 ms                                                | 4.97 ms: 1.02x slower                                                  |
| xml_etree_parse                  | 107 ms                                                 | 110 ms: 1.02x slower                                                   |
| scimark_sparse_mat_mult          | 2.99 ms                                                | 3.07 ms: 1.03x slower                                                  |
| sqlglot_parse                    | 856 us                                                 | 880 us: 1.03x slower                                                   |
| async_generators                 | 295 ms                                                 | 304 ms: 1.03x slower                                                   |
| async_tree_cpu_io_mixed          | 460 ms                                                 | 474 ms: 1.03x slower                                                   |
| django_template                  | 22.2 ms                                                | 23.0 ms: 1.03x slower                                                  |
| sqlglot_transpile                | 1.02 ms                                                | 1.06 ms: 1.04x slower                                                  |
| sqlglot_normalize                | 189 ms                                                 | 197 ms: 1.05x slower                                                   |
| sphinx                           | 603 ms                                                 | 630 ms: 1.05x slower                                                   |
| dulwich_log                      | 28.5 ms                                                | 29.9 ms: 1.05x slower                                                  |
| chaos                            | 41.2 ms                                                | 43.4 ms: 1.05x slower                                                  |
| docutils                         | 1.44 sec                                               | 1.52 sec: 1.06x slower                                                 |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 476 ms: 1.06x slower                                                   |
| mdp                              | 1.49 sec                                               | 1.59 sec: 1.06x slower                                                 |
| sympy_integrate                  | 11.3 ms                                                | 12.1 ms: 1.07x slower                                                  |
| 2to3                             | 187 ms                                                 | 203 ms: 1.08x slower                                                   |
| python_startup_no_site           | 14.5 ms                                                | 15.7 ms: 1.08x slower                                                  |
| python_startup                   | 18.9 ms                                                | 20.5 ms: 1.08x slower                                                  |
| logging_silent                   | 70.1 ns                                                | 76.5 ns: 1.09x slower                                                  |
| json_dumps                       | 6.52 ms                                                | 7.21 ms: 1.11x slower                                                  |
| comprehensions                   | 12.3 us                                                | 13.7 us: 1.11x slower                                                  |
| create_gc_cycles                 | 1.17 ms                                                | 1.32 ms: 1.13x slower                                                  |
| genshi_xml                       | 34.4 ms                                                | 39.3 ms: 1.14x slower                                                  |
| k_core                           | 1.61 sec                                               | 1.87 sec: 1.16x slower                                                 |
| async_tree_io_tg                 | 497 ms                                                 | 593 ms: 1.19x slower                                                   |
| async_tree_io                    | 507 ms                                                 | 609 ms: 1.20x slower                                                   |
| async_tree_eager_io              | 514 ms                                                 | 714 ms: 1.39x slower                                                   |
| async_tree_eager_io_tg           | 477 ms                                                 | 705 ms: 1.48x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.03x faster                                                           |

Benchmark hidden because not significant (7): async_tree_none, fannkuch, pidigits, asyncio_websockets, sqlalchemy_imperative, nqueens, async_tree_none_tg
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, dask, gevent_hub, mypy2, tornado_http
Ignored benchmarks (3) of results/bm-20241130-3.14.0a2+-328187c-JIT/bm-20241130-darwin-arm64-python-328187cc4fcdd578db42-3.14.0a2+-328187c.json: many_optionals, sqlite_synth, subparsers

- Geometric mean (including insignificant results): 1.026x faster

# HPT report

- Reliability score: 89.83% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.05x