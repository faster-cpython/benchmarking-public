# Results vs. 3.12.0

- fork: bdraco
- ref: speed_up_async_sched
- machine: darwin-arm64
- commit hash: f78838c
- commit date: 2024-08-24
- overall geometric mean: 1.086x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 0.70x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240824-darwin-arm64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 169 ms                                                 | 160 ms: 1.06x faster                                                  |
| docutils       | 1.50 sec                                               | 1.47 sec: 1.03x faster                                                |
| tornado_http   | 69.3 ms                                                | 85.2 ms: 1.23x slower                                                 |
| Geometric mean | (ref)                                                  | 1.04x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240824-darwin-arm64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none            | 266 ms                                                 | 192 ms: 1.38x faster                                                  |
| async_tree_memoization_tg  | 323 ms                                                 | 237 ms: 1.36x faster                                                  |
| async_tree_none_tg         | 258 ms                                                 | 198 ms: 1.30x faster                                                  |
| async_tree_memoization     | 312 ms                                                 | 243 ms: 1.28x faster                                                  |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 457 ms: 1.15x faster                                                  |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 465 ms: 1.15x faster                                                  |
| async_tree_io              | 668 ms                                                 | 598 ms: 1.12x faster                                                  |
| async_tree_io_tg           | 669 ms                                                 | 606 ms: 1.10x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.23x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240824-darwin-arm64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 68.8 ms                                                | 59.4 ms: 1.16x faster                                                 |
| float          | 55.8 ms                                                | 48.9 ms: 1.14x faster                                                 |
| Geometric mean | (ref)                                                  | 1.10x faster                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240824-darwin-arm64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 77.9 ms                                                | 66.9 ms: 1.16x faster                                                 |
| regex_effbot   | 2.64 ms                                                | 2.46 ms: 1.07x faster                                                 |
| regex_dna      | 154 ms                                                 | 145 ms: 1.06x faster                                                  |
| regex_v8       | 16.0 ms                                                | 16.5 ms: 1.03x slower                                                 |
| Geometric mean | (ref)                                                  | 1.06x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240824-darwin-arm64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 200 us                                                 | 181 us: 1.10x faster                                                  |
| xml_etree_process    | 39.7 ms                                                | 37.7 ms: 1.05x faster                                                 |
| unpickle_pure_python | 151 us                                                 | 143 us: 1.05x faster                                                  |
| xml_etree_generate   | 55.8 ms                                                | 53.2 ms: 1.05x faster                                                 |
| json_dumps           | 6.22 ms                                                | 6.30 ms: 1.01x slower                                                 |
| xml_etree_parse      | 106 ms                                                 | 110 ms: 1.03x slower                                                  |
| tomli_loads          | 1.39 sec                                               | 1.48 sec: 1.06x slower                                                |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                          |

Benchmark hidden because not significant (2): xml_etree_iterparse, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240824-darwin-arm64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 9.37 ms                                                | 13.5 ms: 1.44x slower                                                 |
| python_startup         | 11.4 ms                                                | 16.5 ms: 1.44x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.44x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240824-darwin-arm64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| django_template | 22.3 ms                                                | 19.7 ms: 1.13x faster                                                 |
| mako            | 7.71 ms                                                | 6.94 ms: 1.11x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.12x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240824-darwin-arm64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy_memo              | 27.7 us                                                | 16.9 us: 1.64x faster                                                 |
| deepcopy                   | 235 us                                                 | 144 us: 1.63x faster                                                  |
| generators                 | 31.1 ms                                                | 20.4 ms: 1.52x faster                                                 |
| comprehensions             | 14.5 us                                                | 9.93 us: 1.46x faster                                                 |
| raytrace                   | 212 ms                                                 | 149 ms: 1.42x faster                                                  |
| async_tree_none            | 266 ms                                                 | 192 ms: 1.38x faster                                                  |
| deepcopy_reduce            | 2.07 us                                                | 1.51 us: 1.37x faster                                                 |
| async_tree_memoization_tg  | 323 ms                                                 | 237 ms: 1.36x faster                                                  |
| async_tree_none_tg         | 258 ms                                                 | 198 ms: 1.30x faster                                                  |
| async_tree_memoization     | 312 ms                                                 | 243 ms: 1.28x faster                                                  |
| deltablue                  | 2.71 ms                                                | 2.13 ms: 1.27x faster                                                 |
| logging_silent             | 76.4 ns                                                | 61.2 ns: 1.25x faster                                                 |
| logging_simple             | 3.69 us                                                | 3.07 us: 1.20x faster                                                 |
| coroutines                 | 19.2 ms                                                | 16.1 ms: 1.20x faster                                                 |
| chaos                      | 42.5 ms                                                | 35.7 ms: 1.19x faster                                                 |
| logging_format             | 3.98 us                                                | 3.40 us: 1.17x faster                                                 |
| nqueens                    | 62.4 ms                                                | 53.3 ms: 1.17x faster                                                 |
| regex_compile              | 77.9 ms                                                | 66.9 ms: 1.16x faster                                                 |
| nbody                      | 68.8 ms                                                | 59.4 ms: 1.16x faster                                                 |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 457 ms: 1.15x faster                                                  |
| sqlglot_parse              | 848 us                                                 | 739 us: 1.15x faster                                                  |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 465 ms: 1.15x faster                                                  |
| float                      | 55.8 ms                                                | 48.9 ms: 1.14x faster                                                 |
| scimark_lu                 | 76.0 ms                                                | 66.7 ms: 1.14x faster                                                 |
| sqlglot_transpile          | 1.02 ms                                                | 897 us: 1.14x faster                                                  |
| django_template            | 22.3 ms                                                | 19.7 ms: 1.13x faster                                                 |
| spectral_norm              | 76.4 ms                                                | 67.7 ms: 1.13x faster                                                 |
| scimark_sparse_mat_mult    | 3.14 ms                                                | 2.78 ms: 1.13x faster                                                 |
| sympy_str                  | 148 ms                                                 | 131 ms: 1.12x faster                                                  |
| sympy_sum                  | 77.6 ms                                                | 69.1 ms: 1.12x faster                                                 |
| bench_thread_pool          | 504 us                                                 | 449 us: 1.12x faster                                                  |
| hexiom                     | 4.54 ms                                                | 4.06 ms: 1.12x faster                                                 |
| async_tree_io              | 668 ms                                                 | 598 ms: 1.12x faster                                                  |
| mako                       | 7.71 ms                                                | 6.94 ms: 1.11x faster                                                 |
| sqlglot_normalize          | 186 ms                                                 | 168 ms: 1.11x faster                                                  |
| mdp                        | 1.58 sec                                               | 1.43 sec: 1.11x faster                                                |
| async_tree_io_tg           | 669 ms                                                 | 606 ms: 1.10x faster                                                  |
| pickle_pure_python         | 200 us                                                 | 181 us: 1.10x faster                                                  |
| dulwich_log                | 29.8 ms                                                | 27.1 ms: 1.10x faster                                                 |
| sympy_integrate            | 11.4 ms                                                | 10.3 ms: 1.10x faster                                                 |
| sqlglot_optimize           | 34.0 ms                                                | 31.2 ms: 1.09x faster                                                 |
| pprint_safe_repr           | 497 ms                                                 | 457 ms: 1.09x faster                                                  |
| pprint_pformat             | 1.01 sec                                               | 930 ms: 1.09x faster                                                  |
| async_generators           | 304 ms                                                 | 281 ms: 1.08x faster                                                  |
| asyncio_tcp                | 449 ms                                                 | 416 ms: 1.08x faster                                                  |
| richards_super             | 36.0 ms                                                | 33.4 ms: 1.08x faster                                                 |
| regex_effbot               | 2.64 ms                                                | 2.46 ms: 1.07x faster                                                 |
| sympy_expand               | 241 ms                                                 | 226 ms: 1.07x faster                                                  |
| regex_dna                  | 154 ms                                                 | 145 ms: 1.06x faster                                                  |
| 2to3                       | 169 ms                                                 | 160 ms: 1.06x faster                                                  |
| richards                   | 32.1 ms                                                | 30.4 ms: 1.06x faster                                                 |
| scimark_fft                | 195 ms                                                 | 185 ms: 1.06x faster                                                  |
| pycparser                  | 677 ms                                                 | 643 ms: 1.05x faster                                                  |
| xml_etree_process          | 39.7 ms                                                | 37.7 ms: 1.05x faster                                                 |
| unpickle_pure_python       | 151 us                                                 | 143 us: 1.05x faster                                                  |
| xml_etree_generate         | 55.8 ms                                                | 53.2 ms: 1.05x faster                                                 |
| scimark_monte_carlo        | 45.0 ms                                                | 43.3 ms: 1.04x faster                                                 |
| pathlib                    | 24.2 ms                                                | 23.5 ms: 1.03x faster                                                 |
| docutils                   | 1.50 sec                                               | 1.47 sec: 1.03x faster                                                |
| json                       | 3.09 ms                                                | 3.01 ms: 1.02x faster                                                 |
| typing_runtime_protocols   | 93.0 us                                                | 90.9 us: 1.02x faster                                                 |
| crypto_pyaes               | 51.9 ms                                                | 50.9 ms: 1.02x faster                                                 |
| meteor_contest             | 71.7 ms                                                | 72.5 ms: 1.01x slower                                                 |
| json_dumps                 | 6.22 ms                                                | 6.30 ms: 1.01x slower                                                 |
| pyflate                    | 316 ms                                                 | 321 ms: 1.02x slower                                                  |
| asyncio_tcp_ssl            | 1.24 sec                                               | 1.27 sec: 1.02x slower                                                |
| gc_traversal               | 2.40 ms                                                | 2.47 ms: 1.03x slower                                                 |
| xml_etree_parse            | 106 ms                                                 | 110 ms: 1.03x slower                                                  |
| regex_v8                   | 16.0 ms                                                | 16.5 ms: 1.03x slower                                                 |
| go                         | 102 ms                                                 | 106 ms: 1.04x slower                                                  |
| fannkuch                   | 248 ms                                                 | 260 ms: 1.05x slower                                                  |
| tomli_loads                | 1.39 sec                                               | 1.48 sec: 1.06x slower                                                |
| scimark_sor                | 87.4 ms                                                | 93.3 ms: 1.07x slower                                                 |
| bench_mp_pool              | 44.9 ms                                                | 48.7 ms: 1.09x slower                                                 |
| coverage                   | 38.9 ms                                                | 44.3 ms: 1.14x slower                                                 |
| tornado_http               | 69.3 ms                                                | 85.2 ms: 1.23x slower                                                 |
| create_gc_cycles           | 701 us                                                 | 906 us: 1.29x slower                                                  |
| telco                      | 3.68 ms                                                | 4.78 ms: 1.30x slower                                                 |
| python_startup_no_site     | 9.37 ms                                                | 13.5 ms: 1.44x slower                                                 |
| python_startup             | 11.4 ms                                                | 16.5 ms: 1.44x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.08x faster                                                          |

Benchmark hidden because not significant (4): xml_etree_iterparse, json_loads, asyncio_websockets, pidigits
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (14) of results/bm-20240824-3.14.0a0-f78838c/bm-20240824-darwin-arm64-bdraco-speed_up_async_sched-3.14.0a0-f78838c.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

- Geometric mean (including insignificant results): 1.086x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 0.70x