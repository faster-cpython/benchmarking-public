# Results vs. 3.13.0

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: b9e10d1
- commit date: 2024-08-19
- overall geometric mean: 1.01x faster
- HPT reliability: 53.08%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240819-linux-x86_64-python-main-3.14.0a0-b9e10d1 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| 2to3           | 265 ms                                                 | 260 ms: 1.02x faster                                  |
| docutils       | 2.58 sec                                               | 2.70 sec: 1.05x slower                                |
| html5lib       | 64.5 ms                                                | 65.0 ms: 1.01x slower                                 |
| tornado_http   | 91.5 ms                                                | 90.2 ms: 1.01x faster                                 |
| Geometric mean | (ref)                                                  | 1.00x slower                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240819-linux-x86_64-python-main-3.14.0a0-b9e10d1 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| async_tree_memoization_tg  | 465 ms                                                 | 393 ms: 1.18x faster                                  |
| async_tree_none            | 354 ms                                                 | 323 ms: 1.10x faster                                  |
| async_tree_none_tg         | 320 ms                                                 | 302 ms: 1.06x faster                                  |
| async_tree_memoization     | 442 ms                                                 | 423 ms: 1.05x faster                                  |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 535 ms: 1.02x faster                                  |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 566 ms: 1.01x faster                                  |
| asyncio_tcp                | 488 ms                                                 | 483 ms: 1.01x faster                                  |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.78 sec: 1.00x faster                                |
| asyncio_websockets         | 555 ms                                                 | 558 ms: 1.01x slower                                  |
| async_generators           | 433 ms                                                 | 437 ms: 1.01x slower                                  |
| async_tree_io              | 843 ms                                                 | 901 ms: 1.07x slower                                  |
| async_tree_io_tg           | 825 ms                                                 | 890 ms: 1.08x slower                                  |
| coroutines                 | 22.5 ms                                                | 24.7 ms: 1.10x slower                                 |
| Geometric mean             | (ref)                                                  | 1.01x faster                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240819-linux-x86_64-python-main-3.14.0a0-b9e10d1 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| pidigits       | 186 ms                                                 | 188 ms: 1.01x slower                                  |
| nbody          | 85.7 ms                                                | 86.9 ms: 1.01x slower                                 |
| Geometric mean | (ref)                                                  | 1.01x slower                                          |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240819-linux-x86_64-python-main-3.14.0a0-b9e10d1 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.59 ms: 1.08x faster                                 |
| regex_v8       | 25.3 ms                                                | 24.5 ms: 1.03x faster                                 |
| regex_compile  | 131 ms                                                 | 130 ms: 1.01x faster                                  |
| Geometric mean | (ref)                                                  | 1.03x faster                                          |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240819-linux-x86_64-python-main-3.14.0a0-b9e10d1 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| xml_etree_process    | 60.4 ms                                                | 58.6 ms: 1.03x faster                                 |
| xml_etree_generate   | 87.0 ms                                                | 84.8 ms: 1.03x faster                                 |
| tomli_loads          | 2.11 sec                                               | 2.08 sec: 1.02x faster                                |
| unpickle_pure_python | 213 us                                                 | 212 us: 1.00x faster                                  |
| json_dumps           | 10.4 ms                                                | 10.5 ms: 1.01x slower                                 |
| pickle_pure_python   | 300 us                                                 | 304 us: 1.01x slower                                  |
| xml_etree_iterparse  | 102 ms                                                 | 105 ms: 1.03x slower                                  |
| json_loads           | 27.0 us                                                | 28.6 us: 1.06x slower                                 |
| Geometric mean       | (ref)                                                  | 1.00x slower                                          |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240819-linux-x86_64-python-main-3.14.0a0-b9e10d1 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.5 ms: 1.00x faster                                 |
| python_startup_no_site | 6.99 ms                                                | 7.08 ms: 1.01x slower                                 |
| Geometric mean         | (ref)                                                  | 1.00x slower                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240819-linux-x86_64-python-main-3.14.0a0-b9e10d1 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| django_template | 34.4 ms                                                | 34.0 ms: 1.01x faster                                 |
| genshi_xml      | 50.3 ms                                                | 50.0 ms: 1.01x faster                                 |
| mako            | 11.1 ms                                                | 11.3 ms: 1.01x slower                                 |
| Geometric mean  | (ref)                                                  | 1.00x faster                                          |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240819-linux-x86_64-python-main-3.14.0a0-b9e10d1 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| deepcopy                   | 352 us                                                 | 260 us: 1.36x faster                                  |
| deepcopy_memo              | 38.0 us                                                | 29.9 us: 1.27x faster                                 |
| deepcopy_reduce            | 3.17 us                                                | 2.65 us: 1.20x faster                                 |
| async_tree_memoization_tg  | 465 ms                                                 | 393 ms: 1.18x faster                                  |
| async_tree_none            | 354 ms                                                 | 323 ms: 1.10x faster                                  |
| regex_effbot               | 3.88 ms                                                | 3.59 ms: 1.08x faster                                 |
| pathlib                    | 17.1 ms                                                | 15.8 ms: 1.08x faster                                 |
| async_tree_none_tg         | 320 ms                                                 | 302 ms: 1.06x faster                                  |
| pycparser                  | 1.19 sec                                               | 1.13 sec: 1.06x faster                                |
| richards                   | 48.1 ms                                                | 45.6 ms: 1.05x faster                                 |
| richards_super             | 54.4 ms                                                | 51.7 ms: 1.05x faster                                 |
| telco                      | 8.45 ms                                                | 8.05 ms: 1.05x faster                                 |
| logging_simple             | 5.66 us                                                | 5.42 us: 1.05x faster                                 |
| async_tree_memoization     | 442 ms                                                 | 423 ms: 1.05x faster                                  |
| bench_thread_pool          | 815 us                                                 | 784 us: 1.04x faster                                  |
| generators                 | 28.8 ms                                                | 27.8 ms: 1.04x faster                                 |
| logging_format             | 6.25 us                                                | 6.03 us: 1.04x faster                                 |
| regex_v8                   | 25.3 ms                                                | 24.5 ms: 1.03x faster                                 |
| xml_etree_process          | 60.4 ms                                                | 58.6 ms: 1.03x faster                                 |
| xml_etree_generate         | 87.0 ms                                                | 84.8 ms: 1.03x faster                                 |
| raytrace                   | 262 ms                                                 | 255 ms: 1.02x faster                                  |
| thrift                     | 796 us                                                 | 778 us: 1.02x faster                                  |
| gc_traversal               | 3.81 ms                                                | 3.72 ms: 1.02x faster                                 |
| 2to3                       | 265 ms                                                 | 260 ms: 1.02x faster                                  |
| tomli_loads                | 2.11 sec                                               | 2.08 sec: 1.02x faster                                |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 535 ms: 1.02x faster                                  |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 566 ms: 1.01x faster                                  |
| tornado_http               | 91.5 ms                                                | 90.2 ms: 1.01x faster                                 |
| django_template            | 34.4 ms                                                | 34.0 ms: 1.01x faster                                 |
| logging_silent             | 102 ns                                                 | 101 ns: 1.01x faster                                  |
| asyncio_tcp                | 488 ms                                                 | 483 ms: 1.01x faster                                  |
| regex_compile              | 131 ms                                                 | 130 ms: 1.01x faster                                  |
| scimark_fft                | 369 ms                                                 | 365 ms: 1.01x faster                                  |
| nqueens                    | 80.6 ms                                                | 79.9 ms: 1.01x faster                                 |
| scimark_lu                 | 115 ms                                                 | 114 ms: 1.01x faster                                  |
| meteor_contest             | 108 ms                                                 | 107 ms: 1.01x faster                                  |
| deltablue                  | 3.15 ms                                                | 3.12 ms: 1.01x faster                                 |
| genshi_xml                 | 50.3 ms                                                | 50.0 ms: 1.01x faster                                 |
| pprint_safe_repr           | 744 ms                                                 | 739 ms: 1.01x faster                                  |
| sqlglot_optimize           | 53.9 ms                                                | 53.6 ms: 1.01x faster                                 |
| spectral_norm              | 115 ms                                                 | 114 ms: 1.00x faster                                  |
| unpickle_pure_python       | 213 us                                                 | 212 us: 1.00x faster                                  |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.78 sec: 1.00x faster                                |
| python_startup             | 10.6 ms                                                | 10.5 ms: 1.00x faster                                 |
| sqlglot_normalize          | 107 ms                                                 | 108 ms: 1.00x slower                                  |
| asyncio_websockets         | 555 ms                                                 | 558 ms: 1.01x slower                                  |
| html5lib                   | 64.5 ms                                                | 65.0 ms: 1.01x slower                                 |
| json_dumps                 | 10.4 ms                                                | 10.5 ms: 1.01x slower                                 |
| pidigits                   | 186 ms                                                 | 188 ms: 1.01x slower                                  |
| pprint_pformat             | 1.51 sec                                               | 1.52 sec: 1.01x slower                                |
| async_generators           | 433 ms                                                 | 437 ms: 1.01x slower                                  |
| chaos                      | 58.4 ms                                                | 58.9 ms: 1.01x slower                                 |
| pickle_pure_python         | 300 us                                                 | 304 us: 1.01x slower                                  |
| python_startup_no_site     | 6.99 ms                                                | 7.08 ms: 1.01x slower                                 |
| mako                       | 11.1 ms                                                | 11.3 ms: 1.01x slower                                 |
| nbody                      | 85.7 ms                                                | 86.9 ms: 1.01x slower                                 |
| sympy_sum                  | 150 ms                                                 | 152 ms: 1.01x slower                                  |
| crypto_pyaes               | 73.0 ms                                                | 74.0 ms: 1.01x slower                                 |
| sqlglot_parse              | 1.27 ms                                                | 1.28 ms: 1.01x slower                                 |
| hexiom                     | 6.13 ms                                                | 6.23 ms: 1.02x slower                                 |
| coverage                   | 83.7 ms                                                | 85.2 ms: 1.02x slower                                 |
| comprehensions             | 16.4 us                                                | 16.7 us: 1.02x slower                                 |
| json                       | 5.20 ms                                                | 5.32 ms: 1.02x slower                                 |
| scimark_monte_carlo        | 66.3 ms                                                | 67.8 ms: 1.02x slower                                 |
| typing_runtime_protocols   | 159 us                                                 | 164 us: 1.03x slower                                  |
| xml_etree_iterparse        | 102 ms                                                 | 105 ms: 1.03x slower                                  |
| scimark_sor                | 122 ms                                                 | 126 ms: 1.03x slower                                  |
| pyflate                    | 460 ms                                                 | 477 ms: 1.04x slower                                  |
| docutils                   | 2.58 sec                                               | 2.70 sec: 1.05x slower                                |
| bpe_tokeniser              | 4.69 sec                                               | 4.94 sec: 1.05x slower                                |
| json_loads                 | 27.0 us                                                | 28.6 us: 1.06x slower                                 |
| async_tree_io              | 843 ms                                                 | 901 ms: 1.07x slower                                  |
| async_tree_io_tg           | 825 ms                                                 | 890 ms: 1.08x slower                                  |
| create_gc_cycles           | 1.61 ms                                                | 1.74 ms: 1.08x slower                                 |
| coroutines                 | 22.5 ms                                                | 24.7 ms: 1.10x slower                                 |
| fannkuch                   | 381 ms                                                 | 420 ms: 1.10x slower                                  |
| Geometric mean             | (ref)                                                  | 1.01x faster                                          |

Benchmark hidden because not significant (13): go, genshi_text, sympy_integrate, sympy_expand, mdp, regex_dna, sympy_str, bench_mp_pool, sqlglot_transpile, scimark_sparse_mat_mult, float, xml_etree_parse, pylint
Ignored benchmarks (15) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 53.08% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x