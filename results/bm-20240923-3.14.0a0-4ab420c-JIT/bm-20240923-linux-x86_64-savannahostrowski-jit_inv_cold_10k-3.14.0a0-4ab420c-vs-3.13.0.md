# Results vs. 3.13.0

- fork: savannahostrowski
- ref: jit_inv_cold_10k
- machine: linux-x86_64
- commit hash: 4ab420c
- commit date: 2024-09-23
- overall geometric mean: 1.02x slower
- HPT reliability: 88.31%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_cold_10k-3.14.0a0-4ab420c |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 285 ms: 1.08x slower                                                         |
| docutils       | 2.58 sec                                               | 2.89 sec: 1.12x slower                                                       |
| html5lib       | 64.5 ms                                                | 66.2 ms: 1.03x slower                                                        |
| tornado_http   | 91.5 ms                                                | 96.0 ms: 1.05x slower                                                        |
| Geometric mean | (ref)                                                  | 1.07x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_cold_10k-3.14.0a0-4ab420c |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 465 ms                                                 | 389 ms: 1.20x faster                                                         |
| async_tree_memoization     | 442 ms                                                 | 399 ms: 1.11x faster                                                         |
| async_tree_none            | 354 ms                                                 | 320 ms: 1.11x faster                                                         |
| async_tree_none_tg         | 320 ms                                                 | 301 ms: 1.06x faster                                                         |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.01x slower                                                       |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 551 ms: 1.01x slower                                                         |
| asyncio_tcp                | 488 ms                                                 | 495 ms: 1.01x slower                                                         |
| coroutines                 | 22.5 ms                                                | 23.5 ms: 1.04x slower                                                        |
| async_tree_io              | 843 ms                                                 | 886 ms: 1.05x slower                                                         |
| async_generators           | 433 ms                                                 | 456 ms: 1.05x slower                                                         |
| async_tree_io_tg           | 825 ms                                                 | 878 ms: 1.06x slower                                                         |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                                 |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_cold_10k-3.14.0a0-4ab420c |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 71.4 ms: 1.10x faster                                                        |
| nbody          | 85.7 ms                                                | 82.1 ms: 1.04x faster                                                        |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                         |
| Geometric mean | (ref)                                                  | 1.05x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_cold_10k-3.14.0a0-4ab420c |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.78 ms: 1.03x faster                                                        |
| regex_dna      | 220 ms                                                 | 224 ms: 1.02x slower                                                         |
| regex_v8       | 25.3 ms                                                | 26.2 ms: 1.04x slower                                                        |
| regex_compile  | 131 ms                                                 | 139 ms: 1.06x slower                                                         |
| Geometric mean | (ref)                                                  | 1.02x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_cold_10k-3.14.0a0-4ab420c |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 2.11 sec                                               | 1.93 sec: 1.09x faster                                                       |
| xml_etree_generate   | 87.0 ms                                                | 80.7 ms: 1.08x faster                                                        |
| xml_etree_process    | 60.4 ms                                                | 56.2 ms: 1.07x faster                                                        |
| xml_etree_parse      | 156 ms                                                 | 149 ms: 1.05x faster                                                         |
| json_dumps           | 10.4 ms                                                | 10.2 ms: 1.03x faster                                                        |
| xml_etree_iterparse  | 102 ms                                                 | 99.7 ms: 1.02x faster                                                        |
| pickle_pure_python   | 300 us                                                 | 303 us: 1.01x slower                                                         |
| pickle               | 11.6 us                                                | 11.7 us: 1.01x slower                                                        |
| json_loads           | 27.0 us                                                | 27.4 us: 1.01x slower                                                        |
| unpickle_pure_python | 213 us                                                 | 219 us: 1.03x slower                                                         |
| pickle_list          | 5.01 us                                                | 5.18 us: 1.03x slower                                                        |
| pickle_dict          | 33.2 us                                                | 34.6 us: 1.04x slower                                                        |
| unpickle_list        | 4.96 us                                                | 5.32 us: 1.07x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                                 |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_cold_10k-3.14.0a0-4ab420c |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.5 ms: 1.01x faster                                                        |
| python_startup_no_site | 6.99 ms                                                | 7.05 ms: 1.01x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.00x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_cold_10k-3.14.0a0-4ab420c |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.94 ms: 1.12x faster                                                        |
| django_template | 34.4 ms                                                | 36.9 ms: 1.07x slower                                                        |
| genshi_text     | 22.9 ms                                                | 25.7 ms: 1.12x slower                                                        |
| genshi_xml      | 50.3 ms                                                | 60.8 ms: 1.21x slower                                                        |
| Geometric mean  | (ref)                                                  | 1.07x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_cold_10k-3.14.0a0-4ab420c |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| deepcopy_memo              | 38.0 us                                                | 27.0 us: 1.41x faster                                                        |
| deepcopy                   | 352 us                                                 | 269 us: 1.31x faster                                                         |
| async_tree_memoization_tg  | 465 ms                                                 | 389 ms: 1.20x faster                                                         |
| deepcopy_reduce            | 3.17 us                                                | 2.67 us: 1.19x faster                                                        |
| scimark_fft                | 369 ms                                                 | 317 ms: 1.16x faster                                                         |
| richards_super             | 54.4 ms                                                | 47.0 ms: 1.16x faster                                                        |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.40 ms: 1.14x faster                                                        |
| richards                   | 48.1 ms                                                | 42.7 ms: 1.13x faster                                                        |
| mako                       | 11.1 ms                                                | 9.94 ms: 1.12x faster                                                        |
| async_tree_memoization     | 442 ms                                                 | 399 ms: 1.11x faster                                                         |
| async_tree_none            | 354 ms                                                 | 320 ms: 1.11x faster                                                         |
| float                      | 78.5 ms                                                | 71.4 ms: 1.10x faster                                                        |
| tomli_loads                | 2.11 sec                                               | 1.93 sec: 1.09x faster                                                       |
| xml_etree_generate         | 87.0 ms                                                | 80.7 ms: 1.08x faster                                                        |
| crypto_pyaes               | 73.0 ms                                                | 67.9 ms: 1.08x faster                                                        |
| xml_etree_process          | 60.4 ms                                                | 56.2 ms: 1.07x faster                                                        |
| mdp                        | 2.74 sec                                               | 2.55 sec: 1.07x faster                                                       |
| async_tree_none_tg         | 320 ms                                                 | 301 ms: 1.06x faster                                                         |
| pathlib                    | 17.1 ms                                                | 16.1 ms: 1.06x faster                                                        |
| telco                      | 8.45 ms                                                | 8.03 ms: 1.05x faster                                                        |
| xml_etree_parse            | 156 ms                                                 | 149 ms: 1.05x faster                                                         |
| scimark_sor                | 122 ms                                                 | 117 ms: 1.04x faster                                                         |
| nbody                      | 85.7 ms                                                | 82.1 ms: 1.04x faster                                                        |
| go                         | 142 ms                                                 | 136 ms: 1.04x faster                                                         |
| scimark_monte_carlo        | 66.3 ms                                                | 63.7 ms: 1.04x faster                                                        |
| sqlite_synth               | 2.85 us                                                | 2.77 us: 1.03x faster                                                        |
| regex_effbot               | 3.88 ms                                                | 3.78 ms: 1.03x faster                                                        |
| json_dumps                 | 10.4 ms                                                | 10.2 ms: 1.03x faster                                                        |
| spectral_norm              | 115 ms                                                 | 112 ms: 1.02x faster                                                         |
| xml_etree_iterparse        | 102 ms                                                 | 99.7 ms: 1.02x faster                                                        |
| json                       | 5.20 ms                                                | 5.08 ms: 1.02x faster                                                        |
| fannkuch                   | 381 ms                                                 | 376 ms: 1.01x faster                                                         |
| thrift                     | 796 us                                                 | 786 us: 1.01x faster                                                         |
| logging_format             | 6.25 us                                                | 6.18 us: 1.01x faster                                                        |
| meteor_contest             | 108 ms                                                 | 106 ms: 1.01x faster                                                         |
| pyflate                    | 460 ms                                                 | 456 ms: 1.01x faster                                                         |
| python_startup             | 10.6 ms                                                | 10.5 ms: 1.01x faster                                                        |
| gc_traversal               | 3.81 ms                                                | 3.80 ms: 1.00x faster                                                        |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                                         |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.01x slower                                                       |
| python_startup_no_site     | 6.99 ms                                                | 7.05 ms: 1.01x slower                                                        |
| pickle_pure_python         | 300 us                                                 | 303 us: 1.01x slower                                                         |
| pickle                     | 11.6 us                                                | 11.7 us: 1.01x slower                                                        |
| json_loads                 | 27.0 us                                                | 27.4 us: 1.01x slower                                                        |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 551 ms: 1.01x slower                                                         |
| asyncio_tcp                | 488 ms                                                 | 495 ms: 1.01x slower                                                         |
| chaos                      | 58.4 ms                                                | 59.3 ms: 1.01x slower                                                        |
| regex_dna                  | 220 ms                                                 | 224 ms: 1.02x slower                                                         |
| pprint_safe_repr           | 744 ms                                                 | 760 ms: 1.02x slower                                                         |
| unpickle_pure_python       | 213 us                                                 | 219 us: 1.03x slower                                                         |
| html5lib                   | 64.5 ms                                                | 66.2 ms: 1.03x slower                                                        |
| comprehensions             | 16.4 us                                                | 16.8 us: 1.03x slower                                                        |
| pycparser                  | 1.19 sec                                               | 1.23 sec: 1.03x slower                                                       |
| bench_thread_pool          | 815 us                                                 | 841 us: 1.03x slower                                                         |
| pickle_list                | 5.01 us                                                | 5.18 us: 1.03x slower                                                        |
| pprint_pformat             | 1.51 sec                                               | 1.57 sec: 1.04x slower                                                       |
| regex_v8                   | 25.3 ms                                                | 26.2 ms: 1.04x slower                                                        |
| coverage                   | 83.7 ms                                                | 86.9 ms: 1.04x slower                                                        |
| typing_runtime_protocols   | 159 us                                                 | 165 us: 1.04x slower                                                         |
| coroutines                 | 22.5 ms                                                | 23.5 ms: 1.04x slower                                                        |
| pickle_dict                | 33.2 us                                                | 34.6 us: 1.04x slower                                                        |
| bpe_tokeniser              | 4.69 sec                                               | 4.90 sec: 1.05x slower                                                       |
| tornado_http               | 91.5 ms                                                | 96.0 ms: 1.05x slower                                                        |
| async_tree_io              | 843 ms                                                 | 886 ms: 1.05x slower                                                         |
| async_generators           | 433 ms                                                 | 456 ms: 1.05x slower                                                         |
| regex_compile              | 131 ms                                                 | 139 ms: 1.06x slower                                                         |
| async_tree_io_tg           | 825 ms                                                 | 878 ms: 1.06x slower                                                         |
| sqlglot_parse              | 1.27 ms                                                | 1.35 ms: 1.07x slower                                                        |
| create_gc_cycles           | 1.61 ms                                                | 1.72 ms: 1.07x slower                                                        |
| django_template            | 34.4 ms                                                | 36.9 ms: 1.07x slower                                                        |
| unpickle_list              | 4.96 us                                                | 5.32 us: 1.07x slower                                                        |
| sqlglot_transpile          | 1.57 ms                                                | 1.69 ms: 1.07x slower                                                        |
| 2to3                       | 265 ms                                                 | 285 ms: 1.08x slower                                                         |
| raytrace                   | 262 ms                                                 | 281 ms: 1.08x slower                                                         |
| dulwich_log                | 63.0 ms                                                | 68.1 ms: 1.08x slower                                                        |
| nqueens                    | 80.6 ms                                                | 87.7 ms: 1.09x slower                                                        |
| sympy_expand               | 462 ms                                                 | 503 ms: 1.09x slower                                                         |
| sqlglot_normalize          | 107 ms                                                 | 117 ms: 1.09x slower                                                         |
| docutils                   | 2.58 sec                                               | 2.89 sec: 1.12x slower                                                       |
| genshi_text                | 22.9 ms                                                | 25.7 ms: 1.12x slower                                                        |
| sympy_str                  | 274 ms                                                 | 308 ms: 1.13x slower                                                         |
| sympy_sum                  | 150 ms                                                 | 172 ms: 1.15x slower                                                         |
| deltablue                  | 3.15 ms                                                | 3.65 ms: 1.16x slower                                                        |
| sqlglot_optimize           | 53.9 ms                                                | 64.3 ms: 1.19x slower                                                        |
| genshi_xml                 | 50.3 ms                                                | 60.8 ms: 1.21x slower                                                        |
| pylint                     | 313 ms                                                 | 380 ms: 1.21x slower                                                         |
| generators                 | 28.8 ms                                                | 35.6 ms: 1.23x slower                                                        |
| hexiom                     | 6.13 ms                                                | 7.80 ms: 1.27x slower                                                        |
| sympy_integrate            | 19.9 ms                                                | 26.7 ms: 1.34x slower                                                        |
| unpack_sequence            | 42.4 ns                                                | 112 ns: 2.64x slower                                                         |
| Geometric mean             | (ref)                                                  | 1.02x slower                                                                 |

Benchmark hidden because not significant (7): async_tree_cpu_io_mixed, asyncio_websockets, bench_mp_pool, logging_simple, logging_silent, scimark_lu, unpickle
Ignored benchmarks (7) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 88.31% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.05x