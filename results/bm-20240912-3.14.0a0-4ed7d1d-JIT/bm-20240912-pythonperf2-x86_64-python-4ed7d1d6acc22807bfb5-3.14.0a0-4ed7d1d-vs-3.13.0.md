# Results vs. 3.13.0

- fork: python
- ref: 4ed7d1d6acc22807bfb5
- machine: linux-x86_64
- commit hash: 4ed7d1d
- commit date: 2024-09-12
- overall geometric mean: 1.01x faster
- HPT reliability: 82.32%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-pythonperf2-x86_64-python-4ed7d1d6acc22807bfb5-3.14.0a0-4ed7d1d |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                       | 309 ms: 1.06x slower                                                        |
| docutils       | 2.81 sec                                                     | 3.15 sec: 1.12x slower                                                      |
| html5lib       | 71.9 ms                                                      | 71.1 ms: 1.01x faster                                                       |
| tornado_http   | 120 ms                                                       | 122 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                        | 1.05x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-pythonperf2-x86_64-python-4ed7d1d6acc22807bfb5-3.14.0a0-4ed7d1d |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 461 ms                                                       | 393 ms: 1.17x faster                                                        |
| async_tree_none            | 372 ms                                                       | 323 ms: 1.15x faster                                                        |
| async_tree_memoization     | 452 ms                                                       | 404 ms: 1.12x faster                                                        |
| async_tree_none_tg         | 340 ms                                                       | 311 ms: 1.09x faster                                                        |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 549 ms: 1.05x faster                                                        |
| async_tree_io              | 847 ms                                                       | 812 ms: 1.04x faster                                                        |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 576 ms: 1.04x faster                                                        |
| asyncio_tcp                | 380 ms                                                       | 377 ms: 1.01x faster                                                        |
| asyncio_tcp_ssl            | 1.58 sec                                                     | 1.58 sec: 1.00x slower                                                      |
| asyncio_websockets         | 382 ms                                                       | 395 ms: 1.03x slower                                                        |
| async_generators           | 359 ms                                                       | 393 ms: 1.09x slower                                                        |
| Geometric mean             | (ref)                                                        | 1.04x faster                                                                |

Benchmark hidden because not significant (2): coroutines, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-pythonperf2-x86_64-python-4ed7d1d6acc22807bfb5-3.14.0a0-4ed7d1d |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 81.9 ms                                                      | 74.6 ms: 1.10x faster                                                       |
| nbody          | 88.0 ms                                                      | 81.8 ms: 1.08x faster                                                       |
| pidigits       | 253 ms                                                       | 250 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                        | 1.06x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-pythonperf2-x86_64-python-4ed7d1d6acc22807bfb5-3.14.0a0-4ed7d1d |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 244 ms                                                       | 233 ms: 1.05x faster                                                        |
| regex_v8       | 26.2 ms                                                      | 25.7 ms: 1.02x faster                                                       |
| regex_compile  | 144 ms                                                       | 147 ms: 1.02x slower                                                        |
| regex_effbot   | 3.37 ms                                                      | 3.49 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                        | 1.00x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-pythonperf2-x86_64-python-4ed7d1d6acc22807bfb5-3.14.0a0-4ed7d1d |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.41 sec                                                     | 2.13 sec: 1.13x faster                                                      |
| pickle_list          | 4.59 us                                                      | 4.18 us: 1.10x faster                                                       |
| xml_etree_process    | 60.9 ms                                                      | 55.9 ms: 1.09x faster                                                       |
| pickle_dict          | 32.1 us                                                      | 29.5 us: 1.09x faster                                                       |
| xml_etree_generate   | 85.3 ms                                                      | 80.1 ms: 1.07x faster                                                       |
| json_dumps           | 11.0 ms                                                      | 10.6 ms: 1.03x faster                                                       |
| pickle               | 10.5 us                                                      | 10.4 us: 1.01x faster                                                       |
| xml_etree_iterparse  | 100 ms                                                       | 98.9 ms: 1.01x faster                                                       |
| xml_etree_parse      | 145 ms                                                       | 143 ms: 1.01x faster                                                        |
| unpickle_list        | 4.62 us                                                      | 4.72 us: 1.02x slower                                                       |
| pickle_pure_python   | 318 us                                                       | 326 us: 1.02x slower                                                        |
| unpickle_pure_python | 214 us                                                       | 220 us: 1.03x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.03x faster                                                                |

Benchmark hidden because not significant (2): json_loads, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-pythonperf2-x86_64-python-4ed7d1d6acc22807bfb5-3.14.0a0-4ed7d1d |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 13.3 ms                                                      | 13.4 ms: 1.00x slower                                                       |
| python_startup_no_site | 8.94 ms                                                      | 9.00 ms: 1.01x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.01x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-pythonperf2-x86_64-python-4ed7d1d6acc22807bfb5-3.14.0a0-4ed7d1d |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 10.4 ms                                                      | 9.23 ms: 1.13x faster                                                       |
| django_template | 38.9 ms                                                      | 42.8 ms: 1.10x slower                                                       |
| genshi_text     | 26.6 ms                                                      | 29.5 ms: 1.11x slower                                                       |
| genshi_xml      | 57.3 ms                                                      | 66.0 ms: 1.15x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.06x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-pythonperf2-x86_64-python-4ed7d1d6acc22807bfb5-3.14.0a0-4ed7d1d |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy_memo              | 39.5 us                                                      | 27.1 us: 1.46x faster                                                       |
| deepcopy                   | 397 us                                                       | 289 us: 1.37x faster                                                        |
| deepcopy_reduce            | 3.54 us                                                      | 2.92 us: 1.21x faster                                                       |
| scimark_sor                | 126 ms                                                       | 105 ms: 1.20x faster                                                        |
| spectral_norm              | 97.4 ms                                                      | 81.6 ms: 1.19x faster                                                       |
| richards                   | 52.7 ms                                                      | 44.5 ms: 1.18x faster                                                       |
| async_tree_memoization_tg  | 461 ms                                                       | 393 ms: 1.17x faster                                                        |
| async_tree_none            | 372 ms                                                       | 323 ms: 1.15x faster                                                        |
| richards_super             | 59.8 ms                                                      | 52.1 ms: 1.15x faster                                                       |
| tomli_loads                | 2.41 sec                                                     | 2.13 sec: 1.13x faster                                                      |
| mako                       | 10.4 ms                                                      | 9.23 ms: 1.13x faster                                                       |
| async_tree_memoization     | 452 ms                                                       | 404 ms: 1.12x faster                                                        |
| float                      | 81.9 ms                                                      | 74.6 ms: 1.10x faster                                                       |
| pickle_list                | 4.59 us                                                      | 4.18 us: 1.10x faster                                                       |
| pyflate                    | 492 ms                                                       | 449 ms: 1.10x faster                                                        |
| async_tree_none_tg         | 340 ms                                                       | 311 ms: 1.09x faster                                                        |
| pathlib                    | 17.4 ms                                                      | 16.0 ms: 1.09x faster                                                       |
| xml_etree_process          | 60.9 ms                                                      | 55.9 ms: 1.09x faster                                                       |
| pickle_dict                | 32.1 us                                                      | 29.5 us: 1.09x faster                                                       |
| scimark_fft                | 314 ms                                                       | 290 ms: 1.08x faster                                                        |
| nbody                      | 88.0 ms                                                      | 81.8 ms: 1.08x faster                                                       |
| go                         | 160 ms                                                       | 149 ms: 1.07x faster                                                        |
| bpe_tokeniser              | 5.10 sec                                                     | 4.75 sec: 1.07x faster                                                      |
| xml_etree_generate         | 85.3 ms                                                      | 80.1 ms: 1.07x faster                                                       |
| deltablue                  | 3.41 ms                                                      | 3.21 ms: 1.06x faster                                                       |
| crypto_pyaes               | 72.8 ms                                                      | 69.3 ms: 1.05x faster                                                       |
| regex_dna                  | 244 ms                                                       | 233 ms: 1.05x faster                                                        |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 549 ms: 1.05x faster                                                        |
| scimark_sparse_mat_mult    | 4.29 ms                                                      | 4.10 ms: 1.04x faster                                                       |
| async_tree_io              | 847 ms                                                       | 812 ms: 1.04x faster                                                        |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 576 ms: 1.04x faster                                                        |
| telco                      | 8.58 ms                                                      | 8.28 ms: 1.04x faster                                                       |
| sqlite_synth               | 2.79 us                                                      | 2.69 us: 1.04x faster                                                       |
| json_dumps                 | 11.0 ms                                                      | 10.6 ms: 1.03x faster                                                       |
| fannkuch                   | 365 ms                                                       | 358 ms: 1.02x faster                                                        |
| pprint_safe_repr           | 812 ms                                                       | 796 ms: 1.02x faster                                                        |
| regex_v8                   | 26.2 ms                                                      | 25.7 ms: 1.02x faster                                                       |
| json                       | 5.22 ms                                                      | 5.14 ms: 1.02x faster                                                       |
| dulwich_log                | 65.5 ms                                                      | 64.6 ms: 1.01x faster                                                       |
| pickle                     | 10.5 us                                                      | 10.4 us: 1.01x faster                                                       |
| xml_etree_iterparse        | 100 ms                                                       | 98.9 ms: 1.01x faster                                                       |
| xml_etree_parse            | 145 ms                                                       | 143 ms: 1.01x faster                                                        |
| html5lib                   | 71.9 ms                                                      | 71.1 ms: 1.01x faster                                                       |
| pidigits                   | 253 ms                                                       | 250 ms: 1.01x faster                                                        |
| asyncio_tcp                | 380 ms                                                       | 377 ms: 1.01x faster                                                        |
| asyncio_tcp_ssl            | 1.58 sec                                                     | 1.58 sec: 1.00x slower                                                      |
| python_startup             | 13.3 ms                                                      | 13.4 ms: 1.00x slower                                                       |
| python_startup_no_site     | 8.94 ms                                                      | 9.00 ms: 1.01x slower                                                       |
| thrift                     | 877 us                                                       | 885 us: 1.01x slower                                                        |
| logging_format             | 7.07 us                                                      | 7.15 us: 1.01x slower                                                       |
| scimark_lu                 | 97.8 ms                                                      | 99.3 ms: 1.01x slower                                                       |
| meteor_contest             | 128 ms                                                       | 131 ms: 1.02x slower                                                        |
| mdp                        | 2.52 sec                                                     | 2.57 sec: 1.02x slower                                                      |
| tornado_http               | 120 ms                                                       | 122 ms: 1.02x slower                                                        |
| regex_compile              | 144 ms                                                       | 147 ms: 1.02x slower                                                        |
| unpickle_list              | 4.62 us                                                      | 4.72 us: 1.02x slower                                                       |
| pickle_pure_python         | 318 us                                                       | 326 us: 1.02x slower                                                        |
| bench_thread_pool          | 901 us                                                       | 924 us: 1.03x slower                                                        |
| unpickle_pure_python       | 214 us                                                       | 220 us: 1.03x slower                                                        |
| logging_silent             | 97.7 ns                                                      | 100 ns: 1.03x slower                                                        |
| asyncio_websockets         | 382 ms                                                       | 395 ms: 1.03x slower                                                        |
| logging_simple             | 6.40 us                                                      | 6.62 us: 1.04x slower                                                       |
| regex_effbot               | 3.37 ms                                                      | 3.49 ms: 1.04x slower                                                       |
| typing_runtime_protocols   | 174 us                                                       | 181 us: 1.04x slower                                                        |
| comprehensions             | 17.3 us                                                      | 18.2 us: 1.06x slower                                                       |
| sympy_expand               | 505 ms                                                       | 533 ms: 1.06x slower                                                        |
| sympy_str                  | 296 ms                                                       | 313 ms: 1.06x slower                                                        |
| scimark_monte_carlo        | 64.9 ms                                                      | 68.9 ms: 1.06x slower                                                       |
| 2to3                       | 291 ms                                                       | 309 ms: 1.06x slower                                                        |
| chaos                      | 61.7 ms                                                      | 65.7 ms: 1.06x slower                                                       |
| raytrace                   | 289 ms                                                       | 310 ms: 1.07x slower                                                        |
| sqlglot_parse              | 1.38 ms                                                      | 1.49 ms: 1.08x slower                                                       |
| sqlglot_normalize          | 118 ms                                                       | 129 ms: 1.09x slower                                                        |
| sqlglot_transpile          | 1.78 ms                                                      | 1.94 ms: 1.09x slower                                                       |
| async_generators           | 359 ms                                                       | 393 ms: 1.09x slower                                                        |
| sympy_sum                  | 154 ms                                                       | 169 ms: 1.10x slower                                                        |
| django_template            | 38.9 ms                                                      | 42.8 ms: 1.10x slower                                                       |
| sqlglot_optimize           | 59.7 ms                                                      | 65.7 ms: 1.10x slower                                                       |
| hexiom                     | 6.33 ms                                                      | 6.98 ms: 1.10x slower                                                       |
| create_gc_cycles           | 1.76 ms                                                      | 1.94 ms: 1.10x slower                                                       |
| genshi_text                | 26.6 ms                                                      | 29.5 ms: 1.11x slower                                                       |
| docutils                   | 2.81 sec                                                     | 3.15 sec: 1.12x slower                                                      |
| nqueens                    | 88.2 ms                                                      | 99.1 ms: 1.12x slower                                                       |
| generators                 | 33.5 ms                                                      | 37.6 ms: 1.12x slower                                                       |
| bench_mp_pool              | 4.65 ms                                                      | 5.25 ms: 1.13x slower                                                       |
| sympy_integrate            | 23.3 ms                                                      | 26.6 ms: 1.14x slower                                                       |
| genshi_xml                 | 57.3 ms                                                      | 66.0 ms: 1.15x slower                                                       |
| pylint                     | 346 ms                                                       | 410 ms: 1.18x slower                                                        |
| gc_traversal               | 4.11 ms                                                      | 4.87 ms: 1.19x slower                                                       |
| unpack_sequence            | 56.8 ns                                                      | 89.4 ns: 1.57x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.01x faster                                                                |

Benchmark hidden because not significant (7): pycparser, coroutines, json_loads, unpickle, coverage, pprint_pformat, async_tree_io_tg
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 82.32% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.09x