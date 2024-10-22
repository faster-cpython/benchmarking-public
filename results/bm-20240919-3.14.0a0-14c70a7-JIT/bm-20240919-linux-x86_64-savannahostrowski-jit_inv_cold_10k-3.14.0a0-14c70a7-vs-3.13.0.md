# Results vs. 3.13.0

- fork: savannahostrowski
- ref: jit_inv_cold_10k
- machine: linux-x86_64
- commit hash: 14c70a7
- commit date: 2024-09-19
- overall geometric mean: 1.01x slower
- HPT reliability: 68.81%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_cold_10k-3.14.0a0-14c70a7 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 285 ms: 1.07x slower                                                         |
| docutils       | 2.58 sec                                               | 2.88 sec: 1.11x slower                                                       |
| html5lib       | 64.5 ms                                                | 63.9 ms: 1.01x faster                                                        |
| tornado_http   | 91.5 ms                                                | 95.5 ms: 1.04x slower                                                        |
| Geometric mean | (ref)                                                  | 1.05x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_cold_10k-3.14.0a0-14c70a7 |
|---------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg | 465 ms                                                 | 387 ms: 1.20x faster                                                         |
| async_tree_memoization    | 442 ms                                                 | 395 ms: 1.12x faster                                                         |
| async_tree_none           | 354 ms                                                 | 321 ms: 1.10x faster                                                         |
| async_tree_none_tg        | 320 ms                                                 | 299 ms: 1.07x faster                                                         |
| async_tree_cpu_io_mixed   | 574 ms                                                 | 558 ms: 1.03x faster                                                         |
| asyncio_tcp               | 488 ms                                                 | 491 ms: 1.01x slower                                                         |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.80 sec: 1.01x slower                                                       |
| coroutines                | 22.5 ms                                                | 23.4 ms: 1.04x slower                                                        |
| async_tree_io             | 843 ms                                                 | 883 ms: 1.05x slower                                                         |
| async_tree_io_tg          | 825 ms                                                 | 874 ms: 1.06x slower                                                         |
| async_generators          | 433 ms                                                 | 460 ms: 1.06x slower                                                         |
| Geometric mean            | (ref)                                                  | 1.02x faster                                                                 |

Benchmark hidden because not significant (2): asyncio_websockets, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_cold_10k-3.14.0a0-14c70a7 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 71.5 ms: 1.10x faster                                                        |
| nbody          | 85.7 ms                                                | 79.7 ms: 1.08x faster                                                        |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                         |
| Geometric mean | (ref)                                                  | 1.06x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_cold_10k-3.14.0a0-14c70a7 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.65 ms: 1.07x faster                                                        |
| regex_dna      | 220 ms                                                 | 215 ms: 1.02x faster                                                         |
| regex_v8       | 25.3 ms                                                | 25.5 ms: 1.01x slower                                                        |
| regex_compile  | 131 ms                                                 | 139 ms: 1.06x slower                                                         |
| Geometric mean | (ref)                                                  | 1.00x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_cold_10k-3.14.0a0-14c70a7 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_generate   | 87.0 ms                                                | 79.8 ms: 1.09x faster                                                        |
| xml_etree_process    | 60.4 ms                                                | 55.5 ms: 1.09x faster                                                        |
| xml_etree_parse      | 156 ms                                                 | 145 ms: 1.08x faster                                                         |
| tomli_loads          | 2.11 sec                                               | 1.96 sec: 1.08x faster                                                       |
| json_dumps           | 10.4 ms                                                | 10.1 ms: 1.03x faster                                                        |
| xml_etree_iterparse  | 102 ms                                                 | 99.4 ms: 1.03x faster                                                        |
| json_loads           | 27.0 us                                                | 26.8 us: 1.01x faster                                                        |
| pickle_dict          | 33.2 us                                                | 33.4 us: 1.01x slower                                                        |
| pickle               | 11.6 us                                                | 11.7 us: 1.01x slower                                                        |
| pickle_pure_python   | 300 us                                                 | 306 us: 1.02x slower                                                         |
| unpickle_pure_python | 213 us                                                 | 219 us: 1.02x slower                                                         |
| unpickle_list        | 4.96 us                                                | 5.31 us: 1.07x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                                 |

Benchmark hidden because not significant (2): unpickle, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_cold_10k-3.14.0a0-14c70a7 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.5 ms: 1.01x faster                                                        |
| python_startup_no_site | 6.99 ms                                                | 7.04 ms: 1.01x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.00x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_cold_10k-3.14.0a0-14c70a7 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 10.0 ms: 1.11x faster                                                        |
| django_template | 34.4 ms                                                | 35.4 ms: 1.03x slower                                                        |
| genshi_text     | 22.9 ms                                                | 25.5 ms: 1.11x slower                                                        |
| genshi_xml      | 50.3 ms                                                | 61.0 ms: 1.21x slower                                                        |
| Geometric mean  | (ref)                                                  | 1.06x slower                                                                 |

All benchmarks:
===============

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_cold_10k-3.14.0a0-14c70a7 |
|---------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| deepcopy_memo             | 38.0 us                                                | 27.1 us: 1.40x faster                                                        |
| deepcopy                  | 352 us                                                 | 265 us: 1.33x faster                                                         |
| deepcopy_reduce           | 3.17 us                                                | 2.63 us: 1.20x faster                                                        |
| async_tree_memoization_tg | 465 ms                                                 | 387 ms: 1.20x faster                                                         |
| scimark_fft               | 369 ms                                                 | 309 ms: 1.19x faster                                                         |
| richards_super            | 54.4 ms                                                | 47.0 ms: 1.16x faster                                                        |
| async_tree_memoization    | 442 ms                                                 | 395 ms: 1.12x faster                                                         |
| mako                      | 11.1 ms                                                | 10.0 ms: 1.11x faster                                                        |
| richards                  | 48.1 ms                                                | 43.5 ms: 1.11x faster                                                        |
| async_tree_none           | 354 ms                                                 | 321 ms: 1.10x faster                                                         |
| scimark_sparse_mat_mult   | 5.03 ms                                                | 4.56 ms: 1.10x faster                                                        |
| float                     | 78.5 ms                                                | 71.5 ms: 1.10x faster                                                        |
| xml_etree_generate        | 87.0 ms                                                | 79.8 ms: 1.09x faster                                                        |
| xml_etree_process         | 60.4 ms                                                | 55.5 ms: 1.09x faster                                                        |
| xml_etree_parse           | 156 ms                                                 | 145 ms: 1.08x faster                                                         |
| tomli_loads               | 2.11 sec                                               | 1.96 sec: 1.08x faster                                                       |
| nbody                     | 85.7 ms                                                | 79.7 ms: 1.08x faster                                                        |
| async_tree_none_tg        | 320 ms                                                 | 299 ms: 1.07x faster                                                         |
| scimark_monte_carlo       | 66.3 ms                                                | 61.9 ms: 1.07x faster                                                        |
| crypto_pyaes              | 73.0 ms                                                | 68.2 ms: 1.07x faster                                                        |
| regex_effbot              | 3.88 ms                                                | 3.65 ms: 1.07x faster                                                        |
| pathlib                   | 17.1 ms                                                | 16.2 ms: 1.05x faster                                                        |
| mdp                       | 2.74 sec                                               | 2.62 sec: 1.05x faster                                                       |
| scimark_sor               | 122 ms                                                 | 117 ms: 1.05x faster                                                         |
| telco                     | 8.45 ms                                                | 8.10 ms: 1.04x faster                                                        |
| sqlite_synth              | 2.85 us                                                | 2.74 us: 1.04x faster                                                        |
| json                      | 5.20 ms                                                | 5.02 ms: 1.03x faster                                                        |
| go                        | 142 ms                                                 | 137 ms: 1.03x faster                                                         |
| json_dumps                | 10.4 ms                                                | 10.1 ms: 1.03x faster                                                        |
| async_tree_cpu_io_mixed   | 574 ms                                                 | 558 ms: 1.03x faster                                                         |
| gc_traversal              | 3.81 ms                                                | 3.71 ms: 1.03x faster                                                        |
| xml_etree_iterparse       | 102 ms                                                 | 99.4 ms: 1.03x faster                                                        |
| regex_dna                 | 220 ms                                                 | 215 ms: 1.02x faster                                                         |
| spectral_norm             | 115 ms                                                 | 113 ms: 1.02x faster                                                         |
| html5lib                  | 64.5 ms                                                | 63.9 ms: 1.01x faster                                                        |
| thrift                    | 796 us                                                 | 790 us: 1.01x faster                                                         |
| json_loads                | 27.0 us                                                | 26.8 us: 1.01x faster                                                        |
| pyflate                   | 460 ms                                                 | 456 ms: 1.01x faster                                                         |
| python_startup            | 10.6 ms                                                | 10.5 ms: 1.01x faster                                                        |
| pidigits                  | 186 ms                                                 | 186 ms: 1.00x faster                                                         |
| asyncio_tcp               | 488 ms                                                 | 491 ms: 1.01x slower                                                         |
| pickle_dict               | 33.2 us                                                | 33.4 us: 1.01x slower                                                        |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.80 sec: 1.01x slower                                                       |
| python_startup_no_site    | 6.99 ms                                                | 7.04 ms: 1.01x slower                                                        |
| pickle                    | 11.6 us                                                | 11.7 us: 1.01x slower                                                        |
| logging_silent            | 102 ns                                                 | 103 ns: 1.01x slower                                                         |
| regex_v8                  | 25.3 ms                                                | 25.5 ms: 1.01x slower                                                        |
| fannkuch                  | 381 ms                                                 | 386 ms: 1.01x slower                                                         |
| coverage                  | 83.7 ms                                                | 85.3 ms: 1.02x slower                                                        |
| pickle_pure_python        | 300 us                                                 | 306 us: 1.02x slower                                                         |
| chaos                     | 58.4 ms                                                | 59.6 ms: 1.02x slower                                                        |
| comprehensions            | 16.4 us                                                | 16.8 us: 1.02x slower                                                        |
| unpickle_pure_python      | 213 us                                                 | 219 us: 1.02x slower                                                         |
| pprint_pformat            | 1.51 sec                                               | 1.55 sec: 1.03x slower                                                       |
| django_template           | 34.4 ms                                                | 35.4 ms: 1.03x slower                                                        |
| bench_thread_pool         | 815 us                                                 | 841 us: 1.03x slower                                                         |
| typing_runtime_protocols  | 159 us                                                 | 164 us: 1.03x slower                                                         |
| coroutines                | 22.5 ms                                                | 23.4 ms: 1.04x slower                                                        |
| bpe_tokeniser             | 4.69 sec                                               | 4.88 sec: 1.04x slower                                                       |
| tornado_http              | 91.5 ms                                                | 95.5 ms: 1.04x slower                                                        |
| async_tree_io             | 843 ms                                                 | 883 ms: 1.05x slower                                                         |
| async_tree_io_tg          | 825 ms                                                 | 874 ms: 1.06x slower                                                         |
| regex_compile             | 131 ms                                                 | 139 ms: 1.06x slower                                                         |
| sqlglot_parse             | 1.27 ms                                                | 1.34 ms: 1.06x slower                                                        |
| async_generators          | 433 ms                                                 | 460 ms: 1.06x slower                                                         |
| unpickle_list             | 4.96 us                                                | 5.31 us: 1.07x slower                                                        |
| create_gc_cycles          | 1.61 ms                                                | 1.72 ms: 1.07x slower                                                        |
| 2to3                      | 265 ms                                                 | 285 ms: 1.07x slower                                                         |
| sqlglot_transpile         | 1.57 ms                                                | 1.69 ms: 1.07x slower                                                        |
| raytrace                  | 262 ms                                                 | 281 ms: 1.08x slower                                                         |
| sqlglot_normalize         | 107 ms                                                 | 116 ms: 1.08x slower                                                         |
| nqueens                   | 80.6 ms                                                | 88.1 ms: 1.09x slower                                                        |
| sympy_expand              | 462 ms                                                 | 505 ms: 1.09x slower                                                         |
| dulwich_log               | 63.0 ms                                                | 68.9 ms: 1.09x slower                                                        |
| docutils                  | 2.58 sec                                               | 2.88 sec: 1.11x slower                                                       |
| genshi_text               | 22.9 ms                                                | 25.5 ms: 1.11x slower                                                        |
| sympy_str                 | 274 ms                                                 | 306 ms: 1.12x slower                                                         |
| sympy_sum                 | 150 ms                                                 | 173 ms: 1.15x slower                                                         |
| deltablue                 | 3.15 ms                                                | 3.68 ms: 1.17x slower                                                        |
| sqlglot_optimize          | 53.9 ms                                                | 63.7 ms: 1.18x slower                                                        |
| genshi_xml                | 50.3 ms                                                | 61.0 ms: 1.21x slower                                                        |
| pylint                    | 313 ms                                                 | 382 ms: 1.22x slower                                                         |
| generators                | 28.8 ms                                                | 36.2 ms: 1.26x slower                                                        |
| hexiom                    | 6.13 ms                                                | 7.89 ms: 1.29x slower                                                        |
| sympy_integrate           | 19.9 ms                                                | 26.5 ms: 1.33x slower                                                        |
| unpack_sequence           | 42.4 ns                                                | 109 ns: 2.58x slower                                                         |
| Geometric mean            | (ref)                                                  | 1.01x slower                                                                 |

Benchmark hidden because not significant (11): unpickle, pycparser, pprint_safe_repr, pickle_list, meteor_contest, bench_mp_pool, logging_simple, scimark_lu, asyncio_websockets, logging_format, async_tree_cpu_io_mixed_tg
Ignored benchmarks (7) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 68.81% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.05x