# Results vs. 3.10.4

- fork: python
- ref: c9932a9ec8a3077933a8
- machine: darwin-arm64
- commit hash: c9932a9
- commit date: 2025-03-01
- overall geometric mean: 1.470x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.28x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250301-darwin-arm64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 151 ms: 1.33x faster                                                   |
| docutils       | 1.74 sec                                               | 1.36 sec: 1.28x faster                                                 |
| html5lib       | 43.5 ms                                                | 28.8 ms: 1.51x faster                                                  |
| sphinx         | 729 ms                                                 | 540 ms: 1.35x faster                                                   |
| Geometric mean | (ref)                                                  | 1.37x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250301-darwin-arm64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|-------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 56.6 ms: 6.93x faster                                                  |
| async_tree_eager_memoization  | 483 ms                                                 | 133 ms: 3.65x faster                                                   |
| async_tree_eager_io           | 1.01 sec                                               | 334 ms: 3.04x faster                                                   |
| async_tree_io                 | 1.02 sec                                               | 338 ms: 3.01x faster                                                   |
| async_tree_memoization        | 481 ms                                                 | 181 ms: 2.65x faster                                                   |
| async_tree_none               | 391 ms                                                 | 151 ms: 2.59x faster                                                   |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 345 ms: 1.94x faster                                                   |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 403 ms: 1.66x faster                                                   |
| coroutines                    | 20.5 ms                                                | 15.0 ms: 1.36x faster                                                  |
| async_generators              | 233 ms                                                 | 235 ms: 1.01x slower                                                   |
| asyncio_websockets            | 242 ms                                                 | 249 ms: 1.03x slower                                                   |
| Geometric mean                | (ref)                                                  | 2.23x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250301-darwin-arm64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 72.4 ms                                                | 44.1 ms: 1.64x faster                                                  |
| nbody          | 92.5 ms                                                | 63.3 ms: 1.46x faster                                                  |
| Geometric mean | (ref)                                                  | 1.34x faster                                                           |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250301-darwin-arm64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 95.6 ms                                                | 62.0 ms: 1.54x faster                                                  |
| regex_dna      | 175 ms                                                 | 145 ms: 1.21x faster                                                   |
| regex_v8       | 19.1 ms                                                | 17.8 ms: 1.08x faster                                                  |
| Geometric mean | (ref)                                                  | 1.19x faster                                                           |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250301-darwin-arm64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| unpickle_pure_python | 198 us                                                 | 125 us: 1.59x faster                                                   |
| pickle_pure_python   | 285 us                                                 | 184 us: 1.54x faster                                                   |
| tomli_loads          | 1.72 sec                                               | 1.14 sec: 1.51x faster                                                 |
| xml_etree_process    | 44.6 ms                                                | 33.5 ms: 1.33x faster                                                  |
| json_dumps           | 8.31 ms                                                | 7.10 ms: 1.17x faster                                                  |
| xml_etree_generate   | 53.9 ms                                                | 48.3 ms: 1.12x faster                                                  |
| xml_etree_iterparse  | 74.5 ms                                                | 68.4 ms: 1.09x faster                                                  |
| xml_etree_parse      | 109 ms                                                 | 101 ms: 1.09x faster                                                   |
| json_loads           | 16.6 us                                                | 17.9 us: 1.08x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.24x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250301-darwin-arm64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 19.6 ms                                                | 18.2 ms: 1.08x faster                                                  |
| python_startup_no_site | 12.8 ms                                                | 13.4 ms: 1.05x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.02x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250301-darwin-arm64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text     | 17.7 ms                                                | 12.6 ms: 1.41x faster                                                  |
| mako            | 9.81 ms                                                | 7.08 ms: 1.39x faster                                                  |
| genshi_xml      | 35.1 ms                                                | 27.0 ms: 1.30x faster                                                  |
| django_template | 24.4 ms                                                | 18.8 ms: 1.29x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.35x faster                                                           |

All benchmarks:
===============

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250301-darwin-arm64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|-------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 56.6 ms: 6.93x faster                                                  |
| typing_runtime_protocols      | 326 us                                                 | 83.9 us: 3.89x faster                                                  |
| async_tree_eager_memoization  | 483 ms                                                 | 133 ms: 3.65x faster                                                   |
| subparsers                    | 39.8 ms                                                | 11.3 ms: 3.52x faster                                                  |
| async_tree_eager_io           | 1.01 sec                                               | 334 ms: 3.04x faster                                                   |
| async_tree_io                 | 1.02 sec                                               | 338 ms: 3.01x faster                                                   |
| async_tree_memoization        | 481 ms                                                 | 181 ms: 2.65x faster                                                   |
| async_tree_none               | 391 ms                                                 | 151 ms: 2.59x faster                                                   |
| deltablue                     | 4.99 ms                                                | 2.05 ms: 2.43x faster                                                  |
| go                            | 163 ms                                                 | 70.5 ms: 2.32x faster                                                  |
| deepcopy_memo                 | 34.7 us                                                | 16.4 us: 2.12x faster                                                  |
| raytrace                      | 327 ms                                                 | 161 ms: 2.03x faster                                                   |
| deepcopy                      | 276 us                                                 | 139 us: 1.99x faster                                                   |
| logging_silent                | 117 ns                                                 | 59.4 ns: 1.97x faster                                                  |
| sqlglot_parse                 | 1.35 ms                                                | 694 us: 1.94x faster                                                   |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 345 ms: 1.94x faster                                                   |
| chaos                         | 67.7 ms                                                | 34.9 ms: 1.94x faster                                                  |
| richards_super                | 61.0 ms                                                | 31.5 ms: 1.94x faster                                                  |
| scimark_sor                   | 140 ms                                                 | 73.7 ms: 1.90x faster                                                  |
| richards                      | 52.3 ms                                                | 28.0 ms: 1.87x faster                                                  |
| sqlglot_transpile             | 1.56 ms                                                | 843 us: 1.85x faster                                                   |
| scimark_monte_carlo           | 72.4 ms                                                | 39.4 ms: 1.84x faster                                                  |
| generators                    | 31.7 ms                                                | 17.7 ms: 1.80x faster                                                  |
| comprehensions                | 17.3 us                                                | 9.77 us: 1.77x faster                                                  |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 403 ms: 1.66x faster                                                   |
| hexiom                        | 6.25 ms                                                | 3.80 ms: 1.64x faster                                                  |
| float                         | 72.4 ms                                                | 44.1 ms: 1.64x faster                                                  |
| unpickle_pure_python          | 198 us                                                 | 125 us: 1.59x faster                                                   |
| deepcopy_reduce               | 2.32 us                                                | 1.47 us: 1.58x faster                                                  |
| pylint                        | 231 ms                                                 | 149 ms: 1.55x faster                                                   |
| pickle_pure_python            | 285 us                                                 | 184 us: 1.54x faster                                                   |
| logging_format                | 5.03 us                                                | 3.26 us: 1.54x faster                                                  |
| regex_compile                 | 95.6 ms                                                | 62.0 ms: 1.54x faster                                                  |
| logging_simple                | 4.59 us                                                | 2.98 us: 1.54x faster                                                  |
| pprint_pformat                | 1.33 sec                                               | 864 ms: 1.54x faster                                                   |
| pprint_safe_repr              | 648 ms                                                 | 425 ms: 1.52x faster                                                   |
| html5lib                      | 43.5 ms                                                | 28.8 ms: 1.51x faster                                                  |
| tomli_loads                   | 1.72 sec                                               | 1.14 sec: 1.51x faster                                                 |
| pyflate                       | 448 ms                                                 | 298 ms: 1.50x faster                                                   |
| sqlalchemy_imperative         | 9.07 ms                                                | 6.08 ms: 1.49x faster                                                  |
| scimark_lu                    | 103 ms                                                 | 69.6 ms: 1.47x faster                                                  |
| nbody                         | 92.5 ms                                                | 63.3 ms: 1.46x faster                                                  |
| crypto_pyaes                  | 73.3 ms                                                | 50.2 ms: 1.46x faster                                                  |
| pycparser                     | 887 ms                                                 | 615 ms: 1.44x faster                                                   |
| genshi_text                   | 17.7 ms                                                | 12.6 ms: 1.41x faster                                                  |
| sqlalchemy_declarative        | 75.7 ms                                                | 54.2 ms: 1.40x faster                                                  |
| spectral_norm                 | 95.3 ms                                                | 68.5 ms: 1.39x faster                                                  |
| mako                          | 9.81 ms                                                | 7.08 ms: 1.39x faster                                                  |
| thrift                        | 562 us                                                 | 406 us: 1.38x faster                                                   |
| k_core                        | 2.01 sec                                               | 1.47 sec: 1.37x faster                                                 |
| coroutines                    | 20.5 ms                                                | 15.0 ms: 1.36x faster                                                  |
| sphinx                        | 729 ms                                                 | 540 ms: 1.35x faster                                                   |
| sympy_sum                     | 92.7 ms                                                | 68.9 ms: 1.34x faster                                                  |
| dulwich_log                   | 35.6 ms                                                | 26.5 ms: 1.34x faster                                                  |
| 2to3                          | 201 ms                                                 | 151 ms: 1.33x faster                                                   |
| xml_etree_process             | 44.6 ms                                                | 33.5 ms: 1.33x faster                                                  |
| sympy_integrate               | 13.2 ms                                                | 10.1 ms: 1.30x faster                                                  |
| genshi_xml                    | 35.1 ms                                                | 27.0 ms: 1.30x faster                                                  |
| scimark_fft                   | 225 ms                                                 | 174 ms: 1.30x faster                                                   |
| sympy_str                     | 166 ms                                                 | 128 ms: 1.30x faster                                                   |
| django_template               | 24.4 ms                                                | 18.8 ms: 1.29x faster                                                  |
| docutils                      | 1.74 sec                                               | 1.36 sec: 1.28x faster                                                 |
| sqlglot_optimize              | 37.2 ms                                                | 29.7 ms: 1.25x faster                                                  |
| sympy_expand                  | 269 ms                                                 | 215 ms: 1.25x faster                                                   |
| scimark_sparse_mat_mult       | 3.42 ms                                                | 2.73 ms: 1.25x faster                                                  |
| nqueens                       | 63.8 ms                                                | 51.1 ms: 1.25x faster                                                  |
| fannkuch                      | 303 ms                                                 | 247 ms: 1.22x faster                                                   |
| bench_thread_pool             | 545 us                                                 | 451 us: 1.21x faster                                                   |
| bpe_tokeniser                 | 3.44 sec                                               | 2.85 sec: 1.21x faster                                                 |
| regex_dna                     | 175 ms                                                 | 145 ms: 1.21x faster                                                   |
| sqlglot_normalize             | 192 ms                                                 | 162 ms: 1.18x faster                                                   |
| many_optionals                | 486 us                                                 | 415 us: 1.17x faster                                                   |
| json_dumps                    | 8.31 ms                                                | 7.10 ms: 1.17x faster                                                  |
| mdp                           | 1.65 sec                                               | 1.43 sec: 1.16x faster                                                 |
| pathlib                       | 25.7 ms                                                | 22.7 ms: 1.14x faster                                                  |
| xml_etree_generate            | 53.9 ms                                                | 48.3 ms: 1.12x faster                                                  |
| meteor_contest                | 77.8 ms                                                | 69.8 ms: 1.11x faster                                                  |
| xml_etree_iterparse           | 74.5 ms                                                | 68.4 ms: 1.09x faster                                                  |
| xml_etree_parse               | 109 ms                                                 | 101 ms: 1.09x faster                                                   |
| connected_components          | 318 ms                                                 | 293 ms: 1.09x faster                                                   |
| python_startup                | 19.6 ms                                                | 18.2 ms: 1.08x faster                                                  |
| regex_v8                      | 19.1 ms                                                | 17.8 ms: 1.08x faster                                                  |
| dask                          | 789 ms                                                 | 767 ms: 1.03x faster                                                   |
| json                          | 3.10 ms                                                | 3.02 ms: 1.03x faster                                                  |
| shortest_path                 | 328 ms                                                 | 320 ms: 1.03x faster                                                   |
| async_generators              | 233 ms                                                 | 235 ms: 1.01x slower                                                   |
| sqlite_synth                  | 1.48 us                                                | 1.50 us: 1.01x slower                                                  |
| asyncio_websockets            | 242 ms                                                 | 249 ms: 1.03x slower                                                   |
| python_startup_no_site        | 12.8 ms                                                | 13.4 ms: 1.05x slower                                                  |
| bench_mp_pool                 | 56.0 ms                                                | 59.3 ms: 1.06x slower                                                  |
| create_gc_cycles              | 1.16 ms                                                | 1.25 ms: 1.08x slower                                                  |
| json_loads                    | 16.6 us                                                | 17.9 us: 1.08x slower                                                  |
| coverage                      | 41.2 ms                                                | 45.5 ms: 1.10x slower                                                  |
| gc_traversal                  | 2.71 ms                                                | 3.06 ms: 1.13x slower                                                  |
| telco                         | 3.49 ms                                                | 4.42 ms: 1.27x slower                                                  |
| Geometric mean                | (ref)                                                  | 1.47x faster                                                           |

Benchmark hidden because not significant (2): pidigits, regex_effbot
Ignored benchmarks (4) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: chameleon, djangocms, gevent_hub, tornado_http
Ignored benchmarks (16) of results/bm-20250301-3.14.0a5+-c9932a9-CLANG/bm-20250301-darwin-arm64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9.json: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.470x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.32x
- 95% likely to have a speedup of 1.31x
- 99% likely to have a speedup of 1.28x

# Memory
- memory change: 1.12x