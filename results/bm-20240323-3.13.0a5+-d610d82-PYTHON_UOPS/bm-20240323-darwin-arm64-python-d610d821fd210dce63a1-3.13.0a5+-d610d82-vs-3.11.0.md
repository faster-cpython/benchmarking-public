# Results vs. 3.11.0

- fork: python
- ref: d610d821fd210dce63a1
- machine: darwin-arm64
- commit hash: d610d82
- commit date: 2024-03-23
- overall geometric mean: 1.08x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x slower
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20240323-darwin-arm64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 154 ms                                                 | 177 ms: 1.15x slower                                                   |
| chameleon      | 4.30 ms                                                | 4.71 ms: 1.09x slower                                                  |
| docutils       | 1.43 sec                                               | 1.60 sec: 1.12x slower                                                 |
| html5lib       | 33.0 ms                                                | 35.0 ms: 1.06x slower                                                  |
| tornado_http   | 69.1 ms                                                | 81.6 ms: 1.18x slower                                                  |
| Geometric mean | (ref)                                                  | 1.12x slower                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20240323-darwin-arm64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 352 ms                                                 | 260 ms: 1.35x faster                                                   |
| async_tree_none_tg         | 276 ms                                                 | 216 ms: 1.28x faster                                                   |
| async_tree_memoization     | 336 ms                                                 | 264 ms: 1.27x faster                                                   |
| async_tree_io_tg           | 724 ms                                                 | 591 ms: 1.23x faster                                                   |
| async_tree_none            | 282 ms                                                 | 230 ms: 1.22x faster                                                   |
| async_tree_cpu_io_mixed_tg | 550 ms                                                 | 455 ms: 1.21x faster                                                   |
| async_tree_io              | 697 ms                                                 | 583 ms: 1.19x faster                                                   |
| async_tree_cpu_io_mixed    | 519 ms                                                 | 466 ms: 1.11x faster                                                   |
| Geometric mean             | (ref)                                                  | 1.23x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20240323-darwin-arm64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pidigits       | 280 ms                                                 | 283 ms: 1.01x slower                                                   |
| float          | 50.8 ms                                                | 66.6 ms: 1.31x slower                                                  |
| nbody          | 61.7 ms                                                | 86.0 ms: 1.39x slower                                                  |
| Geometric mean | (ref)                                                  | 1.23x slower                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20240323-darwin-arm64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_dna      | 148 ms                                                 | 151 ms: 1.02x slower                                                   |
| regex_effbot   | 2.43 ms                                                | 2.55 ms: 1.05x slower                                                  |
| regex_v8       | 15.1 ms                                                | 17.2 ms: 1.13x slower                                                  |
| regex_compile  | 72.8 ms                                                | 95.0 ms: 1.30x slower                                                  |
| Geometric mean | (ref)                                                  | 1.12x slower                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20240323-darwin-arm64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| json_dumps           | 7.53 ms                                                | 6.48 ms: 1.16x faster                                                  |
| xml_etree_parse      | 100 ms                                                 | 98.9 ms: 1.01x faster                                                  |
| pickle_pure_python   | 191 us                                                 | 190 us: 1.01x faster                                                   |
| pickle               | 6.98 us                                                | 7.25 us: 1.04x slower                                                  |
| pickle_dict          | 17.1 us                                                | 18.1 us: 1.06x slower                                                  |
| pickle_list          | 2.70 us                                                | 2.96 us: 1.10x slower                                                  |
| xml_etree_iterparse  | 68.3 ms                                                | 75.2 ms: 1.10x slower                                                  |
| unpickle             | 8.29 us                                                | 9.14 us: 1.10x slower                                                  |
| json_loads           | 15.3 us                                                | 17.0 us: 1.10x slower                                                  |
| unpickle_list        | 2.69 us                                                | 3.07 us: 1.14x slower                                                  |
| xml_etree_process    | 33.6 ms                                                | 39.8 ms: 1.19x slower                                                  |
| unpickle_pure_python | 149 us                                                 | 186 us: 1.25x slower                                                   |
| xml_etree_generate   | 45.8 ms                                                | 57.9 ms: 1.26x slower                                                  |
| tomli_loads          | 1.27 sec                                               | 1.68 sec: 1.32x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.10x slower                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20240323-darwin-arm64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                | 14.8 ms: 1.37x slower                                                  |
| python_startup_no_site | 8.57 ms                                                | 13.0 ms: 1.52x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.45x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20240323-darwin-arm64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 20.1 ms                                                | 22.4 ms: 1.11x slower                                                  |
| genshi_text     | 14.4 ms                                                | 16.5 ms: 1.14x slower                                                  |
| mako            | 7.93 ms                                                | 9.45 ms: 1.19x slower                                                  |
| genshi_xml      | 28.5 ms                                                | 34.5 ms: 1.21x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.16x slower                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20240323-darwin-arm64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| typing_runtime_protocols   | 301 us                                                 | 72.4 us: 4.16x faster                                                  |
| asyncio_tcp                | 643 ms                                                 | 409 ms: 1.57x faster                                                   |
| pylint                     | 253 ms                                                 | 181 ms: 1.39x faster                                                   |
| async_tree_memoization_tg  | 352 ms                                                 | 260 ms: 1.35x faster                                                   |
| async_tree_none_tg         | 276 ms                                                 | 216 ms: 1.28x faster                                                   |
| async_tree_memoization     | 336 ms                                                 | 264 ms: 1.27x faster                                                   |
| async_tree_io_tg           | 724 ms                                                 | 591 ms: 1.23x faster                                                   |
| async_tree_none            | 282 ms                                                 | 230 ms: 1.22x faster                                                   |
| async_tree_cpu_io_mixed_tg | 550 ms                                                 | 455 ms: 1.21x faster                                                   |
| async_tree_io              | 697 ms                                                 | 583 ms: 1.19x faster                                                   |
| json_dumps                 | 7.53 ms                                                | 6.48 ms: 1.16x faster                                                  |
| async_tree_cpu_io_mixed    | 519 ms                                                 | 466 ms: 1.11x faster                                                   |
| generators                 | 30.3 ms                                                | 27.4 ms: 1.10x faster                                                  |
| sqlglot_parse              | 890 us                                                 | 819 us: 1.09x faster                                                   |
| sqlglot_transpile          | 1.05 ms                                                | 988 us: 1.06x faster                                                   |
| asyncio_tcp_ssl            | 1.40 sec                                               | 1.31 sec: 1.06x faster                                                 |
| deltablue                  | 2.75 ms                                                | 2.60 ms: 1.06x faster                                                  |
| chaos                      | 47.4 ms                                                | 45.0 ms: 1.05x faster                                                  |
| raytrace                   | 206 ms                                                 | 200 ms: 1.03x faster                                                   |
| xml_etree_parse            | 100 ms                                                 | 98.9 ms: 1.01x faster                                                  |
| pickle_pure_python         | 191 us                                                 | 190 us: 1.01x faster                                                   |
| logging_format             | 3.67 us                                                | 3.69 us: 1.01x slower                                                  |
| gc_traversal               | 2.38 ms                                                | 2.40 ms: 1.01x slower                                                  |
| sympy_sum                  | 80.2 ms                                                | 80.9 ms: 1.01x slower                                                  |
| pidigits                   | 280 ms                                                 | 283 ms: 1.01x slower                                                   |
| create_gc_cycles           | 711 us                                                 | 718 us: 1.01x slower                                                   |
| regex_dna                  | 148 ms                                                 | 151 ms: 1.02x slower                                                   |
| coroutines                 | 17.2 ms                                                | 17.6 ms: 1.02x slower                                                  |
| logging_silent             | 66.5 ns                                                | 68.2 ns: 1.03x slower                                                  |
| dask                       | 219 ms                                                 | 226 ms: 1.03x slower                                                   |
| deepcopy                   | 215 us                                                 | 223 us: 1.03x slower                                                   |
| pickle                     | 6.98 us                                                | 7.25 us: 1.04x slower                                                  |
| dulwich_log                | 28.6 ms                                                | 29.8 ms: 1.04x slower                                                  |
| sympy_integrate            | 11.3 ms                                                | 11.8 ms: 1.05x slower                                                  |
| unpack_sequence            | 33.6 ns                                                | 35.3 ns: 1.05x slower                                                  |
| richards_super             | 37.3 ms                                                | 39.2 ms: 1.05x slower                                                  |
| sympy_str                  | 144 ms                                                 | 151 ms: 1.05x slower                                                   |
| regex_effbot               | 2.43 ms                                                | 2.55 ms: 1.05x slower                                                  |
| html5lib                   | 33.0 ms                                                | 35.0 ms: 1.06x slower                                                  |
| pickle_dict                | 17.1 us                                                | 18.1 us: 1.06x slower                                                  |
| pathlib                    | 23.2 ms                                                | 24.6 ms: 1.06x slower                                                  |
| pycparser                  | 659 ms                                                 | 702 ms: 1.06x slower                                                   |
| coverage                   | 43.9 ms                                                | 47.0 ms: 1.07x slower                                                  |
| gunicorn                   | 1.10 ms                                                | 1.17 ms: 1.07x slower                                                  |
| sympy_expand               | 229 ms                                                 | 246 ms: 1.07x slower                                                   |
| deepcopy_reduce            | 1.79 us                                                | 1.92 us: 1.07x slower                                                  |
| thrift                     | 410 us                                                 | 441 us: 1.08x slower                                                   |
| deepcopy_memo              | 25.7 us                                                | 27.7 us: 1.08x slower                                                  |
| json                       | 2.75 ms                                                | 2.96 ms: 1.08x slower                                                  |
| bench_thread_pool          | 465 us                                                 | 508 us: 1.09x slower                                                   |
| mdp                        | 1.48 sec                                               | 1.62 sec: 1.09x slower                                                 |
| chameleon                  | 4.30 ms                                                | 4.71 ms: 1.09x slower                                                  |
| aiohttp                    | 1.02 ms                                                | 1.12 ms: 1.10x slower                                                  |
| go                         | 105 ms                                                 | 116 ms: 1.10x slower                                                   |
| pickle_list                | 2.70 us                                                | 2.96 us: 1.10x slower                                                  |
| xml_etree_iterparse        | 68.3 ms                                                | 75.2 ms: 1.10x slower                                                  |
| unpickle                   | 8.29 us                                                | 9.14 us: 1.10x slower                                                  |
| json_loads                 | 15.3 us                                                | 17.0 us: 1.10x slower                                                  |
| comprehensions             | 14.4 us                                                | 16.0 us: 1.11x slower                                                  |
| django_template            | 20.1 ms                                                | 22.4 ms: 1.11x slower                                                  |
| docutils                   | 1.43 sec                                               | 1.60 sec: 1.12x slower                                                 |
| bench_mp_pool              | 41.0 ms                                                | 46.0 ms: 1.12x slower                                                  |
| regex_v8                   | 15.1 ms                                                | 17.2 ms: 1.13x slower                                                  |
| unpickle_list              | 2.69 us                                                | 3.07 us: 1.14x slower                                                  |
| genshi_text                | 14.4 ms                                                | 16.5 ms: 1.14x slower                                                  |
| meteor_contest             | 71.1 ms                                                | 81.3 ms: 1.14x slower                                                  |
| 2to3                       | 154 ms                                                 | 177 ms: 1.15x slower                                                   |
| sqlglot_normalize          | 162 ms                                                 | 188 ms: 1.16x slower                                                   |
| richards                   | 31.1 ms                                                | 36.0 ms: 1.16x slower                                                  |
| tornado_http               | 69.1 ms                                                | 81.6 ms: 1.18x slower                                                  |
| xml_etree_process          | 33.6 ms                                                | 39.8 ms: 1.19x slower                                                  |
| mako                       | 7.93 ms                                                | 9.45 ms: 1.19x slower                                                  |
| crypto_pyaes               | 47.5 ms                                                | 56.8 ms: 1.20x slower                                                  |
| genshi_xml                 | 28.5 ms                                                | 34.5 ms: 1.21x slower                                                  |
| sqlglot_optimize           | 29.6 ms                                                | 36.0 ms: 1.22x slower                                                  |
| pprint_pformat             | 979 ms                                                 | 1.20 sec: 1.23x slower                                                 |
| pprint_safe_repr           | 478 ms                                                 | 588 ms: 1.23x slower                                                   |
| unpickle_pure_python       | 149 us                                                 | 186 us: 1.25x slower                                                   |
| xml_etree_generate         | 45.8 ms                                                | 57.9 ms: 1.26x slower                                                  |
| sqlite_synth               | 1.26 us                                                | 1.63 us: 1.30x slower                                                  |
| regex_compile              | 72.8 ms                                                | 95.0 ms: 1.30x slower                                                  |
| nqueens                    | 55.9 ms                                                | 73.1 ms: 1.31x slower                                                  |
| float                      | 50.8 ms                                                | 66.6 ms: 1.31x slower                                                  |
| tomli_loads                | 1.27 sec                                               | 1.68 sec: 1.32x slower                                                 |
| mypy2                      | 372 ms                                                 | 495 ms: 1.33x slower                                                   |
| hexiom                     | 4.58 ms                                                | 6.15 ms: 1.34x slower                                                  |
| python_startup             | 10.8 ms                                                | 14.8 ms: 1.37x slower                                                  |
| scimark_monte_carlo        | 43.5 ms                                                | 60.6 ms: 1.39x slower                                                  |
| nbody                      | 61.7 ms                                                | 86.0 ms: 1.39x slower                                                  |
| scimark_sparse_mat_mult    | 2.81 ms                                                | 3.98 ms: 1.41x slower                                                  |
| scimark_fft                | 173 ms                                                 | 245 ms: 1.42x slower                                                   |
| scimark_sor                | 79.2 ms                                                | 113 ms: 1.43x slower                                                   |
| pyflate                    | 284 ms                                                 | 409 ms: 1.44x slower                                                   |
| fannkuch                   | 240 ms                                                 | 349 ms: 1.46x slower                                                   |
| scimark_lu                 | 67.7 ms                                                | 99.8 ms: 1.47x slower                                                  |
| telco                      | 3.17 ms                                                | 4.78 ms: 1.51x slower                                                  |
| python_startup_no_site     | 8.57 ms                                                | 13.0 ms: 1.52x slower                                                  |
| async_generators           | 192 ms                                                 | 299 ms: 1.56x slower                                                   |
| spectral_norm              | 65.7 ms                                                | 103 ms: 1.56x slower                                                   |
| Geometric mean             | (ref)                                                  | 1.08x slower                                                           |

Benchmark hidden because not significant (2): asyncio_websockets, logging_simple
Ignored benchmarks (3) of results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (8) of results/bm-20240323-3.13.0a5+-d610d82-PYTHON_UOPS/bm-20240323-darwin-arm64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg


# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.06x
- 95% likely to have a slowdown of 1.05x
- 99% likely to have a slowdown of 1.04x


# Memory

- memory change: 1.08x