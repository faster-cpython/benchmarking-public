# Results vs. 3.13.0

- fork: savannahostrowski
- ref: jit_inv_mem_100k
- machine: linux-x86_64
- commit hash: 17ece50
- commit date: 2024-09-23
- overall geometric mean: 1.01x slower
- HPT reliability: 72.05%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_mem_100k-3.14.0a0-17ece50 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 280 ms: 1.06x slower                                                         |
| docutils       | 2.58 sec                                               | 2.93 sec: 1.13x slower                                                       |
| html5lib       | 64.5 ms                                                | 65.8 ms: 1.02x slower                                                        |
| tornado_http   | 91.5 ms                                                | 94.9 ms: 1.04x slower                                                        |
| Geometric mean | (ref)                                                  | 1.06x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_mem_100k-3.14.0a0-17ece50 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 465 ms                                                 | 391 ms: 1.19x faster                                                         |
| async_tree_none            | 354 ms                                                 | 318 ms: 1.11x faster                                                         |
| async_tree_memoization     | 442 ms                                                 | 409 ms: 1.08x faster                                                         |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.01x slower                                                       |
| asyncio_tcp                | 488 ms                                                 | 495 ms: 1.01x slower                                                         |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 552 ms: 1.02x slower                                                         |
| coroutines                 | 22.5 ms                                                | 23.1 ms: 1.03x slower                                                        |
| async_tree_io              | 843 ms                                                 | 886 ms: 1.05x slower                                                         |
| async_generators           | 433 ms                                                 | 457 ms: 1.06x slower                                                         |
| async_tree_io_tg           | 825 ms                                                 | 880 ms: 1.07x slower                                                         |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                                 |

Benchmark hidden because not significant (3): async_tree_none_tg, async_tree_cpu_io_mixed, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_mem_100k-3.14.0a0-17ece50 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 71.1 ms: 1.10x faster                                                        |
| nbody          | 85.7 ms                                                | 80.6 ms: 1.06x faster                                                        |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                         |
| Geometric mean | (ref)                                                  | 1.06x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_mem_100k-3.14.0a0-17ece50 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.65 ms: 1.06x faster                                                        |
| regex_dna      | 220 ms                                                 | 221 ms: 1.00x slower                                                         |
| regex_v8       | 25.3 ms                                                | 25.4 ms: 1.01x slower                                                        |
| regex_compile  | 131 ms                                                 | 144 ms: 1.10x slower                                                         |
| Geometric mean | (ref)                                                  | 1.01x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_mem_100k-3.14.0a0-17ece50 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_generate   | 87.0 ms                                                | 78.2 ms: 1.11x faster                                                        |
| tomli_loads          | 2.11 sec                                               | 1.92 sec: 1.10x faster                                                       |
| xml_etree_process    | 60.4 ms                                                | 55.6 ms: 1.09x faster                                                        |
| xml_etree_parse      | 156 ms                                                 | 148 ms: 1.05x faster                                                         |
| json_dumps           | 10.4 ms                                                | 10.0 ms: 1.04x faster                                                        |
| xml_etree_iterparse  | 102 ms                                                 | 98.8 ms: 1.03x faster                                                        |
| json_loads           | 27.0 us                                                | 27.2 us: 1.01x slower                                                        |
| pickle_pure_python   | 300 us                                                 | 308 us: 1.03x slower                                                         |
| pickle_list          | 5.01 us                                                | 5.15 us: 1.03x slower                                                        |
| pickle               | 11.6 us                                                | 11.9 us: 1.03x slower                                                        |
| unpickle_pure_python | 213 us                                                 | 221 us: 1.03x slower                                                         |
| unpickle_list        | 4.96 us                                                | 5.15 us: 1.04x slower                                                        |
| pickle_dict          | 33.2 us                                                | 34.9 us: 1.05x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                                 |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_mem_100k-3.14.0a0-17ece50 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.5 ms: 1.00x faster                                                        |
| python_startup_no_site | 6.99 ms                                                | 7.07 ms: 1.01x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.00x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_mem_100k-3.14.0a0-17ece50 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.75 ms: 1.14x faster                                                        |
| django_template | 34.4 ms                                                | 36.3 ms: 1.05x slower                                                        |
| genshi_text     | 22.9 ms                                                | 25.4 ms: 1.11x slower                                                        |
| genshi_xml      | 50.3 ms                                                | 59.2 ms: 1.18x slower                                                        |
| Geometric mean  | (ref)                                                  | 1.05x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_mem_100k-3.14.0a0-17ece50 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| deepcopy_memo              | 38.0 us                                                | 27.1 us: 1.40x faster                                                        |
| deepcopy                   | 352 us                                                 | 265 us: 1.33x faster                                                         |
| deepcopy_reduce            | 3.17 us                                                | 2.64 us: 1.20x faster                                                        |
| async_tree_memoization_tg  | 465 ms                                                 | 391 ms: 1.19x faster                                                         |
| richards_super             | 54.4 ms                                                | 46.0 ms: 1.18x faster                                                        |
| richards                   | 48.1 ms                                                | 40.9 ms: 1.18x faster                                                        |
| scimark_fft                | 369 ms                                                 | 317 ms: 1.16x faster                                                         |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.38 ms: 1.15x faster                                                        |
| mako                       | 11.1 ms                                                | 9.75 ms: 1.14x faster                                                        |
| xml_etree_generate         | 87.0 ms                                                | 78.2 ms: 1.11x faster                                                        |
| async_tree_none            | 354 ms                                                 | 318 ms: 1.11x faster                                                         |
| spectral_norm              | 115 ms                                                 | 104 ms: 1.11x faster                                                         |
| float                      | 78.5 ms                                                | 71.1 ms: 1.10x faster                                                        |
| tomli_loads                | 2.11 sec                                               | 1.92 sec: 1.10x faster                                                       |
| crypto_pyaes               | 73.0 ms                                                | 66.7 ms: 1.09x faster                                                        |
| xml_etree_process          | 60.4 ms                                                | 55.6 ms: 1.09x faster                                                        |
| async_tree_memoization     | 442 ms                                                 | 409 ms: 1.08x faster                                                         |
| mdp                        | 2.74 sec                                               | 2.54 sec: 1.08x faster                                                       |
| pathlib                    | 17.1 ms                                                | 15.9 ms: 1.07x faster                                                        |
| go                         | 142 ms                                                 | 132 ms: 1.07x faster                                                         |
| regex_effbot               | 3.88 ms                                                | 3.65 ms: 1.06x faster                                                        |
| nbody                      | 85.7 ms                                                | 80.6 ms: 1.06x faster                                                        |
| telco                      | 8.45 ms                                                | 7.98 ms: 1.06x faster                                                        |
| xml_etree_parse            | 156 ms                                                 | 148 ms: 1.05x faster                                                         |
| scimark_monte_carlo        | 66.3 ms                                                | 63.0 ms: 1.05x faster                                                        |
| scimark_sor                | 122 ms                                                 | 117 ms: 1.05x faster                                                         |
| bpe_tokeniser              | 4.69 sec                                               | 4.50 sec: 1.04x faster                                                       |
| json_dumps                 | 10.4 ms                                                | 10.0 ms: 1.04x faster                                                        |
| sqlite_synth               | 2.85 us                                                | 2.75 us: 1.04x faster                                                        |
| gc_traversal               | 3.81 ms                                                | 3.68 ms: 1.03x faster                                                        |
| xml_etree_iterparse        | 102 ms                                                 | 98.8 ms: 1.03x faster                                                        |
| scimark_lu                 | 115 ms                                                 | 111 ms: 1.03x faster                                                         |
| json                       | 5.20 ms                                                | 5.10 ms: 1.02x faster                                                        |
| thrift                     | 796 us                                                 | 786 us: 1.01x faster                                                         |
| python_startup             | 10.6 ms                                                | 10.5 ms: 1.00x faster                                                        |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                                         |
| regex_dna                  | 220 ms                                                 | 221 ms: 1.00x slower                                                         |
| meteor_contest             | 108 ms                                                 | 108 ms: 1.01x slower                                                         |
| regex_v8                   | 25.3 ms                                                | 25.4 ms: 1.01x slower                                                        |
| json_loads                 | 27.0 us                                                | 27.2 us: 1.01x slower                                                        |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.01x slower                                                       |
| python_startup_no_site     | 6.99 ms                                                | 7.07 ms: 1.01x slower                                                        |
| asyncio_tcp                | 488 ms                                                 | 495 ms: 1.01x slower                                                         |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 552 ms: 1.02x slower                                                         |
| html5lib                   | 64.5 ms                                                | 65.8 ms: 1.02x slower                                                        |
| pycparser                  | 1.19 sec                                               | 1.22 sec: 1.02x slower                                                       |
| chaos                      | 58.4 ms                                                | 59.6 ms: 1.02x slower                                                        |
| logging_silent             | 102 ns                                                 | 104 ns: 1.02x slower                                                         |
| deltablue                  | 3.15 ms                                                | 3.22 ms: 1.02x slower                                                        |
| coroutines                 | 22.5 ms                                                | 23.1 ms: 1.03x slower                                                        |
| pickle_pure_python         | 300 us                                                 | 308 us: 1.03x slower                                                         |
| pickle_list                | 5.01 us                                                | 5.15 us: 1.03x slower                                                        |
| pickle                     | 11.6 us                                                | 11.9 us: 1.03x slower                                                        |
| bench_thread_pool          | 815 us                                                 | 839 us: 1.03x slower                                                         |
| typing_runtime_protocols   | 159 us                                                 | 164 us: 1.03x slower                                                         |
| comprehensions             | 16.4 us                                                | 16.9 us: 1.03x slower                                                        |
| pprint_pformat             | 1.51 sec                                               | 1.56 sec: 1.03x slower                                                       |
| unpickle_pure_python       | 213 us                                                 | 221 us: 1.03x slower                                                         |
| tornado_http               | 91.5 ms                                                | 94.9 ms: 1.04x slower                                                        |
| unpickle_list              | 4.96 us                                                | 5.15 us: 1.04x slower                                                        |
| async_tree_io              | 843 ms                                                 | 886 ms: 1.05x slower                                                         |
| pickle_dict                | 33.2 us                                                | 34.9 us: 1.05x slower                                                        |
| django_template            | 34.4 ms                                                | 36.3 ms: 1.05x slower                                                        |
| async_generators           | 433 ms                                                 | 457 ms: 1.06x slower                                                         |
| 2to3                       | 265 ms                                                 | 280 ms: 1.06x slower                                                         |
| sqlglot_normalize          | 107 ms                                                 | 114 ms: 1.06x slower                                                         |
| sqlglot_parse              | 1.27 ms                                                | 1.35 ms: 1.06x slower                                                        |
| async_tree_io_tg           | 825 ms                                                 | 880 ms: 1.07x slower                                                         |
| create_gc_cycles           | 1.61 ms                                                | 1.72 ms: 1.07x slower                                                        |
| coverage                   | 83.7 ms                                                | 89.3 ms: 1.07x slower                                                        |
| raytrace                   | 262 ms                                                 | 281 ms: 1.08x slower                                                         |
| sqlglot_transpile          | 1.57 ms                                                | 1.69 ms: 1.08x slower                                                        |
| nqueens                    | 80.6 ms                                                | 87.1 ms: 1.08x slower                                                        |
| dulwich_log                | 63.0 ms                                                | 68.5 ms: 1.09x slower                                                        |
| sympy_expand               | 462 ms                                                 | 507 ms: 1.10x slower                                                         |
| regex_compile              | 131 ms                                                 | 144 ms: 1.10x slower                                                         |
| genshi_text                | 22.9 ms                                                | 25.4 ms: 1.11x slower                                                        |
| sympy_str                  | 274 ms                                                 | 305 ms: 1.11x slower                                                         |
| sqlglot_optimize           | 53.9 ms                                                | 60.7 ms: 1.13x slower                                                        |
| docutils                   | 2.58 sec                                               | 2.93 sec: 1.13x slower                                                       |
| hexiom                     | 6.13 ms                                                | 7.02 ms: 1.15x slower                                                        |
| sympy_integrate            | 19.9 ms                                                | 23.1 ms: 1.16x slower                                                        |
| sympy_sum                  | 150 ms                                                 | 176 ms: 1.17x slower                                                         |
| genshi_xml                 | 50.3 ms                                                | 59.2 ms: 1.18x slower                                                        |
| pylint                     | 313 ms                                                 | 378 ms: 1.21x slower                                                         |
| generators                 | 28.8 ms                                                | 35.2 ms: 1.22x slower                                                        |
| unpack_sequence            | 42.4 ns                                                | 107 ns: 2.53x slower                                                         |
| Geometric mean             | (ref)                                                  | 1.01x slower                                                                 |

Benchmark hidden because not significant (10): async_tree_none_tg, fannkuch, logging_format, pyflate, async_tree_cpu_io_mixed, unpickle, bench_mp_pool, asyncio_websockets, logging_simple, pprint_safe_repr
Ignored benchmarks (7) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 72.05% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.06x