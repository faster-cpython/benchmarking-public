# Results vs. 3.10.4

- fork: python
- ref: 009e7b36981fd07f7cca
- machine: darwin-arm64
- commit hash: 009e7b3
- commit date: 2025-05-18
- overall geometric mean: 1.191x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.34x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250518-darwin-arm64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 205 ms: 1.02x slower                                                  |
| docutils       | 1.74 sec                                               | 1.53 sec: 1.14x faster                                                |
| html5lib       | 43.5 ms                                                | 35.2 ms: 1.24x faster                                                 |
| sphinx         | 729 ms                                                 | 648 ms: 1.13x faster                                                  |
| Geometric mean | (ref)                                                  | 1.12x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250518-darwin-arm64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|-------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 91.6 ms: 4.28x faster                                                 |
| async_tree_eager_memoization  | 483 ms                                                 | 154 ms: 3.14x faster                                                  |
| async_tree_eager_io           | 1.01 sec                                               | 343 ms: 2.96x faster                                                  |
| async_tree_io                 | 1.02 sec                                               | 362 ms: 2.81x faster                                                  |
| async_tree_memoization        | 481 ms                                                 | 205 ms: 2.35x faster                                                  |
| async_tree_none               | 391 ms                                                 | 173 ms: 2.26x faster                                                  |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 373 ms: 1.79x faster                                                  |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 415 ms: 1.61x faster                                                  |
| coroutines                    | 20.5 ms                                                | 18.9 ms: 1.09x faster                                                 |
| asyncio_websockets            | 242 ms                                                 | 237 ms: 1.02x faster                                                  |
| async_generators              | 233 ms                                                 | 291 ms: 1.25x slower                                                  |
| Geometric mean                | (ref)                                                  | 1.95x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250518-darwin-arm64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 72.4 ms                                                | 53.8 ms: 1.35x faster                                                 |
| pidigits       | 280 ms                                                 | 280 ms: 1.00x faster                                                  |
| nbody          | 92.5 ms                                                | 95.3 ms: 1.03x slower                                                 |
| Geometric mean | (ref)                                                  | 1.09x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250518-darwin-arm64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_dna      | 175 ms                                                 | 136 ms: 1.28x faster                                                  |
| regex_v8       | 19.1 ms                                                | 15.1 ms: 1.27x faster                                                 |
| regex_effbot   | 2.34 ms                                                | 2.11 ms: 1.11x faster                                                 |
| regex_compile  | 95.6 ms                                                | 95.8 ms: 1.00x slower                                                 |
| Geometric mean | (ref)                                                  | 1.16x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250518-darwin-arm64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| json_dumps           | 8.31 ms                                                | 7.27 ms: 1.14x faster                                                 |
| xml_etree_parse      | 109 ms                                                 | 97.6 ms: 1.12x faster                                                 |
| xml_etree_iterparse  | 74.5 ms                                                | 66.7 ms: 1.12x faster                                                 |
| tomli_loads          | 1.72 sec                                               | 1.64 sec: 1.05x faster                                                |
| pickle_pure_python   | 285 us                                                 | 272 us: 1.05x faster                                                  |
| unpickle_pure_python | 198 us                                                 | 190 us: 1.04x faster                                                  |
| xml_etree_process    | 44.6 ms                                                | 48.2 ms: 1.08x slower                                                 |
| json_loads           | 16.6 us                                                | 19.1 us: 1.15x slower                                                 |
| xml_etree_generate   | 53.9 ms                                                | 63.4 ms: 1.18x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250518-darwin-arm64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 19.6 ms                                                | 19.8 ms: 1.01x slower                                                 |
| python_startup_no_site | 12.8 ms                                                | 15.3 ms: 1.19x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.10x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250518-darwin-arm64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 17.7 ms                                                | 19.4 ms: 1.10x slower                                                 |
| genshi_xml      | 35.1 ms                                                | 38.8 ms: 1.10x slower                                                 |
| mako            | 9.81 ms                                                | 11.6 ms: 1.18x slower                                                 |
| django_template | 24.4 ms                                                | 29.0 ms: 1.19x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.14x slower                                                          |

All benchmarks:
===============

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250518-darwin-arm64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|-------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 91.6 ms: 4.28x faster                                                 |
| async_tree_eager_memoization  | 483 ms                                                 | 154 ms: 3.14x faster                                                  |
| async_tree_eager_io           | 1.01 sec                                               | 343 ms: 2.96x faster                                                  |
| async_tree_io                 | 1.02 sec                                               | 362 ms: 2.81x faster                                                  |
| typing_runtime_protocols      | 326 us                                                 | 124 us: 2.63x faster                                                  |
| subparsers                    | 39.8 ms                                                | 15.7 ms: 2.53x faster                                                 |
| async_tree_memoization        | 481 ms                                                 | 205 ms: 2.35x faster                                                  |
| async_tree_none               | 391 ms                                                 | 173 ms: 2.26x faster                                                  |
| mdp                           | 1.65 sec                                               | 905 ms: 1.82x faster                                                  |
| gc_traversal                  | 2.71 ms                                                | 1.49 ms: 1.82x faster                                                 |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 373 ms: 1.79x faster                                                  |
| deltablue                     | 4.99 ms                                                | 3.01 ms: 1.66x faster                                                 |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 415 ms: 1.61x faster                                                  |
| go                            | 163 ms                                                 | 111 ms: 1.48x faster                                                  |
| raytrace                      | 327 ms                                                 | 228 ms: 1.43x faster                                                  |
| create_gc_cycles              | 1.16 ms                                                | 824 us: 1.41x faster                                                  |
| deepcopy                      | 276 us                                                 | 200 us: 1.38x faster                                                  |
| scimark_sor                   | 140 ms                                                 | 102 ms: 1.38x faster                                                  |
| deepcopy_memo                 | 34.7 us                                                | 25.6 us: 1.36x faster                                                 |
| float                         | 72.4 ms                                                | 53.8 ms: 1.35x faster                                                 |
| chaos                         | 67.7 ms                                                | 51.3 ms: 1.32x faster                                                 |
| pylint                        | 231 ms                                                 | 177 ms: 1.30x faster                                                  |
| regex_dna                     | 175 ms                                                 | 136 ms: 1.28x faster                                                  |
| dulwich_log                   | 35.6 ms                                                | 28.0 ms: 1.27x faster                                                 |
| regex_v8                      | 19.1 ms                                                | 15.1 ms: 1.27x faster                                                 |
| richards_super                | 61.0 ms                                                | 48.2 ms: 1.26x faster                                                 |
| richards                      | 52.3 ms                                                | 41.5 ms: 1.26x faster                                                 |
| k_core                        | 2.01 sec                                               | 1.63 sec: 1.24x faster                                                |
| html5lib                      | 43.5 ms                                                | 35.2 ms: 1.24x faster                                                 |
| pyflate                       | 448 ms                                                 | 364 ms: 1.23x faster                                                  |
| pycparser                     | 887 ms                                                 | 734 ms: 1.21x faster                                                  |
| spectral_norm                 | 95.3 ms                                                | 81.0 ms: 1.18x faster                                                 |
| scimark_monte_carlo           | 72.4 ms                                                | 62.5 ms: 1.16x faster                                                 |
| comprehensions                | 17.3 us                                                | 14.9 us: 1.16x faster                                                 |
| json_dumps                    | 8.31 ms                                                | 7.27 ms: 1.14x faster                                                 |
| docutils                      | 1.74 sec                                               | 1.53 sec: 1.14x faster                                                |
| sphinx                        | 729 ms                                                 | 648 ms: 1.13x faster                                                  |
| xml_etree_parse               | 109 ms                                                 | 97.6 ms: 1.12x faster                                                 |
| xml_etree_iterparse           | 74.5 ms                                                | 66.7 ms: 1.12x faster                                                 |
| crypto_pyaes                  | 73.3 ms                                                | 66.1 ms: 1.11x faster                                                 |
| regex_effbot                  | 2.34 ms                                                | 2.11 ms: 1.11x faster                                                 |
| hexiom                        | 6.25 ms                                                | 5.72 ms: 1.09x faster                                                 |
| coroutines                    | 20.5 ms                                                | 18.9 ms: 1.09x faster                                                 |
| deepcopy_reduce               | 2.32 us                                                | 2.15 us: 1.08x faster                                                 |
| sqlite_synth                  | 1.48 us                                                | 1.37 us: 1.08x faster                                                 |
| thrift                        | 562 us                                                 | 524 us: 1.07x faster                                                  |
| sympy_integrate               | 13.2 ms                                                | 12.3 ms: 1.07x faster                                                 |
| bpe_tokeniser                 | 3.44 sec                                               | 3.27 sec: 1.05x faster                                                |
| pprint_pformat                | 1.33 sec                                               | 1.26 sec: 1.05x faster                                                |
| sympy_sum                     | 92.7 ms                                                | 88.3 ms: 1.05x faster                                                 |
| tomli_loads                   | 1.72 sec                                               | 1.64 sec: 1.05x faster                                                |
| pickle_pure_python            | 285 us                                                 | 272 us: 1.05x faster                                                  |
| scimark_lu                    | 103 ms                                                 | 98.2 ms: 1.04x faster                                                 |
| pprint_safe_repr              | 648 ms                                                 | 621 ms: 1.04x faster                                                  |
| unpickle_pure_python          | 198 us                                                 | 190 us: 1.04x faster                                                  |
| asyncio_websockets            | 242 ms                                                 | 237 ms: 1.02x faster                                                  |
| pathlib                       | 25.7 ms                                                | 25.4 ms: 1.02x faster                                                 |
| pidigits                      | 280 ms                                                 | 280 ms: 1.00x faster                                                  |
| regex_compile                 | 95.6 ms                                                | 95.8 ms: 1.00x slower                                                 |
| generators                    | 31.7 ms                                                | 31.9 ms: 1.01x slower                                                 |
| python_startup                | 19.6 ms                                                | 19.8 ms: 1.01x slower                                                 |
| logging_format                | 5.03 us                                                | 5.11 us: 1.02x slower                                                 |
| scimark_fft                   | 225 ms                                                 | 229 ms: 1.02x slower                                                  |
| 2to3                          | 201 ms                                                 | 205 ms: 1.02x slower                                                  |
| json                          | 3.10 ms                                                | 3.18 ms: 1.02x slower                                                 |
| logging_simple                | 4.59 us                                                | 4.72 us: 1.03x slower                                                 |
| nbody                         | 92.5 ms                                                | 95.3 ms: 1.03x slower                                                 |
| sympy_str                     | 166 ms                                                 | 172 ms: 1.03x slower                                                  |
| fannkuch                      | 303 ms                                                 | 315 ms: 1.04x slower                                                  |
| scimark_sparse_mat_mult       | 3.42 ms                                                | 3.57 ms: 1.04x slower                                                 |
| connected_components          | 318 ms                                                 | 333 ms: 1.04x slower                                                  |
| many_optionals                | 486 us                                                 | 518 us: 1.07x slower                                                  |
| meteor_contest                | 77.8 ms                                                | 83.4 ms: 1.07x slower                                                 |
| xml_etree_process             | 44.6 ms                                                | 48.2 ms: 1.08x slower                                                 |
| shortest_path                 | 328 ms                                                 | 359 ms: 1.09x slower                                                  |
| genshi_text                   | 17.7 ms                                                | 19.4 ms: 1.10x slower                                                 |
| sympy_expand                  | 269 ms                                                 | 297 ms: 1.10x slower                                                  |
| genshi_xml                    | 35.1 ms                                                | 38.8 ms: 1.10x slower                                                 |
| json_loads                    | 16.6 us                                                | 19.1 us: 1.15x slower                                                 |
| nqueens                       | 63.8 ms                                                | 73.6 ms: 1.15x slower                                                 |
| xml_etree_generate            | 53.9 ms                                                | 63.4 ms: 1.18x slower                                                 |
| mako                          | 9.81 ms                                                | 11.6 ms: 1.18x slower                                                 |
| django_template               | 24.4 ms                                                | 29.0 ms: 1.19x slower                                                 |
| python_startup_no_site        | 12.8 ms                                                | 15.3 ms: 1.19x slower                                                 |
| async_generators              | 233 ms                                                 | 291 ms: 1.25x slower                                                  |
| bench_mp_pool                 | 56.0 ms                                                | 73.8 ms: 1.32x slower                                                 |
| bench_thread_pool             | 545 us                                                 | 762 us: 1.40x slower                                                  |
| telco                         | 3.49 ms                                                | 5.33 ms: 1.53x slower                                                 |
| coverage                      | 41.2 ms                                                | 66.6 ms: 1.62x slower                                                 |
| logging_silent                | 117 ns                                                 | 373 ns: 3.19x slower                                                  |
| Geometric mean                | (ref)                                                  | 1.16x faster                                                          |
Ignored benchmarks (11) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: chameleon, dask, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (20) of results/bm-20250518-3.15.0a0-009e7b3-NOGIL/bm-20250518-darwin-arm64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3.json: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.191x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.34x