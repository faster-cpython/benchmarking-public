# Results vs. base

- fork: Fidget-Spinner
- ref: disable_tailcall
- machine: darwin-arm64
- commit hash: da5ad58
- commit date: 2025-02-25
- overall geometric mean: 1.106x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250222-darwin-arm64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 | bm-20250225-darwin-arm64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 152 ms                                                                 | 196 ms: 1.29x slower                                                         |
| docutils       | 1.35 sec                                                               | 1.44 sec: 1.07x slower                                                       |
| html5lib       | 28.8 ms                                                                | 32.5 ms: 1.13x slower                                                        |
| sphinx         | 539 ms                                                                 | 581 ms: 1.08x slower                                                         |
| Geometric mean | (ref)                                                                  | 1.14x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20250222-darwin-arm64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 | bm-20250225-darwin-arm64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|----------------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| asyncio_websockets               | 242 ms                                                                 | 243 ms: 1.00x slower                                                         |
| async_tree_eager_cpu_io_mixed_tg | 380 ms                                                                 | 392 ms: 1.03x slower                                                         |
| async_tree_cpu_io_mixed_tg       | 400 ms                                                                 | 414 ms: 1.04x slower                                                         |
| async_tree_cpu_io_mixed          | 401 ms                                                                 | 416 ms: 1.04x slower                                                         |
| async_tree_eager_cpu_io_mixed    | 344 ms                                                                 | 359 ms: 1.04x slower                                                         |
| async_tree_memoization_tg        | 183 ms                                                                 | 200 ms: 1.09x slower                                                         |
| async_tree_eager_io_tg           | 349 ms                                                                 | 382 ms: 1.09x slower                                                         |
| async_tree_io_tg                 | 339 ms                                                                 | 372 ms: 1.10x slower                                                         |
| async_tree_eager_memoization_tg  | 165 ms                                                                 | 181 ms: 1.10x slower                                                         |
| async_tree_eager_memoization     | 133 ms                                                                 | 146 ms: 1.10x slower                                                         |
| async_tree_eager_io              | 335 ms                                                                 | 370 ms: 1.10x slower                                                         |
| async_tree_eager_tg              | 122 ms                                                                 | 135 ms: 1.11x slower                                                         |
| async_generators                 | 237 ms                                                                 | 265 ms: 1.12x slower                                                         |
| async_tree_none                  | 150 ms                                                                 | 168 ms: 1.12x slower                                                         |
| async_tree_none_tg               | 143 ms                                                                 | 160 ms: 1.13x slower                                                         |
| async_tree_memoization           | 181 ms                                                                 | 208 ms: 1.15x slower                                                         |
| async_tree_io                    | 337 ms                                                                 | 391 ms: 1.16x slower                                                         |
| async_tree_eager                 | 56.8 ms                                                                | 67.1 ms: 1.18x slower                                                        |
| coroutines                       | 15.1 ms                                                                | 19.0 ms: 1.26x slower                                                        |
| Geometric mean                   | (ref)                                                                  | 1.10x slower                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250222-darwin-arm64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 | bm-20250225-darwin-arm64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pidigits       | 280 ms                                                                 | 281 ms: 1.00x slower                                                         |
| float          | 43.9 ms                                                                | 48.9 ms: 1.11x slower                                                        |
| nbody          | 63.9 ms                                                                | 81.0 ms: 1.27x slower                                                        |
| Geometric mean | (ref)                                                                  | 1.12x slower                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250222-darwin-arm64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 | bm-20250225-darwin-arm64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 2.34 ms                                                                | 2.34 ms: 1.00x slower                                                        |
| regex_v8       | 17.7 ms                                                                | 17.9 ms: 1.01x slower                                                        |
| regex_compile  | 61.9 ms                                                                | 76.2 ms: 1.23x slower                                                        |
| Geometric mean | (ref)                                                                  | 1.06x slower                                                                 |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250222-darwin-arm64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 | bm-20250225-darwin-arm64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|----------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| json_loads           | 17.9 us                                                                | 18.0 us: 1.00x slower                                                        |
| xml_etree_parse      | 101 ms                                                                 | 103 ms: 1.02x slower                                                         |
| json_dumps           | 7.09 ms                                                                | 7.37 ms: 1.04x slower                                                        |
| xml_etree_iterparse  | 68.6 ms                                                                | 72.5 ms: 1.06x slower                                                        |
| xml_etree_generate   | 48.4 ms                                                                | 56.5 ms: 1.17x slower                                                        |
| pickle_pure_python   | 184 us                                                                 | 220 us: 1.19x slower                                                         |
| xml_etree_process    | 33.6 ms                                                                | 40.9 ms: 1.22x slower                                                        |
| unpickle_pure_python | 124 us                                                                 | 161 us: 1.30x slower                                                         |
| tomli_loads          | 1.15 sec                                                               | 1.57 sec: 1.37x slower                                                       |
| Geometric mean       | (ref)                                                                  | 1.15x slower                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250222-darwin-arm64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 | bm-20250225-darwin-arm64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 13.9 ms                                                                | 14.1 ms: 1.01x slower                                                        |
| Geometric mean         | (ref)                                                                  | 1.01x slower                                                                 |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250222-darwin-arm64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 | bm-20250225-darwin-arm64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|-----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 7.08 ms                                                                | 7.91 ms: 1.12x slower                                                        |
| genshi_text     | 12.7 ms                                                                | 15.2 ms: 1.20x slower                                                        |
| genshi_xml      | 26.9 ms                                                                | 32.6 ms: 1.21x slower                                                        |
| django_template | 18.7 ms                                                                | 23.0 ms: 1.23x slower                                                        |
| Geometric mean  | (ref)                                                                  | 1.19x slower                                                                 |

All benchmarks:
===============

| Benchmark                        | bm-20250222-darwin-arm64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 | bm-20250225-darwin-arm64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|----------------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| spectral_norm                    | 67.7 ms                                                                | 65.1 ms: 1.04x faster                                                        |
| regex_effbot                     | 2.34 ms                                                                | 2.34 ms: 1.00x slower                                                        |
| pidigits                         | 280 ms                                                                 | 281 ms: 1.00x slower                                                         |
| asyncio_websockets               | 242 ms                                                                 | 243 ms: 1.00x slower                                                         |
| json_loads                       | 17.9 us                                                                | 18.0 us: 1.00x slower                                                        |
| regex_v8                         | 17.7 ms                                                                | 17.9 ms: 1.01x slower                                                        |
| python_startup_no_site           | 13.9 ms                                                                | 14.1 ms: 1.01x slower                                                        |
| coverage                         | 44.3 ms                                                                | 44.7 ms: 1.01x slower                                                        |
| json                             | 3.01 ms                                                                | 3.05 ms: 1.01x slower                                                        |
| bench_mp_pool                    | 59.6 ms                                                                | 60.5 ms: 1.02x slower                                                        |
| shortest_path                    | 319 ms                                                                 | 326 ms: 1.02x slower                                                         |
| xml_etree_parse                  | 101 ms                                                                 | 103 ms: 1.02x slower                                                         |
| k_core                           | 1.47 sec                                                               | 1.51 sec: 1.02x slower                                                       |
| sqlite_synth                     | 1.50 us                                                                | 1.55 us: 1.03x slower                                                        |
| async_tree_eager_cpu_io_mixed_tg | 380 ms                                                                 | 392 ms: 1.03x slower                                                         |
| async_tree_cpu_io_mixed_tg       | 400 ms                                                                 | 414 ms: 1.04x slower                                                         |
| async_tree_cpu_io_mixed          | 401 ms                                                                 | 416 ms: 1.04x slower                                                         |
| mdp                              | 1.43 sec                                                               | 1.48 sec: 1.04x slower                                                       |
| json_dumps                       | 7.09 ms                                                                | 7.37 ms: 1.04x slower                                                        |
| pathlib                          | 22.5 ms                                                                | 23.4 ms: 1.04x slower                                                        |
| async_tree_eager_cpu_io_mixed    | 344 ms                                                                 | 359 ms: 1.04x slower                                                         |
| telco                            | 4.44 ms                                                                | 4.64 ms: 1.04x slower                                                        |
| xml_etree_iterparse              | 68.6 ms                                                                | 72.5 ms: 1.06x slower                                                        |
| dulwich_log                      | 26.6 ms                                                                | 28.2 ms: 1.06x slower                                                        |
| raytrace                         | 162 ms                                                                 | 173 ms: 1.06x slower                                                         |
| crypto_pyaes                     | 49.3 ms                                                                | 52.5 ms: 1.07x slower                                                        |
| docutils                         | 1.35 sec                                                               | 1.44 sec: 1.07x slower                                                       |
| pyflate                          | 295 ms                                                                 | 316 ms: 1.07x slower                                                         |
| sphinx                           | 539 ms                                                                 | 581 ms: 1.08x slower                                                         |
| scimark_fft                      | 176 ms                                                                 | 190 ms: 1.08x slower                                                         |
| pylint                           | 148 ms                                                                 | 160 ms: 1.08x slower                                                         |
| async_tree_memoization_tg        | 183 ms                                                                 | 200 ms: 1.09x slower                                                         |
| async_tree_eager_io_tg           | 349 ms                                                                 | 382 ms: 1.09x slower                                                         |
| sympy_integrate                  | 10.1 ms                                                                | 11.1 ms: 1.09x slower                                                        |
| thrift                           | 410 us                                                                 | 448 us: 1.09x slower                                                         |
| async_tree_io_tg                 | 339 ms                                                                 | 372 ms: 1.10x slower                                                         |
| async_tree_eager_memoization_tg  | 165 ms                                                                 | 181 ms: 1.10x slower                                                         |
| bench_thread_pool                | 454 us                                                                 | 501 us: 1.10x slower                                                         |
| async_tree_eager_memoization     | 133 ms                                                                 | 146 ms: 1.10x slower                                                         |
| async_tree_eager_io              | 335 ms                                                                 | 370 ms: 1.10x slower                                                         |
| sympy_sum                        | 68.9 ms                                                                | 76.2 ms: 1.11x slower                                                        |
| bpe_tokeniser                    | 2.84 sec                                                               | 3.14 sec: 1.11x slower                                                       |
| async_tree_eager_tg              | 122 ms                                                                 | 135 ms: 1.11x slower                                                         |
| scimark_lu                       | 69.9 ms                                                                | 77.4 ms: 1.11x slower                                                        |
| scimark_sparse_mat_mult          | 2.73 ms                                                                | 3.03 ms: 1.11x slower                                                        |
| sqlalchemy_declarative           | 54.4 ms                                                                | 60.5 ms: 1.11x slower                                                        |
| subparsers                       | 11.4 ms                                                                | 12.7 ms: 1.11x slower                                                        |
| float                            | 43.9 ms                                                                | 48.9 ms: 1.11x slower                                                        |
| mako                             | 7.08 ms                                                                | 7.91 ms: 1.12x slower                                                        |
| pycparser                        | 619 ms                                                                 | 693 ms: 1.12x slower                                                         |
| async_generators                 | 237 ms                                                                 | 265 ms: 1.12x slower                                                         |
| many_optionals                   | 414 us                                                                 | 466 us: 1.12x slower                                                         |
| async_tree_none                  | 150 ms                                                                 | 168 ms: 1.12x slower                                                         |
| async_tree_none_tg               | 143 ms                                                                 | 160 ms: 1.13x slower                                                         |
| html5lib                         | 28.8 ms                                                                | 32.5 ms: 1.13x slower                                                        |
| meteor_contest                   | 70.3 ms                                                                | 79.3 ms: 1.13x slower                                                        |
| sympy_str                        | 128 ms                                                                 | 144 ms: 1.13x slower                                                         |
| sympy_expand                     | 214 ms                                                                 | 243 ms: 1.13x slower                                                         |
| richards_super                   | 31.1 ms                                                                | 35.5 ms: 1.14x slower                                                        |
| sqlglot_normalize                | 163 ms                                                                 | 187 ms: 1.15x slower                                                         |
| sqlglot_optimize                 | 29.8 ms                                                                | 34.2 ms: 1.15x slower                                                        |
| async_tree_memoization           | 181 ms                                                                 | 208 ms: 1.15x slower                                                         |
| logging_format                   | 3.25 us                                                                | 3.74 us: 1.15x slower                                                        |
| deltablue                        | 2.03 ms                                                                | 2.34 ms: 1.15x slower                                                        |
| richards                         | 27.6 ms                                                                | 32.0 ms: 1.16x slower                                                        |
| chaos                            | 35.0 ms                                                                | 40.6 ms: 1.16x slower                                                        |
| async_tree_io                    | 337 ms                                                                 | 391 ms: 1.16x slower                                                         |
| logging_simple                   | 2.95 us                                                                | 3.44 us: 1.16x slower                                                        |
| typing_runtime_protocols         | 84.0 us                                                                | 97.8 us: 1.16x slower                                                        |
| xml_etree_generate               | 48.4 ms                                                                | 56.5 ms: 1.17x slower                                                        |
| nqueens                          | 50.7 ms                                                                | 59.7 ms: 1.18x slower                                                        |
| scimark_sor                      | 74.4 ms                                                                | 88.0 ms: 1.18x slower                                                        |
| async_tree_eager                 | 56.8 ms                                                                | 67.1 ms: 1.18x slower                                                        |
| sqlglot_transpile                | 844 us                                                                 | 1.00 ms: 1.19x slower                                                        |
| sqlglot_parse                    | 698 us                                                                 | 829 us: 1.19x slower                                                         |
| scimark_monte_carlo              | 39.9 ms                                                                | 47.4 ms: 1.19x slower                                                        |
| pickle_pure_python               | 184 us                                                                 | 220 us: 1.19x slower                                                         |
| genshi_text                      | 12.7 ms                                                                | 15.2 ms: 1.20x slower                                                        |
| sqlalchemy_imperative            | 6.05 ms                                                                | 7.27 ms: 1.20x slower                                                        |
| genshi_xml                       | 26.9 ms                                                                | 32.6 ms: 1.21x slower                                                        |
| xml_etree_process                | 33.6 ms                                                                | 40.9 ms: 1.22x slower                                                        |
| deepcopy_reduce                  | 1.48 us                                                                | 1.81 us: 1.22x slower                                                        |
| comprehensions                   | 9.76 us                                                                | 11.9 us: 1.22x slower                                                        |
| django_template                  | 18.7 ms                                                                | 23.0 ms: 1.23x slower                                                        |
| regex_compile                    | 61.9 ms                                                                | 76.2 ms: 1.23x slower                                                        |
| logging_silent                   | 57.1 ns                                                                | 71.3 ns: 1.25x slower                                                        |
| go                               | 70.4 ms                                                                | 88.0 ms: 1.25x slower                                                        |
| fannkuch                         | 247 ms                                                                 | 310 ms: 1.26x slower                                                         |
| coroutines                       | 15.1 ms                                                                | 19.0 ms: 1.26x slower                                                        |
| nbody                            | 63.9 ms                                                                | 81.0 ms: 1.27x slower                                                        |
| pprint_pformat                   | 882 ms                                                                 | 1.12 sec: 1.27x slower                                                       |
| pprint_safe_repr                 | 439 ms                                                                 | 560 ms: 1.28x slower                                                         |
| deepcopy                         | 141 us                                                                 | 181 us: 1.28x slower                                                         |
| 2to3                             | 152 ms                                                                 | 196 ms: 1.29x slower                                                         |
| unpickle_pure_python             | 124 us                                                                 | 161 us: 1.30x slower                                                         |
| hexiom                           | 3.76 ms                                                                | 4.90 ms: 1.30x slower                                                        |
| deepcopy_memo                    | 16.5 us                                                                | 22.2 us: 1.35x slower                                                        |
| generators                       | 17.7 ms                                                                | 23.9 ms: 1.35x slower                                                        |
| tomli_loads                      | 1.15 sec                                                               | 1.57 sec: 1.37x slower                                                       |
| Geometric mean                   | (ref)                                                                  | 1.12x slower                                                                 |

Benchmark hidden because not significant (6): connected_components, gc_traversal, dask, regex_dna, create_gc_cycles, python_startup

- Geometric mean (including insignificant results): 1.106x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.09x
- 95% likely to have a slowdown of 1.09x
- 99% likely to have a slowdown of 1.08x

# Memory
- memory change: 1.01x