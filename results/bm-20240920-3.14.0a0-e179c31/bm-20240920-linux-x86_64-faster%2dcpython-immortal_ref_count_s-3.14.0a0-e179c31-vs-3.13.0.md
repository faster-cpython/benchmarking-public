# Results vs. 3.13.0

- fork: faster-cpython
- ref: immortal_ref_count_s
- machine: linux-x86_64
- commit hash: e179c31
- commit date: 2024-09-20
- overall geometric mean: 1.02x faster
- HPT reliability: 99.48%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-linux-x86_64-faster%2dcpython-immortal_ref_count_s-3.14.0a0-e179c31 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 255 ms: 1.04x faster                                                            |
| docutils       | 2.58 sec                                               | 2.65 sec: 1.02x slower                                                          |
| html5lib       | 64.5 ms                                                | 62.2 ms: 1.04x faster                                                           |
| tornado_http   | 91.5 ms                                                | 89.8 ms: 1.02x faster                                                           |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-linux-x86_64-faster%2dcpython-immortal_ref_count_s-3.14.0a0-e179c31 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 465 ms                                                 | 385 ms: 1.21x faster                                                            |
| async_tree_none            | 354 ms                                                 | 310 ms: 1.14x faster                                                            |
| async_tree_memoization     | 442 ms                                                 | 391 ms: 1.13x faster                                                            |
| async_tree_none_tg         | 320 ms                                                 | 297 ms: 1.08x faster                                                            |
| asyncio_tcp                | 488 ms                                                 | 468 ms: 1.04x faster                                                            |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 563 ms: 1.02x faster                                                            |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.79 sec: 1.00x faster                                                          |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 554 ms: 1.02x slower                                                            |
| coroutines                 | 22.5 ms                                                | 23.4 ms: 1.04x slower                                                           |
| async_tree_io_tg           | 825 ms                                                 | 868 ms: 1.05x slower                                                            |
| Geometric mean             | (ref)                                                  | 1.04x faster                                                                    |

Benchmark hidden because not significant (3): async_generators, asyncio_websockets, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-linux-x86_64-faster%2dcpython-immortal_ref_count_s-3.14.0a0-e179c31 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 76.6 ms: 1.02x faster                                                           |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x slower                                                            |
| nbody          | 85.7 ms                                                | 89.9 ms: 1.05x slower                                                           |
| Geometric mean | (ref)                                                  | 1.01x slower                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-linux-x86_64-faster%2dcpython-immortal_ref_count_s-3.14.0a0-e179c31 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.68 ms: 1.05x faster                                                           |
| regex_compile  | 131 ms                                                 | 127 ms: 1.03x faster                                                            |
| regex_v8       | 25.3 ms                                                | 24.7 ms: 1.02x faster                                                           |
| regex_dna      | 220 ms                                                 | 225 ms: 1.02x slower                                                            |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-linux-x86_64-faster%2dcpython-immortal_ref_count_s-3.14.0a0-e179c31 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_process    | 60.4 ms                                                | 58.7 ms: 1.03x faster                                                           |
| json_dumps           | 10.4 ms                                                | 10.1 ms: 1.03x faster                                                           |
| xml_etree_generate   | 87.0 ms                                                | 84.8 ms: 1.03x faster                                                           |
| xml_etree_parse      | 156 ms                                                 | 154 ms: 1.01x faster                                                            |
| tomli_loads          | 2.11 sec                                               | 2.10 sec: 1.01x faster                                                          |
| json_loads           | 27.0 us                                                | 26.8 us: 1.01x faster                                                           |
| unpickle_pure_python | 213 us                                                 | 214 us: 1.01x slower                                                            |
| pickle               | 11.6 us                                                | 11.7 us: 1.01x slower                                                           |
| pickle_pure_python   | 300 us                                                 | 304 us: 1.01x slower                                                            |
| xml_etree_iterparse  | 102 ms                                                 | 105 ms: 1.03x slower                                                            |
| pickle_list          | 5.01 us                                                | 5.18 us: 1.03x slower                                                           |
| unpickle_list        | 4.96 us                                                | 5.27 us: 1.06x slower                                                           |
| pickle_dict          | 33.2 us                                                | 35.4 us: 1.07x slower                                                           |
| unpickle             | 14.9 us                                                | 16.0 us: 1.08x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-linux-x86_64-faster%2dcpython-immortal_ref_count_s-3.14.0a0-e179c31 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.5 ms: 1.01x faster                                                           |
| python_startup_no_site | 6.99 ms                                                | 7.00 ms: 1.00x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.00x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-linux-x86_64-faster%2dcpython-immortal_ref_count_s-3.14.0a0-e179c31 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_text    | 22.9 ms                                                | 21.9 ms: 1.04x faster                                                           |
| genshi_xml     | 50.3 ms                                                | 49.2 ms: 1.02x faster                                                           |
| mako           | 11.1 ms                                                | 11.4 ms: 1.02x slower                                                           |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                    |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-linux-x86_64-faster%2dcpython-immortal_ref_count_s-3.14.0a0-e179c31 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| deepcopy                   | 352 us                                                 | 256 us: 1.37x faster                                                            |
| deepcopy_memo              | 38.0 us                                                | 30.4 us: 1.25x faster                                                           |
| async_tree_memoization_tg  | 465 ms                                                 | 385 ms: 1.21x faster                                                            |
| deepcopy_reduce            | 3.17 us                                                | 2.67 us: 1.19x faster                                                           |
| go                         | 142 ms                                                 | 120 ms: 1.18x faster                                                            |
| async_tree_none            | 354 ms                                                 | 310 ms: 1.14x faster                                                            |
| async_tree_memoization     | 442 ms                                                 | 391 ms: 1.13x faster                                                            |
| async_tree_none_tg         | 320 ms                                                 | 297 ms: 1.08x faster                                                            |
| gc_traversal               | 3.81 ms                                                | 3.55 ms: 1.07x faster                                                           |
| json                       | 5.20 ms                                                | 4.86 ms: 1.07x faster                                                           |
| pathlib                    | 17.1 ms                                                | 16.1 ms: 1.06x faster                                                           |
| regex_effbot               | 3.88 ms                                                | 3.68 ms: 1.05x faster                                                           |
| pprint_safe_repr           | 744 ms                                                 | 710 ms: 1.05x faster                                                            |
| asyncio_tcp                | 488 ms                                                 | 468 ms: 1.04x faster                                                            |
| thrift                     | 796 us                                                 | 763 us: 1.04x faster                                                            |
| genshi_text                | 22.9 ms                                                | 21.9 ms: 1.04x faster                                                           |
| richards_super             | 54.4 ms                                                | 52.3 ms: 1.04x faster                                                           |
| 2to3                       | 265 ms                                                 | 255 ms: 1.04x faster                                                            |
| html5lib                   | 64.5 ms                                                | 62.2 ms: 1.04x faster                                                           |
| pprint_pformat             | 1.51 sec                                               | 1.46 sec: 1.04x faster                                                          |
| richards                   | 48.1 ms                                                | 46.5 ms: 1.04x faster                                                           |
| generators                 | 28.8 ms                                                | 27.9 ms: 1.03x faster                                                           |
| bench_thread_pool          | 815 us                                                 | 791 us: 1.03x faster                                                            |
| regex_compile              | 131 ms                                                 | 127 ms: 1.03x faster                                                            |
| xml_etree_process          | 60.4 ms                                                | 58.7 ms: 1.03x faster                                                           |
| crypto_pyaes               | 73.0 ms                                                | 71.0 ms: 1.03x faster                                                           |
| json_dumps                 | 10.4 ms                                                | 10.1 ms: 1.03x faster                                                           |
| xml_etree_generate         | 87.0 ms                                                | 84.8 ms: 1.03x faster                                                           |
| float                      | 78.5 ms                                                | 76.6 ms: 1.02x faster                                                           |
| scimark_lu                 | 115 ms                                                 | 112 ms: 1.02x faster                                                            |
| pycparser                  | 1.19 sec                                               | 1.17 sec: 1.02x faster                                                          |
| genshi_xml                 | 50.3 ms                                                | 49.2 ms: 1.02x faster                                                           |
| regex_v8                   | 25.3 ms                                                | 24.7 ms: 1.02x faster                                                           |
| sympy_str                  | 274 ms                                                 | 268 ms: 1.02x faster                                                            |
| nqueens                    | 80.6 ms                                                | 78.9 ms: 1.02x faster                                                           |
| sympy_sum                  | 150 ms                                                 | 146 ms: 1.02x faster                                                            |
| sqlglot_optimize           | 53.9 ms                                                | 52.9 ms: 1.02x faster                                                           |
| tornado_http               | 91.5 ms                                                | 89.8 ms: 1.02x faster                                                           |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 563 ms: 1.02x faster                                                            |
| sympy_integrate            | 19.9 ms                                                | 19.5 ms: 1.02x faster                                                           |
| mdp                        | 2.74 sec                                               | 2.69 sec: 1.02x faster                                                          |
| spectral_norm              | 115 ms                                                 | 113 ms: 1.02x faster                                                            |
| sqlglot_normalize          | 107 ms                                                 | 106 ms: 1.02x faster                                                            |
| xml_etree_parse            | 156 ms                                                 | 154 ms: 1.01x faster                                                            |
| typing_runtime_protocols   | 159 us                                                 | 157 us: 1.01x faster                                                            |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.96 ms: 1.01x faster                                                           |
| logging_simple             | 5.66 us                                                | 5.59 us: 1.01x faster                                                           |
| sympy_expand               | 462 ms                                                 | 456 ms: 1.01x faster                                                            |
| logging_format             | 6.25 us                                                | 6.19 us: 1.01x faster                                                           |
| meteor_contest             | 108 ms                                                 | 107 ms: 1.01x faster                                                            |
| python_startup             | 10.6 ms                                                | 10.5 ms: 1.01x faster                                                           |
| tomli_loads                | 2.11 sec                                               | 2.10 sec: 1.01x faster                                                          |
| json_loads                 | 27.0 us                                                | 26.8 us: 1.01x faster                                                           |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.79 sec: 1.00x faster                                                          |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x slower                                                            |
| python_startup_no_site     | 6.99 ms                                                | 7.00 ms: 1.00x slower                                                           |
| sqlglot_transpile          | 1.57 ms                                                | 1.58 ms: 1.00x slower                                                           |
| unpickle_pure_python       | 213 us                                                 | 214 us: 1.01x slower                                                            |
| comprehensions             | 16.4 us                                                | 16.5 us: 1.01x slower                                                           |
| sqlglot_parse              | 1.27 ms                                                | 1.28 ms: 1.01x slower                                                           |
| chaos                      | 58.4 ms                                                | 59.0 ms: 1.01x slower                                                           |
| scimark_sor                | 122 ms                                                 | 124 ms: 1.01x slower                                                            |
| pickle                     | 11.6 us                                                | 11.7 us: 1.01x slower                                                           |
| hexiom                     | 6.13 ms                                                | 6.20 ms: 1.01x slower                                                           |
| pickle_pure_python         | 300 us                                                 | 304 us: 1.01x slower                                                            |
| raytrace                   | 262 ms                                                 | 265 ms: 1.01x slower                                                            |
| logging_silent             | 102 ns                                                 | 104 ns: 1.02x slower                                                            |
| bpe_tokeniser              | 4.69 sec                                               | 4.77 sec: 1.02x slower                                                          |
| pyflate                    | 460 ms                                                 | 468 ms: 1.02x slower                                                            |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 554 ms: 1.02x slower                                                            |
| scimark_monte_carlo        | 66.3 ms                                                | 67.7 ms: 1.02x slower                                                           |
| dulwich_log                | 63.0 ms                                                | 64.3 ms: 1.02x slower                                                           |
| regex_dna                  | 220 ms                                                 | 225 ms: 1.02x slower                                                            |
| mako                       | 11.1 ms                                                | 11.4 ms: 1.02x slower                                                           |
| docutils                   | 2.58 sec                                               | 2.65 sec: 1.02x slower                                                          |
| xml_etree_iterparse        | 102 ms                                                 | 105 ms: 1.03x slower                                                            |
| pickle_list                | 5.01 us                                                | 5.18 us: 1.03x slower                                                           |
| coverage                   | 83.7 ms                                                | 86.8 ms: 1.04x slower                                                           |
| deltablue                  | 3.15 ms                                                | 3.28 ms: 1.04x slower                                                           |
| coroutines                 | 22.5 ms                                                | 23.4 ms: 1.04x slower                                                           |
| nbody                      | 85.7 ms                                                | 89.9 ms: 1.05x slower                                                           |
| async_tree_io_tg           | 825 ms                                                 | 868 ms: 1.05x slower                                                            |
| fannkuch                   | 381 ms                                                 | 404 ms: 1.06x slower                                                            |
| unpickle_list              | 4.96 us                                                | 5.27 us: 1.06x slower                                                           |
| pickle_dict                | 33.2 us                                                | 35.4 us: 1.07x slower                                                           |
| unpickle                   | 14.9 us                                                | 16.0 us: 1.08x slower                                                           |
| create_gc_cycles           | 1.61 ms                                                | 1.73 ms: 1.08x slower                                                           |
| unpack_sequence            | 42.4 ns                                                | 46.4 ns: 1.10x slower                                                           |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                                    |

Benchmark hidden because not significant (9): scimark_fft, async_generators, sqlite_synth, bench_mp_pool, django_template, asyncio_websockets, telco, async_tree_io, pylint
Ignored benchmarks (7) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 99.48% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x