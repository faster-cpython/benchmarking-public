# Results vs. 3.13.0

- fork: python
- ref: 342e654b8eda24c68da6
- machine: linux-x86_64
- commit hash: 342e654
- commit date: 2024-09-20
- overall geometric mean: 1.02x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                       | 282 ms: 1.03x faster                                                        |
| docutils       | 2.81 sec                                                     | 2.90 sec: 1.03x slower                                                      |
| html5lib       | 71.9 ms                                                      | 72.4 ms: 1.01x slower                                                       |
| tornado_http   | 120 ms                                                       | 117 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                        | 1.00x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 461 ms                                                       | 390 ms: 1.18x faster                                                        |
| async_tree_none            | 372 ms                                                       | 323 ms: 1.15x faster                                                        |
| async_tree_memoization     | 452 ms                                                       | 400 ms: 1.13x faster                                                        |
| async_tree_none_tg         | 340 ms                                                       | 310 ms: 1.10x faster                                                        |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 543 ms: 1.06x faster                                                        |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 570 ms: 1.05x faster                                                        |
| async_tree_io              | 847 ms                                                       | 807 ms: 1.05x faster                                                        |
| async_tree_io_tg           | 819 ms                                                       | 790 ms: 1.04x faster                                                        |
| asyncio_tcp                | 380 ms                                                       | 372 ms: 1.02x faster                                                        |
| asyncio_tcp_ssl            | 1.58 sec                                                     | 1.57 sec: 1.01x faster                                                      |
| coroutines                 | 21.6 ms                                                      | 22.0 ms: 1.02x slower                                                       |
| asyncio_websockets         | 382 ms                                                       | 397 ms: 1.04x slower                                                        |
| Geometric mean             | (ref)                                                        | 1.05x faster                                                                |

Benchmark hidden because not significant (1): async_generators

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 81.9 ms                                                      | 78.2 ms: 1.05x faster                                                       |
| nbody          | 88.0 ms                                                      | 91.6 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                        | 1.00x faster                                                                |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                      | 25.2 ms: 1.04x faster                                                       |
| regex_compile  | 144 ms                                                       | 142 ms: 1.02x faster                                                        |
| regex_effbot   | 3.37 ms                                                      | 3.61 ms: 1.07x slower                                                       |
| Geometric mean | (ref)                                                        | 1.00x slower                                                                |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_list          | 4.59 us                                                      | 4.28 us: 1.07x faster                                                       |
| pickle_dict          | 32.1 us                                                      | 30.3 us: 1.06x faster                                                       |
| pickle               | 10.5 us                                                      | 10.2 us: 1.03x faster                                                       |
| json_dumps           | 11.0 ms                                                      | 10.6 ms: 1.03x faster                                                       |
| xml_etree_parse      | 145 ms                                                       | 141 ms: 1.03x faster                                                        |
| xml_etree_process    | 60.9 ms                                                      | 59.4 ms: 1.02x faster                                                       |
| unpickle             | 15.1 us                                                      | 15.1 us: 1.01x faster                                                       |
| xml_etree_generate   | 85.3 ms                                                      | 84.9 ms: 1.00x faster                                                       |
| pickle_pure_python   | 318 us                                                       | 321 us: 1.01x slower                                                        |
| unpickle_list        | 4.62 us                                                      | 4.69 us: 1.01x slower                                                       |
| json_loads           | 24.0 us                                                      | 24.6 us: 1.02x slower                                                       |
| unpickle_pure_python | 214 us                                                       | 229 us: 1.07x slower                                                        |
| tomli_loads          | 2.41 sec                                                     | 2.63 sec: 1.09x slower                                                      |
| Geometric mean       | (ref)                                                        | 1.00x faster                                                                |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup | 13.3 ms                                                      | 13.3 ms: 1.00x slower                                                       |
| Geometric mean | (ref)                                                        | 1.00x slower                                                                |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 26.6 ms                                                      | 25.7 ms: 1.04x faster                                                       |
| genshi_xml      | 57.3 ms                                                      | 56.4 ms: 1.02x faster                                                       |
| django_template | 38.9 ms                                                      | 39.5 ms: 1.02x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.01x faster                                                                |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy                   | 397 us                                                       | 284 us: 1.40x faster                                                        |
| deepcopy_memo              | 39.5 us                                                      | 29.3 us: 1.35x faster                                                       |
| deepcopy_reduce            | 3.54 us                                                      | 2.86 us: 1.24x faster                                                       |
| async_tree_memoization_tg  | 461 ms                                                       | 390 ms: 1.18x faster                                                        |
| go                         | 160 ms                                                       | 139 ms: 1.15x faster                                                        |
| async_tree_none            | 372 ms                                                       | 323 ms: 1.15x faster                                                        |
| generators                 | 33.5 ms                                                      | 29.6 ms: 1.13x faster                                                       |
| async_tree_memoization     | 452 ms                                                       | 400 ms: 1.13x faster                                                        |
| pathlib                    | 17.4 ms                                                      | 15.7 ms: 1.11x faster                                                       |
| async_tree_none_tg         | 340 ms                                                       | 310 ms: 1.10x faster                                                        |
| unpack_sequence            | 56.8 ns                                                      | 52.6 ns: 1.08x faster                                                       |
| pickle_list                | 4.59 us                                                      | 4.28 us: 1.07x faster                                                       |
| pickle_dict                | 32.1 us                                                      | 30.3 us: 1.06x faster                                                       |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 543 ms: 1.06x faster                                                        |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 570 ms: 1.05x faster                                                        |
| bench_thread_pool          | 901 us                                                       | 857 us: 1.05x faster                                                        |
| richards_super             | 59.8 ms                                                      | 57.0 ms: 1.05x faster                                                       |
| async_tree_io              | 847 ms                                                       | 807 ms: 1.05x faster                                                        |
| float                      | 81.9 ms                                                      | 78.2 ms: 1.05x faster                                                       |
| scimark_sor                | 126 ms                                                       | 120 ms: 1.05x faster                                                        |
| regex_v8                   | 26.2 ms                                                      | 25.2 ms: 1.04x faster                                                       |
| scimark_sparse_mat_mult    | 4.29 ms                                                      | 4.12 ms: 1.04x faster                                                       |
| genshi_text                | 26.6 ms                                                      | 25.7 ms: 1.04x faster                                                       |
| async_tree_io_tg           | 819 ms                                                       | 790 ms: 1.04x faster                                                        |
| richards                   | 52.7 ms                                                      | 50.9 ms: 1.04x faster                                                       |
| pickle                     | 10.5 us                                                      | 10.2 us: 1.03x faster                                                       |
| bpe_tokeniser              | 5.10 sec                                                     | 4.94 sec: 1.03x faster                                                      |
| scimark_fft                | 314 ms                                                       | 305 ms: 1.03x faster                                                        |
| sqlglot_optimize           | 59.7 ms                                                      | 57.9 ms: 1.03x faster                                                       |
| json_dumps                 | 11.0 ms                                                      | 10.6 ms: 1.03x faster                                                       |
| 2to3                       | 291 ms                                                       | 282 ms: 1.03x faster                                                        |
| thrift                     | 877 us                                                       | 851 us: 1.03x faster                                                        |
| pycparser                  | 1.26 sec                                                     | 1.22 sec: 1.03x faster                                                      |
| xml_etree_parse            | 145 ms                                                       | 141 ms: 1.03x faster                                                        |
| telco                      | 8.58 ms                                                      | 8.34 ms: 1.03x faster                                                       |
| hexiom                     | 6.33 ms                                                      | 6.16 ms: 1.03x faster                                                       |
| tornado_http               | 120 ms                                                       | 117 ms: 1.03x faster                                                        |
| xml_etree_process          | 60.9 ms                                                      | 59.4 ms: 1.02x faster                                                       |
| asyncio_tcp                | 380 ms                                                       | 372 ms: 1.02x faster                                                        |
| coverage                   | 81.1 ms                                                      | 79.6 ms: 1.02x faster                                                       |
| regex_compile              | 144 ms                                                       | 142 ms: 1.02x faster                                                        |
| pyflate                    | 492 ms                                                       | 483 ms: 1.02x faster                                                        |
| sqlglot_normalize          | 118 ms                                                       | 116 ms: 1.02x faster                                                        |
| genshi_xml                 | 57.3 ms                                                      | 56.4 ms: 1.02x faster                                                       |
| sympy_integrate            | 23.3 ms                                                      | 23.0 ms: 1.01x faster                                                       |
| meteor_contest             | 128 ms                                                       | 127 ms: 1.01x faster                                                        |
| logging_format             | 7.07 us                                                      | 6.98 us: 1.01x faster                                                       |
| comprehensions             | 17.3 us                                                      | 17.0 us: 1.01x faster                                                       |
| pprint_safe_repr           | 812 ms                                                       | 802 ms: 1.01x faster                                                        |
| sympy_sum                  | 154 ms                                                       | 152 ms: 1.01x faster                                                        |
| raytrace                   | 289 ms                                                       | 286 ms: 1.01x faster                                                        |
| fannkuch                   | 365 ms                                                       | 361 ms: 1.01x faster                                                        |
| sympy_expand               | 505 ms                                                       | 501 ms: 1.01x faster                                                        |
| pprint_pformat             | 1.65 sec                                                     | 1.64 sec: 1.01x faster                                                      |
| sqlite_synth               | 2.79 us                                                      | 2.77 us: 1.01x faster                                                       |
| spectral_norm              | 97.4 ms                                                      | 96.7 ms: 1.01x faster                                                       |
| unpickle                   | 15.1 us                                                      | 15.1 us: 1.01x faster                                                       |
| asyncio_tcp_ssl            | 1.58 sec                                                     | 1.57 sec: 1.01x faster                                                      |
| xml_etree_generate         | 85.3 ms                                                      | 84.9 ms: 1.00x faster                                                       |
| python_startup             | 13.3 ms                                                      | 13.3 ms: 1.00x slower                                                       |
| crypto_pyaes               | 72.8 ms                                                      | 73.2 ms: 1.01x slower                                                       |
| html5lib                   | 71.9 ms                                                      | 72.4 ms: 1.01x slower                                                       |
| pickle_pure_python         | 318 us                                                       | 321 us: 1.01x slower                                                        |
| sqlglot_transpile          | 1.78 ms                                                      | 1.80 ms: 1.01x slower                                                       |
| nqueens                    | 88.2 ms                                                      | 89.1 ms: 1.01x slower                                                       |
| typing_runtime_protocols   | 174 us                                                       | 176 us: 1.01x slower                                                        |
| scimark_lu                 | 97.8 ms                                                      | 99.0 ms: 1.01x slower                                                       |
| dulwich_log                | 65.5 ms                                                      | 66.4 ms: 1.01x slower                                                       |
| unpickle_list              | 4.62 us                                                      | 4.69 us: 1.01x slower                                                       |
| django_template            | 38.9 ms                                                      | 39.5 ms: 1.02x slower                                                       |
| coroutines                 | 21.6 ms                                                      | 22.0 ms: 1.02x slower                                                       |
| logging_silent             | 97.7 ns                                                      | 99.7 ns: 1.02x slower                                                       |
| json_loads                 | 24.0 us                                                      | 24.6 us: 1.02x slower                                                       |
| sqlglot_parse              | 1.38 ms                                                      | 1.42 ms: 1.03x slower                                                       |
| chaos                      | 61.7 ms                                                      | 63.4 ms: 1.03x slower                                                       |
| scimark_monte_carlo        | 64.9 ms                                                      | 67.1 ms: 1.03x slower                                                       |
| docutils                   | 2.81 sec                                                     | 2.90 sec: 1.03x slower                                                      |
| asyncio_websockets         | 382 ms                                                       | 397 ms: 1.04x slower                                                        |
| nbody                      | 88.0 ms                                                      | 91.6 ms: 1.04x slower                                                       |
| unpickle_pure_python       | 214 us                                                       | 229 us: 1.07x slower                                                        |
| regex_effbot               | 3.37 ms                                                      | 3.61 ms: 1.07x slower                                                       |
| gc_traversal               | 4.11 ms                                                      | 4.49 ms: 1.09x slower                                                       |
| tomli_loads                | 2.41 sec                                                     | 2.63 sec: 1.09x slower                                                      |
| create_gc_cycles           | 1.76 ms                                                      | 1.99 ms: 1.13x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.02x faster                                                                |

Benchmark hidden because not significant (13): mako, logging_simple, mdp, async_generators, python_startup_no_site, pidigits, sympy_str, xml_etree_iterparse, deltablue, regex_dna, bench_mp_pool, json, pylint
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x