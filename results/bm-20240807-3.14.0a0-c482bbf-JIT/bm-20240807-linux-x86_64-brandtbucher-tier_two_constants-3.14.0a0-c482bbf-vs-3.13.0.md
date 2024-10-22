# Results vs. 3.13.0

- fork: brandtbucher
- ref: tier_two_constants
- machine: linux-x86_64
- commit hash: c482bbf
- commit date: 2024-08-07
- overall geometric mean: 1.01x faster
- HPT reliability: 72.10%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240807-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-c482bbf |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 274 ms: 1.04x slower                                                      |
| docutils       | 2.58 sec                                               | 2.91 sec: 1.13x slower                                                    |
| html5lib       | 64.5 ms                                                | 66.1 ms: 1.02x slower                                                     |
| tornado_http   | 91.5 ms                                                | 92.7 ms: 1.01x slower                                                     |
| Geometric mean | (ref)                                                  | 1.05x slower                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240807-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-c482bbf |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 465 ms                                                 | 392 ms: 1.18x faster                                                      |
| async_tree_none            | 354 ms                                                 | 324 ms: 1.09x faster                                                      |
| async_tree_none_tg         | 320 ms                                                 | 300 ms: 1.07x faster                                                      |
| async_tree_memoization     | 442 ms                                                 | 420 ms: 1.05x faster                                                      |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 533 ms: 1.02x faster                                                      |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.01x slower                                                    |
| coroutines                 | 22.5 ms                                                | 22.8 ms: 1.01x slower                                                     |
| asyncio_tcp                | 488 ms                                                 | 500 ms: 1.03x slower                                                      |
| async_tree_io_tg           | 825 ms                                                 | 863 ms: 1.05x slower                                                      |
| async_generators           | 433 ms                                                 | 459 ms: 1.06x slower                                                      |
| async_tree_io              | 843 ms                                                 | 901 ms: 1.07x slower                                                      |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                              |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240807-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-c482bbf |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 70.0 ms: 1.12x faster                                                     |
| nbody          | 85.7 ms                                                | 78.1 ms: 1.10x faster                                                     |
| pidigits       | 186 ms                                                 | 185 ms: 1.00x faster                                                      |
| Geometric mean | (ref)                                                  | 1.07x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240807-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-c482bbf |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.84 ms: 1.01x faster                                                     |
| regex_v8       | 25.3 ms                                                | 25.4 ms: 1.00x slower                                                     |
| regex_compile  | 131 ms                                                 | 134 ms: 1.02x slower                                                      |
| regex_dna      | 220 ms                                                 | 228 ms: 1.04x slower                                                      |
| Geometric mean | (ref)                                                  | 1.01x slower                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240807-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-c482bbf |
|---------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads         | 2.11 sec                                               | 1.92 sec: 1.10x faster                                                    |
| xml_etree_generate  | 87.0 ms                                                | 79.4 ms: 1.10x faster                                                     |
| xml_etree_process   | 60.4 ms                                                | 55.8 ms: 1.08x faster                                                     |
| xml_etree_parse     | 156 ms                                                 | 146 ms: 1.07x faster                                                      |
| xml_etree_iterparse | 102 ms                                                 | 99.2 ms: 1.03x faster                                                     |
| pickle_pure_python  | 300 us                                                 | 295 us: 1.02x faster                                                      |
| json_dumps          | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                     |
| json_loads          | 27.0 us                                                | 28.0 us: 1.04x slower                                                     |
| Geometric mean      | (ref)                                                  | 1.04x faster                                                              |

Benchmark hidden because not significant (1): unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240807-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-c482bbf |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.6 ms: 1.00x slower                                                     |
| python_startup_no_site | 6.99 ms                                                | 7.20 ms: 1.03x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240807-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-c482bbf |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.70 ms: 1.14x faster                                                     |
| django_template | 34.4 ms                                                | 36.0 ms: 1.05x slower                                                     |
| genshi_text     | 22.9 ms                                                | 24.0 ms: 1.05x slower                                                     |
| genshi_xml      | 50.3 ms                                                | 53.4 ms: 1.06x slower                                                     |
| Geometric mean  | (ref)                                                  | 1.00x slower                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240807-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-c482bbf |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| deepcopy_memo              | 38.0 us                                                | 28.6 us: 1.33x faster                                                     |
| deepcopy                   | 352 us                                                 | 274 us: 1.29x faster                                                      |
| scimark_fft                | 369 ms                                                 | 306 ms: 1.20x faster                                                      |
| async_tree_memoization_tg  | 465 ms                                                 | 392 ms: 1.18x faster                                                      |
| richards                   | 48.1 ms                                                | 41.1 ms: 1.17x faster                                                     |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.31 ms: 1.17x faster                                                     |
| richards_super             | 54.4 ms                                                | 47.0 ms: 1.16x faster                                                     |
| deepcopy_reduce            | 3.17 us                                                | 2.74 us: 1.15x faster                                                     |
| mako                       | 11.1 ms                                                | 9.70 ms: 1.14x faster                                                     |
| float                      | 78.5 ms                                                | 70.0 ms: 1.12x faster                                                     |
| spectral_norm              | 115 ms                                                 | 103 ms: 1.12x faster                                                      |
| scimark_monte_carlo        | 66.3 ms                                                | 60.1 ms: 1.10x faster                                                     |
| tomli_loads                | 2.11 sec                                               | 1.92 sec: 1.10x faster                                                    |
| nbody                      | 85.7 ms                                                | 78.1 ms: 1.10x faster                                                     |
| xml_etree_generate         | 87.0 ms                                                | 79.4 ms: 1.10x faster                                                     |
| async_tree_none            | 354 ms                                                 | 324 ms: 1.09x faster                                                      |
| pyflate                    | 460 ms                                                 | 421 ms: 1.09x faster                                                      |
| crypto_pyaes               | 73.0 ms                                                | 66.9 ms: 1.09x faster                                                     |
| xml_etree_process          | 60.4 ms                                                | 55.8 ms: 1.08x faster                                                     |
| telco                      | 8.45 ms                                                | 7.90 ms: 1.07x faster                                                     |
| xml_etree_parse            | 156 ms                                                 | 146 ms: 1.07x faster                                                      |
| async_tree_none_tg         | 320 ms                                                 | 300 ms: 1.07x faster                                                      |
| mdp                        | 2.74 sec                                               | 2.57 sec: 1.07x faster                                                    |
| pathlib                    | 17.1 ms                                                | 16.1 ms: 1.06x faster                                                     |
| fannkuch                   | 381 ms                                                 | 361 ms: 1.06x faster                                                      |
| async_tree_memoization     | 442 ms                                                 | 420 ms: 1.05x faster                                                      |
| bpe_tokeniser              | 4.69 sec                                               | 4.47 sec: 1.05x faster                                                    |
| scimark_sor                | 122 ms                                                 | 118 ms: 1.04x faster                                                      |
| pprint_safe_repr           | 744 ms                                                 | 720 ms: 1.03x faster                                                      |
| xml_etree_iterparse        | 102 ms                                                 | 99.2 ms: 1.03x faster                                                     |
| meteor_contest             | 108 ms                                                 | 106 ms: 1.02x faster                                                      |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 533 ms: 1.02x faster                                                      |
| pickle_pure_python         | 300 us                                                 | 295 us: 1.02x faster                                                      |
| logging_format             | 6.25 us                                                | 6.18 us: 1.01x faster                                                     |
| regex_effbot               | 3.88 ms                                                | 3.84 ms: 1.01x faster                                                     |
| json_dumps                 | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                     |
| logging_simple             | 5.66 us                                                | 5.61 us: 1.01x faster                                                     |
| gc_traversal               | 3.81 ms                                                | 3.77 ms: 1.01x faster                                                     |
| pidigits                   | 186 ms                                                 | 185 ms: 1.00x faster                                                      |
| python_startup             | 10.6 ms                                                | 10.6 ms: 1.00x slower                                                     |
| regex_v8                   | 25.3 ms                                                | 25.4 ms: 1.00x slower                                                     |
| bench_thread_pool          | 815 us                                                 | 819 us: 1.01x slower                                                      |
| comprehensions             | 16.4 us                                                | 16.5 us: 1.01x slower                                                     |
| raytrace                   | 262 ms                                                 | 263 ms: 1.01x slower                                                      |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.01x slower                                                    |
| go                         | 142 ms                                                 | 143 ms: 1.01x slower                                                      |
| tornado_http               | 91.5 ms                                                | 92.7 ms: 1.01x slower                                                     |
| coroutines                 | 22.5 ms                                                | 22.8 ms: 1.01x slower                                                     |
| sqlglot_parse              | 1.27 ms                                                | 1.29 ms: 1.02x slower                                                     |
| html5lib                   | 64.5 ms                                                | 66.1 ms: 1.02x slower                                                     |
| regex_compile              | 131 ms                                                 | 134 ms: 1.02x slower                                                      |
| asyncio_tcp                | 488 ms                                                 | 500 ms: 1.03x slower                                                      |
| sqlglot_transpile          | 1.57 ms                                                | 1.62 ms: 1.03x slower                                                     |
| python_startup_no_site     | 6.99 ms                                                | 7.20 ms: 1.03x slower                                                     |
| sqlglot_optimize           | 53.9 ms                                                | 55.7 ms: 1.03x slower                                                     |
| 2to3                       | 265 ms                                                 | 274 ms: 1.04x slower                                                      |
| regex_dna                  | 220 ms                                                 | 228 ms: 1.04x slower                                                      |
| json_loads                 | 27.0 us                                                | 28.0 us: 1.04x slower                                                     |
| sqlglot_normalize          | 107 ms                                                 | 112 ms: 1.04x slower                                                      |
| async_tree_io_tg           | 825 ms                                                 | 863 ms: 1.05x slower                                                      |
| django_template            | 34.4 ms                                                | 36.0 ms: 1.05x slower                                                     |
| genshi_text                | 22.9 ms                                                | 24.0 ms: 1.05x slower                                                     |
| typing_runtime_protocols   | 159 us                                                 | 167 us: 1.05x slower                                                      |
| nqueens                    | 80.6 ms                                                | 84.8 ms: 1.05x slower                                                     |
| genshi_xml                 | 50.3 ms                                                | 53.4 ms: 1.06x slower                                                     |
| async_generators           | 433 ms                                                 | 459 ms: 1.06x slower                                                      |
| async_tree_io              | 843 ms                                                 | 901 ms: 1.07x slower                                                      |
| hexiom                     | 6.13 ms                                                | 6.64 ms: 1.08x slower                                                     |
| coverage                   | 83.7 ms                                                | 90.9 ms: 1.09x slower                                                     |
| sympy_str                  | 274 ms                                                 | 298 ms: 1.09x slower                                                      |
| sympy_expand               | 462 ms                                                 | 508 ms: 1.10x slower                                                      |
| create_gc_cycles           | 1.61 ms                                                | 1.77 ms: 1.10x slower                                                     |
| deltablue                  | 3.15 ms                                                | 3.48 ms: 1.11x slower                                                     |
| docutils                   | 2.58 sec                                               | 2.91 sec: 1.13x slower                                                    |
| sympy_integrate            | 19.9 ms                                                | 22.5 ms: 1.13x slower                                                     |
| sympy_sum                  | 150 ms                                                 | 170 ms: 1.13x slower                                                      |
| pylint                     | 313 ms                                                 | 355 ms: 1.14x slower                                                      |
| generators                 | 28.8 ms                                                | 33.1 ms: 1.15x slower                                                     |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                              |

Benchmark hidden because not significant (11): scimark_lu, async_tree_cpu_io_mixed, pycparser, json, logging_silent, pprint_pformat, chaos, bench_mp_pool, asyncio_websockets, thrift, unpickle_pure_python
Ignored benchmarks (15) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 72.10% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.08x