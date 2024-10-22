# Results vs. 3.13.0

- fork: python
- ref: 33eeccf6d4f16e483b4c
- machine: linux-x86_64
- commit hash: 33eeccf
- commit date: 2024-09-17
- overall geometric mean: 1.00x slower
- HPT reliability: 59.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240917-linux-x86_64-python-33eeccf6d4f16e483b4c-3.14.0a0-33eeccf |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 276 ms: 1.04x slower                                                  |
| docutils       | 2.58 sec                                               | 2.96 sec: 1.15x slower                                                |
| html5lib       | 64.5 ms                                                | 65.1 ms: 1.01x slower                                                 |
| tornado_http   | 91.5 ms                                                | 94.4 ms: 1.03x slower                                                 |
| Geometric mean | (ref)                                                  | 1.06x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240917-linux-x86_64-python-33eeccf6d4f16e483b4c-3.14.0a0-33eeccf |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg  | 465 ms                                                 | 387 ms: 1.20x faster                                                  |
| async_tree_none            | 354 ms                                                 | 316 ms: 1.12x faster                                                  |
| async_tree_memoization     | 442 ms                                                 | 399 ms: 1.11x faster                                                  |
| async_tree_none_tg         | 320 ms                                                 | 306 ms: 1.04x faster                                                  |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.01x slower                                                |
| asyncio_tcp                | 488 ms                                                 | 497 ms: 1.02x slower                                                  |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 557 ms: 1.02x slower                                                  |
| async_generators           | 433 ms                                                 | 451 ms: 1.04x slower                                                  |
| coroutines                 | 22.5 ms                                                | 23.6 ms: 1.05x slower                                                 |
| async_tree_io_tg           | 825 ms                                                 | 870 ms: 1.05x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                          |

Benchmark hidden because not significant (3): async_tree_cpu_io_mixed, asyncio_websockets, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240917-linux-x86_64-python-33eeccf6d4f16e483b4c-3.14.0a0-33eeccf |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 69.9 ms: 1.12x faster                                                 |
| nbody          | 85.7 ms                                                | 79.7 ms: 1.08x faster                                                 |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                  | 1.07x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240917-linux-x86_64-python-33eeccf6d4f16e483b4c-3.14.0a0-33eeccf |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_v8       | 25.3 ms                                                | 24.6 ms: 1.03x faster                                                 |
| regex_effbot   | 3.88 ms                                                | 3.82 ms: 1.02x faster                                                 |
| regex_dna      | 220 ms                                                 | 224 ms: 1.02x slower                                                  |
| regex_compile  | 131 ms                                                 | 142 ms: 1.08x slower                                                  |
| Geometric mean | (ref)                                                  | 1.01x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240917-linux-x86_64-python-33eeccf6d4f16e483b4c-3.14.0a0-33eeccf |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_generate   | 87.0 ms                                                | 77.8 ms: 1.12x faster                                                 |
| xml_etree_process    | 60.4 ms                                                | 54.1 ms: 1.12x faster                                                 |
| tomli_loads          | 2.11 sec                                               | 1.95 sec: 1.08x faster                                                |
| xml_etree_parse      | 156 ms                                                 | 146 ms: 1.07x faster                                                  |
| xml_etree_iterparse  | 102 ms                                                 | 98.2 ms: 1.04x faster                                                 |
| json_dumps           | 10.4 ms                                                | 10.1 ms: 1.03x faster                                                 |
| pickle               | 11.6 us                                                | 11.4 us: 1.02x faster                                                 |
| unpickle             | 14.9 us                                                | 14.8 us: 1.01x faster                                                 |
| json_loads           | 27.0 us                                                | 26.9 us: 1.00x faster                                                 |
| unpickle_pure_python | 213 us                                                 | 215 us: 1.01x slower                                                  |
| pickle_list          | 5.01 us                                                | 5.09 us: 1.02x slower                                                 |
| pickle_pure_python   | 300 us                                                 | 307 us: 1.02x slower                                                  |
| pickle_dict          | 33.2 us                                                | 34.1 us: 1.03x slower                                                 |
| unpickle_list        | 4.96 us                                                | 5.40 us: 1.09x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240917-linux-x86_64-python-33eeccf6d4f16e483b4c-3.14.0a0-33eeccf |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 6.99 ms                                                | 7.09 ms: 1.02x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                          |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240917-linux-x86_64-python-33eeccf6d4f16e483b4c-3.14.0a0-33eeccf |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 10.0 ms: 1.11x faster                                                 |
| django_template | 34.4 ms                                                | 36.1 ms: 1.05x slower                                                 |
| genshi_text     | 22.9 ms                                                | 25.5 ms: 1.11x slower                                                 |
| genshi_xml      | 50.3 ms                                                | 59.6 ms: 1.18x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.06x slower                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240917-linux-x86_64-python-33eeccf6d4f16e483b4c-3.14.0a0-33eeccf |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy_memo              | 38.0 us                                                | 27.0 us: 1.41x faster                                                 |
| deepcopy                   | 352 us                                                 | 263 us: 1.34x faster                                                  |
| richards                   | 48.1 ms                                                | 39.7 ms: 1.21x faster                                                 |
| async_tree_memoization_tg  | 465 ms                                                 | 387 ms: 1.20x faster                                                  |
| richards_super             | 54.4 ms                                                | 45.7 ms: 1.19x faster                                                 |
| deepcopy_reduce            | 3.17 us                                                | 2.67 us: 1.19x faster                                                 |
| scimark_fft                | 369 ms                                                 | 312 ms: 1.18x faster                                                  |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.39 ms: 1.15x faster                                                 |
| float                      | 78.5 ms                                                | 69.9 ms: 1.12x faster                                                 |
| spectral_norm              | 115 ms                                                 | 102 ms: 1.12x faster                                                  |
| async_tree_none            | 354 ms                                                 | 316 ms: 1.12x faster                                                  |
| xml_etree_generate         | 87.0 ms                                                | 77.8 ms: 1.12x faster                                                 |
| xml_etree_process          | 60.4 ms                                                | 54.1 ms: 1.12x faster                                                 |
| async_tree_memoization     | 442 ms                                                 | 399 ms: 1.11x faster                                                  |
| mako                       | 11.1 ms                                                | 10.0 ms: 1.11x faster                                                 |
| crypto_pyaes               | 73.0 ms                                                | 66.2 ms: 1.10x faster                                                 |
| go                         | 142 ms                                                 | 130 ms: 1.08x faster                                                  |
| tomli_loads                | 2.11 sec                                               | 1.95 sec: 1.08x faster                                                |
| nbody                      | 85.7 ms                                                | 79.7 ms: 1.08x faster                                                 |
| xml_etree_parse            | 156 ms                                                 | 146 ms: 1.07x faster                                                  |
| telco                      | 8.45 ms                                                | 8.01 ms: 1.06x faster                                                 |
| scimark_lu                 | 115 ms                                                 | 109 ms: 1.05x faster                                                  |
| scimark_sor                | 122 ms                                                 | 116 ms: 1.05x faster                                                  |
| bpe_tokeniser              | 4.69 sec                                               | 4.45 sec: 1.05x faster                                                |
| pathlib                    | 17.1 ms                                                | 16.2 ms: 1.05x faster                                                 |
| async_tree_none_tg         | 320 ms                                                 | 306 ms: 1.04x faster                                                  |
| scimark_monte_carlo        | 66.3 ms                                                | 63.5 ms: 1.04x faster                                                 |
| xml_etree_iterparse        | 102 ms                                                 | 98.2 ms: 1.04x faster                                                 |
| json                       | 5.20 ms                                                | 5.02 ms: 1.04x faster                                                 |
| sqlite_synth               | 2.85 us                                                | 2.76 us: 1.03x faster                                                 |
| mdp                        | 2.74 sec                                               | 2.66 sec: 1.03x faster                                                |
| pycparser                  | 1.19 sec                                               | 1.16 sec: 1.03x faster                                                |
| json_dumps                 | 10.4 ms                                                | 10.1 ms: 1.03x faster                                                 |
| regex_v8                   | 25.3 ms                                                | 24.6 ms: 1.03x faster                                                 |
| pyflate                    | 460 ms                                                 | 448 ms: 1.03x faster                                                  |
| logging_format             | 6.25 us                                                | 6.10 us: 1.02x faster                                                 |
| fannkuch                   | 381 ms                                                 | 373 ms: 1.02x faster                                                  |
| thrift                     | 796 us                                                 | 781 us: 1.02x faster                                                  |
| pickle                     | 11.6 us                                                | 11.4 us: 1.02x faster                                                 |
| logging_simple             | 5.66 us                                                | 5.57 us: 1.02x faster                                                 |
| regex_effbot               | 3.88 ms                                                | 3.82 ms: 1.02x faster                                                 |
| meteor_contest             | 108 ms                                                 | 106 ms: 1.01x faster                                                  |
| unpickle                   | 14.9 us                                                | 14.8 us: 1.01x faster                                                 |
| json_loads                 | 27.0 us                                                | 26.9 us: 1.00x faster                                                 |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                                  |
| chaos                      | 58.4 ms                                                | 58.8 ms: 1.01x slower                                                 |
| html5lib                   | 64.5 ms                                                | 65.1 ms: 1.01x slower                                                 |
| unpickle_pure_python       | 213 us                                                 | 215 us: 1.01x slower                                                  |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.01x slower                                                |
| pprint_safe_repr           | 744 ms                                                 | 753 ms: 1.01x slower                                                  |
| python_startup_no_site     | 6.99 ms                                                | 7.09 ms: 1.02x slower                                                 |
| pickle_list                | 5.01 us                                                | 5.09 us: 1.02x slower                                                 |
| logging_silent             | 102 ns                                                 | 104 ns: 1.02x slower                                                  |
| coverage                   | 83.7 ms                                                | 85.2 ms: 1.02x slower                                                 |
| comprehensions             | 16.4 us                                                | 16.7 us: 1.02x slower                                                 |
| asyncio_tcp                | 488 ms                                                 | 497 ms: 1.02x slower                                                  |
| deltablue                  | 3.15 ms                                                | 3.21 ms: 1.02x slower                                                 |
| regex_dna                  | 220 ms                                                 | 224 ms: 1.02x slower                                                  |
| pickle_pure_python         | 300 us                                                 | 307 us: 1.02x slower                                                  |
| gc_traversal               | 3.81 ms                                                | 3.90 ms: 1.02x slower                                                 |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 557 ms: 1.02x slower                                                  |
| bench_thread_pool          | 815 us                                                 | 837 us: 1.03x slower                                                  |
| pickle_dict                | 33.2 us                                                | 34.1 us: 1.03x slower                                                 |
| typing_runtime_protocols   | 159 us                                                 | 164 us: 1.03x slower                                                  |
| tornado_http               | 91.5 ms                                                | 94.4 ms: 1.03x slower                                                 |
| pprint_pformat             | 1.51 sec                                               | 1.57 sec: 1.04x slower                                                |
| nqueens                    | 80.6 ms                                                | 83.9 ms: 1.04x slower                                                 |
| async_generators           | 433 ms                                                 | 451 ms: 1.04x slower                                                  |
| 2to3                       | 265 ms                                                 | 276 ms: 1.04x slower                                                  |
| coroutines                 | 22.5 ms                                                | 23.6 ms: 1.05x slower                                                 |
| django_template            | 34.4 ms                                                | 36.1 ms: 1.05x slower                                                 |
| async_tree_io_tg           | 825 ms                                                 | 870 ms: 1.05x slower                                                  |
| raytrace                   | 262 ms                                                 | 276 ms: 1.05x slower                                                  |
| sqlglot_normalize          | 107 ms                                                 | 113 ms: 1.06x slower                                                  |
| sqlglot_parse              | 1.27 ms                                                | 1.34 ms: 1.06x slower                                                 |
| dulwich_log                | 63.0 ms                                                | 67.6 ms: 1.07x slower                                                 |
| sqlglot_transpile          | 1.57 ms                                                | 1.69 ms: 1.07x slower                                                 |
| sqlglot_optimize           | 53.9 ms                                                | 58.0 ms: 1.08x slower                                                 |
| regex_compile              | 131 ms                                                 | 142 ms: 1.08x slower                                                  |
| unpickle_list              | 4.96 us                                                | 5.40 us: 1.09x slower                                                 |
| sympy_expand               | 462 ms                                                 | 503 ms: 1.09x slower                                                  |
| create_gc_cycles           | 1.61 ms                                                | 1.76 ms: 1.09x slower                                                 |
| sympy_str                  | 274 ms                                                 | 299 ms: 1.09x slower                                                  |
| genshi_text                | 22.9 ms                                                | 25.5 ms: 1.11x slower                                                 |
| hexiom                     | 6.13 ms                                                | 6.88 ms: 1.12x slower                                                 |
| generators                 | 28.8 ms                                                | 32.7 ms: 1.14x slower                                                 |
| sympy_integrate            | 19.9 ms                                                | 22.8 ms: 1.15x slower                                                 |
| docutils                   | 2.58 sec                                               | 2.96 sec: 1.15x slower                                                |
| sympy_sum                  | 150 ms                                                 | 172 ms: 1.15x slower                                                  |
| genshi_xml                 | 50.3 ms                                                | 59.6 ms: 1.18x slower                                                 |
| pylint                     | 313 ms                                                 | 372 ms: 1.19x slower                                                  |
| unpack_sequence            | 42.4 ns                                                | 112 ns: 2.65x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.00x slower                                                          |

Benchmark hidden because not significant (5): python_startup, async_tree_cpu_io_mixed, bench_mp_pool, asyncio_websockets, async_tree_io
Ignored benchmarks (7) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 59.00% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.08x