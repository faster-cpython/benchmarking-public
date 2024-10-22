# Results vs. 3.13.0

- fork: brandtbucher
- ref: decref_escapes
- machine: linux-x86_64
- commit hash: 87cbfd7
- commit date: 2024-09-23
- overall geometric mean: 1.00x slower
- HPT reliability: 79.41%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-linux-x86_64-brandtbucher-decref_escapes-3.14.0a0-87cbfd7 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 278 ms: 1.05x slower                                                  |
| docutils       | 2.58 sec                                               | 2.96 sec: 1.15x slower                                                |
| html5lib       | 64.5 ms                                                | 62.7 ms: 1.03x faster                                                 |
| tornado_http   | 91.5 ms                                                | 94.9 ms: 1.04x slower                                                 |
| Geometric mean | (ref)                                                  | 1.05x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-linux-x86_64-brandtbucher-decref_escapes-3.14.0a0-87cbfd7 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg  | 465 ms                                                 | 388 ms: 1.20x faster                                                  |
| async_tree_memoization     | 442 ms                                                 | 395 ms: 1.12x faster                                                  |
| async_tree_none            | 354 ms                                                 | 317 ms: 1.12x faster                                                  |
| async_tree_none_tg         | 320 ms                                                 | 308 ms: 1.04x faster                                                  |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.01x slower                                                |
| asyncio_tcp                | 488 ms                                                 | 494 ms: 1.01x slower                                                  |
| async_tree_io              | 843 ms                                                 | 862 ms: 1.02x slower                                                  |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 557 ms: 1.03x slower                                                  |
| async_generators           | 433 ms                                                 | 457 ms: 1.06x slower                                                  |
| async_tree_io_tg           | 825 ms                                                 | 874 ms: 1.06x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                          |

Benchmark hidden because not significant (3): asyncio_websockets, async_tree_cpu_io_mixed, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-linux-x86_64-brandtbucher-decref_escapes-3.14.0a0-87cbfd7 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 70.6 ms: 1.11x faster                                                 |
| nbody          | 85.7 ms                                                | 81.4 ms: 1.05x faster                                                 |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                  | 1.05x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-linux-x86_64-brandtbucher-decref_escapes-3.14.0a0-87cbfd7 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.61 ms: 1.07x faster                                                 |
| regex_v8       | 25.3 ms                                                | 24.1 ms: 1.05x faster                                                 |
| regex_dna      | 220 ms                                                 | 215 ms: 1.02x faster                                                  |
| regex_compile  | 131 ms                                                 | 142 ms: 1.08x slower                                                  |
| Geometric mean | (ref)                                                  | 1.02x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-linux-x86_64-brandtbucher-decref_escapes-3.14.0a0-87cbfd7 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_generate   | 87.0 ms                                                | 78.2 ms: 1.11x faster                                                 |
| xml_etree_process    | 60.4 ms                                                | 55.0 ms: 1.10x faster                                                 |
| tomli_loads          | 2.11 sec                                               | 1.95 sec: 1.08x faster                                                |
| xml_etree_parse      | 156 ms                                                 | 146 ms: 1.07x faster                                                  |
| json_dumps           | 10.4 ms                                                | 10.1 ms: 1.03x faster                                                 |
| xml_etree_iterparse  | 102 ms                                                 | 99.3 ms: 1.03x faster                                                 |
| pickle               | 11.6 us                                                | 11.4 us: 1.01x faster                                                 |
| json_loads           | 27.0 us                                                | 26.7 us: 1.01x faster                                                 |
| pickle_list          | 5.01 us                                                | 5.04 us: 1.01x slower                                                 |
| unpickle_pure_python | 213 us                                                 | 216 us: 1.01x slower                                                  |
| pickle_pure_python   | 300 us                                                 | 308 us: 1.02x slower                                                  |
| unpickle_list        | 4.96 us                                                | 5.31 us: 1.07x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                          |

Benchmark hidden because not significant (2): unpickle, pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-linux-x86_64-brandtbucher-decref_escapes-3.14.0a0-87cbfd7 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.5 ms: 1.00x faster                                                 |
| python_startup_no_site | 6.99 ms                                                | 7.06 ms: 1.01x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.00x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-linux-x86_64-brandtbucher-decref_escapes-3.14.0a0-87cbfd7 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.77 ms: 1.14x faster                                                 |
| django_template | 34.4 ms                                                | 36.4 ms: 1.06x slower                                                 |
| genshi_text     | 22.9 ms                                                | 24.9 ms: 1.09x slower                                                 |
| genshi_xml      | 50.3 ms                                                | 60.0 ms: 1.19x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.05x slower                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-linux-x86_64-brandtbucher-decref_escapes-3.14.0a0-87cbfd7 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy_memo              | 38.0 us                                                | 27.0 us: 1.41x faster                                                 |
| deepcopy                   | 352 us                                                 | 260 us: 1.35x faster                                                  |
| deepcopy_reduce            | 3.17 us                                                | 2.62 us: 1.21x faster                                                 |
| async_tree_memoization_tg  | 465 ms                                                 | 388 ms: 1.20x faster                                                  |
| scimark_fft                | 369 ms                                                 | 315 ms: 1.17x faster                                                  |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.32 ms: 1.16x faster                                                 |
| richards_super             | 54.4 ms                                                | 47.2 ms: 1.15x faster                                                 |
| mako                       | 11.1 ms                                                | 9.77 ms: 1.14x faster                                                 |
| richards                   | 48.1 ms                                                | 42.7 ms: 1.13x faster                                                 |
| async_tree_memoization     | 442 ms                                                 | 395 ms: 1.12x faster                                                  |
| async_tree_none            | 354 ms                                                 | 317 ms: 1.12x faster                                                  |
| spectral_norm              | 115 ms                                                 | 103 ms: 1.12x faster                                                  |
| xml_etree_generate         | 87.0 ms                                                | 78.2 ms: 1.11x faster                                                 |
| float                      | 78.5 ms                                                | 70.6 ms: 1.11x faster                                                 |
| xml_etree_process          | 60.4 ms                                                | 55.0 ms: 1.10x faster                                                 |
| mdp                        | 2.74 sec                                               | 2.52 sec: 1.09x faster                                                |
| tomli_loads                | 2.11 sec                                               | 1.95 sec: 1.08x faster                                                |
| crypto_pyaes               | 73.0 ms                                                | 67.6 ms: 1.08x faster                                                 |
| regex_effbot               | 3.88 ms                                                | 3.61 ms: 1.07x faster                                                 |
| xml_etree_parse            | 156 ms                                                 | 146 ms: 1.07x faster                                                  |
| go                         | 142 ms                                                 | 133 ms: 1.07x faster                                                  |
| pathlib                    | 17.1 ms                                                | 16.1 ms: 1.06x faster                                                 |
| nbody                      | 85.7 ms                                                | 81.4 ms: 1.05x faster                                                 |
| scimark_monte_carlo        | 66.3 ms                                                | 63.1 ms: 1.05x faster                                                 |
| bpe_tokeniser              | 4.69 sec                                               | 4.47 sec: 1.05x faster                                                |
| telco                      | 8.45 ms                                                | 8.06 ms: 1.05x faster                                                 |
| regex_v8                   | 25.3 ms                                                | 24.1 ms: 1.05x faster                                                 |
| sqlite_synth               | 2.85 us                                                | 2.73 us: 1.05x faster                                                 |
| async_tree_none_tg         | 320 ms                                                 | 308 ms: 1.04x faster                                                  |
| pyflate                    | 460 ms                                                 | 443 ms: 1.04x faster                                                  |
| json_dumps                 | 10.4 ms                                                | 10.1 ms: 1.03x faster                                                 |
| json                       | 5.20 ms                                                | 5.04 ms: 1.03x faster                                                 |
| scimark_sor                | 122 ms                                                 | 119 ms: 1.03x faster                                                  |
| html5lib                   | 64.5 ms                                                | 62.7 ms: 1.03x faster                                                 |
| xml_etree_iterparse        | 102 ms                                                 | 99.3 ms: 1.03x faster                                                 |
| pprint_safe_repr           | 744 ms                                                 | 726 ms: 1.03x faster                                                  |
| scimark_lu                 | 115 ms                                                 | 112 ms: 1.02x faster                                                  |
| regex_dna                  | 220 ms                                                 | 215 ms: 1.02x faster                                                  |
| pycparser                  | 1.19 sec                                               | 1.17 sec: 1.02x faster                                                |
| meteor_contest             | 108 ms                                                 | 106 ms: 1.02x faster                                                  |
| thrift                     | 796 us                                                 | 786 us: 1.01x faster                                                  |
| pickle                     | 11.6 us                                                | 11.4 us: 1.01x faster                                                 |
| json_loads                 | 27.0 us                                                | 26.7 us: 1.01x faster                                                 |
| python_startup             | 10.6 ms                                                | 10.5 ms: 1.00x faster                                                 |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                                  |
| pickle_list                | 5.01 us                                                | 5.04 us: 1.01x slower                                                 |
| coverage                   | 83.7 ms                                                | 84.4 ms: 1.01x slower                                                 |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.01x slower                                                |
| asyncio_tcp                | 488 ms                                                 | 494 ms: 1.01x slower                                                  |
| python_startup_no_site     | 6.99 ms                                                | 7.06 ms: 1.01x slower                                                 |
| logging_silent             | 102 ns                                                 | 103 ns: 1.01x slower                                                  |
| unpickle_pure_python       | 213 us                                                 | 216 us: 1.01x slower                                                  |
| pprint_pformat             | 1.51 sec                                               | 1.53 sec: 1.01x slower                                                |
| typing_runtime_protocols   | 159 us                                                 | 162 us: 1.02x slower                                                  |
| chaos                      | 58.4 ms                                                | 59.4 ms: 1.02x slower                                                 |
| async_tree_io              | 843 ms                                                 | 862 ms: 1.02x slower                                                  |
| comprehensions             | 16.4 us                                                | 16.8 us: 1.02x slower                                                 |
| pickle_pure_python         | 300 us                                                 | 308 us: 1.02x slower                                                  |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 557 ms: 1.03x slower                                                  |
| gc_traversal               | 3.81 ms                                                | 3.91 ms: 1.03x slower                                                 |
| bench_thread_pool          | 815 us                                                 | 839 us: 1.03x slower                                                  |
| tornado_http               | 91.5 ms                                                | 94.9 ms: 1.04x slower                                                 |
| deltablue                  | 3.15 ms                                                | 3.27 ms: 1.04x slower                                                 |
| 2to3                       | 265 ms                                                 | 278 ms: 1.05x slower                                                  |
| async_generators           | 433 ms                                                 | 457 ms: 1.06x slower                                                  |
| sqlglot_normalize          | 107 ms                                                 | 114 ms: 1.06x slower                                                  |
| django_template            | 34.4 ms                                                | 36.4 ms: 1.06x slower                                                 |
| async_tree_io_tg           | 825 ms                                                 | 874 ms: 1.06x slower                                                  |
| raytrace                   | 262 ms                                                 | 279 ms: 1.06x slower                                                  |
| nqueens                    | 80.6 ms                                                | 86.1 ms: 1.07x slower                                                 |
| sqlglot_parse              | 1.27 ms                                                | 1.35 ms: 1.07x slower                                                 |
| unpickle_list              | 4.96 us                                                | 5.31 us: 1.07x slower                                                 |
| sqlglot_optimize           | 53.9 ms                                                | 58.2 ms: 1.08x slower                                                 |
| regex_compile              | 131 ms                                                 | 142 ms: 1.08x slower                                                  |
| sqlglot_transpile          | 1.57 ms                                                | 1.71 ms: 1.08x slower                                                 |
| genshi_text                | 22.9 ms                                                | 24.9 ms: 1.09x slower                                                 |
| dulwich_log                | 63.0 ms                                                | 68.5 ms: 1.09x slower                                                 |
| sympy_str                  | 274 ms                                                 | 299 ms: 1.09x slower                                                  |
| sympy_expand               | 462 ms                                                 | 505 ms: 1.09x slower                                                  |
| create_gc_cycles           | 1.61 ms                                                | 1.76 ms: 1.09x slower                                                 |
| hexiom                     | 6.13 ms                                                | 7.00 ms: 1.14x slower                                                 |
| sympy_integrate            | 19.9 ms                                                | 22.7 ms: 1.14x slower                                                 |
| generators                 | 28.8 ms                                                | 33.0 ms: 1.14x slower                                                 |
| docutils                   | 2.58 sec                                               | 2.96 sec: 1.15x slower                                                |
| sympy_sum                  | 150 ms                                                 | 172 ms: 1.15x slower                                                  |
| genshi_xml                 | 50.3 ms                                                | 60.0 ms: 1.19x slower                                                 |
| pylint                     | 313 ms                                                 | 374 ms: 1.20x slower                                                  |
| unpack_sequence            | 42.4 ns                                                | 112 ns: 2.65x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.00x slower                                                          |

Benchmark hidden because not significant (9): fannkuch, asyncio_websockets, bench_mp_pool, unpickle, async_tree_cpu_io_mixed, pickle_dict, logging_format, logging_simple, coroutines
Ignored benchmarks (7) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 79.41% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.09x