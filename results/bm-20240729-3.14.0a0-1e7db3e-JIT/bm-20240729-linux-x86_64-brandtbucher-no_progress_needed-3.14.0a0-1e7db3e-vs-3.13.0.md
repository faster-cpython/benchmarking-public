# Results vs. 3.13.0

- fork: brandtbucher
- ref: no_progress_needed
- machine: linux-x86_64
- commit hash: 1e7db3e
- commit date: 2024-07-29
- overall geometric mean: 1.01x slower
- HPT reliability: 90.88%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240729-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-1e7db3e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 289 ms: 1.09x slower                                                      |
| docutils       | 2.58 sec                                               | 3.09 sec: 1.19x slower                                                    |
| html5lib       | 64.5 ms                                                | 67.5 ms: 1.05x slower                                                     |
| tornado_http   | 91.5 ms                                                | 94.7 ms: 1.03x slower                                                     |
| Geometric mean | (ref)                                                  | 1.09x slower                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240729-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-1e7db3e |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 465 ms                                                 | 394 ms: 1.18x faster                                                      |
| async_tree_none            | 354 ms                                                 | 329 ms: 1.08x faster                                                      |
| async_tree_none_tg         | 320 ms                                                 | 301 ms: 1.06x faster                                                      |
| async_tree_memoization     | 442 ms                                                 | 429 ms: 1.03x faster                                                      |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 532 ms: 1.02x faster                                                      |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 563 ms: 1.02x faster                                                      |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.01x slower                                                    |
| asyncio_tcp                | 488 ms                                                 | 507 ms: 1.04x slower                                                      |
| async_tree_io_tg           | 825 ms                                                 | 874 ms: 1.06x slower                                                      |
| async_tree_io              | 843 ms                                                 | 914 ms: 1.08x slower                                                      |
| async_generators           | 433 ms                                                 | 473 ms: 1.09x slower                                                      |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                              |

Benchmark hidden because not significant (2): coroutines, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240729-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-1e7db3e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 71.6 ms: 1.10x faster                                                     |
| nbody          | 85.7 ms                                                | 80.1 ms: 1.07x faster                                                     |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                      |
| Geometric mean | (ref)                                                  | 1.06x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240729-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-1e7db3e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.70 ms: 1.05x faster                                                     |
| regex_v8       | 25.3 ms                                                | 24.2 ms: 1.04x faster                                                     |
| regex_dna      | 220 ms                                                 | 225 ms: 1.02x slower                                                      |
| regex_compile  | 131 ms                                                 | 151 ms: 1.15x slower                                                      |
| Geometric mean | (ref)                                                  | 1.02x slower                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240729-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-1e7db3e |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 2.11 sec                                               | 1.98 sec: 1.07x faster                                                    |
| xml_etree_generate   | 87.0 ms                                                | 82.0 ms: 1.06x faster                                                     |
| xml_etree_parse      | 156 ms                                                 | 147 ms: 1.06x faster                                                      |
| xml_etree_process    | 60.4 ms                                                | 57.9 ms: 1.04x faster                                                     |
| json_dumps           | 10.4 ms                                                | 10.2 ms: 1.02x faster                                                     |
| xml_etree_iterparse  | 102 ms                                                 | 101 ms: 1.01x faster                                                      |
| pickle_pure_python   | 300 us                                                 | 304 us: 1.01x slower                                                      |
| unpickle_pure_python | 213 us                                                 | 216 us: 1.01x slower                                                      |
| json_loads           | 27.0 us                                                | 27.9 us: 1.03x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240729-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-1e7db3e |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.5 ms: 1.01x faster                                                     |
| python_startup_no_site | 6.99 ms                                                | 7.13 ms: 1.02x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240729-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-1e7db3e |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.63 ms: 1.15x faster                                                     |
| genshi_text     | 22.9 ms                                                | 24.6 ms: 1.08x slower                                                     |
| django_template | 34.4 ms                                                | 38.0 ms: 1.10x slower                                                     |
| genshi_xml      | 50.3 ms                                                | 56.2 ms: 1.12x slower                                                     |
| Geometric mean  | (ref)                                                  | 1.04x slower                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240729-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-1e7db3e |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| deepcopy_memo              | 38.0 us                                                | 27.9 us: 1.36x faster                                                     |
| deepcopy                   | 352 us                                                 | 271 us: 1.30x faster                                                      |
| deepcopy_reduce            | 3.17 us                                                | 2.66 us: 1.19x faster                                                     |
| async_tree_memoization_tg  | 465 ms                                                 | 394 ms: 1.18x faster                                                      |
| scimark_fft                | 369 ms                                                 | 313 ms: 1.18x faster                                                      |
| mako                       | 11.1 ms                                                | 9.63 ms: 1.15x faster                                                     |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.42 ms: 1.14x faster                                                     |
| spectral_norm              | 115 ms                                                 | 102 ms: 1.12x faster                                                      |
| float                      | 78.5 ms                                                | 71.6 ms: 1.10x faster                                                     |
| crypto_pyaes               | 73.0 ms                                                | 67.0 ms: 1.09x faster                                                     |
| richards                   | 48.1 ms                                                | 44.7 ms: 1.08x faster                                                     |
| async_tree_none            | 354 ms                                                 | 329 ms: 1.08x faster                                                      |
| nbody                      | 85.7 ms                                                | 80.1 ms: 1.07x faster                                                     |
| tomli_loads                | 2.11 sec                                               | 1.98 sec: 1.07x faster                                                    |
| async_tree_none_tg         | 320 ms                                                 | 301 ms: 1.06x faster                                                      |
| xml_etree_generate         | 87.0 ms                                                | 82.0 ms: 1.06x faster                                                     |
| richards_super             | 54.4 ms                                                | 51.3 ms: 1.06x faster                                                     |
| telco                      | 8.45 ms                                                | 7.98 ms: 1.06x faster                                                     |
| xml_etree_parse            | 156 ms                                                 | 147 ms: 1.06x faster                                                      |
| regex_effbot               | 3.88 ms                                                | 3.70 ms: 1.05x faster                                                     |
| mdp                        | 2.74 sec                                               | 2.62 sec: 1.05x faster                                                    |
| regex_v8                   | 25.3 ms                                                | 24.2 ms: 1.04x faster                                                     |
| xml_etree_process          | 60.4 ms                                                | 57.9 ms: 1.04x faster                                                     |
| scimark_monte_carlo        | 66.3 ms                                                | 63.7 ms: 1.04x faster                                                     |
| pathlib                    | 17.1 ms                                                | 16.4 ms: 1.04x faster                                                     |
| async_tree_memoization     | 442 ms                                                 | 429 ms: 1.03x faster                                                      |
| deltablue                  | 3.15 ms                                                | 3.08 ms: 1.02x faster                                                     |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 532 ms: 1.02x faster                                                      |
| pyflate                    | 460 ms                                                 | 450 ms: 1.02x faster                                                      |
| logging_format             | 6.25 us                                                | 6.12 us: 1.02x faster                                                     |
| bpe_tokeniser              | 4.69 sec                                               | 4.60 sec: 1.02x faster                                                    |
| json_dumps                 | 10.4 ms                                                | 10.2 ms: 1.02x faster                                                     |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 563 ms: 1.02x faster                                                      |
| logging_simple             | 5.66 us                                                | 5.57 us: 1.02x faster                                                     |
| fannkuch                   | 381 ms                                                 | 375 ms: 1.02x faster                                                      |
| logging_silent             | 102 ns                                                 | 101 ns: 1.01x faster                                                      |
| xml_etree_iterparse        | 102 ms                                                 | 101 ms: 1.01x faster                                                      |
| meteor_contest             | 108 ms                                                 | 107 ms: 1.01x faster                                                      |
| python_startup             | 10.6 ms                                                | 10.5 ms: 1.01x faster                                                     |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                                      |
| gc_traversal               | 3.81 ms                                                | 3.81 ms: 1.00x slower                                                     |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.01x slower                                                    |
| pickle_pure_python         | 300 us                                                 | 304 us: 1.01x slower                                                      |
| unpickle_pure_python       | 213 us                                                 | 216 us: 1.01x slower                                                      |
| pprint_safe_repr           | 744 ms                                                 | 757 ms: 1.02x slower                                                      |
| python_startup_no_site     | 6.99 ms                                                | 7.13 ms: 1.02x slower                                                     |
| regex_dna                  | 220 ms                                                 | 225 ms: 1.02x slower                                                      |
| chaos                      | 58.4 ms                                                | 60.0 ms: 1.03x slower                                                     |
| bench_thread_pool          | 815 us                                                 | 839 us: 1.03x slower                                                      |
| pprint_pformat             | 1.51 sec                                               | 1.56 sec: 1.03x slower                                                    |
| json_loads                 | 27.0 us                                                | 27.9 us: 1.03x slower                                                     |
| comprehensions             | 16.4 us                                                | 17.0 us: 1.03x slower                                                     |
| tornado_http               | 91.5 ms                                                | 94.7 ms: 1.03x slower                                                     |
| asyncio_tcp                | 488 ms                                                 | 507 ms: 1.04x slower                                                      |
| html5lib                   | 64.5 ms                                                | 67.5 ms: 1.05x slower                                                     |
| async_tree_io_tg           | 825 ms                                                 | 874 ms: 1.06x slower                                                      |
| sqlglot_parse              | 1.27 ms                                                | 1.34 ms: 1.06x slower                                                     |
| go                         | 142 ms                                                 | 152 ms: 1.07x slower                                                      |
| raytrace                   | 262 ms                                                 | 281 ms: 1.07x slower                                                      |
| genshi_text                | 22.9 ms                                                | 24.6 ms: 1.08x slower                                                     |
| async_tree_io              | 843 ms                                                 | 914 ms: 1.08x slower                                                      |
| sqlglot_transpile          | 1.57 ms                                                | 1.71 ms: 1.09x slower                                                     |
| dask                       | 338 ms                                                 | 368 ms: 1.09x slower                                                      |
| 2to3                       | 265 ms                                                 | 289 ms: 1.09x slower                                                      |
| scimark_sor                | 122 ms                                                 | 134 ms: 1.09x slower                                                      |
| async_generators           | 433 ms                                                 | 473 ms: 1.09x slower                                                      |
| coverage                   | 83.7 ms                                                | 91.6 ms: 1.09x slower                                                     |
| create_gc_cycles           | 1.61 ms                                                | 1.76 ms: 1.10x slower                                                     |
| sqlglot_normalize          | 107 ms                                                 | 119 ms: 1.10x slower                                                      |
| django_template            | 34.4 ms                                                | 38.0 ms: 1.10x slower                                                     |
| typing_runtime_protocols   | 159 us                                                 | 176 us: 1.11x slower                                                      |
| genshi_xml                 | 50.3 ms                                                | 56.2 ms: 1.12x slower                                                     |
| sqlglot_optimize           | 53.9 ms                                                | 60.4 ms: 1.12x slower                                                     |
| scimark_lu                 | 115 ms                                                 | 132 ms: 1.14x slower                                                      |
| regex_compile              | 131 ms                                                 | 151 ms: 1.15x slower                                                      |
| nqueens                    | 80.6 ms                                                | 94.6 ms: 1.17x slower                                                     |
| sympy_str                  | 274 ms                                                 | 322 ms: 1.18x slower                                                      |
| sympy_expand               | 462 ms                                                 | 545 ms: 1.18x slower                                                      |
| generators                 | 28.8 ms                                                | 34.1 ms: 1.18x slower                                                     |
| docutils                   | 2.58 sec                                               | 3.09 sec: 1.19x slower                                                    |
| sympy_sum                  | 150 ms                                                 | 186 ms: 1.24x slower                                                      |
| sympy_integrate            | 19.9 ms                                                | 24.8 ms: 1.25x slower                                                     |
| pylint                     | 313 ms                                                 | 394 ms: 1.26x slower                                                      |
| hexiom                     | 6.13 ms                                                | 8.07 ms: 1.32x slower                                                     |
| Geometric mean             | (ref)                                                  | 1.01x slower                                                              |

Benchmark hidden because not significant (6): thrift, coroutines, asyncio_websockets, bench_mp_pool, json, pycparser
Ignored benchmarks (14) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 90.88% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.10x