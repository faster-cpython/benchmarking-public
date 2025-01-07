# Results vs. 3.12.0

- fork: kumaraditya303
- ref: fast_state
- machine: darwin-arm64
- commit hash: 7de6e22
- commit date: 2025-01-07
- overall geometric mean: 1.084x slower
- HPT reliability: 99.56%
- HPT 99th percentile: 1.01x slower
- Memory change: 1.36x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-darwin-arm64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 169 ms                                                 | 206 ms: 1.22x slower                                                 |
| Geometric mean | (ref)                                                  | 1.10x slower                                                         |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-darwin-arm64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_io_tg           | 669 ms                                                 | 391 ms: 1.71x faster                                                 |
| async_tree_io              | 668 ms                                                 | 415 ms: 1.61x faster                                                 |
| async_tree_none_tg         | 258 ms                                                 | 170 ms: 1.52x faster                                                 |
| async_tree_memoization_tg  | 323 ms                                                 | 216 ms: 1.50x faster                                                 |
| async_tree_none            | 266 ms                                                 | 191 ms: 1.39x faster                                                 |
| async_tree_memoization     | 312 ms                                                 | 235 ms: 1.33x faster                                                 |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 419 ms: 1.27x faster                                                 |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 441 ms: 1.19x faster                                                 |
| Geometric mean             | (ref)                                                  | 1.43x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-darwin-arm64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| pidigits       | 282 ms                                                 | 280 ms: 1.01x faster                                                 |
| float          | 55.8 ms                                                | 65.8 ms: 1.18x slower                                                |
| nbody          | 68.8 ms                                                | 86.5 ms: 1.26x slower                                                |
| Geometric mean | (ref)                                                  | 1.14x slower                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-darwin-arm64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_effbot   | 2.64 ms                                                | 2.10 ms: 1.26x faster                                                |
| regex_dna      | 154 ms                                                 | 136 ms: 1.14x faster                                                 |
| regex_v8       | 16.0 ms                                                | 15.8 ms: 1.01x faster                                                |
| regex_compile  | 77.9 ms                                                | 83.2 ms: 1.07x slower                                                |
| Geometric mean | (ref)                                                  | 1.08x faster                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-darwin-arm64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| xml_etree_iterparse  | 74.0 ms                                                | 66.1 ms: 1.12x faster                                                |
| xml_etree_parse      | 106 ms                                                 | 102 ms: 1.05x faster                                                 |
| json_loads           | 17.2 us                                                | 17.2 us: 1.00x faster                                                |
| xml_etree_generate   | 55.8 ms                                                | 58.3 ms: 1.04x slower                                                |
| tomli_loads          | 1.39 sec                                               | 1.47 sec: 1.05x slower                                               |
| xml_etree_process    | 39.7 ms                                                | 44.0 ms: 1.11x slower                                                |
| json_dumps           | 6.22 ms                                                | 8.16 ms: 1.31x slower                                                |
| unpickle_pure_python | 151 us                                                 | 201 us: 1.34x slower                                                 |
| pickle_pure_python   | 200 us                                                 | 289 us: 1.44x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.11x slower                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-darwin-arm64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup_no_site | 9.37 ms                                                | 15.2 ms: 1.63x slower                                                |
| python_startup         | 11.4 ms                                                | 20.2 ms: 1.77x slower                                                |
| Geometric mean         | (ref)                                                  | 1.70x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-darwin-arm64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| django_template | 22.3 ms                                                | 27.1 ms: 1.21x slower                                                |
| mako            | 7.71 ms                                                | 11.1 ms: 1.44x slower                                                |
| Geometric mean  | (ref)                                                  | 1.32x slower                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-darwin-arm64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| asyncio_websockets         | 409 ms                                                 | 238 ms: 1.72x faster                                                 |
| async_tree_io_tg           | 669 ms                                                 | 391 ms: 1.71x faster                                                 |
| async_tree_io              | 668 ms                                                 | 415 ms: 1.61x faster                                                 |
| async_tree_none_tg         | 258 ms                                                 | 170 ms: 1.52x faster                                                 |
| async_tree_memoization_tg  | 323 ms                                                 | 216 ms: 1.50x faster                                                 |
| async_tree_none            | 266 ms                                                 | 191 ms: 1.39x faster                                                 |
| deepcopy                   | 235 us                                                 | 174 us: 1.35x faster                                                 |
| async_tree_memoization     | 312 ms                                                 | 235 ms: 1.33x faster                                                 |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 419 ms: 1.27x faster                                                 |
| regex_effbot               | 2.64 ms                                                | 2.10 ms: 1.26x faster                                                |
| deepcopy_memo              | 27.7 us                                                | 22.8 us: 1.22x faster                                                |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 441 ms: 1.19x faster                                                 |
| sqlite_synth               | 1.57 us                                                | 1.35 us: 1.16x faster                                                |
| coroutines                 | 19.2 ms                                                | 16.6 ms: 1.16x faster                                                |
| regex_dna                  | 154 ms                                                 | 136 ms: 1.14x faster                                                 |
| deepcopy_reduce            | 2.07 us                                                | 1.82 us: 1.14x faster                                                |
| xml_etree_iterparse        | 74.0 ms                                                | 66.1 ms: 1.12x faster                                                |
| generators                 | 31.1 ms                                                | 27.9 ms: 1.11x faster                                                |
| pathlib                    | 24.2 ms                                                | 22.8 ms: 1.06x faster                                                |
| nqueens                    | 62.4 ms                                                | 58.9 ms: 1.06x faster                                                |
| json                       | 3.09 ms                                                | 2.93 ms: 1.05x faster                                                |
| xml_etree_parse            | 106 ms                                                 | 102 ms: 1.05x faster                                                 |
| async_generators           | 304 ms                                                 | 295 ms: 1.03x faster                                                 |
| spectral_norm              | 76.4 ms                                                | 75.1 ms: 1.02x faster                                                |
| regex_v8                   | 16.0 ms                                                | 15.8 ms: 1.01x faster                                                |
| pidigits                   | 282 ms                                                 | 280 ms: 1.01x faster                                                 |
| json_loads                 | 17.2 us                                                | 17.2 us: 1.00x faster                                                |
| mdp                        | 1.58 sec                                               | 1.60 sec: 1.01x slower                                               |
| xml_etree_generate         | 55.8 ms                                                | 58.3 ms: 1.04x slower                                                |
| tomli_loads                | 1.39 sec                                               | 1.47 sec: 1.05x slower                                               |
| pycparser                  | 677 ms                                                 | 721 ms: 1.06x slower                                                 |
| regex_compile              | 77.9 ms                                                | 83.2 ms: 1.07x slower                                                |
| sympy_sum                  | 77.6 ms                                                | 83.7 ms: 1.08x slower                                                |
| sqlglot_optimize           | 34.0 ms                                                | 37.1 ms: 1.09x slower                                                |
| scimark_fft                | 195 ms                                                 | 213 ms: 1.09x slower                                                 |
| sqlglot_normalize          | 186 ms                                                 | 203 ms: 1.09x slower                                                 |
| gc_traversal               | 2.40 ms                                                | 2.64 ms: 1.10x slower                                                |
| sympy_str                  | 148 ms                                                 | 162 ms: 1.10x slower                                                 |
| dulwich_log                | 29.8 ms                                                | 32.9 ms: 1.10x slower                                                |
| xml_etree_process          | 39.7 ms                                                | 44.0 ms: 1.11x slower                                                |
| meteor_contest             | 71.7 ms                                                | 79.9 ms: 1.11x slower                                                |
| sympy_integrate            | 11.4 ms                                                | 12.7 ms: 1.12x slower                                                |
| sympy_expand               | 241 ms                                                 | 276 ms: 1.15x slower                                                 |
| scimark_sparse_mat_mult    | 3.14 ms                                                | 3.61 ms: 1.15x slower                                                |
| fannkuch                   | 248 ms                                                 | 290 ms: 1.17x slower                                                 |
| comprehensions             | 14.5 us                                                | 17.0 us: 1.17x slower                                                |
| float                      | 55.8 ms                                                | 65.8 ms: 1.18x slower                                                |
| logging_simple             | 3.69 us                                                | 4.36 us: 1.18x slower                                                |
| sqlalchemy_declarative     | 62.3 ms                                                | 75.1 ms: 1.21x slower                                                |
| crypto_pyaes               | 51.9 ms                                                | 62.6 ms: 1.21x slower                                                |
| logging_format             | 3.98 us                                                | 4.81 us: 1.21x slower                                                |
| django_template            | 22.3 ms                                                | 27.1 ms: 1.21x slower                                                |
| 2to3                       | 169 ms                                                 | 206 ms: 1.22x slower                                                 |
| pyflate                    | 316 ms                                                 | 386 ms: 1.22x slower                                                 |
| sqlalchemy_imperative      | 6.68 ms                                                | 8.29 ms: 1.24x slower                                                |
| pprint_pformat             | 1.01 sec                                               | 1.26 sec: 1.24x slower                                               |
| pprint_safe_repr           | 497 ms                                                 | 618 ms: 1.24x slower                                                 |
| nbody                      | 68.8 ms                                                | 86.5 ms: 1.26x slower                                                |
| scimark_lu                 | 76.0 ms                                                | 95.8 ms: 1.26x slower                                                |
| typing_runtime_protocols   | 93.0 us                                                | 117 us: 1.26x slower                                                 |
| hexiom                     | 4.54 ms                                                | 5.86 ms: 1.29x slower                                                |
| json_dumps                 | 6.22 ms                                                | 8.16 ms: 1.31x slower                                                |
| richards_super             | 36.0 ms                                                | 47.4 ms: 1.31x slower                                                |
| raytrace                   | 212 ms                                                 | 282 ms: 1.33x slower                                                 |
| richards                   | 32.1 ms                                                | 42.7 ms: 1.33x slower                                                |
| coverage                   | 38.9 ms                                                | 51.9 ms: 1.34x slower                                                |
| unpickle_pure_python       | 151 us                                                 | 201 us: 1.34x slower                                                 |
| chaos                      | 42.5 ms                                                | 57.0 ms: 1.34x slower                                                |
| scimark_sor                | 87.4 ms                                                | 118 ms: 1.35x slower                                                 |
| telco                      | 3.68 ms                                                | 5.04 ms: 1.37x slower                                                |
| go                         | 102 ms                                                 | 143 ms: 1.41x slower                                                 |
| scimark_monte_carlo        | 45.0 ms                                                | 63.9 ms: 1.42x slower                                                |
| mako                       | 7.71 ms                                                | 11.1 ms: 1.44x slower                                                |
| pickle_pure_python         | 200 us                                                 | 289 us: 1.44x slower                                                 |
| sqlglot_transpile          | 1.02 ms                                                | 1.48 ms: 1.45x slower                                                |
| logging_silent             | 76.4 ns                                                | 113 ns: 1.48x slower                                                 |
| sqlglot_parse              | 848 us                                                 | 1.26 ms: 1.49x slower                                                |
| bench_mp_pool              | 44.9 ms                                                | 68.4 ms: 1.53x slower                                                |
| mypy2                      | 380 ms                                                 | 611 ms: 1.61x slower                                                 |
| bench_thread_pool          | 504 us                                                 | 817 us: 1.62x slower                                                 |
| python_startup_no_site     | 9.37 ms                                                | 15.2 ms: 1.63x slower                                                |
| create_gc_cycles           | 701 us                                                 | 1.15 ms: 1.64x slower                                                |
| deltablue                  | 2.71 ms                                                | 4.54 ms: 1.68x slower                                                |
| python_startup             | 11.4 ms                                                | 20.2 ms: 1.77x slower                                                |
| Geometric mean             | (ref)                                                  | 1.10x slower                                                         |

Benchmark hidden because not significant (1): docutils
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (20) of results/bm-20250107-3.14.0a3+-7de6e22-NOGIL/bm-20250107-darwin-arm64-kumaraditya303-fast_state-3.14.0a3+-7de6e22.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.084x slower

# HPT report

- Reliability score: 99.56% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 1.36x