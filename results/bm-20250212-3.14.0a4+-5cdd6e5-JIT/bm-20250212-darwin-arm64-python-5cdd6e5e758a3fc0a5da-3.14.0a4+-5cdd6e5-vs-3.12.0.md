# Results vs. 3.12.0

- fork: python
- ref: 5cdd6e5e758a3fc0a5da
- machine: darwin-arm64
- commit hash: 5cdd6e5
- commit date: 2025-02-12
- overall geometric mean: 1.080x faster
- HPT reliability: 99.97%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250212-darwin-arm64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 168 ms                                                 | 164 ms: 1.03x faster                                                   |
| html5lib       | 33.4 ms                                                | 29.5 ms: 1.13x faster                                                  |
| sphinx         | 613 ms                                                 | 568 ms: 1.08x faster                                                   |
| Geometric mean | (ref)                                                  | 1.06x faster                                                           |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250212-darwin-arm64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg                 | 673 ms                                                 | 364 ms: 1.85x faster                                                   |
| async_tree_eager_io              | 666 ms                                                 | 364 ms: 1.83x faster                                                   |
| async_tree_io                    | 672 ms                                                 | 372 ms: 1.81x faster                                                   |
| async_tree_eager_io_tg           | 617 ms                                                 | 373 ms: 1.66x faster                                                   |
| async_tree_none_tg               | 255 ms                                                 | 155 ms: 1.65x faster                                                   |
| async_tree_none                  | 263 ms                                                 | 162 ms: 1.62x faster                                                   |
| async_tree_memoization_tg        | 318 ms                                                 | 197 ms: 1.62x faster                                                   |
| async_tree_memoization           | 310 ms                                                 | 197 ms: 1.58x faster                                                   |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 417 ms: 1.27x faster                                                   |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 416 ms: 1.27x faster                                                   |
| coroutines                       | 19.7 ms                                                | 15.8 ms: 1.25x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 145 ms: 1.16x faster                                                   |
| async_generators                 | 299 ms                                                 | 273 ms: 1.09x faster                                                   |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 363 ms: 1.03x faster                                                   |
| asyncio_websockets               | 243 ms                                                 | 242 ms: 1.00x faster                                                   |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 393 ms: 1.13x slower                                                   |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 175 ms: 1.23x slower                                                   |
| async_tree_eager_tg              | 46.9 ms                                                | 131 ms: 2.80x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.22x faster                                                           |

Benchmark hidden because not significant (1): async_tree_eager

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250212-darwin-arm64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 54.1 ms                                                | 46.9 ms: 1.15x faster                                                  |
| nbody          | 67.6 ms                                                | 65.6 ms: 1.03x faster                                                  |
| pidigits       | 283 ms                                                 | 283 ms: 1.00x slower                                                   |
| Geometric mean | (ref)                                                  | 1.06x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250212-darwin-arm64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 75.9 ms                                                | 67.9 ms: 1.12x faster                                                  |
| regex_effbot   | 2.44 ms                                                | 2.24 ms: 1.09x faster                                                  |
| regex_dna      | 143 ms                                                 | 140 ms: 1.02x faster                                                   |
| regex_v8       | 15.1 ms                                                | 16.7 ms: 1.11x slower                                                  |
| Geometric mean | (ref)                                                  | 1.03x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250212-darwin-arm64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| unpickle_pure_python | 145 us                                                 | 130 us: 1.12x faster                                                   |
| tomli_loads          | 1.36 sec                                               | 1.21 sec: 1.12x faster                                                 |
| xml_etree_generate   | 55.4 ms                                                | 49.9 ms: 1.11x faster                                                  |
| xml_etree_parse      | 108 ms                                                 | 98.6 ms: 1.09x faster                                                  |
| xml_etree_process    | 38.9 ms                                                | 35.5 ms: 1.09x faster                                                  |
| xml_etree_iterparse  | 75.5 ms                                                | 69.6 ms: 1.08x faster                                                  |
| pickle_pure_python   | 197 us                                                 | 194 us: 1.01x faster                                                   |
| json_loads           | 17.0 us                                                | 17.8 us: 1.05x slower                                                  |
| json_dumps           | 6.19 ms                                                | 7.30 ms: 1.18x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250212-darwin-arm64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 17.8 ms                                                | 19.2 ms: 1.08x slower                                                  |
| python_startup_no_site | 13.2 ms                                                | 14.3 ms: 1.09x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.09x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250212-darwin-arm64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 7.44 ms                                                | 6.46 ms: 1.15x faster                                                  |
| genshi_text     | 14.7 ms                                                | 13.6 ms: 1.08x faster                                                  |
| genshi_xml      | 30.5 ms                                                | 29.3 ms: 1.04x faster                                                  |
| django_template | 19.7 ms                                                | 21.0 ms: 1.06x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.05x faster                                                           |

All benchmarks:
===============

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250212-darwin-arm64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| subparsers                       | 32.1 ms                                                | 12.0 ms: 2.68x faster                                                  |
| async_tree_io_tg                 | 673 ms                                                 | 364 ms: 1.85x faster                                                   |
| async_tree_eager_io              | 666 ms                                                 | 364 ms: 1.83x faster                                                   |
| async_tree_io                    | 672 ms                                                 | 372 ms: 1.81x faster                                                   |
| async_tree_eager_io_tg           | 617 ms                                                 | 373 ms: 1.66x faster                                                   |
| async_tree_none_tg               | 255 ms                                                 | 155 ms: 1.65x faster                                                   |
| async_tree_none                  | 263 ms                                                 | 162 ms: 1.62x faster                                                   |
| async_tree_memoization_tg        | 318 ms                                                 | 197 ms: 1.62x faster                                                   |
| async_tree_memoization           | 310 ms                                                 | 197 ms: 1.58x faster                                                   |
| deepcopy                         | 226 us                                                 | 150 us: 1.51x faster                                                   |
| deepcopy_memo                    | 26.0 us                                                | 18.3 us: 1.42x faster                                                  |
| generators                       | 29.4 ms                                                | 22.9 ms: 1.28x faster                                                  |
| deepcopy_reduce                  | 2.01 us                                                | 1.58 us: 1.27x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 417 ms: 1.27x faster                                                   |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 416 ms: 1.27x faster                                                   |
| spectral_norm                    | 76.5 ms                                                | 61.3 ms: 1.25x faster                                                  |
| coroutines                       | 19.7 ms                                                | 15.8 ms: 1.25x faster                                                  |
| go                               | 98.5 ms                                                | 80.5 ms: 1.22x faster                                                  |
| raytrace                         | 204 ms                                                 | 171 ms: 1.19x faster                                                   |
| async_tree_eager_memoization     | 168 ms                                                 | 145 ms: 1.16x faster                                                   |
| float                            | 54.1 ms                                                | 46.9 ms: 1.15x faster                                                  |
| mako                             | 7.44 ms                                                | 6.46 ms: 1.15x faster                                                  |
| logging_simple                   | 3.60 us                                                | 3.13 us: 1.15x faster                                                  |
| bpe_tokeniser                    | 3.28 sec                                               | 2.87 sec: 1.14x faster                                                 |
| logging_format                   | 3.90 us                                                | 3.44 us: 1.14x faster                                                  |
| comprehensions                   | 14.0 us                                                | 12.3 us: 1.13x faster                                                  |
| html5lib                         | 33.4 ms                                                | 29.5 ms: 1.13x faster                                                  |
| pylint                           | 182 ms                                                 | 161 ms: 1.13x faster                                                   |
| k_core                           | 1.72 sec                                               | 1.53 sec: 1.13x faster                                                 |
| scimark_fft                      | 194 ms                                                 | 173 ms: 1.13x faster                                                   |
| unpickle_pure_python             | 145 us                                                 | 130 us: 1.12x faster                                                   |
| tomli_loads                      | 1.36 sec                                               | 1.21 sec: 1.12x faster                                                 |
| regex_compile                    | 75.9 ms                                                | 67.9 ms: 1.12x faster                                                  |
| xml_etree_generate               | 55.4 ms                                                | 49.9 ms: 1.11x faster                                                  |
| bench_mp_pool                    | 65.5 ms                                                | 58.9 ms: 1.11x faster                                                  |
| scimark_sor                      | 85.8 ms                                                | 77.7 ms: 1.10x faster                                                  |
| xml_etree_parse                  | 108 ms                                                 | 98.6 ms: 1.09x faster                                                  |
| pyflate                          | 311 ms                                                 | 284 ms: 1.09x faster                                                   |
| xml_etree_process                | 38.9 ms                                                | 35.5 ms: 1.09x faster                                                  |
| async_generators                 | 299 ms                                                 | 273 ms: 1.09x faster                                                   |
| deltablue                        | 2.57 ms                                                | 2.35 ms: 1.09x faster                                                  |
| regex_effbot                     | 2.44 ms                                                | 2.24 ms: 1.09x faster                                                  |
| scimark_sparse_mat_mult          | 3.14 ms                                                | 2.90 ms: 1.08x faster                                                  |
| xml_etree_iterparse              | 75.5 ms                                                | 69.6 ms: 1.08x faster                                                  |
| sphinx                           | 613 ms                                                 | 568 ms: 1.08x faster                                                   |
| thrift                           | 468 us                                                 | 434 us: 1.08x faster                                                   |
| genshi_text                      | 14.7 ms                                                | 13.6 ms: 1.08x faster                                                  |
| logging_silent                   | 72.5 ns                                                | 67.4 ns: 1.08x faster                                                  |
| pathlib                          | 24.7 ms                                                | 23.1 ms: 1.07x faster                                                  |
| chaos                            | 41.6 ms                                                | 39.2 ms: 1.06x faster                                                  |
| sqlalchemy_declarative           | 61.9 ms                                                | 58.9 ms: 1.05x faster                                                  |
| dulwich_log                      | 29.2 ms                                                | 27.9 ms: 1.05x faster                                                  |
| scimark_monte_carlo              | 44.5 ms                                                | 42.5 ms: 1.05x faster                                                  |
| genshi_xml                       | 30.5 ms                                                | 29.3 ms: 1.04x faster                                                  |
| nbody                            | 67.6 ms                                                | 65.6 ms: 1.03x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 363 ms: 1.03x faster                                                   |
| 2to3                             | 168 ms                                                 | 164 ms: 1.03x faster                                                   |
| sympy_str                        | 144 ms                                                 | 141 ms: 1.02x faster                                                   |
| sympy_sum                        | 76.2 ms                                                | 74.7 ms: 1.02x faster                                                  |
| regex_dna                        | 143 ms                                                 | 140 ms: 1.02x faster                                                   |
| dask                             | 779 ms                                                 | 768 ms: 1.01x faster                                                   |
| pickle_pure_python               | 197 us                                                 | 194 us: 1.01x faster                                                   |
| sqlite_synth                     | 1.55 us                                                | 1.53 us: 1.01x faster                                                  |
| json                             | 3.00 ms                                                | 2.98 ms: 1.01x faster                                                  |
| shortest_path                    | 331 ms                                                 | 328 ms: 1.01x faster                                                   |
| connected_components             | 300 ms                                                 | 298 ms: 1.01x faster                                                   |
| asyncio_websockets               | 243 ms                                                 | 242 ms: 1.00x faster                                                   |
| pidigits                         | 283 ms                                                 | 283 ms: 1.00x slower                                                   |
| sqlalchemy_imperative            | 6.60 ms                                                | 6.63 ms: 1.00x slower                                                  |
| sqlglot_normalize                | 180 ms                                                 | 182 ms: 1.01x slower                                                   |
| richards_super                   | 34.6 ms                                                | 35.1 ms: 1.01x slower                                                  |
| sqlglot_parse                    | 808 us                                                 | 828 us: 1.02x slower                                                   |
| sympy_expand                     | 233 ms                                                 | 239 ms: 1.02x slower                                                   |
| sqlglot_transpile                | 973 us                                                 | 997 us: 1.02x slower                                                   |
| crypto_pyaes                     | 51.4 ms                                                | 52.7 ms: 1.02x slower                                                  |
| mdp                              | 1.49 sec                                               | 1.53 sec: 1.03x slower                                                 |
| richards                         | 30.6 ms                                                | 31.4 ms: 1.03x slower                                                  |
| sympy_integrate                  | 11.1 ms                                                | 11.4 ms: 1.03x slower                                                  |
| bench_thread_pool                | 483 us                                                 | 497 us: 1.03x slower                                                   |
| nqueens                          | 59.5 ms                                                | 61.6 ms: 1.03x slower                                                  |
| pprint_pformat                   | 986 ms                                                 | 1.03 sec: 1.04x slower                                                 |
| typing_runtime_protocols         | 91.5 us                                                | 95.3 us: 1.04x slower                                                  |
| json_loads                       | 17.0 us                                                | 17.8 us: 1.05x slower                                                  |
| gc_traversal                     | 2.95 ms                                                | 3.12 ms: 1.06x slower                                                  |
| django_template                  | 19.7 ms                                                | 21.0 ms: 1.06x slower                                                  |
| hexiom                           | 4.38 ms                                                | 4.67 ms: 1.07x slower                                                  |
| pprint_safe_repr                 | 483 ms                                                 | 519 ms: 1.07x slower                                                   |
| python_startup                   | 17.8 ms                                                | 19.2 ms: 1.08x slower                                                  |
| fannkuch                         | 250 ms                                                 | 271 ms: 1.09x slower                                                   |
| meteor_contest                   | 69.1 ms                                                | 75.1 ms: 1.09x slower                                                  |
| python_startup_no_site           | 13.2 ms                                                | 14.3 ms: 1.09x slower                                                  |
| many_optionals                   | 403 us                                                 | 446 us: 1.11x slower                                                   |
| regex_v8                         | 15.1 ms                                                | 16.7 ms: 1.11x slower                                                  |
| create_gc_cycles                 | 1.15 ms                                                | 1.28 ms: 1.11x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 393 ms: 1.13x slower                                                   |
| telco                            | 3.92 ms                                                | 4.57 ms: 1.17x slower                                                  |
| json_dumps                       | 6.19 ms                                                | 7.30 ms: 1.18x slower                                                  |
| coverage                         | 38.5 ms                                                | 46.1 ms: 1.20x slower                                                  |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 175 ms: 1.23x slower                                                   |
| async_tree_eager_tg              | 46.9 ms                                                | 131 ms: 2.80x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.08x faster                                                           |

Benchmark hidden because not significant (5): sqlglot_optimize, scimark_lu, async_tree_eager, docutils, pycparser
Ignored benchmarks (5) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.080x faster

# HPT report

- Reliability score: 99.97% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.11x