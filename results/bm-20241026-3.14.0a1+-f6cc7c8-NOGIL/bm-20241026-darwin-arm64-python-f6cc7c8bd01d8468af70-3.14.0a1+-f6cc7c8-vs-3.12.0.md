# Results vs. 3.12.0

- fork: python
- ref: f6cc7c8bd01d8468af70
- machine: darwin-arm64
- commit hash: f6cc7c8
- commit date: 2024-10-26
- overall geometric mean: 1.242x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.16x slower
- Memory change: 1.29x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241026-darwin-arm64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 169 ms                                                 | 242 ms: 1.43x slower                                                   |
| docutils       | 1.50 sec                                               | 1.68 sec: 1.12x slower                                                 |
| tornado_http   | 69.3 ms                                                | 108 ms: 1.57x slower                                                   |
| Geometric mean | (ref)                                                  | 1.36x slower                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241026-darwin-arm64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg           | 669 ms                                                 | 495 ms: 1.35x faster                                                   |
| async_tree_io              | 668 ms                                                 | 515 ms: 1.30x faster                                                   |
| async_tree_none_tg         | 258 ms                                                 | 203 ms: 1.27x faster                                                   |
| async_tree_memoization_tg  | 323 ms                                                 | 260 ms: 1.24x faster                                                   |
| async_tree_none            | 266 ms                                                 | 227 ms: 1.17x faster                                                   |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 459 ms: 1.16x faster                                                   |
| async_tree_memoization     | 312 ms                                                 | 283 ms: 1.10x faster                                                   |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 483 ms: 1.09x faster                                                   |
| Geometric mean             | (ref)                                                  | 1.21x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241026-darwin-arm64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 93.1 ms: 1.67x slower                                                  |
| nbody          | 68.8 ms                                                | 149 ms: 2.17x slower                                                   |
| Geometric mean | (ref)                                                  | 1.54x slower                                                           |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241026-darwin-arm64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_dna      | 154 ms                                                 | 135 ms: 1.14x faster                                                   |
| regex_effbot   | 2.64 ms                                                | 2.35 ms: 1.12x faster                                                  |
| regex_v8       | 16.0 ms                                                | 16.3 ms: 1.02x slower                                                  |
| regex_compile  | 77.9 ms                                                | 118 ms: 1.52x slower                                                   |
| Geometric mean | (ref)                                                  | 1.05x slower                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241026-darwin-arm64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_parse      | 106 ms                                                 | 98.2 ms: 1.08x faster                                                  |
| xml_etree_iterparse  | 74.0 ms                                                | 74.9 ms: 1.01x slower                                                  |
| json_loads           | 17.2 us                                                | 18.2 us: 1.06x slower                                                  |
| xml_etree_generate   | 55.8 ms                                                | 65.6 ms: 1.18x slower                                                  |
| xml_etree_process    | 39.7 ms                                                | 53.2 ms: 1.34x slower                                                  |
| json_dumps           | 6.22 ms                                                | 8.69 ms: 1.40x slower                                                  |
| tomli_loads          | 1.39 sec                                               | 1.97 sec: 1.42x slower                                                 |
| pickle_pure_python   | 200 us                                                 | 338 us: 1.69x slower                                                   |
| unpickle_pure_python | 151 us                                                 | 261 us: 1.73x slower                                                   |
| Geometric mean       | (ref)                                                  | 1.28x slower                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241026-darwin-arm64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 9.37 ms                                                | 16.1 ms: 1.72x slower                                                  |
| python_startup         | 11.4 ms                                                | 20.6 ms: 1.81x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.76x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241026-darwin-arm64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 22.3 ms                                                | 34.1 ms: 1.53x slower                                                  |
| mako            | 7.71 ms                                                | 13.4 ms: 1.74x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.63x slower                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241026-darwin-arm64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| asyncio_websockets         | 409 ms                                                 | 238 ms: 1.72x faster                                                   |
| async_tree_io_tg           | 669 ms                                                 | 495 ms: 1.35x faster                                                   |
| async_tree_io              | 668 ms                                                 | 515 ms: 1.30x faster                                                   |
| async_tree_none_tg         | 258 ms                                                 | 203 ms: 1.27x faster                                                   |
| async_tree_memoization_tg  | 323 ms                                                 | 260 ms: 1.24x faster                                                   |
| async_tree_none            | 266 ms                                                 | 227 ms: 1.17x faster                                                   |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 459 ms: 1.16x faster                                                   |
| regex_dna                  | 154 ms                                                 | 135 ms: 1.14x faster                                                   |
| regex_effbot               | 2.64 ms                                                | 2.35 ms: 1.12x faster                                                  |
| async_tree_memoization     | 312 ms                                                 | 283 ms: 1.10x faster                                                   |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 483 ms: 1.09x faster                                                   |
| xml_etree_parse            | 106 ms                                                 | 98.2 ms: 1.08x faster                                                  |
| generators                 | 31.1 ms                                                | 31.0 ms: 1.00x faster                                                  |
| deepcopy                   | 235 us                                                 | 234 us: 1.00x faster                                                   |
| xml_etree_iterparse        | 74.0 ms                                                | 74.9 ms: 1.01x slower                                                  |
| regex_v8                   | 16.0 ms                                                | 16.3 ms: 1.02x slower                                                  |
| json                       | 3.09 ms                                                | 3.22 ms: 1.04x slower                                                  |
| gc_traversal               | 2.40 ms                                                | 2.51 ms: 1.05x slower                                                  |
| json_loads                 | 17.2 us                                                | 18.2 us: 1.06x slower                                                  |
| async_generators           | 304 ms                                                 | 327 ms: 1.08x slower                                                   |
| deepcopy_memo              | 27.7 us                                                | 29.9 us: 1.08x slower                                                  |
| docutils                   | 1.50 sec                                               | 1.68 sec: 1.12x slower                                                 |
| deepcopy_reduce            | 2.07 us                                                | 2.34 us: 1.13x slower                                                  |
| mdp                        | 1.58 sec                                               | 1.82 sec: 1.15x slower                                                 |
| xml_etree_generate         | 55.8 ms                                                | 65.6 ms: 1.18x slower                                                  |
| nqueens                    | 62.4 ms                                                | 73.4 ms: 1.18x slower                                                  |
| coroutines                 | 19.2 ms                                                | 22.8 ms: 1.19x slower                                                  |
| meteor_contest             | 71.7 ms                                                | 88.1 ms: 1.23x slower                                                  |
| comprehensions             | 14.5 us                                                | 19.1 us: 1.31x slower                                                  |
| xml_etree_process          | 39.7 ms                                                | 53.2 ms: 1.34x slower                                                  |
| scimark_fft                | 195 ms                                                 | 262 ms: 1.34x slower                                                   |
| pycparser                  | 677 ms                                                 | 909 ms: 1.34x slower                                                   |
| scimark_sparse_mat_mult    | 3.14 ms                                                | 4.22 ms: 1.35x slower                                                  |
| dulwich_log                | 29.8 ms                                                | 40.2 ms: 1.35x slower                                                  |
| coverage                   | 38.9 ms                                                | 52.9 ms: 1.36x slower                                                  |
| json_dumps                 | 6.22 ms                                                | 8.69 ms: 1.40x slower                                                  |
| sympy_integrate            | 11.4 ms                                                | 15.9 ms: 1.40x slower                                                  |
| sqlglot_normalize          | 186 ms                                                 | 261 ms: 1.41x slower                                                   |
| tomli_loads                | 1.39 sec                                               | 1.97 sec: 1.42x slower                                                 |
| 2to3                       | 169 ms                                                 | 242 ms: 1.43x slower                                                   |
| sqlalchemy_declarative     | 62.3 ms                                                | 89.3 ms: 1.43x slower                                                  |
| fannkuch                   | 248 ms                                                 | 356 ms: 1.43x slower                                                   |
| sqlglot_optimize           | 34.0 ms                                                | 49.9 ms: 1.47x slower                                                  |
| sqlalchemy_imperative      | 6.68 ms                                                | 9.86 ms: 1.47x slower                                                  |
| telco                      | 3.68 ms                                                | 5.43 ms: 1.48x slower                                                  |
| crypto_pyaes               | 51.9 ms                                                | 78.4 ms: 1.51x slower                                                  |
| pyflate                    | 316 ms                                                 | 477 ms: 1.51x slower                                                   |
| regex_compile              | 77.9 ms                                                | 118 ms: 1.52x slower                                                   |
| django_template            | 22.3 ms                                                | 34.1 ms: 1.53x slower                                                  |
| sympy_str                  | 148 ms                                                 | 226 ms: 1.53x slower                                                   |
| bench_mp_pool              | 44.9 ms                                                | 68.9 ms: 1.54x slower                                                  |
| typing_runtime_protocols   | 93.0 us                                                | 143 us: 1.54x slower                                                   |
| logging_simple             | 3.69 us                                                | 5.70 us: 1.55x slower                                                  |
| create_gc_cycles           | 701 us                                                 | 1.09 ms: 1.56x slower                                                  |
| logging_format             | 3.98 us                                                | 6.22 us: 1.56x slower                                                  |
| tornado_http               | 69.3 ms                                                | 108 ms: 1.57x slower                                                   |
| bench_thread_pool          | 504 us                                                 | 794 us: 1.58x slower                                                   |
| pprint_safe_repr           | 497 ms                                                 | 796 ms: 1.60x slower                                                   |
| pprint_pformat             | 1.01 sec                                               | 1.62 sec: 1.60x slower                                                 |
| spectral_norm              | 76.4 ms                                                | 127 ms: 1.66x slower                                                   |
| float                      | 55.8 ms                                                | 93.1 ms: 1.67x slower                                                  |
| richards                   | 32.1 ms                                                | 53.7 ms: 1.67x slower                                                  |
| hexiom                     | 4.54 ms                                                | 7.66 ms: 1.69x slower                                                  |
| raytrace                   | 212 ms                                                 | 357 ms: 1.69x slower                                                   |
| pickle_pure_python         | 200 us                                                 | 338 us: 1.69x slower                                                   |
| python_startup_no_site     | 9.37 ms                                                | 16.1 ms: 1.72x slower                                                  |
| richards_super             | 36.0 ms                                                | 61.9 ms: 1.72x slower                                                  |
| logging_silent             | 76.4 ns                                                | 131 ns: 1.72x slower                                                   |
| sympy_expand               | 241 ms                                                 | 415 ms: 1.72x slower                                                   |
| scimark_monte_carlo        | 45.0 ms                                                | 77.7 ms: 1.72x slower                                                  |
| unpickle_pure_python       | 151 us                                                 | 261 us: 1.73x slower                                                   |
| mako                       | 7.71 ms                                                | 13.4 ms: 1.74x slower                                                  |
| go                         | 102 ms                                                 | 178 ms: 1.75x slower                                                   |
| sympy_sum                  | 77.6 ms                                                | 136 ms: 1.75x slower                                                   |
| chaos                      | 42.5 ms                                                | 75.1 ms: 1.76x slower                                                  |
| scimark_sor                | 87.4 ms                                                | 156 ms: 1.79x slower                                                   |
| sqlglot_transpile          | 1.02 ms                                                | 1.84 ms: 1.81x slower                                                  |
| python_startup             | 11.4 ms                                                | 20.6 ms: 1.81x slower                                                  |
| scimark_lu                 | 76.0 ms                                                | 142 ms: 1.87x slower                                                   |
| sqlglot_parse              | 848 us                                                 | 1.63 ms: 1.92x slower                                                  |
| deltablue                  | 2.71 ms                                                | 5.41 ms: 2.00x slower                                                  |
| nbody                      | 68.8 ms                                                | 149 ms: 2.17x slower                                                   |
| Geometric mean             | (ref)                                                  | 1.33x slower                                                           |

Benchmark hidden because not significant (2): pidigits, pathlib
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20241026-3.14.0a1+-f6cc7c8-NOGIL/bm-20241026-darwin-arm64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift

- Geometric mean (including insignificant results): 1.242x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.24x
- 95% likely to have a slowdown of 1.21x
- 99% likely to have a slowdown of 1.16x

# Memory
- memory change: 1.29x