# Results vs. 3.13.0

- fork: brandtbucher
- ref: underflow_known
- machine: linux-x86_64
- commit hash: 8763a2d
- commit date: 2024-09-07
- overall geometric mean: 1.01x slower
- HPT reliability: 57.78%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240907-linux-x86_64-brandtbucher-underflow_known-3.14.0a0-8763a2d |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 281 ms: 1.06x slower                                                   |
| docutils       | 2.58 sec                                               | 3.01 sec: 1.16x slower                                                 |
| html5lib       | 64.5 ms                                                | 61.9 ms: 1.04x faster                                                  |
| tornado_http   | 91.5 ms                                                | 96.8 ms: 1.06x slower                                                  |
| Geometric mean | (ref)                                                  | 1.06x slower                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240907-linux-x86_64-brandtbucher-underflow_known-3.14.0a0-8763a2d |
|---------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg | 465 ms                                                 | 402 ms: 1.15x faster                                                   |
| async_tree_memoization    | 442 ms                                                 | 396 ms: 1.12x faster                                                   |
| async_tree_none           | 354 ms                                                 | 327 ms: 1.08x faster                                                   |
| async_tree_none_tg        | 320 ms                                                 | 310 ms: 1.03x faster                                                   |
| async_tree_cpu_io_mixed   | 574 ms                                                 | 563 ms: 1.02x faster                                                   |
| asyncio_tcp               | 488 ms                                                 | 482 ms: 1.01x faster                                                   |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.80 sec: 1.01x slower                                                 |
| async_generators          | 433 ms                                                 | 462 ms: 1.07x slower                                                   |
| async_tree_io_tg          | 825 ms                                                 | 898 ms: 1.09x slower                                                   |
| async_tree_io             | 843 ms                                                 | 936 ms: 1.11x slower                                                   |
| Geometric mean            | (ref)                                                  | 1.01x faster                                                           |

Benchmark hidden because not significant (3): asyncio_websockets, async_tree_cpu_io_mixed_tg, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240907-linux-x86_64-brandtbucher-underflow_known-3.14.0a0-8763a2d |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 70.1 ms: 1.12x faster                                                  |
| nbody          | 85.7 ms                                                | 80.4 ms: 1.07x faster                                                  |
| pidigits       | 186 ms                                                 | 187 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                  | 1.06x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240907-linux-x86_64-brandtbucher-underflow_known-3.14.0a0-8763a2d |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.62 ms: 1.07x faster                                                  |
| regex_dna      | 220 ms                                                 | 213 ms: 1.03x faster                                                   |
| regex_v8       | 25.3 ms                                                | 24.4 ms: 1.03x faster                                                  |
| regex_compile  | 131 ms                                                 | 146 ms: 1.11x slower                                                   |
| Geometric mean | (ref)                                                  | 1.01x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240907-linux-x86_64-brandtbucher-underflow_known-3.14.0a0-8763a2d |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_generate   | 87.0 ms                                                | 76.9 ms: 1.13x faster                                                  |
| xml_etree_process    | 60.4 ms                                                | 54.4 ms: 1.11x faster                                                  |
| unpickle_pure_python | 213 us                                                 | 198 us: 1.08x faster                                                   |
| tomli_loads          | 2.11 sec                                               | 1.96 sec: 1.08x faster                                                 |
| xml_etree_parse      | 156 ms                                                 | 146 ms: 1.07x faster                                                   |
| xml_etree_iterparse  | 102 ms                                                 | 98.4 ms: 1.04x faster                                                  |
| pickle               | 11.6 us                                                | 12.0 us: 1.04x slower                                                  |
| json_loads           | 27.0 us                                                | 28.2 us: 1.05x slower                                                  |
| pickle_dict          | 33.2 us                                                | 34.9 us: 1.05x slower                                                  |
| unpickle_list        | 4.96 us                                                | 5.25 us: 1.06x slower                                                  |
| pickle_list          | 5.01 us                                                | 5.30 us: 1.06x slower                                                  |
| pickle_pure_python   | 300 us                                                 | 323 us: 1.08x slower                                                   |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                           |

Benchmark hidden because not significant (2): json_dumps, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240907-linux-x86_64-brandtbucher-underflow_known-3.14.0a0-8763a2d |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.7 ms: 1.01x slower                                                  |
| python_startup_no_site | 6.99 ms                                                | 7.17 ms: 1.03x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240907-linux-x86_64-brandtbucher-underflow_known-3.14.0a0-8763a2d |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.72 ms: 1.14x faster                                                  |
| django_template | 34.4 ms                                                | 35.7 ms: 1.04x slower                                                  |
| genshi_text     | 22.9 ms                                                | 23.9 ms: 1.05x slower                                                  |
| genshi_xml      | 50.3 ms                                                | 54.1 ms: 1.07x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.01x slower                                                           |

All benchmarks:
===============

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240907-linux-x86_64-brandtbucher-underflow_known-3.14.0a0-8763a2d |
|---------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| deepcopy_memo             | 38.0 us                                                | 25.2 us: 1.51x faster                                                  |
| deepcopy                  | 352 us                                                 | 267 us: 1.32x faster                                                   |
| richards_super            | 54.4 ms                                                | 42.3 ms: 1.29x faster                                                  |
| richards                  | 48.1 ms                                                | 37.8 ms: 1.27x faster                                                  |
| deepcopy_reduce           | 3.17 us                                                | 2.69 us: 1.18x faster                                                  |
| scimark_fft               | 369 ms                                                 | 316 ms: 1.17x faster                                                   |
| async_tree_memoization_tg | 465 ms                                                 | 402 ms: 1.15x faster                                                   |
| mako                      | 11.1 ms                                                | 9.72 ms: 1.14x faster                                                  |
| spectral_norm             | 115 ms                                                 | 101 ms: 1.14x faster                                                   |
| xml_etree_generate        | 87.0 ms                                                | 76.9 ms: 1.13x faster                                                  |
| float                     | 78.5 ms                                                | 70.1 ms: 1.12x faster                                                  |
| async_tree_memoization    | 442 ms                                                 | 396 ms: 1.12x faster                                                   |
| scimark_sparse_mat_mult   | 5.03 ms                                                | 4.49 ms: 1.12x faster                                                  |
| xml_etree_process         | 60.4 ms                                                | 54.4 ms: 1.11x faster                                                  |
| crypto_pyaes              | 73.0 ms                                                | 66.5 ms: 1.10x faster                                                  |
| async_tree_none           | 354 ms                                                 | 327 ms: 1.08x faster                                                   |
| pathlib                   | 17.1 ms                                                | 15.7 ms: 1.08x faster                                                  |
| unpickle_pure_python      | 213 us                                                 | 198 us: 1.08x faster                                                   |
| tomli_loads               | 2.11 sec                                               | 1.96 sec: 1.08x faster                                                 |
| mdp                       | 2.74 sec                                               | 2.55 sec: 1.08x faster                                                 |
| regex_effbot              | 3.88 ms                                                | 3.62 ms: 1.07x faster                                                  |
| xml_etree_parse           | 156 ms                                                 | 146 ms: 1.07x faster                                                   |
| nbody                     | 85.7 ms                                                | 80.4 ms: 1.07x faster                                                  |
| telco                     | 8.45 ms                                                | 7.97 ms: 1.06x faster                                                  |
| gc_traversal              | 3.81 ms                                                | 3.59 ms: 1.06x faster                                                  |
| scimark_sor               | 122 ms                                                 | 117 ms: 1.05x faster                                                   |
| bpe_tokeniser             | 4.69 sec                                               | 4.48 sec: 1.05x faster                                                 |
| html5lib                  | 64.5 ms                                                | 61.9 ms: 1.04x faster                                                  |
| scimark_lu                | 115 ms                                                 | 110 ms: 1.04x faster                                                   |
| xml_etree_iterparse       | 102 ms                                                 | 98.4 ms: 1.04x faster                                                  |
| regex_dna                 | 220 ms                                                 | 213 ms: 1.03x faster                                                   |
| regex_v8                  | 25.3 ms                                                | 24.4 ms: 1.03x faster                                                  |
| thrift                    | 796 us                                                 | 771 us: 1.03x faster                                                   |
| async_tree_none_tg        | 320 ms                                                 | 310 ms: 1.03x faster                                                   |
| sqlite_synth              | 2.85 us                                                | 2.77 us: 1.03x faster                                                  |
| go                        | 142 ms                                                 | 139 ms: 1.02x faster                                                   |
| fannkuch                  | 381 ms                                                 | 373 ms: 1.02x faster                                                   |
| async_tree_cpu_io_mixed   | 574 ms                                                 | 563 ms: 1.02x faster                                                   |
| logging_silent            | 102 ns                                                 | 101 ns: 1.01x faster                                                   |
| asyncio_tcp               | 488 ms                                                 | 482 ms: 1.01x faster                                                   |
| pyflate                   | 460 ms                                                 | 455 ms: 1.01x faster                                                   |
| deltablue                 | 3.15 ms                                                | 3.12 ms: 1.01x faster                                                  |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.80 sec: 1.01x slower                                                 |
| pidigits                  | 186 ms                                                 | 187 ms: 1.01x slower                                                   |
| pprint_safe_repr          | 744 ms                                                 | 751 ms: 1.01x slower                                                   |
| python_startup            | 10.6 ms                                                | 10.7 ms: 1.01x slower                                                  |
| meteor_contest            | 108 ms                                                 | 109 ms: 1.01x slower                                                   |
| comprehensions            | 16.4 us                                                | 16.6 us: 1.01x slower                                                  |
| coverage                  | 83.7 ms                                                | 85.4 ms: 1.02x slower                                                  |
| pprint_pformat            | 1.51 sec                                               | 1.55 sec: 1.02x slower                                                 |
| bench_thread_pool         | 815 us                                                 | 835 us: 1.02x slower                                                   |
| python_startup_no_site    | 6.99 ms                                                | 7.17 ms: 1.03x slower                                                  |
| json                      | 5.20 ms                                                | 5.38 ms: 1.03x slower                                                  |
| typing_runtime_protocols  | 159 us                                                 | 165 us: 1.03x slower                                                   |
| pycparser                 | 1.19 sec                                               | 1.24 sec: 1.04x slower                                                 |
| django_template           | 34.4 ms                                                | 35.7 ms: 1.04x slower                                                  |
| pickle                    | 11.6 us                                                | 12.0 us: 1.04x slower                                                  |
| genshi_text               | 22.9 ms                                                | 23.9 ms: 1.05x slower                                                  |
| json_loads                | 27.0 us                                                | 28.2 us: 1.05x slower                                                  |
| pickle_dict               | 33.2 us                                                | 34.9 us: 1.05x slower                                                  |
| chaos                     | 58.4 ms                                                | 61.6 ms: 1.05x slower                                                  |
| sqlglot_normalize         | 107 ms                                                 | 113 ms: 1.06x slower                                                   |
| unpickle_list             | 4.96 us                                                | 5.25 us: 1.06x slower                                                  |
| tornado_http              | 91.5 ms                                                | 96.8 ms: 1.06x slower                                                  |
| pickle_list               | 5.01 us                                                | 5.30 us: 1.06x slower                                                  |
| 2to3                      | 265 ms                                                 | 281 ms: 1.06x slower                                                   |
| async_generators          | 433 ms                                                 | 462 ms: 1.07x slower                                                   |
| nqueens                   | 80.6 ms                                                | 86.2 ms: 1.07x slower                                                  |
| genshi_xml                | 50.3 ms                                                | 54.1 ms: 1.07x slower                                                  |
| pickle_pure_python        | 300 us                                                 | 323 us: 1.08x slower                                                   |
| raytrace                  | 262 ms                                                 | 283 ms: 1.08x slower                                                   |
| sqlglot_transpile         | 1.57 ms                                                | 1.70 ms: 1.08x slower                                                  |
| async_tree_io_tg          | 825 ms                                                 | 898 ms: 1.09x slower                                                   |
| sqlglot_optimize          | 53.9 ms                                                | 58.7 ms: 1.09x slower                                                  |
| sqlglot_parse             | 1.27 ms                                                | 1.38 ms: 1.09x slower                                                  |
| create_gc_cycles          | 1.61 ms                                                | 1.75 ms: 1.09x slower                                                  |
| sympy_expand              | 462 ms                                                 | 508 ms: 1.10x slower                                                   |
| async_tree_io             | 843 ms                                                 | 936 ms: 1.11x slower                                                   |
| regex_compile             | 131 ms                                                 | 146 ms: 1.11x slower                                                   |
| sympy_str                 | 274 ms                                                 | 306 ms: 1.12x slower                                                   |
| dulwich_log               | 63.0 ms                                                | 70.8 ms: 1.12x slower                                                  |
| generators                | 28.8 ms                                                | 33.1 ms: 1.15x slower                                                  |
| sympy_integrate           | 19.9 ms                                                | 23.0 ms: 1.16x slower                                                  |
| docutils                  | 2.58 sec                                               | 3.01 sec: 1.16x slower                                                 |
| scimark_monte_carlo       | 66.3 ms                                                | 77.3 ms: 1.17x slower                                                  |
| pylint                    | 313 ms                                                 | 373 ms: 1.19x slower                                                   |
| sympy_sum                 | 150 ms                                                 | 179 ms: 1.19x slower                                                   |
| hexiom                    | 6.13 ms                                                | 7.72 ms: 1.26x slower                                                  |
| unpack_sequence           | 42.4 ns                                                | 145 ns: 3.42x slower                                                   |
| Geometric mean            | (ref)                                                  | 1.01x slower                                                           |

Benchmark hidden because not significant (8): logging_format, json_dumps, bench_mp_pool, logging_simple, asyncio_websockets, async_tree_cpu_io_mixed_tg, coroutines, unpickle
Ignored benchmarks (7) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 57.78% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.11x