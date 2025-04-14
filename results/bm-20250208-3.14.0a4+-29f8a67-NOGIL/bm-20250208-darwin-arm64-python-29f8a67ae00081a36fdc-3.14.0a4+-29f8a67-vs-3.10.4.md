# Results vs. 3.10.4

- fork: python
- ref: 29f8a67ae00081a36fdc
- machine: darwin-arm64
- commit hash: 29f8a67
- commit date: 2025-02-08
- overall geometric mean: 1.168x faster
- HPT reliability: 99.98%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.29x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 202 ms: 1.00x slower                                                   |
| docutils       | 1.74 sec                                               | 1.50 sec: 1.16x faster                                                 |
| html5lib       | 43.5 ms                                                | 36.2 ms: 1.20x faster                                                  |
| sphinx         | 729 ms                                                 | 636 ms: 1.15x faster                                                   |
| Geometric mean | (ref)                                                  | 1.12x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|-------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 93.3 ms: 4.20x faster                                                  |
| async_tree_eager_memoization  | 483 ms                                                 | 167 ms: 2.90x faster                                                   |
| async_tree_eager_io           | 1.01 sec                                               | 361 ms: 2.81x faster                                                   |
| async_tree_io                 | 1.02 sec                                               | 374 ms: 2.72x faster                                                   |
| async_tree_none               | 391 ms                                                 | 182 ms: 2.15x faster                                                   |
| async_tree_memoization        | 481 ms                                                 | 228 ms: 2.11x faster                                                   |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 383 ms: 1.75x faster                                                   |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 435 ms: 1.54x faster                                                   |
| coroutines                    | 20.5 ms                                                | 18.9 ms: 1.09x faster                                                  |
| asyncio_websockets            | 242 ms                                                 | 238 ms: 1.02x faster                                                   |
| async_generators              | 233 ms                                                 | 282 ms: 1.21x slower                                                   |
| Geometric mean                | (ref)                                                  | 1.88x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 72.4 ms                                                | 56.2 ms: 1.29x faster                                                  |
| pidigits       | 280 ms                                                 | 281 ms: 1.00x slower                                                   |
| nbody          | 92.5 ms                                                | 106 ms: 1.14x slower                                                   |
| Geometric mean | (ref)                                                  | 1.04x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_dna      | 175 ms                                                 | 138 ms: 1.27x faster                                                   |
| regex_v8       | 19.1 ms                                                | 16.1 ms: 1.19x faster                                                  |
| regex_effbot   | 2.34 ms                                                | 2.16 ms: 1.08x faster                                                  |
| regex_compile  | 95.6 ms                                                | 92.9 ms: 1.03x faster                                                  |
| Geometric mean | (ref)                                                  | 1.14x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_parse      | 109 ms                                                 | 96.7 ms: 1.13x faster                                                  |
| xml_etree_iterparse  | 74.5 ms                                                | 67.4 ms: 1.11x faster                                                  |
| pickle_pure_python   | 285 us                                                 | 270 us: 1.05x faster                                                   |
| unpickle_pure_python | 198 us                                                 | 189 us: 1.05x faster                                                   |
| json_dumps           | 8.31 ms                                                | 7.98 ms: 1.04x faster                                                  |
| tomli_loads          | 1.72 sec                                               | 1.66 sec: 1.03x faster                                                 |
| xml_etree_process    | 44.6 ms                                                | 45.9 ms: 1.03x slower                                                  |
| xml_etree_generate   | 53.9 ms                                                | 60.9 ms: 1.13x slower                                                  |
| json_loads           | 16.6 us                                                | 19.1 us: 1.15x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 19.6 ms                                                | 20.5 ms: 1.04x slower                                                  |
| python_startup_no_site | 12.8 ms                                                | 15.8 ms: 1.23x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.13x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 24.4 ms                                                | 27.1 ms: 1.11x slower                                                  |
| genshi_xml      | 35.1 ms                                                | 39.2 ms: 1.12x slower                                                  |
| mako            | 9.81 ms                                                | 11.0 ms: 1.12x slower                                                  |
| genshi_text     | 17.7 ms                                                | 20.1 ms: 1.13x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.12x slower                                                           |

All benchmarks:
===============

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|-------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 93.3 ms: 4.20x faster                                                  |
| async_tree_eager_memoization  | 483 ms                                                 | 167 ms: 2.90x faster                                                   |
| subparsers                    | 39.8 ms                                                | 14.1 ms: 2.83x faster                                                  |
| async_tree_eager_io           | 1.01 sec                                               | 361 ms: 2.81x faster                                                   |
| async_tree_io                 | 1.02 sec                                               | 374 ms: 2.72x faster                                                   |
| typing_runtime_protocols      | 326 us                                                 | 126 us: 2.59x faster                                                   |
| async_tree_none               | 391 ms                                                 | 182 ms: 2.15x faster                                                   |
| async_tree_memoization        | 481 ms                                                 | 228 ms: 2.11x faster                                                   |
| gc_traversal                  | 2.71 ms                                                | 1.40 ms: 1.94x faster                                                  |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 383 ms: 1.75x faster                                                   |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 435 ms: 1.54x faster                                                   |
| create_gc_cycles              | 1.16 ms                                                | 764 us: 1.52x faster                                                   |
| deltablue                     | 4.99 ms                                                | 3.46 ms: 1.44x faster                                                  |
| go                            | 163 ms                                                 | 115 ms: 1.42x faster                                                   |
| deepcopy                      | 276 us                                                 | 204 us: 1.35x faster                                                   |
| raytrace                      | 327 ms                                                 | 243 ms: 1.34x faster                                                   |
| logging_silent                | 117 ns                                                 | 87.3 ns: 1.34x faster                                                  |
| scimark_sor                   | 140 ms                                                 | 107 ms: 1.31x faster                                                   |
| pylint                        | 231 ms                                                 | 177 ms: 1.31x faster                                                   |
| float                         | 72.4 ms                                                | 56.2 ms: 1.29x faster                                                  |
| richards_super                | 61.0 ms                                                | 47.3 ms: 1.29x faster                                                  |
| sqlglot_transpile             | 1.56 ms                                                | 1.21 ms: 1.29x faster                                                  |
| sqlglot_parse                 | 1.35 ms                                                | 1.06 ms: 1.28x faster                                                  |
| regex_dna                     | 175 ms                                                 | 138 ms: 1.27x faster                                                   |
| chaos                         | 67.7 ms                                                | 53.4 ms: 1.27x faster                                                  |
| richards                      | 52.3 ms                                                | 42.0 ms: 1.24x faster                                                  |
| pycparser                     | 887 ms                                                 | 716 ms: 1.24x faster                                                   |
| pyflate                       | 448 ms                                                 | 369 ms: 1.21x faster                                                   |
| deepcopy_memo                 | 34.7 us                                                | 28.8 us: 1.21x faster                                                  |
| html5lib                      | 43.5 ms                                                | 36.2 ms: 1.20x faster                                                  |
| regex_v8                      | 19.1 ms                                                | 16.1 ms: 1.19x faster                                                  |
| k_core                        | 2.01 sec                                               | 1.69 sec: 1.19x faster                                                 |
| comprehensions                | 17.3 us                                                | 14.7 us: 1.18x faster                                                  |
| spectral_norm                 | 95.3 ms                                                | 82.1 ms: 1.16x faster                                                  |
| scimark_monte_carlo           | 72.4 ms                                                | 62.5 ms: 1.16x faster                                                  |
| docutils                      | 1.74 sec                                               | 1.50 sec: 1.16x faster                                                 |
| sphinx                        | 729 ms                                                 | 636 ms: 1.15x faster                                                   |
| sqlalchemy_imperative         | 9.07 ms                                                | 7.93 ms: 1.14x faster                                                  |
| xml_etree_parse               | 109 ms                                                 | 96.7 ms: 1.13x faster                                                  |
| sqlite_synth                  | 1.48 us                                                | 1.32 us: 1.12x faster                                                  |
| dulwich_log                   | 35.6 ms                                                | 31.7 ms: 1.12x faster                                                  |
| crypto_pyaes                  | 73.3 ms                                                | 66.3 ms: 1.11x faster                                                  |
| xml_etree_iterparse           | 74.5 ms                                                | 67.4 ms: 1.11x faster                                                  |
| pathlib                       | 25.7 ms                                                | 23.5 ms: 1.10x faster                                                  |
| deepcopy_reduce               | 2.32 us                                                | 2.12 us: 1.10x faster                                                  |
| coroutines                    | 20.5 ms                                                | 18.9 ms: 1.09x faster                                                  |
| regex_effbot                  | 2.34 ms                                                | 2.16 ms: 1.08x faster                                                  |
| logging_simple                | 4.59 us                                                | 4.25 us: 1.08x faster                                                  |
| thrift                        | 562 us                                                 | 522 us: 1.08x faster                                                   |
| sqlalchemy_declarative        | 75.7 ms                                                | 70.6 ms: 1.07x faster                                                  |
| logging_format                | 5.03 us                                                | 4.72 us: 1.07x faster                                                  |
| sympy_sum                     | 92.7 ms                                                | 87.0 ms: 1.06x faster                                                  |
| pickle_pure_python            | 285 us                                                 | 270 us: 1.05x faster                                                   |
| unpickle_pure_python          | 198 us                                                 | 189 us: 1.05x faster                                                   |
| json_dumps                    | 8.31 ms                                                | 7.98 ms: 1.04x faster                                                  |
| scimark_lu                    | 103 ms                                                 | 98.8 ms: 1.04x faster                                                  |
| hexiom                        | 6.25 ms                                                | 6.02 ms: 1.04x faster                                                  |
| tomli_loads                   | 1.72 sec                                               | 1.66 sec: 1.03x faster                                                 |
| pprint_pformat                | 1.33 sec                                               | 1.29 sec: 1.03x faster                                                 |
| bpe_tokeniser                 | 3.44 sec                                               | 3.33 sec: 1.03x faster                                                 |
| regex_compile                 | 95.6 ms                                                | 92.9 ms: 1.03x faster                                                  |
| pprint_safe_repr              | 648 ms                                                 | 632 ms: 1.02x faster                                                   |
| asyncio_websockets            | 242 ms                                                 | 238 ms: 1.02x faster                                                   |
| pidigits                      | 280 ms                                                 | 281 ms: 1.00x slower                                                   |
| 2to3                          | 201 ms                                                 | 202 ms: 1.00x slower                                                   |
| mdp                           | 1.65 sec                                               | 1.66 sec: 1.00x slower                                                 |
| json                          | 3.10 ms                                                | 3.16 ms: 1.02x slower                                                  |
| many_optionals                | 486 us                                                 | 499 us: 1.03x slower                                                   |
| scimark_fft                   | 225 ms                                                 | 232 ms: 1.03x slower                                                   |
| xml_etree_process             | 44.6 ms                                                | 45.9 ms: 1.03x slower                                                  |
| sympy_str                     | 166 ms                                                 | 171 ms: 1.03x slower                                                   |
| sqlglot_optimize              | 37.2 ms                                                | 38.5 ms: 1.03x slower                                                  |
| generators                    | 31.7 ms                                                | 32.8 ms: 1.04x slower                                                  |
| python_startup                | 19.6 ms                                                | 20.5 ms: 1.04x slower                                                  |
| sympy_integrate               | 13.2 ms                                                | 13.8 ms: 1.05x slower                                                  |
| sympy_expand                  | 269 ms                                                 | 285 ms: 1.06x slower                                                   |
| connected_components          | 318 ms                                                 | 340 ms: 1.07x slower                                                   |
| meteor_contest                | 77.8 ms                                                | 83.5 ms: 1.07x slower                                                  |
| fannkuch                      | 303 ms                                                 | 329 ms: 1.09x slower                                                   |
| sqlglot_normalize             | 192 ms                                                 | 210 ms: 1.09x slower                                                   |
| nqueens                       | 63.8 ms                                                | 71.0 ms: 1.11x slower                                                  |
| django_template               | 24.4 ms                                                | 27.1 ms: 1.11x slower                                                  |
| genshi_xml                    | 35.1 ms                                                | 39.2 ms: 1.12x slower                                                  |
| mako                          | 9.81 ms                                                | 11.0 ms: 1.12x slower                                                  |
| xml_etree_generate            | 53.9 ms                                                | 60.9 ms: 1.13x slower                                                  |
| shortest_path                 | 328 ms                                                 | 371 ms: 1.13x slower                                                   |
| genshi_text                   | 17.7 ms                                                | 20.1 ms: 1.13x slower                                                  |
| nbody                         | 92.5 ms                                                | 106 ms: 1.14x slower                                                   |
| scimark_sparse_mat_mult       | 3.42 ms                                                | 3.92 ms: 1.15x slower                                                  |
| json_loads                    | 16.6 us                                                | 19.1 us: 1.15x slower                                                  |
| bench_mp_pool                 | 56.0 ms                                                | 64.5 ms: 1.15x slower                                                  |
| async_generators              | 233 ms                                                 | 282 ms: 1.21x slower                                                   |
| python_startup_no_site        | 12.8 ms                                                | 15.8 ms: 1.23x slower                                                  |
| coverage                      | 41.2 ms                                                | 54.7 ms: 1.33x slower                                                  |
| bench_thread_pool             | 545 us                                                 | 802 us: 1.47x slower                                                   |
| telco                         | 3.49 ms                                                | 5.15 ms: 1.48x slower                                                  |
| Geometric mean                | (ref)                                                  | 1.16x faster                                                           |
Ignored benchmarks (5) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: chameleon, dask, djangocms, gevent_hub, tornado_http
Ignored benchmarks (16) of results/bm-20250208-3.14.0a4+-29f8a67-NOGIL/bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.168x faster

# HPT report

- Reliability score: 99.98% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.29x