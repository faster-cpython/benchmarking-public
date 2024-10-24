# Results vs. 3.13.0

- fork: colesbury
- ref: gh_125610_STORE_ATTR
- machine: linux-x86_64
- commit hash: 3a126a8
- commit date: 2024-10-16
- overall geometric mean: 1.01x slower
- HPT reliability: 76.64%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-linux-x86_64-colesbury-gh_125610_STORE_ATTR-3.14.0a1+-3a126a8 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 254 ms: 1.04x faster                                                      |
| docutils       | 2.58 sec                                               | 2.64 sec: 1.02x slower                                                    |
| html5lib       | 64.5 ms                                                | 63.0 ms: 1.02x faster                                                     |
| tornado_http   | 91.5 ms                                                | 90.2 ms: 1.01x faster                                                     |
| Geometric mean | (ref)                                                  | 1.02x faster                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-linux-x86_64-colesbury-gh_125610_STORE_ATTR-3.14.0a1+-3a126a8 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 465 ms                                                 | 381 ms: 1.22x faster                                                      |
| async_tree_none            | 354 ms                                                 | 328 ms: 1.08x faster                                                      |
| async_tree_memoization     | 442 ms                                                 | 415 ms: 1.06x faster                                                      |
| asyncio_websockets         | 555 ms                                                 | 553 ms: 1.00x faster                                                      |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 564 ms: 1.04x slower                                                      |
| coroutines                 | 22.5 ms                                                | 23.6 ms: 1.05x slower                                                     |
| async_tree_io_tg           | 825 ms                                                 | 975 ms: 1.18x slower                                                      |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                              |

Benchmark hidden because not significant (4): async_tree_none_tg, async_generators, async_tree_cpu_io_mixed, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-linux-x86_64-colesbury-gh_125610_STORE_ATTR-3.14.0a1+-3a126a8 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pidigits       | 186 ms                                                 | 187 ms: 1.01x slower                                                      |
| nbody          | 85.7 ms                                                | 89.3 ms: 1.04x slower                                                     |
| Geometric mean | (ref)                                                  | 1.02x slower                                                              |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-linux-x86_64-colesbury-gh_125610_STORE_ATTR-3.14.0a1+-3a126a8 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.61 ms: 1.08x faster                                                     |
| regex_dna      | 220 ms                                                 | 210 ms: 1.04x faster                                                      |
| regex_v8       | 25.3 ms                                                | 24.6 ms: 1.03x faster                                                     |
| regex_compile  | 131 ms                                                 | 129 ms: 1.02x faster                                                      |
| Geometric mean | (ref)                                                  | 1.04x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-linux-x86_64-colesbury-gh_125610_STORE_ATTR-3.14.0a1+-3a126a8 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| xml_etree_process    | 60.4 ms                                                | 59.6 ms: 1.01x faster                                                     |
| tomli_loads          | 2.11 sec                                               | 2.09 sec: 1.01x faster                                                    |
| xml_etree_generate   | 87.0 ms                                                | 86.1 ms: 1.01x faster                                                     |
| unpickle_pure_python | 213 us                                                 | 217 us: 1.02x slower                                                      |
| xml_etree_parse      | 156 ms                                                 | 160 ms: 1.02x slower                                                      |
| pickle_pure_python   | 300 us                                                 | 309 us: 1.03x slower                                                      |
| xml_etree_iterparse  | 102 ms                                                 | 106 ms: 1.04x slower                                                      |
| json_dumps           | 10.4 ms                                                | 11.5 ms: 1.10x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.02x slower                                                              |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-linux-x86_64-colesbury-gh_125610_STORE_ATTR-3.14.0a1+-3a126a8 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 6.99 ms                                                | 7.04 ms: 1.01x slower                                                     |
| python_startup         | 10.6 ms                                                | 11.8 ms: 1.12x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-linux-x86_64-colesbury-gh_125610_STORE_ATTR-3.14.0a1+-3a126a8 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| django_template | 34.4 ms                                                | 34.2 ms: 1.01x faster                                                     |
| genshi_xml      | 50.3 ms                                                | 51.3 ms: 1.02x slower                                                     |
| mako            | 11.1 ms                                                | 11.5 ms: 1.04x slower                                                     |
| Geometric mean  | (ref)                                                  | 1.01x slower                                                              |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-linux-x86_64-colesbury-gh_125610_STORE_ATTR-3.14.0a1+-3a126a8 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| deepcopy                   | 352 us                                                 | 262 us: 1.34x faster                                                      |
| deepcopy_memo              | 38.0 us                                                | 30.7 us: 1.24x faster                                                     |
| async_tree_memoization_tg  | 465 ms                                                 | 381 ms: 1.22x faster                                                      |
| go                         | 142 ms                                                 | 120 ms: 1.18x faster                                                      |
| deepcopy_reduce            | 3.17 us                                                | 2.71 us: 1.17x faster                                                     |
| async_tree_none            | 354 ms                                                 | 328 ms: 1.08x faster                                                      |
| regex_effbot               | 3.88 ms                                                | 3.61 ms: 1.08x faster                                                     |
| telco                      | 8.45 ms                                                | 7.86 ms: 1.08x faster                                                     |
| async_tree_memoization     | 442 ms                                                 | 415 ms: 1.06x faster                                                      |
| pathlib                    | 17.1 ms                                                | 16.1 ms: 1.06x faster                                                     |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.80 ms: 1.05x faster                                                     |
| regex_dna                  | 220 ms                                                 | 210 ms: 1.04x faster                                                      |
| richards                   | 48.1 ms                                                | 46.1 ms: 1.04x faster                                                     |
| 2to3                       | 265 ms                                                 | 254 ms: 1.04x faster                                                      |
| richards_super             | 54.4 ms                                                | 52.2 ms: 1.04x faster                                                     |
| generators                 | 28.8 ms                                                | 27.7 ms: 1.04x faster                                                     |
| logging_simple             | 5.66 us                                                | 5.47 us: 1.04x faster                                                     |
| logging_format             | 6.25 us                                                | 6.05 us: 1.03x faster                                                     |
| regex_v8                   | 25.3 ms                                                | 24.6 ms: 1.03x faster                                                     |
| html5lib                   | 64.5 ms                                                | 63.0 ms: 1.02x faster                                                     |
| sympy_str                  | 274 ms                                                 | 268 ms: 1.02x faster                                                      |
| pycparser                  | 1.19 sec                                               | 1.17 sec: 1.02x faster                                                    |
| pprint_safe_repr           | 744 ms                                                 | 730 ms: 1.02x faster                                                      |
| json                       | 5.20 ms                                                | 5.10 ms: 1.02x faster                                                     |
| thrift                     | 796 us                                                 | 782 us: 1.02x faster                                                      |
| sympy_sum                  | 150 ms                                                 | 147 ms: 1.02x faster                                                      |
| regex_compile              | 131 ms                                                 | 129 ms: 1.02x faster                                                      |
| scimark_fft                | 369 ms                                                 | 363 ms: 1.02x faster                                                      |
| sympy_expand               | 462 ms                                                 | 455 ms: 1.02x faster                                                      |
| pprint_pformat             | 1.51 sec                                               | 1.49 sec: 1.02x faster                                                    |
| sqlglot_optimize           | 53.9 ms                                                | 53.1 ms: 1.01x faster                                                     |
| tornado_http               | 91.5 ms                                                | 90.2 ms: 1.01x faster                                                     |
| sqlglot_normalize          | 107 ms                                                 | 106 ms: 1.01x faster                                                      |
| xml_etree_process          | 60.4 ms                                                | 59.6 ms: 1.01x faster                                                     |
| mdp                        | 2.74 sec                                               | 2.71 sec: 1.01x faster                                                    |
| tomli_loads                | 2.11 sec                                               | 2.09 sec: 1.01x faster                                                    |
| xml_etree_generate         | 87.0 ms                                                | 86.1 ms: 1.01x faster                                                     |
| crypto_pyaes               | 73.0 ms                                                | 72.4 ms: 1.01x faster                                                     |
| django_template            | 34.4 ms                                                | 34.2 ms: 1.01x faster                                                     |
| meteor_contest             | 108 ms                                                 | 107 ms: 1.01x faster                                                      |
| scimark_lu                 | 115 ms                                                 | 114 ms: 1.00x faster                                                      |
| asyncio_websockets         | 555 ms                                                 | 553 ms: 1.00x faster                                                      |
| sympy_integrate            | 19.9 ms                                                | 19.8 ms: 1.00x faster                                                     |
| spectral_norm              | 115 ms                                                 | 115 ms: 1.00x slower                                                      |
| pidigits                   | 186 ms                                                 | 187 ms: 1.01x slower                                                      |
| python_startup_no_site     | 6.99 ms                                                | 7.04 ms: 1.01x slower                                                     |
| dulwich_log                | 63.0 ms                                                | 63.6 ms: 1.01x slower                                                     |
| sqlglot_transpile          | 1.57 ms                                                | 1.59 ms: 1.01x slower                                                     |
| comprehensions             | 16.4 us                                                | 16.6 us: 1.01x slower                                                     |
| unpickle_pure_python       | 213 us                                                 | 217 us: 1.02x slower                                                      |
| hexiom                     | 6.13 ms                                                | 6.23 ms: 1.02x slower                                                     |
| logging_silent             | 102 ns                                                 | 104 ns: 1.02x slower                                                      |
| raytrace                   | 262 ms                                                 | 266 ms: 1.02x slower                                                      |
| genshi_xml                 | 50.3 ms                                                | 51.3 ms: 1.02x slower                                                     |
| bpe_tokeniser              | 4.69 sec                                               | 4.78 sec: 1.02x slower                                                    |
| docutils                   | 2.58 sec                                               | 2.64 sec: 1.02x slower                                                    |
| sqlglot_parse              | 1.27 ms                                                | 1.29 ms: 1.02x slower                                                     |
| xml_etree_parse            | 156 ms                                                 | 160 ms: 1.02x slower                                                      |
| chaos                      | 58.4 ms                                                | 59.9 ms: 1.03x slower                                                     |
| nqueens                    | 80.6 ms                                                | 82.7 ms: 1.03x slower                                                     |
| bench_thread_pool          | 815 us                                                 | 838 us: 1.03x slower                                                      |
| pickle_pure_python         | 300 us                                                 | 309 us: 1.03x slower                                                      |
| scimark_sor                | 122 ms                                                 | 126 ms: 1.03x slower                                                      |
| deltablue                  | 3.15 ms                                                | 3.25 ms: 1.03x slower                                                     |
| scimark_monte_carlo        | 66.3 ms                                                | 68.5 ms: 1.03x slower                                                     |
| mako                       | 11.1 ms                                                | 11.5 ms: 1.04x slower                                                     |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 564 ms: 1.04x slower                                                      |
| nbody                      | 85.7 ms                                                | 89.3 ms: 1.04x slower                                                     |
| xml_etree_iterparse        | 102 ms                                                 | 106 ms: 1.04x slower                                                      |
| pyflate                    | 460 ms                                                 | 480 ms: 1.04x slower                                                      |
| coroutines                 | 22.5 ms                                                | 23.6 ms: 1.05x slower                                                     |
| fannkuch                   | 381 ms                                                 | 406 ms: 1.07x slower                                                      |
| json_dumps                 | 10.4 ms                                                | 11.5 ms: 1.10x slower                                                     |
| python_startup             | 10.6 ms                                                | 11.8 ms: 1.12x slower                                                     |
| gc_traversal               | 3.81 ms                                                | 4.37 ms: 1.15x slower                                                     |
| async_tree_io_tg           | 825 ms                                                 | 975 ms: 1.18x slower                                                      |
| create_gc_cycles           | 1.61 ms                                                | 2.66 ms: 1.65x slower                                                     |
| bench_mp_pool              | 24.0 ms                                                | 78.5 ms: 3.27x slower                                                     |
| Geometric mean             | (ref)                                                  | 1.01x slower                                                              |

Benchmark hidden because not significant (10): json_loads, genshi_text, coverage, async_tree_none_tg, typing_runtime_protocols, async_generators, async_tree_cpu_io_mixed, float, pylint, async_tree_io
Ignored benchmarks (16) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (1) of results/bm-20241016-3.14.0a1+-3a126a8/bm-20241016-linux-x86_64-colesbury-gh_125610_STORE_ATTR-3.14.0a1+-3a126a8.json: sphinx

# HPT report

- Reliability score: 76.64% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.12x