# Results vs. 3.10.4

- fork: python
- ref: 3.14
- machine: darwin-arm64
- commit hash: 964c29d
- commit date: 2025-06-16
- overall geometric mean: 1.240x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.09x faster
- Memory change: 1.17x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250616-darwin-arm64-python-3.14-3.14.0b2+-964c29d |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 190 ms: 1.06x faster                                   |
| docutils       | 1.74 sec                                               | 1.52 sec: 1.14x faster                                 |
| html5lib       | 43.5 ms                                                | 34.3 ms: 1.27x faster                                  |
| sphinx         | 729 ms                                                 | 620 ms: 1.18x faster                                   |
| Geometric mean | (ref)                                                  | 1.16x faster                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250616-darwin-arm64-python-3.14-3.14.0b2+-964c29d |
|-------------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 73.1 ms: 5.36x faster                                  |
| async_tree_eager_memoization  | 483 ms                                                 | 151 ms: 3.19x faster                                   |
| async_tree_eager_io           | 1.01 sec                                               | 393 ms: 2.58x faster                                   |
| async_tree_io                 | 1.02 sec                                               | 414 ms: 2.46x faster                                   |
| async_tree_memoization        | 481 ms                                                 | 216 ms: 2.23x faster                                   |
| async_tree_none               | 391 ms                                                 | 183 ms: 2.14x faster                                   |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 368 ms: 1.82x faster                                   |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 434 ms: 1.54x faster                                   |
| coroutines                    | 20.5 ms                                                | 19.3 ms: 1.06x faster                                  |
| async_generators              | 233 ms                                                 | 274 ms: 1.17x slower                                   |
| Geometric mean                | (ref)                                                  | 1.92x faster                                           |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250616-darwin-arm64-python-3.14-3.14.0b2+-964c29d |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| float          | 72.4 ms                                                | 58.4 ms: 1.24x faster                                  |
| nbody          | 92.5 ms                                                | 86.5 ms: 1.07x faster                                  |
| pidigits       | 280 ms                                                 | 283 ms: 1.01x slower                                   |
| Geometric mean | (ref)                                                  | 1.10x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250616-darwin-arm64-python-3.14-3.14.0b2+-964c29d |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_dna      | 175 ms                                                 | 143 ms: 1.22x faster                                   |
| regex_v8       | 19.1 ms                                                | 16.2 ms: 1.18x faster                                  |
| regex_compile  | 95.6 ms                                                | 81.9 ms: 1.17x faster                                  |
| regex_effbot   | 2.34 ms                                                | 2.34 ms: 1.00x slower                                  |
| Geometric mean | (ref)                                                  | 1.14x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250616-darwin-arm64-python-3.14-3.14.0b2+-964c29d |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| json_dumps           | 8.31 ms                                                | 6.78 ms: 1.23x faster                                  |
| pickle_pure_python   | 285 us                                                 | 242 us: 1.18x faster                                   |
| tomli_loads          | 1.72 sec                                               | 1.47 sec: 1.17x faster                                 |
| unpickle_pure_python | 198 us                                                 | 177 us: 1.12x faster                                   |
| xml_etree_parse      | 109 ms                                                 | 101 ms: 1.09x faster                                   |
| xml_etree_process    | 44.6 ms                                                | 43.7 ms: 1.02x faster                                  |
| xml_etree_generate   | 53.9 ms                                                | 58.5 ms: 1.09x slower                                  |
| json_loads           | 16.6 us                                                | 18.1 us: 1.09x slower                                  |
| Geometric mean       | (ref)                                                  | 1.07x faster                                           |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250616-darwin-arm64-python-3.14-3.14.0b2+-964c29d |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 19.6 ms                                                | 18.4 ms: 1.07x faster                                  |
| python_startup_no_site | 12.8 ms                                                | 13.4 ms: 1.05x slower                                  |
| Geometric mean         | (ref)                                                  | 1.01x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250616-darwin-arm64-python-3.14-3.14.0b2+-964c29d |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 9.81 ms                                                | 8.79 ms: 1.12x faster                                  |
| genshi_text     | 17.7 ms                                                | 17.8 ms: 1.01x slower                                  |
| django_template | 24.4 ms                                                | 25.6 ms: 1.05x slower                                  |
| genshi_xml      | 35.1 ms                                                | 37.0 ms: 1.05x slower                                  |
| Geometric mean  | (ref)                                                  | 1.00x faster                                           |

All benchmarks:
===============

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250616-darwin-arm64-python-3.14-3.14.0b2+-964c29d |
|-------------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 73.1 ms: 5.36x faster                                  |
| async_tree_eager_memoization  | 483 ms                                                 | 151 ms: 3.19x faster                                   |
| typing_runtime_protocols      | 326 us                                                 | 116 us: 2.82x faster                                   |
| subparsers                    | 39.8 ms                                                | 14.9 ms: 2.66x faster                                  |
| async_tree_eager_io           | 1.01 sec                                               | 393 ms: 2.58x faster                                   |
| async_tree_io                 | 1.02 sec                                               | 414 ms: 2.46x faster                                   |
| async_tree_memoization        | 481 ms                                                 | 216 ms: 2.23x faster                                   |
| async_tree_none               | 391 ms                                                 | 183 ms: 2.14x faster                                   |
| mdp                           | 1.65 sec                                               | 844 ms: 1.95x faster                                   |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 368 ms: 1.82x faster                                   |
| deltablue                     | 4.99 ms                                                | 2.77 ms: 1.80x faster                                  |
| go                            | 163 ms                                                 | 103 ms: 1.59x faster                                   |
| deepcopy                      | 276 us                                                 | 177 us: 1.56x faster                                   |
| deepcopy_memo                 | 34.7 us                                                | 22.3 us: 1.56x faster                                  |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 434 ms: 1.54x faster                                   |
| raytrace                      | 327 ms                                                 | 213 ms: 1.54x faster                                   |
| scimark_sor                   | 140 ms                                                 | 92.3 ms: 1.52x faster                                  |
| richards_super                | 61.0 ms                                                | 41.6 ms: 1.47x faster                                  |
| richards                      | 52.3 ms                                                | 37.2 ms: 1.41x faster                                  |
| chaos                         | 67.7 ms                                                | 48.3 ms: 1.40x faster                                  |
| k_core                        | 2.01 sec                                               | 1.47 sec: 1.37x faster                                 |
| pylint                        | 231 ms                                                 | 169 ms: 1.36x faster                                   |
| scimark_monte_carlo           | 72.4 ms                                                | 53.3 ms: 1.36x faster                                  |
| dulwich_log                   | 35.6 ms                                                | 26.9 ms: 1.32x faster                                  |
| pyflate                       | 448 ms                                                 | 340 ms: 1.32x faster                                   |
| html5lib                      | 43.5 ms                                                | 34.3 ms: 1.27x faster                                  |
| spectral_norm                 | 95.3 ms                                                | 76.5 ms: 1.25x faster                                  |
| comprehensions                | 17.3 us                                                | 13.9 us: 1.24x faster                                  |
| float                         | 72.4 ms                                                | 58.4 ms: 1.24x faster                                  |
| sqlalchemy_imperative         | 9.07 ms                                                | 7.33 ms: 1.24x faster                                  |
| json_dumps                    | 8.31 ms                                                | 6.78 ms: 1.23x faster                                  |
| regex_dna                     | 175 ms                                                 | 143 ms: 1.22x faster                                   |
| deepcopy_reduce               | 2.32 us                                                | 1.90 us: 1.22x faster                                  |
| scimark_lu                    | 103 ms                                                 | 84.6 ms: 1.21x faster                                  |
| hexiom                        | 6.25 ms                                                | 5.17 ms: 1.21x faster                                  |
| crypto_pyaes                  | 73.3 ms                                                | 61.2 ms: 1.20x faster                                  |
| pycparser                     | 887 ms                                                 | 745 ms: 1.19x faster                                   |
| regex_v8                      | 19.1 ms                                                | 16.2 ms: 1.18x faster                                  |
| pickle_pure_python            | 285 us                                                 | 242 us: 1.18x faster                                   |
| sphinx                        | 729 ms                                                 | 620 ms: 1.18x faster                                   |
| tomli_loads                   | 1.72 sec                                               | 1.47 sec: 1.17x faster                                 |
| regex_compile                 | 95.6 ms                                                | 81.9 ms: 1.17x faster                                  |
| sqlalchemy_declarative        | 75.7 ms                                                | 64.9 ms: 1.17x faster                                  |
| sympy_integrate               | 13.2 ms                                                | 11.5 ms: 1.15x faster                                  |
| logging_format                | 5.03 us                                                | 4.41 us: 1.14x faster                                  |
| docutils                      | 1.74 sec                                               | 1.52 sec: 1.14x faster                                 |
| sympy_sum                     | 92.7 ms                                                | 81.9 ms: 1.13x faster                                  |
| pathlib                       | 25.7 ms                                                | 23.0 ms: 1.12x faster                                  |
| logging_simple                | 4.59 us                                                | 4.11 us: 1.12x faster                                  |
| unpickle_pure_python          | 198 us                                                 | 177 us: 1.12x faster                                   |
| mako                          | 9.81 ms                                                | 8.79 ms: 1.12x faster                                  |
| pprint_pformat                | 1.33 sec                                               | 1.20 sec: 1.10x faster                                 |
| scimark_fft                   | 225 ms                                                 | 206 ms: 1.10x faster                                   |
| pprint_safe_repr              | 648 ms                                                 | 594 ms: 1.09x faster                                   |
| xml_etree_parse               | 109 ms                                                 | 101 ms: 1.09x faster                                   |
| connected_components          | 318 ms                                                 | 297 ms: 1.07x faster                                   |
| scimark_sparse_mat_mult       | 3.42 ms                                                | 3.19 ms: 1.07x faster                                  |
| nbody                         | 92.5 ms                                                | 86.5 ms: 1.07x faster                                  |
| python_startup                | 19.6 ms                                                | 18.4 ms: 1.07x faster                                  |
| sympy_str                     | 166 ms                                                 | 156 ms: 1.06x faster                                   |
| 2to3                          | 201 ms                                                 | 190 ms: 1.06x faster                                   |
| coroutines                    | 20.5 ms                                                | 19.3 ms: 1.06x faster                                  |
| bpe_tokeniser                 | 3.44 sec                                               | 3.26 sec: 1.06x faster                                 |
| meteor_contest                | 77.8 ms                                                | 75.0 ms: 1.04x faster                                  |
| dask                          | 789 ms                                                 | 771 ms: 1.02x faster                                   |
| xml_etree_process             | 44.6 ms                                                | 43.7 ms: 1.02x faster                                  |
| json                          | 3.10 ms                                                | 3.04 ms: 1.02x faster                                  |
| sympy_expand                  | 269 ms                                                 | 264 ms: 1.02x faster                                   |
| shortest_path                 | 328 ms                                                 | 326 ms: 1.01x faster                                   |
| generators                    | 31.7 ms                                                | 31.6 ms: 1.00x faster                                  |
| regex_effbot                  | 2.34 ms                                                | 2.34 ms: 1.00x slower                                  |
| genshi_text                   | 17.7 ms                                                | 17.8 ms: 1.01x slower                                  |
| pidigits                      | 280 ms                                                 | 283 ms: 1.01x slower                                   |
| fannkuch                      | 303 ms                                                 | 309 ms: 1.02x slower                                   |
| many_optionals                | 486 us                                                 | 500 us: 1.03x slower                                   |
| python_startup_no_site        | 12.8 ms                                                | 13.4 ms: 1.05x slower                                  |
| django_template               | 24.4 ms                                                | 25.6 ms: 1.05x slower                                  |
| genshi_xml                    | 35.1 ms                                                | 37.0 ms: 1.05x slower                                  |
| xml_etree_generate            | 53.9 ms                                                | 58.5 ms: 1.09x slower                                  |
| json_loads                    | 16.6 us                                                | 18.1 us: 1.09x slower                                  |
| sqlite_synth                  | 1.48 us                                                | 1.63 us: 1.10x slower                                  |
| nqueens                       | 63.8 ms                                                | 71.9 ms: 1.13x slower                                  |
| create_gc_cycles              | 1.16 ms                                                | 1.36 ms: 1.16x slower                                  |
| async_generators              | 233 ms                                                 | 274 ms: 1.17x slower                                   |
| gc_traversal                  | 2.71 ms                                                | 3.20 ms: 1.18x slower                                  |
| coverage                      | 41.2 ms                                                | 49.8 ms: 1.21x slower                                  |
| telco                         | 3.49 ms                                                | 4.72 ms: 1.35x slower                                  |
| logging_silent                | 117 ns                                                 | 342 ns: 2.92x slower                                   |
| Geometric mean                | (ref)                                                  | 1.22x faster                                           |

Benchmark hidden because not significant (2): xml_etree_iterparse, asyncio_websockets
Ignored benchmarks (11) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (12) of results/bm-20250616-3.14.0b2+-964c29d/bm-20250616-darwin-arm64-python-3.14-3.14.0b2+-964c29d.json: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.240x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.12x
- 95% likely to have a speedup of 1.11x
- 99% likely to have a speedup of 1.09x

# Memory
- memory change: 1.17x