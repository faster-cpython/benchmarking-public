# Results vs. base

- fork: python
- ref: 401fff7423ca3c8bf1d0
- machine: darwin-arm64
- commit hash: 401fff7
- commit date: 2024-09-14
- overall geometric mean: 1.049x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20240914-3.14.0a0-401fff7/bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7.json | results/bm-20240914-3.14.0a0-401fff7-JIT/bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7.json |
|----------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 159 ms                                                                                                          | 178 ms: 1.12x slower                                                                                                |
| docutils       | 1.40 sec                                                                                                        | 1.57 sec: 1.12x slower                                                                                              |
| html5lib       | 30.1 ms                                                                                                         | 32.8 ms: 1.09x slower                                                                                               |
| Geometric mean | (ref)                                                                                                           | 1.12x slower                                                                                                        |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                    | results/bm-20240914-3.14.0a0-401fff7/bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7.json | results/bm-20240914-3.14.0a0-401fff7-JIT/bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7.json |
|------------------------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| asyncio_tcp                  | 440 ms                                                                                                          | 396 ms: 1.11x faster                                                                                                |
| coroutines                   | 16.0 ms                                                                                                         | 16.1 ms: 1.00x slower                                                                                               |
| async_tree_cpu_io_mixed_tg   | 462 ms                                                                                                          | 464 ms: 1.00x slower                                                                                                |
| async_tree_eager_tg          | 42.1 ms                                                                                                         | 42.7 ms: 1.01x slower                                                                                               |
| async_tree_cpu_io_mixed      | 460 ms                                                                                                          | 470 ms: 1.02x slower                                                                                                |
| async_tree_eager_memoization | 153 ms                                                                                                          | 157 ms: 1.03x slower                                                                                                |
| async_tree_io                | 580 ms                                                                                                          | 597 ms: 1.03x slower                                                                                                |
| async_tree_eager             | 61.1 ms                                                                                                         | 64.5 ms: 1.06x slower                                                                                               |
| async_generators             | 278 ms                                                                                                          | 295 ms: 1.06x slower                                                                                                |
| Geometric mean               | (ref)                                                                                                           | 1.01x slower                                                                                                        |

Benchmark hidden because not significant (12): async_tree_io_tg, async_tree_eager_cpu_io_mixed_tg, asyncio_websockets, async_tree_none_tg, async_tree_eager_cpu_io_mixed, async_tree_memoization_tg, async_tree_eager_io, asyncio_tcp_ssl, async_tree_eager_memoization_tg, async_tree_eager_io_tg, async_tree_memoization, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20240914-3.14.0a0-401fff7/bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7.json | results/bm-20240914-3.14.0a0-401fff7-JIT/bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7.json |
|----------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| float          | 48.7 ms                                                                                                         | 46.6 ms: 1.04x faster                                                                                               |
| pidigits       | 282 ms                                                                                                          | 282 ms: 1.00x slower                                                                                                |
| nbody          | 60.0 ms                                                                                                         | 63.5 ms: 1.06x slower                                                                                               |
| Geometric mean | (ref)                                                                                                           | 1.01x slower                                                                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20240914-3.14.0a0-401fff7/bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7.json | results/bm-20240914-3.14.0a0-401fff7-JIT/bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7.json |
|----------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| regex_dna      | 145 ms                                                                                                          | 145 ms: 1.00x slower                                                                                                |
| regex_effbot   | 2.44 ms                                                                                                         | 2.47 ms: 1.01x slower                                                                                               |
| regex_v8       | 16.4 ms                                                                                                         | 16.6 ms: 1.01x slower                                                                                               |
| regex_compile  | 67.2 ms                                                                                                         | 74.9 ms: 1.11x slower                                                                                               |
| Geometric mean | (ref)                                                                                                           | 1.03x slower                                                                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20240914-3.14.0a0-401fff7/bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7.json | results/bm-20240914-3.14.0a0-401fff7-JIT/bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7.json |
|----------------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| tomli_loads          | 1.48 sec                                                                                                        | 1.24 sec: 1.19x faster                                                                                              |
| xml_etree_process    | 37.6 ms                                                                                                         | 34.6 ms: 1.09x faster                                                                                               |
| unpickle_pure_python | 140 us                                                                                                          | 131 us: 1.07x faster                                                                                                |
| xml_etree_generate   | 52.7 ms                                                                                                         | 51.3 ms: 1.03x faster                                                                                               |
| xml_etree_iterparse  | 73.7 ms                                                                                                         | 71.8 ms: 1.03x faster                                                                                               |
| xml_etree_parse      | 110 ms                                                                                                          | 108 ms: 1.02x faster                                                                                                |
| pickle_pure_python   | 181 us                                                                                                          | 179 us: 1.01x faster                                                                                                |
| json_dumps           | 6.43 ms                                                                                                         | 6.36 ms: 1.01x faster                                                                                               |
| pickle_dict          | 18.3 us                                                                                                         | 18.3 us: 1.00x faster                                                                                               |
| pickle_list          | 2.94 us                                                                                                         | 2.96 us: 1.01x slower                                                                                               |
| unpickle             | 9.24 us                                                                                                         | 9.37 us: 1.01x slower                                                                                               |
| Geometric mean       | (ref)                                                                                                           | 1.03x faster                                                                                                        |

Benchmark hidden because not significant (3): pickle, unpickle_list, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20240914-3.14.0a0-401fff7/bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7.json | results/bm-20240914-3.14.0a0-401fff7-JIT/bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7.json |
|------------------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| python_startup         | 17.0 ms                                                                                                         | 17.1 ms: 1.01x slower                                                                                               |
| python_startup_no_site | 13.8 ms                                                                                                         | 14.1 ms: 1.02x slower                                                                                               |
| Geometric mean         | (ref)                                                                                                           | 1.01x slower                                                                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20240914-3.14.0a0-401fff7/bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7.json | results/bm-20240914-3.14.0a0-401fff7-JIT/bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7.json |
|-----------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| mako            | 6.93 ms                                                                                                         | 6.51 ms: 1.06x faster                                                                                               |
| django_template | 20.0 ms                                                                                                         | 23.2 ms: 1.16x slower                                                                                               |
| genshi_text     | 13.9 ms                                                                                                         | 16.8 ms: 1.21x slower                                                                                               |
| genshi_xml      | 30.2 ms                                                                                                         | 41.6 ms: 1.38x slower                                                                                               |
| Geometric mean  | (ref)                                                                                                           | 1.16x slower                                                                                                        |

All benchmarks:
===============

| Benchmark                    | results/bm-20240914-3.14.0a0-401fff7/bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7.json | results/bm-20240914-3.14.0a0-401fff7-JIT/bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7.json |
|------------------------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| tomli_loads                  | 1.48 sec                                                                                                        | 1.24 sec: 1.19x faster                                                                                              |
| asyncio_tcp                  | 440 ms                                                                                                          | 396 ms: 1.11x faster                                                                                                |
| xml_etree_process            | 37.6 ms                                                                                                         | 34.6 ms: 1.09x faster                                                                                               |
| unpickle_pure_python         | 140 us                                                                                                          | 131 us: 1.07x faster                                                                                                |
| mako                         | 6.93 ms                                                                                                         | 6.51 ms: 1.06x faster                                                                                               |
| scimark_sor                  | 93.1 ms                                                                                                         | 88.3 ms: 1.05x faster                                                                                               |
| float                        | 48.7 ms                                                                                                         | 46.6 ms: 1.04x faster                                                                                               |
| scimark_lu                   | 67.8 ms                                                                                                         | 65.4 ms: 1.04x faster                                                                                               |
| xml_etree_generate           | 52.7 ms                                                                                                         | 51.3 ms: 1.03x faster                                                                                               |
| xml_etree_iterparse          | 73.7 ms                                                                                                         | 71.8 ms: 1.03x faster                                                                                               |
| deepcopy_memo                | 16.5 us                                                                                                         | 16.2 us: 1.02x faster                                                                                               |
| xml_etree_parse              | 110 ms                                                                                                          | 108 ms: 1.02x faster                                                                                                |
| logging_format               | 3.35 us                                                                                                         | 3.30 us: 1.01x faster                                                                                               |
| pickle_pure_python           | 181 us                                                                                                          | 179 us: 1.01x faster                                                                                                |
| json_dumps                   | 6.43 ms                                                                                                         | 6.36 ms: 1.01x faster                                                                                               |
| bpe_tokeniser                | 3.13 sec                                                                                                        | 3.10 sec: 1.01x faster                                                                                              |
| logging_simple               | 3.02 us                                                                                                         | 3.01 us: 1.00x faster                                                                                               |
| pickle_dict                  | 18.3 us                                                                                                         | 18.3 us: 1.00x faster                                                                                               |
| pidigits                     | 282 ms                                                                                                          | 282 ms: 1.00x slower                                                                                                |
| coroutines                   | 16.0 ms                                                                                                         | 16.1 ms: 1.00x slower                                                                                               |
| gc_traversal                 | 2.45 ms                                                                                                         | 2.46 ms: 1.00x slower                                                                                               |
| async_tree_cpu_io_mixed_tg   | 462 ms                                                                                                          | 464 ms: 1.00x slower                                                                                                |
| regex_dna                    | 145 ms                                                                                                          | 145 ms: 1.00x slower                                                                                                |
| pickle_list                  | 2.94 us                                                                                                         | 2.96 us: 1.01x slower                                                                                               |
| python_startup               | 17.0 ms                                                                                                         | 17.1 ms: 1.01x slower                                                                                               |
| regex_effbot                 | 2.44 ms                                                                                                         | 2.47 ms: 1.01x slower                                                                                               |
| regex_v8                     | 16.4 ms                                                                                                         | 16.6 ms: 1.01x slower                                                                                               |
| create_gc_cycles             | 895 us                                                                                                          | 904 us: 1.01x slower                                                                                                |
| unpickle                     | 9.24 us                                                                                                         | 9.37 us: 1.01x slower                                                                                               |
| async_tree_eager_tg          | 42.1 ms                                                                                                         | 42.7 ms: 1.01x slower                                                                                               |
| spectral_norm                | 67.0 ms                                                                                                         | 67.9 ms: 1.01x slower                                                                                               |
| python_startup_no_site       | 13.8 ms                                                                                                         | 14.1 ms: 1.02x slower                                                                                               |
| thrift                       | 420 us                                                                                                          | 428 us: 1.02x slower                                                                                                |
| typing_runtime_protocols     | 94.4 us                                                                                                         | 96.1 us: 1.02x slower                                                                                               |
| async_tree_cpu_io_mixed      | 460 ms                                                                                                          | 470 ms: 1.02x slower                                                                                                |
| logging_silent               | 60.7 ns                                                                                                         | 62.1 ns: 1.02x slower                                                                                               |
| coverage                     | 44.0 ms                                                                                                         | 45.0 ms: 1.02x slower                                                                                               |
| sqlite_synth                 | 1.55 us                                                                                                         | 1.58 us: 1.02x slower                                                                                               |
| mdp                          | 1.42 sec                                                                                                        | 1.46 sec: 1.03x slower                                                                                              |
| async_tree_eager_memoization | 153 ms                                                                                                          | 157 ms: 1.03x slower                                                                                                |
| async_tree_io                | 580 ms                                                                                                          | 597 ms: 1.03x slower                                                                                                |
| pyflate                      | 321 ms                                                                                                          | 331 ms: 1.03x slower                                                                                                |
| crypto_pyaes                 | 50.1 ms                                                                                                         | 52.1 ms: 1.04x slower                                                                                               |
| fannkuch                     | 260 ms                                                                                                          | 271 ms: 1.04x slower                                                                                                |
| meteor_contest               | 71.8 ms                                                                                                         | 75.0 ms: 1.04x slower                                                                                               |
| bench_mp_pool                | 49.7 ms                                                                                                         | 52.0 ms: 1.05x slower                                                                                               |
| scimark_fft                  | 183 ms                                                                                                          | 192 ms: 1.05x slower                                                                                                |
| async_tree_eager             | 61.1 ms                                                                                                         | 64.5 ms: 1.06x slower                                                                                               |
| bench_thread_pool            | 448 us                                                                                                          | 473 us: 1.06x slower                                                                                                |
| nbody                        | 60.0 ms                                                                                                         | 63.5 ms: 1.06x slower                                                                                               |
| async_generators             | 278 ms                                                                                                          | 295 ms: 1.06x slower                                                                                                |
| deepcopy                     | 145 us                                                                                                          | 154 us: 1.07x slower                                                                                                |
| dulwich_log                  | 27.2 ms                                                                                                         | 29.0 ms: 1.07x slower                                                                                               |
| pycparser                    | 637 ms                                                                                                          | 685 ms: 1.08x slower                                                                                                |
| sqlglot_normalize            | 169 ms                                                                                                          | 185 ms: 1.09x slower                                                                                                |
| pprint_safe_repr             | 460 ms                                                                                                          | 501 ms: 1.09x slower                                                                                                |
| html5lib                     | 30.1 ms                                                                                                         | 32.8 ms: 1.09x slower                                                                                               |
| nqueens                      | 53.3 ms                                                                                                         | 58.4 ms: 1.10x slower                                                                                               |
| sympy_str                    | 131 ms                                                                                                          | 145 ms: 1.10x slower                                                                                                |
| pprint_pformat               | 938 ms                                                                                                          | 1.03 sec: 1.10x slower                                                                                              |
| sympy_expand                 | 228 ms                                                                                                          | 252 ms: 1.10x slower                                                                                                |
| sympy_sum                    | 68.4 ms                                                                                                         | 76.3 ms: 1.11x slower                                                                                               |
| regex_compile                | 67.2 ms                                                                                                         | 74.9 ms: 1.11x slower                                                                                               |
| deltablue                    | 2.12 ms                                                                                                         | 2.36 ms: 1.11x slower                                                                                               |
| 2to3                         | 159 ms                                                                                                          | 178 ms: 1.12x slower                                                                                                |
| docutils                     | 1.40 sec                                                                                                        | 1.57 sec: 1.12x slower                                                                                              |
| scimark_sparse_mat_mult      | 2.77 ms                                                                                                         | 3.11 ms: 1.12x slower                                                                                               |
| chaos                        | 35.8 ms                                                                                                         | 40.8 ms: 1.14x slower                                                                                               |
| scimark_monte_carlo          | 43.1 ms                                                                                                         | 49.5 ms: 1.15x slower                                                                                               |
| sympy_integrate              | 10.2 ms                                                                                                         | 11.7 ms: 1.15x slower                                                                                               |
| sqlglot_optimize             | 31.4 ms                                                                                                         | 36.1 ms: 1.15x slower                                                                                               |
| pylint                       | 180 ms                                                                                                          | 208 ms: 1.15x slower                                                                                                |
| sqlglot_parse                | 743 us                                                                                                          | 858 us: 1.16x slower                                                                                                |
| sqlglot_transpile            | 905 us                                                                                                          | 1.05 ms: 1.16x slower                                                                                               |
| django_template              | 20.0 ms                                                                                                         | 23.2 ms: 1.16x slower                                                                                               |
| raytrace                     | 149 ms                                                                                                          | 174 ms: 1.17x slower                                                                                                |
| hexiom                       | 4.05 ms                                                                                                         | 4.76 ms: 1.17x slower                                                                                               |
| comprehensions               | 10.9 us                                                                                                         | 12.9 us: 1.18x slower                                                                                               |
| generators                   | 20.5 ms                                                                                                         | 24.4 ms: 1.19x slower                                                                                               |
| genshi_text                  | 13.9 ms                                                                                                         | 16.8 ms: 1.21x slower                                                                                               |
| go                           | 79.2 ms                                                                                                         | 102 ms: 1.29x slower                                                                                                |
| genshi_xml                   | 30.2 ms                                                                                                         | 41.6 ms: 1.38x slower                                                                                               |
| richards_super               | 34.2 ms                                                                                                         | 48.1 ms: 1.41x slower                                                                                               |
| richards                     | 31.1 ms                                                                                                         | 46.1 ms: 1.48x slower                                                                                               |
| unpack_sequence              | 26.4 ns                                                                                                         | 75.8 ns: 2.87x slower                                                                                               |
| Geometric mean               | (ref)                                                                                                           | 1.06x slower                                                                                                        |

Benchmark hidden because not significant (20): async_tree_io_tg, pickle, unpickle_list, async_tree_eager_cpu_io_mixed_tg, asyncio_websockets, telco, async_tree_none_tg, deepcopy_reduce, json_loads, pathlib, json, async_tree_eager_cpu_io_mixed, async_tree_memoization_tg, async_tree_eager_io, asyncio_tcp_ssl, async_tree_eager_memoization_tg, async_tree_eager_io_tg, async_tree_memoization, async_tree_none, tornado_http

- Geometric mean (including insignificant results): 1.049x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 1.00x