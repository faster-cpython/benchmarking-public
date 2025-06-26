# Results vs. base

- fork: faster-cpython
- ref: explicit_check_perio
- machine: darwin-arm64
- commit hash: 892a89d
- commit date: 2025-06-26
- overall geometric mean: 1.127x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250619-darwin-arm64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250626-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 186 ms                                                                | 163 ms: 1.14x faster                                                            |
| docutils       | 1.51 sec                                                              | 1.41 sec: 1.07x faster                                                          |
| html5lib       | 34.1 ms                                                               | 29.4 ms: 1.16x faster                                                           |
| sphinx         | 614 ms                                                                | 568 ms: 1.08x faster                                                            |
| Geometric mean | (ref)                                                                 | 1.11x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20250619-darwin-arm64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250626-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|----------------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_eager                 | 72.8 ms                                                               | 60.5 ms: 1.20x faster                                                           |
| coroutines                       | 18.8 ms                                                               | 16.0 ms: 1.17x faster                                                           |
| async_tree_none                  | 182 ms                                                                | 157 ms: 1.16x faster                                                            |
| async_tree_memoization           | 214 ms                                                                | 185 ms: 1.15x faster                                                            |
| async_tree_eager_tg              | 143 ms                                                                | 125 ms: 1.15x faster                                                            |
| async_tree_io                    | 413 ms                                                                | 365 ms: 1.13x faster                                                            |
| async_tree_none_tg               | 171 ms                                                                | 151 ms: 1.13x faster                                                            |
| async_tree_eager_io              | 393 ms                                                                | 347 ms: 1.13x faster                                                            |
| async_tree_eager_memoization_tg  | 182 ms                                                                | 163 ms: 1.12x faster                                                            |
| async_tree_eager_io_tg           | 402 ms                                                                | 362 ms: 1.11x faster                                                            |
| async_tree_io_tg                 | 405 ms                                                                | 364 ms: 1.11x faster                                                            |
| async_tree_memoization_tg        | 206 ms                                                                | 187 ms: 1.11x faster                                                            |
| async_tree_eager_memoization     | 151 ms                                                                | 137 ms: 1.10x faster                                                            |
| async_generators                 | 274 ms                                                                | 259 ms: 1.06x faster                                                            |
| async_tree_cpu_io_mixed          | 432 ms                                                                | 409 ms: 1.06x faster                                                            |
| async_tree_eager_cpu_io_mixed    | 368 ms                                                                | 354 ms: 1.04x faster                                                            |
| async_tree_cpu_io_mixed_tg       | 422 ms                                                                | 407 ms: 1.04x faster                                                            |
| async_tree_eager_cpu_io_mixed_tg | 399 ms                                                                | 386 ms: 1.04x faster                                                            |
| asyncio_websockets               | 242 ms                                                                | 242 ms: 1.00x faster                                                            |
| Geometric mean                   | (ref)                                                                 | 1.10x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250619-darwin-arm64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250626-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 85.2 ms                                                               | 68.6 ms: 1.24x faster                                                           |
| float          | 58.2 ms                                                               | 47.0 ms: 1.24x faster                                                           |
| pidigits       | 284 ms                                                                | 283 ms: 1.00x faster                                                            |
| Geometric mean | (ref)                                                                 | 1.16x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250619-darwin-arm64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250626-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 81.0 ms                                                               | 65.9 ms: 1.23x faster                                                           |
| regex_v8       | 16.1 ms                                                               | 16.0 ms: 1.01x faster                                                           |
| regex_effbot   | 2.36 ms                                                               | 2.34 ms: 1.01x faster                                                           |
| regex_dna      | 143 ms                                                                | 143 ms: 1.00x slower                                                            |
| Geometric mean | (ref)                                                                 | 1.06x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250619-darwin-arm64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250626-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| unpickle_pure_python | 177 us                                                                | 144 us: 1.23x faster                                                            |
| tomli_loads          | 1.45 sec                                                              | 1.19 sec: 1.23x faster                                                          |
| pickle_pure_python   | 243 us                                                                | 203 us: 1.19x faster                                                            |
| xml_etree_process    | 43.2 ms                                                               | 37.3 ms: 1.16x faster                                                           |
| xml_etree_generate   | 58.4 ms                                                               | 51.9 ms: 1.13x faster                                                           |
| json_dumps           | 6.79 ms                                                               | 6.39 ms: 1.06x faster                                                           |
| xml_etree_iterparse  | 73.9 ms                                                               | 70.7 ms: 1.05x faster                                                           |
| xml_etree_parse      | 105 ms                                                                | 103 ms: 1.02x faster                                                            |
| json_loads           | 16.5 us                                                               | 16.3 us: 1.01x faster                                                           |
| Geometric mean       | (ref)                                                                 | 1.12x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250619-darwin-arm64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250626-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 12.2 ms                                                               | 11.7 ms: 1.05x faster                                                           |
| python_startup         | 16.5 ms                                                               | 16.0 ms: 1.03x faster                                                           |
| Geometric mean         | (ref)                                                                 | 1.04x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250619-darwin-arm64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250626-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|-----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_text     | 17.7 ms                                                               | 13.4 ms: 1.32x faster                                                           |
| genshi_xml      | 36.2 ms                                                               | 28.6 ms: 1.27x faster                                                           |
| django_template | 25.1 ms                                                               | 20.9 ms: 1.20x faster                                                           |
| mako            | 9.03 ms                                                               | 7.64 ms: 1.18x faster                                                           |
| Geometric mean  | (ref)                                                                 | 1.24x faster                                                                    |

All benchmarks:
===============

| Benchmark                        | bm-20250619-darwin-arm64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250626-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|----------------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| generators                       | 31.8 ms                                                               | 23.2 ms: 1.37x faster                                                           |
| genshi_text                      | 17.7 ms                                                               | 13.4 ms: 1.32x faster                                                           |
| go                               | 99.2 ms                                                               | 77.1 ms: 1.29x faster                                                           |
| sqlglot_v2_parse                 | 986 us                                                                | 769 us: 1.28x faster                                                            |
| genshi_xml                       | 36.2 ms                                                               | 28.6 ms: 1.27x faster                                                           |
| chaos                            | 46.9 ms                                                               | 37.1 ms: 1.27x faster                                                           |
| fannkuch                         | 303 ms                                                                | 241 ms: 1.26x faster                                                            |
| sqlglot_v2_transpile             | 1.16 ms                                                               | 931 us: 1.25x faster                                                            |
| raytrace                         | 212 ms                                                                | 169 ms: 1.25x faster                                                            |
| scimark_monte_carlo              | 52.6 ms                                                               | 42.3 ms: 1.24x faster                                                           |
| nbody                            | 85.2 ms                                                               | 68.6 ms: 1.24x faster                                                           |
| float                            | 58.2 ms                                                               | 47.0 ms: 1.24x faster                                                           |
| unpickle_pure_python             | 177 us                                                                | 144 us: 1.23x faster                                                            |
| nqueens                          | 70.2 ms                                                               | 57.0 ms: 1.23x faster                                                           |
| regex_compile                    | 81.0 ms                                                               | 65.9 ms: 1.23x faster                                                           |
| tomli_loads                      | 1.45 sec                                                              | 1.19 sec: 1.23x faster                                                          |
| hexiom                           | 5.09 ms                                                               | 4.15 ms: 1.23x faster                                                           |
| deepcopy_memo                    | 21.8 us                                                               | 17.8 us: 1.23x faster                                                           |
| deltablue                        | 2.82 ms                                                               | 2.34 ms: 1.21x faster                                                           |
| comprehensions                   | 13.1 us                                                               | 10.9 us: 1.21x faster                                                           |
| async_tree_eager                 | 72.8 ms                                                               | 60.5 ms: 1.20x faster                                                           |
| typing_runtime_protocols         | 109 us                                                                | 90.9 us: 1.20x faster                                                           |
| django_template                  | 25.1 ms                                                               | 20.9 ms: 1.20x faster                                                           |
| pickle_pure_python               | 243 us                                                                | 203 us: 1.19x faster                                                            |
| pprint_pformat                   | 1.27 sec                                                              | 1.07 sec: 1.18x faster                                                          |
| mako                             | 9.03 ms                                                               | 7.64 ms: 1.18x faster                                                           |
| pprint_safe_repr                 | 623 ms                                                                | 528 ms: 1.18x faster                                                            |
| deepcopy                         | 175 us                                                                | 149 us: 1.18x faster                                                            |
| scimark_sor                      | 89.6 ms                                                               | 76.1 ms: 1.18x faster                                                           |
| sqlglot_v2_normalize             | 76.4 ms                                                               | 65.0 ms: 1.18x faster                                                           |
| deepcopy_reduce                  | 1.90 us                                                               | 1.62 us: 1.18x faster                                                           |
| coroutines                       | 18.8 ms                                                               | 16.0 ms: 1.17x faster                                                           |
| richards_super                   | 41.5 ms                                                               | 35.5 ms: 1.17x faster                                                           |
| logging_simple                   | 4.07 us                                                               | 3.47 us: 1.17x faster                                                           |
| pyflate                          | 332 ms                                                                | 284 ms: 1.17x faster                                                            |
| html5lib                         | 34.1 ms                                                               | 29.4 ms: 1.16x faster                                                           |
| async_tree_none                  | 182 ms                                                                | 157 ms: 1.16x faster                                                            |
| xml_etree_process                | 43.2 ms                                                               | 37.3 ms: 1.16x faster                                                           |
| async_tree_memoization           | 214 ms                                                                | 185 ms: 1.15x faster                                                            |
| richards                         | 37.1 ms                                                               | 32.3 ms: 1.15x faster                                                           |
| logging_format                   | 4.35 us                                                               | 3.78 us: 1.15x faster                                                           |
| async_tree_eager_tg              | 143 ms                                                                | 125 ms: 1.15x faster                                                            |
| 2to3                             | 186 ms                                                                | 163 ms: 1.14x faster                                                            |
| sqlglot_v2_optimize              | 36.5 ms                                                               | 31.9 ms: 1.14x faster                                                           |
| pycparser                        | 741 ms                                                                | 648 ms: 1.14x faster                                                            |
| scimark_lu                       | 84.5 ms                                                               | 74.4 ms: 1.14x faster                                                           |
| mdp                              | 823 ms                                                                | 725 ms: 1.14x faster                                                            |
| async_tree_io                    | 413 ms                                                                | 365 ms: 1.13x faster                                                            |
| async_tree_none_tg               | 171 ms                                                                | 151 ms: 1.13x faster                                                            |
| sympy_expand                     | 262 ms                                                                | 231 ms: 1.13x faster                                                            |
| sympy_str                        | 154 ms                                                                | 137 ms: 1.13x faster                                                            |
| subparsers                       | 14.8 ms                                                               | 13.1 ms: 1.13x faster                                                           |
| async_tree_eager_io              | 393 ms                                                                | 347 ms: 1.13x faster                                                            |
| xml_etree_generate               | 58.4 ms                                                               | 51.9 ms: 1.13x faster                                                           |
| scimark_fft                      | 202 ms                                                                | 179 ms: 1.13x faster                                                            |
| crypto_pyaes                     | 60.9 ms                                                               | 54.2 ms: 1.12x faster                                                           |
| spectral_norm                    | 72.3 ms                                                               | 64.7 ms: 1.12x faster                                                           |
| async_tree_eager_memoization_tg  | 182 ms                                                                | 163 ms: 1.12x faster                                                            |
| sympy_sum                        | 81.3 ms                                                               | 72.9 ms: 1.12x faster                                                           |
| async_tree_eager_io_tg           | 402 ms                                                                | 362 ms: 1.11x faster                                                            |
| async_tree_io_tg                 | 405 ms                                                                | 364 ms: 1.11x faster                                                            |
| async_tree_memoization_tg        | 206 ms                                                                | 187 ms: 1.11x faster                                                            |
| bpe_tokeniser                    | 3.24 sec                                                              | 2.93 sec: 1.11x faster                                                          |
| async_tree_eager_memoization     | 151 ms                                                                | 137 ms: 1.10x faster                                                            |
| many_optionals                   | 495 us                                                                | 452 us: 1.09x faster                                                            |
| dulwich_log                      | 26.4 ms                                                               | 24.1 ms: 1.09x faster                                                           |
| telco                            | 4.79 ms                                                               | 4.42 ms: 1.08x faster                                                           |
| sympy_integrate                  | 11.3 ms                                                               | 10.5 ms: 1.08x faster                                                           |
| sphinx                           | 614 ms                                                                | 568 ms: 1.08x faster                                                            |
| thrift                           | 469 us                                                                | 435 us: 1.08x faster                                                            |
| meteor_contest                   | 74.6 ms                                                               | 69.7 ms: 1.07x faster                                                           |
| docutils                         | 1.51 sec                                                              | 1.41 sec: 1.07x faster                                                          |
| pylint                           | 168 ms                                                                | 157 ms: 1.07x faster                                                            |
| logging_silent                   | 342 ns                                                                | 321 ns: 1.06x faster                                                            |
| json_dumps                       | 6.79 ms                                                               | 6.39 ms: 1.06x faster                                                           |
| async_generators                 | 274 ms                                                                | 259 ms: 1.06x faster                                                            |
| async_tree_cpu_io_mixed          | 432 ms                                                                | 409 ms: 1.06x faster                                                            |
| python_startup_no_site           | 12.2 ms                                                               | 11.7 ms: 1.05x faster                                                           |
| xml_etree_iterparse              | 73.9 ms                                                               | 70.7 ms: 1.05x faster                                                           |
| scimark_sparse_mat_mult          | 3.23 ms                                                               | 3.09 ms: 1.05x faster                                                           |
| coverage                         | 49.4 ms                                                               | 47.5 ms: 1.04x faster                                                           |
| async_tree_eager_cpu_io_mixed    | 368 ms                                                                | 354 ms: 1.04x faster                                                            |
| async_tree_cpu_io_mixed_tg       | 422 ms                                                                | 407 ms: 1.04x faster                                                            |
| async_tree_eager_cpu_io_mixed_tg | 399 ms                                                                | 386 ms: 1.04x faster                                                            |
| connected_components             | 304 ms                                                                | 295 ms: 1.03x faster                                                            |
| json                             | 2.94 ms                                                               | 2.87 ms: 1.03x faster                                                           |
| python_startup                   | 16.5 ms                                                               | 16.0 ms: 1.03x faster                                                           |
| shortest_path                    | 328 ms                                                                | 320 ms: 1.02x faster                                                            |
| sqlite_synth                     | 1.63 us                                                               | 1.59 us: 1.02x faster                                                           |
| xml_etree_parse                  | 105 ms                                                                | 103 ms: 1.02x faster                                                            |
| k_core                           | 1.47 sec                                                              | 1.44 sec: 1.02x faster                                                          |
| pathlib                          | 22.6 ms                                                               | 22.3 ms: 1.01x faster                                                           |
| regex_v8                         | 16.1 ms                                                               | 16.0 ms: 1.01x faster                                                           |
| regex_effbot                     | 2.36 ms                                                               | 2.34 ms: 1.01x faster                                                           |
| json_loads                       | 16.5 us                                                               | 16.3 us: 1.01x faster                                                           |
| dask                             | 769 ms                                                                | 765 ms: 1.00x faster                                                            |
| pidigits                         | 284 ms                                                                | 283 ms: 1.00x faster                                                            |
| gc_traversal                     | 3.19 ms                                                               | 3.18 ms: 1.00x faster                                                           |
| asyncio_websockets               | 242 ms                                                                | 242 ms: 1.00x faster                                                            |
| regex_dna                        | 143 ms                                                                | 143 ms: 1.00x slower                                                            |
| Geometric mean                   | (ref)                                                                 | 1.13x faster                                                                    |

Benchmark hidden because not significant (1): create_gc_cycles

- Geometric mean (including insignificant results): 1.127x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.11x
- 95% likely to have a speedup of 1.10x
- 99% likely to have a speedup of 1.10x

# Memory
- memory change: 1.01x