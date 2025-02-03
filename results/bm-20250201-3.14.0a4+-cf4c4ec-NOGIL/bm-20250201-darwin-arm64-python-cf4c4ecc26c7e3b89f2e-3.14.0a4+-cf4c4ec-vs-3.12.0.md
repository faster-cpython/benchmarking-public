# Results vs. 3.12.0

- fork: python
- ref: cf4c4ecc26c7e3b89f2e
- machine: darwin-arm64
- commit hash: cf4c4ec
- commit date: 2025-02-01
- overall geometric mean: 1.051x faster
- HPT reliability: 72.17%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.21x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250201-darwin-arm64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 168 ms                                                 | 177 ms: 1.05x slower                                                   |
| docutils       | 1.45 sec                                               | 1.36 sec: 1.07x faster                                                 |
| html5lib       | 33.4 ms                                                | 30.4 ms: 1.10x faster                                                  |
| sphinx         | 613 ms                                                 | 582 ms: 1.05x faster                                                   |
| Geometric mean | (ref)                                                  | 1.04x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250201-darwin-arm64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg                 | 673 ms                                                 | 304 ms: 2.22x faster                                                   |
| async_tree_eager_io              | 666 ms                                                 | 313 ms: 2.13x faster                                                   |
| async_tree_eager_io_tg           | 617 ms                                                 | 295 ms: 2.09x faster                                                   |
| async_tree_io                    | 672 ms                                                 | 326 ms: 2.06x faster                                                   |
| async_tree_memoization_tg        | 318 ms                                                 | 172 ms: 1.85x faster                                                   |
| async_tree_none_tg               | 255 ms                                                 | 140 ms: 1.82x faster                                                   |
| async_tree_none                  | 263 ms                                                 | 157 ms: 1.68x faster                                                   |
| async_tree_memoization           | 310 ms                                                 | 194 ms: 1.60x faster                                                   |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 380 ms: 1.39x faster                                                   |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 404 ms: 1.30x faster                                                   |
| coroutines                       | 19.7 ms                                                | 16.0 ms: 1.23x faster                                                  |
| async_generators                 | 299 ms                                                 | 259 ms: 1.15x faster                                                   |
| async_tree_eager_memoization     | 168 ms                                                 | 150 ms: 1.12x faster                                                   |
| asyncio_websockets               | 243 ms                                                 | 237 ms: 1.02x faster                                                   |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 368 ms: 1.01x faster                                                   |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 365 ms: 1.05x slower                                                   |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 158 ms: 1.11x slower                                                   |
| async_tree_eager                 | 65.8 ms                                                | 80.1 ms: 1.22x slower                                                  |
| async_tree_eager_tg              | 46.9 ms                                                | 118 ms: 2.51x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.30x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250201-darwin-arm64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 54.1 ms                                                | 47.1 ms: 1.15x faster                                                  |
| pidigits       | 283 ms                                                 | 280 ms: 1.01x faster                                                   |
| nbody          | 67.6 ms                                                | 87.7 ms: 1.30x slower                                                  |
| Geometric mean | (ref)                                                  | 1.04x slower                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250201-darwin-arm64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 2.44 ms                                                | 2.09 ms: 1.17x faster                                                  |
| regex_compile  | 75.9 ms                                                | 73.6 ms: 1.03x faster                                                  |
| regex_dna      | 143 ms                                                 | 139 ms: 1.03x faster                                                   |
| regex_v8       | 15.1 ms                                                | 15.4 ms: 1.02x slower                                                  |
| Geometric mean | (ref)                                                  | 1.05x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250201-darwin-arm64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_iterparse  | 75.5 ms                                                | 62.2 ms: 1.21x faster                                                  |
| xml_etree_parse      | 108 ms                                                 | 95.5 ms: 1.13x faster                                                  |
| xml_etree_generate   | 55.4 ms                                                | 54.9 ms: 1.01x faster                                                  |
| tomli_loads          | 1.36 sec                                               | 1.35 sec: 1.01x faster                                                 |
| xml_etree_process    | 38.9 ms                                                | 40.1 ms: 1.03x slower                                                  |
| unpickle_pure_python | 145 us                                                 | 151 us: 1.04x slower                                                   |
| pickle_pure_python   | 197 us                                                 | 217 us: 1.10x slower                                                   |
| json_loads           | 17.0 us                                                | 18.8 us: 1.10x slower                                                  |
| json_dumps           | 6.19 ms                                                | 7.67 ms: 1.24x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.02x slower                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250201-darwin-arm64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 17.8 ms                                                | 18.4 ms: 1.04x slower                                                  |
| python_startup_no_site | 13.2 ms                                                | 13.7 ms: 1.04x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.04x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250201-darwin-arm64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_xml      | 30.5 ms                                                | 31.6 ms: 1.04x slower                                                  |
| genshi_text     | 14.7 ms                                                | 15.5 ms: 1.06x slower                                                  |
| django_template | 19.7 ms                                                | 23.1 ms: 1.17x slower                                                  |
| mako            | 7.44 ms                                                | 9.93 ms: 1.33x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.14x slower                                                           |

All benchmarks:
===============

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250201-darwin-arm64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| subparsers                       | 32.1 ms                                                | 12.5 ms: 2.56x faster                                                  |
| async_tree_io_tg                 | 673 ms                                                 | 304 ms: 2.22x faster                                                   |
| async_tree_eager_io              | 666 ms                                                 | 313 ms: 2.13x faster                                                   |
| async_tree_eager_io_tg           | 617 ms                                                 | 295 ms: 2.09x faster                                                   |
| async_tree_io                    | 672 ms                                                 | 326 ms: 2.06x faster                                                   |
| gc_traversal                     | 2.95 ms                                                | 1.45 ms: 2.03x faster                                                  |
| async_tree_memoization_tg        | 318 ms                                                 | 172 ms: 1.85x faster                                                   |
| async_tree_none_tg               | 255 ms                                                 | 140 ms: 1.82x faster                                                   |
| async_tree_none                  | 263 ms                                                 | 157 ms: 1.68x faster                                                   |
| async_tree_memoization           | 310 ms                                                 | 194 ms: 1.60x faster                                                   |
| deepcopy                         | 226 us                                                 | 161 us: 1.40x faster                                                   |
| create_gc_cycles                 | 1.15 ms                                                | 823 us: 1.40x faster                                                   |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 380 ms: 1.39x faster                                                   |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 404 ms: 1.30x faster                                                   |
| deepcopy_memo                    | 26.0 us                                                | 21.0 us: 1.24x faster                                                  |
| coroutines                       | 19.7 ms                                                | 16.0 ms: 1.23x faster                                                  |
| sqlite_synth                     | 1.55 us                                                | 1.27 us: 1.22x faster                                                  |
| xml_etree_iterparse              | 75.5 ms                                                | 62.2 ms: 1.21x faster                                                  |
| generators                       | 29.4 ms                                                | 24.8 ms: 1.18x faster                                                  |
| regex_effbot                     | 2.44 ms                                                | 2.09 ms: 1.17x faster                                                  |
| deepcopy_reduce                  | 2.01 us                                                | 1.74 us: 1.16x faster                                                  |
| async_generators                 | 299 ms                                                 | 259 ms: 1.15x faster                                                   |
| float                            | 54.1 ms                                                | 47.1 ms: 1.15x faster                                                  |
| xml_etree_parse                  | 108 ms                                                 | 95.5 ms: 1.13x faster                                                  |
| comprehensions                   | 14.0 us                                                | 12.5 us: 1.12x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 150 ms: 1.12x faster                                                   |
| pylint                           | 182 ms                                                 | 163 ms: 1.12x faster                                                   |
| pathlib                          | 24.7 ms                                                | 22.1 ms: 1.12x faster                                                  |
| bpe_tokeniser                    | 3.28 sec                                               | 2.95 sec: 1.11x faster                                                 |
| go                               | 98.5 ms                                                | 89.6 ms: 1.10x faster                                                  |
| html5lib                         | 33.4 ms                                                | 30.4 ms: 1.10x faster                                                  |
| pycparser                        | 673 ms                                                 | 622 ms: 1.08x faster                                                   |
| docutils                         | 1.45 sec                                               | 1.36 sec: 1.07x faster                                                 |
| k_core                           | 1.72 sec                                               | 1.61 sec: 1.07x faster                                                 |
| sphinx                           | 613 ms                                                 | 582 ms: 1.05x faster                                                   |
| spectral_norm                    | 76.5 ms                                                | 73.1 ms: 1.05x faster                                                  |
| bench_mp_pool                    | 65.5 ms                                                | 63.5 ms: 1.03x faster                                                  |
| regex_compile                    | 75.9 ms                                                | 73.6 ms: 1.03x faster                                                  |
| pyflate                          | 311 ms                                                 | 302 ms: 1.03x faster                                                   |
| regex_dna                        | 143 ms                                                 | 139 ms: 1.03x faster                                                   |
| asyncio_websockets               | 243 ms                                                 | 237 ms: 1.02x faster                                                   |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 368 ms: 1.01x faster                                                   |
| dulwich_log                      | 29.2 ms                                                | 28.9 ms: 1.01x faster                                                  |
| xml_etree_generate               | 55.4 ms                                                | 54.9 ms: 1.01x faster                                                  |
| pidigits                         | 283 ms                                                 | 280 ms: 1.01x faster                                                   |
| tomli_loads                      | 1.36 sec                                               | 1.35 sec: 1.01x faster                                                 |
| nqueens                          | 59.5 ms                                                | 59.2 ms: 1.01x faster                                                  |
| logging_simple                   | 3.60 us                                                | 3.59 us: 1.01x faster                                                  |
| logging_format                   | 3.90 us                                                | 3.93 us: 1.01x slower                                                  |
| sqlglot_optimize                 | 33.2 ms                                                | 33.6 ms: 1.01x slower                                                  |
| raytrace                         | 204 ms                                                 | 208 ms: 1.02x slower                                                   |
| thrift                           | 468 us                                                 | 479 us: 1.02x slower                                                   |
| regex_v8                         | 15.1 ms                                                | 15.4 ms: 1.02x slower                                                  |
| sqlglot_normalize                | 180 ms                                                 | 184 ms: 1.02x slower                                                   |
| sympy_sum                        | 76.2 ms                                                | 78.2 ms: 1.03x slower                                                  |
| scimark_sor                      | 85.8 ms                                                | 88.4 ms: 1.03x slower                                                  |
| xml_etree_process                | 38.9 ms                                                | 40.1 ms: 1.03x slower                                                  |
| mdp                              | 1.49 sec                                               | 1.54 sec: 1.03x slower                                                 |
| json                             | 3.00 ms                                                | 3.10 ms: 1.03x slower                                                  |
| genshi_xml                       | 30.5 ms                                                | 31.6 ms: 1.04x slower                                                  |
| python_startup                   | 17.8 ms                                                | 18.4 ms: 1.04x slower                                                  |
| unpickle_pure_python             | 145 us                                                 | 151 us: 1.04x slower                                                   |
| sqlalchemy_declarative           | 61.9 ms                                                | 64.5 ms: 1.04x slower                                                  |
| logging_silent                   | 72.5 ns                                                | 75.6 ns: 1.04x slower                                                  |
| python_startup_no_site           | 13.2 ms                                                | 13.7 ms: 1.04x slower                                                  |
| sympy_str                        | 144 ms                                                 | 150 ms: 1.04x slower                                                   |
| chaos                            | 41.6 ms                                                | 43.6 ms: 1.05x slower                                                  |
| 2to3                             | 168 ms                                                 | 177 ms: 1.05x slower                                                   |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 365 ms: 1.05x slower                                                   |
| shortest_path                    | 331 ms                                                 | 350 ms: 1.06x slower                                                   |
| genshi_text                      | 14.7 ms                                                | 15.5 ms: 1.06x slower                                                  |
| sqlglot_transpile                | 973 us                                                 | 1.03 ms: 1.06x slower                                                  |
| hexiom                           | 4.38 ms                                                | 4.70 ms: 1.07x slower                                                  |
| sqlalchemy_imperative            | 6.60 ms                                                | 7.12 ms: 1.08x slower                                                  |
| sympy_integrate                  | 11.1 ms                                                | 11.9 ms: 1.08x slower                                                  |
| sympy_expand                     | 233 ms                                                 | 252 ms: 1.08x slower                                                   |
| sqlglot_parse                    | 808 us                                                 | 875 us: 1.08x slower                                                   |
| connected_components             | 300 ms                                                 | 325 ms: 1.09x slower                                                   |
| scimark_fft                      | 194 ms                                                 | 212 ms: 1.09x slower                                                   |
| pickle_pure_python               | 197 us                                                 | 217 us: 1.10x slower                                                   |
| deltablue                        | 2.57 ms                                                | 2.82 ms: 1.10x slower                                                  |
| json_loads                       | 17.0 us                                                | 18.8 us: 1.10x slower                                                  |
| pprint_pformat                   | 986 ms                                                 | 1.09 sec: 1.10x slower                                                 |
| many_optionals                   | 403 us                                                 | 447 us: 1.11x slower                                                   |
| scimark_monte_carlo              | 44.5 ms                                                | 49.4 ms: 1.11x slower                                                  |
| pprint_safe_repr                 | 483 ms                                                 | 537 ms: 1.11x slower                                                   |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 158 ms: 1.11x slower                                                   |
| crypto_pyaes                     | 51.4 ms                                                | 57.7 ms: 1.12x slower                                                  |
| meteor_contest                   | 69.1 ms                                                | 77.5 ms: 1.12x slower                                                  |
| scimark_sparse_mat_mult          | 3.14 ms                                                | 3.53 ms: 1.12x slower                                                  |
| fannkuch                         | 250 ms                                                 | 284 ms: 1.14x slower                                                   |
| richards_super                   | 34.6 ms                                                | 40.0 ms: 1.16x slower                                                  |
| richards                         | 30.6 ms                                                | 35.4 ms: 1.16x slower                                                  |
| scimark_lu                       | 73.5 ms                                                | 86.1 ms: 1.17x slower                                                  |
| django_template                  | 19.7 ms                                                | 23.1 ms: 1.17x slower                                                  |
| async_tree_eager                 | 65.8 ms                                                | 80.1 ms: 1.22x slower                                                  |
| json_dumps                       | 6.19 ms                                                | 7.67 ms: 1.24x slower                                                  |
| typing_runtime_protocols         | 91.5 us                                                | 114 us: 1.25x slower                                                   |
| telco                            | 3.92 ms                                                | 4.97 ms: 1.27x slower                                                  |
| nbody                            | 67.6 ms                                                | 87.7 ms: 1.30x slower                                                  |
| mako                             | 7.44 ms                                                | 9.93 ms: 1.33x slower                                                  |
| coverage                         | 38.5 ms                                                | 51.4 ms: 1.33x slower                                                  |
| bench_thread_pool                | 483 us                                                 | 782 us: 1.62x slower                                                   |
| async_tree_eager_tg              | 46.9 ms                                                | 118 ms: 2.51x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.05x faster                                                           |
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: chameleon, dask, djangocms, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (8) of results/bm-20250201-3.14.0a4+-cf4c4ec-NOGIL/bm-20250201-darwin-arm64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.051x faster

# HPT report

- Reliability score: 72.17% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.21x