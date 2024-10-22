# Results vs. 3.13.0

- fork: brandtbucher
- ref: tier_two_constants_p
- machine: linux-x86_64
- commit hash: e2ba0e8
- commit date: 2024-09-13
- overall geometric mean: 1.00x slower
- HPT reliability: 51.25%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240913-linux-x86_64-brandtbucher-tier_two_constants_p-3.14.0a0-e2ba0e8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 280 ms: 1.06x slower                                                        |
| docutils       | 2.58 sec                                               | 2.97 sec: 1.15x slower                                                      |
| html5lib       | 64.5 ms                                                | 65.6 ms: 1.02x slower                                                       |
| tornado_http   | 91.5 ms                                                | 95.1 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                  | 1.06x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240913-linux-x86_64-brandtbucher-tier_two_constants_p-3.14.0a0-e2ba0e8 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 465 ms                                                 | 387 ms: 1.20x faster                                                        |
| async_tree_memoization     | 442 ms                                                 | 400 ms: 1.11x faster                                                        |
| async_tree_none            | 354 ms                                                 | 320 ms: 1.11x faster                                                        |
| async_tree_none_tg         | 320 ms                                                 | 307 ms: 1.04x faster                                                        |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.01x slower                                                      |
| coroutines                 | 22.5 ms                                                | 23.0 ms: 1.02x slower                                                       |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 554 ms: 1.02x slower                                                        |
| asyncio_tcp                | 488 ms                                                 | 502 ms: 1.03x slower                                                        |
| async_tree_io              | 843 ms                                                 | 888 ms: 1.05x slower                                                        |
| async_tree_io_tg           | 825 ms                                                 | 872 ms: 1.06x slower                                                        |
| async_generators           | 433 ms                                                 | 460 ms: 1.06x slower                                                        |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                                |

Benchmark hidden because not significant (2): asyncio_websockets, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240913-linux-x86_64-brandtbucher-tier_two_constants_p-3.14.0a0-e2ba0e8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 69.6 ms: 1.13x faster                                                       |
| nbody          | 85.7 ms                                                | 81.7 ms: 1.05x faster                                                       |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x slower                                                        |
| Geometric mean | (ref)                                                  | 1.06x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240913-linux-x86_64-brandtbucher-tier_two_constants_p-3.14.0a0-e2ba0e8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.59 ms: 1.08x faster                                                       |
| regex_dna      | 220 ms                                                 | 221 ms: 1.00x slower                                                        |
| regex_v8       | 25.3 ms                                                | 25.4 ms: 1.01x slower                                                       |
| regex_compile  | 131 ms                                                 | 142 ms: 1.08x slower                                                        |
| Geometric mean | (ref)                                                  | 1.00x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240913-linux-x86_64-brandtbucher-tier_two_constants_p-3.14.0a0-e2ba0e8 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_generate   | 87.0 ms                                                | 76.9 ms: 1.13x faster                                                       |
| xml_etree_process    | 60.4 ms                                                | 54.1 ms: 1.12x faster                                                       |
| tomli_loads          | 2.11 sec                                               | 1.98 sec: 1.07x faster                                                      |
| xml_etree_parse      | 156 ms                                                 | 147 ms: 1.06x faster                                                        |
| json_dumps           | 10.4 ms                                                | 10.1 ms: 1.04x faster                                                       |
| xml_etree_iterparse  | 102 ms                                                 | 98.6 ms: 1.03x faster                                                       |
| json_loads           | 27.0 us                                                | 26.7 us: 1.01x faster                                                       |
| unpickle_pure_python | 213 us                                                 | 215 us: 1.01x slower                                                        |
| pickle_pure_python   | 300 us                                                 | 303 us: 1.01x slower                                                        |
| pickle               | 11.6 us                                                | 11.8 us: 1.02x slower                                                       |
| pickle_list          | 5.01 us                                                | 5.11 us: 1.02x slower                                                       |
| pickle_dict          | 33.2 us                                                | 34.6 us: 1.04x slower                                                       |
| unpickle_list        | 4.96 us                                                | 5.34 us: 1.08x slower                                                       |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                                |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240913-linux-x86_64-brandtbucher-tier_two_constants_p-3.14.0a0-e2ba0e8 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.5 ms: 1.01x faster                                                       |
| python_startup_no_site | 6.99 ms                                                | 7.05 ms: 1.01x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.00x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240913-linux-x86_64-brandtbucher-tier_two_constants_p-3.14.0a0-e2ba0e8 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.73 ms: 1.14x faster                                                       |
| django_template | 34.4 ms                                                | 35.8 ms: 1.04x slower                                                       |
| genshi_text     | 22.9 ms                                                | 25.8 ms: 1.13x slower                                                       |
| genshi_xml      | 50.3 ms                                                | 59.0 ms: 1.17x slower                                                       |
| Geometric mean  | (ref)                                                  | 1.05x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240913-linux-x86_64-brandtbucher-tier_two_constants_p-3.14.0a0-e2ba0e8 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy_memo              | 38.0 us                                                | 27.1 us: 1.40x faster                                                       |
| deepcopy                   | 352 us                                                 | 277 us: 1.27x faster                                                        |
| richards                   | 48.1 ms                                                | 39.6 ms: 1.21x faster                                                       |
| richards_super             | 54.4 ms                                                | 45.1 ms: 1.21x faster                                                       |
| async_tree_memoization_tg  | 465 ms                                                 | 387 ms: 1.20x faster                                                        |
| scimark_fft                | 369 ms                                                 | 316 ms: 1.17x faster                                                        |
| deepcopy_reduce            | 3.17 us                                                | 2.71 us: 1.17x faster                                                       |
| spectral_norm              | 115 ms                                                 | 99.6 ms: 1.15x faster                                                       |
| mako                       | 11.1 ms                                                | 9.73 ms: 1.14x faster                                                       |
| xml_etree_generate         | 87.0 ms                                                | 76.9 ms: 1.13x faster                                                       |
| float                      | 78.5 ms                                                | 69.6 ms: 1.13x faster                                                       |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.47 ms: 1.12x faster                                                       |
| xml_etree_process          | 60.4 ms                                                | 54.1 ms: 1.12x faster                                                       |
| async_tree_memoization     | 442 ms                                                 | 400 ms: 1.11x faster                                                        |
| async_tree_none            | 354 ms                                                 | 320 ms: 1.11x faster                                                        |
| crypto_pyaes               | 73.0 ms                                                | 67.3 ms: 1.08x faster                                                       |
| mdp                        | 2.74 sec                                               | 2.53 sec: 1.08x faster                                                      |
| regex_effbot               | 3.88 ms                                                | 3.59 ms: 1.08x faster                                                       |
| go                         | 142 ms                                                 | 131 ms: 1.08x faster                                                        |
| tomli_loads                | 2.11 sec                                               | 1.98 sec: 1.07x faster                                                      |
| bpe_tokeniser              | 4.69 sec                                               | 4.40 sec: 1.07x faster                                                      |
| pathlib                    | 17.1 ms                                                | 16.0 ms: 1.06x faster                                                       |
| xml_etree_parse            | 156 ms                                                 | 147 ms: 1.06x faster                                                        |
| nbody                      | 85.7 ms                                                | 81.7 ms: 1.05x faster                                                       |
| telco                      | 8.45 ms                                                | 8.07 ms: 1.05x faster                                                       |
| scimark_monte_carlo        | 66.3 ms                                                | 63.3 ms: 1.05x faster                                                       |
| async_tree_none_tg         | 320 ms                                                 | 307 ms: 1.04x faster                                                        |
| scimark_sor                | 122 ms                                                 | 118 ms: 1.04x faster                                                        |
| sqlite_synth               | 2.85 us                                                | 2.74 us: 1.04x faster                                                       |
| json                       | 5.20 ms                                                | 5.02 ms: 1.04x faster                                                       |
| json_dumps                 | 10.4 ms                                                | 10.1 ms: 1.04x faster                                                       |
| xml_etree_iterparse        | 102 ms                                                 | 98.6 ms: 1.03x faster                                                       |
| scimark_lu                 | 115 ms                                                 | 111 ms: 1.03x faster                                                        |
| pprint_safe_repr           | 744 ms                                                 | 722 ms: 1.03x faster                                                        |
| pyflate                    | 460 ms                                                 | 447 ms: 1.03x faster                                                        |
| gc_traversal               | 3.81 ms                                                | 3.72 ms: 1.02x faster                                                       |
| fannkuch                   | 381 ms                                                 | 374 ms: 1.02x faster                                                        |
| json_loads                 | 27.0 us                                                | 26.7 us: 1.01x faster                                                       |
| logging_format             | 6.25 us                                                | 6.21 us: 1.01x faster                                                       |
| python_startup             | 10.6 ms                                                | 10.5 ms: 1.01x faster                                                       |
| meteor_contest             | 108 ms                                                 | 107 ms: 1.00x faster                                                        |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x slower                                                        |
| regex_dna                  | 220 ms                                                 | 221 ms: 1.00x slower                                                        |
| regex_v8                   | 25.3 ms                                                | 25.4 ms: 1.01x slower                                                       |
| unpickle_pure_python       | 213 us                                                 | 215 us: 1.01x slower                                                        |
| pickle_pure_python         | 300 us                                                 | 303 us: 1.01x slower                                                        |
| python_startup_no_site     | 6.99 ms                                                | 7.05 ms: 1.01x slower                                                       |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.01x slower                                                      |
| pycparser                  | 1.19 sec                                               | 1.21 sec: 1.01x slower                                                      |
| pprint_pformat             | 1.51 sec                                               | 1.53 sec: 1.01x slower                                                      |
| chaos                      | 58.4 ms                                                | 59.2 ms: 1.01x slower                                                       |
| deltablue                  | 3.15 ms                                                | 3.19 ms: 1.01x slower                                                       |
| html5lib                   | 64.5 ms                                                | 65.6 ms: 1.02x slower                                                       |
| pickle                     | 11.6 us                                                | 11.8 us: 1.02x slower                                                       |
| coverage                   | 83.7 ms                                                | 85.3 ms: 1.02x slower                                                       |
| logging_silent             | 102 ns                                                 | 104 ns: 1.02x slower                                                        |
| coroutines                 | 22.5 ms                                                | 23.0 ms: 1.02x slower                                                       |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 554 ms: 1.02x slower                                                        |
| pickle_list                | 5.01 us                                                | 5.11 us: 1.02x slower                                                       |
| typing_runtime_protocols   | 159 us                                                 | 164 us: 1.03x slower                                                        |
| asyncio_tcp                | 488 ms                                                 | 502 ms: 1.03x slower                                                        |
| bench_thread_pool          | 815 us                                                 | 839 us: 1.03x slower                                                        |
| django_template            | 34.4 ms                                                | 35.8 ms: 1.04x slower                                                       |
| tornado_http               | 91.5 ms                                                | 95.1 ms: 1.04x slower                                                       |
| pickle_dict                | 33.2 us                                                | 34.6 us: 1.04x slower                                                       |
| comprehensions             | 16.4 us                                                | 17.2 us: 1.05x slower                                                       |
| sqlglot_normalize          | 107 ms                                                 | 113 ms: 1.05x slower                                                        |
| async_tree_io              | 843 ms                                                 | 888 ms: 1.05x slower                                                        |
| 2to3                       | 265 ms                                                 | 280 ms: 1.06x slower                                                        |
| async_tree_io_tg           | 825 ms                                                 | 872 ms: 1.06x slower                                                        |
| async_generators           | 433 ms                                                 | 460 ms: 1.06x slower                                                        |
| raytrace                   | 262 ms                                                 | 280 ms: 1.07x slower                                                        |
| nqueens                    | 80.6 ms                                                | 86.5 ms: 1.07x slower                                                       |
| sqlglot_parse              | 1.27 ms                                                | 1.36 ms: 1.07x slower                                                       |
| unpickle_list              | 4.96 us                                                | 5.34 us: 1.08x slower                                                       |
| regex_compile              | 131 ms                                                 | 142 ms: 1.08x slower                                                        |
| dulwich_log                | 63.0 ms                                                | 68.3 ms: 1.08x slower                                                       |
| sqlglot_transpile          | 1.57 ms                                                | 1.71 ms: 1.08x slower                                                       |
| sqlglot_optimize           | 53.9 ms                                                | 58.7 ms: 1.09x slower                                                       |
| create_gc_cycles           | 1.61 ms                                                | 1.75 ms: 1.09x slower                                                       |
| sympy_expand               | 462 ms                                                 | 508 ms: 1.10x slower                                                        |
| sympy_str                  | 274 ms                                                 | 302 ms: 1.10x slower                                                        |
| genshi_text                | 22.9 ms                                                | 25.8 ms: 1.13x slower                                                       |
| generators                 | 28.8 ms                                                | 32.8 ms: 1.14x slower                                                       |
| docutils                   | 2.58 sec                                               | 2.97 sec: 1.15x slower                                                      |
| hexiom                     | 6.13 ms                                                | 7.05 ms: 1.15x slower                                                       |
| sympy_integrate            | 19.9 ms                                                | 23.1 ms: 1.16x slower                                                       |
| genshi_xml                 | 50.3 ms                                                | 59.0 ms: 1.17x slower                                                       |
| sympy_sum                  | 150 ms                                                 | 176 ms: 1.17x slower                                                        |
| pylint                     | 313 ms                                                 | 376 ms: 1.20x slower                                                        |
| unpack_sequence            | 42.4 ns                                                | 108 ns: 2.55x slower                                                        |
| Geometric mean             | (ref)                                                  | 1.00x slower                                                                |

Benchmark hidden because not significant (6): unpickle, asyncio_websockets, bench_mp_pool, thrift, logging_simple, async_tree_cpu_io_mixed
Ignored benchmarks (7) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 51.25% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.10x