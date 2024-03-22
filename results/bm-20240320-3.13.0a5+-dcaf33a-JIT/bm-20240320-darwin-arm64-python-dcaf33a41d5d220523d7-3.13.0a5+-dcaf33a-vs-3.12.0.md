# Results vs. 3.12.0

- fork: python
- ref: dcaf33a41d5d220523d7
- machine: darwin-arm64
- commit hash: dcaf33a
- commit date: 2024-03-20
- overall geometric mean: 1.26x slower
- HPT reliability: 99.78%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.43x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240320-darwin-arm64-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 169 ms                                                 | 192 ms: 1.14x slower                                                   |
| chameleon      | 4.70 ms                                                | 4.46 ms: 1.05x faster                                                  |
| docutils       | 1.50 sec                                               | 2.60 sec: 1.73x slower                                                 |
| tornado_http   | 69.3 ms                                                | 83.9 ms: 1.21x slower                                                  |
| Geometric mean | (ref)                                                  | 1.23x slower                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240320-darwin-arm64-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_cpu_io_mixed    | 526 ms                                                 | 2.80 sec: 5.32x slower                                                 |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 2.96 sec: 5.56x slower                                                 |
| async_tree_none            | 266 ms                                                 | 2.21 sec: 8.32x slower                                                 |
| async_tree_memoization     | 312 ms                                                 | 2.82 sec: 9.04x slower                                                 |
| async_tree_memoization_tg  | 323 ms                                                 | 2.96 sec: 9.18x slower                                                 |
| async_tree_none_tg         | 258 ms                                                 | 2.44 sec: 9.48x slower                                                 |
| async_tree_io              | 668 ms                                                 | 8.92 sec: 13.35x slower                                                |
| async_tree_io_tg           | 669 ms                                                 | 9.35 sec: 13.98x slower                                                |
| Geometric mean             | (ref)                                                  | 8.80x slower                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240320-darwin-arm64-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pidigits       | 282 ms                                                 | 283 ms: 1.00x slower                                                   |
| nbody          | 68.8 ms                                                | 70.3 ms: 1.02x slower                                                  |
| float          | 55.8 ms                                                | 89.5 ms: 1.60x slower                                                  |
| Geometric mean | (ref)                                                  | 1.18x slower                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240320-darwin-arm64-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_dna      | 154 ms                                                 | 152 ms: 1.01x faster                                                   |
| regex_compile  | 77.9 ms                                                | 82.0 ms: 1.05x slower                                                  |
| regex_v8       | 16.0 ms                                                | 17.1 ms: 1.07x slower                                                  |
| Geometric mean | (ref)                                                  | 1.03x slower                                                           |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240320-darwin-arm64-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 200 us                                                 | 184 us: 1.08x faster                                                   |
| tomli_loads          | 1.39 sec                                               | 1.31 sec: 1.07x faster                                                 |
| unpickle_pure_python | 151 us                                                 | 142 us: 1.06x faster                                                   |
| json_loads           | 17.2 us                                                | 17.0 us: 1.01x faster                                                  |
| pickle_dict          | 18.1 us                                                | 18.1 us: 1.00x slower                                                  |
| unpickle_list        | 3.02 us                                                | 3.05 us: 1.01x slower                                                  |
| pickle_list          | 2.89 us                                                | 2.96 us: 1.03x slower                                                  |
| json_dumps           | 6.22 ms                                                | 6.39 ms: 1.03x slower                                                  |
| pickle               | 7.23 us                                                | 7.44 us: 1.03x slower                                                  |
| xml_etree_process    | 39.7 ms                                                | 41.1 ms: 1.03x slower                                                  |
| xml_etree_generate   | 55.8 ms                                                | 60.2 ms: 1.08x slower                                                  |
| xml_etree_parse      | 106 ms                                                 | 132 ms: 1.24x slower                                                   |
| xml_etree_iterparse  | 74.0 ms                                                | 106 ms: 1.43x slower                                                   |
| Geometric mean       | (ref)                                                  | 1.04x slower                                                           |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240320-darwin-arm64-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 11.4 ms                                                | 17.8 ms: 1.56x slower                                                  |
| python_startup_no_site | 9.37 ms                                                | 16.1 ms: 1.72x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.64x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240320-darwin-arm64-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 7.71 ms                                                | 6.90 ms: 1.12x faster                                                  |
| django_template | 22.3 ms                                                | 20.5 ms: 1.09x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.10x faster                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240320-darwin-arm64-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| typing_runtime_protocols   | 93.0 us                                                | 69.6 us: 1.34x faster                                                  |
| comprehensions             | 14.5 us                                                | 12.2 us: 1.19x faster                                                  |
| raytrace                   | 212 ms                                                 | 179 ms: 1.18x faster                                                   |
| logging_silent             | 76.4 ns                                                | 65.5 ns: 1.17x faster                                                  |
| generators                 | 31.1 ms                                                | 27.1 ms: 1.15x faster                                                  |
| deepcopy_memo              | 27.7 us                                                | 24.4 us: 1.13x faster                                                  |
| mako                       | 7.71 ms                                                | 6.90 ms: 1.12x faster                                                  |
| logging_simple             | 3.69 us                                                | 3.30 us: 1.12x faster                                                  |
| deepcopy_reduce            | 2.07 us                                                | 1.86 us: 1.11x faster                                                  |
| logging_format             | 3.98 us                                                | 3.60 us: 1.11x faster                                                  |
| crypto_pyaes               | 51.9 ms                                                | 47.0 ms: 1.10x faster                                                  |
| chaos                      | 42.5 ms                                                | 38.6 ms: 1.10x faster                                                  |
| deepcopy                   | 235 us                                                 | 213 us: 1.10x faster                                                   |
| deltablue                  | 2.71 ms                                                | 2.46 ms: 1.10x faster                                                  |
| django_template            | 22.3 ms                                                | 20.5 ms: 1.09x faster                                                  |
| pickle_pure_python         | 200 us                                                 | 184 us: 1.08x faster                                                   |
| coroutines                 | 19.2 ms                                                | 17.8 ms: 1.08x faster                                                  |
| asyncio_tcp                | 449 ms                                                 | 418 ms: 1.07x faster                                                   |
| sympy_str                  | 148 ms                                                 | 138 ms: 1.07x faster                                                   |
| tomli_loads                | 1.39 sec                                               | 1.31 sec: 1.07x faster                                                 |
| sqlglot_normalize          | 186 ms                                                 | 174 ms: 1.07x faster                                                   |
| unpickle_pure_python       | 151 us                                                 | 142 us: 1.06x faster                                                   |
| chameleon                  | 4.70 ms                                                | 4.46 ms: 1.05x faster                                                  |
| json                       | 3.09 ms                                                | 2.93 ms: 1.05x faster                                                  |
| sympy_sum                  | 77.6 ms                                                | 75.0 ms: 1.03x faster                                                  |
| sympy_integrate            | 11.4 ms                                                | 11.0 ms: 1.03x faster                                                  |
| richards_super             | 36.0 ms                                                | 35.0 ms: 1.03x faster                                                  |
| spectral_norm              | 76.4 ms                                                | 74.5 ms: 1.03x faster                                                  |
| sqlglot_parse              | 848 us                                                 | 826 us: 1.03x faster                                                   |
| sympy_expand               | 241 ms                                                 | 236 ms: 1.02x faster                                                   |
| bench_thread_pool          | 504 us                                                 | 493 us: 1.02x faster                                                   |
| regex_dna                  | 154 ms                                                 | 152 ms: 1.01x faster                                                   |
| sqlglot_transpile          | 1.02 ms                                                | 1.01 ms: 1.01x faster                                                  |
| richards                   | 32.1 ms                                                | 31.7 ms: 1.01x faster                                                  |
| nqueens                    | 62.4 ms                                                | 61.6 ms: 1.01x faster                                                  |
| json_loads                 | 17.2 us                                                | 17.0 us: 1.01x faster                                                  |
| pprint_safe_repr           | 497 ms                                                 | 492 ms: 1.01x faster                                                   |
| scimark_monte_carlo        | 45.0 ms                                                | 44.7 ms: 1.01x faster                                                  |
| asyncio_websockets         | 409 ms                                                 | 409 ms: 1.00x faster                                                   |
| pickle_dict                | 18.1 us                                                | 18.1 us: 1.00x slower                                                  |
| pidigits                   | 282 ms                                                 | 283 ms: 1.00x slower                                                   |
| unpickle_list              | 3.02 us                                                | 3.05 us: 1.01x slower                                                  |
| sqlite_synth               | 1.57 us                                                | 1.59 us: 1.01x slower                                                  |
| pprint_pformat             | 1.01 sec                                               | 1.02 sec: 1.01x slower                                                 |
| mdp                        | 1.58 sec                                               | 1.60 sec: 1.01x slower                                                 |
| gc_traversal               | 2.40 ms                                                | 2.43 ms: 1.01x slower                                                  |
| sqlglot_optimize           | 34.0 ms                                                | 34.7 ms: 1.02x slower                                                  |
| pathlib                    | 24.2 ms                                                | 24.7 ms: 1.02x slower                                                  |
| scimark_fft                | 195 ms                                                 | 199 ms: 1.02x slower                                                   |
| nbody                      | 68.8 ms                                                | 70.3 ms: 1.02x slower                                                  |
| pickle_list                | 2.89 us                                                | 2.96 us: 1.03x slower                                                  |
| json_dumps                 | 6.22 ms                                                | 6.39 ms: 1.03x slower                                                  |
| pickle                     | 7.23 us                                                | 7.44 us: 1.03x slower                                                  |
| meteor_contest             | 71.7 ms                                                | 73.9 ms: 1.03x slower                                                  |
| xml_etree_process          | 39.7 ms                                                | 41.1 ms: 1.03x slower                                                  |
| go                         | 102 ms                                                 | 105 ms: 1.04x slower                                                   |
| pyflate                    | 316 ms                                                 | 330 ms: 1.05x slower                                                   |
| fannkuch                   | 248 ms                                                 | 261 ms: 1.05x slower                                                   |
| regex_compile              | 77.9 ms                                                | 82.0 ms: 1.05x slower                                                  |
| asyncio_tcp_ssl            | 1.24 sec                                               | 1.31 sec: 1.06x slower                                                 |
| hexiom                     | 4.54 ms                                                | 4.82 ms: 1.06x slower                                                  |
| create_gc_cycles           | 701 us                                                 | 749 us: 1.07x slower                                                   |
| scimark_lu                 | 76.0 ms                                                | 81.4 ms: 1.07x slower                                                  |
| regex_v8                   | 16.0 ms                                                | 17.1 ms: 1.07x slower                                                  |
| xml_etree_generate         | 55.8 ms                                                | 60.2 ms: 1.08x slower                                                  |
| aiohttp                    | 1.08 ms                                                | 1.17 ms: 1.08x slower                                                  |
| gunicorn                   | 1.15 ms                                                | 1.25 ms: 1.09x slower                                                  |
| async_generators           | 304 ms                                                 | 344 ms: 1.13x slower                                                   |
| 2to3                       | 169 ms                                                 | 192 ms: 1.14x slower                                                   |
| bench_mp_pool              | 44.9 ms                                                | 54.0 ms: 1.20x slower                                                  |
| tornado_http               | 69.3 ms                                                | 83.9 ms: 1.21x slower                                                  |
| coverage                   | 38.9 ms                                                | 47.2 ms: 1.21x slower                                                  |
| scimark_sor                | 87.4 ms                                                | 107 ms: 1.23x slower                                                   |
| xml_etree_parse            | 106 ms                                                 | 132 ms: 1.24x slower                                                   |
| pycparser                  | 677 ms                                                 | 840 ms: 1.24x slower                                                   |
| telco                      | 3.68 ms                                                | 4.57 ms: 1.24x slower                                                  |
| mypy2                      | 380 ms                                                 | 531 ms: 1.40x slower                                                   |
| xml_etree_iterparse        | 74.0 ms                                                | 106 ms: 1.43x slower                                                   |
| python_startup             | 11.4 ms                                                | 17.8 ms: 1.56x slower                                                  |
| float                      | 55.8 ms                                                | 89.5 ms: 1.60x slower                                                  |
| python_startup_no_site     | 9.37 ms                                                | 16.1 ms: 1.72x slower                                                  |
| docutils                   | 1.50 sec                                               | 2.60 sec: 1.73x slower                                                 |
| dask                       | 222 ms                                                 | 456 ms: 2.05x slower                                                   |
| unpack_sequence            | 31.5 ns                                                | 113 ns: 3.59x slower                                                   |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 2.80 sec: 5.32x slower                                                 |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 2.96 sec: 5.56x slower                                                 |
| async_tree_none            | 266 ms                                                 | 2.21 sec: 8.32x slower                                                 |
| async_tree_memoization     | 312 ms                                                 | 2.82 sec: 9.04x slower                                                 |
| async_tree_memoization_tg  | 323 ms                                                 | 2.96 sec: 9.18x slower                                                 |
| async_tree_none_tg         | 258 ms                                                 | 2.44 sec: 9.48x slower                                                 |
| async_tree_io              | 668 ms                                                 | 8.92 sec: 13.35x slower                                                |
| async_tree_io_tg           | 669 ms                                                 | 9.35 sec: 13.98x slower                                                |
| Geometric mean             | (ref)                                                  | 1.26x slower                                                           |

Benchmark hidden because not significant (4): dulwich_log, unpickle, regex_effbot, scimark_sparse_mat_mult
Ignored benchmarks (2) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (13) of results/bm-20240320-3.13.0a5+-dcaf33a-JIT/bm-20240320-darwin-arm64-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, genshi_text, genshi_xml, html5lib, pylint, thrift


# HPT report

- Reliability score: 99.78% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x


# Memory

- memory change: 1.43x