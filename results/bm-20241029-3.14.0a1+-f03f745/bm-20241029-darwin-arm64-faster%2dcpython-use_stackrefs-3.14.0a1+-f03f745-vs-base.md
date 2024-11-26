# Results vs. base

- fork: faster-cpython
- ref: use_stackrefs
- machine: darwin-arm64
- commit hash: f03f745
- commit date: 2024-10-29
- overall geometric mean: 1.052x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241029-darwin-arm64-python-faa3272fb8d63d481a13-3.14.0a1+-faa3272 | bm-20241029-darwin-arm64-faster%2dcpython-use_stackrefs-3.14.0a1+-f03f745 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 165 ms                                                                 | 171 ms: 1.04x slower                                                      |
| docutils       | 1.41 sec                                                               | 1.47 sec: 1.04x slower                                                    |
| html5lib       | 30.2 ms                                                                | 33.5 ms: 1.11x slower                                                     |
| sphinx         | 581 ms                                                                 | 611 ms: 1.05x slower                                                      |
| Geometric mean | (ref)                                                                  | 1.07x slower                                                              |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241029-darwin-arm64-python-faa3272fb8d63d481a13-3.14.0a1+-faa3272 | bm-20241029-darwin-arm64-faster%2dcpython-use_stackrefs-3.14.0a1+-f03f745 |
|----------------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_eager_io_tg           | 730 ms                                                                 | 740 ms: 1.01x slower                                                      |
| async_tree_eager_cpu_io_mixed_tg | 333 ms                                                                 | 338 ms: 1.02x slower                                                      |
| async_tree_eager_cpu_io_mixed    | 357 ms                                                                 | 364 ms: 1.02x slower                                                      |
| async_tree_eager_memoization_tg  | 131 ms                                                                 | 134 ms: 1.02x slower                                                      |
| async_tree_cpu_io_mixed          | 458 ms                                                                 | 469 ms: 1.02x slower                                                      |
| async_tree_eager_memoization     | 152 ms                                                                 | 156 ms: 1.03x slower                                                      |
| async_tree_io_tg                 | 618 ms                                                                 | 640 ms: 1.04x slower                                                      |
| async_tree_memoization_tg        | 234 ms                                                                 | 244 ms: 1.04x slower                                                      |
| async_generators                 | 277 ms                                                                 | 289 ms: 1.04x slower                                                      |
| async_tree_none_tg               | 214 ms                                                                 | 224 ms: 1.05x slower                                                      |
| async_tree_memoization           | 247 ms                                                                 | 262 ms: 1.06x slower                                                      |
| async_tree_none                  | 200 ms                                                                 | 213 ms: 1.06x slower                                                      |
| async_tree_eager_tg              | 42.1 ms                                                                | 45.5 ms: 1.08x slower                                                     |
| async_tree_eager                 | 60.8 ms                                                                | 66.3 ms: 1.09x slower                                                     |
| coroutines                       | 16.3 ms                                                                | 18.1 ms: 1.11x slower                                                     |
| Geometric mean                   | (ref)                                                                  | 1.04x slower                                                              |

Benchmark hidden because not significant (4): asyncio_websockets, async_tree_io, async_tree_cpu_io_mixed_tg, async_tree_eager_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241029-darwin-arm64-python-faa3272fb8d63d481a13-3.14.0a1+-faa3272 | bm-20241029-darwin-arm64-faster%2dcpython-use_stackrefs-3.14.0a1+-f03f745 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 65.5 ms                                                                | 64.9 ms: 1.01x faster                                                     |
| pidigits       | 283 ms                                                                 | 283 ms: 1.00x slower                                                      |
| float          | 49.5 ms                                                                | 51.4 ms: 1.04x slower                                                     |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241029-darwin-arm64-python-faa3272fb8d63d481a13-3.14.0a1+-faa3272 | bm-20241029-darwin-arm64-faster%2dcpython-use_stackrefs-3.14.0a1+-f03f745 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_v8       | 16.7 ms                                                                | 16.5 ms: 1.01x faster                                                     |
| regex_dna      | 141 ms                                                                 | 140 ms: 1.00x faster                                                      |
| regex_effbot   | 2.44 ms                                                                | 2.45 ms: 1.00x slower                                                     |
| regex_compile  | 68.6 ms                                                                | 74.2 ms: 1.08x slower                                                     |
| Geometric mean | (ref)                                                                  | 1.02x slower                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241029-darwin-arm64-python-faa3272fb8d63d481a13-3.14.0a1+-faa3272 | bm-20241029-darwin-arm64-faster%2dcpython-use_stackrefs-3.14.0a1+-f03f745 |
|----------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| json_dumps           | 7.26 ms                                                                | 7.37 ms: 1.01x slower                                                     |
| xml_etree_iterparse  | 73.6 ms                                                                | 74.8 ms: 1.02x slower                                                     |
| json_loads           | 16.5 us                                                                | 16.9 us: 1.03x slower                                                     |
| xml_etree_process    | 37.9 ms                                                                | 40.8 ms: 1.08x slower                                                     |
| tomli_loads          | 1.49 sec                                                               | 1.64 sec: 1.10x slower                                                    |
| xml_etree_generate   | 52.7 ms                                                                | 58.6 ms: 1.11x slower                                                     |
| pickle_pure_python   | 184 us                                                                 | 209 us: 1.13x slower                                                      |
| unpickle_pure_python | 143 us                                                                 | 167 us: 1.16x slower                                                      |
| Geometric mean       | (ref)                                                                  | 1.07x slower                                                              |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241029-darwin-arm64-python-faa3272fb8d63d481a13-3.14.0a1+-faa3272 | bm-20241029-darwin-arm64-faster%2dcpython-use_stackrefs-3.14.0a1+-f03f745 |
|------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 12.2 ms                                                                | 12.4 ms: 1.02x slower                                                     |
| python_startup         | 16.8 ms                                                                | 17.1 ms: 1.02x slower                                                     |
| Geometric mean         | (ref)                                                                  | 1.02x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241029-darwin-arm64-python-faa3272fb8d63d481a13-3.14.0a1+-faa3272 | bm-20241029-darwin-arm64-faster%2dcpython-use_stackrefs-3.14.0a1+-f03f745 |
|-----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| django_template | 19.7 ms                                                                | 21.5 ms: 1.09x slower                                                     |
| genshi_xml      | 30.0 ms                                                                | 32.9 ms: 1.10x slower                                                     |
| mako            | 6.60 ms                                                                | 7.35 ms: 1.11x slower                                                     |
| genshi_text     | 13.7 ms                                                                | 15.8 ms: 1.15x slower                                                     |
| Geometric mean  | (ref)                                                                  | 1.11x slower                                                              |

All benchmarks:
===============

| Benchmark                        | bm-20241029-darwin-arm64-python-faa3272fb8d63d481a13-3.14.0a1+-faa3272 | bm-20241029-darwin-arm64-faster%2dcpython-use_stackrefs-3.14.0a1+-f03f745 |
|----------------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| comprehensions                   | 11.4 us                                                                | 11.2 us: 1.02x faster                                                     |
| nbody                            | 65.5 ms                                                                | 64.9 ms: 1.01x faster                                                     |
| gc_traversal                     | 2.97 ms                                                                | 2.94 ms: 1.01x faster                                                     |
| regex_v8                         | 16.7 ms                                                                | 16.5 ms: 1.01x faster                                                     |
| regex_dna                        | 141 ms                                                                 | 140 ms: 1.00x faster                                                      |
| pidigits                         | 283 ms                                                                 | 283 ms: 1.00x slower                                                      |
| regex_effbot                     | 2.44 ms                                                                | 2.45 ms: 1.00x slower                                                     |
| coverage                         | 44.0 ms                                                                | 44.2 ms: 1.00x slower                                                     |
| bench_mp_pool                    | 58.5 ms                                                                | 59.1 ms: 1.01x slower                                                     |
| telco                            | 4.64 ms                                                                | 4.69 ms: 1.01x slower                                                     |
| async_tree_eager_io_tg           | 730 ms                                                                 | 740 ms: 1.01x slower                                                      |
| pathlib                          | 22.4 ms                                                                | 22.8 ms: 1.01x slower                                                     |
| json_dumps                       | 7.26 ms                                                                | 7.37 ms: 1.01x slower                                                     |
| shortest_path                    | 346 ms                                                                 | 351 ms: 1.01x slower                                                      |
| async_tree_eager_cpu_io_mixed_tg | 333 ms                                                                 | 338 ms: 1.02x slower                                                      |
| xml_etree_iterparse              | 73.6 ms                                                                | 74.8 ms: 1.02x slower                                                     |
| json                             | 2.89 ms                                                                | 2.94 ms: 1.02x slower                                                     |
| sqlite_synth                     | 1.51 us                                                                | 1.54 us: 1.02x slower                                                     |
| python_startup_no_site           | 12.2 ms                                                                | 12.4 ms: 1.02x slower                                                     |
| async_tree_eager_cpu_io_mixed    | 357 ms                                                                 | 364 ms: 1.02x slower                                                      |
| mdp                              | 1.47 sec                                                               | 1.50 sec: 1.02x slower                                                    |
| connected_components             | 320 ms                                                                 | 327 ms: 1.02x slower                                                      |
| python_startup                   | 16.8 ms                                                                | 17.1 ms: 1.02x slower                                                     |
| meteor_contest                   | 71.1 ms                                                                | 72.8 ms: 1.02x slower                                                     |
| async_tree_eager_memoization_tg  | 131 ms                                                                 | 134 ms: 1.02x slower                                                      |
| async_tree_cpu_io_mixed          | 458 ms                                                                 | 469 ms: 1.02x slower                                                      |
| json_loads                       | 16.5 us                                                                | 16.9 us: 1.03x slower                                                     |
| async_tree_eager_memoization     | 152 ms                                                                 | 156 ms: 1.03x slower                                                      |
| async_tree_io_tg                 | 618 ms                                                                 | 640 ms: 1.04x slower                                                      |
| 2to3                             | 165 ms                                                                 | 171 ms: 1.04x slower                                                      |
| float                            | 49.5 ms                                                                | 51.4 ms: 1.04x slower                                                     |
| docutils                         | 1.41 sec                                                               | 1.47 sec: 1.04x slower                                                    |
| async_tree_memoization_tg        | 234 ms                                                                 | 244 ms: 1.04x slower                                                      |
| sympy_integrate                  | 11.0 ms                                                                | 11.5 ms: 1.04x slower                                                     |
| async_generators                 | 277 ms                                                                 | 289 ms: 1.04x slower                                                      |
| pprint_pformat                   | 935 ms                                                                 | 979 ms: 1.05x slower                                                      |
| sympy_sum                        | 69.9 ms                                                                | 73.2 ms: 1.05x slower                                                     |
| deepcopy_memo                    | 17.0 us                                                                | 17.8 us: 1.05x slower                                                     |
| async_tree_none_tg               | 214 ms                                                                 | 224 ms: 1.05x slower                                                      |
| pprint_safe_repr                 | 458 ms                                                                 | 480 ms: 1.05x slower                                                      |
| sqlglot_normalize                | 168 ms                                                                 | 177 ms: 1.05x slower                                                      |
| sphinx                           | 581 ms                                                                 | 611 ms: 1.05x slower                                                      |
| nqueens                          | 54.7 ms                                                                | 57.6 ms: 1.05x slower                                                     |
| async_tree_memoization           | 247 ms                                                                 | 262 ms: 1.06x slower                                                      |
| dulwich_log                      | 27.2 ms                                                                | 28.8 ms: 1.06x slower                                                     |
| scimark_monte_carlo              | 43.6 ms                                                                | 46.2 ms: 1.06x slower                                                     |
| sympy_str                        | 135 ms                                                                 | 143 ms: 1.06x slower                                                      |
| deepcopy                         | 146 us                                                                 | 155 us: 1.06x slower                                                      |
| sqlalchemy_declarative           | 56.1 ms                                                                | 59.6 ms: 1.06x slower                                                     |
| sqlglot_transpile                | 907 us                                                                 | 962 us: 1.06x slower                                                      |
| thrift                           | 416 us                                                                 | 442 us: 1.06x slower                                                      |
| sqlglot_optimize                 | 31.4 ms                                                                | 33.3 ms: 1.06x slower                                                     |
| pycparser                        | 638 ms                                                                 | 678 ms: 1.06x slower                                                      |
| async_tree_none                  | 200 ms                                                                 | 213 ms: 1.06x slower                                                      |
| raytrace                         | 154 ms                                                                 | 164 ms: 1.06x slower                                                      |
| sqlglot_parse                    | 743 us                                                                 | 792 us: 1.07x slower                                                      |
| sympy_expand                     | 227 ms                                                                 | 242 ms: 1.07x slower                                                      |
| pyflate                          | 325 ms                                                                 | 347 ms: 1.07x slower                                                      |
| fannkuch                         | 265 ms                                                                 | 283 ms: 1.07x slower                                                      |
| scimark_fft                      | 190 ms                                                                 | 203 ms: 1.07x slower                                                      |
| scimark_sor                      | 96.2 ms                                                                | 103 ms: 1.07x slower                                                      |
| xml_etree_process                | 37.9 ms                                                                | 40.8 ms: 1.08x slower                                                     |
| sqlalchemy_imperative            | 6.37 ms                                                                | 6.88 ms: 1.08x slower                                                     |
| regex_compile                    | 68.6 ms                                                                | 74.2 ms: 1.08x slower                                                     |
| bench_thread_pool                | 438 us                                                                 | 474 us: 1.08x slower                                                      |
| bpe_tokeniser                    | 3.10 sec                                                               | 3.35 sec: 1.08x slower                                                    |
| async_tree_eager_tg              | 42.1 ms                                                                | 45.5 ms: 1.08x slower                                                     |
| typing_runtime_protocols         | 92.4 us                                                                | 101 us: 1.09x slower                                                      |
| deepcopy_reduce                  | 1.51 us                                                                | 1.65 us: 1.09x slower                                                     |
| async_tree_eager                 | 60.8 ms                                                                | 66.3 ms: 1.09x slower                                                     |
| django_template                  | 19.7 ms                                                                | 21.5 ms: 1.09x slower                                                     |
| genshi_xml                       | 30.0 ms                                                                | 32.9 ms: 1.10x slower                                                     |
| tomli_loads                      | 1.49 sec                                                               | 1.64 sec: 1.10x slower                                                    |
| logging_silent                   | 62.6 ns                                                                | 69.0 ns: 1.10x slower                                                     |
| chaos                            | 36.3 ms                                                                | 40.0 ms: 1.10x slower                                                     |
| coroutines                       | 16.3 ms                                                                | 18.1 ms: 1.11x slower                                                     |
| scimark_sparse_mat_mult          | 2.82 ms                                                                | 3.13 ms: 1.11x slower                                                     |
| html5lib                         | 30.2 ms                                                                | 33.5 ms: 1.11x slower                                                     |
| xml_etree_generate               | 52.7 ms                                                                | 58.6 ms: 1.11x slower                                                     |
| scimark_lu                       | 67.6 ms                                                                | 75.3 ms: 1.11x slower                                                     |
| mako                             | 6.60 ms                                                                | 7.35 ms: 1.11x slower                                                     |
| spectral_norm                    | 69.5 ms                                                                | 78.0 ms: 1.12x slower                                                     |
| logging_simple                   | 3.06 us                                                                | 3.44 us: 1.12x slower                                                     |
| deltablue                        | 2.25 ms                                                                | 2.53 ms: 1.13x slower                                                     |
| generators                       | 20.2 ms                                                                | 22.8 ms: 1.13x slower                                                     |
| logging_format                   | 3.35 us                                                                | 3.78 us: 1.13x slower                                                     |
| pickle_pure_python               | 184 us                                                                 | 209 us: 1.13x slower                                                      |
| richards                         | 31.1 ms                                                                | 35.3 ms: 1.13x slower                                                     |
| richards_super                   | 34.6 ms                                                                | 39.2 ms: 1.13x slower                                                     |
| hexiom                           | 4.14 ms                                                                | 4.72 ms: 1.14x slower                                                     |
| crypto_pyaes                     | 51.2 ms                                                                | 58.6 ms: 1.14x slower                                                     |
| genshi_text                      | 13.7 ms                                                                | 15.8 ms: 1.15x slower                                                     |
| go                               | 82.9 ms                                                                | 96.4 ms: 1.16x slower                                                     |
| unpickle_pure_python             | 143 us                                                                 | 167 us: 1.16x slower                                                      |
| Geometric mean                   | (ref)                                                                  | 1.06x slower                                                              |

Benchmark hidden because not significant (9): create_gc_cycles, asyncio_websockets, async_tree_io, xml_etree_parse, k_core, async_tree_cpu_io_mixed_tg, async_tree_eager_io, pylint, tornado_http

- Geometric mean (including insignificant results): 1.052x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: 1.00x