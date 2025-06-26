# Results vs. 3.12.0

- fork: faster-cpython
- ref: explicit_check_perio
- machine: darwin-arm64
- commit hash: 892a89d
- commit date: 2025-06-26
- overall geometric mean: 1.111x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250626-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 168 ms                                                 | 163 ms: 1.04x faster                                                            |
| docutils       | 1.45 sec                                               | 1.41 sec: 1.03x faster                                                          |
| html5lib       | 33.4 ms                                                | 29.4 ms: 1.14x faster                                                           |
| sphinx         | 613 ms                                                 | 568 ms: 1.08x faster                                                            |
| Geometric mean | (ref)                                                  | 1.07x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250626-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|----------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_eager_io              | 666 ms                                                 | 347 ms: 1.92x faster                                                            |
| async_tree_io_tg                 | 673 ms                                                 | 364 ms: 1.85x faster                                                            |
| async_tree_io                    | 672 ms                                                 | 365 ms: 1.84x faster                                                            |
| async_tree_eager_io_tg           | 617 ms                                                 | 362 ms: 1.71x faster                                                            |
| async_tree_memoization_tg        | 318 ms                                                 | 187 ms: 1.71x faster                                                            |
| async_tree_none_tg               | 255 ms                                                 | 151 ms: 1.69x faster                                                            |
| async_tree_none                  | 263 ms                                                 | 157 ms: 1.68x faster                                                            |
| async_tree_memoization           | 310 ms                                                 | 185 ms: 1.67x faster                                                            |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 407 ms: 1.30x faster                                                            |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 409 ms: 1.29x faster                                                            |
| coroutines                       | 19.7 ms                                                | 16.0 ms: 1.23x faster                                                           |
| async_tree_eager_memoization     | 168 ms                                                 | 137 ms: 1.23x faster                                                            |
| async_generators                 | 299 ms                                                 | 259 ms: 1.15x faster                                                            |
| async_tree_eager                 | 65.8 ms                                                | 60.5 ms: 1.09x faster                                                           |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 354 ms: 1.06x faster                                                            |
| asyncio_websockets               | 243 ms                                                 | 242 ms: 1.00x faster                                                            |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 386 ms: 1.11x slower                                                            |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 163 ms: 1.15x slower                                                            |
| async_tree_eager_tg              | 46.9 ms                                                | 125 ms: 2.66x slower                                                            |
| Geometric mean                   | (ref)                                                  | 1.27x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250626-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 54.1 ms                                                | 47.0 ms: 1.15x faster                                                           |
| pidigits       | 283 ms                                                 | 283 ms: 1.00x slower                                                            |
| nbody          | 67.6 ms                                                | 68.6 ms: 1.02x slower                                                           |
| Geometric mean | (ref)                                                  | 1.04x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250626-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 75.9 ms                                                | 65.9 ms: 1.15x faster                                                           |
| regex_effbot   | 2.44 ms                                                | 2.34 ms: 1.04x faster                                                           |
| regex_v8       | 15.1 ms                                                | 16.0 ms: 1.06x slower                                                           |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                    |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250626-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 1.36 sec                                               | 1.19 sec: 1.14x faster                                                          |
| xml_etree_iterparse  | 75.5 ms                                                | 70.7 ms: 1.07x faster                                                           |
| xml_etree_generate   | 55.4 ms                                                | 51.9 ms: 1.07x faster                                                           |
| xml_etree_parse      | 108 ms                                                 | 103 ms: 1.05x faster                                                            |
| json_loads           | 17.0 us                                                | 16.3 us: 1.04x faster                                                           |
| xml_etree_process    | 38.9 ms                                                | 37.3 ms: 1.04x faster                                                           |
| unpickle_pure_python | 145 us                                                 | 144 us: 1.01x faster                                                            |
| pickle_pure_python   | 197 us                                                 | 203 us: 1.03x slower                                                            |
| json_dumps           | 6.19 ms                                                | 6.39 ms: 1.03x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250626-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 13.2 ms                                                | 11.7 ms: 1.13x faster                                                           |
| python_startup         | 17.8 ms                                                | 16.0 ms: 1.11x faster                                                           |
| Geometric mean         | (ref)                                                  | 1.12x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250626-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_text     | 14.7 ms                                                | 13.4 ms: 1.10x faster                                                           |
| genshi_xml      | 30.5 ms                                                | 28.6 ms: 1.07x faster                                                           |
| mako            | 7.44 ms                                                | 7.64 ms: 1.03x slower                                                           |
| django_template | 19.7 ms                                                | 20.9 ms: 1.06x slower                                                           |
| Geometric mean  | (ref)                                                  | 1.02x faster                                                                    |

All benchmarks:
===============

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250626-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|----------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| subparsers                       | 32.1 ms                                                | 13.1 ms: 2.45x faster                                                           |
| mdp                              | 1.49 sec                                               | 725 ms: 2.06x faster                                                            |
| async_tree_eager_io              | 666 ms                                                 | 347 ms: 1.92x faster                                                            |
| async_tree_io_tg                 | 673 ms                                                 | 364 ms: 1.85x faster                                                            |
| async_tree_io                    | 672 ms                                                 | 365 ms: 1.84x faster                                                            |
| async_tree_eager_io_tg           | 617 ms                                                 | 362 ms: 1.71x faster                                                            |
| async_tree_memoization_tg        | 318 ms                                                 | 187 ms: 1.71x faster                                                            |
| async_tree_none_tg               | 255 ms                                                 | 151 ms: 1.69x faster                                                            |
| async_tree_none                  | 263 ms                                                 | 157 ms: 1.68x faster                                                            |
| async_tree_memoization           | 310 ms                                                 | 185 ms: 1.67x faster                                                            |
| deepcopy                         | 226 us                                                 | 149 us: 1.52x faster                                                            |
| deepcopy_memo                    | 26.0 us                                                | 17.8 us: 1.46x faster                                                           |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 407 ms: 1.30x faster                                                            |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 409 ms: 1.29x faster                                                            |
| comprehensions                   | 14.0 us                                                | 10.9 us: 1.29x faster                                                           |
| go                               | 98.5 ms                                                | 77.1 ms: 1.28x faster                                                           |
| generators                       | 29.4 ms                                                | 23.2 ms: 1.26x faster                                                           |
| deepcopy_reduce                  | 2.01 us                                                | 1.62 us: 1.25x faster                                                           |
| coroutines                       | 19.7 ms                                                | 16.0 ms: 1.23x faster                                                           |
| async_tree_eager_memoization     | 168 ms                                                 | 137 ms: 1.23x faster                                                            |
| dulwich_log                      | 29.2 ms                                                | 24.1 ms: 1.21x faster                                                           |
| raytrace                         | 204 ms                                                 | 169 ms: 1.20x faster                                                            |
| k_core                           | 1.72 sec                                               | 1.44 sec: 1.19x faster                                                          |
| spectral_norm                    | 76.5 ms                                                | 64.7 ms: 1.18x faster                                                           |
| pylint                           | 182 ms                                                 | 157 ms: 1.16x faster                                                            |
| async_generators                 | 299 ms                                                 | 259 ms: 1.15x faster                                                            |
| float                            | 54.1 ms                                                | 47.0 ms: 1.15x faster                                                           |
| regex_compile                    | 75.9 ms                                                | 65.9 ms: 1.15x faster                                                           |
| tomli_loads                      | 1.36 sec                                               | 1.19 sec: 1.14x faster                                                          |
| html5lib                         | 33.4 ms                                                | 29.4 ms: 1.14x faster                                                           |
| python_startup_no_site           | 13.2 ms                                                | 11.7 ms: 1.13x faster                                                           |
| scimark_sor                      | 85.8 ms                                                | 76.1 ms: 1.13x faster                                                           |
| chaos                            | 41.6 ms                                                | 37.1 ms: 1.12x faster                                                           |
| bpe_tokeniser                    | 3.28 sec                                               | 2.93 sec: 1.12x faster                                                          |
| pathlib                          | 24.7 ms                                                | 22.3 ms: 1.11x faster                                                           |
| python_startup                   | 17.8 ms                                                | 16.0 ms: 1.11x faster                                                           |
| deltablue                        | 2.57 ms                                                | 2.34 ms: 1.10x faster                                                           |
| genshi_text                      | 14.7 ms                                                | 13.4 ms: 1.10x faster                                                           |
| pyflate                          | 311 ms                                                 | 284 ms: 1.09x faster                                                            |
| async_tree_eager                 | 65.8 ms                                                | 60.5 ms: 1.09x faster                                                           |
| scimark_fft                      | 194 ms                                                 | 179 ms: 1.09x faster                                                            |
| sphinx                           | 613 ms                                                 | 568 ms: 1.08x faster                                                            |
| thrift                           | 468 us                                                 | 435 us: 1.08x faster                                                            |
| xml_etree_iterparse              | 75.5 ms                                                | 70.7 ms: 1.07x faster                                                           |
| xml_etree_generate               | 55.4 ms                                                | 51.9 ms: 1.07x faster                                                           |
| genshi_xml                       | 30.5 ms                                                | 28.6 ms: 1.07x faster                                                           |
| sympy_integrate                  | 11.1 ms                                                | 10.5 ms: 1.06x faster                                                           |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 354 ms: 1.06x faster                                                            |
| hexiom                           | 4.38 ms                                                | 4.15 ms: 1.05x faster                                                           |
| sympy_str                        | 144 ms                                                 | 137 ms: 1.05x faster                                                            |
| scimark_monte_carlo              | 44.5 ms                                                | 42.3 ms: 1.05x faster                                                           |
| xml_etree_parse                  | 108 ms                                                 | 103 ms: 1.05x faster                                                            |
| json                             | 3.00 ms                                                | 2.87 ms: 1.05x faster                                                           |
| sympy_sum                        | 76.2 ms                                                | 72.9 ms: 1.05x faster                                                           |
| regex_effbot                     | 2.44 ms                                                | 2.34 ms: 1.04x faster                                                           |
| nqueens                          | 59.5 ms                                                | 57.0 ms: 1.04x faster                                                           |
| json_loads                       | 17.0 us                                                | 16.3 us: 1.04x faster                                                           |
| xml_etree_process                | 38.9 ms                                                | 37.3 ms: 1.04x faster                                                           |
| fannkuch                         | 250 ms                                                 | 241 ms: 1.04x faster                                                            |
| pycparser                        | 673 ms                                                 | 648 ms: 1.04x faster                                                            |
| logging_simple                   | 3.60 us                                                | 3.47 us: 1.04x faster                                                           |
| 2to3                             | 168 ms                                                 | 163 ms: 1.04x faster                                                            |
| shortest_path                    | 331 ms                                                 | 320 ms: 1.03x faster                                                            |
| logging_format                   | 3.90 us                                                | 3.78 us: 1.03x faster                                                           |
| docutils                         | 1.45 sec                                               | 1.41 sec: 1.03x faster                                                          |
| scimark_sparse_mat_mult          | 3.14 ms                                                | 3.09 ms: 1.02x faster                                                           |
| dask                             | 779 ms                                                 | 765 ms: 1.02x faster                                                            |
| connected_components             | 300 ms                                                 | 295 ms: 1.02x faster                                                            |
| unpickle_pure_python             | 145 us                                                 | 144 us: 1.01x faster                                                            |
| sympy_expand                     | 233 ms                                                 | 231 ms: 1.01x faster                                                            |
| asyncio_websockets               | 243 ms                                                 | 242 ms: 1.00x faster                                                            |
| pidigits                         | 283 ms                                                 | 283 ms: 1.00x slower                                                            |
| meteor_contest                   | 69.1 ms                                                | 69.7 ms: 1.01x slower                                                           |
| scimark_lu                       | 73.5 ms                                                | 74.4 ms: 1.01x slower                                                           |
| nbody                            | 67.6 ms                                                | 68.6 ms: 1.02x slower                                                           |
| richards_super                   | 34.6 ms                                                | 35.5 ms: 1.03x slower                                                           |
| mako                             | 7.44 ms                                                | 7.64 ms: 1.03x slower                                                           |
| sqlite_synth                     | 1.55 us                                                | 1.59 us: 1.03x slower                                                           |
| pickle_pure_python               | 197 us                                                 | 203 us: 1.03x slower                                                            |
| json_dumps                       | 6.19 ms                                                | 6.39 ms: 1.03x slower                                                           |
| crypto_pyaes                     | 51.4 ms                                                | 54.2 ms: 1.05x slower                                                           |
| richards                         | 30.6 ms                                                | 32.3 ms: 1.06x slower                                                           |
| regex_v8                         | 15.1 ms                                                | 16.0 ms: 1.06x slower                                                           |
| django_template                  | 19.7 ms                                                | 20.9 ms: 1.06x slower                                                           |
| gc_traversal                     | 2.95 ms                                                | 3.18 ms: 1.08x slower                                                           |
| pprint_pformat                   | 986 ms                                                 | 1.07 sec: 1.09x slower                                                          |
| pprint_safe_repr                 | 483 ms                                                 | 528 ms: 1.09x slower                                                            |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 386 ms: 1.11x slower                                                            |
| many_optionals                   | 403 us                                                 | 452 us: 1.12x slower                                                            |
| telco                            | 3.92 ms                                                | 4.42 ms: 1.13x slower                                                           |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 163 ms: 1.15x slower                                                            |
| create_gc_cycles                 | 1.15 ms                                                | 1.36 ms: 1.18x slower                                                           |
| coverage                         | 38.5 ms                                                | 47.5 ms: 1.23x slower                                                           |
| async_tree_eager_tg              | 46.9 ms                                                | 125 ms: 2.66x slower                                                            |
| logging_silent                   | 72.5 ns                                                | 321 ns: 4.43x slower                                                            |
| Geometric mean                   | (ref)                                                  | 1.09x faster                                                                    |

Benchmark hidden because not significant (2): typing_runtime_protocols, regex_dna
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250626-3.15.0a0-892a89d/bm-20250626-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.111x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.12x