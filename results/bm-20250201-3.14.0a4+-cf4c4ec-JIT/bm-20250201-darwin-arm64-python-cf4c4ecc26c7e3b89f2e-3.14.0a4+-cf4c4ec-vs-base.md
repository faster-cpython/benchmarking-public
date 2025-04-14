# Results vs. base

- fork: python
- ref: cf4c4ecc26c7e3b89f2e
- machine: darwin-arm64
- commit hash: cf4c4ec
- commit date: 2025-02-01
- overall geometric mean: 1.041x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250201-3.14.0a4+-cf4c4ec/bm-20250201-darwin-arm64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec.json | results/bm-20250201-3.14.0a4+-cf4c4ec-JIT/bm-20250201-darwin-arm64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 158 ms                                                                                                            | 164 ms: 1.03x slower                                                                                                  |
| docutils       | 1.40 sec                                                                                                          | 1.45 sec: 1.04x slower                                                                                                |
| html5lib       | 28.6 ms                                                                                                           | 31.7 ms: 1.11x slower                                                                                                 |
| sphinx         | 558 ms                                                                                                            | 586 ms: 1.05x slower                                                                                                  |
| Geometric mean | (ref)                                                                                                             | 1.06x slower                                                                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | results/bm-20250201-3.14.0a4+-cf4c4ec/bm-20250201-darwin-arm64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec.json | results/bm-20250201-3.14.0a4+-cf4c4ec-JIT/bm-20250201-darwin-arm64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec.json |
|-------------------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed_tg    | 416 ms                                                                                                            | 413 ms: 1.01x faster                                                                                                  |
| coroutines                    | 15.7 ms                                                                                                           | 15.6 ms: 1.01x faster                                                                                                 |
| async_tree_eager_cpu_io_mixed | 358 ms                                                                                                            | 359 ms: 1.00x slower                                                                                                  |
| async_tree_memoization        | 194 ms                                                                                                            | 196 ms: 1.01x slower                                                                                                  |
| async_tree_none               | 158 ms                                                                                                            | 161 ms: 1.02x slower                                                                                                  |
| async_tree_eager_memoization  | 140 ms                                                                                                            | 144 ms: 1.03x slower                                                                                                  |
| async_tree_eager              | 61.9 ms                                                                                                           | 65.7 ms: 1.06x slower                                                                                                 |
| async_generators              | 246 ms                                                                                                            | 271 ms: 1.10x slower                                                                                                  |
| Geometric mean                | (ref)                                                                                                             | 1.01x slower                                                                                                          |

Benchmark hidden because not significant (13): asyncio_tcp, async_tree_eager_cpu_io_mixed_tg, async_tree_io_tg, async_tree_cpu_io_mixed, async_tree_eager_io_tg, asyncio_websockets, async_tree_none_tg, asyncio_tcp_ssl, async_tree_eager_io, async_tree_eager_tg, async_tree_eager_memoization_tg, async_tree_memoization_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250201-3.14.0a4+-cf4c4ec/bm-20250201-darwin-arm64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec.json | results/bm-20250201-3.14.0a4+-cf4c4ec-JIT/bm-20250201-darwin-arm64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| nbody          | 68.6 ms                                                                                                           | 63.9 ms: 1.07x faster                                                                                                 |
| float          | 46.2 ms                                                                                                           | 45.5 ms: 1.02x faster                                                                                                 |
| Geometric mean | (ref)                                                                                                             | 1.03x faster                                                                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250201-3.14.0a4+-cf4c4ec/bm-20250201-darwin-arm64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec.json | results/bm-20250201-3.14.0a4+-cf4c4ec-JIT/bm-20250201-darwin-arm64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| regex_effbot   | 2.28 ms                                                                                                           | 2.24 ms: 1.02x faster                                                                                                 |
| regex_dna      | 141 ms                                                                                                            | 140 ms: 1.01x faster                                                                                                  |
| regex_v8       | 16.8 ms                                                                                                           | 16.7 ms: 1.01x faster                                                                                                 |
| regex_compile  | 65.5 ms                                                                                                           | 67.5 ms: 1.03x slower                                                                                                 |
| Geometric mean | (ref)                                                                                                             | 1.00x slower                                                                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20250201-3.14.0a4+-cf4c4ec/bm-20250201-darwin-arm64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec.json | results/bm-20250201-3.14.0a4+-cf4c4ec-JIT/bm-20250201-darwin-arm64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec.json |
|----------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| xml_etree_process    | 37.7 ms                                                                                                           | 35.4 ms: 1.07x faster                                                                                                 |
| unpickle_pure_python | 137 us                                                                                                            | 130 us: 1.06x faster                                                                                                  |
| xml_etree_generate   | 51.9 ms                                                                                                           | 49.6 ms: 1.05x faster                                                                                                 |
| json_dumps           | 7.29 ms                                                                                                           | 7.10 ms: 1.03x faster                                                                                                 |
| pickle_pure_python   | 195 us                                                                                                            | 191 us: 1.02x faster                                                                                                  |
| xml_etree_iterparse  | 70.6 ms                                                                                                           | 69.4 ms: 1.02x faster                                                                                                 |
| unpickle_list        | 2.91 us                                                                                                           | 2.93 us: 1.01x slower                                                                                                 |
| unpickle             | 9.11 us                                                                                                           | 9.21 us: 1.01x slower                                                                                                 |
| tomli_loads          | 1.18 sec                                                                                                          | 1.21 sec: 1.02x slower                                                                                                |
| Geometric mean       | (ref)                                                                                                             | 1.01x faster                                                                                                          |

Benchmark hidden because not significant (5): xml_etree_parse, pickle_list, json_loads, pickle_dict, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20250201-3.14.0a4+-cf4c4ec/bm-20250201-darwin-arm64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec.json | results/bm-20250201-3.14.0a4+-cf4c4ec-JIT/bm-20250201-darwin-arm64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec.json |
|------------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| python_startup         | 16.0 ms                                                                                                           | 16.6 ms: 1.04x slower                                                                                                 |
| python_startup_no_site | 11.4 ms                                                                                                           | 12.1 ms: 1.06x slower                                                                                                 |
| Geometric mean         | (ref)                                                                                                             | 1.05x slower                                                                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20250201-3.14.0a4+-cf4c4ec/bm-20250201-darwin-arm64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec.json | results/bm-20250201-3.14.0a4+-cf4c4ec-JIT/bm-20250201-darwin-arm64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec.json |
|-----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| mako            | 7.21 ms                                                                                                           | 6.39 ms: 1.13x faster                                                                                                 |
| django_template | 20.4 ms                                                                                                           | 22.2 ms: 1.08x slower                                                                                                 |
| genshi_text     | 13.3 ms                                                                                                           | 15.6 ms: 1.17x slower                                                                                                 |
| genshi_xml      | 28.0 ms                                                                                                           | 40.2 ms: 1.43x slower                                                                                                 |
| Geometric mean  | (ref)                                                                                                             | 1.13x slower                                                                                                          |

All benchmarks:
===============

| Benchmark                     | results/bm-20250201-3.14.0a4+-cf4c4ec/bm-20250201-darwin-arm64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec.json | results/bm-20250201-3.14.0a4+-cf4c4ec-JIT/bm-20250201-darwin-arm64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec.json |
|-------------------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| mako                          | 7.21 ms                                                                                                           | 6.39 ms: 1.13x faster                                                                                                 |
| nbody                         | 68.6 ms                                                                                                           | 63.9 ms: 1.07x faster                                                                                                 |
| xml_etree_process             | 37.7 ms                                                                                                           | 35.4 ms: 1.07x faster                                                                                                 |
| unpickle_pure_python          | 137 us                                                                                                            | 130 us: 1.06x faster                                                                                                  |
| xml_etree_generate            | 51.9 ms                                                                                                           | 49.6 ms: 1.05x faster                                                                                                 |
| scimark_lu                    | 71.7 ms                                                                                                           | 69.7 ms: 1.03x faster                                                                                                 |
| json_dumps                    | 7.29 ms                                                                                                           | 7.10 ms: 1.03x faster                                                                                                 |
| pickle_pure_python            | 195 us                                                                                                            | 191 us: 1.02x faster                                                                                                  |
| xml_etree_iterparse           | 70.6 ms                                                                                                           | 69.4 ms: 1.02x faster                                                                                                 |
| regex_effbot                  | 2.28 ms                                                                                                           | 2.24 ms: 1.02x faster                                                                                                 |
| float                         | 46.2 ms                                                                                                           | 45.5 ms: 1.02x faster                                                                                                 |
| regex_dna                     | 141 ms                                                                                                            | 140 ms: 1.01x faster                                                                                                  |
| telco                         | 4.54 ms                                                                                                           | 4.51 ms: 1.01x faster                                                                                                 |
| async_tree_cpu_io_mixed_tg    | 416 ms                                                                                                            | 413 ms: 1.01x faster                                                                                                  |
| regex_v8                      | 16.8 ms                                                                                                           | 16.7 ms: 1.01x faster                                                                                                 |
| coroutines                    | 15.7 ms                                                                                                           | 15.6 ms: 1.01x faster                                                                                                 |
| deepcopy_memo                 | 17.7 us                                                                                                           | 17.7 us: 1.00x faster                                                                                                 |
| async_tree_eager_cpu_io_mixed | 358 ms                                                                                                            | 359 ms: 1.00x slower                                                                                                  |
| gc_traversal                  | 3.10 ms                                                                                                           | 3.11 ms: 1.00x slower                                                                                                 |
| connected_components          | 295 ms                                                                                                            | 297 ms: 1.01x slower                                                                                                  |
| unpickle_list                 | 2.91 us                                                                                                           | 2.93 us: 1.01x slower                                                                                                 |
| unpickle                      | 9.11 us                                                                                                           | 9.21 us: 1.01x slower                                                                                                 |
| sqlalchemy_declarative        | 57.6 ms                                                                                                           | 58.3 ms: 1.01x slower                                                                                                 |
| async_tree_memoization        | 194 ms                                                                                                            | 196 ms: 1.01x slower                                                                                                  |
| pathlib                       | 21.8 ms                                                                                                           | 22.1 ms: 1.01x slower                                                                                                 |
| shortest_path                 | 323 ms                                                                                                            | 328 ms: 1.02x slower                                                                                                  |
| scimark_fft                   | 170 ms                                                                                                            | 173 ms: 1.02x slower                                                                                                  |
| async_tree_none               | 158 ms                                                                                                            | 161 ms: 1.02x slower                                                                                                  |
| sqlite_synth                  | 1.52 us                                                                                                           | 1.55 us: 1.02x slower                                                                                                 |
| tomli_loads                   | 1.18 sec                                                                                                          | 1.21 sec: 1.02x slower                                                                                                |
| thrift                        | 426 us                                                                                                            | 436 us: 1.02x slower                                                                                                  |
| crypto_pyaes                  | 51.4 ms                                                                                                           | 52.7 ms: 1.03x slower                                                                                                 |
| regex_compile                 | 65.5 ms                                                                                                           | 67.5 ms: 1.03x slower                                                                                                 |
| async_tree_eager_memoization  | 140 ms                                                                                                            | 144 ms: 1.03x slower                                                                                                  |
| sympy_sum                     | 72.3 ms                                                                                                           | 74.6 ms: 1.03x slower                                                                                                 |
| typing_runtime_protocols      | 92.7 us                                                                                                           | 95.7 us: 1.03x slower                                                                                                 |
| deepcopy_reduce               | 1.52 us                                                                                                           | 1.57 us: 1.03x slower                                                                                                 |
| 2to3                          | 158 ms                                                                                                            | 164 ms: 1.03x slower                                                                                                  |
| pylint                        | 158 ms                                                                                                            | 163 ms: 1.04x slower                                                                                                  |
| spectral_norm                 | 59.6 ms                                                                                                           | 61.9 ms: 1.04x slower                                                                                                 |
| python_startup                | 16.0 ms                                                                                                           | 16.6 ms: 1.04x slower                                                                                                 |
| subparsers                    | 11.7 ms                                                                                                           | 12.2 ms: 1.04x slower                                                                                                 |
| sympy_expand                  | 228 ms                                                                                                            | 237 ms: 1.04x slower                                                                                                  |
| docutils                      | 1.40 sec                                                                                                          | 1.45 sec: 1.04x slower                                                                                                |
| sympy_integrate               | 11.0 ms                                                                                                           | 11.5 ms: 1.04x slower                                                                                                 |
| sympy_str                     | 136 ms                                                                                                            | 142 ms: 1.05x slower                                                                                                  |
| sqlalchemy_imperative         | 6.34 ms                                                                                                           | 6.64 ms: 1.05x slower                                                                                                 |
| sphinx                        | 558 ms                                                                                                            | 586 ms: 1.05x slower                                                                                                  |
| mdp                           | 1.48 sec                                                                                                          | 1.55 sec: 1.05x slower                                                                                                |
| dulwich_log                   | 27.2 ms                                                                                                           | 28.6 ms: 1.05x slower                                                                                                 |
| meteor_contest                | 69.8 ms                                                                                                           | 73.5 ms: 1.05x slower                                                                                                 |
| sqlglot_normalize             | 176 ms                                                                                                            | 185 ms: 1.05x slower                                                                                                  |
| sqlglot_optimize              | 31.8 ms                                                                                                           | 33.7 ms: 1.06x slower                                                                                                 |
| bench_thread_pool             | 477 us                                                                                                            | 505 us: 1.06x slower                                                                                                  |
| many_optionals                | 431 us                                                                                                            | 457 us: 1.06x slower                                                                                                  |
| async_tree_eager              | 61.9 ms                                                                                                           | 65.7 ms: 1.06x slower                                                                                                 |
| python_startup_no_site        | 11.4 ms                                                                                                           | 12.1 ms: 1.06x slower                                                                                                 |
| django_template               | 20.4 ms                                                                                                           | 22.2 ms: 1.08x slower                                                                                                 |
| pyflate                       | 283 ms                                                                                                            | 308 ms: 1.09x slower                                                                                                  |
| deepcopy                      | 146 us                                                                                                            | 159 us: 1.09x slower                                                                                                  |
| deltablue                     | 2.28 ms                                                                                                           | 2.50 ms: 1.09x slower                                                                                                 |
| async_generators              | 246 ms                                                                                                            | 271 ms: 1.10x slower                                                                                                  |
| logging_format                | 3.40 us                                                                                                           | 3.74 us: 1.10x slower                                                                                                 |
| scimark_monte_carlo           | 42.1 ms                                                                                                           | 46.3 ms: 1.10x slower                                                                                                 |
| pycparser                     | 633 ms                                                                                                            | 697 ms: 1.10x slower                                                                                                  |
| richards_super                | 34.9 ms                                                                                                           | 38.4 ms: 1.10x slower                                                                                                 |
| richards                      | 31.2 ms                                                                                                           | 34.4 ms: 1.10x slower                                                                                                 |
| scimark_sor                   | 75.9 ms                                                                                                           | 83.9 ms: 1.10x slower                                                                                                 |
| html5lib                      | 28.6 ms                                                                                                           | 31.7 ms: 1.11x slower                                                                                                 |
| sqlglot_transpile             | 915 us                                                                                                            | 1.02 ms: 1.11x slower                                                                                                 |
| logging_simple                | 3.10 us                                                                                                           | 3.45 us: 1.11x slower                                                                                                 |
| scimark_sparse_mat_mult       | 2.62 ms                                                                                                           | 2.92 ms: 1.11x slower                                                                                                 |
| sqlglot_parse                 | 757 us                                                                                                            | 844 us: 1.12x slower                                                                                                  |
| pprint_pformat                | 919 ms                                                                                                            | 1.03 sec: 1.12x slower                                                                                                |
| chaos                         | 37.3 ms                                                                                                           | 41.7 ms: 1.12x slower                                                                                                 |
| nqueens                       | 56.5 ms                                                                                                           | 63.2 ms: 1.12x slower                                                                                                 |
| raytrace                      | 168 ms                                                                                                            | 188 ms: 1.12x slower                                                                                                  |
| pprint_safe_repr              | 452 ms                                                                                                            | 510 ms: 1.13x slower                                                                                                  |
| logging_silent                | 67.3 ns                                                                                                           | 76.3 ns: 1.13x slower                                                                                                 |
| fannkuch                      | 243 ms                                                                                                            | 278 ms: 1.15x slower                                                                                                  |
| comprehensions                | 11.8 us                                                                                                           | 13.8 us: 1.17x slower                                                                                                 |
| genshi_text                   | 13.3 ms                                                                                                           | 15.6 ms: 1.17x slower                                                                                                 |
| generators                    | 23.1 ms                                                                                                           | 27.8 ms: 1.20x slower                                                                                                 |
| hexiom                        | 4.16 ms                                                                                                           | 5.05 ms: 1.21x slower                                                                                                 |
| go                            | 77.2 ms                                                                                                           | 97.5 ms: 1.26x slower                                                                                                 |
| unpack_sequence               | 27.8 ns                                                                                                           | 39.1 ns: 1.41x slower                                                                                                 |
| genshi_xml                    | 28.0 ms                                                                                                           | 40.2 ms: 1.43x slower                                                                                                 |
| Geometric mean                | (ref)                                                                                                             | 1.04x slower                                                                                                          |

Benchmark hidden because not significant (26): asyncio_tcp, xml_etree_parse, async_tree_eager_cpu_io_mixed_tg, async_tree_io_tg, create_gc_cycles, async_tree_cpu_io_mixed, json, pickle_list, json_loads, async_tree_eager_io_tg, bench_mp_pool, dask, pickle_dict, pidigits, bpe_tokeniser, asyncio_websockets, async_tree_none_tg, asyncio_tcp_ssl, pickle, coverage, async_tree_eager_io, async_tree_eager_tg, async_tree_eager_memoization_tg, async_tree_memoization_tg, async_tree_io, k_core

- Geometric mean (including insignificant results): 1.041x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 1.02x