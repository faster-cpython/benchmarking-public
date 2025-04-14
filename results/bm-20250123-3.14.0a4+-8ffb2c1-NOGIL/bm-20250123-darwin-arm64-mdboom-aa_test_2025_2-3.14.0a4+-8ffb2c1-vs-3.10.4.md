# Results vs. 3.10.4

- fork: mdboom
- ref: aa_test_2025_2
- machine: darwin-arm64
- commit hash: 8ffb2c1
- commit date: 2025-01-23
- overall geometric mean: 1.257x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.11x faster
- Memory change: 1.29x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250123-darwin-arm64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 189 ms: 1.07x faster                                             |
| docutils       | 1.74 sec                                               | 1.43 sec: 1.22x faster                                           |
| html5lib       | 43.5 ms                                                | 33.3 ms: 1.31x faster                                            |
| sphinx         | 729 ms                                                 | 614 ms: 1.19x faster                                             |
| Geometric mean | (ref)                                                  | 1.19x faster                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250123-darwin-arm64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|-------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 81.5 ms: 4.81x faster                                            |
| async_tree_eager_memoization  | 483 ms                                                 | 151 ms: 3.19x faster                                             |
| async_tree_eager_io           | 1.01 sec                                               | 329 ms: 3.08x faster                                             |
| async_tree_io                 | 1.02 sec                                               | 343 ms: 2.96x faster                                             |
| async_tree_none               | 391 ms                                                 | 160 ms: 2.44x faster                                             |
| async_tree_memoization        | 481 ms                                                 | 199 ms: 2.42x faster                                             |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 370 ms: 1.81x faster                                             |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 409 ms: 1.64x faster                                             |
| coroutines                    | 20.5 ms                                                | 17.0 ms: 1.21x faster                                            |
| asyncio_websockets            | 242 ms                                                 | 238 ms: 1.02x faster                                             |
| async_generators              | 233 ms                                                 | 260 ms: 1.11x slower                                             |
| Geometric mean                | (ref)                                                  | 2.05x faster                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250123-darwin-arm64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| float          | 72.4 ms                                                | 50.7 ms: 1.43x faster                                            |
| nbody          | 92.5 ms                                                | 87.6 ms: 1.06x faster                                            |
| pidigits       | 280 ms                                                 | 280 ms: 1.00x faster                                             |
| Geometric mean | (ref)                                                  | 1.15x faster                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250123-darwin-arm64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_dna      | 175 ms                                                 | 137 ms: 1.28x faster                                             |
| regex_compile  | 95.6 ms                                                | 77.1 ms: 1.24x faster                                            |
| regex_v8       | 19.1 ms                                                | 15.5 ms: 1.23x faster                                            |
| regex_effbot   | 2.34 ms                                                | 2.08 ms: 1.12x faster                                            |
| Geometric mean | (ref)                                                  | 1.22x faster                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250123-darwin-arm64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| pickle_pure_python   | 285 us                                                 | 224 us: 1.27x faster                                             |
| tomli_loads          | 1.72 sec                                               | 1.36 sec: 1.27x faster                                           |
| unpickle_pure_python | 198 us                                                 | 162 us: 1.22x faster                                             |
| xml_etree_iterparse  | 74.5 ms                                                | 62.5 ms: 1.19x faster                                            |
| xml_etree_parse      | 109 ms                                                 | 99.6 ms: 1.10x faster                                            |
| json_dumps           | 8.31 ms                                                | 7.96 ms: 1.04x faster                                            |
| xml_etree_process    | 44.6 ms                                                | 45.6 ms: 1.02x slower                                            |
| xml_etree_generate   | 53.9 ms                                                | 56.1 ms: 1.04x slower                                            |
| json_loads           | 16.6 us                                                | 17.7 us: 1.07x slower                                            |
| Geometric mean       | (ref)                                                  | 1.10x faster                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250123-darwin-arm64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup         | 19.6 ms                                                | 20.7 ms: 1.05x slower                                            |
| python_startup_no_site | 12.8 ms                                                | 16.1 ms: 1.26x slower                                            |
| Geometric mean         | (ref)                                                  | 1.15x slower                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250123-darwin-arm64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| genshi_xml      | 35.1 ms                                                | 33.1 ms: 1.06x faster                                            |
| genshi_text     | 17.7 ms                                                | 17.2 ms: 1.03x faster                                            |
| django_template | 24.4 ms                                                | 24.6 ms: 1.01x slower                                            |
| mako            | 9.81 ms                                                | 9.98 ms: 1.02x slower                                            |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                     |

All benchmarks:
===============

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250123-darwin-arm64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|-------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 81.5 ms: 4.81x faster                                            |
| async_tree_eager_memoization  | 483 ms                                                 | 151 ms: 3.19x faster                                             |
| async_tree_eager_io           | 1.01 sec                                               | 329 ms: 3.08x faster                                             |
| subparsers                    | 39.8 ms                                                | 13.4 ms: 2.98x faster                                            |
| async_tree_io                 | 1.02 sec                                               | 343 ms: 2.96x faster                                             |
| typing_runtime_protocols      | 326 us                                                 | 117 us: 2.79x faster                                             |
| async_tree_none               | 391 ms                                                 | 160 ms: 2.44x faster                                             |
| async_tree_memoization        | 481 ms                                                 | 199 ms: 2.42x faster                                             |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 370 ms: 1.81x faster                                             |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 409 ms: 1.64x faster                                             |
| deepcopy_memo                 | 34.7 us                                                | 21.8 us: 1.60x faster                                            |
| deepcopy                      | 276 us                                                 | 173 us: 1.59x faster                                             |
| go                            | 163 ms                                                 | 104 ms: 1.57x faster                                             |
| chaos                         | 67.7 ms                                                | 46.2 ms: 1.46x faster                                            |
| deltablue                     | 4.99 ms                                                | 3.41 ms: 1.46x faster                                            |
| scimark_sor                   | 140 ms                                                 | 96.8 ms: 1.45x faster                                            |
| float                         | 72.4 ms                                                | 50.7 ms: 1.43x faster                                            |
| create_gc_cycles              | 1.16 ms                                                | 821 us: 1.42x faster                                             |
| pyflate                       | 448 ms                                                 | 317 ms: 1.41x faster                                             |
| richards_super                | 61.0 ms                                                | 44.2 ms: 1.38x faster                                            |
| pylint                        | 231 ms                                                 | 170 ms: 1.36x faster                                             |
| sqlglot_parse                 | 1.35 ms                                                | 1.01 ms: 1.34x faster                                            |
| generators                    | 31.7 ms                                                | 23.8 ms: 1.33x faster                                            |
| richards                      | 52.3 ms                                                | 39.4 ms: 1.33x faster                                            |
| pycparser                     | 887 ms                                                 | 673 ms: 1.32x faster                                             |
| raytrace                      | 327 ms                                                 | 249 ms: 1.31x faster                                             |
| html5lib                      | 43.5 ms                                                | 33.3 ms: 1.31x faster                                            |
| sqlglot_transpile             | 1.56 ms                                                | 1.19 ms: 1.31x faster                                            |
| deepcopy_reduce               | 2.32 us                                                | 1.78 us: 1.31x faster                                            |
| spectral_norm                 | 95.3 ms                                                | 74.2 ms: 1.28x faster                                            |
| regex_dna                     | 175 ms                                                 | 137 ms: 1.28x faster                                             |
| scimark_monte_carlo           | 72.4 ms                                                | 56.9 ms: 1.27x faster                                            |
| pickle_pure_python            | 285 us                                                 | 224 us: 1.27x faster                                             |
| tomli_loads                   | 1.72 sec                                               | 1.36 sec: 1.27x faster                                           |
| logging_silent                | 117 ns                                                 | 92.6 ns: 1.26x faster                                            |
| k_core                        | 2.01 sec                                               | 1.62 sec: 1.24x faster                                           |
| regex_compile                 | 95.6 ms                                                | 77.1 ms: 1.24x faster                                            |
| regex_v8                      | 19.1 ms                                                | 15.5 ms: 1.23x faster                                            |
| unpickle_pure_python          | 198 us                                                 | 162 us: 1.22x faster                                             |
| docutils                      | 1.74 sec                                               | 1.43 sec: 1.22x faster                                           |
| comprehensions                | 17.3 us                                                | 14.2 us: 1.22x faster                                            |
| coroutines                    | 20.5 ms                                                | 17.0 ms: 1.21x faster                                            |
| logging_simple                | 4.59 us                                                | 3.81 us: 1.21x faster                                            |
| pprint_pformat                | 1.33 sec                                               | 1.10 sec: 1.20x faster                                           |
| logging_format                | 5.03 us                                                | 4.18 us: 1.20x faster                                            |
| dulwich_log                   | 35.6 ms                                                | 29.6 ms: 1.20x faster                                            |
| pprint_safe_repr              | 648 ms                                                 | 541 ms: 1.20x faster                                             |
| crypto_pyaes                  | 73.3 ms                                                | 61.5 ms: 1.19x faster                                            |
| xml_etree_iterparse           | 74.5 ms                                                | 62.5 ms: 1.19x faster                                            |
| sphinx                        | 729 ms                                                 | 614 ms: 1.19x faster                                             |
| gc_traversal                  | 2.71 ms                                                | 2.31 ms: 1.17x faster                                            |
| sqlalchemy_imperative         | 9.07 ms                                                | 7.78 ms: 1.17x faster                                            |
| hexiom                        | 6.25 ms                                                | 5.40 ms: 1.16x faster                                            |
| sympy_sum                     | 92.7 ms                                                | 80.4 ms: 1.15x faster                                            |
| bpe_tokeniser                 | 3.44 sec                                               | 3.03 sec: 1.14x faster                                           |
| sqlite_synth                  | 1.48 us                                                | 1.31 us: 1.13x faster                                            |
| sqlalchemy_declarative        | 75.7 ms                                                | 67.4 ms: 1.12x faster                                            |
| pathlib                       | 25.7 ms                                                | 22.9 ms: 1.12x faster                                            |
| regex_effbot                  | 2.34 ms                                                | 2.08 ms: 1.12x faster                                            |
| xml_etree_parse               | 109 ms                                                 | 99.6 ms: 1.10x faster                                            |
| thrift                        | 562 us                                                 | 519 us: 1.08x faster                                             |
| sympy_integrate               | 13.2 ms                                                | 12.3 ms: 1.07x faster                                            |
| scimark_fft                   | 225 ms                                                 | 211 ms: 1.07x faster                                             |
| 2to3                          | 201 ms                                                 | 189 ms: 1.07x faster                                             |
| sympy_str                     | 166 ms                                                 | 156 ms: 1.07x faster                                             |
| fannkuch                      | 303 ms                                                 | 285 ms: 1.06x faster                                             |
| genshi_xml                    | 35.1 ms                                                | 33.1 ms: 1.06x faster                                            |
| nqueens                       | 63.8 ms                                                | 60.4 ms: 1.06x faster                                            |
| nbody                         | 92.5 ms                                                | 87.6 ms: 1.06x faster                                            |
| sqlglot_optimize              | 37.2 ms                                                | 35.4 ms: 1.05x faster                                            |
| json_dumps                    | 8.31 ms                                                | 7.96 ms: 1.04x faster                                            |
| many_optionals                | 486 us                                                 | 466 us: 1.04x faster                                             |
| json                          | 3.10 ms                                                | 2.98 ms: 1.04x faster                                            |
| scimark_lu                    | 103 ms                                                 | 99.1 ms: 1.03x faster                                            |
| mdp                           | 1.65 sec                                               | 1.60 sec: 1.03x faster                                           |
| genshi_text                   | 17.7 ms                                                | 17.2 ms: 1.03x faster                                            |
| asyncio_websockets            | 242 ms                                                 | 238 ms: 1.02x faster                                             |
| sympy_expand                  | 269 ms                                                 | 265 ms: 1.02x faster                                             |
| sqlglot_normalize             | 192 ms                                                 | 191 ms: 1.01x faster                                             |
| pidigits                      | 280 ms                                                 | 280 ms: 1.00x faster                                             |
| django_template               | 24.4 ms                                                | 24.6 ms: 1.01x slower                                            |
| mako                          | 9.81 ms                                                | 9.98 ms: 1.02x slower                                            |
| meteor_contest                | 77.8 ms                                                | 79.4 ms: 1.02x slower                                            |
| xml_etree_process             | 44.6 ms                                                | 45.6 ms: 1.02x slower                                            |
| connected_components          | 318 ms                                                 | 326 ms: 1.02x slower                                             |
| xml_etree_generate            | 53.9 ms                                                | 56.1 ms: 1.04x slower                                            |
| scimark_sparse_mat_mult       | 3.42 ms                                                | 3.58 ms: 1.05x slower                                            |
| python_startup                | 19.6 ms                                                | 20.7 ms: 1.05x slower                                            |
| shortest_path                 | 328 ms                                                 | 350 ms: 1.07x slower                                             |
| json_loads                    | 16.6 us                                                | 17.7 us: 1.07x slower                                            |
| async_generators              | 233 ms                                                 | 260 ms: 1.11x slower                                             |
| bench_mp_pool                 | 56.0 ms                                                | 66.9 ms: 1.19x slower                                            |
| coverage                      | 41.2 ms                                                | 51.3 ms: 1.24x slower                                            |
| python_startup_no_site        | 12.8 ms                                                | 16.1 ms: 1.26x slower                                            |
| telco                         | 3.49 ms                                                | 4.92 ms: 1.41x slower                                            |
| bench_thread_pool             | 545 us                                                 | 794 us: 1.46x slower                                             |
| Geometric mean                | (ref)                                                  | 1.24x faster                                                     |
Ignored benchmarks (5) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: chameleon, dask, djangocms, gevent_hub, tornado_http
Ignored benchmarks (8) of results/bm-20250123-3.14.0a4+-8ffb2c1-NOGIL/bm-20250123-darwin-arm64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1.json: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

- Geometric mean (including insignificant results): 1.257x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.15x
- 95% likely to have a speedup of 1.13x
- 99% likely to have a speedup of 1.11x

# Memory
- memory change: 1.29x