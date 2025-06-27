# Results vs. base

- fork: faster-cpython
- ref: explicit_check_perio
- machine: darwin-arm64
- commit hash: 892a89d
- commit date: 2025-06-26
- overall geometric mean: 1.093x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250619-darwin-arm64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250626-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 185 ms                                                                | 168 ms: 1.10x faster                                                            |
| docutils       | 1.52 sec                                                              | 1.45 sec: 1.05x faster                                                          |
| html5lib       | 34.1 ms                                                               | 29.4 ms: 1.16x faster                                                           |
| sphinx         | 616 ms                                                                | 574 ms: 1.07x faster                                                            |
| Geometric mean | (ref)                                                                 | 1.10x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20250619-darwin-arm64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250626-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|----------------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_eager                 | 71.7 ms                                                               | 61.3 ms: 1.17x faster                                                           |
| coroutines                       | 18.8 ms                                                               | 16.1 ms: 1.17x faster                                                           |
| async_tree_none                  | 177 ms                                                                | 156 ms: 1.13x faster                                                            |
| async_tree_eager_tg              | 140 ms                                                                | 125 ms: 1.12x faster                                                            |
| async_tree_memoization           | 207 ms                                                                | 186 ms: 1.12x faster                                                            |
| async_tree_eager_io              | 387 ms                                                                | 348 ms: 1.11x faster                                                            |
| async_tree_io                    | 406 ms                                                                | 368 ms: 1.10x faster                                                            |
| async_tree_none_tg               | 166 ms                                                                | 151 ms: 1.10x faster                                                            |
| async_tree_io_tg                 | 397 ms                                                                | 360 ms: 1.10x faster                                                            |
| async_tree_eager_io_tg           | 398 ms                                                                | 361 ms: 1.10x faster                                                            |
| async_tree_eager_memoization_tg  | 179 ms                                                                | 163 ms: 1.10x faster                                                            |
| async_tree_eager_memoization     | 150 ms                                                                | 138 ms: 1.09x faster                                                            |
| async_tree_memoization_tg        | 203 ms                                                                | 187 ms: 1.09x faster                                                            |
| async_tree_cpu_io_mixed          | 427 ms                                                                | 410 ms: 1.04x faster                                                            |
| async_generators                 | 287 ms                                                                | 276 ms: 1.04x faster                                                            |
| async_tree_cpu_io_mixed_tg       | 421 ms                                                                | 407 ms: 1.04x faster                                                            |
| async_tree_eager_cpu_io_mixed    | 368 ms                                                                | 356 ms: 1.03x faster                                                            |
| async_tree_eager_cpu_io_mixed_tg | 400 ms                                                                | 387 ms: 1.03x faster                                                            |
| asyncio_websockets               | 242 ms                                                                | 242 ms: 1.00x faster                                                            |
| Geometric mean                   | (ref)                                                                 | 1.09x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250619-darwin-arm64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250626-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 58.0 ms                                                               | 46.8 ms: 1.24x faster                                                           |
| nbody          | 74.9 ms                                                               | 74.3 ms: 1.01x faster                                                           |
| Geometric mean | (ref)                                                                 | 1.08x faster                                                                    |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250619-darwin-arm64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250626-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 79.3 ms                                                               | 66.6 ms: 1.19x faster                                                           |
| regex_v8       | 16.3 ms                                                               | 16.1 ms: 1.02x faster                                                           |
| regex_effbot   | 2.37 ms                                                               | 2.34 ms: 1.02x faster                                                           |
| Geometric mean | (ref)                                                                 | 1.05x faster                                                                    |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250619-darwin-arm64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250626-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pickle_pure_python   | 227 us                                                                | 200 us: 1.14x faster                                                            |
| tomli_loads          | 1.32 sec                                                              | 1.17 sec: 1.13x faster                                                          |
| xml_etree_process    | 37.5 ms                                                               | 35.0 ms: 1.07x faster                                                           |
| json_dumps           | 6.88 ms                                                               | 6.46 ms: 1.07x faster                                                           |
| unpickle_pure_python | 138 us                                                                | 133 us: 1.04x faster                                                            |
| xml_etree_iterparse  | 73.4 ms                                                               | 70.8 ms: 1.04x faster                                                           |
| xml_etree_generate   | 51.7 ms                                                               | 50.2 ms: 1.03x faster                                                           |
| json_loads           | 16.5 us                                                               | 16.4 us: 1.01x faster                                                           |
| Geometric mean       | (ref)                                                                 | 1.06x faster                                                                    |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250619-darwin-arm64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250626-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 18.0 ms                                                               | 17.9 ms: 1.01x faster                                                           |
| python_startup_no_site | 13.5 ms                                                               | 13.4 ms: 1.01x faster                                                           |
| Geometric mean         | (ref)                                                                 | 1.01x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250619-darwin-arm64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250626-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|-----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_text     | 17.7 ms                                                               | 13.5 ms: 1.31x faster                                                           |
| genshi_xml      | 36.1 ms                                                               | 29.0 ms: 1.25x faster                                                           |
| django_template | 25.2 ms                                                               | 21.0 ms: 1.20x faster                                                           |
| mako            | 6.94 ms                                                               | 6.82 ms: 1.02x faster                                                           |
| Geometric mean  | (ref)                                                                 | 1.19x faster                                                                    |

All benchmarks:
===============

| Benchmark                        | bm-20250619-darwin-arm64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250626-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|----------------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| generators                       | 31.6 ms                                                               | 23.1 ms: 1.37x faster                                                           |
| go                               | 102 ms                                                                | 77.9 ms: 1.31x faster                                                           |
| genshi_text                      | 17.7 ms                                                               | 13.5 ms: 1.31x faster                                                           |
| chaos                            | 46.7 ms                                                               | 37.0 ms: 1.26x faster                                                           |
| scimark_monte_carlo              | 52.8 ms                                                               | 42.3 ms: 1.25x faster                                                           |
| genshi_xml                       | 36.1 ms                                                               | 29.0 ms: 1.25x faster                                                           |
| float                            | 58.0 ms                                                               | 46.8 ms: 1.24x faster                                                           |
| raytrace                         | 210 ms                                                                | 170 ms: 1.24x faster                                                            |
| deepcopy_memo                    | 22.4 us                                                               | 18.3 us: 1.22x faster                                                           |
| django_template                  | 25.2 ms                                                               | 21.0 ms: 1.20x faster                                                           |
| regex_compile                    | 79.3 ms                                                               | 66.6 ms: 1.19x faster                                                           |
| nqueens                          | 69.8 ms                                                               | 58.9 ms: 1.19x faster                                                           |
| logging_simple                   | 4.08 us                                                               | 3.47 us: 1.18x faster                                                           |
| async_tree_eager                 | 71.7 ms                                                               | 61.3 ms: 1.17x faster                                                           |
| deepcopy                         | 174 us                                                                | 149 us: 1.17x faster                                                            |
| deepcopy_reduce                  | 1.90 us                                                               | 1.62 us: 1.17x faster                                                           |
| scimark_sor                      | 89.2 ms                                                               | 76.3 ms: 1.17x faster                                                           |
| coroutines                       | 18.8 ms                                                               | 16.1 ms: 1.17x faster                                                           |
| deltablue                        | 2.89 ms                                                               | 2.49 ms: 1.16x faster                                                           |
| html5lib                         | 34.1 ms                                                               | 29.4 ms: 1.16x faster                                                           |
| sqlglot_v2_normalize             | 75.9 ms                                                               | 65.6 ms: 1.16x faster                                                           |
| logging_format                   | 4.37 us                                                               | 3.79 us: 1.15x faster                                                           |
| richards                         | 37.4 ms                                                               | 32.5 ms: 1.15x faster                                                           |
| scimark_lu                       | 84.5 ms                                                               | 74.0 ms: 1.14x faster                                                           |
| pickle_pure_python               | 227 us                                                                | 200 us: 1.14x faster                                                            |
| async_tree_none                  | 177 ms                                                                | 156 ms: 1.13x faster                                                            |
| subparsers                       | 14.9 ms                                                               | 13.1 ms: 1.13x faster                                                           |
| richards_super                   | 41.8 ms                                                               | 37.0 ms: 1.13x faster                                                           |
| sqlglot_v2_parse                 | 879 us                                                                | 777 us: 1.13x faster                                                            |
| pyflate                          | 313 ms                                                                | 277 ms: 1.13x faster                                                            |
| tomli_loads                      | 1.32 sec                                                              | 1.17 sec: 1.13x faster                                                          |
| sqlglot_v2_transpile             | 1.07 ms                                                               | 947 us: 1.13x faster                                                            |
| mdp                              | 824 ms                                                                | 732 ms: 1.13x faster                                                            |
| async_tree_eager_tg              | 140 ms                                                                | 125 ms: 1.12x faster                                                            |
| comprehensions                   | 13.0 us                                                               | 11.6 us: 1.12x faster                                                           |
| sqlglot_v2_optimize              | 36.6 ms                                                               | 32.7 ms: 1.12x faster                                                           |
| sympy_expand                     | 265 ms                                                                | 236 ms: 1.12x faster                                                            |
| sympy_str                        | 155 ms                                                                | 139 ms: 1.12x faster                                                            |
| async_tree_memoization           | 207 ms                                                                | 186 ms: 1.12x faster                                                            |
| spectral_norm                    | 72.1 ms                                                               | 64.7 ms: 1.11x faster                                                           |
| hexiom                           | 4.99 ms                                                               | 4.49 ms: 1.11x faster                                                           |
| async_tree_eager_io              | 387 ms                                                                | 348 ms: 1.11x faster                                                            |
| sympy_sum                        | 81.1 ms                                                               | 73.3 ms: 1.11x faster                                                           |
| dulwich_log                      | 26.8 ms                                                               | 24.2 ms: 1.10x faster                                                           |
| 2to3                             | 185 ms                                                                | 168 ms: 1.10x faster                                                            |
| async_tree_io                    | 406 ms                                                                | 368 ms: 1.10x faster                                                            |
| async_tree_none_tg               | 166 ms                                                                | 151 ms: 1.10x faster                                                            |
| async_tree_io_tg                 | 397 ms                                                                | 360 ms: 1.10x faster                                                            |
| async_tree_eager_io_tg           | 398 ms                                                                | 361 ms: 1.10x faster                                                            |
| pathlib                          | 24.1 ms                                                               | 21.9 ms: 1.10x faster                                                           |
| async_tree_eager_memoization_tg  | 179 ms                                                                | 163 ms: 1.10x faster                                                            |
| typing_runtime_protocols         | 104 us                                                                | 95.2 us: 1.10x faster                                                           |
| async_tree_eager_memoization     | 150 ms                                                                | 138 ms: 1.09x faster                                                            |
| pycparser                        | 747 ms                                                                | 686 ms: 1.09x faster                                                            |
| many_optionals                   | 507 us                                                                | 466 us: 1.09x faster                                                            |
| async_tree_memoization_tg        | 203 ms                                                                | 187 ms: 1.09x faster                                                            |
| thrift                           | 470 us                                                                | 434 us: 1.08x faster                                                            |
| sphinx                           | 616 ms                                                                | 574 ms: 1.07x faster                                                            |
| xml_etree_process                | 37.5 ms                                                               | 35.0 ms: 1.07x faster                                                           |
| sympy_integrate                  | 11.4 ms                                                               | 10.7 ms: 1.07x faster                                                           |
| json_dumps                       | 6.88 ms                                                               | 6.46 ms: 1.07x faster                                                           |
| pylint                           | 169 ms                                                                | 159 ms: 1.06x faster                                                            |
| pprint_pformat                   | 1.20 sec                                                              | 1.14 sec: 1.05x faster                                                          |
| logging_silent                   | 342 ns                                                                | 325 ns: 1.05x faster                                                            |
| coverage                         | 49.3 ms                                                               | 47.0 ms: 1.05x faster                                                           |
| pprint_safe_repr                 | 595 ms                                                                | 568 ms: 1.05x faster                                                            |
| docutils                         | 1.52 sec                                                              | 1.45 sec: 1.05x faster                                                          |
| async_tree_cpu_io_mixed          | 427 ms                                                                | 410 ms: 1.04x faster                                                            |
| async_generators                 | 287 ms                                                                | 276 ms: 1.04x faster                                                            |
| crypto_pyaes                     | 57.2 ms                                                               | 55.0 ms: 1.04x faster                                                           |
| unpickle_pure_python             | 138 us                                                                | 133 us: 1.04x faster                                                            |
| fannkuch                         | 300 ms                                                                | 290 ms: 1.04x faster                                                            |
| xml_etree_iterparse              | 73.4 ms                                                               | 70.8 ms: 1.04x faster                                                           |
| async_tree_cpu_io_mixed_tg       | 421 ms                                                                | 407 ms: 1.04x faster                                                            |
| async_tree_eager_cpu_io_mixed    | 368 ms                                                                | 356 ms: 1.03x faster                                                            |
| async_tree_eager_cpu_io_mixed_tg | 400 ms                                                                | 387 ms: 1.03x faster                                                            |
| xml_etree_generate               | 51.7 ms                                                               | 50.2 ms: 1.03x faster                                                           |
| json                             | 2.96 ms                                                               | 2.88 ms: 1.03x faster                                                           |
| bpe_tokeniser                    | 3.10 sec                                                              | 3.04 sec: 1.02x faster                                                          |
| mako                             | 6.94 ms                                                               | 6.82 ms: 1.02x faster                                                           |
| meteor_contest                   | 76.9 ms                                                               | 75.7 ms: 1.02x faster                                                           |
| regex_v8                         | 16.3 ms                                                               | 16.1 ms: 1.02x faster                                                           |
| regex_effbot                     | 2.37 ms                                                               | 2.34 ms: 1.02x faster                                                           |
| shortest_path                    | 340 ms                                                                | 335 ms: 1.02x faster                                                            |
| python_startup                   | 18.0 ms                                                               | 17.9 ms: 1.01x faster                                                           |
| json_loads                       | 16.5 us                                                               | 16.4 us: 1.01x faster                                                           |
| nbody                            | 74.9 ms                                                               | 74.3 ms: 1.01x faster                                                           |
| scimark_sparse_mat_mult          | 3.57 ms                                                               | 3.55 ms: 1.01x faster                                                           |
| sqlite_synth                     | 1.58 us                                                               | 1.57 us: 1.01x faster                                                           |
| python_startup_no_site           | 13.5 ms                                                               | 13.4 ms: 1.01x faster                                                           |
| connected_components             | 310 ms                                                                | 309 ms: 1.01x faster                                                            |
| dask                             | 771 ms                                                                | 768 ms: 1.00x faster                                                            |
| asyncio_websockets               | 242 ms                                                                | 242 ms: 1.00x faster                                                            |
| scimark_fft                      | 200 ms                                                                | 201 ms: 1.01x slower                                                            |
| create_gc_cycles                 | 1.36 ms                                                               | 1.37 ms: 1.01x slower                                                           |
| telco                            | 4.57 ms                                                               | 4.62 ms: 1.01x slower                                                           |
| gc_traversal                     | 3.19 ms                                                               | 3.35 ms: 1.05x slower                                                           |
| Geometric mean                   | (ref)                                                                 | 1.09x faster                                                                    |

Benchmark hidden because not significant (4): k_core, xml_etree_parse, pidigits, regex_dna

- Geometric mean (including insignificant results): 1.093x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: 1.01x