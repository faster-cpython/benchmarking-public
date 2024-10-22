# Results vs. 3.13.0

- fork: python
- ref: d9efa45d7457b0dfea46
- machine: linux-x86_64
- commit hash: d9efa45
- commit date: 2024-07-25
- overall geometric mean: 1.01x faster
- HPT reliability: 94.48%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240725-linux-x86_64-python-d9efa45d7457b0dfea46-3.14.0a0-d9efa45 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 263 ms: 1.01x faster                                                  |
| docutils       | 2.58 sec                                               | 2.72 sec: 1.05x slower                                                |
| html5lib       | 64.5 ms                                                | 63.9 ms: 1.01x faster                                                 |
| tornado_http   | 91.5 ms                                                | 89.9 ms: 1.02x faster                                                 |
| Geometric mean | (ref)                                                  | 1.00x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240725-linux-x86_64-python-d9efa45d7457b0dfea46-3.14.0a0-d9efa45 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg  | 465 ms                                                 | 390 ms: 1.19x faster                                                  |
| async_tree_memoization     | 442 ms                                                 | 399 ms: 1.11x faster                                                  |
| async_tree_none            | 354 ms                                                 | 324 ms: 1.09x faster                                                  |
| async_tree_none_tg         | 320 ms                                                 | 298 ms: 1.07x faster                                                  |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 527 ms: 1.03x faster                                                  |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 560 ms: 1.03x faster                                                  |
| asyncio_tcp                | 488 ms                                                 | 482 ms: 1.01x faster                                                  |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.79 sec: 1.00x slower                                                |
| asyncio_websockets         | 555 ms                                                 | 558 ms: 1.00x slower                                                  |
| coroutines                 | 22.5 ms                                                | 23.0 ms: 1.02x slower                                                 |
| async_tree_io_tg           | 825 ms                                                 | 863 ms: 1.05x slower                                                  |
| async_tree_io              | 843 ms                                                 | 904 ms: 1.07x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                          |

Benchmark hidden because not significant (1): async_generators

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240725-linux-x86_64-python-d9efa45d7457b0dfea46-3.14.0a0-d9efa45 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 78.0 ms: 1.01x faster                                                 |
| nbody          | 85.7 ms                                                | 88.5 ms: 1.03x slower                                                 |
| Geometric mean | (ref)                                                  | 1.01x slower                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240725-linux-x86_64-python-d9efa45d7457b0dfea46-3.14.0a0-d9efa45 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_v8       | 25.3 ms                                                | 24.4 ms: 1.04x faster                                                 |
| regex_effbot   | 3.88 ms                                                | 3.78 ms: 1.03x faster                                                 |
| regex_dna      | 220 ms                                                 | 221 ms: 1.00x slower                                                  |
| Geometric mean | (ref)                                                  | 1.01x faster                                                          |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240725-linux-x86_64-python-d9efa45d7457b0dfea46-3.14.0a0-d9efa45 |
|---------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads         | 2.11 sec                                               | 2.04 sec: 1.03x faster                                                |
| xml_etree_process   | 60.4 ms                                                | 59.0 ms: 1.02x faster                                                 |
| xml_etree_generate  | 87.0 ms                                                | 85.3 ms: 1.02x faster                                                 |
| json_loads          | 27.0 us                                                | 27.7 us: 1.03x slower                                                 |
| xml_etree_iterparse | 102 ms                                                 | 105 ms: 1.03x slower                                                  |
| Geometric mean      | (ref)                                                  | 1.00x faster                                                          |

Benchmark hidden because not significant (4): xml_etree_parse, json_dumps, unpickle_pure_python, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240725-linux-x86_64-python-d9efa45d7457b0dfea46-3.14.0a0-d9efa45 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.5 ms: 1.00x faster                                                 |
| python_startup_no_site | 6.99 ms                                                | 7.07 ms: 1.01x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.00x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240725-linux-x86_64-python-d9efa45d7457b0dfea46-3.14.0a0-d9efa45 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| django_template | 34.4 ms                                                | 34.1 ms: 1.01x faster                                                 |
| mako            | 11.1 ms                                                | 11.2 ms: 1.01x slower                                                 |
| genshi_xml      | 50.3 ms                                                | 51.6 ms: 1.03x slower                                                 |
| genshi_text     | 22.9 ms                                                | 23.8 ms: 1.04x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.02x slower                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240725-linux-x86_64-python-d9efa45d7457b0dfea46-3.14.0a0-d9efa45 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy                   | 352 us                                                 | 262 us: 1.35x faster                                                  |
| deepcopy_memo              | 38.0 us                                                | 29.9 us: 1.27x faster                                                 |
| deepcopy_reduce            | 3.17 us                                                | 2.62 us: 1.21x faster                                                 |
| async_tree_memoization_tg  | 465 ms                                                 | 390 ms: 1.19x faster                                                  |
| async_tree_memoization     | 442 ms                                                 | 399 ms: 1.11x faster                                                  |
| async_tree_none            | 354 ms                                                 | 324 ms: 1.09x faster                                                  |
| mdp                        | 2.74 sec                                               | 2.52 sec: 1.09x faster                                                |
| pathlib                    | 17.1 ms                                                | 15.9 ms: 1.07x faster                                                 |
| async_tree_none_tg         | 320 ms                                                 | 298 ms: 1.07x faster                                                  |
| richards                   | 48.1 ms                                                | 45.1 ms: 1.07x faster                                                 |
| richards_super             | 54.4 ms                                                | 51.2 ms: 1.06x faster                                                 |
| bench_thread_pool          | 815 us                                                 | 784 us: 1.04x faster                                                  |
| logging_simple             | 5.66 us                                                | 5.45 us: 1.04x faster                                                 |
| regex_v8                   | 25.3 ms                                                | 24.4 ms: 1.04x faster                                                 |
| telco                      | 8.45 ms                                                | 8.16 ms: 1.04x faster                                                 |
| tomli_loads                | 2.11 sec                                               | 2.04 sec: 1.03x faster                                                |
| spectral_norm              | 115 ms                                                 | 111 ms: 1.03x faster                                                  |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 527 ms: 1.03x faster                                                  |
| logging_format             | 6.25 us                                                | 6.07 us: 1.03x faster                                                 |
| thrift                     | 796 us                                                 | 773 us: 1.03x faster                                                  |
| regex_effbot               | 3.88 ms                                                | 3.78 ms: 1.03x faster                                                 |
| pycparser                  | 1.19 sec                                               | 1.16 sec: 1.03x faster                                                |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 560 ms: 1.03x faster                                                  |
| logging_silent             | 102 ns                                                 | 99.6 ns: 1.02x faster                                                 |
| generators                 | 28.8 ms                                                | 28.1 ms: 1.02x faster                                                 |
| xml_etree_process          | 60.4 ms                                                | 59.0 ms: 1.02x faster                                                 |
| gc_traversal               | 3.81 ms                                                | 3.72 ms: 1.02x faster                                                 |
| scimark_lu                 | 115 ms                                                 | 113 ms: 1.02x faster                                                  |
| xml_etree_generate         | 87.0 ms                                                | 85.3 ms: 1.02x faster                                                 |
| tornado_http               | 91.5 ms                                                | 89.9 ms: 1.02x faster                                                 |
| raytrace                   | 262 ms                                                 | 257 ms: 1.02x faster                                                  |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.94 ms: 1.02x faster                                                 |
| asyncio_tcp                | 488 ms                                                 | 482 ms: 1.01x faster                                                  |
| json                       | 5.20 ms                                                | 5.13 ms: 1.01x faster                                                 |
| crypto_pyaes               | 73.0 ms                                                | 72.1 ms: 1.01x faster                                                 |
| nqueens                    | 80.6 ms                                                | 79.7 ms: 1.01x faster                                                 |
| go                         | 142 ms                                                 | 140 ms: 1.01x faster                                                  |
| html5lib                   | 64.5 ms                                                | 63.9 ms: 1.01x faster                                                 |
| sympy_integrate            | 19.9 ms                                                | 19.7 ms: 1.01x faster                                                 |
| 2to3                       | 265 ms                                                 | 263 ms: 1.01x faster                                                  |
| django_template            | 34.4 ms                                                | 34.1 ms: 1.01x faster                                                 |
| pprint_safe_repr           | 744 ms                                                 | 739 ms: 1.01x faster                                                  |
| sqlglot_optimize           | 53.9 ms                                                | 53.6 ms: 1.01x faster                                                 |
| float                      | 78.5 ms                                                | 78.0 ms: 1.01x faster                                                 |
| sqlglot_transpile          | 1.57 ms                                                | 1.57 ms: 1.01x faster                                                 |
| python_startup             | 10.6 ms                                                | 10.5 ms: 1.00x faster                                                 |
| meteor_contest             | 108 ms                                                 | 107 ms: 1.00x faster                                                  |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.79 sec: 1.00x slower                                                |
| regex_dna                  | 220 ms                                                 | 221 ms: 1.00x slower                                                  |
| asyncio_websockets         | 555 ms                                                 | 558 ms: 1.00x slower                                                  |
| sympy_sum                  | 150 ms                                                 | 150 ms: 1.01x slower                                                  |
| sqlglot_parse              | 1.27 ms                                                | 1.27 ms: 1.01x slower                                                 |
| deltablue                  | 3.15 ms                                                | 3.17 ms: 1.01x slower                                                 |
| mako                       | 11.1 ms                                                | 11.2 ms: 1.01x slower                                                 |
| python_startup_no_site     | 6.99 ms                                                | 7.07 ms: 1.01x slower                                                 |
| hexiom                     | 6.13 ms                                                | 6.21 ms: 1.01x slower                                                 |
| typing_runtime_protocols   | 159 us                                                 | 162 us: 1.02x slower                                                  |
| coroutines                 | 22.5 ms                                                | 23.0 ms: 1.02x slower                                                 |
| scimark_monte_carlo        | 66.3 ms                                                | 67.7 ms: 1.02x slower                                                 |
| genshi_xml                 | 50.3 ms                                                | 51.6 ms: 1.03x slower                                                 |
| json_loads                 | 27.0 us                                                | 27.7 us: 1.03x slower                                                 |
| xml_etree_iterparse        | 102 ms                                                 | 105 ms: 1.03x slower                                                  |
| nbody                      | 85.7 ms                                                | 88.5 ms: 1.03x slower                                                 |
| bpe_tokeniser              | 4.69 sec                                               | 4.85 sec: 1.03x slower                                                |
| genshi_text                | 22.9 ms                                                | 23.8 ms: 1.04x slower                                                 |
| scimark_sor                | 122 ms                                                 | 127 ms: 1.04x slower                                                  |
| async_tree_io_tg           | 825 ms                                                 | 863 ms: 1.05x slower                                                  |
| dask                       | 338 ms                                                 | 354 ms: 1.05x slower                                                  |
| pyflate                    | 460 ms                                                 | 483 ms: 1.05x slower                                                  |
| docutils                   | 2.58 sec                                               | 2.72 sec: 1.05x slower                                                |
| fannkuch                   | 381 ms                                                 | 406 ms: 1.07x slower                                                  |
| async_tree_io              | 843 ms                                                 | 904 ms: 1.07x slower                                                  |
| create_gc_cycles           | 1.61 ms                                                | 1.74 ms: 1.08x slower                                                 |
| coverage                   | 83.7 ms                                                | 92.6 ms: 1.11x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                          |

Benchmark hidden because not significant (16): sympy_str, scimark_fft, xml_etree_parse, async_generators, comprehensions, bench_mp_pool, pidigits, chaos, sympy_expand, json_dumps, unpickle_pure_python, sqlglot_normalize, pprint_pformat, regex_compile, pickle_pure_python, pylint
Ignored benchmarks (14) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 94.48% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x