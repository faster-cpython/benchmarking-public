# Results vs. 3.12.0

- fork: brandtbucher
- ref: jit_targets
- machine: darwin-arm64
- commit hash: 997a858
- commit date: 2025-07-08
- overall geometric mean: 1.076x faster
- HPT reliability: 99.85%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.14x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250708-darwin-arm64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 168 ms                                                 | 169 ms: 1.01x slower                                               |
| docutils       | 1.45 sec                                               | 1.44 sec: 1.01x faster                                             |
| html5lib       | 33.4 ms                                                | 32.5 ms: 1.03x faster                                              |
| sphinx         | 613 ms                                                 | 581 ms: 1.05x faster                                               |
| Geometric mean | (ref)                                                  | 1.02x faster                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250708-darwin-arm64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|----------------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_eager_io              | 666 ms                                                 | 358 ms: 1.86x faster                                               |
| async_tree_io                    | 672 ms                                                 | 370 ms: 1.82x faster                                               |
| async_tree_io_tg                 | 673 ms                                                 | 375 ms: 1.79x faster                                               |
| async_tree_eager_io_tg           | 617 ms                                                 | 370 ms: 1.67x faster                                               |
| async_tree_memoization_tg        | 318 ms                                                 | 191 ms: 1.66x faster                                               |
| async_tree_none_tg               | 255 ms                                                 | 155 ms: 1.65x faster                                               |
| async_tree_none                  | 263 ms                                                 | 161 ms: 1.64x faster                                               |
| async_tree_memoization           | 310 ms                                                 | 192 ms: 1.62x faster                                               |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 410 ms: 1.29x faster                                               |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 415 ms: 1.27x faster                                               |
| async_tree_eager_memoization     | 168 ms                                                 | 139 ms: 1.20x faster                                               |
| coroutines                       | 19.7 ms                                                | 17.1 ms: 1.15x faster                                              |
| async_generators                 | 299 ms                                                 | 280 ms: 1.07x faster                                               |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 357 ms: 1.05x faster                                               |
| async_tree_eager                 | 65.8 ms                                                | 62.9 ms: 1.05x faster                                              |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 390 ms: 1.12x slower                                               |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 167 ms: 1.18x slower                                               |
| async_tree_eager_tg              | 46.9 ms                                                | 128 ms: 2.73x slower                                               |
| Geometric mean                   | (ref)                                                  | 1.23x faster                                                       |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250708-darwin-arm64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| float          | 54.1 ms                                                | 49.9 ms: 1.08x faster                                              |
| pidigits       | 283 ms                                                 | 284 ms: 1.00x slower                                               |
| nbody          | 67.6 ms                                                | 72.0 ms: 1.07x slower                                              |
| Geometric mean | (ref)                                                  | 1.00x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250708-darwin-arm64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_compile  | 75.9 ms                                                | 70.6 ms: 1.08x faster                                              |
| regex_effbot   | 2.44 ms                                                | 2.35 ms: 1.04x faster                                              |
| regex_dna      | 143 ms                                                 | 144 ms: 1.01x slower                                               |
| regex_v8       | 15.1 ms                                                | 16.0 ms: 1.06x slower                                              |
| Geometric mean | (ref)                                                  | 1.01x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250708-darwin-arm64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| tomli_loads          | 1.36 sec                                               | 1.19 sec: 1.14x faster                                             |
| unpickle_pure_python | 145 us                                                 | 129 us: 1.13x faster                                               |
| xml_etree_process    | 38.9 ms                                                | 34.8 ms: 1.12x faster                                              |
| xml_etree_generate   | 55.4 ms                                                | 49.6 ms: 1.12x faster                                              |
| xml_etree_parse      | 108 ms                                                 | 102 ms: 1.06x faster                                               |
| xml_etree_iterparse  | 75.5 ms                                                | 72.0 ms: 1.05x faster                                              |
| json_loads           | 17.0 us                                                | 16.5 us: 1.03x faster                                              |
| pickle_pure_python   | 197 us                                                 | 205 us: 1.04x slower                                               |
| json_dumps           | 6.19 ms                                                | 6.65 ms: 1.07x slower                                              |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250708-darwin-arm64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup         | 17.8 ms                                                | 20.5 ms: 1.15x slower                                              |
| python_startup_no_site | 13.2 ms                                                | 15.9 ms: 1.21x slower                                              |
| Geometric mean         | (ref)                                                  | 1.18x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250708-darwin-arm64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| mako            | 7.44 ms                                                | 6.64 ms: 1.12x faster                                              |
| genshi_text     | 14.7 ms                                                | 14.9 ms: 1.01x slower                                              |
| genshi_xml      | 30.5 ms                                                | 31.2 ms: 1.02x slower                                              |
| django_template | 19.7 ms                                                | 21.7 ms: 1.10x slower                                              |
| Geometric mean  | (ref)                                                  | 1.00x slower                                                       |

All benchmarks:
===============

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250708-darwin-arm64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|----------------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| subparsers                       | 32.1 ms                                                | 13.7 ms: 2.35x faster                                              |
| mdp                              | 1.49 sec                                               | 754 ms: 1.98x faster                                               |
| async_tree_eager_io              | 666 ms                                                 | 358 ms: 1.86x faster                                               |
| async_tree_io                    | 672 ms                                                 | 370 ms: 1.82x faster                                               |
| async_tree_io_tg                 | 673 ms                                                 | 375 ms: 1.79x faster                                               |
| async_tree_eager_io_tg           | 617 ms                                                 | 370 ms: 1.67x faster                                               |
| async_tree_memoization_tg        | 318 ms                                                 | 191 ms: 1.66x faster                                               |
| async_tree_none_tg               | 255 ms                                                 | 155 ms: 1.65x faster                                               |
| async_tree_none                  | 263 ms                                                 | 161 ms: 1.64x faster                                               |
| async_tree_memoization           | 310 ms                                                 | 192 ms: 1.62x faster                                               |
| deepcopy                         | 226 us                                                 | 156 us: 1.45x faster                                               |
| deepcopy_memo                    | 26.0 us                                                | 19.5 us: 1.33x faster                                              |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 410 ms: 1.29x faster                                               |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 415 ms: 1.27x faster                                               |
| comprehensions                   | 14.0 us                                                | 11.3 us: 1.24x faster                                              |
| generators                       | 29.4 ms                                                | 24.1 ms: 1.22x faster                                              |
| deepcopy_reduce                  | 2.01 us                                                | 1.67 us: 1.21x faster                                              |
| async_tree_eager_memoization     | 168 ms                                                 | 139 ms: 1.20x faster                                               |
| spectral_norm                    | 76.5 ms                                                | 64.1 ms: 1.19x faster                                              |
| dulwich_log                      | 29.2 ms                                                | 25.1 ms: 1.16x faster                                              |
| coroutines                       | 19.7 ms                                                | 17.1 ms: 1.15x faster                                              |
| raytrace                         | 204 ms                                                 | 178 ms: 1.14x faster                                               |
| go                               | 98.5 ms                                                | 86.1 ms: 1.14x faster                                              |
| tomli_loads                      | 1.36 sec                                               | 1.19 sec: 1.14x faster                                             |
| k_core                           | 1.72 sec                                               | 1.51 sec: 1.14x faster                                             |
| unpickle_pure_python             | 145 us                                                 | 129 us: 1.13x faster                                               |
| pylint                           | 182 ms                                                 | 161 ms: 1.13x faster                                               |
| mako                             | 7.44 ms                                                | 6.64 ms: 1.12x faster                                              |
| xml_etree_process                | 38.9 ms                                                | 34.8 ms: 1.12x faster                                              |
| xml_etree_generate               | 55.4 ms                                                | 49.6 ms: 1.12x faster                                              |
| bpe_tokeniser                    | 3.28 sec                                               | 2.94 sec: 1.12x faster                                             |
| pathlib                          | 24.7 ms                                                | 22.2 ms: 1.11x faster                                              |
| pyflate                          | 311 ms                                                 | 283 ms: 1.10x faster                                               |
| pprint_pformat                   | 986 ms                                                 | 901 ms: 1.09x faster                                               |
| float                            | 54.1 ms                                                | 49.9 ms: 1.08x faster                                              |
| pprint_safe_repr                 | 483 ms                                                 | 446 ms: 1.08x faster                                               |
| regex_compile                    | 75.9 ms                                                | 70.6 ms: 1.08x faster                                              |
| async_generators                 | 299 ms                                                 | 280 ms: 1.07x faster                                               |
| chaos                            | 41.6 ms                                                | 39.1 ms: 1.06x faster                                              |
| thrift                           | 468 us                                                 | 440 us: 1.06x faster                                               |
| xml_etree_parse                  | 108 ms                                                 | 102 ms: 1.06x faster                                               |
| sphinx                           | 613 ms                                                 | 581 ms: 1.05x faster                                               |
| logging_simple                   | 3.60 us                                                | 3.43 us: 1.05x faster                                              |
| xml_etree_iterparse              | 75.5 ms                                                | 72.0 ms: 1.05x faster                                              |
| logging_format                   | 3.90 us                                                | 3.72 us: 1.05x faster                                              |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 357 ms: 1.05x faster                                               |
| async_tree_eager                 | 65.8 ms                                                | 62.9 ms: 1.05x faster                                              |
| json                             | 3.00 ms                                                | 2.89 ms: 1.04x faster                                              |
| regex_effbot                     | 2.44 ms                                                | 2.35 ms: 1.04x faster                                              |
| json_loads                       | 17.0 us                                                | 16.5 us: 1.03x faster                                              |
| html5lib                         | 33.4 ms                                                | 32.5 ms: 1.03x faster                                              |
| scimark_fft                      | 194 ms                                                 | 190 ms: 1.02x faster                                               |
| sympy_sum                        | 76.2 ms                                                | 74.8 ms: 1.02x faster                                              |
| dask                             | 779 ms                                                 | 766 ms: 1.02x faster                                               |
| docutils                         | 1.45 sec                                               | 1.44 sec: 1.01x faster                                             |
| sympy_integrate                  | 11.1 ms                                                | 11.0 ms: 1.01x faster                                              |
| sympy_str                        | 144 ms                                                 | 143 ms: 1.01x faster                                               |
| logging_silent                   | 72.5 ns                                                | 72.2 ns: 1.00x faster                                              |
| pidigits                         | 283 ms                                                 | 284 ms: 1.00x slower                                               |
| 2to3                             | 168 ms                                                 | 169 ms: 1.01x slower                                               |
| regex_dna                        | 143 ms                                                 | 144 ms: 1.01x slower                                               |
| sqlite_synth                     | 1.55 us                                                | 1.56 us: 1.01x slower                                              |
| deltablue                        | 2.57 ms                                                | 2.60 ms: 1.01x slower                                              |
| genshi_text                      | 14.7 ms                                                | 14.9 ms: 1.01x slower                                              |
| shortest_path                    | 331 ms                                                 | 337 ms: 1.02x slower                                               |
| hexiom                           | 4.38 ms                                                | 4.47 ms: 1.02x slower                                              |
| genshi_xml                       | 30.5 ms                                                | 31.2 ms: 1.02x slower                                              |
| typing_runtime_protocols         | 91.5 us                                                | 93.8 us: 1.02x slower                                              |
| fannkuch                         | 250 ms                                                 | 257 ms: 1.03x slower                                               |
| connected_components             | 300 ms                                                 | 308 ms: 1.03x slower                                               |
| scimark_monte_carlo              | 44.5 ms                                                | 45.9 ms: 1.03x slower                                              |
| nqueens                          | 59.5 ms                                                | 61.7 ms: 1.04x slower                                              |
| sympy_expand                     | 233 ms                                                 | 242 ms: 1.04x slower                                               |
| meteor_contest                   | 69.1 ms                                                | 71.6 ms: 1.04x slower                                              |
| pickle_pure_python               | 197 us                                                 | 205 us: 1.04x slower                                               |
| scimark_sor                      | 85.8 ms                                                | 89.2 ms: 1.04x slower                                              |
| crypto_pyaes                     | 51.4 ms                                                | 53.9 ms: 1.05x slower                                              |
| regex_v8                         | 15.1 ms                                                | 16.0 ms: 1.06x slower                                              |
| scimark_sparse_mat_mult          | 3.14 ms                                                | 3.35 ms: 1.07x slower                                              |
| nbody                            | 67.6 ms                                                | 72.0 ms: 1.07x slower                                              |
| json_dumps                       | 6.19 ms                                                | 6.65 ms: 1.07x slower                                              |
| gc_traversal                     | 2.95 ms                                                | 3.19 ms: 1.08x slower                                              |
| django_template                  | 19.7 ms                                                | 21.7 ms: 1.10x slower                                              |
| scimark_lu                       | 73.5 ms                                                | 82.1 ms: 1.12x slower                                              |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 390 ms: 1.12x slower                                               |
| telco                            | 3.92 ms                                                | 4.41 ms: 1.12x slower                                              |
| richards_super                   | 34.6 ms                                                | 39.3 ms: 1.14x slower                                              |
| richards                         | 30.6 ms                                                | 35.2 ms: 1.15x slower                                              |
| python_startup                   | 17.8 ms                                                | 20.5 ms: 1.15x slower                                              |
| many_optionals                   | 403 us                                                 | 470 us: 1.17x slower                                               |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 167 ms: 1.18x slower                                               |
| create_gc_cycles                 | 1.15 ms                                                | 1.37 ms: 1.19x slower                                              |
| python_startup_no_site           | 13.2 ms                                                | 15.9 ms: 1.21x slower                                              |
| coverage                         | 38.5 ms                                                | 48.4 ms: 1.26x slower                                              |
| async_tree_eager_tg              | 46.9 ms                                                | 128 ms: 2.73x slower                                               |
| Geometric mean                   | (ref)                                                  | 1.08x faster                                                       |

Benchmark hidden because not significant (2): asyncio_websockets, pycparser
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250708-3.15.0a0-997a858-JIT/bm-20250708-darwin-arm64-brandtbucher-jit_targets-3.15.0a0-997a858.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.076x faster

# HPT report

- Reliability score: 99.85% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.14x