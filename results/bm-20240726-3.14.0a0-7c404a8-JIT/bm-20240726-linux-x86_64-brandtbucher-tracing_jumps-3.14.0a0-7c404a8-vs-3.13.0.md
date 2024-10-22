# Results vs. 3.13.0

- fork: brandtbucher
- ref: tracing_jumps
- machine: linux-x86_64
- commit hash: 7c404a8
- commit date: 2024-07-26
- overall geometric mean: 1.01x faster
- HPT reliability: 64.28%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240726-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-7c404a8 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 275 ms: 1.04x slower                                                 |
| docutils       | 2.58 sec                                               | 2.90 sec: 1.12x slower                                               |
| html5lib       | 64.5 ms                                                | 65.2 ms: 1.01x slower                                                |
| tornado_http   | 91.5 ms                                                | 92.5 ms: 1.01x slower                                                |
| Geometric mean | (ref)                                                  | 1.04x slower                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240726-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-7c404a8 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_memoization_tg  | 465 ms                                                 | 390 ms: 1.19x faster                                                 |
| async_tree_memoization     | 442 ms                                                 | 394 ms: 1.12x faster                                                 |
| async_tree_none            | 354 ms                                                 | 326 ms: 1.09x faster                                                 |
| async_tree_none_tg         | 320 ms                                                 | 300 ms: 1.07x faster                                                 |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 532 ms: 1.02x faster                                                 |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 564 ms: 1.02x faster                                                 |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.01x slower                                               |
| asyncio_tcp                | 488 ms                                                 | 498 ms: 1.02x slower                                                 |
| async_generators           | 433 ms                                                 | 455 ms: 1.05x slower                                                 |
| async_tree_io_tg           | 825 ms                                                 | 871 ms: 1.06x slower                                                 |
| async_tree_io              | 843 ms                                                 | 902 ms: 1.07x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                         |

Benchmark hidden because not significant (2): asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240726-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-7c404a8 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 70.3 ms: 1.12x faster                                                |
| nbody          | 85.7 ms                                                | 80.2 ms: 1.07x faster                                                |
| pidigits       | 186 ms                                                 | 185 ms: 1.00x faster                                                 |
| Geometric mean | (ref)                                                  | 1.06x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240726-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-7c404a8 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.79 ms: 1.02x faster                                                |
| regex_dna      | 220 ms                                                 | 221 ms: 1.00x slower                                                 |
| regex_compile  | 131 ms                                                 | 134 ms: 1.02x slower                                                 |
| regex_v8       | 25.3 ms                                                | 25.9 ms: 1.03x slower                                                |
| Geometric mean | (ref)                                                  | 1.01x slower                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240726-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-7c404a8 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| xml_etree_generate   | 87.0 ms                                                | 80.6 ms: 1.08x faster                                                |
| xml_etree_process    | 60.4 ms                                                | 56.1 ms: 1.08x faster                                                |
| tomli_loads          | 2.11 sec                                               | 1.97 sec: 1.07x faster                                               |
| xml_etree_parse      | 156 ms                                                 | 146 ms: 1.07x faster                                                 |
| xml_etree_iterparse  | 102 ms                                                 | 99.1 ms: 1.03x faster                                                |
| json_dumps           | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                |
| pickle_pure_python   | 300 us                                                 | 298 us: 1.01x faster                                                 |
| unpickle_pure_python | 213 us                                                 | 216 us: 1.01x slower                                                 |
| json_loads           | 27.0 us                                                | 28.3 us: 1.05x slower                                                |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240726-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-7c404a8 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.6 ms: 1.00x slower                                                |
| python_startup_no_site | 6.99 ms                                                | 7.17 ms: 1.03x slower                                                |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240726-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-7c404a8 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.65 ms: 1.15x faster                                                |
| django_template | 34.4 ms                                                | 36.0 ms: 1.05x slower                                                |
| genshi_xml      | 50.3 ms                                                | 53.1 ms: 1.05x slower                                                |
| genshi_text     | 22.9 ms                                                | 24.2 ms: 1.06x slower                                                |
| Geometric mean  | (ref)                                                  | 1.00x slower                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240726-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-7c404a8 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| deepcopy_memo              | 38.0 us                                                | 28.5 us: 1.33x faster                                                |
| deepcopy                   | 352 us                                                 | 269 us: 1.31x faster                                                 |
| scimark_fft                | 369 ms                                                 | 309 ms: 1.19x faster                                                 |
| async_tree_memoization_tg  | 465 ms                                                 | 390 ms: 1.19x faster                                                 |
| richards                   | 48.1 ms                                                | 41.4 ms: 1.16x faster                                                |
| richards_super             | 54.4 ms                                                | 47.1 ms: 1.16x faster                                                |
| mako                       | 11.1 ms                                                | 9.65 ms: 1.15x faster                                                |
| deepcopy_reduce            | 3.17 us                                                | 2.77 us: 1.14x faster                                                |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.45 ms: 1.13x faster                                                |
| async_tree_memoization     | 442 ms                                                 | 394 ms: 1.12x faster                                                 |
| float                      | 78.5 ms                                                | 70.3 ms: 1.12x faster                                                |
| spectral_norm              | 115 ms                                                 | 103 ms: 1.12x faster                                                 |
| scimark_monte_carlo        | 66.3 ms                                                | 60.9 ms: 1.09x faster                                                |
| async_tree_none            | 354 ms                                                 | 326 ms: 1.09x faster                                                 |
| crypto_pyaes               | 73.0 ms                                                | 67.5 ms: 1.08x faster                                                |
| xml_etree_generate         | 87.0 ms                                                | 80.6 ms: 1.08x faster                                                |
| xml_etree_process          | 60.4 ms                                                | 56.1 ms: 1.08x faster                                                |
| tomli_loads                | 2.11 sec                                               | 1.97 sec: 1.07x faster                                               |
| nbody                      | 85.7 ms                                                | 80.2 ms: 1.07x faster                                                |
| async_tree_none_tg         | 320 ms                                                 | 300 ms: 1.07x faster                                                 |
| xml_etree_parse            | 156 ms                                                 | 146 ms: 1.07x faster                                                 |
| telco                      | 8.45 ms                                                | 7.96 ms: 1.06x faster                                                |
| pathlib                    | 17.1 ms                                                | 16.1 ms: 1.06x faster                                                |
| pyflate                    | 460 ms                                                 | 435 ms: 1.06x faster                                                 |
| pprint_safe_repr           | 744 ms                                                 | 707 ms: 1.05x faster                                                 |
| fannkuch                   | 381 ms                                                 | 366 ms: 1.04x faster                                                 |
| bpe_tokeniser              | 4.69 sec                                               | 4.51 sec: 1.04x faster                                               |
| pprint_pformat             | 1.51 sec                                               | 1.46 sec: 1.03x faster                                               |
| meteor_contest             | 108 ms                                                 | 104 ms: 1.03x faster                                                 |
| xml_etree_iterparse        | 102 ms                                                 | 99.1 ms: 1.03x faster                                                |
| logging_format             | 6.25 us                                                | 6.09 us: 1.03x faster                                                |
| logging_simple             | 5.66 us                                                | 5.53 us: 1.03x faster                                                |
| regex_effbot               | 3.88 ms                                                | 3.79 ms: 1.02x faster                                                |
| pycparser                  | 1.19 sec                                               | 1.17 sec: 1.02x faster                                               |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 532 ms: 1.02x faster                                                 |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 564 ms: 1.02x faster                                                 |
| chaos                      | 58.4 ms                                                | 57.7 ms: 1.01x faster                                                |
| json_dumps                 | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                |
| comprehensions             | 16.4 us                                                | 16.2 us: 1.01x faster                                                |
| thrift                     | 796 us                                                 | 789 us: 1.01x faster                                                 |
| gc_traversal               | 3.81 ms                                                | 3.77 ms: 1.01x faster                                                |
| pickle_pure_python         | 300 us                                                 | 298 us: 1.01x faster                                                 |
| mdp                        | 2.74 sec                                               | 2.72 sec: 1.01x faster                                               |
| pidigits                   | 186 ms                                                 | 185 ms: 1.00x faster                                                 |
| python_startup             | 10.6 ms                                                | 10.6 ms: 1.00x slower                                                |
| regex_dna                  | 220 ms                                                 | 221 ms: 1.00x slower                                                 |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.01x slower                                               |
| html5lib                   | 64.5 ms                                                | 65.2 ms: 1.01x slower                                                |
| tornado_http               | 91.5 ms                                                | 92.5 ms: 1.01x slower                                                |
| unpickle_pure_python       | 213 us                                                 | 216 us: 1.01x slower                                                 |
| sqlglot_parse              | 1.27 ms                                                | 1.29 ms: 1.02x slower                                                |
| asyncio_tcp                | 488 ms                                                 | 498 ms: 1.02x slower                                                 |
| regex_compile              | 131 ms                                                 | 134 ms: 1.02x slower                                                 |
| regex_v8                   | 25.3 ms                                                | 25.9 ms: 1.03x slower                                                |
| python_startup_no_site     | 6.99 ms                                                | 7.17 ms: 1.03x slower                                                |
| sqlglot_transpile          | 1.57 ms                                                | 1.62 ms: 1.03x slower                                                |
| sqlglot_optimize           | 53.9 ms                                                | 55.6 ms: 1.03x slower                                                |
| raytrace                   | 262 ms                                                 | 270 ms: 1.03x slower                                                 |
| 2to3                       | 265 ms                                                 | 275 ms: 1.04x slower                                                 |
| logging_silent             | 102 ns                                                 | 106 ns: 1.04x slower                                                 |
| go                         | 142 ms                                                 | 148 ms: 1.05x slower                                                 |
| nqueens                    | 80.6 ms                                                | 84.4 ms: 1.05x slower                                                |
| sqlglot_normalize          | 107 ms                                                 | 112 ms: 1.05x slower                                                 |
| django_template            | 34.4 ms                                                | 36.0 ms: 1.05x slower                                                |
| json_loads                 | 27.0 us                                                | 28.3 us: 1.05x slower                                                |
| scimark_sor                | 122 ms                                                 | 129 ms: 1.05x slower                                                 |
| async_generators           | 433 ms                                                 | 455 ms: 1.05x slower                                                 |
| genshi_xml                 | 50.3 ms                                                | 53.1 ms: 1.05x slower                                                |
| async_tree_io_tg           | 825 ms                                                 | 871 ms: 1.06x slower                                                 |
| genshi_text                | 22.9 ms                                                | 24.2 ms: 1.06x slower                                                |
| async_tree_io              | 843 ms                                                 | 902 ms: 1.07x slower                                                 |
| dask                       | 338 ms                                                 | 364 ms: 1.08x slower                                                 |
| scimark_lu                 | 115 ms                                                 | 124 ms: 1.08x slower                                                 |
| hexiom                     | 6.13 ms                                                | 6.63 ms: 1.08x slower                                                |
| sympy_str                  | 274 ms                                                 | 296 ms: 1.08x slower                                                 |
| typing_runtime_protocols   | 159 us                                                 | 173 us: 1.08x slower                                                 |
| create_gc_cycles           | 1.61 ms                                                | 1.76 ms: 1.09x slower                                                |
| sympy_expand               | 462 ms                                                 | 505 ms: 1.09x slower                                                 |
| dulwich_log                | 63.0 ms                                                | 69.4 ms: 1.10x slower                                                |
| coverage                   | 83.7 ms                                                | 92.7 ms: 1.11x slower                                                |
| docutils                   | 2.58 sec                                               | 2.90 sec: 1.12x slower                                               |
| sympy_integrate            | 19.9 ms                                                | 22.3 ms: 1.12x slower                                                |
| sympy_sum                  | 150 ms                                                 | 168 ms: 1.13x slower                                                 |
| deltablue                  | 3.15 ms                                                | 3.57 ms: 1.13x slower                                                |
| pylint                     | 313 ms                                                 | 355 ms: 1.14x slower                                                 |
| generators                 | 28.8 ms                                                | 33.1 ms: 1.15x slower                                                |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                         |

Benchmark hidden because not significant (5): json, asyncio_websockets, bench_mp_pool, bench_thread_pool, coroutines
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 64.28% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.08x