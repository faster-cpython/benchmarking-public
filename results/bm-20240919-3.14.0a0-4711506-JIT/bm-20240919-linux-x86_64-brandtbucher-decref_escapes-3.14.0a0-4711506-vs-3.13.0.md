# Results vs. 3.13.0

- fork: brandtbucher
- ref: decref_escapes
- machine: linux-x86_64
- commit hash: 4711506
- commit date: 2024-09-19
- overall geometric mean: 1.00x slower
- HPT reliability: 51.25%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240919-linux-x86_64-brandtbucher-decref_escapes-3.14.0a0-4711506 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 277 ms: 1.04x slower                                                  |
| docutils       | 2.58 sec                                               | 2.97 sec: 1.15x slower                                                |
| html5lib       | 64.5 ms                                                | 63.8 ms: 1.01x faster                                                 |
| tornado_http   | 91.5 ms                                                | 95.1 ms: 1.04x slower                                                 |
| Geometric mean | (ref)                                                  | 1.05x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240919-linux-x86_64-brandtbucher-decref_escapes-3.14.0a0-4711506 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg  | 465 ms                                                 | 389 ms: 1.19x faster                                                  |
| async_tree_none            | 354 ms                                                 | 319 ms: 1.11x faster                                                  |
| async_tree_memoization     | 442 ms                                                 | 403 ms: 1.10x faster                                                  |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.01x slower                                                |
| asyncio_tcp                | 488 ms                                                 | 498 ms: 1.02x slower                                                  |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 555 ms: 1.02x slower                                                  |
| coroutines                 | 22.5 ms                                                | 23.0 ms: 1.02x slower                                                 |
| async_generators           | 433 ms                                                 | 451 ms: 1.04x slower                                                  |
| async_tree_io_tg           | 825 ms                                                 | 876 ms: 1.06x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                          |

Benchmark hidden because not significant (4): async_tree_none_tg, async_tree_cpu_io_mixed, asyncio_websockets, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240919-linux-x86_64-brandtbucher-decref_escapes-3.14.0a0-4711506 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 70.7 ms: 1.11x faster                                                 |
| nbody          | 85.7 ms                                                | 80.2 ms: 1.07x faster                                                 |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                  | 1.06x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240919-linux-x86_64-brandtbucher-decref_escapes-3.14.0a0-4711506 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.68 ms: 1.06x faster                                                 |
| regex_v8       | 25.3 ms                                                | 25.1 ms: 1.01x faster                                                 |
| regex_dna      | 220 ms                                                 | 224 ms: 1.02x slower                                                  |
| regex_compile  | 131 ms                                                 | 142 ms: 1.08x slower                                                  |
| Geometric mean | (ref)                                                  | 1.01x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240919-linux-x86_64-brandtbucher-decref_escapes-3.14.0a0-4711506 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_generate   | 87.0 ms                                                | 77.9 ms: 1.12x faster                                                 |
| xml_etree_process    | 60.4 ms                                                | 54.6 ms: 1.11x faster                                                 |
| tomli_loads          | 2.11 sec                                               | 1.95 sec: 1.08x faster                                                |
| xml_etree_parse      | 156 ms                                                 | 146 ms: 1.07x faster                                                  |
| xml_etree_iterparse  | 102 ms                                                 | 98.0 ms: 1.04x faster                                                 |
| json_dumps           | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                 |
| unpickle_pure_python | 213 us                                                 | 216 us: 1.01x slower                                                  |
| pickle_pure_python   | 300 us                                                 | 305 us: 1.02x slower                                                  |
| json_loads           | 27.0 us                                                | 27.5 us: 1.02x slower                                                 |
| unpickle_list        | 4.96 us                                                | 5.16 us: 1.04x slower                                                 |
| pickle_dict          | 33.2 us                                                | 35.2 us: 1.06x slower                                                 |
| pickle_list          | 5.01 us                                                | 5.37 us: 1.07x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                          |

Benchmark hidden because not significant (2): pickle, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240919-linux-x86_64-brandtbucher-decref_escapes-3.14.0a0-4711506 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.6 ms: 1.00x faster                                                 |
| python_startup_no_site | 6.99 ms                                                | 7.08 ms: 1.01x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240919-linux-x86_64-brandtbucher-decref_escapes-3.14.0a0-4711506 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.97 ms: 1.11x faster                                                 |
| django_template | 34.4 ms                                                | 35.4 ms: 1.03x slower                                                 |
| genshi_text     | 22.9 ms                                                | 24.5 ms: 1.07x slower                                                 |
| genshi_xml      | 50.3 ms                                                | 58.0 ms: 1.15x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.03x slower                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240919-linux-x86_64-brandtbucher-decref_escapes-3.14.0a0-4711506 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy_memo              | 38.0 us                                                | 26.9 us: 1.41x faster                                                 |
| deepcopy                   | 352 us                                                 | 263 us: 1.34x faster                                                  |
| richards                   | 48.1 ms                                                | 39.9 ms: 1.21x faster                                                 |
| richards_super             | 54.4 ms                                                | 45.6 ms: 1.19x faster                                                 |
| async_tree_memoization_tg  | 465 ms                                                 | 389 ms: 1.19x faster                                                  |
| deepcopy_reduce            | 3.17 us                                                | 2.66 us: 1.19x faster                                                 |
| scimark_fft                | 369 ms                                                 | 310 ms: 1.19x faster                                                  |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.29 ms: 1.17x faster                                                 |
| spectral_norm              | 115 ms                                                 | 102 ms: 1.13x faster                                                  |
| xml_etree_generate         | 87.0 ms                                                | 77.9 ms: 1.12x faster                                                 |
| mako                       | 11.1 ms                                                | 9.97 ms: 1.11x faster                                                 |
| async_tree_none            | 354 ms                                                 | 319 ms: 1.11x faster                                                  |
| float                      | 78.5 ms                                                | 70.7 ms: 1.11x faster                                                 |
| xml_etree_process          | 60.4 ms                                                | 54.6 ms: 1.11x faster                                                 |
| async_tree_memoization     | 442 ms                                                 | 403 ms: 1.10x faster                                                  |
| crypto_pyaes               | 73.0 ms                                                | 67.2 ms: 1.09x faster                                                 |
| tomli_loads                | 2.11 sec                                               | 1.95 sec: 1.08x faster                                                |
| go                         | 142 ms                                                 | 132 ms: 1.08x faster                                                  |
| pathlib                    | 17.1 ms                                                | 15.9 ms: 1.07x faster                                                 |
| xml_etree_parse            | 156 ms                                                 | 146 ms: 1.07x faster                                                  |
| nbody                      | 85.7 ms                                                | 80.2 ms: 1.07x faster                                                 |
| telco                      | 8.45 ms                                                | 7.94 ms: 1.06x faster                                                 |
| scimark_monte_carlo        | 66.3 ms                                                | 62.7 ms: 1.06x faster                                                 |
| regex_effbot               | 3.88 ms                                                | 3.68 ms: 1.06x faster                                                 |
| bpe_tokeniser              | 4.69 sec                                               | 4.47 sec: 1.05x faster                                                |
| scimark_sor                | 122 ms                                                 | 117 ms: 1.05x faster                                                  |
| scimark_lu                 | 115 ms                                                 | 110 ms: 1.05x faster                                                  |
| xml_etree_iterparse        | 102 ms                                                 | 98.0 ms: 1.04x faster                                                 |
| sqlite_synth               | 2.85 us                                                | 2.76 us: 1.03x faster                                                 |
| logging_format             | 6.25 us                                                | 6.13 us: 1.02x faster                                                 |
| pyflate                    | 460 ms                                                 | 451 ms: 1.02x faster                                                  |
| mdp                        | 2.74 sec                                               | 2.70 sec: 1.02x faster                                                |
| fannkuch                   | 381 ms                                                 | 375 ms: 1.01x faster                                                  |
| json_dumps                 | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                 |
| html5lib                   | 64.5 ms                                                | 63.8 ms: 1.01x faster                                                 |
| regex_v8                   | 25.3 ms                                                | 25.1 ms: 1.01x faster                                                 |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                                  |
| python_startup             | 10.6 ms                                                | 10.6 ms: 1.00x faster                                                 |
| gc_traversal               | 3.81 ms                                                | 3.83 ms: 1.01x slower                                                 |
| coverage                   | 83.7 ms                                                | 84.5 ms: 1.01x slower                                                 |
| pycparser                  | 1.19 sec                                               | 1.21 sec: 1.01x slower                                                |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.01x slower                                                |
| unpickle_pure_python       | 213 us                                                 | 216 us: 1.01x slower                                                  |
| python_startup_no_site     | 6.99 ms                                                | 7.08 ms: 1.01x slower                                                 |
| logging_silent             | 102 ns                                                 | 103 ns: 1.01x slower                                                  |
| pickle_pure_python         | 300 us                                                 | 305 us: 1.02x slower                                                  |
| deltablue                  | 3.15 ms                                                | 3.21 ms: 1.02x slower                                                 |
| regex_dna                  | 220 ms                                                 | 224 ms: 1.02x slower                                                  |
| asyncio_tcp                | 488 ms                                                 | 498 ms: 1.02x slower                                                  |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 555 ms: 1.02x slower                                                  |
| json_loads                 | 27.0 us                                                | 27.5 us: 1.02x slower                                                 |
| comprehensions             | 16.4 us                                                | 16.8 us: 1.02x slower                                                 |
| coroutines                 | 22.5 ms                                                | 23.0 ms: 1.02x slower                                                 |
| pprint_safe_repr           | 744 ms                                                 | 761 ms: 1.02x slower                                                  |
| django_template            | 34.4 ms                                                | 35.4 ms: 1.03x slower                                                 |
| bench_thread_pool          | 815 us                                                 | 838 us: 1.03x slower                                                  |
| pprint_pformat             | 1.51 sec                                               | 1.56 sec: 1.03x slower                                                |
| tornado_http               | 91.5 ms                                                | 95.1 ms: 1.04x slower                                                 |
| chaos                      | 58.4 ms                                                | 60.8 ms: 1.04x slower                                                 |
| unpickle_list              | 4.96 us                                                | 5.16 us: 1.04x slower                                                 |
| async_generators           | 433 ms                                                 | 451 ms: 1.04x slower                                                  |
| 2to3                       | 265 ms                                                 | 277 ms: 1.04x slower                                                  |
| sqlglot_normalize          | 107 ms                                                 | 113 ms: 1.05x slower                                                  |
| sqlglot_parse              | 1.27 ms                                                | 1.34 ms: 1.06x slower                                                 |
| async_tree_io_tg           | 825 ms                                                 | 876 ms: 1.06x slower                                                  |
| pickle_dict                | 33.2 us                                                | 35.2 us: 1.06x slower                                                 |
| raytrace                   | 262 ms                                                 | 280 ms: 1.07x slower                                                  |
| genshi_text                | 22.9 ms                                                | 24.5 ms: 1.07x slower                                                 |
| sqlglot_transpile          | 1.57 ms                                                | 1.69 ms: 1.07x slower                                                 |
| pickle_list                | 5.01 us                                                | 5.37 us: 1.07x slower                                                 |
| sqlglot_optimize           | 53.9 ms                                                | 57.9 ms: 1.07x slower                                                 |
| regex_compile              | 131 ms                                                 | 142 ms: 1.08x slower                                                  |
| dulwich_log                | 63.0 ms                                                | 68.3 ms: 1.08x slower                                                 |
| nqueens                    | 80.6 ms                                                | 87.9 ms: 1.09x slower                                                 |
| create_gc_cycles           | 1.61 ms                                                | 1.75 ms: 1.09x slower                                                 |
| sympy_expand               | 462 ms                                                 | 504 ms: 1.09x slower                                                  |
| sympy_str                  | 274 ms                                                 | 299 ms: 1.09x slower                                                  |
| hexiom                     | 6.13 ms                                                | 6.98 ms: 1.14x slower                                                 |
| sympy_integrate            | 19.9 ms                                                | 22.8 ms: 1.15x slower                                                 |
| generators                 | 28.8 ms                                                | 33.1 ms: 1.15x slower                                                 |
| sympy_sum                  | 150 ms                                                 | 172 ms: 1.15x slower                                                  |
| genshi_xml                 | 50.3 ms                                                | 58.0 ms: 1.15x slower                                                 |
| docutils                   | 2.58 sec                                               | 2.97 sec: 1.15x slower                                                |
| pylint                     | 313 ms                                                 | 374 ms: 1.19x slower                                                  |
| unpack_sequence            | 42.4 ns                                                | 106 ns: 2.50x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.00x slower                                                          |

Benchmark hidden because not significant (12): async_tree_none_tg, json, async_tree_cpu_io_mixed, thrift, logging_simple, meteor_contest, pickle, bench_mp_pool, asyncio_websockets, typing_runtime_protocols, async_tree_io, unpickle
Ignored benchmarks (7) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 51.25% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.09x