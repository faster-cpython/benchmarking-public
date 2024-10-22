# Results vs. 3.13.0

- fork: brandtbucher
- ref: main
- machine: linux-x86_64
- commit hash: e256a75
- commit date: 2024-09-24
- overall geometric mean: 1.00x faster
- HPT reliability: 70.22%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-linux-x86_64-brandtbucher-main-3.14.0a0-e256a75 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 275 ms: 1.04x slower                                        |
| docutils       | 2.58 sec                                               | 2.95 sec: 1.14x slower                                      |
| tornado_http   | 91.5 ms                                                | 94.5 ms: 1.03x slower                                       |
| Geometric mean | (ref)                                                  | 1.05x slower                                                |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-linux-x86_64-brandtbucher-main-3.14.0a0-e256a75 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------:|
| async_tree_memoization_tg  | 465 ms                                                 | 388 ms: 1.20x faster                                        |
| async_tree_none            | 354 ms                                                 | 317 ms: 1.12x faster                                        |
| async_tree_memoization     | 442 ms                                                 | 401 ms: 1.10x faster                                        |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.80 sec: 1.01x slower                                      |
| asyncio_tcp                | 488 ms                                                 | 493 ms: 1.01x slower                                        |
| coroutines                 | 22.5 ms                                                | 22.9 ms: 1.02x slower                                       |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 555 ms: 1.02x slower                                        |
| async_generators           | 433 ms                                                 | 450 ms: 1.04x slower                                        |
| async_tree_io              | 843 ms                                                 | 885 ms: 1.05x slower                                        |
| async_tree_io_tg           | 825 ms                                                 | 873 ms: 1.06x slower                                        |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                |

Benchmark hidden because not significant (3): async_tree_none_tg, async_tree_cpu_io_mixed, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-linux-x86_64-brandtbucher-main-3.14.0a0-e256a75 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------:|
| float          | 78.5 ms                                                | 69.2 ms: 1.13x faster                                       |
| nbody          | 85.7 ms                                                | 79.3 ms: 1.08x faster                                       |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                        |
| Geometric mean | (ref)                                                  | 1.07x faster                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-linux-x86_64-brandtbucher-main-3.14.0a0-e256a75 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------:|
| regex_v8       | 25.3 ms                                                | 24.5 ms: 1.03x faster                                       |
| regex_effbot   | 3.88 ms                                                | 3.83 ms: 1.01x faster                                       |
| regex_dna      | 220 ms                                                 | 225 ms: 1.02x slower                                        |
| regex_compile  | 131 ms                                                 | 142 ms: 1.08x slower                                        |
| Geometric mean | (ref)                                                  | 1.01x slower                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-linux-x86_64-brandtbucher-main-3.14.0a0-e256a75 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------:|
| xml_etree_generate   | 87.0 ms                                                | 77.2 ms: 1.13x faster                                       |
| xml_etree_process    | 60.4 ms                                                | 54.7 ms: 1.10x faster                                       |
| tomli_loads          | 2.11 sec                                               | 1.94 sec: 1.09x faster                                      |
| xml_etree_parse      | 156 ms                                                 | 145 ms: 1.08x faster                                        |
| xml_etree_iterparse  | 102 ms                                                 | 98.5 ms: 1.04x faster                                       |
| unpickle             | 14.9 us                                                | 14.5 us: 1.02x faster                                       |
| json_dumps           | 10.4 ms                                                | 10.2 ms: 1.02x faster                                       |
| unpickle_pure_python | 213 us                                                 | 215 us: 1.01x slower                                        |
| pickle               | 11.6 us                                                | 11.7 us: 1.01x slower                                       |
| pickle_pure_python   | 300 us                                                 | 308 us: 1.03x slower                                        |
| pickle_list          | 5.01 us                                                | 5.16 us: 1.03x slower                                       |
| pickle_dict          | 33.2 us                                                | 34.3 us: 1.03x slower                                       |
| unpickle_list        | 4.96 us                                                | 5.18 us: 1.04x slower                                       |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-linux-x86_64-brandtbucher-main-3.14.0a0-e256a75 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.5 ms: 1.00x faster                                       |
| python_startup_no_site | 6.99 ms                                                | 7.06 ms: 1.01x slower                                       |
| Geometric mean         | (ref)                                                  | 1.00x slower                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-linux-x86_64-brandtbucher-main-3.14.0a0-e256a75 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.80 ms: 1.13x faster                                       |
| django_template | 34.4 ms                                                | 36.0 ms: 1.05x slower                                       |
| genshi_text     | 22.9 ms                                                | 24.9 ms: 1.09x slower                                       |
| genshi_xml      | 50.3 ms                                                | 57.3 ms: 1.14x slower                                       |
| Geometric mean  | (ref)                                                  | 1.03x slower                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-linux-x86_64-brandtbucher-main-3.14.0a0-e256a75 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------:|
| deepcopy_memo              | 38.0 us                                                | 26.7 us: 1.42x faster                                       |
| deepcopy                   | 352 us                                                 | 260 us: 1.36x faster                                        |
| richards                   | 48.1 ms                                                | 39.4 ms: 1.22x faster                                       |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.16 ms: 1.21x faster                                       |
| richards_super             | 54.4 ms                                                | 45.2 ms: 1.20x faster                                       |
| deepcopy_reduce            | 3.17 us                                                | 2.64 us: 1.20x faster                                       |
| async_tree_memoization_tg  | 465 ms                                                 | 388 ms: 1.20x faster                                        |
| scimark_fft                | 369 ms                                                 | 309 ms: 1.19x faster                                        |
| spectral_norm              | 115 ms                                                 | 100.0 ms: 1.15x faster                                      |
| float                      | 78.5 ms                                                | 69.2 ms: 1.13x faster                                       |
| mako                       | 11.1 ms                                                | 9.80 ms: 1.13x faster                                       |
| xml_etree_generate         | 87.0 ms                                                | 77.2 ms: 1.13x faster                                       |
| async_tree_none            | 354 ms                                                 | 317 ms: 1.12x faster                                        |
| xml_etree_process          | 60.4 ms                                                | 54.7 ms: 1.10x faster                                       |
| async_tree_memoization     | 442 ms                                                 | 401 ms: 1.10x faster                                        |
| crypto_pyaes               | 73.0 ms                                                | 66.4 ms: 1.10x faster                                       |
| tomli_loads                | 2.11 sec                                               | 1.94 sec: 1.09x faster                                      |
| nbody                      | 85.7 ms                                                | 79.3 ms: 1.08x faster                                       |
| pathlib                    | 17.1 ms                                                | 15.8 ms: 1.08x faster                                       |
| xml_etree_parse            | 156 ms                                                 | 145 ms: 1.08x faster                                        |
| go                         | 142 ms                                                 | 131 ms: 1.08x faster                                        |
| mdp                        | 2.74 sec                                               | 2.55 sec: 1.07x faster                                      |
| scimark_monte_carlo        | 66.3 ms                                                | 61.9 ms: 1.07x faster                                       |
| telco                      | 8.45 ms                                                | 7.93 ms: 1.07x faster                                       |
| bpe_tokeniser              | 4.69 sec                                               | 4.42 sec: 1.06x faster                                      |
| scimark_sor                | 122 ms                                                 | 117 ms: 1.05x faster                                        |
| sqlite_synth               | 2.85 us                                                | 2.75 us: 1.04x faster                                       |
| pycparser                  | 1.19 sec                                               | 1.15 sec: 1.04x faster                                      |
| xml_etree_iterparse        | 102 ms                                                 | 98.5 ms: 1.04x faster                                       |
| json                       | 5.20 ms                                                | 5.03 ms: 1.03x faster                                       |
| scimark_lu                 | 115 ms                                                 | 111 ms: 1.03x faster                                        |
| regex_v8                   | 25.3 ms                                                | 24.5 ms: 1.03x faster                                       |
| gc_traversal               | 3.81 ms                                                | 3.70 ms: 1.03x faster                                       |
| unpickle                   | 14.9 us                                                | 14.5 us: 1.02x faster                                       |
| json_dumps                 | 10.4 ms                                                | 10.2 ms: 1.02x faster                                       |
| pyflate                    | 460 ms                                                 | 450 ms: 1.02x faster                                        |
| fannkuch                   | 381 ms                                                 | 373 ms: 1.02x faster                                        |
| thrift                     | 796 us                                                 | 782 us: 1.02x faster                                        |
| regex_effbot               | 3.88 ms                                                | 3.83 ms: 1.01x faster                                       |
| meteor_contest             | 108 ms                                                 | 107 ms: 1.01x faster                                        |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                        |
| python_startup             | 10.6 ms                                                | 10.5 ms: 1.00x faster                                       |
| comprehensions             | 16.4 us                                                | 16.5 us: 1.00x slower                                       |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.80 sec: 1.01x slower                                      |
| unpickle_pure_python       | 213 us                                                 | 215 us: 1.01x slower                                        |
| chaos                      | 58.4 ms                                                | 59.0 ms: 1.01x slower                                       |
| asyncio_tcp                | 488 ms                                                 | 493 ms: 1.01x slower                                        |
| logging_silent             | 102 ns                                                 | 103 ns: 1.01x slower                                        |
| python_startup_no_site     | 6.99 ms                                                | 7.06 ms: 1.01x slower                                       |
| pickle                     | 11.6 us                                                | 11.7 us: 1.01x slower                                       |
| typing_runtime_protocols   | 159 us                                                 | 161 us: 1.01x slower                                        |
| pprint_pformat             | 1.51 sec                                               | 1.54 sec: 1.02x slower                                      |
| coroutines                 | 22.5 ms                                                | 22.9 ms: 1.02x slower                                       |
| deltablue                  | 3.15 ms                                                | 3.21 ms: 1.02x slower                                       |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 555 ms: 1.02x slower                                        |
| coverage                   | 83.7 ms                                                | 85.6 ms: 1.02x slower                                       |
| regex_dna                  | 220 ms                                                 | 225 ms: 1.02x slower                                        |
| bench_thread_pool          | 815 us                                                 | 835 us: 1.02x slower                                        |
| pickle_pure_python         | 300 us                                                 | 308 us: 1.03x slower                                        |
| pickle_list                | 5.01 us                                                | 5.16 us: 1.03x slower                                       |
| tornado_http               | 91.5 ms                                                | 94.5 ms: 1.03x slower                                       |
| pickle_dict                | 33.2 us                                                | 34.3 us: 1.03x slower                                       |
| 2to3                       | 265 ms                                                 | 275 ms: 1.04x slower                                        |
| async_generators           | 433 ms                                                 | 450 ms: 1.04x slower                                        |
| unpickle_list              | 4.96 us                                                | 5.18 us: 1.04x slower                                       |
| django_template            | 34.4 ms                                                | 36.0 ms: 1.05x slower                                       |
| async_tree_io              | 843 ms                                                 | 885 ms: 1.05x slower                                        |
| raytrace                   | 262 ms                                                 | 275 ms: 1.05x slower                                        |
| sqlglot_normalize          | 107 ms                                                 | 113 ms: 1.05x slower                                        |
| sqlglot_parse              | 1.27 ms                                                | 1.34 ms: 1.06x slower                                       |
| async_tree_io_tg           | 825 ms                                                 | 873 ms: 1.06x slower                                        |
| sqlglot_transpile          | 1.57 ms                                                | 1.67 ms: 1.06x slower                                       |
| nqueens                    | 80.6 ms                                                | 86.4 ms: 1.07x slower                                       |
| dulwich_log                | 63.0 ms                                                | 67.7 ms: 1.07x slower                                       |
| sqlglot_optimize           | 53.9 ms                                                | 58.0 ms: 1.08x slower                                       |
| create_gc_cycles           | 1.61 ms                                                | 1.74 ms: 1.08x slower                                       |
| regex_compile              | 131 ms                                                 | 142 ms: 1.08x slower                                        |
| sympy_expand               | 462 ms                                                 | 502 ms: 1.09x slower                                        |
| genshi_text                | 22.9 ms                                                | 24.9 ms: 1.09x slower                                       |
| sympy_str                  | 274 ms                                                 | 298 ms: 1.09x slower                                        |
| hexiom                     | 6.13 ms                                                | 6.86 ms: 1.12x slower                                       |
| genshi_xml                 | 50.3 ms                                                | 57.3 ms: 1.14x slower                                       |
| generators                 | 28.8 ms                                                | 32.8 ms: 1.14x slower                                       |
| docutils                   | 2.58 sec                                               | 2.95 sec: 1.14x slower                                      |
| sympy_integrate            | 19.9 ms                                                | 22.8 ms: 1.14x slower                                       |
| sympy_sum                  | 150 ms                                                 | 172 ms: 1.15x slower                                        |
| pylint                     | 313 ms                                                 | 371 ms: 1.19x slower                                        |
| unpack_sequence            | 42.4 ns                                                | 107 ns: 2.53x slower                                        |
| Geometric mean             | (ref)                                                  | 1.00x faster                                                |

Benchmark hidden because not significant (9): async_tree_none_tg, logging_format, async_tree_cpu_io_mixed, asyncio_websockets, bench_mp_pool, json_loads, html5lib, logging_simple, pprint_safe_repr
Ignored benchmarks (7) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 70.22% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.09x