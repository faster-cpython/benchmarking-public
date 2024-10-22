# Results vs. base

- fork: python
- ref: 79c542b5cc774ba758ac
- machine: darwin-arm64
- commit hash: 79c542b
- commit date: 2024-08-17
- overall geometric mean: 1.05x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20240817-3.14.0a0-79c542b/bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b.json | results/bm-20240817-3.14.0a0-79c542b-JIT/bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b.json |
|----------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 162 ms                                                                                                          | 179 ms: 1.11x slower                                                                                                |
| docutils       | 1.47 sec                                                                                                        | 1.62 sec: 1.11x slower                                                                                              |
| html5lib       | 31.4 ms                                                                                                         | 34.5 ms: 1.10x slower                                                                                               |
| Geometric mean | (ref)                                                                                                           | 1.06x slower                                                                                                        |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | results/bm-20240817-3.14.0a0-79c542b/bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b.json | results/bm-20240817-3.14.0a0-79c542b-JIT/bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b.json |
|----------------------------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| async_tree_io_tg                 | 505 ms                                                                                                          | 492 ms: 1.03x faster                                                                                                |
| coroutines                       | 16.2 ms                                                                                                         | 16.1 ms: 1.00x faster                                                                                               |
| async_tree_eager_cpu_io_mixed_tg | 336 ms                                                                                                          | 338 ms: 1.00x slower                                                                                                |
| asyncio_tcp_ssl                  | 1.28 sec                                                                                                        | 1.29 sec: 1.01x slower                                                                                              |
| async_tree_eager_cpu_io_mixed    | 360 ms                                                                                                          | 367 ms: 1.02x slower                                                                                                |
| async_tree_none                  | 192 ms                                                                                                          | 197 ms: 1.03x slower                                                                                                |
| async_tree_eager_memoization     | 151 ms                                                                                                          | 155 ms: 1.03x slower                                                                                                |
| async_tree_eager                 | 62.0 ms                                                                                                         | 64.8 ms: 1.04x slower                                                                                               |
| async_generators                 | 282 ms                                                                                                          | 297 ms: 1.05x slower                                                                                                |
| asyncio_tcp                      | 413 ms                                                                                                          | 448 ms: 1.08x slower                                                                                                |
| Geometric mean                   | (ref)                                                                                                           | 1.02x slower                                                                                                        |

Benchmark hidden because not significant (11): asyncio_websockets, async_tree_eager_tg, async_tree_none_tg, async_tree_memoization, async_tree_memoization_tg, async_tree_cpu_io_mixed, async_tree_io, async_tree_eager_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20240817-3.14.0a0-79c542b/bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b.json | results/bm-20240817-3.14.0a0-79c542b-JIT/bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b.json |
|----------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| float          | 48.7 ms                                                                                                         | 46.6 ms: 1.04x faster                                                                                               |
| nbody          | 60.8 ms                                                                                                         | 63.8 ms: 1.05x slower                                                                                               |
| Geometric mean | (ref)                                                                                                           | 1.00x slower                                                                                                        |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20240817-3.14.0a0-79c542b/bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b.json | results/bm-20240817-3.14.0a0-79c542b-JIT/bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b.json |
|----------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| regex_dna      | 145 ms                                                                                                          | 145 ms: 1.00x faster                                                                                                |
| regex_effbot   | 2.47 ms                                                                                                         | 2.46 ms: 1.00x faster                                                                                               |
| regex_v8       | 16.6 ms                                                                                                         | 16.9 ms: 1.01x slower                                                                                               |
| regex_compile  | 68.0 ms                                                                                                         | 74.8 ms: 1.10x slower                                                                                               |
| Geometric mean | (ref)                                                                                                           | 1.03x slower                                                                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20240817-3.14.0a0-79c542b/bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b.json | results/bm-20240817-3.14.0a0-79c542b-JIT/bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b.json |
|----------------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| tomli_loads          | 1.48 sec                                                                                                        | 1.26 sec: 1.17x faster                                                                                              |
| xml_etree_process    | 37.3 ms                                                                                                         | 34.4 ms: 1.08x faster                                                                                               |
| unpickle_pure_python | 143 us                                                                                                          | 134 us: 1.07x faster                                                                                                |
| xml_etree_generate   | 53.1 ms                                                                                                         | 50.3 ms: 1.06x faster                                                                                               |
| xml_etree_iterparse  | 74.8 ms                                                                                                         | 71.7 ms: 1.04x faster                                                                                               |
| xml_etree_parse      | 111 ms                                                                                                          | 109 ms: 1.02x faster                                                                                                |
| pickle_pure_python   | 182 us                                                                                                          | 179 us: 1.02x faster                                                                                                |
| json_loads           | 17.3 us                                                                                                         | 17.2 us: 1.01x faster                                                                                               |
| json_dumps           | 6.38 ms                                                                                                         | 6.50 ms: 1.02x slower                                                                                               |
| Geometric mean       | (ref)                                                                                                           | 1.05x faster                                                                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20240817-3.14.0a0-79c542b/bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b.json | results/bm-20240817-3.14.0a0-79c542b-JIT/bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b.json |
|------------------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| python_startup         | 13.8 ms                                                                                                         | 14.3 ms: 1.04x slower                                                                                               |
| python_startup_no_site | 10.9 ms                                                                                                         | 11.6 ms: 1.06x slower                                                                                               |
| Geometric mean         | (ref)                                                                                                           | 1.05x slower                                                                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20240817-3.14.0a0-79c542b/bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b.json | results/bm-20240817-3.14.0a0-79c542b-JIT/bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b.json |
|-----------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| mako            | 6.96 ms                                                                                                         | 6.50 ms: 1.07x faster                                                                                               |
| django_template | 19.6 ms                                                                                                         | 23.0 ms: 1.17x slower                                                                                               |
| genshi_text     | 14.1 ms                                                                                                         | 17.0 ms: 1.20x slower                                                                                               |
| genshi_xml      | 30.4 ms                                                                                                         | 42.1 ms: 1.39x slower                                                                                               |
| Geometric mean  | (ref)                                                                                                           | 1.16x slower                                                                                                        |

All benchmarks:
===============

| Benchmark                        | results/bm-20240817-3.14.0a0-79c542b/bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b.json | results/bm-20240817-3.14.0a0-79c542b-JIT/bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b.json |
|----------------------------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| tomli_loads                      | 1.48 sec                                                                                                        | 1.26 sec: 1.17x faster                                                                                              |
| xml_etree_process                | 37.3 ms                                                                                                         | 34.4 ms: 1.08x faster                                                                                               |
| mako                             | 6.96 ms                                                                                                         | 6.50 ms: 1.07x faster                                                                                               |
| unpickle_pure_python             | 143 us                                                                                                          | 134 us: 1.07x faster                                                                                                |
| scimark_sor                      | 93.8 ms                                                                                                         | 88.0 ms: 1.07x faster                                                                                               |
| mdp                              | 1.54 sec                                                                                                        | 1.45 sec: 1.06x faster                                                                                              |
| deepcopy_memo                    | 17.1 us                                                                                                         | 16.2 us: 1.06x faster                                                                                               |
| xml_etree_generate               | 53.1 ms                                                                                                         | 50.3 ms: 1.06x faster                                                                                               |
| float                            | 48.7 ms                                                                                                         | 46.6 ms: 1.04x faster                                                                                               |
| xml_etree_iterparse              | 74.8 ms                                                                                                         | 71.7 ms: 1.04x faster                                                                                               |
| scimark_lu                       | 67.8 ms                                                                                                         | 65.6 ms: 1.03x faster                                                                                               |
| async_tree_io_tg                 | 505 ms                                                                                                          | 492 ms: 1.03x faster                                                                                                |
| xml_etree_parse                  | 111 ms                                                                                                          | 109 ms: 1.02x faster                                                                                                |
| pickle_pure_python               | 182 us                                                                                                          | 179 us: 1.02x faster                                                                                                |
| logging_format                   | 3.40 us                                                                                                         | 3.33 us: 1.02x faster                                                                                               |
| coverage                         | 45.4 ms                                                                                                         | 44.6 ms: 1.02x faster                                                                                               |
| json                             | 2.98 ms                                                                                                         | 2.92 ms: 1.02x faster                                                                                               |
| logging_simple                   | 3.07 us                                                                                                         | 3.02 us: 1.02x faster                                                                                               |
| bpe_tokeniser                    | 3.10 sec                                                                                                        | 3.07 sec: 1.01x faster                                                                                              |
| json_loads                       | 17.3 us                                                                                                         | 17.2 us: 1.01x faster                                                                                               |
| deepcopy_reduce                  | 1.51 us                                                                                                         | 1.51 us: 1.01x faster                                                                                               |
| coroutines                       | 16.2 ms                                                                                                         | 16.1 ms: 1.00x faster                                                                                               |
| regex_dna                        | 145 ms                                                                                                          | 145 ms: 1.00x faster                                                                                                |
| regex_effbot                     | 2.47 ms                                                                                                         | 2.46 ms: 1.00x faster                                                                                               |
| async_tree_eager_cpu_io_mixed_tg | 336 ms                                                                                                          | 338 ms: 1.00x slower                                                                                                |
| thrift                           | 432 us                                                                                                          | 434 us: 1.01x slower                                                                                                |
| pathlib                          | 23.4 ms                                                                                                         | 23.5 ms: 1.01x slower                                                                                               |
| asyncio_tcp_ssl                  | 1.28 sec                                                                                                        | 1.29 sec: 1.01x slower                                                                                              |
| regex_v8                         | 16.6 ms                                                                                                         | 16.9 ms: 1.01x slower                                                                                               |
| telco                            | 4.58 ms                                                                                                         | 4.64 ms: 1.01x slower                                                                                               |
| fannkuch                         | 265 ms                                                                                                          | 269 ms: 1.02x slower                                                                                                |
| pyflate                          | 321 ms                                                                                                          | 327 ms: 1.02x slower                                                                                                |
| json_dumps                       | 6.38 ms                                                                                                         | 6.50 ms: 1.02x slower                                                                                               |
| async_tree_eager_cpu_io_mixed    | 360 ms                                                                                                          | 367 ms: 1.02x slower                                                                                                |
| logging_silent                   | 60.4 ns                                                                                                         | 62.1 ns: 1.03x slower                                                                                               |
| crypto_pyaes                     | 50.7 ms                                                                                                         | 52.1 ms: 1.03x slower                                                                                               |
| typing_runtime_protocols         | 93.2 us                                                                                                         | 95.8 us: 1.03x slower                                                                                               |
| async_tree_none                  | 192 ms                                                                                                          | 197 ms: 1.03x slower                                                                                                |
| async_tree_eager_memoization     | 151 ms                                                                                                          | 155 ms: 1.03x slower                                                                                                |
| spectral_norm                    | 67.2 ms                                                                                                         | 69.7 ms: 1.04x slower                                                                                               |
| meteor_contest                   | 71.9 ms                                                                                                         | 74.6 ms: 1.04x slower                                                                                               |
| python_startup                   | 13.8 ms                                                                                                         | 14.3 ms: 1.04x slower                                                                                               |
| bench_thread_pool                | 450 us                                                                                                          | 469 us: 1.04x slower                                                                                                |
| async_tree_eager                 | 62.0 ms                                                                                                         | 64.8 ms: 1.04x slower                                                                                               |
| scimark_fft                      | 185 ms                                                                                                          | 194 ms: 1.05x slower                                                                                                |
| dulwich_log                      | 26.9 ms                                                                                                         | 28.2 ms: 1.05x slower                                                                                               |
| nbody                            | 60.8 ms                                                                                                         | 63.8 ms: 1.05x slower                                                                                               |
| async_generators                 | 282 ms                                                                                                          | 297 ms: 1.05x slower                                                                                                |
| go                               | 96.6 ms                                                                                                         | 102 ms: 1.05x slower                                                                                                |
| bench_mp_pool                    | 46.5 ms                                                                                                         | 49.1 ms: 1.06x slower                                                                                               |
| python_startup_no_site           | 10.9 ms                                                                                                         | 11.6 ms: 1.06x slower                                                                                               |
| deepcopy                         | 146 us                                                                                                          | 155 us: 1.06x slower                                                                                                |
| asyncio_tcp                      | 413 ms                                                                                                          | 448 ms: 1.08x slower                                                                                                |
| pycparser                        | 638 ms                                                                                                          | 695 ms: 1.09x slower                                                                                                |
| deltablue                        | 2.11 ms                                                                                                         | 2.32 ms: 1.10x slower                                                                                               |
| html5lib                         | 31.4 ms                                                                                                         | 34.5 ms: 1.10x slower                                                                                               |
| pprint_safe_repr                 | 466 ms                                                                                                          | 512 ms: 1.10x slower                                                                                                |
| scimark_sparse_mat_mult          | 2.81 ms                                                                                                         | 3.08 ms: 1.10x slower                                                                                               |
| sympy_sum                        | 70.4 ms                                                                                                         | 77.3 ms: 1.10x slower                                                                                               |
| sympy_str                        | 134 ms                                                                                                          | 147 ms: 1.10x slower                                                                                                |
| regex_compile                    | 68.0 ms                                                                                                         | 74.8 ms: 1.10x slower                                                                                               |
| sqlglot_normalize                | 168 ms                                                                                                          | 185 ms: 1.10x slower                                                                                                |
| scimark_monte_carlo              | 43.5 ms                                                                                                         | 48.0 ms: 1.10x slower                                                                                               |
| sympy_expand                     | 228 ms                                                                                                          | 252 ms: 1.10x slower                                                                                                |
| pprint_pformat                   | 952 ms                                                                                                          | 1.05 sec: 1.10x slower                                                                                              |
| docutils                         | 1.47 sec                                                                                                        | 1.62 sec: 1.11x slower                                                                                              |
| nqueens                          | 53.3 ms                                                                                                         | 59.2 ms: 1.11x slower                                                                                               |
| 2to3                             | 162 ms                                                                                                          | 179 ms: 1.11x slower                                                                                                |
| raytrace                         | 147 ms                                                                                                          | 164 ms: 1.11x slower                                                                                                |
| chaos                            | 35.8 ms                                                                                                         | 40.1 ms: 1.12x slower                                                                                               |
| pylint                           | 181 ms                                                                                                          | 205 ms: 1.14x slower                                                                                                |
| sympy_integrate                  | 10.5 ms                                                                                                         | 11.9 ms: 1.14x slower                                                                                               |
| sqlglot_parse                    | 744 us                                                                                                          | 856 us: 1.15x slower                                                                                                |
| sqlglot_optimize                 | 31.3 ms                                                                                                         | 36.0 ms: 1.15x slower                                                                                               |
| hexiom                           | 4.10 ms                                                                                                         | 4.72 ms: 1.15x slower                                                                                               |
| sqlglot_transpile                | 902 us                                                                                                          | 1.05 ms: 1.17x slower                                                                                               |
| django_template                  | 19.6 ms                                                                                                         | 23.0 ms: 1.17x slower                                                                                               |
| genshi_text                      | 14.1 ms                                                                                                         | 17.0 ms: 1.20x slower                                                                                               |
| generators                       | 20.3 ms                                                                                                         | 24.5 ms: 1.20x slower                                                                                               |
| comprehensions                   | 10.0 us                                                                                                         | 12.7 us: 1.26x slower                                                                                               |
| genshi_xml                       | 30.4 ms                                                                                                         | 42.1 ms: 1.39x slower                                                                                               |
| richards_super                   | 33.3 ms                                                                                                         | 48.1 ms: 1.44x slower                                                                                               |
| richards                         | 30.3 ms                                                                                                         | 45.9 ms: 1.52x slower                                                                                               |
| Geometric mean                   | (ref)                                                                                                           | 1.05x slower                                                                                                        |

Benchmark hidden because not significant (15): tornado_http, create_gc_cycles, pidigits, asyncio_websockets, async_tree_eager_tg, async_tree_none_tg, gc_traversal, async_tree_memoization, async_tree_memoization_tg, async_tree_cpu_io_mixed, async_tree_io, async_tree_eager_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 1.00x