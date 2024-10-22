# Results vs. 3.13.0

- fork: mdboom
- ref: remove_redundant_typ
- machine: linux-x86_64
- commit hash: b0f5f3a
- commit date: 2024-09-23
- overall geometric mean: 1.02x faster
- HPT reliability: 99.72%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-linux-x86_64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 255 ms: 1.04x faster                                                  |
| docutils       | 2.58 sec                                               | 2.63 sec: 1.02x slower                                                |
| html5lib       | 64.5 ms                                                | 61.5 ms: 1.05x faster                                                 |
| tornado_http   | 91.5 ms                                                | 90.4 ms: 1.01x faster                                                 |
| Geometric mean | (ref)                                                  | 1.02x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-linux-x86_64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg  | 465 ms                                                 | 389 ms: 1.20x faster                                                  |
| async_tree_memoization     | 442 ms                                                 | 392 ms: 1.13x faster                                                  |
| async_tree_none            | 354 ms                                                 | 315 ms: 1.12x faster                                                  |
| async_tree_none_tg         | 320 ms                                                 | 301 ms: 1.06x faster                                                  |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 560 ms: 1.03x faster                                                  |
| asyncio_tcp                | 488 ms                                                 | 477 ms: 1.02x faster                                                  |
| async_generators           | 433 ms                                                 | 430 ms: 1.01x faster                                                  |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.78 sec: 1.00x faster                                                |
| asyncio_websockets         | 555 ms                                                 | 558 ms: 1.00x slower                                                  |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 549 ms: 1.01x slower                                                  |
| coroutines                 | 22.5 ms                                                | 22.8 ms: 1.01x slower                                                 |
| async_tree_io              | 843 ms                                                 | 867 ms: 1.03x slower                                                  |
| async_tree_io_tg           | 825 ms                                                 | 874 ms: 1.06x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-linux-x86_64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 75.6 ms: 1.04x faster                                                 |
| pidigits       | 186 ms                                                 | 187 ms: 1.00x slower                                                  |
| nbody          | 85.7 ms                                                | 86.7 ms: 1.01x slower                                                 |
| Geometric mean | (ref)                                                  | 1.01x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-linux-x86_64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 131 ms                                                 | 128 ms: 1.03x faster                                                  |
| regex_v8       | 25.3 ms                                                | 25.1 ms: 1.01x faster                                                 |
| regex_dna      | 220 ms                                                 | 225 ms: 1.02x slower                                                  |
| Geometric mean | (ref)                                                  | 1.00x faster                                                          |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-linux-x86_64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_process    | 60.4 ms                                                | 58.6 ms: 1.03x faster                                                 |
| xml_etree_generate   | 87.0 ms                                                | 84.8 ms: 1.03x faster                                                 |
| tomli_loads          | 2.11 sec                                               | 2.06 sec: 1.02x faster                                                |
| json_dumps           | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                 |
| pickle_dict          | 33.2 us                                                | 32.7 us: 1.01x faster                                                 |
| json_loads           | 27.0 us                                                | 26.7 us: 1.01x faster                                                 |
| pickle_list          | 5.01 us                                                | 4.98 us: 1.01x faster                                                 |
| unpickle_pure_python | 213 us                                                 | 216 us: 1.01x slower                                                  |
| xml_etree_iterparse  | 102 ms                                                 | 103 ms: 1.01x slower                                                  |
| pickle_pure_python   | 300 us                                                 | 305 us: 1.02x slower                                                  |
| pickle               | 11.6 us                                                | 11.8 us: 1.02x slower                                                 |
| unpickle_list        | 4.96 us                                                | 5.15 us: 1.04x slower                                                 |
| unpickle             | 14.9 us                                                | 15.5 us: 1.04x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.00x slower                                                          |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-linux-x86_64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.5 ms: 1.00x faster                                                 |
| python_startup_no_site | 6.99 ms                                                | 7.00 ms: 1.00x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.00x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-linux-x86_64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 22.9 ms                                                | 22.1 ms: 1.04x faster                                                 |
| genshi_xml      | 50.3 ms                                                | 48.6 ms: 1.04x faster                                                 |
| django_template | 34.4 ms                                                | 34.2 ms: 1.01x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.02x faster                                                          |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-linux-x86_64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy                   | 352 us                                                 | 255 us: 1.38x faster                                                  |
| deepcopy_memo              | 38.0 us                                                | 29.9 us: 1.27x faster                                                 |
| deepcopy_reduce            | 3.17 us                                                | 2.64 us: 1.20x faster                                                 |
| async_tree_memoization_tg  | 465 ms                                                 | 389 ms: 1.20x faster                                                  |
| go                         | 142 ms                                                 | 119 ms: 1.19x faster                                                  |
| async_tree_memoization     | 442 ms                                                 | 392 ms: 1.13x faster                                                  |
| async_tree_none            | 354 ms                                                 | 315 ms: 1.12x faster                                                  |
| pathlib                    | 17.1 ms                                                | 16.0 ms: 1.07x faster                                                 |
| async_tree_none_tg         | 320 ms                                                 | 301 ms: 1.06x faster                                                  |
| richards                   | 48.1 ms                                                | 45.4 ms: 1.06x faster                                                 |
| richards_super             | 54.4 ms                                                | 51.6 ms: 1.05x faster                                                 |
| json                       | 5.20 ms                                                | 4.94 ms: 1.05x faster                                                 |
| pprint_safe_repr           | 744 ms                                                 | 708 ms: 1.05x faster                                                  |
| html5lib                   | 64.5 ms                                                | 61.5 ms: 1.05x faster                                                 |
| 2to3                       | 265 ms                                                 | 255 ms: 1.04x faster                                                  |
| pprint_pformat             | 1.51 sec                                               | 1.45 sec: 1.04x faster                                                |
| float                      | 78.5 ms                                                | 75.6 ms: 1.04x faster                                                 |
| genshi_text                | 22.9 ms                                                | 22.1 ms: 1.04x faster                                                 |
| genshi_xml                 | 50.3 ms                                                | 48.6 ms: 1.04x faster                                                 |
| bench_thread_pool          | 815 us                                                 | 789 us: 1.03x faster                                                  |
| xml_etree_process          | 60.4 ms                                                | 58.6 ms: 1.03x faster                                                 |
| xml_etree_generate         | 87.0 ms                                                | 84.8 ms: 1.03x faster                                                 |
| sympy_str                  | 274 ms                                                 | 267 ms: 1.03x faster                                                  |
| sympy_sum                  | 150 ms                                                 | 146 ms: 1.03x faster                                                  |
| regex_compile              | 131 ms                                                 | 128 ms: 1.03x faster                                                  |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 560 ms: 1.03x faster                                                  |
| scimark_lu                 | 115 ms                                                 | 112 ms: 1.03x faster                                                  |
| thrift                     | 796 us                                                 | 777 us: 1.03x faster                                                  |
| tomli_loads                | 2.11 sec                                               | 2.06 sec: 1.02x faster                                                |
| asyncio_tcp                | 488 ms                                                 | 477 ms: 1.02x faster                                                  |
| spectral_norm              | 115 ms                                                 | 112 ms: 1.02x faster                                                  |
| generators                 | 28.8 ms                                                | 28.2 ms: 1.02x faster                                                 |
| mdp                        | 2.74 sec                                               | 2.69 sec: 1.02x faster                                                |
| sympy_expand               | 462 ms                                                 | 453 ms: 1.02x faster                                                  |
| pycparser                  | 1.19 sec                                               | 1.17 sec: 1.02x faster                                                |
| sympy_integrate            | 19.9 ms                                                | 19.6 ms: 1.02x faster                                                 |
| nqueens                    | 80.6 ms                                                | 79.4 ms: 1.01x faster                                                 |
| sqlglot_optimize           | 53.9 ms                                                | 53.1 ms: 1.01x faster                                                 |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.95 ms: 1.01x faster                                                 |
| json_dumps                 | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                 |
| pickle_dict                | 33.2 us                                                | 32.7 us: 1.01x faster                                                 |
| sqlglot_normalize          | 107 ms                                                 | 106 ms: 1.01x faster                                                  |
| tornado_http               | 91.5 ms                                                | 90.4 ms: 1.01x faster                                                 |
| crypto_pyaes               | 73.0 ms                                                | 72.0 ms: 1.01x faster                                                 |
| json_loads                 | 27.0 us                                                | 26.7 us: 1.01x faster                                                 |
| comprehensions             | 16.4 us                                                | 16.2 us: 1.01x faster                                                 |
| logging_format             | 6.25 us                                                | 6.20 us: 1.01x faster                                                 |
| regex_v8                   | 25.3 ms                                                | 25.1 ms: 1.01x faster                                                 |
| logging_simple             | 5.66 us                                                | 5.62 us: 1.01x faster                                                 |
| django_template            | 34.4 ms                                                | 34.2 ms: 1.01x faster                                                 |
| async_generators           | 433 ms                                                 | 430 ms: 1.01x faster                                                  |
| pickle_list                | 5.01 us                                                | 4.98 us: 1.01x faster                                                 |
| python_startup             | 10.6 ms                                                | 10.5 ms: 1.00x faster                                                 |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.78 sec: 1.00x faster                                                |
| meteor_contest             | 108 ms                                                 | 107 ms: 1.00x faster                                                  |
| python_startup_no_site     | 6.99 ms                                                | 7.00 ms: 1.00x slower                                                 |
| pidigits                   | 186 ms                                                 | 187 ms: 1.00x slower                                                  |
| chaos                      | 58.4 ms                                                | 58.6 ms: 1.00x slower                                                 |
| sqlglot_transpile          | 1.57 ms                                                | 1.58 ms: 1.00x slower                                                 |
| asyncio_websockets         | 555 ms                                                 | 558 ms: 1.00x slower                                                  |
| gc_traversal               | 3.81 ms                                                | 3.83 ms: 1.01x slower                                                 |
| sqlite_synth               | 2.85 us                                                | 2.87 us: 1.01x slower                                                 |
| scimark_sor                | 122 ms                                                 | 123 ms: 1.01x slower                                                  |
| hexiom                     | 6.13 ms                                                | 6.19 ms: 1.01x slower                                                 |
| raytrace                   | 262 ms                                                 | 264 ms: 1.01x slower                                                  |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 549 ms: 1.01x slower                                                  |
| nbody                      | 85.7 ms                                                | 86.7 ms: 1.01x slower                                                 |
| unpickle_pure_python       | 213 us                                                 | 216 us: 1.01x slower                                                  |
| coroutines                 | 22.5 ms                                                | 22.8 ms: 1.01x slower                                                 |
| xml_etree_iterparse        | 102 ms                                                 | 103 ms: 1.01x slower                                                  |
| sqlglot_parse              | 1.27 ms                                                | 1.28 ms: 1.02x slower                                                 |
| pickle_pure_python         | 300 us                                                 | 305 us: 1.02x slower                                                  |
| bpe_tokeniser              | 4.69 sec                                               | 4.77 sec: 1.02x slower                                                |
| pickle                     | 11.6 us                                                | 11.8 us: 1.02x slower                                                 |
| docutils                   | 2.58 sec                                               | 2.63 sec: 1.02x slower                                                |
| regex_dna                  | 220 ms                                                 | 225 ms: 1.02x slower                                                  |
| scimark_monte_carlo        | 66.3 ms                                                | 68.2 ms: 1.03x slower                                                 |
| dulwich_log                | 63.0 ms                                                | 64.8 ms: 1.03x slower                                                 |
| async_tree_io              | 843 ms                                                 | 867 ms: 1.03x slower                                                  |
| pyflate                    | 460 ms                                                 | 473 ms: 1.03x slower                                                  |
| deltablue                  | 3.15 ms                                                | 3.25 ms: 1.03x slower                                                 |
| logging_silent             | 102 ns                                                 | 106 ns: 1.04x slower                                                  |
| unpickle_list              | 4.96 us                                                | 5.15 us: 1.04x slower                                                 |
| unpickle                   | 14.9 us                                                | 15.5 us: 1.04x slower                                                 |
| async_tree_io_tg           | 825 ms                                                 | 874 ms: 1.06x slower                                                  |
| fannkuch                   | 381 ms                                                 | 404 ms: 1.06x slower                                                  |
| create_gc_cycles           | 1.61 ms                                                | 1.72 ms: 1.07x slower                                                 |
| unpack_sequence            | 42.4 ns                                                | 49.3 ns: 1.16x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                          |

Benchmark hidden because not significant (9): telco, xml_etree_parse, coverage, typing_runtime_protocols, mako, bench_mp_pool, regex_effbot, scimark_fft, pylint
Ignored benchmarks (7) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 99.72% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x