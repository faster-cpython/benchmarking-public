# Results vs. base

- fork: python
- ref: d3d94e0ed715829d9bf9
- machine: darwin-arm64
- commit hash: d3d94e0
- commit date: 2025-08-30
- overall geometric mean: 1.010x faster
- HPT reliability: 66.76%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250830-3.15.0a0-d3d94e0/bm-20250830-darwin-arm64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0.json | results/bm-20250830-3.15.0a0-d3d94e0-JIT/bm-20250830-darwin-arm64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0.json |
|----------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 170 ms                                                                                                          | 187 ms: 1.10x slower                                                                                                |
| docutils       | 1.43 sec                                                                                                        | 1.44 sec: 1.01x slower                                                                                              |
| html5lib       | 32.5 ms                                                                                                         | 33.2 ms: 1.02x slower                                                                                               |
| Geometric mean | (ref)                                                                                                           | 1.03x slower                                                                                                        |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | results/bm-20250830-3.15.0a0-d3d94e0/bm-20250830-darwin-arm64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0.json | results/bm-20250830-3.15.0a0-d3d94e0-JIT/bm-20250830-darwin-arm64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0.json |
|-------------------------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| async_tree_io_tg              | 376 ms                                                                                                          | 367 ms: 1.03x faster                                                                                                |
| async_tree_io                 | 385 ms                                                                                                          | 378 ms: 1.02x faster                                                                                                |
| async_tree_eager_io           | 370 ms                                                                                                          | 364 ms: 1.02x faster                                                                                                |
| async_tree_none_tg            | 160 ms                                                                                                          | 158 ms: 1.01x faster                                                                                                |
| async_tree_eager              | 65.9 ms                                                                                                         | 65.0 ms: 1.01x faster                                                                                               |
| async_tree_memoization        | 197 ms                                                                                                          | 195 ms: 1.01x faster                                                                                                |
| async_tree_none               | 172 ms                                                                                                          | 170 ms: 1.01x faster                                                                                                |
| async_tree_cpu_io_mixed       | 420 ms                                                                                                          | 417 ms: 1.01x faster                                                                                                |
| async_tree_eager_cpu_io_mixed | 360 ms                                                                                                          | 363 ms: 1.01x slower                                                                                                |
| coroutines                    | 16.3 ms                                                                                                         | 16.5 ms: 1.01x slower                                                                                               |
| async_generators              | 279 ms                                                                                                          | 286 ms: 1.03x slower                                                                                                |
| Geometric mean                | (ref)                                                                                                           | 1.01x faster                                                                                                        |

Benchmark hidden because not significant (10): asyncio_tcp, async_tree_eager_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_memoization, async_tree_memoization_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_cpu_io_mixed_tg, asyncio_tcp_ssl, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250830-3.15.0a0-d3d94e0/bm-20250830-darwin-arm64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0.json | results/bm-20250830-3.15.0a0-d3d94e0-JIT/bm-20250830-darwin-arm64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0.json |
|----------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| nbody          | 80.0 ms                                                                                                         | 71.7 ms: 1.12x faster                                                                                               |
| float          | 49.1 ms                                                                                                         | 50.6 ms: 1.03x slower                                                                                               |
| Geometric mean | (ref)                                                                                                           | 1.03x faster                                                                                                        |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250830-3.15.0a0-d3d94e0/bm-20250830-darwin-arm64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0.json | results/bm-20250830-3.15.0a0-d3d94e0-JIT/bm-20250830-darwin-arm64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0.json |
|----------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| regex_v8       | 15.6 ms                                                                                                         | 15.3 ms: 1.02x faster                                                                                               |
| regex_dna      | 137 ms                                                                                                          | 138 ms: 1.00x slower                                                                                                |
| regex_compile  | 72.4 ms                                                                                                         | 72.7 ms: 1.00x slower                                                                                               |
| regex_effbot   | 2.13 ms                                                                                                         | 2.14 ms: 1.01x slower                                                                                               |
| Geometric mean | (ref)                                                                                                           | 1.00x faster                                                                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20250830-3.15.0a0-d3d94e0/bm-20250830-darwin-arm64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0.json | results/bm-20250830-3.15.0a0-d3d94e0-JIT/bm-20250830-darwin-arm64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0.json |
|----------------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| unpickle_pure_python | 155 us                                                                                                          | 129 us: 1.21x faster                                                                                                |
| xml_etree_process    | 39.5 ms                                                                                                         | 34.7 ms: 1.14x faster                                                                                               |
| tomli_loads          | 1.41 sec                                                                                                        | 1.25 sec: 1.13x faster                                                                                              |
| xml_etree_generate   | 55.6 ms                                                                                                         | 49.4 ms: 1.13x faster                                                                                               |
| pickle_pure_python   | 216 us                                                                                                          | 206 us: 1.05x faster                                                                                                |
| xml_etree_parse      | 103 ms                                                                                                          | 101 ms: 1.02x faster                                                                                                |
| pickle               | 7.64 us                                                                                                         | 7.62 us: 1.00x faster                                                                                               |
| json_loads           | 17.4 us                                                                                                         | 17.4 us: 1.00x slower                                                                                               |
| unpickle             | 9.00 us                                                                                                         | 9.04 us: 1.00x slower                                                                                               |
| pickle_list          | 3.03 us                                                                                                         | 3.05 us: 1.01x slower                                                                                               |
| unpickle_list        | 3.04 us                                                                                                         | 3.06 us: 1.01x slower                                                                                               |
| json_dumps           | 5.67 ms                                                                                                         | 5.77 ms: 1.02x slower                                                                                               |
| Geometric mean       | (ref)                                                                                                           | 1.04x faster                                                                                                        |

Benchmark hidden because not significant (2): xml_etree_iterparse, pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20250830-3.15.0a0-d3d94e0/bm-20250830-darwin-arm64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0.json | results/bm-20250830-3.15.0a0-d3d94e0-JIT/bm-20250830-darwin-arm64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0.json |
|------------------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| python_startup         | 18.8 ms                                                                                                         | 18.9 ms: 1.01x slower                                                                                               |
| python_startup_no_site | 14.3 ms                                                                                                         | 14.4 ms: 1.01x slower                                                                                               |
| Geometric mean         | (ref)                                                                                                           | 1.01x slower                                                                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20250830-3.15.0a0-d3d94e0/bm-20250830-darwin-arm64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0.json | results/bm-20250830-3.15.0a0-d3d94e0-JIT/bm-20250830-darwin-arm64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0.json |
|-----------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| mako            | 8.04 ms                                                                                                         | 6.50 ms: 1.24x faster                                                                                               |
| django_template | 23.0 ms                                                                                                         | 23.3 ms: 1.01x slower                                                                                               |
| genshi_xml      | 32.6 ms                                                                                                         | 33.3 ms: 1.02x slower                                                                                               |
| genshi_text     | 14.9 ms                                                                                                         | 15.5 ms: 1.04x slower                                                                                               |
| Geometric mean  | (ref)                                                                                                           | 1.04x faster                                                                                                        |

All benchmarks:
===============

| Benchmark                     | results/bm-20250830-3.15.0a0-d3d94e0/bm-20250830-darwin-arm64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0.json | results/bm-20250830-3.15.0a0-d3d94e0-JIT/bm-20250830-darwin-arm64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0.json |
|-------------------------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| mako                          | 8.04 ms                                                                                                         | 6.50 ms: 1.24x faster                                                                                               |
| pprint_pformat                | 1.11 sec                                                                                                        | 900 ms: 1.23x faster                                                                                                |
| pprint_safe_repr              | 546 ms                                                                                                          | 449 ms: 1.22x faster                                                                                                |
| unpickle_pure_python          | 155 us                                                                                                          | 129 us: 1.21x faster                                                                                                |
| xml_etree_process             | 39.5 ms                                                                                                         | 34.7 ms: 1.14x faster                                                                                               |
| tomli_loads                   | 1.41 sec                                                                                                        | 1.25 sec: 1.13x faster                                                                                              |
| xml_etree_generate            | 55.6 ms                                                                                                         | 49.4 ms: 1.13x faster                                                                                               |
| nbody                         | 80.0 ms                                                                                                         | 71.7 ms: 1.12x faster                                                                                               |
| fannkuch                      | 276 ms                                                                                                          | 249 ms: 1.11x faster                                                                                                |
| bpe_tokeniser                 | 3.14 sec                                                                                                        | 2.92 sec: 1.08x faster                                                                                              |
| pyflate                       | 301 ms                                                                                                          | 285 ms: 1.06x faster                                                                                                |
| telco                         | 4.16 ms                                                                                                         | 3.95 ms: 1.05x faster                                                                                               |
| sqlglot_v2_parse              | 821 us                                                                                                          | 781 us: 1.05x faster                                                                                                |
| pickle_pure_python            | 216 us                                                                                                          | 206 us: 1.05x faster                                                                                                |
| crypto_pyaes                  | 51.6 ms                                                                                                         | 49.6 ms: 1.04x faster                                                                                               |
| sqlglot_v2_transpile          | 989 us                                                                                                          | 951 us: 1.04x faster                                                                                                |
| comprehensions                | 11.7 us                                                                                                         | 11.4 us: 1.03x faster                                                                                               |
| sqlite_synth                  | 1.61 us                                                                                                         | 1.57 us: 1.03x faster                                                                                               |
| async_tree_io_tg              | 376 ms                                                                                                          | 367 ms: 1.03x faster                                                                                                |
| xml_etree_parse               | 103 ms                                                                                                          | 101 ms: 1.02x faster                                                                                                |
| regex_v8                      | 15.6 ms                                                                                                         | 15.3 ms: 1.02x faster                                                                                               |
| async_tree_io                 | 385 ms                                                                                                          | 378 ms: 1.02x faster                                                                                                |
| async_tree_eager_io           | 370 ms                                                                                                          | 364 ms: 1.02x faster                                                                                                |
| async_tree_none_tg            | 160 ms                                                                                                          | 158 ms: 1.01x faster                                                                                                |
| async_tree_eager              | 65.9 ms                                                                                                         | 65.0 ms: 1.01x faster                                                                                               |
| async_tree_memoization        | 197 ms                                                                                                          | 195 ms: 1.01x faster                                                                                                |
| async_tree_none               | 172 ms                                                                                                          | 170 ms: 1.01x faster                                                                                                |
| raytrace                      | 177 ms                                                                                                          | 175 ms: 1.01x faster                                                                                                |
| meteor_contest                | 73.4 ms                                                                                                         | 72.7 ms: 1.01x faster                                                                                               |
| async_tree_cpu_io_mixed       | 420 ms                                                                                                          | 417 ms: 1.01x faster                                                                                                |
| typing_runtime_protocols      | 97.1 us                                                                                                         | 96.5 us: 1.01x faster                                                                                               |
| sympy_sum                     | 77.1 ms                                                                                                         | 76.7 ms: 1.01x faster                                                                                               |
| coverage                      | 47.8 ms                                                                                                         | 47.5 ms: 1.01x faster                                                                                               |
| sqlglot_v2_optimize           | 33.7 ms                                                                                                         | 33.6 ms: 1.00x faster                                                                                               |
| pickle                        | 7.64 us                                                                                                         | 7.62 us: 1.00x faster                                                                                               |
| regex_dna                     | 137 ms                                                                                                          | 138 ms: 1.00x slower                                                                                                |
| gc_traversal                  | 3.16 ms                                                                                                         | 3.17 ms: 1.00x slower                                                                                               |
| json_loads                    | 17.4 us                                                                                                         | 17.4 us: 1.00x slower                                                                                               |
| chaos                         | 38.8 ms                                                                                                         | 38.9 ms: 1.00x slower                                                                                               |
| unpickle                      | 9.00 us                                                                                                         | 9.04 us: 1.00x slower                                                                                               |
| regex_compile                 | 72.4 ms                                                                                                         | 72.7 ms: 1.00x slower                                                                                               |
| richards_super                | 37.2 ms                                                                                                         | 37.4 ms: 1.01x slower                                                                                               |
| dulwich_log                   | 25.2 ms                                                                                                         | 25.3 ms: 1.01x slower                                                                                               |
| regex_effbot                  | 2.13 ms                                                                                                         | 2.14 ms: 1.01x slower                                                                                               |
| docutils                      | 1.43 sec                                                                                                        | 1.44 sec: 1.01x slower                                                                                              |
| pickle_list                   | 3.03 us                                                                                                         | 3.05 us: 1.01x slower                                                                                               |
| unpickle_list                 | 3.04 us                                                                                                         | 3.06 us: 1.01x slower                                                                                               |
| scimark_sor                   | 83.1 ms                                                                                                         | 83.7 ms: 1.01x slower                                                                                               |
| python_startup                | 18.8 ms                                                                                                         | 18.9 ms: 1.01x slower                                                                                               |
| mdp                           | 772 ms                                                                                                          | 779 ms: 1.01x slower                                                                                                |
| richards                      | 33.2 ms                                                                                                         | 33.5 ms: 1.01x slower                                                                                               |
| sympy_integrate               | 10.8 ms                                                                                                         | 10.9 ms: 1.01x slower                                                                                               |
| sympy_expand                  | 246 ms                                                                                                          | 248 ms: 1.01x slower                                                                                                |
| async_tree_eager_cpu_io_mixed | 360 ms                                                                                                          | 363 ms: 1.01x slower                                                                                                |
| logging_format                | 3.55 us                                                                                                         | 3.58 us: 1.01x slower                                                                                               |
| python_startup_no_site        | 14.3 ms                                                                                                         | 14.4 ms: 1.01x slower                                                                                               |
| django_template               | 23.0 ms                                                                                                         | 23.3 ms: 1.01x slower                                                                                               |
| coroutines                    | 16.3 ms                                                                                                         | 16.5 ms: 1.01x slower                                                                                               |
| pycparser                     | 687 ms                                                                                                          | 695 ms: 1.01x slower                                                                                                |
| generators                    | 24.4 ms                                                                                                         | 24.7 ms: 1.01x slower                                                                                               |
| spectral_norm                 | 62.8 ms                                                                                                         | 63.8 ms: 1.02x slower                                                                                               |
| json_dumps                    | 5.67 ms                                                                                                         | 5.77 ms: 1.02x slower                                                                                               |
| logging_simple                | 3.26 us                                                                                                         | 3.31 us: 1.02x slower                                                                                               |
| hexiom                        | 4.53 ms                                                                                                         | 4.61 ms: 1.02x slower                                                                                               |
| logging_silent                | 71.9 ns                                                                                                         | 73.3 ns: 1.02x slower                                                                                               |
| html5lib                      | 32.5 ms                                                                                                         | 33.2 ms: 1.02x slower                                                                                               |
| deepcopy_reduce               | 1.76 us                                                                                                         | 1.80 us: 1.02x slower                                                                                               |
| genshi_xml                    | 32.6 ms                                                                                                         | 33.3 ms: 1.02x slower                                                                                               |
| nqueens                       | 61.0 ms                                                                                                         | 62.3 ms: 1.02x slower                                                                                               |
| deepcopy                      | 171 us                                                                                                          | 174 us: 1.02x slower                                                                                                |
| scimark_lu                    | 73.8 ms                                                                                                         | 75.6 ms: 1.03x slower                                                                                               |
| async_generators              | 279 ms                                                                                                          | 286 ms: 1.03x slower                                                                                                |
| deepcopy_memo                 | 21.2 us                                                                                                         | 21.8 us: 1.03x slower                                                                                               |
| scimark_fft                   | 187 ms                                                                                                          | 192 ms: 1.03x slower                                                                                                |
| float                         | 49.1 ms                                                                                                         | 50.6 ms: 1.03x slower                                                                                               |
| subparsers                    | 25.4 ms                                                                                                         | 26.3 ms: 1.03x slower                                                                                               |
| many_optionals                | 594 us                                                                                                          | 615 us: 1.03x slower                                                                                                |
| scimark_monte_carlo           | 44.4 ms                                                                                                         | 46.2 ms: 1.04x slower                                                                                               |
| genshi_text                   | 14.9 ms                                                                                                         | 15.5 ms: 1.04x slower                                                                                               |
| go                            | 84.0 ms                                                                                                         | 87.6 ms: 1.04x slower                                                                                               |
| deltablue                     | 2.42 ms                                                                                                         | 2.53 ms: 1.05x slower                                                                                               |
| k_core                        | 1.52 sec                                                                                                        | 1.59 sec: 1.05x slower                                                                                              |
| shortest_path                 | 334 ms                                                                                                          | 351 ms: 1.05x slower                                                                                                |
| connected_components          | 306 ms                                                                                                          | 322 ms: 1.05x slower                                                                                                |
| scimark_sparse_mat_mult       | 3.12 ms                                                                                                         | 3.41 ms: 1.09x slower                                                                                               |
| 2to3                          | 170 ms                                                                                                          | 187 ms: 1.10x slower                                                                                                |
| unpack_sequence               | 38.0 ns                                                                                                         | 48.1 ns: 1.27x slower                                                                                               |
| Geometric mean                | (ref)                                                                                                           | 1.01x faster                                                                                                        |

Benchmark hidden because not significant (24): asyncio_tcp, async_tree_eager_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, xml_etree_iterparse, async_tree_eager_memoization, async_tree_memoization_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_cpu_io_mixed_tg, asyncio_tcp_ssl, pickle_dict, bench_thread_pool, sympy_str, dask, create_gc_cycles, pidigits, pylint, asyncio_websockets, thrift, sqlglot_v2_normalize, json, pathlib, bench_mp_pool, sphinx

- Geometric mean (including insignificant results): 1.010x faster

# HPT report

- Reliability score: 66.76% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.02x