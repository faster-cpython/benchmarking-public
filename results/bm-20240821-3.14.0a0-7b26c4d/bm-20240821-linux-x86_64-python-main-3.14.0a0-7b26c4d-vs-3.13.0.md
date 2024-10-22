# Results vs. 3.13.0

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 7b26c4d
- commit date: 2024-08-21
- overall geometric mean: 1.01x faster
- HPT reliability: 85.18%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240821-linux-x86_64-python-main-3.14.0a0-7b26c4d |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| 2to3           | 265 ms                                                 | 262 ms: 1.01x faster                                  |
| docutils       | 2.58 sec                                               | 2.72 sec: 1.05x slower                                |
| html5lib       | 64.5 ms                                                | 63.5 ms: 1.02x faster                                 |
| tornado_http   | 91.5 ms                                                | 90.2 ms: 1.01x faster                                 |
| Geometric mean | (ref)                                                  | 1.00x slower                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240821-linux-x86_64-python-main-3.14.0a0-7b26c4d |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| async_tree_memoization_tg  | 465 ms                                                 | 392 ms: 1.18x faster                                  |
| async_tree_none            | 354 ms                                                 | 323 ms: 1.10x faster                                  |
| async_tree_memoization     | 442 ms                                                 | 413 ms: 1.07x faster                                  |
| async_tree_none_tg         | 320 ms                                                 | 300 ms: 1.07x faster                                  |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 529 ms: 1.03x faster                                  |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 560 ms: 1.03x faster                                  |
| asyncio_tcp                | 488 ms                                                 | 480 ms: 1.02x faster                                  |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.78 sec: 1.01x faster                                |
| asyncio_websockets         | 555 ms                                                 | 560 ms: 1.01x slower                                  |
| coroutines                 | 22.5 ms                                                | 23.1 ms: 1.02x slower                                 |
| async_tree_io_tg           | 825 ms                                                 | 867 ms: 1.05x slower                                  |
| async_tree_io              | 843 ms                                                 | 903 ms: 1.07x slower                                  |
| Geometric mean             | (ref)                                                  | 1.02x faster                                          |

Benchmark hidden because not significant (1): async_generators

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240821-linux-x86_64-python-main-3.14.0a0-7b26c4d |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| pidigits       | 186 ms                                                 | 187 ms: 1.00x slower                                  |
| nbody          | 85.7 ms                                                | 87.7 ms: 1.02x slower                                 |
| Geometric mean | (ref)                                                  | 1.01x slower                                          |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240821-linux-x86_64-python-main-3.14.0a0-7b26c4d |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.59 ms: 1.08x faster                                 |
| regex_v8       | 25.3 ms                                                | 24.9 ms: 1.02x faster                                 |
| regex_compile  | 131 ms                                                 | 130 ms: 1.01x faster                                  |
| regex_dna      | 220 ms                                                 | 223 ms: 1.01x slower                                  |
| Geometric mean | (ref)                                                  | 1.02x faster                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240821-linux-x86_64-python-main-3.14.0a0-7b26c4d |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| tomli_loads          | 2.11 sec                                               | 2.07 sec: 1.02x faster                                |
| xml_etree_parse      | 156 ms                                                 | 153 ms: 1.02x faster                                  |
| xml_etree_process    | 60.4 ms                                                | 59.6 ms: 1.01x faster                                 |
| xml_etree_generate   | 87.0 ms                                                | 86.1 ms: 1.01x faster                                 |
| unpickle_pure_python | 213 us                                                 | 215 us: 1.01x slower                                  |
| pickle_pure_python   | 300 us                                                 | 303 us: 1.01x slower                                  |
| json_dumps           | 10.4 ms                                                | 10.5 ms: 1.01x slower                                 |
| xml_etree_iterparse  | 102 ms                                                 | 105 ms: 1.03x slower                                  |
| json_loads           | 27.0 us                                                | 28.4 us: 1.05x slower                                 |
| Geometric mean       | (ref)                                                  | 1.01x slower                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240821-linux-x86_64-python-main-3.14.0a0-7b26c4d |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.5 ms: 1.00x faster                                 |
| python_startup_no_site | 6.99 ms                                                | 7.09 ms: 1.01x slower                                 |
| Geometric mean         | (ref)                                                  | 1.01x slower                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240821-linux-x86_64-python-main-3.14.0a0-7b26c4d |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| django_template | 34.4 ms                                                | 33.8 ms: 1.02x faster                                 |
| mako            | 11.1 ms                                                | 11.3 ms: 1.02x slower                                 |
| genshi_xml      | 50.3 ms                                                | 51.3 ms: 1.02x slower                                 |
| genshi_text     | 22.9 ms                                                | 23.5 ms: 1.03x slower                                 |
| Geometric mean  | (ref)                                                  | 1.01x slower                                          |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240821-linux-x86_64-python-main-3.14.0a0-7b26c4d |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| deepcopy                   | 352 us                                                 | 262 us: 1.34x faster                                  |
| deepcopy_memo              | 38.0 us                                                | 30.2 us: 1.26x faster                                 |
| async_tree_memoization_tg  | 465 ms                                                 | 392 ms: 1.18x faster                                  |
| deepcopy_reduce            | 3.17 us                                                | 2.69 us: 1.18x faster                                 |
| async_tree_none            | 354 ms                                                 | 323 ms: 1.10x faster                                  |
| regex_effbot               | 3.88 ms                                                | 3.59 ms: 1.08x faster                                 |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.67 ms: 1.08x faster                                 |
| async_tree_memoization     | 442 ms                                                 | 413 ms: 1.07x faster                                  |
| async_tree_none_tg         | 320 ms                                                 | 300 ms: 1.07x faster                                  |
| thrift                     | 796 us                                                 | 754 us: 1.06x faster                                  |
| mdp                        | 2.74 sec                                               | 2.60 sec: 1.05x faster                                |
| pycparser                  | 1.19 sec                                               | 1.14 sec: 1.05x faster                                |
| pathlib                    | 17.1 ms                                                | 16.2 ms: 1.05x faster                                 |
| logging_simple             | 5.66 us                                                | 5.45 us: 1.04x faster                                 |
| bench_thread_pool          | 815 us                                                 | 785 us: 1.04x faster                                  |
| spectral_norm              | 115 ms                                                 | 111 ms: 1.04x faster                                  |
| richards                   | 48.1 ms                                                | 46.6 ms: 1.03x faster                                 |
| telco                      | 8.45 ms                                                | 8.18 ms: 1.03x faster                                 |
| generators                 | 28.8 ms                                                | 27.9 ms: 1.03x faster                                 |
| logging_format             | 6.25 us                                                | 6.06 us: 1.03x faster                                 |
| richards_super             | 54.4 ms                                                | 52.8 ms: 1.03x faster                                 |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 529 ms: 1.03x faster                                  |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 560 ms: 1.03x faster                                  |
| scimark_fft                | 369 ms                                                 | 361 ms: 1.02x faster                                  |
| tomli_loads                | 2.11 sec                                               | 2.07 sec: 1.02x faster                                |
| django_template            | 34.4 ms                                                | 33.8 ms: 1.02x faster                                 |
| logging_silent             | 102 ns                                                 | 100 ns: 1.02x faster                                  |
| asyncio_tcp                | 488 ms                                                 | 480 ms: 1.02x faster                                  |
| html5lib                   | 64.5 ms                                                | 63.5 ms: 1.02x faster                                 |
| xml_etree_parse            | 156 ms                                                 | 153 ms: 1.02x faster                                  |
| regex_v8                   | 25.3 ms                                                | 24.9 ms: 1.02x faster                                 |
| tornado_http               | 91.5 ms                                                | 90.2 ms: 1.01x faster                                 |
| crypto_pyaes               | 73.0 ms                                                | 71.9 ms: 1.01x faster                                 |
| xml_etree_process          | 60.4 ms                                                | 59.6 ms: 1.01x faster                                 |
| regex_compile              | 131 ms                                                 | 130 ms: 1.01x faster                                  |
| 2to3                       | 265 ms                                                 | 262 ms: 1.01x faster                                  |
| xml_etree_generate         | 87.0 ms                                                | 86.1 ms: 1.01x faster                                 |
| nqueens                    | 80.6 ms                                                | 80.1 ms: 1.01x faster                                 |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.78 sec: 1.01x faster                                |
| pprint_safe_repr           | 744 ms                                                 | 740 ms: 1.01x faster                                  |
| meteor_contest             | 108 ms                                                 | 107 ms: 1.00x faster                                  |
| comprehensions             | 16.4 us                                                | 16.3 us: 1.00x faster                                 |
| sqlglot_optimize           | 53.9 ms                                                | 53.7 ms: 1.00x faster                                 |
| sympy_integrate            | 19.9 ms                                                | 19.8 ms: 1.00x faster                                 |
| python_startup             | 10.6 ms                                                | 10.5 ms: 1.00x faster                                 |
| sqlglot_normalize          | 107 ms                                                 | 108 ms: 1.00x slower                                  |
| pidigits                   | 186 ms                                                 | 187 ms: 1.00x slower                                  |
| unpickle_pure_python       | 213 us                                                 | 215 us: 1.01x slower                                  |
| pprint_pformat             | 1.51 sec                                               | 1.52 sec: 1.01x slower                                |
| raytrace                   | 262 ms                                                 | 263 ms: 1.01x slower                                  |
| asyncio_websockets         | 555 ms                                                 | 560 ms: 1.01x slower                                  |
| pickle_pure_python         | 300 us                                                 | 303 us: 1.01x slower                                  |
| gc_traversal               | 3.81 ms                                                | 3.85 ms: 1.01x slower                                 |
| json_dumps                 | 10.4 ms                                                | 10.5 ms: 1.01x slower                                 |
| sqlglot_parse              | 1.27 ms                                                | 1.28 ms: 1.01x slower                                 |
| regex_dna                  | 220 ms                                                 | 223 ms: 1.01x slower                                  |
| python_startup_no_site     | 6.99 ms                                                | 7.09 ms: 1.01x slower                                 |
| chaos                      | 58.4 ms                                                | 59.3 ms: 1.02x slower                                 |
| mako                       | 11.1 ms                                                | 11.3 ms: 1.02x slower                                 |
| genshi_xml                 | 50.3 ms                                                | 51.3 ms: 1.02x slower                                 |
| json                       | 5.20 ms                                                | 5.31 ms: 1.02x slower                                 |
| nbody                      | 85.7 ms                                                | 87.7 ms: 1.02x slower                                 |
| scimark_sor                | 122 ms                                                 | 125 ms: 1.02x slower                                  |
| coroutines                 | 22.5 ms                                                | 23.1 ms: 1.02x slower                                 |
| genshi_text                | 22.9 ms                                                | 23.5 ms: 1.03x slower                                 |
| pyflate                    | 460 ms                                                 | 472 ms: 1.03x slower                                  |
| scimark_monte_carlo        | 66.3 ms                                                | 68.3 ms: 1.03x slower                                 |
| go                         | 142 ms                                                 | 146 ms: 1.03x slower                                  |
| xml_etree_iterparse        | 102 ms                                                 | 105 ms: 1.03x slower                                  |
| bpe_tokeniser              | 4.69 sec                                               | 4.84 sec: 1.03x slower                                |
| typing_runtime_protocols   | 159 us                                                 | 165 us: 1.03x slower                                  |
| async_tree_io_tg           | 825 ms                                                 | 867 ms: 1.05x slower                                  |
| docutils                   | 2.58 sec                                               | 2.72 sec: 1.05x slower                                |
| json_loads                 | 27.0 us                                                | 28.4 us: 1.05x slower                                 |
| fannkuch                   | 381 ms                                                 | 403 ms: 1.06x slower                                  |
| async_tree_io              | 843 ms                                                 | 903 ms: 1.07x slower                                  |
| create_gc_cycles           | 1.61 ms                                                | 1.74 ms: 1.08x slower                                 |
| Geometric mean             | (ref)                                                  | 1.01x faster                                          |

Benchmark hidden because not significant (12): sympy_str, sympy_expand, scimark_lu, float, sympy_sum, sqlglot_transpile, bench_mp_pool, hexiom, coverage, async_generators, deltablue, pylint
Ignored benchmarks (15) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 85.18% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x