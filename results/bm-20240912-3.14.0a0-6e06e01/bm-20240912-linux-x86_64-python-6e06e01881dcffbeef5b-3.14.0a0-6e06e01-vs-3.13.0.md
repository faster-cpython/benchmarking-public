# Results vs. 3.13.0

- fork: python
- ref: 6e06e01881dcffbeef5b
- machine: linux-x86_64
- commit hash: 6e06e01
- commit date: 2024-09-12
- overall geometric mean: 1.02x faster
- HPT reliability: 99.81%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 253 ms: 1.05x faster                                                  |
| docutils       | 2.58 sec                                               | 2.66 sec: 1.03x slower                                                |
| html5lib       | 64.5 ms                                                | 62.4 ms: 1.03x faster                                                 |
| tornado_http   | 91.5 ms                                                | 89.9 ms: 1.02x faster                                                 |
| Geometric mean | (ref)                                                  | 1.02x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg  | 465 ms                                                 | 391 ms: 1.19x faster                                                  |
| async_tree_none            | 354 ms                                                 | 315 ms: 1.13x faster                                                  |
| async_tree_memoization     | 442 ms                                                 | 395 ms: 1.12x faster                                                  |
| asyncio_tcp                | 488 ms                                                 | 471 ms: 1.04x faster                                                  |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.78 sec: 1.01x faster                                                |
| asyncio_websockets         | 555 ms                                                 | 559 ms: 1.01x slower                                                  |
| async_generators           | 433 ms                                                 | 437 ms: 1.01x slower                                                  |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 558 ms: 1.03x slower                                                  |
| coroutines                 | 22.5 ms                                                | 23.2 ms: 1.03x slower                                                 |
| async_tree_io              | 843 ms                                                 | 873 ms: 1.04x slower                                                  |
| async_tree_io_tg           | 825 ms                                                 | 875 ms: 1.06x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                          |

Benchmark hidden because not significant (2): async_tree_none_tg, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 76.7 ms: 1.02x faster                                                 |
| pidigits       | 186 ms                                                 | 187 ms: 1.00x slower                                                  |
| nbody          | 85.7 ms                                                | 89.5 ms: 1.04x slower                                                 |
| Geometric mean | (ref)                                                  | 1.01x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.65 ms: 1.06x faster                                                 |
| regex_v8       | 25.3 ms                                                | 24.6 ms: 1.03x faster                                                 |
| regex_compile  | 131 ms                                                 | 129 ms: 1.02x faster                                                  |
| regex_dna      | 220 ms                                                 | 216 ms: 1.02x faster                                                  |
| Geometric mean | (ref)                                                  | 1.03x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|---------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads         | 2.11 sec                                               | 2.04 sec: 1.03x faster                                                |
| pickle_list         | 5.01 us                                                | 4.87 us: 1.03x faster                                                 |
| xml_etree_process   | 60.4 ms                                                | 59.0 ms: 1.02x faster                                                 |
| xml_etree_generate  | 87.0 ms                                                | 85.4 ms: 1.02x faster                                                 |
| pickle              | 11.6 us                                                | 11.4 us: 1.01x faster                                                 |
| json_dumps          | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                 |
| pickle_pure_python  | 300 us                                                 | 302 us: 1.01x slower                                                  |
| pickle_dict         | 33.2 us                                                | 33.8 us: 1.02x slower                                                 |
| xml_etree_iterparse | 102 ms                                                 | 105 ms: 1.03x slower                                                  |
| unpickle_list       | 4.96 us                                                | 5.36 us: 1.08x slower                                                 |
| Geometric mean      | (ref)                                                  | 1.00x slower                                                          |

Benchmark hidden because not significant (4): xml_etree_parse, json_loads, unpickle_pure_python, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.5 ms: 1.01x faster                                                 |
| python_startup_no_site | 6.99 ms                                                | 6.99 ms: 1.00x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.00x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 22.9 ms                                                | 21.7 ms: 1.06x faster                                                 |
| genshi_xml      | 50.3 ms                                                | 48.6 ms: 1.04x faster                                                 |
| django_template | 34.4 ms                                                | 34.6 ms: 1.00x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.02x faster                                                          |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy                   | 352 us                                                 | 255 us: 1.38x faster                                                  |
| deepcopy_memo              | 38.0 us                                                | 29.5 us: 1.29x faster                                                 |
| go                         | 142 ms                                                 | 117 ms: 1.21x faster                                                  |
| deepcopy_reduce            | 3.17 us                                                | 2.63 us: 1.20x faster                                                 |
| async_tree_memoization_tg  | 465 ms                                                 | 391 ms: 1.19x faster                                                  |
| async_tree_none            | 354 ms                                                 | 315 ms: 1.13x faster                                                  |
| async_tree_memoization     | 442 ms                                                 | 395 ms: 1.12x faster                                                  |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.60 ms: 1.09x faster                                                 |
| pathlib                    | 17.1 ms                                                | 15.9 ms: 1.08x faster                                                 |
| regex_effbot               | 3.88 ms                                                | 3.65 ms: 1.06x faster                                                 |
| pycparser                  | 1.19 sec                                               | 1.12 sec: 1.06x faster                                                |
| genshi_text                | 22.9 ms                                                | 21.7 ms: 1.06x faster                                                 |
| richards_super             | 54.4 ms                                                | 51.7 ms: 1.05x faster                                                 |
| richards                   | 48.1 ms                                                | 45.8 ms: 1.05x faster                                                 |
| 2to3                       | 265 ms                                                 | 253 ms: 1.05x faster                                                  |
| pprint_safe_repr           | 744 ms                                                 | 714 ms: 1.04x faster                                                  |
| asyncio_tcp                | 488 ms                                                 | 471 ms: 1.04x faster                                                  |
| bench_thread_pool          | 815 us                                                 | 787 us: 1.04x faster                                                  |
| genshi_xml                 | 50.3 ms                                                | 48.6 ms: 1.04x faster                                                 |
| html5lib                   | 64.5 ms                                                | 62.4 ms: 1.03x faster                                                 |
| tomli_loads                | 2.11 sec                                               | 2.04 sec: 1.03x faster                                                |
| logging_simple             | 5.66 us                                                | 5.49 us: 1.03x faster                                                 |
| pprint_pformat             | 1.51 sec                                               | 1.47 sec: 1.03x faster                                                |
| pickle_list                | 5.01 us                                                | 4.87 us: 1.03x faster                                                 |
| crypto_pyaes               | 73.0 ms                                                | 71.1 ms: 1.03x faster                                                 |
| regex_v8                   | 25.3 ms                                                | 24.6 ms: 1.03x faster                                                 |
| sympy_str                  | 274 ms                                                 | 267 ms: 1.02x faster                                                  |
| float                      | 78.5 ms                                                | 76.7 ms: 1.02x faster                                                 |
| xml_etree_process          | 60.4 ms                                                | 59.0 ms: 1.02x faster                                                 |
| thrift                     | 796 us                                                 | 779 us: 1.02x faster                                                  |
| logging_silent             | 102 ns                                                 | 99.9 ns: 1.02x faster                                                 |
| generators                 | 28.8 ms                                                | 28.2 ms: 1.02x faster                                                 |
| logging_format             | 6.25 us                                                | 6.12 us: 1.02x faster                                                 |
| regex_compile              | 131 ms                                                 | 129 ms: 1.02x faster                                                  |
| spectral_norm              | 115 ms                                                 | 113 ms: 1.02x faster                                                  |
| sympy_integrate            | 19.9 ms                                                | 19.5 ms: 1.02x faster                                                 |
| sympy_sum                  | 150 ms                                                 | 147 ms: 1.02x faster                                                  |
| mdp                        | 2.74 sec                                               | 2.69 sec: 1.02x faster                                                |
| xml_etree_generate         | 87.0 ms                                                | 85.4 ms: 1.02x faster                                                 |
| scimark_lu                 | 115 ms                                                 | 113 ms: 1.02x faster                                                  |
| tornado_http               | 91.5 ms                                                | 89.9 ms: 1.02x faster                                                 |
| regex_dna                  | 220 ms                                                 | 216 ms: 1.02x faster                                                  |
| scimark_fft                | 369 ms                                                 | 363 ms: 1.02x faster                                                  |
| sqlglot_optimize           | 53.9 ms                                                | 53.2 ms: 1.01x faster                                                 |
| sympy_expand               | 462 ms                                                 | 456 ms: 1.01x faster                                                  |
| pickle                     | 11.6 us                                                | 11.4 us: 1.01x faster                                                 |
| json_dumps                 | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                 |
| python_startup             | 10.6 ms                                                | 10.5 ms: 1.01x faster                                                 |
| sqlite_synth               | 2.85 us                                                | 2.83 us: 1.01x faster                                                 |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.78 sec: 1.01x faster                                                |
| scimark_sor                | 122 ms                                                 | 122 ms: 1.00x faster                                                  |
| deltablue                  | 3.15 ms                                                | 3.14 ms: 1.00x faster                                                 |
| python_startup_no_site     | 6.99 ms                                                | 6.99 ms: 1.00x slower                                                 |
| sqlglot_transpile          | 1.57 ms                                                | 1.58 ms: 1.00x slower                                                 |
| pidigits                   | 186 ms                                                 | 187 ms: 1.00x slower                                                  |
| django_template            | 34.4 ms                                                | 34.6 ms: 1.00x slower                                                 |
| sqlglot_normalize          | 107 ms                                                 | 108 ms: 1.00x slower                                                  |
| pickle_pure_python         | 300 us                                                 | 302 us: 1.01x slower                                                  |
| hexiom                     | 6.13 ms                                                | 6.16 ms: 1.01x slower                                                 |
| asyncio_websockets         | 555 ms                                                 | 559 ms: 1.01x slower                                                  |
| async_generators           | 433 ms                                                 | 437 ms: 1.01x slower                                                  |
| scimark_monte_carlo        | 66.3 ms                                                | 67.1 ms: 1.01x slower                                                 |
| sqlglot_parse              | 1.27 ms                                                | 1.28 ms: 1.01x slower                                                 |
| pickle_dict                | 33.2 us                                                | 33.8 us: 1.02x slower                                                 |
| coverage                   | 83.7 ms                                                | 85.7 ms: 1.02x slower                                                 |
| dulwich_log                | 63.0 ms                                                | 64.5 ms: 1.02x slower                                                 |
| gc_traversal               | 3.81 ms                                                | 3.90 ms: 1.03x slower                                                 |
| comprehensions             | 16.4 us                                                | 16.8 us: 1.03x slower                                                 |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 558 ms: 1.03x slower                                                  |
| xml_etree_iterparse        | 102 ms                                                 | 105 ms: 1.03x slower                                                  |
| coroutines                 | 22.5 ms                                                | 23.2 ms: 1.03x slower                                                 |
| docutils                   | 2.58 sec                                               | 2.66 sec: 1.03x slower                                                |
| bpe_tokeniser              | 4.69 sec                                               | 4.86 sec: 1.04x slower                                                |
| pyflate                    | 460 ms                                                 | 476 ms: 1.04x slower                                                  |
| async_tree_io              | 843 ms                                                 | 873 ms: 1.04x slower                                                  |
| nbody                      | 85.7 ms                                                | 89.5 ms: 1.04x slower                                                 |
| fannkuch                   | 381 ms                                                 | 403 ms: 1.06x slower                                                  |
| async_tree_io_tg           | 825 ms                                                 | 875 ms: 1.06x slower                                                  |
| create_gc_cycles           | 1.61 ms                                                | 1.73 ms: 1.07x slower                                                 |
| unpickle_list              | 4.96 us                                                | 5.36 us: 1.08x slower                                                 |
| unpack_sequence            | 42.4 ns                                                | 46.3 ns: 1.09x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                          |

Benchmark hidden because not significant (16): async_tree_none_tg, json, async_tree_cpu_io_mixed, typing_runtime_protocols, nqueens, chaos, xml_etree_parse, json_loads, meteor_contest, unpickle_pure_python, bench_mp_pool, raytrace, telco, mako, unpickle, pylint
Ignored benchmarks (7) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 99.81% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x