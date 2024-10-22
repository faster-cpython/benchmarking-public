# Results vs. 3.13.0

- fork: python
- ref: 54dd77fb8c880d7655ff
- machine: linux-x86_64
- commit hash: 54dd77f
- commit date: 2024-09-24
- overall geometric mean: 1.00x faster
- HPT reliability: 82.78%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-pythonperf2-x86_64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                       | 312 ms: 1.07x slower                                                        |
| docutils       | 2.81 sec                                                     | 3.18 sec: 1.13x slower                                                      |
| html5lib       | 71.9 ms                                                      | 71.4 ms: 1.01x faster                                                       |
| tornado_http   | 120 ms                                                       | 122 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                        | 1.05x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-pythonperf2-x86_64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 461 ms                                                       | 394 ms: 1.17x faster                                                        |
| async_tree_none            | 372 ms                                                       | 325 ms: 1.14x faster                                                        |
| async_tree_memoization     | 452 ms                                                       | 408 ms: 1.11x faster                                                        |
| async_tree_none_tg         | 340 ms                                                       | 313 ms: 1.08x faster                                                        |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 547 ms: 1.05x faster                                                        |
| async_tree_io              | 847 ms                                                       | 806 ms: 1.05x faster                                                        |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 578 ms: 1.04x faster                                                        |
| async_tree_io_tg           | 819 ms                                                       | 795 ms: 1.03x faster                                                        |
| coroutines                 | 21.6 ms                                                      | 21.3 ms: 1.02x faster                                                       |
| asyncio_tcp_ssl            | 1.58 sec                                                     | 1.58 sec: 1.00x slower                                                      |
| asyncio_websockets         | 382 ms                                                       | 392 ms: 1.02x slower                                                        |
| async_generators           | 359 ms                                                       | 387 ms: 1.08x slower                                                        |
| Geometric mean             | (ref)                                                        | 1.04x faster                                                                |

Benchmark hidden because not significant (1): asyncio_tcp

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-pythonperf2-x86_64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 81.9 ms                                                      | 73.6 ms: 1.11x faster                                                       |
| nbody          | 88.0 ms                                                      | 83.8 ms: 1.05x faster                                                       |
| pidigits       | 253 ms                                                       | 250 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                        | 1.06x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-pythonperf2-x86_64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 244 ms                                                       | 234 ms: 1.04x faster                                                        |
| regex_v8       | 26.2 ms                                                      | 25.8 ms: 1.01x faster                                                       |
| regex_compile  | 144 ms                                                       | 148 ms: 1.03x slower                                                        |
| regex_effbot   | 3.37 ms                                                      | 3.50 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                        | 1.00x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-pythonperf2-x86_64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.41 sec                                                     | 2.11 sec: 1.14x faster                                                      |
| xml_etree_process    | 60.9 ms                                                      | 56.4 ms: 1.08x faster                                                       |
| xml_etree_generate   | 85.3 ms                                                      | 80.2 ms: 1.06x faster                                                       |
| json_dumps           | 11.0 ms                                                      | 10.6 ms: 1.03x faster                                                       |
| xml_etree_iterparse  | 100 ms                                                       | 98.2 ms: 1.02x faster                                                       |
| unpickle             | 15.1 us                                                      | 14.9 us: 1.02x faster                                                       |
| pickle_list          | 4.59 us                                                      | 4.54 us: 1.01x faster                                                       |
| xml_etree_parse      | 145 ms                                                       | 143 ms: 1.01x faster                                                        |
| pickle_dict          | 32.1 us                                                      | 32.2 us: 1.00x slower                                                       |
| json_loads           | 24.0 us                                                      | 24.2 us: 1.01x slower                                                       |
| pickle               | 10.5 us                                                      | 10.6 us: 1.01x slower                                                       |
| unpickle_pure_python | 214 us                                                       | 216 us: 1.01x slower                                                        |
| pickle_pure_python   | 318 us                                                       | 325 us: 1.02x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.02x faster                                                                |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-pythonperf2-x86_64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 8.94 ms                                                      | 9.00 ms: 1.01x slower                                                       |
| python_startup         | 13.3 ms                                                      | 13.4 ms: 1.01x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.01x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-pythonperf2-x86_64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 10.4 ms                                                      | 9.16 ms: 1.14x faster                                                       |
| django_template | 38.9 ms                                                      | 42.4 ms: 1.09x slower                                                       |
| genshi_text     | 26.6 ms                                                      | 29.5 ms: 1.11x slower                                                       |
| genshi_xml      | 57.3 ms                                                      | 68.6 ms: 1.20x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.06x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-pythonperf2-x86_64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy_memo              | 39.5 us                                                      | 26.9 us: 1.47x faster                                                       |
| deepcopy                   | 397 us                                                       | 298 us: 1.33x faster                                                        |
| deepcopy_reduce            | 3.54 us                                                      | 2.92 us: 1.21x faster                                                       |
| scimark_sor                | 126 ms                                                       | 104 ms: 1.21x faster                                                        |
| spectral_norm              | 97.4 ms                                                      | 81.4 ms: 1.20x faster                                                       |
| richards                   | 52.7 ms                                                      | 44.6 ms: 1.18x faster                                                       |
| async_tree_memoization_tg  | 461 ms                                                       | 394 ms: 1.17x faster                                                        |
| richards_super             | 59.8 ms                                                      | 51.6 ms: 1.16x faster                                                       |
| async_tree_none            | 372 ms                                                       | 325 ms: 1.14x faster                                                        |
| tomli_loads                | 2.41 sec                                                     | 2.11 sec: 1.14x faster                                                      |
| mako                       | 10.4 ms                                                      | 9.16 ms: 1.14x faster                                                       |
| float                      | 81.9 ms                                                      | 73.6 ms: 1.11x faster                                                       |
| async_tree_memoization     | 452 ms                                                       | 408 ms: 1.11x faster                                                        |
| pyflate                    | 492 ms                                                       | 445 ms: 1.10x faster                                                        |
| pathlib                    | 17.4 ms                                                      | 15.9 ms: 1.10x faster                                                       |
| scimark_fft                | 314 ms                                                       | 287 ms: 1.09x faster                                                        |
| async_tree_none_tg         | 340 ms                                                       | 313 ms: 1.08x faster                                                        |
| go                         | 160 ms                                                       | 148 ms: 1.08x faster                                                        |
| xml_etree_process          | 60.9 ms                                                      | 56.4 ms: 1.08x faster                                                       |
| bpe_tokeniser              | 5.10 sec                                                     | 4.73 sec: 1.08x faster                                                      |
| deltablue                  | 3.41 ms                                                      | 3.17 ms: 1.07x faster                                                       |
| scimark_sparse_mat_mult    | 4.29 ms                                                      | 4.01 ms: 1.07x faster                                                       |
| xml_etree_generate         | 85.3 ms                                                      | 80.2 ms: 1.06x faster                                                       |
| nbody                      | 88.0 ms                                                      | 83.8 ms: 1.05x faster                                                       |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 547 ms: 1.05x faster                                                        |
| async_tree_io              | 847 ms                                                       | 806 ms: 1.05x faster                                                        |
| sqlite_synth               | 2.79 us                                                      | 2.66 us: 1.05x faster                                                       |
| telco                      | 8.58 ms                                                      | 8.20 ms: 1.05x faster                                                       |
| regex_dna                  | 244 ms                                                       | 234 ms: 1.04x faster                                                        |
| crypto_pyaes               | 72.8 ms                                                      | 69.9 ms: 1.04x faster                                                       |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 578 ms: 1.04x faster                                                        |
| json_dumps                 | 11.0 ms                                                      | 10.6 ms: 1.03x faster                                                       |
| async_tree_io_tg           | 819 ms                                                       | 795 ms: 1.03x faster                                                        |
| pprint_safe_repr           | 812 ms                                                       | 792 ms: 1.02x faster                                                        |
| dulwich_log                | 65.5 ms                                                      | 64.3 ms: 1.02x faster                                                       |
| xml_etree_iterparse        | 100 ms                                                       | 98.2 ms: 1.02x faster                                                       |
| unpickle                   | 15.1 us                                                      | 14.9 us: 1.02x faster                                                       |
| coverage                   | 81.1 ms                                                      | 79.8 ms: 1.02x faster                                                       |
| coroutines                 | 21.6 ms                                                      | 21.3 ms: 1.02x faster                                                       |
| regex_v8                   | 26.2 ms                                                      | 25.8 ms: 1.01x faster                                                       |
| fannkuch                   | 365 ms                                                       | 360 ms: 1.01x faster                                                        |
| pidigits                   | 253 ms                                                       | 250 ms: 1.01x faster                                                        |
| pickle_list                | 4.59 us                                                      | 4.54 us: 1.01x faster                                                       |
| xml_etree_parse            | 145 ms                                                       | 143 ms: 1.01x faster                                                        |
| html5lib                   | 71.9 ms                                                      | 71.4 ms: 1.01x faster                                                       |
| asyncio_tcp_ssl            | 1.58 sec                                                     | 1.58 sec: 1.00x slower                                                      |
| pickle_dict                | 32.1 us                                                      | 32.2 us: 1.00x slower                                                       |
| meteor_contest             | 128 ms                                                       | 129 ms: 1.00x slower                                                        |
| python_startup_no_site     | 8.94 ms                                                      | 9.00 ms: 1.01x slower                                                       |
| json_loads                 | 24.0 us                                                      | 24.2 us: 1.01x slower                                                       |
| python_startup             | 13.3 ms                                                      | 13.4 ms: 1.01x slower                                                       |
| pickle                     | 10.5 us                                                      | 10.6 us: 1.01x slower                                                       |
| unpickle_pure_python       | 214 us                                                       | 216 us: 1.01x slower                                                        |
| json                       | 5.22 ms                                                      | 5.33 ms: 1.02x slower                                                       |
| pickle_pure_python         | 318 us                                                       | 325 us: 1.02x slower                                                        |
| tornado_http               | 120 ms                                                       | 122 ms: 1.02x slower                                                        |
| asyncio_websockets         | 382 ms                                                       | 392 ms: 1.02x slower                                                        |
| logging_format             | 7.07 us                                                      | 7.26 us: 1.03x slower                                                       |
| pycparser                  | 1.26 sec                                                     | 1.29 sec: 1.03x slower                                                      |
| bench_thread_pool          | 901 us                                                       | 927 us: 1.03x slower                                                        |
| mdp                        | 2.52 sec                                                     | 2.60 sec: 1.03x slower                                                      |
| regex_compile              | 144 ms                                                       | 148 ms: 1.03x slower                                                        |
| regex_effbot               | 3.37 ms                                                      | 3.50 ms: 1.04x slower                                                       |
| logging_simple             | 6.40 us                                                      | 6.67 us: 1.04x slower                                                       |
| thrift                     | 877 us                                                       | 915 us: 1.04x slower                                                        |
| typing_runtime_protocols   | 174 us                                                       | 183 us: 1.05x slower                                                        |
| comprehensions             | 17.3 us                                                      | 18.2 us: 1.05x slower                                                       |
| scimark_monte_carlo        | 64.9 ms                                                      | 68.5 ms: 1.05x slower                                                       |
| sympy_str                  | 296 ms                                                       | 313 ms: 1.06x slower                                                        |
| sympy_expand               | 505 ms                                                       | 537 ms: 1.06x slower                                                        |
| logging_silent             | 97.7 ns                                                      | 104 ns: 1.06x slower                                                        |
| 2to3                       | 291 ms                                                       | 312 ms: 1.07x slower                                                        |
| gc_traversal               | 4.11 ms                                                      | 4.42 ms: 1.07x slower                                                       |
| sqlglot_parse              | 1.38 ms                                                      | 1.49 ms: 1.08x slower                                                       |
| async_generators           | 359 ms                                                       | 387 ms: 1.08x slower                                                        |
| create_gc_cycles           | 1.76 ms                                                      | 1.91 ms: 1.08x slower                                                       |
| sqlglot_normalize          | 118 ms                                                       | 128 ms: 1.08x slower                                                        |
| chaos                      | 61.7 ms                                                      | 66.9 ms: 1.09x slower                                                       |
| django_template            | 38.9 ms                                                      | 42.4 ms: 1.09x slower                                                       |
| bench_mp_pool              | 4.65 ms                                                      | 5.08 ms: 1.09x slower                                                       |
| sqlglot_transpile          | 1.78 ms                                                      | 1.95 ms: 1.09x slower                                                       |
| hexiom                     | 6.33 ms                                                      | 6.95 ms: 1.10x slower                                                       |
| sqlglot_optimize           | 59.7 ms                                                      | 65.6 ms: 1.10x slower                                                       |
| sympy_sum                  | 154 ms                                                       | 170 ms: 1.10x slower                                                        |
| genshi_text                | 26.6 ms                                                      | 29.5 ms: 1.11x slower                                                       |
| nqueens                    | 88.2 ms                                                      | 98.2 ms: 1.11x slower                                                       |
| generators                 | 33.5 ms                                                      | 37.3 ms: 1.11x slower                                                       |
| docutils                   | 2.81 sec                                                     | 3.18 sec: 1.13x slower                                                      |
| sympy_integrate            | 23.3 ms                                                      | 26.5 ms: 1.14x slower                                                       |
| raytrace                   | 289 ms                                                       | 332 ms: 1.15x slower                                                        |
| pylint                     | 346 ms                                                       | 411 ms: 1.19x slower                                                        |
| genshi_xml                 | 57.3 ms                                                      | 68.6 ms: 1.20x slower                                                       |
| unpack_sequence            | 56.8 ns                                                      | 87.7 ns: 1.54x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.00x faster                                                                |

Benchmark hidden because not significant (4): asyncio_tcp, pprint_pformat, unpickle_list, scimark_lu
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 82.78% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.09x