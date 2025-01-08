# Results vs. base

- fork: Fidget-Spinner
- ref: tail_call
- machine: darwin-arm64
- commit hash: f1d3190
- commit date: 2025-01-07
- overall geometric mean: 1.147x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250105-darwin-arm64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250107-darwin-arm64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 170 ms                                                                 | 150 ms: 1.13x faster                                                  |
| docutils       | 1.45 sec                                                               | 1.36 sec: 1.06x faster                                                |
| html5lib       | 34.2 ms                                                                | 28.9 ms: 1.18x faster                                                 |
| sphinx         | 581 ms                                                                 | 539 ms: 1.08x faster                                                  |
| Geometric mean | (ref)                                                                  | 1.11x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20250105-darwin-arm64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250107-darwin-arm64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|----------------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager_tg              | 48.7 ms                                                                | 40.6 ms: 1.20x faster                                                 |
| async_tree_eager                 | 69.8 ms                                                                | 58.8 ms: 1.19x faster                                                 |
| async_tree_none                  | 174 ms                                                                 | 152 ms: 1.15x faster                                                  |
| async_tree_io_tg                 | 378 ms                                                                 | 331 ms: 1.14x faster                                                  |
| async_tree_none_tg               | 158 ms                                                                 | 138 ms: 1.14x faster                                                  |
| async_tree_memoization           | 215 ms                                                                 | 191 ms: 1.13x faster                                                  |
| coroutines                       | 16.6 ms                                                                | 14.7 ms: 1.13x faster                                                 |
| async_tree_io                    | 389 ms                                                                 | 348 ms: 1.12x faster                                                  |
| async_tree_eager_memoization_tg  | 129 ms                                                                 | 115 ms: 1.12x faster                                                  |
| async_tree_eager_io              | 379 ms                                                                 | 341 ms: 1.11x faster                                                  |
| async_tree_eager_io_tg           | 382 ms                                                                 | 345 ms: 1.11x faster                                                  |
| async_tree_eager_memoization     | 148 ms                                                                 | 135 ms: 1.10x faster                                                  |
| async_tree_memoization_tg        | 199 ms                                                                 | 181 ms: 1.10x faster                                                  |
| async_generators                 | 304 ms                                                                 | 278 ms: 1.09x faster                                                  |
| async_tree_cpu_io_mixed          | 419 ms                                                                 | 402 ms: 1.04x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 414 ms                                                                 | 398 ms: 1.04x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 362 ms                                                                 | 350 ms: 1.03x faster                                                  |
| async_tree_eager_cpu_io_mixed_tg | 339 ms                                                                 | 330 ms: 1.03x faster                                                  |
| Geometric mean                   | (ref)                                                                  | 1.10x faster                                                          |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250105-darwin-arm64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250107-darwin-arm64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 79.6 ms                                                                | 60.1 ms: 1.32x faster                                                 |
| float          | 53.2 ms                                                                | 43.4 ms: 1.23x faster                                                 |
| pidigits       | 280 ms                                                                 | 280 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                                  | 1.18x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250105-darwin-arm64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250107-darwin-arm64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 79.3 ms                                                                | 62.0 ms: 1.28x faster                                                 |
| regex_v8       | 17.0 ms                                                                | 16.9 ms: 1.01x faster                                                 |
| regex_effbot   | 2.06 ms                                                                | 2.05 ms: 1.01x faster                                                 |
| Geometric mean | (ref)                                                                  | 1.07x faster                                                          |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250105-darwin-arm64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250107-darwin-arm64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|----------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 1.63 sec                                                               | 1.14 sec: 1.43x faster                                                |
| unpickle_pure_python | 164 us                                                                 | 120 us: 1.37x faster                                                  |
| pickle_pure_python   | 226 us                                                                 | 180 us: 1.26x faster                                                  |
| xml_etree_process    | 41.3 ms                                                                | 33.6 ms: 1.23x faster                                                 |
| xml_etree_generate   | 56.4 ms                                                                | 48.4 ms: 1.17x faster                                                 |
| xml_etree_parse      | 103 ms                                                                 | 97.5 ms: 1.06x faster                                                 |
| json_dumps           | 7.49 ms                                                                | 7.10 ms: 1.05x faster                                                 |
| xml_etree_iterparse  | 72.7 ms                                                                | 69.5 ms: 1.05x faster                                                 |
| json_loads           | 16.3 us                                                                | 16.1 us: 1.01x faster                                                 |
| Geometric mean       | (ref)                                                                  | 1.17x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250105-darwin-arm64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250107-darwin-arm64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 13.7 ms                                                                | 13.7 ms: 1.01x slower                                                 |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                          |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250105-darwin-arm64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250107-darwin-arm64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|-----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 16.6 ms                                                                | 12.5 ms: 1.34x faster                                                 |
| genshi_xml      | 35.0 ms                                                                | 26.3 ms: 1.33x faster                                                 |
| django_template | 23.1 ms                                                                | 18.9 ms: 1.22x faster                                                 |
| mako            | 8.15 ms                                                                | 6.92 ms: 1.18x faster                                                 |
| Geometric mean  | (ref)                                                                  | 1.26x faster                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20250105-darwin-arm64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250107-darwin-arm64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|----------------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| generators                       | 25.0 ms                                                                | 17.2 ms: 1.45x faster                                                 |
| tomli_loads                      | 1.63 sec                                                               | 1.14 sec: 1.43x faster                                                |
| deepcopy_memo                    | 23.0 us                                                                | 16.5 us: 1.39x faster                                                 |
| unpickle_pure_python             | 164 us                                                                 | 120 us: 1.37x faster                                                  |
| go                               | 96.5 ms                                                                | 70.9 ms: 1.36x faster                                                 |
| genshi_text                      | 16.6 ms                                                                | 12.5 ms: 1.34x faster                                                 |
| hexiom                           | 4.95 ms                                                                | 3.71 ms: 1.33x faster                                                 |
| genshi_xml                       | 35.0 ms                                                                | 26.3 ms: 1.33x faster                                                 |
| logging_silent                   | 76.4 ns                                                                | 57.6 ns: 1.33x faster                                                 |
| nbody                            | 79.6 ms                                                                | 60.1 ms: 1.32x faster                                                 |
| deepcopy                         | 182 us                                                                 | 139 us: 1.31x faster                                                  |
| fannkuch                         | 318 ms                                                                 | 245 ms: 1.30x faster                                                  |
| scimark_monte_carlo              | 48.4 ms                                                                | 37.4 ms: 1.29x faster                                                 |
| pprint_pformat                   | 1.14 sec                                                               | 882 ms: 1.29x faster                                                  |
| regex_compile                    | 79.3 ms                                                                | 62.0 ms: 1.28x faster                                                 |
| comprehensions                   | 13.7 us                                                                | 10.7 us: 1.28x faster                                                 |
| pprint_safe_repr                 | 559 ms                                                                 | 438 ms: 1.28x faster                                                  |
| sqlglot_parse                    | 871 us                                                                 | 686 us: 1.27x faster                                                  |
| scimark_sor                      | 92.0 ms                                                                | 72.7 ms: 1.27x faster                                                 |
| pickle_pure_python               | 226 us                                                                 | 180 us: 1.26x faster                                                  |
| sqlglot_transpile                | 1.05 ms                                                                | 841 us: 1.25x faster                                                  |
| chaos                            | 43.3 ms                                                                | 34.6 ms: 1.25x faster                                                 |
| richards                         | 33.9 ms                                                                | 27.4 ms: 1.24x faster                                                 |
| deepcopy_reduce                  | 1.80 us                                                                | 1.46 us: 1.23x faster                                                 |
| xml_etree_process                | 41.3 ms                                                                | 33.6 ms: 1.23x faster                                                 |
| float                            | 53.2 ms                                                                | 43.4 ms: 1.23x faster                                                 |
| richards_super                   | 37.7 ms                                                                | 30.8 ms: 1.22x faster                                                 |
| sqlalchemy_imperative            | 7.49 ms                                                                | 6.13 ms: 1.22x faster                                                 |
| nqueens                          | 61.7 ms                                                                | 50.6 ms: 1.22x faster                                                 |
| deltablue                        | 2.50 ms                                                                | 2.05 ms: 1.22x faster                                                 |
| django_template                  | 23.1 ms                                                                | 18.9 ms: 1.22x faster                                                 |
| async_tree_eager_tg              | 48.7 ms                                                                | 40.6 ms: 1.20x faster                                                 |
| scimark_lu                       | 77.1 ms                                                                | 64.3 ms: 1.20x faster                                                 |
| scimark_sparse_mat_mult          | 3.11 ms                                                                | 2.60 ms: 1.20x faster                                                 |
| pyflate                          | 332 ms                                                                 | 278 ms: 1.19x faster                                                  |
| async_tree_eager                 | 69.8 ms                                                                | 58.8 ms: 1.19x faster                                                 |
| raytrace                         | 180 ms                                                                 | 152 ms: 1.18x faster                                                  |
| html5lib                         | 34.2 ms                                                                | 28.9 ms: 1.18x faster                                                 |
| scimark_fft                      | 197 ms                                                                 | 167 ms: 1.18x faster                                                  |
| typing_runtime_protocols         | 106 us                                                                 | 90.1 us: 1.18x faster                                                 |
| mako                             | 8.15 ms                                                                | 6.92 ms: 1.18x faster                                                 |
| logging_simple                   | 3.48 us                                                                | 2.95 us: 1.18x faster                                                 |
| xml_etree_generate               | 56.4 ms                                                                | 48.4 ms: 1.17x faster                                                 |
| logging_format                   | 3.77 us                                                                | 3.25 us: 1.16x faster                                                 |
| spectral_norm                    | 68.2 ms                                                                | 59.2 ms: 1.15x faster                                                 |
| sqlglot_normalize                | 191 ms                                                                 | 166 ms: 1.15x faster                                                  |
| pycparser                        | 698 ms                                                                 | 608 ms: 1.15x faster                                                  |
| async_tree_none                  | 174 ms                                                                 | 152 ms: 1.15x faster                                                  |
| sympy_str                        | 149 ms                                                                 | 130 ms: 1.14x faster                                                  |
| sqlglot_optimize                 | 34.8 ms                                                                | 30.4 ms: 1.14x faster                                                 |
| async_tree_io_tg                 | 378 ms                                                                 | 331 ms: 1.14x faster                                                  |
| crypto_pyaes                     | 53.3 ms                                                                | 46.6 ms: 1.14x faster                                                 |
| async_tree_none_tg               | 158 ms                                                                 | 138 ms: 1.14x faster                                                  |
| 2to3                             | 170 ms                                                                 | 150 ms: 1.13x faster                                                  |
| sympy_expand                     | 248 ms                                                                 | 220 ms: 1.13x faster                                                  |
| async_tree_memoization           | 215 ms                                                                 | 191 ms: 1.13x faster                                                  |
| bpe_tokeniser                    | 3.24 sec                                                               | 2.87 sec: 1.13x faster                                                |
| coroutines                       | 16.6 ms                                                                | 14.7 ms: 1.13x faster                                                 |
| subparsers                       | 12.8 ms                                                                | 11.4 ms: 1.12x faster                                                 |
| sqlalchemy_declarative           | 61.7 ms                                                                | 55.1 ms: 1.12x faster                                                 |
| sympy_sum                        | 77.6 ms                                                                | 69.3 ms: 1.12x faster                                                 |
| async_tree_io                    | 389 ms                                                                 | 348 ms: 1.12x faster                                                  |
| async_tree_eager_memoization_tg  | 129 ms                                                                 | 115 ms: 1.12x faster                                                  |
| many_optionals                   | 471 us                                                                 | 424 us: 1.11x faster                                                  |
| async_tree_eager_io              | 379 ms                                                                 | 341 ms: 1.11x faster                                                  |
| meteor_contest                   | 78.1 ms                                                                | 70.3 ms: 1.11x faster                                                 |
| bench_thread_pool                | 505 us                                                                 | 456 us: 1.11x faster                                                  |
| async_tree_eager_io_tg           | 382 ms                                                                 | 345 ms: 1.11x faster                                                  |
| sympy_integrate                  | 11.2 ms                                                                | 10.2 ms: 1.10x faster                                                 |
| thrift                           | 455 us                                                                 | 413 us: 1.10x faster                                                  |
| async_tree_eager_memoization     | 148 ms                                                                 | 135 ms: 1.10x faster                                                  |
| async_tree_memoization_tg        | 199 ms                                                                 | 181 ms: 1.10x faster                                                  |
| dulwich_log                      | 28.7 ms                                                                | 26.2 ms: 1.10x faster                                                 |
| async_generators                 | 304 ms                                                                 | 278 ms: 1.09x faster                                                  |
| pylint                           | 163 ms                                                                 | 150 ms: 1.09x faster                                                  |
| sphinx                           | 581 ms                                                                 | 539 ms: 1.08x faster                                                  |
| telco                            | 4.71 ms                                                                | 4.41 ms: 1.07x faster                                                 |
| docutils                         | 1.45 sec                                                               | 1.36 sec: 1.06x faster                                                |
| xml_etree_parse                  | 103 ms                                                                 | 97.5 ms: 1.06x faster                                                 |
| mdp                              | 1.50 sec                                                               | 1.42 sec: 1.06x faster                                                |
| json_dumps                       | 7.49 ms                                                                | 7.10 ms: 1.05x faster                                                 |
| xml_etree_iterparse              | 72.7 ms                                                                | 69.5 ms: 1.05x faster                                                 |
| async_tree_cpu_io_mixed          | 419 ms                                                                 | 402 ms: 1.04x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 414 ms                                                                 | 398 ms: 1.04x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 362 ms                                                                 | 350 ms: 1.03x faster                                                  |
| json                             | 2.88 ms                                                                | 2.80 ms: 1.03x faster                                                 |
| connected_components             | 302 ms                                                                 | 293 ms: 1.03x faster                                                  |
| async_tree_eager_cpu_io_mixed_tg | 339 ms                                                                 | 330 ms: 1.03x faster                                                  |
| shortest_path                    | 329 ms                                                                 | 321 ms: 1.02x faster                                                  |
| sqlite_synth                     | 1.57 us                                                                | 1.54 us: 1.02x faster                                                 |
| bench_mp_pool                    | 61.3 ms                                                                | 60.1 ms: 1.02x faster                                                 |
| json_loads                       | 16.3 us                                                                | 16.1 us: 1.01x faster                                                 |
| regex_v8                         | 17.0 ms                                                                | 16.9 ms: 1.01x faster                                                 |
| regex_effbot                     | 2.06 ms                                                                | 2.05 ms: 1.01x faster                                                 |
| pidigits                         | 280 ms                                                                 | 280 ms: 1.00x faster                                                  |
| python_startup_no_site           | 13.7 ms                                                                | 13.7 ms: 1.01x slower                                                 |
| gc_traversal                     | 3.06 ms                                                                | 3.10 ms: 1.01x slower                                                 |
| create_gc_cycles                 | 1.26 ms                                                                | 1.28 ms: 1.02x slower                                                 |
| Geometric mean                   | (ref)                                                                  | 1.15x faster                                                          |

Benchmark hidden because not significant (6): k_core, pathlib, asyncio_websockets, regex_dna, python_startup, coverage

- Geometric mean (including insignificant results): 1.147x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.11x
- 95% likely to have a speedup of 1.11x
- 99% likely to have a speedup of 1.10x

# Memory
- memory change: 1.00x