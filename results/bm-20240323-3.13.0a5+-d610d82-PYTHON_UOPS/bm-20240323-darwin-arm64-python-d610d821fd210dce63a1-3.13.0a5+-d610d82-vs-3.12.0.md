# Results vs. 3.12.0

- fork: python
- ref: d610d821fd210dce63a1
- machine: darwin-arm64
- commit hash: d610d82
- commit date: 2024-03-23
- overall geometric mean: 1.05x slower
- HPT reliability: 99.93%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240323-darwin-arm64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 169 ms                                                 | 177 ms: 1.04x slower                                                   |
| docutils       | 1.50 sec                                               | 1.60 sec: 1.06x slower                                                 |
| tornado_http   | 69.3 ms                                                | 81.6 ms: 1.18x slower                                                  |
| Geometric mean | (ref)                                                  | 1.07x slower                                                           |

Benchmark hidden because not significant (1): chameleon

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240323-darwin-arm64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 323 ms                                                 | 260 ms: 1.24x faster                                                   |
| async_tree_none_tg         | 258 ms                                                 | 216 ms: 1.19x faster                                                   |
| async_tree_memoization     | 312 ms                                                 | 264 ms: 1.18x faster                                                   |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 455 ms: 1.17x faster                                                   |
| async_tree_none            | 266 ms                                                 | 230 ms: 1.15x faster                                                   |
| async_tree_io              | 668 ms                                                 | 583 ms: 1.14x faster                                                   |
| async_tree_io_tg           | 669 ms                                                 | 591 ms: 1.13x faster                                                   |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 466 ms: 1.13x faster                                                   |
| Geometric mean             | (ref)                                                  | 1.17x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240323-darwin-arm64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pidigits       | 282 ms                                                 | 283 ms: 1.01x slower                                                   |
| float          | 55.8 ms                                                | 66.6 ms: 1.19x slower                                                  |
| nbody          | 68.8 ms                                                | 86.0 ms: 1.25x slower                                                  |
| Geometric mean | (ref)                                                  | 1.14x slower                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240323-darwin-arm64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 2.64 ms                                                | 2.55 ms: 1.03x faster                                                  |
| regex_dna      | 154 ms                                                 | 151 ms: 1.02x faster                                                   |
| regex_v8       | 16.0 ms                                                | 17.2 ms: 1.07x slower                                                  |
| regex_compile  | 77.9 ms                                                | 95.0 ms: 1.22x slower                                                  |
| Geometric mean | (ref)                                                  | 1.06x slower                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240323-darwin-arm64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_parse      | 106 ms                                                 | 98.9 ms: 1.08x faster                                                  |
| pickle_pure_python   | 200 us                                                 | 190 us: 1.05x faster                                                   |
| json_loads           | 17.2 us                                                | 17.0 us: 1.02x faster                                                  |
| pickle               | 7.23 us                                                | 7.25 us: 1.00x slower                                                  |
| xml_etree_process    | 39.7 ms                                                | 39.8 ms: 1.00x slower                                                  |
| unpickle_list        | 3.02 us                                                | 3.07 us: 1.02x slower                                                  |
| xml_etree_iterparse  | 74.0 ms                                                | 75.2 ms: 1.02x slower                                                  |
| pickle_list          | 2.89 us                                                | 2.96 us: 1.03x slower                                                  |
| xml_etree_generate   | 55.8 ms                                                | 57.9 ms: 1.04x slower                                                  |
| json_dumps           | 6.22 ms                                                | 6.48 ms: 1.04x slower                                                  |
| tomli_loads          | 1.39 sec                                               | 1.68 sec: 1.21x slower                                                 |
| unpickle_pure_python | 151 us                                                 | 186 us: 1.24x slower                                                   |
| Geometric mean       | (ref)                                                  | 1.03x slower                                                           |

Benchmark hidden because not significant (2): unpickle, pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240323-darwin-arm64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 11.4 ms                                                | 14.8 ms: 1.30x slower                                                  |
| python_startup_no_site | 9.37 ms                                                | 13.0 ms: 1.39x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.34x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240323-darwin-arm64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 22.3 ms                                                | 22.4 ms: 1.00x slower                                                  |
| mako            | 7.71 ms                                                | 9.45 ms: 1.22x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.11x slower                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240323-darwin-arm64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| typing_runtime_protocols   | 93.0 us                                                | 72.4 us: 1.28x faster                                                  |
| async_tree_memoization_tg  | 323 ms                                                 | 260 ms: 1.24x faster                                                   |
| async_tree_none_tg         | 258 ms                                                 | 216 ms: 1.19x faster                                                   |
| async_tree_memoization     | 312 ms                                                 | 264 ms: 1.18x faster                                                   |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 455 ms: 1.17x faster                                                   |
| async_tree_none            | 266 ms                                                 | 230 ms: 1.15x faster                                                   |
| async_tree_io              | 668 ms                                                 | 583 ms: 1.14x faster                                                   |
| async_tree_io_tg           | 669 ms                                                 | 591 ms: 1.13x faster                                                   |
| generators                 | 31.1 ms                                                | 27.4 ms: 1.13x faster                                                  |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 466 ms: 1.13x faster                                                   |
| logging_silent             | 76.4 ns                                                | 68.2 ns: 1.12x faster                                                  |
| asyncio_tcp                | 449 ms                                                 | 409 ms: 1.10x faster                                                   |
| coroutines                 | 19.2 ms                                                | 17.6 ms: 1.09x faster                                                  |
| logging_simple             | 3.69 us                                                | 3.41 us: 1.08x faster                                                  |
| logging_format             | 3.98 us                                                | 3.69 us: 1.08x faster                                                  |
| deepcopy_reduce            | 2.07 us                                                | 1.92 us: 1.08x faster                                                  |
| xml_etree_parse            | 106 ms                                                 | 98.9 ms: 1.08x faster                                                  |
| raytrace                   | 212 ms                                                 | 200 ms: 1.06x faster                                                   |
| pickle_pure_python         | 200 us                                                 | 190 us: 1.05x faster                                                   |
| deepcopy                   | 235 us                                                 | 223 us: 1.05x faster                                                   |
| json                       | 3.09 ms                                                | 2.96 ms: 1.04x faster                                                  |
| deltablue                  | 2.71 ms                                                | 2.60 ms: 1.04x faster                                                  |
| sqlglot_parse              | 848 us                                                 | 819 us: 1.04x faster                                                   |
| regex_effbot               | 2.64 ms                                                | 2.55 ms: 1.03x faster                                                  |
| sqlglot_transpile          | 1.02 ms                                                | 988 us: 1.03x faster                                                   |
| regex_dna                  | 154 ms                                                 | 151 ms: 1.02x faster                                                   |
| async_generators           | 304 ms                                                 | 299 ms: 1.02x faster                                                   |
| json_loads                 | 17.2 us                                                | 17.0 us: 1.02x faster                                                  |
| asyncio_websockets         | 409 ms                                                 | 408 ms: 1.00x faster                                                   |
| django_template            | 22.3 ms                                                | 22.4 ms: 1.00x slower                                                  |
| pickle                     | 7.23 us                                                | 7.25 us: 1.00x slower                                                  |
| xml_etree_process          | 39.7 ms                                                | 39.8 ms: 1.00x slower                                                  |
| pidigits                   | 282 ms                                                 | 283 ms: 1.01x slower                                                   |
| bench_thread_pool          | 504 us                                                 | 508 us: 1.01x slower                                                   |
| sqlglot_normalize          | 186 ms                                                 | 188 ms: 1.01x slower                                                   |
| unpickle_list              | 3.02 us                                                | 3.07 us: 1.02x slower                                                  |
| pathlib                    | 24.2 ms                                                | 24.6 ms: 1.02x slower                                                  |
| xml_etree_iterparse        | 74.0 ms                                                | 75.2 ms: 1.02x slower                                                  |
| sympy_expand               | 241 ms                                                 | 246 ms: 1.02x slower                                                   |
| dask                       | 222 ms                                                 | 226 ms: 1.02x slower                                                   |
| sympy_str                  | 148 ms                                                 | 151 ms: 1.02x slower                                                   |
| create_gc_cycles           | 701 us                                                 | 718 us: 1.02x slower                                                   |
| pickle_list                | 2.89 us                                                | 2.96 us: 1.03x slower                                                  |
| bench_mp_pool              | 44.9 ms                                                | 46.0 ms: 1.03x slower                                                  |
| mdp                        | 1.58 sec                                               | 1.62 sec: 1.03x slower                                                 |
| xml_etree_generate         | 55.8 ms                                                | 57.9 ms: 1.04x slower                                                  |
| pycparser                  | 677 ms                                                 | 702 ms: 1.04x slower                                                   |
| sqlite_synth               | 1.57 us                                                | 1.63 us: 1.04x slower                                                  |
| sympy_integrate            | 11.4 ms                                                | 11.8 ms: 1.04x slower                                                  |
| aiohttp                    | 1.08 ms                                                | 1.12 ms: 1.04x slower                                                  |
| json_dumps                 | 6.22 ms                                                | 6.48 ms: 1.04x slower                                                  |
| sympy_sum                  | 77.6 ms                                                | 80.9 ms: 1.04x slower                                                  |
| 2to3                       | 169 ms                                                 | 177 ms: 1.04x slower                                                   |
| asyncio_tcp_ssl            | 1.24 sec                                               | 1.31 sec: 1.06x slower                                                 |
| sqlglot_optimize           | 34.0 ms                                                | 36.0 ms: 1.06x slower                                                  |
| chaos                      | 42.5 ms                                                | 45.0 ms: 1.06x slower                                                  |
| docutils                   | 1.50 sec                                               | 1.60 sec: 1.06x slower                                                 |
| regex_v8                   | 16.0 ms                                                | 17.2 ms: 1.07x slower                                                  |
| richards_super             | 36.0 ms                                                | 39.2 ms: 1.09x slower                                                  |
| crypto_pyaes               | 51.9 ms                                                | 56.8 ms: 1.09x slower                                                  |
| comprehensions             | 14.5 us                                                | 16.0 us: 1.10x slower                                                  |
| richards                   | 32.1 ms                                                | 36.0 ms: 1.12x slower                                                  |
| unpack_sequence            | 31.5 ns                                                | 35.3 ns: 1.12x slower                                                  |
| meteor_contest             | 71.7 ms                                                | 81.3 ms: 1.13x slower                                                  |
| go                         | 102 ms                                                 | 116 ms: 1.14x slower                                                   |
| nqueens                    | 62.4 ms                                                | 73.1 ms: 1.17x slower                                                  |
| tornado_http               | 69.3 ms                                                | 81.6 ms: 1.18x slower                                                  |
| pprint_safe_repr           | 497 ms                                                 | 588 ms: 1.18x slower                                                   |
| pprint_pformat             | 1.01 sec                                               | 1.20 sec: 1.19x slower                                                 |
| float                      | 55.8 ms                                                | 66.6 ms: 1.19x slower                                                  |
| tomli_loads                | 1.39 sec                                               | 1.68 sec: 1.21x slower                                                 |
| coverage                   | 38.9 ms                                                | 47.0 ms: 1.21x slower                                                  |
| regex_compile              | 77.9 ms                                                | 95.0 ms: 1.22x slower                                                  |
| mako                       | 7.71 ms                                                | 9.45 ms: 1.22x slower                                                  |
| unpickle_pure_python       | 151 us                                                 | 186 us: 1.24x slower                                                   |
| nbody                      | 68.8 ms                                                | 86.0 ms: 1.25x slower                                                  |
| scimark_fft                | 195 ms                                                 | 245 ms: 1.25x slower                                                   |
| scimark_sparse_mat_mult    | 3.14 ms                                                | 3.98 ms: 1.27x slower                                                  |
| python_startup             | 11.4 ms                                                | 14.8 ms: 1.30x slower                                                  |
| pyflate                    | 316 ms                                                 | 409 ms: 1.30x slower                                                   |
| scimark_sor                | 87.4 ms                                                | 113 ms: 1.30x slower                                                   |
| telco                      | 3.68 ms                                                | 4.78 ms: 1.30x slower                                                  |
| mypy2                      | 380 ms                                                 | 495 ms: 1.30x slower                                                   |
| scimark_lu                 | 76.0 ms                                                | 99.8 ms: 1.31x slower                                                  |
| spectral_norm              | 76.4 ms                                                | 103 ms: 1.34x slower                                                   |
| scimark_monte_carlo        | 45.0 ms                                                | 60.6 ms: 1.35x slower                                                  |
| hexiom                     | 4.54 ms                                                | 6.15 ms: 1.35x slower                                                  |
| python_startup_no_site     | 9.37 ms                                                | 13.0 ms: 1.39x slower                                                  |
| fannkuch                   | 248 ms                                                 | 349 ms: 1.40x slower                                                   |
| Geometric mean             | (ref)                                                  | 1.05x slower                                                           |

Benchmark hidden because not significant (7): gc_traversal, dulwich_log, deepcopy_memo, chameleon, unpickle, pickle_dict, gunicorn
Ignored benchmarks (2) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (13) of results/bm-20240323-3.13.0a5+-d610d82-PYTHON_UOPS/bm-20240323-darwin-arm64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, genshi_text, genshi_xml, html5lib, pylint, thrift


# HPT report

- Reliability score: 99.93% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x


# Memory

- memory change: 1.05x