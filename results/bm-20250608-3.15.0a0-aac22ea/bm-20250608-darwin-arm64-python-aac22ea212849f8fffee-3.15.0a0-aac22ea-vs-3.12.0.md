# Results vs. 3.12.0

- fork: python
- ref: aac22ea212849f8fffee
- machine: darwin-arm64
- commit hash: aac22ea
- commit date: 2025-06-08
- overall geometric mean: 1.044x slower
- HPT reliability: 65.03%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250608-darwin-arm64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 168 ms                                                 | 265 ms: 1.57x slower                                                  |
| docutils       | 1.45 sec                                               | 1.52 sec: 1.04x slower                                                |
| html5lib       | 33.4 ms                                                | 31.5 ms: 1.06x faster                                                 |
| sphinx         | 613 ms                                                 | 590 ms: 1.04x faster                                                  |
| Geometric mean | (ref)                                                  | 1.11x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250608-darwin-arm64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager_io              | 666 ms                                                 | 363 ms: 1.83x faster                                                  |
| async_tree_io_tg                 | 673 ms                                                 | 376 ms: 1.79x faster                                                  |
| async_tree_io                    | 672 ms                                                 | 378 ms: 1.78x faster                                                  |
| async_tree_eager_io_tg           | 617 ms                                                 | 374 ms: 1.65x faster                                                  |
| async_tree_memoization_tg        | 318 ms                                                 | 193 ms: 1.65x faster                                                  |
| async_tree_none_tg               | 255 ms                                                 | 157 ms: 1.62x faster                                                  |
| async_tree_none                  | 263 ms                                                 | 164 ms: 1.60x faster                                                  |
| async_tree_memoization           | 310 ms                                                 | 196 ms: 1.59x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 411 ms: 1.28x faster                                                  |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 415 ms: 1.27x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 140 ms: 1.19x faster                                                  |
| coroutines                       | 19.7 ms                                                | 17.0 ms: 1.16x faster                                                 |
| async_generators                 | 299 ms                                                 | 264 ms: 1.13x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 357 ms: 1.05x faster                                                  |
| async_tree_eager                 | 65.8 ms                                                | 64.3 ms: 1.02x faster                                                 |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 390 ms: 1.12x slower                                                  |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 169 ms: 1.19x slower                                                  |
| async_tree_eager_tg              | 46.9 ms                                                | 130 ms: 2.76x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.23x faster                                                          |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250608-darwin-arm64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 54.1 ms                                                | 49.6 ms: 1.09x faster                                                 |
| nbody          | 67.6 ms                                                | 74.9 ms: 1.11x slower                                                 |
| Geometric mean | (ref)                                                  | 1.01x slower                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250608-darwin-arm64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 75.9 ms                                                | 71.9 ms: 1.06x faster                                                 |
| regex_effbot   | 2.44 ms                                                | 2.37 ms: 1.03x faster                                                 |
| regex_dna      | 143 ms                                                 | 143 ms: 1.00x slower                                                  |
| regex_v8       | 15.1 ms                                                | 16.2 ms: 1.07x slower                                                 |
| Geometric mean | (ref)                                                  | 1.00x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250608-darwin-arm64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_iterparse  | 75.5 ms                                                | 69.5 ms: 1.09x faster                                                 |
| xml_etree_parse      | 108 ms                                                 | 99.7 ms: 1.08x faster                                                 |
| json_loads           | 17.0 us                                                | 16.4 us: 1.04x faster                                                 |
| xml_etree_generate   | 55.4 ms                                                | 53.7 ms: 1.03x faster                                                 |
| json_dumps           | 6.19 ms                                                | 6.56 ms: 1.06x slower                                                 |
| unpickle_pure_python | 145 us                                                 | 161 us: 1.10x slower                                                  |
| pickle_pure_python   | 197 us                                                 | 218 us: 1.11x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.00x slower                                                          |

Benchmark hidden because not significant (2): xml_etree_process, tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250608-darwin-arm64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 13.2 ms                                                | 18.6 ms: 1.41x slower                                                 |
| python_startup         | 17.8 ms                                                | 28.0 ms: 1.58x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.49x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250608-darwin-arm64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_xml      | 30.5 ms                                                | 31.2 ms: 1.02x slower                                                 |
| mako            | 7.44 ms                                                | 7.83 ms: 1.05x slower                                                 |
| django_template | 19.7 ms                                                | 21.9 ms: 1.11x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.05x slower                                                          |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250608-darwin-arm64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| subparsers                       | 32.1 ms                                                | 13.7 ms: 2.35x faster                                                 |
| mdp                              | 1.49 sec                                               | 762 ms: 1.96x faster                                                  |
| async_tree_eager_io              | 666 ms                                                 | 363 ms: 1.83x faster                                                  |
| async_tree_io_tg                 | 673 ms                                                 | 376 ms: 1.79x faster                                                  |
| async_tree_io                    | 672 ms                                                 | 378 ms: 1.78x faster                                                  |
| async_tree_eager_io_tg           | 617 ms                                                 | 374 ms: 1.65x faster                                                  |
| async_tree_memoization_tg        | 318 ms                                                 | 193 ms: 1.65x faster                                                  |
| async_tree_none_tg               | 255 ms                                                 | 157 ms: 1.62x faster                                                  |
| async_tree_none                  | 263 ms                                                 | 164 ms: 1.60x faster                                                  |
| async_tree_memoization           | 310 ms                                                 | 196 ms: 1.59x faster                                                  |
| deepcopy                         | 226 us                                                 | 157 us: 1.44x faster                                                  |
| deepcopy_memo                    | 26.0 us                                                | 19.1 us: 1.36x faster                                                 |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 411 ms: 1.28x faster                                                  |
| pathlib                          | 24.7 ms                                                | 19.3 ms: 1.28x faster                                                 |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 415 ms: 1.27x faster                                                  |
| generators                       | 29.4 ms                                                | 24.1 ms: 1.22x faster                                                 |
| async_tree_eager_memoization     | 168 ms                                                 | 140 ms: 1.19x faster                                                  |
| deepcopy_reduce                  | 2.01 us                                                | 1.70 us: 1.19x faster                                                 |
| dulwich_log                      | 29.2 ms                                                | 24.9 ms: 1.17x faster                                                 |
| k_core                           | 1.72 sec                                               | 1.47 sec: 1.17x faster                                                |
| comprehensions                   | 14.0 us                                                | 12.0 us: 1.17x faster                                                 |
| coroutines                       | 19.7 ms                                                | 17.0 ms: 1.16x faster                                                 |
| raytrace                         | 204 ms                                                 | 180 ms: 1.13x faster                                                  |
| async_generators                 | 299 ms                                                 | 264 ms: 1.13x faster                                                  |
| go                               | 98.5 ms                                                | 87.5 ms: 1.13x faster                                                 |
| pylint                           | 182 ms                                                 | 163 ms: 1.11x faster                                                  |
| float                            | 54.1 ms                                                | 49.6 ms: 1.09x faster                                                 |
| xml_etree_iterparse              | 75.5 ms                                                | 69.5 ms: 1.09x faster                                                 |
| xml_etree_parse                  | 108 ms                                                 | 99.7 ms: 1.08x faster                                                 |
| spectral_norm                    | 76.5 ms                                                | 71.0 ms: 1.08x faster                                                 |
| bpe_tokeniser                    | 3.28 sec                                               | 3.08 sec: 1.06x faster                                                |
| html5lib                         | 33.4 ms                                                | 31.5 ms: 1.06x faster                                                 |
| regex_compile                    | 75.9 ms                                                | 71.9 ms: 1.06x faster                                                 |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 357 ms: 1.05x faster                                                  |
| json_loads                       | 17.0 us                                                | 16.4 us: 1.04x faster                                                 |
| sphinx                           | 613 ms                                                 | 590 ms: 1.04x faster                                                  |
| json                             | 3.00 ms                                                | 2.89 ms: 1.04x faster                                                 |
| chaos                            | 41.6 ms                                                | 40.3 ms: 1.03x faster                                                 |
| xml_etree_generate               | 55.4 ms                                                | 53.7 ms: 1.03x faster                                                 |
| regex_effbot                     | 2.44 ms                                                | 2.37 ms: 1.03x faster                                                 |
| async_tree_eager                 | 65.8 ms                                                | 64.3 ms: 1.02x faster                                                 |
| sympy_sum                        | 76.2 ms                                                | 75.8 ms: 1.01x faster                                                 |
| sympy_str                        | 144 ms                                                 | 143 ms: 1.01x faster                                                  |
| sympy_integrate                  | 11.1 ms                                                | 11.0 ms: 1.00x faster                                                 |
| regex_dna                        | 143 ms                                                 | 143 ms: 1.00x slower                                                  |
| deltablue                        | 2.57 ms                                                | 2.59 ms: 1.01x slower                                                 |
| scimark_fft                      | 194 ms                                                 | 196 ms: 1.01x slower                                                  |
| logging_simple                   | 3.60 us                                                | 3.67 us: 1.02x slower                                                 |
| genshi_xml                       | 30.5 ms                                                | 31.2 ms: 1.02x slower                                                 |
| connected_components             | 300 ms                                                 | 307 ms: 1.02x slower                                                  |
| pyflate                          | 311 ms                                                 | 318 ms: 1.02x slower                                                  |
| logging_format                   | 3.90 us                                                | 4.00 us: 1.03x slower                                                 |
| scimark_sparse_mat_mult          | 3.14 ms                                                | 3.23 ms: 1.03x slower                                                 |
| sympy_expand                     | 233 ms                                                 | 241 ms: 1.03x slower                                                  |
| sqlite_synth                     | 1.55 us                                                | 1.60 us: 1.04x slower                                                 |
| scimark_sor                      | 85.8 ms                                                | 88.9 ms: 1.04x slower                                                 |
| nqueens                          | 59.5 ms                                                | 61.8 ms: 1.04x slower                                                 |
| docutils                         | 1.45 sec                                               | 1.52 sec: 1.04x slower                                                |
| scimark_monte_carlo              | 44.5 ms                                                | 46.7 ms: 1.05x slower                                                 |
| mako                             | 7.44 ms                                                | 7.83 ms: 1.05x slower                                                 |
| typing_runtime_protocols         | 91.5 us                                                | 96.3 us: 1.05x slower                                                 |
| json_dumps                       | 6.19 ms                                                | 6.56 ms: 1.06x slower                                                 |
| dask                             | 779 ms                                                 | 827 ms: 1.06x slower                                                  |
| meteor_contest                   | 69.1 ms                                                | 73.7 ms: 1.07x slower                                                 |
| hexiom                           | 4.38 ms                                                | 4.67 ms: 1.07x slower                                                 |
| fannkuch                         | 250 ms                                                 | 267 ms: 1.07x slower                                                  |
| regex_v8                         | 15.1 ms                                                | 16.2 ms: 1.07x slower                                                 |
| gc_traversal                     | 2.95 ms                                                | 3.19 ms: 1.08x slower                                                 |
| unpickle_pure_python             | 145 us                                                 | 161 us: 1.10x slower                                                  |
| pickle_pure_python               | 197 us                                                 | 218 us: 1.11x slower                                                  |
| nbody                            | 67.6 ms                                                | 74.9 ms: 1.11x slower                                                 |
| django_template                  | 19.7 ms                                                | 21.9 ms: 1.11x slower                                                 |
| crypto_pyaes                     | 51.4 ms                                                | 57.3 ms: 1.11x slower                                                 |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 390 ms: 1.12x slower                                                  |
| scimark_lu                       | 73.5 ms                                                | 83.4 ms: 1.13x slower                                                 |
| pprint_pformat                   | 986 ms                                                 | 1.13 sec: 1.14x slower                                                |
| richards_super                   | 34.6 ms                                                | 39.7 ms: 1.15x slower                                                 |
| telco                            | 3.92 ms                                                | 4.51 ms: 1.15x slower                                                 |
| pprint_safe_repr                 | 483 ms                                                 | 557 ms: 1.15x slower                                                  |
| many_optionals                   | 403 us                                                 | 465 us: 1.16x slower                                                  |
| richards                         | 30.6 ms                                                | 35.9 ms: 1.17x slower                                                 |
| create_gc_cycles                 | 1.15 ms                                                | 1.36 ms: 1.18x slower                                                 |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 169 ms: 1.19x slower                                                  |
| python_startup_no_site           | 13.2 ms                                                | 18.6 ms: 1.41x slower                                                 |
| 2to3                             | 168 ms                                                 | 265 ms: 1.57x slower                                                  |
| python_startup                   | 17.8 ms                                                | 28.0 ms: 1.58x slower                                                 |
| async_tree_eager_tg              | 46.9 ms                                                | 130 ms: 2.76x slower                                                  |
| logging_silent                   | 72.5 ns                                                | 335 ns: 4.62x slower                                                  |
| coverage                         | 38.5 ms                                                | 290 ms: 7.52x slower                                                  |
| thrift                           | 468 us                                                 | 322 ms: 689.35x slower                                                |
| Geometric mean                   | (ref)                                                  | 1.06x slower                                                          |

Benchmark hidden because not significant (7): shortest_path, asyncio_websockets, pidigits, genshi_text, xml_etree_process, tomli_loads, pycparser
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250608-3.15.0a0-aac22ea/bm-20250608-darwin-arm64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.044x slower

# HPT report

- Reliability score: 65.03% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.11x