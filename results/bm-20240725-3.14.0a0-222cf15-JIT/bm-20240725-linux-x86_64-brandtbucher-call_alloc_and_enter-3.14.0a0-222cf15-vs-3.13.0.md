# Results vs. 3.13.0

- fork: brandtbucher
- ref: call_alloc_and_enter
- machine: linux-x86_64
- commit hash: 222cf15
- commit date: 2024-07-25
- overall geometric mean: 1.01x faster
- HPT reliability: 77.45%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240725-linux-x86_64-brandtbucher-call_alloc_and_enter-3.14.0a0-222cf15 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 270 ms: 1.02x slower                                                        |
| docutils       | 2.58 sec                                               | 2.91 sec: 1.12x slower                                                      |
| html5lib       | 64.5 ms                                                | 64.2 ms: 1.01x faster                                                       |
| tornado_http   | 91.5 ms                                                | 92.7 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                  | 1.04x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240725-linux-x86_64-brandtbucher-call_alloc_and_enter-3.14.0a0-222cf15 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 465 ms                                                 | 393 ms: 1.18x faster                                                        |
| async_tree_none            | 354 ms                                                 | 328 ms: 1.08x faster                                                        |
| async_tree_none_tg         | 320 ms                                                 | 301 ms: 1.06x faster                                                        |
| async_tree_memoization     | 442 ms                                                 | 416 ms: 1.06x faster                                                        |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 535 ms: 1.02x faster                                                        |
| asyncio_websockets         | 555 ms                                                 | 558 ms: 1.01x slower                                                        |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.01x slower                                                      |
| coroutines                 | 22.5 ms                                                | 22.8 ms: 1.01x slower                                                       |
| asyncio_tcp                | 488 ms                                                 | 503 ms: 1.03x slower                                                        |
| async_tree_io_tg           | 825 ms                                                 | 872 ms: 1.06x slower                                                        |
| async_generators           | 433 ms                                                 | 459 ms: 1.06x slower                                                        |
| async_tree_io              | 843 ms                                                 | 901 ms: 1.07x slower                                                        |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                                |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240725-linux-x86_64-brandtbucher-call_alloc_and_enter-3.14.0a0-222cf15 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 70.1 ms: 1.12x faster                                                       |
| nbody          | 85.7 ms                                                | 80.5 ms: 1.06x faster                                                       |
| pidigits       | 186 ms                                                 | 185 ms: 1.00x faster                                                        |
| Geometric mean | (ref)                                                  | 1.06x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240725-linux-x86_64-brandtbucher-call_alloc_and_enter-3.14.0a0-222cf15 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 25.3 ms                                                | 24.0 ms: 1.05x faster                                                       |
| regex_effbot   | 3.88 ms                                                | 3.70 ms: 1.05x faster                                                       |
| regex_compile  | 131 ms                                                 | 133 ms: 1.01x slower                                                        |
| regex_dna      | 220 ms                                                 | 226 ms: 1.03x slower                                                        |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240725-linux-x86_64-brandtbucher-call_alloc_and_enter-3.14.0a0-222cf15 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.11 sec                                               | 1.93 sec: 1.09x faster                                                      |
| xml_etree_generate   | 87.0 ms                                                | 80.1 ms: 1.09x faster                                                       |
| xml_etree_process    | 60.4 ms                                                | 56.3 ms: 1.07x faster                                                       |
| xml_etree_parse      | 156 ms                                                 | 146 ms: 1.06x faster                                                        |
| xml_etree_iterparse  | 102 ms                                                 | 99.1 ms: 1.03x faster                                                       |
| pickle_pure_python   | 300 us                                                 | 295 us: 1.02x faster                                                        |
| json_loads           | 27.0 us                                                | 27.9 us: 1.03x slower                                                       |
| unpickle_pure_python | 213 us                                                 | 221 us: 1.03x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                                |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240725-linux-x86_64-brandtbucher-call_alloc_and_enter-3.14.0a0-222cf15 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.6 ms: 1.00x slower                                                       |
| python_startup_no_site | 6.99 ms                                                | 7.16 ms: 1.02x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240725-linux-x86_64-brandtbucher-call_alloc_and_enter-3.14.0a0-222cf15 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.79 ms: 1.13x faster                                                       |
| django_template | 34.4 ms                                                | 35.8 ms: 1.04x slower                                                       |
| genshi_text     | 22.9 ms                                                | 25.1 ms: 1.10x slower                                                       |
| genshi_xml      | 50.3 ms                                                | 59.0 ms: 1.17x slower                                                       |
| Geometric mean  | (ref)                                                  | 1.04x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240725-linux-x86_64-brandtbucher-call_alloc_and_enter-3.14.0a0-222cf15 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy_memo              | 38.0 us                                                | 28.7 us: 1.32x faster                                                       |
| deepcopy                   | 352 us                                                 | 272 us: 1.30x faster                                                        |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.14 ms: 1.21x faster                                                       |
| scimark_fft                | 369 ms                                                 | 305 ms: 1.21x faster                                                        |
| richards                   | 48.1 ms                                                | 40.2 ms: 1.20x faster                                                       |
| async_tree_memoization_tg  | 465 ms                                                 | 393 ms: 1.18x faster                                                        |
| richards_super             | 54.4 ms                                                | 46.7 ms: 1.17x faster                                                       |
| deepcopy_reduce            | 3.17 us                                                | 2.75 us: 1.15x faster                                                       |
| mako                       | 11.1 ms                                                | 9.79 ms: 1.13x faster                                                       |
| float                      | 78.5 ms                                                | 70.1 ms: 1.12x faster                                                       |
| spectral_norm              | 115 ms                                                 | 103 ms: 1.12x faster                                                        |
| scimark_monte_carlo        | 66.3 ms                                                | 59.9 ms: 1.11x faster                                                       |
| crypto_pyaes               | 73.0 ms                                                | 66.7 ms: 1.09x faster                                                       |
| tomli_loads                | 2.11 sec                                               | 1.93 sec: 1.09x faster                                                      |
| xml_etree_generate         | 87.0 ms                                                | 80.1 ms: 1.09x faster                                                       |
| mdp                        | 2.74 sec                                               | 2.53 sec: 1.08x faster                                                      |
| async_tree_none            | 354 ms                                                 | 328 ms: 1.08x faster                                                        |
| xml_etree_process          | 60.4 ms                                                | 56.3 ms: 1.07x faster                                                       |
| pycparser                  | 1.19 sec                                               | 1.12 sec: 1.07x faster                                                      |
| xml_etree_parse            | 156 ms                                                 | 146 ms: 1.06x faster                                                        |
| nbody                      | 85.7 ms                                                | 80.5 ms: 1.06x faster                                                       |
| async_tree_none_tg         | 320 ms                                                 | 301 ms: 1.06x faster                                                        |
| telco                      | 8.45 ms                                                | 7.95 ms: 1.06x faster                                                       |
| async_tree_memoization     | 442 ms                                                 | 416 ms: 1.06x faster                                                        |
| bpe_tokeniser              | 4.69 sec                                               | 4.44 sec: 1.06x faster                                                      |
| regex_v8                   | 25.3 ms                                                | 24.0 ms: 1.05x faster                                                       |
| pathlib                    | 17.1 ms                                                | 16.2 ms: 1.05x faster                                                       |
| pyflate                    | 460 ms                                                 | 436 ms: 1.05x faster                                                        |
| regex_effbot               | 3.88 ms                                                | 3.70 ms: 1.05x faster                                                       |
| gc_traversal               | 3.81 ms                                                | 3.64 ms: 1.05x faster                                                       |
| fannkuch                   | 381 ms                                                 | 366 ms: 1.04x faster                                                        |
| pprint_pformat             | 1.51 sec                                               | 1.46 sec: 1.03x faster                                                      |
| pprint_safe_repr           | 744 ms                                                 | 721 ms: 1.03x faster                                                        |
| xml_etree_iterparse        | 102 ms                                                 | 99.1 ms: 1.03x faster                                                       |
| logging_simple             | 5.66 us                                                | 5.54 us: 1.02x faster                                                       |
| meteor_contest             | 108 ms                                                 | 105 ms: 1.02x faster                                                        |
| logging_format             | 6.25 us                                                | 6.14 us: 1.02x faster                                                       |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 535 ms: 1.02x faster                                                        |
| pickle_pure_python         | 300 us                                                 | 295 us: 1.02x faster                                                        |
| thrift                     | 796 us                                                 | 788 us: 1.01x faster                                                        |
| chaos                      | 58.4 ms                                                | 58.0 ms: 1.01x faster                                                       |
| html5lib                   | 64.5 ms                                                | 64.2 ms: 1.01x faster                                                       |
| pidigits                   | 186 ms                                                 | 185 ms: 1.00x faster                                                        |
| python_startup             | 10.6 ms                                                | 10.6 ms: 1.00x slower                                                       |
| asyncio_websockets         | 555 ms                                                 | 558 ms: 1.01x slower                                                        |
| sqlglot_parse              | 1.27 ms                                                | 1.27 ms: 1.01x slower                                                       |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.01x slower                                                      |
| comprehensions             | 16.4 us                                                | 16.6 us: 1.01x slower                                                       |
| go                         | 142 ms                                                 | 143 ms: 1.01x slower                                                        |
| tornado_http               | 91.5 ms                                                | 92.7 ms: 1.01x slower                                                       |
| sqlglot_transpile          | 1.57 ms                                                | 1.59 ms: 1.01x slower                                                       |
| coroutines                 | 22.5 ms                                                | 22.8 ms: 1.01x slower                                                       |
| regex_compile              | 131 ms                                                 | 133 ms: 1.01x slower                                                        |
| bench_thread_pool          | 815 us                                                 | 827 us: 1.02x slower                                                        |
| 2to3                       | 265 ms                                                 | 270 ms: 1.02x slower                                                        |
| raytrace                   | 262 ms                                                 | 268 ms: 1.02x slower                                                        |
| python_startup_no_site     | 6.99 ms                                                | 7.16 ms: 1.02x slower                                                       |
| regex_dna                  | 220 ms                                                 | 226 ms: 1.03x slower                                                        |
| typing_runtime_protocols   | 159 us                                                 | 164 us: 1.03x slower                                                        |
| asyncio_tcp                | 488 ms                                                 | 503 ms: 1.03x slower                                                        |
| json_loads                 | 27.0 us                                                | 27.9 us: 1.03x slower                                                       |
| unpickle_pure_python       | 213 us                                                 | 221 us: 1.03x slower                                                        |
| sqlglot_optimize           | 53.9 ms                                                | 55.8 ms: 1.03x slower                                                       |
| logging_silent             | 102 ns                                                 | 106 ns: 1.04x slower                                                        |
| bench_mp_pool              | 24.0 ms                                                | 25.0 ms: 1.04x slower                                                       |
| django_template            | 34.4 ms                                                | 35.8 ms: 1.04x slower                                                       |
| scimark_sor                | 122 ms                                                 | 128 ms: 1.04x slower                                                        |
| sqlglot_normalize          | 107 ms                                                 | 112 ms: 1.04x slower                                                        |
| async_tree_io_tg           | 825 ms                                                 | 872 ms: 1.06x slower                                                        |
| async_generators           | 433 ms                                                 | 459 ms: 1.06x slower                                                        |
| nqueens                    | 80.6 ms                                                | 85.7 ms: 1.06x slower                                                       |
| hexiom                     | 6.13 ms                                                | 6.52 ms: 1.06x slower                                                       |
| async_tree_io              | 843 ms                                                 | 901 ms: 1.07x slower                                                        |
| sympy_str                  | 274 ms                                                 | 295 ms: 1.08x slower                                                        |
| sympy_expand               | 462 ms                                                 | 498 ms: 1.08x slower                                                        |
| dask                       | 338 ms                                                 | 365 ms: 1.08x slower                                                        |
| create_gc_cycles           | 1.61 ms                                                | 1.75 ms: 1.09x slower                                                       |
| genshi_text                | 22.9 ms                                                | 25.1 ms: 1.10x slower                                                       |
| scimark_lu                 | 115 ms                                                 | 126 ms: 1.10x slower                                                        |
| coverage                   | 83.7 ms                                                | 92.2 ms: 1.10x slower                                                       |
| pylint                     | 313 ms                                                 | 350 ms: 1.12x slower                                                        |
| sympy_integrate            | 19.9 ms                                                | 22.4 ms: 1.12x slower                                                       |
| docutils                   | 2.58 sec                                               | 2.91 sec: 1.12x slower                                                      |
| sympy_sum                  | 150 ms                                                 | 169 ms: 1.13x slower                                                        |
| deltablue                  | 3.15 ms                                                | 3.57 ms: 1.13x slower                                                       |
| genshi_xml                 | 50.3 ms                                                | 59.0 ms: 1.17x slower                                                       |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                                |

Benchmark hidden because not significant (4): async_tree_cpu_io_mixed, json, json_dumps, generators
Ignored benchmarks (14) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 77.45% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.08x