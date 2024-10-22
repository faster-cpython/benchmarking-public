# Results vs. 3.13.0

- fork: brandtbucher
- ref: nojit
- machine: linux-x86_64
- commit hash: a6f1035
- commit date: 2024-09-21
- overall geometric mean: 1.01x faster
- HPT reliability: 95.82%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240921-linux-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 255 ms: 1.04x faster                                         |
| docutils       | 2.58 sec                                               | 2.65 sec: 1.03x slower                                       |
| html5lib       | 64.5 ms                                                | 63.8 ms: 1.01x faster                                        |
| tornado_http   | 91.5 ms                                                | 89.8 ms: 1.02x faster                                        |
| Geometric mean | (ref)                                                  | 1.01x faster                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240921-linux-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_memoization_tg  | 465 ms                                                 | 387 ms: 1.20x faster                                         |
| async_tree_memoization     | 442 ms                                                 | 389 ms: 1.14x faster                                         |
| async_tree_none            | 354 ms                                                 | 312 ms: 1.13x faster                                         |
| async_tree_none_tg         | 320 ms                                                 | 307 ms: 1.04x faster                                         |
| asyncio_tcp                | 488 ms                                                 | 468 ms: 1.04x faster                                         |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 561 ms: 1.02x faster                                         |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.78 sec: 1.01x faster                                       |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 552 ms: 1.02x slower                                         |
| coroutines                 | 22.5 ms                                                | 23.3 ms: 1.03x slower                                        |
| async_tree_io              | 843 ms                                                 | 879 ms: 1.04x slower                                         |
| async_tree_io_tg           | 825 ms                                                 | 869 ms: 1.05x slower                                         |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                 |

Benchmark hidden because not significant (2): asyncio_websockets, async_generators

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240921-linux-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| float          | 78.5 ms                                                | 76.3 ms: 1.03x faster                                        |
| pidigits       | 186 ms                                                 | 187 ms: 1.00x slower                                         |
| nbody          | 85.7 ms                                                | 87.1 ms: 1.02x slower                                        |
| Geometric mean | (ref)                                                  | 1.00x faster                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240921-linux-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.70 ms: 1.05x faster                                        |
| regex_compile  | 131 ms                                                 | 129 ms: 1.02x faster                                         |
| regex_v8       | 25.3 ms                                                | 25.0 ms: 1.01x faster                                        |
| Geometric mean | (ref)                                                  | 1.02x faster                                                 |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240921-linux-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| xml_etree_generate   | 87.0 ms                                                | 84.7 ms: 1.03x faster                                        |
| xml_etree_process    | 60.4 ms                                                | 59.0 ms: 1.02x faster                                        |
| pickle_pure_python   | 300 us                                                 | 301 us: 1.00x slower                                         |
| unpickle_pure_python | 213 us                                                 | 215 us: 1.01x slower                                         |
| json_dumps           | 10.4 ms                                                | 10.6 ms: 1.01x slower                                        |
| json_loads           | 27.0 us                                                | 27.5 us: 1.02x slower                                        |
| unpickle             | 14.9 us                                                | 15.2 us: 1.02x slower                                        |
| pickle_list          | 5.01 us                                                | 5.12 us: 1.02x slower                                        |
| xml_etree_iterparse  | 102 ms                                                 | 105 ms: 1.03x slower                                         |
| pickle_dict          | 33.2 us                                                | 35.1 us: 1.06x slower                                        |
| unpickle_list        | 4.96 us                                                | 5.34 us: 1.08x slower                                        |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                 |

Benchmark hidden because not significant (3): tomli_loads, xml_etree_parse, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240921-linux-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.5 ms: 1.00x faster                                        |
| python_startup_no_site | 6.99 ms                                                | 7.00 ms: 1.00x slower                                        |
| Geometric mean         | (ref)                                                  | 1.00x faster                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240921-linux-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| genshi_text     | 22.9 ms                                                | 22.4 ms: 1.02x faster                                        |
| genshi_xml      | 50.3 ms                                                | 50.0 ms: 1.01x faster                                        |
| django_template | 34.4 ms                                                | 34.1 ms: 1.01x faster                                        |
| mako            | 11.1 ms                                                | 11.3 ms: 1.02x slower                                        |
| Geometric mean  | (ref)                                                  | 1.00x faster                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240921-linux-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| deepcopy                   | 352 us                                                 | 258 us: 1.37x faster                                         |
| deepcopy_memo              | 38.0 us                                                | 29.7 us: 1.28x faster                                        |
| async_tree_memoization_tg  | 465 ms                                                 | 387 ms: 1.20x faster                                         |
| go                         | 142 ms                                                 | 120 ms: 1.18x faster                                         |
| deepcopy_reduce            | 3.17 us                                                | 2.69 us: 1.18x faster                                        |
| async_tree_memoization     | 442 ms                                                 | 389 ms: 1.14x faster                                         |
| async_tree_none            | 354 ms                                                 | 312 ms: 1.13x faster                                         |
| pathlib                    | 17.1 ms                                                | 16.1 ms: 1.06x faster                                        |
| pycparser                  | 1.19 sec                                               | 1.13 sec: 1.06x faster                                       |
| regex_effbot               | 3.88 ms                                                | 3.70 ms: 1.05x faster                                        |
| pprint_safe_repr           | 744 ms                                                 | 711 ms: 1.05x faster                                         |
| async_tree_none_tg         | 320 ms                                                 | 307 ms: 1.04x faster                                         |
| asyncio_tcp                | 488 ms                                                 | 468 ms: 1.04x faster                                         |
| 2to3                       | 265 ms                                                 | 255 ms: 1.04x faster                                         |
| generators                 | 28.8 ms                                                | 27.7 ms: 1.04x faster                                        |
| pprint_pformat             | 1.51 sec                                               | 1.46 sec: 1.04x faster                                       |
| richards                   | 48.1 ms                                                | 46.4 ms: 1.04x faster                                        |
| richards_super             | 54.4 ms                                                | 52.7 ms: 1.03x faster                                        |
| scimark_lu                 | 115 ms                                                 | 112 ms: 1.03x faster                                         |
| float                      | 78.5 ms                                                | 76.3 ms: 1.03x faster                                        |
| xml_etree_generate         | 87.0 ms                                                | 84.7 ms: 1.03x faster                                        |
| xml_etree_process          | 60.4 ms                                                | 59.0 ms: 1.02x faster                                        |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 561 ms: 1.02x faster                                         |
| json                       | 5.20 ms                                                | 5.09 ms: 1.02x faster                                        |
| thrift                     | 796 us                                                 | 780 us: 1.02x faster                                         |
| genshi_text                | 22.9 ms                                                | 22.4 ms: 1.02x faster                                        |
| sympy_str                  | 274 ms                                                 | 269 ms: 1.02x faster                                         |
| tornado_http               | 91.5 ms                                                | 89.8 ms: 1.02x faster                                        |
| regex_compile              | 131 ms                                                 | 129 ms: 1.02x faster                                         |
| sympy_sum                  | 150 ms                                                 | 147 ms: 1.02x faster                                         |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.96 ms: 1.01x faster                                        |
| meteor_contest             | 108 ms                                                 | 106 ms: 1.01x faster                                         |
| logging_format             | 6.25 us                                                | 6.17 us: 1.01x faster                                        |
| sympy_expand               | 462 ms                                                 | 456 ms: 1.01x faster                                         |
| html5lib                   | 64.5 ms                                                | 63.8 ms: 1.01x faster                                        |
| regex_v8                   | 25.3 ms                                                | 25.0 ms: 1.01x faster                                        |
| sympy_integrate            | 19.9 ms                                                | 19.7 ms: 1.01x faster                                        |
| sqlglot_optimize           | 53.9 ms                                                | 53.5 ms: 1.01x faster                                        |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.78 sec: 1.01x faster                                       |
| genshi_xml                 | 50.3 ms                                                | 50.0 ms: 1.01x faster                                        |
| django_template            | 34.4 ms                                                | 34.1 ms: 1.01x faster                                        |
| bench_thread_pool          | 815 us                                                 | 809 us: 1.01x faster                                         |
| sqlglot_normalize          | 107 ms                                                 | 107 ms: 1.01x faster                                         |
| telco                      | 8.45 ms                                                | 8.40 ms: 1.01x faster                                        |
| mdp                        | 2.74 sec                                               | 2.73 sec: 1.00x faster                                       |
| python_startup             | 10.6 ms                                                | 10.5 ms: 1.00x faster                                        |
| python_startup_no_site     | 6.99 ms                                                | 7.00 ms: 1.00x slower                                        |
| sqlglot_transpile          | 1.57 ms                                                | 1.58 ms: 1.00x slower                                        |
| pidigits                   | 186 ms                                                 | 187 ms: 1.00x slower                                         |
| crypto_pyaes               | 73.0 ms                                                | 73.2 ms: 1.00x slower                                        |
| pickle_pure_python         | 300 us                                                 | 301 us: 1.00x slower                                         |
| chaos                      | 58.4 ms                                                | 58.8 ms: 1.01x slower                                        |
| unpickle_pure_python       | 213 us                                                 | 215 us: 1.01x slower                                         |
| nqueens                    | 80.6 ms                                                | 81.4 ms: 1.01x slower                                        |
| raytrace                   | 262 ms                                                 | 264 ms: 1.01x slower                                         |
| json_dumps                 | 10.4 ms                                                | 10.6 ms: 1.01x slower                                        |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 552 ms: 1.02x slower                                         |
| sqlglot_parse              | 1.27 ms                                                | 1.28 ms: 1.02x slower                                        |
| nbody                      | 85.7 ms                                                | 87.1 ms: 1.02x slower                                        |
| scimark_monte_carlo        | 66.3 ms                                                | 67.4 ms: 1.02x slower                                        |
| coverage                   | 83.7 ms                                                | 85.2 ms: 1.02x slower                                        |
| json_loads                 | 27.0 us                                                | 27.5 us: 1.02x slower                                        |
| gc_traversal               | 3.81 ms                                                | 3.88 ms: 1.02x slower                                        |
| scimark_sor                | 122 ms                                                 | 125 ms: 1.02x slower                                         |
| unpickle                   | 14.9 us                                                | 15.2 us: 1.02x slower                                        |
| mako                       | 11.1 ms                                                | 11.3 ms: 1.02x slower                                        |
| pickle_list                | 5.01 us                                                | 5.12 us: 1.02x slower                                        |
| hexiom                     | 6.13 ms                                                | 6.26 ms: 1.02x slower                                        |
| spectral_norm              | 115 ms                                                 | 118 ms: 1.02x slower                                         |
| deltablue                  | 3.15 ms                                                | 3.23 ms: 1.02x slower                                        |
| bpe_tokeniser              | 4.69 sec                                               | 4.81 sec: 1.03x slower                                       |
| docutils                   | 2.58 sec                                               | 2.65 sec: 1.03x slower                                       |
| dulwich_log                | 63.0 ms                                                | 64.7 ms: 1.03x slower                                        |
| xml_etree_iterparse        | 102 ms                                                 | 105 ms: 1.03x slower                                         |
| coroutines                 | 22.5 ms                                                | 23.3 ms: 1.03x slower                                        |
| comprehensions             | 16.4 us                                                | 17.0 us: 1.04x slower                                        |
| async_tree_io              | 843 ms                                                 | 879 ms: 1.04x slower                                         |
| async_tree_io_tg           | 825 ms                                                 | 869 ms: 1.05x slower                                         |
| pickle_dict                | 33.2 us                                                | 35.1 us: 1.06x slower                                        |
| unpickle_list              | 4.96 us                                                | 5.34 us: 1.08x slower                                        |
| fannkuch                   | 381 ms                                                 | 410 ms: 1.08x slower                                         |
| create_gc_cycles           | 1.61 ms                                                | 1.74 ms: 1.08x slower                                        |
| unpack_sequence            | 42.4 ns                                                | 50.3 ns: 1.19x slower                                        |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                 |

Benchmark hidden because not significant (14): logging_silent, scimark_fft, tomli_loads, logging_simple, sqlite_synth, asyncio_websockets, xml_etree_parse, bench_mp_pool, pickle, pyflate, async_generators, typing_runtime_protocols, regex_dna, pylint
Ignored benchmarks (7) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 95.82% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x