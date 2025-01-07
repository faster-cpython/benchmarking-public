# Results vs. 3.12.0

- fork: kumaraditya303
- ref: future_iter
- machine: darwin-arm64
- commit hash: 82b905d
- commit date: 2025-01-05
- overall geometric mean: 1.107x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: 1.20x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250105-darwin-arm64-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 169 ms                                                 | 186 ms: 1.10x slower                                                  |
| docutils       | 1.50 sec                                               | 1.40 sec: 1.07x faster                                                |
| Geometric mean | (ref)                                                  | 1.01x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250105-darwin-arm64-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io_tg           | 669 ms                                                 | 344 ms: 1.94x faster                                                  |
| async_tree_io              | 668 ms                                                 | 348 ms: 1.92x faster                                                  |
| async_tree_none_tg         | 258 ms                                                 | 148 ms: 1.74x faster                                                  |
| async_tree_none            | 266 ms                                                 | 156 ms: 1.71x faster                                                  |
| async_tree_memoization_tg  | 323 ms                                                 | 190 ms: 1.70x faster                                                  |
| async_tree_memoization     | 312 ms                                                 | 193 ms: 1.62x faster                                                  |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 405 ms: 1.32x faster                                                  |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 409 ms: 1.28x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.64x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250105-darwin-arm64-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 46.3 ms: 1.20x faster                                                 |
| nbody          | 68.8 ms                                                | 67.6 ms: 1.02x faster                                                 |
| pidigits       | 282 ms                                                 | 283 ms: 1.00x slower                                                  |
| Geometric mean | (ref)                                                  | 1.07x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250105-darwin-arm64-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.64 ms                                                | 2.05 ms: 1.29x faster                                                 |
| regex_compile  | 77.9 ms                                                | 66.7 ms: 1.17x faster                                                 |
| regex_dna      | 154 ms                                                 | 135 ms: 1.15x faster                                                  |
| regex_v8       | 16.0 ms                                                | 15.9 ms: 1.01x faster                                                 |
| Geometric mean | (ref)                                                  | 1.15x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250105-darwin-arm64-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 1.39 sec                                               | 1.20 sec: 1.17x faster                                                |
| unpickle_pure_python | 151 us                                                 | 137 us: 1.10x faster                                                  |
| xml_etree_generate   | 55.8 ms                                                | 52.2 ms: 1.07x faster                                                 |
| json_loads           | 17.2 us                                                | 16.5 us: 1.05x faster                                                 |
| xml_etree_process    | 39.7 ms                                                | 38.0 ms: 1.04x faster                                                 |
| xml_etree_iterparse  | 74.0 ms                                                | 71.4 ms: 1.04x faster                                                 |
| xml_etree_parse      | 106 ms                                                 | 104 ms: 1.02x faster                                                  |
| pickle_pure_python   | 200 us                                                 | 196 us: 1.02x faster                                                  |
| json_dumps           | 6.22 ms                                                | 7.27 ms: 1.17x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250105-darwin-arm64-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 9.37 ms                                                | 13.5 ms: 1.44x slower                                                 |
| python_startup         | 11.4 ms                                                | 18.5 ms: 1.62x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.53x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250105-darwin-arm64-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 7.71 ms                                                | 6.95 ms: 1.11x faster                                                 |
| django_template | 22.3 ms                                                | 20.9 ms: 1.07x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.09x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250105-darwin-arm64-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io_tg           | 669 ms                                                 | 344 ms: 1.94x faster                                                  |
| async_tree_io              | 668 ms                                                 | 348 ms: 1.92x faster                                                  |
| async_tree_none_tg         | 258 ms                                                 | 148 ms: 1.74x faster                                                  |
| async_tree_none            | 266 ms                                                 | 156 ms: 1.71x faster                                                  |
| async_tree_memoization_tg  | 323 ms                                                 | 190 ms: 1.70x faster                                                  |
| asyncio_websockets         | 409 ms                                                 | 244 ms: 1.68x faster                                                  |
| async_tree_memoization     | 312 ms                                                 | 193 ms: 1.62x faster                                                  |
| deepcopy                   | 235 us                                                 | 148 us: 1.58x faster                                                  |
| deepcopy_memo              | 27.7 us                                                | 18.0 us: 1.54x faster                                                 |
| generators                 | 31.1 ms                                                | 22.6 ms: 1.38x faster                                                 |
| deepcopy_reduce            | 2.07 us                                                | 1.54 us: 1.34x faster                                                 |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 405 ms: 1.32x faster                                                  |
| go                         | 102 ms                                                 | 78.1 ms: 1.30x faster                                                 |
| regex_effbot               | 2.64 ms                                                | 2.05 ms: 1.29x faster                                                 |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 409 ms: 1.28x faster                                                  |
| raytrace                   | 212 ms                                                 | 169 ms: 1.26x faster                                                  |
| spectral_norm              | 76.4 ms                                                | 61.8 ms: 1.24x faster                                                 |
| float                      | 55.8 ms                                                | 46.3 ms: 1.20x faster                                                 |
| coroutines                 | 19.2 ms                                                | 16.0 ms: 1.20x faster                                                 |
| logging_silent             | 76.4 ns                                                | 65.0 ns: 1.18x faster                                                 |
| scimark_sparse_mat_mult    | 3.14 ms                                                | 2.67 ms: 1.17x faster                                                 |
| comprehensions             | 14.5 us                                                | 12.4 us: 1.17x faster                                                 |
| regex_compile              | 77.9 ms                                                | 66.7 ms: 1.17x faster                                                 |
| tomli_loads                | 1.39 sec                                               | 1.20 sec: 1.17x faster                                                |
| logging_simple             | 3.69 us                                                | 3.17 us: 1.16x faster                                                 |
| deltablue                  | 2.71 ms                                                | 2.34 ms: 1.16x faster                                                 |
| regex_dna                  | 154 ms                                                 | 135 ms: 1.15x faster                                                  |
| logging_format             | 3.98 us                                                | 3.48 us: 1.14x faster                                                 |
| scimark_fft                | 195 ms                                                 | 173 ms: 1.13x faster                                                  |
| chaos                      | 42.5 ms                                                | 37.8 ms: 1.13x faster                                                 |
| nqueens                    | 62.4 ms                                                | 55.8 ms: 1.12x faster                                                 |
| scimark_sor                | 87.4 ms                                                | 78.5 ms: 1.11x faster                                                 |
| sqlglot_parse              | 848 us                                                 | 763 us: 1.11x faster                                                  |
| mako                       | 7.71 ms                                                | 6.95 ms: 1.11x faster                                                 |
| dulwich_log                | 29.8 ms                                                | 27.0 ms: 1.10x faster                                                 |
| sqlglot_transpile          | 1.02 ms                                                | 927 us: 1.10x faster                                                  |
| unpickle_pure_python       | 151 us                                                 | 137 us: 1.10x faster                                                  |
| pprint_pformat             | 1.01 sec                                               | 918 ms: 1.10x faster                                                  |
| async_generators           | 304 ms                                                 | 277 ms: 1.10x faster                                                  |
| hexiom                     | 4.54 ms                                                | 4.15 ms: 1.10x faster                                                 |
| pprint_safe_repr           | 497 ms                                                 | 455 ms: 1.09x faster                                                  |
| pyflate                    | 316 ms                                                 | 290 ms: 1.09x faster                                                  |
| pathlib                    | 24.2 ms                                                | 22.3 ms: 1.09x faster                                                 |
| json                       | 3.09 ms                                                | 2.85 ms: 1.08x faster                                                 |
| scimark_monte_carlo        | 45.0 ms                                                | 41.8 ms: 1.08x faster                                                 |
| sqlalchemy_declarative     | 62.3 ms                                                | 58.1 ms: 1.07x faster                                                 |
| docutils                   | 1.50 sec                                               | 1.40 sec: 1.07x faster                                                |
| xml_etree_generate         | 55.8 ms                                                | 52.2 ms: 1.07x faster                                                 |
| sympy_str                  | 148 ms                                                 | 138 ms: 1.07x faster                                                  |
| mdp                        | 1.58 sec                                               | 1.48 sec: 1.07x faster                                                |
| django_template            | 22.3 ms                                                | 20.9 ms: 1.07x faster                                                 |
| sympy_sum                  | 77.6 ms                                                | 72.9 ms: 1.07x faster                                                 |
| pycparser                  | 677 ms                                                 | 635 ms: 1.07x faster                                                  |
| bench_thread_pool          | 504 us                                                 | 475 us: 1.06x faster                                                  |
| sqlglot_optimize           | 34.0 ms                                                | 32.5 ms: 1.05x faster                                                 |
| json_loads                 | 17.2 us                                                | 16.5 us: 1.05x faster                                                 |
| scimark_lu                 | 76.0 ms                                                | 72.7 ms: 1.05x faster                                                 |
| xml_etree_process          | 39.7 ms                                                | 38.0 ms: 1.04x faster                                                 |
| sqlglot_normalize          | 186 ms                                                 | 178 ms: 1.04x faster                                                  |
| sqlalchemy_imperative      | 6.68 ms                                                | 6.44 ms: 1.04x faster                                                 |
| xml_etree_iterparse        | 74.0 ms                                                | 71.4 ms: 1.04x faster                                                 |
| sympy_expand               | 241 ms                                                 | 233 ms: 1.03x faster                                                  |
| sympy_integrate            | 11.4 ms                                                | 11.1 ms: 1.03x faster                                                 |
| richards_super             | 36.0 ms                                                | 35.1 ms: 1.03x faster                                                 |
| xml_etree_parse            | 106 ms                                                 | 104 ms: 1.02x faster                                                  |
| sqlite_synth               | 1.57 us                                                | 1.54 us: 1.02x faster                                                 |
| pickle_pure_python         | 200 us                                                 | 196 us: 1.02x faster                                                  |
| richards                   | 32.1 ms                                                | 31.5 ms: 1.02x faster                                                 |
| nbody                      | 68.8 ms                                                | 67.6 ms: 1.02x faster                                                 |
| fannkuch                   | 248 ms                                                 | 246 ms: 1.01x faster                                                  |
| regex_v8                   | 16.0 ms                                                | 15.9 ms: 1.01x faster                                                 |
| meteor_contest             | 71.7 ms                                                | 71.5 ms: 1.00x faster                                                 |
| pidigits                   | 282 ms                                                 | 283 ms: 1.00x slower                                                  |
| typing_runtime_protocols   | 93.0 us                                                | 94.8 us: 1.02x slower                                                 |
| crypto_pyaes               | 51.9 ms                                                | 53.0 ms: 1.02x slower                                                 |
| 2to3                       | 169 ms                                                 | 186 ms: 1.10x slower                                                  |
| json_dumps                 | 6.22 ms                                                | 7.27 ms: 1.17x slower                                                 |
| coverage                   | 38.9 ms                                                | 46.1 ms: 1.19x slower                                                 |
| telco                      | 3.68 ms                                                | 4.51 ms: 1.22x slower                                                 |
| gc_traversal               | 2.40 ms                                                | 3.08 ms: 1.28x slower                                                 |
| bench_mp_pool              | 44.9 ms                                                | 60.2 ms: 1.34x slower                                                 |
| mypy2                      | 380 ms                                                 | 516 ms: 1.36x slower                                                  |
| python_startup_no_site     | 9.37 ms                                                | 13.5 ms: 1.44x slower                                                 |
| python_startup             | 11.4 ms                                                | 18.5 ms: 1.62x slower                                                 |
| create_gc_cycles           | 701 us                                                 | 1.28 ms: 1.82x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.10x faster                                                          |
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (20) of results/bm-20250105-3.14.0a3+-82b905d/bm-20250105-darwin-arm64-kumaraditya303-future_iter-3.14.0a3+-82b905d.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.107x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.07x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: 1.20x