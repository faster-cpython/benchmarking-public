# Results vs. 3.13.0

- fork: brandtbucher
- ref: load_attr_property
- machine: linux-x86_64
- commit hash: 0b4c6da
- commit date: 2024-07-24
- overall geometric mean: 1.01x faster
- HPT reliability: 56.53%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240724-linux-x86_64-brandtbucher-load_attr_property-3.14.0a0-0b4c6da |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 271 ms: 1.02x slower                                                      |
| docutils       | 2.58 sec                                               | 2.90 sec: 1.12x slower                                                    |
| html5lib       | 64.5 ms                                                | 64.8 ms: 1.00x slower                                                     |
| tornado_http   | 91.5 ms                                                | 92.9 ms: 1.02x slower                                                     |
| Geometric mean | (ref)                                                  | 1.04x slower                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240724-linux-x86_64-brandtbucher-load_attr_property-3.14.0a0-0b4c6da |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 465 ms                                                 | 393 ms: 1.18x faster                                                      |
| async_tree_none            | 354 ms                                                 | 326 ms: 1.09x faster                                                      |
| async_tree_none_tg         | 320 ms                                                 | 304 ms: 1.05x faster                                                      |
| async_tree_memoization     | 442 ms                                                 | 428 ms: 1.03x faster                                                      |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 528 ms: 1.03x faster                                                      |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 560 ms: 1.03x faster                                                      |
| asyncio_websockets         | 555 ms                                                 | 558 ms: 1.00x slower                                                      |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.80 sec: 1.01x slower                                                    |
| coroutines                 | 22.5 ms                                                | 23.0 ms: 1.02x slower                                                     |
| asyncio_tcp                | 488 ms                                                 | 504 ms: 1.03x slower                                                      |
| async_generators           | 433 ms                                                 | 450 ms: 1.04x slower                                                      |
| async_tree_io_tg           | 825 ms                                                 | 875 ms: 1.06x slower                                                      |
| async_tree_io              | 843 ms                                                 | 905 ms: 1.07x slower                                                      |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240724-linux-x86_64-brandtbucher-load_attr_property-3.14.0a0-0b4c6da |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 70.7 ms: 1.11x faster                                                     |
| nbody          | 85.7 ms                                                | 81.0 ms: 1.06x faster                                                     |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                      |
| Geometric mean | (ref)                                                  | 1.06x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240724-linux-x86_64-brandtbucher-load_attr_property-3.14.0a0-0b4c6da |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.90 ms: 1.01x slower                                                     |
| regex_compile  | 131 ms                                                 | 134 ms: 1.02x slower                                                      |
| regex_v8       | 25.3 ms                                                | 26.3 ms: 1.04x slower                                                     |
| regex_dna      | 220 ms                                                 | 230 ms: 1.04x slower                                                      |
| Geometric mean | (ref)                                                  | 1.03x slower                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240724-linux-x86_64-brandtbucher-load_attr_property-3.14.0a0-0b4c6da |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 2.11 sec                                               | 1.95 sec: 1.09x faster                                                    |
| xml_etree_generate   | 87.0 ms                                                | 80.6 ms: 1.08x faster                                                     |
| xml_etree_process    | 60.4 ms                                                | 56.9 ms: 1.06x faster                                                     |
| xml_etree_parse      | 156 ms                                                 | 148 ms: 1.05x faster                                                      |
| xml_etree_iterparse  | 102 ms                                                 | 98.6 ms: 1.04x faster                                                     |
| pickle_pure_python   | 300 us                                                 | 295 us: 1.02x faster                                                      |
| unpickle_pure_python | 213 us                                                 | 217 us: 1.02x slower                                                      |
| json_loads           | 27.0 us                                                | 28.3 us: 1.05x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                              |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240724-linux-x86_64-brandtbucher-load_attr_property-3.14.0a0-0b4c6da |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.6 ms: 1.00x slower                                                     |
| python_startup_no_site | 6.99 ms                                                | 7.17 ms: 1.03x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240724-linux-x86_64-brandtbucher-load_attr_property-3.14.0a0-0b4c6da |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.96 ms: 1.11x faster                                                     |
| django_template | 34.4 ms                                                | 35.9 ms: 1.04x slower                                                     |
| genshi_text     | 22.9 ms                                                | 24.5 ms: 1.07x slower                                                     |
| genshi_xml      | 50.3 ms                                                | 57.5 ms: 1.14x slower                                                     |
| Geometric mean  | (ref)                                                  | 1.03x slower                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240724-linux-x86_64-brandtbucher-load_attr_property-3.14.0a0-0b4c6da |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| deepcopy_memo              | 38.0 us                                                | 28.4 us: 1.34x faster                                                     |
| deepcopy                   | 352 us                                                 | 274 us: 1.29x faster                                                      |
| scimark_fft                | 369 ms                                                 | 305 ms: 1.21x faster                                                      |
| richards                   | 48.1 ms                                                | 39.9 ms: 1.21x faster                                                     |
| async_tree_memoization_tg  | 465 ms                                                 | 393 ms: 1.18x faster                                                      |
| richards_super             | 54.4 ms                                                | 46.6 ms: 1.17x faster                                                     |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.35 ms: 1.16x faster                                                     |
| deepcopy_reduce            | 3.17 us                                                | 2.75 us: 1.15x faster                                                     |
| spectral_norm              | 115 ms                                                 | 101 ms: 1.14x faster                                                      |
| mako                       | 11.1 ms                                                | 9.96 ms: 1.11x faster                                                     |
| float                      | 78.5 ms                                                | 70.7 ms: 1.11x faster                                                     |
| scimark_monte_carlo        | 66.3 ms                                                | 60.5 ms: 1.10x faster                                                     |
| crypto_pyaes               | 73.0 ms                                                | 66.6 ms: 1.09x faster                                                     |
| async_tree_none            | 354 ms                                                 | 326 ms: 1.09x faster                                                      |
| mdp                        | 2.74 sec                                               | 2.52 sec: 1.09x faster                                                    |
| tomli_loads                | 2.11 sec                                               | 1.95 sec: 1.09x faster                                                    |
| xml_etree_generate         | 87.0 ms                                                | 80.6 ms: 1.08x faster                                                     |
| telco                      | 8.45 ms                                                | 7.89 ms: 1.07x faster                                                     |
| pathlib                    | 17.1 ms                                                | 16.0 ms: 1.07x faster                                                     |
| xml_etree_process          | 60.4 ms                                                | 56.9 ms: 1.06x faster                                                     |
| pprint_safe_repr           | 744 ms                                                 | 702 ms: 1.06x faster                                                      |
| nbody                      | 85.7 ms                                                | 81.0 ms: 1.06x faster                                                     |
| xml_etree_parse            | 156 ms                                                 | 148 ms: 1.05x faster                                                      |
| async_tree_none_tg         | 320 ms                                                 | 304 ms: 1.05x faster                                                      |
| pyflate                    | 460 ms                                                 | 438 ms: 1.05x faster                                                      |
| pprint_pformat             | 1.51 sec                                               | 1.45 sec: 1.04x faster                                                    |
| xml_etree_iterparse        | 102 ms                                                 | 98.6 ms: 1.04x faster                                                     |
| async_tree_memoization     | 442 ms                                                 | 428 ms: 1.03x faster                                                      |
| logging_format             | 6.25 us                                                | 6.08 us: 1.03x faster                                                     |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 528 ms: 1.03x faster                                                      |
| bpe_tokeniser              | 4.69 sec                                               | 4.56 sec: 1.03x faster                                                    |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 560 ms: 1.03x faster                                                      |
| logging_simple             | 5.66 us                                                | 5.54 us: 1.02x faster                                                     |
| pycparser                  | 1.19 sec                                               | 1.17 sec: 1.02x faster                                                    |
| fannkuch                   | 381 ms                                                 | 374 ms: 1.02x faster                                                      |
| generators                 | 28.8 ms                                                | 28.3 ms: 1.02x faster                                                     |
| pickle_pure_python         | 300 us                                                 | 295 us: 1.02x faster                                                      |
| meteor_contest             | 108 ms                                                 | 106 ms: 1.02x faster                                                      |
| json                       | 5.20 ms                                                | 5.15 ms: 1.01x faster                                                     |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                                      |
| python_startup             | 10.6 ms                                                | 10.6 ms: 1.00x slower                                                     |
| html5lib                   | 64.5 ms                                                | 64.8 ms: 1.00x slower                                                     |
| asyncio_websockets         | 555 ms                                                 | 558 ms: 1.00x slower                                                      |
| regex_effbot               | 3.88 ms                                                | 3.90 ms: 1.01x slower                                                     |
| sqlglot_transpile          | 1.57 ms                                                | 1.58 ms: 1.01x slower                                                     |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.80 sec: 1.01x slower                                                    |
| bench_thread_pool          | 815 us                                                 | 825 us: 1.01x slower                                                      |
| tornado_http               | 91.5 ms                                                | 92.9 ms: 1.02x slower                                                     |
| raytrace                   | 262 ms                                                 | 266 ms: 1.02x slower                                                      |
| go                         | 142 ms                                                 | 144 ms: 1.02x slower                                                      |
| unpickle_pure_python       | 213 us                                                 | 217 us: 1.02x slower                                                      |
| coroutines                 | 22.5 ms                                                | 23.0 ms: 1.02x slower                                                     |
| gc_traversal               | 3.81 ms                                                | 3.89 ms: 1.02x slower                                                     |
| regex_compile              | 131 ms                                                 | 134 ms: 1.02x slower                                                      |
| 2to3                       | 265 ms                                                 | 271 ms: 1.02x slower                                                      |
| python_startup_no_site     | 6.99 ms                                                | 7.17 ms: 1.03x slower                                                     |
| asyncio_tcp                | 488 ms                                                 | 504 ms: 1.03x slower                                                      |
| sqlglot_optimize           | 53.9 ms                                                | 56.0 ms: 1.04x slower                                                     |
| scimark_sor                | 122 ms                                                 | 127 ms: 1.04x slower                                                      |
| async_generators           | 433 ms                                                 | 450 ms: 1.04x slower                                                      |
| regex_v8                   | 25.3 ms                                                | 26.3 ms: 1.04x slower                                                     |
| sqlglot_normalize          | 107 ms                                                 | 112 ms: 1.04x slower                                                      |
| django_template            | 34.4 ms                                                | 35.9 ms: 1.04x slower                                                     |
| regex_dna                  | 220 ms                                                 | 230 ms: 1.04x slower                                                      |
| json_loads                 | 27.0 us                                                | 28.3 us: 1.05x slower                                                     |
| async_tree_io_tg           | 825 ms                                                 | 875 ms: 1.06x slower                                                      |
| hexiom                     | 6.13 ms                                                | 6.55 ms: 1.07x slower                                                     |
| genshi_text                | 22.9 ms                                                | 24.5 ms: 1.07x slower                                                     |
| dask                       | 338 ms                                                 | 362 ms: 1.07x slower                                                      |
| sympy_str                  | 274 ms                                                 | 293 ms: 1.07x slower                                                      |
| async_tree_io              | 843 ms                                                 | 905 ms: 1.07x slower                                                      |
| dulwich_log                | 63.0 ms                                                | 67.7 ms: 1.07x slower                                                     |
| typing_runtime_protocols   | 159 us                                                 | 171 us: 1.08x slower                                                      |
| sympy_expand               | 462 ms                                                 | 498 ms: 1.08x slower                                                      |
| nqueens                    | 80.6 ms                                                | 87.0 ms: 1.08x slower                                                     |
| scimark_lu                 | 115 ms                                                 | 125 ms: 1.08x slower                                                      |
| create_gc_cycles           | 1.61 ms                                                | 1.76 ms: 1.10x slower                                                     |
| coverage                   | 83.7 ms                                                | 92.3 ms: 1.10x slower                                                     |
| sympy_integrate            | 19.9 ms                                                | 22.1 ms: 1.11x slower                                                     |
| pylint                     | 313 ms                                                 | 348 ms: 1.11x slower                                                      |
| sympy_sum                  | 150 ms                                                 | 167 ms: 1.12x slower                                                      |
| docutils                   | 2.58 sec                                               | 2.90 sec: 1.12x slower                                                    |
| deltablue                  | 3.15 ms                                                | 3.54 ms: 1.12x slower                                                     |
| genshi_xml                 | 50.3 ms                                                | 57.5 ms: 1.14x slower                                                     |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                              |

Benchmark hidden because not significant (7): thrift, sqlglot_parse, logging_silent, chaos, json_dumps, bench_mp_pool, comprehensions
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 56.53% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.08x