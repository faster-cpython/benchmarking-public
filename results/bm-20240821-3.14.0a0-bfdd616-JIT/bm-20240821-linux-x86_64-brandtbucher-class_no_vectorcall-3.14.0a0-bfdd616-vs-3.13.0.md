# Results vs. 3.13.0

- fork: brandtbucher
- ref: class_no_vectorcall
- machine: linux-x86_64
- commit hash: bfdd616
- commit date: 2024-08-21
- overall geometric mean: 1.01x faster
- HPT reliability: 56.85%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240821-linux-x86_64-brandtbucher-class_no_vectorcall-3.14.0a0-bfdd616 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 283 ms: 1.07x slower                                                       |
| docutils       | 2.58 sec                                               | 3.05 sec: 1.18x slower                                                     |
| html5lib       | 64.5 ms                                                | 66.6 ms: 1.03x slower                                                      |
| tornado_http   | 91.5 ms                                                | 94.3 ms: 1.03x slower                                                      |
| Geometric mean | (ref)                                                  | 1.08x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240821-linux-x86_64-brandtbucher-class_no_vectorcall-3.14.0a0-bfdd616 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 465 ms                                                 | 394 ms: 1.18x faster                                                       |
| async_tree_none            | 354 ms                                                 | 325 ms: 1.09x faster                                                       |
| async_tree_none_tg         | 320 ms                                                 | 302 ms: 1.06x faster                                                       |
| async_tree_memoization     | 442 ms                                                 | 425 ms: 1.04x faster                                                       |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 535 ms: 1.02x faster                                                       |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 566 ms: 1.01x faster                                                       |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.80 sec: 1.00x slower                                                     |
| asyncio_tcp                | 488 ms                                                 | 493 ms: 1.01x slower                                                       |
| coroutines                 | 22.5 ms                                                | 23.0 ms: 1.02x slower                                                      |
| async_tree_io_tg           | 825 ms                                                 | 864 ms: 1.05x slower                                                       |
| async_generators           | 433 ms                                                 | 456 ms: 1.05x slower                                                       |
| async_tree_io              | 843 ms                                                 | 907 ms: 1.08x slower                                                       |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                               |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240821-linux-x86_64-brandtbucher-class_no_vectorcall-3.14.0a0-bfdd616 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 70.7 ms: 1.11x faster                                                      |
| nbody          | 85.7 ms                                                | 79.6 ms: 1.08x faster                                                      |
| Geometric mean | (ref)                                                  | 1.06x faster                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240821-linux-x86_64-brandtbucher-class_no_vectorcall-3.14.0a0-bfdd616 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.57 ms: 1.09x faster                                                      |
| regex_dna      | 220 ms                                                 | 218 ms: 1.01x faster                                                       |
| regex_compile  | 131 ms                                                 | 142 ms: 1.08x slower                                                       |
| Geometric mean | (ref)                                                  | 1.00x faster                                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240821-linux-x86_64-brandtbucher-class_no_vectorcall-3.14.0a0-bfdd616 |
|---------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_generate  | 87.0 ms                                                | 77.7 ms: 1.12x faster                                                      |
| xml_etree_process   | 60.4 ms                                                | 55.3 ms: 1.09x faster                                                      |
| tomli_loads         | 2.11 sec                                               | 1.94 sec: 1.09x faster                                                     |
| xml_etree_parse     | 156 ms                                                 | 146 ms: 1.07x faster                                                       |
| json_dumps          | 10.4 ms                                                | 10.0 ms: 1.04x faster                                                      |
| xml_etree_iterparse | 102 ms                                                 | 98.9 ms: 1.03x faster                                                      |
| pickle_pure_python  | 300 us                                                 | 305 us: 1.02x slower                                                       |
| json_loads          | 27.0 us                                                | 28.5 us: 1.06x slower                                                      |
| Geometric mean      | (ref)                                                  | 1.04x faster                                                               |

Benchmark hidden because not significant (1): unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240821-linux-x86_64-brandtbucher-class_no_vectorcall-3.14.0a0-bfdd616 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.5 ms: 1.01x faster                                                      |
| python_startup_no_site | 6.99 ms                                                | 7.11 ms: 1.02x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.00x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240821-linux-x86_64-brandtbucher-class_no_vectorcall-3.14.0a0-bfdd616 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.92 ms: 1.12x faster                                                      |
| django_template | 34.4 ms                                                | 35.5 ms: 1.03x slower                                                      |
| genshi_text     | 22.9 ms                                                | 25.9 ms: 1.13x slower                                                      |
| genshi_xml      | 50.3 ms                                                | 59.5 ms: 1.18x slower                                                      |
| Geometric mean  | (ref)                                                  | 1.05x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240821-linux-x86_64-brandtbucher-class_no_vectorcall-3.14.0a0-bfdd616 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| deepcopy_memo              | 38.0 us                                                | 27.1 us: 1.40x faster                                                      |
| deepcopy                   | 352 us                                                 | 270 us: 1.31x faster                                                       |
| richards                   | 48.1 ms                                                | 39.3 ms: 1.23x faster                                                      |
| richards_super             | 54.4 ms                                                | 44.9 ms: 1.21x faster                                                      |
| async_tree_memoization_tg  | 465 ms                                                 | 394 ms: 1.18x faster                                                       |
| scimark_fft                | 369 ms                                                 | 313 ms: 1.18x faster                                                       |
| deepcopy_reduce            | 3.17 us                                                | 2.75 us: 1.15x faster                                                      |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.41 ms: 1.14x faster                                                      |
| spectral_norm              | 115 ms                                                 | 101 ms: 1.13x faster                                                       |
| xml_etree_generate         | 87.0 ms                                                | 77.7 ms: 1.12x faster                                                      |
| mako                       | 11.1 ms                                                | 9.92 ms: 1.12x faster                                                      |
| float                      | 78.5 ms                                                | 70.7 ms: 1.11x faster                                                      |
| crypto_pyaes               | 73.0 ms                                                | 66.0 ms: 1.10x faster                                                      |
| telco                      | 8.45 ms                                                | 7.71 ms: 1.10x faster                                                      |
| xml_etree_process          | 60.4 ms                                                | 55.3 ms: 1.09x faster                                                      |
| tomli_loads                | 2.11 sec                                               | 1.94 sec: 1.09x faster                                                     |
| async_tree_none            | 354 ms                                                 | 325 ms: 1.09x faster                                                       |
| regex_effbot               | 3.88 ms                                                | 3.57 ms: 1.09x faster                                                      |
| nbody                      | 85.7 ms                                                | 79.6 ms: 1.08x faster                                                      |
| pathlib                    | 17.1 ms                                                | 15.8 ms: 1.08x faster                                                      |
| xml_etree_parse            | 156 ms                                                 | 146 ms: 1.07x faster                                                       |
| mdp                        | 2.74 sec                                               | 2.57 sec: 1.07x faster                                                     |
| gc_traversal               | 3.81 ms                                                | 3.56 ms: 1.07x faster                                                      |
| async_tree_none_tg         | 320 ms                                                 | 302 ms: 1.06x faster                                                       |
| bpe_tokeniser              | 4.69 sec                                               | 4.44 sec: 1.06x faster                                                     |
| scimark_sor                | 122 ms                                                 | 116 ms: 1.05x faster                                                       |
| async_tree_memoization     | 442 ms                                                 | 425 ms: 1.04x faster                                                       |
| pyflate                    | 460 ms                                                 | 442 ms: 1.04x faster                                                       |
| scimark_monte_carlo        | 66.3 ms                                                | 63.8 ms: 1.04x faster                                                      |
| fannkuch                   | 381 ms                                                 | 367 ms: 1.04x faster                                                       |
| pycparser                  | 1.19 sec                                               | 1.15 sec: 1.04x faster                                                     |
| json_dumps                 | 10.4 ms                                                | 10.0 ms: 1.04x faster                                                      |
| logging_format             | 6.25 us                                                | 6.04 us: 1.04x faster                                                      |
| scimark_lu                 | 115 ms                                                 | 111 ms: 1.03x faster                                                       |
| xml_etree_iterparse        | 102 ms                                                 | 98.9 ms: 1.03x faster                                                      |
| logging_simple             | 5.66 us                                                | 5.50 us: 1.03x faster                                                      |
| meteor_contest             | 108 ms                                                 | 105 ms: 1.02x faster                                                       |
| logging_silent             | 102 ns                                                 | 100 ns: 1.02x faster                                                       |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 535 ms: 1.02x faster                                                       |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 566 ms: 1.01x faster                                                       |
| python_startup             | 10.6 ms                                                | 10.5 ms: 1.01x faster                                                      |
| regex_dna                  | 220 ms                                                 | 218 ms: 1.01x faster                                                       |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.80 sec: 1.00x slower                                                     |
| bench_thread_pool          | 815 us                                                 | 821 us: 1.01x slower                                                       |
| asyncio_tcp                | 488 ms                                                 | 493 ms: 1.01x slower                                                       |
| comprehensions             | 16.4 us                                                | 16.6 us: 1.01x slower                                                      |
| coverage                   | 83.7 ms                                                | 84.9 ms: 1.01x slower                                                      |
| chaos                      | 58.4 ms                                                | 59.2 ms: 1.01x slower                                                      |
| pickle_pure_python         | 300 us                                                 | 305 us: 1.02x slower                                                       |
| python_startup_no_site     | 6.99 ms                                                | 7.11 ms: 1.02x slower                                                      |
| coroutines                 | 22.5 ms                                                | 23.0 ms: 1.02x slower                                                      |
| json                       | 5.20 ms                                                | 5.32 ms: 1.02x slower                                                      |
| go                         | 142 ms                                                 | 146 ms: 1.03x slower                                                       |
| tornado_http               | 91.5 ms                                                | 94.3 ms: 1.03x slower                                                      |
| django_template            | 34.4 ms                                                | 35.5 ms: 1.03x slower                                                      |
| html5lib                   | 64.5 ms                                                | 66.6 ms: 1.03x slower                                                      |
| pprint_pformat             | 1.51 sec                                               | 1.56 sec: 1.03x slower                                                     |
| pprint_safe_repr           | 744 ms                                                 | 771 ms: 1.04x slower                                                       |
| sqlglot_parse              | 1.27 ms                                                | 1.32 ms: 1.04x slower                                                      |
| raytrace                   | 262 ms                                                 | 272 ms: 1.04x slower                                                       |
| async_tree_io_tg           | 825 ms                                                 | 864 ms: 1.05x slower                                                       |
| typing_runtime_protocols   | 159 us                                                 | 168 us: 1.05x slower                                                       |
| async_generators           | 433 ms                                                 | 456 ms: 1.05x slower                                                       |
| json_loads                 | 27.0 us                                                | 28.5 us: 1.06x slower                                                      |
| nqueens                    | 80.6 ms                                                | 85.8 ms: 1.06x slower                                                      |
| sqlglot_transpile          | 1.57 ms                                                | 1.68 ms: 1.07x slower                                                      |
| 2to3                       | 265 ms                                                 | 283 ms: 1.07x slower                                                       |
| sqlglot_normalize          | 107 ms                                                 | 115 ms: 1.07x slower                                                       |
| create_gc_cycles           | 1.61 ms                                                | 1.73 ms: 1.08x slower                                                      |
| async_tree_io              | 843 ms                                                 | 907 ms: 1.08x slower                                                       |
| sqlglot_optimize           | 53.9 ms                                                | 58.2 ms: 1.08x slower                                                      |
| regex_compile              | 131 ms                                                 | 142 ms: 1.08x slower                                                       |
| sympy_expand               | 462 ms                                                 | 511 ms: 1.11x slower                                                       |
| sympy_str                  | 274 ms                                                 | 304 ms: 1.11x slower                                                       |
| hexiom                     | 6.13 ms                                                | 6.83 ms: 1.11x slower                                                      |
| genshi_text                | 22.9 ms                                                | 25.9 ms: 1.13x slower                                                      |
| generators                 | 28.8 ms                                                | 32.7 ms: 1.14x slower                                                      |
| sympy_integrate            | 19.9 ms                                                | 23.0 ms: 1.16x slower                                                      |
| sympy_sum                  | 150 ms                                                 | 176 ms: 1.18x slower                                                       |
| pylint                     | 313 ms                                                 | 369 ms: 1.18x slower                                                       |
| docutils                   | 2.58 sec                                               | 3.05 sec: 1.18x slower                                                     |
| genshi_xml                 | 50.3 ms                                                | 59.5 ms: 1.18x slower                                                      |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                               |

Benchmark hidden because not significant (7): thrift, regex_v8, deltablue, unpickle_pure_python, pidigits, bench_mp_pool, asyncio_websockets
Ignored benchmarks (15) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 56.85% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.09x