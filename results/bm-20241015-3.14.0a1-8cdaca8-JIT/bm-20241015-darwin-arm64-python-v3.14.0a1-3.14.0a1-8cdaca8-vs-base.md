# Results vs. base

- fork: python
- ref: v3.14.0a1
- machine: darwin-arm64
- commit hash: 8cdaca8
- commit date: 2024-10-15
- overall geometric mean: 1.042x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20241015-3.14.0a1-8cdaca8/bm-20241015-darwin-arm64-python-v3.14.0a1-3.14.0a1-8cdaca8.json | results/bm-20241015-3.14.0a1-8cdaca8-JIT/bm-20241015-darwin-arm64-python-v3.14.0a1-3.14.0a1-8cdaca8.json |
|----------------|:----------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------:|
| 2to3           | 160 ms                                                                                               | 183 ms: 1.14x slower                                                                                     |
| docutils       | 1.41 sec                                                                                             | 1.57 sec: 1.12x slower                                                                                   |
| html5lib       | 31.8 ms                                                                                              | 34.2 ms: 1.08x slower                                                                                    |
| sphinx         | 577 ms                                                                                               | 664 ms: 1.15x slower                                                                                     |
| Geometric mean | (ref)                                                                                                | 1.10x slower                                                                                             |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | results/bm-20241015-3.14.0a1-8cdaca8/bm-20241015-darwin-arm64-python-v3.14.0a1-3.14.0a1-8cdaca8.json | results/bm-20241015-3.14.0a1-8cdaca8-JIT/bm-20241015-darwin-arm64-python-v3.14.0a1-3.14.0a1-8cdaca8.json |
|----------------------------------|:----------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------:|
| async_tree_io_tg                 | 611 ms                                                                                               | 611 ms: 1.00x slower                                                                                     |
| asyncio_websockets               | 241 ms                                                                                               | 242 ms: 1.00x slower                                                                                     |
| async_tree_eager_cpu_io_mixed_tg | 333 ms                                                                                               | 336 ms: 1.01x slower                                                                                     |
| coroutines                       | 16.5 ms                                                                                              | 16.7 ms: 1.01x slower                                                                                    |
| async_tree_eager_io_tg           | 704 ms                                                                                               | 714 ms: 1.01x slower                                                                                     |
| async_tree_none                  | 196 ms                                                                                               | 199 ms: 1.02x slower                                                                                     |
| async_tree_eager_cpu_io_mixed    | 356 ms                                                                                               | 363 ms: 1.02x slower                                                                                     |
| async_tree_eager_memoization     | 149 ms                                                                                               | 153 ms: 1.03x slower                                                                                     |
| async_tree_eager_tg              | 41.2 ms                                                                                              | 42.6 ms: 1.03x slower                                                                                    |
| asyncio_tcp                      | 437 ms                                                                                               | 456 ms: 1.04x slower                                                                                     |
| async_generators                 | 276 ms                                                                                               | 292 ms: 1.06x slower                                                                                     |
| async_tree_eager                 | 59.0 ms                                                                                              | 63.5 ms: 1.08x slower                                                                                    |
| Geometric mean                   | (ref)                                                                                                | 1.02x slower                                                                                             |

Benchmark hidden because not significant (9): async_tree_none_tg, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, asyncio_tcp_ssl, async_tree_io, async_tree_cpu_io_mixed, async_tree_eager_memoization_tg, async_tree_memoization, async_tree_eager_io

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20241015-3.14.0a1-8cdaca8/bm-20241015-darwin-arm64-python-v3.14.0a1-3.14.0a1-8cdaca8.json | results/bm-20241015-3.14.0a1-8cdaca8-JIT/bm-20241015-darwin-arm64-python-v3.14.0a1-3.14.0a1-8cdaca8.json |
|----------------|:----------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------:|
| float          | 49.7 ms                                                                                              | 48.2 ms: 1.03x faster                                                                                    |
| nbody          | 65.5 ms                                                                                              | 65.3 ms: 1.00x faster                                                                                    |
| pidigits       | 283 ms                                                                                               | 283 ms: 1.00x faster                                                                                     |
| Geometric mean | (ref)                                                                                                | 1.01x faster                                                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20241015-3.14.0a1-8cdaca8/bm-20241015-darwin-arm64-python-v3.14.0a1-3.14.0a1-8cdaca8.json | results/bm-20241015-3.14.0a1-8cdaca8-JIT/bm-20241015-darwin-arm64-python-v3.14.0a1-3.14.0a1-8cdaca8.json |
|----------------|:----------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------:|
| regex_effbot   | 2.59 ms                                                                                              | 2.61 ms: 1.00x slower                                                                                    |
| regex_dna      | 146 ms                                                                                               | 148 ms: 1.01x slower                                                                                     |
| regex_v8       | 16.5 ms                                                                                              | 16.8 ms: 1.02x slower                                                                                    |
| regex_compile  | 68.4 ms                                                                                              | 74.8 ms: 1.09x slower                                                                                    |
| Geometric mean | (ref)                                                                                                | 1.03x slower                                                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20241015-3.14.0a1-8cdaca8/bm-20241015-darwin-arm64-python-v3.14.0a1-3.14.0a1-8cdaca8.json | results/bm-20241015-3.14.0a1-8cdaca8-JIT/bm-20241015-darwin-arm64-python-v3.14.0a1-3.14.0a1-8cdaca8.json |
|----------------------|:----------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------:|
| tomli_loads          | 1.50 sec                                                                                             | 1.25 sec: 1.20x faster                                                                                   |
| unpickle_pure_python | 143 us                                                                                               | 132 us: 1.09x faster                                                                                     |
| xml_etree_process    | 37.5 ms                                                                                              | 34.8 ms: 1.08x faster                                                                                    |
| pickle_pure_python   | 186 us                                                                                               | 178 us: 1.04x faster                                                                                     |
| xml_etree_generate   | 52.5 ms                                                                                              | 50.4 ms: 1.04x faster                                                                                    |
| xml_etree_iterparse  | 75.1 ms                                                                                              | 73.1 ms: 1.03x faster                                                                                    |
| unpickle_list        | 3.01 us                                                                                              | 2.97 us: 1.02x faster                                                                                    |
| xml_etree_parse      | 109 ms                                                                                               | 107 ms: 1.01x faster                                                                                     |
| pickle_list          | 2.98 us                                                                                              | 2.95 us: 1.01x faster                                                                                    |
| json_dumps           | 7.18 ms                                                                                              | 7.13 ms: 1.01x faster                                                                                    |
| pickle_dict          | 18.1 us                                                                                              | 18.2 us: 1.01x slower                                                                                    |
| json_loads           | 16.4 us                                                                                              | 16.5 us: 1.01x slower                                                                                    |
| Geometric mean       | (ref)                                                                                                | 1.04x faster                                                                                             |

Benchmark hidden because not significant (2): unpickle, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20241015-3.14.0a1-8cdaca8/bm-20241015-darwin-arm64-python-v3.14.0a1-3.14.0a1-8cdaca8.json | results/bm-20241015-3.14.0a1-8cdaca8-JIT/bm-20241015-darwin-arm64-python-v3.14.0a1-3.14.0a1-8cdaca8.json |
|------------------------|:----------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------:|
| python_startup_no_site | 14.7 ms                                                                                              | 14.6 ms: 1.01x faster                                                                                    |
| Geometric mean         | (ref)                                                                                                | 1.00x faster                                                                                             |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20241015-3.14.0a1-8cdaca8/bm-20241015-darwin-arm64-python-v3.14.0a1-3.14.0a1-8cdaca8.json | results/bm-20241015-3.14.0a1-8cdaca8-JIT/bm-20241015-darwin-arm64-python-v3.14.0a1-3.14.0a1-8cdaca8.json |
|-----------------|:----------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------:|
| mako            | 7.01 ms                                                                                              | 6.46 ms: 1.09x faster                                                                                    |
| django_template | 19.8 ms                                                                                              | 23.0 ms: 1.16x slower                                                                                    |
| genshi_text     | 13.7 ms                                                                                              | 16.6 ms: 1.22x slower                                                                                    |
| genshi_xml      | 29.8 ms                                                                                              | 42.3 ms: 1.42x slower                                                                                    |
| Geometric mean  | (ref)                                                                                                | 1.17x slower                                                                                             |

All benchmarks:
===============

| Benchmark                        | results/bm-20241015-3.14.0a1-8cdaca8/bm-20241015-darwin-arm64-python-v3.14.0a1-3.14.0a1-8cdaca8.json | results/bm-20241015-3.14.0a1-8cdaca8-JIT/bm-20241015-darwin-arm64-python-v3.14.0a1-3.14.0a1-8cdaca8.json |
|----------------------------------|:----------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------:|
| tomli_loads                      | 1.50 sec                                                                                             | 1.25 sec: 1.20x faster                                                                                   |
| scimark_sor                      | 95.9 ms                                                                                              | 86.0 ms: 1.12x faster                                                                                    |
| unpickle_pure_python             | 143 us                                                                                               | 132 us: 1.09x faster                                                                                     |
| mako                             | 7.01 ms                                                                                              | 6.46 ms: 1.09x faster                                                                                    |
| xml_etree_process                | 37.5 ms                                                                                              | 34.8 ms: 1.08x faster                                                                                    |
| scimark_lu                       | 68.2 ms                                                                                              | 64.6 ms: 1.06x faster                                                                                    |
| pickle_pure_python               | 186 us                                                                                               | 178 us: 1.04x faster                                                                                     |
| xml_etree_generate               | 52.5 ms                                                                                              | 50.4 ms: 1.04x faster                                                                                    |
| deepcopy_memo                    | 17.4 us                                                                                              | 16.8 us: 1.04x faster                                                                                    |
| float                            | 49.7 ms                                                                                              | 48.2 ms: 1.03x faster                                                                                    |
| xml_etree_iterparse              | 75.1 ms                                                                                              | 73.1 ms: 1.03x faster                                                                                    |
| coverage                         | 44.8 ms                                                                                              | 43.8 ms: 1.02x faster                                                                                    |
| unpickle_list                    | 3.01 us                                                                                              | 2.97 us: 1.02x faster                                                                                    |
| bpe_tokeniser                    | 3.10 sec                                                                                             | 3.05 sec: 1.02x faster                                                                                   |
| spectral_norm                    | 70.2 ms                                                                                              | 69.3 ms: 1.01x faster                                                                                    |
| xml_etree_parse                  | 109 ms                                                                                               | 107 ms: 1.01x faster                                                                                     |
| pickle_list                      | 2.98 us                                                                                              | 2.95 us: 1.01x faster                                                                                    |
| json_dumps                       | 7.18 ms                                                                                              | 7.13 ms: 1.01x faster                                                                                    |
| python_startup_no_site           | 14.7 ms                                                                                              | 14.6 ms: 1.01x faster                                                                                    |
| pyflate                          | 327 ms                                                                                               | 325 ms: 1.01x faster                                                                                     |
| nbody                            | 65.5 ms                                                                                              | 65.3 ms: 1.00x faster                                                                                    |
| pidigits                         | 283 ms                                                                                               | 283 ms: 1.00x faster                                                                                     |
| scimark_fft                      | 190 ms                                                                                               | 190 ms: 1.00x slower                                                                                     |
| async_tree_io_tg                 | 611 ms                                                                                               | 611 ms: 1.00x slower                                                                                     |
| asyncio_websockets               | 241 ms                                                                                               | 242 ms: 1.00x slower                                                                                     |
| fannkuch                         | 268 ms                                                                                               | 269 ms: 1.00x slower                                                                                     |
| regex_effbot                     | 2.59 ms                                                                                              | 2.61 ms: 1.00x slower                                                                                    |
| create_gc_cycles                 | 1.30 ms                                                                                              | 1.30 ms: 1.00x slower                                                                                    |
| pickle_dict                      | 18.1 us                                                                                              | 18.2 us: 1.01x slower                                                                                    |
| json_loads                       | 16.4 us                                                                                              | 16.5 us: 1.01x slower                                                                                    |
| deepcopy_reduce                  | 1.52 us                                                                                              | 1.53 us: 1.01x slower                                                                                    |
| logging_simple                   | 3.08 us                                                                                              | 3.10 us: 1.01x slower                                                                                    |
| async_tree_eager_cpu_io_mixed_tg | 333 ms                                                                                               | 336 ms: 1.01x slower                                                                                     |
| telco                            | 4.53 ms                                                                                              | 4.57 ms: 1.01x slower                                                                                    |
| sqlite_synth                     | 1.52 us                                                                                              | 1.54 us: 1.01x slower                                                                                    |
| regex_dna                        | 146 ms                                                                                               | 148 ms: 1.01x slower                                                                                     |
| coroutines                       | 16.5 ms                                                                                              | 16.7 ms: 1.01x slower                                                                                    |
| async_tree_eager_io_tg           | 704 ms                                                                                               | 714 ms: 1.01x slower                                                                                     |
| async_tree_none                  | 196 ms                                                                                               | 199 ms: 1.02x slower                                                                                     |
| async_tree_eager_cpu_io_mixed    | 356 ms                                                                                               | 363 ms: 1.02x slower                                                                                     |
| json                             | 2.87 ms                                                                                              | 2.93 ms: 1.02x slower                                                                                    |
| logging_format                   | 3.35 us                                                                                              | 3.42 us: 1.02x slower                                                                                    |
| pathlib                          | 22.0 ms                                                                                              | 22.4 ms: 1.02x slower                                                                                    |
| regex_v8                         | 16.5 ms                                                                                              | 16.8 ms: 1.02x slower                                                                                    |
| thrift                           | 416 us                                                                                               | 426 us: 1.02x slower                                                                                     |
| async_tree_eager_memoization     | 149 ms                                                                                               | 153 ms: 1.03x slower                                                                                     |
| async_tree_eager_tg              | 41.2 ms                                                                                              | 42.6 ms: 1.03x slower                                                                                    |
| asyncio_tcp                      | 437 ms                                                                                               | 456 ms: 1.04x slower                                                                                     |
| scimark_monte_carlo              | 43.6 ms                                                                                              | 45.5 ms: 1.04x slower                                                                                    |
| pprint_safe_repr                 | 462 ms                                                                                               | 483 ms: 1.04x slower                                                                                     |
| crypto_pyaes                     | 51.7 ms                                                                                              | 54.0 ms: 1.04x slower                                                                                    |
| bench_mp_pool                    | 58.9 ms                                                                                              | 61.8 ms: 1.05x slower                                                                                    |
| meteor_contest                   | 70.5 ms                                                                                              | 74.4 ms: 1.05x slower                                                                                    |
| pprint_pformat                   | 936 ms                                                                                               | 990 ms: 1.06x slower                                                                                     |
| async_generators                 | 276 ms                                                                                               | 292 ms: 1.06x slower                                                                                     |
| dulwich_log                      | 27.3 ms                                                                                              | 28.9 ms: 1.06x slower                                                                                    |
| deepcopy                         | 146 us                                                                                               | 154 us: 1.06x slower                                                                                     |
| typing_runtime_protocols         | 92.3 us                                                                                              | 97.8 us: 1.06x slower                                                                                    |
| pycparser                        | 635 ms                                                                                               | 678 ms: 1.07x slower                                                                                     |
| mdp                              | 1.46 sec                                                                                             | 1.56 sec: 1.07x slower                                                                                   |
| deltablue                        | 2.23 ms                                                                                              | 2.38 ms: 1.07x slower                                                                                    |
| html5lib                         | 31.8 ms                                                                                              | 34.2 ms: 1.08x slower                                                                                    |
| async_tree_eager                 | 59.0 ms                                                                                              | 63.5 ms: 1.08x slower                                                                                    |
| sympy_expand                     | 227 ms                                                                                               | 246 ms: 1.08x slower                                                                                     |
| regex_compile                    | 68.4 ms                                                                                              | 74.8 ms: 1.09x slower                                                                                    |
| bench_thread_pool                | 433 us                                                                                               | 474 us: 1.09x slower                                                                                     |
| nqueens                          | 53.6 ms                                                                                              | 58.8 ms: 1.10x slower                                                                                    |
| raytrace                         | 154 ms                                                                                               | 171 ms: 1.11x slower                                                                                     |
| scimark_sparse_mat_mult          | 2.83 ms                                                                                              | 3.14 ms: 1.11x slower                                                                                    |
| chaos                            | 37.3 ms                                                                                              | 41.5 ms: 1.11x slower                                                                                    |
| sqlglot_normalize                | 166 ms                                                                                               | 186 ms: 1.12x slower                                                                                     |
| docutils                         | 1.41 sec                                                                                             | 1.57 sec: 1.12x slower                                                                                   |
| richards_super                   | 34.3 ms                                                                                              | 38.7 ms: 1.13x slower                                                                                    |
| richards                         | 31.0 ms                                                                                              | 35.0 ms: 1.13x slower                                                                                    |
| sympy_str                        | 133 ms                                                                                               | 151 ms: 1.13x slower                                                                                     |
| sympy_sum                        | 69.6 ms                                                                                              | 79.4 ms: 1.14x slower                                                                                    |
| sympy_integrate                  | 11.0 ms                                                                                              | 12.5 ms: 1.14x slower                                                                                    |
| 2to3                             | 160 ms                                                                                               | 183 ms: 1.14x slower                                                                                     |
| logging_silent                   | 60.9 ns                                                                                              | 69.8 ns: 1.15x slower                                                                                    |
| sphinx                           | 577 ms                                                                                               | 664 ms: 1.15x slower                                                                                     |
| django_template                  | 19.8 ms                                                                                              | 23.0 ms: 1.16x slower                                                                                    |
| sqlglot_transpile                | 901 us                                                                                               | 1.06 ms: 1.17x slower                                                                                    |
| pylint                           | 180 ms                                                                                               | 212 ms: 1.17x slower                                                                                     |
| sqlglot_parse                    | 743 us                                                                                               | 875 us: 1.18x slower                                                                                     |
| comprehensions                   | 11.1 us                                                                                              | 13.1 us: 1.18x slower                                                                                    |
| go                               | 82.1 ms                                                                                              | 97.6 ms: 1.19x slower                                                                                    |
| sqlglot_optimize                 | 31.1 ms                                                                                              | 37.1 ms: 1.19x slower                                                                                    |
| hexiom                           | 4.13 ms                                                                                              | 4.96 ms: 1.20x slower                                                                                    |
| genshi_text                      | 13.7 ms                                                                                              | 16.6 ms: 1.22x slower                                                                                    |
| generators                       | 20.1 ms                                                                                              | 25.4 ms: 1.26x slower                                                                                    |
| genshi_xml                       | 29.8 ms                                                                                              | 42.3 ms: 1.42x slower                                                                                    |
| unpack_sequence                  | 26.8 ns                                                                                              | 76.0 ns: 2.84x slower                                                                                    |
| Geometric mean                   | (ref)                                                                                                | 1.05x slower                                                                                             |

Benchmark hidden because not significant (14): async_tree_none_tg, unpickle, python_startup, pickle, tornado_http, gc_traversal, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, asyncio_tcp_ssl, async_tree_io, async_tree_cpu_io_mixed, async_tree_eager_memoization_tg, async_tree_memoization, async_tree_eager_io

- Geometric mean (including insignificant results): 1.042x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 1.09x