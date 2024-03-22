# Results vs. 3.11.0

- fork: python
- ref: dcaf33a41d5d220523d7
- machine: darwin-arm64
- commit hash: dcaf33a
- commit date: 2024-03-20
- overall geometric mean: 1.30x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x slower
- Memory change: 1.49x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20240320-darwin-arm64-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 154 ms                                                 | 192 ms: 1.25x slower                                                   |
| chameleon      | 4.30 ms                                                | 4.46 ms: 1.04x slower                                                  |
| docutils       | 1.43 sec                                               | 2.60 sec: 1.82x slower                                                 |
| html5lib       | 33.0 ms                                                | 38.1 ms: 1.16x slower                                                  |
| tornado_http   | 69.1 ms                                                | 83.9 ms: 1.21x slower                                                  |
| Geometric mean | (ref)                                                  | 1.27x slower                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20240320-darwin-arm64-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_cpu_io_mixed_tg | 550 ms                                                 | 2.96 sec: 5.38x slower                                                 |
| async_tree_cpu_io_mixed    | 519 ms                                                 | 2.80 sec: 5.39x slower                                                 |
| async_tree_none            | 282 ms                                                 | 2.21 sec: 7.84x slower                                                 |
| async_tree_memoization     | 336 ms                                                 | 2.82 sec: 8.41x slower                                                 |
| async_tree_memoization_tg  | 352 ms                                                 | 2.96 sec: 8.41x slower                                                 |
| async_tree_none_tg         | 276 ms                                                 | 2.44 sec: 8.83x slower                                                 |
| async_tree_io              | 697 ms                                                 | 8.92 sec: 12.79x slower                                                |
| async_tree_io_tg           | 724 ms                                                 | 9.35 sec: 12.92x slower                                                |
| Geometric mean             | (ref)                                                  | 8.34x slower                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20240320-darwin-arm64-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pidigits       | 280 ms                                                 | 283 ms: 1.01x slower                                                   |
| nbody          | 61.7 ms                                                | 70.3 ms: 1.14x slower                                                  |
| float          | 50.8 ms                                                | 89.5 ms: 1.76x slower                                                  |
| Geometric mean | (ref)                                                  | 1.26x slower                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20240320-darwin-arm64-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_dna      | 148 ms                                                 | 152 ms: 1.03x slower                                                   |
| regex_effbot   | 2.43 ms                                                | 2.64 ms: 1.09x slower                                                  |
| regex_compile  | 72.8 ms                                                | 82.0 ms: 1.13x slower                                                  |
| regex_v8       | 15.1 ms                                                | 17.1 ms: 1.13x slower                                                  |
| Geometric mean | (ref)                                                  | 1.09x slower                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20240320-darwin-arm64-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| json_dumps           | 7.53 ms                                                | 6.39 ms: 1.18x faster                                                  |
| unpickle_pure_python | 149 us                                                 | 142 us: 1.04x faster                                                   |
| pickle_pure_python   | 191 us                                                 | 184 us: 1.04x faster                                                   |
| tomli_loads          | 1.27 sec                                               | 1.31 sec: 1.03x slower                                                 |
| pickle_dict          | 17.1 us                                                | 18.1 us: 1.06x slower                                                  |
| pickle               | 6.98 us                                                | 7.44 us: 1.07x slower                                                  |
| pickle_list          | 2.70 us                                                | 2.96 us: 1.10x slower                                                  |
| unpickle             | 8.29 us                                                | 9.11 us: 1.10x slower                                                  |
| json_loads           | 15.3 us                                                | 17.0 us: 1.11x slower                                                  |
| unpickle_list        | 2.69 us                                                | 3.05 us: 1.13x slower                                                  |
| xml_etree_process    | 33.6 ms                                                | 41.1 ms: 1.22x slower                                                  |
| xml_etree_parse      | 100 ms                                                 | 132 ms: 1.31x slower                                                   |
| xml_etree_generate   | 45.8 ms                                                | 60.2 ms: 1.31x slower                                                  |
| xml_etree_iterparse  | 68.3 ms                                                | 106 ms: 1.55x slower                                                   |
| Geometric mean       | (ref)                                                  | 1.11x slower                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20240320-darwin-arm64-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                | 17.8 ms: 1.65x slower                                                  |
| python_startup_no_site | 8.57 ms                                                | 16.1 ms: 1.88x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.76x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20240320-darwin-arm64-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 7.93 ms                                                | 6.90 ms: 1.15x faster                                                  |
| django_template | 20.1 ms                                                | 20.5 ms: 1.02x slower                                                  |
| genshi_text     | 14.4 ms                                                | 14.7 ms: 1.02x slower                                                  |
| genshi_xml      | 28.5 ms                                                | 35.7 ms: 1.25x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.03x slower                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20240320-darwin-arm64-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| typing_runtime_protocols   | 301 us                                                 | 69.6 us: 4.32x faster                                                  |
| asyncio_tcp                | 643 ms                                                 | 418 ms: 1.54x faster                                                   |
| chaos                      | 47.4 ms                                                | 38.6 ms: 1.23x faster                                                  |
| comprehensions             | 14.4 us                                                | 12.2 us: 1.18x faster                                                  |
| json_dumps                 | 7.53 ms                                                | 6.39 ms: 1.18x faster                                                  |
| mako                       | 7.93 ms                                                | 6.90 ms: 1.15x faster                                                  |
| raytrace                   | 206 ms                                                 | 179 ms: 1.15x faster                                                   |
| generators                 | 30.3 ms                                                | 27.1 ms: 1.12x faster                                                  |
| deltablue                  | 2.75 ms                                                | 2.46 ms: 1.12x faster                                                  |
| sqlglot_parse              | 890 us                                                 | 826 us: 1.08x faster                                                   |
| sympy_sum                  | 80.2 ms                                                | 75.0 ms: 1.07x faster                                                  |
| richards_super             | 37.3 ms                                                | 35.0 ms: 1.07x faster                                                  |
| asyncio_tcp_ssl            | 1.40 sec                                               | 1.31 sec: 1.06x faster                                                 |
| deepcopy_memo              | 25.7 us                                                | 24.4 us: 1.06x faster                                                  |
| sqlglot_transpile          | 1.05 ms                                                | 1.01 ms: 1.04x faster                                                  |
| unpickle_pure_python       | 149 us                                                 | 142 us: 1.04x faster                                                   |
| sympy_str                  | 144 ms                                                 | 138 ms: 1.04x faster                                                   |
| pickle_pure_python         | 191 us                                                 | 184 us: 1.04x faster                                                   |
| logging_simple             | 3.41 us                                                | 3.30 us: 1.03x faster                                                  |
| sympy_integrate            | 11.3 ms                                                | 11.0 ms: 1.02x faster                                                  |
| logging_format             | 3.67 us                                                | 3.60 us: 1.02x faster                                                  |
| logging_silent             | 66.5 ns                                                | 65.5 ns: 1.02x faster                                                  |
| deepcopy                   | 215 us                                                 | 213 us: 1.01x faster                                                   |
| crypto_pyaes               | 47.5 ms                                                | 47.0 ms: 1.01x faster                                                  |
| pidigits                   | 280 ms                                                 | 283 ms: 1.01x slower                                                   |
| django_template            | 20.1 ms                                                | 20.5 ms: 1.02x slower                                                  |
| richards                   | 31.1 ms                                                | 31.7 ms: 1.02x slower                                                  |
| gc_traversal               | 2.38 ms                                                | 2.43 ms: 1.02x slower                                                  |
| genshi_text                | 14.4 ms                                                | 14.7 ms: 1.02x slower                                                  |
| tomli_loads                | 1.27 sec                                               | 1.31 sec: 1.03x slower                                                 |
| regex_dna                  | 148 ms                                                 | 152 ms: 1.03x slower                                                   |
| scimark_monte_carlo        | 43.5 ms                                                | 44.7 ms: 1.03x slower                                                  |
| sympy_expand               | 229 ms                                                 | 236 ms: 1.03x slower                                                   |
| pprint_safe_repr           | 478 ms                                                 | 492 ms: 1.03x slower                                                   |
| coroutines                 | 17.2 ms                                                | 17.8 ms: 1.04x slower                                                  |
| chameleon                  | 4.30 ms                                                | 4.46 ms: 1.04x slower                                                  |
| deepcopy_reduce            | 1.79 us                                                | 1.86 us: 1.04x slower                                                  |
| meteor_contest             | 71.1 ms                                                | 73.9 ms: 1.04x slower                                                  |
| dulwich_log                | 28.6 ms                                                | 29.8 ms: 1.04x slower                                                  |
| pprint_pformat             | 979 ms                                                 | 1.02 sec: 1.05x slower                                                 |
| hexiom                     | 4.58 ms                                                | 4.82 ms: 1.05x slower                                                  |
| thrift                     | 410 us                                                 | 433 us: 1.05x slower                                                   |
| create_gc_cycles           | 711 us                                                 | 749 us: 1.05x slower                                                   |
| pickle_dict                | 17.1 us                                                | 18.1 us: 1.06x slower                                                  |
| bench_thread_pool          | 465 us                                                 | 493 us: 1.06x slower                                                   |
| pathlib                    | 23.2 ms                                                | 24.7 ms: 1.06x slower                                                  |
| json                       | 2.75 ms                                                | 2.93 ms: 1.07x slower                                                  |
| pickle                     | 6.98 us                                                | 7.44 us: 1.07x slower                                                  |
| coverage                   | 43.9 ms                                                | 47.2 ms: 1.08x slower                                                  |
| sqlglot_normalize          | 162 ms                                                 | 174 ms: 1.08x slower                                                   |
| mdp                        | 1.48 sec                                               | 1.60 sec: 1.08x slower                                                 |
| regex_effbot               | 2.43 ms                                                | 2.64 ms: 1.09x slower                                                  |
| fannkuch                   | 240 ms                                                 | 261 ms: 1.09x slower                                                   |
| pickle_list                | 2.70 us                                                | 2.96 us: 1.10x slower                                                  |
| unpickle                   | 8.29 us                                                | 9.11 us: 1.10x slower                                                  |
| nqueens                    | 55.9 ms                                                | 61.6 ms: 1.10x slower                                                  |
| json_loads                 | 15.3 us                                                | 17.0 us: 1.11x slower                                                  |
| scimark_sparse_mat_mult    | 2.81 ms                                                | 3.14 ms: 1.12x slower                                                  |
| regex_compile              | 72.8 ms                                                | 82.0 ms: 1.13x slower                                                  |
| regex_v8                   | 15.1 ms                                                | 17.1 ms: 1.13x slower                                                  |
| spectral_norm              | 65.7 ms                                                | 74.5 ms: 1.13x slower                                                  |
| unpickle_list              | 2.69 us                                                | 3.05 us: 1.13x slower                                                  |
| nbody                      | 61.7 ms                                                | 70.3 ms: 1.14x slower                                                  |
| aiohttp                    | 1.02 ms                                                | 1.17 ms: 1.14x slower                                                  |
| gunicorn                   | 1.10 ms                                                | 1.25 ms: 1.14x slower                                                  |
| scimark_fft                | 173 ms                                                 | 199 ms: 1.15x slower                                                   |
| html5lib                   | 33.0 ms                                                | 38.1 ms: 1.16x slower                                                  |
| pyflate                    | 284 ms                                                 | 330 ms: 1.16x slower                                                   |
| sqlglot_optimize           | 29.6 ms                                                | 34.7 ms: 1.17x slower                                                  |
| scimark_lu                 | 67.7 ms                                                | 81.4 ms: 1.20x slower                                                  |
| tornado_http               | 69.1 ms                                                | 83.9 ms: 1.21x slower                                                  |
| xml_etree_process          | 33.6 ms                                                | 41.1 ms: 1.22x slower                                                  |
| 2to3                       | 154 ms                                                 | 192 ms: 1.25x slower                                                   |
| genshi_xml                 | 28.5 ms                                                | 35.7 ms: 1.25x slower                                                  |
| sqlite_synth               | 1.26 us                                                | 1.59 us: 1.26x slower                                                  |
| pycparser                  | 659 ms                                                 | 840 ms: 1.27x slower                                                   |
| xml_etree_parse            | 100 ms                                                 | 132 ms: 1.31x slower                                                   |
| xml_etree_generate         | 45.8 ms                                                | 60.2 ms: 1.31x slower                                                  |
| bench_mp_pool              | 41.0 ms                                                | 54.0 ms: 1.32x slower                                                  |
| scimark_sor                | 79.2 ms                                                | 107 ms: 1.35x slower                                                   |
| mypy2                      | 372 ms                                                 | 531 ms: 1.42x slower                                                   |
| telco                      | 3.17 ms                                                | 4.57 ms: 1.44x slower                                                  |
| xml_etree_iterparse        | 68.3 ms                                                | 106 ms: 1.55x slower                                                   |
| python_startup             | 10.8 ms                                                | 17.8 ms: 1.65x slower                                                  |
| float                      | 50.8 ms                                                | 89.5 ms: 1.76x slower                                                  |
| async_generators           | 192 ms                                                 | 344 ms: 1.79x slower                                                   |
| docutils                   | 1.43 sec                                               | 2.60 sec: 1.82x slower                                                 |
| python_startup_no_site     | 8.57 ms                                                | 16.1 ms: 1.88x slower                                                  |
| dask                       | 219 ms                                                 | 456 ms: 2.08x slower                                                   |
| pylint                     | 253 ms                                                 | 588 ms: 2.33x slower                                                   |
| unpack_sequence            | 33.6 ns                                                | 113 ns: 3.35x slower                                                   |
| async_tree_cpu_io_mixed_tg | 550 ms                                                 | 2.96 sec: 5.38x slower                                                 |
| async_tree_cpu_io_mixed    | 519 ms                                                 | 2.80 sec: 5.39x slower                                                 |
| async_tree_none            | 282 ms                                                 | 2.21 sec: 7.84x slower                                                 |
| async_tree_memoization     | 336 ms                                                 | 2.82 sec: 8.41x slower                                                 |
| async_tree_memoization_tg  | 352 ms                                                 | 2.96 sec: 8.41x slower                                                 |
| async_tree_none_tg         | 276 ms                                                 | 2.44 sec: 8.83x slower                                                 |
| async_tree_io              | 697 ms                                                 | 8.92 sec: 12.79x slower                                                |
| async_tree_io_tg           | 724 ms                                                 | 9.35 sec: 12.92x slower                                                |
| Geometric mean             | (ref)                                                  | 1.30x slower                                                           |

Benchmark hidden because not significant (2): go, asyncio_websockets
Ignored benchmarks (3) of results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (8) of results/bm-20240320-3.13.0a5+-dcaf33a-JIT/bm-20240320-darwin-arm64-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg


# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.07x
- 95% likely to have a slowdown of 1.07x
- 99% likely to have a slowdown of 1.05x


# Memory

- memory change: 1.49x