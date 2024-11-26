# Results vs. 3.12.0

- fork: brandtbucher
- ref: justin_frame_pointer
- machine: darwin-arm64
- commit hash: b1f0a4e
- commit date: 2024-11-14
- overall geometric mean: 1.008x slower
- HPT reliability: 89.47%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.27x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241114-darwin-arm64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 169 ms                                                 | 193 ms: 1.14x slower                                                         |
| docutils       | 1.50 sec                                               | 1.61 sec: 1.07x slower                                                       |
| Geometric mean | (ref)                                                  | 1.11x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241114-darwin-arm64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 323 ms                                                 | 241 ms: 1.34x faster                                                         |
| async_tree_none            | 266 ms                                                 | 212 ms: 1.25x faster                                                         |
| async_tree_none_tg         | 258 ms                                                 | 208 ms: 1.24x faster                                                         |
| async_tree_memoization     | 312 ms                                                 | 257 ms: 1.21x faster                                                         |
| async_tree_io              | 668 ms                                                 | 596 ms: 1.12x faster                                                         |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 473 ms: 1.11x faster                                                         |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 480 ms: 1.11x faster                                                         |
| async_tree_io_tg           | 669 ms                                                 | 628 ms: 1.07x faster                                                         |
| Geometric mean             | (ref)                                                  | 1.18x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241114-darwin-arm64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 51.2 ms: 1.09x faster                                                        |
| pidigits       | 282 ms                                                 | 283 ms: 1.01x slower                                                         |
| nbody          | 68.8 ms                                                | 72.8 ms: 1.06x slower                                                        |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241114-darwin-arm64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 2.64 ms                                                | 2.33 ms: 1.13x faster                                                        |
| regex_dna      | 154 ms                                                 | 141 ms: 1.09x faster                                                         |
| regex_compile  | 77.9 ms                                                | 79.1 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                  | 1.05x faster                                                                 |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241114-darwin-arm64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_generate   | 55.8 ms                                                | 51.4 ms: 1.09x faster                                                        |
| xml_etree_process    | 39.7 ms                                                | 36.6 ms: 1.08x faster                                                        |
| tomli_loads          | 1.39 sec                                               | 1.30 sec: 1.07x faster                                                       |
| json_loads           | 17.2 us                                                | 16.7 us: 1.03x faster                                                        |
| unpickle_pure_python | 151 us                                                 | 148 us: 1.02x faster                                                         |
| pickle_pure_python   | 200 us                                                 | 201 us: 1.00x slower                                                         |
| json_dumps           | 6.22 ms                                                | 7.27 ms: 1.17x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                                 |

Benchmark hidden because not significant (2): xml_etree_parse, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241114-darwin-arm64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 9.37 ms                                                | 15.0 ms: 1.60x slower                                                        |
| python_startup         | 11.4 ms                                                | 19.7 ms: 1.73x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.66x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241114-darwin-arm64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 7.71 ms                                                | 6.61 ms: 1.17x faster                                                        |
| django_template | 22.3 ms                                                | 23.8 ms: 1.07x slower                                                        |
| Geometric mean  | (ref)                                                  | 1.05x faster                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241114-darwin-arm64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| asyncio_websockets         | 409 ms                                                 | 242 ms: 1.69x faster                                                         |
| deepcopy                   | 235 us                                                 | 163 us: 1.44x faster                                                         |
| deepcopy_memo              | 27.7 us                                                | 19.2 us: 1.44x faster                                                        |
| async_tree_memoization_tg  | 323 ms                                                 | 241 ms: 1.34x faster                                                         |
| deepcopy_reduce            | 2.07 us                                                | 1.60 us: 1.29x faster                                                        |
| async_tree_none            | 266 ms                                                 | 212 ms: 1.25x faster                                                         |
| async_tree_none_tg         | 258 ms                                                 | 208 ms: 1.24x faster                                                         |
| async_tree_memoization     | 312 ms                                                 | 257 ms: 1.21x faster                                                         |
| mako                       | 7.71 ms                                                | 6.61 ms: 1.17x faster                                                        |
| regex_effbot               | 2.64 ms                                                | 2.33 ms: 1.13x faster                                                        |
| async_tree_io              | 668 ms                                                 | 596 ms: 1.12x faster                                                         |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 473 ms: 1.11x faster                                                         |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 480 ms: 1.11x faster                                                         |
| regex_dna                  | 154 ms                                                 | 141 ms: 1.09x faster                                                         |
| coroutines                 | 19.2 ms                                                | 17.6 ms: 1.09x faster                                                        |
| float                      | 55.8 ms                                                | 51.2 ms: 1.09x faster                                                        |
| raytrace                   | 212 ms                                                 | 195 ms: 1.09x faster                                                         |
| xml_etree_generate         | 55.8 ms                                                | 51.4 ms: 1.09x faster                                                        |
| generators                 | 31.1 ms                                                | 28.6 ms: 1.08x faster                                                        |
| xml_etree_process          | 39.7 ms                                                | 36.6 ms: 1.08x faster                                                        |
| logging_simple             | 3.69 us                                                | 3.41 us: 1.08x faster                                                        |
| pathlib                    | 24.2 ms                                                | 22.5 ms: 1.07x faster                                                        |
| logging_format             | 3.98 us                                                | 3.72 us: 1.07x faster                                                        |
| json                       | 3.09 ms                                                | 2.88 ms: 1.07x faster                                                        |
| tomli_loads                | 1.39 sec                                               | 1.30 sec: 1.07x faster                                                       |
| async_tree_io_tg           | 669 ms                                                 | 628 ms: 1.07x faster                                                         |
| json_loads                 | 17.2 us                                                | 16.7 us: 1.03x faster                                                        |
| scimark_lu                 | 76.0 ms                                                | 73.7 ms: 1.03x faster                                                        |
| unpickle_pure_python       | 151 us                                                 | 148 us: 1.02x faster                                                         |
| spectral_norm              | 76.4 ms                                                | 75.2 ms: 1.02x faster                                                        |
| dulwich_log                | 29.8 ms                                                | 29.4 ms: 1.01x faster                                                        |
| sqlite_synth               | 1.57 us                                                | 1.55 us: 1.01x faster                                                        |
| bench_thread_pool          | 504 us                                                 | 499 us: 1.01x faster                                                         |
| comprehensions             | 14.5 us                                                | 14.4 us: 1.01x faster                                                        |
| pickle_pure_python         | 200 us                                                 | 201 us: 1.00x slower                                                         |
| sqlalchemy_imperative      | 6.68 ms                                                | 6.72 ms: 1.01x slower                                                        |
| scimark_fft                | 195 ms                                                 | 196 ms: 1.01x slower                                                         |
| pidigits                   | 282 ms                                                 | 283 ms: 1.01x slower                                                         |
| async_generators           | 304 ms                                                 | 307 ms: 1.01x slower                                                         |
| scimark_sparse_mat_mult    | 3.14 ms                                                | 3.17 ms: 1.01x slower                                                        |
| regex_compile              | 77.9 ms                                                | 79.1 ms: 1.02x slower                                                        |
| nqueens                    | 62.4 ms                                                | 63.4 ms: 1.02x slower                                                        |
| mdp                        | 1.58 sec                                               | 1.61 sec: 1.02x slower                                                       |
| pprint_safe_repr           | 497 ms                                                 | 507 ms: 1.02x slower                                                         |
| sqlalchemy_declarative     | 62.3 ms                                                | 63.7 ms: 1.02x slower                                                        |
| pprint_pformat             | 1.01 sec                                               | 1.04 sec: 1.02x slower                                                       |
| deltablue                  | 2.71 ms                                                | 2.79 ms: 1.03x slower                                                        |
| pycparser                  | 677 ms                                                 | 700 ms: 1.03x slower                                                         |
| go                         | 102 ms                                                 | 106 ms: 1.04x slower                                                         |
| nbody                      | 68.8 ms                                                | 72.8 ms: 1.06x slower                                                        |
| sqlglot_normalize          | 186 ms                                                 | 197 ms: 1.06x slower                                                         |
| fannkuch                   | 248 ms                                                 | 264 ms: 1.06x slower                                                         |
| chaos                      | 42.5 ms                                                | 45.2 ms: 1.06x slower                                                        |
| sympy_sum                  | 77.6 ms                                                | 82.5 ms: 1.06x slower                                                        |
| sqlglot_parse              | 848 us                                                 | 903 us: 1.06x slower                                                         |
| django_template            | 22.3 ms                                                | 23.8 ms: 1.07x slower                                                        |
| scimark_monte_carlo        | 45.0 ms                                                | 48.0 ms: 1.07x slower                                                        |
| richards_super             | 36.0 ms                                                | 38.5 ms: 1.07x slower                                                        |
| meteor_contest             | 71.7 ms                                                | 76.9 ms: 1.07x slower                                                        |
| docutils                   | 1.50 sec                                               | 1.61 sec: 1.07x slower                                                       |
| sympy_str                  | 148 ms                                                 | 158 ms: 1.07x slower                                                         |
| sympy_expand               | 241 ms                                                 | 259 ms: 1.07x slower                                                         |
| sqlglot_transpile          | 1.02 ms                                                | 1.11 ms: 1.08x slower                                                        |
| richards                   | 32.1 ms                                                | 34.8 ms: 1.08x slower                                                        |
| crypto_pyaes               | 51.9 ms                                                | 56.3 ms: 1.09x slower                                                        |
| typing_runtime_protocols   | 93.0 us                                                | 102 us: 1.10x slower                                                         |
| pyflate                    | 316 ms                                                 | 347 ms: 1.10x slower                                                         |
| scimark_sor                | 87.4 ms                                                | 96.4 ms: 1.10x slower                                                        |
| logging_silent             | 76.4 ns                                                | 85.0 ns: 1.11x slower                                                        |
| coverage                   | 38.9 ms                                                | 44.3 ms: 1.14x slower                                                        |
| 2to3                       | 169 ms                                                 | 193 ms: 1.14x slower                                                         |
| sqlglot_optimize           | 34.0 ms                                                | 39.0 ms: 1.15x slower                                                        |
| sympy_integrate            | 11.4 ms                                                | 13.2 ms: 1.16x slower                                                        |
| json_dumps                 | 6.22 ms                                                | 7.27 ms: 1.17x slower                                                        |
| gc_traversal               | 2.40 ms                                                | 2.93 ms: 1.22x slower                                                        |
| hexiom                     | 4.54 ms                                                | 5.60 ms: 1.23x slower                                                        |
| telco                      | 3.68 ms                                                | 4.65 ms: 1.26x slower                                                        |
| bench_mp_pool              | 44.9 ms                                                | 65.2 ms: 1.45x slower                                                        |
| python_startup_no_site     | 9.37 ms                                                | 15.0 ms: 1.60x slower                                                        |
| python_startup             | 11.4 ms                                                | 19.7 ms: 1.73x slower                                                        |
| create_gc_cycles           | 701 us                                                 | 1.33 ms: 1.89x slower                                                        |
| Geometric mean             | (ref)                                                  | 1.01x slower                                                                 |

Benchmark hidden because not significant (3): xml_etree_parse, regex_v8, xml_etree_iterparse
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (20) of results/bm-20241114-3.14.0a1+-b1f0a4e-JIT/bm-20241114-darwin-arm64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.008x slower
# HPT report

- Reliability score: 89.47% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.27x